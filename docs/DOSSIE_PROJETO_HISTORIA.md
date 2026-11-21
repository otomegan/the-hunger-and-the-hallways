# ==============================================================================
# DOSSIÊ COMPLETO DE ARQUITETURA, RECURSOS E NARRATIVA
# "THE HUNGER & THE HALLWAYS" (Ren'Py 8.x / Python 3)
# Versão Atualizada da Live Build — Novembro de 2026
# ==============================================================================

> Este documento consolida o inventário técnico e narrativo real da live build de
> **The Hunger & The Hallways** (Academia São Cipriano). Para decisões profundas
> de balanceamento e progressão, consulte também [`GAME_DESIGN_DOCUMENT_HH.md`](GAME_DESIGN_DOCUMENT_HH.md).

---

## 1. ESTRUTURA GERAL DO DIRETÓRIO `game/`

- **16 arquivos `.rpy` principais** na raiz de `game/`
- **971 arquivos visuais** distribuídos em `game/images/`
- **739 arquivos de áudio** distribuídos em `game/audio/` (309 vozes em 10 subpastas, incluindo 118 faixas de mobs)

```text
the hunger and the hallways/
└── game/
    ├── script.rpy                   # Roteiro principal: Prólogo, Atos, Marcos de DOOM e 5 Finais (5.551 linhas)
    ├── definitions.rpy              # Characters, transforms ATL, variáveis, pools e helpers de mídia (19.308 linhas)
    ├── custom_screens.rpy           # Mapa tático 17 setores, Feniks, Enfermaria, Dormitório, Lojas, Crafting, Toques e 8 Marcos (24.768 linhas)
    ├── th_sistema_narrativo.rpy     # Canais narrativos, BARKS_VOZ, BARKS_INIMIGOS, th_musica/th_sfx/th_stinger/th_bark (1.590 linhas)
    ├── sistemas_social_rpg.rpy      # Sistema Feniks Social: 9 Perks, paciência/strikes, Rastro Olfativo e HeroinaStatus (1.068 linhas)
    ├── sistemas_avancados.rpy       # CATALOGO_ITENS (14 itens), multiplicadores econômicos e utilitários de inventário (995 linhas)
    ├── expansao_conflitos_lore.rpy  # 18 eventos canônicos de conflito, espionagem, Rh-nulo e lore pré-diluviana (908 linhas)
    ├── combate.rpy                  # Motor tático estilo Persona 5: QTE, 4 arquétipos de IA, Hold-Up e drenagem (581 linhas)
    ├── sistemas_world_of_horror.rpy # MisterioCaso (5 casos), GerenciadorRuina (DOOM/Cain), d20 e 6 Climas Diários (278 linhas)
    ├── sistema_som_ambiente.rpy     # Canal ambient em loop e MAPA_AMBIENTES_BACKGROUNDS por sala/horário (276 linhas)
    ├── calendario.rpy               # Máquina do Prólogo Guiado, thresholds automáticos de DOOM, slot_livre e fim_de_evento (205 linhas)
    ├── animacoes_cenas_intimas.rpy  # Transforms ATL íntimos (ofegante, estocadas, flash_red) e template de cena (136 linhas)
    ├── bg_fit.rpy                   # Ajuste automático 2K -> 1920x1080 cover para fundos estáticos (26 linhas)
    ├── screens.rpy                  # Telas nativas customizadas: main_menu parallax, quick_menu e navigation (1.656 linhas)
    ├── gui.rpy & options.rpy        # UI Full HD 1920x1080, tipografia e build "thehungerandthehallways" (493 + 220 linhas)
    ├── audio/                       # 705 arquivos (44 raiz + 275 voice/ + 61 sfx/ + 235 ambiente/ + 90 musicas/)
    └── images/                      # 971 arquivos distribuídos em 16 subpastas + 2 artes de logo na raiz
```

---

## 2. MATRIZ COMPLETA DOS 16 ARQUIVOS `.rpy`

