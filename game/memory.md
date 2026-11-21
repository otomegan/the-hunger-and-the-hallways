# MEMORY.md — Contexto Completo, Lore, Variáveis e Estado de "The Hunger & The Hallways"

Este documento contém a memória consolidada de design, lore, psicologia de personagens, inventário de variáveis e diretrizes técnicas do projeto. Consulte-o sempre antes de implementar novas cenas ou mecânicas.

---

## 1. PREMISSA CENTRAL E MITOLOGIA DO MUNDO

- **Logline:** *The Hunger & The Hallways* é uma visual novel de horror gótico e sobrevivência psicológica na qual **Victor Vane**, um bolsista transferido do interior transformado em lacaio vampírico (*Ghoul*) na noite do Dia 1, precisa administrar sua fome de sangue, navegar as intrigas políticas de uma academia isolada e decidir quanto de sua humanidade sacrificará enquanto uma força titânica adormecida deteriora a realidade (medida pelo **DOOM Clock**).
- **A Dinâmica do Tempo (DOOM Clock vs Contagem de Dias):**
  - O jogo **NÃO** possui um limite rígido de 21 dias.
  - A contagem de dias (`dia_atual`) avança livremente como métrica de sobrevivência e interesse para o jogador.
  - O verdadeiro ritmo da ruína e os grandes eventos da trama são governados pelo **DOOM Clock (0% a 100%)**:
    - **DOOM 30%:** Primeira fratura sobrenatural visível e aumento da histeria coletiva.
    - **DOOM 50%:** Baile de Máscaras e imposição de toque de recolher estrito.
    - **DOOM 70%:** Conflito aberto e incursão ao Cofre Subterrâneo.
    - **DOOM 85%:** Véspera do colapso / Lei marcial no campus.
    - **DOOM 100%:** Clímax: O Eclipse Total e o Despertar da Entidade Subterrânea.
  - Ações bem-sucedidas (conter anomalias, resolver lendas urbanas, purificar contaminações) reduzem o DOOM, dando mais dias ao jogador. Erros, frenesi e quebra de sigilo aceleram o avanço do DOOM.
- **O Segredo das Profundezas (Cain):**
  - **REGRA DE OURO:** O nome e a identidade de **Cain** NUNCA devem ser revelados prematuramente, nem no prólogo, nem na interface/HUD, nem em notificações.
  - O jogador descobre que algo colossal está despertando sob a escola devido aos tremores, contaminações e histeria. A identidade do Progenitor Faminto é um mistério conquistado por meio de investigação profunda próximo do clímax.
- **A Ferida Psicológica de Victor Vane:**
  - Na antiga universidade, Victor confiou cegamente em seu mentor acadêmico, que o traiu e o fez levar a culpa sozinho por uma fraude para salvar o próprio nome.
  - O trauma central de Victor é **o pavor visceral de dever favores, ser descartado ou depender da bondade alheia**.
  - Suas anotações pessoais definem regras estritas de sobrevivência (Regra 1: nunca assinar sem ler; Regra 2: desconfiar de quem sorri antes de pedir; Regra 3: nunca ser o último a saber; Regra 4: nunca ser descartável).

---

## 2. ELENCO PRINCIPAL E DINÂMICAS DE RELACIONAMENTO

1. **Victor Vane (`protagonist`):**
   - Possui 3 fases visuais dinâmicas baseadas no nível de `humanidade`:
     - **Fase 1 (`humanidade >= 65`):** Estudante Humano (olhar são, empatia preservada).
     - **Fase 2 (`35 <= humanidade < 65`):** Lacaio Desgastado (olheiras marcadas, palidez, sede constante).
     - **Fase 3 (`humanidade < 35`):** Predador Carmesim (instinto monstruoso dominante, olhos brilhantes).
     - **Frenesi (`fome_sangue < 20`):** Perda iminente de controle racional, instinto de caça ativado.
2. **Lility (`mestra` — A Criadora Confinada):**
   - Vampira nobre confinada na abandonada Sala de Música pelo **Grilhão de Sangue** imposto por Elara.
   - **Mistério da Idade:** Lility **NÃO** revela sua idade ancestral nem sua história para Victor. Quando questionada sobre visões de eras passadas ou águas profundas vislumbradas no Transe, desconversa com sarcasmo aristocrático e superioridade defensiva.
   - **Psicologia:** Trata Victor formalmente como lacaio ("cachorrinho"), mas divide com ele uma solidão profunda. A conexão sensorial do Transe de Sangue permite que ambos acessem fragmentos traumáticos da mente um do outro.
   - **Covil:** Após o primeiro transe no Dia 2, a Sala de Música torna-se o refúgio seguro de alimentação de Victor.
3. **Presidente Elara (`elara` — Conselho Estudantil / A Máscara):**
   - Vampira aristocrata de cabelos platinados, olhos carmesins e uniforme branco impecável.
   - **A Máscara:** Mantém o controle absoluto sobre o campus e pune com execução qualquer exposição aos mortais.
   - **O Dilúvio e o Segredo Ancestral:** Elara **NÃO** relata toda a história do Dilúvio de imediato; faz apenas advertências crípticas sobre ancestrais descuidados que foram "corrigidos pela água", deixando a verdade para ser descoberta pelo jogador.
   - **O Termo do Grilhão:** No Dia 2 manhã, submete Victor a um julgamento tenso, forçando-o a assinar o termo de conduta que ata a disciplina dele ao sofrimento físico de Lility.
4. **Emília von Karsten (`emilia` — A Exorcista Bolsista):**
   - Filha de uma linhagem de caçadores. Usa o uniforme preto dos estudantes comuns, frequenta a Biblioteca e o Clube de Ocultismo.
   - **Investigação:** Monitora a campanha semestral de doações de sangue e mapeia os desaparecimentos de alunos.
   - **Dilema:** É a personagem mais compassiva com Victor, mas se `duvida_emilia` se elevar enquanto a humanidade dele cai, ela pode se tornar sua caçadora mais implacável.
5. **Valéria (`valeria` — Turma do Fundão / Mercado Negro das Caldeiras):**
   - Mercadora cínica, pragmática e destemida instalada nos porões aquecidos pelas caldeiras.
   - Negocia bolsas filtradas puras, gazes, chaves mestras e informações sem julgamentos morais, desde que haja pagamento.

---

## 3. ESTRUTURA DO PRÓLOGO E DO ATO I

- **Abertura:**
  1. Vídeo de introdução atmosférico seguido de tela preta.
  2. Victor acorda sobressaltado em seu quarto com o pesadelo de Lility chorando e lhe estendendo a mão (`cena victor pesadelo 1` e `cena victor pesadelo 2`).
  3. Monólogo reflexivo: Victor nota que o sonho é recorrente, mas tenta se convencer de que é apenas estresse pela nova vida, deixando para trás a traição e a miséria de sua cidade natal.
  4. Viagem de trem-bala em direção à capital (`cena victor trem bala`), dividido entre a ansiedade e a determinação de vencer.
  5. Chegada diante dos portões monumentais da Academia São Cipriano (`cena victor portoes academia`), engolindo em seco mas encarando o destino de frente.
- **A Noite do Dia 1:**
  - Encontro e ataque de Nora na ala interditada (`cena quase morte nora`).
  - Lility surge das sombras, ajoelha-se diante de Victor à beira da morte e realiza o pacto de sangue (`cena quase morte encontra lility`, `cena quase morte lility ajoelha`, `cena quase morte lility proposta sangue`).
