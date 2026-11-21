# 🛒 CATÁLOGO GERAL DA ECONOMIA, LOJAS, CRAFTING & LOOT
## *The Hunger and the Hallways* — Guia Completo da Economia (Build Novembro 2026)

---

## 1. CANAIS ECONÔMICOS E DE SUPRIMENTO

O ecossistema econômico da Academia São Cipriano gira em torno de três pilares integrados a `dinheiro_jogador` (`$`), ao inventário (`CATALOGO_ITENS` em `game/sistemas_avancados.rpy`), ao **Livro de Dívidas** (`registro_dividas_ativas`) e às tabelas de coleta de `loot_aleatorio_bs` (`game/custom_screens.rpy`):

1. **Mercado Negro das Caldeiras (`caldeiras` — Valéria):** Acessado após investigar `5/5` vezes as Caldeiras Centrais (ou desbloqueado no Dia 10 Noite), com **30% de chance diária de fechamento** contra rondas (`sortear_abertura_mercado_negro()`). Opera com **vitrine rotativa híbrida diária** (`sortear_vitrine_mercado_negro()` em `menu_loja_valeria_loop`), tornando-se o canal mais vantajoso frente ao ágio da Enfermaria.
2. **Enfermaria do Campus (`enfermaria` — Dra. Clara Vance):** Ala oficial na Superfície (`xpos 530 ypos 440`), operada via `acao_consultar_enfermaria` / `menu_enfermaria_loop`. Cobra **ágio institucional alto** (`$165` Bolsa 1x/dia, `$105` Kit 1x/dia, `$140` Sequela) e sofre sobrecarga de **`+25%`** (além de `-20%` no hemograma) se Victor estiver sob a sequela `taxa_inadimplente`.
3. **Bancada de Engenharia Oculta & Crafting (`bancada_crafting`):** Acessível nas Caldeiras (`caldeiras` e `sala_caldeiras`) e pela Central Tática, transformando matérias-primas coletadas nos corredores em equipamentos avançados.
4. **Tesouraria do Conselho & Cobrança Periódica (`evento_cobranca_taxa_academica`):** A cada **6 períodos (2 dias completos)** a partir do Dia 3 (`Dia 5 Manhã` em diante), cobra **`$135`** se `divida_monitores > 0` (abatendo da dívida) ou **`$100`** de quota estudantil; inadimplência aplica `taxa_inadimplente` e abre `divida_taxa_atrasada` no Livro de Dívidas.

---

## 2. MODIFICADORES ECONÔMICOS DINÂMICOS (LOJA DA VALÉRIA)

Os preços da loja de Valéria (`calcular_preco_valeria()`) aplicam `obter_multiplicador_valeria()` × modificador do slot (`0.80` em Lote `-20%`, `1.15` em Escassez `+15%`):

| Condição de Estado / Clima | Multiplicador | Preço Base da Bolsa Filtrada | Impacto em Jogo |
| :--- | :---: | :---: | :--- |
| **Normal (`dinheiro_jogador` inicial `$200`)** | `x1.0` | **$120** | Preços padrão de tabela. |
| **`status_escola == "inquietante"`** | `x1.2` (+20%) | **$144** | Tensão do DOOM encarece o contrabando subterrâneo. |
| **`clima_diario_id == "toque_recolher"`** | `x0.8` (-20%) | **$96** | Menos fiscais nos porões; desconto de toque de recolher nas Caldeiras. |
| **Desconto de Confiança (`status_valeria.afeto >= 6`)** | `x0.90` (-10% acumulável) | **$108** *(normal)* | Recompensa fidelidade no balcão (cumulativo com clima). |

*(A Enfermaria da Dra. Clara Vance aplica tabela institucional fixa com acréscimo de `+25%` caso `taxa_inadimplente` esteja ativa).*

---

## 3. LOJA CLANDESTINA DE VALÉRIA (`menu_loja_valeria_loop` — VITRINE ROTATIVA HÍBRIDA)

### 3.1 Essenciais Fixos Diários + Passe
| Item / Serviço | ID | Custo Base (`x1.0`) | Regra & Efeito Real na Build |
| :--- | :--- | :---: | :--- |
| **🩸 Bolsa de Sangue Filtrado** | `bolsa_sangue_filtrado` | **$120** | **1x por dia** (+ Fiado se sem caixa). **+35% Saciedade** sem perda de Humanidade. |
| **🩹 Kit de Curativos Médicos** | `kit_curativo` | **$70** | **1x por dia**. **+30 HP** fora ou dentro do combate. Insumo base da Gaze Consagrada. |
| **🎟️ Passe Clandestino do Fundão** | `tem_passe_fada_verde` | **$260** | Desbloqueia permanentemente o **Bar da Fada Verde**. *(Exige confiança: `vinculo_sangue >= 15`, `afeto >= 8` ou dívida quitada com Valéria).* |