| Arquivo | Linhas | Responsabilidade Técnica na Live Build |
| :--- | :---: | :--- |
| `custom_screens.rpy` | 24.768 | Telas HUD, `mapa_tatico_escola` (17 setores), Dormitório Safe Zone (Emília, Lility e `evento_embate_dormitorio_lility_emilia`), Enfermaria (`acao_consultar_enfermaria`), `hud_exploracao_bs`, `bancada_crafting` (4 receitas), Loja da Valéria, `galeria_memorias` (8 slots), 5 telas de toque, `encontro_mob_figurante`, `micro_evento_ito_corredor` (6 cenas), `emboscada_aleatoria_bs` (26 inimigos) e `evento_marco_*` (8 eventos). |
| `definitions.rpy` | 19.308 | Canais customizados (`barks`, `stinger`), transforms ATL ("Falso Live2D"), matrizes de iluminação por turno, variáveis `default`, `persistent.`, registro de imagens/vídeos, `obter_sprite_victor()`, `sortear_posicoes_heroinas()`, `executar_transe_sangue` e `verificar_marco_disponivel()`. |
| `script.rpy` | 5.551 | Abertura, Prólogo Guiado (`Dia 1` a `Dia 2 Manhã`), primeiros encontros por setor, `evt_d06_tarde` até `evt_d20_noite` (Marcos de DOOM), Clímax `evt_d21_noite` (5 Finais `A`–`E` + derrota), `evento_emilia_pacto_sangue` e `evento_valeria_safra_rara`. |
| `screens.rpy` | 1.656 | Interface nativa do Ren'Py modificada com `main_menu` Parallax, `quick_menu` e atalhos para Central Fênix, Mapa, Inventário e Galeria. |
| `th_sistema_narrativo.rpy` | 1.590 | Helpers `th_musica`, `th_sfx`, `th_stinger` (8 stingers), `th_voz`, `th_bark`, `th_bark_inimigo`, `th_bark_mob` (com suporte desacoplado a abordagem e conversa rotativa de mobs), dicionários `BARKS_VOZ` e `BARKS_INIMIGOS`, além da camada de quitação/gestão narrativa do Livro de Dívidas. |
| `sistemas_social_rpg.rpy` | 1.068 | Classe `HeroinaStatus`, 9 Perks (`CATALOGO_PERKS` em 3 ramos), matriz de paciência/strikes, `Rastro Olfativo`, sistema de `Fiado`, bônus sociais de atributo e alias de notificação `th_notificar_recibo`. |
| `sistemas_avancados.rpy` | 995 | Catálogo oficial `CATALOGO_ITENS` (25 itens), vitrine rotativa diária híbrida de Valéria (`sortear_vitrine_mercado_negro`), multiplicadores econômicos e utilitários de inventário. |
| `expansao_conflitos_lore.rpy` | 908 | 18 cenas canônicas de tensão entre facções, sigilo Rh-nulo, genealogia de Lyra von Blut, água negra subterrânea, lei marcial dos Executores e auditoria de Clara Vance. |
| `combate.rpy` | 581 | Motor universal `iniciar_combate`: QTE com timer dinâmico (`hud_combate_zona_vermelha`), 8 ações táticas, 4 arquétipos de IA (`gremio`, `corrompido`, `inorganico`, `humano`), rendição Persona 5 (`executar_golpe_critico_persona`), `pos_combate_drenagem` e `morte_definitiva`. |
| `gui.rpy` | 493 | Paleta gótica de UI, fontes, bordas de diálogos e dimensionamento Full HD. |
| `sistemas_world_of_horror.rpy` | 278 | `MisterioCaso` (5 casos), `GerenciadorRuina` (`ruina_cain`, fases e sequelas), `testar_pericia_rpg` (d20) e `CLIMAS_ACADEMIA` (6 modificadores diários). |
| `sistema_som_ambiente.rpy` | 276 | Canal `ambient`, `MAPA_AMBIENTES_BACKGROUNDS` e callback automático `_gerenciador_audio_ambiente_callback`. |
| `options.rpy` | 220 | Metadados (`the hunger and the hallways` v1.0), transições padrão e regras de empacotamento. |
| `calendario.rpy` | 205 | Máquina de estados temporais: Prólogo Guiado, `verificar_evento_por_threshold_doom()`, `slot_atual`, `slot_livre` e `fim_de_evento`. |
| `animacoes_cenas_intimas.rpy` | 136 | 7 transforms ATL sensoriais e `template_cena_intima_exemplo`. *(Atualmente `flash_red`, `pulso_sensual_lento`, `cena_lewd_ofegante`, `cena_lewd_ofegante_rapida` e `tremor_climax` estão ativos; restam `estocada_impacto` e `estocada_forte` para futuras CGs).* |
| `bg_fit.rpy` | 26 | Escalador `init 1 python` para fundos estáticos 2K em tela 1080p. |