- **O Dia 2 (Desacoplamento e Exploração Aberta):**
  - **Manhã:** Audiência perante Elara no Gabinete da Presidência (`evt_d02_manha`), assinatura do Termo do Grilhão.
  - **Liberação Imediata do Mapa:** Ao cruzar as portas do Gabinete, o mapa tático é desbloqueado (`modo_exploracao_livre = True`, `passos_restantes_periodo = 3`, `jump abrir_mapa_tatico`).
  - **Estrutura Modular:** Não há mais cenas sequenciais obrigatórias. Cada local aciona seu evento próprio somente na visita do jogador:
    - *Sala de Música:* `evento_primeiro_transe_lility` (primeira alimentação e desbloqueio do covil).
    - *Banheiro Abandonado:* `evento_loira_banheiro_anomalia` (combate de anomalia contra a Loira do Banheiro, -12% DOOM).
    - *Biblioteca:* `evento_emilia_caderno_doacoes_dia2` (análise do caderno de doações de sangue).
    - *Caldeiras:* `evento_conhecer_valeria_caldeiras` (abertura do mercado clandestino de suprimentos).

---

## 4. DIRETRIZES TÉCNICAS E BOAS PRÁTICAS

### 4.1 Sintaxe de Menus no Ren'Py
- **Regra das Aspas:** Em blocos `menu:`, nunca utilize aspas duplas retas desprotegidas dentro da string da opção. Utilize SEMPRE aspas tipográficas (`“...”`):
  ```renpy
  menu:
      "“Porque eu não fujo de dívidas. E me recuso a ser descartado de novo.” (+Coragem)":
          $ coragem += 1
  ```
  Isso previne o erro de compilação `expected ':' not found`.

### 4.2 Sincronização entre Arquivos
- Qualquer alteração realizada em `game/script.rpy` DEVE ser replicada integralmente no arquivo de trabalho do usuário `c:\Users\otome\Downloads\ato1_rework.rpy`.

### 4.3 Gestão de Imagens e Displayables
- Sempre que criar novos nomes ou atalhos para imagens, declare os aliases apropriados em `game/definitions.rpy`.
- Nomes de arquivos contendo acentos (ex: `cabeça`) devem possuir aliases sem acento (ex: `cabeca`) para evitar inconsistências no linter e em diferentes sistemas operacionais.

### 4.4 Combate e Balanceamento
- Vitórias sobre lendas urbanas e anomalias diminuem a taxa de DOOM (ex: derrotar a Loira do Banheiro reduz 12% de ruína).
- O combate calcula bônus por atributos de Victor (`coragem`, `intelecto`, `ressonancia_pre_diluviana`) e reduz a vida do inimigo com feedback visual e sonoro condicional (`renpy.loadable`).

---

## 5. ARQUITETURA DO LOOPING DE GAMEPLAY APROVADA

- **Micro-Loop (Turno / Período: 3 Passos):**
  - Cada período (Manhã, Tarde, Noite) concede 3 Pontos de Ação (AP) para escolher salas no mapa tático.
  - Ações no passo: Encontro com Heroína (50%), Interação com Figurante (*Mobu Kyara* - 35% a 60%), Emboscada na Zona Vermelha (10% a 65%), Coleta de Loot (Sucata/Giz) ou Pistas de Lendas Urbanas.
- **Meso-Loop (Ciclo Diário):**
  - *Manhã:* Manutenção de fachada social, recuperação de paciência das heroínas, coleta de boatos civis.
  - *Tarde:* Negócios e crafting nas Caldeiras com Valéria, agendamento de encontros clandestinos.
  - *Noite:* Período de alto risco com aumento de anomalias, execuções do Conselho, encontros íntimos e incursões subterrâneas.
- **Macro-Loop (Sobrevivência contra o DOOM):**
  - O DOOM Clock avança passivamente a cada período (+1% a +3%).
  - Resolver os 5 Casos de Lendas Urbanas (*World of Horror*) com 3 pistas e derrotar anomalias reduz o DOOM em 5% a 15%, comprando mais dias.
  - Atingir thresholds (30%, 50%, 70%, 85%, 100%) dispara os grandes eventos canônicos da trama.
- **As 5 Atividades Centrais:**
  1. *Trilema da Alimentação:* Bolsas filtradas (seguro/caro) vs. Predação de figurantes (grátis/arriscado) vs. Covil de Lility (místico/dependência).
  2. *Investigação de Lendas Urbanas (Os 5 Casos Totalmente Conectados):*
     - Cada caso possui 3 pistas distribuídas organicamente nas ações de "Vasculhar" das salas temáticas:
       • **Loira do Banheiro:** Banheiro Abandonado (Confronto no Espelho com halo de batom ➔ -12% DOOM).
       • **A Mulher de Oito Pés (Hachishakusama):** Cemitério da Névoa / Pátio (Confronto na Névoa à Noite ➔ -12% DOOM).
       • **O Lote Necrótico:** Caldeiras / Bar da Fada Verde (Confronto com Alquimista Renegado ➔ +$120, +1 Bolsa, +Afeto Valéria, -12% DOOM).
       • **A Partitura Carnal:** Sala de Música / Biblioteca (Confronto com Marionete de Fios no Piano com Lility ➔ +Partitura Rúnica, +Afeto Lility, -12% DOOM).
       • **Os Arquivos Mortos:** Salão do Grêmio / Ocultismo (Confronto com Inquisidor Tático ➔ +Arquivos Confidenciais, Emília sabe a verdade, -12% DOOM).
  3. *Rotina Clandestina & Toque Sensorial:* Agendamento de encontros noturnos, gestão de paciência e minigame tátil.
  4. *Engenharia de Hardware & Mercado Negro:* Coleta de sucata/giz ➔ crafting de dispositivos de choque e filtros nas Caldeiras.
  5. *A Máscara & Burocracia Política:* Prestar contas a Elara, espionagem interna e controle de Exposição.



---

## 6. BANCADA DE CRAFTING EXPANDIDA & SISTEMA DE ITENS TÁTICOS

- **Local de Acesso Primário:** Bancada de Manutenção e Hardware nas Caldeiras (`bancada_crafting`), acessada diretamente via botão tático quando Victor está nas Caldeiras, e em atalhos de inventário (`central_feniks_expandida` e `inventario_tatico`).
- **As 4 Receitas Oficiais e Seus Impactos:**
  1. **Dispositivo de Choque Rúnico (`dispositivo_choque`):**
     - *Receita:* 1x Sucata Eletrônica + 1x Giz de Proteção.
     - *Impacto:* Causa 30 de dano direto em combate e atordoa o oponente, cancelando seu próximo contra-ataque sem gastar o turno do jogador.
  2. **Filtro Rúnico de Bolso (`filtro_runico`):**
     - *Receita:* 1x Sucata Eletrônica + 1x Giz de Proteção.
     - *Impacto:* Transforma 1x Bolsa de Sangue Adulterado (encontrada no lixo/caldeiras/catacumbas) em 1x Bolsa de Sangue Filtrado Puro (+35% Saciedade) sem contaminação, preservando a Humanidade e a discrição.
  3. **Gaze Consagrada (`gaze_consagrada`):**
     - *Receita:* 1x Kit de Curativos + 1x Giz de Proteção.
     - *Impacto:* Cura +40 HP (vida) no inventário ou durante o combate e sela ferimentos e hemorragias sobrenaturais instantaneamente.
  4. **Dose Estimulante Rúnica (`dose_estimulante`):**
     - *Receita:* 1x Sucata Eletrônica + 1x Dose de Absinto.
     - *Impacto:* Desacelera a percepção sensorial de Victor, concedendo `+2.5s` extras no timer QTE e 50% de chance de esquiva completa contra o próximo golpe inimigo.
