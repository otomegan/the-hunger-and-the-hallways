# 🎙️ CATÁLOGO COMPLETO DE VOZES, BARKS, TRILHAS & ÁUDIOS
## *The Hunger and the Hallways* — Inventário Completo da Live Build (Novembro de 2026)

- **Acervo Total em `game/audio/`:** **739 arquivos** (`309` vozes `.ogg` em 10 subpastas • `61` SFX • `235` em `ambiente/` • `90` em `musicas/` • `44` faixas e stingers na raiz)
- **Padrão Técnico Ren'Py / FFmpeg:** **44.100 Hz, Estéreo (2 canais), `.ogg` Vorbis `q:6`, pico normalizado a `-1.5 dBFS`**, fade de 12ms nas pontas
- **Canais Nativos Configurados:**
  - **`barks`** (`mixer="voice"`, `loop=False`): `th_bark`, `th_bark_inimigo`, `th_bark_mob`, `th_voz` *(nunca cancelado pelo surgimento de falas `say`)*
  - **`ambient`** (`mixer="sfx"`, `loop=True`): `_gerenciador_audio_ambiente_callback` & `MAPA_AMBIENTES_BACKGROUNDS` em `sistema_som_ambiente.rpy`
  - **`stinger`** (`mixer="sfx"`, `loop=False`): `th_stinger` (8 impactos dramáticos)
  - **`music` / `sfx`**: `th_musica`, `th_sfx`

---

## 1. REGRAS DE ROTEAMENTO & FALLBACKS (`th_sistema_narrativo.rpy`)

1. **Roteamento Inteligente de Inimigos (`resolver_tipo_inimigo`):** Mapeia nomes de monstros em `combate.rpy` para os 9 arquétipos de `BARKS_INIMIGOS` (`aluna`, `policial`, `estudante`, `inquisidor`, `executora`, `alquimista`, `capanga`, `guarda_prata`, `marionete`), enquanto **Elara** e **Lility** possuem desvio prioritário para `BARKS_VOZ`.
2. **Fallback Dinâmico e Rotativo de Figurantes (`th_bark_mob`):**
   - Abordagem inicial: constrói dinamicamente `{id_mob_atual}_{f1|f2|f3|mordida|suborno}` conforme `humanidade` (`>=65`, `35-64`, `<35`) ou `fome_sangue < 20`.
   - Diálogo / Investigação (`acao="conversa"`): sorteia dinamicamente entre `{id_mob_atual}_conversa_1.ogg` e `{id_mob_atual}_conversa_2.ogg`, evitando repetição vocal em um mesmo encontro.
3. **Prioridade de Voz Local:** Pool Gemini TTS (`gemini-3.8-flash-tts`, `gemini-3.8-flash-lite-tts`, `gemini-3.1-flash-tts-preview`) com failover neural offline Kokoro ONNX / Edge-TTS (`GEMINI.md`).

---

## 2. HEROÍNAS PRINCIPAIS (`audio/voice/{lility,elara,emilia,valeria}` — 73 Faixas)

### 2.1 Mestra Lility (20 Faixas em `voice/lility/`)
- **Casting:** Gemini `Kore` / `Aoede` • Kokoro `af_bella`
- **Tonalidade em `BARKS_VOZ["lility"]`:** `padrao`, `confronto`, `decisao`, `irritada`, `timida`, `transe`, `crit`, `ciume`, `aviso`, `rejeicao`, `prazer`, `luta`, `pesadelo`, `risada`.

| Arquivo (.ogg) | Uso / Contexto |
| :--- | :--- |
| `lility_bark_ameaca`, `lility_bark_dentes` | Dúvida alta / confronto predatório (`confronto`, `irritada`) |
| `lility_bark_aviso`, `lility_bark_tedio` | Entrada no covil / tédio aristocrático |
| `lility_bark_cachorrinho`, `lility_bark_deboche` | Provocação e sedução inicial (`padrao`) |
| `lility_bark_inacabada`, `lility_bark_fome_antiga` | Melancolia régia e condescendência literária (`decisao`, `padrao`) |
| `lility_bark_ciume`, `lility_bark_crit` | Ciúme de rivais / crítico social positivo |
| `lility_bark_luta`, `lility_bark_pesadelo`, `lility_bark_rejeicao` | Combate, pós-pesadelo de Victor e insubordinação |
| `lility_bark_transe`, `lility_bark_prazer`, `lility_bark_vergonha` | Transe de Sangue, êxtase e flerte ao acordar |
| `lility_bark_risada`, `lility_risada_deboche`, `lility_risada_ronronar` | Variantes de risada e carinho (`risada`) |
| `lyra_bark_genealogia` 🌟 | Segredo da identidade falsa `"Lyra von Blut"` |

