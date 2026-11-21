# Manual de Produção & Arquitetura: Cenas Íntimas, Transe & Lewd
**Projeto:** *The Hunger and the Hallways* (Build Novembro de 2026)  
**Motor:** Ren'Py 8.x / Python 3  
**Arquivos Vinculados:** `game/animacoes_cenas_intimas.rpy`, `game/definitions.rpy` (`executar_transe_sangue`), `game/custom_screens.rpy` (`interacao_toque_*`, `interacao_lility_dormindo`, `galeria_memorias`, `evento_marco_*`)

---

## 1. SISTEMAS ÍNTIMOS JÁ ATIVOS NA LIVE BUILD

Diferente de um manual puramente conceitual, a build atual já opera **quatro camadas íntimas integradas** ao loop tático:

### 1.1 Transe de Sangue (`executar_transe_sangue(heroina)` — `definitions.rpy:9990`)
- Dispara `with flash_red`, reproduz `audio/sfx/heartbeat.ogg`, toca o voice bark de transe da heroína via `$ th_bark(heroina, "transe")` (`channel="barks"`) e sorteia as sequências visuais específicas (ex: `sortear_cena_transe_lility()`).
- Integrado diretamente às rotas do **Covil de Lility** (`menu_alimentacao_covil_lility` — 5 modalidades, limite de 1x por período, bloqueado se `fome_sangue >= 85`), ao **Pacto de Sangue de Emília** (`evento_emilia_pacto_sangue`), à **Safra Rara de Valéria** (`evento_valeria_safra_rara`) e à submissão de **Elara** (`elara_subjugada_no_cofre`).

### 1.2 As 5 Telas de Toque Sensorial (`custom_screens.rpy`)
Cada tela exibe a heroína em `sprite_padrao` com modo debug opcional de hitboxes (`debug_mostrar_hitboxes`):

| Tela | Áreas / Hotspots Mapeados | Desvios & Consequências |
| :--- | :--- | :--- |
| **`interacao_toque_lility`** | Cabeça (`tocou_cabeca_lility`), Rosto (`tocou_rosto_lility`), Peito (`tocou_peito_lility`) | Provocação, vergonha ou punição por insolência (`cliques_irritantes_lility`). |
| **`interacao_lility_dormindo`** | Cabeça (`toque_sono_cabeca`), Bochecha (`toque_sono_bochecha`), Ombros (`toque_sono_ombros`) | Disparada de manhã por `evento_rng_lility_dormindo_manha` (`lility cena dormindo`, música `sighs_in_the_dark.ogg`), com risco de `lility_acorda_assustada` ou saída furtiva (`sair_sem_acordar_lility`). |
| **`interacao_toque_emilia`** | Cabeça (`tocou_cabeca_emilia`), Óculos (`tocou_oculos_emilia`), Crucifixo (`tocou_crucifixo_emilia`) | Queimadura sagrada na prata (`emilia_bark_prata`), timidez e reações de suspeita. |
| **`interacao_toque_valeria`** | Cabeça (`tocou_cabeca_valeria`), Corpo (`tocou_corpo_valeria`), Bolso (`tocou_bolso_valeria`) | Humor ácido, alerta de choque/faísca e defesa do balcão (`toques_valeria`). |
| **`interacao_toque_elara`** | Rosto (`tocou_rosto_elara`), Reação Corporal (`tocou_elara_reacao`) | Varia drasticamente entre desprezo aristocrático e reação submissa se `elara_subjugada_no_cofre == True`. |

### 1.3 Galeria de Memórias & Os 8 Marcos Íntimos (`galeria_memorias` — `custom_screens.rpy:19565`)
Desbloqueados via `verificar_marco_disponivel()` e salvos em `persistent.mem_*` para replay permanente:

| Slot | Heroína & Título | Flag Persistente | Requisitos de Desbloqueio em Campanha |
| :---: | :--- | :--- | :--- |
| **1** | 🩸 Lility I — *A Coleira de Veludo* | `persistent.mem_lility_1` | `Afeto 3+` • Sala de Música à Noite (`evento_marco_lility_1`) |
| **2** | 🩸 Lility II — *Sede Invertida no Piano* | `persistent.mem_lility_2` | `Estágio 2` + `Afeto 6+` • Sala de Música à Noite (`evento_marco_lility_2`) |
| **3** | ✝️ Emília I — *Cicatrizes Entre Estantes* | `persistent.mem_emilia_1` | `Afeto 3+` • Encontrar de Manhã ou Tarde (`evento_marco_emilia_1`) |
| **4** | ✝️ Emília II — *Calor Humano no Quarto* | `persistent.mem_emilia_2` | `Estágio 2` + `Afeto 6+` • Qualquer horário (`evento_marco_emilia_2`) |
| **5** | 🧪 Valéria I — *Contrato de Exclusividade* | `persistent.mem_valeria_1` | `Afeto 2+` • Caldeiras ou Bar da Fada Verde (`evento_marco_valeria_1`) |
| **6** | 🧪 Valéria II — *Dona do Submundo* | `persistent.mem_valeria_2` | `Estágio 2` + `Afeto 5+` • `Domínio 2+` (`evento_marco_valeria_2`) |
| **7** | ⚖️ Elara I — *Inspeção a Portas Fechadas* | `persistent.mem_elara_1` | `Afeto 2+` • Gabinete do Grêmio (`evento_marco_elara_1`) |
| **8** | ⚖️ Elara II — *A Coroa Subjugada* | `persistent.mem_elara_2` | `Estágio 2` + `Afeto 5+` *(ou Subjugação no Cofre)* (`evento_marco_elara_2`) |