- **Ciclo de Coleta e Utilidade do Loot:**
  - Armários e frestas de Dormitório, Caldeiras, Bar da Fada Verde, Cemitério e Catacumbas agora concedem componentes com propósitos específicos: Sucatas, Giz, Kits de Curativos, Doses de Absinto e Bolsas de Sangue Adulterado.
  - O jogador deixa de depender exclusivamente da loja cara de Valéria e passa a fabricar seus próprios suprimentos essenciais para sobreviver à noite e aos combates da Zona Vermelha.


---

## 7. O COVIL DE LILITY & O TRILEMA DA ALIMENTAÇÃO CONSOLIDADO

- **Restrições de Acesso ao Sangue da Mestra:**
  - *Limite:* Victor só pode se alimentar de Lility 1 vez por período (`alimentou_lility_periodo`).
  - *Bloqueio por Saciedade:* Se a fome estiver >= 85%, Lility recusa com desdém (*"Não desperdice meu sangue por gula"*).
- **As 4 Modalidades de Alimentação:**
  1. **Oferenda de Absinto Esmeralda (1x Absinto):** +100% Sede, +2 Afeto, +15 Vínculo Carmesim. Transe poético e suave.
  2. **Oferenda Magna da Partitura Rúnica:** +100% Sede, +3 Afeto, +25 Vínculo Carmesim. Lility revela vulnerabilidade inédita sobre sua prisão.
  3. **Relatório de Espionagem sobre Elara:** +70% Sede, +1 Afeto, +10 Vínculo, -10% Exposição. Cooperação política contra a Presidente.
  4. **Mãos Vazias (A Confissão Íntima):** +60% Sede, -2 Humanidade. Victor deve confessar um trauma (a traição do professor, a solidão ou o ódio), desgastando sua sanidade.
  5. **Mãos Vazias (Transe Violento):** +80% Sede, -15 HP, -3 Humanidade, +2 Ressonância Pré-Diluviana. O sangue entra como chumbo líquido com visões do Dilúvio.
- **Impacto no Trilema:** Alimentar-se de Lility não é mais gratuito nem infinito. O jogador deve alternar ativamente entre bolsas compradas de Valéria ($120), predação furtiva em corredores escuros e oferendas/custos mentais com Lility.

---

## 8. MODIFICADORES DIÁRIOS DE CLIMA & TENSÃO (DAILY MODIFIERS)

- **Mecânica:** A cada novo amanhecer (`dia_atual += 1`), o campus sorteia automaticamente um modificador temporário através de `sortear_modificador_diario()` em `sistemas_world_of_horror.rpy`.
- **Os 6 Climas da Academia:**
  1. **⚔️ Inspeção Rígida do Conselho:** +10% Exposição extra em infrações; relatórios entregues a Elara rendem o dobro ($240 em vez de $120).
  2. **🩸 Campanha Semestral de Sangue:** Predação no Pátio/Banheiro tem 85% de chance de sucesso e concede +45% Sede; flagrantes punem com +30% Exposição.
  3. **🌫️ Névoa Carmesim do Abismo:** DOOM sobe +2% extra; monstros na Zona Vermelha causam +25% de dano e dropam o dobro de moedas e despojos da névoa.
  4. **🌙 Toque de Recolher Estrito:** Mercado Negro de Valéria tem 20% de desconto; descansar no dormitório à noite gera +15% de Exposição por rondas nos quartos.
  5. **🌧️ Chuva Fria nos Vitrais:** Alunos recolhidos em salas fechadas; heroínas começam o dia com 4 pontos de Paciência (em vez de 3), favorecendo diálogos e dates.
  6. **🕯️ Calmaria Ilusória:** Dia estável de recomposição; Victor regenera +15 HP passivos ao amanhecer.
- **HUD Integrado:** O indicador do clima ativo (`[clima_diario_icone] [clima_diario_nome]`) fica visível no topo da tela em `hud_sobrevivencia` com tooltip explicativo.


---

## 9. O CICLO ATIVO DE QUITAÇÃO DO LIVRO DE DÍVIDAS DE VICTOR

- **Fundação Psicológica:** Victor Vane vive sob o trauma de ter levado a culpa pela fraude de seu mentor acadêmico na universidade anterior. Seu código pessoal dita: *"Eu não fujo de dívidas. Mas me recuso a ser descartável de novo."*
- **Aba "📜 LIVRO DE DÍVIDAS" na Central Tática:**
  - Acessível na barra de abas da Central Fêniks (`central_tatica_feniks`, aba `"dividas"`), pelo botão `📜 DÍVIDAS` no HUD superior (`hud_sobrevivencia`) e dentro do inventário (`inventario_victor`).
  - **Coluna Esquerda:** Exibe as 4 Regras de Victor escritas no verso da carta de bolsa (com destaque riscado se violadas e status intacto se preservadas), além da fundamentação de sua filosofia de sobrevivência.
  - **Coluna Direita:** Lista interativa das obrigações ativas registradas em `registro_dividas_ativas` (objetos `DividaAtiva`), exibindo:
    - Nome do credor (Valéria, Elara, Emília, Lility, Monitores).
    - Descrição da dívida e requisito exato de recursos em estoque ($dinheiro, sucata, giz, relatórios ou conhecimento oculto).
    - Recompensa e impacto prático ao quitar.
    - Botão dinâmico **`⚖️ [[ QUITAR DÉBITO ]]`** quando os requisitos são cumpridos.
- **Efeitos da Quitação:**
  - **Valéria:** +2 Afeto, +$60 de crédito comercial e respeito da Turma do Fundão.
  - **Elara:** -20% Exposição, +1 Afeto e redução da vigilância do Conselho Estudantil.
  - **Emília:** +2 Afeto, +3 Humanidade por cumprir promessas éticas.
  - **Lility:** +2 Afeto, +15 Vínculo Carmesim por honrar a vida prorrogada.
  - **Monitores:** -15% Exposição e arquivamento de boletim de infração.
- **Compra de Sangue Fiado nas Caldeiras:**
  - Se Victor estiver sem dinheiro para comprar bolsas na loja de Valéria, pode pedir uma bolsa a prazo, assumindo uma dívida ativa que exige pagar 2x Sucatas depois, mantendo o jogador vivo mesmo na falência extrema.


## 10. AUDITORIA E CORREÇÃO DOS 4 BUGS CRÍTICOS (SESSÃO DE REVISÃO FINAL)

1. **Bug 1: Aba "Livro de Dívidas" vs. "Talentos" (`game/sistemas_avancados.rpy`):**
   - *Correção:* O bloco `elif aba_central_feniks == "dividas":` foi reposicionado para depois do término de todos os 3 Ramos da aba `"talentos"` (Humanidade, Subterfúgio e Predador). Agora ambas as abas operam com layout horizontal completo e navegação fluida sem sobreposições.
2. **Bug 2: IDs de Locais Divergentes em Encontros Agendados (`game/custom_screens.rpy`):**
   - *Correção:* Em `menu_encontro_emilia`, o agendamento foi corrigido de `"clube_ocultismo"` para `"sala_ocultismo"`. Em `menu_encontro_elara`, de `"gremio"` para `"salao_gremio"`. Com isso, `verificar_encontro_agendado` identifica com precisão a presença de Victor nas salas corretas do mapa, evitando faltas e strikes injustos.