### 3.2 Os 5 Slots Rotativos Diários (`sortear_vitrine_mercado_negro()` — Pool de 19 Itens)
- **Slots 1–2 (Suprimentos / Materiais, até 2x em lote):** `bolsa_sangue_adulterado` (`$55`, 2x), `giz_protecao` (`$65`, 2x), `sucata_eletronica` (`$55`, 2x), `dose_absinto` (`$115`, 1x), `tampao_hemostatico` (`$110`, 1x).
- **Slot 3 (Contrabando Tático, 1x):** `cracha_falso` (`$160`), `ampola_prata` (`$145`), `incenso_mirra` (`$130`), `sais_vigilia` (`$125`), `dispositivo_choque` (`$165`).
- **Slot 4 (Lote Raro & Variância `20% Lote -20%` / `15% Escassez +15%`, 1x):** `filtro_runico` (`$135`), `gaze_consagrada` (`$155`), `dose_estimulante` (`$175`), e `amuleto_estanho` (`$195`, desbloqueado a partir do `Dia >= 5`).
- **Slot 5 (Presente Clandestino & Luxo, 1x):** `presente_flores` (`$85`), `presente_perfume` (`$135`), `presente_colar` (`$175`), `presente_roupa` (`$220`), `presente_anel` (`$260`, peso maior a partir do `Dia >= 4`).

### Sistema de Fiado (`registro_dividas_ativas`)
- Disponível em `menu_loja_valeria_loop` quando `dinheiro_jogador < preco_sangue` e não houver dívida `divida_valeria_sangue_fiado` pendente:
  - **Entrega imediata:** `+1 Bolsa de Sangue Filtrado` por **$0**.
  - **Dívida registrada:** Pagar **`2x Sucata Eletrônica`** via aba **Livro de Dívidas** (`Central Fênix`).
  - **Recompensa de Quitação:** **`+2 Afeto Valéria`**, liberação do balcão de fiado novamente e habilitação de confiança para o Passe do Fundão *(sem cashback gratuito em dinheiro)*.

---

## 4. DISPENSÁRIO DA ENFERMARIA (`acao_consultar_enfermaria` — Dra. Clara Vance)

| Serviço / Produto | Custo / Ganho Base | Custo c/ Inadimplência | Condição & Efeito Completo |
| :--- | :---: | :---: | :--- |
| **🩸 Comprar Bolsa de Sangue Filtrado** | **-$165** *(1x/dia)* | **-$206** | Mais caro que o Mercado Negro (`$120`); garante sobrevida diária se as Caldeiras estiverem fechadas. |
| **🩹 Comprar Kit de Curativos e Sutura** | **-$105** *(1x/dia)* | **-$131** | Tabela hospitalar rígida; adiciona `+1 kit_curativo`. |
| **🩹 Tratar Sequela Física** | **-$140** | **-$175** | Requer sequela física (não remove `taxa_inadimplente`) + recupera **`+20 HP`**. |
| **🔬 Vender Hemograma (Sangue Dourado Rh-Nulo)** | **+$90** | **+$72** | Limite 1x/dia (`coleta_enfermeira_hoje`) e exige `hp_jogador > 20`. Aplica **`-15 HP` (`>= 15`)** e **`+10% Exposição`**. |
| **🩸 Drenagem Furtiva (Banquete Clínico)** | **Gratuito** | **Gratuito** | Requer `fome_sangue < 70` e 1x/dia (`drenou_enfermeira_hoje`). Concede `+30% Saciedade`, `+20 HP`, `+1 Intelecto`, `-2 Humanidade`, `+10% Exposição`, `+3% DOOM` interno e aplica transe hipnótico em Clara. |

---

## 5. BANCADA DE ENGENHARIA & CRAFTING (`bancada_crafting` — 4 Receitas)

| Produto | Materiais Necessários | Preço de Catálogo | Efeito em Jogo |
| :--- | :--- | :---: | :--- |
| **⚡ Dispositivo de Choque Rúnico** | `1x Sucata Eletrônica` + `1x Giz de Proteção` | `$165` | **30 Dano** (**50 vs `inorganico`**) + **Stun (1 turno)** em combate. |
| **🧪 Filtro Rúnico de Bolso** | `1x Sucata Eletrônica` + `1x Giz de Proteção` | `$135` | Purifica `1x Bolsa de Sangue Adulterado` em `1x Bolsa de Sangue Filtrado Puro` (`+35% Saciedade`, `0` perda de Humanidade). |
| **🩹 Gaze Consagrada** | `1x Kit de Curativos` + `1x Giz de Proteção` | `$155` | **`+40 HP`** (inventário ou combate) + cura imediata de **Sequela / Hemorragia**. |
| **💉 Dose Estimulante Rúnica** | `1x Sucata Eletrônica` + `1x Dose de Absinto` | `$175` | Ativa `efeito_estimulante_ativo`: **`+2.5s` no timer QTE** e **`50%` chance de esquiva**. |

