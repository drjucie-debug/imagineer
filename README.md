# Claude Imagineer

> "É meio divertido fazer o impossível." — princípio que guia o plugin

**Claude Imagineer** é um plugin para Claude e Claude Code que pensa *à frente* de qualquer projeto. Em vez de responder "como fazer X um pouco melhor", ele responde "como seria X se fosse projetado hoje do zero, como uma experiência inesquecível — e qual o caminho de engenharia para chegar lá".

O método se inspira na forma de trabalhar dos Imagineers da Disney: misturar sonhadores e engenheiros na mesma sala, começar pela história, projetar a partir do olhar do convidado e nunca considerar uma ideia terminada ("plussing").

---

## Exemplo de uso

```
/imagineer:imagine novas formas de vender carros
```

O plugin entrega um **Imagineering Brief** com:

1. **A história primeiro** — uma frase com coração (herói, desejo, transformação, lugar) que comanda o ciclo inteiro.
2. **Varredura do futuro** — pesquisa web com fontes etiquetadas por tipo ([primária], [fornecedor]…).
3. **Blue Sky** — 20+ ideias sem restrição, cada uma como cena desenhável.
4. **Shortlist** — teste do coração na porta + notas; o filtro não mata a ousadia.
5. **História e jornada** — conceitos com weenie, momento mágico, personas e dores.
6. **Plussing** — "e se fosse ainda melhor?".
7. **Veto do convidado** — depois do plussing: urgência falsa, exposição e dark patterns caem, sempre com correção.
8. **Engenharia "Sim, se…"** — H1/H2/H3, embrião H1 e MVP de 2 semanas; nenhum obstáculo volta como "não dá".
9. **Entrega** — brief conferido no checklist dos Dez Mandamentos + um experimento por conceito.

Pedido de *coisas* ("imagine novos pokémons", "crie 5 sabores") entra no **modo criação**: o plugin entrega as criações em si, com ficha — nunca uma estratégia sobre elas.

Para **um** conceito rápido (≈1 min, sem subagentes nem pesquisa): `/imagineer:spark <desafio>` — reenquadra, 8 ideias, escolhe 1, cena, plus, veto e MVP de 2 semanas.

Exemplos reais: [`examples/moda-online.md`](examples/moda-online.md) (modo estratégia, 9 fases com subagentes) e [`examples/novos-pokemons.md`](examples/novos-pokemons.md) (modo criação, 3 criaturas com ficha).

---

## Estrutura

```
imagineer/
├── .claude-plugin/
│   ├── plugin.json                   # manifesto
│   └── marketplace.json              # marketplace de um plugin só
├── commands/                         # comandos de barra
│   ├── imagine.md                    # /imagine  — ciclo completo
│   ├── spark.md                      # /spark    — 1 conceito rápido, sem subagentes
│   ├── blue-sky.md                   # /blue-sky — só a explosão de ideias
│   ├── plus.md                       # /plus     — melhora uma ideia existente
│   ├── story.md                      # /story    — transforma ideia em narrativa
│   ├── guest-journey.md              # /guest-journey — mapa da experiência
│   ├── future-scan.md                # /future-scan — sinais e tendências
│   ├── ideas.md                      # /ideas — status e resultados das ideias
│   ├── board.md                      # /board — quadro de ideias como página interativa
│   └── pitch.md                      # /pitch — roteiro de 7 quadros para vender um conceito
├── hooks/
│   ├── hooks.json                    # SessionStart
│   └── session-start.sh              # resume .imagineer/ideas.md na sessão
├── agents/                           # a "sala de Imagineering"
│   ├── futurist-scout.md             # pesquisa sinais do futuro
│   ├── blue-sky-dreamer.md           # ideação sem limites
│   ├── story-architect.md            # narrativa e "weenie"
│   ├── guest-advocate.md             # voz do cliente/usuário
│   ├── show-engineer.md              # viabilidade técnica e de negócio
│   └── devils-plusser.md             # crítico construtivo que eleva a ideia
├── skills/imagineering-method/       # o método em si
│   ├── SKILL.md
│   └── references/
│       ├── principios.md             # os princípios de Imagineering
│       ├── tecnicas.md               # técnicas de ideação e plussing
│       ├── horizontes.md             # modelo H1/H2/H3 e critérios
│       ├── brief-template.md         # formato do entregável
│       ├── ideas-format.md           # memória .imagineer/ do projeto
│       ├── checklist.md              # conferência antes de entregar
│       └── creation-template.md      # entregável do modo criação
├── examples/                         # moda-online.md (estratégia), novos-pokemons.md (criação)
├── tests/check_plugin.py             # verificação estrutural (roda no CI)
└── CHANGELOG.md
```

## Como o ciclo roda

