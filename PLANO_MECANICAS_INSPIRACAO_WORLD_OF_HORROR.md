# ==============================================================================
# GUIA MESTRE DE DESIGN DE TENSÃO, HORROR INVESTIGATIVO E MECÂNICAS
# "THE HUNGER & THE HALLWAYS" × "WORLD OF HORROR (PANSTASZ)"
# Análise de Engenharia Narrativa: Como a Progressão de Tensão Implacável
# e os Mistérios Modulares Elevam o Terror Gótico da Academia
# ==============================================================================

## 1. O DIAGNÓSTICO: POR QUE "WORLD OF HORROR" É UMA OBRA-PRIMA DA TENSÃO?

Criado pelo desenvolvedor e dentista polonês **Paweł Koźmiński (panstasz)** e distribuído pela Ysbryd Games, *World of Horror* (WoH) é universalmente aclamado como o ápice da tradução do terror cósmico/lovecraftiano e do mangá de horror psicológico de **Junji Ito** para a linguagem de videogames.

A tensão de *World of Horror* não vem de *jumpscares* baratos; ela é construída por meio de uma **pressão mecânica asfixiante e deliberada**:

---

### 1.1 O Relógio Implacável da Ruína (The Inexorable DOOM Clock)
Em praticamente todos os RPGs convencionais, o jogador pode pausar, explorar infinitamente cada canto do mapa, curar-se e acumular recursos sem pressa. Em *World of Horror*, **o tempo é um recurso escasso e impiedoso**:
* Cada ação investigativa, cada movimento entre bairros, cada feitiço lançado e cada rodada prolongada de combate adiciona **+1% a +5% de DOOM**.
* Se o DOOM atingir **100%**, o Deus Antigo desperta em sua totalidade, a cidade de Shiokawa é tragada pelo abismo e a partida termina em Game Over imediato.
* **O Efeito Psicológico:** O jogador está em um constante dilema de escassez. Tomar banho para recuperar sanidade? Custa +5% de Doom. Comprar armas no mercado? Custa tempo e Doom. Salvar um colega ferido? Custa Doom. O jogador nunca se sente seguro.

---

### 1.2 Degeneração em Cascata do Cenário (Milestone World Degradation)
O avanço do DOOM não é apenas um número abstrato no canto da tela; **o mundo ao redor do jogador apodrece à medida que o fim se aproxima**:
* Em marcos críticos (ex: 20%, 40%, 60%, 80% de Doom), o jogo aplica **Efeitos Globais da Cidade (Town Status)**:
  * Os preços das lojas dobram porque a população entra em histeria e esvazia as prateleiras.
  * O hospital corta suprimentos de medicamentos.
  * A água encanada passa a sair com gosto de ferrugem e sangue.
  * A polícia passa a abordar o protagonista com agressividade paranóica.
* Isso garante que a segunda metade da partida seja exponencialmente mais desesperadora que a primeira.

---

### 1.3 O Atrito Duplo Físico-Psicológico: Stamina (Corpo) vs. Reason (Mente)
WoH utiliza duas barras vitais simétricas:
1. **STAMINA (Vigor Físico / HP):** Esgotada por facadas, mordidas, venenos e ferimentos. Se chegar a 0, você morre de choque traumático.
2. **REASON (Sanidade Mental / SAN):** Esgotada ao testemunhar monstruosidades, ler grimórios proibidos, ouvir sussurros dos Deuses Antigos ou falhar em testes de terror. Se chegar a 0, você enlouquece completamente.
* **O Dilema Mecânico:** Muitas vezes, a escolha do jogador é: *"Aceito quebrar um osso (-3 Stamina) para manter minha mente sã, ou deixo minha mente contemplar o abismo (-3 Reason) para manter meu corpo ileso?"*

---

### 1.4 A Arquitetura Modular de Lendas Urbanas (The Mystery Board)
Ao invés de uma história linear única e previsível, cada jornada em WoH é composta por **5 Mistérios Independentes (Casos / Lendas Urbanas)** sorteados de uma vasta biblioteca:
* Exemplos canônicos:
  * *Tragic Tale of the Thaumaturgy Teacher* (A professora possuída que desenha portais na lousa).
  * *Macabre Memoir of Morbid Mermaids* (O zelador louco que mutila estudantes para costurar caudas de peixe).
  * *Sorrowful Saga of the Scissor Lady* (A lenda urbana da Kuchisake-onna assombrando a escola).
