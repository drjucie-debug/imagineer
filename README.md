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

Veja o exemplo completo em [`examples/vender-carros.md`](examples/vender-carros.md).

---

## Estrutura

```
claude-imagineer/
├── .claude-plugin/plugin.json        # manifesto
├── commands/                         # comandos de barra
│   ├── imagine.md                    # /imagine  — ciclo completo
│   ├── blue-sky.md                   # /blue-sky — só a explosão de ideias
│   ├── plus.md                       # /plus     — melhora uma ideia existente
│   ├── story.md                      # /story    — transforma ideia em narrativa
│   ├── guest-journey.md              # /guest-journey — mapa da experiência
│   └── future-scan.md                # /future-scan — sinais e tendências
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
│       └── horizontes.md             # modelo H1/H2/H3 e critérios
├── templates/imagineering-brief.md   # formato do entregável
└── examples/vender-carros.md         # exemplo completo
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
           [4] story-architect + guest-advocate (3–5 conceitos)
                          │
                          ▼
                [5] devils-plusser (3 rodadas de plussing)
                          │
                          ▼
                [6] show-engineer (viabilidade, H1/H2/H3)
                          │
                          ▼
                 Imagineering Brief + próximos passos
```

No Claude Code, os agentes rodam como subagentes (em paralelo quando independentes). No Claude (app), a skill `imagineering-method` executa as mesmas fases em sequência, interpretando cada papel.

## Instalação (Claude Code)

```bash
# a partir de um marketplace local
/plugin marketplace add ./caminho/para/marketplace
/plugin install claude-imagineer

# ou, para testar durante o desenvolvimento
claude --plugin-dir ./claude-imagineer
```

No app Claude, o conteúdo de `skills/imagineering-method` pode ser enviado como skill personalizada.

## Configuração opcional

| Variável | Padrão | Efeito |
|---|---|---|
| `IMAGINEER_DEPTH` | `full` | `quick` pula pesquisa e faz 1 rodada de plussing |
| `IMAGINEER_IDEAS` | `20` | quantidade mínima de ideias no Blue Sky |
| `IMAGINEER_LANG` | `pt-BR` | idioma do brief |

## Roadmap

- **v0.1** (este esboço) — comandos, agentes, skill, template e exemplo.
- **v0.2** — hook `SessionStart` que lê o `CLAUDE.md` do projeto e oferece um "/imagine" focado nele; memória de ideias por projeto (`.imagineer/ideas.md`).
- **v0.3** — servidor MCP "Idea Vault" com busca de ideias anteriores, votação e status (sonho → piloto → lançado).
- **v0.4** — modo "Imagineer contínuo": tarefa agendada semanal que varre sinais do futuro de cada projeto ativo e envia um "postcard do futuro".
- **v1.0** — artifact interativo de quadro (Blue Sky board) com arrastar ideias entre horizontes.

## Nota sobre nome

"Imagineering" é marca registrada da Disney. Para uso interno o nome funciona; se for publicar em marketplace, vale considerar um nome próprio (ex.: *Claude Dreamforge*, *Horizonte*) mantendo o método.
