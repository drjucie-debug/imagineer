#!/bin/sh
# Injects the project's idea memory into the session. Silent when the project has none.
dir="${CLAUDE_PROJECT_DIR:-$PWD}/.imagineer"
[ -f "$dir/ideas.md" ] || exit 0

latest=$(ls -t "$dir"/briefs/*.md 2>/dev/null | head -1)

awk -F'|' -v today="$(date +%F)" -v latest="${latest#"${CLAUDE_PROJECT_DIR:-$PWD}/"}" '
  function trim(s) { gsub(/^[ \t]+|[ \t]+$/, "", s); return s }
  /^\|/ {
    idea = trim($3); status = trim($6)
    if (idea == "" || idea == "Ideia" || idea ~ /^-+$/) next
    total++; by[status]++
    if (status != "arquivada") active[++n] = "- " idea " (" trim($5) ", " status ")"
    due = trim($8)
    if (status == "testando" && due != "" && due < today) overdue[++m] = "- " idea " (teste até " due ")"
  }
  END {
    if (!total) exit
    sep = ""; for (s in by) { counts = counts sep by[s] " " s; sep = ", " }
    printf "[imagineer] Este projeto tem memória de Imagineering em .imagineer/: %d ideias (%s).\n", total, counts
    if (latest != "") print "Último brief: " latest
    if (n) print "Ideias ativas mais recentes:"
    for (i = n; i > 0 && i > n - 5; i--) print active[i]
    if (m) { print "Experimentos vencidos — deu certo? Registre com /imagineer:ideas:"; for (i = 1; i <= m; i++) print overdue[i] }
    print "Use como ponto de partida quando o assunto for ideias ou inovação, e não repita ideias já registradas. Status e resultados: /imagineer:ideas."
  }
' "$dir/ideas.md"