3. **Bug 3: Eventos Narrativos Órfãos Conectados ao DOOM (`game/calendario.rpy`):**
   - *Correção:* Integrados os marcos `evt_d10_noite` (Threshold 40% / Dia 10 Noite - Bar da Fada Verde e lote contaminado de Valéria) e `evt_d17_tarde` (Threshold 60% / Dia 17 Tarde - Chegada de Lorde Phillip von Karsten e liberação do `ritual_corte_vinculo_desbloqueado = True`). As verificações foram organizadas em ordem ascendente, garantindo coerência narrativa cronológica mesmo em caso de elevação súbita do DOOM. Adicionados atalhos diretos no `painel_debug_interno`.
4. **Bug 4: Desconto Duplo de Fome e Cabelos de Lility no Ato I (`game/script.rpy`):**
   - *Correção de Fome:* Removida a subtração direta `$ fome_sangue -= 20` nas aberturas de `evt_d15_noite` e `evt_d19_noite`, deixando a degradação passiva a cargo unicamente do `avancar_turno_mapa`.
   - *Correção Visual de Lility:* Textos do Ato I (`evt_d01_manha`, `evt_d01_tarde` e `evt_d01_noite`) que a descreviam incorretamente com "cabelos prateados como geada" (traço exclusivo da Presidente Elara) foram corrigidos para "longos cabelos carmesins profundos / escarlates".
   - *Sincronização Binária:* Arquivo `game/script.rpy` sincronizado e verificado com `c:\Users\otome\Downloads\ato1_rework.rpy` via `fc.exe /b` (0 diferenças).


## 11. AUDITORIA COMPLETA DOS 9 PONTOS DE ENGENHARIA (GEMINI ARGON 4)

1. **Camada Social e 13º Arquivo (`sistemas_social_rpg.rpy`):**
   - Confirmado ativo com 494 linhas, gerindo instâncias `HeroinaStatus`, rastros de aroma, reatividade de fases e árvore de talentos.
2. **Soma Duplicada de Afeto ao Quitar Dívidas (`th_sistema_narrativo.rpy`):**
   - Removido o incremento duplo em `store.status_*.afeto`, já que o setter do objeto muta a variável do store nativamente.
3. **Quitação da Dívida Institucional "A Escola" (`th_sistema_narrativo.rpy`):**
   - A dívida da bolsa integral agora é do tipo `"institucional"`, exigindo $480 ou a entrega do Relatório Político do Grêmio para concessão de +3 Humanidade e -25% Exposição. O tipo `"livre"` não permite quitação automática (`pode_quitar = False`).
4. **Alinhamento do Caso "Loira do Banheiro" (`custom_screens.rpy`):**
   - `banheiro_abandonado` agora requer 3 pistas coletadas para acionar o confronto com a anomalia.
   - Adicionadas as 3 pistas ambientais atmosféricas na exploração do banheiro em `pista_ambiental_bs`.
5. **Remoção de Exploit no Quadro de Mistérios (`custom_screens.rpy`):**
   - O botão de atalho no mural agora exige passos disponíveis e salta diretamente para `investigar_passo_bs`, consumindo 1 Ponto de Ação e integrando-se organicamente ao loop de exploração.
6. **Reset de Casos no Novo Jogo (`sistemas_world_of_horror.rpy` e `calendario.rpy`):**
   - Criada a função `reiniciar_misterios_woh()`, chamada no `label start:` para zerar casos concluídos e pistas ao reiniciar a campanha.
7. **Paciência Máxima das Heroínas e Clima Diário (`sistemas_world_of_horror.rpy`):**
   - `sortear_modificador_diario()` preserva as bases individuais (`paciencias_base = {"lility": 4, "valeria": 4, "elara": 3, "emilia": 3}`), aplicando +1 apenas sob o efeito do clima `chuva_vitrais`.
8. **Conexão Real de `status_escola` e `sequelas_ativas` (`custom_screens.rpy` e `combate.rpy`):**
   - Preços no Mercado Negro aumentam em +20% quando `status_escola == "inquietante"`.
   - Inimigos desferem +20% de dano adicional quando `status_escola == "histeria"`.
   - Fugas arriscadas com baixa vida podem infligir a sequela `trauma_fuga` ("Paranoia de Emboscada").
   - Descansar no dormitório ou aplicar `Gaze Consagrada` remove e cura sequelas ativas.

## 12. PADRONIZAÇÃO DE CENÁRIOS DE CHUVA, CONVERSÃO WEBM E AUDITORIA VISUAL 1:1

1. **Auditoria Visual Profunda e Correção das Confusões de Cenários:**
   - **Correção da Troca Corredor <-> Gabinete:**
     - `bg animado gabinete diretor chuva.webm` (contém a grande mesa executiva, trono de couro, globo e candelabro da Elara).
     - `bg animado corredor academia chuva.webm` (contém os armários/lockers escolares, mural de avisos e retratos dos mestres).
     - `bg corredor academia chuva.webp` (versão estática oficial do corredor).
   - **Correção do Trio Cemitério / Entrada Portões / Avenida:**
     - `bg animado cemiterio chuva.webm` (lápides, cruzes, túmulos e árvores retorcidas sob chuva/névoa).
     - `bg animado entrada academia portoes chuva.webm` (grandes portões de ferro forjado de frente, gárgulas nos pilares e fachada da catedral).
     - `bg animado rua avenida campus chuva.webm` / `bg animado rua portao academia chuva.webm` (avenida metropolitana com táxi amarelo, carros e prédios).
   - **Correção das Perspectivas do Pátio e Fonte:**
     - `bg animado patio arvore chuva.webm` / `bg patio academia arvores chuva.webp` (alameda das grandes árvores centenárias).
     - `bg animado patio claustro fonte chuva.webm` / `bg patio claustro fonte chuva.webp` (pátio aberto com a fonte gótica ao centro).
     - `bg animado patio claustro arcos chuva.webm` / `bg arcos claustro patio fonte chuva.webp` (visão debaixo dos arcos da galeria voltada para a fonte).
   - **Cenários Internos Auditados:**
     - `bg animado biblioteca gotica mesas chuva.webm` / `bg biblioteca gotica mesas chuva.webp` (biblioteca com mesas de estudo e abajures).
     - `bg animado sala musica piano vitral chuva.webm` / `bg sala musica piano chuva.webp` (sala de Lility com piano de cauda e vitrais coloridos).
     - `bg animado dormitorio quarto chuva.webm` (quarto de Victor com janela gótica na chuva).
     - `bg animado dormitorio externo chuva.webm` / `bg dormitorio externo chuva.webp` (fachada em U de tijolos e hera do dormitório).

2. **Matriz de Conversão e Otimização WEBM (VP9, -an):**
   - Todos os 12 vídeos de chuva convertidos para `.webm` (codec `VP9`, 1080p, sem áudio embutido, silenciosos e otimizados para GPU).
   - Redução de peso: de **56.33 MB** para **13.70 MB** (**-75.7% de economia**). Todos os `.mp4` brutos foram removidos.
   - Correspondência 1:1 validada via matriz de comparação de pixels contra as versões estáticas.

