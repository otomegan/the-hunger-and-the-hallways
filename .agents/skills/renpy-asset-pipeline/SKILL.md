---
name: renpy-asset-pipeline
description: Asset pipeline manager, sprite expression director, and visual/audio consistency guardian for Ren'Py 8.x in The Hunger and the Hallways. Use when organizing image tags, character sprites, ATL transitions, background lighting matrix, audio channels, and asset paths.
---

# Ren'Py Asset Pipeline & Consistency Manager: The Hunger and the Hallways

This skill guarantees that all visual assets (sprites, backgrounds, UI frames) and acoustic assets (barks, SFX, OST) are properly registered, sized, displayed, and played without glitches, clipping, or scale distortion.

---

## 1. Character Sprite Standards & Image Tagging

In Ren'Py 8.x, sprites use structured tag naming so that changing expressions automatically replaces the previous face without needing manual `hide` statements.

### Structured Image Naming Pattern
```renpy
# Sintaxe: image <personagem> <roupa> <expressao> = "caminho"
image lility padrao sorriso = "images/characters/lility_padrao_sorriso.png"
image lility padrao seria = "images/characters/lility_padrao_seria.png"
image valeria caldeiras cinica = "images/characters/valeria_caldeiras_cinica.png"
image valeria caldeiras surpresa = "images/characters/valeria_caldeiras_surpresa.png"
```

### Expression Transitions in Dialogue
When swapping expressions during conversation:
```renpy
show lility padrao sorriso with dissolve
lility "Você é tão previsível, Victor..."
show lility padrao seria with dissolve
lility "Mas não cometa esse erro uma segunda vez."
```

---

## 2. Standard ATL Transforms & Framing

All character sprites in *The Hunger and the Hallways* must adhere to standard ATL framing defined in `definitions.rpy`:

```renpy
transform sprite_padrao:
    xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 1.0 ysize 980 fit "contain"
    block:
        easein 1.8 yzoom 1.014 xzoom 1.004 yoffset 2
        easeout 1.8 yzoom 1.0 xzoom 1.0 yoffset 0
        repeat

transform sprite_close:
    xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 1.0 ysize 1080 fit "contain"

transform pulo_susto:
    yanchor 1.0 ypos 1.0 ysize 980 fit "contain"
    easein 0.1 yoffset -25
    easeout 0.1 yoffset 0
```
- **Rule:** Never display raw unscaled sprites. Always apply `at sprite_padrao` (or appropriate ATL) and `fit "contain"` to prevent sprite cutoffs on 1080p canvas.

---

## 3. Background Lighting Matrix & Atmosphere Transforms

Match the background tone to the day/period and tension level:
- `transform luz_zona_amarela`: Warm daylight / library interior (`TintMatrix("#ffdd99")`).
- `transform luz_zona_vermelha`: Danger zone, boiler room, or high corruption (`TintMatrix("#ff4444")`).
- `transform luz_sombra_noturna`: Curfew night / marble hallway (`TintMatrix("#666699")`).

Example:
```renpy
scene bg_corredor_marmore at luz_sombra_noturna with dissolve
```

---

## 4. Audio Pipeline & Channel Routing (CRITICAL)

Strict adherence to audio architecture:

1. **Voice Barks:**
   - **MUST USE** `channel="barks"`:
     ```renpy
     play barks "audio/voice/valeria/valeria_bark_cinica.ogg"
     valeria "Perdeu alguma coisa aqui embaixo, garoto?"
     ```
   - **NEVER** route short reaction barks to `channel="voice"`, because Ren'Py’s native voice channel is cleared upon rendering the subsequent `say` textbox.
2. **SFX & Ambient Foley:**
   - Use `play sound "audio/sfx_passos_marmore_colegio.ogg"`.
3. **Soundtrack (OST):**
   - Use `play music "audio/ost_caldeiras.ogg" fadein 2.0 fadeout 2.0 loop`.
4. **Mastering Standard:**
   - All `.ogg` files must be Vorbis Stereo 44.1 kHz, Quality 6, normalized to `-1.5 dBFS` peak.

