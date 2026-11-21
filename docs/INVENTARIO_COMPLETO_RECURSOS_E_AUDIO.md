# 🏛️ THE HUNGER AND THE HALLWAYS — INVENTÁRIO MESTRE DE ATIVOS & RECURSOS

## Catálogo Técnico Completo: Músicas, Personagens, Áudios, Transcrições, Sprites, Cenas e SFX

*Compilação Oficial da Live Build do Jogo — Ren'Py 8.x • Resolução Nativa: 1920×1080 Full HD*

> [!NOTE]
> Este inventário detalha minuciosamente **100% dos ativos visuais e acústicos** integrados ao projeto, servindo como documento mestre para roteiristas, diretores de arte, dubladores e programadores de sistemas.

---

## 📊 1. Resumo Executivo do Acervo Técnico

| Categoria de Ativo | Quantidade em Produção | Formato Técnico Padrão | Observações |
| :--- | :---: | :--- | :--- |
| **Trilhas Musicais (BGM)** | **122 faixas** | `.mp3` / `.ogg` (320kbps / Vorbis q6) | Temas orquestrais, góticos, jazz noir e industriais |
| **Efeitos Sonoros (SFX)** | **69 efeitos** | `.ogg` Vorbis 44.1kHz Estéreo | Combate, manipulação de itens, armas, portas e interfaces |
| **Stingers Dramáticos** | **8 faixas** | `.ogg` Vorbis (2.5s a 5.0s) | Afeto Up, Alerta Dúvida, Pista Revelada, Zona Vermelha |
| **Vozes & Voice Barks** | **361 falas** | `.ogg` Vorbis -1.5 dBFS com fade 12ms | Heroínas, Victor, Chefes, Mobs e falas de Clímax |
| **Ambiência Acústica (Setores)** | **243 faixas** | `.ogg` Vorbis em Loop Contínuo | Chuva nos vitrais, caldeiras a vapor, sussurros e ventos |
| **Sprites de Personagens Principais** | **288 arquivos** | `.webp` (Q92 transparência alpha) | Victor (78), Lility (61), Valéria (54), Emília (47), Elara (43) |
| **Sprites de Mobs & Figurantes** | **256 arquivos** | `.webp` (Q92) | 17 figurantes ativos com 6-8 expressões emocionais |
| **Bestiário & Inimigos de Batalha** | **145 arquivos** | `.webp` (Q92) | 26 arquétipos com poses de prontidão, ataque e derrota |
| **Cenas & CGs de Eventos Narrativos** | **61 arquivos** | `.webp` / `.jpg` (1920×1080 fit cover) | Ilustrações de memórias, flashbacks, transes e clímax |
| **Wallpapers Estáticos** | **88 arquivos** | `.webp` 1080p / 2K calibrado | Cenários da escola, dormitórios, catacumbas e pátios |
| **Fundos Animados em Vídeo** | **148 arquivos** | `.webm` VP9 sem áudio (`-an`) | Partículas de poeira, chuva nos vitrais, tochas e névoa |

---

## 🎵 2. Catálogo Geral de Músicas (Trilhas Sonoras & BGM)

As trilhas musicais definem a identidade gótica, o suspense claustrofóbico e o ritmo tático da academia. Cada faixa possui volume masterizado e transição suave via `th_musica(nome, fade=1.5)`:

