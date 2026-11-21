# GAME DESIGN DOCUMENT (GDD v4.0) — *THE HUNGER & THE HALLWAYS*

- **Título:** *The Hunger & The Hallways* (*A Fome e os Corredores*)
- **Engine & Build:** Ren'Py 8.x / Python 3 (`config.version = "1.0"`, `1920x1080`)
- **Gênero:** Survival Horror RPG Noir • Visual Novel Psicológica • Dating Sim Sombrio
- **Inspirações Mecânicas:** *World of Horror*, *Persona 5*, *Vampire: The Masquerade – Bloodlines*, *Black Survival*
- **Escopo da Live Build:** 16 arquivos `.rpy` • 17 setores no mapa tático • 26 arquétipos de inimigos • 5 Casos Investigativos • 6 Climas Diários • 18 Cenas de Expansão de Lore • 739 Faixas de Áudio (118 de Mobs) • Vitrine Rotativa & Economia Balanceada • 5 Finais Canônicos + Game Over

---

## 1. VISÃO DE JOGO & PILARES TEMÁTICOS

**Logline:** Victor Vane, bolsista transferido à isolada **Academia São Cipriano**, sobrevive por um fio na Noite do Dia 1 ao firmar o pacto de sangue com a antiga vampira **Lility**. Preso entre a fome física crescente, o rigor burocrático e letal do Conselho Estudantil de **Elara**, as rondas inquisitoriais de **Emília von Karsten**, o contrabando subterrâneo de **Valéria** e o despertar de uma entidade antediluviana nas profundezas (**DOOM Clock**), Victor precisa decidir quanto de sua humanidade está disposto a negociar.

### Os Quatro Pilares
1. **A Fome como Parasita Existencial:** Alimentar-se preserva força e evita o Frenesi (`<20%`), mas corrói `humanidade` (alterando permanentemente a aparência e o desfecho moral de Victor).
2. **Economia de Favores e Dívidas (`Livro de Dívidas`):** Nada na academia é gratuito. Contratos institucionais, favores e compras `Fiado` no subsolo formam uma malha de obrigações com efeitos políticos e emocionais reais.
3. **Sigilo & Escalada Cósmica (`DOOM Clock` / `ruina_cain`):** O jogador explora em liberdade pós-prólogo sem limite rígido de passos no quarto, comprando dias extras ao conter lendas urbanas enquanto o **DOOM** avança rumo ao colapso. *(Regra de sigilo: a identidade de **Cain** não aparece na HUD pública nem antes do clímax).*
4. **Conflito de Facções e Múltiplas Máscaras:** Navegar simultaneamente entre o Grêmio de Uniformes Brancos, a Inquisição e o subsolo clandestino produz ciúmes, embates diretos e descobertas olfativas cruzadas.

---

## 2. ARQUITETURA NARRATIVA & PROGRESSÃO TEMPORAL (`calendario.rpy` & `script.rpy`)

