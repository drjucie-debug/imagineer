# Memória de ideias do projeto

Cada projeto guarda suas ideias em `.imagineer/` na raiz:

```
.imagineer/
├── ideas.md                         # uma linha por ideia
└── briefs/<slug>-<AAAA-MM-DD>.md     # um brief por ciclo /imagine
```

## Formato de `ideas.md`

```
# Ideias — <nome do projeto>

| Data | Ideia | Brief | Horizonte | Status |
|---|---|---|---|---|
| 2026-10-16 | Vendedor em 30s | briefs/vender-online-2026-10-16.md | H1 | sonho |
```

- Uma linha por ideia; acrescente sempre no **fim** (a mais nova fica embaixo).
- Crie o arquivo com o cabeçalho acima se ele não existir.
- **Status:** `sonho` → `testando` → `piloto` → `lançado`, ou `arquivada`.
- Registre os conceitos do brief (não as 20+ ideias do Blue Sky) — no máximo 5 por ciclo.
- Não use `|` dentro das células.

## Antes de gerar ideias

Se `ideas.md` existir, leia-o primeiro:
- não repita ideias já registradas — evolua-as (plussing) ou cite-as;
- ideias `arquivada` só voltam com um motivo novo explícito.