| Arquivo de Áudio | Localização / Pasta | Tamanho | Utilização no Roteiro / Contexto |
| :--- | :--- | :---: | :--- |
| `At the Green Fairy - usesuno.com.mp3` | `audio/musicas/At the Green Fairy - usesuno.com.mp3` | 5961.1 KB | Acervo / Trilha Disponível |
| `at_the_green_fairy.mp3` | `audio/musicas/at_the_green_fairy.mp3` | 5961.1 KB | combate.rpy, custom_screens.rpy, script.rpy |
| `Authority_Breach.mp3` | `audio/musicas/Authority_Breach.mp3` | 4230.4 KB | custom_screens.rpy, expansao_conflitos_lore.rpy, script.rpy |
| `bar-da-fada-verde [usesuno.com].mp3` | `audio/musicas/bar-da-fada-verde [usesuno.com].mp3` | 5257.1 KB | Acervo / Trilha Disponível |
| `bar-da-fada-verde.mp3` | `audio/musicas/bar-da-fada-verde.mp3` | 5257.1 KB | custom_screens.rpy |
| `bar_da_fada_verde.mp3` | `audio/musicas/bar_da_fada_verde.mp3` | 5257.1 KB | Acervo / Trilha Disponível |
| `batalha_hachishakusama.mp3` | `audio/musicas/batalha_hachishakusama.mp3` | 6142.0 KB | combate.rpy, th_sistema_narrativo.rpy |
| `batalha_hachishakusama.ogg` | `audio/musicas/batalha_hachishakusama.ogg` | 3813.6 KB | combate.rpy, th_sistema_narrativo.rpy |
| `batalha_loira_banheiro.mp3` | `audio/musicas/batalha_loira_banheiro.mp3` | 5262.4 KB | combate.rpy, th_sistema_narrativo.rpy |
| `batalha_loira_banheiro.ogg` | `audio/musicas/batalha_loira_banheiro.ogg` | 3256.8 KB | combate.rpy, th_sistema_narrativo.rpy |
| `Cain — Inane - tema provavelmente não vou usar.mp3` | `audio/musicas/Cain — Inane - tema provavelmente não vou usar.mp3` | 3881.0 KB | Acervo / Trilha Disponível |
| `cain_inane.mp3` | `audio/musicas/cain_inane.mp3` | 3881.0 KB | script.rpy |
| `Catactic Requiem - tema da resucitacao de Cain.mp3` | `audio/musicas/Catactic Requiem - tema da resucitacao de Cain.mp3` | 5984.7 KB | Acervo / Trilha Disponível |
| `catactic_requiem.mp3` | `audio/musicas/catactic_requiem.mp3` | 5984.7 KB | custom_screens.rpy, th_sistema_narrativo.rpy |
| `dance_of_the_shadowed_court.mp3` | `audio/musicas/dance_of_the_shadowed_court.mp3` | 5519.8 KB | script.rpy |
| `Dangerous Bargain - provavelmente não vou usar.mp3` | `audio/musicas/Dangerous Bargain - provavelmente não vou usar.mp3` | 5166.8 KB | Acervo / Trilha Disponível |
| `Duty_Unspoken - provavelmente não vou usar.mp3` | `audio/musicas/Duty_Unspoken - provavelmente não vou usar.mp3` | 3390.6 KB | Acervo / Trilha Disponível |
| `duty_unspoken.mp3` | `audio/musicas/duty_unspoken.mp3` | 3390.6 KB | script.rpy |
| `elara_tema.mp3` | `audio/musicas/elara_tema.mp3` | 5722.3 KB | combate.rpy |
| `Funeral in the Catacombs - tema da batalha contra Cain segunda parte.mp3` | `audio/musicas/Funeral in the Catacombs - tema da batalha contra Cain segunda parte.mp3` | 5961.0 KB | Acervo / Trilha Disponível |
| `funeral_in_the_catacombs.mp3` | `audio/musicas/funeral_in_the_catacombs.mp3` | 5961.0 KB | custom_screens.rpy, script.rpy, th_sistema_narrativo.rpy |
| `gothic_waltz.mp3` | `audio/musicas/gothic_waltz.mp3` | 7000.8 KB | custom_screens.rpy, script.rpy |
| `Insistent Bass - tema do bar e da turma do fundao.mp3` | `audio/musicas/Insistent Bass - tema do bar e da turma do fundao.mp3` | 5574.9 KB | Acervo / Trilha Disponível |
| `insistent_bass.mp3` | `audio/musicas/insistent_bass.mp3` | 5574.9 KB | script.rpy |
| `Iron_Lungs - tema da caldeiras.mp3` | `audio/musicas/Iron_Lungs - tema da caldeiras.mp3` | 4198.6 KB | Acervo / Trilha Disponível |
| `iron_lungs.mp3` | `audio/musicas/iron_lungs.mp3` | 4198.6 KB | custom_screens.rpy, script.rpy, th_sistema_narrativo.rpy |
| `menu musica.mp3` | `audio/musicas/menu musica.mp3` | 5160.7 KB | Acervo / Trilha Disponível |
| `menu_musica.mp3` | `audio/musicas/menu_musica.mp3` | 5160.7 KB | options.rpy, screens.rpy, th_sistema_narrativo.rpy |
| `menu_musica.ogg` | `audio/musicas/menu_musica.ogg` | 5956.6 KB | options.rpy, screens.rpy, th_sistema_narrativo.rpy |
| `Midnight_in_the_Underpass - tema bar, tema fada verde, tema turma do fundao.mp3` | `audio/musicas/Midnight_in_the_Underpass - tema bar, tema fada verde, tema turma do fundao.mp3` | 3729.0 KB | Acervo / Trilha Disponível |
| `Midnight_in_the_Underpass - tema valeria, tema bar, tema turma do fundao.mp3` | `audio/musicas/Midnight_in_the_Underpass - tema valeria, tema bar, tema turma do fundao.mp3` | 3710.6 KB | Acervo / Trilha Disponível |
| `midnight_in_the_underpass.mp3` | `audio/musicas/midnight_in_the_underpass.mp3` | 3710.6 KB | custom_screens.rpy, script.rpy, th_sistema_narrativo.rpy |
| `My_Workspace-Steady_Groove - tema quarto.mp3` | `audio/musicas/My_Workspace-Steady_Groove - tema quarto.mp3` | 4386.7 KB | Acervo / Trilha Disponível |
| `My_Workspace-Steady_Groove.mp3` | `audio/musicas/My_Workspace-Steady_Groove.mp3` | 4386.7 KB | script.rpy |
| `my_workspace_steady_groove.mp3` | `audio/musicas/my_workspace_steady_groove.mp3` | 4386.7 KB | Acervo / Trilha Disponível |
| `Obscura - transe de sangue com Lility.mp3` | `audio/musicas/Obscura - transe de sangue com Lility.mp3` | 5175.4 KB | Acervo / Trilha Disponível |
| `obscura.mp3` | `audio/musicas/obscura.mp3` | 5175.4 KB | custom_screens.rpy, expansao_conflitos_lore.rpy, script.rpy, th_sistema_narrativo.rpy |
| `Provavelmente não vou usar.mp3` | `audio/musicas/Provavelmente não vou usar.mp3` | 3768.4 KB | Acervo / Trilha Disponível |
| `pulsao_sombra.mp3` | `audio/musicas/pulsao_sombra.mp3` | 4934.0 KB | custom_screens.rpy, script.rpy, th_sistema_narrativo.rpy |
| `pulsão-sombra - tema de investigacao.mp3` | `audio/musicas/pulsão-sombra - tema de investigacao.mp3` | 4934.0 KB | Acervo / Trilha Disponível |
| `Safe_Within_the_Blue.mp3` | `audio/musicas/Safe_Within_the_Blue.mp3` | 3751.6 KB | custom_screens.rpy, script.rpy |
| `safe_within_the_blue_2.mp3` | `audio/musicas/safe_within_the_blue_2.mp3` | 3751.6 KB | custom_screens.rpy, script.rpy |
| `Sighs in the Dark - tema transe de sangue Lility, Elara, Emília.mp3` | `audio/musicas/Sighs in the Dark - tema transe de sangue Lility, Elara, Emília.mp3` | 5612.4 KB | Acervo / Trilha Disponível |
| `sighs_in_the_dark.mp3` | `audio/musicas/sighs_in_the_dark.mp3` | 5612.4 KB | animacoes_cenas_intimas.rpy, custom_screens.rpy, expansao_conflitos_lore.rpy, th_sistema_narrativo.rpy |
| `Steel Loop - tema de batalha - talvez a luta com Phillip.mp3` | `audio/musicas/Steel Loop - tema de batalha - talvez a luta com Phillip.mp3` | 5602.0 KB | Acervo / Trilha Disponível |
| `steel_loop.mp3` | `audio/musicas/steel_loop.mp3` | 5602.0 KB | combate.rpy, expansao_conflitos_lore.rpy, script.rpy, th_sistema_narrativo.rpy |
| `suspense_sombrio.mp3` | `audio/musicas/suspense_sombrio.mp3` | 4934.0 KB | custom_screens.rpy, script.rpy |
| `Tema da valsa.mp3` | `audio/musicas/Tema da valsa.mp3` | 7000.8 KB | Acervo / Trilha Disponível |
| `Tema de Elara.mp3` | `audio/musicas/Tema de Elara.mp3` | 5722.3 KB | Acervo / Trilha Disponível |
| `tema do conselho estudantil.mp3` | `audio/musicas/tema do conselho estudantil.mp3` | 4803.9 KB | Acervo / Trilha Disponível |
| `tema_bar.mp3` | `audio/musicas/tema_bar.mp3` | 3710.6 KB | Acervo / Trilha Disponível |
| `tema_caldeiras.mp3` | `audio/musicas/tema_caldeiras.mp3` | 4198.6 KB | th_sistema_narrativo.rpy |
| `tema_conselho_estudantil.mp3` | `audio/musicas/tema_conselho_estudantil.mp3` | 4803.9 KB | custom_screens.rpy, th_sistema_narrativo.rpy |
| `tema_da_valsa.mp3` | `audio/musicas/tema_da_valsa.mp3` | 7000.8 KB | custom_screens.rpy, th_sistema_narrativo.rpy |
| `tema_de_elara.mp3` | `audio/musicas/tema_de_elara.mp3` | 5722.3 KB | custom_screens.rpy, th_sistema_narrativo.rpy |
| `tema_elara.mp3` | `audio/musicas/tema_elara.mp3` | 5722.3 KB | th_sistema_narrativo.rpy |
| `tema_emilia.mp3` | `audio/musicas/tema_emilia.mp3` | 3793.5 KB | th_sistema_narrativo.rpy |
| `tema_fundao.mp3` | `audio/musicas/tema_fundao.mp3` | 3710.6 KB | Acervo / Trilha Disponível |
| `tema_investigacao.mp3` | `audio/musicas/tema_investigacao.mp3` | 4934.0 KB | Acervo / Trilha Disponível |
| `tema_investigativo_2.mp3` | `audio/musicas/tema_investigativo_2.mp3` | 5273.4 KB | th_sistema_narrativo.rpy |
| `tema_menu.mp3` | `audio/musicas/tema_menu.mp3` | 5160.7 KB | th_sistema_narrativo.rpy |
| `tema_menu.ogg` | `audio/musicas/tema_menu.ogg` | 5956.6 KB | th_sistema_narrativo.rpy |
| `tema_phillip.mp3` | `audio/musicas/tema_phillip.mp3` | 4291.1 KB | th_sistema_narrativo.rpy |
| `tema_quarto.mp3` | `audio/musicas/tema_quarto.mp3` | 4386.7 KB | custom_screens.rpy, th_sistema_narrativo.rpy |
| `tema_valeria.mp3` | `audio/musicas/tema_valeria.mp3` | 3710.6 KB | th_sistema_narrativo.rpy |
| `the crimson chamber - tema principal.mp3` | `audio/musicas/the crimson chamber - tema principal.mp3` | 4163.8 KB | Acervo / Trilha Disponível |
| `The_Cold_Decree - talvez tema de Phillip.mp3` | `audio/musicas/The_Cold_Decree - talvez tema de Phillip.mp3` | 4291.1 KB | Acervo / Trilha Disponível |
| `the_cold_decree.mp3` | `audio/musicas/the_cold_decree.mp3` | 4291.1 KB | combate.rpy, custom_screens.rpy, expansao_conflitos_lore.rpy, script.rpy, th_sistema_narrativo.rpy |
| `The_Crimson_Chamber - tema principal.mp3` | `audio/musicas/The_Crimson_Chamber - tema principal.mp3` | 4155.1 KB | Acervo / Trilha Disponível |
| `the_crimson_chamber.mp3` | `audio/musicas/the_crimson_chamber.mp3` | 4155.1 KB | custom_screens.rpy, script.rpy, th_sistema_narrativo.rpy |
| `the_crimson_chamber_2.mp3` | `audio/musicas/the_crimson_chamber_2.mp3` | 4155.1 KB | script.rpy |
| `the_crimson_chamber_principal.mp3` | `audio/musicas/the_crimson_chamber_principal.mp3` | 4155.1 KB | Acervo / Trilha Disponível |
| `The_Hunger_of_Ancient_Gods - batalha segunda forma cain.mp3` | `audio/musicas/The_Hunger_of_Ancient_Gods - batalha segunda forma cain.mp3` | 4145.3 KB | Acervo / Trilha Disponível |
| `the_hunger_of_ancient_gods.mp3` | `audio/musicas/the_hunger_of_ancient_gods.mp3` | 4145.3 KB | combate.rpy, expansao_conflitos_lore.rpy, script.rpy, th_sistema_narrativo.rpy |
| `the_keepers_ledger.mp3` | `audio/musicas/the_keepers_ledger.mp3` | 3793.5 KB | custom_screens.rpy, expansao_conflitos_lore.rpy, script.rpy, th_sistema_narrativo.rpy |
| `the_keepers_ledger_tema_emilia.mp3` | `audio/musicas/the_keepers_ledger_tema_emilia.mp3` | 3793.5 KB | Acervo / Trilha Disponível |
| `The_Keeper’s_Ledger - tema emilia.mp3` | `audio/musicas/The_Keeper’s_Ledger - tema emilia.mp3` | 3793.5 KB | Acervo / Trilha Disponível |
| `The_Keeper’s_Ledger.mp3` | `audio/musicas/The_Keeper’s_Ledger.mp3` | 3793.5 KB | Acervo / Trilha Disponível |
| `The_Unfinished_Lesson - tema, não sei onde poderia colocar.mp3` | `audio/musicas/The_Unfinished_Lesson - tema, não sei onde poderia colocar.mp3` | 4166.1 KB | Acervo / Trilha Disponível |
| `the_unfinished_lesson.mp3` | `audio/musicas/the_unfinished_lesson.mp3` | 4166.1 KB | custom_screens.rpy, script.rpy |
| `untitled - tema investigativo segundo.mp3` | `audio/musicas/untitled - tema investigativo segundo.mp3` | 5273.4 KB | Acervo / Trilha Disponível |
| `untitled_investigativo.mp3` | `audio/musicas/untitled_investigativo.mp3` | 5273.4 KB | Acervo / Trilha Disponível |
| `waltz-of-midnight-cries [usesuno.com].mp3` | `audio/musicas/waltz-of-midnight-cries [usesuno.com].mp3` | 5519.8 KB | Acervo / Trilha Disponível |
| `Weeping Cello - usesuno.com.mp3` | `audio/musicas/Weeping Cello - usesuno.com.mp3` | 5373.6 KB | Acervo / Trilha Disponível |
| `weeping_cello.mp3` | `audio/musicas/weeping_cello.mp3` | 5373.6 KB | expansao_conflitos_lore.rpy, script.rpy |
| `Where the Room Turns Blue - usesuno.com.mp3` | `audio/musicas/Where the Room Turns Blue - usesuno.com.mp3` | 5611.1 KB | Acervo / Trilha Disponível |
| `where_the_room_turns_blue.mp3` | `audio/musicas/where_the_room_turns_blue.mp3` | 5611.1 KB | custom_screens.rpy, expansao_conflitos_lore.rpy, script.rpy |
| `at_the_green_fairy.ogg` | `audio/at_the_green_fairy.ogg` | 5961.1 KB | combate.rpy, custom_screens.rpy, script.rpy |
| `Authority_Breach.ogg` | `audio/Authority_Breach.ogg` | 4230.4 KB | custom_screens.rpy, expansao_conflitos_lore.rpy, script.rpy |
| `bar-da-fada-verde.ogg` | `audio/bar-da-fada-verde.ogg` | 5257.1 KB | custom_screens.rpy |
| `batalha_hachishakusama.mp3` | `audio/batalha_hachishakusama.mp3` | 6142.0 KB | combate.rpy, th_sistema_narrativo.rpy |
| `batalha_hachishakusama.ogg` | `audio/batalha_hachishakusama.ogg` | 3813.6 KB | combate.rpy, th_sistema_narrativo.rpy |
| `batalha_loira_banheiro.mp3` | `audio/batalha_loira_banheiro.mp3` | 5262.4 KB | combate.rpy, th_sistema_narrativo.rpy |
| `batalha_loira_banheiro.ogg` | `audio/batalha_loira_banheiro.ogg` | 3256.8 KB | combate.rpy, th_sistema_narrativo.rpy |
| `blade_slash_heavy.ogg` | `audio/blade_slash_heavy.ogg` | 10.2 KB | combate.rpy, custom_screens.rpy |
| `cain_inane.ogg` | `audio/cain_inane.ogg` | 3881.0 KB | script.rpy |
| `catactic_requiem.ogg` | `audio/catactic_requiem.ogg` | 5984.7 KB | custom_screens.rpy, th_sistema_narrativo.rpy |
| `dance_of_the_shadowed_court.ogg` | `audio/dance_of_the_shadowed_court.ogg` | 5519.8 KB | script.rpy |
| `duty_unspoken.ogg` | `audio/duty_unspoken.ogg` | 3390.6 KB | script.rpy |
| `funeral_in_the_catacombs.ogg` | `audio/funeral_in_the_catacombs.ogg` | 5961.0 KB | custom_screens.rpy, script.rpy, th_sistema_narrativo.rpy |
| `gothic_waltz.ogg` | `audio/gothic_waltz.ogg` | 7000.8 KB | custom_screens.rpy, script.rpy |
| `heartbeat.ogg` | `audio/heartbeat.ogg` | 137.9 KB | combate.rpy, custom_screens.rpy, script.rpy |
| `insistent_bass.ogg` | `audio/insistent_bass.ogg` | 5574.9 KB | script.rpy |
| `Iron_Lungs.ogg` | `audio/Iron_Lungs.ogg` | 4198.6 KB | custom_screens.rpy, script.rpy, th_sistema_narrativo.rpy |
| `menu_musica.ogg` | `audio/menu_musica.ogg` | 5956.6 KB | options.rpy, screens.rpy, th_sistema_narrativo.rpy |
| `midnight_in_the_underpass.ogg` | `audio/midnight_in_the_underpass.ogg` | 3710.6 KB | custom_screens.rpy, script.rpy, th_sistema_narrativo.rpy |
| `obscura.ogg` | `audio/obscura.ogg` | 5175.4 KB | custom_screens.rpy, expansao_conflitos_lore.rpy, script.rpy, th_sistema_narrativo.rpy |
| `pulsao_sombra.ogg` | `audio/pulsao_sombra.ogg` | 4934.0 KB | custom_screens.rpy, script.rpy, th_sistema_narrativo.rpy |
| `Safe_Within_the_Blue.ogg` | `audio/Safe_Within_the_Blue.ogg` | 3751.6 KB | custom_screens.rpy, script.rpy |
| `Safe_Within_the_Blue_2.ogg` | `audio/Safe_Within_the_Blue_2.ogg` | 3751.6 KB | custom_screens.rpy, script.rpy |
| `sighs_in_the_dark.ogg` | `audio/sighs_in_the_dark.ogg` | 5612.4 KB | animacoes_cenas_intimas.rpy, custom_screens.rpy, expansao_conflitos_lore.rpy, th_sistema_narrativo.rpy |
| `steel_loop.ogg` | `audio/steel_loop.ogg` | 5602.0 KB | combate.rpy, expansao_conflitos_lore.rpy, script.rpy, th_sistema_narrativo.rpy |
| `suspense_sombrio.ogg` | `audio/suspense_sombrio.ogg` | 4934.0 KB | custom_screens.rpy, script.rpy |
| `tema_menu.ogg` | `audio/tema_menu.ogg` | 5956.6 KB | th_sistema_narrativo.rpy |
| `The_Cold_Decree.ogg` | `audio/The_Cold_Decree.ogg` | 4291.1 KB | combate.rpy, custom_screens.rpy, expansao_conflitos_lore.rpy, script.rpy, th_sistema_narrativo.rpy |
| `The_Crimson_Chamber.ogg` | `audio/The_Crimson_Chamber.ogg` | 4155.1 KB | custom_screens.rpy, script.rpy, th_sistema_narrativo.rpy |
| `the_crimson_chamber_2.ogg` | `audio/the_crimson_chamber_2.ogg` | 4155.1 KB | script.rpy |
| `the_hunger_of_ancient_gods.ogg` | `audio/the_hunger_of_ancient_gods.ogg` | 4145.3 KB | combate.rpy, expansao_conflitos_lore.rpy, script.rpy, th_sistema_narrativo.rpy |
| `the_keepers_ledger.ogg` | `audio/the_keepers_ledger.ogg` | 3793.5 KB | custom_screens.rpy, expansao_conflitos_lore.rpy, script.rpy, th_sistema_narrativo.rpy |
| `The_Unfinished_Lesson.ogg` | `audio/The_Unfinished_Lesson.ogg` | 4166.1 KB | custom_screens.rpy, script.rpy |
| `weeping_cello.ogg` | `audio/weeping_cello.ogg` | 5373.6 KB | expansao_conflitos_lore.rpy, script.rpy |
| `where_the_room_turns_blue.ogg` | `audio/where_the_room_turns_blue.ogg` | 5611.1 KB | custom_screens.rpy, expansao_conflitos_lore.rpy, script.rpy |

---

## 🔊 3. Efeitos Sonoros (SFX) & Stingers Dramáticos

### 3.1 Stingers Musicais de Impacto Narrativo (`audio/stinger_*.ogg`)

| Stinger | Arquivo | Canal Ren'Py | Contexto de Disparo no Jogo |
| :--- | :--- | :--- | :--- |
| **Afeto Up** | `stinger_afeto_up.ogg` | `stinger` | Conexão profunda, presente perfeito ou sintonia emocional em diálogo. |
| **Alerta de Dúvida** | `stinger_duvida_alerta.ogg` | `stinger` | Suspeita elevada (Dúvida >= 4) ou falha grave de blefe. |
| **Pista Oculta** | `stinger_pista_oculta.ogg` | `stinger` | Descoberta de evidência de mistério do World of Horror. |
| **Zona Vermelha** | `stinger_zona_vermelha.ogg` | `stinger` | Entrada em setor de alto perigo / toque de recolher ativo. |
| **Jumpscare / Anomalia** | `stinger_jumpscare_anomalia.ogg` | `stinger` | Manifestação sobrenatural súbita (espelho, aparições, alucinação). |
| **Fome & Frenesi** | `stinger_fome_frenesi.ogg` | `stinger` | Sede crítica (< 20%) ou colapso de controle da Besta interior. |
| **Vitória em Combate** | `stinger_vitoria_combate.ogg` | `stinger` | Fim de batalha tática com derrota ou rendição inimiga. |
| **Morte Definitiva** | `stinger_morte_definitiva.ogg` | `stinger` | Game Over / morte do protagonista. |

