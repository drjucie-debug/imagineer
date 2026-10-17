#!/usr/bin/env python3
"""Structural check for the plugin. Run: python3 tests/check_plugin.py"""
import json
import re
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
    print("ok")


if __name__ == "__main__":
    main()