---

## 3. REGRAS DE ESTADO, ATRIBUTOS & VARIÁVEIS CENTRAIS

### 3.1 Status Vitais & Mecânicas Ocultas de Victor Vane

- **`hp_jogador` / `hp_jogador_max`** (base 100): Saúde física. Zerar em combate leva à tela letal `morte_definitiva`.
- **`fome_sangue`** (0 a 100): Saciedade vampírica. Queda abaixo de 20% dispara estado de **Frenesi** (`victor furia` e alucinações críticas).
- **`humanidade`** (0 a 100): Governa aparência de `obter_sprite_victor()` e finais/reações morais:
  - **`humanidade >= 65` (Fase 1):** Estudante Humano (uniforme padrão escolar, aparência saudável).
  - **`35 <= humanidade < 65` (Fase 2):** Lacaio Desgastado (palidez, olheiras, uniforme ainda ativo).
  - **`humanidade < 35` (Fase 3):** Predador Carmesim (bloqueia sprites de uniforme humano; ativa `victor fase3 predador *` e *Terror Predatório* no subsolo).
- **`exposicao`** (0 a 100%): Nível de alerta no Conselho Estudantil de Elara e nos boletins disciplinares.
- **`tensao_psicologica`**: Fadiga mental acumulada por horrores, traições e abstinência.
- **`ruina_cain`** (0 a 100%, exibida publicamente como **DOOM**): Relógio de apocalipse subterrâneo.
  - `< 30%`: Calmaria ilusória.
  - `30–59%`: Primeiras fraturas e tremores.
  - `60–84%`: Histeria coletiva, Baile/Lei Marcial e conflito aberto.
  - `>= 85%`: Pré-Eclipse / Iminência do Despertar (Desfecho forçado ao atingir `100%` ou cruzar a noite do `Dia 21`).
- **`rastro_olfativo` & `sequelas_ativas`**: Vestígios de sangue no corpo de Victor detectáveis por Elara/Emília e traumas físicos/psíquicos (`trauma_fuga`, `trauma_impacto`, hemorragias) tratáveis por repouso prolongado, Gaze Consagrada ou Dra. Clara Vance.

### 3.2 Atributos RPG & Sociais

- **Principais em combate e perícias (`d20`):** `coragem`, `intelecto`, `ressonancia_pre_diluviana`, `conhecimento_oculto`, `dominio_jogador`, `charme`.
- **Estado social por heroína (`HeroinaStatus` em `sistemas_social_rpg.rpy`):**
  - **Lility (`status_lility` / `mestra`):** `afeto_mestra`, `duvida_mestra`, `vinculo_sangue_mestra`, `paciencia_base = 4`.
  - **Elara (`status_elara`):** `afeto_elara`, `duvida_elara`, `vinculo_sangue_elara`, `paciencia_base = 3`.
  - **Emília (`status_emilia`):** `afeto_emilia`, `duvida_emilia`, `vinculo_sangue_emilia`, `paciencia_base = 3`.
  - **Valéria (`status_valeria`):** `afeto_valeria`, `duvida_valeria`, `vinculo_sangue_valeria`, `paciencia_base = 4`.