### 2.2 Presidente Elara von Weiss (18 Faixas em `voice/elara/`)
- **Casting:** Gemini `Aoede` • Kokoro `af_sarah`
- **Tonalidade em `BARKS_VOZ["elara"]`:** `padrao`, `confronto`, `decisao`, `irritada`, `timida`, `transe`, `crit`, `ciume`, `dor`, `derrota`, `hesitacao`, `alerta`, `risada`.

| Arquivo (.ogg) | Uso / Contexto |
| :--- | :--- |
| `elara_bark_chamado`, `elara_bark_registered`, `elara_bark_aprovacao` | Despacho no Gabinete / aprovação fria |
| `elara_bark_data_point`, `elara_bark_liability`, `elara_bark_someone_pays` | Burocracia implacável (`confronto`, `decisao`) |
| `elara_bark_ordem`, `elara_bark_desprezo`, `elara_bark_alerta` | Grilhão de Sangue, quebra de ordem e patrulha |
| `elara_bark_ciume`, `elara_bark_corada`, `elara_bark_transe` | Ciúmes, toque inesperado e comunhão de sangue |
| `elara_bark_dor`, `elara_bark_derrota`, `elara_bark_hesitacao` | Duelo, orgulho ferido e dilema moral |
| `elara_bark_risada`, `elara_risada_desprezo`, `elara_risada_divertida` | Risadas aristocráticas e flerte intelectual |

### 2.3 Emília von Karsten (18 Faixas em `voice/emilia/`)
- **Casting:** Gemini `Leda` • Kokoro `af_nicole`
- **Tonalidade em `BARKS_VOZ["emilia"]`:** `padrao`, `suspeita`, `votos`, `timida`, `irritada`, `alerta`, `transe`, `crit`, `dor`, `consolo`, `reza`, `lagrima`, `risada`.

| Arquivo (.ogg) | Uso / Contexto |
| :--- | :--- |
| `emilia_bark_chamado`, `emilia_bark_cura`, `emilia_bark_consolo`, `emilia_bark_crit` | Saudação na Biblioteca/Quarto, bênçãos e confiança |
| `emilia_bark_oracao`, `emilia_bark_reza`, `emilia_bark_votos` | Orações em latim e conflito interior dos votos |
| `emilia_bark_suspeita`, `emilia_bark_po_nas_maos`, `emilia_bark_prata` | Cheiro de sangue, poeira das catacumbas e cruz de prata |
| `emilia_bark_alerta`, `emilia_bark_dor`, `emilia_bark_lagrima` | Ameaça sombria, queimadura e apelo contra Frenesi |
| `emilia_bark_timida`, `emilia_bark_pacto` | Toque próximo e Pacto Sagrado |
| `emilia_bark_risada`, `emilia_risada_alivio`, `emilia_risada_timida` | Risadas nervosas, alívio e romance |

### 2.4 Valéria (17 Faixas em `voice/valeria/`)
- **Casting:** Gemini `Zephyr` • Kokoro `af_sky`
- **Tonalidade em `BARKS_VOZ["valeria"]`:** `padrao`, `provocacao`, `toque`, `irritada`, `transe`, `crit`, `dor`, `segredo`, `vitoria`, `risada`.

| Arquivo (.ogg) | Uso / Contexto |
| :--- | :--- |
| `valeria_bark_negocios`, `valeria_bark_who_pays`, `valeria_bark_price_not_value` | Balcão das Caldeiras e pragmatismo comercial |
| `valeria_bark_bloqueio`, `valeria_bark_armadilha`, `valeria_bark_crit`, `valeria_bark_vitoria` | Sem fundos, fiado, acordo perfeito e lucro |
| `valeria_bark_provocacao`, `valeria_bark_tres_goles`, `valeria_bark_segredo` | Provocação no subsolo e limite da mordida |
| `valeria_bark_safra`, `valeria_bark_transe`, `valeria_bark_toque`, `valeria_bark_dor` | Safra Rara, interação tátil e combate |
| `valeria_bark_risada`, `valeria_risada_cinica`, `valeria_risada_estalo` | Humor ácido e estalo irônico |

---

## 3. PROTAGONISTA: VICTOR VANE (`voice/victor/` — 13 Faixas + 2 em `climax/`)