* **Estrutura de cada Mistério:**
  1. **Introdução / Rumor:** A manchete do jornal ou o sussurro nos corredores.
  2. **Etapas de Investigação:** Explorar nós de mapa procurando pistas específicas.
  3. **Finais Múltiplos (Ending A, B, C, D):** Dependendo dos itens coletados, pistas decifradas ou aliados sacrificados, o mistério tem desfechos completamente diferentes (salvar as crianças, queimar a escola, ser amaldiçoado ou condenar a si mesmo).
  4. **A Chave do Farol:** Resolver cada mistério concede uma chave para entrar no Farol onde o ritual final está sendo selado.

---

### 1.5 Sequelas e Maldições Cumulativas (Injuries & Curses)
O combate e os eventos não subtraem apenas números; eles deixam **marcas tangíveis no personagem**:
* **Ferimentos Graves (Injuries):** *Costela Quebrada* (-Ataque), *Tendão Cortado* (-Velocidade de esquiva), *Olho Furado* (-Percepção).
* **Perturbações Mentais (Curses & Status):** *Paranoia* (losing Reason raises Doom), *Insônia* (não recupera HP ao dormir), *Alucinações* (falsos inimigos no mapa).
* Isso cria cicatrizes narrativas reais ao longo dos dias.

---

## 2. A TRANSLIGAÇÃO COM "THE HUNGER & THE HALLWAYS"

| Pilar de Tensão em World of Horror | Equivalente em The Hunger & The Hallways | Impacto Dramático no Terror Gótico |
| :--- | :--- | :--- |
| **Relógio de DOOM (0 a 100%)** | **Ruína do Sarcófago (`ruina_cain`)** | A cada dia e a cada quebra de máscara, o Deus Adormecido Cain se aproxima do despertar nas catacumbas. |
| **Stamina (HP Físico)** | **Vida de Victor (`hp_jogador`)** | A integridade física do bolsista contra as lâminas da Inquisição e garras de aberrações. |
| **Reason (Sanidade Mental)** | **Humanidade vs. Tensão Psicológica** | O conflito interno de Victor entre preservar sua alma humana ou ceder à Besta Vermelha. |
| **Degeneração da Cidade (Town Status)** | **Degeneração da Academia (`status_escola`)** | Blecautes no subsolo, toque de recolher draconiano do Grêmio, água das torneiras com sangue, histeria estudantil. |
| **Mistérios e Lendas Urbanas** | **Os 5 Rumores das Alas Proibidas** | Casos como *Hachishaku-sama*, *A Loira do Banheiro*, *O Lote Necrótico das Caldeiras* e *A Partitura de Lility*. |
| **As Chaves do Farol** | **As 5 Relíquias do Selamento de Cain** | Resolver os mistérios da escola concede os talismãs necessários para a Batalha do Dia 21 no sarcófago. |
| **Injuries & Curses** | **Sequelas de Predação & Paranoias Vampíricas** | Queimaduras de prata, estresse pós-combate, presas hipersensíveis e delírios olfativos. |

---

## 3. AS NOVAS MECÂNICAS PROPOSTAS PARA IMPLEMENTAÇÃO

---

### 3.1 MECÂNICA 1: O RELÓGIO DA RUÍNA DA CRIPTA (`ruina_cain` / DOOM SYSTEM)

No modelo atual, a história avança do Dia 1 ao 21 através do calendário diário. Para incorporar a genialidade de WoH, introduzimos a variável global **`ruina_cain` (0% a 100%)**, que mede a ressonância profana do sarcófago subterrâneo.

#### Como a Ruína Sobe:
* Cada transição de período normal: `+1% a +2%`.
* Entrar em **Frenesi de Sangue** (abaixo de 20% de fome): `+5% de Ruína`.
* Sofrer penalidade de **Exposição da Máscara** acima de 80%: `+4% de Ruína`.
* Matar ou drenar um estudante inocente nos corredores: `+3% de Ruína`.
* Falhar em testes de horror em micro-eventos: `+2% de Ruína`.