- **Sistema de Dívidas (`registro_dividas_ativas` / `DividaAtiva`):** Centralizado na aba **Livro de Dívidas** da Central Fênix, cobrindo dívidas institucionais e `Fiado` no Mercado Negro.

### 3.3 Ciclo Temporal & Zonas de Risco

- **`dia_atual`** (contagem livre de sobrevivência; clímax máximo forçado em `>= 21` ou `DOOM 100%`) e **`periodo`**:
  - **Manhã (`Zona Azul`):** Foco em manutenção social, Enfermaria, pátios diurnos e coleta segura.
  - **Tarde (`Zona Amarela`):** Fiscalização elevada, crafting, casos WOH e negociações nas Caldeiras.
  - **Noite (`Zona Vermelha`):** Caça letal nas alas escuras, 26 arquétipos em `emboscada_aleatoria_bs`, rituais, Transe e encontros críticos.
- **Dormitório (`dormitorio`):** **Zona Segura (`0` passos)**. Sem consumo de AP para investigar nem risco de combate nos corredores; permite descansar (`acao_descansar_dormitorio`) e interagir diretamente com Emília, Lility ou ambas em confronto (`evento_embate_dormitorio_lility_emilia`).

---

## 4. INVENTÁRIO ATUAL DE MÍDIA (`game/images/` — 971 Arquivos)

| Pasta | Arquivos | Formatos | Função na Build |
| :--- | :---: | :---: | :--- |
| `Background Wallpapers motions/` | 148 | 85 `.webm`, 59 `.mp4`, 4 `.webp` | Fundos animados de salas, horários, chuva, catacumbas, caldeiras e eclipse. *(Nota: os `.mp4` são resíduos/duplicatas pré-conversão VP9).* |
| `wallpapers static/` | 88 | 81 `.webp`, 7 `.jpg` | Fundos estáticos 2K/1080p, mapas (`mapa manha/tarde/noite`), bibliotecas e criptas. |
| `Enemy's/` | 145 | 145 `.webp` | Sprites de combate + sprites dedicados de derrota pós-luta dos **26 arquétipos** da Zona Vermelha e chefes (`hachishaku`, `loira do banheiro`, `fada verde`). |
| `mobs/` | 256 | 250 `.webp`, 6 `.png` | Figurantes *Mobu Kyara* (`calouro`, `veterano`, `veterana`, `policial`, `diretor`, `enfermeira`, `executora`, `ocultista`, etc.). |
| `elara/` | 38 | 38 `.webp` | Poses da Presidente (23 raiz + 15 em `corpo inteiro elara, apenas para batalha/`). |
| `emilia/` | 45 | 45 `.webp` | Poses de Emília (39 raiz incl. 5 NSFW camisa aberta/caída + 6 `corpo inteiro apenas para batalha/`). |
| `lility/` | 43 | 43 `.webp` | Poses da Mestra (38 raiz + 5 em `corpo inteiro/`). |
| `valeria/` | 44 | 44 `.webp` | Poses da Mercadora (22 raiz + 22 em `corpo inteiro/` incl. 5 variações NSFW). |
| `victor/` | 41 | 24 `.webp`, 17 `.png` | 19 expressões/meio-corpo + 5 corpo inteiro + 17 backups em `png_originais/`. |
| `cain/` | 5 | 5 `.webp` | Formas do Progenitor (`cain agachado`, `ameaca flutuando`, `combate pose`, `neutro espada`, etc.). |
| `Phillip/` | 5 | 5 `.webp` | Lorde Phillip von Karsten (Inquisidor da Fundação). |
| `nora/` | 3 | 3 `.webp` | Cobaia #31 / Executora Nora. |
| `cenas/` | 61 | 24 `.webp`, 33 `.jpg`, 2 `.webm`, 1 `.mp4`, 1 `.png` | CGs narrativos (prólogo, quase morte, pesadelo, transe de sangue das heroínas). |
| `menu/` | 39 | 8 `.webp`, 27 `.png`, 2 `.mp4`, 1 `.webm`, 1 `.py` | Arte parallax da tela título, botões e ícones de interface. |
| `ilustrações especiais/` | 4 | 4 `.png` | 4 artes especiais fora da conversão `.webp` (atualmente sem chamadas `.rpy`). |
| `novos backgrounds para se tirar o som/` | 4 | 4 `.mp4` | Clipes pendentes de extração/conversão para `.webm -an`. |
| Raiz `images/` | 2 | 2 `.jpg` | Referências visuais de posicionamento de logotipo. |