### 3.2 Efeitos Sonoros de Combate, Ambiente & Mecânicas (`audio/sfx/`)

| Arquivo SFX | Tamanho | Função Mecânica no Jogo |
| :--- | :---: | :--- |
| `blade_slash_heavy.ogg` | 10.2 KB | Acionado via `th_sfx('blade_slash_heavy')` |
| `heartbeat.ogg` | 137.9 KB | Acionado via `th_sfx('heartbeat')` |
| `heartbeat.wav` | 137.9 KB | Acionado via `th_sfx('heartbeat')` |
| `hellhound_rosnar.ogg` | 50.5 KB | Acionado via `th_sfx('hellhound_rosnar')` |
| `menu_musica_alt.ogg` | 5956.6 KB | Acionado via `th_sfx('menu_musica_alt')` |
| `sfx_aberracao_gosma_rastejar.ogg` | 71.7 KB | Acionado via `th_sfx('sfx_aberracao_gosma_rastejar')` |
| `sfx_amassar_lata_caldeiras.ogg` | 23.8 KB | Acionado via `th_sfx('sfx_amassar_lata_caldeiras')` |
| `sfx_ambiente_cemiterio_manha.ogg` | 198.1 KB | Acionado via `th_sfx('sfx_ambiente_cemiterio_manha')` |
| `sfx_ambiente_cemiterio_noite.ogg` | 220.9 KB | Acionado via `th_sfx('sfx_ambiente_cemiterio_noite')` |
| `sfx_ambiente_patio_arvore_entardecer_dourado.ogg` | 193.8 KB | Acionado via `th_sfx('sfx_ambiente_patio_arvore_entardecer_dourado')` |
| `sfx_besta_dano_gemido.ogg` | 26.4 KB | Acionado via `th_sfx('sfx_besta_dano_gemido')` |
| `sfx_besta_rosnado_ameaca.ogg` | 44.4 KB | Acionado via `th_sfx('sfx_besta_rosnado_ameaca')` |
| `sfx_caixa_registradora_valeria.ogg` | 37.4 KB | Acionado via `th_sfx('sfx_caixa_registradora_valeria')` |
| `sfx_caldeiras_vapor_chiado.ogg` | 101.7 KB | Acionado via `th_sfx('sfx_caldeiras_vapor_chiado')` |
| `sfx_chicote_sangue_estalo.ogg` | 24.9 KB | Acionado via `th_sfx('sfx_chicote_sangue_estalo')` |
| `sfx_chuva_ambiente.ogg` | 143.9 KB | Acionado via `th_sfx('sfx_chuva_ambiente')` |
| `sfx_cidade_cyberpunk_hum_noite.ogg` | 199.3 KB | Acionado via `th_sfx('sfx_cidade_cyberpunk_hum_noite')` |
| `sfx_click_seco.ogg` | 11.4 KB | Acionado via `th_sfx('sfx_click_seco')` |
| `sfx_combate_golpe_esforco.ogg` | 25.5 KB | Acionado via `th_sfx('sfx_combate_golpe_esforco')` |
| `sfx_dado_rolagem_rpg.ogg` | 14.3 KB | Acionado via `th_sfx('sfx_dado_rolagem_rpg')` |
| `sfx_desembrulhar_doce_curativo.ogg` | 74.2 KB | Acionado via `th_sfx('sfx_desembrulhar_doce_curativo')` |
| `sfx_distorted_whoosh_vampirico.ogg` | 17.2 KB | Acionado via `th_sfx('sfx_distorted_whoosh_vampirico')` |
| `sfx_dossie_carta_deslizar.ogg` | 13.0 KB | Acionado via `th_sfx('sfx_dossie_carta_deslizar')` |
| `sfx_eletricidade_arco_choque.ogg` | 60.4 KB | Acionado via `th_sfx('sfx_eletricidade_arco_choque')` |
| `sfx_explosao_caldeira_impacto.ogg` | 32.7 KB | Acionado via `th_sfx('sfx_explosao_caldeira_impacto')` |
| `sfx_frasco_alquimia_vidro.ogg` | 6.7 KB | Acionado via `th_sfx('sfx_frasco_alquimia_vidro')` |
| `sfx_fratura_osso_mordida.ogg` | 45.6 KB | Acionado via `th_sfx('sfx_fratura_osso_mordida')` |
| `sfx_ghoul_gargarejo_fome.ogg` | 22.2 KB | Acionado via `th_sfx('sfx_ghoul_gargarejo_fome')` |
| `sfx_hellhound_rosnar_gutural.ogg` | 50.5 KB | Acionado via `th_sfx('sfx_hellhound_rosnar_gutural')` |
| `sfx_impacto_corpo.ogg` | 7.6 KB | Acionado via `th_sfx('sfx_impacto_corpo')` |
| `sfx_inventario_abrir_pasta.ogg` | 12.7 KB | Acionado via `th_sfx('sfx_inventario_abrir_pasta')` |
| `sfx_lamina_corte_rapido.ogg` | 17.5 KB | Acionado via `th_sfx('sfx_lamina_corte_rapido')` |
| `sfx_lamina_espada_corte.ogg` | 18.8 KB | Acionado via `th_sfx('sfx_lamina_espada_corte')` |
| `sfx_lanterna_click.ogg` | 11.1 KB | Acionado via `th_sfx('sfx_lanterna_click')` |
| `sfx_mapa_ambiente_chuva.ogg` | 209.5 KB | Acionado via `th_sfx('sfx_mapa_ambiente_chuva')` |
| `sfx_mapa_ambiente_manha.ogg` | 198.2 KB | Acionado via `th_sfx('sfx_mapa_ambiente_manha')` |
| `sfx_mapa_ambiente_neblina_noite.ogg` | 196.4 KB | Acionado via `th_sfx('sfx_mapa_ambiente_neblina_noite')` |
| `sfx_mapa_ambiente_noturno.ogg` | 202.1 KB | Acionado via `th_sfx('sfx_mapa_ambiente_noturno')` |
| `sfx_mapa_ambiente_subsolo.ogg` | 251.9 KB | Acionado via `th_sfx('sfx_mapa_ambiente_subsolo')` |
| `sfx_mapa_ambiente_tarde.ogg` | 193.5 KB | Acionado via `th_sfx('sfx_mapa_ambiente_tarde')` |
| `sfx_moedas_ouro_transacao.ogg` | 8.8 KB | Acionado via `th_sfx('sfx_moedas_ouro_transacao')` |
| `sfx_moedas_tilintar.ogg` | 8.0 KB | Acionado via `th_sfx('sfx_moedas_tilintar')` |
| `sfx_monstro_rosnar_triplo.ogg` | 58.1 KB | Acionado via `th_sfx('sfx_monstro_rosnar_triplo')` |
| `sfx_nevoeiro_uivo_criatura.ogg` | 93.2 KB | Acionado via `th_sfx('sfx_nevoeiro_uivo_criatura')` |
| `sfx_passos_gravilha_patio.ogg` | 105.5 KB | Acionado via `th_sfx('sfx_passos_gravilha_patio')` |
| `sfx_passos_madeira_ranger.ogg` | 60.0 KB | Acionado via `th_sfx('sfx_passos_madeira_ranger')` |
| `sfx_patio_fonte_noite.ogg` | 202.1 KB | Acionado via `th_sfx('sfx_patio_fonte_noite')` |
| `sfx_pena_anotacao_pista.ogg` | 6.8 KB | Acionado via `th_sfx('sfx_pena_anotacao_pista')` |
| `sfx_psiquico_distorcao_sanidade.ogg` | 4.7 KB | Acionado via `th_sfx('sfx_psiquico_distorcao_sanidade')` |
| `sfx_rpg_afeto_levelup.ogg` | 18.2 KB | Acionado via `th_sfx('sfx_rpg_afeto_levelup')` |
| `sfx_sangue_viscoso_borbulhar.ogg` | 73.9 KB | Acionado via `th_sfx('sfx_sangue_viscoso_borbulhar')` |
| `sfx_splash_sangue_tinta.ogg` | 12.7 KB | Acionado via `th_sfx('sfx_splash_sangue_tinta')` |
| `sfx_sussurros_espelho_banheiro.ogg` | 301.1 KB | Acionado via `th_sfx('sfx_sussurros_espelho_banheiro')` |
| `sfx_tiro_escopeta_reverberacao.ogg` | 46.4 KB | Acionado via `th_sfx('sfx_tiro_escopeta_reverberacao')` |
| `sfx_tiro_pistola_seco.ogg` | 25.8 KB | Acionado via `th_sfx('sfx_tiro_pistola_seco')` |
| `sfx_ui_item_coletado.ogg` | 10.2 KB | Acionado via `th_sfx('sfx_ui_item_coletado')` |
| `sfx_vasculhar_gaveta_abrir.ogg` | 32.1 KB | Acionado via `th_sfx('sfx_vasculhar_gaveta_abrir')` |
| `sfx_vasculhar_objetos_mexer.ogg` | 68.9 KB | Acionado via `th_sfx('sfx_vasculhar_objetos_mexer')` |
| `sfx_zumbi_morte_estertor.ogg` | 28.3 KB | Acionado via `th_sfx('sfx_zumbi_morte_estertor')` |
| `stinger_afeto_up.ogg` | 45.4 KB | Acionado via `th_sfx('stinger_afeto_up')` |
| `stinger_duvida_alerta.ogg` | 37.5 KB | Acionado via `th_sfx('stinger_duvida_alerta')` |
| `stinger_fome_frenesi.ogg` | 48.5 KB | Acionado via `th_sfx('stinger_fome_frenesi')` |
| `stinger_jumpscare_anomalia.ogg` | 38.1 KB | Acionado via `th_sfx('stinger_jumpscare_anomalia')` |
| `stinger_morte_definitiva.ogg` | 62.2 KB | Acionado via `th_sfx('stinger_morte_definitiva')` |
| `stinger_pista_oculta.ogg` | 45.4 KB | Acionado via `th_sfx('stinger_pista_oculta')` |
| `stinger_vitoria_combate.ogg` | 53.4 KB | Acionado via `th_sfx('stinger_vitoria_combate')` |
| `stinger_zona_vermelha.ogg` | 40.3 KB | Acionado via `th_sfx('stinger_zona_vermelha')` |
| `ui_click.ogg` | 4.5 KB | Acionado via `th_sfx('ui_click')` |
| `ui_hover.ogg` | 4.3 KB | Acionado via `th_sfx('ui_hover')` |

---

## 👥 4. Personagens Principais: Sprites, Vozes e Transcrições

### 4.1 Victor Vane (Protagonista)

- **Perfil & Lore:** Bolsista transferido de 20 anos, portador de sangue Rh-Nulo ('Sangue Dourado'). Transformado em vampiro/ghoul na noite do Dia 1 por Lility.
- **Casting de Voz:** Gemini TTS `Algieba` • Kokoro `am_michael`
- **Composição do Guarda-Roupa & Sprites:**
  - **Fase 1 (Humanidade >= 65):** Monitor Bolsista com uniforme escolar impecável (21 expressões + 5 versões 2K alinhadas).
  - **Fase 2 (Humanidade 35-64):** Lacaio em desgaste e decadência física (10 expressões de desgaste, cinismo e cansaço).
  - **Fase 3 (Humanidade < 35):** Predador Vampírico no Abismo (10 expressões severas, olhos rubros intensos e postura predatória).
  - **Frenesi Tríptico:** 3 sprites dedicados (`victor fase1 frenesi.webp`, `victor fase2 frenesi.webp`, `victor fase3 frenesi.webp`).

#### 🎙️ Voice Barks & Transcrições Oficiais (`game/audio/voice/victor`)

