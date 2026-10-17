---
name: imagineering-method
description: Pensa à frente de qualquer projeto com o método dos Imagineers — reenquadra o desafio, pesquisa sinais do futuro, gera ideias Blue Sky, dá história e jornada aos melhores conceitos, aplica plussing e fecha com viabilidade em horizontes H1/H2/H3. Use quando o usuário pedir novas formas, ideias inovadoras, o futuro de um setor, como reinventar um produto/serviço, ou disser "pense como um Imagineer".
---

# Método Imagineering

Este método transforma um pedido vago ("pesquise novas formas de vender carros") em **conceitos de experiência com caminho de execução**.

## Quando ativar

- "Pesquise novas formas de…", "como reinventar…", "qual o futuro de…", "ideias inovadoras para…", "pense fora da caixa", "pense como a Disney".
- Qualquer projeto em que o usuário queira ir além da melhoria incremental.

## O ciclo (9 fases)

| # | Fase | Papel | Saída |
|---|---|---|---|
| 1 | Reenquadrar | Imagineer-chefe | Pergunta "Como poderíamos…?", convidado, momento da verdade |
| 2 | Varrer o futuro | futurist-scout | Fatos, sinais fracos, analogias, fontes |
| 3 | Blue Sky | blue-sky-dreamer | 20+ ideias com 8 lentes |
| 4 | Shortlist | Imagineer-chefe | Notas 1–5 (horizontes.md), 3–5 escolhidas com motivo |
| 5 | História + Jornada | story-architect + guest-advocate | Conceitos com weenie e momento mágico |
| 6 | Plussing | devils-plusser | 3 rodadas por conceito |
| 7 | Veto do convidado | guest-advocate | Plus manipuladores vetados e corrigidos |
| 8 | Engenharia | show-engineer | Viabilidade, H1/H2/H3, embrião H1, MVP |
| 9 | Entrega | Imagineer-chefe | Brief no template, conferido no checklist |

**No Claude Code:** delegue cada papel ao subagente de mesmo nome. Na fase 5 os dois papéis rodam em paralelo. Os tipos levam o prefixo do plugin (`imagineer:futurist-scout`…). Subagentes não veem a conversa nem a pasta da skill — passe no prompt:
- **scout:** pergunta real, convidado, suposições, nº de buscas;
- **dreamer:** pergunta real, convidado, saída do scout, ideias já registradas;
- **story + guest:** shortlist (nome + cena), convidado, momento da verdade, sinais ligados;
- **plusser:** conceitos + jornada e dores;
- **guest (veto):** versões plussed + `references/principios.md`;
- **engineer:** conceitos corrigidos + `references/horizontes.md`, país e setor.
**No app Claude (sem subagentes):** interprete cada papel em sequência, marcando claramente a fase. Use pesquisa web na fase 2.

## Princípios inegociáveis

Leia `references/principios.md`. Resumo:

1. **Sonhar e filtrar são fases separadas.** Nunca avalie viabilidade durante o Blue Sky.
2. **História antes de produto.** Se não cabe numa cena, não está pronto.
3. **O convidado é o herói.** Projete a partir dos olhos de quem vive a experiência.
4. **Weenie.** Todo conceito tem algo que puxa a pessoa de longe.
5. **Plussing.** Nenhuma ideia está terminada.
6. **Atenção ao detalhe.** O detalhe escondido é o que vira lenda.
7. **Inspiração de fora.** Pelo menos metade das referências vem de outros setores.
8. **Ousadia com caminho.** Toda ideia H3 tem uma versão H1 testável.
9. **Ética do encantamento.** Encantar, nunca manipular. O `guest-advocate` tem poder de veto.

## Técnicas

Ver `references/tecnicas.md` — inversão, transplante, exagero 10×, remoção, futuro pleno, ritual, comunidade, criança de 8 anos, "Como poderíamos…?", storyboard de 6 quadros.

## Horizontes

Ver `references/horizontes.md` — critérios para H1, H2, H3 e a matriz Encantamento × Viabilidade.

## Formato de entrega

Use `references/brief-template.md`. Mantenha:
- Sumário executivo de 5 linhas no topo.
- Cada conceito com nome, logline, momento mágico e horizonte.
- Fontes no fim.
- Fechamento com experimentos de 2 semanas.
- Antes de entregar, confira `references/checklist.md`.

## Memória do projeto

Ver `references/ideas-format.md`. Leia `.imagineer/ideas.md` antes de gerar ideias e registre os conceitos ao final de cada ciclo.

## Calibragem

- Pedido curto ou flag `--quick`: fase 2 com 5 buscas, 10 ideias, 3 conceitos, 1 rodada de plussing.
- Pedido amplo ("o futuro do varejo"): faça a fase 2 completa e 5 conceitos.
- Se o usuário tem um projeto em andamento (CLAUDE.md, README, arquivos), leia antes e ancore os conceitos nele.
