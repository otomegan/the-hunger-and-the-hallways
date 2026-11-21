---
name: renpy-dating-sim-mechanics
description: Expert engine for dating sim and social RPG mechanics in Ren'Py 8.x for The Hunger and the Hallways. Use when scripting heroine interactions, affection and suspicion math, social duels, moral preference matrix, patience/strike systems, intimacy milestones, and dating branch logic.
---

# Ren'Py Dating Sim & Social RPG Mechanics: The Hunger and the Hallways

This skill governs the complex psychological dating sim, social interaction, and affection architecture of *The Hunger and the Hallways*, integrating the systems defined in `game/sistemas_social_rpg.rpy`, `game/definitions.rpy`, and `game/calendario.rpy`.

---

## 1. Heroine Psychological Architecture (`HeroinaStatus`)

Each romantic/social interest is managed through a stateful `HeroinaStatus` object synchronized with store variables:

| Heroína | ID | Variável Afeto | Variável Dúvida | Variável Vínculo | Paciência Máx | Resistência Base |
|---|---|---|---|---|---|---|
| **Lility** | `"lility"` | `afeto_mestra` | `duvida_mestra` | `vinculo_sangue_lility` | 4 | 80 |
| **Elara** | `"elara"` | `afeto_elara` | `duvida_elara` | `vinculo_sangue_elara` | 3 | 65 |
| **Emília** | `"emilia"` | `afeto_emilia` | `duvida_emilia` | `vinculo_sangue_emilia` | 3 | 40 |
| **Valéria** | `"valeria"` | `afeto_valeria` | `duvida_valeria` | `vinculo_sangue_valeria` | 4 | 50 |

### Dynamic Social States
- **Afeto (`afeto`):** Romantic, emotional, and psychological proximity. Unlocks intimacy milestones and cooperative endings.
- **Dúvida (`duvida`):** Suspicion of Victor’s true motives or monstrosity. High doubt locks out vulnerable confessions and adds paranoia to dialogue.
- **Vínculo de Sangue (`vinculo_sangue`):** Occult metaphysical pact. Grants unique combat/magic bonuses at the cost of shared agony.
- **Paciência & Turnos:** Each interaction deducts patience (`$ status_heroina.gastar_paciencia()`). When patience reaches 0, the heroine dismisses Victor for the remainder of the period.
- **Strikes & Bloqueio Diário (`aplicar_strike`):** Offensive or clumsy choices cause a strike. Reaching 2 strikes sets `bloqueada_hoje = True`, slamming the door on Victor until the next day.
- **Alavancagens (`adicionar_alavancagem`):** Discovered secrets, past misdeeds, or hidden debts that can be used to bypass locked dialogue or win arguments.

---

## 2. Moral Preference Matrix (Social Critical Hits)

In conversations and dating choices, heroines evaluate Victor's approach through `OPINIOES_HEROINAS`:

```python
OPINIOES_HEROINAS = {
    "lility":  {"morbido": 2, "autoridade": 2, "compaixao": -2, "sarcasmo": 1, "submissao": 1},
    "elara":   {"morbido": -2, "autoridade": -1, "disciplina": 2, "intelecto": 2, "sarcasmo": -1},
    "emilia":  {"morbido": -2, "compaixao": 2, "gentileza": 2, "agressao": -2, "ocultismo": 1},
    "valeria": {"lucro": 2, "sarcasmo": 2, "moralismo": -2, "astucia": 2, "autoridade": 1}
}
```

### Scripting Social Choices
When writing dialogue choices, always tag options semantically with their psychological archetype:
- **Lility:** Favors morbid curiosity, dominance, and dark surrender. Rejects naive moral compassion.
- **Elara:** Favors disciplined logic, empirical intellect, and adherence to procedure. Rejects morbid indulgence and mockery.
- **Emília:** Favors gentle warmth, spiritual compassion, and gentle occult inquiry. Rejects aggression and cruelty.
- **Valéria:** Favors concrete financial/survival gain, sharp sarcasm, and street cunning. Rejects preachy moralism and aristocratic etiquette.

---

## 3. Stat Checks & Skill Gating in Dialogue

Choices in dating encounters should frequently gate unique paths behind Victor's RPG stats:
```renpy
menu:
    "Dar uma resposta evasiva e formal":
        jump .resposta_neutra

    "Analisar a reação química do reagente" if intelecto >= 2:
        $ status_elara.afeto += 2
        elara "Impressionante. Poucos bolsistas reconheceriam um precipitado de cinabre..."
        jump .sucesso_elara

    "Sustentar o olhar com firmeza predadora" if coragem >= 2 and fome_sangue > 30:
        $ status_lility.afeto += 3
        $ status_lility.submissao += 1
        lility "Olhos famintos... É assim que eu gosto de ver você, Victor."
        jump .sucesso_lility

    "Usar o charme da penumbra para desarmá-la" if charme >= 2:
        $ status_valeria.afeto += 1
        valeria "Não vem com esse sorrisinho de lado pra cima de mim, Vane."
        jump .sucesso_valeria
```

---

## 4. Atmospheric Feedback Protocol (Zero Popup Spam)

As defined in `sistemas_social_rpg.rpy`:
- **DO NOT** trigger immersion-breaking floating screen popups or loud arcade chimes during intimate narrative moments.
- Use `notificar_rpg(titulo, descricao, cor)` or subtle screen tints/sound barks:
  ```renpy
  $ status_valeria.afeto += 1
  play sound "audio/sfx_passos_marmore_colegio.ogg" # ou som ambiente
  show valeria cinica pirulito with dissolve
  ```
- All affection gains and strikes are logged quietly to `historico_tatico_feniks` and displayed in the character status/tactical ledger screen.

