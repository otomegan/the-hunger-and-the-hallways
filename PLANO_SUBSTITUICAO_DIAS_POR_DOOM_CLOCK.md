# ==============================================================================
# GUIA DE TRANSIÇÃO E DESIGN: DOOM CLOCK × CALENDÁRIO FIXO
# "THE HUNGER & THE HALLWAYS" — A Influência do Despertar de Cain
# Substituindo os 21 Dias Rígidos por um Ritmo Dinâmico de DOOM (Estilo World of Horror)
# ==============================================================================

## 1. A JUSTIFICATIVA DE DESIGN: POR QUE MUDAR?

### 1.1 As Limitações dos "21 Dias Fixos":
No modelo original de 21 dias fixos:
1. **Início Apressado:** O jogador mal tem tempo de conhecer as quatro heroínas, entender o que é o Grêmio, as Caldeiras ou a Sala de Música, e os dias já estão sendo consumidos mecanicamente a cada período.
2. **Falta de Agência:** Não importa se o jogador joga de forma impecável (discreto, bem alimentado, estratégico) ou de forma imprudente (matando calouros na frente de todos, em frenesi constante); o jogo chegava ao clímax no mesmo "Dia 21".
3. **Ritmo Plano:** Um relógio de dias calendário convencional não transmite a sensação de horror cósmico crescente.

### 1.2 A Solução "DOOM Clock" (A Influência do Despertar de Cain):
Inspirado na genialidade de *World of Horror*:
* **O fim do jogo não é uma data arbitrária no calendário; é o despertar de Cain (DOOM = 100%).**
* **Ritmo Elástico:** O início (0% a 25% de Ruína) é cadenciado, calmo e atmosférico, permitindo ao jogador explorar a academia, interagir com Emília, Valéria, Elara e Lility, entender o combate e investigar mistérios.
* **Aceleração da Tensão:** À medida que a Ruína de Cain sobe (25% -> 50% -> 75% -> 100%), o ritmo dos eventos se torna vertiginoso, as penalidades se agravam e a escola se degenera fisicamente.
* **Recompensa por Competência:** Um jogador hábil que resolve casos de lendas urbanas, mantém a saciedade controlada e realiza rituais de contenção consegue adiar o DOOM, ganhando mais dias para aprofundar laços com as garotas e se armar com relíquias para o confronto final!

---

## 2. AS 4 FASES DA INFLUÊNCIA DE CAIN (A CURVA DE TENSÃO)

```
[0% ──────────── 25% ──────────── 50% ──────────── 75% ──────────── 100%]
   Fase I:          Fase II:         Fase III:        Fase IV:        CLÍMAX:
   O Sussurro       O Despertar      A Fratura        O Eclipse       A Ruptura
   Adormecido       da Carne         da Máscara       Iminente        do Sarcófago
 (Ritmo Calmo)   (Sinais Estranhos) (Toque Recolher) (Pânico Total)  (Boss Fight)
```

---

### FASE I: O SUSSURRO ADORMECIDO (DOOM 0% a 24%)
* **Clima:** A escola de São Cipriano aparenta normalidade aristocrática. O sol brilha no pátio da fonte; calouros fofocam nos corredores; as regras do colégio são convencionais.
* **Objetivo do Jogador:** Conhecer as 4 heroínas, entender seus gostos e fraquezas, aprender o sistema de combate, comprar os primeiros suprimentos com Valéria e descobrir os primeiros boatos de lendas urbanas.
* **Velocidade do DOOM:** Muito lenta. Passar um período em exploração normal adiciona apenas **+1% de Ruína**.
* **Fome & Saciedade:** A Besta Vampírica consome o sangue em ritmo lento (-5% por período).

---

### FASE II: O DESPERTAR DA CARNE (DOOM 25% a 49%)
* **Gatilho de Transição (25% DOOM):** O primeiro abalo sísmico nas fundações.
* **Clima:** Murmúrios inquietantes ecoam pelos canos de vapor. O gado escolar começa a adoecer; sangue de hospital começa a escassear.
* **Efeitos Mecânicos:**
  * Os preços da Loja de Valéria aumentam em 20% (histeria e risco de contrabando).
  * A Dúvida das heroínas sobe mais facilmente se Victor agir com desdém.
  * O avanço passivo do DOOM sobe para **+2% por período**.
* **Narrativa:** O primeiro mistério modular (ex: *O Lote Necrótico das Caldeiras* ou *A Loira do Banheiro*) entra em estágio crítico.

---

### FASE III: A FRATURA DA MÁSCARA (DOOM 50% a 74%)
* **Gatilho de Transição (50% DOOM):** O Grêmio Estudantil e a Inquisição declaram **Estado de Sítio na Academia**.
* **Clima:** Lâmpadas piscam em tons carmesins; a água das torneiras tem cheiro e gosto de ferro. Executores de uniforme branco patrulham com lâminas bentas e espadas rúnicas.
* **Efeitos Mecânicos:**
  * **Toque de Recolher Noturno:** Andar pelos corredores sem autorização aciona rondas de combate ou testes exigentes de Furtividade/Domínio.
  * A taxa de degradação da fome de Victor aumenta (-10% de Saciedade por período).
  * O avanço passivo do DOOM sobe para **+3% por período**.
  * Falhar em combates ou ser capturado por patrulhas adiciona **+4% de DOOM imediato**.