---

## 5. INVENTÁRIO DE ÁUDIO E CANAIS (`game/audio/` — 705 Arquivos)

- **Canais Registrados no Motor:**
  1. **`barks`** (`mixer="voice"`, `loop=False`): Voice barks rápidos via `th_bark`, `th_bark_inimigo`, `th_bark_mob` e `th_voz` (imune a corte por nova caixa `say`).
  2. **`ambient`** (`mixer="sfx"`, `loop=True`): Loop ambiental contínuo por sala gerenciado em `sistema_som_ambiente.rpy`.
  3. **`stinger`** (`mixer="sfx"`, `loop=False`): 8 impactos dramáticos (`stinger_afeto_up`, `duvida_alerta`, `fome_frenesi`, `jumpscare_anomalia`, `morte_definitiva`, `pista_oculta`, `vitoria_combate`, `zona_vermelha`).
  4. **`music` & `sfx`**: Trilhas dinâmicas e efeitos de combate/UI (`blade_slash_heavy.ogg`, `sfx_impacto_corpo.ogg`, `heartbeat.ogg`, etc.).

- **Distribuição em Disco (705 arquivos):**
  - `audio/` raiz (`44` arquivos): trilhas principais (`Tema_Menu`, `The_Cold_Decree`, `Authority_Breach`, `The_Crimson_Chamber`, `The_Hunger_of_Ancient_Gods`, `Iron_Lungs`, `weeping_cello`, `cain_inane`, `bar-da-fada-verde`, etc.) + 8 stingers + SFX base.
  - `audio/voice/` (`275` `.ogg` em 10 pastas): `climax` (63), `elara` (18), `emilia` (18), `inimigos` (27), `lility` (20), `mobs` (84), `nora` (1), `outros` (14), `valeria` (17), `victor` (13).
  - `audio/sfx/` (`61` arquivos: 60 `.ogg`, 1 `.wav`).
  - `audio/ambiente/` (`235` arquivos): 57 loops por sala na raiz + biblioteca pública Kenney (154 `.ogg` + txt) + acervo bruto selecionado.
  - `audio/musicas/` (`90` arquivos: 83 `.mp3`, 4 `.ogg`, 2 `.mp4`, 1 `.png` — acervo de trabalho/alternativas).

Para o mapeamento linha por linha das falas e arquivos, consulte [`CATALOGO_COMPLETO_VOZES_E_AUDIOS.md`](CATALOGO_COMPLETO_VOZES_E_AUDIOS.md).

---

## 6. OS 17 SETORES DO MAPA TÁTICO & METROIDVANIA (`mapa_tatico_escola`)

- **Planta I — Superfície (11 Setores):** `salao_gremio`, `biblioteca`, `sala_musica`, `patio_arvore`, `sala_ocultismo`, `patio_fonte`, `banheiro_abandonado` (trava: rumor/Emília), `dormitorio` (**Zona Segura 0 passos**), `portoes_praca`, `rua_portao`, `enfermaria` (Dra. Clara Vance).
- **Planta II — Subsolo & Exterior Oculto (6 Setores):** `cemiterio_nevoa`, `caldeiras` (Mercado Negro de Valéria — trava de `5/5` pistas nas Caldeiras Centrais + **30%** chance diária de fechar até o Dia 10), `sala_caldeiras` (sorteio antirrepetição entre 3 cenários industriais), `bar_fada_verde` (trava de Passe Clandestino), `catacumbas` (sorteio antirrepetição entre 3 galerias), `cripta_cofre` (trava `3/3` Fragmentos Rúnicos da Chave nas Catacumbas).