#### Degraus de Colapso da Academia (Milestone Thresholds):
1. **0% a 24% (Normalidade Inquieta):**
   * A escola aparenta normalidade. Alunos conversam sobre provas e aulas.
2. **25% a 49% (Primeira Rachadura):**
   * *Efeito:* Murmúrios nos canos. Os preços da loja de Valéria aumentam em 20% (custo de contrabando elevado).
   * Alunos começam a faltar às aulas. Pequenos animais mortos aparecem no pátio da fonte.
3. **50% a 74% (A Máscara Trincada):**
   * *Efeito:* O Conselho Estudantil decreta **Toque de Recolher Rígido**. Executores de Elara patrulham os corredores; entrar em qualquer ala sem salvo-conduto gera teste de Furtividade/Domínio.
   * As lâmpadas dos corredores piscam em tons vermelhos; a água das pias tem gosto de ferro.
4. **75% a 99% (Histeria Pré-Diluviana):**
   * *Efeito:* O subsolo entra em colapso. Névoa fétida sobe pelos ralos. Calouros choram trancados nos armários.
   * Todos os inimigos nas Zonas Amarela e Vermelha ganham **+20% de Dano**.
   * Victor ouve batimentos cardíacos colossais constantes (`audio/heartbeat.ogg`) ecoando sob seus pés.
5. **100% (Despertar Prematuro do Deus Adormecido):**
   * Gatilho de fim catastrófico antecipado ou boss fight desesperada nas catacumbas antes do Dia 21!

---

### 3.2 MECÂNICA 2: O QUADRO DE LENDAS URBANAS (MYSTERY BOARD DA ACADEMIA)

