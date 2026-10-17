#!/usr/bin/env python3
"""Structural check for the plugin. Run: python3 tests/check_plugin.py"""
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/imagineering-method"
COMMANDS = list(ROOT.glob("commands/*.md"))
AGENTS = list(ROOT.glob("agents/*.md"))


def frontmatter(path):
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(), re.S)
    assert m, f"{path.name}: missing frontmatter"
    return {k.strip(): v.strip() for k, v in
            (l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)}


def main():
    manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    assert market.get("owner", {}).get("name"), "marketplace: owner.name required"
    entry = next(p for p in market["plugins"] if p["name"] == manifest["name"])
    assert entry["source"] == "./", "marketplace: plugin source must be ./"

    # Config nothing reads, and paths that break once installed.
    for f in [*COMMANDS, *AGENTS, *SKILL.rglob("*.md"), ROOT / "README.md"]:
        text = f.read_text()
        assert "IMAGINEER_" not in text, f"{f.relative_to(ROOT)}: dead env var"
        assert "templates/" not in text, f"{f.relative_to(ROOT)}: template outside skill"

    # Bare `references/` paths only resolve inside the skill.
    for f in [*COMMANDS, *AGENTS]:
        assert "`references/" not in f.read_text(), \
            f"{f.relative_to(ROOT)}: bare references/ path outside skill"
    for ref in re.findall(r"references/[\w-]+\.md", (SKILL / "SKILL.md").read_text()):
        assert (SKILL / ref).exists(), f"SKILL.md cites missing {ref}"

    agents = {frontmatter(a)["name"] for a in AGENTS}
    for a in AGENTS:
        assert {"name", "description", "tools"} <= frontmatter(a).keys(), a.name
    known = agents | {c.stem for c in COMMANDS} | {"imagineering-method"}
    for c in COMMANDS:
        assert "description" in frontmatter(c), c.name
        for cited in re.findall(r"`([a-z]+(?:-[a-z]+)+)`", c.read_text()):
            assert cited in known, f"{c.name} cites unknown `{cited}`"
    assert frontmatter(SKILL / "SKILL.md")["name"] == "imagineering-method"
    assert (SKILL / "references/ideas-format.md").exists(), "ideas.md format undocumented"

    # Method guarantees: scored shortlist, late veto, quality gate, source tags, handoffs.
    template = (SKILL / "references/brief-template.md").read_text()
    for field in ("Embrião H1", "Shortlist", "Veto do convidado"):
        assert field in template, f"brief template missing {field}"
    assert (SKILL / "references/checklist.md").exists(), "quality checklist missing"
    assert "references/checklist.md" in (SKILL / "SKILL.md").read_text()
    imagine = (ROOT / "commands/imagine.md").read_text()
    assert imagine.index("Shortlist") < imagine.index("story-architect"), "shortlist must precede story"
    assert imagine.rindex("guest-advocate") > imagine.index("devils-plusser"), "veto must follow plussing"
    assert imagine.count("**Passe:**") >= 5, "each delegated phase must say what to hand over"
    assert "[fornecedor]" in (ROOT / "agents/futurist-scout.md").read_text(), "source tags missing"
    assert "Detran" not in (ROOT / "agents/show-engineer.md").read_text(), "car example leaked"

    # Installed agents are namespaced; the skill must stand alone (Claude app upload).
    for c in COMMANDS:
        if "subagente" in c.read_text():
            assert "imagineer:" in c.read_text(), f"{c.name}: agent type must be imagineer:<name>"
    assert "commands/" not in (SKILL / "SKILL.md").read_text(), "skill must not depend on commands/"
    assert (ROOT / "commands/ideas.md").exists(), "no way to update idea status/results"
    assert "Resultado" in (SKILL / "references/ideas-format.md").read_text()
    assert (ROOT / "LICENSE").exists(), "plugin.json says MIT but LICENSE missing"
    assert not (ROOT / "templates").exists(), "stale templates/ dir"

    # /spark: one concept, fast, no subagents — but never skips the veto or the memory.
    spark = ROOT / "commands/spark.md"
    assert spark.exists(), "/spark missing"
    fm, body = frontmatter(spark), spark.read_text()
    assert "Agent" not in fm.get("allowed-tools", ""), "/spark must run without subagents"
    for must in ("Veto", "ideas.md", "MVP", "--quick"):
        assert must in body, f"/spark missing {must}"
    assert "Como tornar real:**" in body, "/spark needs a creation-mode output format"

    # --quick: everything in the main thread except the independent veto (1 subagent, not 6).
    quick = next(l for l in imagine.splitlines() if l.startswith("- `--quick`"))
    assert "conversa principal" in quick and "guest-advocate" in quick, quick

    # Real-WDI engine: story first, heart test, "Yes, if", Ten Commandments.
    principios = (SKILL / "references/principios.md").read_text()
    for must in ("Dez Mandamentos", "Sim, se", "Encantar, nunca manipular", "weenie"):
        assert must in principios, f"principios.md missing {must}"
    assert "Teste do coração" in (SKILL / "references/tecnicas.md").read_text()
    skill_text = (SKILL / "SKILL.md").read_text()
    assert "A história primeiro" in skill_text and "Sim, se" in skill_text
    assert "A história primeiro" in imagine, "phase 1 must produce a story, not a business question"
    assert "teste do coração" in imagine, "shortlist needs the heart-test gate"
    assert "Sim, se" in (ROOT / "agents/show-engineer.md").read_text(), "engineer must answer 'Sim, se'"
    assert "Dez Mandamentos" in (SKILL / "references/checklist.md").read_text()

    # Creation requests ("imagine novos pokémons") must get the things themselves, not a strategy.
    assert (SKILL / "references/creation-template.md").exists(), "no template for creation mode"
    for f in [SKILL / "SKILL.md", ROOT / "commands/imagine.md", spark,
              ROOT / "agents/blue-sky-dreamer.md", ROOT / "agents/story-architect.md"]:
        assert "Modo criação" in f.read_text(), f"{f.name}: creation mode missing"
    assert "nunca troque o entregável" in (SKILL / "SKILL.md").read_text().lower()
    assert "Entregável" in (SKILL / "references/checklist.md").read_text()
    check_session_hook()
    print("ok")