```
Pedido do usuário
      │
      ▼
[1] A história primeiro ─► [2] futurist-scout (pesquisa)
                          │
                          ▼
                    [3] blue-sky-dreamer (20+ ideias)
                          │
                          ▼
                    [4] Shortlist com nota (3–5)
                          │
                          ▼
           [5] story-architect + guest-advocate
                          │
                          ▼
                [6] devils-plusser (plussing)
                          │
                          ▼
                [7] guest-advocate (veto pós-plussing)
                          │
                          ▼
                [8] show-engineer (H1/H2/H3 + embrião H1)
                          │
                          ▼
           [9] Brief conferido no checklist + experimentos
```

No Claude Code, os agentes rodam como subagentes (em paralelo quando independentes). No Claude (app), a skill `imagineering-method` executa as mesmas fases em sequência, interpretando cada papel.

## Instalação (Claude Code)

```bash
git clone https://github.com/drjucie-debug/imagineer
# a pasta do plugin já é um marketplace
/plugin marketplace add ./imagineer
/plugin install imagineer@imagineer

# ou, para testar durante o desenvolvimento
claude --plugin-dir ./imagineer
```

No app Claude, o conteúdo de `skills/imagineering-method` pode ser enviado como skill personalizada.

## Opções do `/imagine`

| Flag | Padrão | Efeito |
|---|---|---|
| `--quick` | desligado | sem subagentes (só o veto fica independente), 5 buscas, 10 ideias, 3 conceitos, 1 rodada de plussing |
| `--ideas N` | `20` | quantidade mínima de ideias no Blue Sky |

O brief sai no idioma do pedido.

Exemplo: `/imagine --quick --ideas 30 novas formas de vender carros`

## Desenvolvimento

```bash
python3 tests/check_plugin.py   # imprime "ok" se a estrutura está íntegra
claude plugin validate .
claude plugin eval . --no-publish  # suíte comportamental em evals/ — CUIDADO: roda sessões reais (custa dinheiro)
```

O Claude Code instala uma **cópia** do plugin em `~/.claude/plugins/cache/`. Depois de editar (e subir a `version` no plugin.json), atualize e abra uma sessão nova:

```bash
claude plugin marketplace update imagineer
claude plugin update imagineer@imagineer
```

## Roadmap

- **v0.1** — comandos, agentes, skill, template e exemplo.
- **v0.2** — memória de ideias por projeto (`.imagineer/ideas.md` + `briefs/`); hook `SessionStart` que injeta o resumo dessa memória (silencioso em projetos sem `.imagineer/`); `/imagine` lê CLAUDE.md/README do projeto e pergunta quem é o convidado quando o pedido é vago.
- **v0.7** (atual) — formas de entrega: brief como página publicada, `/board` (Blue Sky Board com votos — antecipa o v1.0), `/pitch` em 7 quadros e esboço do cartão-postal em imagem; tudo degrada para markdown quando a sessão não tem as ferramentas.
- **v0.6** — cartão-postal com esboço no topo do brief, etiqueta [memória], entrega em duas camadas, mapa do parque, kit de segunda-feira, cobrança de experimento vencido (Teste até), fantasma 1000 e suíte de evals comportamental (`claude plugin eval`).
- **v0.5** — motor refundado no método real da WDI: a história primeiro, teste do coração, "Sim, se…", Dez Mandamentos de Mickey no checklist (fontes em `skills/imagineering-method/references/principios.md`).
- **v0.4** — modo criação: pedidos de *coisas* (criaturas, personagens, produtos, nomes) entregam as coisas com ficha, em vez de estratégia; regra "nunca troque o entregável"; `/spark` para um conceito rápido.
- **v0.3** — shortlist com nota, veto pós-plussing, checklist de qualidade, fontes etiquetadas; `/ideas` para status e resultado de experimentos (cobre o "Idea Vault" sem servidor MCP — servidor só se houver várias pessoas votando).
- **v0.8** — modo "Imagineer contínuo": tarefa agendada semanal que varre sinais do futuro de cada projeto ativo e envia um "postcard do futuro".
- **v1.0** — polimento pós-uso real; candidato a marketplace.

## O nome

O nome é uma homenagem homônima a **Claude Coats** (1913–1992), Disney Legend e um dos maiores Imagineers: pintor de fundos de *Branca de Neve* a *Cinderela*, foi para a WED Enterprises em 1955 e assinou a direção de arte de Pirates of the Caribbean e da metade sombria da Haunted Mansion — a mansão dos "999 fantasmas felizes" que serve de exemplo ao teste do coração desta skill. A coincidência com o nome do modelo que roda o plugin é o resto da graça. Por regra da Anthropic, o id técnico do plugin não pode começar com "claude-", então ele se instala como `imagineer`.

## Marca e afiliação

Projeto independente, **não afiliado, patrocinado nem endossado** pela Disney ou pela Walt Disney Imagineering. "Imagineering" é marca registrada da Disney Enterprises; o método aqui é uma releitura educacional de princípios publicados em fontes públicas, citadas em `skills/imagineering-method/references/principios.md`. Os exemplos de fan design citam as marcas apenas nominativamente e não têm fim comercial. Para distribuição ampla, considere um nome próprio (ex.: *Dreamforge*, *Horizonte*) mantendo o método.

## Licença

[MIT](LICENSE).