Inspirado diretamente na tela de investigação de *World of Horror*, a escola de São Cipriano possui **5 Grandes Mistérios Investigativos**. Cada um funciona como uma cadeia autônoma de pistas com múltiplos desfechos:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    QUADRO DE MISTÉRIOS DE SÃO CIPRIANO                          │
│                                                                                 │
│  [1] 👻 A MULHER DE 8 PÉS           [2] 🪞 O ESPELHO DA LOIRA DO BANHEIRO       │
│      Ala Antiga / Zona Vermelha          Banheiro Feminino do 3º Andar          │
│      Progresso: 2/3 pistas               Progresso: 0/3 pistas                  │
│      Status: RASTRO ATIVO                Status: NÃO INICIADO                   │
│                                                                                 │
│  [3] 🧪 O LOTE NECRÓTICO            [4] 🎹 A PARTITURA CARNAL                   │
│      Caldeiras & Subsolo                 Sala de Música / Covil                 │
│      Progresso: 3/3 [RESOLVIDO: A]       Progresso: 1/3 pistas                  │
│      Recompensa: Chave Rúnica α          Status: INVESTIGANDO                   │
│                                                                                 │
│  [5] 📜 OS ARQUIVOS DA INQUISIÇÃO (Gabinete da Presidência & Cofre)             │
│      Progresso: 1/4 pistas | Requer Aliança Política com Elara ou Emília        │
└─────────────────────────────────────────────────────────────────────────────────┘
```

#### Os 5 Mistérios Estruturados (Estilo WoH):

#### Caso 1: "O Terror da Mulher de Oito Pés (Hachishaku-sama)"
* **Sinopse:** Uma entidade colossal com chapéu de palha e risada abafada (*"Po... Po... Po..."*) ronda as janelas do 2º andar, atraindo estudantes bolsistas para fora das janelas.
* **Passos Investigativos:**
  1. Encontrar o chapéu ensanguentado no telhado do pátio (Teste de `Sensibilidade`).
  2. Entrevistar o calouro sobrevivente na enfermaria (Teste de `Charme` ou suborno de `$30`).
  3. Confrontar a entidade na Ala Antiga à noite.
* **Finais Alternativos:**
  * **Final A (Exorcismo Rúnico):** Usando *Giz de Proteção* nos quatro cantos da sala, Victor aprisiona a entidade e obtém a **Relíquia do Sal Consagrado** (-15% Ruína de Cain).
  * **Final B (Banquete Monstruoso):** Victor a destrói em combate corpo a corpo e devora sua essência (+50 Saciedade, mas +10% Ruína e -5 Humanidade).
  * **Final C (Fuga Covarde):** O calouro é levado; Victor foge traumatizado (+10 Tensão / +1 Maldição de Paranoia).

#### Caso 2: "O Enigma do Espelho Trincado (A Dama do Banheiro)"
* **Sinopse:** Alunos que batem três vezes na última cabine do banheiro do 3º andar à meia-noite veem reflexos de suas próprias mortes.
* **Finais Alternativos:**
  * **Final A (A Revelação Oculta):** Victor decifra os símbolos de sangue no vidro com `Intelecto >= 14`, obtendo a **Chave de Contenção de Espelhos**.
  * **Final B (Possessão Trágica):** O espelho quebra e estilhaça, causando a sequela *Cortes Profundos* (-15 HP Max até ser tratado por Emília).

#### Caso 3: "O Lote Necrótico das Caldeiras"
* **Sinopse:** Bolsas de sangue adulteradas com resíduos alquímicos estão transformando operários do subsolo em carcaças canibais.
* **Finais Alternativos:**
  * **Final A (Sindicato Sombrio):** Aliança com Valéria para purificar a linha de produção (Habilita a compra da *Bolsa de Sangue Filtrado Puro*).
  * **Final B (Queima de Arquivo):** Destruir os registros com dispositivo incendiário (+15% Exposição, mas fecha a rota da Inquisição).

#### Caso 4: "A Partitura Carnal da Sala de Música"
* **Sinopse:** Um réquiem composto por Lility em 1888 que faz as veias de quem o ouve vibrarem até romperem.
* **Finais Alternativos:**
  * **Final A (Execução Perfeita):** Victor toca a peça sem errar notas com `Sensibilidade >= 15`, acalmando a sede da Mestra (+20 Afeto com Lility).
  * **Final B (Dissonância Carmesim):** As cordas do piano arrebentam, cortando as mãos de Victor (Sequela *Dedos Mutilados*: -2 em combate por 3 dias).

#### Caso 5: "O Inquérito Negro de Lorde Phillip"
* **Sinopse:** A lista confidencial dos estudantes marcados para "doação forçada" na enfermaria da Inquisição.
* **Finais Alternativos:**
  * **Final A (Vazamento Estratégico):** Victor entrega os documentos a Emília, destruindo a fé cega dela no próprio pai e consolidando o Pacto de Sangue.
  * **Final B (Chantagem Política):** Victor confronta Elara com as provas, reduzindo a vigilância do Grêmio a zero.

---

### 3.3 MECÂNICA 3: MICRO-EVENTOS PROCEDURAIS DE CORREDOR (ESTILO `.ITO`)

Cada vez que Victor explora um setor da escola durante seu turno, além do menu de heroínas, o jogo pode disparar um **Micro-Evento com Teste de Perícia**:

#### Estrutura Técnica de um Evento `.ito` em Ren'Py:
```renpy
# Exemplo de Micro-Evento adaptado da sintaxe de World of Horror:
label evento_woh_sala_professores_vazia:
    $ renpy.play("audio/heartbeat.ogg")
    scene bg corredor_noite_escuro with dissolve
    "A porta da Sala dos Professores está entreaberta. Um cheiro acre de folhas queimadas e café frio vaza pelo vão."
    "Sobre a mesa de centro, uma maleta de couro repousa sob a luz tênue do poste externo. As fivelas de prata estão cobertas de fuligem fresca."

    menu:
        "🔍 Forçar a tranca com um clipe de metal (Teste de Intelecto / Destreza)":
            $ sucesso, diff = testar_pericia_rpg("intelecto", dificuldade=12)
            if sucesso:
                "Com um estalo suave, a fivela cede! Você encontra $60 em notas do Grêmio e um Frasco de Água Benta intacto."
                $ dinheiro_jogador += 60
                $ notificar_rpg("🎒 SAQUE BEM-SUCEDIDO", "+$60 e 1x Água Benta obtidos!", "#00ffcc")
            else:
                with hpunch
                "A trava dispara uma lâmina de contenção da Inquisição! O corte queima sua carne de ghoul. (-15 HP / +2% Ruína)"
                $ hp_jogador = max(1, hp_jogador - 15)
                $ ruina_cain = min(100, ruina_cain + 2)
                $ notificar_rpg("⚠️ ARMADILHA RÚNICA", "Você foi ferido por prata benta (-15 HP)!", "#ff4444")
            jump entrar_local_exploracao_bs

        "👁️ Sondar a sala com Visão Vampírica (Custo: 10% Saciedade de Sangue)":
            if fome_sangue >= 10:
                $ fome_sangue -= 10
                "Seus olhos ardem em carmesim. Você enxerga os fios mágicos de alarme ligados à maçaneta e os desativa com segurança."
                $ conhecimento_oculto += 1
                $ notificar_rpg("🔮 PERCEPÇÃO ABERRANTE", "Armadilha desarmada com sangue! (+1 Ocultismo)", "#ff66cc")
            else:
                "Sua sede é grande demais; suas presas doem e você não consegue focar o poder da besta."
            jump entrar_local_exploracao_bs

        "👣 Ignorar e seguir pelas sombras (Opção Cautelosa)":
            "Você engole a curiosidade e desliza rente à parede. Algumas portas neste colégio foram feitas para ficarem trancadas."
            jump entrar_local_exploracao_bs