| Arquivo de Áudio | Gatilho / Contexto Ren'Py | Transcrição Oficial (Português) | Fala em Inglês |
| :--- | :--- | :--- | :--- |
| `victor_bark_acordar.ogg` | `Início de Turno / Pesadelo` | *"Arf... Arf... [Ofegante após o pesadelo do julgamento]"* | *"[Respiração pesada e ofegante de despertar súbito]"* |
| `victor_bark_ataque.ogg` | `Golpe Básico em Combate` | *"Tome isso!"* | *"Take this!"* |
| `victor_bark_dano.ogg` | `Recebendo Dano` | *"Argh... Maldito...!"* | *"Argh... Damn you...!"* |
| `victor_bark_divida.ogg` | `Desafio do Grêmio` | *"Eu não fujo de dívidas, mas me recuso a ser descartável de novo."* | *"I don't run from debts, but I refuse to be disposable again."* |
| `victor_bark_dor_leve.ogg` | `Resistencia Estoica a Golpe (Victor)` | *"Kh... Is that all you've got?"* | *"Kh... Is that all you've got?"* |
| `victor_bark_drenar.ogg` | `Drenar Inimigo Derrotado` | *"Seu sangue pertence a mim agora."* | *"Your blood belongs to me now."* |
| `victor_bark_frenesi.ogg` | `Fome de Sangue < 20%` | *"Minha garganta está em chamas... Preciso de sangue agora!"* | *"My throat is burning... I need blood right now!"* |
| `victor_bark_furioso.ogg` | `Furia do Julgamento e Injustica Passada (Victor)` | *"You framed me once... You won't take my life twice!"* | *"You framed me once... You won't take my life twice!"* |
| `victor_bark_garras.ogg` | `Golpe de Garras / QTE` | *"Saia do meu caminho!"* | *"Out of my way!"* |
| `victor_bark_morte.ogg` | `Game Over / HP a 0` | *"Não... Não posso deixar terminar neste chão frio..."* | *"No... I can't let it end on this cold floor..."* |
| `victor_bark_regras.ogg` | `Lembrete das 4 Regras de Sobrevivencia (Victor)` | *"Four rules. That's all that keeps me human."* | *"Four rules. That's all that keeps me human."* |
| `victor_bark_vitoria.ogg` | `Vitoria em Combate (Victor)` | *"Another debt settled. Keep moving."* | *"Another debt settled. Keep moving."* |
| `victor_climax_juramento.ogg` | `Expansion Voice 28` | *"I will not be disposable. Not to the Council, not to the Church, and not to ancient gods."* | — |

### 4.2 Mestra Lility / Lyra von Blut

- **Perfil & Lore:** Vampira ancestral e criadora pré-diluviana disfarçada sob a persona escolar de 'Lyra von Blut'. Vinculada a Victor pelo Grilhão de Sangue.
- **Casting de Voz:** Gemini TTS `Kore` • Fallback `Aoede` • Kokoro `af_bella`
- **Composição do Guarda-Roupa & Sprites:**
  - **Repertório Expressivo (19 Sprites Modernos WebP 92):** `gelida`, `mal_humorada`, `maravilhada`, `melancolica`, `vibrante`, `sorriso_bondoso`, `sorriso_malicioso`, `vergonhosa`, `apreensiva`, `chocada`, `chorando`, `confusa`, `desconfiada`, `desdenhando`, `enojada`, `entediada`, `exausta`, `furiosa`, `olhando_com_confianca`.
  - **Sprites de Gala e Poses Especiais:** Vestido clássico de veludo para piano, poses de intimidade e carinho na cabeça (`lility carinho na cabeca.webp`, `lility sorrindo e com bochechas vermelhas.webp`, `lility com a mao levantada.webp`).

#### 🎙️ Voice Barks & Transcrições Oficiais (`game/audio/voice/lility`)

| Arquivo de Áudio | Gatilho / Contexto Ren'Py | Transcrição Oficial (Português) | Fala em Inglês |
| :--- | :--- | :--- | :--- |
| `lility_bark_ameaca.ogg` | `Dúvida Alta / Alerta` | *"Cuidado com essas garras, Victor. Lembre-se de que ainda sou sua mestra."* | *"Disobey me again, and I'll drain you until your marrow turns to dust."* |
  | `lility_bark_aviso.ogg` | `Entrada no Covil` | *"Ouça-me com muita atenção, Victor... As sombras nestes corredores têm dentes."* | *"Watch your step, fledgling. The shadows in these halls have teeth of their own."* |
| `lility_bark_exposicao.ogg` | `Exposição Crítica (>=60%)` | *"O grilhão está queimando a minha carne, Victor... Pare de agir como uma presa descuidada."* | *"The bond is scorching my flesh, Victor... Stop being such careless prey."* |
| `lility_exposicao_critica_completa.ogg` | `Ameaça do Grilhão Completa` | *"O grilhão de sangue arde como ferro em brasa na minha garganta... Você está deixando rastros desleixados..."* | *"The blood shackle burns like hot iron against my throat, Victor... You are leaving clumsy tracks through these corridors. The Council's hounds and the Church's sentinels have already caught your scent. If you keep prowling like an amateur, I will slit your throat myself to stifle the scandal."* |
| `lility_bark_cachorrinho.ogg` | `Afeto / Provocação` | *"Que adorável... Meu cachorrinho doce querendo ditar as regras."* | *"How utterly adorable, my sweet little puppy wanting to dictate the rules."* |
| `lility_bark_ciume.ogg` | `Ciúme de Outras` | *"Que cheiro vulgar é esse no seu colarinho, Victor?"* | *"Staring at another girl again, pet? Have you forgotten whose collar you wear?"* |
| `lility_bark_crit.ogg` | `Crítico Social` | *"Delicioso... Finalmente alguém que fala a minha língua."* | *"Delicious! Finally, someone who speaks my language."* |
| `lility_bark_deboche.ogg` | `Sedução Inicial` | *"Ora, ora... que olhar faminto, Victor. Você deseja o meu sangue ou o meu favor?"* | *"Well now, what a hungry gaze, Victor. Do you desire my blood or my favour?"* |
| `lility_bark_dentes.ogg` | `Ameaça Predatória` | *"A coleira é de ferro, cachorrinho. Mas os dentes são meus."* | *"The leash is iron, little dog. But the teeth are mine."* |
| `lility_bark_fome_antiga.ogg` | `Condescendência Sedução` | *"Você não me serve porque sou antiga, Victor. Você me serve porque tem fome."* | *"You do not serve me because I am ancient, Victor. You serve me because you are hungry."* |
| `lility_bark_inacabada.ogg` | `Melancolia Régia` | *"A música ficou inacabada."* | *"The music remained unfinished."* |
| `lility_bark_luta.ogg` | `Ordem de Caca Predatoria (Lility)` | *"Show them what the master's blood can do. Tear them apart!"* | *"Show them what the master's blood can do. Tear them apart!"* |
| `lility_bark_pesadelo.ogg` | `Despertar Possessivo apos Pesadelo (Lility)` | *"Wake up, my little bat. You are not allowed to die in your sleep."* | *"Wake up, my little bat. You are not allowed to die in your sleep."* |
| `lility_bark_prazer.ogg` | `Seducao e Transe de Sangue Carnal (Lility)` | *"Ah... Sweet surrender... Let the thirst consume you."* | *"Ah... Sweet surrender... Let the thirst consume you."* |
| `lility_bark_rejeicao.ogg` | `Rejeicao Fria e Dominadora (Lility)` | *"Did you truly think you could defy your blood, Victor? You are mine."* | *"Did you truly think you could defy your blood, Victor? You are mine."* |
| `lility_bark_risada.ogg` | `Risada Padrão` | *"Você realmente achou que conseguiria resistir a mim, morceguinho?"* | *"Did you really think you could resist me, little bat?"* |
| `lility_bark_tedio.ogg` | `Tédio / Ordem` | *"Tão barulhento... Fique em silêncio e sangre por mim."* | *"How utterly boring. Entertain me before I lose my patience."* |
| `lility_bark_transe.ogg` | `Vínculo / Alimentação` | *"Isso... Aproxime-se e beba devagar..."* | *"Drink deep, my sweet thrall. Surrender your thoughts to the crimson velvet."* |
| `lility_bark_vergonha.ogg` | `Flerte / Acordando` | *"O-Ora, seu garoto insolente! Eu não estava dormindo!"* | *"W-Why, you insolent boy! I wasn't sleeping!"* |
| `lility_risada_deboche.ogg` | `Vitória / Deboche` | *"Achou mesmo que resistiria a mim, morceguinho? Fufufu..."* | *"Did you really think you could resist me, little bat? Fufufu..."* |
| `lility_risada_ronronar.ogg` | `Intimidade / Carinho` | *"Você é tão adorável quando se esforça tanto... Venha mais perto..."* | *"You are so adorable when you try this hard. Come closer..."* |
| `lyra_bark_genealogia.ogg` | `` | *"Lyra von Blut... Um título vulgar para tempos vulgares, Victor. A fidalga menor da Silésia com dote atrasado... O sangue nestas veias conquistava reinos antes desta escola ter uma única pedra."* | *"Von Blut...? A vulgar alias for vulgar times, Victor... The blood in these veins was conquering kingdoms before this school laid a single stone."* |
| `lility_bark_elara_desdem.ogg` | `Desdém a Elara / Grêmio` | *"Preocupado com o Conselho Estudantil? Deixe aquele cão latir de seu castelo de mármore..."* | *"Worried about the Student Council? Let that white-uniformed hound bark from her marble castle... We have far larger storms coming before the Eclipse."* |
| `lility_bark_grilhao_dor.ogg` | `Dano no Grilhão de Sangue` | *"Nngh...! Olhe por onde pisa, Victor... Cada erro que você comete queima na minha clavícula."* | *"Nngh...! Watch your step out there, Victor... Every clumsy mistake you make burns straight through my collarbone."* |
| `lility_bark_faro_gremio.ogg` | `Faro Cruzado (Sangue Grêmio)` | *"Hmm... Você bebeu de um dos cães de sangue de Elara? Que adorável má educação, cachorrinho."* | *"Hmm... You drank from one of Elara's precious little bloodhounds? How delightfully bad-mannered of you, my puppy."* |
| `lility_bark_faro_clero.ogg` | `Faro Cruzado (Sangue Clero)` | *"Ugh... Incenso e prata nas suas veias? Pare de beber daquela garota exorcista antes que nos envenene."* | *"Ugh... Incense and silver in your veins? Stop drinking from that exorcist girl before you poison us both."* |
| `lility_bark_toque_orelha.ogg` | `Touch Mode (Orelha / Cabelo)` | *"Hmph... Suas mãos humanas são quentes demais para as minhas orelhas, Victor. Não pare agora..."* | *"Hmph... Your human hands are far too warm for my ears, Victor. Don't stop now... or I might bite."* |
| `lility_bark_toque_broche.ogg` | `Touch Mode (Peito / Broche)` | *"Dedos atrevidos... Está verificando se meu coração ainda bate ou cansou de ter dez dedos?"* | *"Bold fingers... Are you checking if my heart still beats, or just tired of having all ten of yours?"* |
| `lility_bark_duelo_falha.ogg` | `Falha em Diálogo / Duelo` | *"Poupe-me das desculpas mortais trêmulas, lacaio. Não o tirei da tumba para ouvi-lo choramingar."* | *"Spare me the trembling mortal excuses, lackey. I did not pull you from the grave to listen to you whimper."* |
| `lility_bark_fome_critica.ogg` | `Fome Crítica (<20%)` | *"Olhe para você tremendo feito um vira-lata faminto... Venha aqui e ajoelhe-se."* | *"Look at you shaking like a starved stray... Come here and kneel, before you embarrass yourself in the hallways."* |
| `lility_bark_noite_fora.ogg` | `Contemplação nos Portões` | *"Logo além destes portões de ferro, uma cidade inteira dorme em ignorância..."* | *"Just beyond these iron gates, an entire city sleeps in ignorance... Enjoy the quiet while the barrier still holds."* |
| `lility_bark_afeto_alto.ogg` | `Visita de Alto Afeto (8+)` | *"Você sempre retorna a este quarto empoeirado, mesmo sem nada a ganhar... Uma verdadeira anomalia."* | *"You always return to this dusty room, even when you have nothing left to gain... You truly are an anomaly, Victor."* |
| `lility_bark_cain_eco.ogg` | `Eco do Despertar de Cain` | *"O ritmo ancestral sob a fundação está respondendo ao seu pulso... Cuidado para não acordá-lo."* | *"The ancient rhythm beneath the foundation is answering your pulse... Be careful not to wake it too soon."* |
| `lility_climax_06_mortal.ogg` | `Final C (Perda da Imortalidade)` | *"Que ruído é esse batendo no meu peito...?! Sinto o ar gelado... Você roubou minha morte!"* | *"What is this noise pounding inside my chest...?! I feel the cold air on my skin... Victor, you cruel, selfish boy... you stole my death from me."* |

### 4.3 Presidente Elara von Weiss

- **Perfil & Lore:** Presidente do Grêmio Estudantil (21 anos). Nobre herdeira da dinastia fundadora, guardiã austera da Máscara institucional e da disciplina de sangue.
- **Casting de Voz:** Gemini TTS `Aoede` • Kokoro `af_sarah`
- **Composição do Guarda-Roupa & Sprites:**
  - **Repertório de Uniforme Oficial:** `uniforme arrogante`, `uniforme observando`, `uniforme serena`, `uniforme seria`, `encarando neutra`, `irritada e com desprezo`.
  - **Novos Sprites de Vulnerabilidade e Duelo:** `elara ativando grilhao de sangue e encarando.webp`, `elara apos ativar grilhao do sangue.webp`, `elara envergonhada afastado.webp`, `elara meio corpo com vergonha olhando pro lado.webp`.

#### 🎙️ Voice Barks & Transcrições Oficiais (`game/audio/voice/elara`)

