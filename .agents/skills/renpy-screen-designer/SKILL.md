---
name: renpy-screen-designer
description: Expert UI/UX screen designer and Screen Language engineer for Ren'Py 8.x in The Hunger and the Hallways. Use when designing, debugging, or styling custom screens, character status profiles, relationship HUDs, inventory grids, modal popups, and dark gothic interface elements.
---

# Ren'Py Screen Designer: The Hunger and the Hallways

This skill provides expert UI architecture and visual design principles for crafting custom screens in Ren'Py 8.x, ensuring stability, responsive layout, and adherence to the dark gothic aesthetic of *The Hunger and the Hallways*.

---

## 1. The Bracket Escaping Rule (CRITICAL)

In Ren'Py text displayables, single square brackets `[...]` interpolate Python expressions.
- Any literal bracket displayed to the player **MUST BE ESCAPED** as `[[...]]`:
  - ❌ **SYNTAX CRASH:** `text "🔒 [Valéria não confia em você]."`
  - ✅ **SAFE UI TEXT:** `text "🔒 [[Valéria não confia em você]."`
  - ✅ **SAFE UI TEXT:** `text "⚡ [[STRIKE MÁXIMO ATINGIDO]]"`

---

## 2. Screen Architecture & Z-Order Hierarchy

| Layer | Z-Order | Modal | Purpose & Screen Examples |
|---|---|---|---|
| **Background / CG** | 0 | False | Standard scene visual and ATL animations. |
| **Dialogue Window** | 20 | False | Native `say` screen and NVL textboxes. |
| **Ambient HUD** | 50 | False | Day/Period tracker (`hud_calendario`), Blood Hunger meter, Quick Menu. |
| **Full Menus & Profiles**| 90 | True | Heroine relationship dossier, Inventory, Tactical Ledger, Quest Log. |
| **Critical Alerts / VFX**| 100 | False | Red Frenzy pulse (`overlay_frenesi_vermelho`), flash effects, jumpscares. |

### Modal Screen Architecture Template
Every modal menu (Character Profile, Inventory, Status Screen) must allow easy exit:
```renpy
screen perfil_heroina(heroina):
    modal True
    zorder 90
    style_prefix "gothic_profile"

    # Tecla ESC ou botão direito fecha a tela
    key "game_menu" action Return()

    # Backdrop semi-transparente escuro
    add Solid("#0d0d12dd")

    frame:
        xalign 0.5 yalign 0.5
        xsize 1100 ysize 720
        background Frame("gui/frame_gotico.png", 12, 12)

        vbox:
            spacing 15
            hbox:
                spacing 20
                text "[heroina.nome]" size 32 color heroina.cor bold True
                textbutton "✖ FECHAR":
                    xalign 1.0
                    action Return()

            # Conteúdo em viewport com scroll suave
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                ysize 580

                vbox:
                    spacing 10
                    text "Afeto: [heroina.afeto]" size 20
                    text "Vínculo de Sangue: [heroina.vinculo_sangue]" size 20
                    text "Paciência: [heroina.paciencia]/[heroina.paciencia_max]" size 20
```

---

## 3. Dark Gothic Color Palette & Styling Tokens

Use consistent, atmospheric color tokens aligned with the visual novel’s world:
- **Crimson Blood (#c20000):** Lility, Frenzy, Blood Hunger meter, violent choices.
- **Antique Bone & Parchment (#d9c9a3):** Diretor Ambrósio, official letters, debt records, neutral narration text.
- **Toxic Boiler Green (#2eb82e):** Valéria, alchemy, industrial steam, survival perks.
- **Exorcist Sorrow Blue (#5c85d6):** Emília, chapel records, holy relics, melancholic memories.
- **Deep Slate Charcoal (#0d0d12):** Background frames, modal overlays, solid backdrops.
- **Warning Amber (#ffaa00):** High tension, low sanity warnings, patience depletion.

---

## 4. Screen Actions & Dynamic Bars

1. **Multiple Actions in Lists:**
   ```renpy
   textbutton "Oferecer Sangue":
       action [
           SetVariable("fome_sangue", fome_sangue - 15),
           SetVariable("status_lility.afeto", status_lility.afeto + 2),
           Play("sound", "audio/sfx_passos_marmore_colegio.ogg"),
           Notify("Vínculo com Lility fortalecido.")
       ]
   ```
2. **Dynamic Progress Bars:**
   Always specify `range` and `xysize`:
   ```renpy
   bar:
       value fome_sangue
       range 100
       xysize (280, 18)
       left_bar Solid("#c20000")
       right_bar Solid("#1a1a24")
   ```