3. **Canal de Áudio Ambiente e Extração da Chuva:**
   - Efeito sonoro extraído para **`game/audio/sfx_chuva_ambiente.ogg`** (147 KB, Vorbis q4).
   - Canal nativo **`ambient`** registrado (`renpy.music.register_channel("ambient", mixer="sfx", loop=True)` em `game/definitions.rpy`).

4. **Substituição Dinâmica no Ciclo de Exploração (`game/custom_screens.rpy`):**
   - Na rotina `label entrar_local_exploracao_bs`, a verificação climática ativa cenários e áudio quando `clima_diario_id == "chuva_vitrais" and periodo in ["Manhã", "Tarde"]`:
     - **Dormitório de Victor:** `bg animado dormitorio quarto chuva`.
     - **Pátio Central & Fonte:** `bg animado patio claustro fonte chuva`.
     - **Portões & Praça:** `bg animado entrada academia portoes chuva`.
     - **Biblioteca:** `bg animado biblioteca gotica mesas chuva`.
     - **Salão do Grêmio (Gabinete):** `bg animado gabinete diretor chuva`.
     - **Sala de Música (Lility):** `bg animado sala musica piano vitral chuva`.
     - **Cemitério da Névoa:** `bg animado cemiterio chuva`.
     - **Corredores após Alimentação de Emília:** `bg animado corredor academia chuva`.
   - **Mapa Tático (`screen mapa_tatico_escola`):** Overlay sutil (`Solid("#0b192844")`) aplicado durante a chuva nos períodos diurnos.

## 13. INTEGRAÇÃO NO MAPA TÁTICO E LOOP DE EXPLORAÇÃO: PÁTIO DAS ÁRVORES E RUA EXTERNA

1. **Catalogação de Novas Áreas Oficiais no Mapa Tático (`screen mapa_tatico_escola`):**
   - **`patio_arvore` (🌳 Pátio das Árvores Centenárias / Bosque da Academia):**
     - Pino inserido em `xpos 960 ypos 400` (alameda verde de árvores centenárias atrás da torre do relógio, no centro-direita do mapa).
     - Drops temáticos: Folhas Sagradas, Giz de Proteção Rúnico, Dinheiro perdido de calouros e Curativos em bancos de pedra.
     - Conexão narrativa: Coleta de pistas para o Caso da Mulher de Oito Pés (Hachishakusama - galhos quebrados na copa a 3 metros de altura).
   - **`rua_portao` (🚗 Rua Externa & Avenida do Campus / Perímetro Urbano):**
     - Pino inserido em `xpos 220 ypos 860` na Superfície e `xpos 760 ypos 840` no Subsolo/Exterior (esquina de asfalto com postes e trânsito fora dos portões).
     - Drops temáticos: Sucata Eletrônica de fiação e postes, Dinheiro caído no meio-fio molhado, Doses de Absinto de contrabandistas noturnos e Curativos de ambulâncias.
     - Conexão de figurantes: Policiais em ronda e transeuntes civis.

2. **Ciclos Temporais e Integração Climática de Chuva (`label entrar_local_exploracao_bs`):**
   - **Ciclo de `patio_arvore`:**
     - *Chuva (Manhã/Tarde):* `bg animado patio arvore chuva` (com áudio contínuo no canal `ambient`).
     - *Manhã:* `bg animado patio arvore dia claro`.
     - *Tarde:* `bg animado patio arvore entardecer folhas`.
     - *Noite:* `bg animado patio arvore postes noite`.
   - **Ciclo de `rua_portao` (Perímetro Urbano / Rua Externa):**
     - *Chuva (Manhã/Tarde):* `bg animado rua avenida campus chuva` (com áudio contínuo no canal `ambient`).
     - *Manhã:* `bg animado rua portao academia manha` (WebM VP9 padronizado).
     - *Tarde:* `bg animado rua portao academia tarde` (WebM VP9 padronizado).
     - *Noite:* `bg animado rua portao academia noite` (WebM VP9).
   - **Ciclo de `portoes_praca` (Entrada & Portões da Academia):**
     - *Chuva (Manhã/Tarde):* `bg animado entrada academia portoes chuva`.
     - *Manhã:* `bg animado entrada academia portoes manha` (WebM VP9 padronizado).
     - *Tarde:* `bg animado entrada academia portoes entardecer sol`.
     - *Noite:* `bg animado entrada academia portoes nevoeiro noite`.

3. **Declarações e Aliases Oficiais (`game/definitions.rpy`):**
   - Registrados explicitamente todos os Movie() correspondentes para `.webm` VP9 e aliases estáticos em `.webp`.
   - Atualizada a distribuição de figurantes `sortear_mob_por_local()` mapeando calouros para o bosque de árvores e rondas policiais para a rua externa.

## 14. SISTEMA DE PROGRESSÃO NARRATIVA E TRAVAS DE MAPA (METROIDVANIA TÁTICO)

Três áreas de alto valor investigativo e tático do mapa foram estruturadas com bloqueios orgânicos de narrativa e progressão mecânica:

1. **Banheiro Abandonado (2º Andar / Ala Interditada - `banheiro_abandonado`):**
   - **Mecânica de Bloqueio:** O pino no Mapa Tático (`screen mapa_tatico_escola`) exibe `🔒 Banheiro Abandonado` desabilitado, com feedback sonoro/visual informando que a ala está interditada pela reitoria. Caso o jogador tente forçar entrada via console/label, `entrar_local_exploracao_bs` bloqueia com notificação de segurança.
   - **Gatilho de Desbloqueio (`desbloqueou_banheiro_abandonado = True`):**
     - *Caminho 1:* Conversa com Emília nos encontros clandestinos (`menu_encontro_emilia`), onde ela relata os três desaparecimentos recentes e o rastro de sangue coagulado diante do grande espelho rachado.
     - *Caminho 2:* Escolha de diálogo direta `"Ouvi rumores sobre um banheiro interditado no segundo andar..."`, garantindo +1 de Intelecto e reação positiva de Ocultismo.

2. **Bar da Fada Verde (`bar_fada_verde`):**
   - **Mecânica de Bloqueio:** O pino no Subsolo exibe `🔒 Bar da Fada Verde` requerendo o Passe Clandestino do Fundão.
   - **Gatilho de Desbloqueio (`tem_passe_fada_verde = True`):**
     - Disponibilizado na Loja Clandestina de Valéria (`screen loja_valeria`) por **$260** (sujeito aos multiplicadores de clima econômico), **apenas quando Valéria confia em Victor** (Vínculo >= 15, Afeto >= 8, ou dívida de sangue quitada).
     - *Rede de Segurança Narrativa:* Desbloqueio automático garantido na noite do Dia 10 (`marco_40_fada_verde` em `game/calendario.rpy`), impedindo travamentos na história principal.

3. **Cripta de Vidro / Tumba das Profundezas (`cripta_cofre`):**
   - **Mecânica de Bloqueio:** Exibe `🔒 Tumba Selada ([fragmentos_chave_cripta]/3 Peças)` com contador dinâmico e tom misterioso.
   - **Regra de Ouro Cumprida:** O nome de Cain nunca é mencionado no pino ou nas notificações. É tratada como "Selo Proibido das Profundezas" e "Cofre de Contenção".
   - **Gatilho de Desbloqueio (`desbloqueou_cripta_cofre = True`):**
     - O jogador deve explorar e escavar as **Catacumbas & Esgoto Colonial (`catacumbas`)**. A cada incursão com sucesso de loot, há 60% de chance de desenterrar um fragmento rúnico da chave ancestral:
       - *Peça 1/3:* Haste de prata e obsidiana com ranhuras em espiral desenterrada de uma sepultura violada.
       - *Peça 2/3:* Cilindro de latão marcado com glifos de contenção encontrado atrás de uma gárgula partida.
       - *Peça 3/3:* Engrenagem mística sob o altar em ruínas. As três peças se fundem em um clique mecânico ressonante, liberando permanentemente o acesso ao Cofre e Cripta mais profunda.