| Arquivo de Áudio | Gatilho / Contexto Ren'Py | Transcrição Oficial (Português) | Fala em Inglês |
| :--- | :--- | :--- | :--- |
| `elara_bark_alerta.ogg` | `Alerta de Segurança do Grêmio` | *"Mantenha a guarda! Há uma quebra grave de protocolo nestas imediações."* | *"Keep your guard up! There is a severe protocol breach in these premises."* |
| `elara_bark_exposicao.ogg` | `Exposição Crítica (>=60%)` | *"Bolsista Vane. Sua imprudência ultrapassou qualquer limite aceitável."* | *"Scholarship boy Vane. Your recklessness has exceeded all permissible bounds."* |
| `elara_exposicao_critica_completa.ogg` | `Ordem de Expurgo Completa` | *"Bolsista Vane. A exposição das suas escapadas noturnas cruzou qualquer linha tolerável... Esta academia não abrigará um lacaio descuidado..."* | *"Scholarship boy Vane. The exposure of your nocturnal escapades has crossed every tolerable line. The avenue police patrols and Council inspectors have crossed paths with your description twice tonight. This academy will not shelter a sloppy lackey. Erase your tracks immediately, or my next decree will be your order of purge."* |
| `elara_bark_aprovacao.ogg` | `Acordo Político` | *"Raciocínio frio e eficiente. Muito bem."* | *"Cold and efficient reasoning. Very well."* |
| `elara_bark_chamado.ogg` | `Entrada Gabinete` | *"Bolsista Vane. Espero que não esteja desperdiçando o tempo do Grêmio Estudantil."* | *"Scholar Vane, I trust you are not wasting the Student Council's time."* |
| `elara_bark_ciume.ogg` | `Suspeita / Ciúme` | *"Você andou rastejando pelas caldeiras ou rezando na capela, Victor?"* | *"Have you been crawling in the boilers, or praying in the chapel, Victor?"* |
| `elara_bark_corada.ogg` | `Intimidade Inesperada` | *"N-Não me toque dessa maneira diante dos retratos do Conselho..."* | *"D-Do not touch me like that in front of the Council portraits..."* |
| `elara_bark_data_point.ogg` | `Frieza Burocrática` | *"Isso é um dado, Victor. Não um sentimento."* | *"That is a data point, Victor. Not a feeling."* |
| `elara_bark_derrota.ogg` | `Derrota Orgulhosa (Elara)` | *"Tsk... The Council will not forget this insolence... Not ever."* | *"Tsk... The Council will not forget this insolence... Not ever."* |
| `elara_bark_desprezo.ogg` | `Quebra de Ordem` | *"Patético. Você realmente acreditava que estava no controle?"* | *"Pathetic. Did you truly believe you were the one in control?"* |
| `elara_bark_dor.ogg` | `Reacao de Dor e Odio em Combate (Elara)` | *"Ugh...! Incompetent dog, you will pay dearly for that!"* | *"Ugh...! Incompetent dog, you will pay dearly for that!"* |
| `elara_bark_hesitacao.ogg` | `Hesitacao e Conflito Pessoal (Elara)` | *"Victor... Do not force my hand. I don't want to sign your execution."* | *"Victor... Do not force my hand. I don't want to sign your execution."* |
| `elara_bark_liability.ogg` | `Advertência Institucional` | *"Sua bolsa de estudos foi um investimento, Vane. Não a transforme em um passivo."* | *"Your scholarship was an investment, Vane. Do not turn it into a liability."* |
| `elara_bark_ordem.ogg` | `Grilhão de Sangue` | *"O Grilhão de Sangue vai lhe ensinar o seu lugar. Ajoelhe-se!"* | *"The Blood Shackle will teach you your place. Kneel!"* |
| `elara_bark_registered.ogg` | `Despacho Formal` | *"Registrado. Não me faça repetir o regulamento."* | *"Registered. Do not make me repeat the regulation."* |
| `elara_bark_risada.ogg` | `Risada Aristocrática` | *"Que pitoresco. Você realmente acreditava que tinha escolha aqui?"* | *"How quaint. Did you truly believe you had a choice here?"* |
| `elara_bark_someone_pays.ogg` | `Decisão Utilitária` | *"Alguém sempre paga. A única escolha é quem."* | *"Someone always pays. The only choice is who."* |
| `elara_bark_transe.ogg` | `Intimidade / Sangue` | *"Tranque a porta... Dois dedos abaixo da clavícula."* | *"Lock the door. Two fingers below the collarbone."* |
| `elara_risada_desprezo.ogg` | `Punição / Duelo` | *"Que ingênuo. Acreditava mesmo ter escolha aqui? Hmph."* | *"How quaint. Did you truly believe you had a choice here? Hmph."* |
| `elara_risada_divertida.ogg` | `Flerte Intelectual` | *"Você me diverte, Victor. Mas não confunda minha diversão com fraqueza."* | *"You amuse me, Victor. But do not mistake my amusement for weakness."* |
| `elara_bark_sangue_clero.ogg` | `Faro Cruzado (Sangue Clero)` | *"Incenso e sebo de igreja nas suas roupas...? Continue se ajoelhando para aquela noviça e o Conselho o marcará."* | *"I smell consecrated silver in your pulse, Vane. Drinking from the Church's bloodline is a slow poison—even for a mongrel."* |
| `elara_bark_canibalismo.ogg` | `Faro Cruzado (Sangue do Conselho)` | *"Você... você se alimentou de um membro do Conselho Estudantil?! Seu carniceiro desprezível..."* | *"Feasting on Council blood in the dark? Lility clearly failed to teach her stray dog basic civilized manners."* |
| `elara_bark_relatorio_ok.ogg` | `Relatório Aprovado / Tarefa` | *"Relatório aceito, Vane. Limpo, ordeiro e sem desculpas sentimentais. É assim que mantém o pescoço intacto."* | *"Acceptable work, scholarship boy. Keep the perimeter clean, and the Council may yet tolerate your existence."* |
| `elara_bark_submundo.ogg` | `Alerta de Contrabando` | *"Vapor de caldeira e contrabando barato...? Continue rastejando no subsolo e meus executores o arrastarão."* | *"The boilers exist to contain stray rats, not to arm them. Do not test the limits of my patience, Mister Vane."* |
| `elara_bark_barreira_falha.ogg` | `Pulso do DOOM / Barreira` | *"A barreira de contenção oscilou mais duas vezes nesta noite. Tranque a porta do seu dormitório."* | *"The foundation seals are fracturing faster than projected... Leave my sight, I have decrees to sign."* |
| `elara_bark_toque_bracadeira.ogg` | `Touch Mode (Braçadeira do Grêmio)` | *"Tire a mão da minha braçadeira oficial, bolsista. Você não tem jurisdição para encostar nesta insígnia."* | *"Do you have any idea what happens to lesser creatures who soil the white uniform of the Student Council? Step back."* |
| `elara_bark_toque_submissa.ogg` | `Touch Mode Subjugada` | *"N-Não me toque com essa liberdade no gabinete... Se os executores virem isso, a disciplina desmorona."* | *"Do not look at me with those triumphant eyes... If any executor walks through that door and sees me like this..."* |
| `elara_bark_combate_foice.ogg` | `Ataque com Foice em Batalha` | *"Pela autoridade da Reitoria e do Conselho Estudantil... sua sentença foi assinada!"* | *"The Mask is absolute! If you cannot control your hunger, I will grant you the mercy of the void myself!"* |
| `elara_bark_derrota_luta.ogg` | `Derrota na Arena de Batalha` | *"N-Não... Como um lacaio de uniforme preto conseguiu quebrar a minha postura...?!"* | *"Impossible... A mere ghoul breaking through centuries of pure blood... What exactly did Lility awaken in you?"* |
| `elara_bark_alianca.ogg` | `Aliança Institucional` | *"A partir desta noite, Victor, você não é apenas um monitor. Meus executores respondem ao seu comando."* | *"Everyone in this academy wants me to be an unbreakable statue of ivory... You are the first to see the weight of the crown."* |
| `elara_bark_nora_desvio.ogg` | `Conspiração Nora Vance` | *"O prontuário dos sujeitos de teste está selado por decreto. Continue perguntando sobre Nora e dividirá a ala com ela."* | *"Subject Thirty-One is contained beneath the crypt for the safety of the campus. Drop this inquiry immediately."* |
| `elara_climax_04_trono.ogg` | `Final F (Comandante dos Executores)` | *"Um acordo selado em ferro e sangue, Victor. A partir desta noite você é o Comandante dos meus Executores."* | *"If the old world must burn tonight, Victor Vane... then we shall rewrite the laws of the blood together, side by side."* |

### 4.4 Emília von Karsten

- **Perfil & Lore:** Nobre fidalga e noviça da Capela da Academia (20 anos). Dividida entre sua devoção religiosa, a cruz de prata da família e a culpa por acolher Victor.
- **Casting de Voz:** Gemini TTS `Leda` • Kokoro `af_nicole`
- **Composição do Guarda-Roupa & Sprites:**
  - **Repertório Sagrado & Investigativo:** `uniforme calma`, `uniforme seria investigativa`, `uniforme seria triste`, `uniforme ajeitando oculos`, `uniforme corada`.
  - **Novos Sprites Íntimos & Toque:** `emilia com vergonha segurando a cruz.webp`, `emilia fofa toque no rosto.webp`.

#### 🎙️ Voice Barks & Transcrições Oficiais (`game/audio/voice/emilia`)

