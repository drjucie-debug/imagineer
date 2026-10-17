---
description: Blue Sky Board — publica o quadro de ideias do projeto como página interativa (horizontes, votos)
argument-hint: (sem argumento — usa .imagineer/ideas.md)
allowed-tools: Read, Write, Edit, Skill, Artifact, ArtifactData
---

# /board

Publique o quadro de ideias do projeto como página.

1. Leia `.imagineer/ideas.md` (formato em references/ideas-format.md da skill `imagineering-method`). Sem arquivo: diga que o projeto ainda não tem memória e sugira `/imagineer:imagine`.
2. Monte uma página HTML única. Antes de escrever, carregue a skill de design de artifacts do host, se existir (ex.: artifact-design).
   - Colunas por horizonte: **H1 · H2 · H3**, mais **Vagas** (fantasmas 1000) e um contador discreto de arquivadas.
   - Cada ideia é um card: nome, status, resultado, "teste até" (vencido em destaque), nome do arquivo do brief (sem o conteúdo).
   - Capa de uma linha: nome do projeto + "nunca está terminado enquanto houver imaginação".
3. Interação: se a skill **artifact-capabilities** estiver disponível, dê à página o capability db e permita votar num card (1 clique) e mover card entre horizontes, gravando cada ação no db. Sem capabilities, publique a versão estática.
4. Publique como artifact e devolva o link. Numa nova chamada de `/board`: leia votos e movimentos do db (ArtifactData), proponha as mudanças de horizonte no `ideas.md` (pergunte antes de editar) e republique no **MESMO url**.
5. O board mostra, não cria: ideia nova nasce em `/imagine` e `/spark`.

Sem a ferramenta Artifact na sessão, entregue o quadro como tabela markdown na conversa e diga que a versão interativa precisa do Claude Code com artifacts.

Privacidade: o board publica nomes e status das ideias. Na primeira publicação do projeto, pergunte antes se esse conteúdo pode virar página.