```

---

### 3.4 MECÂNICA 4: SISTEMA DE SEQUELAS FÍSICAS & MALDIÇÕES MENTAIS (INJURIES & PARANOIAS)

Em *World of Horror*, a saúde não é uma mera barra que recarrega no dia seguinte. Victor acumula **Condições Especiais**:

#### Tabela de Sequelas Táticas:
| Nome da Condição | Tipo | Causa | Efeito Mecânico | Forma de Cura |
| :--- | :--- | :--- | :--- | :--- |
| **Queimadura de Prata** | Sequela Física | Toque em relíquias ou lâminas de caçadores | -15 HP Máximo; cura natural bloqueada. | Tratamento de Emília no Clube ou Bálsamo Alquímico de Valéria. |
| **Garganta Seca / Caninos Expostos** | Condição Predatória | Fome abaixo de 25% | -3 em testes de Charme com humanos; +10% Exposição se conversar. | Beber de Lility, Emília, Valéria ou Elara. |
| **Paranoia do Executor** | Maldição Mental | Exposição acima de 70% ou flagra de patrulha | +1% de Ruína ao mudar de andar; passos restantes do turno reduzidos em 1. | Tomar Dose de Absinto ou passar a noite descansando no Covil. |
| **Alucinação Auditiva (Eco de Cain)** | Maldição Mental | Ruína acima de 60% | Ouve batimentos cardíacos falsos; testes de Intelecto sofrem penalidade de -2. | Usar Partitura Rúnica com Lility ou banho quente. |
| **Faro Contaminado** | Condição Química | Beber de lote adulterado nas Caldeiras | Não detecta o cheiro das heroínas por 2 dias; perde bônus olfativo. | Comprar Filtro Alquímico de Valéria ($50). |

---

## 4. ARQUITETURA DE CÓDIGO PYTHON / REN'PY (IMPLEMENTAÇÃO COMPLETA)

Abaixo está a arquitetura modular pronta para ser inserida em `game/sistemas_world_of_horror.rpy`:

```python
# ==============================================================================
# SISTEMA WORLD OF HORROR: RUÍNA, MISTÉRIOS MODULARES E SEQUELAS
# ==============================================================================

