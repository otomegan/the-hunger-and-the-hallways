---
name: renpy-branching-narrative
description: Expert conditional branching and decision tree architect for Ren'Py 8.x. Use when structuring complex nested menus, conditional dialogue branches, route divergence, local scoped labels, state flags, and preventing label fall-through leaks or rollback desyncs.
---

# Ren'Py Branching Narrative & Conditional Architecture

This skill prevents bugs, dead ends, and state corruption across deep, branching decision trees in Ren'Py 8.x visual novels.

---

## 1. The Cardinal Rule: Zero Label Fall-Through

In Ren'Py, if execution reaches the end of a `label` block without an explicit `jump`, `return`, or convergence, it will blindly fall through into the physically next line of code, triggering scenes out of order.

### ❌ The Broken Fall-Through Bug
```renpy
label escolha_valeria:
    valeria "Decida logo."
    menu:
        "Ajudar a carregar o carvão":
            $ afeto_valeria += 1
            valeria "Valeu, garoto."
            # BUG: Falls right into recusa_valeria!
        "Recusar e ir embora":
            label recusa_valeria:
                valeria "Então sai do meu caminho."
```

### ✅ Clean Convergence Pattern (Explicit Convergence)
```renpy
label escolha_valeria:
    valeria "Decida logo."
    menu:
        "Ajudar a carregar o carvão":
            $ status_valeria.afeto += 1
            valeria "Valeu, garoto."
            jump .fim_escolha

        "Recusar e ir embora":
            $ status_valeria.aplicar_strike("Recusou ajuda braçal")
            valeria "Então sai do meu caminho."
            jump .fim_escolha

    label .fim_escolha:
        # Ponto de convergência limpo e seguro
        scene bg_caldeiras with dissolve
```

---

## 2. Local Scoped Labels (`label .nome_local:`)

Always prefix sub-labels with a dot (`.`):
- Ren'Py treats dot-prefixed labels as children of the parent label.
- Prevents global namespace pollution and naming collisions across different chapter files.
- Can be jumped to locally via `jump .nome_local` or from outside via `jump parent_label.nome_local`.

---

## 3. Nested Menus & Inline Conditionals

When designing multi-level dialogue choices (interrogations, negotiations, seductions):
```renpy
menu:
    "Perguntar sobre os sussurros do espelho" if conhece_lenda_espelho:
        emilia "Você... também ouviu? Pensei que era só a minha culpa falando."
        menu:
            "Segurar a mão trêmula dela" if afeto_emilia >= 2:
                $ status_emilia.afeto += 2
                emilia "Sua mão está fria, Victor... mas não me dá medo."
                jump .conforto_emilia

            "Pressionar por respostas firmes":
                $ status_emilia.gastar_paciencia()
                emilia "Por favor... não me force a lembrar."
                jump .recuo_emilia

    "Mudar de assunto e oferecer chá":
        jump .cha_tranquilo
```

---

## 4. State Flag Discipline

1. **Explicit Enums over Ambiguous Booleans:**
   - Instead of 5 booleans (`recusou`, `aceitou`, `hesitou`), use a single descriptive string state:
     ```renpy
     default pacto_lility_status = "pendente" # "pendente", "aceito_parcial", "recusado", "submetido"
     ```
2. **Never overwrite state in multiple contradictory places:**
   - Always verify if a flag was already set before modifying it in late-game branches.
3. **Rollback Integrity:**
   - Do not perform external I/O or mutate native non-Ren'Py objects inside dialogue branches. Keep state modifications inside standard Ren'Py store variables or serializable Python classes (`default`).