### 1.4 Assets Visuais e Sonoros Reais Disponíveis em Disco
- **Lility:** `lility provocante pose corpo inteiro.webp`, `lility sedutora provocante corpo inteiro.webp`, `cena lility dormindo na sala de musica de manha.webp`, `cena de lility provocando e insinuando a victor...webp`.
- **Emília:** 5 variações NSFW dedicadas (`emilia camisa aberta nsfw corada.webp`, `emilia camisa aberta nsfw corpo inteiro.webp`, `emilia camisa aberta nsfw sentada.webp`, `emilia camisa aberta nsfw timida.webp`, `emilia camisa caida nsfw timida.webp`), `emilia excitada encarando com prazer.webp` e `images/cenas/transe de sangue com emilia.webp`.
- **Valéria:** 5 variações NSFW dedicadas em `valeria/corpo inteiro/` (`valeria nsfw short foco bunda*.webp` e `valeria nsfw sem short foco bunda*.webp`) + `valeria sorriso provocante pirulito meio corpo.webp`.
- **Elara:** `elara com prazer.webp`, `elara com as bochechas rosadas.webp`.
- **Trilha & SFX Reais:** `audio/sighs_in_the_dark.ogg`, `audio/the_crimson_chamber_2.ogg`, `audio/obscura.ogg`, `audio/sfx/heartbeat.ogg` (e `audio/heartbeat.ogg`), `audio/sfx_impacto_corpo.ogg`, e todas as falas de `audio/voice/climax/*.ogg` e `audio/voice/{heroina}/*_bark_*.ogg` tocadas exclusivamente por `$ th_bark(...)` / `$ th_voz(...)` no canal `barks`.

---

## 2. PIPELINE DE GERAÇÃO DE MÍDIA ÍNTIMA (OFFLINE / PIXAI / FLOW)

### A Realidade do Google Flow (Google Veo) vs Motores Locais
- **Google Flow (Veo):** Excelente para preliminares, olhares em transe, mordidas no pescoço, suor e respiração ofegante sem nudez explícita. Nudez/genitália ou atos sexuais diretos sofrem bloqueio automático.
- **Rota A — PixAI + Quadros Alternados `.webp` (Mais leve e garantida):**
  Gerar pose base + 2 a 3 quadros faciais/corporais no **PixAI** (`Qualidade 92 .webp` mantendo transparência em sprites ou `< 350 KB` em CGs) e alternar no Ren'Py com `repeat` sobre os transforms ATL.
- **Rota B — Vídeo `.webm` Local ou Sem Censura:**
  Exportar clipes curtos em **VP9 `.webm` sem faixa de áudio (`-an`)** via FFmpeg local para reduzir VRAM/peso sem conflito com os canais `music`/`barks`:
  ```powershell
  ffmpeg -y -i "scratch/clip_bruto.mp4" -an -c:v libvpx-vp9 -b:v 1800k -crf 28 -pix_fmt yuv420p "game/images/cenas/cena_transe.webm"
  ```

---

## 3. TRANSFORMS ATL EM `game/animacoes_cenas_intimas.rpy`

O arquivo define **7 transforms prontos** (e `label template_cena_intima_exemplo`):

1. `cena_lewd_ofegante`: Balanço e respiração lenta contínua (`zoom 1.015`, `easein 0.8 -> 1.032`).
2. `cena_lewd_ofegante_rapida`: Ritmo acelerado pré-clímax (`0.42s / 0.48s`).
3. `estocada_impacto`: Avanço vertical brusco (`yoffset -32`, `zoom 1.07`) seguido de recuo suave.
4. `estocada_forte`: Impacto intenso em dupla batida (`yoffset -50 -> +20`, `zoom 1.12`).
5. `tremor_climax`: Micro-vibrações horizontais de espasmo no ápice.
6. `pulso_sensual_lento`: Oscilação contínua e sutil (`zoom 1.02 -> 1.035`).
7. `flash_red`: Clarão carmesim para mordidas, golpes e picos de desejo (`alpha 0.35 -> 0.0`).

> [!IMPORTANT]
> **Status de Auditoria na Live Build:** `flash_red`, `pulso_sensual_lento`, `cena_lewd_ofegante`, `cena_lewd_ofegante_rapida` e `tremor_climax` (**5 de 7 transforms**) agora estão integrados em combates, `executar_transe_sangue` e CGs da Sala de Música. Apenas os 2 transforms de impacto (`estocada_impacto` e `estocada_forte`) permanecem sem chamador aguardando novas CGs explícitas, assim como `template_cena_intima_exemplo`.

### Modelo Corrigido Alinhado à Build (Usando Assets & Helpers Reais)
```renpy
label exemplo_cena_intima_real:
    scene "images/cenas/transe de sangue com emilia.webp" at cena_lewd_ofegante with dissolve
    $ th_musica("sighs_in_the_dark", fade=1.5)
    play sound "audio/sfx/heartbeat.ogg" loop

    $ th_bark("emilia", "timida")
    emilia "Victor... espere... meu coração está batendo rápido demais..."

    show expression "images/cenas/transe de sangue com emilia.webp" at cena_lewd_ofegante_rapida with dissolve
    $ th_bark("emilia", "transe")

    show expression "images/cenas/transe de sangue com emilia.webp" at estocada_impacto
    play sound "audio/sfx_impacto_corpo.ogg"
    with hpunch
    with flash_red

    stop sound fadeout 1.5
```
*(Regra de ouro de áudio: NUNCA use `channel="voice"` em barks curtos ou `audio/beneath_the_heavy_velvet.ogg` inexistente — use sempre `th_bark`, `th_voz` e faixas existentes em `game/audio/`).*
