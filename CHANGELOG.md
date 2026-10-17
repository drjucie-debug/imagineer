# Changelog

## 0.7.0 — 2026-10-17
- **Formas de entrega:** o brief pode virar página publicada (capa = cartão-postal, conceitos como cards); `/board` publica o quadro de ideias como página interativa com votos e movimentos entre horizontes; `/pitch` transforma um conceito em roteiro de 7 quadros (máx. 20 palavras por quadro); o esboço do cartão-postal pode virar imagem gerada. Tudo condicional às ferramentas da sessão, com fallback em markdown.

## 0.6.0 — 2026-10-17
- **Cartão-postal:** o brief abre com a história em 1 frase, a cena mais forte e um prompt de esboço à la Herb Ryman; no modo criação, cada ficha ganha "silhueta em 3 traços".
- **Etiqueta `[memória]`:** fato sem fonte lida não entra no sumário nem no cartão-postal.
- **Entrega em duas camadas:** a conversa mostra o essencial; o brief inteiro vai para `.imagineer/briefs/`.
- **Mapa do parque:** `/imagine` sem argumento mostra as 3 portas; todo brief fecha com um "próximo brinquedo".
- **Kit de segunda-feira:** o experimento H1 sai com a peça pronta, não só o plano.
- **Cobrança:** coluna `Teste até` no ideas.md; o hook avisa experimento vencido.
- **Fantasma 1000:** todo brief termina com uma pergunta em aberto (status `vaga`) que semeia o próximo /spark.
- **Evals comportamentais:** 3 casos em `evals/` para `claude plugin eval` (criação entrega fichas; história primeiro; "Sim, se…").

## 0.5.1 — 2026-10-17
- Empacotamento para GitHub: exemplos reais (estratégia e criação), CHANGELOG, CI, .gitignore, aviso de marca.

## 0.5.0 — 2026-10-17
- **Motor refundado no método real da WDI:** a história primeiro (1 frase com coração), teste do coração na shortlist, engenharia "Sim, se…", Dez Mandamentos de Mickey (Sklar) no checklist, Hench e as 7 fases oficiais — com fontes em `references/principios.md`.

## 0.4.x — 2026-10-16
- **Modo criação:** pedido de coisas (criaturas, personagens, produtos) entrega as coisas com ficha; regra "nunca troque o entregável"; template próprio.
- `--quick` na conversa principal; só o veto continua em subagente (≈1/5 do custo).

## 0.3.x — 2026-10-16
- Shortlist com nota, veto pós-plussing, checklist de qualidade, fontes etiquetadas por tipo, handoffs explícitos entre agentes.
- `/ideas` (status e resultado de experimentos), `/spark` (1 conceito rápido), LICENSE, skill autossuficiente, agentes com namespace.

## 0.2.0 — 2026-10-16
- Memória por projeto (`.imagineer/ideas.md` + `briefs/`) e hook `SessionStart` que a resume (mudo sem `.imagineer/`).

## 0.1.x — 2026-10-16
- Esboço inicial; renomeado para `imagineer` (prefixo `claude-` é reservado); marketplace local e instalação funcionando.