Para coordenadas, trilhas sonoras de ambiente e fluxos de desbloqueio completos, consulte [`GUIA_ARQUITETURA_E_MAPA_DA_ESCOLA.md`](GUIA_ARQUITETURA_E_MAPA_DA_ESCOLA.md).

---

## 7. AS 18 CENAS DE EXPANSÃO E LORE (`expansao_conflitos_lore.rpy`)

Todas as **18 cenas canônicas** são disparadas organicamente pela exploração, períodos e variáveis de relação:

1. `ev_lility_fronteira_portoes` — Fronteira de Ferro nos portões à noite (`portoes_praca`).
2. `ev_interceptacao_lility_ponto_cego` — Interceptação de Lility na `biblioteca` ou `patio_arvore`.
3. `ev_visita_noturna_lility_dormitorio` — Vigília de Lility no dormitório à noite (`afeto >= 3`).
4. `ev_embate_noturno_lility_emilia` — Colisão ideológica entre Lility e Emília nas alas periféricas.
5. `ev_negociacao_sombra_lility_valeria` — Encomenda alquímica de Lility nas caldeiras.
6. `ev_rastro_oculto_nora_enfermaria` — Descoberta do Prontuário Sigiloso #31 de Nora.
7. `ev_c01_janela_lility` — A Janela Aberta no Dilúvio na Sala de Música.
8. `ev_c02_triagem_enfermaria` — Triagem da Campanha e segredo do Sangue Dourado (Rh-nulo).
9. `ev_c03_divida_teo_corredor` — Extorsão de Teo na segunda parcela do Termo 112 (`ruina_cain >= 10`).
10. `ev_c05_voce_nao_come` — Emília nota que Victor nunca ingere alimento sólido.
11. `ev_c06_lista_rh_nulo` — Lista confidencial de doadores compatíveis do Grêmio.
12. `ev_c08_escuta_decreto_elara` — Escuta clandestina da discussão entre Elara e Lility.
13. `ev_c12_relatorio_odores_elara` — Relatório Olfativo da Presidência e proposta de agente duplo.
14. `ev_c15_fome_sem_plateia_valeria` — Colapso de abstinência nas caldeiras e pacto pragmático com Valéria.
15. `ev_c16_investigacao_genealogica_lyra` — Investigação heráldica de Emília provando que "von Blut" não existe em nobiliários históricos.
16. `ev_c17_inundacao_agua_negra` — Rompimento da câmara 3 e inundação de água negra nas galerias com Valéria.
17. `ev_c18_vigilia_executores_sombra` — Lei Marcial noturna dos Executores de Choque e cães de caça no Pátio da Fonte.
18. `ev_c19_laudo_sincope_clara` — Auditoria forense de emergência da Fundação sobre as fichas adulteradas da Enfermaria.

---

## 8. MODELO OFICIAL PARA ESCREVER UMA NOVA CENA (`AGENTS.md` COMPLIANT)

```renpy
label exemplo_nova_cena:
    # Nunca defina dia_atual ou periodo manualmente nem desconte fome de turno aqui.
    scene bg animado gabinete diretor entardecer sol with fade
    $ th_musica("The_Cold_Decree", fade=1.5)

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve
    show elara uniforme arrogante meio corpo at sprite_direita with dissolve
    $ th_bark("elara", "sarcastica")

    elara "Você demorou, Victor. Espero que sua desculpa seja melhor do que a que deu na triagem."

    show elara encarando de forma astuta at risada_deboche
    elara "Ou será que esteve andando onde o Conselho mandou trancar?"

    menu:
        "“Sustentar o olhar em silêncio.”":
            $ status_elara.afeto += 1
            $ exposicao = min(100, exposicao + 5)
        "“Estive na biblioteca estudando com Emília.”":
            $ status_elara.duvida += 1
            $ status_emilia.afeto = max(0, status_emilia.afeto - 1)

    jump fim_de_evento
```