### 2.1 Prólogo Guiado (Eventos Obrigatórios)
1. **Abertura & Pesadelo:** Vídeo introdutório, despertar com Lility estendendo a mão no pesadelo, viagem de trem-bala e chegada aos portões de São Cipriano.
2. **Dia 1 Manhã / Tarde (`evt_d01_manha`, `evt_d01_tarde`):** Chegada ao dormitório, Diretor Ambrósio, encontro inicial com Emília e assinatura/pressão do Termo 112 (dívida de Teo).
3. **Dia 1 Noite (`evt_d01_noite`):** Ataque letal de Nora (Cobaia #31) na ala interditada e o Pacto de Sangue de Lility à beira da morte.
4. **Dia 2 Manhã (`evt_d02_manha`):** Julgamento no Gabinete de Elara e assinatura do **Termo do Grilhão** (que amarra o comportamento de Victor à dor física de Lility). A partir daqui o **Mapa Tático** abre em modo livre.

*(Nota técnica de estado atual: `evt_d02_tarde` e `evt_d02_noite` existem como labels de transição rápida para `slot_livre`).*

### 2.2 Marcos Dinâmicos do DOOM Clock (`verificar_evento_por_threshold_doom`)
Ao avançar o turno em `calendario.rpy`, o sistema verifica um marco por dia (em ordem crescente de DOOM/dia):
- **25% DOOM / Dia 6+ (`evt_d06_tarde` — Marco 30% Tenso):** Primeiras fissuras sobrenaturais e pânico estudantil.
- **35% DOOM / Dia 8+ (`evt_d08_manha` — Marco 35% Inspeção):** Aumento da vigilância sanitária e política do Grêmio.
- **40% DOOM / Dia 10+ (`evt_d10_noite` — Marco 40% Fada Verde):** Crise no Bar da Fada Verde e liberação garantida do Mercado Negro.
- **45% DOOM / Dia 12+ (`evt_d12_noite` — Marco 50% Baile):** Baile de Máscaras, valsa e endurecimento do toque de recolher.
- **55% DOOM / Dia 15+ (`evt_d15_noite` — Marco 70% Cripta):** Incursão subterrânea e fissura nas defesas antigas.
- **60% DOOM / Dia 17+ (`evt_d17_tarde` — Marco 60% Inquisição):** Chegada de **Lorde Phillip von Karsten** e desbloqueio do `ritual_corte_vinculo_desbloqueado = True`.
- **75% DOOM / Dia 19+ (`evt_d19_noite` — Marco 85% Colapso):** Ruptura disciplinar e histeria coletiva avançada.
- **85% DOOM / Dia 20+ (`evt_d20_noite` — Marco 90% Pré-Eclipse):** Véspera do Eclipse Vermelho.
- **100% DOOM ou Dia >= 21 (`evt_d21_noite` — Clímax Final):** Confronto contra o Despertar e escolha entre os **5 Finais Canônicos**.

### 2.3 Expansões Orgânicas & Eventos Secundários
- **18 Cenas em `expansao_conflitos_lore.rpy`:** Disparadas conforme presença de heroínas, horários, `afeto`, `ruina_cain` e investigações (incl. genealogia falsa de "Lyra von Blut", inundação de água negra, vigília armada dos Executores e auditoria forense em Clara Vance).
- **6 Micro-Eventos de Ito (`micro_evento_ito_corredor`):** Pequenas vinhetas de rotina estudantil e deterioração escolar nos corredores.
- **Eventos de Consolidação de Rota:** `evento_emilia_pacto_sangue` (repercussões imediatas com Elara e Lility) e `evento_valeria_safra_rara` (retribuído com comentários ácidos das rivais).

---

## 3. CORES DE GAMEPLAY (MICRO, MESO E MACRO-LOOPS)

### 3.1 Micro-Loop de Exploração (`slot_livre` & `investigar_passo_bs`)
- **3 Passos por Período** (`passos_restantes_periodo = 3`) e até **3 Visitas** entre salas (`2` se o perk/efeito `paranoia_executor` estiver ativo).
- **Dormitório = Zona Segura (0 Passos):** Entrar, conversar com Emília, Lility ou mediar o **Grande Embate (`evento_embate_dormitorio_lility_emilia`)** e descansar não gasta AP nem gera emboscadas.
- **Vasculhar (`investigar_passo_bs`):** Animação ampliada de exploração seguida de sorteio modular:
  - Presença de heroína no setor (com diálogo, toques e eventos de marco).
  - Encontro com figurante *Mobu Kyara* (`encontro_mob_figurante`: alimentação furtiva, conversa, suborno ou intimidação).
  - Coleta de `loot_aleatorio_bs` (Sucata, Giz, Absinto, Kits, Sangue Adulterado, Dinheiro ou **Fragmentos da Chave da Cripta**).
  - Pistas dos **5 Casos Investigativos**.
  - Emboscada letal da **Zona Vermelha** (principalmente Tarde/Noite ou Subsolo).

### 3.2 Meso-Loop Diário & Climas (`sistemas_world_of_horror.rpy`)
Cada turno alterna entre **Manhã (Azul)**, **Tarde (Amarela)** e **Noite (Vermelha)**, aplicando passivamente consumo de fome e pequeno avanço de DOOM (+1% a +3%). Todo amanhecer sorteia um dos **6 Climas da Academia**:
1. **Inspeção Rígida do Conselho:** `+10%` Exposição em infrações; relatórios rendem dobro (`$240`).
2. **Campanha Semestral de Sangue:** Predação no Pátio/Banheiro sobe para 85% de sucesso (`+45%` Sede); flagras dão `+30%` Exposição.
3. **Névoa Carmesim do Abismo:** DOOM `+2%` extra; inimigos causam `+25%` de dano e deixam o dobro de espólios.
4. **Toque de Recolher Estrito:** Desconto de `20%` no Mercado Negro (`0.8x`). Dormitório é `0%` risco; fora dele o risco noturno explode.
5. **Chuva Fria nos Vitrais:** Ativa vídeos animados de temporal em todos os setores e concede `+1` Paciência máxima às heroínas naquele dia.
6. **Calmaria Ilusória:** Regenera `+15 HP` ao amanhecer.

*(Também existem efeitos de ambiente `status_escola == "inquietante"` -> `+20%` preços na loja; `status_escola == "histeria"` -> `+20%` dano inimigo).*

### 3.3 Macro-Loop Investigativo: Os 5 Casos (`MisterioCaso`)
Coletar **3/3 pistas** e vencer a anomalia correspondente reduz o DOOM em **-12% por caso concluído** (`MisterioCaso.concluir()`):
1. **A Loira do Banheiro** (`banheiro_abandonado`)
2. **A Mulher de Oito Pés / Hachishaku-sama** (`patio_arvore` / `cemiterio_nevoa` / `portoes_praca`)
3. **O Lote Necrótico** (`sala_caldeiras` / `bar_fada_verde`) -> recompensa extra `$120`, `+1 Bolsa`, `+Afeto Valéria`
4. **A Partitura Carnal** (`sala_musica` / `biblioteca`) -> desbloqueia item-chave *Partitura Rúnica*, `+Afeto Lility`
5. **Os Arquivos Mortos** (`salao_gremio` / `sala_ocultismo`) -> *Arquivos Confidenciais*, aprofunda vínculo de verdade com Emília

---

## 4. MAPA TÁTICO METROIDVANIA (17 SETORES)

- **Planta I — Superfície (11 Setores):** `salao_gremio`, `biblioteca`, `sala_musica`, `patio_arvore`, `sala_ocultismo`, `patio_fonte`, `banheiro_abandonado` (`desbloqueou_banheiro_abandonado`), `dormitorio` (**Safe Zone**), `portoes_praca`, `rua_portao`, `enfermaria` (**Dra. Clara Vance**).
- **Planta II — Subsolo & Exterior Oculto (6 Setores):** `cemiterio_nevoa`, `caldeiras` (Mercado Negro de Valéria — requer `5/5` pistas nas Caldeiras Centrais e possui **30%** de chance diária de fechar para evitar rondas até o Dia 10), `sala_caldeiras` (sorteio antirrepetição de 3 cenários industriais), `bar_fada_verde` (requer Passe Clandestino `$260` base), `catacumbas` (sorteio antirrepetição de 3 galerias), `cripta_cofre` (requer `3/3` fragmentos desenterrados nas Catacumbas — cela da Cobaia #31 Nora).

---

## 5. ECONOMIA, LOJAS & BANCADA DE CRAFTING

- **Catálogo (`CATALOGO_ITENS` — 25 Itens) & Economia ($200 Iniciais):** Combina consumíveis de sobrevida (`bolsa_sangue_filtrado`, `bolsa_sangue_adulterado`, `kit_curativo`, `dose_absinto`, `gaze_consagrada`, `dispositivo_choque`, `filtro_runico`, `dose_estimulante`), novidades táticas (`cracha_falso`, `ampola_prata`, `tampao_hemostatico`, `incenso_mirra`, `sais_vigilia`, `amuleto_estanho`), matérias-primas (`sucata_eletronica`, `giz_protecao`), **5 Presentes Clandestinos** (`presente_flores`, `presente_perfume`, `presente_colar`, `presente_roupa`, `presente_anel`) e 4 relíquias/itens-chave (`partitura_runica`, `relicario_sangue`, `chave_contencao`, `grimorio_corte`).
- **Quatro Pilares Econômicos:**
  1. **Enfermaria (`acao_consultar_enfermaria`):** Ágio oficial alto para recompensar a abertura do Mercado Negro — Bolsa Filtrada `$165` (`1x/dia`), Kit `$105` (`1x/dia`), Curar Sequela física `$140`, Hemograma Rh-Nulo (`+$90` / `-15 HP` seguro / `+10% Exp`), além da Drenagem Furtiva em Clara Vance (`+30%` Fome, `+20 HP`, `+1 Int`, `-2 Hum`, `+10% Exp`, `+3% DOOM`). Inadimplência (`taxa_inadimplente`) aplica `+25%` nos preços e `-20%` na coleta.
  2. **Mercado Negro de Valéria (`menu_loja_valeria_loop` — Vitrine Rotativa Híbrida):** Garante 2 essenciais diários limitados (`1x Bolsa Filtrada` + `Fiado`, `1x Kit Curativo`), sorteia **5 slots rotativos únicos/dia** (`2x Suprimentos`, `1x Contrabando Tático`, `1x Raro/Lote com variância -20% ou +15%` e `1x Presente de Luxo`) dentre 19 itens, oferece `-10%` de desconto por confiança (`afeto >= 6`) e vende o **Passe da Fada Verde (`$260`)**.
  3. **Cobrança Periódica do Conselho (`evento_cobranca_taxa_academica`):** Disparada a cada **6 períodos (2 dias)** a partir do Dia 3 Manhã (`$135` caso `divida_monitores > 0` com abatimento automático, ou `$100` padrão), oferecendo quitação integral, acordo de extração sanguínea (`-15 HP` seguro) ou inadimplência controlável via Livro de Dívidas.
  4. **Bancada de Crafting (`bancada_crafting` — 4 Receitas):**
     - `Dispositivo de Choque`: `1x Sucata + 1x Giz` (30 dmg ou 50 vs `inorganico` + stun).
     - `Filtro Rúnico de Bolso`: `1x Sucata + 1x Giz` (purifica Bolsa Adulterada em Pura `+35%`).
     - `Gaze Consagrada`: `1x Kit + 1x Giz` (`+40 HP` + sela hemorragia/sequela).
     - `Dose Estimulante Rúnica`: `1x Sucata + 1x Absinto` (`+2.5s` no timer QTE + `50%` esquiva).

---

## 6. SISTEMA DE COMBATE (`combate.rpy` — ESTILO PERSONA 5)

- **Bestiário de 26 Arquétipos (`sorteio_mob = 1..26`):** Inclui Executores do Conselho, Duelistas, Hellhounds, Marionetes de Fios, Gárgulas, Bestas Urso, Esqueletos Rúnicos, Capangas/Mecânicos/Alquimistas do Fundão, Inquisidores Táticos, Sombras e Ghouls, cada qual com sprite base e sprite exclusivo de derrota (`img_inimigo_derrota`).
- **4 Arquétipos de IA:** `gremio` (guarda/riposte e perfuração de prata), `corrompido` (ataque duplo e uivo redutor de tempo QTE `-0.7s`), `inorganico` (esmagamento com 45% de chance de `trauma_impacto`) e `humano` (ácido redutor de `-10%` Fome e tiro à queima-roupa).
- **8 Ações em Turno:** Ataque Rápido, Garras de Sangue (`-20% Fome`; `+20` dano extra se perk `garras_sedentas` e Fome `<50%`), Dispositivo de Choque, Revestir Lâmina com Prata Líquida (`+18` Dano e rompe guarda), Coagulantes Sintéticos (`+20 HP`, remove sangramento e `+6 Defesa`), Kit Médico, Gaze Consagrada, Dose Estimulante, Bolsa Filtrada e Fuga Tática (`-12 HP`, 50% `trauma_fuga` se `HP <= 35`).
- **Mecânica Hold-Up (`executar_golpe_critico_persona`):** Ao quebrar/atordoar o oponente ou vencer vantagem crítica, permite escolher **Drenagem Letal**, **All-Out Attack (`+2 Ressonância`)** ou **Extorquir (`+$55 a $105` + `40%` Bolsa Filtrada / `60%` Adulterada)** sem duplicar o saque monetário pós-batalha.

---

## 7. SISTEMA SOCIAL FÊNIKS, TOQUES & GALERIA DE MEMÓRIAS

- **Central Fênix (`menu_victor`) com 5 Abas:** Status Geral, Relacionamentos/Dossiê, **Talentos (9 Perks em 3 Árvores: Humanidade, Subterfúgio e Predador)**, **Livro de Dívidas** e Quadro de Casos WOH.
- **Paciência, Strikes & Rastro Olfativo:** Cada diálogo consome paciência modificada pelo clima (`chuva_vitrais` dá `+1`); falhas sociais acumulam `strikes`. Cheiro de sangue (`rastro_olfativo`) delata Victor diante de Elara e Emília até ser lavado no Dormitório.
- **Transe de Sangue & 5 Telas de Toque Sensorial:** Alimentação direta das heroínas via `executar_transe_sangue` e interações táteis (`tocou_cabeca_lility`, `tocou_rosto_lility`, `tocou_peito_lility`, `tocou_cabeca_emilia`, `tocou_oculos_emilia`, `tocou_crucifixo_emilia` além de `evento_rng_lility_dormindo_manha`).
- **Galeria de Memórias (`galeria_memorias` — 8 Slots):** Marcos I e II de **Lility, Emília, Valéria e Elara** desbloqueáveis via `verificar_marco_disponivel()` (`evento_marco_*`).
- **Sistema Social de Presentes Clandestinos (`fluxo_entregar_presente_heroina`):**
  - **5 Itens de Presente:** `presente_flores` ($85), `presente_perfume` ($135), `presente_colar` ($175), `presente_roupa` ($220), `presente_anel` ($260), limitados a 1x/dia por heroína.
  - **Reações Exclusivas e Preferências:** Lility busca luxo aristocrático e simbolismo imortal; Elara oculta sentimentos sob decoro e aceita joias finas de prata; Emília comove-se com simplicidade sincera e flores silvestres em conflito com votos; Valéria avalia utilidade prática, valor de revenda e peças de seda nobre.

---

## 8. ELENCO PRINCIPAL & AS 4 FACÇÕES

| Personagem / Entidade | Facção & Uniforme | Papel & Arco Central |
| :--- | :--- | :--- |
| **Victor Vane** | Bolsista (Preto -> Fase 3 Predador) | Lacaio recém-convertido traumatizado por traição passada e guiado por 4 regras estritas de sobrevivência. |
| **Lyra von Blut (Mestra / "Lili" / Segredo: Lility)** | Mestra Antediluviana (Roxo/Escuro) | Vampira milenar confinada na Sala de Música pelo Termo do Grilhão. Guarda segredos sobre Cain e o Dilúvio. Apresenta-se como Lyra von Blut perante a escola; chamada de "Mestra" por Victor no início, "Lili" no Estágio 2 e sua verdadeira identidade primordial "Lility" é um segredo velado. |
| **Elara** | Conselho Estudantil (Branco Imaculado) | Presidente tirânica e pragmática. Mantém a Máscara por burocracia implacável e patrulhas de Executores. |
| **Emília von Karsten** | Exorcista / Inquisição (Preto) | Filha de Lorde Phillip. Compassiva com vítimas, mortal com predadores confirmados; investiga desaparecimentos e Rh-nulo. |
| **Valéria** | Turma do Fundão (Subsolo) | Alquimista pragmática do Mercado Negro das Caldeiras. Vende bolsas, passe do Bar e oferece rota de fuga independente. |
| **Dra. Clara Vance** | Enfermaria / Fundação (Jaleco) | Hematologista encurralada entre a coleta de Sangue Dourado e o estoque clandestino da reitoria. |
| **Nora (Cobaia #31)** | Ex-Executora Selada | Responsável pela ferida mortal de Victor no Dia 1; aprisionada sob runas na Cripta do Subsolo Profundo. |
| **Lorde Phillip, Diretor Ambrósio, Ito & Cain** | Autoridades / Progenitor | Forças macro-políticas e a entidade adormecida sob as galerias subterrâneas. |

### 8.1 Sistema de Figurantes Sem Rosto (Mobs) & Variedade Vocal
- **17 Figurantes Mapeados (`MOBS_LORE_DATABASE` em `definitions.rpy`):** Calouros anêmicos, veteranos delinquentes, ocultistas, docentes exaustos, hematologistas da mantenedora e policiais corruptos.
- **Banco Anti-Repetição por Ato:** Listas de múltiplas falas temáticas por Ato (Ato 1, 2 e 3) sorteadas dinamicamente via `sortear_mob_por_local`.
- **Áudio Desacoplado no Canal `barks` (118 Faixas de Mobs):**
  - Ao avistar: `th_bark_mob("abordagem")` (barks `_f1..f3`).
  - Ao conversar: `th_bark_mob("conversa")` (sorteio dinâmico entre `_conversa_1.ogg` e `_conversa_2.ogg` gerados via Gemini TTS com masterização Vorbis 44.1kHz Stereo, -1.5 dBFS).

### 8.2 Diretrizes de Missões de Infiltração em Quartos Privados
- **Escopo e Natureza:** Atividades e missões furtivas específicas nos aposentos privados das heroínas (Quarto de Elara no Grêmio, Quarto de Emília na Ala das Noviças, Aposentos de Valéria nas Caldeiras, e Santuário de Lility na Sala de Música).
- **Pilares de Gameplay:**
  - Testes de Furtividade / Tensão Sensorial baseados em Atributos (`subterfugio`, `intelecto`, `sensibilidade`).
  - Risco de Flagrante e Tensão de Descoberta com penalidade em Paciência e acúmulo de Strikes.
  - Coleta de Relíquias Pessoais e Segredos Íntimos (peças de vestuário, cartas não enviadas, diários trancados, instrumentos proibidos) para alavancagem psicológica, bônus românticos e novas opções de diálogo.

### 8.3 Sistema de Obrigações Acadêmicas & Fachada Escolar
- **Ciclo de Tarefas Pedagógicas:** Como bolsista monitor em São Cipriano, Victor deve manter notas e assiduidade. A cada 4 a 6 períodos a partir do Dia 2, o sistema sorteia uma obrigação formal com prazo estrito em períodos:
  - *Ensaio de Filosofia Hermética & Alquimia dos Fluidos* (Prazo: 4 períodos)
  - *Catalogação dos Tomos Proibidos da Biblioteca* (Prazo: 5 períodos)
  - *Relatório de Frequência e Monitoria do Conselho* (Prazo: 4 períodos)
  - *Herbologia Eclesiástica e Infusões da Capela* (Prazo: 4 períodos)
- **Vias de Cumprimento:**
  - *Estudo Diligente:* Ação dedicada na Biblioteca ou Sala de Ocultismo (1 passo, +1 Intelecto, dever quitado).
  - *Coação Social Vampírica:* Pressionar um calouro amedrontado nos corredores a redigir o dever (0 passos, -2 Humanidade).
- **Punições Progressivas por Inadimplência:**
  - *1ª Falta:* Advertência formal afixada no Mural do Pátio (+15% Exposição).
  - *2ª Falta:* Retenção da Bolsa pelo Grêmio Estudantil (-$50 dos fundos de Victor).
  - *3ª Falta:* Convocação Disciplinar por Elara von Weiss (+20% Exposição e sequela `intimacao_disciplinar`).

### 8.4 Interações Expandidas com Mobs, Cadência Heroínas & Frenesi Inevitável
- **Novas Ações com Figurantes (Mobs):**
  - *🧤 Mão Leve / Punga Furtiva:* Teste de Subterfúgio D10 para surrupiar $25 a $55 sem violência (falha resulta em alarme e +15% Exposição).
  - *🔍 Sondar Rumores:* Revela a localização em tempo real de uma heroína no mapa tático escolar e ativa sua visualização no mapa naquele turno (`rumores_heroina_periodo`).
  - *📝 Coagir Tarefa Acadêmica:* Resolve o dever pendente sem gastar passos de investigação.
- **Radar Dinâmico de Heroínas no Mapa Tático (`heroina_revelada_no_mapa`):**
  - As heroínas iniciam com ícones ocultos nos pinos de exploração do mapa.
  - Conforme Victor aprofunda seu relacionamento (Afeto $\ge 2$, estágios avançados, pactos ou relatórios), sua percepção aguçada desbloqueia a marcação permanente da heroína no mapa.
  - Conversar com alunos figurantes e sondar boatos desbloqueia a visualização temporária (`[RUMOR]`) no mapa durante todo o período corrente.
- **Cadência Social (1 Conversa por Período):** As 4 heroínas principais e os encontros de quarto possuem trava de 1 conversa profunda de lore por período (`conversou_heroina_periodo`), com diálogos e barks naturais de dispensa ao insistir no mesmo turno.
- **Trava da Gaze de Emília:** A restauração de ferimentos e sequelas com Gaze Consagrada no dormitório é limitada a 1 uso por período (`emilia_curou_gaze_periodo`).
- **Frenesi Inevitável (`fome_sangue <= 0`):** Ao atingir zero de sangue, a Besta assume controle incondicional ao cruzar com qualquer mob, disparando ataque sangrento imediato (-8 Humanidade, +35% Exposição).
- **Sincronização de Cenários (`restaurar_fundo_local_atual`):** Subrotina unificada que restaura o cenário de fundo exato considerando local, período e clima diário após cenas de transe ou CGs.

---

## 9. CONDIÇÕES DOS 5 FINAIS CANÔNICOS + GAME OVER (`evt_d21_noite`)

1. **Final A — Consorte Imortal (A Nova Dinastia Carmesim):** Sempre disponível no confronto com o Relicário caso não derrotado; Victor e Lility drenam Cain e assumem o domínio noturno.
2. **Final B — Quase Humano (O Peso da Liberdade):** Requer **`ritual_corte_vinculo_desbloqueado == True`**. Victor realiza o Ritual do Corte ao lado de Emília, libertando Lility em cinzas douradas e recuperando o pulsar humano.
3. **Final C — A Configuração do Lamento (Todos Sobrevivem, Todos Perdem):** Requer **`ritual_corte_vinculo_desbloqueado == True`**. Ao salvar Emília mortalmente ferida transformando-a em vampira, Victor inverte o ritual no Relicário, toma a maldição imortal de Lility e a condena à mortalidade sob sua proteção.
4. **Final D — A Última Transação (Sobreviventes do Submundo):** Requer **`afeto_valeria >= 1`**. Victor abandona a academia em colapso e foge pelos túneis das caldeiras no furgão de Valéria com carga de vitae e tecnologia arcana.
5. **Final Secreto E — A Harmonia Proibida (Aliança das Quatro Soberanas):** Requer **`afeto >= 8` com Lility, Emília, Valéria e Elara** e **`humanidade >= 40`**. Todas sobrevivem em um pacto político inédito que sela a fenda.
6. **Game Over (`morte_definitiva` / derrota no clímax):** Encerra o ciclo por `$ renpy.full_restart()`.