def check_session_hook():
    hooks = json.loads((ROOT / "hooks/hooks.json").read_text())["hooks"]
    cmd = hooks["SessionStart"][0]["hooks"][0]["command"]
    script = ROOT / "hooks/session-start.sh"
    assert cmd == "\"${CLAUDE_PLUGIN_ROOT}/hooks/session-start.sh\"", cmd
    assert os.access(script, os.X_OK), "session-start.sh not executable"

    def run(project):
        env = {**os.environ, "CLAUDE_PROJECT_DIR": str(project)}
        r = subprocess.run([str(script)], env=env, capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        return r.stdout

    with tempfile.TemporaryDirectory() as d:
        project = Path(d)
        assert run(project) == "", "hook must be silent without .imagineer/"
        (project / ".imagineer/briefs").mkdir(parents=True)
        (project / ".imagineer/briefs/vender-online-2026-10-16.md").write_text("x")
        (project / ".imagineer/ideas.md").write_text(
            "# Ideias\n\n| Data | Ideia | Brief | Horizonte | Status |\n|---|---|---|---|---|\n"
            "| 2026-10-16 | Vendedor em 30s | briefs/vender-online-2026-10-16.md | H1 | testando |\n"
            "| 2026-10-16 | Vaquinha | briefs/vender-online-2026-10-16.md | H1 | sonho |\n"
            "| 2026-10-01 | Loja sem site | briefs/x.md | H3 | arquivada |\n")
        out = run(project)
        assert "3 ideias" in out, out
        assert "Vendedor em 30s" in out and "Vaquinha" in out, out
        assert "Loja sem site" not in out, "archived ideas must not be listed"
        assert "vender-online-2026-10-16.md" in out, "latest brief missing"


if __name__ == "__main__":
    main()