| Arquivo de Áudio | Gatilho / Contexto Ren'Py | Transcrição Oficial (Português) | Fala em Inglês |
| :--- | :--- | :--- | :--- |
| `emilia_bark_alerta.ogg` | `Perigo Sobrenatural` | *"Fique atrás de mim, Victor! Há algo nas sombras!"* | *"Stay behind me, Victor! There is something in the shadows!"* |
| `emilia_bark_exposicao.ogg` | `Exposição Crítica (>=60%)` | *"Victor, por favor... dê um passo para trás! Os sentinelas do meu pai estão revistando cada corredor!"* | *"Victor, please... step back! My father's sentinels are searching every corridor!"* |
| `emilia_exposicao_critica_completa.ogg` | `Alerta Inquisitorial Completo` | *"Victor... por favor, mantenha distância agora. Patrulhas do Grêmio e sentinelas da ordem do meu pai estão inspecionando cada corredor..."* | *"Victor... please, keep your distance right now. Council patrols and sentinels from my father's order are inspecting every corridor. Your name is already circulating in the disciplinary dispatches... If they catch us alone together, not even my family's cross will shield you from the pyre."* |
| `emilia_bark_chamado.ogg` | `Entrada Biblioteca` | *"Ah, Victor! Você veio até a biblioteca só para me ver?"* | *"Ah, Victor! Did you come all the way to the library to see me?"* |
| `emilia_bark_consolo.ogg` | `Consolo e Protecao Espiritual (Emilia)` | *"It's alright, Victor... I won't let the darkness take you."* | *"It's alright, Victor... I won't let the darkness take you."* |
| `emilia_bark_crit.ogg` | `Confiança Máxima` | *"Obrigada por não mentir para mim, Victor."* | *"Thank you for not lying to me, Victor."* |
| `emilia_bark_cura.ogg` | `Curativo / Bênção` | *"Que a luz purifique suas feridas. Segure firme, Victor."* | *"May the light cleanse your wounds. Hold on tight, Victor."* |
| `emilia_bark_dor.ogg` | `Dano Recebido em Combate` | *"Ugh...! Pelos santos... A luz há de me sustentar!"* | *"Ugh...! By the saints... The light shall sustain me!"* |
| `emilia_bark_lagrima.ogg` | `Apelo Emocional a Beira do Frenesi (Emilia)` | *"Victor, please... look at me, don't let the hunger win..."* | *"Victor, please... look at me, don't let the hunger win..."* |
| `emilia_bark_oracao.ogg` | `Resolução Trágica` | *"Uma oração não é um escudo. É um lembrete do que sangra."* | *"A prayer is not a shield. It is a reminder of what bleeds."* |
| `emilia_bark_pacto.ogg` | `Comunhão / Sangue` | *"Ahn... P-Pelos céus... Por favor, vá devagar..."* | *"Ahn... B-By the heavens... Please, go slowly..."* |
| `emilia_bark_po_nas_maos.ogg` | `Suspeita Sagrada` | *"Posso sentir o cheiro da poeira das catacumbas em suas mãos, Victor."* | *"I can smell the dust of the catacombs on your hands, Victor."* |
| `emilia_bark_prata.ogg` | `Toque no Crucifixo` | *"Céus sagrados! Você acabou de queimar os dedos na minha cruz de prata?!"* | *"Good heavens, did you just burn your fingers on my silver cross?!"* |
| `emilia_bark_reza.ogg` | `Oracao em Latim Sussurrada (Emilia)` | *"Sancta Maria, mater Dei... dona nobis pacem..."* | *"Sancta Maria, mater Dei... dona nobis pacem..."* |
| `emilia_bark_risada.ogg` | `Risada Tímida` | *"Por favor, não olhe assim pra mim! Meu coração está disparado..."* | *"Please don't look at me like that! My heart is racing..."* |
| `emilia_bark_suspeita.ogg` | `Cheiro de Sangue` | *"Victor... Por que há sangue no seu colarinho?"* | *"Victor... Why is there blood on your collar?"* |
| `emilia_bark_timida.ogg` | `Proximidade Física` | *"Espere, Victor! Não fique tão perto... Minhas orações não vão me proteger disso..."* | *"Wait, Victor! Please don't be so close... My prayers won't protect me from this..."* |
| `emilia_bark_votos.ogg` | `Vulnerabilidade & Dor` | *"Não me faça escolher entre meus votos e a sua vida."* | *"Do not make me choose between my vows and your life."* |
| `emilia_risada_alivio.ogg` | `Alívio Cômico` | *"Ai, hihi! Graças a Deus! Por um segundo achei que fosse desmaiar!"* | *"Oh, tee-hee! Thank goodness! For a second I thought I was gonna faint!"* |
| `emilia_risada_timida.ogg` | `Momento Romântico` | *"Por favor, não me encare assim... Meu coração está acelerado..."* | *"Please don't look at me like that... My heart is racing..."* |
| `emilia_bark_manha_cansada.ogg` | `Saudação Matinal Cansada` | *"Bom dia, Victor... Você parece tão pálido. As sombras o mantiveram acordado a noite toda de novo?"* | *"Good morning, Victor... Sorry, I was up late researching those old disappearance files again."* |
| `emilia_bark_fase2_pena.ogg` | `Reação à Degradação Humana` | *"Victor... seus olhos... Não deixe a sede devorar o rapaz gentil que me ajudou na capela..."* | *"You look pale as a ghost, Victor... Please promise me you'll rest in your dorm tonight instead of wandering the halls."* |
| `emilia_bark_duvida_alta.ogg` | `Dúvida Alta (>=4)` | *"Não dê mais nenhum passo, Victor. O cheiro de cinzas e mentiras que você carrega... é insuportável."* | *"Strange... The cold air follows you everywhere lately, Victor. Tell me the truth—what are you hiding?"* |
| `emilia_bark_cacada_inicio.ogg` | `Início de Caçada / Ronda` | *"Mantenha a cruz por perto e o passo em silêncio... O que dorme sob este cemitério está ouvindo."* | *"Keep the consecrated chalk inside the circle and stay close to my light. Whatever lurks in this mist won't take another student."* |
| `emilia_bark_cacada_vitoria.ogg` | `Purificação Concluída` | *"Graças aos santos... A luz sagrada ainda encontra brechas para queimar mesmo no abismo mais escuro."* | *"We actually survived that... Thank you, Victor. I couldn't have held the line alone."* |
| `emilia_bark_toque_oculos.ogg` | `Touch Mode (Ajuste dos Óculos)` | *"A armação de prata entortou de novo...? Não fique tão perto, Victor... Me desconcentra."* | *"Oh! My glasses almost slipped... You really shouldn't lean in so suddenly, Victor, my heart is racing..."* |
| `emilia_bark_toque_mao.ogg` | `Touch Mode (Mãos / Rosário)` | *"Seus dedos estão tremendo contra as contas do rosário... Se procura perdão, Victor... estou ouvindo."* | *"Your hands are cold, but... I'm glad you're here with me. We'll find a way out of this nightmare together."* |
| `emilia_bark_faro_profano.ogg` | `Faro Cruzado (Contaminação)` | *"Há algo profano e podre no seu cheiro... Onde você esteve rastejando, Victor?!"* | *"Wait... My silver cross just turned ice cold. Have you been near the forbidden music wing, Victor?"* |
| `emilia_bark_phillip_conflito.ogg` | `Conflito com Lorde Phillip` | *"Os sentinelas do meu pai não veem estudantes... veem lenha para a fogueira. Deixe-me ajudá-lo antes que o alcancem."* | *"My father sees only monsters in the dark... but I know there is still a human soul fighting inside you!"* |
| `emilia_bark_cacadora_hostil.ogg` | `Desafio aos Inquisidores` | *"Fiz um juramento de curar, não de degolar! Ponha um dedo nele e verá como os von Karsten purgam hereges!"* | *"I prayed I was wrong about you, Victor... Forgive me, but I cannot let a predator walk these halls anymore."* |
| `emilia_bark_ritual_corte.ogg` | `Ritual do Corte (Final B)` | *"As runas de vinculação estão quebrando... Corte o fio, Victor! Não deixe a dor dela arrastá-lo para a cova!"* | *"These pages describe a way to sever a primordial blood bond... Hold on a little longer, Victor. There is still hope."* |
| `emilia_climax_02_lamento.ogg` | `Final C (Abraço Profano)` | *"O que... o que você fez comigo, Victor...?! Eu sou um demônio... Por que roubou o meu céu...?!"* | *"Victor... it's so dark... Why did you give me your blood...? My eyes... why do I suddenly crave the sound of your heartbeat?"* |

### 4.5 Valéria das Caldeiras (Mercado Negro)

- **Perfil & Lore:** Contrabandista e operadora do Mercado Negro no subsolo (21 anos). Especialista em bolsas de sangue filtradas, absinto esmeralda e armas modificadas.
- **Casting de Voz:** Gemini TTS `Zephyr` • Kokoro `af_sky`
- **Composição do Guarda-Roupa & Sprites:**
  - **Repertório Mercantil & Casaco de Pele:** `seria mochila frascos`, `provocando sorriso`, `sorriso cinico`, `transe surpresa`.
  - **Novos Sprites de Expressões & Reação (15 Sprites Integrados):** `afastando e ativando armadilha`, `cobrando toque`, `determinada`, `entediada cansada`, `exausta`, `irritada`, `mal humorada`, `maquiavelica`, `melancolica`, `preocupada`, `sorriso de pura felicidade`, `vergonha`, `confusa`, `desconfiada`, `desprezando`.

#### 🎙️ Voice Barks & Transcrições Oficiais (`game/audio/voice/valeria`)

| Arquivo de Áudio | Gatilho / Contexto Ren'Py | Transcrição Oficial (Português) | Fala em Inglês |
| :--- | :--- | :--- | :--- |
| `valeria_bark_armadilha.ogg` | `Dívida Pendente` | *"Haha! Achou mesmo que conseguiria fiado aqui embaixo?"* | *"Haha! Did you really think you'd get anything on credit down here?"* |
| `valeria_bark_exposicao.ogg` | `Exposição Crítica (>=60%)` | *"Ei, parceiro... você tá brilhando feito brasa viva. Recua antes que você traga a lei aqui pra baixo!"* | *"Hey, partner... you're glowing like an open flame. Back off before you bring the law down here!"* |
| `valeria_exposicao_critica_completa.ogg` | `Taxa de Risco Completa` | *"Ei, garoto da bolsa... você tá queimando quente o suficiente pra fritar um ovo. A patrulha da avenida tá batendo lanterna nos dutos... Se trouxer a polícia pro meu covil, eu triplico o preço de tudo..."* | *"Hey, scholarship kid... you're burning hot enough to fry an egg. The avenue patrol's got flashlights rattling through my boiler vents because of you. If you bring captains and bloodhounds into my contraband den, I'm tripling the price on every single vial just to cover the hazard fee. Cool your heat before you blow our cover."* |
| `valeria_bark_bloqueio.ogg` | `Sem Dinheiro` | *"Sem grana na mão, sem conversa no balcão. Circulando."* | *"No cash in hand, no talk at the counter. Move along."* |
| `valeria_bark_crit.ogg` | `Negociação Perfeita` | *"Gostei disso. Um negociante com coragem é raro por aqui."* | *"I like that. A dealer with a backbone is rare around here."* |
| `valeria_bark_dor.ogg` | `Reacao de Dor Aspera em Luta (Valeria)` | *"Tch! Bastard got lucky...!"* | *"Tch! Bastard got lucky...!"* |
| `valeria_bark_negocios.ogg` | `Entrada Caldeiras` | *"E aí, sangue frio. Veio quitar sua dívida ou tá atrás de mais crédito?"* | *"Hey there, cold blood. You here to settle your debt or looking for more credit?"* |
| `valeria_bark_price_not_value.ogg` | `Provocação Pragmática` | *"Isso é um preço, Vane. Não um valor."* | *"That is a price, Vane. Not a value."* |
| `valeria_bark_provocacao.ogg` | `Provocacao Sarcastica (Valeria)` | *"Is that all you got, scholar boy? I've seen rusty pipes hit harder!"* | *"Is that all you got, scholar boy? I've seen rusty pipes hit harder!"* |
| `valeria_bark_risada.ogg` | `Risada Cínica` | *"Olha só pra você. Sobreviver aqui tem um preço, mas você não tem preço."* | *"Look at you. Survival in these halls has a price, but you're priceless."* |
| `valeria_bark_safra.ogg` | `Tráfico de Sangue` | *"Puxe o portão dos fundos e não deixe marcas no meu pescoço."* | *"Pull the back gate shut and don't leave a mark on my neck."* |
| `valeria_bark_segredo.ogg` | `Sussurro Cumplice de Mercado Negro (Valeria)` | *"Keep this between us, or the boilers won't be your only problem."* | *"Keep this between us, or the boilers won't be your only problem."* |
| `valeria_bark_toque.ogg` | `Toque na Jaqueta` | *"Tira a mão da jaqueta, garoto. Quer faísca na cara ou o quê?"* | *"Hands off the jacket, kid. You looking for sparks in your face or what?"* |
| `valeria_bark_transe.ogg` | `Mordida Intensa` | *"Nngh... Droga, Vane! Essa mordida foi mais funda do que combinamos!"* | *"Nngh, dammit Vane, that bite was deeper than we agreed!"* |
| `valeria_bark_tres_goles.ogg` | `Limite Tenso na Fornalha` | *"Três goles, Vane. O quarto custa seus dedos."* | *"Three sips, Vane. The fourth costs your fingers."* |
| `valeria_bark_vitoria.ogg` | `Vitoria em Negocios Clandestinos (Valeria)` | *"Ha! Cash in hand, blood in the bag. Clean business."* | *"Ha! Cash in hand, blood in the bag. Clean business."* |
| `valeria_bark_who_pays.ogg` | `Ceticismo Comercial` | *"Quem vai pagar por isso?"* | *"Who is paying for that?"* |
| `valeria_risada_cinica.ogg` | `Deboche nas Caldeiras` | *"Pfft! Haha! Sobreviver aqui custa caro, mas você é uma comédia."* | *"Pfft! Haha! Survival in these halls has a price, but you're priceless."* |
| `valeria_risada_estalo.ogg` | `Elogio Ácido` | *"Você tem culhões mesmo, saco de sangue! Tenho que admitir."* | *"You really got guts, blood bag! I'll give you that much."* |
| `valeria_bark_saudacao_01.ogg` | `Saudação Mercado Negro` | *"E aí, cliente VIP. Se veio atrás de bolsas filtradas ou fofocas da ronda, o balcão tá aberto."* | *"Lost your way down here, new kid? Look around—everything in the boilers has a price tag, and I don't do charity."* |
| `valeria_bark_saudacao_02.ogg` | `Saudação Conspiratória Noturna` | *"Entra logo e encosta a porta de ferro. O ar lá em cima tá cheio de cães farejadores esta noite."* | *"Back again, partner? Keep flashing cash like that and you'll be my favorite customer before the Eclipse hits."* |
| `valeria_bark_negocios.ogg` | `Compra Cara Concluída` | *"Dinheiro na mão, caldeira funcionando. Adoro fazer negócios com quem não chora desconto."* | *"Pleasure doing business with you, lackey. No refunds, no questions asked."* |
| `valeria_bark_sem_dinheiro.ogg` | `Tentativa Sem Saldo` | *"Ei, parceiro... você tá liso feito um sapão. Sem grana na mesa, a vitrine fica fechada."* | *"Empty pockets? Come back when your wallet matches your attitude, rookie. Nothing in this basement runs on credit."* |
| `valeria_bark_confronto_ghoul.ogg` | `Encontro de Túneis / Ghouls` | *"Eles tão vindo pelos tubos de vapor! Mira nos joelhos, Vane, não desperdiça cartucho!"* | *"Easy there, fangs. Nothing personal—she paid for blood, I delivered. Not my fault the basement air soured the batch."* |
| `valeria_bark_lote_contaminado.ogg` | `Alerta de Lote Raro Contaminado` | *"Algo antigo tá vazando da fundação para o meu suprimento... Se o Conselho souber, estamos mortos."* | *"Something ancient is bleeding through the foundation into my supply... If the Council finds out, we're both dead."* |
| `valeria_bark_fada_verde.ogg` | `Bar da Fada Verde` | *"Um trago da Fada Verde e as paredes começam a responder, Vane. Vê se não perde o juízo."* | *"One sip of the Green Fairy and the walls start talking back, Vane. Try not to lose your mind in the neon."* |
| `valeria_bark_toque_cabelo.ogg` | `Touch Mode (Cabelo / Provocação)` | *"Ei, mãos longe do cabelo! Vinte pratas por minuto se quiser passar a mão."* | *"Hey, hands off the hair! I'm not some stray puppy you get to pet for free—twenty bucks a minute if you wanna touch."* |
| `valeria_bark_toque_taxa.ogg` | `Touch Mode (Pedágio no Corpo)` | *"Cinquentinha direto do seu bolso. Continua deixando a mão passear que compro o Grêmio até sexta."* | *"Fifty straight out of your pocket. Keep letting your hands wander and I'll buy out the Student Council by Friday."* |
| `valeria_bark_toque_choque.ogg` | `Touch Mode (Tentativa de Furto)` | *"Hah! Tentando bater a carteira da maior contrabandista desta escola? Tomou choque, amador!"* | *"Hah! Did you seriously try to pickpocket the biggest smuggler in this school? Touching my stash bites back, amateur!"* |
| `valeria_bark_toque_submissa.ogg` | `Touch Mode Submissão Íntima` | *"Tch... Não na frente do balcão aberto, seu idiota... Espera trancar a porta de ferro se quiser o resto."* | *"Tch... Not in front of the open counter, you idiot... Wait till I bolt the iron door if you want to collect the rest."* |
| `valeria_bark_faro_ousadia.ogg` | `Faro Cruzado (Adrenalina / Rua)` | *"Ora, ora... Você tá cheirando a adrenalina de rua e encrenca esta noite. Criando dentes de verdade."* | *"Well, well... You smell like street adrenaline and trouble tonight. Finally growing some real teeth, partner."* |
| `valeria_bark_duelo_crit.ogg` | `Crítico em Negociação / Duelo` | *"Agora você tá falando a minha língua! Danem-se os discursos nobres—siga a grana e saímos vivos."* | *"Now you're speaking my language! Screw the noble speeches—follow the money and we walk out of here alive."* |
| `valeria_bark_duelo_falha.ogg` | `Falha em Duelo Social` | *"Ugh, me poupa do sermãozinho santo. Guarda essa rotina de coroinha pra Emília, me dá azia."* | *"Ugh, spare me the saintly lecture. Save that choir-boy routine for Emilia, it makes me sick."* |
| `valeria_bark_monopolio_virada.ogg` | `Marco I (Exigência de Sócio)` | *"Recusando minha grana...? Você joga perigoso, Victor Vane. Dita os seus termos se der conta de mim."* | *"Refusing my cash...? You're playing a dangerous game, Victor Vane. Fine—name your terms, if you think you can handle me."* |
| `valeria_climax_05_alianca.ogg` | `Final D (A Última Transação)` | *"Não vai morrer agora, lacaio! Você é meu maior investimento nesta cidade podre—e eu protejo meus ativos!"* | *"Don't go dying on me now, lackey! You're my biggest investment in this rotten city—and I always protect my assets!"* |

