---
name: vn-narrative-continuity
description: Narrative continuity and state integrity checker for The Hunger and the Hallways. Use when drafting, editing, or testing narrative branches, route flags, timeline events, quest progression, debt ledger updates, and Ren'Py state variables to prevent plot holes and logic desyncs.
---

# Visual Novel Narrative Continuity Checker: The Hunger and the Hallways

This skill enforces strict chronological, state, and branch continuity across all chapters, events, and dialogue files of *The Hunger and the Hallways*.

## Why Continuity Fails in Branching VNs

Visual novels with heavy RPG mechanics (like *The Hunger and the Hallways*) suffer from three fatal continuity bugs when written iteratively:
1. **Amnesia Loops:** Characters react to information as if it's new, despite prior scenes where it was revealed.
2. **Zombie Flags:** Deceased, missing, or hostile characters appearing casually in general background scenes or exploratory nodes.
3. **State Desync:** Narrative describing Victor as healthy and composed when `fome_sangue < 20` or `tensao_psicologica > 80`, or claiming he has no debts when `livro_de_dividas` is full.

---

## 1. Core State Matrix to Verify

Whenever writing or auditing a scene, cross-check these Ren'Py state variables:

### Timeline & Calendar
- `dia_atual` (Dia 1 a 21+): Are characters' knowledge, schedules, and seasonal tension appropriate for the current day?
- `periodo` ("Manhã", "Tarde", "Noite", "Madrugada"):
  - Are background visuals (`scene bg_*`) matching the lighting and shift?
  - Are student curfews, patrol densities, and shadow entities consistent with the time of day?

### Victor's Physiological & Psychological State
- `fome_sangue` (0 - 100):
  - `> 70`: Victor maintains rational lucidity; senses are sharp.
  - `30 - 69`: Irritability, hyper-awareness of jugular pulses, subtle tremors.
  - `< 30`: Frenzy threshold (`overlay_frenesi_vermelho`). Monologues must show compulsive intrusive thoughts, sensory distortion, hunger pain.
- `humanidade` vs `corrupcao`:
  - Narrative choices must reflect Victor's moral erosion or moral resistance.
- `tensao_psicologica`:
  - High tension triggers paranoia, distorted mirror reflections (`reflexo`), and auditory hallucinations (`th_tocar_sfx("sussurros")`).

### Social & Relationship Graph
- Heroine Affection & Suspicion (`afeto_*`, `duvida_*`):
  - Dialogue tone must branch based on threshold checks (`if afeto_valeria >= 3: ... else: ...`).
  - Suspicion (`duvida_*`) locks out honest confessions and increases vigilance.
- **The Debt Ledger (`livro_de_dividas`, `livro_de_creditos`):**
  - Favors accepted from Lility, Elara, or Valéria MUST be tracked. No free favors in this academy.
  - If Victor promised an item, alibi, or blood donation, future dialogue must acknowledge compliance or breach.
- **Broken Rules (`regras_quebradas`):**
  - Victor's mental weight increases each time he breaks Rule 1, 2, 3, or 4.

---

## 2. Continuity Audit Protocol

Before finalizing any `.rpy` scene script, run this 5-point verification checklist:

1. **Prerequisite Check (Gating):**
   - Are `if` conditions guarding dialogue branches logically sound?
   - Example: Did the player already encounter the *Banheiro Abandonado* before discussing the mirror with Emilia?
2. **Flag Mutex & Exclusivity:**
   - Are branching outcomes mutually exclusive? (e.g., if `assinou_doacao_dia1 == "recusou"`, avoid executing code blocks intended for `"assinou"`).
3. **Inventory & Key Item Verification:**
   - Does Victor actually possess the key, letter, chalk, or relic mentioned in dialogue choices? Check `tem_item(...)` or `$ inventory.append(...)`.
4. **NPC Presence & Location Matrix:**
   - Check `loc_mestra`, `loc_emilia`, `loc_elara`, `loc_valeria`. If Valéria is stationed in `caldeiras`, she cannot casually bump into Victor in the `sala_musica` without narrative explanation.
5. **Call / Jump Cleanliness:**
   - Does every `menu` branch end in a clean `jump`, `call`, or flow into a shared convergence label without orphan lines or fall-through leaks?

