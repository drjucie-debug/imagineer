---
description: Memória de ideias do projeto — lista, muda status e registra resultado de experimentos
argument-hint: [vazio para listar | "<ideia> testando" | "<ideia> resultado: conversão 2x"]
allowed-tools: Read, Edit, Write, Skill
---

# /ideas

Pedido: **$ARGUMENTS**

Arquivo: `.imagineer/ideas.md` na raiz do projeto. O formato está em references/ideas-format.md da skill `imagineering-method` — carregue-a se precisar criar o arquivo.

## Sem argumento: listar
Agrupe por status, na ordem `testando` → `piloto` → `sonho` → `lançado` → `arquivada` (arquivadas só contadas, não listadas). Para cada ideia: nome, horizonte, resultado (se houver).
Termine com **uma** sugestão: a ideia `sonho` de H1 mais antiga ("está esperando há N dias — que tal testar?") ou, se houver `testando` sem resultado há mais de 14 dias, pergunte pelo resultado.

## Com argumento: atualizar
- Encontre a linha pelo nome (aproximado vale; se houver duas candidatas, pergunte qual).
- Status válidos: `sonho`, `testando`, `piloto`, `lançado`, `arquivada`. Outro valor: mostre os válidos e pare.
- Resultado: acrescente à coluna Resultado com a data (`2026-10-30: conversão 2,1×, n=48`), sem apagar o que havia.
- Ideia nova (não existe): acrescente no fim com status `sonho`, horizonte `?` e brief `—`.
- Mostre a linha antes e depois.

Se `.imagineer/ideas.md` não existir e o pedido for listar, diga que o projeto ainda não tem memória e sugira `/imagineer:imagine`.