---

## 👤 5. Personagens Secundários, Chefes & Clímax

### 5.1 Nora Vasques (Cobaia #31 / Ghoul Rival)

- **Papel no Jogo:** Aluna transferida que enlouqueceu na noite do Dia 1 sob abstinência de sangue contaminado. Confinada nas Criptas mais profundas.
- **Sprites Disponíveis:** 3 arquivos: `nora neutra.webp`, `nora atacando descontrolada.webp`, `nora atacando descontrolada e frenesi.webp`.
- **Falas Vocais & Transcrições Oficiais:**

| Arquivo (.ogg) | Transcrição Oficial (Português) | Fala em Inglês |
| :--- | :--- | :--- |
| `nora_carteira_vazia.ogg` | *"Meu nome estava no livro antes de apagarem... Trinta e Um! Eu sou a Paciente Trinta e Um!"* | *"My name was in the book before they erased it... Thirty-One! I am Patient Thirty-One!"* |
| `nora_climax_01_caneta.ogg` | *"Tem uma caneta sobrando? A minha secou e eu preciso terminar isto antes que... antes que ele chegue."* | *"Do you have a spare pen? Mine dried up, and I need to finish this before... before he arrives."* |
| `nora_climax_02_parede.ogg` | *"A parede está batendo! Você não ouve?! Tum, tum! Ela pede sangue limpo, e eu paguei por ele! Cale esse coração barulhento!"* | *"The wall is beating! Don't you hear it?! Thump, thump! It demands clean blood, and I paid for it! Shut that noisy heart up!"* |
| `nora_climax_03_cela_cripta.ogg` | *"...V-Victor...? É você...? O bolsista... do primeiro dia..."* | *"Victor...? Is it you...? The scholarship boy from the first day..."* |
| `nora_bark_aviso_cain.ogg` | *"O Grêmio... Elara e os executores de casaco branco... Eles me trouxeram para cá..."* | *"The Council... Elara and the white-coated enforcers... They brought me down here..."* |
| `nora_bark_loucura.ogg` | *"Cale a boca! Silencie esse coração barulhento! As paredes estão com sede!"* | *"Shut up! Please just shut up! Silence that noisy heart! The walls are thirsty!"* |
| `nora_bark_dor.ogg` | *"Argh...! A lâmina... corta as vozes...!"* | *"Argh...! The blade... it cuts through the voices...!"* |
| `nora_bark_risada.ogg` | *"Hahaha! O sangue dourado... nós vamos bebê-lo juntos nas trevas!"* | *"Hahaha! The golden blood... we shall drink it together in the dark!"* |

### 5.2 Cain (O Progenitor Ancestral)

- **Papel no Jogo:** Entidade antediluviana adormecida nas fundações de São Cipriano. Desperta quando a Ruína (DOOM) atinge 100%.
- **Sprites Disponíveis:** 5 arquivos em `game/images/cain/corpo inteiro/`: `cain agachado.webp`, `cain ameaca flutuando.webp`, `cain combate pose.webp`, `cain neutro espada.webp`.
- **Falas Vocais & Transcrições Oficiais:**

| Arquivo (.ogg) | Transcrição Oficial (Português) | Fala em Inglês |
| :--- | :--- | :--- |
| `cain_bark_desafio.ogg` | *"Mais um vira-lata em coleira nova? Mostre-me suas presas, garoto!"* | *"Another mutt on a fresh leash? Show me your fangs, boy!"* |
| `cain_climax_01_despertar.ogg` | *"A terra treme... O Progenitor reclama o seu tributo de vitae milenar!"* | *"The earth trembles... The Progenitor claims his tribute of ancient vitae!"* |
| `victor_despertar_cain.ogg` | *"As rachaduras no solo sangram luz carmesim. Ele abriu os olhos sob a terra... O Progenitor despertou."* | *"The cracks in the earth bleed crimson light. He opened his eyes beneath the ground... The Progenitor is awake."* |

### 5.3 Lorde Phillip von Karsten

- **Papel no Jogo:** Grão-Inquisidor e patriarca da Casa von Karsten, pai de Emília. Chega à escola no Dia 17 com sentinelas blindadas.
- **Sprites Disponíveis:** 5 arquivos em `game/images/Phillip/corpo inteiro/`: `phillip combate guarda.webp`, `phillip derrota.webp`, `phillip neutro espada.webp`, `phillip pensativo espada.webp`.
- **Falas Vocais & Transcrições Oficiais:**

| Arquivo (.ogg) | Transcrição Oficial (Português) | Fala em Inglês |
| :--- | :--- | :--- |
| `phillip_bark_ameaca.ogg` | *"Afastem-se da minha filha, abominação. A hesitação é fatal."* | *"Step away from my daughter, abomination. Hesitation is fatal."* |
| `phillip_bark_dor.ogg` | *"Ugh...! A espada de prata... ainda não foi partida!"* | *"Ugh...! The silver blade... has not yet been shattered!"* |
| `phillip_bark_risada.ogg` | *"Você ousa erguer os olhos contra a Inquisição, herege?!"* | *"Do you dare look into the eyes of the Inquisition, heretic?!"* |

### 5.4 Dra. Clara Vance (Hematologista Oficial da Enfermaria)

- **Papel no Jogo:** Médica legista e hematologista do Conselho Estudantil. Conduz a Campanha de Saúde Comunitária e gerencia as coletas de sangue Rh-Nulo.
- **Sprites Disponíveis:** Sprites da Enfermeira em `game/images/mobs/`: `mob enfermeira neutra.webp`, `desconfiada`, `sorrindo`, `medo`, `transe`.
- **Falas Vocais & Transcrições Oficiais:**

| Arquivo (.ogg) | Transcrição Oficial (Português) | Fala em Inglês |
| :--- | :--- | :--- |
| `mob_enfermeira_f1.ogg` | *"Arregace a manga, Sr. Vane. Um doador raro como o senhor garante créditos extras e chá doce após a agulha."* | *"Roll up your sleeve, Mister Vane... A rare donor like you gets an excused absence and a cup of sweet tea after the needle."* |
| `mob_enfermeira_f2.ogg` | *"Sem pulso sob o estetoscópio, pele fria e pupilas dilatadas... A Presidente Elara me alertou sobre seu prontuário."* | *"No pulse under the stethoscope, ice-cold skin, and dilated pupils... President Elara warned me your blood chart had changed."* |
| `mob_enfermeira_f3.ogg` | *"F-Fique longe do refrigerador, Vane! Pegue as chaves do sangue... só não rasgue a minha garganta!"* | *"S-Stay away from the refrigerator, Vane! Take the keys to the blood cooler... just don't tear my throat out!"* |
| `mob_enfermeira_mordida.ogg` | *"Ahn...! Direto na carótida... Então é assim que o gado se sente..."* | *"Ahn...! Right in the carotid... So this is how the livestock feels..."* |
| `mob_enfermeira_anemia_recusa.ogg` | *"Afaste-se da maca, Sr. Vane. Eu não tiro sangue de cadáveres ambulantes."* | *"Step away from the gurney, Mister Vane. I do not draw blood from walking corpses."* |
| `enfermeira_recusa_anemia_completa.ogg` | *"De jeito nenhum, Sr. Vane. Seus lábios estão lívidos e sua pressão arterial mal registra... Se eu espetar essa veia com esse quadro de anemia aguda, você desmaia na maca..."* | *"Absolutely not, Mister Vane. Your lips are chalk-white and your arterial pulse barely registers on the gauge. If I plunge a needle into that vein under acute hypovolemic shock, you'll collapse on my floor before you collect your credits. Go rest for a few turns, eat something substantial, and recover your marrow before you attempt to sell another drop."* |
| `enfermeira_climax_01_nora.ogg` | *"A paciente trinta e um foi transferida voluntariamente segundo os registros oficiais, senhor Vane."* | *"Subject Thirty-One was officially signed off as a voluntary transfer, Mister Vane."* |
| `enfermeira_climax_02_sangue_dourado.ogg` | *"Inacreditável... Sangue Rh-nulo puro, fundido a uma vitae antediluviana."* | *"Incredible... Golden Rh-Null blood fused with antediluvian vitae."* |
| `enfermeira_climax_03_suborno.ogg` | *"Leve a bolsa filtrada sob o casaco. Eu não vi você entrar, e você nunca viu quem assina os atestados."* | *"Take the filtered bag under your coat. I didn't see you come in, and you never saw who signs the death certificates."* |
| `enfermeira_climax_04_campanha.ogg` | *"Duas bolsas de O-negativo em jejum sempre deixam os calouros tontos..."* | *"Two bags of O-negative on an empty stomach always makes the scholarship kids dizzy."* |

### 5.5 Diretor Ambrósio

- **Papel no Jogo:** Burocrata corrupto da reitoria humana que assina os termos de doação e faz vista grossa para a servidão de bolsistas.
- **Sprites Disponíveis:** Sprites do Diretor em `game/images/mobs/`: `mob diretor.webp`.
- **Falas Vocais & Transcrições Oficiais:**

| Arquivo (.ogg) | Transcrição Oficial (Português) | Fala em Inglês |
| :--- | :--- | :--- |
| `diretor_climax_01_sangue_dourado.ogg` | *"Uma biologia singularíssima, Sr. Vane. Rh Nulo. Sangue Dourado. Um órfão sem ninguém para ligar em emergências. Perfeito."* | *"A most singular biology, Mister Vane. Rh Null. Golden Blood. An orphan with no one to call in case of emergency. Perfect."* |
| `diretor_bark_histeria.ogg` | *"Os registros foram incinerados! Não sobrou papelada nenhuma para me incriminar!"* | *"The records were incinerated! There is no paperwork left to incriminate me!"* |
| `diretor_bark_drenado.ogg` | *"Misericórdia, Vane... Eu apenas assinei o que o Conselho exigiu...!"* | *"Mercy, Vane... I only signed what the Council demanded...!"* |

### 5.6 Anomalias Urbanas & Chefes Menores (World of Horror)

- **Papel no Jogo:** Aparições e lendas que assombram os setores periféricos da academia.
- **Sprites Disponíveis:** Sprites em `game/images/Enemy's/`.
- **Falas Vocais & Transcrições Oficiais:**

| Arquivo (.ogg) | Transcrição Oficial (Português) | Fala em Inglês |
| :--- | :--- | :--- |
| `loira_bark_espelho.ogg` | *"Alimente o vidro com sua garganta! Eu serei o seu reflexo!"* | *"Feed your throat to the glass! I shall become your reflection!"* |
| `loira_bark_dor.ogg` | *"O espelho trinca... Mas o reflexo nunca morre!"* | *"The glass cracks... But the reflection never dies!"* |
| `loira_bark_risada.ogg` | *"Hihihi... Olhe bem para o espelho antes de apagar a luz..."* | *"Tee-hee... Take a close look in the glass before turning off the lights..."* |
| `hachishaku_bark_po.ogg` | *"Po... po... po... Entregue seu pulso à névoa..."* | *"Po... po... po... Surrender your wrist to the mist..."* |
| `fada_bark_enigma.ogg` | *"Um nome é apenas uma coleira! A coisa sob as fundações está faminta!"* | *"A name is merely a collar! The thing beneath the foundations is starving!"* |
| `fada_bark_dor.ogg` | *"Argh! O absinto queima nas veias mortas!"* | *"Argh! The absinthe burns in dead veins!"* |
| `fada_bark_risada.ogg` | *"Hahaha! Beba mais um copo e esqueça sua humanidade!"* | *"Hahaha! Drink one more glass and forget your humanity!"* |