## 15. SORTEIO DINÂMICO DE CENÁRIOS ANIMADOS NAS CATACUMBAS

1. **Objetivo de Imersão Subterrânea:**
   - Para transmitir a atmosfera labiríntica e imprevisível das Catacumbas coloniais da Academia, o cenário não fica restrito a uma única vista fixa.
   - A cada entrada no local (`local_atual == "catacumbas"` em `game/custom_screens.rpy`), o sistema sorteia aleatoriamente entre os 3 cenários animados temáticos existentes em `Background Wallpapers motions/`:
     - **Corredor de Tochas:** `bg animado catacumbas corredor tochas` (galeria úmida de pedra com chamas avermelhadas).
     - **Corredor com Runas:** `bg animado catacumbas corredor runas tochas` (glifos de contenção gravados nas paredes ressoando em azul/carmesim).
     - **Câmara do Cofre Antigo:** `bg animado catacumbas cofre velas verdes` (candelabros de chamas esmeralda e sarcófagos dos fundadores).

2. **Lógica Antirrepetição Inteligente (`sortear_bg_catacumbas()` em `game/definitions.rpy`):**
   - Implementada a função com filtro de exclusão da última cena visualizada (`ultimo_bg_catacumbas`), garantindo que o jogador não visualize o mesmo trecho duas vezes seguidas ao sair e reentrar nas catacumbas.


## 16. SEPARAÇÃO DO MERCADO NEGRO E CALDEIRAS INDUSTRIAIS COM SORTEIO DE CENÁRIOS

1. **Separação Temática no Subsolo (`screen mapa_tatico_escola`):**
   - **`caldeiras` (🛒 Mercado Negro):** O pino anterior "Caldeiras & Mercado Negro" foi renomeado exclusivamente para **"🛒 Mercado Negro"** (`xpos 340 ypos 480`). Mantém o esconderijo secreto de Valéria, a Loja Clandestina (`loja_valeria`), o diálogo inicial de introdução e o background temático de loja clandestina (`bg animado caldeiras esconderijo tocha azul e fogo`).
   - **`sala_caldeiras` (🔥 Caldeiras da Academia - NOVO):** Nova área dedicada adicionada no setor central do Subsolo (`xpos 740 ypos 440`). Representa o complexo industrial de válvulas, encanamentos de alta pressão e fornalhas a carvão que aquecem a academia.

2. **Sorteio Dinâmico Antirrepetição dos Cenários das Caldeiras (`sortear_bg_caldeiras()`):**
   - A cada visita às Caldeiras (`local_atual == "sala_caldeiras"` em `game/custom_screens.rpy`), o motor sorteia aleatoriamente entre 3 cenários industriais animados:
     - **Corredor Industrial com Vapor:** `bg animado corredor industrial subsolo vapor` (tubulações de metal silvando vapor).
     - **Corredor da Caldeira Central:** `bg animado corredor industrial caldeira subsolo vapor` (grandes caldeiras com vazamento de pressão).
     - **Oficina da Fornalha em Brasa:** `bg animado caldeiras oficina fornalha brasa` (fornalha ardente com labaredas e cinzas).
   - O sistema filtra o último cenário exibido (`ultimo_bg_caldeiras`), evitando repetições consecutivas.

3. **Integração Mecânica:**
   - **Áudio Ambiente:** Reproduz a faixa industrial e sufocante **`audio/Iron_Lungs.ogg`**.
   - **Bancada de Crafting:** Acesso rápido à bancada mantido tanto no Mercado Negro quanto nas Caldeiras.
   - **Loot & Sobrevivência:** Coleta de Sucata Eletrônica, Absinto, Dinheiro e Sangue Adulterado.
   - **Pistas do Lote Necrótico:** Pistas investigativas de química clandestina e confronto final vinculados ao complexo.


## 17. TRAVA DE INVESTIGAÇÃO E CHANCE DIÁRIA DE ABERTURA DO MERCADO NEGRO

1. **Desbloqueio Progressivo (5 Investigações nas Caldeiras):**
   - **Estado Inicial:** O pino no Mapa Tático exibe `🔒 Mercado Negro ([investigacoes_caldeiras]/5 Pistas)`. Clicar nele exibe uma notificação informando que a entrada é oculta e que o jogador deve vasculhar as Caldeiras.
   - **Progressão Narrativa:** A cada visita às Caldeiras da Academia (`sala_caldeiras`), o contador `investigacoes_caldeiras` avança de 1 a 5, entregando pistas ambientais progressivas:
     - *1/5:* Pegadas furtivas com resíduos de graxa fresca e cinzas.
     - *2/5:* Bitucas de cigarro mentolado e símbolo mercantil talhado no metal.
     - *3/5:* Eco abafado de risadas e tilintar de garrafas por trás de uma grade.
     - *4/5:* Mapeamento da rota de desvio das rondas do Conselho.
     - *5/5:* Chapa de aço solta empurrada atrás da fornalha principal, liberando permanentemente o acesso ao Mercado Negro de Valéria (`desbloqueou_mercado_negro = True`).
   - **Indicador Visual Duplo:** Tanto o botão do Mercado Negro quanto o das Caldeiras indicam o progresso `[investigacoes_caldeiras]/5`.

2. **Mecânica Clandestina Diária (30% de Chance de Estar Fechado):**
   - Ao virar o dia (`avancar_turno_mapa` ao amanhecer), a função `sortear_abertura_mercado_negro()` sorteia o estado operacional do mercado:
     - **70% de Chance:** Aberto normalmente para compras e encontros.
     - **30% de Chance:** Fechado por precaução para despistar patrulhas e fiscalizações do Grêmio Estudantil.
   - Quando fechado, o pino no mapa exibe `🔒 Mercado Negro (Fechado Hoje)` em tom acinzentado/avermelhado, avisando que Valéria suspendeu as operações naquele dia.
   - Acesso forçado é barrado com segurança em `entrar_local_exploracao_bs`.

3. **Rede de Segurança Narrativa:**
   - Na noite do Dia 10 (`evt_d10_noite`), o marco automático garante `desbloqueou_mercado_negro = True` e `mercado_negro_aberto_hoje = True`, assegurando que a história principal nunca seja bloqueada.


## 18. SPRITES EXPRESSIVOS DE VICTOR VANE (PADRONIZAÇÃO, FASES E ROTEIRO)