---

### FASE IV: O ECLIPSE IMINENTE (DOOM 75% a 99%)
* **Gatilho de Transição (75% DOOM):** A névoa da cripta vaza pelos bueiros do colégio.
* **Clima:** Pânico generalizado. Estudantes trancam-se nos dormitórios rezando ou entram em transes hipnóticos. Victor escuta batimentos cardíacos titânicos constantes (`audio/heartbeat.ogg`) ressoando sob o piso.
* **Efeitos Mecânicos:**
  * Todos os inimigos nas Zonas Amarela e Vermelha ganham **+20% de Dano**.
  * As quatro heroínas entram em diálogos de urgência dramática:
    * Emília quer fugir com Victor ou se sacrificar para fechar os portais.
    * Valéria tranca as caldeiras e vende suas armas mais letais.
    * Elara admite a perda de controle da Inquisição e cogita uma aliança proibida.
    * Lility se prepara para a quebra definitiva do sarcófago.
  * O avanço passivo do DOOM é de **+4% por período**.

---

### FASE V: O DESPERTAR DE CAIN (DOOM 100%)
* **O Clímax Definitivo:** O selo ancestral do sarcófago é destruído! A Esfera de Sangue se abre no céu sobre a academia.
* Dispara a batalha lendária contra **Cain, O Progenitor Faminto** nas catacumbas profundas (`label evt_d21_noite`).
* As relíquias obtidas ao resolver os 5 Casos de Lendas Urbanas enfraquecem Cain, e o nível de afeto/vínculo acumulado com cada heroína desbloqueia os Finais Canônicos (Consorte Imortal, Redenção com Emília, Trono com Elara, etc.).

---

## 3. AGÊNCIA DO JOGADOR: MECÂNICA DE ACELERAÇÃO E CONTENÇÃO ATIVA

O que torna esse sistema fascinante é que o jogador **pode controlar a velocidade do relógio**:

### Ações que Aceleram o DOOM (+Risco / Erros do Jogador):
* Entrar em **Frenesi de Ghoul** (fome < 20%): `+5% de DOOM`.
* Ser desmascarado / atingir 100% de Exposição: `+6% de DOOM`.
* Matar ou drenar estudantes inocentes nos corredores: `+3% de DOOM`.
* Perder um combate contra guardas da Inquisição: `+4% de DOOM`.
* Falhar em testes de terror nos micro-eventos: `+2% de DOOM`.

### Ações que Contêm e Reduzem o DOOM (-Alívio / Competência do Jogador):
* **Resolver um Caso de Lenda Urbana (Final A):** `-10% a -15% de DOOM` (um grande respiro na campanha!).
* **Orar e purificar com Emília:** `-3% de DOOM`.
* **Rituais de sonolência rúnica com Lility:** `-3% de DOOM`.
* **Auditoria e reforço de selos com Elara:** `-3% de DOOM`.
* **Descontaminar linhas de suprimento com Valéria:** `-2% de DOOM`.

---

## 4. O QUE MUDA NA INTERFACE E NO CÓDIGO

1. **No HUD Superior (`hud_sobrevivencia`):**
   * O texto `"📅 DIA X/21"` passa a ser `"📅 DIA X • SOBREVIVÊNCIA"`, registrando há quantos dias Victor está resistindo na escola.
   * O medidor de **`⚡ RUÍNA DE CAIN: [ruina_cain]%`** torna-se o termômetro principal do jogo, mudando de cor:
     * Azul/Branco (0-24%) ➔ Amarelo (25-49%) ➔ Laranja (50-74%) ➔ Vermelho Sangue Pulsante (75-100%).
2. **Na Transição de Turnos (`avancar_turno_mapa`):**
   * O DOOM sobe dinamicamente de acordo com a fase atual (Fase 1: +1%, Fase 2: +2%, Fase 3: +3%, Fase 4: +4%).
   * Se o DOOM atingir 100%, o jogo transita imediatamente para o clímax de Cain, sem esperar nenhum dia arbitrário.
3. **No Calendário de Eventos de História:**
   * Os grandes marcos narrativos deixam de ser escravos de um dia rígido e passam a disparar nos degraus de DOOM (25%, 50%, 75%) ou quando o jogador investigar as áreas correspondentes.

---

## 5. CONCLUSÃO

Essa substituição eleva *The Hunger & The Hallways* de um jogo com contagem regressiva artificial para um **thriller de sobrevivência cósmico-gótico interativo**:
* O jogador dita o próprio ritmo.
* Se quiser passar mais tempo com as garotas e explorar o castelo, ele precisa **trabalhar ativamente para conter a Ruína de Cain**.
* Se for imprudente e faminto, ele causará o Apocalipse muito mais rápido do que esperava!
