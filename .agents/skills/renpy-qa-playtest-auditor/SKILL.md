---
name: renpy-qa-playtest-auditor
description: Automated QA, regression testing, and codebase auditor for Ren'Py 8.x in The Hunger and the Hallways. Use when detecting broken image tags, missing audio paths, non-ASCII filename warnings, rollback desync, unhandled menu jumps, and executing headless Ren'Py linting.
---

# Ren'Py QA & Playtest Auditor: The Hunger and the Hallways

This skill establishes automated quality assurance, regression testing, and static analysis procedures for *The Hunger and the Hallways*.

---

## 1. Execução do Linter Oficial Headless Ren'Py 8.5.3

Sempre execute o interpretador oficial headless para validar scripts e schemas após qualquer alteração:

```powershell
& "C:\Users\otome\Downloads\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe" "C:\Users\otome\Downloads\renpy-8.5.3-sdk\renpy.py" "c:\Users\otome\Documents\the hunger and the hallways" lint
```

### Critérios de Aceite no Lint:
- **0 Erros de Sintaxe / Exceções Não Capturadas.**
- **0 Arquivos de Áudio Ausentes:** Nenhuma chamada `play music`, `play sound` ou `play ambient` apontando para arquivos inexistentes.
- **Métricas Esperadas:** ~1.385 blocos de diálogo, 58 menus, 240+ imagens e 49+ telas ativas.

---

## 2. Validador Rápido de Scripts (`scratch/linter_rpy.py`)

Para verificações instantâneas de sintaxe e indentação durante desenvolvimento:

```powershell
python scratch/linter_rpy.py
```

### O que o script valida:
1. Paridade de blocos `python:` e indentações de 4 espaços.
2. Fechamento de colchetes, aspas e parênteses em chamadas `$ th_bark()` e `$ th_sfx()`.
3. Declarações `default` e `define` duplicadas entre arquivos.

---

## 3. Checklist de Auditoria de Áudio e Canais

Para evitar sobreposições ou quebras no motor de som:

| Canal | Uso Permitido | Proibições Rigorosas |
|---|---|---|
| `ambient` | Áudios contínuos de cenários (`audio/ambiente/`) e chuva (`sfx_chuva_ambiente.ogg`). | Nunca chamar `play sound` para sons atmosféricos de cenário. |
| `sound` | Efeitos sonoros pontuais (golpes de lâmina, passos, batimentos, trincados). | Não tocar faixas de loop contínuo sem parar explicitamente. |
| `music` | Trilhas sonoras BGM dos cenários e combate. | Sempre usar `fadein 1.5` ou `fadein 2.0` para evitar cortes abruptos. |
| `barks` | Falas curtas de reação de heroínas e mobs (`th_bark`). | **Nunca usar `channel="voice"` para Voice Barks**, pois o Ren'Py o cancela ao desenhar novos diálogos. |

---

## 4. Prevenção de Desincronização de Rollback e Saves

1. **Objetos no Store:** Classes Python complexas (`HeroinaStatus`, `MisterioCaso`) devem herdar de `store.object` ou `renpy.python.RevertableObject` para participar do rollback com fidelidade total.
2. **`renpy.block_rollback()`:** Sempre bloqueie o rollback imediatamente no início de loops de combate ou eventos com morte permanente:
   ```renpy
   label loop_turno_combate:
       $ renpy.block_rollback()
   ```
3. **Registro Idempotente de Canais:** Canais de áudio devem ser registrados em `init -5 python:` sem introspecção arriscada:
   ```renpy
   init -5 python:
       renpy.music.register_channel("ambient", mixer="sfx", loop=True)
   ```

---

## 5. Auditoria de Tags de Imagem e Resoluções

1. **Resolução Padrão:** O projeto roda em **1920x1080 (Full HD)**. Sprites e CGs devem ser exportados em proporções compatíveis.
2. **Nomes de Arquivo ASCII:** Evite acentos e caracteres especiais (`ç`, `ã`, `é`) em nomes de arquivos de imagem e áudio para garantir compatibilidade com builds multiplataforma (Linux, Mac e Windows).
3. **Limpeza Pré-Combate:** Antes de exibir a arena de batalha, garanta que todos os sprites de cena foram ocultados com `python: for _t in (...): renpy.hide(_t)`.

