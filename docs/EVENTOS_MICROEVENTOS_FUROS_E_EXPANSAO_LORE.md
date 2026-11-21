# AUDITORIA TÉCNICA (FUROS), MICRO-EVENTOS, GRANDES EVENTOS E EXPANSÃO DE LORE
**Projeto:** *The Hunger and the Hallways* (Build Atual — Ren'Py 8.x)  
**Finalidade:** Documento vivo de QA narrativo/técnico e *roadmap* criativo baseado 100% na auditoria do código-fonte (`.rpy`), assets em disco (`game/images/`, `game/audio/`) e regras canônicas de continuidade (`vn-lore-keeper` / `vn-narrative-continuity`).

---

## SUMÁRIO
1. [Parte I — Furos Técnicos, Divergências UI vs. Matemática & Assets Órfãos](#parte-i--furos-técnicos-divergências-ui-vs-matemática--assets-órfãos)
2. [Parte II — 10 Novos Micro-Eventos Táticos & Atmosféricos (Aproveitando Assets em Disco)](#parte-ii--10-novos-micro-eventos-táticos--atmosféricos-aproveitando-assets-em-disco)
3. [Parte III — Novos Grandes Eventos, Pontes Narrativas & Desfechos Intermediários](#parte-iii--novos-grandes-eventos-pontes-narrativas--desfechos-intermediários)
4. [Parte IV — Expansão Profunda de Lore, Facções & Cronologia Secreta](#parte-iv--expansão-profunda-de-lore-facções--cronologia-secreta)

---

## PARTE I — FUROS TÉCNICOS, DIVERGÊNCIAS UI VS. MATEMÁTICA & ASSETS ÓRFÃOS

*(Nota: Auditoria atualizada após as sessões técnicas e de expansão vocal de Novembro de 2026. Foram corrigidos e retirados da lista de furos:
1. **Exceção de Notificação Financeira:** `NameError: name 'th_notificar_recibo'` em `custom_screens.rpy:25114` corrigido com chamada a `notificar_rpg` e alias de segurança em `sistemas_social_rpg.rpy`.
2. **Repetição de Falas e Áudios de Figurantes:** Totalmente resolvido com o banco de falas rotativas por Ato (1, 2 e 3) em `MOBS_LORE_DATABASE`, síntese de 34 novas faixas via Gemini TTS (`_conversa_1.ogg` e `_conversa_2.ogg` para os 17 mobs) e desacoplamento vocal de `abordagem` e `conversa` em `th_bark_mob` (`channel="barks"`).
3. **Economia Dinâmica & Cobrança Periódica:** Vitrine rotativa diária de 5 slots na loja de Valéria, ágio clínico na enfermaria para recompensar o mercado negro, cobrança a cada 6 períodos da taxa acadêmica (`evento_cobranca_taxa_academica`) com controle de inadimplência e sistema de 5 presentes para heroínas (`presente_*`).
4. **Higiene de Sprites de Inimigos:** Correção de sprites espelhados/invertidos e conversão de novos sprites de combate para WebP qualidade 92.
5. **Planejamento de Infiltração:** Estruturado em `plano_missoes_infiltracao_quartos.md` para as incursões nos aposentos privados de Elara, Emília e Valéria sob estética de romance gótico e suspense psicológico.
Restam exclusivamente lacunas narrativas, assets órfãos para cenas futuras e higiene de mídia bruta.)*

### 1.1 Lacunas Narrativas & Acoplamentos Pendentes de História
1. **Buraco Cronológico no Dia 2 (`game/script.rpy:3253-3265`):**  
   As labels `evt_d02_tarde:` e `evt_d02_noite:` contêm apenas `jump slot_livre`. Como o Prólogo bloqueia os marcos do DOOM até `dia == 2 and periodo_atual == "Noite"` (`calendario.rpy:37`), o jogador passa do impacto institucional da manhã do Dia 2 direto para o turno livre sem uma cena de assentamento no dormitório ou patrulha inicial noturna.
2. **Repetição de Fala no Prólogo (Dia 1):**  
   No roteiro do Dia 1 (`LIVRO_NARRATIVO_COMPLETO_PARA_CLAUDE.md:176, 180`), a fala *"Quer dizer: lamento muito, rapaz. Lamento muito."* do Diretor Ambrósio aparece duplicada em dois blocos quase contíguos.
3. **2 Transforms ATL de Impacto Aguardando Novas CGs (`game/animacoes_cenas_intimas.rpy`):**  
   Após o acoplamento de `pulso_sensual_lento`, `cena_lewd_ofegante`, `cena_lewd_ofegante_rapida` e `tremor_climax` às CGs Full HD de `executar_transe_sangue` e da Sala de Música (somando-se a `flash_red`), restam apenas **2 transforms sem chamador** (`estocada_impacto` L34 e `estocada_forte` L40), reservados para futuras sequências explícitas em tela cheia.

### 1.2 Assets Órfãos, Duplicados e Higiene de Mídia
- **Vozes Prontas Não Referenciadas em `.rpy`:**  
  - Clímax & Victor: `audio/voice/climax/cain_climax_01_despertar.ogg`, `audio/voice/climax/victor_despertar_cain.ogg`, `audio/voice/climax/victor_fome_abismo.ogg`, `audio/voice/victor/victor_climax_juramento.ogg`.  
  - Diretor & Experimentos Qwen (`audio/voice/mobs/`): `diretor_bark_drenado.ogg`, `diretor_bark_histeria.ogg`, além dos 5 testes `qwen_aluna_delinquente_provocacao.ogg`, `qwen_caloura_b_alerta.ogg`, `qwen_calouro_anemico_apelo.ogg`, `qwen_executora_decreto.ogg`, `qwen_policial_ronda_toque.ogg`.
- **SFX Órfãos (`audio/sfx/` — 8 de 61 arquivos):**  
  `menu_musica_alt.ogg`, `sfx_ambiente_cemiterio_manha.ogg`, `sfx_ambiente_cemiterio_noite.ogg`, `sfx_ambiente_patio_arvore_entardecer_dourado.ogg`, `sfx_caldeiras_vapor_chiado.ogg`, `sfx_cidade_cyberpunk_hum_noite.ogg`, `sfx_patio_fonte_noite.ogg`, `sfx_sussurros_espelho_banheiro.ogg`.
- **Ilustrações & Sprites Órfãos:**  
  - `images/ilustrações especiais/` (**4/4 arquivos sem referência em `.rpy`**): `emilia triste de frente.png`, `hallowen lility looking you.png`, `medico ou monstro victor.png`, `quadro busto lility.png`.  
  - `images/cenas/transe de sangue com emilia apos mordida.png` (versão PNG pré-conversão ainda órfã/duplicada).  
  - `images/Enemy's/` (**66/145 variantes sem chamada explícita** — majoritariamente poses de derrota/guarda/variações `alt` recém-convertidas que podem enriquecer telas de vitória pós-Hold-Up e transições de guarda quebrada).  
  - `images/mobs/`: prefixos legados não utilizados pelo `obter_sprite_mob` (como `aluna feminina veterana*`, `aluno masculino veterano*`, `enfermeira feminina*` em `.png`/`.webp` e `mob femenina*`/`mob masculino*` antigos), coexistindo com os conjuntos ativos `mob *`.
- **Sobrecarga de Formatos Brutos / Backup no Repositório:**  
  - Em `game/images/`: **66 `.mp4`**, **55 `.png`**, e o utilitário de build `images/menu/logo_organizado/logo_metrics.py`, além dos 4 vídeos fonte em `images/novos backgrounds para se tirar o som/*.mp4`.  
  - Em `game/audio/`: **88 `.mp3`**, **15 `.wav`**, **3 `.flac`**, **2 `.mp4`**, **2 `.url`**, **1 `.txt`** e **1 `.png`** (inclui `audio/sfx/heartbeat.wav` ao lado do `.ogg`, 157 arquivos de licença/fonte Kenney e 21 originais WAV/FLAC).

---

## PARTE II — 10 NOVOS MICRO-EVENTOS TÁTICOS & ATMOSFÉRICOS (APROVEITANDO ASSETS EM DISCO)

Projetados no espírito de *World of Horror* e sob as regras de `vn-lore-keeper` (horror físico, isolamento claustrofóbico, sigilo de Cain/DOOM antes do clímax e economia de recursos/Exposição):

| # | Título & Setor | Gatilho / Requisito | Assets Hoje Órfãos Resgatados | Mecânica, Teste & Consequências |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **O Chamado do Espelho Úmido**<br>*(Banheiro Abandonado — Noite)* | `desbloqueou_banheiro_abandonado` & Humanidade < 65 | `sfx/sfx_sussurros_espelho_banheiro.ogg` | O vidro embaçado escreve o número `41` invertido enquanto algo respira do outro lado. **Sensibilidade (D11):** ganhar +1 Pista da Loira do Banheiro e -4% Ruína; **Quebrar a Pia/Fugir:** -12 HP por estilhaços ou +10% Exposição. |
| **2** | **Válvula de Vapor Rompida**<br>*(Caldeiras / Subsolo — Qualquer turno)* | Saciedade < 60% ou clima quente/tenso | `sfx/sfx_caldeiras_vapor_chiado.ogg` | Um duto secundário estoura jato escaldante misturado a cinza de ossos. **Estancar com Sucata (gasta 1x Sucata):** +1 Absinto escondido na caixa de manutenção e +1 Afeto Valéria; **Atravessar na Força:** -14 HP (queimadura) mas coleta +$90 e +1 Conhecimento Oculto. |
| **3** | **A Fonte de Água Turva**<br>*(Pátio Central — Noite / Névoa)* | Período == `"Noite"` | `sfx/sfx_patio_fonte_noite.ogg` & `sfx/sfx_ambiente_patio_arvore_entardecer_dourado.ogg` | Na borda da fonte iluminada por postes úmidos, moedas rituais flutuam sobre óleo vermelho. **Examinar com Giz (-1 Giz):** limpa um resíduo do Grilhão (-5% DOOM); **Recolher moedas:** +$75, mas +8% Exposição e -4 Humanidade ao molhar as mãos. |
| **4** | **Ronda do Inquisidor Solitário**<br>*(Portões / Corredores — Toque de Recolher)* | `clima_diario_id == "toque_recolher"` ou Exposição >= 50 | `qwen_policial_ronda_toque.ogg`, `qwen_executora_decreto.ogg` | O facho da lanterna varre as pilastras após o toque. **Subornar (-$80):** -18% Exposição; **Charme/Sombra (D12):** escapar ileso e obter rota da ronda (+1 Domínio); **Falha:** combate imediato ou detenção (+20% Exposição, -15 HP). |
| **5** | **Confissão Histérica da Diretoria**<br>*(Gabinete / Corredor Nobre — Pós-Lei Marcial)* | `ruina_cain >= 55` | `diretor_bark_histeria.ogg`, `diretor_bark_drenado.ogg` | Victor flagra o Diretor Ambrósio destruindo cópias do Termo de 1898 num triturador travado. **Chantagear com Dossiê:** quita ou abate $150 de dívida e reduz 10% Exposição; **Drenar no Pânico (Fome < 40%):** aciona `diretor_bark_drenado.ogg` (+35% Saciedade, -8 Humanidade, +6% DOOM). |
| **6** | **O Velório Sem Nome**<br>*(Cemitério da Névoa — Manhã / Noite)* | Manhã ou Noite no Cemitério | `sfx/sfx_ambiente_cemiterio_manha.ogg`, `sfx/sfx_ambiente_cemiterio_noite.ogg` | Coveiros silenciosos tampam uma cova rasa marcada apenas com `"Cobaia — Falha Renal"`. **Coragem/Intelecto (D10):** ler a ficha médica no paletó (+1 Conhecimento Oculto, +1 Gaze); **Rezar / Honrar:** +6 Humanidade, -1 passo de turno. |
| **7** | **O Boato do Uniforme Preto**<br>*(Pátio / Corredores — Tarde)* | `dia_atual >= 3` e Humanidade >= 45 | `qwen_caloura_b_alerta.ogg`, `qwen_calouro_anemico_apelo.ogg` | Um calouro anêmico treme após "doação voluntária" dupla na Enfermaria enquanto uma veterana observa. **Ajudar com Curativo (-1 Kit):** +8 Humanidade e ganha um aliado informante (-10% Exposição na ala); **Extorquir / Ignorar:** +$60 ou -6 Humanidade. |
| **8** | **Retrato da Dama Sob Repintura**<br>*(Biblioteca — Tarde / Noite)* | Após descobrir quadro `O Banquete de 1889` | `images/ilustrações especiais/quadro busto lility.png` | Atrás de um painel falso da galeria repousa um retrato a óleo de séculos atrás idêntico a Lility. **Comparar Datas (`conhecimento_oculto >= 5`):** desbloqueia diálogo secreto no Dormitório com Lility (+2 Afeto, +2 Conhecimento Oculto); **Tocar sem luvas:** -5 HP (lacre rúnico). |
| **9** | **O Caderno Caído no Oratório**<br>*(Biblioteca / Capela — Manhã)* | `estagio_emilia >= 1` | `images/ilustrações especiais/emilia triste de frente.png` | Victor encontra Emília isolada, de joelhos, encarando as próprias mãos sujas de cinza enquanto tenta conciliar a fé von Karsten com o pacto/verdade sobre Victor. **Ouvir em Silêncio / Segurar o Rosário:** +2 Afeto Emília, +5 Humanidade; **Fugir da Culpa:** -3 Humanidade. |
| **10** | **Transe Hipnótico de Rua vs. Safra do Subsolo**<br>*(Avenida do Campus / Caldeiras — Noite)* | Período == `"Noite"` | `sfx/sfx_cidade_cyberpunk_hum_noite.ogg`, `qwen_aluna_delinquente_provocacao.ogg` | Além dos portões, o zumbido elétrico da metrópole abafa o toque de recolher; uma aluna delinquente tenta vender ampolas roubadas fora do controle de Valéria. **Entregar o Nome a Valéria:** +2 Afeto Valéria e +$100; **Comprar em Segredo (-$70):** +1 Bolsa Adulterada (+30% Sede, -5 HP). |

---

## PARTE III — NOVOS GRANDES EVENTOS, PONTES NARRATIVAS & DESFECHOS INTERMEDIÁRIOS

### 3.1 Preenchimento Canônico de `evt_d02_tarde` e `evt_d02_noite` (Eliminando os Stubs de `script.rpy:3253-3265`)
- **`evt_d02_tarde` — "A Assinatura Seca no Termo de Saúde":** Antes de liberar o livre-arbítrio da tarde, Clara Vance (ou um monitor enviado por Elara) intercepta Victor no corredor para coletar a primeira amostra "de rotina" após o incidente da noite anterior. O jogador escolhe entre **forjar fadiga com glicose**, **exigir privacidade invocando uma brecha do regulamento** (teste de `intelecto` / `charme`) ou **ceder uma gota controlada (-8 HP, -10% Exposição)**. Garante que o Dia 2 apresente o peso jurídico da Campanha de Saúde antes da exploração aberta.
- **`evt_d02_noite` — "A Primeira Vigília Atrás da Porta Trancada":** Ao cair da primeira noite sem tutela integral, Victor sente a dor real da abstinência e da febre do novo metabolismo no Dormitório (`dormitorio` como Zona Segura). O evento ensina organicamente o funcionamento das **4 Regras no cartão de bolsista**, introduz um vulto passando pelo corredor sob a fresta da porta e deixa o jogador decidir se aceita o chá distante de Emília ou o silêncio predador sob o luar — conectando diretamente com o desbloqueio livre no Dia 3+.

### 3.2 Três Grandes Conflitos Cruzados Entre Facções
1. **Triângulo Clínico-Político: "Médico ou Monstro" (`Enfermaria`, Pós-`ev_c19_laudo_sincope_clara`):**  
   - **Assets integrados:** `images/ilustrações especiais/medico ou monstro victor.png` + `mob enfermeira` + `elara`.  
   - **Premissa:** Quando Elara exige os arquivos fechados da Enfermaria e Clara começa a juntar as lacunas de memória causadas pela hipnose de Victor, ele precisa encarar seu próprio reflexo partido nos aços cirúrgicos: **ou transforma Clara em cúmplice ciente** (trocando silêncio por acesso livre às bolsas sem gastar `$100` e desbloqueando rota científica alternativa), **ou sacrifica o registro de uma cobaia anônima**, ou **incrimina o Diretor Ambrósio** (aumentando a tensão com o Grêmio em troca de salvar a hematologista).
2. **Aliança Improvável: "O Contrabando da Capela" (`Caldeiras` / `Patio`, Valéria + Emília):**  
   - **Premissa:** Faltam suprimentos estéreis tanto para os curativos de Emília quanto para a filtragem clandestina de Valéria. Victor precisa intermediar um encontro tenso à meia-noite atrás das fornalhas sem deixar que Emília descubra que a fonte dos filtros vem das cobaias mortas das Catacumbas, e sem deixar Valéria saber o quão fundo vai o selo inquisitorial dos von Karsten. Oferece grande ganho mútuo de afeto necessário para o **Final Secreto E**.
3. **Rescaldo da Vigília Dupla no Dormitório (`Dormitório`, Pós-`evento_embate_dormitorio_lility_emilia`):**  
   - Se Victor optou por **"Pacificação Improvável"** ou **"Autoridade Absoluta"** durante o embate entre Lility e Emília no quarto, dispara uma continuação noturna dias depois: Lility provoca Emília ao entregar a ela um registro de família von Karsten do século XIX que menciona o próprio Pacto da Fundação, testando se a fé da noviça quebra ou se transforma em determinação pragmática.

### 3.3 Integração Completa de Vozes & Animações Órfãs no Clímax e no Lewd
- **Pré-Clímax & `evt_d21_noite` (Usando as 4 Vozes de Clímax/Victor hoje mudas):**  
  - Antes da descida final pela Cripta, inserir monólogo de juramento usando `audio/voice/victor/victor_climax_juramento.ogg` conforme o estado de Humanidade.  
  - Ao abrir a fenda de `Cain` em `script.rpy:4861`, acoplar `audio/voice/climax/cain_climax_01_despertar.ogg` imediatamente antes da fala do Progenitor, seguido da resposta de `victor_despertar_cain.ogg` e — caso `fome_sangue < 30` no embate — `victor_fome_abismo.ogg`.
- **Acoplamento dos 2 Transforms Restantes de Impacto & Poses de Toque (`animacoes_cenas_intimas.rpy`):**  
  - Com `pulso_sensual_lento`, `cena_lewd_ofegante`, `cena_lewd_ofegante_rapida` e `tremor_climax` já acoplados às CGs Full HD de `executar_transe_sangue` e da Sala de Música, integrar em futuras cenas explícitas os dois transforms de impacto ainda ociosos (`estocada_impacto` e `estocada_forte`), reaproveitando também a pose especial `hallowen lility looking you.png` como evento sazonal/secreto noturno de Afeto 8+ e `transe de sangue com emilia apos mordida.png` convertida para `.webp`.
- **Poses de Derrota Pós-Combate (`Enemy's/`):**  
  - Aproveitar as sprites de derrota/ajoelhamento extras e poses de guarda em `Enemy's/` ainda não chamadas diretamente em `.rpy` para enriquecer variações no menu de Hold-Up / Negociação / Extorquir.

### 3.4 Desdobramento Alternativo do Dia 21 Quando DOOM < 85%
- Embora `script.rpy:4841-4847` agora já exiba `[ruina_cain] por cento` sem afirmar falsamente 100%, ainda é possível expandir `calendario.rpy:41-42` em dois ramos narrativos distintos no Dia 21:  
  - **Se `ruina_cain >= 85` (ou na descida voluntária com a Chave da Cripta):** dispara `evt_d21_noite` canônico (Despertar de Cain).  
  - **Se `dia >= 21` e `ruina_cain < 85`:** dispara **"A Auditoria Terminal da Fundação"** — a Junta Externa chega para lacrar o campus e executar uma varredura de sangue nos bolsistas em 24h, forçando Lility/Elara a descerem à Cripta agora ou enfrentarem o massacre militar.

---

## PARTE IV — EXPANSÃO PROFUNDA DE LORE, FACÇÕES & CRONOLOGIA SECRETA

*(Alinhamento rigoroso com `vn-lore-keeper`: preservar a tensão física do vampirismo como maldição predatória, a moeda jurídica da dívida e o sigilo sobre Cain até os arquivos mais profundos e o clímax.)*

### 1. O Banquete de 1889 e a Trilogia Oculta da Fundação
O quadro *"O Banquete de 1889"* citado na Biblioteca não mostra apenas vampiros antigos reunidos à mesa: ele marca a assinatura do **Acordo das Três Assinaturas** que originou a Academia São Cipriano sobre o sarcófago subterrâneo:
1. **A Casa von Karsten (Linhagem Inquisitorial de Emília):** Forneceu os ritos de contenção litúrgica, os selos de prata e a "bênção" usada para justificar a capela e os sinos sobre a Cripta. O conflito trágico de Emília nasce ao descobrir que seu pai, **Lorde Phillip**, não foi enviado apenas para "proteger alunos", mas para garantir que o sacrifício periódico de sangue humano continuasse alimentando as correntes sem chamar atenção do Vaticano secular.
2. **O Conselho Estudantil / Fundação Mantenedora (Linhagem Burocrática de Elara):** Assumiu a gestão legal do campus, transformando o tributo de sangue em **bolsas de estudo integrais** e na **Campanha de Saúde Comunitária** — onde alunos pobres ("Uniforme Preto") pagam sua dívida estudantil mantendo estável a pressão sanguínea da escola inteira.
3. **A Patroa Sem Nome / Casa von Blut (Lility):** Agiu como fiadora silenciosa das runas pré-diluvianas. A pista descoberta por Victor e Emília em `ev_c16_investigacao_genealogica_lyra` (anotações aramaicas citando `"Lili..."` onde a nobreza bávara de "von Blut" nunca existiu) pode ser expandida mostrando que Lility **nunca quis manter o selo eternamente**: durante séculos ela esperou surgir uma anomalia biológica compatível — **Sangue Dourado (Rh-Nulo puro acima de 95%)** — capaz de finalmente cortar sua imortalidade ou dividir seu fardo.

### 2. Dossiê Perdido das Cobaias #01–#40 (Ponte para Nora #31 e Victor #41)
Em `ev_c06_lista_rh_nulo`, o documento cita 41 nomes históricos com Victor (#41, 99.8%) e Nora Vasques (#31, 88%). Uma expansão documental nas **Catacumbas** e na **Cripta** esclarece o destino das cobaias anteriores e dá rosto humano aos horrores físicos do bestiário:
- **Cobaias #01–#18 (Geração do Século XIX / Início XX):** Submetidas a transfusões brutas de plasma da cripta sem filtragem — seus remanescentes ossificados e encantados pelos primeiros executores explicam construtos como o **Esqueleto Nobre Rúnico** e as câmaras seladas do subsolo profundo.
- **Cobaias #19–#30 (Falhas de Contenção Neural):** Bolsistas cujo sistema nervoso entrou em rejeição, dando origem às anomalias ligadas por tendões e controle sanguíneo (**Marionetes de Fios de Sangue** e **Ghouls Hostis** abandonados nos dutos condenados).
- **Cobaia #31 — Nora Vasques (88%):** Primeira paciente a sobreviver ao contato prolongado em cápsula viva sob o pretexto médico de "doença hematológica rara" — mantendo a consciência fragmentada dentro da cela octogonal de obsidiana e servindo de espelho sombrio do futuro que espera Victor caso ele se submeta à Fundação.
- **Cobaias #32–#40 (Protocolo Termo de Saúde):** Alunos mais recentes drenados aos poucos por Clara Vance sob ordens do Grêmio e registrados como "transferência disciplinar" ou "desistência por anemia severa", interligando diretamente o desaparecimento que ativa o mistério do **Banheiro Abandonado**.

### 3. Economia Subterrânea do Fundão & A Engenharia do Absinto Esmeralda
Por que um colégio gótico possui um bar clandestino (`Bar da Fada Verde`) e capangas com máscaras de gás e escopetas logo abaixo das caldeiras?
- **Origem Militar-Industrial do Subsolo:** Sob o colégio corre um antigo entroncamento de galerias coloniais de drenagem usado nos anos 1920 para escoar dejetos químicos do laboratório de alquimia da Fundação.
- **O Segredo do Absinto Esmeralda:** A bebida traficada por Valéria não é mero destilado boêmio; trata-se de um **solvente microdosado de absinto, prata coloidal e extrato de raízes tratadas no vapor das caldeiras** capaz de dissolver resíduos do miasma da tumba sem matar o usuário. É por isso que o `Absinto` serve tanto para baixar o frenesi/tensão quanto como reagente de crafting (`Dose Estimulante Rúnica` e ataque à assinatura do Fundador em `script.rpy:2922`).
- **A Rota de Fuga do Final D:** Os furgões e trilhos de serviço atrás da fornalha oeste existem porque, década após década, os mecânicos do Fundão perceberam o avanço lento da "Água Negra" nos ralos (`ev_c17_inundacao_agua_negra`) e construíram sua própria saída de emergência muito antes de o Conselho sequer cogitar evacuação.

### 4. Termo 112 (Teo) & O Papel dos Bolsistas Sem Voz
Expandir o micro-arco financeiro de **Teo (`#112`)** (`teo_bark_divida_01.ogg`, `teo_bark_alivio_02.ogg`, `ledger_devedores`) consolida a regra #1 de Victor (*"Não dever nada a ninguém"*):
- Quando um bolsista atrasa duas contribuições semanais de sangue na Enfermaria ou falha em pagar multas aplicadas pelos Monitores de Uniforme Branco, sua dívida é convertida em **horas compulsórias de limpeza no Subsolo 1** (onde desaparecem nos esgotos ou viram fornecedores forçados do Mercado Negro).
- Permitir que Victor quite ou renegocie o **Termo 112** não apenas limpa o registro de Teo no Livro de Dívidas, mas revela uma **lista de transferência falsificada** assinada pelo próprio Diretor Ambrósio, ligando a economia estudantil do dia a dia diretamente ao coração político do clímax.