init -1 python:
    class MisterioCaso:
        def __init__(self, id_caso, titulo, local_foco, pistas_totais, recompensa_nome):
            self.id = id_caso
            self.titulo = titulo
            self.local_foco = local_foco
            self.pistas_totais = pistas_totais
            self.pistas_coletadas = 0
            self.resolvido = False
            self.desfecho_final = None   # "A", "B", "C"
            self.recompensa_nome = recompensa_nome

        @property
        def progresso_texto(self):
            if self.resolvido:
                return f"RESOLVIDO (FINAL {self.desfecho_final})"
            return f"{self.pistas_coletadas}/{self.pistas_totais} Pistas"

        def coletar_pista(self):
            if not self.resolvido:
                self.pistas_coletadas = min(self.pistas_totais, self.pistas_coletadas + 1)
                notificar_rpg("🔍 PISTA ENCONTRADA", f"{self.titulo}: ({self.pistas_coletadas}/{self.pistas_totais})", "#ffcc00")
                if self.pistas_coletadas >= self.pistas_totais:
                    notificar_rpg("🗝️ CLÍMAX DO MISTÉRIO", f"Confronto final disponível em {self.local_foco}!", "#ff4444")

        def concluir(self, desfecho="A"):
            self.resolvido = True
            self.desfecho_final = desfecho
            notificar_rpg("🏆 CASO ENCERRADO", f"{self.titulo}: Desfecho {desfecho}! [{self.recompensa_nome}] obtido!", "#00ffcc")

    class GerenciadorRuina:
        @staticmethod
        def adicionar_ruina(qtd, motivo="Avanço das Sombras"):
            store.ruina_cain = min(100, store.ruina_cain + qtd)
            notificar_rpg("⚡ ECO DA CRIPTA", f"+{qtd}% Ruína de Cain ({store.ruina_cain}% Total) — {motivo}", "#ff2244")
            GerenciadorRuina.verificar_degraus()

        @staticmethod
        def reduzir_ruina(qtd, motivo="Ritual Sagrado"):
            store.ruina_cain = max(0, store.ruina_cain - qtd)
            notificar_rpg("🕊️ CONTENÇÃO RÚNICA", f"-{qtd}% Ruína de Cain ({store.ruina_cain}% Total) — {motivo}", "#66ff66")

        @staticmethod
        def verificar_degraus():
            r = store.ruina_cain
            if r >= 75 and not store.degrau_75_alertado:
                store.degrau_75_alertado = True
                store.status_escola = "histeria"
                renpy.notify("⚠️ AVISO: A Ruína atingiu 75%! Névoa fétida e histeria tomam os corredores!")
            elif r >= 50 and not store.degrau_50_alertado:
                store.degrau_50_alertado = True
                store.status_escola = "toque_recolher"
                renpy.notify("⚠️ AVISO: A Ruína atingiu 50%! O Grêmio decretou Toque de Recolher com Executores!")
            elif r >= 25 and not store.degrau_25_alertado:
                store.degrau_25_alertado = True
                store.status_escola = "inquietante"
                renpy.notify("⚠️ AVISO: A Ruína atingiu 25%! Murmúrios nos canos e preços aumentados.")
```

---

## 5. ROTEIRO DE INTEGRAÇÃO NO LOOP CENTRAL DO JOGO

1. **No HUD Principal (`hud_exploracao_bs`):**
   * Adicionar um medidor circular ou barra de pulso gótica para a **Ruína de Cain (`ruina_cain`)** ao lado da Saciedade de Sangue.
   * Adicionar um botão de atalho `"📋 Mistérios & Casos"` abrindo o quadro interativo de lendas urbanas.
2. **Nas Zonas de Exploração (Pátio, Caldeiras, Clube, Grêmio, Biblioteca):**
   * Inserir 1 a 2 micro-eventos aleatórios com escolhas de perigo antes de abrir os menus de diálogo com as personagens.
3. **Na Batalha do Dia 21 (O Sarcófago de Cain):**
   * Cada mistério resolvido (Final A) concede um talismã que enfraquece o chefe final em 15% de vida máxima e concede habilidades extras para as 4 heroínas.

---

## 6. CONCLUSÃO: O GANHO DRAMÁTICO E SENSORIAL

Ao fundir a **tensão inexorável de World of Horror** com o **triângulo de facções de Harem Heaven** e o **eixo duplo de intimidade de Love & Sex: Second Base**, *The Hunger & The Hallways* atinge um patamar único na ficção interativa:
* O colégio não é apenas um cenário estático de conversa fiada; é uma **bomba-relógio que está afundando a cada hora**.
* Cada mordida em Emília, Valéria, Elara ou Lility não é um mero colecionável de fetiche: é uma **necessidade biológica desesperada de sobrevivência** para manter a mente e o corpo funcionais diante de horrores ancestrais que rastejam pelas paredes.
