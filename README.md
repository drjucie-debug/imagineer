# Claude Imagineer

> "É meio divertido fazer o impossível." — princípio que guia o plugin

**Claude Imagineer** é um plugin para Claude e Claude Code que pensa *à frente* de qualquer projeto. Em vez de responder "como fazer X um pouco melhor", ele responde "como seria X se fosse projetado hoje do zero, como uma experiência inesquecível — e qual o caminho de engenharia para chegar lá".

O método se inspira na forma de trabalhar dos Imagineers da Disney: misturar sonhadores e engenheiros na mesma sala, começar pela história, projetar a partir do olhar do convidado e nunca considerar uma ideia terminada ("plussing").

---

## Exemplo de uso

```
/imagine Pesquise novas formas de vender carros
```

O plugin entrega um **Imagineering Brief** com:

1. **Reenquadramento** — a pergunta real por trás do pedido ("vender carros" → "como alguém passa a confiar e amar o carro que vai ter").
2. **Varredura do presente e sinais do futuro** — pesquisa web de tendências, casos e sinais fracos.
3. **Blue Sky** — 20+ ideias sem restrição, inclusive as absurdas.
4. **Histórias** — as 3–5 melhores viram conceitos com narrativa, personagem e "momento mágico".
5. **Jornada do Convidado** — antes, durante e depois, com pontos de dor e de encantamento.
6. **Plussing** — cada conceito passa por 3 rodadas de "e se fosse ainda melhor?".
7. **Engenharia de viabilidade** — o que é possível hoje, em 2 anos e em 5 anos; custo, risco e MVP.
8. **Horizontes** — H1 (fazer na segunda-feira), H2 (piloto em 6–18 meses), H3 (aposta de futuro).
9. **Próximos passos** — experimento de menor custo para validar cada conceito.

Para **um** conceito rápido (≈1 min, sem subagentes nem pesquisa): `/imagineer:spark <desafio>` — reenquadra, 8 ideias, escolhe 1, cena, plus, veto e MVP de 2 semanas.

Exemplos: [`examples/moda-online.md`](examples/moda-online.md) (ciclo real de 9 fases, `--quick`, com fontes) e [`examples/vender-carros.md`](examples/vender-carros.md) (ilustrativo, sem pesquisa).

---

## Estrutura

```
claude-imagineer/
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
│   └── ideas.md                      # /ideas — status e resultados das ideias
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
├── tests/check_plugin.py             # verificação estrutural
└── examples/                        # moda-online.md (real), vender-carros.md (ilustrativo)
```

## Como o ciclo roda

```
Pedido do usuário
      │
      ▼
[1] Reenquadrar ──► [2] futurist-scout (pesquisa)
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
# a pasta do plugin já é um marketplace
/plugin marketplace add ~/Downloads/claude-imagineer
/plugin install imagineer@imagineer

# ou, para testar durante o desenvolvimento
claude --plugin-dir ./claude-imagineer
```

No app Claude, o conteúdo de `skills/imagineering-method` pode ser enviado como skill personalizada.

## Opções do `/imagine`

| Flag | Padrão | Efeito |
|---|---|---|
| `--quick` | desligado | pula pesquisa, 10 ideias, 3 conceitos, 1 rodada de plussing |
| `--ideas N` | `20` | quantidade mínima de ideias no Blue Sky |

O brief sai no idioma do pedido.

Exemplo: `/imagine --quick --ideas 30 novas formas de vender carros`

## Desenvolvimento

```bash
python3 tests/check_plugin.py   # imprime "ok" se a estrutura está íntegra
claude plugin validate .
```

O Claude Code instala uma **cópia** do plugin em `~/.claude/plugins/cache/`. Depois de editar (e subir a `version` no plugin.json), atualize e abra uma sessão nova:

```bash
claude plugin marketplace update imagineer
claude plugin update imagineer@imagineer
```

## Roadmap

- **v0.1** — comandos, agentes, skill, template e exemplo.
- **v0.2** — memória de ideias por projeto (`.imagineer/ideas.md` + `briefs/`); hook `SessionStart` que injeta o resumo dessa memória (silencioso em projetos sem `.imagineer/`); `/imagine` lê CLAUDE.md/README do projeto e pergunta quem é o convidado quando o pedido é vago.
- **v0.4** (atual) — modo criação: pedidos de *coisas* (criaturas, personagens, produtos, nomes) entregam as coisas com ficha, em vez de estratégia; regra "nunca troque o entregável"; `/spark` para um conceito rápido.
- **v0.3** — shortlist com nota, veto pós-plussing, checklist de qualidade, fontes etiquetadas; `/ideas` para status e resultado de experimentos (cobre o "Idea Vault" sem servidor MCP — servidor só se houver várias pessoas votando).
- **v0.5** — modo "Imagineer contínuo": tarefa agendada semanal que varre sinais do futuro de cada projeto ativo e envia um "postcard do futuro".
- **v1.0** — artifact interativo de quadro (Blue Sky board) com arrastar ideias entre horizontes.

## Nota sobre nome

"Imagineering" é marca registrada da Disney. Para uso interno o nome funciona; se for publicar em marketplace, vale considerar um nome próprio (ex.: *Claude Dreamforge*, *Horizonte*) mantendo o método.
