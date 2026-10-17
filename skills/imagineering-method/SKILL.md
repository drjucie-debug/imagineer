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

Compacta as 7 fases oficiais da WDI (Blue Sky → Conceito → Viabilidade → Design → Produção → Instalação → Abertura) numa conversa:

| # | Fase | Papel | Saída |
|---|---|---|---|
| 1 | A história primeiro | Imagineer-chefe | História em 1 frase com coração; convidado-herói; lugar; momento da verdade |
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

## Dois modos — decida na fase 1

**Regra de ouro: nunca troque o entregável.** Reenquadrar amplia o pedido, não o substitui. Se pediram coisas, entregue as coisas; a "pergunta real" entra como lente para elas ficarem melhores.

| Modo | Sinal no pedido | Entregável |
|---|---|---|
| **Modo criação** | pede *coisas*: criaturas, personagens, produtos, nomes, histórias, cardápio, mundos ("imagine novos pokémons", "crie 5 sabores") | as próprias criações, com ficha — `references/creation-template.md` |
| **Modo estratégia** | pede *como*: vender, reinventar, crescer, o futuro de um setor | conceitos de experiência com caminho — `references/brief-template.md` |

Ambíguo? Pergunte numa linha. Os dois juntos ("novos sabores e como vendê-los")? Criação primeiro; estratégia vira a seção final.

**No modo criação, as fases mudam de função:**
- Reenquadrar: o que torna uma criação desse tipo inesquecível (critérios de bom design), para quem, e as regras do universo (cânone, tipos, estilo).
- Pesquisa: o que já existe (para não repetir), lacunas do universo, inspiração de fora (biologia, folclore, arquitetura, culinária…).
- Blue Sky: cada ideia é **a criação em si** — nome + o que é numa linha.
- Shortlist: Encantamento, Originalidade (≠ existentes), Coerência (respeita as regras do universo), Potencial (história, evolução, variações).
- História: uma **ficha** por criação (aparência, comportamento, origem, momento em que alguém a encontra).
- Plussing: no design da criação.
- Veto: ofensa, estereótipo cultural, adequação ao público (ex.: criança), semelhança com algo existente.
- Engenharia: vira **"Como tornar real"** curto — protótipo (esboço, mock, receita), e direitos/IP quando o universo é de terceiros (criação de fã ≠ uso comercial).

## O motor: pensar como um Imagineer

Três leis regem todas as fases (detalhe e fontes em `references/principios.md`):

1. **A história primeiro.** A fase 1 não produz "pergunta de negócio": produz uma história em UMA frase com coração — herói (o convidado), desejo, transformação, lugar. Pesquisa, ideias e engenharia servem a ela, nunca o contrário.
2. **O convidado é a câmera.** Tudo se escreve como cena desenhável, em primeira pessoa, no presente. Se não dá para desenhar ou maquetar, ainda está abstrato.
3. **"Sim, se…".** Viabilidade nunca responde "não dá"; responde "sim, se [condição]". A condição vira requisito, define o horizonte ou vira o embrião H1.

Regras de sala: sonhar e filtrar nunca na mesma fase; metade das referências vem de fora do setor; toda ideia H3 tem embrião H1; encantar, nunca manipular (o `guest-advocate` veta). O padrão de qualidade são os **Dez Mandamentos de Mickey** (Sklar) — o checklist da entrega deriva deles.

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

- Pedido curto ou flag `--quick`: tudo na conversa principal, só o veto num subagente `guest-advocate`; fase 2 com 5 buscas, 10 ideias, 3 conceitos, 1 rodada de plussing.
- Pedido amplo ("o futuro do varejo"): faça a fase 2 completa e 5 conceitos.
- Se o usuário tem um projeto em andamento (CLAUDE.md, README, arquivos), leia antes e ancore os conceitos nele.
