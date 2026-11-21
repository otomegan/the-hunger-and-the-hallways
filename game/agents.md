# AGENTS.md — Diretrizes de Engenharia e Regras de Ouro ("The Hunger & The Hallways")

Você está atuando como Engenheiro Sênior de Ren'Py 8 (Python 3) e Designer Narrativo no projeto **"The Hunger & The Hallways"** (A Fome e os Corredores), um *Survival Horror RPG Noir / Visual Novel / Dating Sim* governado pelo **DOOM Clock** (`ruina_cain` de 0% a 100%, com marcos escalonados e colapso final em 100% ou na noite do Dia 21) e mecânicas inspiradas em *World of Horror*, *Vampire: The Masquerade – Bloodlines*, *Persona 5*, *Black Survival* e *Femboy Futa House*.

Sempre que editar, criar ou refatorar qualquer arquivo `.rpy`, você **DEVE** seguir estritamente as regras abaixo.

---

## 🚨 1. REGRAS INVIOLÁVEIS (TRAVAS DE SEGURANÇA)

1. **PROIBIDO APAGAR MECÂNICAS, LABELS OU MENUS:**
   - Nunca remova labels de sistemas existentes (`pos_combate_drenagem`, `morte_definitiva`, `investigar_passo_bs`, `encontro_mob_figurante`, `evento_marco_*`, `avancar_turno_mapa`, `slot_atual`, `dormitorio_duo_*`).
   - Nunca simplifique ou resuma diálogos existentes. O padrão literário do jogo exige subtexto psicológico, tensão e escolhas com consequências reais.
2. **CONTROLE EXCLUSIVO DE TEMPO NO `calendario.rpy`:**
   - **NENHUM** bloco de história (`evt_dNN_periodo` em `script.rpy`) pode definir manualmente `$ dia_atual = ...` ou `$ periodo = ...` ou descontar fome de passagem de turno no início da cena.
   - Todo evento de história deve obrigatoriamente terminar com `jump fim_de_evento`.
   - O avanço do relógio e a queda passiva de `fome_sangue` acontecem exclusivamente em `avancar_turno_mapa` -> `slot_atual`.
3. **PROIBIDO ALTERAR OS TRANSFORMS DE ESCALA DOS SPRITES:**
   - Mantenha sempre `xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 1.0 ysize 980 fit "contain"` em `sprite_padrao` (e `xpos 0.25` / `xpos 0.75` para esquerda/direita; `ysize 1080` para `sprite_colossal`).
   - **NUNCA** substitua por `truecenter` ou `yalign 0.55`, pois isso faz os sprites `.webp` flutuarem ou serem cortados.
   - Os sprites de meio-corpo de Victor (`victor fase1 estudante serio meio corpo`, etc.) utilizam `crop (0, 0, 1536, 1450)` para manter proporção exata com as heroínas.
4. **SINTAXE SEGURA EM TELAS E DIÁLOGOS REN'PY:**
   - Em strings de diálogo ou botões (`text` / `textbutton`), sempre escape colchetes duplos `[[TEXTO]]` quando quiser exibir colchetes literais, evitando que o Ren'Py tente interpolar como variável inexistente.
   - Em `Notify()` ou `text` dentro de `screen`, escape sinais de porcentagem com `%%` (ex: `+35%% Saciedade`).
   - Sempre envolva chamadas de música e SFX em `if renpy.loadable("audio/arquivo.ogg"):` ou use os helpers seguros (`th_musica`, `th_sfx`, `th_stinger`, `th_voz`, `th_bark`).
5. **MORTE DEFINITIVA DENTRO DE `call iniciar_combate`:**
   - Como o combate é invocado via `call iniciar_combate(...)`, o label `morte_definitiva` **JAMAIS** deve terminar com `return` (pois retornaria para a cena de história como se o jogador tivesse vencido). Ele deve encerrar o ciclo via `$ renpy.full_restart()` ou carregamento de save.
6. **SIGILO DE NARRATIVA (`DOOM` vs `Cain`) & ÁUDIO `barks`:**
   - Nunca exiba `"Cain"` ou `"Ruína de Cain"` na interface pública do jogador; referencie a barra sempre como **DOOM** / **Deterioração**.
   - Voice Barks curtos devem sempre usar `channel="barks"` (via `th_bark`, `th_bark_inimigo`, `th_bark_mob` ou `th_voz`), nunca `channel="voice"`, evitando cancelamento automático antes de falas `say`.

---

## 🗂️ 2. ARQUITETURA MODULAR DE ARQUIVOS (`game/`)

Mantenha a separação de responsabilidades entre os **16 arquivos `.rpy`** do projeto:

| Arquivo | Responsabilidade Exclusiva |
| :--- | :--- |
| `calendario.rpy` | Máquina de estados do Prólogo Guiado (`D1 Manhã` a `D2 Manhã`), disparo automático de marcos via `verificar_evento_por_threshold_doom()`, `slot_atual`, `slot_livre` (3 passos, `sortear_posicoes_heroinas()`) e `fim_de_evento`. |
| `definitions.rpy` | Declaração de `Character()`, canais (`barks`, `stinger`), transforms ATL ("Falso Live2D"), matrizes de luz, variáveis `default`, flags `persistent.`, helpers `th_voz`/`th_bark`, sprites dinâmicos, pools de inimigos (`sorteio_mob`), `executar_transe_sangue` e `verificar_marco_disponivel`. |
| `bg_fit.rpy` | Script `init 1 python` que intercepta fundos estáticos 2K (`2560x1440`) e registra com `Transform(..., xysize=(1920, 1080), fit="cover")`. Não afeta vídeos nem sprites. |
| `combate.rpy` | Motor universal de luta em turnos estilo Persona 5 com timer QTE (`hud_combate_zona_vermelha`), 8 ações táticas, 4 arquétipos de IA (`gremio`, `corrompido`, `inorganico`, `humano`), rendição Hold-Up (`executar_golpe_critico_persona`), `pos_combate_drenagem` e `morte_definitiva`. |
| `custom_screens.rpy` | Telas táticas e hubs livres: Feniks `menu_victor` (5 abas), `mapa_tatico_escola` (**17 setores**: 11 Superfície + 6 Subsolo/Exterior), Zona Segura do Dormitório (vigílias + Emília/Lility/embate `duo`), Enfermaria (Clara Vance), `hud_exploracao_bs`, `bancada_crafting` (4 receitas), Loja da Valéria, `galeria_memorias` (8 slots), Telas de Toque (5), Mobs, `micro_evento_ito_corredor` (6 cenas) e `evento_marco_*` (8 marcos). |
| `script.rpy` | Roteiro principal: Abertura, Prólogo Guiado (`D1` a `D2 Manhã`), eventos de primeiro encontro por setor, Marcos de Ruína (30/50/70/85%) e os **5 Finais Canônicos (`A`, `B`, `C`, `D`, `E`)** no clímax (`evt_d21_noite`). |
| `expansao_conflitos_lore.rpy` | **18 eventos canônicos** de aprofundamento psicológico, atritos de facção, segredos da Academia São Cipriano e reações exclusivas por rota. |
| `th_sistema_narrativo.rpy` | Camada de apresentação narrativa e sonora: helpers `th_musica`, `th_sfx`, `th_stinger` (8 stingers), `th_bark`, `th_bark_inimigo`, `th_bark_mob`, mapeamentos `BARKS_VOZ` / `BARKS_INIMIGOS` e feedback visual. |
| `sistemas_social_rpg.rpy` | Sistema Feniks Social: **9 Perks** em 3 árvores, matriz de paciência/strikes, duelos retóricos, `Rastro Olfativo`, sistema de Dívidas (`Fiado`) e modificadores de interação com heroínas. |
| `sistemas_avancados.rpy` | Catálogo oficial de itens (`CATALOGO_ITENS` — 14 itens táticos, relíquias, ingredientes e bolsas), multiplicadores de preço dinâmicos e utilitários de inventário. |
| `sistemas_world_of_horror.rpy` | Arquitetura WoH: classe `MisterioCaso` (5 casos investigáveis), `GerenciadorRuina` (DOOM `ruina_cain`, fases e sequelas), `testar_pericia_rpg` (d20) e 6 Climas Diários (`CLIMAS_ACADEMIA`). |
| `sistema_som_ambiente.rpy` | Registra `channel="ambient"` (`mixer="sfx"`, loop) e gerencia `_gerenciador_audio_ambiente_callback` + `MAPA_AMBIENTES_BACKGROUNDS` por sala e horário. |
| `animacoes_cenas_intimas.rpy` | Transforms ATL dedicados para intimidade (`cena_lewd_ofegante`, `estocada_impacto`, `tremor_climax`, `flash_red`, etc.) e `template_cena_intima_exemplo`. |
| `screens.rpy` | Telas nativas customizadas: `main_menu` com Mouse Parallax, `quick_menu` e `navigation` integrados aos menus táticos. |
| `gui.rpy` & `options.rpy` | Configuração Full HD (`1920x1080`), tipografia, identidade da build (`config.name = "the hunger and the hallways"`) e estilos visuais. |

---

## 🎨 3. CONVENÇÕES VISUAIS, DE ÁUDIO E DE ZONA SEGURA

- **Formatos Padrão:** Sprites, inimigos (`game/images/Enemy's/`) e figurantes (`game/images/mobs/`) em **`.webp` (Qualidade 92)** mantendo fundo transparente; fundos estáticos em **`.webp`**; fundos animados em **`.webm` (VP9 1080p, sem áudio `-an`)**; todos os áudios em **`.ogg` Vorbis (44.1 kHz Stereo q6, -1.5 dBFS)**. Evitar deixar `.png`, `.mp4` ou `.mp3` duplicados ativos na build final.
- **Contraste de Facções (Código de Cores de Uniforme):**
  - **Uniforme Branco Imaculado:** Exclusivo da elite vampírica do **Conselho Estudantil / Grêmio** (Presidente Elara e Executores).
  - **Uniforme Preto Padrão:** Usado pelos **estudantes humanos comuns** (Victor Vane, Emília von Karsten e os figurantes *Mobu Kyara* / *The Faceless*), que servem sem saber como rebanho seguro nas campanhas de doação da Enfermaria.
- **Estilo dos Figurantes (*Mobu Kyara*) & Bestiário:** Figurantes em `game/images/mobs/` com rostos sombreados/sem olhos; **26 arquétipos de inimigos** na Zona Vermelha (`game/images/Enemy's/` + `sorteio_mob`), cada qual com sprite base e sprite de derrota após combate.
- **Regra do Dormitório (Zona Segura):** O quarto de Victor nunca consome passos de investigação (`investigar_passo_bs`) nem gera emboscadas hostis. Visitas aleatórias de Emília, Lility ou **ambas simultaneamente (`duo`)** ocorrem mediante gatilhos próprios do dormitório com opção de interação contextual sem risco letal imediato.