1. **Classificação e Nomenclatura dos 17 Sprites:**
   - **14 Sprites de Uniforme Escolar (896x1200, WebP qualidade 95 com canal alfa):**
     - `victor uniforme neutro.webp`: Olhar sereno, compenetrado, postura padrão.
     - `victor uniforme serio.webp`: Olhar firme, grave e compenetrado.
     - `victor uniforme pensando.webp`: Mão no queixo, analítico e reflexivo.
     - `victor uniforme confiante.webp`: Mãos nos bolsos, meio sorriso calmo e seguro.
     - `victor uniforme sorrindo.webp`: Sorriso aberto, amigável e caloroso.
     - `victor uniforme falando.webp`: Boca entreaberta em diálogo, explicando.
     - `victor uniforme surpreso.webp`: Olhos arregalados e boca aberta em choque/espanto.
     - `victor uniforme triste.webp`: Cabeça baixa, olhar abatido e melancólico.
     - `victor uniforme sem jeito.webp`: Gota de suor na têmpora, sorriso tímido / envergonhado.
     - `victor uniforme constrangido.webp`: Dentes trincados, mão no ombro, embaraçado.
     - `victor uniforme charmoso.webp`: Olhar sedutor, meio sorriso de canto, flertando.
     - `victor uniforme ferido combate.webp`: Sangue no rosto e uniforme, punhos cerrados em guarda de combate.
     - `victor uniforme ferido determinado.webp`: Sangue na têmpora/bochecha, inclinado à frente, determinado.
     - `victor uniforme ferido sorriso.webp`: Ferido com sangue, mas mantendo sorriso irônico/aliviado.
   - **3 Sprites da Fase 3 de Vampiro Predador:**
     - `victor fase3 predador serio.webp` (1024x1024): Olhos vermelhos brilhantes, aura intimidadora e fria de vampiro.
     - `victor fase3 predador rindo.webp` (1024x1024): Risada sádica e debochada de predador, presas proeminentes.
     - `victor fase3 predador postura.webp` (768x1280): Plano americano, camisa aberta, marcas de sangue e ataduras, postura predatória.
   - **Backup e Arquivo:** Os 17 arquivos originais em PNG foram salvos e preservados com segurança na pasta `game/images/victor/png_originais/`.

2. **Regra de Fases e Função `obter_sprite_victor(modo)`:**
   - **Fases 1 e 2 (Humanidade >= 35):** Os sprites de uniforme cobrem todas as expressões e estados emocionais de Victor como estudante da academia.
   - **Fase 3 (Humanidade < 35):** Victor opera como Vampiro Predador Completo; uniformes humanos são bloqueados e apenas os sprites de vampiro são retornados (`victor fase3 predador serio`, `victor fase3 predador rindo`, `victor fase3 predador postura`, `victor fase3 predador busto`).
   - **Fome Crítica (< 20) ou Frenesi:** Retorna imediatamente `victor furia`.

3. **Integração no Roteiro e Cenas Sociais:**
   - **`game/script.rpy`:** Cenas-chave receberam reações expressivas dinâmicas (encontro com Emília no corredor, Nora no banco, Diretor Ambrósio, Teo e Heitor no Termo 112, Gabinete de Elara, confronto na neblina, Baile de Máscaras, Valsa na Sala de Música, Pacto de Sangue de Emília, e Clímax Final C).
   - **Sincronia Binária:** `c:\Users\otome\Downloads\ato1_rework.rpy` mantido em 100% de paridade com `game/script.rpy` (`fc.exe /b` = 0).
   - **`game/custom_screens.rpy`:** Marcos de relacionamento I e II de Lility, Emília, Valéria e Elara atualizados com poses expressivas de Victor.

---

## 19. ENFERMARIA DA ACADEMIA & DRA. CLARA VANCE (`enfermaria`)

1. **11º Setor da Superfície (`mapa_tatico_escola`, `xpos 530 ypos 440`):**
   - Localizada na ala médica oficial da Campanha de Saúde Comunitária e gerência do "Rebanho Seguro".
   - Rótulo de controle principal: `acao_consultar_enfermaria` / `menu_enfermaria_loop` (alias legado `menu_enfermaria_academia`).
   - Gatilho automático com `emilia_sabe_vampiro`: aciona `ev_c02_triagem_enfermaria` durante o dia caso ainda não visto.
2. **Operações e Regras da Dra. Clara Vance (`mob_enfermeira`):**
   - **Compra de Suprimentos:** Bolsa de Sangue Filtrado (`$100`, abaixo dos `$120` padrão da Valéria) e Kit de Curativos e Sutura (`$50`).
   - **Tratamento Médico:** Cura de sequela ativa + `+20 HP` por `$80`.
   - **Coleta de Hemograma (Sangue Dourado Rh-Nulo):** Uma vez por dia (`coleta_enfermeira_hoje`), rende `+$120` e `+10% Exposição`.
   - **Drenagem Furtiva (Banquete Clínico):** Disponível quando `fome_sangue < 70` e `not drenou_enfermeira_hoje`. Recupera `+30% Fome`, `+20 HP`, `+1 Intelecto`, aplica `-2 Humanidade`, adiciona `+10% Exposição` e `+3% DOOM`, hipnotiza Clara (`mob enfermeira transe`).

---

## 20. DORMITÓRIO COMO ZONA SEGURA (`0` PASSOS) & INTERAÇÕES EMÍLIA / LILITY / DUO

1. **Regra de Zona Segura Inviolável (`dormitorio`):**
   - `investigar_passo_bs` barra gasto de passos no dormitório; nunca ocorrem emboscadas hostis da Zona Vermelha nem perda passiva de AP ao visitar ou conversar.
   - `acao_descansar_dormitorio` escala recuperação de HP e cura de sequelas pelos passos restantes do período (`>=3` -> `+45 HP` / `100%` cura sequela / `-5% Exposição`; `2` -> `+30 HP` / `70%`; `1` -> `+15 HP`; `0` -> `+5 HP`), descontando `-10 HP` caso haja pesadelos de fome (`fome_sangue < 25`), limpando `rastro_olfativo` e oferecendo imunidade ao toque de recolher (`0%` risco noturno).
   - **Sinergias de Vigília no Repouso:** Emília + Lility juntas (`+10 Humanidade`, `-15 Tensão`, `+1 Afeto` ambas); Emília só (`+10 Humanidade`, `-15 Tensão`, `+1 Afeto`); Lility só (`+5 Fome`, `-10 Tensão`, `+1 Afeto`).
2. **Encontros Diretos & Embate Simultâneo (`0` Passos):**
   - **`menu_encontro_emilia_dormitorio`:** Chá de camomila e mirra (`+5 Hum`, `-15 Tensão`, `+1 Afeto`), Gaze Consagrada (`+35 HP` + cura sequela), conversa sobre Lorde Phillip (`+Afeto`/`+Intelecto`/`+Conhecimento Oculto`), Tensão da Sede (`fome < 25`) e atalho de Marco. Contém reações exclusivas se Lility também estiver no quarto (`loc_mestra == "dormitorio"`).
   - **`menu_encontro_lility_dormitorio`:** Transe noturno no leito (`+1 Afeto`, `-20 Tensão`), Comunhão de Sangue (`fome < 35` -> `+30 Fome`), tática contra o Conselho (`+1 Conhecimento Oculto`, `-5% Exposição`), atalho de Marco e evento `ev_visita_noturna_lility_dormitorio` à noite se `afeto >= 3`.
   - **`evento_embate_dormitorio_lility_emilia`:** Disparado quando ambas dividem o quarto (`loc_emilia == "dormitorio" and loc_mestra == "dormitorio"`), oferecendo 4 resoluções: apoiar Emília, apoiar Lility, impor autoridade de Victor (`+2 Coragem`, `+1 Intelecto`, `+1 Afeto` ambas) ou pacificação improvisada no chá (`+5 Hum`, `-20 Tensão`, `+1 Afeto` ambas).

---

## 21. BESTIÁRIO COMPLETO (26 ARQUÉTIPOS + DERROTA), PERSONA HOLD-UP & MICRO-EVENTOS DE ITO

