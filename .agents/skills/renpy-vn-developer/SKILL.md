---
name: renpy-vn-developer
description: Expert Ren'Py 8.x visual novel development skill. Use when creating, refactoring, or debugging Ren'Py scripts, custom screens, UI styling, variable states, dialogue branching, rollback management, and game systems.
---

# Ren'Py 8.x Visual Novel Developer Skill

Expert architectural guidance for developing and debugging Visual Novels in Ren'Py 8.x.

## 1. Syntax & String Interpolation Rules (CRITICAL)

In Ren'Py text displayables (`text`, dialog lines, button captions):
- **Single square brackets `[...]` interpolate Python expressions**: e.g., `text "HP: [hp]/[hp_max]"`.
- **Literal brackets MUST be escaped with double brackets `[[...]]`**:
  - ❌ **BROKEN:** `text "🔒 [Valéria não confia em você]."` -> Causes `SyntaxError: invalid syntax` in py_eval!
  - ✅ **CORRECT:** `text "🔒 [[Valéria não confia em você]."`
  - ✅ **CORRECT:** `text "🌟 [[MARCO DISPONÍVEL!]]"`
- **Percentages in text**: Use `%%` to output a literal `%` in interpolated strings: e.g., `"Exposição: [exposicao]%%"`.

## 2. Screen Language Best Practices

When building custom UI screens (`screen nome_da_tela()`):
- **Predictable layout nesting**: Always wrap layout elements in `frame`, `vbox`, `hbox`, or `grid` with explicit `xalign`, `yalign`, `xysize`, and `spacing`.
- **Z-Order & Modality**:
  - Modal overlay screens (like inventory, shops, character stats): use `modal True` and `zorder 90` to block interaction with underlying dialogue.
  - Non-modal HUD overlays: use `zorder 50` or `zorder 80` without `modal True`.
- **Screen Actions**:
  - Multiple actions must be in a list: `action [SetVariable("item", 1), Notify("Obtido!"), Return()]`.
  - Conditional button sensitivity: use `sensitive condicao` instead of omitting the button, or provide an alternative `action Notify(...)` explaining why it is locked.

## 3. State Management & Variables

- **`default` for mutable game state**: Any variable that changes during gameplay (HP, affection, money, flags) MUST be defined with `default var = valor`.
  - Ensures correct serialization into save files and clean rollback.
- **`define` for static constants**: Characters, transitions, constants, fonts, and fixed configurations use `define`.
- **Rollback Safety**:
  - Use `$ renpy.block_rollback()` at the start of irreversible mini-games or combat loops.
  - Never alter external Python global states that bypass Ren'Py's `store`. Always access store variables via `store.nome_variavel` or direct variable names.

## 4. Ren'Py Lint & Verification

Always validate code with the official Ren'Py SDK lint after modifying `.rpy` files:
```powershell
& "C:\Users\otome\Downloads\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe" "C:\Users\otome\Downloads\renpy-8.5.3-sdk\renpy.py" "c:\Users\otome\Documents\the hunger and the hallways" lint
```
A successful release must pass with **0 errors**.

