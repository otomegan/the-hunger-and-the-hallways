# THE HUNGER AND THE HALLWAYS — DOSSIÊ NARRATIVO COMPLETO (ATO I)
**Gênero:** Dark Gothic Psychological Horror, Survival RPG (WOH-like) & Dating Sim  
**Protagonista:** Victor Vane (Estudante bolsista #41 — Rh-Nulo / Sangue Dourado infectado pela sede de sangue)  
**Ambientação:** Academia São Cipriano — Um internato gótico vitoriano administrado pelo Diretor Ambrósio, pela Presidente Elara e por uma Fundação ocultista, habitado por anomalias pré-diluvianas e vampiras.  
**Instruções para o Claude (Prompt de Revisão Integrado):**
> Você está atuando como um Editor Narrativo Sênior e Especialista em Visual Novels de Terror Psicológico e Romance Sombrio.
> Analise este dossiê completo que contém os eventos centrais, diálogos, ramificações de escolha, sistemas emergentes e interações sociais de *The Hunger and the Hallways*.
> 
> **Focos da sua avaliação:**
> 1. **Consistência da Lore e Pacing:** A transição do Prólogo Guiado (Dias 1–2) para o loop aberto governado pelo DOOM Clock (0–100%, escalado até o Dia 21 / 100% Ruína) mantém a tensão da dívida e da fome sem perder o ritmo? Há furos de continuidade?
> 2. **Diferenciação das Heroínas (Idiolectos & Vozes):** Lility (Mestra milenar sádica/fatigada), Emília (noviça devota em crise), Valéria (mercadora pragmática das Caldeiras) e Elara (aristocrata fria do Grêmio) — além de Clara Vance (hematologista da Enfermaria) — possuem vozes literárias distintas e sem clichês genéricos?
> 3. **Equilíbrio Terror vs. Romance (Dating Sim vs. Horror):** As escolhas íntimas, cenas de dormitório e de afeto enriquecem ou enfraquecem a atmosfera de pesadelo?
> 4. **Psicologia de Victor Vane:** A decadência moral (Humanidade), o controle da Besta (Saciedade/Fome) e a pressão de Exposição estão convincentes?
> 5. **Oportunidades de Polimento:** Quais cenas e transições têm o maior potencial de melhoria literária?

---

## SUMÁRIO GERAL DA HISTÓRIA
- **Parte I:** Regras de Victor Vane, Medidores e Sistema de Dívidas na Academia São Cipriano
- **Parte II:** Prólogo Guiado, Marcos do DOOM Clock & 5 Finais Canônicos (`evt_d21_noite`)
- **Parte III:** Eventos de Clímax, Mistérios WOH & Anomalias Sobrenaturais
- **Parte IV:** Interações Sociais Livres & Rotas com Heroínas
- **Parte V:** Narrativas de Pós-Combate, Drenagem e Morte
- **Parte VI:** Expansão Narrativa Canônica — As Fronteiras do Grilhão, A Cobaia 31 e os 18 Conflitos de Lore
- **Parte VII:** Sistemas Sociais, Zona Segura do Dormitório, Enfermaria & Micro-Eventos da Build Atual

---

## PARTE I: REGRAS DE VICTOR VANE & PSICOLOGIA
Victor Vane sobrevive na Academia São Cipriano guiado por quatro regras escritas no verso de sua carta de bolsa:
1. *Não dever nada a ninguém.*
2. *Nunca confiar em quem sorri antes de pedir.*
3. *Nunca ser o último a saber.*
4. *Nunca ser descartável.*

Todas as suas interações giram em torno dos medidores vitais e psicológicos da live build:
- **Vitalidade (`hp_jogador`, 0–100)** e **Sequelas (`sequelas_ativas`):** Dano físico e traumas persistentes curáveis apenas por descanso, Gaze Consagrada ou Enfermaria.
- **Saciedade / Fome (`fome_sangue`, 0–100):** Quanto menor, mais perto do Frenesi (< 20%) e de testes involuntários de ataque ao cruzar com figurantes.
- **Humanidade (`humanidade`, 0–100) & Exposição (`exposicao`, 0–100):** Medem quanto da máscara humana e moral de Victor resta, bem como o alerta do Grêmio e dos Inquisidores.
- **Tensão Psicológica & DOOM Clock (`ruina_cain`, 10–100%):** O relógio oculto de deterioração do mundo que regula marcos guiados (`calendario.rpy`), climas diários e o despertar em `evt_d21_noite`. *(Regra de sigilo: o nome de Cain e o DOOM permanecem velados nos turnos iniciais até o clímax.)*
- **Livro de Dívidas e Créditos (`ledger_devedores`, `dinheiro_jogador`):** Toda ajuda ou acordo financeiro/vital com Lility, Valéria, Teo (#112), Emília ou o Grêmio cobra seu preço.

---

## PARTE II: PRÓLOGO GUIADO, MARCOS DO DOOM & FINAIS (ATO I)


### DIA 01 — Manha (`evt_d01_manha`)

**VOZ NA ESCURIDÃO**: "Responda sem pensar, Victor. Você quer me salvar porque se importa comigo... ou porque não suporta a ideia de ficar sozinho outra vez?"
O chão pulsa. Não como terremoto — mais como coração. Batida por batida, o cascalho sob meus pés absorve o impacto e devolve.
A fumaça carmesim desce do céu rasgado em filamentos. E ali, no centro de tudo que está pegando fogo, uma mulher de pé em silêncio.
Cabelos do tom de vinho que secou. Boca fechada. Olhos que olham atravessando a pele — como se o que ela quisesse examinar ficasse atrás das costelas.
O cheiro chega antes do nome. Mirra. Ferro velho. Algo mais fundo que ferro.
Eu abro a boca. O som não sai. A fumaça fecha.
Eu sempre fui bom com contas. Quanto custa. Quanto eu devo. Quanto sobra.
Mas existem perguntas que não cabem em coluna nenhuma. E a sensação mais estranha de todas... é que aquele delírio não parecia memória. Parecia um aviso.
Acordo com a palma da mão espalmada contra a madeira do beliche. O quarto escuro. A cama fria do lado de fora do cobertor.
Ela estava lá de novo. Lágrimas escorrendo sem choro — sem convulsão, sem soluço — direto pela bochecha pálida, como se chorar fosse para ela o mesmo que respirar é para mim. Natural. Inevitável.
E os lábios se moviam. Sempre se movem. Eu nunca ouço.
Esfrego o rosto com o dorso da mão. A pele da bochecha está fria — suor que já secou.
Olho para o teto do beliche. Quinta noite com aquela mulher de cabelos cor de sangue. Talvez sexta. Parei de contar.
Levanto. O chão do quartinho de pensão range sob o peso. Dobro o cobertor com um cuidado idiota para a hora e fico parado diante da vidraça embaçada pela chuva da madrugada.
A chuva escorre pelo vidro... e o eco daquela sala fechada volta sem pedir licença. Não como memória inteira: como um corte que ainda sangra.
A mão direita ainda lembra do peso daquela caneta barata de metal.
Uma sala sem janelas no centro da cidade. Cheiro de café velho, fumaça de cigarro e o zumbido monótono de uma lâmpada fluorescente.
Um termo de confissão e transferência forçada empurrado sobre o fórmica da escrivaninha. Do outro lado da mesa, homens de terno impecável sorrindo enquanto esperavam a minha capitulação.
Eu assinei. A mão tremendo, os nós dos dedos ainda esfolados. Assinei para não ser trancado numa cela comum antes dos vinte anos... e porque a única pessoa por quem eu teria colocado a mão no fogo abaixou a cabeça, olhou para o chão e deixou que a culpa caísse inteira sobre os meus ombros.
Ali morreu a minha ingenuidade. Foi ali que entendi que estender a mão para salvar alguém só serve para colocar a corda no seu próprio pescoço.
Afastei a mão da vidraça da pensão. O passado é uma dívida que já paguei caro demais.
Apenas uma instituição aceitou minha matrícula depois que a ficha disciplinar foi manchada: a Academia São Cipriano. Não por compaixão — lugares aristocráticos não sabem o que é compaixão —, mas porque o formulário médico do vestibular destacou em amarelo uma anomalia rara no meu hemograma.
Rh Nulo. Sangue Dourado. Um caso a cada seis milhões.
Hoje eu recomeço do zero. Quatro regras escritas a lápis no bolso do casaco. E a promessa irrevogável de nunca mais virar descarte.
Os trilhos magnéticos não fazem barulho. Esse é o detalhe que me incomoda mais do que devia.
Pela janela, os campos viram viadutos de concreto cinzento. A metrópole gótica surge no horizonte entre as nuvens baixas.
Tiro a carta de recomendação de dentro do casaco. O papel está gasto nas dobras de tantas vezes que o reli durante a noite. No anexo médico, as duas palavras sublinhadas com precisão clínica: Rh Nulo / Sangue Dourado.
Eles sabem o que querem de mim. Agora preciso descobrir o que vou arrancar deles para continuar inteiro.
Os carvalhos terminam. Os portões começam.
Ferro batido, três metros de altura, ponteiros em forma de lanças. Uma gárgula no pilar esquerdo com a boca aberta na direção de quem chega — não em ameaça: em aviso.
No prospecto acadêmico que recebi pelo correio, havia uma foto dos portões com filtro de luz dourada e o slogan 'Excelência que Dura Gerações'. Agora, de perto, sem filtro, eles parecem o que são: um portão que fecha por dentro.
Quatro linhas a lápis. Não são promessas — promessas eu já quebrei. São contabilidade.
Atravesso.
O segundo andar tem vitrais demais e placas de menos. Passo pela primeira vez por um corredor largo e silencioso, ladeado por pesadas molduras douradas.
Uma tela a óleo em particular domina a parede leste: o retrato solene de um aristocrata de casaca preta e barba aparada, com olhos penetrantes que parecem esculpidos em âmbar. A plaquinha de latão na base diz apenas: O Fundador.
Paro diante dele. A pintura tem um brilho oleoso e denso sob a luz que corta os vitrais. Não é apenas antiga; o verniz parece espesso, vivo, como se as pinceladas guardassem uma respiração reprimida sob o linho.
Desvio o olhar. A regra três diz que nunca serei o último a saber. A regra não diz como. Eu poderia perguntar a alguém onde fica a secretaria, mas perguntar é admitir que outra pessoa sabe mais do que eu.
Então dou a volta pela ala oeste, conto os passos e tento me orientar pelos arcos de pedra. Quinze minutos depois, as mesmas tapeçarias carmesins, as mesmas portas fechadas... e a mesma parede.
Passo novamente diante da tela a óleo. O Fundador ainda está lá.
Mas quando dou três passos à frente, sinto um arrepio gélido subir pela nuca — a sensação física, inconfundível e nauseante de estar sendo observado.
Travo os calcanhares e giro o pescoço para trás.
Tenho certeza absoluta de que, na primeira volta, as pupilas dele apontavam em direção à janela. Agora... elas estão cravadas diretamente na altura do meu peito, acompanhando cada milímetro do meu movimento.
O ar ao redor da moldura parece ter caído cinco graus. Um cheiro sutil de terebintina e ferro velho paira no linho.
**EMÍLIA (Noviça Devota)**: "Ele gosta de você."
Dou um solavanco para trás, o coração disparando contra as costelas!
**VICTOR VANE**: "...Pelos céus! De onde você surgiu?!"
**EMÍLIA (Noviça Devota)**: "Da biblioteca. Eu vi você passar da primeira vez pela fresta da porta."
**EMÍLIA (Noviça Devota)**: "E o Fundador... quase ninguém encara essa moldura três vezes seguidas. Costuma ser sinal de que a pessoa está completamente perdida procurando a secretaria."
**VICTOR VANE**: "Eu não estou perdido. Estou fazendo um reconhecimento da planta da escola."
**EMÍLIA (Noviça Devota)**: "Dando voltas no mesmo corredor há vinte minutos?"
**VICTOR VANE**: "É um método de eliminação."
Ela ri pelo nariz, baixinho, como quem tenta não ser pega rindo. Há olheiras discretas sob os óculos. Quem dormiu pouco reconhece quem dormiu pouco.
**VICTOR VANE**: "E sobre esse quadro... Eu juraria que o ângulo do olhar dele mudou entre a primeira e a última volta."
O sorriso complacente de Emília murcha aos poucos. Ela ajeita os óculos redondos e olha de soslaio para a enorme pintura do Barão Cipriano.
**EMÍLIA (Noviça Devota)**: "Não diga isso muito alto pelos corredores, calouro. Mas... você não é o primeiro a notar."
**EMÍLIA (Noviça Devota)**: "Os quadros desta escola... sempre foram meio estranhos."
**EMÍLIA (Noviça Devota)**: "A administração jura que é apenas a perspectiva do claro-escuro barroco. Mas meu tio-avô, que estudou aqui nos anos sessenta, contava que algumas telas foram encomendadas com misturas alquímicas de pigmentos que reagem à umidade e ao calor dos corpos."
**EMÍLIA (Noviça Devota)**: "Outros alunos juram que ouviram murmúrios abafados vindo das molduras da galeria leste tarde da noite, logo antes do toque de recolher."
**EMÍLIA (Noviça Devota)**: "Dizem que quem passa tempo demais encarando os retratos antigos acaba perdendo o rumo dos corredores... ou esquecendo de voltar para o dormitório."
**EMÍLIA (Noviça Devota)**: "Por via das dúvidas: se você andar por aqui à noite, nunca responda se alguma pintura parecer sussurrar na sua direção."
Ela me dá esse conselho com um tom de voz que não parece folclore estudantil. Parece aviso de sobrevivência.
**EMÍLIA (Noviça Devota)**: "Não é vigiar. É... eu anoto as coisas. É um hábito. Emília von Karsten."
**VICTOR VANE**: "Victor Vane."
**EMÍLIA (Noviça Devota)**: "Eu sei."
Duas palavras, e o corredor parece ficar mais estreito.
**EMÍLIA (Noviça Devota)**: "A sua pasta de transferência estava na mesa da recepção hoje cedo. Bolsista integral, vindo do interior, notas máximas. E nenhum pedido de monitoria."
**VICTOR VANE**: "Você lê a pasta dos outros por diversão?"
**EMÍLIA (Noviça Devota)**: "Eu leio tudo o que cai na minha frente. Aqui, quem lê menos descobre mais tarde."
Ela tira do caderno um mapa dobrado. As margens estão cheias de letra miúda e três áreas riscadas em vermelho.
**EMÍLIA (Noviça Devota)**: "Bloco leste, escadaria principal, segunda porta. A secretaria fecha às duas. E isto aqui..."
A ponta do dedo dela pousa sobre as áreas vermelhas.
**EMÍLIA (Noviça Devota)**: "...são as alas interditadas. Ninguém explica o motivo, e eu aprendi que, quando ninguém explica, o aviso já foi dado."
Ela estende o mapa. Fica esperando. Não insiste, não sorri, não retira a mão. É pior do que se insistisse.

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Pegar o mapa. \"Obrigado.\" Só isso. (+Afeto Emília)"*
A palavra sai estranha da minha boca, como moeda de outro país. Dobro o papel e guardo.
A regra dois diz para desconfiar de quem sorri antes de oferecer. Ela sorriu antes de oferecer. Anoto.
**EMÍLIA (Noviça Devota)**: "Viu? Não doeu."
**VICTOR VANE**: "Ainda."
**EMÍLIA (Noviça Devota)**: "...Ainda."
> - 🔹 Escolha: *"\"Obrigado, mas eu resolvo.\" (+Autonomia / +Dúvida Emília)"*
**EMÍLIA (Noviça Devota)**: "Todo mundo diz isso no primeiro dia."
**VICTOR VANE**: "E no segundo?"
**EMÍLIA (Noviça Devota)**: "No segundo, quase todos já descobriram que a escola não dá medalha para quem resolveu sozinho."
Ela não discute. Apoia o mapa no parapeito da janela, dobrado ao meio, como quem deixa um bilhete que alguém pode querer ou não.
> - 🔹 Escolha: *"\"Ninguém oferece um mapa de graça. O que você ganha com isso?\" (+Intelecto / +Dúvida)"*
Pela primeira vez, ela hesita de verdade. Os dedos apertam a borda do caderno.
**EMÍLIA (Noviça Devota)**: "Justo. É uma boa pergunta."
**EMÍLIA (Noviça Devota)**: "Eu ganho uma pessoa a menos para procurar depois que anoitecer."
**VICTOR VANE**: "Procurar?"
**EMÍLIA (Noviça Devota)**: "...É só um jeito de falar. Pegue, Victor. Ou não. Mas a pergunta foi boa."
Ela estende o papel de novo, e dessa vez não sorri. Eu pego. Não sei se foi por educação ou por medo de descobrir o que ela quis dizer.
**EMÍLIA (Noviça Devota)**: "Mais uma coisa, a única que eu realmente quero que você leve. Quando o sol começar a baixar, não fique vagando pelos corredores."
**VICTOR VANE**: "Existe toque de recolher?"
**EMÍLIA (Noviça Devota)**: "Existe um costume. Aqui, as duas coisas se parecem muito."
Ela vai embora sem olhar para trás. Só quem tem certeza do que anotou consegue andar assim.
Espero ela virar o corredor. Conto até dez. Depois volto e pego o mapa do parapeito, sem testemunhas, como quem recupera o que já era seu.
**VICTOR VANE**: "Isso não conta como ajuda. Eu só... encontrei."
Diante da porta da secretaria há um banco de madeira e uma garota sentada nele, curvada sobre um caderno. Uniforme preto, mangas puxadas até os dedos. No colarinho, um alfinete de prata com o número 31.
Ela escreve, risca, escreve de novo. A caneta falha. Ela a sacode, a morde, a sacode outra vez.
**NORA (Prisioneira das Criptas)**: "...Merda."
Levanta os olhos e me flagra encarando. São claros demais, e os cantos estão vermelhos de quem não dorme faz dias.
**NORA (Prisioneira das Criptas)**: "Você é o transferido, né? Todo mundo falou. 'O bolsista novo do interior.'"
**VICTOR VANE**: "Boa fama costuma chegar antes."
**NORA (Prisioneira das Criptas)**: "Má. Mas chegou antes mesmo."
Ela tenta rir, e a risada sai com a metade do tamanho. Os dedos da mão esquerda não param de tremer contra o caderno.
**NORA (Prisioneira das Criptas)**: "Tem uma caneta sobrando? A minha secou e eu preciso terminar isto antes que..."
O olhar dela escorrega para o relógio no fim do corredor.
**NORA (Prisioneira das Criptas)**: "...antes que ele chegue."

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Emprestar a caneta. (+Humanidade / Dívida de Nora)"*
**NORA (Prisioneira das Criptas)**: "Obrigada. De verdade. Te devo uma. Eu pago o que devo, pergunta pra qualquer um."
**VICTOR VANE**: "É só uma caneta."
**NORA (Prisioneira das Criptas)**: "Aqui, nada é só uma caneta."
Ela volta a escrever, mais rápido, como quem recebeu uma extensão de prazo. Eu devia dizer algo. Não sei o quê.
**NORA (Prisioneira das Criptas)**: "Meu mestre disse que me buscava depois da aula. Faz três semanas, mas ele disse."
Não sei o que é um 'mestre' neste lugar. Acho melhor não perguntar. Acho que isso também quebra uma regra.
> - 🔹 Escolha: *"\"Não tenho. Resolva sozinha.\" (+Orgulho Defensivo)"*
**NORA (Prisioneira das Criptas)**: "Tá."
Só isso. Nem raiva, nem surpresa. Ela baixa o rosto de volta para o caderno.
**NORA (Prisioneira das Criptas)**: "Todo mundo resolve sozinho aqui. Você vai se dar bem."
Não sei se foi uma bênção ou uma maldição. Pelo tom, ela também não.
**DIRETOR AMBRÓSIO**: "Sr. Vane! Entre, entre. O seu é o processo mais bonito da pilha."
O Diretor Ambrósio tem um sorriso largo, mãos dobradas sobre a mesa e olhos que acompanham o que eu digo com meio segundo de atraso, como um vídeo mal sincronizado.
Ele folheia a pasta grossa sobre o couro verde da escrivaninha. Uma tarja vermelha de 'RESTRIÇÃO DISCIPLINAR' está colada na capa, mas o dedo dele a ignora com indiferença ensaiada, descendo direto para o laudo médico anexado no fundo.
**DIRETOR AMBRÓSIO**: "Bolsa integral, notas máximas em ciências exatas... Um pequeno 'incidente' no estacionamento da sua antiga faculdade que nós gentilmente arquivamos... e nenhum parente a avisar em caso de emergência."
**VICTOR VANE**: "Sou órfão."
**DIRETOR AMBRÓSIO**: "Perfeito."
A palavra fica no ar uma fração a mais do que devia.
**DIRETOR AMBRÓSIO**: "Quer dizer: lamento muito, rapaz. Lamento muito."
Ele corrige a frase com o mesmo sorriso, na mesma velocidade. Como quem aperta o botão certo depois de apertar o errado. Seus olhos descem novamente para a linha sublinhada em dourado no laudo do hemograma.
**DIRETOR AMBRÓSIO**: "E, acima de tudo... uma biologia singularíssima. Rh Nulo. Sangue Dourado legítimo. A mantenedora desta academia aprecia alunos com... potencial de contribuição único."
A palavra fica no ar uma fração a mais do que devia.
**DIRETOR AMBRÓSIO**: "Quer dizer: lamento muito, rapaz. Lamento muito."
Ele corrige a frase com o mesmo sorriso, na mesma velocidade. Como quem aperta o botão certo depois de apertar o errado.
**DIRETOR AMBRÓSIO**: "Só falta uma formalidade. O Termo de Saúde Comunitária. Todo bolsista assina."
Duas páginas. A primeira fala em 'cidadania', 'solidariedade' e 'campanha semestral'. A segunda tem letra do tamanho de uma formiga.

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Assinar sem ler. A bolsa vale mais do que a briga."*
Rubrico as duas folhas. A regra um acabou de nascer com defeito: uma bolsa integral é só uma dívida com juros que eu ainda não sei contar.
**DIRETOR AMBRÓSIO**: "Excelente escolha! Os melhores alunos são os que confiam."
> - 🔹 Escolha: *"Ler a página dois antes de assinar. (+Intelecto)"*
Leio com o dedo, linha por linha, enquanto o Diretor tamborila a mesa num ritmo que não é o do relógio.
O material biológico coletado terá 'destinação a critério da Fundação mantenedora'. Não diz qual hospital. Não diz qual Fundação.
**VICTOR VANE**: "Que Fundação é essa?"
**DIRETOR AMBRÓSIO**: "A mantenedora."
**VICTOR VANE**: "Isso eu entendi. Qual é o nome dela?"
**DIRETOR AMBRÓSIO**: "Ninguém lê essa parte, Sr. Vane."
Ele repete a frase em seguida. Dessa vez, o sorriso chega depois das palavras.
Assino. Preciso da bolsa. Mas agora sei o que assinei, e isso é uma vantagem pequena. As melhores costumam ser.
> - 🔹 Escolha: *"Recusar. \"Prefiro doar quando eu escolher.\" (+Dúvida Elara)"*
O sorriso do Diretor não muda. É o resto do rosto que para. Por um segundo inteiro, ele parece uma fotografia dele mesmo.
**DIRETOR AMBRÓSIO**: "...Claro. A participação é voluntária."
**DIRETOR AMBRÓSIO**: "Bolsistas costumam participar."
Ele anota alguma coisa no canto da ficha. A caneta raspa o papel com uma pressa que não combina com a voz.
**DIRETOR AMBRÓSIO**: "Sua matrícula está concluída. O dormitório é o bloco norte. E, Sr. Vane..."
Os olhos dele finalmente me alcançam, no tempo certo, e é pior.
**DIRETOR AMBRÓSIO**: "...é prudente não ficar fora do dormitório depois do pôr do sol."
Três pessoas em uma só manhã, e todas me mandaram para casa antes do escuro. Quando todo mundo dá o mesmo conselho, a pergunta não é se existe um motivo.
A pergunta é por que ninguém o diz em voz alta.
No retrato, os olhos do Fundador voltam a me seguir. Só que agora tenho a impressão de que não estão me julgando. Estão anotando.
Uma manhã. Já devo uma bolsa, uma resposta e talvez um mapa. E a tarde nem começou.

---


### DIA 01 — Tarde (`evt_d01_tarde`)

O dormitório cheira a madeira velha e alvejante. A cama tem um colchão fino e a janela dá para outro muro. Largo a mala, troco de camisa — a da viagem está com o colarinho erguido de tanto suor — e saio.
De tarde, a escola parece uma coleção de poses. O sol baixo projetando sombras compridas. Ninguém corre — correr chama atenção. Todos andam depressa, que é diferente.
A diferença entre 'estou atrasado' e 'estou com medo' é a posição dos cotovelos.
O depósito anexo fica no fim de um corredor que ninguém varre. A porta está aberta. Lá dentro, alguém chora sem fazer barulho, o que exige prática.
Dois veteranos de braçadeira branca — monitores — encurralam um garoto de uniforme remendado contra as prateleiras. No chão, um frasco de cristal azulado estilhaçado numa poça que cintila.
Heitor" "Olha ele. O bolsista novo. Chegou na hora.
Bia" "Chegou na hora de assinar.
Teo" "Eu juro que não encostei. A prateleira... a prateleira já estava torta.
Bia estende uma folha em minha direção. No alto: Termo de Ressarcimento nº 112. Valor: quatro mil e oitocentos em créditos. O campo do responsável está em branco.
Número 112. Já existem cento e onze antes deste. Cento e onze vezes alguém assinou por um frasco.
Heitor" "É simples, Vane. Você assina como responsável. O valor sai dos seus créditos de bolsista, devagarinho. Ninguém sente.
Heitor" "O Teo já tem uma advertência. Mais uma e perde a vaga. Você chegou hoje, ninguém liga para o seu nome.
Bia" "Aqui ninguém é preso, Vane. Todo mundo só... deve.
Olho para o Teo. Meu estômago contrai em um espasmo seco.
O cheiro de poeira úmida do depósito evapora, substituído de repente pela memória física do asfalto molhado.
Flash físico: faróis de carro cortando a garoa no estacionamento. O impacto seco dos meus nós dos dedos contra a mandíbula de um agressor que achava que podia tocar em quem quisesse.
Eu já fui esse garoto. Já quebrei a mão para tentar defender alguém que estava encurralada sem poder revidar... e a recompensa foi ver o homem caído se levantar, sacar um telefone e comprar a polícia antes que eu pudesse respirar.
Aqui estão eles de novo. Duas hienas de braçadeira branca empurrando a conta para uma presa que não sabe morder.
Eu conheço esse roteiro. Sei exatamente o gosto amargo da última página.

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Pegar a caneta. \"Eu assumo.\" (+Humanidade / +Coragem / Quebra Regra 1)"*
Teo" "Não! Você não precisa...
**VICTOR VANE**: "Eu assumo."
A regra um grita. Meu nome vai para o campo em branco. Eu preencho com mais firmeza do que sinto.
Heitor" "Muito nobre, novato. Bem-vindo à escola.
> - 🔹 Escolha: *"Pegar o termo e ler em voz alta. Com atenção às brechas. (+Intelecto / +Dúvida Elara)"*
**VICTOR VANE**: "Termo número cento e doze. Data em branco, testemunha em branco, responsável em branco. Assinar isto é assinar um cheque sem valor."
**VICTOR VANE**: "E o frasco está rachado no fundo, de fábrica. Ele não quebrou na queda. Ele cedeu. Vocês sabiam do lote."
A cor some do rosto da Bia. Heitor aperta o maxilar, mas o dedo dele já está procurando o nome da próxima vítima.
Heitor" "Um bolsista novo que lê. Que aborrecimento.
Teo olha para mim como quem acabou de ser puxado de dentro d'água. Eu devia me sentir bem. Sinto apenas que acabei de acender uma luz em um quarto onde as pessoas preferem o escuro.
> - 🔹 Escolha: *"Virar as costas. \"Não toquei em nada. Resolvam entre vocês.\" (-Humanidade)"*
Teo" "Por favor...
Não olho. Se eu olhar, eu fico. Se eu ficar, eu pago. Regra um, regra três, regra quatro — todas concordam comigo.
A voz do Teo me segue pelo corredor até virar um som que eu consigo fingir que não é uma voz.
Um silêncio estranho cai no depósito. Não é o silêncio de quem foi vencido. É o silêncio de quem ouviu passos.
No fim do corredor, o ruído das conversas desaparece de uma vez. Alguém está vindo. E todo mundo sabe quem.
Uniforme branco imaculado. Cabelos brancos, olhos vermelhos. A Presidente do Grêmio Estudantil atravessa o corredor e o corredor se afasta dela como água de um barco.
Não há raiva no olhar dela. Só a atenção clínica de quem observa insetos num vidro.
**ELARA (Presidente do Grêmio)**: "Um bolsista que paga por um frasco que não quebrou. Nobre, ou ingênuo. Na minha experiência, a diferença dura uma semana."
**VICTOR VANE**: "E depois de uma semana?"
**ELARA (Presidente do Grêmio)**: "Depois, o nobre vira cobrador. Ou vira cobrança."
**ELARA (Presidente do Grêmio)**: "Seu coração não acelerou nem ao assinar quatro mil e oitocentos. Ou é coragem, Sr. Vane, ou é desinteresse pela própria vida. Eu descobrirei qual."
**ELARA (Presidente do Grêmio)**: "Notável. O termo sem testemunha, o frasco rachado de origem. Heitor, Bia: três semanas de turno na rouparia."
Heitor" "Presidente, nós só—
**ELARA (Presidente do Grêmio)**: "Eu sei exatamente o que vocês só."
**ELARA (Presidente do Grêmio)**: "E você, Sr. Vane, acaba de ganhar a atenção de duas pessoas que não gostam de ser lidas."
**VICTOR VANE**: "Atenção?"
**ELARA (Presidente do Grêmio)**: "Aqui, atenção é uma moeda. Cuide de quanto gasta."
**ELARA (Presidente do Grêmio)**: "Sensato. A maioria dos novatos leva uma semana para aprender que o problema alheio é um luxo."
Era o elogio mais frio que já recebi. E mesmo assim algo em mim se encolheu, como se tivesse sido aprovado por um motivo errado.
**ELARA (Presidente do Grêmio)**: "Seu coração está muito calmo, Sr. Vane. Gosto de calma. Ela costuma esconder coisas interessantes."
**ELARA (Presidente do Grêmio)**: "Heitor. E a trinta e um?"
Heitor" "Não voltou ao dormitório desde ontem, Presidente. Continua comprando nas caldeiras.
**ELARA (Presidente do Grêmio)**: "Sem mestre, sem registro, sem autorização para sair à noite. Se ela cruzar um portão depois do pôr do sol, quero ser avisada. Antes do pôr do sol, de preferência."
Trinta e um. O número do alfinete no colarinho da garota do banco. Fico em silêncio. Essa é uma das poucas coisas que sei fazer bem.
Heitor" "Seu cadastro de bolsista está na sala da monitoria, segundo andar. Libera às seis. Se não for retirado até as seis e meia, a bolsa entra em suspensão.
**VICTOR VANE**: "Vocês seguraram o meu cadastro."
Heitor" "Seguramos o seu futuro, Vane. É diferente.
Sem o cadastro, a bolsa não ativa. Sem a bolsa, eu não tenho cama. Sem cama, eu não tenho para onde voltar. Cláusulas, cláusulas.
O sino do pátio bate seis vezes. Lá fora, o dourado do entardecer vira cobre. Os últimos estudantes passam por mim em silêncio de procissão, de cabeça baixa, como se obedecessem a uma ordem invisível.
No final da galeria envidraçada que dá para a ala velha da academia, meus passos travam subitamente.
Parada junto a um dos arcos de pedra, observando o pátio banhado em luz âmbar, há uma jovem.
Ela não veste o uniforme preto dos calouros, nem as túnicas engomadas da elite do Grêmio. O vestido escuro, de cortes aristocráticos e tecido pesado, parece pertencer a um século esquecido pela história.
A luz do entardecer toca o perfil dela de lado. Cabelos carmesins. Postura reta, mas não rígida — o tipo de postura de quem parou de se preocupar com o que parece há tempo demais para se calcular.
Ela olha para o pátio como quem não está vendo o pátio.
O ar aqui tem um gosto diferente. Mirra. Ferro. Algo mais fundo.
Os pelos do antebraço erguem contra o tecido da camisa.
**VICTOR VANE**: "(Eu sonhei com ela.)"
Não é uma impressão. Não é cansaço da viagem. O rosto é o mesmo. Os cabelos são os mesmos. Os olhos que ela vai levantar daqui a três segundos serão os mesmos.
Quase em câmera lenta, como se sentisse o peso da minha presença, ela desvia o olhar do nada e me percebe a encarando à distância.
Nossos olhares se cruzam por uma fração de segundo. Não há choque, curiosidade ou escárnio em seu semblante — apenas uma indiferença muda.
Ela simplesmente me ignora, desvia os olhos como se eu fosse um detalhe invisível na paisagem e dá meia-volta, saindo calmamente de onde estava.
Fico parado. Ela vai embora sem pressa, como se a minha presença fosse um detalhe que ela catalogou e descartou no mesmo segundo.
Minha mão esquerdou tinha se movido na direção dela. Não sei o que ia fazer. Chamo de volta.
**VICTOR VANE**: "(Coincidência. Cansaço da viagem. Isso é o que eu vou anotar.)"
Pego o cadastro na monitoria. Subo. Desço. Quando termino, a janela mostra um céu sem nenhuma cor.

---


### DIA 01 — Noite (`evt_d01_noite`)

As luzes do corredor trocam de cor sem barulho. De âmbar para carmesim, como se alguém tivesse virado uma chave que eu não vi.
O ar tem gosto de cobre. As paredes parecem mais próximas. E, ao longe, um som seco, repetido: raspar. Parar. Raspar.
Eu sei que devia voltar para o dormitório. Eu sei. Mas o atalho pela ala leste economiza dez minutos, e dez minutos é a diferença entre cumprir um prazo e perder uma bolsa.
Orgulho disfarçado de responsabilidade. Eu ainda não sabia que esse era o meu defeito.
A ala interditada. Um corredor largo, vazio. E, na parede inteira, centenas de linhas escritas à tinta, empilhadas até o teto, sem nenhum espaço.
ELE VEM DEPOIS DA AULA. ELE VEM DEPOIS DA AULA. ELE VEM DEPOIS DA AULA.
Ao pé da parede, de costas, uma garota de uniforme preto. A mão esquerda escreve sem parar. Na direita, uma caneta. A minha.
**NORA (Prisioneira das Criptas)**: "A aula acabou. Não acabou? A aula... acabou."
**VICTOR VANE**: "Nora?"
Ela vira o rosto devagar. Os olhos agora são só o vermelho que sobrou dos cantos. Unhas quebradas. Veias negras pulsando no pescoço como cabos sob a pele.
**NORA (Prisioneira das Criptas)**: "Você é o da caneta."
**NORA (Prisioneira das Criptas)**: "Eu te devo uma caneta. Eu pago o que devo. Eu... eu pago."
A voz racha no meio da frase, e, por um instante, volta a ser a mesma da secretaria. Depois, a voz escorrega.
**NORA (Prisioneira das Criptas)**: "O que não tinha caneta. Eu achei uma. Achei... no chão."
Mentira. Mas ela acredita nessa mentira com a mesma intensidade com que precisa de uma.
**NORA (Prisioneira das Criptas)**: "A parede está batendo. Você não ouve? Tum. Tum. Ela pede sangue limpo, e eu só tinha o do lote. Eu paguei! Disseram que era limpo!"
**VICTOR VANE**: "Nora, você precisa de ajuda. Eu vou chamar—"
**NORA (Prisioneira das Criptas)**: "Cala a boca! Cala esse coração barulhento!"
As garras chegam antes que eu feche o braço. O impacto na garganta é seco — mais pancada do que corte, até o corte chegar.
Caio de lado. O piso de pedra faz barulho quando minha cabeça bate. O sangue sai quente. O chão está muito frio.
Ela fica sobre mim. A mão erguida banhada em sangue. Fica ali, ofegante, como se o gesto tivesse travado no meio do caminho.
O olhar dela desce devagar até a caneta, ainda cravada trêmula entre os próprios dedos.
**NORA (Prisioneira das Criptas)**: "...Eu ia te pagar."
**NORA (Prisioneira das Criptas)**: "...Você não tinha caneta. Eu só queria escrever."
Passos pesados da patrulha do Conselho ecoam com urgência no fim do corredor. Ela recua atordoada, tropeça no próprio medo e foge para o breu das sombras.
O sangue empoça devagar. Esse é um detalhe que eu não esperava notar — a lentidão. Achei que ia ser mais rápido.
Não gritei. A regra quatro exigiria uma explicação melhor para isso. Não tenho.
Eu não vim de tão longe para morrer num corredor que nem consta no mapa.
A patrulha se afasta. O corredor engole o eco das botas.
Minha visão vai reduzindo. Começa pelas bordas — como quando você aperta o olho contra um vidro escuro e o campo vai diminuindo até sobrar só o centro.
E então chega o cheiro. Mirra. Ferro. Algo antigo que não tem nome no vocabulário que eu aprendi.
Passos. Lentos. Sem pressa de ninguém que tenha medo de chegar tarde.
É ela.
Do pesadelo. Da galeria de tarde. Da pergunta que eu ainda não sei responder.
Ela para ao meu lado. Abaixa o joelho direito no piso manchado — sem hesitar, sem proteger o vestido.
A cabeça dela inclina de lado, como quem avalia o ângulo certo para dissecar algo que ainda está se mexendo.
**MESTRA**: "Fascinante. Você não gritou."
**MESTRA**: "Os mortais nessa posição imploram a um deus surdo. Ou chamam pela mãe. Você só cravou as unhas na pedra e se recusou a apagar."
**MESTRA**: "Que orgulho patético."
**VICTOR VANE**: "Eu não vim... de tão longe... para morrer no escuro como descarte."
**MESTRA**: "Descarte. Que palavra interessante para usar quando se tem a traqueia aberta."
**MESTRA**: "Qual é o seu nome?"
**VICTOR VANE**: "Victor. Victor Vane."
**MESTRA**: "Vane. Um nome que só existe para apontar o vento. Responda sem pensar, Victor Vane: o que você deve?"
**VICTOR VANE**: "...O quê?"
**MESTRA**: "Todo mundo morre devendo alguma coisa. Qual é a sua dívida?"
**VICTOR VANE**: "Nada. Eu não devo nada a ninguém."
Ela ri. Uma risada baixa, rouca e demorada, que parece vibrar diretamente na raiz dos meus ossos.
**MESTRA**: "Que mentira cara. Eu admiro mentiras caras."
Ela ergue a mão pálida e passa a unha afiada pelo próprio pulso. O sangue brota denso, escuro como rubi líquido, exalando calor proibido e poder primordial.
**MESTRA**: "Uma prorrogação. Abra a boca."
**VICTOR VANE**: "O preço..."
**MESTRA**: "Prorrogação tem juros, Victor. Mas ninguém jamais perguntou antes. Eles só agradecem. Depois."
Por uma fração de segundo, o deboche se esvai de sua postura. Ela me encara no fundo dos olhos como quem enxerga através de séculos de solidão.

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Agarrar o pulso dela. \"Eu aceito. Mas é só um empréstimo.\" (+Coragem / +Afeto Lility)"*
**MESTRA**: "Chame como quiser. O contrato não se importa com o nome."
> - 🔹 Escolha: *"\"Qual é o juro?\" (+Intelecto / Postura Pragmática)"*
**MESTRA**: "Pragmático até sangrando. Que delícia."
**MESTRA**: "Você vai descobrir que não é cobrado em dinheiro."
> - 🔹 Escolha: *"\"Se é para virar bicho de estimação... sirva algo decente.\" (+Charme / +Afeto Lility)"*
**MESTRA**: "Atrevido até na sarjeta. Beba, insolente. A minha safra é melhor que qualquer refeição que você já teve na vida."
O sangue dela desce como brasa líquida. A carne rasgada se fecha com estalos rápidos, e o meu coração dá uma última batida... e para.
Eu continuo aqui. Respirando por hábito. Sem pulso nenhum.
E então algo mais fundo que o meu peito responde ao choque do pacto: uma batida lenta, cavada e titânica, vinda do mais profundo dos alicerces. As pedras do chão tremem sob meus joelhos. Poeira de séculos despenca das abóbadas.
O alarme de contenção estala mudo nos tubos de cobre. Algo que dormia sob a Academia São Cipriano abriu um dos olhos.
**MESTRA**: "...Interessante."
**VICTOR VANE**: "Você sentiu isso?"
**MESTRA**: "Senti o quê? O seu pulso foi embora, meu bem. Ouça o silêncio. Todo mundo se acostuma."
Ela mente. Eu anoto.
**VICTOR VANE**: "Por que me salvou? Você não parece do tipo que faz caridade."
**MESTRA**: "Hábito. Eu estava entediada, e a sua teimosia me pareceu um passatempo razoável."
Ela diz 'tédio' com a boca. Com os olhos, diz outra coisa. Eu ainda não sei o nome dela.
**VICTOR VANE**: "E como devo te chamar?"
**MESTRA**: "Lility. E quando eu perguntar algo, você responde 'Mestra'."
**VICTOR VANE**: "Prefiro Lility."
**MESTRA**: "Por enquanto."
O tabuado estala. As duas portas se abrem num estrondo seco!
A figura que surge na soleira parece talhada em mármore gélido. Uniforme branco impecável, sem uma única dobra fora do lugar — o emblema de ouro do Grêmio Estudantil reluzindo no peito com a altivez de quem se julga a única guardiã da ordem.
Cabelos alvos como geada e dois olhos carmesins afiados que varrem o chão manchado de sangue, cravando-se em Lility com fúria contida.
**ELARA (Presidente do Grêmio)**: "Lility. Eu a proibi terminantemente de produzir novos membros ou lacaios neste campus."
**MESTRA**: "Tecnicamente, Presidente, ele é um ghoul. 'Lacaio' pressupõe um contrato de emprego com benefícios. Achei que vocês, os puro-sangues da diretoria, fossem obcecados pelo rigor da lei."
**ELARA (Presidente do Grêmio)**: "Cale a boca. Você perdeu qualquer direito de ironizar as nossas leis no instante em que cruzou esta fronteira."
O olhar de Elara se desvia devagar de Lility e recai sobre mim. Por um instante, a rigidez austera de sua postura cede a algo inesperado — não nojo, nem desprezo... mas uma piedade sombria e trágica.
**ELARA (Presidente do Grêmio)**: "Nome."
**VICTOR VANE**: "Victor. Victor Vane."
**ELARA (Presidente do Grêmio)**: "O bolsista transferido. Você chegou esta manhã com uma mala surrada e um histórico acadêmico exemplar, Sr. Vane. Tinha uma vida mortal inteira pela frente... E agora olhe para você."
**VICTOR VANE**: "Eu fui atacado no corredor. Uma aluna... Nora Vasques."
Por um microssegundo, a máscara imperturbável da Presidente falha. Os lábios dela se comprimem.
**ELARA (Presidente do Grêmio)**: "...Nora. A cobaia trinta e um da lista de contenção."
**VICTOR VANE**: "Ela estava enlouquecida, falando que a parede batia e pedindo sangue limpo! O que vocês vão fazer com ela?!"
**ELARA (Presidente do Grêmio)**: "O que for necessário. Os executores já recolheram o que sobrou. E, para ser sincera, Sr. Vane... você deveria ter tido o mesmo destino."
**VICTOR VANE**: "O quê?!"
**ELARA (Presidente do Grêmio)**: "A morte humana. O descanso da terra."
Ela dá um passo à frente, apontando a mão enluvada na direção de Lility com um ressentimento cortante.
**ELARA (Presidente do Grêmio)**: "Você não compreende a atrocidade que esta mulher cometeu contra a sua existência, garoto. Os mortais têm alma, têm um ciclo que se fecha e têm o direito sagrado de descansar em paz. Mas nós? Os da nossa espécie não encontram céu e nem inferno ao fechar os olhos."
**ELARA (Presidente do Grêmio)**: "Quando um vampiro é destruído, só existe o Vazio. O esquecimento eterno ou um torpor milenar sob a lama fria. Ao te transformar para satisfazer os próprios caprichos, ela roubou o seu descanso eterno e te acorrentou a uma fome que vai queimar a sua consciência dia após dia até você virar um monstro sem mente como a Nora."
**MESTRA**: "Que discurso comovente, Elara. Quase me faz esquecer que a sua 'misericórdia' aristocrática sempre termina com uma lâmina de prata no coração de quem não tem berço nobre para pagar as propinas do Grêmio."
**ELARA (Presidente do Grêmio)**: "Você é uma pária exilada, Lility. Já toleramos a sua insolência de baixo clero por tempo demais — inclusive quando foi flagrada rondando as catacumbas do subsolo, cobiçando o que não lhe pertence. Mas forçar a criação de um ghoul após o Tratado... isso é traição direta à Máscara."
Elara se vira para mim com passos firmes. O ar congela ao redor de seus dedos.
**ELARA (Presidente do Grêmio)**: "...Há um ritmo no seu peito que não é seu. Uma ressonância que este colégio não pode tolerar solta."
**MESTRA**: "Tire as mãos dele, Presidente."
**ELARA (Presidente do Grêmio)**: "Quem dita os termos sou eu."
A palma da mão dela bate no meu peito antes que eu registre o movimento. Frio. Depois quente. Depois uma coisa que não é nem um nem outro — é pressão dentro do osso, como uma broca sem broca.
**VICTOR VANE**: "Aaargh...! O que... o que você fez?!"
Atrás de mim, um estalo seco ecoa no ar. Fios etéreos avermelhados saltam da runa no meu peito e chicoteiam o ar até os pulsos de Lility!
A pele pálida dela se rasga em vergões sangrentos. Ela dá um passo em falso, respirando entre os dentes cerrados pela dor súbita — a essência selada de seu corpo antigo não tem força para repelir a magia de contenção moderna.
**MESTRA**: "Ugh... Francamente, Presidente... Cuidado com o carpete. Manchas de sangue não saem fácil."
Ela força um sorriso debochado, mas seus dedos tremem ao segurar os pulsos feridos. Ela está sofrendo de verdade.
**ELARA (Presidente do Grêmio)**: "O Grilhão está selado. Cada falha sua queima nela. Cada exposição cai sobre ela. É assim."
**VICTOR VANE**: "Isso é covardia."
**ELARA (Presidente do Grêmio)**: "É contabilidade. Há diferença, Sr. Vane. Aprenda logo qual."
**ELARA (Presidente do Grêmio)**: "Amanhã de manhã. Ao nascer do sol. Compareça ao Gabinete da Presidência para a sua audiência formal. Decidiremos se você tem serventia para o campus... ou se a execução será aplicada como misericórdia antes da sua primeira crise de fome."
**ELARA (Presidente do Grêmio)**: "E você, Lility: está formalmente confinada à ala interditada. Se colocar os pés nas áreas nobres ou na diretoria, meus executores farão você sangrar até secar."
A porta bate num estrondo que faz o pó do teto cair. O silêncio que sobra é sufocante.
Lility olha para os pulsos. Os vergões já param de sangrar — mas ela continua olhando, como se o que ela vê não fossem feridas novas, mas uma conta velha que alguém finalmente imprimiu.
**MESTRA**: "Boa noite, cachorrinho. Amanhã você vai ter muitas perguntas. E eu... poucas respostas."
Ouço o silêncio. Não o meu coração — esse parou. O silêncio do corredor, das paredes, do ar.
A regra um prometia que eu nunca ia dever. Hoje assinei débito com a minha própria vida.
Dia um.

---


### DIA 02 — Manha (`evt_d02_manha`)

Acordei sem ter dormido. A gola da camisa está dura de sangue seco. Passei dez minutos procurando uma cicatriz no pescoço. Não achei nenhuma.
Dois executores de branco me buscaram às sete e meia. Não disseram nada. Não precisavam.
Lá fora, os vitrais projetam losangos dourados no mármore. Aqui dentro, o meu peito é mudo como câmara fria.
O gabinete cheira a papel envelhecido e decisão irreversível. No canto, numa poltrona que parece pequena demais para a função que ele representa, está o Diretor Ambrósio.
Ele assoberbou a cabeça antes de Elara falar. Treino, provavelmente.
Elara está de pé atrás da pesada escrivaninha de mogno escuro. Não sentada — de pé. As mãos enluvadas apoiadas na madeira polida com a autoridade fria de quem não precisa de apresentações.
O olhar dela varre minha silhueta da gola até os sapatos. Sem pressa. Sem desprezo. Apenas a inspeção metódica de uma cirurgiã diante de um espécime anômalo.
**ELARA (Presidente do Grêmio)**: "Garganta aberta às dez da noite. Sete da manhã, sem cicatriz. Sem pulso."
**ELARA (Presidente do Grêmio)**: "Não pergunte como sei. Você aprende a perceber o silêncio onde deveria haver batimento."
Ela pousa algo sobre a mesa, sem pressa. Um alfinete de prata polida com um número gravado em baixo-relevo: 31.
O metal tilinta levemente sobre o mogno, refletindo a seriedade fúnebre de seus olhos carmesins.
**ELARA (Presidente do Grêmio)**: "Encontrado no corredor leste, onde você caiu. O número da aluna Nora."
**VICTOR VANE**: "E ela?"
**ELARA (Presidente do Grêmio)**: "Contida. Onde a fome não a alcançará mais."
**VICTOR VANE**: "Isso é um eufemismo para execução?"
**ELARA (Presidente do Grêmio)**: "É o protocolo para quem perde o controle da própria sede. E você está a um milímetro de ter a mesma ficha encerrada, Sr. Vane."
**ELARA (Presidente do Grêmio)**: "Estacionamento. Noite. Um docente de sobrenome caro e um punho que foi mais rápido que o bom senso."
Ela desliza uma cópia amarelada do boletim de ocorrência sobre o mogno. A imagem mental do aperto de mãos corrupto entre o diretor e a autoridade queima nos meus olhos.
**ELARA (Presidente do Grêmio)**: "Agressão qualificada contra um membro da cátedra. Um inquérito que evaporou mediante um aperto de mãos e um acordo confidencial da reitoria para preservar a honra da família do agressor."
Ela apoia as mãos enluvadas sobre o mogno da escrivaninha e se inclina para a frente. Não há ódio no semblante dela — apenas uma seriedade fúnebre e pesada.
**ELARA (Presidente do Grêmio)**: "E a garota que você tentou proteger assinou contra você. O diretor arquivou o B.O. com um sorriso, e você foi empurrado para fora da sua própria vida."
**ELARA (Presidente do Grêmio)**: "Exceto pela nossa lista de transferência. Porque nós lemos mais devagar — e chegamos sempre à mesma página."
**ELARA (Presidente do Grêmio)**: "Rh Nulo. Sangue Dourado. Um a cada seis milhões de nascidos. E você achou que era azarado."
**ELARA (Presidente do Grêmio)**: "Ontem de manhã você era um mortal, Sr. Vane. Tinha o direito sagrado de tropeçar, envelhecer, adoecer e... quando a hora chegasse, descansar em paz."
**ELARA (Presidente do Grêmio)**: "Agora você é um cadáver reanimado. Uma aberração incompleta acorrentada à coleira de uma vampira exilada que você sequer conhece."
**VICTOR VANE**: "Eu não escolhi ser atacado. E não escolhi ser transformado."
**ELARA (Presidente do Grêmio)**: "Eu sei. É exatamente por isso que sinto pena de você."
Piedade.
Eu ouço a palavra e fico procurando o truque. Não acho.
**ELARA (Presidente do Grêmio)**: "Você acredita em algo além da sua própria teimosia, Victor?"
**ELARA (Presidente do Grêmio)**: "Mortais têm esse privilégio. A fé como anestesia. Nós não."
**ELARA (Presidente do Grêmio)**: "Quando um dos nossos morre, não há cerimônia. Não há testemunha. Há o chão. Há o silêncio. E há quem varreu."
**ELARA (Presidente do Grêmio)**: "Se eu chamasse os executores agora, seria o único favor genuíno que este colégio te faria. Você ainda dorme, Victor. Ainda tem restos de algo que parece consciência. Nora não tinha mais isso. Leva oito semanas, em média, perder o que te sobrou."
**ELARA (Presidente do Grêmio)**: "Portanto, responda olhando nos meus olhos: por que eu deveria deixá-lo sair vivo desta sala? O que faz você achar que a sua existência vale o risco da nossa Máscara?"

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"“Porque eu não fujo de dívidas. E me recuso a ser descartado de novo.” (+Coragem / O Credo de Victor)"*
**VICTOR VANE**: "Eu passei a vida inteira aprendendo que ninguém me dá nada de graça, Presidente. O meu antigo orientador tentou me empurrar para a sarjeta para salvar o próprio nome, e eu sobrevivi. Não vim até esta capital para ser executado pela 'misericórdia' de ninguém."
**VICTOR VANE**: "Eu tenho regras. A quarta diz: nunca ser descartável. Se a minha vida agora tem uma dívida de sangue, eu vou pagar até o último centavo. Mas eu decido como ando."
**ELARA (Presidente do Grêmio)**: "Olha só... O lacaio tem dentes. A maioria dos que provam do sangue rastejam implorando por clemência. Mas você se agarra ao próprio orgulho como se fosse um escudo."
**ELARA (Presidente do Grêmio)**: "A sua existência é uma fissura perigosa na ordem. Mas a sua teimosia... é fascinante. E eu aprecio peças que se recusam a quebrar no primeiro impacto."
> - 🔹 Escolha: *"“Matar um bolsista no segundo dia destrói a Máscara mais rápido do que a minha sede.” (+Intelecto / +Afeto Elara)"*
**VICTOR VANE**: "Um estudante transferido desaparecido nas primeiras vinte e quatro horas abre uma investigação no Ministério da Educação, traz a polícia para o campus e atrai a atenção dos caçadores que vocês tanto querem longe."
**VICTOR VANE**: "Eu tenho disciplina analítica. Posso me controlar, seguir as regras e ser útil ao Grêmio como uma ponte entre os dois lados. Executar-me agora cria uma anomalia burocrática impossível de varrer para baixo do tapete."
**ELARA (Presidente do Grêmio)**: "Olha só. Ele pensa antes de sangrar."
**ELARA (Presidente do Grêmio)**: "Raciocínio frio, avaliação de danos colaterais e pragmatismo político. Você tem razão: um cadáver bolsista agora é um problema administrativo caro demais. Continue assim e talvez chegue vivo ao próximo mês."
> - 🔹 Escolha: *"“Uniforme branco impecável, Presidente. Tem medo de sujar com o meu sangue?” (+Charme / +Dúvida Elara)"*
**VICTOR VANE**: "Uniforme branco imaculado, gabinete banhado a ouro e discursos poéticos sobre misericórdia... Tem medo de sujar as luvas com o sangue de alguém sem sobrenome aristocrático?"
**VICTOR VANE**: "Ou o que realmente incomoda o Grêmio é perceber que um humano qualquer tem mais coragem de encarar a realidade do que toda essa sua nobreza encenada?"
**ELARA (Presidente do Grêmio)**: "Sujeira se limpa com alvejante, Sr. Vane. Insolência se extirpa pela raiz com lâmina de prata. Guarde as ironias para quando não estiver cercado pelos meus carrascos."
**ELARA (Presidente do Grêmio)**: "Mas admito... é raro ver alguém com o coração parado falar com tanta vivacidade. Vamos ver quanto tempo esse sarcasmo dura quando a primeira crise de abstinência rasgar o seu estômago."
Ela se endireita. A postura volta a ser a de uma soberana absoluta.
**ELARA (Presidente do Grêmio)**: "Há uma regra mais antiga do que esta academia, Sr. Vane: ninguém de fora pode saber. Ninguém pode sequer suspeitar."
**ELARA (Presidente do Grêmio)**: "Houve uma era em que os nossos ancestrais foram descuidados... e a água corrigiu isso. A Máscara não é vaidade ou protocolo estudantil: é a única coisa que impede o céu de olhar para nós outra vez."
**ELARA (Presidente do Grêmio)**: "Se você quebrar o sigilo, a punição não virá apenas dos meus carrascos. O mundo inteiro cobra a conta."
Ela abre uma pasta de couro e desliza uma folha timbrada pela mesa de mogno. No topo, grafado em caligrafia de ferro: Termo do Grilhão.
I. A Máscara é inviolável. Nenhum humano comum presencia ou suspeita do que somos.
II. Lility permanece estritamente confinada à ala interditada. Os atos de um são cobrados do outro.
III. A alimentação será feita exclusivamente por bolsas filtradas da enfermaria. Caça de alunos é crime de execução imediata.
IV. Toda e qualquer Exposição pública é paga em carne viva de quem o criou.
V. O Grêmio revisará o seu termo e o seu destino conforme o estado da escola e o avanço da anomalia do Eclipse.
**VICTOR VANE**: "O alinhamento do Eclipse está avançando a cada ciclo. A cidade inteira está sentindo as anomalias."
**ELARA (Presidente do Grêmio)**: "Então aproveite enquanto o campus ainda está de pé para me convencer de que a misericórdia de deixá-lo respirar não foi um erro de cálculo."
Ela estende uma caneta de aparo dourada. Há espaço, na margem inferior, para uma única cláusula condicional.

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Cláusula IV. “Cobrem de mim. Não dela.” (+Humanidade / Grilhão Compartilhado)"*
**VICTOR VANE**: "Se eu cometer um deslize, cobrem de mim. Ela me salvou da morte, quer você aprove o método ou não. Eu não empurro as minhas contas para as costas de ninguém."
Elara me encara por um longo segundo, visivelmente desconcertada por um mortal defender a criatura que o amaldiçoou.
**ELARA (Presidente do Grêmio)**: "O Grilhão não negocia a punição primária. Mas posso dividi-la. Cada choque que a carne dela receber por sua causa agora também rasgará a sua própria pele."
**ELARA (Presidente do Grêmio)**: "Curioso... Você prefere sangrar a dever favores a uma vampira. Concedido."
> - 🔹 Escolha: *"Cláusula III. “Duas bolsas por semana não bastam.” (+2 Bolsas / Informante de Elara)"*
**VICTOR VANE**: "Duas bolsas por semana não mantêm um ghoul recém-criado lúcido. Se o Grêmio quer que eu passe despercebido nas aulas, preciso de sustento real."
**ELARA (Presidente do Grêmio)**: "Eu aprecio quem sabe negociar custos operacionais. Duas bolsas extras entregues na enfermaria toda semana. Em troca, relatórios detalhados: quem anda investigando as caldeiras e quem faz perguntas sobre as catacumbas do subsolo."
**VICTOR VANE**: "Isso é espionagem interna."
**ELARA (Presidente do Grêmio)**: "Isso é diplomacia aplicada, Sr. Vane. A diferença é a quem se deve lealdade."
> - 🔹 Escolha: *"Assinar como está. (Sem exigências)"*
**ELARA (Presidente do Grêmio)**: "Quem assina um contrato draconiano sem negociar uma vírgula ou confia cegamente em mim... ou planeja quebrar cada linha na primeira oportunidade. Qual dos dois, Sr. Vane?"
**VICTOR VANE**: "Prefiro que a Presidente descubra com o tempo."
**ELARA (Presidente do Grêmio)**: "Ambas as respostas servem aos meus propósitos."
Pressiono a pena contra o pergaminho e assino. A tinta parece fria como gelo sob as pontas dos meus dedos.
No canto escuro do gabinete, o Diretor Ambrósio murmura baixinho, ajeitando a gravata borboleta: 'A Presidente tem toda a minha confiança... Tudo em perfeita conformidade com as diretrizes educacionais.'
**ELARA (Presidente do Grêmio)**: "Uma última coisa, Victor. O que você viu ontem na ala leste... e a pulsação colossal que sentiu sob o piso de pedra... não existiram."
**VICTOR VANE**: "Você também sentiu. O chão inteiro respondeu ao sangue dela."
**ELARA (Presidente do Grêmio)**: "Eu não senti nada. E se você valoriza o que sobrou da sua existência, esquecerá que o subsolo desta escola tem profundidade."
Ela mente. Duas vezes em doze horas, a mesma mentira arrogante vinda de quem me exige transparência absoluta.
A regra três das minhas anotações: nunca ser o último a saber. Cheguei ontem, estou há um dia nesta academia, e já querem me enterrar na ignorância.
Saio do Gabinete da Presidência e as pesadas portas de carvalho se fecham com um baque seco às minhas costas.
Solto a respiração que nem percebi que segurava. Minhas mãos ainda tremem, mas o mármore sob os meus sapatos é sólido.
Estou sob liberdade vigiada, com um Grilhão rúnico queimando no peito e a garganta seca como lixa. Mas estou vivo.
A partir de agora, as dependências da Academia São Cipriano estão abertas. Preciso explorar os setores, gerenciar minha sede e investigar o que esta escola esconde antes que a noite caia.

---


### DIA 03 — Manha (`evt_d03_manha`)

Nos Dias 3 e 4, percebo uma carteira vazia no fundo da sala com o nome raspado na madeira. Os alunos desconversam: uns dizem que a colega nunca existiu; outros, que foi transferida.
No arquivo médico anexo, encontro os pertences recolhidos da Ghoul Rival que me atacou no Dia 1: um cartão de estudante, uma folha de exercícios corrigidos e um bilhete amassado dizendo 'Não se esqueça de me esperar depois da aula'.
**EMÍLIA (Noviça Devota)**: "Você está olhando esses pertences há cinco minutos, Victor. Ela tentou matar você naquela noite, não foi?"
**VICTOR VANE**: "Sim. Mas enquanto eu lembrar apenas do ataque, fica fácil fingir que ela nasceu sendo um monstro. Se eu esquecer quem ela era antes, fica fácil fazer o mesmo com qualquer pessoa."
**EMÍLIA (Noviça Devota)**: "O nome dela foi alterado para 'transferida' no sistema oficial, Victor. Mentir é uma pessoa escondendo a verdade; alterar os registros significa que a instituição inteira quer que a mentira sobreviva."
**EMÍLIA (Noviça Devota)**: "Eu estou fazendo perguntas porque quero acreditar em você... mas você ainda não me contou como sobreviveu àquele corredor."
**VICTOR VANE**: "Você acha que eu sou seu inimigo, Emília?"
**EMÍLIA (Noviça Devota)**: "Você acha que eu sou?"
**VICTOR VANE**: "Acho que você ainda não decidiu o que eu sou."

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Admitir parte da verdade: 'Alguém me salvou naquela noite, mas estou preso a um segredo.' (+Confiança Emília)"*
**EMÍLIA (Noviça Devota)**: "Obrigada por não mentir para mim. Vou descobrir quem adulterou aquele sangue."
> - 🔹 Escolha: *"Desviar a conversa perguntando o que ela faria se eu estivesse infectado (+Intelecto / +Suspeita leve)"*
**EMÍLIA (Noviça Devota)**: "...Eu rezaria para que você ainda tivesse escolha."

---


### DIA 04 — Tarde (`evt_d04_tarde`)

Fim de tarde no Bloco Esquecido. O sol poente corta os vitrais empoeirados da sala de música em feixes de cobre e poeira suspensa.
De longe, nos corredores frios, um som me atraiu: notas limpas de piano, lentas, carregadas de uma melancolia tão antiga que o ar pareceu esfriar dois graus a cada compasso.
Lility está sentada ao piano de cauda. O vestido clássico de veludo escuro e detalhes rendados cobre os degraus do tablado. Os cabelos carmesins reluzem suavemente contra a madeira escura.
Dou dois passos silenciosos para dentro da sala. Encosto na moldura de carvalho carcomido.
Ela não me ouve. Os dedos pálidos deslizam sobre o marfim com precisão cirúrgica. Não há o deboche habitual nos lábios dela, nem a altivez predatória que ela ostenta para manter o campus à distância. Há apenas concentração. Uma dor sem pressa.
Uma tábua do piso estala sob meu peso.
As mãos de Lility travam num acorde dissonante que corta o silêncio como vidro trincado. Ela vira o rosto num solavanco — os olhos carmesins arregalados em um susto genuíno, antes que a máscara de senhora implacável consiga se recompor.
Ela se levanta do banco do piano devagar, o tecido do vestido farfalhando na penumbra. O olhar dela me mede da cabeça aos pés, recalculando a distância entre nós.
**MESTRA**: "Você tem o péssimo hábito de rastejar como rato, Victor. Se eu estivesse com sede de verdade, sua cabeça já estaria rolando sob o pedal."
**VICTOR VANE**: "A terceira sequência. Você errou a oitava antes do estalo da madeira."
Ela estreita os olhos. Um meio sorriso perigoso repuxa o canto da boca dela.
**MESTRA**: "Eu não errei. Essa partitura foi composta antes que seus ancestrais aprendessem a polir pedras. Ela não segue as regrinhas quadradas da sua academiazinha de burgueses."
**VICTOR VANE**: "Quem a compôs?"
**MESTRA**: "Alguém que esperou por uma embarcação que nunca chegou. A água subiu, cobriu as colunas da cidade... e a música ficou inacabada."
**VICTOR VANE**: "Então o compositor devia ter reescrito o final em vez de se afogar com a partitura na mão."
**MESTRA**: "Você realmente acha que todo final trágico pode ser recalculado, garoto? Que petulância mortal."
Ela dá um passo à frente, descendo do tablado. O perfume de mirra e ferro ancestral preenche a distância entre nós. Ela estende a mão delgada, envolvida pela renda negra, em minha direção.
**MESTRA**: "Se você se julga tão capaz de ditar o andamento das coisas... mostre. Sem instrumentos. Sem cálculos. Apenas o compasso."
**VICTOR VANE**: "Uma dança? Aqui?"
**MESTRA**: "Está com medo de que o seu cadáver não saiba acompanhar uma dama, Sr. Vane? Ou sua arrogância só serve para analisar termos de dívida?"
A regra um grita no meu ouvido: não dever favor a ninguém. Mas o Grilhão de Sangue no meu peito responde com um calor estranho — um pulsar compassado que não é de dor.
Eu estendo a mão. Meus dedos fecham sobre a renda fria.
Ela me puxa com uma força suave e incontestável. Giramos no meio da sala vazia.
Não há orquestra tocando. Não há música gravada nas caixas de som. Apenas o atrito das solas contra a madeira antiga e o som do vento fustigando as janelas de chumbo.
Ela se move com a leveza de quem já cruzou séculos de salões de baile, mas os passos não são mecânicos. Há um ritmo compartilhado entre nós — o sangue que ela me deu na noite da quase morte conversando com o meu próprio sangue.
A valsa desacelera até estancarmos no centro do salão. Os corpos próximos. O calor contido na respiração dela roça a curva do meu maxilar.
Por uma fração de segundo, os olhos carmesins dela perdem toda a crueldade. O que resta é uma mulher que sobreviveu ao fim de tudo o que conhecia, presa numa gaiola de pedra, encarando a única criatura viva que não se ajoelhou por medo.

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Manter o olhar firme e conduzir o último giro com reverência silenciosa (+Afeto Lility / +Humanidade)"*
**VICTOR VANE**: "Nem todo mundo que sobrevive precisa ficar sozinho na sala vazia, Lility."
Os lábios dela entreabrem, surpresos com a calma das minhas palavras. Ela desvia o olhar devagar para a janela poente.
**MESTRA**: "...Você fala bobagens demais para quem mal aprendeu a caçar, Victor."
Mas a mão dela demora três segundos a mais para soltar a minha.
> - 🔹 Escolha: *"Aproveitar a proximidade para ler os segredos da respiração dela (+Intelecto / +Ressonância)"*
**VICTOR VANE**: "Essa música... não era sobre uma cidade que afundou. Era sobre uma promessa que você fez e não pôde cumprir."
Os olhos dela cintilam com um perigo repentino e fascinado.
**MESTRA**: "Cuidado, meu cachorrinho. Se cavar fundo demais no meu passado, você pode encontrar o túmulo de coisas que não deveriam acordar."
> - 🔹 Escolha: *"Recuar com um sorriso irônico e quebrar o feitiço antes que ela tente morder (+Charme / +Autonomia)"*
**VICTOR VANE**: "Para quem dizia que eu era só um rato de laboratório... até que você não errou muitos passos."
Ela solta uma risada curta, rouca e genuinamente divertida.
**MESTRA**: "Insolente. Um dia desses eu ainda corto esse seu atrevimento com as presas."
O sol finalmente se põe atrás das torres da academia. As sombras longas engolem a sala de música, trazendo de volta o frio habitual da pedra.
Lility dá dois passos para trás, voltando para a penumbra junto ao piano.
**MESTRA**: "A noite começou, Victor. Vá para o seu dormitório antes que Elara mande a ronda te caçar. E pratique os seus passos... você ainda é pesado demais para a minha safra."
Ela vira as costas e volta a folhear as folhas amareladas da partitura. Eu saio para o corredor sentindo o sangue queimar nos pulsos.

---


### DIA 05 — Noite (`evt_d05_noite`)

Dias 5 a 8 — Noite. A neblina que sobe nos portões da academia traz o cheiro de água estagnada das catacumbas. Ao longe, um som gutural ecoa entre os postes: 'Po... po... po...'
**EMÍLIA (Noviça Devota)**: "Você fica atrás de mim, Victor! Se eu disser para correr, você corre sem tentar bancar o herói. Entendido?"
**VICTOR VANE**: "Não. Se não queria um parceiro, não deveria ter me chamado."
**EMÍLIA (Noviça Devota)**: "Eu convidei você porque não quero que morra sozinho nos corredores!"
**VICTOR VANE**: "E eu vim porque não quero depender de alguém decidindo como eu devo sobreviver."
**EMÍLIA (Noviça Devota)**: "Você sabe que essas duas coisas podem ser verdade ao mesmo tempo?! Quando você tenta controlar tudo para não dever nada a ninguém, fala exatamente como o meu pai!"
**HACHISHAKU**: "Po... po... po..."
Após dissiparmos a entidade na neblina, Emília segura meu braço ferido e começa a enfaixar o corte.
**VICTOR VANE**: "Eu consigo cuidar disso sozinho. Você não precisa fazer isso por mim."
**EMÍLIA (Noviça Devota)**: "Eu sei que não preciso."
**VICTOR VANE**: "Então por que está fazendo?"
**EMÍLIA (Noviça Devota)**: "Porque você está ferido, Victor. Nem todo gesto de cuidado é uma fatura que vão te cobrar depois."
Fico em silêncio. Sei lidar com dívidas e ameaças, mas ainda não sei como reagir quando alguém me ajuda sem exigir uma coleira em troca.

---


### DIA 06 — Tarde (`evt_d06_tarde`)

Tarde tensa no campus. O ar vibra com anomalias crescentes. Ao redor da Fonte Gótica, a divisão invisível da escola salta aos olhos como um tabuleiro de xadrez.
De um lado, dezenas de estudantes comuns em seus uniformes pretos conversam baixo, vários deles com pequenos curativos de algodão na dobra do braço após a 'campanha de doação'.
No balcão superior de mármore, os membros do Conselho Estudantil vestem seus uniformes brancos impecáveis. Nenhum deles jamais entra na fila da enfermaria.
**VALÉRIA (Mercadora das Caldeiras)**: "Bonito o contraste, né, bolsista? Preto embaixo, branco em cima."
**VICTOR VANE**: "Os alunos de uniforme preto nem desconfiam para onde vão as bolsas da enfermaria?"
**VALÉRIA (Mercadora das Caldeiras)**: "Eles preferem não saber, Victor. Um ponto extra no histórico escolar e uma dispensa de Educação Física compram muita cegueira voluntária."
**VALÉRIA (Mercadora das Caldeiras)**: "A diferença entre mim e a Presidente Elara é que, quando eu vendo alguma coisa nas caldeiras, o rótulo diz exatamente quanto custa."

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"\"E você não se importa de ver o 'rebanho' sendo drenado assim?\" (+Humanidade)"*
**VALÉRIA (Mercadora das Caldeiras)**: "Eu me importo em manter os meus vivos lá embaixo. Quem tenta salvar o prédio inteiro sozinho costuma virar fundação."
> - 🔹 Escolha: *"\"Pelo menos sabemos onde encontrar suprimento se o subsolo secar.\" (-Humanidade / +Intelecto)"*
**VALÉRIA (Mercadora das Caldeiras)**: "Olha só... O gatinho da Lility já está aprendendo a pensar como quem está no topo da cadeia alimentar."

---


### DIA 07 — Noite (`evt_d07_noite`)

Dia 7 — Noite. Uma semana desde que meu coração mudou de ritmo. Atravesso o corredor vazio do primeiro andar quando esbarro num calouro de uniforme preto que ficou trancado após a monitoria.
Ele derruba os cadernos no chão. Quando estendo a mão para ajudá-lo, sinto o cheiro quente do pulso dele a poucos centímetros do meu rosto.
**MOB_CALOURO_A**: "D-desculpe, veterano! Os monitores trancaram a escada leste e eu não sei como sair..."

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Controlar a respiração e indicar a saída lateral (+Humanidade / +Coragem)"*
**VICTOR VANE**: "Vá pela porta de serviço atrás da biblioteca. E não olhe para trás se ouvir alguém chamando seu nome."
Cravo as unhas na palma da minha própria mão até o calouro desaparecer em segurança.
> - 🔹 Escolha: *"Prendê-lo contra o armário e beber um gole rápido nas sombras (+35%% Sangue / +10%% Exposição / -Humanidade)"*
Antes que ele possa gritar, cubro sua boca e sacio a queimação na garganta, deixando-o tonto encostado nos armários.
**MESTRA**: "Eu senti sua fome daqui de dentro, Victor... e senti quando você deixou a presa ir embora de mãos abanando. Que desperdício adorável."
**MESTRA**: "Cheiro de sangue fresco no colarinho, meu cachorrinho? Cuidado... O primeiro gole roubado nos corredores é sempre o mais difícil de limpar."

---


### DIA 08 — Manha (`evt_d08_manha`)

Dia 8 — Manhã. Na antiga sala do Clube de Ocultismo, Emília analisa amostras de cinza recolhidas nos portões após a luta contra a Mulher Gigante.
**EMÍLIA (Noviça Devota)**: "Victor, olhe para este reagente de prata. Entidades comuns se dissipam no éter, mas as anomalias desta escola estão sendo puxadas de baixo para cima, como se algo sob as catacumbas estivesse respirando."
**VICTOR VANE**: "Se o seu pai souber disso, o que a Ordem vai fazer com a escola?"
**EMÍLIA (Noviça Devota)**: "Expurgo total. Eles não separariam os alunos inocentes de uniforme preto dos vampiros do Conselho. É por isso que preciso encontrar a fonte antes do Dia 17."

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Compartilhar o que ouviu sobre o Cofre do Conselho (+Confiança Emília / +Intelecto)"*
**EMÍLIA (Noviça Devota)**: "Você está arriscando o pescoço para me dar essa pista, Victor. Prometo que não vou deixar o meu pai tocar em quem ainda luta para ser humano."
> - 🔹 Escolha: *"Aconselhá-la a não descer às catacumbas sozinha (+Coragem / +Afeto)"*
**EMÍLIA (Noviça Devota)**: "T-tudo bem... Da próxima vez que eu descer, chamo você primeiro."

---


### DIA 09 — Noite (`evt_d09_noite`)

Noite do Dia 9. A investigação na neblina elevou minha Exposição perante o Grêmio. Quando entro na Sala de Música, encontro Lility apoiada na mesa, com o pulso marcado pelas queimaduras do Grilhão de Sangue e um fio carmesim no canto da boca.
**MESTRA**: "Ora, ora... Você andou fazendo bastante barulho pelos corredores, não é, meu cachorrinho? Cada vez que você trinca a Máscara lá fora, os carcereiros da Elara cobram o pedágio aqui dentro."
**VICTOR VANE**: "Por que não me avisou que o Grilhão feria você diretamente?!"
**MESTRA**: "E você teria obedecido se eu avisasse? Não use a minha dor para alimentar sua culpa moral, Victor. Se for quebrar as regras daquela cadela de uniforme branco, faça valer a pena: traga-me a Partitura Rúnica das catacumbas."

---


### DIA 10 — Noite (`evt_d10_noite`)

No Dia 10, desço ao bar clandestino para rastrear a origem da contaminação. O vapor de absinto altera minha percepção até que uma entidade esmeralda flutua sobre o balcão.
**FADA_VERDE**: "Vocês chamam essa febre de 'fome' porque têm pavor de conhecer a coisa que está faminta debaixo do alicerce."
**VICTOR VANE**: "Você está falando da entidade nas profundezas? Do que está adormecido sob o alicerce?"
**FADA_VERDE**: "Um nome é apenas uma coleira! A noiva de cabelos vermelhos trancou o túmulo no Dilúvio, mas agora quer abrir a porta. Pergunte a ela se quem procura o primeiro predador quer mesmo um trono... ou apenas o fim!"
Logo atrás do bar, encontro uma caixa de bolsas de sangue com o selo raspado: filamentos escuros se movem dentro do líquido quando aproximo a mão. Valéria fecha a tampa no mesmo instante.
**VICTOR VANE**: "A garota que me atacou no Dia 1 comprou deste lote. Isso aqui está vivo, Valéria!"
**VALÉRIA (Mercadora das Caldeiras)**: "Eu sei. Suspani esse lote assim que dois clientes enlouqueceram e meus rapazes ouviram batidas vindas da parede das catacumbas."
**VICTOR VANE**: "E você não disse nada?!"
**VALÉRIA (Mercadora das Caldeiras)**: "Escute bem, Victor: eu vendo o que consigo obter num lugar onde os nobres do Grêmio fingem que os Renegados não existem. Descobri tarde demais que o vazamento lá de baixo contaminou a mercadoria — não confunda isso com inocência."
Coloco um artefato raro recuperado do subsolo sobre a bancada dela.
**VALÉRIA (Mercadora das Caldeiras)**: "Bonito. Valioso. E você não está com cara de quem quer dinheiro. Está tentando me comprar... ou está viciado no poder de me fazer dizer 'sim' quando eu deveria dizer 'não'?"

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Exigir parceria estratégica e os registros da rota subterrânea (+Intelecto / +Afeto Valéria)"*
**VICTOR VANE**: "Quero que pare de me tratar como cliente. Quero os registros de transporte e uma rota de saída para quando a barreira cair."
**VALÉRIA (Mercadora das Caldeiras)**: "Fechado, sócio. Mas lembre-se: eu nunca vendo a minha independência."
> - 🔹 Escolha: *"Pressioná-la a cooperar com a investigação de Emília (+Humanidade)"*
**VICTOR VANE**: "Entregue a rota do lote contaminado para Emília sem expor seus fornecedores. Se aquilo sob o alicerce despertar, não vai sobrar mercado para ninguém."
**VALÉRIA (Mercadora das Caldeiras)**: "Trégua prática com a santinha? Que seja."

---


### DIA 11 — Tarde (`evt_d11_tarde`)

Dia 11 — Tarde. Duas viaturas da polícia metropolitana estão paradas diante dos portões de ferro da academia. O Diretor humano enxuga o suor da testa enquanto Elara observa a cena a poucos passos.
**MOB_POLICIAL_C**: "São quatro estudantes transferidos sem rastro em dez dias, Srta. Presidente. A delegacia central está começando a fazer perguntas."
**ELARA (Presidente do Grêmio)**: "E os relatórios médicos assinados pelo nosso Diretor já foram encaminhados ao comissário, Detetive. Surto de anemia sazonal e transferências voluntárias."
**ELARA (Presidente do Grêmio)**: "Tenho certeza de que a doação generosa da Fundação ao fundo da polícia ajudará a manter a imprensa longe dos nossos portões."
Quando o detetive vai embora em silêncio, Elara vira os olhos carmesim na minha direção.
**ELARA (Presidente do Grêmio)**: "Viu como o mundo lá fora é frágil, Sr. Vane? Humanos de uniforme preto ou de distintivo... todos têm um preço. Certifique-se de que a sua sede não encareça a minha contabilidade."

---


### DIA 12 — Noite (`evt_d12_noite`)

Dia 12 — Noite. Desço pela tubulação de vapor entre as caldeiras e as catacumbas. Por trás de uma grade enferrujada, ouço vozes conhecidas discutindo em tom baixo.
**ELARA (Presidente do Grêmio)**: "Quero o dobro de sedativos alquímicos até a noite do Baile, Valéria. Os lacaios do segundo andar estão ficando agitados com a aproximação do Eclipse."
**VALÉRIA (Mercadora das Caldeiras)**: "O preço subiu, Presidente. Meus rapazes do Fundão não vão descer perto daquela parede que pulsa pelo valor antigo."
**ELARA (Presidente do Grêmio)**: "Você existe neste porão porque eu permito. Entregue a remessa e elimine qualquer curioso que chegue perto da grade do Cofre."
Recuo em silêncio pelas sombras... mas os guardas contratados me avistam na subida das escadas, preparando a emboscada da madrugada!

---


### DIA 13 — Manha (`evt_d13_manha`)

Nos corredores subterrâneos interditados, encosto a mão na parede de pedra antiga e sinto uma pulsação lenta e colossal — o mesmo ritmo abafado que senti no Transe de Sangue. A escola inteira foi erguida sobre o sarcófago de algo proibido e ancestral.
À noite, ao descobrir o acordo silencioso entre o Grêmio e o mercado negro, sou emboscado por capangas das caldeiras a mando de Elara, mas consigo derrotá-los.
Na manhã seguinte, entro no Gabinete da Presidência mancando levemente. Elara serve uma xícara de chá impecável sem levantar os olhos.
**ELARA (Presidente do Grêmio)**: "Você está mancando, Sr. Vane. Que pena. Eu esperava que os meninos das caldeiras fossem mais eficientes."
**VICTOR VANE**: "Você mandou eles me matarem porque descobri que o Grêmio tolera o mercado de Valéria para conter os Renegados."
**ELARA (Presidente do Grêmio)**: "Eu mandei testarem você. Se morresse, um problema a menos. Como sobreviveu... provou que ainda pode ser moldado. A partir de hoje os setores subterrâneos estão bloqueados sob minha responsabilidade."
**VICTOR VANE**: "E se tudo ruir no Eclipse, a senhora também vai assumir a responsabilidade?"
**ELARA (Presidente do Grêmio)**: "...Eu já a assumi há um século, Victor."

---


### DIA 14 — Noite (`evt_d14_noite`)

Dia 14 — Noite. Sobre a escrivaninha do meu quarto, há uma máscara negra enviada para o Baile de Inverno de amanhã. Do lado de fora, a lua já apresenta uma auréola avermelhada.

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Passar a véspera revisando as partituras antigas de Lility (+Afeto Lility / +Ressonância)"*
As notas rúnicas parecem vibrar sob os meus dedos, preparando meu sangue para a valsa na Sala de Música.
> - 🔹 Escolha: *"Limpar e afiar os amuletos de proteção com o guia de Emília (+Afeto Emília / +Humanidade)"*
Guardo o pequeno amuleto de prata no bolso interno do blazer, determinado a encarar Emília de frente amanhã.
> - 🔹 Escolha: *"Conferir o mapa de dutos de fuga enviado por Valéria (+Afeto Valéria / +Intelecto)"*
Memorizo cada tranca subterrânea caso o Baile de Máscaras se transforme num massacre.
> - 🔹 Escolha: *"Polir o broche de inspeção do Grêmio para provocar Elara (+Afeto Elara / +Domínio)"*
Amanhã à noite, a Presidente verá que o lacaio sob o Grilhão aprendeu a jogar o jogo da corte.

---


### DIA 15 — Noite (`evt_d15_noite`)

Noite do Baile de Máscaras. A Deterioração atinge metade de seu ciclo. A elite da academia celebra sob máscaras venezianas para fingir que a barreira não está cedendo.
No terraço iluminado pela lua, Emília me confronta. Sua voz treme enquanto seus dedos seguram a máscara prateada e o cabo da adaga consagrada.
**EMÍLIA (Noviça Devota)**: "O sangue no subsolo... e a forma como seus ferimentos cicatrizaram depois da caçada. Não foi sorte, Victor. Eu vi o que o Grilhão fez no seu peito quando você tentou esconder sua condição."
**VICTOR VANE**: "Eu não pedi para ser transformado, Emília."
**EMÍLIA (Noviça Devota)**: "Eu sei! Mas você olhou para mim todos os dias e escolheu esconder a verdade!"
**VICTOR VANE**: "Eu não sabia se você ainda conseguiria olhar para mim como uma pessoa depois de ouvir!"
**EMÍLIA (Noviça Devota)**: "Então você decidiu por mim! Tirou de mim o direito de escolher, exatamente como fizeram com você!"

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Abrir o coração sem reservas: 'Não vou mais mentir. Minha vida está nas suas mãos.' (+Confiança Emília)"*
**EMÍLIA (Noviça Devota)**: "...Dance comigo por cinco minutos, Victor. Antes que o meu pai chegue à cidade amanhã, preciso lembrar pelo que estou lutando."
> - 🔹 Escolha: *"Manter a distância defensiva: 'Fiz o que precisava para nós dois sobrevivermos.' (-Confiança)"*
**EMÍLIA (Noviça Devota)**: "Se você cruzar o limite e ferir um inocente, Victor... eu mesma terminarei isso."
Mais tarde, na Sala de Música interditada, a valsa abafada do salão ecoa pelo piso de madeira. Lility se aproxima da janela após observar o brasão antigo da escola com desprezo.
**VICTOR VANE**: "Você fala como se já soubesse o que vai acontecer depois do Eclipse, Lility. Mas nunca fala do que quer fazer no dia seguinte."
**MESTRA**: "Tenho uma imaginação extraordinária. Vou escolher um palácio, reconstruir os corredores e proibir esses uniformes horríveis."
**VICTOR VANE**: "Você está brincando."
**MESTRA**: "Naturalmente."
**VICTOR VANE**: "Você não quer um reino. Você quer que alguma coisa termine."
O sorriso de Lility se desfaz por completo. O silêncio na sala pesa como chumbo.
**MESTRA**: "Cuidado, Victor. Eu já aceitei desaparecer quando o sarcófago abrir... Não seja cruel tentando me fazer querer ficar."

---


### DIA 16 — Noite (`evt_d16_noite`)

Dia 16. A aproximação do Eclipse dobra a velocidade da Fome de Sangue. No corredor dos dormitórios, passo por um estudante humano com um corte recente no braço; o som das palavras dele fica abafado pelo pulsar da veia exposta.
**VICTOR VANE**: "(Afaste-se... agora! Eu estou tentando impedir que precisem me parar!)"
**MESTRA**: "Você está tremendo, Victor."
**VICTOR VANE**: "Estou cansado. Não preciso de você."
**MESTRA**: "Não foi isso que eu perguntei."
**VICTOR VANE**: "...Eu não quero precisar de você."
**MESTRA**: "Ah. Isso é muito diferente. Precisar de alguém para continuar de pé não significa que essa pessoa tenha vencido. Beba logo e me diga como vamos entrar no Cofre."

---


### DIA 17 — Tarde (`evt_d17_tarde`)

Dia 17. Lorde Phillip von Karsten, inquisidor da Ordem e pai de Emília, atravessa os portões da academia.
**PHILLIP**: "Afaste-se da minha filha, garoto. Você carrega o fedor da abominação ancestral misturado ao perfume de Emília. A criatura dentro de você não precisa da sua autorização para destruí-la."
**VICTOR VANE**: "E o senhor não precisa saber quem eu sou para decidir me executar. Sei muito bem o que acontece quando alguém decide a vida de outra pessoa e chama isso de proteção."
**PHILLIP**: "Eu vi cidades inteiras desaparecerem porque inquisidores jovens insistiram em compreender o monstro antes de detê-lo. A hesitação mata, Victor Vane. O Ritual do Corte do Vínculo existe no meu grimório, mas jamais o entregarei voluntariamente a você."
**EMÍLIA (Noviça Devota)**: "Pai, você me ensinou que a hesitação mata, mas estou vendo que a sua certeza cega também! Eu mesma copiei as páginas do grimório do Corte do Vínculo para o Victor!"
Sou forçado a cruzar lâminas contra o veterano inquisidor para abrir caminho e arrancar as anotações do ritual!

---


### DIA 18 — Noite (`evt_d18_noite`)

A Ruptura da Máscara. A Lei Marcial foi decretada no campus: os alunos de uniforme preto foram trancados nos dormitórios enquanto Inquisidores da Igreja e Gárgulas do Conselho guerreiam nos corredores!
Uma Gárgula de Elite do Conselho despenca do vitral superior para bloquear meu avanço rumo ao subsolo!
Com o construto de mármore despedaçado no chão, o caminho para o Assalto ao Cofre de amanhã à noite está finalmente aberto.

---


### DIA 19 — Noite (`evt_d19_noite`)

Noite 19. A contagem regressiva para o Eclipse está quase no fim. A Ruína vibra pelas pedras ancestrais do colégio.
Diante de mim está a passagem secreta para as entranhas mais profundas do subsolo: o Cofre de Contenção do Conselho Estudantil.
Lá dentro repousam as duas únicas peças capazes de controlar o despertar de Cain: o Relicário de Sangue Puro e a Chave de Contenção de Grau Zero.
Avanço pelos primeiros degraus da escadaria em espiral. O ar estala com faíscas azuladas: o chão está entalhado com uma malha de glifos rúnicos da Inquisição, projetados para incinerar qualquer vampiro que pise em falso.

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"[[CONHECIMENTO OCULTO]] Decifrar a frequência dos glifos e desarmar o circuito arcano"*
Com as pontas dos dedos e a mente fria, analiso a geometria dos nós arcanos. Reconheço o fluxo de energia e quebro o contato do eletrodo central com a ponta de uma lâmina!
As faíscas silenciam-se. O caminho está livre sem disparar nenhum alarme!
Hesito ao tocar no glifo errado! Uma descarga de eletricidade rúnica percorre meu corpo, queimando as terminações nervosas das minhas mãos (-20 HP)!
Rangendo os dentes, forço o passo adiante até a descarga se extinguir na pedra fria.
Lembro-me da oração de proteção e da pureza que corre nas minhas veias desde a troca de sangue com Emília.
Um halo tênue de luz prateada envolve meus passos. Ao pisar nas lajes entalhadas, as runas inquisitoriais reconhecem a assinatura sagrada e se dissipam como névoa diante do sol!
> - 🔹 Escolha: *"[[RESISTÊNCIA BRUTA]] Avançar em disparada suportando a queimação dos selos"*
Sem tempo para sutilezas, disparo escada abaixo em velocidade vampírica! Os arcos voltaicos queimam minhas roupas e cortam minha pele, mas minha determinação me arrasta até o patamar inferior (-20 HP).
Chego à antecâmara fortificada. Diante da porta blindada de titânio do Cofre, três guardas de elite do Conselho Estudantil em uniformes brancos impecáveis vigiam a entrada, espadas e rapieiras desembainhadas.

> **[DECISÃO DO JOGADOR]:**
Localizo a escotilha de manutenção na penumbra do teto. Insiro a Chave-Mestra de latão que Nora me confiou na cripta.
A trava estala suavemente. Rastejo pelos dutos estreitos de ventilação, passando exatamente sobre os capacetes dos guardas de elite sem emitir um único ruído.
Desço do outro lado da barricada e giro a manivela de emergência, travando a porta pesada por dentro e deixando a guarda isolada do lado de fora!
Conforme as instruções que aprendi com Valéria no submundo das Caldeiras, acoplo o bypass na válvula de purga de gás.
Abro o registro com força: uma nuvem espessa de vapor químico e anestésico preenche a câmara dos guardas!
Tossindo e cambaleando, os executores do Grêmio perdem os sentidos antes de conseguirem soar o alarme.
> - 🔹 Escolha: *"[[COMBATE TÁTICO]] Enfrentar o Capitão da Guarda de Elite do Grêmio"*
Salto da escuridão com as presas à mostra! Os guardas entram em formação e o Capitão da Guarda ergue sua espada prateada para conter minha invasão!
Com um golpe decisivo, desarmo o líder da guarda e arrombo os trincos da antecâmara!
As portas do cofre interno se abrem com um gemido de dobradiças ancestrais. A sala é iluminada por chamas verdes que tremulam em candelabros de bronze.
Sobre o altar de pedra no fundo do recinto, o Relicário de Sangue Puro pulsa com um brilho escarlate hipnótico. Ao lado dele, a Chave de Contenção de Cain brilha em ouro fosco.
Mas entre mim e o relicário, uma silhueta solitária me espera com postura régia.
**ELARA (Presidente do Grêmio)**: "Você foi longe demais, Victor Vane."
**VICTOR VANE**: "O baile de máscaras acabou, Elara. Quantas vidas mais você vai jogar nesta fornalha?"
**ELARA (Presidente do Grêmio)**: "Vidas? Você ousa me dar lições de moral? Olhe para este colégio! Olhe para a cidade lá fora! Há mais de cem anos o Grêmio equilibra a balança entre monstros insaciáveis e uma humanidade frágil que seria varrida do mapa em três noites se Cain despertasse!"
**VICTOR VANE**: "Equilibra a balança sacrificando os alunos de uniforme preto na enfermaria? Usando cobaias como a Nora em tubos de vidro no subsolo enquanto o Conselho veste branco e toma vinho consagrado?"
**ELARA (Presidente do Grêmio)**: "Sacrifícios necessários para manter a ordem! Alguém precisa carregar a culpa pelas engrenagens que giram nas sombras! Mas você... você é apenas o fantoche de Lility. Ela quer o apocalipse porque já viveu demais; você quer bancar o herói porque não sabe o que é governar!"
**ELARA (Presidente do Grêmio)**: "Eu prefiro ver seu corpo empalado nas portas deste cofre do que permitir que você entregue o sangue primordial para quem quer ver o mundo queimar!"
**ELARA (Presidente do Grêmio)**: "Você... você realmente acredita que derrotar-me mudará o que está acordando lá embaixo?"
**VICTOR VANE**: "Proteger uma instituição pelo medo não é o mesmo que proteger as pessoas que vivem nela, Elara."

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Forçar o Transe de Sangue Invertido e subjugar Elara (+Domínio / -Humanidade)"*
**VICTOR VANE**: "Você passou todo esse tempo me lembrando de quem segurava a coleira, Presidente. Agora prove do sangue que corre nas minhas veias."
**ELARA (Presidente do Grêmio)**: "...Você é pior do que Lility. Ela só queria morrer... e você quer me fazer querer viver sob o seu comando."
> - 🔹 Escolha: *"Estender a mão e exigir uma trégua política pelo bem da escola (+Humanidade)"*
**VICTOR VANE**: "Levante-se, Presidente. Não vim tomar o seu trono; vim impedir que Cain devore a escola que você jurou proteger."
**ELARA (Presidente do Grêmio)**: "...Que não reste dúvida, Victor Vane: se falharmos amanhã, cairemos juntos."
**VICTOR VANE**: "Eu estive na cripta selada, Elara. Eu vi o que vocês fizeram com a Nora. Alfinete 31. Uma aluna humana jogada numa cuba ácida como peça de reposição."
**ELARA (Presidente do Grêmio)**: "...Nora... Você a encontrou...?"
**VICTOR VANE**: "Eu encontrei. E não a tratei como um número descartável, como você fez. Se o seu Grêmio precisa devorar as próprias crianças para sobreviver, ele não merece estar de pé. Mas se você se levantar agora e lutar ao meu lado pelo amanhã, podemos construir algo melhor do que essa farsa."
**ELARA (Presidente do Grêmio)**: "......"
Pela primeira vez em um século, vejo os olhos da Presidente marejados pela vergonha. Ela segura minha mão estendida e se levanta lentamente.
**ELARA (Presidente do Grêmio)**: "Pela primeira vez... alguém me lembrou por que fundamos este refúgio. Quando o sol nascer depois de Cain... o Conselho prestará contas."

---


### DIA 20 — Noite (`evt_d20_noite`)

Véspera do Eclipse. A Deterioração atinge o estágio crítico. Pela primeira vez, as vozes da escola colidem na mesma sala antes da descida final às catacumbas.
**ELARA (Presidente do Grêmio)**: "O ritual original foi construído para manter Cain adormecido, não para matá-lo."
**VALÉRIA (Mercadora das Caldeiras)**: "Então o grande plano da nobreza é entrar na sala de um deus faminto que não pode morrer e pedir educadamente que ele volte a dormir?"
**VICTOR VANE**: "Vocês continuam falando como se estivéssemos discutindo quem vai vencer. Estamos discutindo o que cada um aqui está disposto a destruir para não admitir que pode perder."
**MESTRA**: "...Amanhã à noite, na câmara do sarcófago, veremos qual é a sua resposta final, Victor."

---


### DIA 21 — Noite (`evt_d21_noite`)

O Eclipse Total. A Deterioração atinge cem por cento. No fundo das catacumbas, Lility crava o Relicário de Sangue Puro no sarcófago ancestral.
As correntes de ouro se partem com um estrondo sísmico! O teto da academia rui sob a Esfera de Sangue que se abre no céu noturno, e Cain desperta.
**VICTOR VANE**: "Você vai drenar a metrópole inteira! E quando não houver mais sangue ao alcance?!"
**CAIN**: "A cidade inteira é apenas o que resta ao alcance do despertar. Quando secar, a fome terá aprendido o tamanho do mundo."
**VICTOR VANE**: "Você não quer governar nada..."
**CAIN**: "Governar é o nome vaidoso que os famintos dão ao intervalo entre duas refeições."
Arranco Lility do vórtice de drenagem de Cain no último instante antes que sua imortalidade seja consumida até o fim!
**MESTRA**: "Por que você me puxou de volta, seu tolo teimoso?! Só a fome dele podia encerrar a minha existência!"
**VICTOR VANE**: "No primeiro dia você me salvou quando eu estava morrendo no corredor — não por utilidade, mas porque escolheu! E você não precisa fingir que quer um reino se tudo o que desejava era que alguém terminasse a sua história!"
**MESTRA**: "Se você me pedir para parar agora... diga-me a verdade, Victor: você quer me salvar porque se importa comigo... ou porque não suporta a ideia de ficar sozinho de novo?"

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"1. (FINAL A — CONSORTE IMORTAL) 'Não quero que atravesse a eternidade sozinha. Vamos drenar Cain e reinar juntos!'"*
**VICTOR VANE**: "Segure o Relicário comigo, Lility! Se a eternidade era vazia porque você carregava essa maldição sozinha, nós vamos usurpar o sangue de Cain e dividir o peso dessa coroa!"
**MESTRA**: "...Você nunca aprendeu a seguir uma ordem simples, meu doce cachorrinho. Então que o mundo antigo queime sob os nossos pés!"
Cravamos nossas mãos simultaneamente no peito do Progenitor! O vórtice de sangue milenar explode em uma coluna escarlate que rasga os céus da academia!
A vitae divina de Cain queima através de nós, purificando nossa fraqueza e coroando nossas almas com a autoridade pré-diluviana absoluta.
As pedras do teto desmoronam, revelando a metrópole sob o eclipse permanente. As cortes vampíricas e os inquisidores ajoelham-se em pânico e reverência diante da nova dinastia.
Lility apoia o queixo em meu ombro, o olhar afiado como navalha, enquanto nossas sombras se fundem no trono do mundo noturno.
🏆 FINAL A DESBLOQUEADO: CONSORTE IMORTAL (A Nova Dinastia Carmesim).
**VICTOR VANE**: "Eu não vou prender você aqui por egoísmo, Lility. Você me devolveu a vida naquela primeira noite no corredor; agora eu uso o Ritual do Corte para conceder o descanso sagrado que você buscou por milênios."
**MESTRA**: "Finalmente... uma resposta que não me deixa entediada. Obrigada por ter sido a minha última testemunha, Victor... viva por nós dois."
Ergo a lâmina rúnica e quebro o selo ancestral do Relicário. Uma luz dourada e suave emana do corpo de Lility.
Sem dor, sem fogo — apenas um alívio imenso. Seu corpo imortal desfaz-se em cinzas de luz que fecham para sempre a fenda dimensional de Cain.
Quando a poeira baixa, os primeiros raios do sol da manhã filtram-se pelas arcadas em ruínas da capela.
Emília corre em minha direção com lágrimas nos olhos, segurando com força minhas mãos geladas. Aqueço-me ao toque dela.
De repente, sinto um estalo profundo sob o esterno: TUM... TUM... TUM... Meu coração volta a bater, compassado e quente. As presas recuam. O peso da maldição se foi.
**EMÍLIA (Noviça Devota)**: "Você conseguiu, Victor... Você está aqui. Você está vivo."
**VICTOR VANE**: "Nós estamos vivos, Emília."
🏆 FINAL B DESBLOQUEADO: QUASE HUMANO (O Peso da Liberdade).
No estertor final de Cain, um espinho calcificado da criatura é projetado pelo ar em rota de colisão contra o meu peito!
Emília salta na minha frente com seu crucifixo erguido — a lâmina de osso perfura seu peito de lado a lado!
**VICTOR VANE**: "EMÍLIA! NÃO!"
Seguro seu corpo trêmulo nos meus braços enquanto o sangue humano jorra sobre o piso sagrado. Os olhos dela perdem o foco; seus lábios balbuciam uma prece agonizante.
**EMÍLIA (Noviça Devota)**: "Victor... está frio... Me deixe ir... por favor... para a luz..."
O pânico cego me enlouquece. Não posso permitir. Não vou deixar mais ninguém morrer por mim nesta escola maldita!
Mordo meu próprio pulso até rasgar o tendão e pressiono a ferida sangrenta contra a boca de Emília, forçando minha vitae profana por sua garganta!
O corpo de Emília convulsiona violentamente! A pureza que ela protegeu a vida inteira é corrompida pelo abraço vampírico. Quando ela reabre os olhos, as íris estão escarlates como brasas vivas.
Duas presas afiadas rasgam seus lábios trêmulos; lágrimas de sangue espesso escorrem por suas bochechas enquanto ela fita as próprias mãos com horror absoluto.
**EMÍLIA (Noviça Devota)**: "O que... o que você fez comigo, Victor...?! Eu sou... um demônio... Por que você roubou o meu céu...?!"
Com as mãos ainda tintas do sangue dela, viro-me para o Relicário onde Lility aguardava o fim!
**VICTOR VANE**: "No primeiro dia você teve pena de mim porque queria ver alguém lutar pela vida, Lility?! Agora eu tomo a sua maldição milenar para mim... e condeno você a viver!"
Inverto os glifos de corte no Relicário! Em um relâmpago ensurdecedor, o sarcófago tranca Cain para sempre, arrancando o dom da imortalidade do peito de Lility e transferindo toda a carga primordial para as minhas veias!
Pela primeira vez em três mil anos, Lility perde o equilíbrio e cai de joelhos no chão úmido da cripta. O rubor mortal sobe às suas maçãs do rosto; suas presas se recolhem e seu peito sobe e desce em arquejos aflitos de ar.
**MESTRA**: "O que... o que você fez comigo, monstro?! Minhas mãos... estão tremendo de frio... Meu pulso está acelerado... Eu sinto fome... sinto dor... O que sobrou de mim?!"
**VICTOR VANE**: "Todos sobreviveram, Lility... e todos nós perdemos exatamente o que desejávamos. Emília viverá na noite me odiando pela eternidade; e você viverá como uma mortal frágil sob a minha guarda, gota por gota."
Fico de pé no centro das ruínas sob a chuva escura. Um rei que salvou todos que amava ao preço de destruir suas almas.
🏆 FINAL OCULTO C DESBLOQUEADO: A CONFIGURAÇÃO DO LAMENTO (Todos Sobrevivem, Todos Perdem).
**VALÉRIA (Mercadora das Caldeiras)**: "O túnel de drenagem das caldeiras está aberto, bolsista! A carga já está no furgão e o teto vai virar poeira em dois minutos!"
**VICTOR VANE**: "Você realmente consegue virar as costas para a escola inteira e nunca mais olhar para trás, Valéria?"
**VALÉRIA (Mercadora das Caldeiras)**: "Não confunda sentimentalismo com lucro, Victor! Eu passei anos montando essa rota de fuga para quando os nobres fizessem merda. O Grêmio ruiu, Cain foi selado nos escombros, e nós temos um estoque de vitae purificada e tecnologia arcana que vale uma fortuna lá fora!"
**VICTOR VANE**: "E qual é o nosso primeiro destino, sócia?"
**VALÉRIA (Mercadora das Caldeiras)**: "Bem longe daqui. Além da jurisdição de qualquer inquisidor ou conselho. Onde nós dois é que mandamos na tabela de preços."
Aceleramos pela galeria subterrânea enquanto os alicerces da velha academia desabam em estrondo atrás de nós. Cruzamos a divisa da metrópole antes dos primeiros clarões do dia, donos do próprio destino.
🏆 FINAL D DESBLOQUEADO: A ÚLTIMA TRANSAÇÃO (Sobreviventes do Submundo).
Diante da fenda de Cain que racha o tecido da realidade, recuso o caminho fácil da morte ou da dominação.
**VICTOR VANE**: "Chega! Nenhuma de vocês vai se sacrificar hoje! Nem Lility como oferenda milenar, nem Emília como mártir cega, nem Valéria como fugitiva nas sombras, e nem Elara como carrasca dos próprios alunos!"
**MESTRA**: "Victor... do que você está falando?! O selo primordial exige um tributo de sangue imenso para conter Cain!"
**ELARA (Presidente do Grêmio)**: "Ele tem razão, Lility. Nós passamos um século nos digladiando em castas e segredos porque tínhamos medo de admitir que nenhuma facção conseguiria governar este fardo sozinha."
**VALÉRIA (Mercadora das Caldeiras)**: "Se é sobre redistribuir carga e pressão sem estourar a caldeira... vocês estão olhando para a especialista certa."
**EMÍLIA (Noviça Devota)**: "E se a pureza divina pode redimir em vez de apenas queimar... a bênção dos von Karsten estará neste círculo!"
Colocamo-nos ao redor do Relicário de Sangue Puro em uma formação estelar de cinco pontas.
Lility conjura as runas pré-diluvianas de sangue ancestral, tecendo correntes vivas que paralisam o coração cósmico de Cain.
Emília estende seu rosário consagrado, canalizando a luz sacra para purificar a corrupção do despertar sem ferir os envolvidos.
Valéria acopla os condutores arcanos das caldeiras, drenando o excesso catastrófico de energia para abastecer a infraestrutura subterrânea da cidade.
E Elara crava o cetro do Conselho Estudantil na laje mestra, assinando com sua vitae o Decreto de Dissolução das Castas e a anistia universal dos alunos de uniforme preto.
A fenda de Cain se fecha harmoniosamente! O abismo se sela não por um massacre, mas pelo equilíbrio absoluto entre Poder Ancestral, Fé Sacra, Ciência do Submundo e Ordem Política.
Meses depois. O grande gabinete da academia está banhado pela luz solar e tochas rúnicas. Não há mais uniformes pretos e brancos separados pela vergonha; não há mais cobaias em cápsulas de vidro.
As doações de sangue agora são feitas sob contrato e respeito mútuo. À mesa central da diretoria, o Conselho das Quatro reúne-se ao meu lado.
**VICTOR VANE**: "Uma nova aliança. Uma nova noite."
**MESTRA**: "Quem diria que o garoto quase morto no corredor leste se tornaria o único homem capaz de manter quatro rainhas no mesmo reino..."
**ELARA (Presidente do Grêmio)**: "Não se acostume com os elogios, Victor. A ata da reunião de hoje tem trinta páginas de reformas para você assinar."
**VALÉRIA (Mercadora das Caldeiras)**: "E a minha margem de lucro nos filtros continua intocada, sócio."
**EMÍLIA (Noviça Devota)**: "E a paz dos estudantes finalmente está protegida pela luz e pela verdade."
Olho para cada uma delas, sabendo que cada escolha, cada gota de sangue e cada gesto de empatia valeram a pena.
🏆 FINAL SECRETO E DESBLOQUEADO: A HARMONIA PROIBIDA (O Coven das Quatro Soberanas).

---

## PARTE III: EVENTOS DE CLÍMAX & ANOMALIAS SOBRENATURAIS


### Evento Especial: `evento_emilia_caderno_doacoes_dia2`

No mural antes da biblioteca, um cartaz: 'Campanha Semestral de Saúde Comunitária. Dispensa de uma aula por doação. Créditos extras para bolsistas.'
Dois alunos conversam diante dele, rindo. Um deles diz que ficou tonto na última coleta, mas ganhou a tarde livre. O outro pergunta para onde vai o sangue. O primeiro dá de ombros, ainda sorrindo.
Ninguém aqui parece ter medo da campanha. Só de quem não participa.
**EMÍLIA (Noviça Devota)**: "Senta. Não é um pedido, é um alerta."
Ela abre o caderno sobre a mesa. Três colunas à mão: data, nome, créditos. Páginas e páginas, frente e verso, numa letra miúda que não deixa respirar.
**EMÍLIA (Noviça Devota)**: "Doze alunos com mais de quarenta créditos de doação nos últimos dois semestres. Nenhum deles está matriculado hoje."
**VICTOR VANE**: "Transferidos?"
**EMÍLIA (Noviça Devota)**: "A lista de 'transferências voluntárias' tem exatamente os mesmos nomes da lista de doadores. Eu não sei para onde vão. Só sei que não é para outra escola."
**EMÍLIA (Noviça Devota)**: "Esta escola trata os alunos comuns como um rebanho seguro, Victor. Fazem a gente pagar com uma coisa que acha que está dando."
O papel rubricado hoje cedo pesa mais do que devia dentro do bolso.
**VICTOR VANE**: "Eu assinei o termo hoje."
**EMÍLIA (Noviça Devota)**: "Então você está na lista. A primeira coleta dos novos bolsistas é no dia seis, no Pátio da Fonte."
**EMÍLIA (Noviça Devota)**: "Eu posso tentar mudar a sua data. Não posso prometer."
**VICTOR VANE**: "Eu li a página dois. 'Fundação mantenedora.' Sem nome, sem endereço."
**EMÍLIA (Noviça Devota)**: "Você leu a página dois?! Em três anos, só eu li."
Pela primeira vez desde que a conheci, ela sorri sem tentar disfarçar. Dura dois segundos.
**EMÍLIA (Noviça Devota)**: "A coleta dos novos é no dia seis, no Pátio da Fonte. Já que você leu, vai gostar de ver de perto."
**VICTOR VANE**: "Eu recusei assinar."
**EMÍLIA (Noviça Devota)**: "Ainda bem. Eles vão insistir. A recusa fica no registro, e eu odeio que fique, mas fica."
**VICTOR VANE**: "Por que você anota tudo isso?"
**EMÍLIA (Noviça Devota)**: "Meu pai diz que a memória é a primeira coisa que o medo apaga. Então eu escrevo. Se eu esquecer, o papel lembra por mim."
**VICTOR VANE**: "E o seu pai acredita no que você escreve?"
**EMÍLIA (Noviça Devota)**: "Meu pai acredita em muitas coisas. Raramente em perguntas."
**EMÍLIA (Noviça Devota)**: "Agora a minha. A Júlia do bloco norte disse que você chegou ontem com o colarinho encharcado. Hoje, o seu pescoço não tem uma marca."
**EMÍLIA (Noviça Devota)**: "O que aconteceu, Victor?"

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"“Caí na escada. O sangue era de um nariz.” (+Dúvida Emília)"*
**EMÍLIA (Noviça Devota)**: "Um nariz sangra de baixo para cima. Um colarinho encharca de cima para baixo."
**EMÍLIA (Noviça Devota)**: "Tudo bem. Não é uma acusação. Só mais uma linha no caderno."
> - 🔹 Escolha: *"“Fui atacado. Alguém me ajudou. Não posso dizer quem.” (+Afeto Emília / +Dúvida)"*
**EMÍLIA (Noviça Devota)**: "Obrigada por não mentir. Dizer 'não posso' é mais honesto do que a maioria."
**EMÍLIA (Noviça Devota)**: "Mas quem ajuda de graça aqui costuma cobrar caro."
Ela acabou de descrever, sem saber, o meu dia inteiro.
> - 🔹 Escolha: *"“Quem te disse que eu estava sangrando?” (+Intelecto / +Dúvida)"*
**EMÍLIA (Noviça Devota)**: "A Júlia. A Júlia fala com a Bete, a Bete fala com o refeitório, e o refeitório sabe de tudo. Os boatos são a única rede que a escola não consegue vigiar."
Ela me entrega o jeito de ler esta escola numa frase só. Guardo o dado, sem agradecer. Agradecer é dever.
Emília hesita um instante, tocando o pequeno crucifixo sob o colarinho antes de responder à pergunta que eu sequer fiz.
**EMÍLIA (Noviça Devota)**: "O que for necessário para que ninguém inocente se machuque. É só isso que eu quero."
A resposta me tranquiliza e me gela ao mesmo tempo. Para ela, proteger inocentes pode significar exterminar exatamente o que eu me tornei.
Meus olhos descem para o rodapé da terceira página. Três nomes de bolsistas estão riscados com caneta vermelha: Danilo Ramos, Camila Neves, Lucas Prado.
**VICTOR VANE**: "Esses três últimos da lista... Todos eles tinham aulas e dormitórios na ala leste do segundo andar?"
**EMÍLIA (Noviça Devota)**: "Sim. Por que você reparou nisso?"
**VICTOR VANE**: "No meu primeiro dia aqui, passei três vezes diante da pintura a óleo do Fundador. Você mesma me avisou que os quadros desta escola sempre foram meio estranhos e que os olhos dele pareciam me seguir."
Caminhamos até o parapeito do mezanino, onde a fileira de molduras históricas vigia o corredor em silêncio sepulcral.
**VICTOR VANE**: "Ontem, ao passar por lá no entardecer, notei que o fundo da tela 'O Banquete de 1889' havia mudado. Havia sombras novas debaixo dos candelabros pintados... três figuras encolhidas usando o uniforme preto de bolsista."
**EMÍLIA (Noviça Devota)**: "Meu Deus... O verniz de sacrifício."
**EMÍLIA (Noviça Devota)**: "Os arquivos da minha família mencionam telas tratadas com cinza ritualística e óleo de linhaça impregnado de sangue antigo. O Barão Cipriano era obcecado por capturar o tempo antes que a morte o alcançasse."
**EMÍLIA (Noviça Devota)**: "Se aquela pintura está sugando os alunos que se aproximam à noite... Victor, se você andar por aquele corredor durante o toque de recolher, mantenha distância da moldura. Quem aceita qualquer coisa do mundo pintado tem a carne e a alma absorvidas pela tela."
Meus olhos passam pelos nomes riscados no caderno, mas a mente ainda está turva pela adaptação e pela sede. Há um padrão nos desaparecimentos, mas preciso de mais acuidade mental para conectá-lo ao campus. [Requer Intelecto 2+ para deduzir o mistério dos quadros].

---


### Evento Especial: `evento_conhecer_valeria_caldeiras`

Desço pelas escadas de serviço até o calor abafado das caldeiras, território da Turma do Fundão. O ar vibra com o ronco das tubulações. O vapor corre nos canos como sangue em artérias metálicas.
**VALÉRIA (Mercadora das Caldeiras)**: "Fecha a porta. O vapor custa caro."
Ela está sentada num caixote de madeira, separando moedas por peso com a ponta do indicador sem sequer olhar para elas.
**VALÉRIA (Mercadora das Caldeiras)**: "Você é o novo do corredor leste. O que sobreviveu à Nora."
**VICTOR VANE**: "Como você sabe disso?"
**VALÉRIA (Mercadora das Caldeiras)**: "Tudo o que cai nesta escola escorre para cá, garoto. Sangue, fofoca, dívidas e mercadoria que o Grêmio finge que não existe."
**VALÉRIA (Mercadora das Caldeiras)**: "Eu me chamo Valéria. Mas pode me chamar de quem resolve os seus problemas... se tiver como pagar."
**VALÉRIA (Mercadora das Caldeiras)**: "Eu tenho bolsas filtradas puras, gazes, chaves de armário e informações sobre quem manda de verdade neste inferno. Mas não faço fiado para recém-chegado."
**VICTOR VANE**: "Eu não vim pedir esmola."
**VALÉRIA (Mercadora das Caldeiras)**: "Melhor ainda. Negociante com espinha dorsal é raro por aqui."

---


### Evento Especial: `evento_primeiro_transe_lility`

A bolsa filtrada que peguei na enfermaria tinha gosto de plástico velho e cobre estragado. Meu estômago a rejeitou após dois goles, como um veneno morno que se recusa a descer.
Minhas mãos tremem incontrolavelmente. O pulsar das veias nos pescoços dos alunos ao meu redor e a queimação ácida na garganta estão me empurrando para o abismo.
A fome não é uma vontade. É uma ordem biológica, violenta e cega.
Empurro a porta carcomida da sala de música na ala interditada. O Grilhão de Sangue no meu peito arde suavemente, reconhecendo a presença de quem o selou.
Sentada na borda do piano de cauda empoeirado, sob a luz que vaza pelos vitrais quebrados, Lility me observa em silêncio. Seus olhos carmesins analisam minha postura trêmula e o pavor estampado no meu rosto.
**MESTRA**: "Olhe só para você... Parado na soleira como um filhote resgatado de uma tempestade."
**MESTRA**: "Eu tirei você das garras da morte ontem à noite, mas parece que esqueci de te ensinar como continuar respirando neste mundo."
Ela desce do piano devagar, o tecido do vestido gótico farfalhando no silêncio pesado da sala. Por um breve instante, a expressão severa dela se desfaz em uma melancolia antiga e cansada.
**MESTRA**: "A ralé de uniforme branco bebe sangue filtrado porque tem pavor da própria natureza. Eles acham que se comportando como humanos bem-nascidos, o céu vai esquecer o que eles são."
**MESTRA**: "Uma mente vazia com sede de sangue é uma sentença de morte, Victor. Se eu deixar você vagando pelos corredores sem direção, os cães da Elara vão farejar o seu desespero e te despedaçar antes do fim da semana."
**VICTOR VANE**: "Por que você me deu o seu sangue ontem? Você não parece do tipo que faz caridade por ninguém."
A pergunta corta o ar. Lility para a poucos centímetros de mim, erguendo o rosto pálido.
**MESTRA**: "Você estava estirado na pedra fria, com a traqueia aberta, cravando as unhas no chão e se recusando a apagar... Quando qualquer mortal comum imploraria a um deus surdo ou se entregaria às lágrimas."
**MESTRA**: "Fazia muito tempo que eu não via alguém lutar com tanta fúria por uma vida tão breve e insignificante. Eu senti pena. E talvez... um pouco de inveja desse fogo que os mortais carregam antes de virarem pó."
Ela ergue o braço direito e encara o próprio pulso pálido. Há uma hesitação sutil e inédita em seus dedos — o peso de quem está prestes a quebrar um jejum sensorial e afetivo de eras.
**MESTRA**: "Aqui fora, no nosso mundo, ninguém divide o sangue sem que haja uma faca apontada nas costas ou um estratagema político."
**MESTRA**: "Faz muito tempo que eu não compartilho um vínculo verdadeiro... que não deixo alguém entrar no Transe comigo."
**MESTRA**: "Pense nisso como quiser. Empréstimo, pagamento ou favor. Não tenha medo. Beba. Deixe que o meu sangue acalme o caos dentro de você."
A pele dela é fria como mármore sob o luar, mas a proximidade é febril e hipnótica. Ela inclina a cabeça, exibindo o pulso pálido onde uma gota rubra reluz como rubi líquido.
Com as mãos trêmulas, seguro o braço dela. Meus lábios tocam a pele macia... e as presas afundam.
O sangue desce como brasa líquida pela minha garganta. O tremor convulsivo nos meus braços cessa no mesmo segundo.
Não há náusea. Não há o gosto de plástico ou ferrugem podre das bolsas da enfermaria. É poder concentrado, ancestral, queimando direto nas fibras dos meus músculos.
A sala de música desaparece. O mundo exterior deixa de existir. Duas mentes colidem através da ponte rubra.
Eu sinto a respiração dela na minha nuca, mas não é o ar dos seus pulmões — é o peso avassalador de séculos de solidão, um vazio tão fundo que faz o meu peito doer.
Um vislumbre arranca minha alma da escuridão: uma vastidão de águas revoltas sob um céu de breu e cinzas. Uma torre colossal resistindo ao afogamento do mundo... e a silhueta da mulher de cabelos de fogo assistindo à extinção dos seus iguais sem derramar uma única lágrima humana.
E então, no refluxo do pacto, sinto que a consciência dela invade as minhas próprias gavetas trancadas:
A mente dela escava o que eu passei meses tentando soterrar:
O estacionamento na garoa. O sedã importado. O professor prensando a garota contra a lataria fria, as mãos forçando o casaco dela.
As algemas mordendo meus pulsos sem que ninguém me fizesse uma única pergunta.
O gabinete do delegado. O aperto de mãos do diretor da faculdade — o tio sorridente do canalha — comprando a cumplicidade da lei com um aceno de cabeça.
O termo de rendição empurrado sobre a mesa: confissão de culpa e expulsão sumária, sob ameaça de quatro anos de cadeia.
E a ferida que nunca fechou: a garota sentada no canto, com os olhos vermelhos e a cabeça baixa, assinando o depoimento forjado que me chamava de monstro. Me jogando aos cães para salvar a própria bolsa.
A madrugada seguinte na plataforma vazia. A mala gasta. O banimento para a capital.
Lility bebeu cada gota daquela humilhação. Ela viu onde cada uma das minhas quatro regras foi forjada.
O transe se rompe devagar. Nossas respirações estão curtas e entrecortadas. Lility me encara com os olhos arregalados, a mão ainda pousada na minha nuca.
**MESTRA**: "Um estacionamento cinzento... O cheiro de chuva e ferro... E uma garota covarde virando o rosto enquanto você era algemado."
**VICTOR VANE**: "...O quê?! Como você... Saia da minha cabeça!"
**MESTRA**: "O diretor da sua antiga faculdade sorriu antes de enfiar a faca no seu peito, não foi? Ele sorriu antes de exigir a sua rendição."
**MESTRA**: "E a tola que você tentou salvar te vendeu por um semestre de mensalidade paga. Que espetáculo patético da alma humana."
A segunda regra na minha carta: nunca confiar em quem sorri antes de pedir. E o motivo da minha primeira: nunca dever nada a ninguém. Eu nunca contei isso para uma única alma viva. E ela bebeu cada detalhe direto da minha essência.
**MESTRA**: "Mas o mais fascinante de tudo não foi o seu pequeno trauma de herói traído, cachorrinho..."
Ela passa a ponta da língua pelo canto dos lábios, onde uma gota rubra reluz com uma viscosidade e um brilho quase etéreos.
**MESTRA**: "É o gosto do seu sangue. Rh Nulo... Sangue Dourado imaculado. A mesma seiva pura dos sacerdotes antediluvianos antes que os céus se rompessem."
**MESTRA**: "Agora eu entendo por que você sobreviveu à mordida daquela aberração sem se transformar em uma massa de carne podre. A sua carcaça foi feita sob medida para suportar o que está trancado nas profundezas desta academia."
**VICTOR VANE**: "E o que foi aquilo que eu vi no seu sangue?! Águas negras, uma torre desabando... uma solidão que parecia ter séculos! Quantos anos você tem afinal?!"
Ela recolhe o pulso devagar, limpando a gota escarlate que restou nos lábios com o polegar. Um sorriso de puro escárnio e superioridade se desenha em seu rosto, fechando qualquer fresta de vulnerabilidade.
**MESTRA**: "O sangue é volátil, tolo. Quando duas naturezas se cruzam, a mente mortal preenche os vazios com delírios poéticos."
**MESTRA**: "E perguntar a idade de uma dama é uma grosseria imperdoável, cachorrinho. Especialmente de quem acabou de te dar comida e salvar o seu pescoço."
**MESTRA**: "Tudo o que você precisa saber é que o meu sangue te mantém de pé. O resto não é da sua conta."
**MESTRA**: "Agora que a sua cabeça parou de girar e a sua sede foi saciada sem alertar os carrascos de Elara, escute bem o seu objetivo, Victor."
**MESTRA**: "Antes de você aparecer, aquela puritana arrogante da Presidente me flagrou nas catacumbas e trancou dois artefatos que me pertencem por direito dentro do Cofre de Segurança Máxima do Grêmio."
**MESTRA**: "Com este Grilhão de Sangue nos meus pulsos, meus movimentos estão vigiados dia e noite. Mas você... você é livre para circular."
**VICTOR VANE**: "O que você quer que eu faça?"
**MESTRA**: "Você será os meus olhos e as minhas mãos fora desta prisão."
**MESTRA**: "Primeiro: investigue os porões das caldeiras. Há uma contrabandista chamada Valéria que lidera a 'Turma do Fundão' no mercado negro; eu tinha uma encomenda rúnica vindo por ela antes de ser confinada."
**MESTRA**: "Segundo: observe os passos da garota do Clube de Ocultismo, Emília. Ela anda farejando pergaminhos sobre a história antiga da escola."
**MESTRA**: "Terceiro: descubra as rotinas de Elara e o caminho até o cofre. Conforme você se alimentar e treinar nas Zonas de Perigo, o sangue que te dei despertará poderes latentes que a minha própria essência selada não pode mais manifestar."
**MESTRA**: "Sempre que a fome apertar e você precisar de alívio seguro sem elevar a sua Exposição perante o colégio, venha até mim nesta sala. Eu cuidarei de você."
Pela primeira vez desde que cheguei a esta academia maldita, a névoa do desespero se dissipa. Eu tenho uma dívida, um Grilhão no peito e uma mestra perigosa... mas tenho um rumo.

---


### Evento Especial: `evento_loira_banheiro_anomalia`

O ar no banheiro interditado do segundo andar é gelado e tem cheiro de ferrugem, azulejos úmidos e um perfume barato de décadas passadas.
A lâmpada vermelha de emergência oscila no teto, projetando sombras retorcidas sobre o piso encharcado.
No centro da bancada de porcelana carcomida, repousa o espelho principal.
No centro do vidro fosco e salpicado de mofo, um halo desenhado em batom carmesim reluz com uma luminescência doentia.
Ao me aproximar, a imagem do meu próprio reflexo não acompanha os meus movimentos. A figura no vidro tem a cabeça inclinada, as pálpebras entreabertas e um meio sorriso que gela a espinha.
O vidro começa a tremer e a ranger sob uma pressão descomunal. O desenho de batom se retorce, e uma risada rouca, entrecortada por engasgos de água fria, reverbera nos azulejos.
O espelho se parte com o estampido de uma lâmina partindo osso!
A Dama do Espelho — a Loira do Banheiro — rompe a barreira do reflexo! Garras pálidas e afiadas cravam na moldura estilhaçada, projetando um rosto de beleza cadavérica e olhos negros arregalados com um frenesi doentio.
O sorriso dela é uma fenda rubra manchada de batom e sangue seco que se estende de orelha a orelha.
**LOIRA_BANHEIRO**: "Eu farejo o que corre nessas suas veias de papel! O gosto roubado de uma linhagem pura... o cheiro de um lacaio que não sabe se é homem ou monstro!"
**LOIRA_BANHEIRO**: "Entregue a sua garganta para o vidro! Se você não tem coragem de se olhar no espelho... eu serei o seu reflexo para sempre!"

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Cravar os pés no chão e contra-atacar o bote espectral! (+1 Coragem)"*
**VICTOR VANE**: "Eu já tenho demônios demais cobrando o meu pescoço nesta academia. Você não vai ser mais uma na minha conta!"
> - 🔹 Escolha: *"Analisar o fluxo místico do halo de batom e romper a âncora! (+1 Intelecto)"*
**VICTOR VANE**: "O batom fecha o selo entre o vidro e a carne... Se eu atingir o centro da rachadura, o espectro perde o corpo!"
O golpe definitivo estilhaça o ponto de convergência do halo de batom! A força do impacto atravessa a imagem espectral da loira, desestabilizando o corpo etéreo que a mantinha presa à matéria.
**LOIRA_BANHEIRO**: "NÃÃÃO...! O espelho... não me deixe desaparecer no escuro outra vez...!"
Com um grito agudo que faz as lâmpadas e os espelhos de toda a ala vibrarem, a aparição explode em uma chuva de milhares de estilhaços cristalinos e névoa rubra gélida.
A pressão asfixiante que esmagava o meu peito se desfaz. O gotejar das torneiras silencia.
**VICTOR VANE**: "Mais um fantasma que esta escola tentou sepultar em silêncio. Uma anomalia a menos cobrando a minha garganta."

---


### Evento Especial: `evento_hachishaku_anomalia`

A névoa sobre as lápides do cemitério está tão densa que mal consigo enxergar meus próprios sapatos. O ar cheira a terra revirada, flores murchas e ferro frio.
O fragmento do chapéu de palha no meu bolso arde com um calor espectral. A criatura sabe que a sua âncora foi violada.
Um som gutural, abafado e cavernoso quebra o silêncio da noite, reverberando a poucos metros atrás de mim:
“Po... po... po...”
Ela se ergue por trás de um mausoléu em ruínas. A silhueta é monumental — quase três metros de altura, vestindo um vestido de verão imaculado e um chapéu de abas largas que projeta uma sombra impenetrável sobre o rosto.
Sob a aba do chapéu, apenas um sorriso cadavérico e dois olhos desprovidos de vida me fitam fixamente. A pressão mística faz os ossos do meu crânio estalarem.
**HACHISHAKU**: "Po... po... Você carrega um sangue que não te pertence, garoto... Entregue o seu pulso para a névoa..."

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"“Eu não atravessei uma cidade inteira para virar banquete de fantasma!” (+Coragem)"*
**VICTOR VANE**: "Eu já tenho dívidas demais cobrando a minha carne nesta escola. Uma lenda urbana não vai ditar onde eu caio!"
> - 🔹 Escolha: *"Espalhar o sal consagrado no solo e romper a projeção física! (+Intelecto)"*
**VICTOR VANE**: "A fita rasgada do chapéu ancora a sua forma na pedra... Se o sal quebrar o círculo, a sua matéria se desfaz!"
O impacto do golpe final atravessa o núcleo etéreo da aparição! O sal consagrado queima a barra do vestido branco em labaredas azuis.
**HACHISHAKU**: "POOOOO...!"
Com um uivo espectral que ecoa pelos muros da academia, a mulher colossal se desfaz em uma chuva de cinzas prateadas e neblina dispersa.
O peso sufocante sobre o meu peito desaparece. No solo encharcado, resta apenas uma relíquia consagrada e um fragmento de giz.
**VICTOR VANE**: "A Mulher Gigante foi expurgada do cemitério. Uma anomalia a menos acelerando o fim deste lugar."

---


### Evento Especial: `evento_lote_necrotico_anomalia`

Sigo o rastro de líquido esverdeado e fosforescente pelas galerias mais baixas das caldeiras. O calor aqui é sufocante, misturado a um odor repugnante de ácido sulfúrico e carne necrosada.
Numa câmara fechada atrás das tubulações mestras, avisto tonéis de sangue sendo manipulados clandestinamente.
Um homem com máscara de gás e jaleco de borracha manchado despeja um pó cinzento num tonel de sangue filtrado. Ao ouvir meus passos, ele se vira num solavanco, erguendo um frasco fumegante.
**ALQUIMISTA_RENEGADO**: "Quem mandou você aqui?! Os carrascos de uniforme branco da Presidente... ou aquela ratazana gananciosa da Valéria?!"
**ALQUIMISTA_RENEGADO**: "Não dou a mínima! Esse lote vai render o triplo na enfermaria e a culpa do frenesi vai cair na aberração trancada na sala de música!"

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"“Adulterar o sangue para enlouquecer inocentes acaba aqui.” (+Humanidade)"*
**VICTOR VANE**: "Essa escola já tem monstros demais nas sombras. Você não vai lucrar envenenando quem mal consegue respirar."
> - 🔹 Escolha: *"“Você cometeu um erro de cálculo: sangue estragado me deixa com raiva.” (+Coragem)"*
**VICTOR VANE**: "Você cometeu um erro primário de química, doutor: mexer com a comida de quem tem presas é garantia de pescoço quebrado."
Com um golpe certeiro no antebraço, quebro o frasco de reagente antes que ele possa arremessá-lo! O alquimista desaba de joelhos sobre a grelha de ferro, tossindo com as mãos algemadas pelas próprias tubulações.
**VALÉRIA (Mercadora das Caldeiras)**: "Olha só... O novato tem dentes afiados e faro para desmanche clandestino."
Valéria surge das sombras da tubulação, batendo palmas lentas com um meio sorriso divertido.
**VALÉRIA (Mercadora das Caldeiras)**: "Esse desgraçado estava usando reagentes roubados do meu estoque para batizar bolsas da enfermaria. Se a Elara descobrisse, os carrascos iam descer aqui e fechar o meu mercado inteiro."
**VALÉRIA (Mercadora das Caldeiras)**: "Toma a sua comissão pela faxina, garoto. Negociante competente merece pagamento à vista."
**VICTOR VANE**: "O lote necrótico foi destruído. O sangue que circula nas caldeiras agora é um pouco menos letal."

---


### Evento Especial: `evento_galeria_quadros_anomalia`

O corredor do segundo andar está mergulhado na penumbra da Zona Vermelha. As molduras douradas dos retratos antigos reluzem opacas sob a luz da lua que vaza pelas janelas de chumbo.
Diante de mim repousa uma enorme tela a óleo: 'O Banquete da Fundação, 1889'. Doze nobres aristocratas brindam ao redor de uma mesa de mogno sob candelabros suntuosos.
O ar ao redor da tela é pesado e tem cheiro de terebintina velha, mas minha percepção ainda não é afiada o bastante para romper a barreira do verniz.
Afasto-me da parede antes que a ronda do Grêmio me encontre fora do dormitório.
O corredor do segundo andar cheira a óleo de linhaça podre, terebintina e ferro secular. À noite, a moldura entalhada em ouro parece pesada demais para a pedra da parede.
Paro diante da tela monumental: 'O Banquete da Fundação, 1889'.
Na manhã do meu primeiro dia, havia doze nobres brindando na pintura. Agora, meus olhos contam com clareza clínica: há quinze pessoas sobre o linho.
As três últimas estão espremidas no canto escuro do salão pintado, atrás da pilastra. Três adolescentes. Vestem o uniforme preto de bolsista da São Cipriano. A pele deles tem a textura grossa de pinceladas secas de tinta cinzenta, e seus dedos esmurram o verniz de dentro para fora em um desespero mudo.
**VICTOR VANE**: "Danilo Ramos... O garoto da lista da Emília."
Quando aproximo o rosto do linho, o verniz estala com o som de gelo quebrando. Um calor súbito e avassalador vaza da pintura, trazendo o aroma de carne assada, frutas silvestres e cálices de sangue puro e quente — um banquete suntuoso e proibido que atinge o estômago de Ghoul como uma navalha em brasa.
Na cabeceira da mesa pintada, o Fundador — o Barão Cipriano — vira o pescoço num ângulo seco e antinatural. Um pincel invisível redesenha os lábios dele em tempo real, esticando um sorriso patronal e predatório.
Ele ergue uma taça transbordando em líquido escarlate diretamente na minha direção.
**O BARÃO CIPRIANO (Voz da Pintura)**: "Frio aí fora, não é, Sr. Vane? O mundo dos homens cobra juros a cada batimento. Mas aqui dentro... a mesa está sempre posta. Sem fome. Sem dívidas. Dê apenas um passo."
A moldura sangra gotas espessas de óleo escuro sobre o rodapé. Os dedos dos estudantes aprisionados batem contra a superfície invisível da tela, balançando a cabeça em pânico absoluto, implorando para que eu não aceite.

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Tocar a taça e provar do banquete pintado (A Fome exige alívio imediato)"*
Minha garganta queima. A promessa de saciedade infinita anestesia as minhas defesas.
Estendo os dedos e toco a borda da taça. A tela cede como água morna e espessa.
O calor invade meus braços... mas quando tento puxar o corpo de volta, minha pele ganha a textura rígida e quebradiça do linho cru.
Olho para fora da moldura. O corredor da academia agora parece uma gravura bidimensional, distante e cinzenta. Minha voz não passa de uma camada de verniz transparente.
Um garoto de uniforme preto me passa um prato vazio. O Barão sorri e brinda ao meu lado.
Eu nunca mais senti sede. E nunca mais desci da parede do segundo andar.
Puxo o frasco concentrado de reagente químico do bolso e arremesso o líquido cáustico diretamente sobre a assinatura dourada no canto da pintura!
A reação química ferve com um chiado ensurdecedor de ácido. O óleo de linhaça borbulha em fumaça esmeralda, derretendo a perspectiva da sala de jantar.
O rosto do Barão se desmancha em uma pasta preta e disforme. A ilusão desaba em farrapos de tinta fresca!
Com um estalo seco de verniz quebrado, algo metálico despenca de dentro da tela rasgada e tilinta no chão de pedra.
Abaixo-me e recolho o objeto: é um crachá de metal com o nome gravado: Danilo Ramos — Bolsista de Música nº 18.
Aproximo a placa de metal dos olhos sob a fresta de luz. É a prova definitiva da extorsão da mantenedora. E, na borda da moldura trincada, raspo três lascas brilhantes de Pigmento de Alma condensado.
A pintura volta a ser uma tela morta e inerte. Uma das armadilhas da mantenedora acaba de ser neutralizada.
Se esta tela se alimenta de almas fracas e sangue mortal, a maldição pré-diluviana que corre em minhas veias é veneno puro para a ilusão de um nobre decadente.
Passo a unha sobre a palma da mão direita, abrindo um talho rubro. Pressiono a carne aberta contra o peito do Fundador na pintura!
O impacto reverbera como um trovão subterrâneo. O sangue rubro ferve e queima o linho como brasa viva.
Por três segundos, o véu da arte se rasga: sou puxado para o vazio da sala de jantar onde o estudante aprisionado agarra meu braço antes que o feitiço colapse.
**ESTUDANTE APRISIONADO NA TELA**: "Obrigado... O cofre... Arquivo dos Fundadores... Código trinta e um, zero oito... A Diretoria sabia de tudo..."
O mundo pintado se estilhaça e sou cuspido com violência contra o piso frio do corredor!
Ofegante, estanco o corte na mão. O quadro agora é apenas um emaranhado de cinzas e verniz queimado.
> - 🔹 Escolha: *"Conter a respiração, desviar os olhos e recuar com frieza."*
A regra dois martela no meu crânio: nunca confiar em quem sorri antes de oferecer. E aquele homem na tela sorri como um agiota de almas.
Travo os calcanhares. Dou três passos para trás sem desgrudar a mão da lâmina, até que a escuridão do corredor engula a luz do banquete.
Ainda não é a hora. Mas agora eu sei o que a escola esconde atrás da tinta.

---


### Evento Especial: `entregar_cracha_emilia`

**VICTOR VANE**: "Emília. Eu estive no corredor leste durante a noite."
Pouso o crachá de metal manchado de óleo sobre a mesa de carvalho.
Ela recolhe a placa de identificação com as pontas dos dedos trêmulas. Seus olhos lêem o nome em voz baixa.
**EMÍLIA (Noviça Devota)**: "Danilo Ramos... O garoto da turma de violino."
**EMÍLIA (Noviça Devota)**: "A administração jurou para os pais dele que ele havia embarcado de volta para o interior. Ele estava... ele estava dentro daquela pintura o tempo todo?"
**VICTOR VANE**: "O Barão Cipriano deixou armadilhas vivas nesta escola. Quem não tem dinheiro ou quem perde o controle da dívida acaba servindo de combustível para a tela."
**EMÍLIA (Noviça Devota)**: "Obrigada por resgatar a verdade, Victor. Meu pai sempre disse que a compaixão em uma terra amaldiçoada é uma fraqueza... mas ver você trazer isso de volta me prova que ele estava errado."

---


### Evento Especial: `negociar_pigmento_valeria`

**VICTOR VANE**: "Valéria. Tenho algo que pode te interessar."
Coloco o frasco com as lascas de Pigmento de Alma sobre a bancada de ferro.
Ela apaga o pirulito e pega uma das lascas com uma pinça de relojoeiro, examinando o brilho arroxeado sob a chama da tocha azul.
**VALÉRIA (Mercadora das Caldeiras)**: "Verniz de sacrifício da galeria histórica... Garoto, você tem faro para coisa perigosa. Os falsificadores do Conselho pagam uma fortuna por isso para selar salvo-condutos falsos."
**VALÉRIA (Mercadora das Caldeiras)**: "Toma aqui: cento e cinquenta créditos à vista. Negócio limpo com quem sabe sujar as mãos."

---


### Evento Especial: `evento_partitura_carnal_climax`

Empurro a porta da sala de música com as três estrofes recuperadas da Partitura Carnal entre os dedos. As pautas emitem um calor elétrico que arde na palma da minha mão.
**MESTRA**: "Você reuniu as estrofes... Que cachorrinho dedicado e obstinado."
Lility desce do tampo do piano e seus dedos pálidos deslizam sobre os manuscritos amarelados.
**MESTRA**: "Eu compus este réquiem há muitos séculos, Victor... Na noite em que as primeiras águas negras começaram a subir. Cada compasso é uma âncora que puxa a essência do abismo para a superfície."
**MESTRA**: "Você teve coragem de juntar as notas. Agora vamos ver se os seus nervos suportam a harmonia."
Ela se senta diante do teclado de marfim empoeirado. Seus dedos tocam os primeiros acordes com uma ferocidade majestosa.
As notas vibram nas paredes, fazendo as vidraças rachadas ressoarem. O piso sob os meus pés treme... e do teto de madeira desaba uma teia de fios carmesins que se retorcem no ar!
Uma marionete etérea tecida em fios de sangue puro ganha vida ao som da música, brandindo garras de pura ressonância pré-diluviana!

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"“Toque até o fim, Lility! Eu cuido do que sair do chão!” (+Coragem / +Afeto Lility)"*
**VICTOR VANE**: "Não pare de tocar! Eu não passei por tudo isso para recuar diante de uma boneca de sangue!"
> - 🔹 Escolha: *"Analisar o ponto de tensão dos fios e cortar o elo motriz! (+Intelecto)"*
**VICTOR VANE**: "Os acordes mantêm os fios tensos... Se eu romper o ponto de convergência no peito dela, a estrutura desaba!"
O golpe definitivo corta o feixe principal de sustentação! Os fios de sangue se partem com estalos secos, dissolvendo a marionete em uma névoa carmesim que é absorvida pelo meu próprio peito.
**MESTRA**: "Impressionante... Você não apenas suportou as frequências do Dilúvio como decepou o eco da partitura com precisão cirúrgica."
Ela recolhe as folhas da partitura e as dobra com cuidado antes de entregá-las a mim.
**MESTRA**: "Guarde isso com a sua vida. Quando a hora da descida final chegar, este manuscrito abrirá o que as mãos mortais jamais conseguirão tocar."
**VICTOR VANE**: "A Partitura Carnal foi dominada. Mais um artefato primordial sob o meu controle."

---


### Evento Especial: `evento_inquerito_inquisicao_climax`

Aproveito a penumbra do gabinete vazio durante a troca de turnos da guarda. A chave obtida nas pistas abre com perfeição a gaveta com fundo falso atrás da escrivaninha de mogno de Elara.
Retiro uma pasta grossa timbrada com o selo eclesiástico da Inquisição. Diante dos meus olhos, a lista de doações e sacrifícios voluntários confirma a fraude: alunos bolsistas sendo sistematicamente entregues para manter a barreira do colégio estável.
Um estalo metálico seco ecoa do balcão de vitrais:
**INQUISIDOR_TATICO**: "Documentos confidenciais da cúria não são para os olhos de um ghoul recém-criado."
**INQUISIDOR_TATICO**: "Lorde Phillip foi claro: nenhum registro do pacto sobrevive à auditoria desta semana. Entregue os arquivos ou a sua cabeça será pregada no portão principal antes do amanhecer!"

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"“Esses arquivos são a prova de que esta escola é um abatedouro. Não vou devolvê-los.” (+Humanidade / Credo de Victor)"*
**VICTOR VANE**: "Eu já fui descartado uma vez por mentores covardes que escondiam as próprias fraudes. Não vou deixar vocês fazerem o mesmo com o resto destes alunos."
> - 🔹 Escolha: *"“Você atira devagar demais para quem caça predadores.” (+Coragem)"*
**VICTOR VANE**: "Balestra pesada, mira trêmula e ordens de burocratas... Vamos ver se a sua prata corta mais rápido do que as minhas presas."
O golpe definitivo parte o arco da balestra e arremessa o inquisidor contra a estante de arquivos pesados! Ele cospe sangue, rola pela sacada aberta e salta para os telhados na escuridão.
Recolho a pasta com as provas documentais completas e a enfio por dentro do meu casaco. O segredo mais bem guardado do Conselho Estudantil agora está nas minhas mãos.
**VICTOR VANE**: "O inquérito da Inquisição foi assegurado. Agora eu tenho alavancagem contra quem achava que podia me usar como peça descartável."

---


### Evento Especial: `evento_emilia_pacto_sangue`

A porta do Clube de Ocultismo é trancada com duas voltas na chave. O cheiro de incenso de mirra preenche a sala.
**EMÍLIA (Noviça Devota)**: "Um... um vampiro... Durante todo esse tempo, Victor?"
Suas mãos tremem ao segurar o crucifixo de prata contra o peito. O treinamento dos von Karsten grita para ela sacar a lâmina consagrada, mas seus olhos estão marejados.
**VICTOR VANE**: "Eu não escolhi isso, Emília. Naquela primeira noite, quando você me viu perto do pátio... eu já estava morrendo nas garras daquela coisa."
**VICTOR VANE**: "Eu só queria manter minha bolsa de estudos. Acordei com essa maldição na garganta, sem pedir por nada disso."
O aperto de Emília no crucifixo afrouxa. O terror rígido da caçadora se desfaz, dando lugar a uma compaixão dolorosa ao lembrar do rapaz assustado que conheceu no primeiro dia.
**EMÍLIA (Noviça Devota)**: "Você... você foi apenas uma vítima dessa escola podre. Meu Deus, Victor... o quão solitário e assustador isso deve ter sido para você..."
**EMÍLIA (Noviça Devota)**: "Mas escute bem: eu jamais permitirei que você ceda à escuridão e ataque os alunos desta academia! Nem um único inocente!"
**VICTOR VANE**: "Eu tenho me controlado, Emília. Eu juro."
**EMÍLIA (Noviça Devota)**: "Controle não basta contra a fome! Eu estudei a fisiologia da sua espécie nos arquivos do meu pai. Se você não se alimentar, entrará em Frenesi."
Emília respira fundo, fecha os olhos e murmura três Ave-Marias rápidas. Quando volta a abrir os olhos, seu rosto está completamente vermelho, mas ela desabotoa os dois primeiros botões da gola do uniforme, expondo a pele alva do pescoço.
**EMÍLIA (Noviça Devota)**: "Por isso... eu serei o seu sustento. Beba de mim, Victor. É meu dever cristão impedir uma tragédia nesta escola!"
**VICTOR VANE**: "(Ela acha mesmo que está salvando a escola inteira sozinha... Se ela sonhar que a Lility e a Elara já dividem esse cardápio comigo, ela me exorciza na hora.)"
**VICTOR VANE**: "Emília, tem certeza? Eu não quero machucar você."
**EMÍLIA (Noviça Devota)**: "A-Apenas vá logo antes que eu perca a coragem! É um sacrifício solene pela paz da academia...!"
Aproximo-me devagar. O cheiro dela é uma mistura embriagante de lírios, incenso e algo quente e luminoso que faz minhas presas latejarem.
Quando cravo os dentes de leve em sua pele, Emília solta um suspiro abafado, segurando com força na manga do meu casaco para não cair.
**EMÍLIA (Noviça Devota)**: "Ah...! P-Pelos céus... então é assim que..."
Ao entrar na sala do Grêmio na manhã seguinte, Elara sequer levanta os olhos dos documentos antes de inspirar o ar lentamente.
**ELARA (Presidente do Grêmio)**: "Ora, ora... Que perfume curioso, Victor. Mirra, cera de vela de altar e... fervor juvenil."
**ELARA (Presidente do Grêmio)**: "Andou assaltando a capela ou a senhorita von Karsten resolveu praticar a caridade com os dentes da noite?"
**VICTOR VANE**: "Você tem um olfato irritante, Presidente."
**ELARA (Presidente do Grêmio)**: "E você tem um paladar perigosamente exótico. Cuidado com o sangue do clero, querido. É quente demais... funciona quase como um vinho litúrgico batizado para a nossa espécie."
**ELARA (Presidente do Grêmio)**: "Se beber demais daquela santinha, é capaz de começar a brilhar no escuro... ou pior: sentir vontade de rezar antes de dormir."
**ELARA (Presidente do Grêmio)**: "Ah, e um conselho profissional: morda dois dedos abaixo da clavícula da próxima vez. O colarinho da Inquisição é alto, mas Lorde Phillip tem olhos de águia."
Na sala de música, Lility rodeia Victor como um felino, parando com os lábios a centímetros do ouvido dele.
**LILITY (Vampira Nobre)**: "Hmm... Comendo direto da mão da Igreja, meu cachorrinho? Devo admitir que você gosta de brincar na beira do abismo."
**LILITY (Vampira Nobre)**: "A pequena caçadora reza pela sua alma enquanto oferece o pescoço... achando que é a única heroína mantendo o monstro na coleira."
**LILITY (Vampira Nobre)**: "Me diga, VV: o que você acha que vai acontecer quando a sua 'salvadora exclusiva' descobrir que o sacrifício sagrado dela é apenas a sobremesa depois do banquete que você tem comigo e com a tirana do Grêmio?"
**LILITY (Vampira Nobre)**: "Não vá engasgar com tanta santidade... Eu odiaria perder meu brinquedo favorito para uma crise de ciúmes ungida."

---


### Evento Especial: `evento_valeria_safra_rara`

O vapor das caldeiras silva nos canos enferrujados. O cheiro de metal quente mistura-se à fumaça do cigarro de Valéria.
Jogo uma bolsa de sangue vazia sobre o caixote de ferro que serve de balcão.
**VICTOR VANE**: "Esse último lote tem gosto de plástico velho e anticoagulante, Val. Não tem nada melhor no estoque?"
**VALÉRIA (Mercadora das Caldeiras)**: "Olha só para você... Chegou no fim da semana inteiro. Confesso que apostei contra."
**VALÉRIA (Mercadora das Caldeiras)**: "O fornecimento do hospital tá cercado pelos cães de guarda do Grêmio. Mas como os nossos negócios têm rendido frutos..."
**VALÉRIA (Mercadora das Caldeiras)**: "Acho que você merece acesso ao catálogo restrito."

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"\"Direto ao ponto, Valéria.\""*
**VALÉRIA (Mercadora das Caldeiras)**: "Sem preliminares, né? Gosto assim. Quem enrola muito nas caldeiras acaba virando carvão."
> - 🔹 Escolha: *"\"Quanto vai me custar dessa vez?\""*
**VALÉRIA (Mercadora das Caldeiras)**: "Heh. Gosto quando você já abre a carteira antes de ouvir a oferta. Cliente prático é cliente que volta."
> - 🔹 Escolha: *"\"Vai me vender sangue vencido de novo?\""*
**VALÉRIA (Mercadora das Caldeiras)**: "Ei! Meus produtos têm selo de procedência das caldeiras, seu mal-agradecido. Mas relaxa... O que tenho hoje nunca viu uma embalagem plástica."
**VALÉRIA (Mercadora das Caldeiras)**: "Sangue da melhor qualidade. Sem intermediários... e direto da fonte."
Ela apoia o quadril contra a mesa de metal, deslizando o indicador pela gola da jaqueta até a curvatura do pescoço.
A artéria ali pulsa forte, visível sob a pele pálida e quente.
**VALÉRIA (Mercadora das Caldeiras)**: "Mas vai com calma, querido... Essa safra que você vai beber é edição limitada e bem rara. E o preço acompanha a exclusividade."
**VALÉRIA (Mercadora das Caldeiras)**: "E sem deixar marcas onde a clientela possa ver amanhã... ou eu cobro taxa de indenização por danos à vitrine da empresa."
**VICTOR VANE**: "Pode deixar. Vou fazer valer cada centavo."
Passo o envelope de notas pelo balcão. Valéria confere com os olhos semicerrados e tranca o trinco do escritório.
Aproximo-me devagar. Minhas mãos seguram sua cintura com firmeza, sentindo o calor do corpo dela contra o frio do meu peito.
As presas tocam a pele quente... e o primeiro rasgo libera um surto de nicotina, adrenalina pura e eletricidade.
**VALÉRIA (Mercadora das Caldeiras)**: "Nngh...! E-Ei...!"
A pose de comerciante inabalável dura exatamente três segundos. Os dedos dela cravam nas minhas costas e a respiração se perde num gemido rouco.
**VALÉRIA (Mercadora das Caldeiras)**: "O contrato... era só uma dose rápida, Vane... Quem te deu permissão pra... ahn... pra me puxar desse jeito...?"
**VALÉRIA (Mercadora das Caldeiras)**: "Isso aí... isso aí vai ter custo adicional... seu aproveitador..."
Mais tarde, nos corredores da academia...
**ELARA (Presidente do Grêmio)**: "Francamente, Victor... Cheirando a fuligem de caldeira, nicotina barata e ambição clandestina?"
**ELARA (Presidente do Grêmio)**: "Achei que o seu paladar estivesse refinando... mas vejo que continua frequentando o fast-food do subsolo."
**MESTRA**: "Os antigos caçavam monarcas em seus tronos dourados... e o meu cachorrinho esvazia a carteira no pescoço de uma contrabandista."
**MESTRA**: "Pelo menos me diga que a tal 'safra rara' valeu a sua falência, VV. Seria patético ter um servo pobre e com mau gosto."

---

## PARTE IV: INTERAÇÕES SOCIAIS LIVRES & ROTAS COM HEROÍNAS


### Encontro Social / Exploração: `menu_encontro_lility`

**MESTRA**: "Eu avisei que não quero vê-lo perto de mim pelo resto da noite, lacaio. Saia antes que eu o parta em dois."

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"✋ Aproximar-se / Modo de Toque (Click & Reação)"*
> - 🔹 Escolha: *"🩸 Pedir Audiência para Alimentação no Covil (O Preço do Sangue)"*
> - 🔹 Escolha: *"📜 Deixar Bilhete Clandestino (Agendar Encontro Noturno na Sala de Música)" if encontro_agendado_heroina is None and periodo != "Noite"*
**MESTRA**: "Um bilhete secreto marcando hora no meu piano? Que atrevimento delicioso... Estarei esperando nas sombras."

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"\"Como você suporta ficar confinada nesta sala de música há tanto tempo?\""*
**MESTRA**: "Tempo... Uma invenção tola dos mortais para justificar a própria pressa."
**MESTRA**: "Um século trancada aqui não é nada para quem viu civilizações inteiras afundarem na lama. O tédio... só é perigoso quando me dá vontade de brincar."
> - 🔹 Escolha: *"\"Elara realmente tem controle total sobre você com esse Grilhão?\""*
**MESTRA**: "Aquela boneca de porcelana do Conselho? Ela é apenas a carcereira da superfície."
**MESTRA**: "Deixe que ela finja que manda em mim. A coleira dela aperta o pescoço... mas quem controla a sede lá embaixo somos nós."
> - 🔹 Escolha: *"\"Espero que o meu sangue não esteja deixando a 'Mestra' mimada demais.\""*
**MESTRA**: "Mimada? Ora, que cachorrinho audacioso."
**MESTRA**: "Agradeça por eu não ter arrancado o seu braço como aperitivo hoje, VV. Mas continue insolente... Eu prefiro servos com garras a capachos submissos."
**MESTRA**: "Ora, ora... quem ensinou meu cachorrinho a rosnar com tanta convicção? Talvez haja mais sangue primordial em você do que imaginei."
**MESTRA**: "Não ouse tentar impor sua vontade contra sua criadora, lacaio. Lembre-se de onde veio sua coleira."
> - 🔹 Escolha: *"👣 Continuar Investigando a Área"*

---


### Encontro Social / Exploração: `tocou_cabeca_lility`

**MESTRA**: "Hmph... Fazendo cafuné na própria dona, cachorrinho? Vou permitir só porque suas mãos estão quentes."
**MESTRA**: "O que pensa que está fazendo? Não sou um animal de estimação para receber carinho na cabeça."

---


### Encontro Social / Exploração: `tocou_rosto_lility`

**MESTRA**: "Cuidado onde encosta, Victor... Minhas presas estão muito perto dos seus dedos."

---


### Encontro Social / Exploração: `tocou_peito_lility`

**MESTRA**: "Perdeu o juízo junto com a sua humanidade, lacaio? Encoste a mão aí de novo sem permissão e voltará para o quarto com quatro dedos."
**MESTRA**: "Eu avisei! Parece que meu cachorrinho precisa aprender limites através da dor! (-15 HP)"

---


### Encontro Social / Exploração: `evento_rng_lility_dormindo_manha`

A luz pálida da manhã atravessa a janela empoeirada. Exausta pela vigília noturna, Lility apagou profundamente sobre o sofá.

---


### Encontro Social / Exploração: `menu_alimentacao_covil_lility`

**MESTRA**: "Que asco intolerável... O aroma de mirra e eucaristia daquela caçadora dos von Karsten está impregnado na sua garganta!"
**MESTRA**: "Você ousa pedir o meu sangue sagrado enquanto ainda digere o veneno da Igreja?! Afaste-se de mim antes que eu queime as suas vísceras!"
**MESTRA**: "Dê mais um passo e eu mesma arranco a sua garganta, lacaio. Saia daqui!"
**MESTRA**: "Você já bebeu das minhas veias neste período, cachorrinho. Uma dama não é uma torneira pública. Deixe meu sangue assentar antes de me incomodar de novo."
**MESTRA**: "Você não está à beira da loucura, Victor. Suas veias não tremem, sua respiração está calma. Não desperdice o meu sangue por puro capricho. Volte quando a fome realmente arder."
**MESTRA**: "Você veio até o meu piano suplicando pelo meu pulso... Mas sabe muito bem que nada neste mundo é gratuito, calouro. O que você me trouxe em troca?"

> **[DECISÃO DO JOGADOR]:**
**MESTRA**: "Absinto destilado nas panelas de cobre das caldeiras... O aroma da artemísia quase disfarça a fuligem deste colégio decadente."
**MESTRA**: "Você tem modos afinal, calouro. Aprendeu rápido que uma dama não oferece seu néctar a quem chega de mãos abanando."
Ela recebe a dose com dedos delicados, provando uma gota na ponta da língua antes de estender o pulso alvo como mármore.
**MESTRA**: "Beba devagar... saboreie o calor de quem ainda se importa se você respira amanhã. Agora você carrega meu odor."
**MESTRA**: "A partitura... Minhas notas originais, traçadas antes de Elara me trancar nesta sala carcomida..."
Pela primeira vez, a máscara de soberba de Lility treme. Seus olhos carmesins fixam as pautas amareladas com uma nostalgia quase dolorosa.
**MESTRA**: "Talvez você não seja apenas um cão assustado afinal, Victor. Aproxime-se. Deixe que eu te recompense como um verdadeiro aliado merece."
**MESTRA**: "O sangue que corre entre nós hoje tem o sabor de eras passadas... Uma aliança viva."
**MESTRA**: "Então a puritana de branco anda deslocando os cães do conselho para vigiar o perímetro leste? Previsível... Ela sempre teme o que não pode controlar."
**MESTRA**: "Informação de qualidade vale mais do que ouro nos corredores, Victor. Venha. Você conquistou o seu pagamento de hoje."
**MESTRA**: "Aproveite bem a saciedade. E continue de olhos e ouvidos bem abertos nos corredores de Elara."
> - 🔹 Escolha: *"🩸 Suplicar de Mãos Vazias: A Confissão Íntima (-2 Humanidade / +60%% Saciedade)"*
**MESTRA**: "Veio de mãos abanando, cachorrinho? Sem uma garrafa, sem um relatório, tremendo de fome diante do meu piano..."
**MESTRA**: "Se quer que eu abra minhas veias por misericórdia pura, terá que pagar com algo mais caro do que moedas, Victor. Quero a verdade."
**MESTRA**: "Diga-me... qual foi a sensação exata no seu peito quando aquele seu professor covarde sorriu para você e te empurrou para a sarjeta?"

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"“Senti que a decência humana era uma piada inventada por fracos.” (+Intelecto / -1 Humanidade)"*
**MESTRA**: "Uma conclusão amarga, mas lúcida. A fraqueza é a única praga que os homens nunca conseguem expurgar."
> - 🔹 Escolha: *"“Senti vontade de vê-lo engolir os próprios dentes no chão do laboratório.” (+Coragem / +1 Ressonância)"*
**MESTRA**: "A fúria de quem foi traído... É essa chama que me impediu de deixar você morrer ontem à noite."
> - 🔹 Escolha: *"“Senti apenas frio. E a certeza de que nunca mais dependeria da piedade de ninguém.” (+Afeto / +Vínculo)"*
**MESTRA**: "Frio... É um velho conhecido meu. Uma solidão que não se apaga nem depois de séculos."
Lility aproxima os dedos do meu queixo, forçando meu olhar ao encontro do dela, antes de deslizar a manga e expor a veia pulsante.
**MESTRA**: "Beba, Victor. Suas feridas e seus pecados agora correm comigo."
> - 🔹 Escolha: *"⚡ Suplicar de Mãos Vazias: Transe Violento (-15 HP / -3 Humanidade / +2 Ressonância / +80%% Saciedade)"*
**MESTRA**: "Quer o meu sangue sem concessões, sem palavras e sem oferendas? Então aguente o peso do que está pedindo!"
Ela agarra minha nuca com força inumana e pressiona o pulso aberto contra meus lábios com violência febril.
O sangue ancestral entra como chumbo líquido na minha garganta! O impacto é tão avassalador que meus joelhos batem com estrondo na madeira carcomida do chão.
Visões de cidades submersas e colunas ciclópeas colidem no meu crânio com a violência de uma avalanche! Minha mente vacila no limiar do colapso.
**MESTRA**: "Levante-se, lacaio. Se não for capaz de suportar um trago cru do meu poder, não durará uma semana neste colégio."
> - 🔹 Escolha: *"🔙 Voltar"*

---


### Encontro Social / Exploração: `menu_encontro_emilia`

**EMÍLIA (Noviça Devota)**: "V-Victor?! Seus olhos... suas presas estão visíveis! O que aconteceu com o seu rosto?!"
**EMÍLIA (Noviça Devota)**: "Por favor, Victor... preciso de espaço para rezar e pensar no que está acontecendo nesta escola. Não se aproxime de mim por hoje."

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"✋ Aproximar-se / Modo de Toque (Click & Reação)"*
**EMÍLIA (Noviça Devota)**: "A-Aqui nos corredores não, Victor... Mas se a sua fome está apertando... eu não posso deixar você se descontrolar."
Emília afasta a gola do uniforme com as mãos trêmulas. Quando cravo os dentes de leve em sua pele alva, o calor do sangue sagrado afasta todo o frio do meu peito.
**EMÍLIA (Noviça Devota)**: "Ah...! P-Pelos céus... Faça isso parar antes que alguém venha..."
> - 🔹 Escolha: *"📜 Deixar Bilhete Clandestino (Agendar Encontro Noturno no Clube de Ocultismo)" if pacto_emilia_ativo and encontro_agendado_heroina is None and periodo != "Noite"*
**EMÍLIA (Noviça Devota)**: "U-Um bilhete para nos encontrarmos à noite no Clube de Ocultismo?! Victor... isso é tão arriscado... mas estarei lá pontualmente."
**EMÍLIA (Noviça Devota)**: "Victor...! Você está ferido de novo."
**EMÍLIA (Noviça Devota)**: "Fique parado um instante... Deixe-me trocar esse curativo antes que infeccione. Pronto... Não faça essa cara de dor. (+20 HP)"
**EMÍLIA (Noviça Devota)**: "Sobre o que você gostaria de conversar, Victor?"

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"\"Alguma novidade sobre os desaparecimentos nos corredores?\""*
**EMÍLIA (Noviça Devota)**: "Três novos registros só esta semana... A direção arquivou todos como 'evasão voluntária'."
**EMÍLIA (Noviça Devota)**: "Ninguém foge do colégio de madrugada sem levar as próprias malas, Victor. Algo está se alimentando aqui dentro."
**EMÍLIA (Noviça Devota)**: "O último rastro levava para a ala fechada do segundo andar... Mais especificamente para o antigo banheiro interditado."
**EMÍLIA (Noviça Devota)**: "Encontraram respingos de sangue coagulado diante do grande espelho rachado. Por favor, Victor... me prometa que você não vai se aproximar daquele lugar."
**EMÍLIA (Noviça Devota)**: "Você não deveria saber sobre isso, Victor...! A ala foi isolada porque encontraram um calouro em transe hipnótico diante do espelho."
**EMÍLIA (Noviça Devota)**: "Ele murmurava sobre uma silhueta loira de olhos vermelhos presa atrás do vidro... O conselho quer abafar o caso, mas a porta está apenas encostada."
> - 🔹 Escolha: *"\"Você parece exausta, Emília. Dormiu alguma coisa essa noite?\""*
**EMÍLIA (Noviça Devota)**: "E-Eu...? Só... umas duas horas."
**EMÍLIA (Noviça Devota)**: "Estava relendo relatórios antigos e checando os horários das rondas... Mas obrigada por perguntar. Quase ninguém repara nisso."
> - 🔹 Escolha: *"\"Anotando mais detalhes sobre mim no seu caderninho secreto?\""*
**EMÍLIA (Noviça Devota)**: "N-Não é segredo! São apenas anotações investigativas normais!"
**EMÍLIA (Noviça Devota)**: "...Tá bom, talvez haja uma página com os seus horários. Mas é só para garantir que você não se meta em encrenca, bobo."
**EMÍLIA (Noviça Devota)**: "B-bem... meu pai me enviou alguns relatórios sobre o selo do subsolo... Se prometer não contar a ninguém, posso compartilhar uma anotação com você..."
**EMÍLIA (Noviça Devota)**: "Por que você está tão interessado nos segredos da Inquisição, Victor? Isso não parece curiosidade de um estudante comum..."
> - 🔹 Escolha: *"👣 Continuar Investigando a Área"*

---


### Encontro Social / Exploração: `tocou_cabeca_emilia`

**EMÍLIA (Noviça Devota)**: "V-Victor?! Faz tanto tempo que alguém não faz um gesto tão gentil... Sua mão é tão calma..."

---


### Encontro Social / Exploração: `tocou_oculos_emilia`

**EMÍLIA (Noviça Devota)**: "M-meus óculos estavam tortos de novo? S-se você continuar tão perto assim, meu coração vai disparar..."

---


### Encontro Social / Exploração: `tocou_crucifixo_emilia`

Ao roçar os dedos no crucifixo de prata benta no colarinho dela, meu sangue de Ghoul reage com uma queimadura aguda! (-5 HP)
**EMÍLIA (Noviça Devota)**: "Victor?! Você queimou os dedos só de encostar na minha prata consagrada... Por que a sua pele reagiu assim?"

---


### Encontro Social / Exploração: `menu_encontro_valeria`

**VALÉRIA (Mercadora das Caldeiras)**: "Hoje não tem negócio nem conversa fiada, bolsista. Volta amanhã quando meu humor melhorar."

> **[DECISÃO DO JOGADOR]:**
**VALÉRIA (Mercadora das Caldeiras)**: "Peças de cobre intactas e uma bolsa clandestina inteira... Você é eficiente, bolsista."
**VALÉRIA (Mercadora das Caldeiras)**: "Aqui seus duzentos e cinquenta contos, uma dose de estimulante do meu estoque e abati quatrocentos da sua dívida com os babacas do Grêmio."
> - 🔹 Escolha: *"✋ Aproximar-se / Modo de Toque (Taxa de Ousadia)"*
**VALÉRIA (Mercadora das Caldeiras)**: "Negócio fechado, sócio. Puxa a grade dos fundos e não deixa marca no meu pescoço."
Quando minhas presas tocam sua artéria pulsante, a adrenalina, o café e a nicotina do sangue de Valéria explodem na minha língua.
**VALÉRIA (Mercadora das Caldeiras)**: "Nngh... Caramba, Vane... essa mordida foi mais profunda que da última vez... Você tá me deixando mole nas pernas..."
**VALÉRIA (Mercadora das Caldeiras)**: "Sem dinheiro na mão, sem safra no balcão, Victor. Minha artéria não aceita 'fiado'. Volta quando a sua carteira fizer barulho."
Minha garganta arde... Ter que engolir o deboche comercial dela de estômago vazio é uma humilhação necessária.
> - 🔹 Escolha: *"📜 Deixar Bilhete Clandestino (Agendar Encontro Noturno nas Caldeiras)" if safra_rara_valeria and encontro_agendado_heroina is None and periodo != "Noite"*
**VALÉRIA (Mercadora das Caldeiras)**: "Encontro noturno marcado no meu território? Se você não faltar, eu reservo a melhor torneira das caldeiras pra você, sócio."
> - 🔹 Escolha: *"🛒 Abrir Loja do Mercado Negro"*

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"\"Como você consegue operar o Mercado Negro debaixo do nariz do Grêmio?\""*
**VALÉRIA (Mercadora das Caldeiras)**: "Regra número um dos negócios, sócio: até os santos precisam de quem tire o lixo da capela."
**VALÉRIA (Mercadora das Caldeiras)**: "A Presidente finge que não me vê, e eu garanto que os vampiros desesperados comprem daqui em vez de morderem os monitores nos corredores. Todo mundo ganha."
> - 🔹 Escolha: *"\"As caldeiras não sufocam você? Esse lugar parece um forno.\""*
**VALÉRIA (Mercadora das Caldeiras)**: "O calor espanta os frouxos e o barulho dos pistões abafa qualquer conversa que não deva vazar."
**VALÉRIA (Mercadora das Caldeiras)**: "Prefiro o cheiro de ferrugem e vapor do que a hipocrisia engomada dos andares de cima. Aqui embaixo o jogo é limpo: pagou, levou."
> - 🔹 Escolha: *"\"Esse pirulito na boca é para disfarçar o cheiro de fumaça ou o medo dos monstros?\""*
**VALÉRIA (Mercadora das Caldeiras)**: "Heh. Medo de monstro? Bolsista, eu já fechei contrato com criaturas que fariam você molhar o uniforme."
**VALÉRIA (Mercadora das Caldeiras)**: "O pirulito é só charme da gerência. E garanto que o sabor é bem melhor do que as besteiras que você fala."
**VALÉRIA (Mercadora das Caldeiras)**: "Arg! Tá bom, você é mais esperto do que aparenta. Fica com essa comissão e não espalha meus custos operacionais. (+[total_comissao] moedas)"
**VALÉRIA (Mercadora das Caldeiras)**: "Tentar passar a perna na contrabandista que comanda as caldeiras? Você tem coragem, mas não tem cérebro, sócio."
> - 🔹 Escolha: *"👣 Continuar Investigando a Área"*

---


### Encontro Social / Exploração: `tocou_cabeca_valeria`

**VALÉRIA (Mercadora das Caldeiras)**: "Ei, ei, sem bagunçar o penteado, bolsista. Não sou gato de rua pra ganhar cafuné de graça."

---


### Encontro Social / Exploração: `tocou_corpo_valeria`

**VALÉRIA (Mercadora das Caldeiras)**: "Olhar a vitrine é de graça, lacaio. Mas encostar na mercadoria tem taxa de conveniência: se a mão escorregar de novo, cobro cinquentinha por toque."
**VALÉRIA (Mercadora das Caldeiras)**: "Cinquenta na conta! Gosto de clientes que sabem o que querem e pagam à vista. (-$50 / +1 Domínio / +1 Afeto)"
**VALÉRIA (Mercadora das Caldeiras)**: "Opa! Sem fundos, sem mãos bobas, garoto. Aqui no subsolo ninguém leva nada no fiado! (-10 HP)"

---


### Encontro Social / Exploração: `encontro_nora_cela_cripta`

No centro da abóbada de pedra da cripta, cercada por tubos de cobre e válvulas sibilantes, ergue-se uma cápsula cilíndrica de vidro espesso selada com glifos rúnicos.
Dentro do líquido alquímico âmbar, suspensa por correntes de contenção, está a aluna do alfinete 31 — Nora Vasques.
O uniforme preto rasgado nas mangas. As marcas recentes de agulhas e bisturis nos braços comprovam as extrações forçadas do Grêmio. O líquido borbulha lentamente, mantendo-a em um torpor agonizante.
Ao sentir a vibração dos meus passos contra o mármore frio, os olhos claros de Nora tremulam e se abrem debilmente. Ela ergue a mão pálida, apoiando as pontas dos dedos contra a parede de vidro.
**NORA (Prisioneira das Criptas)**: "...V-Victor...? É você...? O bolsista... do primeiro dia..."
**VICTOR VANE**: "Nora... O que eles fizeram com você?!"
**NORA (Prisioneira das Criptas)**: "O Grêmio... Elara e os executores de casaco branco... Eles não me mataram naquela noite... Eles me trouxeram para cá..."
**NORA (Prisioneira das Criptas)**: "Eles usaram o meu sangue para testar a destilação de vitae contaminada... O rebanho da escola alimenta o cofre... e o cofre alimenta o que está acordando lá embaixo..."
A voz dela ressoa abafada pelas ranhuras acústicas da câmara.
**NORA (Prisioneira das Criptas)**: "Eu sabia que não duraria muito tempo... Antes de me trancarem nesta redoma, eu escondi a Chave-Mestra dos Dutos de Ventilação... Ela caiu no ralo de drenagem sob a base desta cela..."
**NORA (Prisioneira das Criptas)**: "Mas isso... isso está queimando a minha mente... A Besta quer rasgar o vidro... Por favor... não me deixe virar um monstro sem alma..."
Ao sentir a presença de um predador, Nora desperta em sobressalto, batendo debilmente os nós dos dedos contra o vidro espesso.
**NORA (Prisioneira das Criptas)**: "...Q-Quem está aí...? Mais um carrasco do Conselho com frascos de teste...?"
**VICTOR VANE**: "Calma. Eu não sou do Conselho Estudantil."
**NORA (Prisioneira das Criptas)**: "Você... você fede a sangue recém-convertido... Mas ainda tem olhos de gente. Por favor... o líquido desta cuba queima como ácido rúnico... Eu não aguento mais os testes de Elara..."
**NORA (Prisioneira das Criptas)**: "Eles pretendem drenar o que sobrou de mim para abrir as travas do cofre principal..."

> **[DECISÃO DO JOGADOR]:**
Conecto o [item_usado_nora] na válvula de purga lateral e corto a palma da minha mão. Deixo meu sangue vivo escorrer pelos dutos de alimentação para neutralizar a toxina ácida do Grêmio (-10 HP).
O líquido âmbar clareia. As convulsões de Nora cessam e uma respiração calma preenche seus pulmões.
**NORA (Prisioneira das Criptas)**: "...A queimação... parou... Minha mente... está limpa pela primeira vez em semanas..."
**NORA (Prisioneira das Criptas)**: "Você me salvou duas vezes, Victor. Uma com uma caneta... e outra com a sua própria vida."
**NORA (Prisioneira das Criptas)**: "Eu nunca esperei que alguém neste inferno sacrificasse a própria vitae por uma cobaia descartada..."
Nora aponta para a grade inferior de escape, onde a água desceu. Sob a fresta de ferro, retiro uma chave pesada de latão polido: a Chave-Mestra dos Dutos de Ventilação!
**VICTOR VANE**: "Descanse agora, Nora. Assim que eu acertar as contas com Elara e abrir este cofre, eu voltarei para tirar você daqui."
**NORA (Prisioneira das Criptas)**: "Tome cuidado... Os dutos passam por cima do salão dos guardas do Grêmio... Use a chave para contorná-los..."
> - 🔹 Escolha: *"[[MISERICÓRDIA]] Conceder a morte definitiva e poupá-la do sofrimento (+Humanidade / +Saciedade)"*
**NORA (Prisioneira das Criptas)**: "...Obrigada... Por favor... não me deixe acordar no Vazio como uma abominação de Cain..."
Giro a válvula de drenagem emergencial e conecto o fluxo ao meu próprio grilhão. Sorvo a agonia e o resto de vitae de Nora, garantindo-lhe uma partida rápida, sem dor e sem o tormento da fome eterna.
A expressão torturada de Nora finalmente descansa em uma paz serena enquanto a câmara se esvazia.
No fundo do duto de drenagem da cápsula, o metal reluz: encontro a Chave-Mestra dos Dutos de Ventilação que ela escondera.
**VICTOR VANE**: "Descanse em paz, Nora. A sua dívida com esta escola acabou."
> - 🔹 Escolha: *"[[INDIFERENÇA]] Deixar a cápsula intacta e recuar (-5 Humanidade)"*
Não posso me dar ao luxo de gastar meus próprios recursos ou vitae com uma aluna que já foi consumida pelo sistema.
**VICTOR VANE**: "Não posso intervir nisso agora. Seria suicídio."
**NORA (Prisioneira das Criptas)**: "...Não... Por favor... Não me deixe no escuro..."
Dou as costas para o cilindro de vidro enquanto as bolhas voltam a subir, abafando os sussurros de desespero da aluna.

---


### Encontro Social / Exploração: `encontro_mob_figurante`

👤 [[FIGURANTE ENCONTRADO]]: Você cruza o caminho de [nome_mob_atual].
🩸 [[FRENESI DE SANGUE CRÍTICO — SACIEDADE [fome_sangue]%%!]]:
As artérias no pescoço de [nome_mob_atual] pulsam como tambores ensurdecedores! O odor do sangue quente queima suas narinas e suas presas saltam involuntariamente!
🧠 [[FALHA NO TESTE DE AUTOCONTROLE!]] (Resistência Mental: [margem_autocontrole]%% vs Rolagem: [rolo_autocontrole])
A besta carmesim assume o comando absoluto dos seus membros! O verniz da razão desaba e você se lança sobre a presa em pleno corredor!
🧠 [[SUCESSO NO TESTE DE AUTOCONTROLE!]] (Resistência Mental: [margem_autocontrole]%% vs Rolagem: [rolo_autocontrole])
Cravando as unhas nas próprias palmas até verter sangue, você força a mente a sufocar o impulso predatório por alguns instantes! Mas a fome devoradora ainda ruge em suas têmporas...

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"💬 Conversar e sondar informações locais (+Conhecimento / +Intelecto)"*
[nome_mob_atual]" "\"[fala_mob_atual]\"
📘 Você conecta o relato às suas anotações (+1 Conhecimento Oculto / +1 Intelecto).
🕯️ Você memoriza a informação (+1 Conhecimento Oculto).
> - 🔹 Escolha: *"🧛 [[MORDIDA FURTIVA]] Hipnotizar/emboscar no ponto cego (Banquete Oculto / Absorver Natureza da Presa)"*
Você atrai [nome_mob_atual] para o vão escuro entre os pilares e crava as presas com cuidado na jugular, drenando o sangue com precisão predatória e apagando a memória recente da vítima com um choque hipnótico.
🩸 [_desc_banquete]
**EMÍLIA (Noviça Devota)**: "V-Victor?! O que... o que você acabou de fazer nas sombras com aquele colega?!"
**EMÍLIA (Noviça Devota)**: "Eu vi suas presas... e havia sangue no pescoço dele! O que você está escondendo de mim?!"
**ELARA (Presidente do Grêmio)**: "Alimentando-se em plena área comum como um parasita selvagem, Sr. Vane?!"
**ELARA (Presidente do Grêmio)**: "O Grilhão de Sangue cobra cada transgressão à ordem deste campus. Curve-se!"
⚡ O Grilhão de Sangue queima suas veias (-20 HP | +1 Punição do Grêmio)!
**MESTRA**: "Furtivo e contido, meu lacaio... Beber apenas algumas gotas para conter a sede. Poupa o rebanho, mas não sacia o apetite de um verdadeiro predador."
**VALÉRIA (Mercadora das Caldeiras)**: "Belo bote silencioso, Vane. Mas não vai deixar manchas no meu setor, ou vou cobrar taxa de limpeza na sua conta."
> - 🔹 Escolha: *"🩸 [[ATAQUE DE FRENESI!]] Drenar brutalmente até o fim (+65%% Sangue / +30%% Exposição / -8 Humanidade / Flagrante Grave)"*
Você desliza $80 para o bolso de [nome_mob_atual], que queima o boletim de ocorrência noturno (-20%% Exposição).
[nome_mob_atual]" "\"Sem dinheiro para o café, garoto? Circulando antes que eu te leve pra delegacia.\"
Seus olhos frios intimidam [nome_mob_atual], que entrega a carteira tremendo (+$[grana_extorquida] / +1 Domínio / -1 Humanidade).
> - 🔹 Escolha: *"🚶 Ignorar e seguir caminho"*

---


### Encontro Social / Exploração: `investigar_passo_bs`

O tempo deste período se esgotou enquanto você explorava os corredores.
Ao avançar pela penumbra da sala, você sente o aroma inconfundível de mirra e sangue antigo.
Seus passos ecoam pelo piso e você avista Emília organizando anotações de investigação.
Entre a fumaça e a luz baixa, Valéria apoia o cotovelo na bancada contando notas de dinheiro.
O som frio de saltos sobre o mármore anuncia a presença da Presidente Elara inspecionando o setor.

---


### Encontro Social / Exploração: `pista_ambiental_bs`

🕯️ [[PISTA DO CASO — A MULHER DE OITO PÉS (1/3)]]: Sob a névoa fria, você encontra pegadas de barro desproporcionais e galhos quebrados a quase três metros de altura. Um riso oco — 'Po... po... po...' — estremece o ar antes de sumir.
🕯️ [[PISTA DO CASO — A MULHER DE OITO PÉS (2/3)]]: Em uma lápide gótica rachada, você decifra um aviso entalhado: 'A aparição colossal persegue quem carrega sangue duplo. Ela não ultrapassa círculos consagrados com sal.' Pista registrada!
🕯️ [[PISTA DO CASO — A MULHER DE OITO PÉS (3/3)]]: Presa aos espinhos da grade, você recolhe a fita rasgada do chapéu de palha da assombração! A presença dela foi fixada no CEMITÉRIO DA NÉVOA à Noite!
🧪 [[PISTA DO CASO — O LOTE NECRÓTICO (1/3)]]: Perto da fornalha, você encontra bolsas de sangue vazias contendo um lodo esverdeado e borbulhante. O cheiro é de ácido sulfúrico e reagente clandestino.
🧪 [[PISTA DO CASO — O LOTE NECRÓTICO (2/3)]]: Atrás de um tonel de óleo, você acha uma fórmula manuscrita: 'Misturar solvente necrosado barateia a cota. Se os novatos enlouquecerem na fome, ninguém vai suspeitar.' Pista anotada!
🧪 [[PISTA DO CASO — O LOTE NECRÓTICO (3/3)]]: Manchas fosforescentes revelam o laboratório do Alquimista Renegado! O confronto decisivo está disponível nas CALDEIRAS!
🎹 [[PISTA DO CASO — A PARTITURA CARNAL (1/3)]]: Dentro de uma partitura sacra do século dezenove, você encontra a primeira folha de um réquiem antigo com tinta cor de ferrugem. O compasso faz seus ouvidos zumbirem.
🎹 [[PISTA DO CASO — A PARTITURA CARNAL (2/3)]]: Na estante de música, um registro diz: 'A melodia pré-diluviana de Lility só ressoa quando as três estrofes se juntam.' Suas veias pulsam em resposta.
🎹 [[PISTA DO CASO — A PARTITURA CARNAL (3/3)]]: Você recupera o movimento final do réquiem! A Partitura Carnal está completa para ser executada na SALA DE MÚSICA!
📜 [[PISTA DO CASO — OS ARQUIVOS MORTOS (1/3)]]: No arquivo do Ocultismo, você descobre que faltam 14 páginas do ano em que o sarcófago subterrâneo começou a verter sangue.
📜 [[PISTA DO CASO — OS ARQUIVOS MORTOS (2/3)]]: Um recibo secreto comprova repasses da diretoria humana para agentes da Inquisição comprarem o silêncio da polícia.
📜 [[PISTA DO CASO — OS ARQUIVOS MORTOS (3/3)]]: Você descobre a combinação do cofre de arquivos do Grêmio! Os documentos confidenciais estão acessíveis no SALÃO DO GRÊMIO à Tarde ou Noite!
🪞 [[PISTA DO CASO — O ESPELHO DA DAMA DO BANHEIRO (1/3)]]: Ao examinar a pia quebrada, a água pinga em tom avermelhado. No espelho trincado, você vê por um instante um reflexo loiro que não se move com você.
🪞 [[PISTA DO CASO — O ESPELHO DA DAMA DO BANHEIRO (2/3)]]: Atrás do cano enferrujado, você resgata um diário úmido: 'Ela sussurra do vidro quando a luz falha... Ela quer sangue de quem tem medo.' Pista registrada!
🪞 [[PISTA DO CASO — O ESPELHO DA DAMA DO BANHEIRO (3/3)]]: Você recupera o fragmento central do espelho! A entidade está pronta para se manifestar no BANHEIRO ABANDONADO!
🕯️ [[RUMOR DESCOBERTO]]: Dois estudantes cochicham ao longe sobre o banheiro interditado do segundo andar, onde o espelho trincado responde a quem chama pela 'Loira' à meia-noite.
🕯️ [[RUMOR DESCOBERTO]]: Um calouro jura ter visto a silhueta da Mulher Gigante de vestido branco rondando as lápides do cemitério à noite.
🔍 (OBSERVAÇÃO TÁTICA): Você nota inscrições rúnicas quase imperceptíveis gravadas no rodapé das paredes, reforçando a contenção da Máscara (+1 Conhecimento Oculto).
Apenas o som distante dos seus próprios passos e o cheiro de cera fria nos corredores... Nenhum perigo imediato.

---


### Encontro Social / Exploração: `emboscada_aleatoria_bs`

Um vulto ameaçador emerge da escuridão, mas ao avistar seus olhos carmesim de Predador puro e sua silhueta monstruosa, a criatura solta um ganido de pavor e recua para os dutos!
💰 Você vasculha os espólios do confronto e recupera $[recompensa_dinheiro]!

---

## PARTE V: NARRATIVAS DE PÓS-COMBATE, DRENAGEM E MORTE


### Batalha / Resolução: `loop_turno_combate`

**RETURN**: "vitoria_historia"
**RETURN**: "derrota_historia"

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"🗡️ Ataque Rápido (Corte Seco / Sem Custo)"*
O sangue litúrgico em suas veias incendeia a lâmina contra a abominação! (+15 Dano Sagrado)
Você avança com um corte preciso em [nome_inimigo]! (-[dano_rapido] HP)
Suas veias fervem em chamas carmesim!
Você rasga [nome_inimigo] com ferocidade inumana! (-[dano_garras] HP)
O arco voltaico explode no peito de [nome_inimigo]! Ele perde o turno de ataque!
Você estanca os cortes mais profundos às pressas! (+30 HP)
Você aplica a gaze embebida em pó de prata e giz! As feridas fecham sob uma suave fumaça azulada. (+40 HP)
A agulha pneumática estala contra seu braço! O mundo desacelera e seus reflexos atingem o ápice.
Você engole a dose fria de sangue filtrado... A sede recua temporariamente. (+35%% Saciedade)
Suas forças se esvaem enquanto você tenta rastejar pelas sombras...
Você recua pelas sombras sofrendo um corte de raspão!
**RETURN**: "fuga"

---


### Batalha / Resolução: `inimigo_ataca_por_tempo`

Você hesitou na mira! A hesitação custa caro na Zona Vermelha!

---


### Batalha / Resolução: `turno_do_inimigo`

Graças ao estimulante rúnico, você prevê a trajetória do ataque e se esquiva no último milissegundo!
[nome_inimigo] contra-ataca com ferocidade brutal! (-[_dano_final] de HP | Mitigado por [_def_total] de Defesa)

---


### Batalha / Resolução: `executar_golpe_critico_persona`

A postura de [nome_inimigo] quebrou completamente! Ele desaba de joelhos, ofegante e desarmado diante de você.

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"🩸 Predador em Movimento (Finalização Sanguínea / Menu de Drenagem)"*
Você avança sobre a presa vulnerável com instinto predatório implacável!
> - 🔹 Escolha: *"💥 All-Out Attack (Massacre Impiedoso / +Ressonância / Dano de Área)"*
Você e as sombras do corredor convergem em uma sequência avassaladora de estocadas e garras, pulverizando a resistência do alvo!
**RETURN**: "vitoria_all_out"
> - 🔹 Escolha: *"💰 Extorquir & Intimidar (Cobrar Resgate em Créditos e Suprimentos)"*
Você encosta a lâmina fria na garganta de [nome_inimigo]. Sem hesitar, ele esvazia os bolsos e entrega suas provisões antes de rastejar para o escuro.
**RETURN**: "vitoria_extorquiu"

---


### Batalha / Resolução: `pos_combate_drenagem`

O golpe final quebra a postura do adversário! [nome_inimigo] desaba de joelhos, subjugado.
A forma de [nome_inimigo] começa a se desfazer em poeira rúnica.

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"🔮 Absorver Essência Mística (+1 Ressonância)"*
O sangue pré-diluviano em suas veias consome a energia residual do guardião!
**RETURN**: "vitoria_absorveu"
> - 🔹 Escolha: *"🚶 Deixar os restos e avançar"*
**RETURN**: "vitoria"
O cheiro metálico de sangue quente inunda o ar do corredor... Sua garganta queima com a Fome incontrolável de Ghoul.
(O inimigo está caído à sua mercê... O sangue chama como um tambor no seu crânio. Drenar ou conter?)

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"🧛 Drenar o Sangue de [nome_inimigo] (+Sangue / +Poder / -Humanidade)"*
Você crava as presas no inimigo caído, sugando a essência vampírica dele!
⚠️ (+40 Fome de Sangue | +2 Ressonância | -2 Humanidade | Elara sentirá o cheiro deste tabu!)
Você bebe o sangue denso e envenenado pela energia das catacumbas!
⚠️ (+35 Fome de Sangue | +3 Ressonância | -3 Humanidade)
Você se alimenta vorazmente do oponente caído, absorvendo sua vitalidade.
⚠️ (+50 Fome de Sangue | +1 Ressonância | -1 Humanidade | +15 Exposição na Máscara)
**RETURN**: "vitoria_drenou"
> - 🔹 Escolha: *"🛡️ Conter a sede e poupar o derrotado (+Humanidade)"*
Você força suas presas a recuarem e mantém o controle sobre a maldição.
**RETURN**: "vitoria_poupou"

---


### Batalha / Resolução: `morte_definitiva`

Você sucumbiu aos perigos dos corredores...

> **[DECISÃO DO JOGADOR]:**
> - 🔹 Escolha: *"Carregar um jogo salvo"*
> - 🔹 Escolha: *"Voltar ao menu principal"*

---


---

# PARTE VI: EXPANSÃO NARRATIVA CANÔNICA — AS FRONTEIRAS DO GRILHÃO, A COBAIA 31 E OS 18 CONFLITOS DE LORE

Esta seção consolida as grandes expansões narrativas e sistêmicas desenvolvidas para elevar o peso dramático, a reatividade psicológica e a coesão mitológica de The Hunger and the Hallways.

---

## 1. AS REGRAS CANÔNICAS CONSOLIDADAS

### 1.1 A Noite 1: O Ataque no Corredor e a Intervenção de Lility
Victor Vane não foi transformado no soalho da Sala de Música. Em sua primeira noite no campus, Victor foi atacado e quase dilacerado por **Nora Vasques (Alfinete 31)** em pleno corredor durante um surto violento de fúria hemolítica decorrente da corrupção de Cain.

Lility interveio e salvou Victor. Seu plano original era abrir o sarcófago nas catacumbas para que o Primogênito consumisse sua vitae, encerrando milênios de tédio e intrigas vazias. Mas ao ver Victor no chão, cravando as unhas nas lajes e lutando desesperadamente pela própria respiração, ela sentiu uma inveja visceral daquela chama humana autêntica de sobrevivência. Transformá-lo e alimentá-lo foi um capricho nascido dessa fraqueza, o qual ela mascara imediatamente com arrogância aristocrática defensiva: *"Naturalmente. Um lacaio vivo tem mais utilidade que um cadáver no carpete"*.

Antes que pudessem sair do corredor, a Presidente Elara von Weiss (filha do Grão-Duque da Casa von Weiss, a dinastia que financiou a Academia no século XIX sob o brasão do falcão de prata sobre a bigorna de ferro) e seus executores de casaco branco os encurralaram. Elara jogou na cara de Lility suas violações anteriores (quando a flagrou nas catacumbas ofertando seu sangue ao sarcófago, ato que Elara presumiu ser uma tentativa profana de se alimentar da tumba). Elara zombou de seu disfarce como **"Lyra von Blut"**, uma fidalga falida da Silésia com dote atrasado agindo com audácia descabida, e aplicou o **Grilhão de Sangue de Perímetro** para mantê-la na linha até a resolução do selo do Eclipse. Já confinada, Lility alimenta Victor com sua vitae e lhe entrega o propósito e as regras de sobrevivência.

### 1.2 O Segredo Cósmico de Cain
A Fundação Mantenedora, o Diretor Ambrósio e a Presidente Elara vivem na ilusão burocrática de que a tumba no subsolo guarda apenas um *"Espécime Antediluviano"* ou *"Vetor Primário de Classe 4"* — um fóssil energético que eles acreditam poder drenar e usar como reator biológico para alimentar as barreiras da escola. **Apenas Lility sabe a verdade:** quem dorme sob o castelo é **CAIN, O PRIMOGÊNITO**, o primeiro assassino e a raiz de toda a linhagem.

### 1.3 Nora Vasques (Cobaia 31): O Filtro Biológico Vivo
Quando Victor confronta Elara sobre o sumiço de Nora Vasques, Elara usa seu eufemismo gélido: *"Ela foi contida, Victor. Eu cuidei pessoalmente para que a fome não a alcance mais"*. 
A verdade brutal da Cripta Ancestral (`cripta_cofre`) é que Nora não está morta: ela está suspensa viva em uma cápsula cilíndrica de vidro âmbar, atuando como filtro biológico da revolta assassina do miasma de Cain.
Elara justifica sua decisão com frieza utilitária:
> *"Isso é conter? É sustentar a escola, Victor. Solta, ela dilaceraria doze estudantes por quinzena num frenesi cego... Alguém sempre paga a conta do sangue. Eu escolhi quem não tinha quem perguntasse."*
Romper a cápsula ou purgar o fluido para libertar Nora destrói o amortecedor rúnico, disparando um abalo sísmico imediato de **+15% na Ruína de Cain (`ruina_cain += 15`)**.

---

## 2. A ENFERMARIA SÃO CIPRIANO & DRA. CLARA VANCE

### 2.1 A Triagem Médica Reenquadrada
A Enfermeira Clara Vance já possuía o registro de sangue Rh-Nulo na ficha de matrícula do orfanato. O choque da triagem não é a descoberta do tipo sanguíneo, mas a **mutação cadavérica e vampírica**:
- A lanceta de prata extrai sangue que não coagula em contato com o ar ambiente.
- A temperatura dérmica está em 31°C (cadáver ambulante).
- Sob lâmpada de mercúrio e reagente, o sangue emite fosforescência dourada da vitae antiga.
- Clara diagnostica com terror: *"Você deveria estar em uma maca do IML, senhor Vane. Biologicamente, este tecido está morto!"*
- Victor resolve o impasse com suborno de $80 créditos para forjar "anemia ferropriva" ou hipnose clínica de Cain (-15% Fome, -15% Exposição).

### 2.2 Drenagem Furtiva da Enfermeira Clara & Consequências Reais
Ao realizar a Drenagem Furtiva na carótida de Clara, as penalidades refletem a gravidade do ato:
- -2 Humanidade, +3% Ruína de Cain, +10% Exposição.
- Clara entra em transe hipnótico dócil, mas anota episódios recorrentes de síncope inexplicável no prontuário, gerando vestígios que atraem auditorias forenses do Grêmio.

---

## 3. CATÁLOGO DOS 18 EVENTOS ORGÂNICOS DE CONFLITO DE LORE

### Evento 01: `ev_lility_fronteira_portoes` — "A Fronteira de Ferro & O Nome Esquecido"
- **Gatilho:** Noite | `portoes_praca` | Lility presente no perímetro interno.
- **Narrativa:** Victor chama Lility pelo nome público ("Lyra"). Ela demora a responder, vira-se lentamente com deboche e zomba: *"Ah... é assim que esses vermes de uniforme me chamam atualmente, não é? Quase esqueci."* Ela proíbe Victor de usar esse nome a sós, exigindo que a trate por Mestra, ou em momentos de intimidade, "Lili". Quando estende os dedos além do portão, as runas do Grilhão explodem em fogo carmesim nos pulsos.

### Evento 02: `ev_interceptacao_lility_ponto_cego` — "Predadora nas Sombras do Claustro"
- **Gatilho:** Noite | `patio_arvore` ou `biblioteca` | Lility presente.
- **Narrativa:** Lility puxa Victor bruscamente para trás de uma pilastra de pedra segundos antes da patrulha dos monitores passar com lanternas halógenas. Ela fareja o sangue vivo de Victor e exige o tributo da periferia.

### Evento 03: `ev_visita_noturna_lility_dormitorio` — "Vigília no Beliche à Meia-Noite"
- **Gatilho:** Noite | Entrar no Dormitório | Afeto de Lility >= 3.
- **Narrativa:** Lility está sentada na escrivaninha de Victor sob a luz da lua, lendo a folha pautada com as quatro regras de sobrevivência. Ela recorda a noite no corredor em que Nora o atacou e elogia a regra número quatro: *"Nunca se tornar descartável"*. Revela que a chama desesperada de vida de Victor a fez sentir inveja de um mortal.

### Evento 04: `ev_embate_noturno_lility_emilia` — "A Dama do Abismo e a Noviça da Luz"
- **Gatilho:** Noite | Lility e Emília coincidem no mesmo setor (`biblioteca` ou `patio_arvore`).
- **Narrativa:** Emília ergue o crucifixo e o breviário contra Lility, acusando-a de violar os tratados. Lility zomba da fé vazia da noviça. Victor precisa mediar a tensão mortal.

### Evento 05: `ev_negociacao_sombra_lility_valeria` — "A Cobrança no Pátio da Árvore"
- **Gatilho:** Pátio da Árvore (superfície) | Valéria entrega giz rúnico das catacumbas.
- **Narrativa:** Valéria sobe da fornalha cobrando 60 créditos pelo frete até a superfície, pois o Grilhão impede Lility de descer. Lility, quebrada financeiramente, ordena que Victor pague. Se Victor não tiver créditos, Lility o faz aceitar serviço braçal de limpeza nas caldeiras para saldar a dívida com Valéria.

### Evento 06: `ev_rastro_oculto_nora_enfermaria` — "O Eufemismo da Contenção #31"
- **Gatilho:** Tarde/Noite | Vasculhar a Enfermaria com Clara distraída.
- **Narrativa:** Victor descobre a guia interna de remessa para a Cripta Ancestral. O documento revela a verdade: Nora foi confinada na cápsula porque sua revolta no sangue dilaceraria 12 estudantes por quinzena.

### Evento 07: `ev_c01_janela_lility` — "A Janela Aberta no Dilúvio & O Lapso do Passado"
- **Gatilho:** Noite | Sala de Música sob tempestade torrencial.
- **Narrativa:** Diante dos trovões, Victor comenta as pesquisas de Emília sobre a queda dos vampiros antigos. Lility comenta como testemunha ocular viva (*"Os templos cheiravam a cinzas úmidas e mirra barata..."*). Ao notar seu próprio lapso, dá um sorriso sedutor e enganador: *"Esqueça o passado, Victor. O presente tem sangue fresco esperando por nós."*

### Evento 08: `ev_c02_triagem_enfermaria` — "A Triagem da Campanha de Saúde"
- **Gatilho:** Manhã/Tarde na Enfermaria com Emília ciente de sua natureza.
- **Narrativa:** Clara Vance aplica a lanceta e descobre que o sangue não coagula e resplandece em ouro sob luz de mercúrio. Suborno ou hipnose médica para proteger o segredo.

### Evento 09: `ev_c03_divida_teo_corredor` — "A Segunda Parcela do Termo 112"
- **Gatilho:** Manhã/Tarde nos corredores com DOOM >= 10%.
- **Narrativa:** Teo é prensado nos armários pelos fiscais que exigem sangue forçado. Victor intervém com dinheiro ($80), intimidação predatória ou omissão covarde.

### Evento 10: `ev_c05_voce_nao_come` — "'Você Não Come'"
- **Gatilho:** Refeitório com Emília analisando o caderno de anotações.
- **Narrativa:** Emília confronta Victor com dados clínicos: ele não ingere alimentos sólidos há quatro dias, mas sua força muscular dobrou. Teste psicológico da Máscara de Humanidade.

### Evento 11: `ev_c06_lista_rh_nulo` — "Tabela de Afinidade com o Espécime Alfa (Protocolo 1898)"
- **Gatilho:** Sala de alquimia desativada com Emília.
- **Narrativa:** Emília mostra a lista histórica de 41 cobaias testadas pelo Conselho. Nora Vasques é a #31 (ressonância 88%) e Victor Vane encabeça a lista como #41 (catalisador puro de 99.8%). O documento não cita o nome de Cain, preservando o mistério cósmico.

### Evento 12: `ev_c08_escuta_decreto_elara` — "A Escuta do Decreto de Elara"
- **Gatilho:** Porta da Sala de Música com DOOM >= 15%.
- **Narrativa:** Elara repreende Lility com tom gélido e burocrático sobre a presença de Lility na tumba, cometendo o erro de achar que a vampira queria se alimentar do Espécime Alfa. Lility debocha da cegueira científica da presidente.

### Evento 13: `ev_c12_relatorio_odores_elara` — "O Relatório Olfativo da Presidência"
- **Gatilho:** Gabinete do Grêmio com Exposição ou Suspeita elevada.
- **Narrativa:** Elara lê o memorando olfativo dos monitores farejadores (cheiro de lírios de Lyra, graxa de Valéria e mirra de Emília). Propõe transformar Victor em seu agente duplo remunerado.

### Evento 14: `ev_c15_fome_sem_plateia_valeria` — "Fome sem Plateia nas Caldeiras"
- **Gatilho:** Caldeiras em estado de fome crítica (< 30%).
- **Narrativa:** Valéria acolhe Victor tremendo diante da fornalha, arregaça a manga de couro e concede exatamente três tragos na veia para salvar sua vida do frenesi.

### Evento 15: `ev_c16_investigacao_genealogica_lyra` — "Quem é Lyra von Blut?"
- **Gatilho:** Biblioteca | Tarde/Noite | DOOM >= 30%.
- **Narrativa:** Victor e Emília pesquisam o Livro de Ouro da Nobreza da Baviera e Silésia. Emília desdenha do sobrenome óbvio (*"Von Blut... que sobrenome pretensioso para esconder falta de terras"*). Descobrem que a linhagem não existe e encontram anotações medievais em aramaico sobre uma senhora imortal chamada "Lili...".

### Evento 16: `ev_c17_inundacao_agua_negra` — "O Dilúvio do Miasma"
- **Gatilho:** Caldeiras ou pátios inferiores | DOOM >= 60%.
- **Narrativa:** A água fétida e negra da tumba regurgita pelos ralos das galerias de serviço, queimando as solas dos sapatos como ácido fraco. Victor e Valéria arriscam o corpo na válvula mestra de exaustão para impedir o colapso do dormitório.

### Evento 17: `ev_c18_vigilia_executores_sombra` — "A Vigília dos Executores de Choque"
- **Gatilho:** Pátios ou corredores nobres | Noite | DOOM >= 70%.
- **Narrativa:** Elara decreta Lei Marcial. Sentinelas de sobretudos blindados brancos e máscaras de ferro com fendas de quartzo patrulham com cães farejadores e rifles de prata. Victor precisa usar furtividade ou sombras para não ser capturado.

### Evento 18: `ev_c19_laudo_sincope_clara` — "A Auditoria Forense de Clara Vance"
- **Gatilho:** Enfermaria | Tarde/Noite | DOOM >= 50% ou após drenagem de Clara.
- **Narrativa:** A junta médica central requisita os prontuários de Clara Vance devido a suas crises de síncope e laudos anômalos. Victor e Clara precisam invadir o arquivo morto para queimar os papéis ou forjar lâminas de sangue no centrifugador.

---

## 4. OS FINAIS CANÔNICOS DEFINITIVOS (`evt_d21_noite`)

Todos os 5 desfechos reais do clímax em `script.rpy` (linhas 4841–5215), após o combate contra **Cain, O Progenitor Faminto** (450 HP / 42 ATK / QTE 3.0s) e o resgate de Lility no vórtice do Relicário:

1. **Final A — Consorte Imortal (A Nova Dinastia Carmesim):** *Sempre disponível.* Victor e Lility cravam as mãos simultaneamente no peito de Cain, **drenam** sua vitae pré-diluviana divina e ascendem juntos ao trono da noite eterna sob o eclipse permanente.
2. **Final B — Quase Humano (O Peso da Liberdade):** *Requer `ritual_corte_vinculo_desbloqueado`.* Com a ajuda de Emília e o Ritual do Corte, Victor quebra o selo do Relicário sem crueldade; Lility encontra o descanso sagrado em cinzas de luz dourada, fechando a fenda de Cain, e Victor recupera seu batimento cardíaco humano sob o sol da manhã ao lado de Emília.
3. **Final C — A Configuração do Lamento (Todos Sobrevivem, Todos Perdem):** *Requer `ritual_corte_vinculo_desbloqueado`.* No estertor de Cain, um espinho calcificado atinge o peito de Emília enquanto ela protege Victor; em pânico, Victor a transforma com sua própria vitae e inverte os glifos do Relicário para arrancar a imortalidade de Lility — salvando ambas, mas condenando Emília à noite que ela abomina e Lility à mortalidade frágil sob sua guarda.
4. **Final D — A Última Transação (Sobreviventes do Submundo):** *Requer `afeto_valeria >= 1`.* Victor e Valéria abandonam o colégio antes do desabamento total, escapando de furgão pelos túneis de drenagem das caldeiras com o estoque de vitae purificada e tecnologia arcana para comandar o mercado fora da jurisdição da Fundação e dos Inquisidores.
5. **Final Secreto E — A Harmonia Proibida (O Coven das Quatro Soberanas):** *Requer Afeto 8+ com TODAS as quatro heroínas (`afeto_mestra`, `afeto_emilia`, `afeto_valeria`, `afeto_elara` >= 8) e `humanidade >= 40`.* Em formação pentagonal ao redor do Relicário, Lility (sangue ancestral), Emília (rosário sagrado), Valéria (condutores arcanos das caldeiras) e Elara (cetro do Conselho decretando a dissolução das castas) selam a fenda sem sacrifícios, instaurando meses depois um novo conselho de coexistência sob doação contratual.
6. **Game Over / Derrota (`morte_definitiva`):** Disparado caso Victor caia diante de Cain em `evt_d21_noite` ou chegue a 0 HP / colapso absoluto nos turnos de exploração.

---

# PARTE VII: SISTEMAS SOCIAIS, ZONA SEGURA DO DORMITÓRIO, ENFERMARIA & MICRO-EVENTOS DA LIVE BUILD

Para manter a consistência entre o roteiro literário (Partes II–VI) e a jogabilidade atual em `custom_screens.rpy`, o Ato I em diante opera sobre quatro camadas emergentes integradas:

## 1. Zona Segura do Dormitório (`dormitorio` — 0 Passos de Combate)
O Dormitório de Victor (`custom_screens.rpy`, L8107–8489) funciona como santuário narrativo inviolável: não possui botão **"Dar 1 Passo"** nem emboscadas aleatórias, abrigando em vez disso o **Relatório Tático (4 Regras de Sobrevivência)**, o descanso escalonado e a convivência privada com heroínas presentes no turno:

- **Descanso Escalonado (`acao_descansar_dormitorio`):** Conforme os passos restantes no período (`_p_rest`), recupera `+35 HP / -15% Exposição` (3 passos restantes, 100% chance de curar 1 sequela), `+22 HP / -10% Exposição` (2 passos, 65% de cura de sequela) ou `+12 HP / -5% Exposição` (1 passo). Em fome crítica (`< 25%`), a regeneração cai pela metade; dormir em noites de `toque_recolher` confere +5 Humanidade extra.
- **Vigília Cruzada (Emília & Lility Juntas):** Caso `loc_emilia == "dormitorio"` e `loc_mestra == "dormitorio"` ao descansar no Dormitório, o jogo dispara automaticamente o evento **`evento_embate_dormitorio_lility_emilia`** (L8394–8489), com 4 caminhos políticos/afetivos para Victor resolver o atrito entre o crucifixo de Emília e a presença da Mestra no leito:
  1. Apoiar Emília e invocar os limites do Grilhão.
  2. Apoiar Lility e lembrar que disparos de fé alertarão inspetores.
  3. Impor autoridade absoluta de dono do quarto.
  4. Pacificação improvável dividindo a caneca de chá entre ambas.
- **Convivência Individual (com comentários de terceiras se a rival estiver presente):**
  - **Emília (`menu_encontro_emilia_dormitorio`):** Chá de camomila e mirra (1x/turno), tratamento direto de feridas/sequelas com Gaze Consagrada, confissões sobre o Conselho e Lorde Phillip, cena íntima/tensa de autocontrole quando `fome_sangue < 25`, e avanço de marco (`estagio_emilia`).
  - **Lility (`menu_encontro_lility_dormitorio`):** *Transe Noturno & Aconchego Carmesim* no leito, *Comunhão de Sangue na Escuridão* (aplacador de sede se `fome_sangue < 35`), análise estratégica das fraquezas do Conselho/ronda, e avanço de marco (`estagio_mestra`).

## 2. A Enfermaria e a Dra. Clara Vance (`enfermaria` — Piso Superior)
Mapeada como pin autônomo na Superfície (`custom_screens.rpy`), a Enfermaria abriga a hematologista **Dra. Clara Vance (`mob enfermeira`)**:
- **Dispensa Clínica com Ágio Oficial:** Compra de **Bolsa de Sangue Filtrado ($165, 1x/dia)**, **Kit de Primeiros Socorros ($105, 1x/dia)** e **Tratamento de Sequela Física / Sutura ($140)**. O ágio alto foi desenhado intencionalmente para tornar o desbloqueio do Mercado Negro nas Caldeiras uma conquista financeira marcante. Inadimplência na taxa acadêmica (`taxa_inadimplente`) aplica sobretaxa de `+25%` nos preços e reduz a remuneração de hemograma em `20%`.
- **Doação de Sangue Rh-Nulo (`+$90` | `-15 HP` seguro `>= 15` | `+10% Exposição`):** Vender o próprio "Sangue Dourado" à Fundação gera créditos rápidos (1x/dia), mas alimenta os arquivos do Conselho.
- **Drenagem Furtiva & Hipnose Pós-Mordida:** Se `fome_sangue < 70`, Victor pode encurralar Clara junto à bancada (`+30% Saciedade | +20 HP | +1 Intelecto | -2 Humanidade | +10% Exposição | +3% DOOM` interno), selando a memória dela com o **Transe Hipnótico** (1x/dia).

## 3. Os 6 Micro-Eventos Aleatórios de Exploração (`micro_evento_ito_corredor`)
Durante o passo de investigação em setores perigosos (`custom_screens.rpy`), os encontros estilo *World of Horror* sorteiam uma de seis vinhetas táticas:
1. **`professores_trancada` (A Sala dos Professores Trancada):** Arrombamento por **Intelecto (D10)** (`+$140` e `+1 Conhecimento Oculto` ou `+15% Exposição`), espreita com **Visão Predatória** (`-5% Saciedade`, `+2 Conhecimento Oculto`), ou recuo.
2. **`gravador_k7` (O Gravador K7 no Clube de Ocultismo):** Escutar ladainhas pré-diluvianas (`+3 Conhecimento Oculto | +3% Ruína`), destruir a fita no fogo (`+5 Humanidade`), ou vendê-la a Valéria (`+$100`).
3. **`dutos_contrabando` (Entrega Clandestina nos Dutos):** Intimidação por **Coragem (D10)** (`+1 Absinto | +$80` ou `+15% Exposição`), chantagem direta (`+$120 | +8% Exposição`), ou evasão.
4. **`capela_esquecida` (A Capela Antiga Subterrânea):** Prece sobre o solo sagrado (`+10 Humanidade | -10 HP` por queimadura vampírica), decifrar lápides por **Conhecimento Oculto (D9)** (`+2 Conhecimento Oculto`), ou saquear o altar (`+1 Giz | +1 Gaze Consagrada`).
5. **`espelho_trincado` (O Reflexo Distorcido no Corredor):** Inspeção por **Sensibilidade Sobrenatural (D10)** revelando Elara no cofre (`+2 Conhecimento Oculto` ou `-8 HP`), quebrar o espelho (`-6% Ruína | +12% Exposição`), ou desviar o olhar.
6. **`manuscrito_biblioteca` (O Manuscrito Esquecido de 1890):** Decifrar fórmulas rúnicas por **Intelecto (D10)** (`+2 Conhecimento Oculto | +1 Domínio`) ou purificar as folhas com 1x Giz de Proteção (`-5% Ruína`).

## 4. Ecossistema de Rua: 26 Inimigos de Combate & Hold-Up
Nas varreduras de corredores (`sorteio_mob 1..26` em `custom_screens.rpy`), o bestiário cruza quatro facções com sistema **Hold-Up** à moda de *Persona 5* (Negociação/Suborno, Drenagem/Golpe Rápido ou Extorsão de Créditos/Sangue ao derrubar inimigos vulneráveis): **Grêmio & Executores** (Duelistas, Executor da Lâmina Branca, Executores Espada Solar/Lâmina Negra/Machado/Adaga, Inquisidor Tático), **Fundão** (Alquimista Renegado, Mecânico Pesado, Capanga de Escopeta), **Corrompidos & Aberrações** (Marionete de Fios de Sangue, Hellhound, Rivals Ghouls, Ghoul Garota, Colegial das Teias, Besta Urso Acorrentado, Abominação Sombra do Pesadelo) e **Construtos Inorgânicos** (Esqueletos Rúnicos Nobre/Colegial, Gárgula de Pedra Dragão).

## 5. Mercado Negro de Valéria & Vitrine Rotativa Clandestina
Nas Caldeiras Centrais (`menu_loja_valeria_loop`), Valéria opera o comércio do submundo com economia balanceada:
- **Estoque Essencial:** 1x Bolsa Filtrada ($120 com sistema de Fiado caso sem fundos, pagável em 2x Sucata) e 1x Kit Curativo ($70).
- **Vitrine Rotativa de 5 Slots (`sortear_vitrine_mercado_negro`):** Sorteio diário único entre 19 itens (Suprimentos, Contrabando Tático, Lote Raro com variância de preço e Presente de Luxo).
- **Risco Policial:** 30% de chance diária de fechar até o Dia 10 para despistar rondas. Desconto de 10% por confiança (`afeto >= 6`).

## 6. Cobrança da Taxa Acadêmica & Gestão de Inadimplência
A cada **6 períodos (2 dias completos)** a partir do Dia 3, a tesouraria do Conselho aciona `evento_cobranca_taxa_academica`:
- **Valores:** `$135` se houver dívida de monitores pendente (com abatimento direto) ou `$100` cota padrão.
- **Alternativas:** Pagamento integral à vista, cessão de sangue (-15 HP seguro) ou inadimplência controlável. A inadimplência aplica a sequela `taxa_inadimplente`, penalizando o atendimento na enfermaria e gerando juros no Livro de Dívidas.
- **Notificação:** Recibos gerados via `notificar_rpg` / `th_notificar_recibo`.

## 7. Sistema Social de Presentes & Preferências das Heroínas
Disponível em `fluxo_entregar_presente_heroina` (1x/dia por heroína):
- **Itens:** Buquê de Lírios Negros ($85), Perfume Âmbar & Sândalo ($135), Colar de Prata & Granada ($175), Lenço de Seda Nobre ($220) e Anel de Prata Entalhado ($260).
- **Reações:** Lility fascina-se por símbolos imortais e fragrâncias raras; Elara aceita joias finas com decoro aristocrático; Emília emociona-se com simplicidade sincera mas teme culpa moral; Valéria calcula valor comercial e aprecia peças úteis de contrabando.

## 8. Figurantes (Mobs) & Variedade Vocal de Corredor
- **17 Mobs Temáticos:** Calouros assustados, veteranos do contrabando, ocultistas de dark academia, professores exaustos e policiais corruptos.
- **Listas Múltiplas por Ato:** `MOBS_LORE_DATABASE` com 3 falas temáticas para o Ato 1, e variações progressivas para os Atos 2 e 3, sorteadas aleatoriamente em `sortear_mob_por_local`.
- **Desacoplamento Vocal:** Canal `barks` dispara `th_bark_mob("abordagem")` ao avistar o figurante e `th_bark_mob("conversa")` ao dialogar, sorteando entre `_conversa_1.ogg` e `_conversa_2.ogg` geradas via Gemini TTS (118 faixas ativas).