---

## 6. CATÁLOGO OFICIAL COMPLETO (`CATALOGO_ITENS` — 25 Itens em `sistemas_avancados.rpy`)

| ID no Código | Nome Oficial | Categoria | Preço Base | Descrição / Efeito Registrado |
| :--- | :--- | :---: | :---: | :--- |
| `bolsa_sangue` | Bolsa de Sangue Filtrado | Consumível | `$120` | `+35% Saciedade` sem perda de Humanidade. |
| `bolsa_sangue_adulterado` | Bolsa de Sangue Adulterado | Consumível | `$55` | Consumo direto: `+35% Saciedade`, **`-2 Humanidade`**, **`+5% Exposição`**. |
| `kit_curativo` | Kit de Curativos Médicos | Consumível | `$70` | `+30 HP`. |
| `dose_absinto` | Dose de Absinto Esmeralda | Consumível | `$115` | Consumo direto: **`+1 Sensibilidade Sobrenatural`**, **`+1 Coragem`**. |
| `giz_protecao` | Giz de Proteção Rúnico | Material / Uso | `$65` | Uso direto: **`-15% Exposição`** \| Insumo de Crafting. |
| `sucata_eletronica` | Sucata Eletrônica | Material | `$55` | Componente de engenharia para Dispositivos, Filtros e Estimulantes. |
| `dispositivo_choque` | Dispositivo de Choque Rúnico | Combate | `$165` | Paralisa (`Stun`) e causa 30/50 de dano na Zona Vermelha. |
| `filtro_runico` | Filtro Rúnico de Bolso | Consumível | `$135` | Purifica `1x Sangue Adulterado` em `1x Sangue Filtrado`. |
| `gaze_consagrada` | Gaze Consagrada | Consumível | `$155` | `+40 HP` \| Estanca hemorragias e sequelas. |
| `dose_estimulante` | Dose Estimulante Rúnica | Consumível | `$175` | Amplia janela QTE (`+2.5s`) + `50% Esquiva`. |
| `cracha_falso` | Crachá Reserva de Monitor | Consumível | `$160` | **`-25% Exposição`** e apaga `rastro_olfativo_atual` fora de combate. |
| `ampola_prata` | Ampola de Prata Líquida | Combate | `$145` | Combate: reveste a lâmina (`+18 Dano`, ignora armadura `inorganico` e rompe guarda). |
| `tampao_hemostatico` | Coagulantes Sintéticos | Consumível | `$110` | `+20 HP` e remove Sangramento (em combate, também concede `+6 Defesa` durante a luta). |
| `incenso_mirra` | Incenso de Mirra & Enxofre | Consumível | `$130` | `1x/dia` (se `humanidade < 75`): **`-25 Tensão`** e **`+3 Humanidade`**. |
| `sais_vigilia` | Sais Alquímicos de Vigília | Consumível | `$125` | `1x/dia`: **`+1 Passo` neste turno** e `+15 HP` (`+10 Tensão`). |
| `amuleto_estanho` | Selo de Estanho Quebrado | Consumível | `$195` | **`-4% DOOM (Deterioração)`** ao custo de `+8 Tensão`. *(Vitrine Dia 5+).* |
| `presente_flores` | Buquê de Lírios Negros | Presente | `$85` | Presente (`1x/dia` por heroína). Dispara micro-evento `ev_presente_emilia_flores`. |
| `presente_perfume` | Perfume Âmbar & Sândalo | Presente | `$135` | Presente (`1x/dia` por heroína). Dispara micro-evento `ev_presente_lility_perfume`. |
| `presente_colar` | Colar de Prata & Granada | Presente | `$175` | Presente (`1x/dia` por heroína). Dispara micro-evento `ev_presente_elara_colar`. |
| `presente_roupa` | Traje Fino / Jaqueta Sob Medida | Presente | `$220` | Presente (`1x/dia` por heroína). Dispara micro-evento `ev_presente_valeria_roupa`. |
| `presente_anel` | Anel de Ônix & Selo Prateado | Presente | `$260` | Presente de compromisso. Se `afeto >= 6` (1ª entrega), dispara `ev_presente_anel_pacto`. |
| `partitura_runica` | Partitura Rúnica | Relíquia | `$0` | Relíquia obtida no Caso *Partitura Carnal*; permite oferenda magna no covil de Lility. |
| `relicario_sangue` | Relicário de Sangue Puro | Relíquia | `$0` | Artefato ligado ao Cofre de Contenção do Grêmio e ao Clímax. |
| `chave_contencao` | Chave de Contenção | Relíquia | `$0` | Acesso/relíquia das câmaras subterrâneas profundas (`fragmentos_chave_cripta` 3/3 para a Cripta). |
| `grimorio_corte` | Páginas do Corte do Vínculo | Relíquia | `$0` | Transcrição de Lorde Phillip (`ritual_corte_vinculo_desbloqueado`); habilita **Finais B e C**. |