---

## 🏫 6. Catálogo dos 17 Mobs & Figurantes da Academia

Cada figurante conta com **4 a 6 ações de áudio gravadas via Gemini TTS** (Abordagem inicial F1/F2/F3, 2 Diálogos anti-repetição de investigação, Grito de Mordida predatória e Reação de Suborno policial):

| ID do Figurante | Título Social / Facção | Setor Típico | Sprites WebP | Vozes (.ogg) e Falas |
| :--- | :--- | :--- | :---: | :--- |
| `mob_calouro_a` | Calouro Anêmico | Dormitório / Pátio | 7 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_caloura_b` | Caloura de Farmácia | Enfermaria | 7 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_calouro_c` | Calouro Nervoso | Biblioteca | 6 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_veterano_a` | Heitor (Monitor de Disciplina) | Depósito / Corredores | 8 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_veterana_b` | Bia (Monitora da Rouparia) | Gabinete / Pátio | 6 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_veterano_c` | Veterano de Esgrima | Pátio das Árvores | 6 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_veterana_c` | Veterana Nobre | Sala de Música | 6 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_veterana_fundao` | Veterana do Fundão | Bar da Fada Verde | 6 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_veterano_fundao` | Mecânico das Caldeiras | Caldeiras Centrais | 7 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_veterano_a_fundao` | Traficante de Reagentes | Caldeiras | 8 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_veterano_b_fundao` | Batedor Clandestino | Caldeiras | 7 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_veterana_ocultista` | Iniciada Hermética | Sala de Ocultismo | 6 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_veterano_ocultista` | Alquimista de Fluidos | Sala de Ocultismo | 6 expressões | 3 abordagens, 2 conversas, 1 mordida |
| `mob_policial_a` | Soldado da Guarda Noturna | Portões / Praça | 6 expressões | 3 abordagens, 2 conversas, suborno policial |
| `mob_policial_b` | Sargento da Ronda Externa | Avenida do Campus | 6 expressões | 3 abordagens, 2 conversas, suborno policial |
| `mob_policial_c` | Oficial de Contenção | Perímetro Externo | 6 expressões | 3 abordagens, 2 conversas, suborno policial |
| `mob_enfermeira` | Dra. Clara (Equipe Clínica) | Enfermaria | 8 expressões | 3 abordagens, 2 conversas, banquete clínico |

---

## 🖼️ 7. Galeria de Cenas (CGs) & Backgrounds

Todas as 61 cenas foram devidamente calibradas com `Transform(..., xysize=(1920, 1080), fit='cover')`:

### 7.1 Cenas Narrativas Especiais (`game/images/cenas/`)

| Tag Ren'Py | Arquivo de Imagem | Resolução Calibrada | Descrição Narrativa |
| :--- | :--- | :---: | :--- |
| `cena deposito extorsao teo` | `cena deposito anexo frasco azul extorsao teo.webp` | 1920×1080 | Depósito Anexo: Heitor e Bia encurralam Teo pelo frasco quebrado. |
| `cena nora caneta` | `cena de nora pedindo uma caneta a victor...webp` | 1920×1080 | Corredor da manhã: primeiro encontro com Nora antes do frenesi. |
| `cena nora parede loucura` | `cena parede loucura nora escrevendo.webp` | 1920×1080 | Zona Vermelha: Nora escrevendo na parede em estado de loucura. |
| `cena nora parede encarando` | `cena parede loucura nora encarando.webp` | 1920×1080 | Nora vira o rosto banhado em veias negras para encarar Victor. |
| `cena quase morte nora` | `cena da quase morte de victor...webp` | 1920×1080 | Victor caído com a garganta lacerada pelas garras de Nora. |
| `cena quase morte encontra lility` | `cena da quase morte... e encontra lility.webp` | 1920×1080 | Lility surge nas sombras do corredor diante de Victor moribundo. |
| `cena quase morte lility ajoelha` | `cena da quase morte... lility ajoelha.webp` | 1920×1080 | Lility ajoelha ao lado do corpo de Victor para avaliar o sangue. |
| `cena quase morte lility proposta` | `cena da quase morte... lility proposta.webp` | 1920×1080 | Lility oferece o pacto de sangue e a vida eterna como ghoul. |
| `cena passado victor 01 a 11` | `passado de victor/cena 1 a 11.jpg` | 1920×1080 | Flashback completo: estacionamento, o soco, a delegacia e a traição. |
| `cena lility piano 1 a 7` | `encontro com lility tocando piano... 1 a 7.jpg` | 1920×1080 | Sequência completa: Victor entra na sala de música e a valsa gótica. |
| `cena elara conversa manha` | `elara e victor conversando de manha.jpg` | 1920×1080 | Gabinete Presidencial: Audiência matinal e Termo do Grilhão. |
| `cena elara mostra pingente nora` | `elara mostra pingente 31 de nora.jpg` | 1920×1080 | Elara pousa o pingente da Cobaia #31 sobre o mogno da mesa. |
| `cena transe lility 1 a 4` | `cenas de transe de sangue lility/1 a 4.webp` | 1920×1080 | Transe de sangue e conexão sensorial profunda com Lility. |
| `cena lility memoria diluvio` | `passado lility/cena memoria diluvio...webp` | 1920×1080 | Memória antediluviana: a torre colossal diante do dilúvio antigo. |
| `cena transe emilia` | `transe de sangue com emilia.webp` | 1920×1080 | Pacto místico de sangue sob a luz dos vitrais da capela. |
| `cena halo batom espelho 1 e 2` | `O Halo de Batom no Espelho Dia 2 Noite...webp` | 1920×1080 | Mistério do espelho trincado no banheiro do 2º andar. |
| `cena victor quadros 1 a 5` | `mistério dos quadros estranhos/...jpg` | 1920×1080 | Galeria dos Esquecidos: investigação da tela 'O Banquete de 1889'. |

---

## ⚔️ 8. Bestiário & Inimigos de Batalha (`game/images/Enemy's/`)

O jogo dispõe de **26 arquétipos inimigos** com poses de prontidão, ataque e derrota renderizadas em WebP 92:

| Inimigo / Arquétipo | IA / Categoria | Sprites Integrados | Voz / Áudio de Combate (Gemini TTS Inglês) |
| :--- | :--- | :---: | :--- |
| **Policial da Ronda** | Humano / Lei | 3 poses (`neutro`, `ataque`, `derrota`) | `policial_bark_saudacao (1-2)`, `ataque (1-2)`, `dor (1-2)`, `risada (1-2)`, `derrota_1` (Orus) |
| **Inquisidor Sagrado** | Humano / Inquisição | 3 poses (`neutro`, `ataque`, `derrota`) | `inquisidor_bark_saudacao (1-2)`, `ataque (1-2)`, `dor (1-2)`, `risada (1-2)`, `derrota_1` (Algenib) |
| **Executora do Conselho** | Grêmio / Elite | 3 poses (`neutro`, `ataque`, `derrota`) | `executora_bark_saudacao (1-2)`, `ataque (1-2)`, `dor (1-2)`, `risada (1-2)`, `derrota_1` (Aoede) |
| **Guarda de Prata** | Grêmio / Cavaleiro | 3 poses (`neutro`, `ataque`, `derrota`) | `guarda_prata_bark_saudacao (1-2)`, `ataque (1-2)`, `dor (1-2)`, `risada (1-2)`, `derrota_1` (Algieba) |
| **Estudante Delinquente** | Humano / Escola | 3 poses (`neutro`, `ataque`, `derrota`) | `estudante_bark_saudacao (1-2)`, `ataque (1-2)`, `dor (1-2)`, `risada (1-2)`, `derrota_1` (Puck) |
| **Aluna Corrompida** | Corrompido | 3 poses (`neutro`, `ataque`, `derrota`) | `aluna_bark_saudacao (1-2)`, `ataque (1-2)`, `dor (1-2)`, `risada (1-2)`, `derrota_1` (Kore) |
| **Alquimista Renegado** | Humano / Fundão | 3 poses (`neutro`, `ataque`, `derrota`) | `alquimista_bark_saudacao (1-2)`, `ataque (1-2)`, `dor (1-2)`, `risada (1-2)`, `derrota_1` (Charon) |
| **Capanga do Fundão** | Humano / Máscara Gás | 3 poses (`neutro`, `ataque`, `derrota`) | `capanga_bark_saudacao (1-2)`, `ataque (1-2)`, `dor (1-2)`, `risada (1-2)`, `derrota_1` (Fenrir) |
| **Marionete de Fios** | Corrompido / Boneca | 3 poses (`neutro`, `ataque`, `derrota`) | `marionete_bark_saudacao (1-2)`, `ataque (1-2)`, `dor (1-2)`, `risada (1-2)`, `derrota_1` (Leda) |
| **Ghoul Voraz** | Corrompido / Abismo | 3 poses (`neutro`, `ataque`, `derrota`) | `sfx_ghoul_gargarejo_fome.ogg` |
| **Cão Infernal (Hellhound)** | Besta / Ocultismo | 3 poses (`neutro`, `ataque`, `derrota`) | `sfx_hellhound_rosnar_gutural.ogg` |
| **Aberração de Gosma** | Inorgânico / Esgoto | 3 poses (`neutro`, `ataque`, `derrota`) | `sfx_aberracao_gosma_rastejar.ogg` |
| **A Loira do Banheiro** | Anomalia Urbana | 3 poses (`neutro`, `ataque`, `derrota`) | `loira_bark_espelho`, `ataque`, `dor`, `risada`, `derrota` (Kore) |
| **Hachishakusama (8 Pés)** | Anomalia Urbana | 3 poses (`neutro`, `ataque`, `derrota`) | `hachishaku_bark_po.ogg` |
| **A Fada Verde (Absinto)** | Anomalia Urbana | 3 poses (`neutro`, `ataque`, `derrota`) | `fada_bark_enigma`, `ataque`, `dor`, `risada`, `derrota` (Zephyr) |
| **Nora Vasques (Chefe)** | Chefe / Ghoul #31 | 3 poses (`neutra`, `atacando`, `frenesi`) | `nora_bark_loucura`, `ataque`, `dor`, `risada`, `derrota` (Leda) |
| **Lorde Phillip (Chefe)** | Chefe / Inquisidor | 4 poses (`neutro`, `pensativo`, `combate`, `derrota`) | `phillip_bark_ameaca`, `ataque`, `dor`, `risada`, `derrota` (Charon) |
| **Cain (Chefe Final)** | Chefe / Progenitor | 4 poses (`neutro`, `ameaca`, `combate`, `agachado`) | `cain_bark_desafio.ogg`, `dor`, `risada` |

---

## 🏰 9. Cenários do Campus & Wallpapers (Estáticos e Animados)

O mapa tático possui **17 setores navegáveis**:

| Setor / Cenário | Tipo de Fundo | Resolução | Iluminação / Período |
| :--- | :--- | :---: | :--- |
| **Dormitório de Victor** | WebM Vídeo + WebP | 1920×1080 | Manhã, Tarde, Noite (Zona Segura, 0 passos) |
| **Biblioteca Central** | WebM Vídeo + WebP | 1920×1080 | Manhã (solar), Tarde (ouro), Noite (velas) |
| **Gabinete do Grêmio** | WebM Vídeo + WebP | 1920×1080 | Manhã, Tarde, Noite (mesa de mogno de Elara) |
| **Sala de Música** | WebM Vídeo + WebP | 1920×1080 | Noite / Crepúsculo (piano de cauda de Lility) |
| **Caldeiras Centrais** | WebM Vídeo + WebP | 1920×1080 | Subsolo industrial / vapor (Mercado de Valéria) |
| **Bar da Fada Verde** | WebM Vídeo + WebP | 1920×1080 | Jazz noir / neon esmeralda no subsolo |
| **Enfermaria Oficial** | WebM Vídeo + WebP | 1920×1080 | Leitos clínicos / cortina amarela da Dra. Clara |
| **Sala de Ocultismo** | WebM Vídeo + WebP | 1920×1080 | Círculo de giz / estantes de tomos proibidos |
| **Capela da Academia** | WebM Vídeo + WebP | 1920×1080 | Vitrais góticos / altar de prata de Emília |
| **Pátio das Árvores** | WebM Vídeo + WebP | 1920×1080 | Fonte central / folhas secas / névoa |
| **Depósito Anexo** | WebP 1080p | 1920×1080 | Local da extorsão de Teo por Heitor e Bia |
| **Catacumbas / Cripta** | WebM Vídeo + WebP | 1920×1080 | Zona Vermelha profunda / cela de Nora / Cain |

---
*Fim do Inventário Técnico de Ativos & Recursos — The Hunger and the Hallways.*