1. **Pool da Zona Vermelha (`sorteio_mob = 1..26` em `custom_screens.rpy`):**
   - Combina 4 arquétipos de IA em `combate.rpy`: **`gremio`** (Executoras/Vampiros do Conselho, Foice, Espada Solar/Lâmina Negra, Duelista, Rapieira Albina), **`corrompido`** (Hellhound, Rival Ghoul, Ghoul Garota Corrompida, Aluna das Teias, Sombra do Pesadelo, Marionete), **`inorganico`** (Esqueleto Nobre, Esqueleto Colegial Rúnico, Gárgula de Pedra Dragão, Besta Urso Acorrentado) e **`humano`** (Inquisidor Tático, Alquimista Renegado, Mecânico Pesado, Capanga de Escopeta do Fundão).
   - Inclui sprites dedicados de derrota pós-combate (`img_inimigo_derrota`) e `TERROR PREDATÓRIO` automático (Fase 3 com `humanidade < 35` nas áreas subterrâneas).
   - Hold-Up estilo Persona 5 (`executar_golpe_critico_persona`) quando atordoado/vantagem: **Drenagem Letal**, **All-Out Attack (`+2 Ressonância`)** ou **Extorquir (`+$70 a $150` + Bolsa de Sangue)**.
2. **Animação de Vasculhar & Micro-Eventos de Ito (`micro_evento_ito_corredor`):**
   - `investigar_passo_bs` recebeu animação ampliada de busca nos corredores antes de rolar encontro/loot/emboscada.
   - **6 micro-eventos emergentes** em `micro_evento_ito_corredor` expandindo a presença estudantil e tensões escolares no cotidiano da academia.

---

## 22. INVENTÁRIO ATUALIZADO DA BUILD E FINAIS CANÔNICOS (NOVEMBRO 2026)

- **Escopo da Base de Código:** **16 arquivos `.rpy`** ativos em `game/` (`script.rpy`, `custom_screens.rpy`, `definitions.rpy`, `th_sistema_narrativo.rpy`, `sistemas_social_rpg.rpy`, `sistemas_avancados.rpy`, `expansao_conflitos_lore.rpy`, `combate.rpy`, `screens.rpy`, `gui.rpy`, `sistemas_world_of_horror.rpy`, `sistema_som_ambiente.rpy`, `options.rpy`, `calendario.rpy`, `animacoes_cenas_intimas.rpy`, `bg_fit.rpy`).
- **Mídia em Disco:** **971 arquivos** em `game/images/` (inclui `148` motion wallpapers, `88` static wallpapers, `145` Enemy's, `256` mobs, além das heroínas e NPCs) e **705 arquivos** em `game/audio/` (`275` vozes `.ogg` em 10 pastas, `61` SFX em `sfx/`, `235` em `ambiente/` incluindo 57 loops por sala e packs Kenney/raw, `90` em `musicas/` e `44` faixas/stingers na raiz), roteados pelos 4 canais Ren'Py (`barks`, `ambient`, `stinger`, `music`/`sfx`).
- **Os 5 Finais Canônicos (`evt_d21_noite` em `script.rpy`) + Derrota:**
  1. **Final A — Consorte Imortal (A Nova Dinastia Carmesim):** Victor e Lility drenam Cain e assumem o trono noturno.
  2. **Final B — Quase Humano (O Peso da Liberdade):** Requer `ritual_corte_vinculo_desbloqueado`; liberta Lility em luz e devolve o pulsar humano a Victor ao lado de Emília.
  3. **Final C — A Configuração do Lamento (Todos Sobrevivem, Todos Perdem):** Requer `ritual_corte_vinculo_desbloqueado`; Victor abraça Emília mortalmente ferida como vampira e inverte o ritual, roubando a maldição de Lility e condenando-a à mortalidade sob sua guarda.
  4. **Final D — A Última Transação (Sobreviventes do Submundo):** Requer `afeto_valeria >= 1`; fuga pelos túneis das caldeiras com o furgão de vitae e tecnologia arcana.
  5. **Final Secreto E — A Harmonia Proibida (Aliança das Quatro Soberanas):** Requer `afeto >= 8` com **Lility, Emília, Valéria e Elara** + `humanidade >= 40`.
  6. **Game Over (`morte_definitiva`):** Morte em combate ou falha terminal no clímax (`evt_d21_noite`), reiniciando o ciclo sem retorno de label.

---

## 23. REBALANCEAMENTO ECONÔMICO, VITRINE ROTATIVA, TAXA DO CONSELHO & PRESENTES CLANDESTINOS

1. **Economia & Recompensa de Desbloqueio (`definitions.rpy` & `custom_screens.rpy`):**
   - Carteira inicial ajustada para **`$200`**; remoção do cashback gratuito em dinheiro ao quitar `divida_valeria_sangue_fiado`; bloqueio diário em Elara (`relatorio_entregue_hoje` e `inspecao_elara_hoje`); remoção de saque duplicado após Hold-Up *Extorquir* (`extorquiu_combate_atual`, rendendo `$55–$105` + `40%` Filtrada / `60%` Adulterada) e redução de espólios soltos (`loot_aleatorio_bs` / `olhos_no_escuro`).
   - **Enfermaria (`menu_enfermaria_loop`):** Ágio oficial elevado (`$165` Bolsa `1x/dia`, `$105` Kit `1x/dia`, `$140` Sequela física, Hemograma `+$90` / `-15 HP`), com agravante de **`+25%` custo / `-20%` hemograma** sob a sequela `taxa_inadimplente`.
2. **Vitrine Rotativa Híbrida (`sortear_vitrine_mercado_negro()`):**
   - **`2` Essenciais Fixos** (`bolsa_sangue_filtrado` + Fiado, `kit_curativo`, limitados a `1x/dia`) + **`5` Slots Rotativos Únicos** (`2x Suprimentos`, `1x Contrabando Tático`, `1x Raro/Lote [-20% / +15%]`, `1x Presente de Luxo`) sorteados de `19` itens ponderados por clima/fome/exposição + desconto de `-10%` com `status_valeria.afeto >= 6`.
   - `CATALOGO_ITENS` (`sistemas_avancados.rpy`) expandido para **25 itens** (+`cracha_falso`, `ampola_prata`, `tampao_hemostatico`, `incenso_mirra`, `sais_vigilia`, `amuleto_estanho` e os 5 presentes).
3. **Cobrança Periódica do Conselho (`evento_cobranca_taxa_academica`):**
   - Dispara a cada **6 períodos (2 dias)** via `slot_livre` (`calendario.rpy`) a partir do Dia 3 (`$135` se `divida_monitores > 0` com abatimento automático, ou `$100` padrão), com HUD de contagem regressiva/status inadimplente em `hud_sobrevivencia` e no Livro de Dívidas.
4. **Presentes Clandestinos (`fluxo_entregar_presente_heroina`):**
   - 5 presentes (`presente_flores`, `presente_perfume`, `presente_colar`, `presente_roupa`, `presente_anel`) vendidos na vitrine de luxo (+10% drop raro de lírios em `patio_arvore`), entregáveis `1x/dia por heroína` (limite de `+1 Afeto` em repetições), com **20 reações exclusivas** e **5 micro-eventos** (`ev_presente_emilia_flores`, `ev_presente_lility_perfume`, `ev_presente_elara_colar`, `ev_presente_valeria_roupa` e `ev_presente_anel_pacto`).