---

## 7. TABELA DE LOOT POR SETOR (`loot_aleatorio_bs`) & RENDAS ALTERNATIVAS

### 7.1 Drops de Exploração (`label loot_aleatorio_bs`)

| Setor(es) | Itens & Chances Exatas no Código |
| :--- | :--- |
| **`dormitorio`** | 60% `+1 Sucata Eletrônica` \| 40% `+1 Kit de Curativos` *(Dormitório não gasta passo; drop herdado da rotina geral).* |
| **`biblioteca`, `sala_ocultismo`** | 60% `+1 Giz de Proteção Rúnico` \| 40% `+1 Conhecimento Oculto` (pista censurada). |
| **`caldeiras`, `sala_caldeiras`, `bar_fada_verde`** | 35% `+1 Sucata Eletrônica` \| 25% `+$30 a $65` \| 20% `+1 Dose de Absinto` \| 20% `+1 Sangue Adulterado`. |
| **`catacumbas`** *(Prioridade Chave)* | Se `fragmentos_chave_cripta < 3`, **60% de chance** de achar Peça `1/3`, `2/3` ou `3/3` (desbloqueia `cripta_cofre`). Caso contrário, entra na tabela abaixo. |
| **`cemiterio_nevoa`, `catacumbas`, `cripta_cofre`** | 30% `+$45 a $95` \| 25% `+1 Kit de Curativos` \| 20% `+1 Giz Rúnico` \| 25% `+1 Sangue Adulterado`. |
| **`patio_arvore`** | 42% `+1 Giz de Proteção` \| 30% `+$30 a $75` \| 18% `+1 Kit de Curativos` \| **10% `+1 Buquê de Lírios Negros`**. |
| **`rua_portao`** | 40% `+1 Sucata Eletrônica` \| 30% `+$40 a $90` \| 15% `+1 Dose de Absinto` \| 15% `+1 Kit de Curativos`. |
| **Demais Setores (Pátio, Grêmio, Portões, Sala de Música, etc.)** | 50% `+$35 a $80` \| 50% `+1 Giz de Proteção Rúnico`. |
| **Perk `olhos_no_escuro`** | Bônus adicional de **`+$15 a $35`** ao vasculhar. |

### 7.2 Rendas, Tributos & Sistema de Presentes Clandestinos
- **Carteira Inicial:** **`$200`** no início da campanha (`dinheiro_jogador`).
- **Relatórios Políticos a Elara (`salao_gremio`):** `+$120` (ou **`+$240`** no clima **Inspeção Rígida do Conselho**), limitado a **`1x/dia`** (`relatorio_entregue_hoje`), com retenção punitiva de **`-20%`** se `taxa_inadimplente` estiver ativa. A opção *"Prestar Contas / Inspeção de Conduta"* (`-15% Exposição`) também passa a ser **`1x/dia`** (`inspecao_elara_hoje`).
- **Combate & Hold-Up (`combate.rpy` & `emboscada_aleatoria_bs`):**
  - *Extorquir no Hold-Up:* Rende **`+$55 a $105`** + bolsa sorteada (**`40%` Filtrada / `60%` Adulterada**) e **suprime** o saque monetário duplicado pós-batalha (`extorquiu_combate_atual`).
  - *Espólio pós-batalha normal:* Rende **`+$30 a $75`** (humanos/grêmio) ou **`+$25 a $55`** (`corrompido`/`inorganico`).
- **Cobrança Periódica do Conselho (`evento_cobranca_taxa_academica` — a cada 6 períodos):** Exige **`$135`** se `divida_monitores > 0` ou **`$100`** caso contrário. Quitação à vista, acordo corporal (`40%` em dinheiro min `$20` + `-15 HP` seguro `>=20` + `+8 Tensão`) ou inadimplência (`+10% Exposição` com teto seguro `<75%`, `+12 Tensão`, `-2 Humanidade`, sequela `taxa_inadimplente` e reabertura de `divida_taxa_atrasada` no Livro de Dívidas).
- **Presentes Clandestinos (`fluxo_entregar_presente_heroina`):** Acessível nos encontros das 4 heroínas e nos dormitórios de Emília/Lility (`1x/dia por heroína`; entregas repetidas do mesmo item rendem no máximo `+1 Afeto`). Contém **20 reações exclusivas** e **5 micro-eventos** (`ev_presente_emilia_flores`, `ev_presente_lility_perfume`, `ev_presente_elara_colar`, `ev_presente_valeria_roupa` e `ev_presente_anel_pacto`).