- **Casting:** Gemini `Algieba` • Kokoro `am_michael`
- **Barks em `voice/victor/` (13):** `victor_bark_acordar`, `victor_bark_ataque`, `victor_bark_dano`, `victor_bark_divida`, `victor_bark_dor_leve`, `victor_bark_drenar`, `victor_bark_frenesi`, `victor_bark_furioso`, `victor_bark_garras`, `victor_bark_morte`, `victor_bark_regras`, `victor_bark_vitoria`, além de `victor_climax_juramento` *(atualmente sem chamada `.rpy`)*.
- **Falas de Clímax em `voice/climax/` (2):** `victor_despertar_cain.ogg`, `victor_fome_abismo.ogg` *(também sem chamadas ativas no roteiro atual)*.

---

## 4. CHEFES, ANOMALIAS & PERSONAGENS ESPECIAIS (`voice/outros/` & `voice/nora/` — 15 Faixas)

| Pasta | Arquivos (.ogg) | Personagem / Contexto |
| :--- | :--- | :--- |
| `voice/nora/` (1) | `nora_bark_aviso_cain.ogg` | Nora avisando sobre o selo e o Progenitor |
| `voice/outros/` (14) | `cain_bark_desafio.ogg` | Cain desafiando Victor |
| `voice/outros/` | `phillip_bark_ameaca.ogg`, `phillip_bark_dor.ogg`, `phillip_bark_risada.ogg` | Lorde Phillip von Karsten (Batalha / Inquisição) |
| `voice/outros/` | `nora_bark_loucura.ogg`, `nora_bark_dor.ogg`, `nora_bark_risada.ogg` | Nora Vasques (Frenesi / Cobaia #31) |
| `voice/outros/` | `fada_bark_enigma.ogg`, `fada_bark_dor.ogg`, `fada_bark_risada.ogg` | A Fada Verde (Caso Lote Necrótico / Bar) |
| `voice/outros/` | `loira_bark_espelho.ogg`, `loira_bark_dor.ogg`, `loira_bark_risada.ogg` | Loira do Banheiro (Caso Espelho) |
| `voice/outros/` | `hachishaku_bark_po.ogg` | Mulher de Oito Pés (*"Po... po... po..."*) |

---

## 5. INIMIGOS DE COMBATE (`voice/inimigos/` — 27 Faixas)

Cada um dos **9 grupos de `BARKS_INIMIGOS`** possui exatamente 3 arquivos (`_saudacao`, `_dor`, `_risada`), disparados via `th_bark_inimigo(nome, tom)`:
1. `alquimista_bark_{saudacao,dor,risada}.ogg`
2. `aluna_bark_{saudacao,dor,risada}.ogg`
3. `capanga_bark_{saudacao,dor,risada}.ogg`
4. `estudante_bark_{saudacao,dor,risada}.ogg`
5. `executora_bark_{saudacao,dor,risada}.ogg`
6. `guarda_prata_bark_{saudacao,dor,risada}.ogg`
7. `inquisidor_bark_{saudacao,dor,risada}.ogg`
8. `marionete_bark_{saudacao,dor,risada}.ogg`
9. `policial_bark_{saudacao,dor,risada}.ogg`

---

## 6. MOBS, FIGURANTES & EXPERIMENTOS (`voice/mobs/` — 118 Faixas)

- **17 Conjuntos Base de 4 Falas (`_f1`, `_f2`, `_f3`, `_mordida`/`_suborno` — 72 arquivos):**
  - Calouros: `mob_calouro_a`, `mob_caloura_b`, `mob_calouro_c` (regenerado masculino).
  - Veteranos Gerais: `mob_veterano_a`, `mob_veterana_b`, `mob_veterano_c`, `mob_veterana_c`.
  - Veteranos Temáticos: `mob_veterano_fundao`, `mob_veterana_fundao`, `mob_veterano_ocultista`, `mob_veterana_ocultista`.
  - Corpo Docente & Autoridades: `mob_professor_a`, `mob_professora_b`, `mob_diretor`, `mob_enfermeira` (Dra. Clara Vance).
  - Rondas Policiais: `mob_policial_a`, `mob_policial_b`, `mob_policial_c` (`_suborno`).
- **34 Novas Falas Conversacionais Rotativas (`_conversa_1` e `_conversa_2` — 34 arquivos gerados via Gemini TTS):**
  - Cada um dos 17 figurantes ativos possui agora 2 barks de diálogo investigativo acionados em `th_bark_mob("conversa")` ao selecionar a opção de conversar nos corredores, eliminando repetições de áudio.
- **Falas Únicas & Secundários (7 arquivos):**
  - `executora_bark_lei_marcial.ogg` (Lei Marcial em `expansao_conflitos_lore.rpy`)
  - `mob_aluna_delinquente_provocacao.ogg`, `mob_calouro_anemico_apelo.ogg` (Enfermaria sob cortinas)
  - `teo_bark_divida_01.ogg`, `teo_bark_alivio_02.ogg` (Termo 112 / Corredor)
  - `diretor_bark_drenado.ogg`, `diretor_bark_histeria.ogg`
- **Protótipos Locais Qwen (5 arquivos — não roteados em `.rpy`):** `qwen_aluna_delinquente_provocacao.ogg`, `qwen_caloura_b_alerta.ogg`, `qwen_calouro_anemico_apelo.ogg`, `qwen_executora_decreto.ogg`, `qwen_policial_ronda_toque.ogg`.
*(Total em `voice/mobs/`: 72 base + 34 conversacionais + 7 únicas + 5 experimentais = **118 faixas**).*

---

## 7. CENAS CAPITAIS, MARCOS & CLÍMAX (`voice/climax/` — 63 Faixas)

Todos os **63 arquivos** em `game/audio/voice/climax/` listados por personagem:

| Personagem | Quantidade | Arquivos `.ogg` em `audio/voice/climax/` |
| :--- | :---: | :--- |
| **Elara von Weiss** | 13 | `elara_aviso_expedicao`, `elara_climax_00_deposito`, `elara_climax_01_grilhao`, `elara_climax_02_audiencia`, `elara_climax_02b_cha`, `elara_climax_03_derrota_cofre`, `elara_climax_03a_cofre_furia`, `elara_climax_03b_redencao_nora`, `elara_decreto_marcial`, `elara_duelo_chuva`, `elara_marco_01_inspecao`, `elara_marco_02_coroa`, `elara_marco_confissao` |
| **Emília von Karsten** | 12 | `emilia_aviso_relicario`, `emilia_climax_01_pacto`, `emilia_climax_01_quadro`, `emilia_climax_02_caderno`, `emilia_climax_03_curativo`, `emilia_climax_04_baile`, `emilia_climax_05_desafio_pai`, `emilia_embate_lility`, `emilia_investigacao_genealogica`, `emilia_marco_01_estantes`, `emilia_marco_02_quarto`, `emilia_marco_curativo` |
| **Mestra Lility** | 17 | `lility_climax_01_sonho`, `lility_climax_02_pacto`, `lility_climax_03_primeiro_transe`, `lility_climax_03b_trauma`, `lility_climax_04_valsa`, `lility_climax_04a_valsa_convite`, `lility_climax_04b_abstinencia`, `lility_climax_06_final_a`, `lility_climax_08_final_e`, `lility_embate_emilia`, `lility_marco_01_coleira`, `lility_marco_02_piano`, `lility_piano_transe`, `lility_ponto_cego`, `lility_portoes_nome`, `lility_visita_quarto_01`, `lility_visita_quarto_02` |
| **Valéria** | 8 | `valeria_aviso_grimm`, `valeria_caldeiras_revelacao`, `valeria_climax_00_conhecer`, `valeria_climax_02_lote_vivo`, `valeria_fome_secreta`, `valeria_marco_01_socio`, `valeria_marco_02_bar`, `valeria_marco_partilha` |
| **Nora Vasques** | 5 | `nora_carteira_vazia`, `nora_climax_01_caneta`, `nora_climax_02_parede`, `nora_climax_03_cela_cripta`, `nora_cripta_sussurro` |
| **Enfermeira Clara Vance** | 4 | `enfermeira_climax_01_nora`, `enfermeira_climax_02_sangue_dourado`, `enfermeira_climax_03_suborno`, `enfermeira_climax_04_campanha` |
| **Victor Vane** | 2 | `victor_despertar_cain`, `victor_fome_abismo` *(órfãos sem chamada atual)* |
| **Diretor Ambrósio** | 1 | `diretor_climax_01_sangue_dourado` |
| **Cain** | 1 | `cain_climax_01_despertar` *(órfão sem chamada atual)* |

*(Soma exata: 13 + 12 + 17 + 8 + 5 + 4 + 2 + 1 + 1 = **63 arquivos**).*

---

## 8. TRILHAS MUSICAIS, STINGERS, SFX & ÁUDIO AMBIENTE

### 8.1 Raiz de `game/audio/` (44 Arquivos)
- **8 Stingers (`channel="stinger"`):** `stinger_afeto_up.ogg`, `stinger_duvida_alerta.ogg`, `stinger_fome_frenesi.ogg`, `stinger_jumpscare_anomalia.ogg`, `stinger_morte_definitiva.ogg`, `stinger_pista_oculta.ogg`, `stinger_vitoria_combate.ogg`, `stinger_zona_vermelha.ogg`.
- **Trilhas Ativas (31):** `Authority_Breach`, `Iron_Lungs`, `Safe_Within_the_Blue`, `Safe_Within_the_Blue_2`, `The_Cold_Decree`, `The_Crimson_Chamber`, `the_crimson_chamber_2`, `The_Hunger_of_Ancient_Gods`, `The_Unfinished_Lesson`, `at_the_green_fairy`, `bar-da-fada-verde`, `batalha_hachishakusama` (`.ogg`/`.mp3`), `batalha_loira_banheiro` (`.ogg`/`.mp3`), `cain_inane`, `catactic_requiem`, `dance_of_the_shadowed_court`, `duty_unspoken`, `funeral_in_the_catacombs`, `gothic_waltz`, `insistent_bass`, `menu_musica`, `midnight_in_the_underpass`, `obscura`, `pulsao_sombra`, `sighs_in_the_dark`, `steel_loop`, `suspense_sombrio`, `tema_menu`, `the_keepers_ledger`, `weeping_cello`, `where_the_room_turns_blue`.
- **SFX na Raiz (3):** `blade_slash_heavy.ogg`, `heartbeat.ogg`, `sfx_impacto_corpo.ogg`.

### 8.2 Pasta `audio/sfx/` (61 Arquivos: 60 `.ogg` + `heartbeat.wav`)
Contém cópias/aliases dos 8 stingers, efeitos de combate (`sfx_combate_golpe_esforco`, `sfx_lamina_*`, `sfx_tiro_*`, `sfx_eletricidade_arco_choque`, `sfx_fratura_osso_mordida`, `sfx_besta_*`, `sfx_ghoul_*`, `sfx_zumbi_morte_estertor`), ambiente/exploração (`sfx_chuva_ambiente`, `sfx_mapa_ambiente_*`, `sfx_vasculhar_*`, `sfx_passos_*`, `sfx_caldeiras_vapor_chiado`, `sfx_sussurros_espelho_banheiro`, etc.) e UI (`ui_click`, `ui_hover`, `sfx_ui_item_coletado`, `sfx_dado_rolagem_rpg`).

### 8.3 Pasta `audio/ambiente/` (235 Arquivos) & `audio/musicas/` (90 Arquivos)
- **`audio/ambiente/` raiz (57 `.ogg`):** Loops exclusivos por cenário ligados a `MAPA_AMBIENTES_BACKGROUNDS` (`amb_bg_animado_*.ogg` + `amb_bg_animada_enfermaria_*.ogg`).
- **`sons baixados de dominio publico/` (157 arquivos) & `sons baixados e escolhidos por mim/` (21 arquivos):** Biblioteca Kenney e efeitos brutos (`.wav`/`.flac`/`.mp3`) para mixagem.
- **`audio/musicas/` (90 arquivos):** Acervo original de referência e work-in-progress (83 `.mp3`, 4 `.ogg`, 2 `.mp4`, 1 `.png`) usado para gerar as trilhas masterizadas na raiz de `audio/`.

---

## 9. AUDITORIA DE CAMINHOS & ÁUDIOS ÓRFÃOS (ESTADO DA BUILD)

Auditoria pós-patch técnico: **0 caminhos literais quebrados em runtime** (`script.rpy:57` corrigido para `climax/lility_climax_01_sonho`; `custom_screens.rpy:6270-6277` e `sistema_som_ambiente.rpy` corrigidos com prefixo `audio/sfx/`; `th_sistema_narrativo.rpy:1372-1373` corrigido para `audio/sfx/sfx_hellhound_rosnar_gutural.ogg`).

1. **Áudios de Voz & SFX Ainda Aguardando Cenas Futuras (Órfãos):**
   - `climax/`: `cain_climax_01_despertar.ogg`, `victor_despertar_cain.ogg`, `victor_fome_abismo.ogg`.
   - `victor/`: `victor_climax_juramento.ogg`.
   - `mobs/`: `diretor_bark_drenado.ogg`, `diretor_bark_histeria.ogg` e os 5 arquivos experimentais `qwen_*.ogg` *(observação: `mob_veterano_fundao_*`, `mob_veterana_fundao_*`, `mob_veterano_ocultista_*` e `mob_veterana_ocultista_*` já disparam dinamicamente via `sortear_mob_por_local` + `th_bark_mob`)*.
   - `sfx/`: 8 `.ogg` não referenciados (`menu_musica_alt`, `sfx_ambiente_cemiterio_manha/noite`, `sfx_ambiente_patio_arvore_entardecer_dourado`, `sfx_caldeiras_vapor_chiado`, `sfx_cidade_cyberpunk_hum_noite`, `sfx_patio_fonte_noite`, `sfx_sussurros_espelho_banheiro`).
