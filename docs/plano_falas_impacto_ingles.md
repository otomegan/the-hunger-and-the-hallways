# Roteiro & Plano Vocal em Inglês: 24 Voice Barks das Heroínas (Gemini TTS)

> **Status:** Todas as 24 falas em português foram movidas e arquivadas com segurança em `backup_vozes_pt_heroinas/`.
> **Próxima Etapa:** Geração das 24 falas definitivas em **Inglês** utilizando o Gemini TTS com casting de voz específico para cada personagem.

---

## 🎭 Casting Vocal Canônico (Inglês)

| Heroína | Voz Primária (Gemini TTS) | Fallback Neural Local | Estilo de Atuação |
| :--- | :--- | :--- | :--- |
| **Lility (Lyra von Blut)** | `Kore` | `af_bella` (Kokoro) | Aristocrática, lenta, desdenhosa, sussurro perigoso e possessivo. |
| **Elara von Weiss** | `Aoede` | `af_sarah` (Kokoro) | Autoritária, disciplinada, cortante, firme, vulnerabilidade reprimida. |
| **Emília von Karsten** | `Leda` | `af_nicole` (Kokoro) | Doce, melancólica, piedosa, calorosa com leve tremor de devoção. |
| **Valéria (Caldeiras)** | `Zephyr` | `af_sky` (Kokoro) | Sarcástica, rápida, comercial, maliciosa, pragmatismo de rua. |

---

## 📜 Roteiro Oficial das Falas em Inglês

### 1. Lility (Lyra von Blut) — Voz: `Kore`
1. **Fome Crítica (`lility_bark_fome_critica.ogg`):**
   > *"Your pupils are dilated... The blood calls louder than your reason, doesn't it?"*
2. **Alerta de DOOM (`lility_bark_doom_alerta.ogg`):**
   > *"The air grows heavy... The depths are stirring, Victor. Do not dare falter now."*
3. **Despedida (`lility_bark_despedida.ogg`):**
   > *"Go... but never forget whose hands hold your leash."*
4. **Flagrante (`lility_bark_flagrante.ogg`):**
   > *"Well, what do we have here? Prying where you weren't invited, little pet?"*
5. **Limite de Toque (`lility_bark_toque_limite.ogg`):**
   > *"Do not mistake my patience for weakness, Victor. One more step and I'll take those fingers."*
6. **Anel de Pacto (`lility_bark_presente_anel.ogg`):**
   > *"A covenant ring? How bold... Let us see if you have the backbone to keep such a promise."*

---

### 2. Elara von Weiss — Voz: `Aoede`
1. **Fome Crítica (`elara_bark_fome_ameaca.ogg`):**
   > *"Restrain that predatory gaze, Mr. Vane. One wrong step and the Council will act."*
2. **Alerta de DOOM (`elara_bark_doom_alerta.ogg`):**
   > *"Curfew protocol has been elevated. The rot in this school runs deep... Stay on your guard."*
3. **Dispensa Protocolar (`elara_bark_dispensa.ogg`):**
   > *"Our audience is concluded. Return to your station and fulfill your duties."*
4. **Flagrante (`elara_bark_flagrante.ogg`):**
   > *"Hold it right there! What exactly are you doing rifling through confidential files?"*
5. **Toque Corada (`elara_bark_toque_corada.ogg`):**
   > *"Hands off... If anyone from the Council sees us like this, I will have you locked away."*
6. **Presente Colar (`elara_bark_presente_colar.ogg`):**
   > *"Is this... for me? An officer should not accept this, but... I will keep it."*

---

### 3. Emília von Karsten — Voz: `Leda`
1. **Fome Crítica (`emilia_bark_fome_piedade.ogg`):**
   > *"Victor... you look pale, and your hands are trembling. Please, do not let the thirst take you."*
2. **Alerta de DOOM (`emilia_bark_doom_oracao.ogg`):**
   > *"The bell tolls out of hour... May the saints protect us from whatever crawls beneath the boilers."*
3. **Despedida (`emilia_bark_despedida.ogg`):**
   > *"Be careful out there, Victor. I will keep praying that the shadows spare you."*
4. **Flagrante (`emilia_bark_flagrante.ogg`):**
   > *"Victor?! What are you doing here at this hour? You... you weren't supposed to see this..."*
5. **Carinho Gentil (`emilia_bark_toque_calor.ogg`):**
   > *"Your hands are so cold, Victor... Yet I don't want you to pull away."*
6. **Presente Flores (`emilia_bark_presente_flores.ogg`):**
   > *"Chapel blossoms? It's been so long since anyone showed me such kindness..."*

---

### 4. Valéria (Mercadora das Caldeiras) — Voz: `Zephyr`
1. **Fome Crítica (`valeria_bark_fome_recuo.ogg`):**
   > *"Whoa, put those fangs away, count! Carnage scares off the paying customers and stains my crates."*
2. **Alerta de DOOM (`valeria_bark_doom_alerta.ogg`):**
   > *"Hear that rattle in the pipes? Powder prices are gonna double before midnight..."*
3. **Despedida (`valeria_bark_despedida.ogg`):**
   > *"Come back anytime, partner. Cash in hand, mouth shut—that's how we stay alive."*
4. **Flagrante (`valeria_bark_flagrante.ogg`):**
   > *"Caught red-handed, pal! Trying to lift contraband from the official supplier?"*
5. **Toque / Taxa (`valeria_bark_toque_troco.ogg`):**
   > *"Browsing the goods comes with a convenience fee, partner. Credit or blood?"*
6. **Presente Jaqueta (`valeria_bark_presente_jaqueta.ogg`):**
   > *"Reinforced lining and hidden pockets? Damn, you actually do have good taste!"*

---

## 📁 Estado Atual do Projeto
- **Arquivos em Português:** 24 arquivos `.ogg` arquivados em `backup_vozes_pt_heroinas/` (separados do jogo).
- **Código do Ren'Py:** As conexões em `custom_screens.rpy` e `th_sistema_narrativo.rpy` estão prontas. Como o método `th_bark` possui verificação com `renpy.loadable`, ele não quebra nem gera erros enquanto aguarda os arquivos em inglês.
- **Ren'Py Lint:** 0 erros de sintaxe e 0 falhas de carregamento.
