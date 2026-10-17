---
description: Um conceito bom, rápido — reenquadra, 8 ideias, escolhe 1, cena, plus, veto e MVP de 2 semanas (sem subagentes)
argument-hint: <desafio>
allowed-tools: Read, Write, Edit
---

# /spark

Desafio: **$ARGUMENTS**

Você faz tudo sozinho, nesta conversa, sem subagentes e sem pesquisa web. Objetivo: **um** conceito pronto para testar em 2 semanas, em até ~400 palavras. Para pesquisa e vários conceitos, o caminho é `/imagineer:imagine` (ou `/imagineer:imagine --quick`).

## Passos

1. **Memória** — se `.imagineer/ideas.md` existir, leia-o. Não repita ideia registrada; evoluir uma vale.
2. **Reenquadrar** — uma linha cada: pergunta real ("Como poderíamos…?"), convidado, momento da verdade. Se faltar contexto, leia CLAUDE.md/README do projeto; se ainda faltar, assuma e declare em uma linha.
3. **8 ideias** — uma linha cada, lentes variadas (inversão, transplante de outro setor, exagero 10×, remoção, futuro pleno, ritual, comunidade, criança de 8 anos). Pelo menos 2 "impossíveis hoje". Não avalie ainda.
4. **Escolher 1** — nota 1–5 em Encantamento, Diferenciação, Dor resolvida, Viabilidade. Mostre as 3 maiores somas em uma linha. Leve a maior; se ela não tiver Encantamento ≥ 4, leve a de maior Encantamento entre as 3.
5. **Conceito** — nome, logline ("Para [convidado] que [desejo], [conceito] é [promessa], diferente de [hoje]"), weenie e **momento mágico** como cena de 4–6 linhas, no presente, com sentidos.
6. **Plus** — um: o detalhe que faria o convidado contar para um amigo.
7. **Veto** — revise o conceito *depois* do plus como advogado do convidado: urgência ou escassez falsa, pressão social ou exposição, gamificação que vicia, dado além do necessário, custo escondido, promessa que não dá para cumprir, devolução/cancelamento difícil, exclusão (renda, idade, deficiência, região, corpo). Liste o que vetou e a correção, ou "nada vetado" com o motivo. A correção substitui o original.
8. **Caminho** — horizonte (H1 = dá para testar com clientes reais em 2 semanas com o que existe; H2 = precisa de parceria/integração; H3 = depende de tecnologia ou comportamento que ainda não existe). Se H2/H3, um **embrião H1**. Depois: MVP de 2 semanas (com quem, quantos, como), métrica e o resultado que diria "vale continuar".
9. **Gravar** (Claude Code, exceto se o diretório atual for o próprio plugin) — salve a resposta em `.imagineer/briefs/<slug>-<AAAA-MM-DD>-spark.md` e acrescente **uma** linha no fim de `.imagineer/ideas.md`. Se o arquivo não existir, crie com:

```
# Ideias — <nome do projeto>

| Data | Ideia | Brief | Horizonte | Status | Resultado |
|---|---|---|---|---|---|
```

Linha: `| <data> | <nome> | briefs/<arquivo> | <H> | sonho | |` (sem `|` dentro das células).

## Formato da resposta

```
**Pergunta real:** … · **Convidado:** … · **Momento da verdade:** …
**Ideias:** 1. … 8. …
**Escolha:** <nome> (E/D/Dor/V = …, soma …) · próximas: …, …
### <Nome>
**Logline:** …
**Weenie:** …
> momento mágico
**Plus:** …
**Veto:** …
**Horizonte:** … · **Embrião H1:** …
**MVP 2 semanas:** … · **Métrica:** … · **Vale continuar se:** …
```

Sem pesquisa, não cite números de mercado; se um dado for essencial, diga qual e sugira `/imagineer:future-scan`.
