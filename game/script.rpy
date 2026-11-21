# ==============================================================================

# SCRIPT.RPY — REESTRUTURADO POR SLOTS (DIA x PERÍODO)

# Cada bloco 'evt_dNN_periodo' é UM período de história. Nenhum bloco define

# dia_atual/periodo: quem controla o relógio é o calendario.rpy.

# Para adicionar uma cena nova: crie um label evt_dNN_periodo e registre em

# calendario_eventos (calendario.rpy). Slots sem evento viram exploração livre.

# ==============================================================================

# ==============================================================================

# ATO I — O CUSTO DA ENTRADA E O PACTO DE SANGUE (DIAS 1 E 2)

# ------------------------------------------------------------------------------

# Eixo temático: a escola não prende ninguém — ela faz todo mundo DEVER.

#   • Regras de Victor  : o credo que ele escreveu após a traição do mentor.

#   • Livro de Dívidas  : cada favor e ajuda aceita vira uma cobrança pendente.

#   • Boatos e Rumores  : o que os alunos sussurram alimenta as anomalias noturnas.

# ==============================================================================

# ==============================================================================

# DIA 1 — MANHÃ: A CHEGADA E AS QUATRO CLÁUSULAS

# ==============================================================================

label evt_d01_manha:

    # ---- ABERTURA A FRIO: O sonho enigmático com a Mestra e a pergunta crucial --------

    scene black

    stop music fadeout 0.5

    $ th_sfx("heartbeat")

    $ th_voz("climax/lility_climax_01_sonho")

    voz_na_escuridao "Responda sem pensar, Victor.{w=0.6} Você quer me salvar porque se importa comigo...{w=0.8} ou porque não suporta a ideia de ficar sozinho outra vez?"

    # Sonho / Premonição do protagonista — Fundo animado que reproduz apenas uma vez

    scene bg animado inicio sonho premonicao with dissolve

    "O chão pulsa. Não como terremoto — mais como coração. Batida por batida, o cascalho sob meus pés absorve o impacto e devolve."

    "A fumaça carmesim desce do céu rasgado em filamentos. E ali, no centro de tudo que está pegando fogo, uma mulher de pé em silêncio."

    "Cabelos do tom de vinho que secou. Boca fechada. Olhos que olham atravessando a pele — como se o que ela quisesse examinar ficasse atrás das costelas."

    "O cheiro chega antes do nome. Mirra. Ferro velho. Algo mais fundo que ferro."

    "Eu abro a boca. O som não sai. A fumaça fecha."

    # Transição para tela preta marcando o fim do pesadelo e o despertar

    scene black with fade

    $ th_sfx("heartbeat")

    "Eu sempre fui bom com contas. Quanto custa. Quanto eu devo. Quanto sobra."

    "Mas existem perguntas que não cabem em coluna nenhuma. E a sensação mais estranha de todas... é que aquele delírio não parecia memória. Parecia um aviso."

    # ---- CENA 1: DESPERTAR DO PESADELO REPETITIVO COM LILITY ----------------

    scene cena victor pesadelo 1 with dissolve

    play sound "audio/heartbeat.ogg"

    $ th_bark("victor", "acordar")

    "Acordo com a palma da mão espalmada contra a madeira do beliche. O quarto escuro. A cama fria do lado de fora do cobertor."

    "Ela estava lá de novo. Lágrimas escorrendo sem choro — sem convulsão, sem soluço — direto pela bochecha pálida, como se chorar fosse para ela o mesmo que respirar é para mim. Natural. Inevitável."

    "E os lábios se moviam. Sempre se movem. Eu nunca ouço."

    # Transição para reflexão pós-pesadelo

    scene cena victor pesadelo 2 with dissolve

    "Esfrego o rosto com o dorso da mão. A pele da bochecha está fria — suor que já secou."

    "Olho para o teto do beliche. Quinta noite com aquela mulher de cabelos cor de sangue. Talvez sexta. Parei de contar."

    "Levanto. O chão do quartinho de pensão range sob o peso. Dobro o cobertor com um cuidado idiota para a hora e fico parado diante da vidraça embaçada pela chuva da madrugada."

    "A chuva escorre pelo vidro... e o eco daquela sala fechada volta sem pedir licença. Não como memória inteira: como um corte que ainda sangra."

    # ---- FLASHBACK CONTIDO: A COAÇÃO E A ASSINATURA -------------------------

    scene cena passado victor 10 with dissolve

    "A mão direita ainda lembra do peso daquela caneta barata de metal."

    "Uma sala sem janelas no centro da cidade. Cheiro de café velho, fumaça de cigarro e o zumbido monótono de uma lâmpada fluorescente."

    "Um termo de confissão e transferência forçada empurrado sobre o fórmica da escrivaninha. Do outro lado da mesa, homens de terno impecável sorrindo enquanto esperavam a minha capitulação."

    "Eu assinei. A mão tremendo, os nós dos dedos ainda esfolados. Assinei para não ser trancado numa cela comum antes dos vinte anos... e porque a única pessoa por quem eu teria colocado a mão no fogo abaixou a cabeça, olhou para o chão e deixou que a culpa caísse inteira sobre os meus ombros."

    "Ali morreu a minha ingenuidade. Foi ali que entendi que estender a mão para salvar alguém só serve para colocar a corda no seu próprio pescoço."

    # ---- RETORNO AO PRESENTE E A PARTIDA -----------------------------------

    scene cena victor pesadelo 2 with dissolve

    "Afastei a mão da vidraça da pensão. O passado é uma dívida que já paguei caro demais."

    "Apenas uma instituição aceitou minha matrícula depois que a ficha disciplinar foi manchada: a Academia São Cipriano. Não por compaixão — lugares aristocráticos não sabem o que é compaixão —, mas porque o formulário médico do vestibular destacou em amarelo uma anomalia rara no meu hemograma."

    "Rh Nulo. Sangue Dourado. Um caso a cada seis milhões."

    "Hoje eu recomeço do zero. Quatro regras escritas a lápis no bolso do casaco. E a promessa irrevogável de nunca mais virar descarte."

    # ---- CENA 2: NO TREM-BALA RUMO À CAPITAL --------------------------------

    scene cena victor trem bala with fade

    $ th_musica("Safe_Within_the_Blue", 2.0)

    "Os trilhos magnéticos não fazem barulho. Esse é o detalhe que me incomoda mais do que devia."

    scene cena victor trem carta janela with dissolve

    "Pela janela, os campos viram viadutos de concreto cinzento. A metrópole gótica surge no horizonte entre as nuvens baixas."

    scene cena victor trem lendo carta with dissolve

    "Tiro a carta de recomendação de dentro do casaco. O papel está gasto nas dobras de tantas vezes que o reli durante a noite. No anexo médico, as duas palavras sublinhadas com precisão clínica: {i}Rh Nulo / Sangue Dourado{/i}."

    "Eles sabem o que querem de mim. Agora preciso descobrir o que vou arrancar deles para continuar inteiro."

    # ---- CENA 3: DIANTE DOS PORTÕES DA ACADEMIA -----------------------------

    scene cena victor portoes academia with fade

    $ th_cartao(1, "Manhã")

    "Os carvalhos terminam. Os portões começam."

    "Ferro batido, três metros de altura, ponteiros em forma de lanças. Uma gárgula no pilar esquerdo com a boca aberta na direção de quem chega — não em ameaça: em aviso."

    "No prospecto acadêmico que recebi pelo correio, havia uma foto dos portões com filtro de luz dourada e o slogan 'Excelência que Dura Gerações'. Agora, de perto, sem filtro, eles parecem o que são: um portão que fecha por dentro."

    call screen th_regras_victor

    "Quatro linhas a lápis. Não são promessas — promessas eu já quebrei. São contabilidade."

    "Atravesso."

    # ---- O CORREDOR E EMÍLIA: O QUADRO DO FUNDADOR ---------------------------

    scene cena victor quadro fundador 1 with dissolve

    "O segundo andar tem vitrais demais e placas de menos. Passo pela primeira vez por um corredor largo e silencioso, ladeado por pesadas molduras douradas."

    "Uma tela a óleo em particular domina a parede leste: o retrato solene de um aristocrata de casaca preta e barba aparada, com olhos penetrantes que parecem esculpidos em âmbar. A plaquinha de latão na base diz apenas: {i}O Fundador{/i}."

    scene cena victor quadro fundador 2 with dissolve

    "Paro diante dele. A pintura tem um brilho oleoso e denso sob a luz que corta os vitrais. Não é apenas antiga; o verniz parece espesso, vivo, como se as pinceladas guardassem uma respiração reprimida sob o linho."

    "Desvio o olhar. A regra três diz que nunca serei o último a saber. A regra não diz como. Eu poderia perguntar a alguém onde fica a secretaria, mas perguntar é admitir que outra pessoa sabe mais do que eu."

    scene cena victor quadro fundador 3 with dissolve

    "Então dou a volta pela ala oeste, conto os passos e tento me orientar pelos arcos de pedra. Quinze minutos depois, as mesmas tapeçarias carmesins, as mesmas portas fechadas... e a mesma parede."

    "Passo novamente diante da tela a óleo. O Fundador ainda está lá."

    scene cena victor quadro fundador 4 with dissolve

    "Mas quando dou três passos à frente, sinto um arrepio gélido subir pela nuca — a sensação física, inconfundível e nauseante de estar sendo observado."

    "Travo os calcanhares e giro o pescoço para trás."

    "Tenho certeza absoluta de que, na primeira volta, as pupilas dele apontavam em direção à janela. Agora... elas estão cravadas diretamente na altura do meu peito, acompanhando cada milímetro do meu movimento."

    "O ar ao redor da moldura parece ter caído cinco graus. Um cheiro sutil de terebintina e ferro velho paira no linho."

    scene cena victor emilia susto 5 with vpunch
    $ th_sfx("heartbeat")

    $ th_bark("emilia", "padrao")

    $ th_voz("climax/emilia_climax_01_quadro")
    emilia "Ele gosta de você."

    "Dou um solavanco para trás, o coração disparando contra as costelas!"

    scene bg animado corredor academia cortina sol with dissolve

    show expression obter_sprite_victor("surpreso") as victor at sprite_esquerda with dissolve

    show emilia uniforme sorriso amigavel meio corpo at sprite_direita with dissolve

    protagonist "...Pelos céus! De onde você surgiu?!"

    show expression obter_sprite_victor("pensando") as victor at sprite_esquerda with dissolve

    emilia "Da biblioteca. Eu vi você passar da primeira vez pela fresta da porta."

    emilia "E o Fundador... quase ninguém encara essa moldura três vezes seguidas. Costuma ser sinal de que a pessoa está completamente perdida procurando a secretaria."

    show expression obter_sprite_victor("falando") as victor at sprite_esquerda with dissolve

    protagonist "Eu não estou perdido. Estou fazendo um reconhecimento da planta da escola."

    show emilia uniforme calma meio corpo at sprite_direita with dissolve

    emilia "Dando voltas no mesmo corredor há vinte minutos?"

    show expression obter_sprite_victor("sem_jeito") as victor at sprite_esquerda with dissolve

    protagonist "É um método de eliminação."

    "Ela ri pelo nariz, baixinho, como quem tenta não ser pega rindo. Há olheiras discretas sob os óculos. Quem dormiu pouco reconhece quem dormiu pouco."

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    protagonist "E sobre esse quadro... Eu juraria que o ângulo do olhar dele mudou entre a primeira e a última volta."

    show emilia uniforme ajeitando oculos meio corpo at sprite_direita with dissolve

    "O sorriso complacente de Emília murcha aos poucos. Ela ajeita os óculos redondos e olha de soslaio para a enorme pintura do Barão Cipriano."

    emilia "Não diga isso muito alto pelos corredores, calouro. Mas... você não é o primeiro a notar."

    show emilia preocupada at sprite_direita with dissolve

    emilia "Os quadros desta escola... sempre foram meio estranhos."

    emilia "A administração jura que é apenas a perspectiva do claro-escuro barroco. Mas meu tio-avô, que estudou aqui nos anos sessenta, contava que algumas telas foram encomendadas com misturas alquímicas de pigmentos que reagem à umidade e ao calor dos corpos."

    emilia "Outros alunos juram que ouviram murmúrios abafados vindo das molduras da galeria leste tarde da noite, logo antes do toque de recolher."

    show emilia uniforme seria triste meio corpo at sprite_direita with dissolve

    emilia "Dizem que quem passa tempo demais encarando os retratos antigos acaba perdendo o rumo dos corredores... ou esquecendo de voltar para o dormitório."

    emilia "Por via das dúvidas: se você andar por aqui à noite, nunca responda se alguma pintura parecer sussurrar na sua direção."

    "Ela me dá esse conselho com um tom de voz que não parece folclore estudantil. Parece aviso de sobrevivência."

    show emilia uniforme corada timida meio corpo at sprite_direita with dissolve

    emilia "Não é vigiar. É... eu anoto as coisas. É um hábito. Emília von Karsten."

    show expression obter_sprite_victor("neutro") as victor at sprite_esquerda with dissolve

    protagonist "Victor Vane."

    emilia "Eu sei."

    "Duas palavras, e o corredor parece ficar mais estreito."

    emilia "A sua pasta de transferência estava na mesa da recepção hoje cedo. Bolsista integral, vindo do interior, notas máximas. E nenhum pedido de monitoria."

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    protagonist "Você lê a pasta dos outros por diversão?"

    show emilia uniforme serena meio corpo at sprite_direita with dissolve

    emilia "Eu leio tudo o que cai na minha frente. Aqui, quem lê menos descobre mais tarde."

    show emilia uniforme ajeitando oculos meio corpo at sprite_direita with dissolve

    "Ela tira do caderno um mapa dobrado. As margens estão cheias de letra miúda e três áreas riscadas em vermelho."

    emilia "Bloco leste, escadaria principal, segunda porta. A secretaria fecha às duas. E isto aqui..."

    "A ponta do dedo dela pousa sobre as áreas vermelhas."

    emilia "...são as alas interditadas. Ninguém explica o motivo, e eu aprendi que, quando ninguém explica, o aviso já foi dado."

    show expression obter_sprite_victor("pensando") as victor at sprite_esquerda with dissolve

    show emilia uniforme seria triste meio corpo at sprite_direita with dissolve

    "Ela estende o mapa. Fica esperando. Não insiste, não sorri, não retira a mão. É pior do que se insistisse."

    menu:

        "Pegar o mapa. \"Obrigado.\" Só isso. (+Afeto Emília)":

            $ afeto_emilia += 1

            $ th_dever("Emília", "um mapa da escola")

            $ reagir_escolha("emilia", "gentileza")

            $ notificar_rpg("🕊️ CORTESIA", "+1 Afeto Emília | Mapa aceito", "#5c85d6")

            "A palavra sai estranha da minha boca, como moeda de outro país. Dobro o papel e guardo."

            "A regra dois diz para desconfiar de quem sorri antes de oferecer. Ela sorriu antes de oferecer. Anoto."

            show emilia uniforme sorriso amigavel meio corpo at sprite_direita with dissolve

            emilia "Viu? Não doeu."

            protagonist "Ainda."

            emilia "...Ainda."

        "\"Obrigado, mas eu resolvo.\" (+Autonomia / +Dúvida Emília)":

            $ duvida_emilia += 1

            $ recusou_ajuda_dia1 = True

            $ reagir_escolha("emilia", "agressao")

            $ notificar_rpg("🛡️ AUTONOMIA", "+1 Dúvida Emília | Ajuda recusada", "#ffaa00")

            show emilia uniforme calma meio corpo at sprite_direita with dissolve

            emilia "Todo mundo diz isso no primeiro dia."

            protagonist "E no segundo?"

            emilia "No segundo, quase todos já descobriram que a escola não dá medalha para quem resolveu sozinho."

            "Ela não discute. Apoia o mapa no parapeito da janela, dobrado ao meio, como quem deixa um bilhete que alguém pode querer ou não."

        "\"Ninguém oferece um mapa de graça. O que você ganha com isso?\" (+Intelecto / +Dúvida)":

            $ intelecto += 1

            $ duvida_emilia += 1

            $ sondou_emilia_dia1 = True

            $ reagir_escolha("emilia", "ocultismo")

            $ notificar_rpg("📘 INTELECTO", "+1 Intelecto | +1 Dúvida Emília | Sondagem cautelosa", "#00ffcc")

            show emilia uniforme surpresa meio corpo at sprite_direita with dissolve

            "Pela primeira vez, ela hesita de verdade. Os dedos apertam a borda do caderno."

            emilia "Justo. É uma boa pergunta."

            show emilia uniforme seria triste meio corpo at sprite_direita with dissolve

            emilia "Eu ganho uma pessoa a menos para procurar depois que anoitecer."

            protagonist "Procurar?"

            emilia "...É só um jeito de falar. Pegue, Victor. Ou não. Mas a pergunta foi boa."

            $ th_dever("Emília", "um mapa da escola (e uma resposta que ela não completou)")

            "Ela estende o papel de novo, e dessa vez não sorri. Eu pego. Não sei se foi por educação ou por medo de descobrir o que ela quis dizer."

    show emilia uniforme serena meio corpo at sprite_direita with dissolve

    emilia "Mais uma coisa, a única que eu realmente quero que você leve. Quando o sol começar a baixar, não fique vagando pelos corredores."

    protagonist "Existe toque de recolher?"

    emilia "Existe um costume. Aqui, as duas coisas se parecem muito."

    hide emilia with dissolve

    "Ela vai embora sem olhar para trás. Só quem tem certeza do que anotou consegue andar assim."

    if recusou_ajuda_dia1:

        "Espero ela virar o corredor. Conto até dez. Depois volto e pego o mapa do parapeito, sem testemunhas, como quem recupera o que já era seu."

        protagonist "Isso não conta como ajuda. Eu só... encontrei."

        $ th_dever("Emília", "um mapa que eu fingi não aceitar")

    $ th_boato("O Fundador do corredor leste segue com os olhos quem passa por ele três vezes.")

    # ---- O BANCO DA NORA ----------------------------------------------------

    scene cena de nora pedindo uma caneta a victor no corredor de manha with dissolve

    "Diante da porta da secretaria há um banco de madeira e uma garota sentada nele, curvada sobre um caderno. Uniforme preto, mangas puxadas até os dedos. No colarinho, um alfinete de prata com o número 31."

    "Ela escreve, risca, escreve de novo. A caneta falha. Ela a sacode, a morde, a sacode outra vez."

    scene bg animado corredor academia cortina sol with dissolve

    show expression obter_sprite_victor("neutro") as victor at sprite_esquerda with dissolve

    show nora neutra at sprite_direita with dissolve

    nora "...Merda."

    "Levanta os olhos e me flagra encarando. São claros demais, e os cantos estão vermelhos de quem não dorme faz dias."

    nora "Você é o transferido, né? Todo mundo falou. 'O bolsista novo do interior.'"

    show expression obter_sprite_victor("confiante") as victor at sprite_esquerda with dissolve

    protagonist "Boa fama costuma chegar antes."

    nora "Má. Mas chegou antes mesmo."

    "Ela tenta rir, e a risada sai com a metade do tamanho. Os dedos da mão esquerda não param de tremer contra o caderno."

    show expression obter_sprite_victor("pensando") as victor at sprite_esquerda with dissolve

    $ th_voz("climax/nora_climax_01_caneta")
    nora "Tem uma caneta sobrando? A minha secou e eu preciso terminar isto antes que..."

    "O olhar dela escorrega para o relógio no fim do corredor."

    nora "...antes que ele chegue."

    menu:

        "🔮 [[HERANÇA DE SANGUE]]: 'Tome a caneta... mas jogue fora aquele frasco com cheiro de enxofre das caldeiras, Nora.'" if getattr(persistent, "eco_aviso_sangue_adulterado", False):
            $ emprestou_caneta_nora = True
            $ humanidade = min(100, humanidade + 5)
            $ sensibilidade_sobrenatural += 2
            $ th_credito("Nora", "uma caneta e um aviso profético")
            $ notificar_rpg("👁️ ECO PSÍQUICO", "+5 Humanidade | +2 Sensibilidade | Nora alertada do veneno", "#cc66ff")
            show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve
            protagonist "Pegue a caneta. Mas escute com atenção: se alguém te oferecer um frasco de elixir escuro nos dutos das caldeiras para passar nos exames... jogue no fogo. Aquilo não é remédio, Nora."
            "Nora arregala os olhos por trás das mechas desgrenhadas. Suas mãos trêmulas congelam no ar por um instante."
            nora "C-Como você sabe do frasco...? Eu nem... eu nem contei pra ninguém..."
            nora "Eu... eu vou pensar nisso. Obrigada, Victor... Eu nunca esqueço quem me estende a mão."
            jump apos_escolha_caneta_nora

        "Emprestar a caneta. (+Humanidade / Dívida de Nora)":

            $ emprestou_caneta_nora = True

            $ humanidade = min(100, humanidade + 2)

            $ th_credito("Nora", "uma caneta")

            $ notificar_rpg("🕊️ SOLIDARIEDADE", "+2 Humanidade | Caneta emprestada a Nora", "#88ccff")

            nora "Obrigada. De verdade. Te devo uma. Eu pago o que devo, pergunta pra qualquer um."

            show expression obter_sprite_victor("sorrindo") as victor at sprite_esquerda with dissolve

            protagonist "É só uma caneta."

            nora "Aqui, nada é só uma caneta."

            "Ela volta a escrever, mais rápido, como quem recebeu uma extensão de prazo. Eu devia dizer algo. Não sei o quê."

            nora "Meu mestre disse que me buscava depois da aula. Faz três semanas, mas ele disse."

            "Não sei o que é um 'mestre' neste lugar. Acho melhor não perguntar. Acho que isso também quebra uma regra."

        "\"Não tenho. Resolva sozinha.\" (+Orgulho Defensivo)":

            $ notificar_rpg("💔 INDIFERENÇA", "Recusou ajuda a Nora", "#ff5555")

            nora "Tá."

            "Só isso. Nem raiva, nem surpresa. Ela baixa o rosto de volta para o caderno."

            nora "Todo mundo resolve sozinho aqui. Você vai se dar bem."

            "Não sei se foi uma bênção ou uma maldição. Pelo tom, ela também não."

label apos_escolha_caneta_nora:
    hide nora with dissolve

    # ---- A SECRETARIA E O TERMO DE DOAÇÃO -----------------------------------

    scene bg animado gabinete diretor dia cortinas with fade

    show expression obter_sprite_victor("neutro") as victor at sprite_esquerda with dissolve

    show mob diretor as diretor at sprite_direita with dissolve

    diretor_ambrosio "Sr. Vane! Entre, entre. O seu é o processo mais bonito da pilha."

    "O Diretor Ambrósio tem um sorriso largo, mãos dobradas sobre a mesa e olhos que acompanham o que eu digo com meio segundo de atraso, como um vídeo mal sincronizado."

    "Ele folheia a pasta grossa sobre o couro verde da escrivaninha. Uma tarja vermelha de 'RESTRIÇÃO DISCIPLINAR' está colada na capa, mas o dedo dele a ignora com indiferença ensaiada, descendo direto para o laudo médico anexado no fundo."

    diretor_ambrosio "Bolsa integral, notas máximas em ciências exatas... Um pequeno 'incidente' no estacionamento da sua antiga faculdade que nós gentilmente arquivamos... e nenhum parente a avisar em caso de emergência."

    show expression obter_sprite_victor("falando") as victor at sprite_esquerda with dissolve

    protagonist "Sou órfão."

    diretor_ambrosio "Perfeito."

    show expression obter_sprite_victor("surpreso") as victor at sprite_esquerda with dissolve

    "A palavra fica no ar uma fração a mais do que devia."

    diretor_ambrosio "Quer dizer: lamento muito, rapaz. Lamento muito."

    "Ele corrige a frase com o mesmo sorriso, na mesma velocidade. Como quem aperta o botão certo depois de apertar o errado. Seus olhos descem novamente para a linha sublinhada em dourado no laudo do hemograma."

    $ th_voz("climax/diretor_climax_01_sangue_dourado")
    diretor_ambrosio "E, acima de tudo... uma biologia singularíssima. Rh Nulo. Sangue Dourado legítimo. A mantenedora desta academia aprecia alunos com... potencial de contribuição único." 

    diretor_ambrosio "Só falta uma formalidade. O Termo de Saúde Comunitária. Todo bolsista assina."

    "Duas páginas. A primeira fala em 'cidadania', 'solidariedade' e 'campanha semestral'. A segunda tem letra do tamanho de uma formiga."

    menu:

        "Assinar sem ler. A bolsa vale mais do que a briga.":

            $ assinou_doacao_dia1 = "assinou"

            $ th_dever("A Escola", "a bolsa integral (e o que vier escrito na página dois)")

            $ notificar_rpg("📝 CONFORMIDADE", "Assinou o termo de doação sem ler", "#aaaaaa")

            "Rubrico as duas folhas. A regra um acabou de nascer com defeito: uma bolsa integral é só uma dívida com juros que eu ainda não sei contar."

            diretor_ambrosio "Excelente escolha! Os melhores alunos são os que confiam."

        "Ler a página dois antes de assinar. (+Intelecto)":

            $ intelecto += 1

            $ assinou_doacao_dia1 = "leu"

            $ notificar_rpg("📘 INTELECTO", "+1 Intelecto | Descobriu cláusula oculta da mantenedora", "#00ffcc")

            "Leio com o dedo, linha por linha, enquanto o Diretor tamborila a mesa num ritmo que não é o do relógio."

            "O material biológico coletado terá 'destinação a critério da Fundação mantenedora'. Não diz qual hospital. Não diz qual Fundação."

            protagonist "Que Fundação é essa?"

            diretor_ambrosio "A mantenedora."

            protagonist "Isso eu entendi. Qual é o nome dela?"

            diretor_ambrosio "Ninguém lê essa parte, Sr. Vane."

            "Ele repete a frase em seguida. Dessa vez, o sorriso chega depois das palavras."

            $ th_boato("A 'Fundação mantenedora' recebe o sangue da campanha de doação. Ninguém sabe o endereço dela.")

            $ th_dever("A Escola", "a bolsa integral — assinada de olhos abertos")

            "Assino. Preciso da bolsa. Mas agora sei o que assinei, e isso é uma vantagem pequena. As melhores costumam ser."

        "Recusar. \"Prefiro doar quando eu escolher.\" (+Dúvida Elara)":

            $ assinou_doacao_dia1 = "recusou"

            $ duvida_elara += 1

            $ notificar_rpg("⚡ DESOBEDIÊNCIA", "+1 Dúvida Elara | Recusou a campanha semestral", "#ff5555")

            "O sorriso do Diretor não muda. É o resto do rosto que para. Por um segundo inteiro, ele parece uma fotografia dele mesmo."

            diretor_ambrosio "...Claro. A participação é voluntária."

            diretor_ambrosio "Bolsistas costumam participar."

            "Ele anota alguma coisa no canto da ficha. A caneta raspa o papel com uma pressa que não combina com a voz."

    diretor_ambrosio "Sua matrícula está concluída. O dormitório é o bloco norte. E, Sr. Vane..."

    "Os olhos dele finalmente me alcançam, no tempo certo, e é pior."

    diretor_ambrosio "...é prudente não ficar fora do dormitório depois do pôr do sol."

    hide diretor with dissolve

    scene bg animado corredor academia cortina sol with dissolve

    "Três pessoas em uma só manhã, e todas me mandaram para casa antes do escuro. Quando todo mundo dá o mesmo conselho, a pergunta não é se existe um motivo."

    "A pergunta é por que ninguém o diz em voz alta."

    "No retrato, os olhos do Fundador voltam a me seguir. Só que agora tenho a impressão de que não estão me julgando. Estão anotando."

    "Uma manhã. Já devo uma bolsa, uma resposta e talvez um mapa. E a tarde nem começou."

    hide victor with dissolve

    jump fim_de_evento

# ==============================================================================

# DIA 1 — TARDE: O TERMO Nº 112 E O OLHAR DE ELARA

# ==============================================================================

label evt_d01_tarde:

    scene bg animado corredor academia entardecer sol with fade

    $ th_musica("The_Unfinished_Lesson", 2.0)

    $ th_cartao(1, "Tarde")

    "O dormitório cheira a madeira velha e alvejante. A cama tem um colchão fino e a janela dá para outro muro. Largo a mala, troco de camisa — a da viagem está com o colarinho erguido de tanto suor — e saio."

    # ---- O PÁTIO E O CONTRASTE DAS CASTAS -----------------------------------

    scene cena contraste castas patio with dissolve

    "De tarde, a escola parece uma coleção de poses. O sol baixo projetando sombras compridas. Ninguém corre — correr chama atenção. Todos andam depressa, que é diferente."

    "A diferença entre 'estou atrasado' e 'estou com medo' é a posição dos cotovelos."

    # ---- O DEPÓSITO ANEXO ----------------------------------------------------

    scene cena deposito extorsao teo with fade

    "O depósito anexo fica no fim de um corredor que ninguém varre. A porta está aberta. Lá dentro, alguém chora sem fazer barulho, o que exige prática."

    "Dois veteranos de braçadeira branca — monitores — encurralam um garoto de uniforme remendado contra as prateleiras. No chão, um frasco de cristal azulado estilhaçado numa poça que cintila."

    "Heitor" "Olha ele. O bolsista novo. Chegou na hora."

    "Bia" "Chegou na hora de assinar."

    "Teo" "Eu juro que não encostei. A prateleira... a prateleira já estava torta."

    "Bia estende uma folha em minha direção. No alto: Termo de Ressarcimento nº 112. Valor: quatro mil e oitocentos em créditos. O campo do responsável está em branco."

    "Número 112. Já existem cento e onze antes deste. Cento e onze vezes alguém assinou por um frasco."

    "Heitor" "É simples, Vane. Você assina como responsável. O valor sai dos seus créditos de bolsista, devagarinho. Ninguém sente."

    "Heitor" "O Teo já tem uma advertência. Mais uma e perde a vaga. Você chegou hoje, ninguém liga para o seu nome."

    "Bia" "Aqui ninguém é preso, Vane. Todo mundo só... deve."

    "Olho para o Teo. Meu estômago contrai em um espasmo seco."

    "O cheiro de poeira úmida do depósito evapora, substituído de repente pela memória física do asfalto molhado."

    # ---- FLASH SENSORIAL: O SOCO DE DEFESA ---------------------------------

    scene cena passado victor 03 with hpunch

    "Flash físico: faróis de carro cortando a garoa no estacionamento. O impacto seco dos meus nós dos dedos contra a mandíbula de um agressor que achava que podia tocar em quem quisesse."

    "Eu já fui esse garoto. Já quebrei a mão para tentar defender alguém que estava encurralada sem poder revidar... e a recompensa foi ver o homem caído se levantar, sacar um telefone e comprar a polícia antes que eu pudesse respirar."

    scene cena deposito extorsao teo with dissolve

    "Aqui estão eles de novo. Duas hienas de braçadeira branca empurrando a conta para uma presa que não sabe morder."

    "Eu conheço esse roteiro. Sei exatamente o gosto amargo da última página."

    menu:

        "Pegar a caneta. \"Eu assumo.\" (+Humanidade / +Coragem / Quebra Regra 1)":

            $ destino_teo = "assumiu"

            $ humanidade = min(100, humanidade + 5)

            $ coragem += 1

            $ divida_monitores = 4800

            $ protegeu_colega_dia1 = True

            $ th_dever("Os Monitores", "ressarcimento do frasco — 4.800 créditos")

            $ th_quebrar_regra(1)

            $ notificar_rpg("🕊️ COMPAIXÃO CORAJOSA", "+5 Humanidade | +1 Coragem | Assumiu 4.800 créditos", "#88ccff")

            "Teo" "Não! Você não precisa..."

            protagonist "Eu assumo."

            "A regra um grita. Meu nome vai para o campo em branco. Eu preencho com mais firmeza do que sinto."

            "Heitor" "Muito nobre, novato. Bem-vindo à escola."

        "Pegar o termo e ler em voz alta. Com atenção às brechas. (+Intelecto / +Dúvida Elara)":

            $ destino_teo = "denunciou"

            $ intelecto += 1

            $ duvida_elara += 1

            $ notificar_rpg("📘 ASTÚCIA PRAGMÁTICA", "+1 Intelecto | +1 Dúvida Elara | Desmascarou termo fraudulento", "#00ffcc")

            protagonist "Termo número cento e doze. Data em branco, testemunha em branco, responsável em branco. Assinar isto é assinar um cheque sem valor."

            protagonist "E o frasco está rachado no fundo, de fábrica. Ele não quebrou na queda. Ele cedeu. Vocês sabiam do lote."

            "A cor some do rosto da Bia. Heitor aperta o maxilar, mas o dedo dele já está procurando o nome da próxima vítima."

            "Heitor" "Um bolsista novo que lê. Que aborrecimento."

            "Teo olha para mim como quem acabou de ser puxado de dentro d'água. Eu devia me sentir bem. Sinto apenas que acabei de acender uma luz em um quarto onde as pessoas preferem o escuro."

        "Virar as costas. \"Não toquei em nada. Resolvam entre vocês.\" (-Humanidade)":

            $ destino_teo = "abandonou"

            $ humanidade = max(0, humanidade - 4)

            $ notificar_rpg("💔 INDIFERENÇA CÍNICA", "-4 Humanidade | Orgulho defensivo", "#ff5555")

            "Teo" "Por favor..."

            "Não olho. Se eu olhar, eu fico. Se eu ficar, eu pago. Regra um, regra três, regra quatro — todas concordam comigo."

            "A voz do Teo me segue pelo corredor até virar um som que eu consigo fingir que não é uma voz."

    scene bg animado corredor academia entardecer sol with dissolve
    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    if destino_teo != "abandonou":

        "Um silêncio estranho cai no depósito. Não é o silêncio de quem foi vencido. É o silêncio de quem ouviu passos."

    else:

        "No fim do corredor, o ruído das conversas desaparece de uma vez. Alguém está vindo. E todo mundo sabe quem."

    # ---- APARIÇÃO DE ELARA --------------------------------------------------

    $ th_musica("The_Cold_Decree", 1.5)

    $ th_bark("elara", "padrao")

    show elara uniforme arrogante meio corpo at sprite_direita with dissolve

    "Uniforme branco imaculado. Cabelos brancos, olhos vermelhos. A Presidente do Grêmio Estudantil atravessa o corredor e o corredor se afasta dela como água de um barco."

    "Não há raiva no olhar dela. Só a atenção clínica de quem observa insetos num vidro."

    if destino_teo == "assumiu":

        elara "Um bolsista que paga por um frasco que não quebrou. Nobre, ou ingênuo. Na minha experiência, a diferença dura uma semana."

        protagonist "E depois de uma semana?"

        elara "Depois, o nobre vira cobrador. Ou vira cobrança."

        show elara uniforme observando meio corpo at sprite_direita with dissolve

        elara "Seu coração não acelerou nem ao assinar quatro mil e oitocentos. Ou é coragem, Sr. Vane, ou é desinteresse pela própria vida. Eu descobrirei qual."

    elif destino_teo == "denunciou":

        elara "Notável. O termo sem testemunha, o frasco rachado de origem. Heitor, Bia: três semanas de turno na rouparia."

        "Heitor" "Presidente, nós só—"

        elara "Eu sei exatamente o que vocês só."

        show elara uniforme observando meio corpo at sprite_direita with dissolve

        elara "E você, Sr. Vane, acaba de ganhar a atenção de duas pessoas que não gostam de ser lidas."

        protagonist "Atenção?"

        elara "Aqui, atenção é uma moeda. Cuide de quanto gasta."

    else:

        elara "Sensato. A maioria dos novatos leva uma semana para aprender que o problema alheio é um luxo."

        "Era o elogio mais frio que já recebi. E mesmo assim algo em mim se encolheu, como se tivesse sido aprovado por um motivo errado."

        show elara uniforme observando meio corpo at sprite_direita with dissolve

        $ th_voz("climax/elara_climax_00_deposito")
    elara "Seu coração está muito calmo, Sr. Vane. Gosto de calma. Ela costuma esconder coisas interessantes."

    show elara uniforme arrogante meio corpo at sprite_direita with dissolve

    elara "Heitor. E a trinta e um?"

    "Heitor" "Não voltou ao dormitório desde ontem, Presidente. Continua comprando nas caldeiras."

    elara "Sem mestre, sem registro, sem autorização para sair à noite. Se ela cruzar um portão depois do pôr do sol, quero ser avisada. Antes do pôr do sol, de preferência."

    "Trinta e um. O número do alfinete no colarinho da garota do banco. Fico em silêncio. Essa é uma das poucas coisas que sei fazer bem."

    hide elara with dissolve

    # ---- O PRAZO DOS DOCUMENTOS --------------------------------------------

    "Heitor" "Seu cadastro de bolsista está na sala da monitoria, segundo andar. Libera às seis. Se não for retirado até as seis e meia, a bolsa entra em suspensão."

    protagonist "Vocês seguraram o meu cadastro."

    "Heitor" "Seguramos o seu futuro, Vane. É diferente."

    "Sem o cadastro, a bolsa não ativa. Sem a bolsa, eu não tenho cama. Sem cama, eu não tenho para onde voltar. Cláusulas, cláusulas."

    scene bg animado corredor academia entardecer sol with dissolve

    "O sino do pátio bate seis vezes. Lá fora, o dourado do entardecer vira cobre. Os últimos estudantes passam por mim em silêncio de procissão, de cabeça baixa, como se obedecessem a uma ordem invisível."

    # ---- O VISLUMBRE INQUIETANTE: A FIGURA DO SONHO -------------------------

    "No final da galeria envidraçada que dá para a ala velha da academia, meus passos travam subitamente."

    "Parada junto a um dos arcos de pedra, observando o pátio banhado em luz âmbar, há uma jovem."

    "Ela não veste o uniforme preto dos calouros, nem as túnicas engomadas da elite do Grêmio. O vestido escuro, de cortes aristocráticos e tecido pesado, parece pertencer a um século esquecido pela história."

    show lility triste olhando para baixo at sprite_direita with dissolve

    "A luz do entardecer toca o perfil dela de lado. Cabelos carmesins. Postura reta, mas não rígida — o tipo de postura de quem parou de se preocupar com o que parece há tempo demais para se calcular."

    "Ela olha para o pátio como quem não está vendo o pátio."

    "O ar aqui tem um gosto diferente. Mirra. Ferro. Algo mais fundo."

    "Os pelos do antebraço erguem contra o tecido da camisa."

    victor "(Eu sonhei com ela.)"

    "Não é uma impressão. Não é cansaço da viagem. O rosto é o mesmo. Os cabelos são os mesmos. Os olhos que ela vai levantar daqui a três segundos serão os mesmos."

    show lility olhando seria at sprite_direita with dissolve

    "Quase em câmera lenta, como se sentisse o peso da minha presença, ela desvia o olhar do nada e me percebe a encarando à distância."

    "Nossos olhares se cruzam por uma fração de segundo. Não há choque, curiosidade ou escárnio em seu semblante — apenas uma indiferença muda."

    "Ela simplesmente me ignora, desvia os olhos como se eu fosse um detalhe invisível na paisagem e dá meia-volta, saindo calmamente de onde estava."

    hide lility with dissolve

    "Fico parado. Ela vai embora sem pressa, como se a minha presença fosse um detalhe que ela catalogou e descartou no mesmo segundo."

    "Minha mão esquerdou tinha se movido na direção dela. Não sei o que ia fazer. Chamo de volta."

    victor "(Coincidência. Cansaço da viagem. Isso é o que eu vou anotar.)"

    "Pego o cadastro na monitoria. Subo. Desço. Quando termino, a janela mostra um céu sem nenhuma cor."

    hide victor with dissolve

    jump fim_de_evento

# ==============================================================================

# DIA 1 — NOITE: NORA, A ZONA VERMELHA E O PACTO DE SANGUE

# ==============================================================================

label evt_d01_noite:

    show screen hud_sobrevivencia

    scene bg animado corredor academia entardecer sol with fade

    $ th_cartao(1, "Noite")

    "As luzes do corredor trocam de cor sem barulho. De âmbar para carmesim, como se alguém tivesse virado uma chave que eu não vi."

    scene bg animado corredor zona vermelha luzes de sangue with flash_red

    $ th_stinger("zona_vermelha")

    $ th_musica("insistent_bass", 1.0)

    "O ar tem gosto de cobre. As paredes parecem mais próximas. E, ao longe, um som seco, repetido: raspar. Parar. Raspar."

    "Eu sei que devia voltar para o dormitório. Eu sei. Mas o atalho pela ala leste economiza dez minutos, e dez minutos é a diferença entre cumprir um prazo e perder uma bolsa."

    "Orgulho disfarçado de responsabilidade. Eu ainda não sabia que esse era o meu defeito."

    # ---- A PAREDE DA LOUCURA DE NORA ----------------------------------------

    scene cena nora parede loucura with dissolve

    "A ala interditada. Um corredor largo, vazio. E, na parede inteira, centenas de linhas escritas à tinta, empilhadas até o teto, sem nenhum espaço."

    "ELE VEM DEPOIS DA AULA. ELE VEM DEPOIS DA AULA. ELE VEM DEPOIS DA AULA."

    "Ao pé da parede, de costas, uma garota de uniforme preto. A mão esquerda escreve sem parar. Na direita, uma caneta. A minha."

    nora "A aula acabou. Não acabou? A aula... acabou."

    protagonist "Nora?"

    scene cena nora parede encarando with dissolve

    "Ela vira o rosto devagar. Os olhos agora são só o vermelho que sobrou dos cantos. Unhas quebradas. Veias negras pulsando no pescoço como cabos sob a pele."

    nora "Você é o da caneta."

    if emprestou_caneta_nora:

        nora "Eu te devo uma caneta. Eu pago o que devo. Eu... eu pago."

        "A voz racha no meio da frase, e, por um instante, volta a ser a mesma da secretaria. Depois, a voz escorrega."

    else:

        nora "O que não tinha caneta. Eu achei uma. Achei... no chão."

        "Mentira. Mas ela acredita nessa mentira com a mesma intensidade com que precisa de uma."

    $ th_voz("climax/nora_climax_02_parede")
    nora "A parede está batendo. Você não ouve? Tum. Tum. Ela pede sangue limpo, e eu só tinha o do lote. Eu paguei! Disseram que era limpo!"

    protagonist "Nora, você precisa de ajuda. Eu vou chamar—"

    scene bg animado corredor zona vermelha luzes de sangue with flash_red

    show nora atacando descontrolada e frenesi at bote_ataque with hpunch

    nora "Cala a boca! Cala esse coração barulhento!"

    hide nora with dissolve

    call iniciar_combate("Nora Vasques", "nora atacando descontrolada", "nora atacando descontrolada e frenesi", 65, 20, 4.5, "corrompido", True, pode_fugir=False) from _call_iniciar_combate_7

    # ---- CENA 1: QUASE MORTE PELAS MÃOS DE NORA -----------------------------

    scene cena quase morte nora with flash_red

    with vpunch

    $ hp_jogador = 15

    "As garras chegam antes que eu feche o braço. O impacto na garganta é seco — mais pancada do que corte, até o corte chegar."

    "Caio de lado. O piso de pedra faz barulho quando minha cabeça bate. O sangue sai quente. O chão está muito frio."

    "Ela fica sobre mim. A mão erguida banhada em sangue. Fica ali, ofegante, como se o gesto tivesse travado no meio do caminho."

    "O olhar dela desce devagar até a caneta, ainda cravada trêmula entre os próprios dedos."

    if emprestou_caneta_nora:

        nora "...Eu ia te pagar."

    else:

        nora "...Você não tinha caneta. Eu só queria escrever."

    "Passos pesados da patrulha do Conselho ecoam com urgência no fim do corredor. Ela recua atordoada, tropeça no próprio medo e foge para o breu das sombras."

    "O sangue empoça devagar. Esse é um detalhe que eu não esperava notar — a lentidão. Achei que ia ser mais rápido."

    "Não gritei. A regra quatro exigiria uma explicação melhor para isso. Não tenho."

    "Eu não vim de tão longe para morrer num corredor que nem consta no mapa."

    # ---- CENA 2: ENCONTRO COM LILITY DAS SOMBRAS ----------------------------

    stop music fadeout 1.5

    $ th_sfx("heartbeat")

    $ th_musica("The_Crimson_Chamber", 2.0)

    scene cena quase morte encontra lility with fade

    "A patrulha se afasta. O corredor engole o eco das botas."

    "Minha visão vai reduzindo. Começa pelas bordas — como quando você aperta o olho contra um vidro escuro e o campo vai diminuindo até sobrar só o centro."

    "E então chega o cheiro. Mirra. Ferro. Algo antigo que não tem nome no vocabulário que eu aprendi."

    "Passos. Lentos. Sem pressa de ninguém que tenha medo de chegar tarde."

    "É ela."

    "Do pesadelo. Da galeria de tarde. Da pergunta que eu ainda não sei responder."

    # ---- CENA 3: LILITY SE APROXIMA E SE AJOELHA ----------------------------

    scene cena quase morte lility ajoelha with dissolve

    "Ela para ao meu lado. Abaixa o joelho direito no piso manchado — sem hesitar, sem proteger o vestido."

    "A cabeça dela inclina de lado, como quem avalia o ângulo certo para dissecar algo que ainda está se mexendo."

    $ th_voz("climax/lility_climax_02_pacto")
    mestra "Fascinante.{w=0.4} Você não gritou."

    mestra "Os mortais nessa posição imploram a um deus surdo. Ou chamam pela mãe. Você só cravou as unhas na pedra e se recusou a apagar."

    mestra "Que orgulho patético."

    protagonist "Eu não vim... de tão longe... para morrer no escuro como descarte."

    mestra "Descarte. Que palavra interessante para usar quando se tem a traqueia aberta."

    mestra "Qual é o seu nome?"

    protagonist "Victor. Victor Vane."

    mestra "Vane. Um nome que só existe para apontar o vento. Responda sem pensar, Victor Vane: o que você deve?"

    protagonist "...O quê?"

    mestra "Todo mundo morre devendo alguma coisa. Qual é a sua dívida?"

    protagonist "Nada. Eu não devo nada a ninguém."

    "Ela ri. Uma risada baixa, rouca e demorada, que parece vibrar diretamente na raiz dos meus ossos."

    mestra "Que mentira cara. Eu admiro mentiras caras."

    # ---- CENA 4: A PROPOSTA DE SANGUE ---------------------------------------

    scene cena quase morte lility proposta sangue with dissolve

    "Ela ergue a mão pálida e passa a unha afiada pelo próprio pulso. O sangue brota denso, escuro como rubi líquido, exalando calor proibido e poder primordial."

    mestra "Uma prorrogação. Abra a boca."

    protagonist "O preço..."

    mestra "Prorrogação tem juros, Victor. Mas ninguém jamais perguntou antes. Eles só agradecem. Depois."

    "Por uma fração de segundo, o deboche se esvai de sua postura. Ela me encara no fundo dos olhos como quem enxerga uma dor familiar."

    menu:

        "Agarrar o pulso dela. \"Eu aceito. Mas é só um empréstimo.\" (+Coragem / +Afeto com a Mestra)":

            $ coragem += 1

            $ afeto_mestra += 1

            $ reagir_escolha("lility", "autoridade")

            $ notificar_rpg("🩸 PACTO DE SANGUE", "Ressuscitado como Ghoul | +1 Coragem | +1 Afeto com a Mestra", "#ff0044")

            mestra "Chame como quiser. O contrato não se importa com o nome."

        "\"Qual é o juro?\" (+Intelecto / Postura Pragmática)":

            $ intelecto += 1

            $ reagir_escolha("lility", "morbido")

            $ notificar_rpg("🩸 PACTO DE SANGUE", "Ressuscitado como Ghoul | +1 Intelecto | Análise pragmática", "#ff0044")

            mestra "Pragmático até sangrando. Que delícia."

            mestra "Você vai descobrir que não é cobrado em dinheiro."

        "\"Se é para virar bicho de estimação... sirva algo decente.\" (+Charme / +Afeto com a Mestra)":

            $ charme += 1

            $ afeto_mestra += 1

            $ reagir_escolha("lility", "sarcasmo")

            $ notificar_rpg("🩸 PACTO DE SANGUE", "Ressuscitado como Ghoul | +1 Charme | +1 Afeto com a Mestra", "#ff0044")

            mestra "Atrevido até na sarjeta. Beba, insolente. A minha safra é melhor que qualquer refeição que você já teve na vida."

    with flash_red

    $ humanidade = max(0, humanidade - 5)

    $ fome_sangue = 70

    $ hp_jogador = 100

    $ ressonancia_pre_diluviana += 1

    $ covil_sala_musica_ativo = True

    $ th_dever("Mestra", "a minha vida (uma 'prorrogação')")

    $ th_quebrar_regra(1)

    "O sangue dela desce como brasa líquida. A carne rasgada se fecha com estalos rápidos, e o meu coração dá uma última batida... e para."

    "Eu continuo aqui. Respirando por hábito. Sem pulso nenhum."

    "E então algo mais fundo que o meu peito responde ao choque do pacto: uma batida lenta, cavada e titânica, vinda do mais profundo dos alicerces. As pedras do chão tremem sob meus joelhos. Poeira de séculos despenca das abóbadas."

    $ GerenciadorRuina.adicionar_ruina(5, "Ressonância Pré-Diluviana (Despertar do Ghoul de Sangue Dourado)")

    "O alarme de contenção estala mudo nos tubos de cobre. Algo que dormia sob a Academia São Cipriano abriu um dos olhos."

    # Victor se levanta revigorado — a cena volta ao corredor e Lility aparece em pé diante dele

    scene bg animado corredor zona vermelha luzes de sangue with dissolve

    show lility meio corpo chocada at sprite_padrao with dissolve

    mestra "...Interessante."

    protagonist "Você sentiu isso?"

    show lility confiante sorriso meio corpo at sprite_padrao with dissolve

    mestra "Senti o quê? O seu pulso foi embora, meu bem. Ouça o silêncio. Todo mundo se acostuma."

    "Ela mente. Eu anoto."

    protagonist "Por que me salvou? Você não parece do tipo que faz caridade."

    $ th_bark("lility", "risada")

    show lility meio corpo desdenhando at risada_deboche

    mestra "Hábito. Eu estava entediada, e a sua teimosia me pareceu um passatempo razoável."

    "Ela diz 'tédio' com a boca. Com os olhos, diz outra coisa. Eu ainda não sei o nome dela."

    protagonist "E como devo te chamar?"

    mestra "Para você, sou apenas 'Mestra'. E quando eu perguntar algo, você responde com reverência."

    protagonist "E se os outros perguntarem?"

    show lility comportada sorriso meio corpo at sprite_padrao with dissolve

    mestra "Para a burocracia tola desta academia, sou a senhorita Lyra von Blut. Uma fidalga menor da Silésia com dote atrasado, confinada nesta ala por capricho do Conselho."

    "Mestra, então. Eu anoto."

        # ---- A IRRUPÇÃO DE ELARA: O CONFRONTO IDEOLÓGICO -----------------------

    $ th_musica("Authority_Breach", 1.0)

    "O tabuado estala. As duas portas se abrem num estrondo seco!{nw}"

    show lility bracos cruzados seria meio corpo at sprite_esquerda

    $ th_bark("elara", "irritada")

    show elara uniforme arrogante meio corpo at sprite_direita with vpunch

    "A figura que surge na soleira parece talhada em mármore gélido. Uniforme branco impecável, sem uma única dobra fora do lugar — o emblema de ouro do Grêmio Estudantil reluzindo no peito com a altivez de quem se julga a única guardiã da ordem."

    "Cabelos alvos como geada e dois olhos carmesins afiados que varrem o chão manchado de sangue, cravando-se na minha mestra com fúria contida."

    elara "Senhorita von Blut. Eu a proibi terminantemente de produzir novos membros ou lacaios neste campus."

    show lility comportada sorriso meio corpo at sprite_esquerda

    mestra "Tecnicamente, Presidente, ele é um ghoul. 'Lacaio' pressupõe um contrato de emprego com benefícios. Achei que vocês, os puro-sangues da diretoria, fossem obcecados pelo rigor da lei."

    elara "Cale a boca. Você perdeu qualquer direito de ironizar as nossas leis no instante em que cruzou esta fronteira."

    "O olhar de Elara se desvia devagar de Lyra e recai sobre mim. Por um instante, a rigidez austera de sua postura cede a algo inesperado — não nojo, nem desprezo... mas uma piedade sombria e trágica."

    elara "Nome."

    protagonist "Victor. Victor Vane."

    elara "O bolsista transferido. Você chegou esta manhã com uma mala surrada e um histórico acadêmico exemplar, Sr. Vane. Tinha uma vida mortal inteira pela frente... E agora olhe para você."

    protagonist "Eu fui atacado no corredor. Uma aluna... Nora Vasques."

    show elara encarando neutra at sprite_direita with dissolve

    "Por um microssegundo, a máscara imperturbável da Presidente falha. Os lábios dela se comprimem."

    elara "...Nora. A cobaia trinta e um da lista de contenção."

    protagonist "Ela estava enlouquecida, falando que a parede batia e pedindo sangue limpo! O que vocês vão fazer com ela?!"

    elara "O que for necessário. Os executores já recolheram o que sobrou. E, para ser sincera, Sr. Vane... você deveria ter tido o mesmo destino."

    protagonist "O quê?!"

    show elara encarando neutra com cabeca inclinada at sprite_direita with dissolve

    elara "A morte humana. O descanso da terra."

    "Ela dá um passo à frente, apontando a mão enluvada na direção da minha mestra com um ressentimento cortante."

    elara "Você não compreende a atrocidade que esta mulher cometeu contra a sua existência, garoto. Os mortais têm alma, têm um ciclo que se fecha e têm o direito sagrado de descansar em paz. Mas nós? Os da nossa espécie não encontram céu e nem inferno ao fechar os olhos."

    elara "Quando um vampiro é destruído, só existe o Vazio. O esquecimento eterno ou um torpor milenar sob a lama fria. Ao te transformar para satisfazer os próprios caprichos, ela roubou o seu descanso eterno e te acorrentou a uma fome que vai queimar a sua consciência dia após dia até você virar um monstro sem mente como a Nora."

    show lility meio corpo desdenhando at sprite_esquerda with dissolve

    mestra "Que discurso comovente, Elara. Quase me faz esquecer que a sua 'misericórdia' aristocrática sempre termina com uma lâmina de prata no coração de quem não tem berço nobre para pagar as propinas do Grêmio."

    show elara irritada e com desprezo at sprite_direita with dissolve

    elara "Você é uma nobrezinha falida e sem nome, Lyra. Já toleramos a sua insolência de baixo clero por tempo demais — inclusive quando foi flagrada rondando as catacumbas do subsolo, cobiçando o que não lhe pertence. Mas forçar a criação de um ghoul após o Tratado... isso é traição direta à Máscara."

    "Elara se vira para mim com passos firmes. O ar congela ao redor de seus dedos."

    elara "...Há um ritmo no seu peito que não é seu. Uma ressonância que este colégio não pode tolerar solta."

    show lility presas agressiva meio corpo at sprite_esquerda with dissolve

    mestra "Tire as mãos dele, Presidente."

    show elara uniforme arrogante meio corpo at sprite_direita with dissolve

    elara "Quem dita os termos sou eu."

    # Queimadura do Grilhão de Sangue

    $ th_sfx("flesh_burn")

    with flash_red

    "A palma da mão dela bate no meu peito antes que eu registre o movimento. Frio. Depois quente. Depois uma coisa que não é nem um nem outro — é pressão dentro do osso, como uma broca sem broca."

    protagonist "Aaargh...! O que... o que você fez?!"

    "Atrás de mim, um estalo seco ecoa no ar. Fios etéreos avermelhados saltam da runa no meu peito e chicoteiam o ar até os pulsos da minha mestra!"

    "A pele pálida dela se rasga em vergões sangrentos. Ela dá um passo em falso, respirando entre os dentes cerrados pela dor súbita — a essência selada de seu corpo antigo não tem força para repelir a magia de contenção moderna."

    show lility vulneravel timida meio corpo at sprite_esquerda with dissolve

    mestra "Ugh... Francamente, Presidente... Cuidado com o carpete. Manchas de sangue não saem fácil."

    "Ela força um sorriso debochado, mas seus dedos tremem ao segurar os pulsos feridos. Ela está sofrendo de verdade."

    $ th_voz("climax/elara_climax_01_grilhao")
    elara "O Grilhão está selado. Cada falha sua queima nela. Cada exposição cai sobre ela. É assim."

    protagonist "Isso é covardia."

    show elara encarando de cima para baixo at sprite_direita with dissolve

    elara "É contabilidade. Há diferença, Sr. Vane. Aprenda logo qual."

    elara "Amanhã de manhã. Ao nascer do sol. Compareça ao Gabinete da Presidência para a sua audiência formal. Decidiremos se você tem serventia para o campus... ou se a execução será aplicada como misericórdia antes da sua primeira crise de fome."

    elara "E você, Lyra: está formalmente confinada à ala interditada. Se colocar os pés nas áreas nobres ou na diretoria, meus executores farão você sangrar até secar."

    hide elara with dissolve

    "A porta bate num estrondo que faz o pó do teto cair. O silêncio que sobra é sufocante."

    show lility triste olhando para baixo at sprite_padrao with dissolve

    "Minha mestra olha para os pulsos. Os vergões já param de sangrar — mas ela continua olhando, como se o que ela vê não fossem feridas novas, mas uma conta velha que alguém finalmente imprimiu."

    mestra "Boa noite, cachorrinho. Amanhã você vai ter muitas perguntas. E eu... poucas respostas."

    hide lility with dissolve

    scene bg animado sala musica piano noite with fade

    "Ouço o silêncio. Não o meu coração — esse parou. O silêncio do corredor, das paredes, do ar."

    "A regra um prometia que eu nunca ia dever. Hoje assinei débito com a minha própria vida."

    "Dia um."

    call screen th_balanco_dia("FIM DO DIA 1")

    jump fim_de_evento

# ==============================================================================

# # ==============================================================================

# DIA 2 — MANHÃ: A AUDIÊNCIA E O TERMO DO GRILHÃO (O JULGAMENTO DA MÁSCARA)

# ==============================================================================

# ==============================================================================

# DIA 2 — MANHÃ: A AUDIÊNCIA E O TERMO DO GRILHÃO (O JULGAMENTO DA MÁSCARA)

# ==============================================================================

# ==============================================================================

# DIA 2 — MANHÃ: A AUDIÊNCIA E O TERMO DO GRILHÃO (O JULGAMENTO DA MÁSCARA)

# ==============================================================================

label evt_d02_manha:

    scene bg animado gabinete diretor dia cortinas with fade

    $ th_musica("The_Cold_Decree", 1.5)

    $ th_cartao(2, "Manhã")

    "Acordei sem ter dormido. A gola da camisa está dura de sangue seco. Passei dez minutos procurando uma cicatriz no pescoço. Não achei nenhuma."

    $ th_sfx("passos_madeira")

    "Dois executores de branco me buscaram às sete e meia. Não disseram nada. Não precisavam."

    "Lá fora, os vitrais projetam losangos dourados no mármore. Aqui dentro, o meu peito é mudo como câmara fria."

    show expression obter_sprite_victor("triste") as victor at sprite_esquerda with dissolve

    show elara uniforme observando meio corpo at sprite_direita with dissolve

    "O gabinete cheira a papel envelhecido e decisão irreversível. No canto, numa poltrona que parece pequena demais para a função que ele representa, está o Diretor Ambrósio."

    "Ele assoberbou a cabeça antes de Elara falar. Treino, provavelmente."

    scene cena elara conversa manha with fade

    "Elara está de pé atrás da pesada escrivaninha de mogno escuro. Não sentada — de pé. As mãos enluvadas apoiadas na madeira polida com a autoridade fria de quem não precisa de apresentações."

    "O olhar dela varre minha silhueta da gola até os sapatos. Sem pressa. Sem desprezo. Apenas a inspeção metódica de uma cirurgiã diante de um espécime anômalo."

    elara "Garganta aberta às dez da noite. Sete da manhã, sem cicatriz. Sem pulso."

    elara "Não pergunte como sei. Você aprende a perceber o silêncio onde deveria haver batimento."

    scene cena elara mostra pingente nora with dissolve
    $ persistent.eco_aviso_sangue_adulterado = True

    "Ela pousa algo sobre a mesa, sem pressa. Um alfinete de prata polida com um número gravado em baixo-relevo: 31."

    "O metal tilinta levemente sobre o mogno, refletindo a seriedade fúnebre de seus olhos carmesins."

    elara "Encontrado no corredor leste, onde você caiu. O número da aluna Nora."

    protagonist "E ela?"

    elara "Contida. Onde a fome não a alcançará mais."

    protagonist "Isso é um eufemismo para execução?"

    elara "É o protocolo para quem perde o controle da própria sede. E você está a um milímetro de ter a mesma ficha encerrada, Sr. Vane."

    elara "Estacionamento. Noite. Um docente de sobrenome caro e um punho que foi mais rápido que o bom senso."

    scene cena passado victor 08 with dissolve

    "Ela desliza uma cópia amarelada do boletim de ocorrência sobre o mogno. A imagem mental do aperto de mãos corrupto entre o diretor e a autoridade queima nos meus olhos."

    elara "Agressão qualificada contra um membro da cátedra. Um inquérito que evaporou mediante um aperto de mãos e um acordo confidencial da reitoria para preservar a honra da família do agressor."

    # ---- RETORNO AO GABINETE: AMBIENTE COM OS SPRITES CORRETOS ------------
    scene bg animado gabinete diretor dia cortinas with dissolve

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show elara encarando neutra com cabeca inclinada at sprite_direita with dissolve

    "Ela apoia as mãos enluvadas sobre o mogno da escrivaninha e se inclina para a frente. Não há ódio no semblante dela — apenas uma seriedade fúnebre e pesada."

    elara "E a garota que você tentou proteger assinou contra você. O diretor arquivou o B.O. com um sorriso, e você foi empurrado para fora da sua própria vida."

    elara "Exceto pela nossa lista de transferência. Porque nós lemos mais devagar — e chegamos sempre à mesma página."

    elara "Rh Nulo. Sangue Dourado. Um a cada seis milhões de nascidos. E você achou que era azarado." 

    $ th_voz("climax/elara_climax_02_audiencia")
    elara "Ontem de manhã você era um mortal, Sr. Vane. Tinha o direito sagrado de tropeçar, envelhecer, adoecer e... quando a hora chegasse, descansar em paz."

    elara "Agora você é um cadáver reanimado. Uma aberração incompleta acorrentada à coleira de uma vampira exilada que você sequer conhece."

    protagonist "Eu não escolhi ser atacado. E não escolhi ser transformado."

    elara "Eu sei. É exatamente por isso que sinto pena de você."

    "Piedade."

    "Eu ouço a palavra e fico procurando o truque. Não acho."

    elara "Você acredita em algo além da sua própria teimosia, Victor?"

    elara "Mortais têm esse privilégio. A fé como anestesia. Nós não."

    elara "Quando um dos nossos morre, não há cerimônia. Não há testemunha. Há o chão. Há o silêncio. E há quem varreu."

    elara "Se eu chamasse os executores agora, seria o único favor genuíno que este colégio te faria. Você ainda dorme, Victor. Ainda tem restos de algo que parece consciência. Nora não tinha mais isso. Leva oito semanas, em média, perder o que te sobrou."

    show elara encarando de cima para baixo at sprite_direita with dissolve

    elara "Portanto, responda olhando nos meus olhos: por que eu deveria deixá-lo sair vivo desta sala? O que faz você achar que a sua existência vale o risco da nossa Máscara?"

    menu:

        "“Porque eu não fujo de dívidas. E me recuso a ser descartado de novo.” (+Coragem / O Credo de Victor)":

            $ coragem += 1

            $ reagir_escolha("elara", "disciplina")

            $ notificar_rpg("🔥 CORAGEM", "+1 Coragem | O Credo de Victor", "#ff3300")

            protagonist "Eu passei a vida inteira aprendendo que ninguém me dá nada de graça, Presidente. O meu antigo orientador tentou me empurrar para a sarjeta para salvar o próprio nome, e eu sobrevivi. Não vim até esta capital para ser executado pela 'misericórdia' de ninguém."

            protagonist "Eu tenho regras. A quarta diz: nunca ser descartável. Se a minha vida agora tem uma dívida de sangue, eu vou pagar até o último centavo. Mas eu decido como ando."

            show elara uniforme arrogante meio corpo at sprite_direita with dissolve

            elara "Olha só... O lacaio tem dentes. A maioria dos que provam do sangue rastejam implorando por clemência. Mas você se agarra ao próprio orgulho como se fosse um escudo."

            elara "A sua existência é uma fissura perigosa na ordem. Mas a sua teimosia... é fascinante. E eu aprecio peças que se recusam a quebrar no primeiro impacto."

        "“Matar um bolsista no segundo dia destrói a Máscara mais rápido do que a minha sede.” (+Intelecto / +Afeto Elara)":

            $ intelecto += 1

            $ afeto_elara += 1

            $ reagir_escolha("elara", "intelecto")

            $ notificar_rpg("📘 INTELECTO", "+1 Intelecto | +1 Afeto Elara | Raciocínio frio", "#00ffcc")

            protagonist "Um estudante transferido desaparecido nas primeiras vinte e quatro horas abre uma investigação no Ministério da Educação, traz a polícia para o campus e atrai a atenção dos caçadores que vocês tanto querem longe."

            protagonist "Eu tenho disciplina analítica. Posso me controlar, seguir as regras e ser útil ao Grêmio como uma ponte entre os dois lados. Executar-me agora cria uma anomalia burocrática impossível de varrer para baixo do tapete."

            show elara uniforme observando meio corpo at sprite_direita with dissolve

            elara "Olha só. Ele pensa antes de sangrar."

            elara "Raciocínio frio, avaliação de danos colaterais e pragmatismo político. Você tem razão: um cadáver bolsista agora é um problema administrativo caro demais. Continue assim e talvez chegue vivo ao próximo mês."

        "“Uniforme branco impecável, Presidente. Tem medo de sujar com o meu sangue?” (+Charme / +Dúvida Elara)":

            $ charme += 1

            $ duvida_elara += 1

            $ reagir_escolha("elara", "sarcasmo")

            $ notificar_rpg("✨ CHARME", "+1 Charme | +1 Dúvida Elara | Provocação ácida", "#ff66cc")

            protagonist "Uniforme branco imaculado, gabinete banhado a ouro e discursos poéticos sobre misericórdia... Tem medo de sujar as luvas com o sangue de alguém sem sobrenome aristocrático?"

            protagonist "Ou o que realmente incomoda o Grêmio é perceber que um humano qualquer tem mais coragem de encarar a realidade do que toda essa sua nobreza encenada?"

            show elara irritada e com desprezo at sprite_direita with dissolve

            elara "Sujeira se limpa com alvejante, Sr. Vane. Insolência se extirpa pela raiz com lâmina de prata. Guarde as ironias para quando não estiver cercado pelos meus carrascos."

            elara "Mas admito... é raro ver alguém com o coração parado falar com tanta vivacidade. Vamos ver quanto tempo esse sarcasmo dura quando a primeira crise de abstinência rasgar o seu estômago."

    show elara uniforme arrogante meio corpo at sprite_direita with dissolve

    "Ela se endireita. A postura volta a ser a de uma soberana absoluta."

    elara "Há uma regra mais antiga do que esta academia, Sr. Vane: ninguém de fora pode saber. Ninguém pode sequer suspeitar."

    elara "Houve uma era em que os nossos ancestrais foram descuidados... e a água corrigiu isso. A Máscara não é vaidade ou protocolo estudantil: é a única coisa que impede o céu de olhar para nós outra vez."

    elara "Se você quebrar o sigilo, a punição não virá apenas dos meus carrascos. O mundo inteiro cobra a conta."

    "Ela abre uma pasta de couro e desliza uma folha timbrada pela mesa de mogno. No topo, grafado em caligrafia de ferro: Termo do Grilhão."

    "I. A Máscara é inviolável. Nenhum humano comum presencia ou suspeita do que somos."

    "II. A senhorita Lyra von Blut permanece estritamente confinada à ala interditada. Os atos de um são cobrados do outro."

    "III. A alimentação será feita exclusivamente por bolsas filtradas da enfermaria. Caça de alunos é crime de execução imediata."

    "IV. Toda e qualquer Exposição pública é paga em carne viva de quem o criou."

    "V. O Grêmio revisará o seu termo e o seu destino conforme o estado da escola e o avanço da anomalia do Eclipse."

    protagonist "O alinhamento do Eclipse está avançando a cada ciclo. A cidade inteira está sentindo as anomalias."

    elara "Então aproveite enquanto o campus ainda está de pé para me convencer de que a misericórdia de deixá-lo respirar não foi um erro de cálculo."

    "Ela estende uma caneta de aparo dourada. Há espaço, na margem inferior, para uma única cláusula condicional."

    menu:

        "Cláusula IV. “Cobrem de mim. Não dela.” (+Humanidade / Grilhão Compartilhado)":

            $ grilhao_compartilhado = True

            $ humanidade = min(100, humanidade + 3)

            $ notificar_rpg("🕊️ COMPAIXÃO", "+3 Humanidade | Grilhão Compartilhado", "#88ccff")

            protagonist "Se eu cometer um deslize, cobrem de mim. Ela me salvou da morte, quer você aprove o método ou não. Eu não empurro as minhas contas para as costas de ninguém."

            show elara uniforme observando meio corpo at sprite_direita with dissolve

            "Elara me encara por um longo segundo, visivelmente desconcertada por um mortal defender a criatura que o amaldiçoou."

            elara "O Grilhão não negocia a punição primária. Mas posso dividi-la. Cada choque que a carne dela receber por sua causa agora também rasgará a sua própria pele."

            elara "Curioso... Você prefere sangrar a dever favores a uma vampira. Concedido."

            $ th_aviso("GRILHÃO COMPARTILHADO", "A dor cobrada na sua mestra agora também alcança a sua carne.", "#ff8866")

        "Cláusula III. “Duas bolsas por semana não bastam.” (+2 Bolsas / Informante de Elara)":

            $ informante_elara = True

            $ bolsa_sangue_filtrado += 2

            $ notificar_rpg("🩸 INVESTIMENTO", "+2 Bolsas Filtradas | Informante de Elara", "#ff5555")

            protagonist "Duas bolsas por semana não mantêm um ghoul recém-criado lúcido. Se o Grêmio quer que eu passe despercebido nas aulas, preciso de sustento real."

            show elara sorrindo de forma ironica at sprite_direita with dissolve

            elara "Eu aprecio quem sabe negociar custos operacionais. Duas bolsas extras entregues na enfermaria toda semana. Em troca, relatórios detalhados: quem anda investigando as caldeiras e quem faz perguntas sobre as catacumbas do subsolo."

            protagonist "Isso é espionagem interna."

            elara "Isso é diplomacia aplicada, Sr. Vane. A diferença é a quem se deve lealdade."

            $ th_dever("Elara", "duas bolsas extras (em troca de relatórios sobre investigações no subsolo)")

        "Assinar como está. (Sem exigências)":

            $ notificar_rpg("📜 FORMALIDADE", "Assinou o Termo do Grilhão sem objeções", "#aaaaaa")

            show elara encarando de cima para baixo at sprite_direita with dissolve

            elara "Quem assina um contrato draconiano sem negociar uma vírgula ou confia cegamente em mim... ou planeja quebrar cada linha na primeira oportunidade. Qual dos dois, Sr. Vane?"

            protagonist "Prefiro que a Presidente descubra com o tempo."

            show elara sorrindo com rosto arrogante at sprite_direita with dissolve

            elara "Ambas as respostas servem aos meus propósitos."

    "Pressiono a pena contra o pergaminho e assino. A tinta parece fria como gelo sob as pontas dos meus dedos."

    "No canto escuro do gabinete, o Diretor Ambrósio murmura baixinho, ajeitando a gravata borboleta: 'A Presidente tem toda a minha confiança... Tudo em perfeita conformidade com as diretrizes educacionais.'"

    show elara encarando de cima para baixo at sprite_direita with dissolve

    elara "Uma última coisa, Victor. O que você viu ontem na ala leste... e a pulsação colossal que sentiu sob o piso de pedra... não existiram."

    protagonist "Você também sentiu. O chão inteiro respondeu ao sangue dela."

    elara "Eu não senti nada. E se você valoriza o que sobrou da sua existência, esquecerá que o subsolo desta escola tem profundidade."

    "Ela mente. Duas vezes em doze horas, a mesma mentira arrogante vinda de quem me exige transparência absoluta."

    $ th_quebrar_regra(3)

    "A regra três das minhas anotações: nunca ser o último a saber. Cheguei ontem, estou há um dia nesta academia, e já querem me enterrar na ignorância."

    hide elara with dissolve

    hide victor with dissolve

    # ---- SAÍDA DO GABINETE & LIBERAÇÃO DO MAPA TÁTICO ------------------------

    scene bg animado corredor academia manha sol with fade

    $ th_musica("Safe_Within_the_Blue", 1.5)

    "Saio do Gabinete da Presidência e as pesadas portas de carvalho se fecham com um baque seco às minhas costas."

    "Solto a respiração que nem percebi que segurava. Minhas mãos ainda tremem, mas o mármore sob os meus sapatos é sólido."

    "Estou sob liberdade vigiada, com um Grilhão rúnico queimando no peito e a garganta seca como lixa. Mas estou vivo."

    "A partir de agora, as dependências da Academia São Cipriano estão abertas. Preciso explorar os setores, gerenciar minha sede e investigar o que esta escola esconde antes que a noite caia."

    $ notificar_rpg("🗺️ MAPA LIBERADO", "Acesso livre às dependências da Academia São Cipriano", "#00ffcc")

    $ modo_exploracao_livre = True
    $ passos_restantes_periodo = 3
    $ limite_visitas_periodo = 3
    $ visitas_restantes_periodo = 3
    $ locais_visitados_neste_periodo = []
    $ deslocando_pelo_mapa = False
    jump abrir_mapa_tatico

# ==============================================================================

# EVENTO MODULAR: A BIBLIOTECA E O CADERNO DE EMÍLIA (DIA 2)

# ==============================================================================

label evento_emilia_caderno_doacoes_dia2:

    call restaurar_fundo_local_atual

    $ th_musica("The_Unfinished_Lesson", 1.5)

    "No mural antes da biblioteca, um cartaz: 'Campanha Semestral de Saúde Comunitária. Dispensa de uma aula por doação. Créditos extras para bolsistas.'"

    "Dois alunos conversam diante dele, rindo. Um deles diz que ficou tonto na última coleta, mas ganhou a tarde livre. O outro pergunta para onde vai o sangue. O primeiro dá de ombros, ainda sorrindo."

    "Ninguém aqui parece ter medo da campanha. Só de quem não participa."

    show expression obter_sprite_victor("pensando") as victor at sprite_esquerda with dissolve

    show emilia uniforme seria triste meio corpo at sprite_direita with dissolve

    emilia "Senta. Não é um pedido, é um alerta."

    "Ela abre o caderno sobre a mesa. Três colunas à mão: data, nome, créditos. Páginas e páginas, frente e verso, numa letra miúda que não deixa respirar."

    $ th_voz("climax/emilia_climax_02_caderno")
    emilia "Doze alunos com mais de quarenta créditos de doação nos últimos dois semestres. Nenhum deles está matriculado hoje."

    show expression obter_sprite_victor("surpreso") as victor at sprite_esquerda with dissolve

    protagonist "Transferidos?"

    emilia "A lista de 'transferências voluntárias' tem exatamente os mesmos nomes da lista de doadores. Eu não sei para onde vão. Só sei que não é para outra escola."

    emilia "Esta escola trata os alunos comuns como um rebanho seguro, Victor. Fazem a gente pagar com uma coisa que acha que está dando."

    show emilia uniforme ajeitando oculos meio corpo at sprite_direita with dissolve

    if assinou_doacao_dia1 == "assinou":

        "O papel rubricado hoje cedo pesa mais do que devia dentro do bolso."

        protagonist "Eu assinei o termo hoje."

        show emilia preocupada at sprite_direita with dissolve

        emilia "Então você está na lista. A primeira coleta dos novos bolsistas é no dia seis, no Pátio da Fonte."

        emilia "Eu posso tentar mudar a sua data. Não posso prometer."

    elif assinou_doacao_dia1 == "leu":

        protagonist "Eu li a página dois. 'Fundação mantenedora.' Sem nome, sem endereço."

        show emilia uniforme surpresa meio corpo at sprite_direita with dissolve

        emilia "Você leu a página dois?! Em três anos, só eu li."

        "Pela primeira vez desde que a conheci, ela sorri sem tentar disfarçar. Dura dois segundos."

        emilia "A coleta dos novos é no dia seis, no Pátio da Fonte. Já que você leu, vai gostar de ver de perto."

    else:

        protagonist "Eu recusei assinar."

        show emilia uniforme sorriso amigavel meio corpo at sprite_direita with dissolve

        emilia "Ainda bem. Eles vão insistir. A recusa fica no registro, e eu odeio que fique, mas fica."

    $ th_boato("A primeira coleta dos novos bolsistas acontece no dia 6, no Pátio da Fonte.")

    protagonist "Por que você anota tudo isso?"

    show emilia uniforme sorriso timido meio corpo at sprite_direita with dissolve

    emilia "Meu pai diz que a memória é a primeira coisa que o medo apaga. Então eu escrevo. Se eu esquecer, o papel lembra por mim."

    protagonist "E o seu pai acredita no que você escreve?"

    emilia "Meu pai acredita em muitas coisas. Raramente em perguntas."

    show emilia uniforme seria triste meio corpo at sprite_direita with dissolve

    emilia "Agora a minha. A Júlia do bloco norte disse que você chegou ontem com o colarinho encharcado. Hoje, o seu pescoço não tem uma marca."

    emilia "O que aconteceu, Victor?"

    menu:

        "“Caí na escada. O sangue era de um nariz.” (+Dúvida Emília)":

            $ duvida_emilia += 1

            $ reagir_escolha("emilia", "agressao")

            $ notificar_rpg("⚠️ DIVERGÊNCIA", "+1 Dúvida Emília | Mentira óbvia", "#ffaa00")

            show emilia encarando seria neutra at sprite_direita with dissolve

            emilia "Um nariz sangra de baixo para cima. Um colarinho encharca de cima para baixo."

            emilia "Tudo bem. Não é uma acusação. Só mais uma linha no caderno."

        "“Fui atacado. Alguém me ajudou. Não posso dizer quem.” (+Afeto Emília / +Dúvida)":

            $ afeto_emilia += 1

            $ duvida_emilia += 1

            $ reagir_escolha("emilia", "gentileza")

            $ notificar_rpg("🕊️ CONFIANÇA PARCIAL", "+1 Afeto Emília | +1 Dúvida Emília | Honestidade contida", "#5c85d6")

            show emilia uniforme gentil meio corpo at sprite_direita with dissolve

            emilia "Obrigada por não mentir. Dizer 'não posso' é mais honesto do que a maioria."

            show emilia preocupada at sprite_direita with dissolve

            emilia "Mas quem ajuda de graça aqui costuma cobrar caro."

            "Ela acabou de descrever, sem saber, o meu dia inteiro."

        "“Quem te disse que eu estava sangrando?” (+Intelecto / +Dúvida)":

            $ intelecto += 1

            $ duvida_emilia += 1

            $ reagir_escolha("emilia", "ocultismo")

            $ notificar_rpg("📘 INTELECTO", "+1 Intelecto | +1 Dúvida Emília | Mapeou rede de boatos", "#00ffcc")

            show emilia com olhar investigativo at sprite_direita with dissolve

            emilia "A Júlia. A Júlia fala com a Bete, a Bete fala com o refeitório, e o refeitório sabe de tudo. Os boatos são a única rede que a escola não consegue vigiar."

            "Ela me entrega o jeito de ler esta escola numa frase só. Guardo o dado, sem agradecer. Agradecer é dever."

    "Emília hesita um instante, tocando o pequeno crucifixo sob o colarinho antes de responder à pergunta que eu sequer fiz."

    show emilia uniforme confiante meio corpo at sprite_direita with dissolve

    emilia "O que for necessário para que ninguém inocente se machuque. É só isso que eu quero."

    "A resposta me tranquiliza e me gela ao mesmo tempo. Para ela, proteger inocentes pode significar exterminar exatamente o que eu me tornei."

    # ---- DEDUÇÃO DE INVESTIGAÇÃO: O CADERNO E OS QUADROS DO 2º ANDAR -------
    if intelecto >= 2:
        "Meus olhos descem para o rodapé da terceira página. Três nomes de bolsistas estão riscados com caneta vermelha: Danilo Ramos, Camila Neves, Lucas Prado."

        show expression obter_sprite_victor("pensando") as victor at sprite_esquerda with dissolve

        protagonist "Esses três últimos da lista... Todos eles tinham aulas e dormitórios na ala leste do segundo andar?"

        show emilia com olhar investigativo at sprite_direita with dissolve

        emilia "Sim. Por que você reparou nisso?"

        protagonist "No meu primeiro dia aqui, passei três vezes diante da pintura a óleo do Fundador. Você mesma me avisou que os quadros desta escola sempre foram meio estranhos e que os olhos dele pareciam me seguir."

        scene cena victor emilia investigando quadros with dissolve

        "Caminhamos até o parapeito do mezanino, onde a fileira de molduras históricas vigia o corredor em silêncio sepulcral."

        protagonist "Ontem, ao passar por lá no entardecer, notei que o fundo da tela 'O Banquete de 1889' havia mudado. Havia sombras novas debaixo dos candelabros pintados... três figuras encolhidas usando o uniforme preto de bolsista."

        emilia "Meu Deus... O verniz de sacrifício."

        emilia "Os arquivos da minha família mencionam telas tratadas com cinza ritualística e óleo de linhaça impregnado de sangue antigo. O Barão Cipriano era obcecado por capturar o tempo antes que a morte o alcançasse."

        emilia "Se aquela pintura está sugando os alunos que se aproximam à noite... Victor, se você andar por aquele corredor durante o toque de recolher, mantenha distância da moldura. Quem aceita qualquer coisa do mundo pintado tem a carne e a alma absorvidas pela tela."

        $ conhece_misterio_quadros = True
        $ investigou_desaparecidos_emilia = True
        $ th_boato("A Galeria dos Esquecidos: O Banquete de 1889 no corredor leste engole alunos desaparecidos.")
        $ notificar_rpg("🖼️ PISTA: O BANQUETE DA FUNDAÇÃO", "A pintura a óleo do 2º andar guarda o rastro dos desaparecidos!", "#00ffcc")

        call restaurar_fundo_local_atual

    else:
        "Meus olhos passam pelos nomes riscados no caderno, mas a mente ainda está turva pela adaptação e pela sede. Há um padrão nos desaparecimentos, mas preciso de mais acuidade mental para conectá-lo ao campus. [[Requer Intelecto 2+ para deduzir o mistério dos quadros]]."

    hide emilia with dissolve

    hide victor with dissolve

    $ investigou_caderno_emilia_dia2 = True

    jump entrar_local_exploracao_bs

# ==============================================================================

# EVENTO MODULAR: AS CALDEIRAS E VALÉRIA (MERCADO NEGRO)

# ==============================================================================

label evento_conhecer_valeria_caldeiras:

    scene bg animado caldeiras loja pocoes tocha azul with fade

    $ th_musica("Iron_Lungs", 1.5)

    "Desço pelas escadas de serviço até o calor abafado das caldeiras, território da Turma do Fundão. O ar vibra com o ronco das tubulações. O vapor corre nos canos como sangue em artérias metálicas."

    show expression obter_sprite_victor("pensando") as victor at sprite_esquerda with dissolve

    show valeria cinica pirulito meio corpo at sprite_direita with dissolve

    $ th_bark("valeria", "padrao")

    $ th_voz("climax/valeria_climax_00_conhecer")
    valeria "Fecha a porta. O vapor custa caro."

    "Ela está sentada num caixote de madeira, separando moedas por peso com a ponta do indicador sem sequer olhar para elas."

    valeria "Você é o novo do corredor leste. O que sobreviveu à Nora."

    show expression obter_sprite_victor("surpreso") as victor at sprite_esquerda with dissolve

    protagonist "Como você sabe disso?"

    show valeria leve sorriso pirulito meio corpo at sprite_direita with dissolve

    valeria "Tudo o que cai nesta escola escorre para cá, garoto. Sangue, fofoca, dívidas e mercadoria que o Grêmio finge que não existe."

    valeria "Eu me chamo Valéria. Mas pode me chamar de quem resolve os seus problemas... se tiver como pagar."

    show valeria sorriso provocante pirulito meio corpo at sprite_direita with dissolve

    valeria "Eu tenho bolsas filtradas puras, gazes, chaves de armário e informações sobre quem manda de verdade neste inferno. Mas não faço fiado para recém-chegado."

    show expression obter_sprite_victor("confiante") as victor at sprite_esquerda with dissolve

    protagonist "Eu não vim pedir esmola."

    show valeria cinica confiante meio corpo at sprite_direita with dissolve

    valeria "Melhor ainda. Negociante com espinha dorsal é raro por aqui."

    hide valeria with dissolve

    hide victor with dissolve

    $ conheceu_valeria_caldeiras = True

    jump entrar_local_exploracao_bs

# ==============================================================================

# EVENTO MODULAR: A SALA DE MÚSICA & O PRIMEIRO TRANSE DE SANGUE (LILITY)

# ==============================================================================

label evento_primeiro_transe_lility:

    $ local_atual = "sala_musica"
    call restaurar_fundo_local_atual

    $ th_musica("The_Crimson_Chamber", 2.0)

    "A bolsa filtrada que peguei na enfermaria tinha gosto de plástico velho e cobre estragado. Meu estômago a rejeitou após dois goles, como um veneno morno que se recusa a descer."

    "Minhas mãos tremem incontrolavelmente. O pulsar das veias nos pescoços dos alunos ao meu redor e a queimação ácida na garganta estão me empurrando para o abismo."

    "A fome não é uma vontade. É uma ordem biológica, violenta e cega."

    "Empurro a porta carcomida da sala de música na ala interditada. O Grilhão de Sangue no meu peito arde suavemente, reconhecendo a presença de quem o selou."

    show lility triste olhando para baixo at sprite_padrao with dissolve

    "Sentada na borda do piano de cauda empoeirado, sob a luz que vaza pelos vitrais quebrados, minha mestra me observa em silêncio. Seus olhos carmesins analisam minha postura trêmula e o pavor estampado no meu rosto."

    mestra "Olhe só para você... Parado na soleira como um filhote resgatado de uma tempestade."

    mestra "Eu tirei você das garras da morte ontem à noite, mas parece que esqueci de te ensinar como continuar respirando neste mundo."

    "Ela desce do piano devagar, o tecido do vestido gótico farfalhando no silêncio pesado da sala. Por um breve instante, a expressão severa dela se desfaz em uma melancolia antiga e cansada."

    show lility vulneravel timida meio corpo at sprite_padrao with dissolve

    mestra "A ralé de uniforme branco bebe sangue filtrado porque tem pavor da própria natureza. Eles acham que se comportando como humanos bem-nascidos, o céu vai esquecer o que eles são."

    mestra "Uma mente vazia com sede de sangue é uma sentença de morte, Victor. Se eu deixar você vagando pelos corredores sem direção, os cães da Elara vão farejar o seu desespero e te despedaçar antes do fim da semana."

    protagonist "Por que você me deu o seu sangue ontem? Você não parece do tipo que faz caridade por ninguém."

    "A pergunta corta o ar. Ela para a poucos centímetros de mim, erguendo o rosto pálido."

    show lility meio corpo melancolica at sprite_padrao with dissolve

    mestra "Você estava estirado na pedra fria, com a traqueia aberta, cravando as unhas no chão e se recusando a apagar... Quando qualquer mortal comum imploraria a um deus surdo ou se entregaria às lágrimas."

    mestra "Fazia muito tempo que eu não via alguém lutar com tanta fúria por uma vida tão breve e insignificante. Eu senti pena. E talvez... um pouco de inveja desse fogo que os mortais carregam antes de virarem pó."

    show lility comportada sorriso meio corpo at sprite_padrao with dissolve

    "Ela ergue o braço direito e encara o próprio pulso pálido. Há uma hesitação sutil e inédita em seus dedos — o peso de quem não permite que ninguém se aproxime há muito tempo."

    mestra "Aqui fora, no nosso mundo, ninguém divide o sangue sem que haja uma faca apontada nas costas ou um estratagema político."

    $ th_voz("climax/lility_climax_03_primeiro_transe")
    mestra "Faz muito tempo que eu não compartilho um vínculo verdadeiro... que não deixo alguém entrar no Transe comigo."

    mestra "Pense nisso como quiser. Empréstimo, pagamento ou favor. Não tenha medo. Beba. Deixe que o meu sangue acalme o caos dentro de você."

    scene cena de lility provocando e insinuando a victor na sala de musica de noite antes de realizar a troca de sangue with dissolve

    "A pele dela é fria como mármore sob o luar, mas a proximidade é febril e hipnótica. Ela inclina a cabeça, exibindo o pulso pálido onde uma gota rubra reluz como rubi líquido."

    "Com as mãos trêmulas, seguro o braço dela. Meus lábios tocam a pele macia... e as presas afundam."

    # ---- TRANSE DE SANGUE: A CONEXÃO SENSORIAL -----------------------------

    call executar_transe_sangue("lility") from _call_executar_transe_sangue_6

    scene cena transe lility 1 at pulso_sensual_lento with flash_red

    "O sangue desce como brasa líquida pela minha garganta. O tremor convulsivo nos meus braços cessa no mesmo segundo."

    scene cena transe lility 2 at cena_lewd_ofegante with dissolve

    "Não há náusea. Não há o gosto de plástico ou ferrugem podre das bolsas da enfermaria. É poder concentrado, ancestral, queimando direto nas fibras dos meus músculos."

    scene cena transe lility 3 at cena_lewd_ofegante_rapida with dissolve

    "A sala de música desaparece. O mundo exterior deixa de existir. Duas mentes colidem através da ponte rubra."

    scene cena transe lility 4 at tremor_climax with dissolve

    "Eu sinto a respiração dela na minha nuca, mas não é o ar dos seus pulmões — é o peso avassalador de uma solidão profunda, um vazio tão denso que faz o meu peito doer."

    scene cena lility memoria diluvio with dissolve

    "Um vislumbre inexplicável corta a minha visão por uma fração de segundo: águas revoltas, sombras colossais... uma miragem tão rápida que mal consigo assimilar antes de desaparecer."

    "E então, no refluxo do pacto, sinto que a consciência dela invade as minhas próprias gavetas trancadas:"

    # ---- O CLÍMAX DO TRAUMA: LILITY DESVENDA A MEMÓRIA COMPLETA ------------

    scene cena passado victor 01 with dissolve

    "A mente dela escava o que eu passei meses tentando soterrar:"

    "O estacionamento na garoa. O sedã importado. O professor prensando a garota contra a lataria fria, as mãos forçando o casaco dela."

    scene cena passado victor 06 with dissolve

    "As algemas mordendo meus pulsos sem que ninguém me fizesse uma única pergunta."

    scene cena passado victor 08 with dissolve

    "O gabinete do delegado. O aperto de mãos do diretor da faculdade — o tio sorridente do canalha — comprando a cumplicidade da lei com um aceno de cabeça."

    scene cena passado victor 09 with dissolve

    "O termo de rendição empurrado sobre a mesa: confissão de culpa e expulsão sumária, sob ameaça de quatro anos de cadeia."

    scene cena passado victor 10 with dissolve

    "E a ferida que nunca fechou: a garota sentada no canto, com os olhos vermelhos e a cabeça baixa, assinando o depoimento forjado que me chamava de monstro. Me jogando aos cães para salvar a própria bolsa."

    scene cena passado victor 11 with dissolve

    "A madrugada seguinte na plataforma vazia. A mala gasta. O banimento para a capital."

    "Ela bebeu cada gota daquela humilhação. Ela viu onde cada uma das minhas quatro regras foi forjada."

    $ local_atual = "sala_musica"
    call restaurar_fundo_local_atual

    show lility meio corpo chocada at sprite_padrao with dissolve

    "O transe se rompe devagar. Nossas respirações estão curtas e entrecortadas. Ela me encara com os olhos arregalados, a mão ainda pousada na minha nuca."

    mestra "Um estacionamento cinzento... O cheiro de chuva e ferro... E uma garota covarde virando o rosto enquanto você era algemado."

    protagonist "...O quê?! Como você... Saia da minha cabeça!"

    show lility comportada sorriso meio corpo at sprite_padrao with dissolve

    mestra "O diretor da sua antiga faculdade sorriu antes de enfiar a faca no seu peito, não foi? Ele sorriu antes de exigir a sua rendição."

    mestra "E a tola que você tentou salvar te vendeu por um semestre de mensalidade paga. Que espetáculo patético da alma humana."

    "A segunda regra na minha carta: nunca confiar em quem sorri antes de pedir. E o motivo da minha primeira: nunca dever nada a ninguém. Eu nunca contei isso para uma única alma viva. E ela bebeu cada detalhe direto da minha essência."

    show lility meio corpo maravilhada at sprite_padrao with dissolve

    mestra "Mas o mais fascinante de tudo não foi o seu pequeno trauma de herói traído, cachorrinho..."

    "Ela passa a ponta da língua pelo canto dos lábios, onde uma gota rubra reluz com uma viscosidade e um brilho quase etéreos."

    $ th_voz("climax/lility_climax_03b_trauma")
    mestra "É o gosto do seu sangue. Rh Nulo... Sangue Dourado imaculado. A mesma seiva pura dos sacerdotes antediluvianos antes que os céus se rompessem."

    mestra "Agora eu entendo por que você sobreviveu à mordida daquela aberração sem se transformar em uma massa de carne podre. A sua carcaça foi feita sob medida para suportar o que está trancado nas profundezas desta academia." 

    protagonist "E o que foi aquilo que eu vi no seu sangue?! Águas negras, uma torre desabando... uma solidão que parecia ter séculos! Quantos anos você tem afinal?!"

    show lility meio corpo desdenhando at sprite_padrao with dissolve

    "Ela recolhe o pulso devagar, limpando a gota escarlate que restou nos lábios com o polegar. Um sorriso de puro escárnio e superioridade se desenha em seu rosto, fechando qualquer fresta de vulnerabilidade."

    mestra "O sangue é volátil, tolo. Quando duas naturezas se cruzam, a mente mortal preenche os vazios com delírios poéticos."

    mestra "E perguntar a idade de uma dama é uma grosseria imperdoável, cachorrinho. Especialmente de quem acabou de te dar comida e salvar o seu pescoço."

    mestra "Tudo o que você precisa saber é que o meu sangue te mantém de pé. O resto não é da sua conta."

    show lility bracos cruzados seria meio corpo at sprite_padrao with dissolve

    mestra "Agora que a sua cabeça parou de girar e a sua sede foi saciada sem alertar os carrascos de Elara, escute bem o seu objetivo, Victor."

    mestra "Antes de você aparecer, aquela puritana arrogante da Presidente me flagrou nas catacumbas e trancou dois artefatos que me pertencem por direito dentro do Cofre de Segurança Máxima do Grêmio."

    mestra "Com este Grilhão de Sangue nos meus pulsos, meus movimentos estão vigiados dia e noite. Mas você... você é livre para circular."

    protagonist "O que você quer que eu faça?"

    show lility confiante sorriso meio corpo at sprite_padrao with dissolve

    mestra "Você será os meus olhos e as minhas mãos fora desta prisão."

    mestra "Primeiro: investigue os porões das caldeiras. Há uma contrabandista chamada Valéria que lidera a 'Turma do Fundão' no mercado negro; eu tinha uma encomenda rúnica vindo por ela antes de ser confinada."

    mestra "Segundo: observe os passos da garota do Clube de Ocultismo, Emília. Ela anda farejando pergaminhos sobre a história antiga da escola."

    mestra "Terceiro: descubra as rotinas de Elara e o caminho até o cofre. Conforme você se alimentar e treinar nas Zonas de Perigo, o sangue que te dei despertará poderes latentes que a minha própria essência selada não pode mais manifestar."

    mestra "Sempre que a fome apertar e você precisar de alívio seguro sem elevar a sua Exposição perante o colégio, venha até mim nesta sala. Eu cuidarei de você."

    $ primeiro_transe_lility_realizado = True

    $ covil_sala_musica_ativo = True

    $ ressonancia_pre_diluviana += 1

    $ fome_sangue = 100

    $ notificar_rpg("🏰 COVIL DESBLOQUEADO", "A Sala de Música agora é seu refúgio seguro de alimentação | +1 Ressonância", "#9900ff")

    "Pela primeira vez desde que cheguei a esta academia maldita, a névoa do desespero se dissipa. Eu tenho uma dívida, um Grilhão no peito e uma mestra perigosa... mas tenho um rumo."

    jump entrar_local_exploracao_bs

# ==============================================================================

# EVENTO MODULAR: O BANHEIRO ABANDONADO & A LOIRA DO ESPELHO

# ==============================================================================

label evento_loira_banheiro_anomalia:

    $ local_atual = "banheiro_abandonado"
    scene bg animado banheiro abandonado luz vermelha piscando with dissolve

    $ th_musica("pulsao_sombra", 1.5)

    "O ar no banheiro interditado do segundo andar é gelado e tem cheiro de ferrugem, azulejos úmidos e um perfume barato de décadas passadas."

    "A lâmpada vermelha de emergência oscila no teto, projetando sombras retorcidas sobre o piso encharcado."

    "No centro da bancada de porcelana carcomida, repousa o espelho principal."

    scene cena espelho loira banheiro 1 with dissolve

    $ th_sfx("sussurros_espelho")

    "No centro do vidro fosco e salpicado de mofo, um halo desenhado em batom carmesim reluz com uma luminescência doentia."

    "Ao me aproximar, a imagem do meu próprio reflexo não acompanha os meus movimentos. A figura no vidro tem a cabeça inclinada, as pálpebras entreabertas e um meio sorriso que gela a espinha."

    "O vidro começa a tremer e a ranger sob uma pressão descomunal. O desenho de batom se retorce, e uma risada rouca, entrecortada por engasgos de água fria, reverbera nos azulejos."

    with vpunch

    scene cena espelho loira banheiro 2 with flash_red

    $ th_stinger("jumpscare")

    $ th_sfx("heartbeat")

    "O espelho se parte com o estampido de uma lâmina partindo osso!"

    "A Dama do Espelho — a Loira do Banheiro — rompe a barreira do reflexo! Garras pálidas e afiadas cravam na moldura estilhaçada, projetando um rosto de beleza cadavérica e olhos negros arregalados com um frenesi doentio."

    "O sorriso dela é uma fenda rubra manchada de batom e sangue seco que se estende de orelha a orelha."

    $ th_bark("outros", "loira")

    loira_banheiro "Eu farejo o que corre nessas suas veias de papel! O gosto roubado de uma linhagem pura... o cheiro de um lacaio que não sabe se é homem ou monstro!"

    loira_banheiro "Entregue a sua garganta para o vidro! Se você não tem coragem de se olhar no espelho... eu serei o seu reflexo para sempre!"

    menu:

        "Cravar os pés no chão e contra-atacar o bote espectral! (+1 Coragem)":

            $ coragem += 1

            $ notificar_rpg("🔥 RESOLUÇÃO", "+1 Coragem | Resistiu à Coerção do Espelho", "#ff8800")

            protagonist "Eu já tenho demônios demais cobrando o meu pescoço nesta academia. Você não vai ser mais uma na minha conta!"

        "Analisar o fluxo místico do halo de batom e romper a âncora! (+1 Intelecto)":

            $ intelecto += 1

            $ notificar_rpg("🧠 DEDUÇÃO TÁTICA", "+1 Intelecto | Fraqueza Espectral Identificada", "#4488ff")

            protagonist "O batom fecha o selo entre o vidro e a carne... Se eu atingir o centro da rachadura, o espectro perde o corpo!"

    # ---- BATALHA: A LOIRA DO BANHEIRO (ESPÍRITO DO ESPELHO) -----------------

    scene bg animado banheiro abandonado luz vermelha piscando with dissolve

    call iniciar_combate("A Loira do Banheiro (Espírito do Espelho)", "loira banheiro neutra", "loira banheiro ataque", 180, 26, 3.6, "inorganico", True, pode_fugir=False) from _call_iniciar_combate_8

    # ---- DESFECHO DA BATALHA ------------------------------------------------

    scene bg animado banheiro abandonado luz vermelha piscando with flash_red

    $ th_sfx("heartbeat")

    with vpunch

    "O golpe definitivo estilhaça o ponto de convergência do halo de batom! A força do impacto atravessa a imagem espectral da loira, desestabilizando o corpo etéreo que a mantinha presa à matéria."

    show loira banheiro neutra at bote_ataque with dissolve

    loira_banheiro "NÃÃÃO...! O espelho... não me deixe desaparecer no escuro outra vez...!"

    hide loira with dissolve

    with vpunch

    "Com um grito agudo que faz as lâmpadas e os espelhos de toda a ala vibrarem, a aparição explode em uma chuva de milhares de estilhaços cristalinos e névoa rubra gélida."

    "A pressão asfixiante que esmagava o meu peito se desfaz. O gotejar das torneiras silencia."

    $ derrotou_loira_banheiro = True

    $ giz_protecao += 1

    $ conhecimento_oculto += 2

    $ notificar_rpg("🪞 LENDA CONTIDA", "+1 Giz de Proteção | +2 Conhecimento Oculto", "#ff3333")

    if "loira_banheiro" in MISTERIOS_ACADEMIA:

        $ MISTERIOS_ACADEMIA["loira_banheiro"].coletar_pista("Fragmento de Batom Carmesim e a alma dispersa do espelho.")

        $ MISTERIOS_ACADEMIA["loira_banheiro"].concluir("A")

    protagonist "Mais um fantasma que esta escola tentou sepultar em silêncio. Uma anomalia a menos cobrando a minha garganta."

    jump entrar_local_exploracao_bs

# ==============================================================================

# LABELS DE COMPATIBILIDADE (SLOT LIVRE)

# ==============================================================================

# ==============================================================================

# EVENTO MODULAR: A MULHER DE OITO PÉS (HACHISHAKUSAMA NO CEMITÉRIO)

# ==============================================================================

label evento_hachishaku_anomalia:

    $ local_atual = "cemiterio_nevoa"
    scene bg cemiterio nevoeiro postes noite with fade

    $ th_musica("suspense_sombrio", 1.5)

    "A névoa sobre as lápides do cemitério está tão densa que mal consigo enxergar meus próprios sapatos. O ar cheira a terra revirada, flores murchas e ferro frio."

    "O fragmento do chapéu de palha no meu bolso arde com um calor espectral. A criatura sabe que a sua âncora foi violada."

    $ th_sfx("heartbeat")

    with vpunch

    "Um som gutural, abafado e cavernoso quebra o silêncio da noite, reverberando a poucos metros atrás de mim:"

    "“Po...{w=0.4} po...{w=0.4} po...”"

    show inimigo hachishaku mulher gigante vestido branco at sprite_colossal with vpunch

    $ th_stinger("jumpscare")

    $ th_bark("outros", "hachishaku")

    "Ela se ergue por trás de um mausoléu em ruínas. A silhueta é monumental — quase três metros de altura, vestindo um vestido de verão imaculado e um chapéu de abas largas que projeta uma sombra impenetrável sobre o rosto."

    "Sob a aba do chapéu, apenas um sorriso cadavérico e dois olhos desprovidos de vida me fitam fixamente. A pressão mística faz os ossos do meu crânio estalarem."

    hachishaku "Po... po... Você carrega um sangue que não te pertence, garoto... Entregue o seu pulso para a névoa..."

    menu:

        "“Eu não atravessei uma cidade inteira para virar banquete de fantasma!” (+Coragem)":

            $ coragem += 1

            $ notificar_rpg("🔥 RESOLUÇÃO", "+1 Coragem | Resistiu ao Terror Colossal", "#ff8800")

            protagonist "Eu já tenho dívidas demais cobrando a minha carne nesta escola. Uma lenda urbana não vai ditar onde eu caio!"

        "Espalhar o sal consagrado no solo e romper a projeção física! (+Intelecto)":

            $ intelecto += 1

            $ notificar_rpg("🧠 DEDUÇÃO TÁTICA", "+1 Intelecto | Fraqueza Dimensional Explorada", "#4488ff")

            protagonist "A fita rasgada do chapéu ancora a sua forma na pedra... Se o sal quebrar o círculo, a sua matéria se desfaz!"

    # ---- BATALHA: HACHISHAKUSAMA -------------------------------------------

    call iniciar_combate("Hachishakusama (A Mulher Gigante)", "inimigo hachishaku mulher gigante vestido branco", "inimigo hachishaku mulher gigante vestido branco ataque", 220, 30, 3.4, "inorganico", True, pode_fugir=False) from _call_iniciar_combate_9

    # ---- DESFECHO DA BATALHA -----------------------------------------------

    scene bg cemiterio nevoeiro postes noite with flash_red

    $ th_sfx("heartbeat")

    with vpunch

    "O impacto do golpe final atravessa o núcleo etéreo da aparição! O sal consagrado queima a barra do vestido branco em labaredas azuis."

    hachishaku "POOOOO...!"

    hide inimigo with dissolve

    with vpunch

    "Com um uivo espectral que ecoa pelos muros da academia, a mulher colossal se desfaz em uma chuva de cinzas prateadas e neblina dispersa."

    "O peso sufocante sobre o meu peito desaparece. No solo encharcado, resta apenas uma relíquia consagrada e um fragmento de giz."

    $ derrotou_hachishaku = True

    $ giz_protecao += 2

    $ conhecimento_oculto += 2

    $ notificar_rpg("👻 LENDA CONTIDA", "+2 Giz de Proteção | +2 Conhecimento Oculto", "#00ffcc")

    if "hachishaku" in MISTERIOS_ACADEMIA:

        $ MISTERIOS_ACADEMIA["hachishaku"].concluir("A")

    protagonist "A Mulher Gigante foi expurgada do cemitério. Uma anomalia a menos acelerando o fim deste lugar."

    jump entrar_local_exploracao_bs

# ==============================================================================

# EVENTO MODULAR: O LOTE NECRÓTICO DAS CALDEIRAS (ALQUIMISTA DO FUNDÃO)

# ==============================================================================

label evento_lote_necrotico_anomalia:

    scene bg animado caldeiras esconderijo tocha azul e fogo with fade

    $ th_musica("Iron_Lungs", 1.5)

    "Sigo o rastro de líquido esverdeado e fosforescente pelas galerias mais baixas das caldeiras. O calor aqui é sufocante, misturado a um odor repugnante de ácido sulfúrico e carne necrosada."

    "Numa câmara fechada atrás das tubulações mestras, avisto tonéis de sangue sendo manipulados clandestinamente."

    show inimigo fundao alquimista frasco verde arma at sprite_padrao with dissolve

    "Um homem com máscara de gás e jaleco de borracha manchado despeja um pó cinzento num tonel de sangue filtrado. Ao ouvir meus passos, ele se vira num solavanco, erguendo um frasco fumegante."

    alquimista_renegado "Quem mandou você aqui?! Os carrascos de uniforme branco da Presidente... ou aquela ratazana gananciosa da Valéria?!"

    alquimista_renegado "Não dou a mínima! Esse lote vai render o triplo na enfermaria e a culpa do frenesi vai cair na aberração trancada na sala de música!"

    menu:

        "“Adulterar o sangue para enlouquecer inocentes acaba aqui.” (+Humanidade)":

            $ humanidade = min(100, humanidade + 2)

            $ notificar_rpg("🕊️ PRINCÍPIO MORAL", "+2 Humanidade | Recusou a Crueldade Clandestina", "#88ccff")

            protagonist "Essa escola já tem monstros demais nas sombras. Você não vai lucrar envenenando quem mal consegue respirar."

        "“Você cometeu um erro de cálculo: sangue estragado me deixa com raiva.” (+Coragem)":

            $ coragem += 1

            $ notificar_rpg("🔥 RESOLUÇÃO", "+1 Coragem | Ameaça Predatória Direta", "#ff8800")

            protagonist "Você cometeu um erro primário de química, doutor: mexer com a comida de quem tem presas é garantia de pescoço quebrado."

    # ---- BATALHA: ALQUIMISTA RENEGADO ---------------------------------------

    call iniciar_combate("Alquimista Renegado do Fundão", "inimigo fundao alquimista frasco verde arma", "inimigo fundao alquimista frasco verde ataque", 150, 24, 3.6, "humano", True, pode_fugir=False) from _call_iniciar_combate_10

    # ---- DESFECHO DA BATALHA -----------------------------------------------

    scene bg animado caldeiras esconderijo tocha azul e fogo with flash_red

    $ th_sfx("heartbeat")

    with vpunch

    "Com um golpe certeiro no antebraço, quebro o frasco de reagente antes que ele possa arremessá-lo! O alquimista desaba de joelhos sobre a grelha de ferro, tossindo com as mãos algemadas pelas próprias tubulações."

    hide inimigo with dissolve

    show valeria cinica pirulito meio corpo at sprite_direita with dissolve

    valeria "Olha só... O novato tem dentes afiados e faro para desmanche clandestino."

    "Valéria surge das sombras da tubulação, batendo palmas lentas com um meio sorriso divertido."

    valeria "Esse desgraçado estava usando reagentes roubados do meu estoque para batizar bolsas da enfermaria. Se a Elara descobrisse, os carrascos iam descer aqui e fechar o meu mercado inteiro."

    valeria "Toma a sua comissão pela faxina, garoto. Negociante competente merece pagamento à vista."

    $ caso_lote_necrotico_resolvido = True

    $ dinheiro_jogador += 120

    $ bolsa_sangue_filtrado += 1

    $ afeto_valeria += 1

    $ notificar_rpg("🧪 LOTE PURIFICADO", "+$120 | +1 Bolsa Filtrada | +1 Afeto Valéria", "#2eb82e")

    if "lote_necrotico" in MISTERIOS_ACADEMIA:

        $ MISTERIOS_ACADEMIA["lote_necrotico"].concluir("A")

    hide valeria with dissolve

    protagonist "O lote necrótico foi destruído. O sangue que circula nas caldeiras agora é um pouco menos letal."

    jump entrar_local_exploracao_bs

# ==============================================================================

# EVENTO MODULAR: A PARTITURA CARNAL (A MARIONETE DE SANGUE NO PIANO)

# ==============================================================================

# ==============================================================================
# EVENTO MODULAR: A GALERIA DOS ESQUECIDOS (O MUNDO PINTADO DE DUNGEON MESHI)
# ==============================================================================

label evento_galeria_quadros_anomalia:

    # ---- VERIFICAÇÃO DE BARREIRA (GATING: INTELECTO 2+ E PISTA) -------------
    if not conhece_misterio_quadros or intelecto < 2:
        scene bg animado corredor escuro sombras with fade
        $ th_musica("The_Crimson_Chamber", 2.0)
        "O corredor do segundo andar está mergulhado na penumbra da Zona Vermelha. As molduras douradas dos retratos antigos reluzem opacas sob a luz da lua que vaza pelas janelas de chumbo."
        "Diante de mim repousa uma enorme tela a óleo: 'O Banquete da Fundação, 1889'. Doze nobres aristocratas brindam ao redor de uma mesa de mogno sob candelabros suntuosos."
        "O ar ao redor da tela é pesado e tem cheiro de terebintina velha, mas minha percepção ainda não é afiada o bastante para romper a barreira do verniz."
        $ notificar_rpg("⚠️ PERCEPÇÃO INSUFICIENTE", "Requer investigar o Caderno de Emília e possuir Intelecto 2+.", "#ffaa00")
        "Afasto-me da parede antes que a ronda do Grêmio me encontre fora do dormitório."
        jump entrar_local_exploracao_bs

    # ---- EVENTO LIBERADO: A ANOMALIA DA TELA DE ÓLEO ------------------------
    scene cena victor galeria corredor observando with fade

    $ th_musica("The_Crimson_Chamber", 2.0)

    "O corredor do segundo andar cheira a óleo de linhaça podre, terebintina e ferro secular. À noite, a moldura entalhada em ouro parece pesada demais para a pedra da parede."

    "Paro diante da tela monumental: 'O Banquete da Fundação, 1889'."

    "Na manhã do meu primeiro dia, havia doze nobres brindando na pintura. Agora, meus olhos contam com clareza clínica: há quinze pessoas sobre o linho."

    "As três últimas estão espremidas no canto escuro do salão pintado, atrás da pilastra. Três adolescentes. Vestem o uniforme preto de bolsista da São Cipriano. A pele deles tem a textura grossa de pinceladas secas de tinta cinzenta, e seus dedos esmurram o verniz de dentro para fora em um desespero mudo."

    protagonist "Danilo Ramos... O garoto da lista da Emília."

    "Quando aproximo o rosto do linho, o verniz estala com o som de gelo quebrando. Um calor súbito e avassalador vaza da pintura, trazendo o aroma de carne assada, frutas silvestres e cálices de sangue puro e quente — um banquete suntuoso e proibido que atinge o estômago de Ghoul como uma navalha em brasa."

    "Na cabeceira da mesa pintada, o Fundador — o Barão Cipriano — vira o pescoço num ângulo seco e antinatural. Um pincel invisível redesenha os lábios dele em tempo real, esticando um sorriso patronal e predatório."

    "Ele ergue uma taça transbordando em líquido escarlate diretamente na minha direção."

    voz_do_quadro "Frio aí fora, não é, Sr. Vane? O mundo dos homens cobra juros a cada batimento. Mas aqui dentro... a mesa está sempre posta. Sem fome. Sem dívidas. Dê apenas um passo."

    "A moldura sangra gotas espessas de óleo escuro sobre o rodapé. Os dedos dos estudantes aprisionados batem contra a superfície invisível da tela, balançando a cabeça em pânico absoluto, implorando para que eu não aceite."

    menu:
        "Tocar a taça e provar do banquete pintado (A Fome exige alívio imediato)":
            scene cena victor banquete dentro do quadro with flash_red
            "Minha garganta queima. A promessa de saciedade infinita anestesia as minhas defesas."
            "Estendo os dedos e toco a borda da taça. A tela cede como água morna e espessa."
            "O calor invade meus braços... mas quando tento puxar o corpo de volta, minha pele ganha a textura rígida e quebradiça do linho cru."
            "Olho para fora da moldura. O corredor da academia agora parece uma gravura bidimensional, distante e cinzenta. Minha voz não passa de uma camada de verniz transparente."
            "Um garoto de uniforme preto me passa um prato vazio. O Barão sorri e brinda ao meu lado."
            "Eu nunca mais senti sede. E nunca mais desci da parede do segundo andar."
            jump morte_definitiva

        "Atirar o Solvente/Absinto das Caldeiras contra a assinatura do Fundador! [[Requer: 1x Estimulante]]" if dose_estimulante > 0:
            $ dose_estimulante -= 1
            $ intelecto += 1
            $ cracha_aluno_desaparecido = True
            $ pigmento_alma_coletado = True
            $ quadro_banquete_resolvido = True
            $ ruina_cain = max(0, ruina_cain - 10)

            scene cena victor destruindo quadro acido with flash_green
            "Puxo o frasco concentrado de reagente químico do bolso e arremesso o líquido cáustico diretamente sobre a assinatura dourada no canto da pintura!"
            "A reação química ferve com um chiado ensurdecedor de ácido. O óleo de linhaça borbulha em fumaça esmeralda, derretendo a perspectiva da sala de jantar."
            "O rosto do Barão se desmancha em uma pasta preta e disforme. A ilusão desaba em farrapos de tinta fresca!"

            scene cena victor acha id quadro with dissolve
            "Com um estalo seco de verniz quebrado, algo metálico despenca de dentro da tela rasgada e tilinta no chão de pedra."
            "Abaixo-me e recolho o objeto: é um crachá de metal com o nome gravado: {b}Danilo Ramos — Bolsista de Música nº 18{/b}."

            scene cena victor examina id close with dissolve
            "Aproximo a placa de metal dos olhos sob a fresta de luz. É a prova definitiva da extorsão da mantenedora. E, na borda da moldura trincada, raspo três lascas brilhantes de Pigmento de Alma condensado."
            $ notificar_rpg("🧪 PINTURA DILUÍDA", "Crachá nº 18 resgatado | +1 Intelecto | +Pigmento de Alma | -10% DOOM", "#2eb82e")
            "A pintura volta a ser uma tela morta e inerte. Uma das armadilhas da mantenedora acaba de ser neutralizada."
            call restaurar_fundo_local_atual
            jump entrar_local_exploracao_bs

        "Cortar a palma e envenenar a tela com Sangue de Ghoul! (-15 HP / Requer: Coragem 2+)" if coragem >= 2:
            $ hp_jogador = max(10, hp_jogador - 15)
            $ coragem += 1
            $ ressonancia_pre_diluviana += 1
            $ pista_cofre_quadro = True
            $ quadro_banquete_resolvido = True
            $ ruina_cain = max(0, ruina_cain - 10)

            scene bg animado corredor escuro sombras with flash_red
            $ th_sfx("heartbeat")
            "Se esta tela se alimenta de almas fracas e sangue mortal, a maldição pré-diluviana que corre em minhas veias é veneno puro para a ilusão de um nobre decadente."
            "Passo a unha sobre a palma da mão direita, abrindo um talho rubro. Pressiono a carne aberta contra o peito do Fundador na pintura!"
            "O impacto reverbera como um trovão subterrâneo. O sangue rubro ferve e queima o linho como brasa viva."
            "Por três segundos, o véu da arte se rasga: sou puxado para o vazio da sala de jantar onde o estudante aprisionado agarra meu braço antes que o feitiço colapse."
            aluno_pintado "Obrigado... O cofre... Arquivo dos Fundadores... Código trinta e um, zero oito... A Diretoria sabia de tudo..."
            "O mundo pintado se estilhaça e sou cuspido com violência contra o piso frio do corredor!"
            $ notificar_rpg("🩸 VENENO DE GHOUL", "Pista do Cofre Obtida | +1 Coragem | +1 Ressonância | -10% DOOM", "#ff2244")
            "Ofegante, estanco o corte na mão. O quadro agora é apenas um emaranhado de cinzas e verniz queimado."
            jump entrar_local_exploracao_bs

        "Conter a respiração, desviar os olhos e recuar com frieza.":
            scene bg animado corredor escuro sombras with dissolve
            "A regra dois martela no meu crânio: nunca confiar em quem sorri antes de oferecer. E aquele homem na tela sorri como um agiota de almas."
            "Travo os calcanhares. Dou três passos para trás sem desgrudar a mão da lâmina, até que a escuridão do corredor engula a luz do banquete."
            "Ainda não é a hora. Mas agora eu sei o que a escola esconde atrás da tinta."
            jump entrar_local_exploracao_bs

# ==============================================================================
# DESDOBRAMENTO: ENTREGA DE EVIDÊNCIAS À EMÍLIA E VALÉRIA
# ==============================================================================

label entregar_cracha_emilia:
    call restaurar_fundo_local_atual
    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve
    show emilia uniforme seria triste meio corpo at sprite_direita with dissolve

    protagonist "Emília. Eu estive no corredor leste durante a noite."
    "Pouso o crachá de metal manchado de óleo sobre a mesa de carvalho."

    show emilia uniforme surpresa meio corpo at sprite_direita with dissolve
    "Ela recolhe a placa de identificação com as pontas dos dedos trêmulas. Seus olhos lêem o nome em voz baixa."
    emilia "Danilo Ramos... O garoto da turma de violino."
    show emilia preocupada at sprite_direita with dissolve
    emilia "A administração jurou para os pais dele que ele havia embarcado de volta para o interior. Ele estava... ele estava dentro daquela pintura o tempo todo?"
    protagonist "O Barão Cipriano deixou armadilhas vivas nesta escola. Quem não tem dinheiro ou quem perde o controle da dívida acaba servindo de combustível para a tela."
    emilia "Obrigada por resgatar a verdade, Victor. Meu pai sempre disse que a compaixão em uma terra amaldiçoada é uma fraqueza... mas ver você trazer isso de volta me prova que ele estava errado."

    $ afeto_emilia += 3
    $ confianca_emilia += 2
    $ humanidade = min(100, humanidade + 3)
    $ entregou_cracha_emilia = True
    $ notificar_rpg("🕊️ MEMÓRIA RESGATADA", "+3 Afeto Emília | +2 Confiança | +3 Humanidade", "#5c85d6")
    jump entrar_local_exploracao_bs

label negociar_pigmento_valeria:
    scene bg animado caldeiras esconderijo tocha azul e fogo with dissolve
    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve
    show valeria cinica pirulito meio corpo at sprite_direita with dissolve

    protagonist "Valéria. Tenho algo que pode te interessar."
    "Coloco o frasco com as lascas de Pigmento de Alma sobre a bancada de ferro."

    show valeria olhar focado meio corpo at sprite_direita with dissolve
    "Ela apaga o pirulito e pega uma das lascas com uma pinça de relojoeiro, examinando o brilho arroxeado sob a chama da tocha azul."
    valeria "Verniz de sacrifício da galeria histórica... Garoto, você tem faro para coisa perigosa. Os falsificadores do Conselho pagam uma fortuna por isso para selar salvo-condutos falsos."
    valeria "Toma aqui: cento e cinquenta créditos à vista. Negócio limpo com quem sabe sujar as mãos."

    $ dinheiro_jogador += 150
    $ afeto_valeria += 1
    $ vendeu_pigmento_valeria = True
    $ notificar_rpg("💰 VENDA CLANDESTINA", "+150 Créditos | +1 Afeto Valéria | Pigmento Negociado", "#2eb82e")
    jump entrar_local_exploracao_bs

label evento_partitura_carnal_climax:

    scene bg animado sala musica piano noite with fade

    $ th_musica("The_Crimson_Chamber", 2.0)

    "Empurro a porta da sala de música com as três estrofes recuperadas da Partitura Carnal entre os dedos. As pautas emitem um calor elétrico que arde na palma da minha mão."

    show lility meio corpo maravilhada at sprite_padrao with dissolve

    mestra "Você reuniu as estrofes... Que cachorrinho dedicado e obstinado."

    "Ela desce do tampo do piano e seus dedos pálidos deslizam sobre os manuscritos amarelados."

    mestra "Eu compus este réquiem há muito tempo, Victor... Na noite em que as primeiras águas negras começaram a subir. Cada compasso é uma âncora que puxa a essência do abismo para a superfície."

    $ th_voz("climax/lility_piano_transe")
    mestra "Você teve coragem de juntar as notas. Toque a dissonância, Victor... Deixe as teclas de marfim beberem a gota rubra antes que a aurora rompa."

    "Ela se senta diante do teclado de marfim empoeirado. Seus dedos tocam os primeiros acordes com uma ferocidade majestosa."

    "As notas vibram nas paredes, fazendo as vidraças rachadas ressoarem. O piso sob os meus pés treme... e do teto de madeira desaba uma teia de fios carmesins que se retorcem no ar!"

    show inimigo marionete fios sangue flutuando at sprite_padrao with vpunch

    $ th_stinger("anomalia")

    "Uma marionete etérea tecida em fios de sangue puro ganha vida ao som da música, brandindo garras de pura ressonância pré-diluviana!"

    menu:

        "“Toque até o fim! Eu cuido do que sair do chão!” (+Coragem / +Afeto com [nome_display_mestra])":

            $ coragem += 1

            $ afeto_mestra += 1

            $ notificar_rpg("🔥 RESOLUÇÃO", f"+1 Coragem | +1 Afeto {nome_display_mestra} | Manteve a Conexão no Caos", "#9900ff")

            protagonist "Não pare de tocar! Eu não passei por tudo isso para recuar diante de uma boneca de sangue!"

        "Analisar o ponto de tensão dos fios e cortar o elo motriz! (+Intelecto)":

            $ intelecto += 1

            $ notificar_rpg("🧠 DEDUÇÃO TÁTICA", "+1 Intelecto | Fraqueza Estrutural Cortada", "#00ffcc")

            protagonist "Os acordes mantêm os fios tensos... Se eu romper o ponto de convergência no peito dela, a estrutura desaba!"

    # ---- BATALHA: MARIONETE DE FIOS DE SANGUE ------------------------------

    call iniciar_combate("Marionete de Fios de Sangue", "inimigo marionete fios sangue flutuando", "inimigo marionete fios sangue ataque", 145, 24, 3.6, "corrompido", True, pode_fugir=False) from _call_iniciar_combate_11

    # ---- DESFECHO DA BATALHA -----------------------------------------------

    scene bg animado sala musica piano noite with flash_red

    $ th_sfx("heartbeat")

    with vpunch

    "O golpe definitivo corta o feixe principal de sustentação! Os fios de sangue se partem com estalos secos, dissolvendo a marionete em uma névoa carmesim que é absorvida pelo meu próprio peito."

    show lility comportada sorriso meio corpo at sprite_padrao with dissolve

    mestra "Impressionante... Você não apenas suportou as frequências do Dilúvio como decepou o eco da partitura com precisão cirúrgica."

    "Ela recolhe as folhas da partitura e as dobra com cuidado antes de entregá-las a mim."

    mestra "Guarde isso com a sua vida. Quando a hora da descida final chegar, este manuscrito abrirá o que as mãos mortais jamais conseguirão tocar."

    $ caso_partitura_resolvido = True

    $ tem_partitura_runica = True

    $ ressonancia_pre_diluviana += 2

    $ afeto_mestra += 1

    $ notificar_rpg("🎹 RÉQUIEM CONCLUÍDO", f"+1 Partitura Rúnica | +2 Ressonância | +1 Afeto {nome_display_mestra}", "#aa00ff")

    if "partitura_carnal" in MISTERIOS_ACADEMIA:

        $ MISTERIOS_ACADEMIA["partitura_carnal"].concluir("A")

    hide lility with dissolve

    protagonist "A Partitura Carnal foi dominada. Mais um artefato primordial sob o meu controle."

    jump entrar_local_exploracao_bs

# ==============================================================================

# EVENTO MODULAR: OS ARQUIVOS MORTOS (INQUISIÇÃO NO GABINETE DO GRÊMIO)

# ==============================================================================

label evento_inquerito_inquisicao_climax:

    scene bg animado gabinete diretor noite candelabro with fade

    $ th_musica("The_Cold_Decree", 1.5)

    "Aproveito a penumbra do gabinete vazio durante a troca de turnos da guarda. A chave obtida nas pistas abre com perfeição a gaveta com fundo falso atrás da escrivaninha de mogno de Elara."

    "Retiro uma pasta grossa timbrada com o selo eclesiástico da Inquisição. Diante dos meus olhos, a lista de doações e sacrifícios voluntários confirma a fraude: alunos bolsistas sendo sistematicamente entregues para manter a barreira do colégio estável."

    $ th_sfx("heartbeat")

    with vpunch

    "Um estalo metálico seco ecoa do balcão de vitrais:"

    show inimigo inquisidor tatico balestra at sprite_padrao with dissolve

    inquisidor_tatico "Documentos confidenciais da cúria não são para os olhos de um ghoul recém-criado."

    inquisidor_tatico "Lorde Phillip foi claro: nenhum registro do pacto sobrevive à auditoria desta semana. Entregue os arquivos ou a sua cabeça será pregada no portão principal antes do amanhecer!"

    menu:

        "“Esses arquivos são a prova de que esta escola é um abatedouro. Não vou devolvê-los.” (+Humanidade / Credo de Victor)":

            $ humanidade = min(100, humanidade + 2)

            $ notificar_rpg("🕊️ DETERMINAÇÃO MORAL", "+2 Humanidade | O Credo de Victor", "#88ccff")

            protagonist "Eu já fui descartado uma vez por mentores covardes que escondiam as próprias fraudes. Não vou deixar vocês fazerem o mesmo com o resto destes alunos."

        "“Você atira devagar demais para quem caça predadores.” (+Coragem)":

            $ coragem += 1

            $ notificar_rpg("🔥 RESOLUÇÃO", "+1 Coragem | Provocação no Foco de Mira", "#ff8800")

            protagonist "Balestra pesada, mira trêmula e ordens de burocratas... Vamos ver se a sua prata corta mais rápido do que as minhas presas."

    # ---- BATALHA: INQUISIDOR TÁTICO ----------------------------------------

    call iniciar_combate("Inquisidor Tático", "inimigo inquisidor tatico balestra", "inimigo inquisidor tatico balestra ataque", 155, 25, 3.5, "humano", True, pode_fugir=False) from _call_iniciar_combate_12

    # ---- DESFECHO DA BATALHA -----------------------------------------------

    scene bg animado gabinete diretor noite candelabro with flash_red

    $ th_sfx("heartbeat")

    with vpunch

    "O golpe definitivo parte o arco da balestra e arremessa o inquisidor contra a estante de arquivos pesados! Ele cospe sangue, rola pela sacada aberta e salta para os telhados na escuridão."

    hide inimigo with dissolve

    "Recolho a pasta com as provas documentais completas e a enfio por dentro do meu casaco. O segredo mais bem guardado do Conselho Estudantil agora está nas minhas mãos."

    $ caso_inquerito_resolvido = True

    $ emilia_conhece_a_verdade = True

    $ conhecimento_oculto += 3

    $ dominio_jogador += 1

    $ notificar_rpg("📜 VERDADE DESENTERRADA", "+3 Conhecimento | +1 Domínio | Emília Sabe a Verdade", "#00ffcc")

    if "inquerito_inquisicao" in MISTERIOS_ACADEMIA:

        $ MISTERIOS_ACADEMIA["inquerito_inquisicao"].concluir("A")

    protagonist "O inquérito da Inquisição foi assegurado. Agora eu tenho alavancagem contra quem achava que podia me usar como peça descartável."

    jump entrar_local_exploracao_bs

# ==============================================================================
# EVENTO ORGÂNICO (ENFERMARIA): A TRIAGEM CLÍNICA E O SANGUE DOURADO (CLARA)
# ==============================================================================

label evt_d02_tarde:

    $ ev_triagem_dia2_visto = True
    $ local_atual = "enfermaria"
    call restaurar_fundo_local_atual

    $ th_musica("The_Unfinished_Lesson", 1.5)
    $ th_sfx("passos_madeira")

    "O cheiro de éter e ferro hospitalar queima as narinas assim que empurro a porta de vidro fosco da enfermaria."

    "Uma exigência da Presidência do Grêmio: todo novo monitor bolsista é obrigado a passar por triagem física antes de receber o abono do mês."

    show mob enfermeira desconfiada at sprite_direita with dissolve

    $ th_voz("mobs/mob_enfermeira_f2")

    mob_enfermeira "Sente-se na cadeira de exames, senhor Vane. Não temos a tarde toda. A Presidência do Grêmio exige o boletim clínico de todos os novos monitores antes do toque de recolher."

    "Ela ajusta o estetoscópio com movimentos mecânicos e gélidos. O disco de metal toca o meu peito através do linho da camisa."

    $ th_sfx("heartbeat")

    "O silêncio na sala se prolonga por tempo demais. A expressão da enfermeira se fecha."

    mob_enfermeira "Respira fundo... De novo."

    mob_enfermeira "Estranho. O ritmo cardíaco mal atinge vinte batimentos por minuto. E sua temperatura cutânea... está em trinta e um graus cravados."

    "Ela afasta o estetoscópio e pega uma seringa estéril da bandeja de inox."

    mob_enfermeira "Arregace a manga esquerda. Preciso de uma amostra para a contraprova hematológica da Fundação."

    "A agulha penetra na veia do meu antebraço. O êmbolo recua devagar."

    "O líquido que preenche o tubo de vidro não tem a cor de um sangue humano comum. É um carmim denso, quase negro, que projeta reflexos de âmbar dourado sob a lâmpada fria de mercúrio."

    mob_enfermeira "Mas o que... Isto não é apenas Rh-nulo. O plasma parece emitir refração própria... Biologicamente, senhor Vane, suas hemácias estão em torpor cristalino. Qualquer legista diria que esse tecido pertence a um cadáver embalsamado... ou a algo que nunca deveria ter despertado."

    $ th_voz("mobs/mob_calouro_anemico_apelo")

    "Um gemido rouco e agonizante ecoa por trás da cortina amarela da maca três."

    "Voz Fraca Atrás da Cortina" "A-Água... por favor... minha cabeça não para de girar... Eles tiraram... três bolsas..."

    "A enfermeira lança um olhar rápido e tenso na direção da divisória, baixando a voz até um sussurro afiado."

    mob_enfermeira "Não dê atenção ao bolsista na maca três. A Fundação colheu três bolsas dele hoje cedo para a 'Campanha de Saúde Comunitária'. Mais dois dias nesse ritmo e o coração dele desiste."

    mob_enfermeira "Agora me diga, senhor Vane... Que diabo de diagnóstico você espera que eu escreva nesta ficha?"

    menu:
        "Subterfúgio: \"Anote anemia severa por estresse acadêmico. O Grêmio não precisa saber além disso.\" (+Subterfúgio)":
            $ subterfugio += 1
            $ duvida_elara = max(0, duvida_elara - 1)
            $ notificar_rpg("🎭 DISSIMULAÇÃO", "+1 Subterfúgio | Laudo Clínico Camuflado", "#00ffcc")
            protagonist "Anote que a carga horária de monitoria e a desnutrição estão cobrando seu preço. Uma mentira técnica mantém a Fundação longe do meu pescoço e protege a sua licença médica."
            mob_enfermeira "Você pensa rápido demais para quem mal tem pulso... Muito bem. Vou carimbar como Anemia Ferropriva Crônica com restrição de esforços físicos."

        "Ameaça velada: \"Se esse laudo chegar às mãos erradas, o desvio de plasma desta sala será o menor dos seus problemas.\" (+Domínio)":
            $ dominio_jogador += 1
            $ notificar_rpg("👁️ DOMÍNIO", "+1 Domínio | Silêncio Assegurado", "#ff4444")
            protagonist "Eu vi as faturas de desvio sob o balcão, Clara. Se o meu nome aparecer em relatórios da Inquisição ou da Fundação, a presidência vai descobrir exatamente para onde vão as bolsas que somem da câmara fria."
            mob_enfermeira "Você... está blefando. Mas não posso correr esse risco. Vou atestar quadro anêmico padrão e arquivar sua ficha no fundo do armário."

    $ dinheiro_jogador += 50
    $ notificar_rpg("🩺 TRIAGEM CONCLUÍDA", "+$50 Créditos de Monitoria | Prontuário Arquivado", "#00ffcc")

    mob_enfermeira "Aqui está seu auxílio de monitoria adiantado pelo comitê. E escute bem o meu conselho, senhor Vane: recolha-se ao seu dormitório antes das dezoito."

    mob_enfermeira "Se a Presidente Elara ou os inspetores da Fundação sentirem o odor dessa amostra nos seus dedos, a próxima maca com a cortina fechada será a sua."

    hide mob with dissolve
    hide enfermeira with dissolve

    jump entrar_local_exploracao_bs

# ==============================================================================
# EVENTO ORGÂNICO (BANHEIRO ABANDONADO): O HALO DE BATOM NO ESPELHO
# ==============================================================================

label evt_d02_noite:

    $ ev_halo_espelho_banheiro_visto = True
    $ local_atual = "banheiro_abandonado"
    scene bg animado banheiro abandonado luz vermelha piscando with fade

    $ th_musica("The_Cold_Decree", 2.0)
    $ th_sfx("passos_madeira")

    "O silêncio do sanitário interditado do segundo andar é mais pesado do que o frio das pedras seculares da academia."

    $ th_stinger("sombra_passando")

    "As lâmpadas de emergência piscam em um carmesim intermitente. A secura da sede raspa o fundo da minha garganta enquanto caminho até os lavatórios de porcelana."

    scene cena halo batom espelho 1 with dissolve

    "Paro no meio do banheiro abandonado. O vapor frio embaçou o espelho rachado sobre a pia."

    "Mas no centro do vidro, desenhado com um traço firme de batom carmim, há um halo perfeito. Um círculo sacrificial traçado exatamente na altura onde o crânio de quem se curva sobre a pia deveria ficar."

    scene cena halo batom espelho 2 with dissolve

    "Dou um passo à frente. Minha silhueta se encaixa com precisão milimétrica dentro do contorno vermelho."

    "No reflexo, meus olhos reluzem como brasas sob a penumbra vermelha. E por um instante aterrorizante, vejo o reflexo piscar uma fração de segundo depois de mim."

    "Lembro-me das quatro regras sussurradas pelos bolsistas antigos sobre os espelhos desta ala:"

    "Primeira: Jamais lavar o rosto no segundo andar após o toque das seis."

    "Segunda: Jamais responder a sussurros que chamem pelo seu nome de batismo atrás das cabines."

    "Terceira: Nunca olhar para trás se o vapor formar um halo sobre a sua cabeça no vidro."

    "Quarta: Se a sua imagem no espelho sorrir antes de você... saia sem fechar os olhos."

    menu:
        "Abraçar a frieza predatória: \"O reflexo no espelho não é uma ameaça. É a minha única garantia de sobrevivência.\" (+1 Coragem)":
            $ coragem += 1
            $ notificar_rpg("🔥 RESOLUÇÃO", "+1 Coragem | Consciência Predatória", "#ff8800")
            "Respiro fundo e sustento o olhar daquela criatura no vidro. Se os espectros desta ala esperam uma presa dócil, vão quebrar os dentes."

        "Lutar para preservar a humanidade: \"Ainda sou Victor Vane. Nenhum grilhão de sangue vai me transformar em um monstro descartável.\" (+1 Humanidade)":
            $ humanidade = min(100, humanidade + 1)
            $ notificar_rpg("🕊️ HUMANIDADE", "+1 Humanidade | Resistência Moral", "#55aaff")
            "Passo a manga do casaco sobre o vidro com força, borrando o círculo carmim até transformá-lo em uma mancha sem forma. Minha alma ainda me pertence."

    call restaurar_fundo_local_atual

    $ th_sfx("passos_madeira")

    "Recuo um passo da pia rachada. Algo antigo vigia este sanitário... e o rastro da anomalia está mais perto do que parece."

    jump entrar_local_exploracao_bs

# ==============================================================================

label evt_d03_manha:
    # --- DIA 3+: A CARTEIRA VAZIA, A PACIENTE 31 E O AVISO DE CLARA ---
    $ ev_carteira_nora_visto = True
    $ local_atual = "biblioteca"
    call restaurar_fundo_local_atual

    if renpy.loadable("audio/the_keepers_ledger.ogg"):

        play music "audio/the_keepers_ledger.ogg" fadein 1.5

    "Nos Dias 3 e 4, percebo uma carteira vazia no fundo da sala com o nome raspado na madeira. Os alunos desconversam: uns dizem que a colega nunca existiu; outros, que foi transferida."

    play sound "audio/sfx/sfx_psiquico_distorcao_sanidade.ogg"
    $ th_voz("climax/nora_carteira_vazia")
    "Ao passar os dedos pela madeira arranhada, um sussurro gelado vibra na minha mente: 'Meu nome estava no livro antes de apagarem... Trinta e Um! Eu sou a Paciente Trinta e Um!'"

    "No arquivo médico anexo, encontro os pertences recolhidos da Ghoul Rival que me atacou no Dia 1: um cartão de estudante, uma folha de exercícios corrigidos e um bilhete amassado dizendo 'Não se esqueça de me esperar depois da aula'."

    show mob enfermeira desconfiada at sprite_direita with dissolve
    $ th_voz("climax/enfermeira_climax_01_nora")
    mob_enfermeira "A paciente trinta e um foi transferida voluntariamente segundo os registros oficiais, senhor Vane. Se continuar mexendo nesses prontuários, a próxima maca que esvaziaremos será a sua."
    "A Enfermeira Clara recolhe a prancheta de metal das minhas mãos com frieza cirúrgica, trancando o arquivo médico antes de desaparecer entre os biombos da enfermaria."
    hide mob with dissolve

    show expression obter_sprite_victor("padrao") as victor at sprite_esquerda with dissolve

    show emilia uniforme seria triste meio corpo at sprite_direita with dissolve

    emilia "Você está olhando esses pertences há cinco minutos, Victor. Ela tentou matar você naquela noite, não foi?"

    protagonist "Sim. Mas enquanto eu lembrar apenas do ataque, fica fácil fingir que ela nasceu sendo um monstro. Se eu esquecer quem ela era antes, fica fácil fazer o mesmo com qualquer pessoa."

    show emilia uniforme ajeitando oculos meio corpo at sprite_direita with dissolve

    emilia "O nome dela foi alterado para 'transferida' no sistema oficial, Victor. Mentir é uma pessoa escondendo a verdade; alterar os registros significa que a instituição inteira quer que a mentira sobreviva."

    emilia "Eu estou fazendo perguntas porque quero acreditar em você... mas você ainda não me contou como sobreviveu àquele corredor."

    protagonist "Você acha que eu sou seu inimigo, Emília?"

    emilia "Você acha que eu sou?"

    protagonist "Acho que você ainda não decidiu o que eu sou."

    menu:

        "Admitir parte da verdade: 'Alguém me salvou naquela noite, mas estou preso a um segredo.' (+Confiança Emília)":

            $ afeto_emilia += 2

            $ humanidade = min(100, humanidade + 3)

            show emilia uniforme calma meio corpo at sprite_direita with dissolve

            emilia "Obrigada por não mentir para mim. Vou descobrir quem adulterou aquele sangue."

        "Desviar a conversa perguntando o que ela faria se eu estivesse infectado (+Intelecto / +Suspeita leve)":

            $ intelecto += 1

            $ duvida_emilia += 1

            show emilia uniforme seria triste meio corpo at sprite_direita with dissolve

            emilia "...Eu rezaria para que você ainda tivesse escolha."

    hide emilia with dissolve

    hide victor with dissolve

    jump entrar_local_exploracao_bs

label evt_d04_tarde:

    # --- DIA 4 TARDE: A MÚSICA DO MUNDO SUBMERSO & A VALSA DAS SOMBRAS ---

    if renpy.loadable("audio/weeping_cello.ogg"):
        play music "audio/weeping_cello.ogg" fadein 2.0

    scene cena lility piano entretida 1 with fade

    "Fim de tarde no Bloco Esquecido. O sol poente corta os vitrais empoeirados da sala de música em feixes de cobre e poeira suspensa."

    "De longe, nos corredores frios, um som me atraiu: notas limpas de piano, lentas, carregadas de uma melancolia tão antiga que o ar pareceu esfriar dois graus a cada compasso."

    "Minha mestra está sentada ao piano de cauda. O vestido clássico de veludo escuro e detalhes rendados cobre os degraus do tablado. Os cabelos carmesins reluzem suavemente contra a madeira escura."

    scene cena lility piano victor entra 2 with dissolve

    "Dou dois passos silenciosos para dentro da sala. Encosto na moldura de carvalho carcomido."

    "Ela não me ouve. Os dedos pálidos deslizam sobre o marfim com precisão cirúrgica. Não há o deboche habitual nos lábios dela, nem a altivez predatória que ela ostenta para manter o campus à distância. Há apenas concentração. Uma dor sem pressa."

    scene cena lility piano susto para 3 with hpunch

    "Uma tábua do piso estala sob meu peso."

    "As mãos dela travam num acorde dissonante que corta o silêncio como vidro trincado. Ela vira o rosto num solavanco — os olhos carmesins arregalados em um susto genuíno, antes que a máscara de senhora implacável consiga se recompor."

    scene cena lility piano conversa em pe 4 with dissolve

    "Ela se levanta do banco do piano devagar, o tecido do vestido farfalhando na penumbra. O olhar dela me mede da cabeça aos pés, recalculando a distância entre nós."

    mestra "Você tem o péssimo hábito de rastejar como rato, Victor. Se eu estivesse com sede de verdade, sua cabeça já estaria rolando sob o pedal."

    protagonist "A terceira sequência. Você errou a oitava antes do estalo da madeira."

    "Ela estreita os olhos. Um meio sorriso perigoso repuxa o canto da boca dela."

    mestra "Eu não errei. Essa partitura foi composta antes que seus ancestrais aprendessem a polir pedras. Ela não segue as regrinhas quadradas da sua academiazinha de burgueses."

    protagonist "Quem a compôs?"

    mestra "Alguém que esperou por uma embarcação que nunca chegou. A água subiu, cobriu as colunas da cidade... e a música ficou inacabada."

    protagonist "Então o compositor devia ter reescrito o final em vez de se afogar com a partitura na mão."

    mestra "Você realmente acha que todo final trágico pode ser recalculado, garoto? Que petulância mortal."

    scene cena lility danca inicio 5 with dissolve

    "Ela dá um passo à frente, descendo do tablado. O perfume de mirra e ferro ancestral preenche a distância entre nós. Ela estende a mão delgada, envolvida pela renda negra, em minha direção."

    $ th_voz("climax/lility_climax_04a_valsa_convite")
    mestra "Se você se julga tão capaz de ditar o andamento das coisas... mostre. Sem instrumentos. Sem cálculos. Apenas o compasso."

    protagonist "Uma dança? Aqui?"

    mestra "Está com medo de que o seu cadáver não saiba acompanhar uma dama, Sr. Vane? Ou sua arrogância só serve para analisar termos de dívida?"

    "A regra um grita no meu ouvido: não dever favor a ninguém. Mas o Grilhão de Sangue no meu peito responde com um calor estranho — um pulsar compassado que não é de dor."

    "Eu estendo a mão. Meus dedos fecham sobre a renda fria."

    scene cena lility danca valsa 6 with dissolve

    "Ela me puxa com uma força suave e incontestável. Giramos no meio da sala vazia."

    "Não há orquestra tocando. Não há música gravada nas caixas de som. Apenas o atrito das solas contra a madeira antiga e o som do vento fustigando as janelas de chumbo."

    "Ela se move com a leveza de quem já cruzou séculos de salões de baile, mas os passos não são mecânicos. Há um ritmo compartilhado entre nós — o sangue que ela me deu na noite da quase morte conversando com o meu próprio sangue."

    scene cena lility danca close 7 with dissolve

    "A valsa desacelera até estancarmos no centro do salão. Os corpos próximos. O calor contido na respiração dela roça a curva do meu maxilar."

    "Por uma fração de segundo, os olhos carmesins dela perdem toda a crueldade. O que resta é uma mulher que sobreviveu ao fim de tudo o que conhecia, presa numa gaiola de pedra, encarando a única criatura viva que não se ajoelhou por medo."

    menu:
        "Manter o olhar firme e conduzir o último giro com reverência silenciosa (+Afeto com [nome_display_mestra] / +Humanidade)":
            $ afeto_mestra += 2
            $ humanidade = min(100, humanidade + 3)
            $ reagir_escolha("lility", "gentileza")
            $ notificar_rpg("🕊️ COMPASSO COMPARTILHADO", f"+2 Afeto com {nome_display_mestra} | +3 Humanidade | Vínculo Gótico Fortalecido", "#ff3366")

            protagonist "Nem todo mundo que sobrevive precisa ficar sozinho na sala vazia, [nome_display_mestra]."

            "Os lábios dela entreabrem, surpresos com a calma das minhas palavras. Ela desvia o olhar devagar para a janela poente."

            mestra "...Você fala bobagens demais para quem mal aprendeu a caçar, Victor."

            "Mas a mão dela demora três segundos a mais para soltar a minha."

        "Aproveitar a proximidade para ler os segredos da respiração dela (+Intelecto / +Ressonância)":
            $ intelecto += 1
            $ ressonancia_pre_diluviana += 1
            $ reagir_escolha("lility", "ocultismo")
            $ notificar_rpg("🔮 LEITURA PREDATÓRIA", "+1 Intelecto | +1 Ressonância Pré-Diluviana", "#9933ff")

            protagonist "Essa música... não era sobre uma cidade que afundou. Era sobre uma promessa que você fez e não pôde cumprir."

            "Os olhos dela cintilam com um perigo repentino e fascinado."

            mestra "Cuidado, meu cachorrinho. Se cavar fundo demais no meu passado, você pode encontrar o túmulo de coisas que não deveriam acordar."

        "Recuar com um sorriso irônico e quebrar o feitiço antes que ela tente morder (+Charme / +Autonomia)":
            $ charme += 1
            $ coragem += 1
            $ reagir_escolha("lility", "sarcasmo")
            $ notificar_rpg("✨ AUDÁCIA CALCULADA", "+1 Charme | +1 Coragem | Domínio da Distância", "#ffaa00")

            protagonist "Para quem dizia que eu era só um rato de laboratório... até que você não errou muitos passos."

            "Ela solta uma risada curta, rouca e genuinamente divertida."

            mestra "Insolente. Um dia desses eu ainda corto esse seu atrevimento com as presas."

    $ viu_partitura_lility = True
    $ valsa_com_lility_realizada = True

    $ local_atual = "sala_musica"
    call restaurar_fundo_local_atual
    show lility comportada sorriso meio corpo at sprite_padrao with dissolve

    "O sol finalmente se põe atrás das torres da academia. As sombras longas engolem a sala de música, trazendo de volta o frio habitual da pedra."

    "Ela dá dois passos para trás, voltando para a penumbra junto ao piano."

    mestra "A noite começou, Victor. Vá para o seu dormitório antes que Elara mande a ronda te caçar. E pratique os seus passos... você ainda é pesado demais para a minha safra."

    "Ela vira as costas e volta a folhear as folhas amareladas da partitura. Eu saio para o corredor sentindo o sangue queimar nos pulsos."

    hide lility with dissolve
    jump fim_de_evento

label evt_d05_noite:

    # --- DIA 5 A 8: CAÇADA À HACHISHAKUSAMA E A FERIDA DA PROTEÇÃO ---

    $ fome_sangue -= 15

    scene bg animado entrada academia portoes nevoeiro noite with fade

    if renpy.loadable("audio/suspense_sombrio.ogg"):

        play music "audio/suspense_sombrio.ogg" fadein 1.5

    "Dias 5 a 8 — Noite. A neblina que sobe nos portões da academia traz o cheiro de água estagnada das catacumbas. Ao longe, um som gutural ecoa entre os postes: 'Po... po... po...'"

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show emilia uniforme confiante meio corpo at sprite_direita with dissolve

    emilia "Você fica atrás de mim, Victor! Se eu disser para correr, você corre sem tentar bancar o herói. Entendido?"

    protagonist "Não. Se não queria um parceiro, não deveria ter me chamado."

    emilia "Eu convidei você porque não quero que morra sozinho nos corredores!"

    protagonist "E eu vim porque não quero depender de alguém decidindo como eu devo sobreviver."

    show emilia uniforme seria triste meio corpo at sprite_direita with dissolve

    emilia "Você sabe que essas duas coisas podem ser verdade ao mesmo tempo?! Quando você tenta controlar tudo para não dever nada a ninguém, fala exatamente como o meu pai!"

    hide victor with dissolve

    hide emilia with dissolve

    show inimigo hachishaku mulher gigante vestido branco at sprite_colossal with vpunch

    hachishaku "Po... po... po..."

    call iniciar_combate("Hachishakusama (A Mulher Gigante)", "inimigo hachishaku mulher gigante vestido branco", "inimigo hachishaku mulher gigante vestido branco ataque", 220, 30, 3.4, "inorganico", False, pode_fugir=False) from _call_iniciar_combate_13

    $ derrotou_hachishaku = True

    scene bg animado entrada academia portoes nevoeiro noite with dissolve

    show expression obter_sprite_victor("ferido_combate") as victor at sprite_esquerda with dissolve

    show emilia uniforme gentil meio corpo at sprite_direita with dissolve

    "Após dissiparmos a entidade na neblina, Emília segura meu braço ferido e começa a enfaixar o corte."

    show expression obter_sprite_victor("sem_jeito") as victor at sprite_esquerda with dissolve

    protagonist "Eu consigo cuidar disso sozinho. Você não precisa fazer isso por mim."

    emilia "Eu sei que não preciso."

    protagonist "Então por que está fazendo?"

    $ th_voz("climax/emilia_climax_03_curativo")
    emilia "Porque você está ferido, Victor. Nem todo gesto de cuidado é uma fatura que vão te cobrar depois."

    "Fico em silêncio. Sei lidar com dívidas e ameaças, mas ainda não sei como reagir quando alguém me ajuda sem exigir uma coleira em troca."

    hide emilia with dissolve

    hide victor with dissolve

    jump entrar_local_exploracao_bs

label evt_d09_noite:

    # --- DIA 9 A 11: A DOR DO GRILHÃO, A FADA VERDE E O LOTE DE VALÉRIA ---

    $ fome_sangue -= 15

    scene bg animado sala musica piano noite with fade

    if renpy.loadable("audio/the_crimson_chamber_2.ogg"):

        play music "audio/the_crimson_chamber_2.ogg" fadein 1.5

    "Noite do Dia 9. A investigação na neblina elevou minha Exposição perante o Grêmio. Quando entro na Sala de Música, encontro minha mestra apoiada na mesa, com o pulso marcado pelas queimaduras do Grilhão de Sangue e um fio carmesim no canto da boca."

    show lility presas agressiva meio corpo at sprite_padrao with vpunch

    mestra "Ora, ora... Você andou fazendo bastante barulho pelos corredores, não é, meu cachorrinho? Cada vez que você trinca a Máscara lá fora, os carcereiros da Elara cobram o pedágio aqui dentro."

    protagonist "Por que não me avisou que o Grilhão feria você diretamente?!"

    show lility meio corpo desdenhando at sprite_padrao with dissolve

    mestra "E você teria obedecido se eu avisasse? Não use a minha dor para alimentar sua culpa moral, Victor. Se for quebrar as regras daquela cadela de uniforme branco, faça valer a pena: traga-me a Partitura Rúnica das catacumbas."

    jump fim_de_evento

label evt_d10_noite:

    # --- DIA 10: O BAR DA FADA VERDE E O CONFRONTO NAS CALDEIRAS ---

    scene bg animado bar grunge taverna fogo verde with fade

    if renpy.loadable("audio/at_the_green_fairy.ogg"):

        play music "audio/at_the_green_fairy.ogg" fadein 1.5

    "No Dia 10, desço ao bar clandestino para rastrear a origem da contaminação. O vapor de absinto altera minha percepção até que uma entidade esmeralda flutua sobre o balcão."

    show fada verde deboche at entidade_flutuando with flash_green

    fada_verde "Vocês chamam essa febre de 'fome' porque têm pavor de conhecer a coisa que está faminta debaixo do alicerce."

    protagonist "Você está falando da entidade nas profundezas? Do que está adormecido sob o alicerce?"

    show fada verde ameaca at entidade_flutuando with dissolve

    fada_verde "Um nome é apenas uma coleira! A noiva de cabelos vermelhos trancou o túmulo no Dilúvio, mas agora quer abrir a porta. Pergunte a ela se quem procura o primeiro predador quer mesmo um trono... ou apenas o fim!"

    call iniciar_combate("A Fada Verde (Delírio Esmeralda)", "fada verde deboche", "fada verde ameaca", 190, 28, 3.5, "inorganico", False, pode_fugir=False) from _call_iniciar_combate_14

    $ tem_partitura_runica = True

    scene bg animado caldeiras esconderijo tocha azul e fogo with fade

    $ th_musica("My_Workspace-Steady_Groove", 1.5)

    "Logo atrás do bar, encontro uma caixa de bolsas de sangue com o selo raspado: filamentos escuros se movem dentro do líquido quando aproximo a mão. Valéria fecha a tampa no mesmo instante."

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show valeria seria mochila frascos meio corpo at sprite_direita with dissolve

    protagonist "A garota que me atacou no Dia 1 comprou deste lote. Isso aqui está vivo, Valéria!"

    valeria "Eu sei. Suspani esse lote assim que dois clientes enlouqueceram e meus rapazes ouviram batidas vindas da parede das catacumbas."

    protagonist "E você não disse nada?!"

    show valeria olhar focado meio corpo at sprite_direita with dissolve

    $ th_voz("climax/valeria_climax_02_lote_vivo")
    valeria "Escute bem, Victor: eu vendo o que consigo obter num lugar onde os nobres do Grêmio fingem que os Renegados não existem. Descobri tarde demais que o vazamento lá de baixo contaminou a mercadoria — não confunda isso com inocência."

    "Coloco um artefato raro recuperado do subsolo sobre a bancada dela."

    show valeria sorriso provocante pirulito meio corpo at sprite_direita with dissolve

    valeria "Bonito. Valioso. E você não está com cara de quem quer dinheiro. Está tentando me comprar... ou está viciado no poder de me fazer dizer 'sim' quando eu deveria dizer 'não'?"

    menu:

        "Exigir parceria estratégica e os registros da rota subterrânea (+Intelecto / +Afeto Valéria)":

            $ intelecto += 1

            $ afeto_valeria += 3

            $ investigou_lote_contaminado = True

            protagonist "Quero que pare de me tratar como cliente. Quero os registros de transporte e uma rota de saída para quando a barreira cair."

            valeria "Fechado, sócio. Mas lembre-se: eu nunca vendo a minha independência."

        "Pressioná-la a cooperar com a investigação de Emília (+Humanidade)":

            $ humanidade = min(100, humanidade + 4)

            $ alianca_emilia_valeria = True

            protagonist "Entregue a rota do lote contaminado para Emília sem expor seus fornecedores. Se aquilo sob o alicerce despertar, não vai sobrar mercado para ninguém."

            valeria "Trégua prática com a santinha? Que seja."

    hide valeria with dissolve

    hide victor with dissolve

    jump fim_de_evento

label evt_d13_manha:

    # --- DIA 12 A 14: A PAREDE QUE PULSA E O CHÁ DEPOIS DA EMBOSCADA ---

    $ fome_sangue -= 10

    scene bg animado escadaria catacumbas tochas runas with fade

    if renpy.loadable("audio/funeral_in_the_catacombs.ogg"):

        play music "audio/funeral_in_the_catacombs.ogg" fadein 1.5

    "Nos corredores subterrâneos interditados, encosto a mão na parede de pedra antiga e sinto uma pulsação lenta e colossal — o mesmo ritmo abafado que senti no Transe de Sangue. A escola inteira foi erguida sobre o sarcófago de algo proibido e ancestral."

    "À noite, ao descobrir o acordo silencioso entre o Grêmio e o mercado negro, sou emboscado por capangas das caldeiras a mando de Elara, mas consigo derrotá-los."

    call iniciar_combate("Capanga de Contenção", "inimigo fundao mascara gas chave grifo neutro", "inimigo fundao mascara gas chave grifo ataque", 140, 24, 3.6, "humano", False, pode_fugir=False) from _call_iniciar_combate_15

    scene bg animado gabinete diretor dia cortinas with fade

    if renpy.loadable("audio/the_cold_decree.ogg"):

        play music "audio/the_cold_decree.ogg" fadein 1.5

    "Na manhã seguinte, entro no Gabinete da Presidência mancando levemente. Elara serve uma xícara de chá impecável sem levantar os olhos."

    show elara uniforme arrogante meio corpo at sprite_padrao with dissolve

    $ th_voz("climax/elara_climax_02b_cha")
    elara "Você está mancando, Sr. Vane. Que pena. Eu esperava que os meninos das caldeiras fossem mais eficientes."

    protagonist "Você mandou eles me matarem porque descobri que o Grêmio tolera o mercado de Valéria para conter os Renegados."

    show elara sorrindo de forma ironica at sprite_padrao with dissolve

    elara "Eu mandei testarem você. Se morresse, um problema a menos. Como sobreviveu... provou que ainda pode ser moldado. A partir de hoje os setores subterrâneos estão bloqueados sob minha responsabilidade."

    protagonist "E se tudo ruir no Eclipse, a senhora também vai assumir a responsabilidade?"

    show elara uniforme observando meio corpo at sprite_padrao with dissolve

    elara "...Eu já a assumi há um século, Victor."

    hide elara with dissolve

    jump fim_de_evento

# ==============================================================================

# ATO III — A VERDADE, A RUPTURA E A FOME ACELERADA (DIAS 15 A 20)

# ==============================================================================

label evt_d15_noite:

    scene bg animado patio arvore noite postes luz with fade

    if renpy.loadable("audio/dance_of_the_shadowed_court.ogg"):

        play music "audio/dance_of_the_shadowed_court.ogg" fadein 2.0

    "Noite do Baile de Máscaras. A Deterioração atinge metade de seu ciclo. A elite da academia celebra sob máscaras venezianas para fingir que a barreira não está cedendo."

    "No terraço iluminado pela lua, Emília me confronta. Sua voz treme enquanto seus dedos seguram a máscara prateada e o cabo da adaga consagrada."

    show expression obter_sprite_victor("cabisbaixo") as victor at sprite_esquerda with dissolve

    show emilia uniforme seria triste meio corpo at sprite_direita with dissolve

    emilia "O sangue no subsolo... e a forma como seus ferimentos cicatrizaram depois da caçada. Não foi sorte, Victor. Eu vi o que o Grilhão fez no seu peito quando você tentou esconder sua condição."

    protagonist "Eu não pedi para ser transformado, Emília."

    emilia "Eu sei! Mas você olhou para mim todos os dias e escolheu esconder a verdade!"

    protagonist "Eu não sabia se você ainda conseguiria olhar para mim como uma pessoa depois de ouvir!"

    show emilia uniforme surpresa meio corpo at sprite_direita, pulo_susto

    $ th_voz("climax/emilia_climax_04_baile")
    emilia "Então você decidiu por mim! Tirou de mim o direito de escolher, exatamente como fizeram com você!"

    menu:

        "Abrir o coração sem reservas: 'Não vou mais mentir. Minha vida está nas suas mãos.' (+Confiança Emília)":

            $ emilia_conhece_a_verdade = True

            $ afeto_emilia += 3

            $ humanidade = min(100, humanidade + 5)

            show emilia uniforme corada timida meio corpo at sprite_direita with dissolve

            emilia "...Dance comigo por cinco minutos, Victor. Antes que o meu pai chegue à cidade amanhã, preciso lembrar pelo que estou lutando."

        "Manter a distância defensiva: 'Fiz o que precisava para nós dois sobrevivermos.' (-Confiança)":

            $ emilia_conhece_a_verdade = True

            $ duvida_emilia += 3

            show emilia uniforme seria triste meio corpo at sprite_direita with dissolve

            emilia "Se você cruzar o limite e ferir um inocente, Victor... eu mesma terminarei isso."

    hide emilia with dissolve

    hide victor with dissolve

    # --- NOITE DO DIA 15: A VALSA NA SALA DE MÚSICA E A MÁSCARA DE LILITY ---

    scene bg animado sala musica piano noite with fade

    if renpy.loadable("audio/gothic_waltz.ogg"):

        play music "audio/gothic_waltz.ogg" fadein 2.0

    "Mais tarde, na Sala de Música interditada, a valsa abafada do salão ecoa pelo piso de madeira. [nome_display_mestra] se aproxima da janela após observar o brasão antigo da escola com desprezo."

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show lility dinamica sorriso meio corpo at sprite_direita with dissolve

    protagonist "Você fala como se já soubesse o que vai acontecer depois do Eclipse, [nome_display_mestra]. Mas nunca fala do que quer fazer no dia seguinte."

    mestra "Tenho uma imaginação extraordinária. Vou escolher um palácio, reconstruir os corredores e proibir esses uniformes horríveis."

    protagonist "Você está brincando."

    mestra "Naturalmente."

    protagonist "Você não quer um reino. Você quer que alguma coisa termine."

    show lility vulneravel timida meio corpo at sprite_direita with dissolve

    "O sorriso dela se desfaz por completo. O silêncio na sala pesa como chumbo."

    $ th_voz("climax/lility_climax_04_valsa")
    mestra "Cuidado, Victor. Eu já aceitei desaparecer quando o sarcófago abrir... Não seja cruel tentando me fazer querer ficar."

    hide lility with dissolve

    hide victor with dissolve

    jump fim_de_evento

label evt_d16_noite:

    # --- DIA 16 E 17: A ABSTINÊNCIA E A CHEGADA DE LORDE PHILLIP ---

    $ fome_sangue = max(15, fome_sangue - 30)

    scene bg animado corredor zona vermelha luzes de sangue with fade

    if renpy.loadable("audio/pulsao_sombra.ogg"):

        play music "audio/pulsao_sombra.ogg" fadein 1.5

    "Dia 16. A aproximação do Eclipse dobra a velocidade da Fome de Sangue. No corredor dos dormitórios, passo por um estudante humano com um corte recente no braço; o som das palavras dele fica abafado pelo pulsar da veia exposta."

    protagonist "(Afaste-se... agora! Eu estou tentando impedir que precisem me parar!)"

    scene bg animado sala musica piano noite with dissolve

    show lility bracos cruzados seria meio corpo at sprite_padrao with dissolve

    mestra "Você está tremendo, Victor."

    protagonist "Estou cansado. Não preciso de você."

    mestra "Não foi isso que eu perguntei."

    protagonist "...Eu não quero precisar de você."

    show lility comportada sorriso meio corpo at sprite_padrao with dissolve

    $ th_voz("climax/lility_climax_04b_abstinencia")
    mestra "Ah. Isso é muito diferente. Precisar de alguém para continuar de pé não significa que essa pessoa tenha vencido. Beba logo e me diga como vamos entrar no Cofre."

    $ fome_sangue = min(100, fome_sangue + 45)

    hide lility with dissolve

    jump fim_de_evento

label evt_d17_tarde:

    # --- DIA 17: LORDE PHILLIP VON KARSTEN ---

    scene bg animado patio claustro fonte entardecer with fade

    if renpy.loadable("audio/duty_unspoken.ogg"):

        play music "audio/duty_unspoken.ogg" fadein 1.5

    "Dia 17. Lorde Phillip von Karsten, inquisidor da Ordem e pai de Emília, atravessa os portões da academia."

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show phillip neutro espada at sprite_direita with dissolve

    phillip "Afaste-se da minha filha, garoto. Você carrega o fedor da abominação ancestral misturado ao perfume de Emília. A criatura dentro de você não precisa da sua autorização para destruí-la."

    protagonist "E o senhor não precisa saber quem eu sou para decidir me executar. Sei muito bem o que acontece quando alguém decide a vida de outra pessoa e chama isso de proteção."

    show phillip pensativo espada at sprite_direita with dissolve

    phillip "Eu vi cidades inteiras desaparecerem porque inquisidores jovens insistiram em compreender o monstro antes de detê-lo. A hesitação mata, Victor Vane. O Ritual do Corte do Vínculo existe no meu grimório, mas jamais o entregarei voluntariamente a você."

    if afeto_emilia >= 6 and humanidade >= 60:

        show emilia uniforme confiante meio corpo at sprite_padrao with dissolve

        $ th_bark("emilia", "cacadora_hostil")
        $ th_voz("climax/emilia_climax_05_desafio_pai")
        emilia "Pai, você me ensinou que a hesitação mata, mas estou vendo que a sua certeza cega também! Eu mesma copiei as páginas do grimório do Corte do Vínculo para o Victor!"

        $ ritual_corte_vinculo_desbloqueado = True

        hide emilia with dissolve

    else:

        show phillip combate guarda at sprite_direita with vpunch

        "Sou forçado a cruzar lâminas contra o veterano inquisidor para abrir caminho e arrancar as anotações do ritual!"

        hide victor with dissolve

        hide phillip with dissolve

        call iniciar_combate("Lorde Phillip von Karsten", "phillip neutro espada", "phillip ataque lamina carmesim", 320, 34, 3.2, "humano", False, pode_fugir=False) from _call_iniciar_combate_16

        $ ritual_corte_vinculo_desbloqueado = True

    hide phillip with dissolve

    hide victor with dissolve

    jump fim_de_evento

label evt_d19_noite:

    # --- DIA 19: O ASSALTO TÁTICO AO COFRE, AS 3 FASES E O DUELO COM ELARA ---

    scene bg animado catacumbas corredor tochas with fade

    if renpy.loadable("audio/Authority_Breach.ogg"):

        play music "audio/Authority_Breach.ogg" fadein 1.5

    "Noite 19. A contagem regressiva para o Eclipse está quase no fim. A Ruína vibra pelas pedras ancestrais do colégio."

    "Diante de mim está a passagem secreta para as entranhas mais profundas do subsolo: o Cofre de Contenção do Conselho Estudantil."

    "Lá dentro repousam as duas únicas peças capazes de controlar o despertar de Cain: o Relicário de Sangue Puro e a Chave de Contenção de Grau Zero."

    # --------------------------------------------------------------------------

    # FASE 1: A ESCADARIA RÚNICA (ARMADILHAS SACRAS E ELÉTRICAS)

    # --------------------------------------------------------------------------

    "Avanço pelos primeiros degraus da escadaria em espiral. O ar estala com faíscas azuladas: o chão está entalhado com uma malha de glifos rúnicos da Inquisição, projetados para incinerar qualquer vampiro que pise em falso."

    menu:

        "[[CONHECIMENTO OCULTO]] Decifrar a frequência dos glifos e desarmar o circuito arcano":

            if conhecimento_oculto >= 10:

                "Com as pontas dos dedos e a mente fria, analiso a geometria dos nós arcanos. Reconheço o fluxo de energia e quebro o contato do eletrodo central com a ponta de uma lâmina!"

                "As faíscas silenciam-se. O caminho está livre sem disparar nenhum alarme!"

                $ intelecto += 1

                $ conhecimento_oculto += 1

                $ notificar_rpg("⚡ CIRCUITO DESARMADO", "+1 Intelecto | +1 Conhecimento Oculto | Passagem segura!", "#00ffcc")

            else:

                with flash_red

                $ th_sfx("shock")

                $ hp_jogador = max(1, hp_jogador - 20)

                "Hesito ao tocar no glifo errado! Uma descarga de eletricidade rúnica percorre meu corpo, queimando as terminações nervosas das minhas mãos (-20 HP)!"

                "Rangendo os dentes, forço o passo adiante até a descarga se extinguir na pedra fria."

                $ notificar_rpg("⚡ DESCARGA RÚNICA", "-20 HP | Danos de choque rúnico!", "#ff4444")

        "[[SANGUE SACRO / PACTO]] Invocar a bênção de Emília para dissipar as runas" if getattr(store, "pacto_emilia_ativo", False) or getattr(store, "sangue_liturgico_ativo", False) or getattr(store, "bebeu_sangue_emilia", False):

            with flash

            "Lembro-me da oração de proteção e da pureza que corre nas minhas veias desde a troca de sangue com Emília."

            "Um halo tênue de luz prateada envolve meus passos. Ao pisar nas lajes entalhadas, as runas inquisitoriais reconhecem a assinatura sagrada e se dissipam como névoa diante do sol!"

            $ coragem += 2

            $ notificar_rpg("✝️ BÊNÇÃO CONSAGRADA", "+2 Coragem | Selos neutralizados pela graça sacra!", "#88ccff")

        "[[RESISTÊNCIA BRUTA]] Avançar em disparada suportando a queimação dos selos":

            with flash_red

            $ hp_jogador = max(1, hp_jogador - 20)

            $ coragem += 1

            "Sem tempo para sutilezas, disparo escada abaixo em velocidade vampírica! Os arcos voltaicos queimam minhas roupas e cortam minha pele, mas minha determinação me arrasta até o patamar inferior (-20 HP)."

            $ notificar_rpg("🩸 ÍMPETO BRUTAL", "-20 HP | +1 Coragem | Travessia na força bruta!", "#ff8844")

    # --------------------------------------------------------------------------

    # FASE 2: O SALÃO DOS GUARDIÕES DO GRÊMIO

    # --------------------------------------------------------------------------

    scene bg animado catacumbas corredor runas tochas with dissolve

    "Chego à antecâmara fortificada. Diante da porta blindada de titânio do Cofre, três guardas de elite do Conselho Estudantil em uniformes brancos impecáveis vigiam a entrada, espadas e rapieiras desembainhadas."

    menu:

        "[[DUTOS DE VENTILAÇÃO]] Usar a Chave-Mestra de Nora para contornar a guarda pelo teto" if getattr(store, "tem_chave_dutos_nora", False):

            "Localizo a escotilha de manutenção na penumbra do teto. Insiro a Chave-Mestra de latão que Nora me confiou na cripta."

            "A trava estala suavemente. Rastejo pelos dutos estreitos de ventilação, passando exatamente sobre os capacetes dos guardas de elite sem emitir um único ruído."

            "Desço do outro lado da barricada e giro a manivela de emergência, travando a porta pesada por dentro e deixando a guarda isolada do lado de fora!"

            $ intelecto += 2

            $ notificar_rpg("🗝️ CONDUTA DE NORA", "+2 Intelecto | Guardas contornados com sucesso!", "#00ffcc")

        "[[SABOTAGEM DAS CALDEIRAS]] Injetar gás de dormência pelas tubulações de vapor" if afeto_valeria >= 5 and (getattr(store, "desbloqueou_mercado_negro", False) or getattr(store, "mercado_negro_desbloqueado", False)):

            "Conforme as instruções que aprendi com Valéria no submundo das Caldeiras, acoplo o bypass na válvula de purga de gás."

            "Abro o registro com força: uma nuvem espessa de vapor químico e anestésico preenche a câmara dos guardas!"

            "Tossindo e cambaleando, os executores do Grêmio perdem os sentidos antes de conseguirem soar o alarme."

            $ intelecto += 2

            $ notificar_rpg("🧪 SABOTAGEM QUÍMICA", "+2 Intelecto | Guarda do Grêmio neutralizada pelo vapor!", "#2eb82e")

        "[[COMBATE TÁTICO]] Enfrentar o Capitão da Guarda de Elite do Grêmio":

            "Salto da escuridão com as presas à mostra! Os guardas entram em formação e o Capitão da Guarda ergue sua espada prateada para conter minha invasão!"

            call iniciar_combate("Capitão da Guarda do Grêmio", "inimigo executor conselho prata espada ereto", "inimigo executor conselho prata espada ataque", 210, 30, 3.4, "gremio", False, pode_fugir=False) from _call_iniciar_combate_guarda_elite

            "Com um golpe decisivo, desarmo o líder da guarda e arrombo os trincos da antecâmara!"

    # --------------------------------------------------------------------------

    # FASE 3: A CÂMARA DO COFRE & CONFRONTO COM ELARA

    # --------------------------------------------------------------------------

    scene bg animado catacumbas cofre velas verdes with fade

    "As portas do cofre interno se abrem com um gemido de dobradiças ancestrais. A sala é iluminada por chamas verdes que tremulam em candelabros de bronze."

    "Sobre o altar de pedra no fundo do recinto, o Relicário de Sangue Puro pulsa com um brilho escarlate hipnótico. Ao lado dele, a Chave de Contenção de Cain brilha em ouro fosco."

    "Mas entre mim e o relicário, uma silhueta solitária me espera com postura régia."

    show elara foice batalha preparada at sprite_padrao with vpunch

    elara "Você foi longe demais, Victor Vane."

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    protagonist "O baile de máscaras acabou, Elara. Quantas vidas mais você vai jogar nesta fornalha?"

    show elara uniforme autoritaria meio corpo at sprite_direita with dissolve

    $ th_voz("climax/elara_climax_03a_cofre_furia")
    elara "Vidas? Você ousa me dar lições de moral? Olhe para este colégio! Olhe para a cidade lá fora! Há mais de cem anos o Grêmio equilibra a balança entre monstros insaciáveis e uma humanidade frágil que seria varrida do mapa em três noites se o Antediluviano despertasse!"

    protagonist "Equilibra a balança sacrificando os alunos de uniforme preto na enfermaria? Usando cobaias como a Nora em tubos de vidro no subsolo enquanto o Conselho veste branco e toma vinho consagrado?"

    show elara encarando de cima para baixo at sprite_direita with dissolve

    elara "Sacrifícios necessários para manter a ordem! Alguém precisa carregar a culpa pelas engrenagens que giram nas sombras! Mas você... você é apenas o fantoche daquela impostora na Sala de Música! Ela só quer ver esta academia em ruínas porque não tem nada a perder; e você quer bancar o herói porque não sabe o que é governar!"

    show elara foice batalha preparada at sprite_padrao with vpunch
    $ th_voz("climax/elara_duelo_chuva")
    elara "Você desafia o meu decreto com a lâmina de um camponês? Ajoelhe-se diante da linhagem de von Weiss, ou sangre sobre as lajes do pátio! Eu prefiro ver seu corpo empalado nas portas deste cofre do que permitir que você entregue o sangue primordial para quem quer ver o mundo queimar!"

    call iniciar_combate("Presidente Elara", "elara foice batalha preparada", "elara foice golpe corte ataque", 340, 36, 3.2, "gremio", False, pode_fugir=False) from _call_iniciar_combate_17

    $ tem_relicario_sangue = True

    $ tem_chave_contencao = True

    scene bg animado catacumbas cofre velas verdes with dissolve

    show elara derrotada encarando at sprite_padrao with dissolve

    elara "Você... você realmente acredita que derrotar-me mudará o que está acordando lá embaixo?"

    protagonist "Proteger uma instituição pelo medo não é o mesmo que proteger as pessoas que vivem nela, Elara."

    menu:

        "Forçar o Transe de Sangue Invertido e subjugar Elara (+Domínio / -Humanidade)":

            with flash_red

            $ humanidade -= 10

            $ dominio_jogador += 2

            $ afeto_elara += 3

            $ elara_subjugada_no_cofre = True
            $ persistent.eco_conhece_senha_cofre = True

            protagonist "Você passou todo esse tempo me lembrando de quem segurava a coleira, Presidente. Agora prove do sangue que corre nas minhas veias."

            $ th_voz("climax/elara_climax_03_derrota_cofre")
            elara "...Maldito seja, Victor... Eu passei um século segurando a coleira... e agora o seu sangue me faz querer viver sob o seu comando."

        "Estender a mão e exigir uma trégua política pelo bem da escola (+Humanidade)":

            $ humanidade = min(100, humanidade + 5)

            $ afeto_elara += 2

            protagonist "Levante-se, Presidente. Não vim tomar o seu trono; vim impedir que Cain devore a escola que você jurou proteger."

            elara "...Que não reste dúvida, Victor Vane: se falharmos amanhã, cairemos juntos."

        "Confrontá-la com o destino de Nora Vasques e forçar o Grêmio à redenção (+Humanidade / +Respeito)" if getattr(store, "nora_estabilizada_cripta", False) or getattr(store, "nora_misericordia_concedida", False):

            $ humanidade = min(100, humanidade + 5)

            $ afeto_elara += 3

            show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

            protagonist "Eu estive na cripta selada, Elara. Eu vi o que vocês fizeram com a Nora. Alfinete 31. Uma aluna humana jogada numa cuba ácida como peça de reposição."

            show elara shock at sprite_padrao with dissolve

            elara "...Nora... Você a encontrou...?"

            protagonist "Eu encontrei. E não a tratei como um número descartável, como você fez. Se o seu Grêmio precisa devorar os próprios alunos para sobreviver, ele não merece estar de pé. Mas se você se levantar agora e lutar ao meu lado pelo amanhã, podemos construir algo melhor do que essa farsa."

            show elara uniforme observando meio corpo at sprite_padrao with dissolve

            elara "......"

            "Pela primeira vez em um século, vejo os olhos da Presidente marejados pela vergonha. Ela segura minha mão estendida e se levanta lentamente."

            $ th_voz("climax/elara_climax_03b_redencao_nora")
            elara "Pela primeira vez... alguém me lembrou por que fundamos este refúgio. Quando o sol nascer depois do Antediluviano... o Conselho prestará contas."

            $ notificar_rpg("🕊️ PACTO DE REDENÇÃO", "+5 Humanidade | +3 Respeito de Elara | O Grêmio reconhece seus erros.", "#00ffcc")

    hide elara with dissolve

    hide victor with dissolve

    jump fim_de_evento

label evt_d20_noite:

    # --- DIA 20: A ÚLTIMA REUNIÃO ANTES DO ECLIPSE ---

    scene bg animado gabinete diretor noite candelabro with fade

    if renpy.loadable("audio/obscura.ogg"):

        play music "audio/obscura.ogg" fadein 1.5

    "Véspera do Eclipse. A Deterioração atinge o estágio crítico. Pela primeira vez, as vozes da escola colidem na mesma sala antes da descida final às catacumbas."

    show elara uniforme observando meio corpo at sprite_esquerda with dissolve

    show valeria seria neutra meio corpo at sprite_direita with dissolve

    elara "O ritual original foi construído para manter o Antediluviano adormecido, não para matá-lo."

    valeria "Então o grande plano da nobreza é entrar na sala de um deus faminto que não pode morrer e pedir educadamente que ele volte a dormir?"

    hide elara with dissolve

    hide valeria with dissolve

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show lility bracos cruzados seria meio corpo at sprite_direita with dissolve

    protagonist "Vocês continuam falando como se estivéssemos discutindo quem vai vencer. Estamos discutindo o que cada um aqui está disposto a destruir para não admitir que pode perder."

    mestra "...Amanhã à noite, na câmara do sarcófago, veremos qual é a sua resposta final, Victor."

    hide lility with dissolve

    hide victor with dissolve

    jump fim_de_evento

# ==============================================================================

# NOVOS EVENTOS EXPANDIDOS DOS 21 DIAS (UNIFORME PRETO vs. BRANCO, FACÇÕES E ARCOS)

# ==============================================================================

# --- DIA 6 (TARDE): PRETO E BRANCO NO PÁTIO DA FONTE ---

label evt_d06_tarde:

    scene bg animado patio claustro fonte entardecer with fade

    if renpy.loadable("audio/The_Cold_Decree.ogg"):

        play music "audio/The_Cold_Decree.ogg" fadein 1.5

    "Tarde tensa no campus. O ar vibra com anomalias crescentes. Ao redor da Fonte Gótica, a divisão invisível da escola salta aos olhos como um tabuleiro de xadrez."

    "De um lado, dezenas de estudantes comuns em seus uniformes pretos conversam baixo, vários deles com pequenos curativos de algodão na dobra do braço após a 'campanha de doação'."

    "No balcão superior de mármore, os membros do Conselho Estudantil vestem seus uniformes brancos impecáveis. Nenhum deles jamais entra na fila da enfermaria."

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show valeria casaco caqui descontraida corpo inteiro at sprite_direita with dissolve

    valeria "Bonito o contraste, né, bolsista? Preto embaixo, branco em cima."

    protagonist "Os alunos de uniforme preto nem desconfiam para onde vão as bolsas da enfermaria?"

    show valeria cinica pirulito meio corpo at sprite_direita with dissolve

    valeria "Eles preferem não saber, Victor. Um ponto extra no histórico escolar e uma dispensa de Educação Física compram muita cegueira voluntária."

    valeria "A diferença entre mim e a Presidente Elara é que, quando eu vendo alguma coisa nas caldeiras, o rótulo diz exatamente quanto custa."

    menu:

        "\"E você não se importa de ver o 'rebanho' sendo drenado assim?\" (+Humanidade)":

            $ humanidade = min(100, humanidade + 3)

            show valeria seria neutra meio corpo at sprite_direita with dissolve

            valeria "Eu me importo em manter os meus vivos lá embaixo. Quem tenta salvar o prédio inteiro sozinho costuma virar fundação."

        "\"Pelo menos sabemos onde encontrar suprimento se o subsolo secar.\" (-Humanidade / +Intelecto)":

            $ humanidade = max(0, humanidade - 4)

            $ intelecto += 1

            $ afeto_valeria += 1

            show valeria perfil sorriso provocador meio corpo at sprite_direita with dissolve

            valeria "Olha só... O gatinho da senhorita Lyra já está aprendendo a pensar como quem está no topo da cadeia alimentar."

    hide valeria with dissolve

    hide victor with dissolve

    jump fim_de_evento

# --- DIA 7 (NOITE): A PRIMEIRA SEDE DOS SEM ROSTO E O TESTE DE LILITY ---

label evt_d07_noite:

    $ fome_sangue = max(10, fome_sangue - 15)

    scene bg animado corredor academia entardecer sol at luz_zona_vermelha with fade

    if renpy.loadable("audio/pulsao_sombra.ogg"):

        play music "audio/pulsao_sombra.ogg" fadein 1.5

    "Dia 7 — Noite. Uma semana desde que meu coração mudou de ritmo. Atravesso o corredor vazio do primeiro andar quando esbarro num calouro de uniforme preto que ficou trancado após a monitoria."

    "Ele derruba os cadernos no chão. Quando estendo a mão para ajudá-lo, sinto o cheiro quente do pulso dele a poucos centímetros do meu rosto."

    show expression obter_sprite_mob("mob calouro a") as mob_npc at sprite_direita with dissolve

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    mob_calouro_a "D-desculpe, veterano! Os monitores trancaram a escada leste e eu não sei como sair..."

    menu:

        "Controlar a respiração e indicar a saída lateral (+Humanidade / +Coragem)":

            $ humanidade = min(100, humanidade + 4)

            $ coragem += 1

            $ lility_percebeu_compaixao = True

            protagonist "Vá pela porta de serviço atrás da biblioteca. E não olhe para trás se ouvir alguém chamando seu nome."

            hide mob_npc with dissolve

            "Cravo as unhas na palma da minha própria mão até o calouro desaparecer em segurança."

        "Prendê-lo contra o armário e beber um gole rápido nas sombras (+35%% Sangue / +10%% Exposição / -Humanidade)":

            with flash_red

            $ fome_sangue = min(100, fome_sangue + 35)

            $ exposicao += 10

            $ humanidade = max(0, humanidade - 5)

            "Antes que ele possa gritar, cubro sua boca e sacio a queimação na garganta, deixando-o tonto encostado nos armários."

            hide mob_npc with dissolve

    scene bg animado sala musica piano noite with fade

    show lility encarando com sorriso cabeca de lado at sprite_padrao with dissolve

    if lility_percebeu_compaixao:

        mestra "Eu senti sua fome daqui de dentro, Victor... e senti quando você deixou a presa ir embora de mãos abanando. Que desperdício adorável."

    else:

        mestra "Cheiro de sangue fresco no colarinho, meu cachorrinho? Cuidado... O primeiro gole roubado nos corredores é sempre o mais difícil de limpar."

    hide lility with dissolve

    jump fim_de_evento

# --- DIA 8 (MANHÃ): A AUTÓPSIA OCULTA DE EMÍLIA ---

label evt_d08_manha:

    scene bg animado sala aula ocultismo alquimia verde with fade

    if renpy.loadable("audio/The_Unfinished_Lesson.ogg"):

        play music "audio/The_Unfinished_Lesson.ogg" fadein 1.5

    "Dia 8 — Manhã. Na antiga sala do Clube de Ocultismo, Emília analisa amostras de cinza recolhidas nos portões após a luta contra a Mulher Gigante."

    show expression obter_sprite_victor("padrao") as victor at sprite_esquerda with dissolve

    show emilia com olhar investigativo at sprite_direita with dissolve

    emilia "Victor, olhe para este reagente de prata. Entidades comuns se dissipam no éter, mas as anomalias desta escola estão sendo puxadas de baixo para cima, como se algo sob as catacumbas estivesse respirando."

    protagonist "Se o seu pai souber disso, o que a Ordem vai fazer com a escola?"

    show emilia preocupada olhando para baixo at sprite_direita with dissolve

    emilia "Expurgo total. Eles não separariam os alunos inocentes de uniforme preto dos vampiros do Conselho. É por isso que preciso encontrar a fonte antes do Dia 17."

    menu:

        "Compartilhar o que ouviu sobre o Cofre do Conselho (+Confiança Emília / +Intelecto)":

            $ afeto_emilia += 2

            $ intelecto += 1

            show emilia uniforme gentil meio corpo at sprite_direita with dissolve

            emilia "Você está arriscando o pescoço para me dar essa pista, Victor. Prometo que não vou deixar o meu pai tocar em quem ainda luta para ser humano."

        "Aconselhá-la a não descer às catacumbas sozinha (+Coragem / +Afeto)":

            $ coragem += 1

            $ afeto_emilia += 1

            show emilia com vergonha arrumando o oculos e olhando para o lado at sprite_direita with dissolve

            emilia "T-tudo bem... Da próxima vez que eu descer, chamo você primeiro."

    hide emilia with dissolve

    hide victor with dissolve

    jump fim_de_evento

# --- DIA 11 (TARDE): A RONDA DA POLÍCIA E O DIRETOR FANTOCHE ---

label evt_d11_tarde:

    scene bg animado entrada academia portoes entardecer sol with fade

    if renpy.loadable("audio/suspense_sombrio.ogg"):

        play music "audio/suspense_sombrio.ogg" fadein 1.5

    "Dia 11 — Tarde. Duas viaturas da polícia metropolitana estão paradas diante dos portões de ferro da academia. O Diretor humano enxuga o suor da testa enquanto Elara observa a cena a poucos passos."

    show expression obter_sprite_mob("mob policial c") as mob_npc at sprite_esquerda with dissolve

    show elara uniforme arrogante meio corpo at sprite_direita with dissolve

    mob_policial_c "São quatro estudantes transferidos sem rastro em dez dias, Srta. Presidente. A delegacia central está começando a fazer perguntas."

    elara "E os relatórios médicos assinados pelo nosso Diretor já foram encaminhados ao comissário, Detetive. Surto de anemia sazonal e transferências voluntárias."

    show elara sorrindo com arrogancia at sprite_direita with dissolve

    elara "Tenho certeza de que a doação generosa da Fundação ao fundo da polícia ajudará a manter a imprensa longe dos nossos portões."

    hide mob_npc with dissolve

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    "Quando o detetive vai embora em silêncio, Elara vira os olhos carmesim na minha direção."

    elara "Viu como o mundo lá fora é frágil, Sr. Vane? Humanos de uniforme preto ou de distintivo... todos têm um preço. Certifique-se de que a sua sede não encareça a minha contabilidade."

    hide elara with dissolve

    hide victor with dissolve

    jump fim_de_evento

# --- DIA 12 (NOITE): O SUSSURRO DO SARCÓFAGO E O ACORDO NO SUBSOLO ---

label evt_d12_noite:

    scene bg animado corredor industrial subsolo vapor with fade

    if renpy.loadable("audio/obscura.ogg"):

        play music "audio/obscura.ogg" fadein 1.5

    "Dia 12 — Noite. Desço pela tubulação de vapor entre as caldeiras e as catacumbas. Por trás de uma grade enferrujada, ouço vozes conhecidas discutindo em tom baixo."

    show elara encarando de forma astuta at sprite_esquerda with dissolve

    show valeria casaco caqui postura firme corpo inteiro at sprite_direita with dissolve

    elara "Quero o dobro de sedativos alquímicos até a noite do Baile, Valéria. Os lacaios do segundo andar estão ficando agitados com a aproximação do Eclipse."

    valeria "O preço subiu, Presidente. Meus rapazes do Fundão não vão descer perto daquela parede que pulsa pelo valor antigo."

    elara "Você existe neste porão porque eu permito. Entregue a remessa e elimine qualquer curioso que chegue perto da grade do Cofre."

    $ ouviu_acordo_elara_valeria = True

    hide elara with dissolve

    hide valeria with dissolve

    "Recuo em silêncio pelas sombras... mas os guardas contratados me avistam na subida das escadas, preparando a emboscada da madrugada!"

    jump fim_de_evento

# --- DIA 14 (NOITE): VÉSPERA DO BAILE E A ESCOLHA DO PAR ---

label evt_d14_noite:

    scene bg animado dormitorio quarto noite luar with fade

    if renpy.loadable("audio/where_the_room_turns_blue.ogg"):

        play music "audio/where_the_room_turns_blue.ogg" fadein 1.5

    "Dia 14 — Noite. Sobre a escrivaninha do meu quarto, há uma máscara negra enviada para o Baile de Inverno de amanhã. Do lado de fora, a lua já apresenta uma auréola avermelhada."

    menu:

        "Passar a véspera revisando as partituras antigas de [nome_display_mestra] (+Afeto com [nome_display_mestra] / +Ressonância)":

            $ afeto_mestra += 2

            $ ressonancia_pre_diluviana += 1

            "As notas rúnicas parecem vibrar sob os meus dedos, preparando meu sangue para a valsa na Sala de Música."

        "Limpar e afiar os amuletos de proteção com o guia de Emília (+Afeto Emília / +Humanidade)":

            $ afeto_emilia += 2

            $ humanidade = min(100, humanidade + 3)

            "Guardo o pequeno amuleto de prata no bolso interno do blazer, determinado a encarar Emília de frente amanhã."

        "Conferir o mapa de dutos de fuga enviado por Valéria (+Afeto Valéria / +Intelecto)":

            $ afeto_valeria += 2

            $ intelecto += 1

            "Memorizo cada tranca subterrânea caso o Baile de Máscaras se transforme num massacre."

        "Polir o broche de inspeção do Grêmio para provocar Elara (+Afeto Elara / +Domínio)":

            $ afeto_elara += 2

            $ dominio_jogador += 1

            "Amanhã à noite, a Presidente verá que o lacaio sob o Grilhão aprendeu a jogar o jogo da corte."

    jump fim_de_evento

# --- DIA 18 (NOITE): LEI MARCIAL E O EXPURGO DOS CORREDORES ---

label evt_d18_noite:

    $ fome_sangue = max(10, fome_sangue - 15)

    scene bg animado corredor zona vermelha luzes de sangue with fade

    if renpy.loadable("audio/steel_loop.ogg"):

        play music "audio/steel_loop.ogg" fadein 1.5

    "A Ruptura da Máscara. A Lei Marcial foi decretada no campus: os alunos de uniforme preto foram trancados nos dormitórios enquanto Inquisidores da Igreja e Gárgulas do Conselho guerreiam nos corredores!"

    show inimigo gargula elite celestial asas abertas at sprite_colossal with vpunch

    $ th_stinger("anomalia")

    "Uma Gárgula de Elite do Conselho despenca do vitral superior para bloquear meu avanço rumo ao subsolo!"

    call iniciar_combate("Gárgula de Elite do Conselho", "inimigo gargula elite celestial asas abertas", "inimigo gargula elite celestial ataque", 230, 32, 3.4, "inorganico", False, pode_fugir=False) from _call_iniciar_combate_18

    "Com o construto de mármore despedaçado no chão, o caminho para o Assalto ao Cofre de amanhã à noite está finalmente aberto."

    jump fim_de_evento

# ==============================================================================

# ATO IV — O ECLIPSE E OS 4 DESFECHOS CANÔNICOS (DIA 21)

# ==============================================================================

label evt_d21_noite:

    scene bg cripta antecamara portao runas altar 2k with fade

    if renpy.loadable("audio/cain_inane.ogg"):

        play music "audio/cain_inane.ogg" fadein 2.0

    "O Eclipse Total. A Deterioração atinge cem por cento. No fundo das catacumbas, Lility crava o Relicário de Sangue Puro no sarcófago ancestral."

    "As correntes de ouro se partem com um estrondo sísmico! O teto da academia rui sob a Esfera de Sangue que se abre no céu noturno, e Cain desperta."

    scene bg animado apocalipse cratera orb vermelha with flash_red

    if renpy.loadable("audio/the_hunger_of_ancient_gods.ogg"):

        play music "audio/the_hunger_of_ancient_gods.ogg" fadein 1.5

    show cain ameaca flutuando at entidade_flutuando with vpunch

    protagonist "Você vai drenar a metrópole inteira! E quando não houver mais sangue ao alcance?!"

    cain "A cidade inteira é apenas o que resta ao alcance do despertar. Quando secar, a fome terá aprendido o tamanho do mundo."

    protagonist "Você não quer governar nada..."

    cain "Governar é o nome vaidoso que os famintos dão ao intervalo entre duas refeições."

    protagonist "Eu não serei descartável. Nem para o Conselho, nem para a Igreja, e nem para deuses antigos!"

    call iniciar_combate("Cain, O Progenitor Faminto", "cain neutro espada", "cain ataque espada rubra", 450, 42, 3.0, "corrompido", True, pode_fugir=False) from _call_iniciar_combate_19

    if _return == "derrota_historia":

        jump morte_definitiva

    scene bg animado apocalipse cratera orb vermelha with flash_red

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show lility meio corpo chocada at sprite_direita with dissolve

    "Arranco Lility do vórtice de drenagem de Cain no último instante antes que sua imortalidade seja consumida até o fim!"

    mestra "Por que você me puxou de volta, seu tolo teimoso?! Só a fome dele podia encerrar a minha existência!"

    protagonist "No primeiro dia você me salvou quando eu estava morrendo no corredor — não por utilidade, mas porque escolheu! E você não precisa fingir que quer um reino se tudo o que desejava era que alguém terminasse a sua história!"

    show lility vulneravel timida meio corpo at sprite_direita with dissolve

    mestra "Se você me pedir para parar agora... diga-me a verdade, Victor: você quer me salvar porque se importa comigo... ou porque não suporta a ideia de ficar sozinho de novo?"

    # ==========================================================================

    # ESCOLHA DEFINITIVA DOS FINAIS DE THE HUNGER & THE HALLWAYS

    # ==========================================================================

    menu:

        "1. (FINAL A — CONSORTE IMORTAL) 'Não quero que atravesse a eternidade sozinha. Vamos drenar Cain e reinar juntos!'":

            with flash_red

            if renpy.loadable("audio/the_hunger_of_ancient_gods.ogg"):

                play music "audio/the_hunger_of_ancient_gods.ogg" fadein 1.5

            show lility confiante sorriso meio corpo at sprite_direita with dissolve

            protagonist "Segure o Relicário comigo, Lility! Se a eternidade era vazia porque você carregava essa maldição sozinha, nós vamos usurpar o sangue de Cain e dividir o peso dessa coroa!"

            $ th_voz("climax/lility_climax_06_final_a")
            mestra "...Você nunca aprendeu a seguir uma ordem simples, meu doce cachorrinho. Então que o mundo antigo queime sob os nossos pés!"

            "Cravamos nossas mãos simultaneamente no peito do Progenitor! O vórtice de sangue milenar explode em uma coluna escarlate que rasga os céus da academia!"

            "A vitae divina de Cain queima através de nós, purificando nossa fraqueza e coroando nossas almas com a autoridade pré-diluviana absoluta."

            "As pedras do teto desmoronam, revelando a metrópole sob o eclipse permanente. As cortes vampíricas e os inquisidores ajoelham-se em pânico e reverência diante da nova dinastia."

            "Lility apoia o queixo em meu ombro, o olhar afiado como navalha, enquanto nossas sombras se fundem no trono do mundo noturno."

            "🏆 FINAL A DESBLOQUEADO: CONSORTE IMORTAL (A Nova Dinastia Carmesim)."

            return

        "2. (FINAL B — QUASE HUMANO) 'Eu devolvo a sua paz, Lility. Vou realizar o Ritual do Corte ao lado de Emília.'" if ritual_corte_vinculo_desbloqueado and afeto_emilia >= 6:

            with flash

            if renpy.loadable("audio/safe_within_the_blue_2.ogg"):

                play music "audio/safe_within_the_blue_2.ogg" fadein 2.0

            show lility comportada sorriso meio corpo at sprite_direita with dissolve

            protagonist "Eu não vou prender você aqui por egoísmo, Lility. Você me devolveu a vida naquela primeira noite no corredor; agora eu uso o Ritual do Corte para conceder o descanso sagrado que você buscou por milênios."

            mestra "Finalmente... uma resposta que não me deixa entediada. Obrigada por ter sido a minha última testemunha, Victor... viva por nós dois."

            $ th_bark("emilia", "ritual_corte")
            "Ergo a lâmina rúnica e quebro o selo ancestral do Relicário. Uma luz dourada e suave emana do corpo de Lility."

            "Sem dor, sem fogo — apenas um alívio imenso. Seu corpo imortal desfaz-se em cinzas de luz que fecham para sempre a fenda dimensional de Cain."

            hide lility with dissolve

            show emilia uniforme sorriso amigavel meio corpo at sprite_direita with dissolve

            "Quando a poeira baixa, os primeiros raios do sol da manhã filtram-se pelas arcadas em ruínas da capela."

            "Emília corre em minha direção com lágrimas nos olhos, segurando com força minhas mãos geladas. Aqueço-me ao toque dela."

            "De repente, sinto um estalo profundo sob o esterno: TUM... TUM... TUM... Meu coração volta a bater, compassado e quente. As presas recuam. O peso da maldição se foi."

            emilia "Você conseguiu, Victor... Você está aqui. Você está vivo."

            protagonist "Nós estamos vivos, Emília."

            "🏆 FINAL B DESBLOQUEADO: QUASE HUMANO (O Peso da Liberdade)."

            return

        "3. (FINAL C — A CONFIGURAÇÃO DO LAMENTO) 'Inverter o Ritual: Roubar a maldição de Lility e condená-la à fragilidade mortal!'" if ritual_corte_vinculo_desbloqueado:

            with flash_red

            if renpy.loadable("audio/weeping_cello.ogg"):

                play music "audio/weeping_cello.ogg" fadein 2.0

            "No estertor final de Cain, um espinho calcificado da criatura é projetado pelo ar em rota de colisão contra o meu peito!"

            "Emília salta na minha frente com seu crucifixo erguido — a lâmina de osso perfura seu peito de lado a lado!"

            show emilia chocada at sprite_direita with vpunch

            protagonist "EMÍLIA! NÃO!"

            "Seguro seu corpo trêmulo nos meus braços enquanto o sangue humano jorra sobre o piso sagrado. Os olhos dela perdem o foco; seus lábios balbuciam uma prece agonizante."

            emilia "Victor... está frio... Me deixe ir... por favor... para a luz..."

            "O pânico cego me enlouquece. Não posso permitir. Não vou deixar mais ninguém morrer por mim nesta escola maldita!"

            "Mordo meu próprio pulso até rasgar o tendão e pressiono a ferida sangrenta contra a boca de Emília, forçando minha vitae profana por sua garganta!"

            with flash_red

            $ th_sfx("heartbeat")

            "O corpo de Emília convulsiona violentamente! A pureza que ela protegeu a vida inteira é corrompida pelo abraço vampírico. Quando ela reabre os olhos, as íris estão escarlates como brasas vivas."

            show emilia triste at sprite_direita with dissolve

            "Duas presas afiadas rasgam seus lábios trêmulos; lágrimas de sangue espesso escorrem por suas bochechas enquanto ela fita as próprias mãos com horror absoluto."

            $ th_bark("emilia", "climax_02_lamento")
            emilia "O que... o que você fez comigo, Victor...?! Eu sou... um demônio... Por que você roubou o meu céu...?!"

            "Com as mãos ainda tintas do sangue dela, viro-me para o Relicário onde Lility aguardava o fim!"

            show expression obter_sprite_victor("rindo") as victor at sprite_esquerda with dissolve

            protagonist "No primeiro dia você teve pena de mim porque queria ver alguém lutar pela vida, Lility?! Agora eu tomo a sua maldição milenar para mim... e condeno você a viver!"

            "Inverto os glifos de corte no Relicário! Em um relâmpago ensurdecedor, o sarcófago tranca Cain para sempre, arrancando o dom da imortalidade do peito de Lility e transferindo toda a carga primordial para as minhas veias!"

            show lility meio corpo chocada at sprite_direita, pulo_susto

            "Pela primeira vez em três mil anos, Lility perde o equilíbrio e cai de joelhos no chão úmido da cripta. O rubor mortal sobe às suas maçãs do rosto; suas presas se recolhem e seu peito sobe e desce em arquejos aflitos de ar."

            show lility meio corpo chorando at sprite_direita with dissolve

            $ th_bark("lility", "climax_06_mortal")
            mestra "O que... o que você fez comigo, monstro?! Minhas mãos... estão tremendo de frio... Meu pulso está acelerado... Eu sinto fome... sinto dor... O que sobrou de mim?!"

            protagonist "Todos sobreviveram, Lility... e todos nós perdemos exatamente o que desejávamos. Emília viverá na noite me odiando pela eternidade; e você viverá como uma mortal frágil sob a minha guarda, gota por gota."

            "Fico de pé no centro das ruínas sob a chuva escura. Um rei que salvou todos que amava ao preço de destruir suas almas."

            "🏆 FINAL OCULTO C DESBLOQUEADO: A CONFIGURAÇÃO DO LAMENTO (Todos Sobrevivem, Todos Perdem)."

            return

        "4. (FINAL D — A ÚLTIMA TRANSAÇÃO) 'Deixar a escola ruir e escapar pelos túneis das caldeiras com Valéria!'" if afeto_valeria >= 6 and (getattr(store, "desbloqueou_mercado_negro", False) or getattr(store, "mercado_negro_desbloqueado", False)):

            if renpy.loadable("audio/midnight_in_the_underpass.ogg"):

                play music "audio/midnight_in_the_underpass.ogg" fadein 1.5

            hide lility with dissolve

            show valeria olhar focado meio corpo at sprite_direita with dissolve

            valeria "O túnel de drenagem das caldeiras está aberto, bolsista! A carga já está no furgão e o teto vai virar poeira em dois minutos!"

            protagonist "Você realmente consegue virar as costas para a escola inteira e nunca mais olhar para trás, Valéria?"

            show valeria cinica confiante meio corpo at sprite_direita with dissolve

            $ th_bark("valeria", "climax_05_alianca")
            valeria "Não confunda sentimentalismo com lucro, Victor! Eu passei anos montando essa rota de fuga para quando os nobres fizessem merda. O Grêmio ruiu, Cain foi selado nos escombros, e nós temos um estoque de vitae purificada e tecnologia arcana que vale uma fortuna lá fora!"

            show expression obter_sprite_victor("sorrindo") as victor at sprite_esquerda with dissolve

            protagonist "E qual é o nosso primeiro destino, sócia?"

            show valeria cinica pirulito meio corpo at sprite_direita with dissolve

            valeria "Bem longe daqui. Além da jurisdição de qualquer inquisidor ou conselho. Onde nós dois é que mandamos na tabela de preços."

            "Aceleramos pela galeria subterrânea enquanto os alicerces da velha academia desabam em estrondo atrás de nós. Cruzamos a divisa da metrópole antes dos primeiros clarões do dia, donos do próprio destino."

            "🏆 FINAL D DESBLOQUEADO: A ÚLTIMA TRANSAÇÃO (Sobreviventes do Submundo)."

            return

        "5. (FINAL F — A IMPERATRIZ DA ORDEM) 'Aliar-se à convicção de Elara: expurgar os corruptos do Conselho e comandar os Executores ao lado dela!'" if afeto_elara >= 6 and getattr(status_elara, "duvida", 0) <= 2:

            with flash

            if renpy.loadable("audio/The_Cold_Decree.ogg"):
                play music "audio/The_Cold_Decree.ogg" fadein 1.5

            show expression obter_sprite_victor("confiante") as victor at sprite_esquerda with dissolve
            show elara uniforme autoritaria meio corpo at sprite_direita with dissolve

            protagonist "Elara! Abaixe a foice. O problema desta escola nunca foram os alunos de uniforme preto... foram os velhos covardes do Conselho que venderam as nossas veias para a Inquisição!"

            $ th_voz("climax/elara_decreto_marcial")
            elara "Eu sei, Victor. Eu sempre soube. Mas a ordem não se sustenta no vácuo; alguém precisa ter a coragem de carregar a lâmina e assinar as sentenças."

            protagonist "Então não carregue isso sozinha. Deixe Lility selar a fenda com o Relicário. Nós dois vamos assumir a Reitoria e reconstruir São Cipriano nos nossos próprios termos!"

            "Pela primeira vez, o olhar gélido da Presidente desfaz a muralha de aço. Ela estende a mão enluvada em direção à minha, apertando meus dedos com uma determinação implacável."

            show elara encarando sorrindo at sprite_direita with dissolve

            $ th_bark("elara", "climax_04_trono")
            elara "Um acordo selado em ferro e sangue, Victor Vane. A partir desta noite, você não é mais um monitor bolsista... você é o Comandante Oculto dos meus Executores."

            "Canalizamos o poder do decreto institucional sobre o altar rúnico. A fenda de Cain é lacrada sob o selo de ferro do Conselho Estudantil!"

            "Os velhos prelados da Inquisição e os nobres decadentes que compravam bolsas de sangue são presos e expulsos da academia pela ronda dos Executores sob minhas ordens diretas."

            scene bg animado gabinete diretor noite candelabro with fade

            "Meses depois. O gabinete da Presidência está silencioso, iluminado pelo fogo suave da lareira e pelos lustres de prata."

            "Elara revisa as atas de reforma acadêmica à mesa monumental, com o casaco preto do Conselho repousando sobre os ombros e a postura impecável de quem nasceu para reinar."

            show elara superioridade sorriso corpo inteiro at sprite_direita with dissolve

            elara "A ronda das catacumbas foi concluída sem incidentes, Comandante? Os relatórios dos monitores estão sobre a sua mesa."

            show expression obter_sprite_victor("charmoso") as victor at sprite_esquerda with dissolve

            protagonist "Nenhuma anomalia passou pelas muralhas, Presidente. A cidade inteira já sabe que São Cipriano não responde mais a Lorde Phillip nem a nenhum prelado."

            show elara meio corpo com vergonha olhando pro lado at sprite_direita with dissolve

            "Ela pousa a caneta de ouro e ergue os olhos cinzentos para mim. O rubor é contido, mas os olhos traem a cumplicidade absoluta que construímos sobre o fio da navalha."

            elara "Excelente. Agora tranque a porta do gabinete, Victor. A ata institucional foi encerrada... e nós temos pendências particulares para auditar antes da alvorada."

            "Aproximo-me da mesa, segurando sua mão enquanto as luzes da metrópole brilham sob as vidraças góticas. Dois soberanos que transformaram a disciplina em amor e a ordem em salvação."

            "🏆 FINAL F DESBLOQUEADO: A IMPERATRIZ DA ORDEM (O Decreto Conjunto)."

            return

        "6. (FINAL SECRETO E — A HARMONIA PROIBIDA) 'Recusar qualquer sacrifício e forjar a Aliança das Quatro Soberanas!' (Requer Afeto 8+ com Todas e Humanidade 40+)" if getattr(store, "afeto_mestra", 0) >= 8 and getattr(store, "afeto_emilia", 0) >= 8 and getattr(store, "afeto_valeria", 0) >= 8 and getattr(store, "afeto_elara", 0) >= 8 and getattr(store, "humanidade", 0) >= 40:

            with flash

            if renpy.loadable("audio/The_Cold_Decree.ogg"):

                play music "audio/The_Cold_Decree.ogg" fadein 1.5

            "Diante da fenda de Cain que racha o tecido da realidade, recuso o caminho fácil da morte ou da dominação."

            show expression obter_sprite_victor("confiante") as victor at sprite_esquerda with dissolve

            protagonist "Chega! Nenhuma de vocês vai se sacrificar hoje! Nem Lility como oferenda milenar, nem Emília como mártir cega, nem Valéria como fugitiva nas sombras, e nem Elara como carrasca dos próprios alunos!"

            show lility meio corpo chocada at sprite_padrao with dissolve

            mestra "Victor... do que você está falando?! O selo primordial exige um tributo de sangue imenso para conter Cain!"

            show elara uniforme autoritaria meio corpo at sprite_direita with dissolve

            elara "Ele tem razão, Lility. Nós passamos um século nos digladiando em castas e segredos porque tínhamos medo de admitir que nenhuma facção conseguiria governar este fardo sozinha."

            show valeria cinica confiante meio corpo at sprite_esquerda with dissolve

            valeria "Se é sobre redistribuir carga e pressão sem estourar a caldeira... vocês estão olhando para a especialista certa."

            show emilia determinada at sprite_padrao with dissolve

            emilia "E se a pureza divina pode redimir em vez de apenas queimar... a bênção dos von Karsten estará neste círculo!"

            "Colocamo-nos ao redor do Relicário de Sangue Puro em uma formação estelar de cinco pontas."

            "Lility conjura as runas pré-diluvianas de sangue ancestral, tecendo correntes vivas que paralisam o coração cósmico de Cain."

            "Emília estende seu rosário consagrado, canalizando a luz sacra para purificar a corrupção do despertar sem ferir os envolvidos."

            "Valéria acopla os condutores arcanos das caldeiras, drenando o excesso catastrófico de energia para abastecer a infraestrutura subterrânea da cidade."

            "E Elara crava o cetro do Conselho Estudantil na laje mestra, assinando com sua vitae o Decreto de Dissolução das Castas e a anistia universal dos alunos de uniforme preto."

            with flash

            with vpunch

            "A fenda de Cain se fecha harmoniosamente! O abismo se sela não por um massacre, mas pelo equilíbrio absoluto entre Poder Ancestral, Fé Sacra, Ciência do Submundo e Ordem Política."

            scene bg gremio_dia with fade

            "Meses depois. O grande gabinete da academia está banhado pela luz solar e tochas rúnicas. Não há mais uniformes pretos e brancos separados pela vergonha; não há mais cobaias em cápsulas de vidro."

            "As doações de sangue agora são feitas sob contrato e respeito mútuo. À mesa central da diretoria, o Conselho das Quatro reúne-se ao meu lado."

            show lility comportada sorriso meio corpo at sprite_padrao with dissolve:
                xpos 0.16

            show emilia uniforme sorriso amigavel meio corpo at sprite_padrao with dissolve:
                xpos 0.39

            show elara uniforme observando meio corpo at sprite_padrao with dissolve:
                xpos 0.62

            show valeria perfil sorriso provocador meio corpo at sprite_padrao with dissolve:
                xpos 0.84

            protagonist "Uma nova aliança. Uma nova noite."

            $ th_voz("climax/lility_climax_08_final_e")
            mestra "Quem diria que o garoto quase morto no corredor leste se tornaria o único homem capaz de manter quatro rainhas no mesmo reino..."

            elara "Não se acostume com os elogios, Victor. A ata da reunião de hoje tem trinta páginas de reformas para você assinar."

            valeria "E a minha margem de lucro nos filtros continua intocada, sócio."

            emilia "E a paz dos estudantes finalmente está protegida pela luz e pela verdade."

            "Olho para cada uma delas, sabendo que cada escolha, cada gota de sangue e cada gesto de empatia valeram a pena."

            "🏆 FINAL SECRETO E DESBLOQUEADO: A HARMONIA PROIBIDA (O Coven das Quatro Soberanas)."

            return

    return

# ==============================================================================

# EVENTOS ESPECIAIS: PACTO DE SANGUE & SAFRA RARA

# ==============================================================================

label evento_emilia_pacto_sangue:
    $ local_atual = "sala_ocultismo"
    $ periodo = "Noite"
    call restaurar_fundo_local_atual

    play music "audio/the_unfinished_lesson.ogg" fadein 2.0

    "A porta do Clube de Ocultismo é trancada com duas voltas na chave. O cheiro de incenso de mirra preenche a sala."

    

    show expression obter_sprite_victor("triste") as victor at sprite_esquerda with dissolve

    show emilia chocada at sprite_direita with dissolve

    emilia "Um... um vampiro... Durante todo esse tempo, Victor?"

    

    "Suas mãos tremem ao segurar o crucifixo de prata contra o peito. O treinamento dos von Karsten grita para ela sacar a lâmina consagrada, mas seus olhos estão marejados."

    show expression obter_sprite_victor("constrangido") as victor at sprite_esquerda with dissolve

    victor "Eu não escolhi isso, Emília. Naquela primeira noite, quando você me viu perto do pátio... eu já estava morrendo nas garras daquela coisa."

    victor "Eu só queria manter minha bolsa de estudos. Acordei com essa maldição na garganta, sem pedir por nada disso."

    show emilia triste at sprite_direita with dissolve

    "O aperto de Emília no crucifixo afrouxa. O terror rígido da caçadora se desfaz, dando lugar a uma compaixão dolorosa ao lembrar do rapaz assustado que conheceu no primeiro dia."

    emilia "Você... você foi apenas uma vítima dessa escola podre. Meu Deus, Victor... o quão solitário e assustador isso deve ter sido para você..."

    

    show emilia determinada at sprite_direita with dissolve

    emilia "Mas escute bem: eu jamais permitirei que você ceda à escuridão e ataque os alunos desta academia! Nem um único inocente!"

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    victor "Eu tenho me controlado, Emília. Eu juro."

    emilia "Controle não basta contra a fome! Eu estudei a fisiologia da sua espécie nos arquivos do meu pai. Se você não se alimentar, entrará em Frenesi."

    

    show emilia corada at sprite_direita with dissolve

    "Emília respira fundo, fecha os olhos e murmura três Ave-Marias rápidas. Quando volta a abrir os olhos, seu rosto está completamente vermelho, mas ela desabotoa os dois primeiros botões da gola do uniforme, expondo a pele alva do pescoço."

    $ th_voz("climax/emilia_climax_01_pacto")
    emilia "Por isso... eu serei o seu sustento. Beba de mim, Victor. É meu dever cristão impedir uma tragédia nesta escola!"

    show expression obter_sprite_victor("sem_jeito") as victor at sprite_esquerda with dissolve

    if getattr(store, "safra_rara_valeria", False):
        victor "(Ela acha mesmo que está salvando a escola inteira sozinha... Se ela sonhar que a Mestra e a própria contrabandista das caldeiras já sustentam a minha sede, ela me exorciza na hora.)"
    else:
        victor "(Ela acha mesmo que está salvando a escola inteira sozinha... Se ela sonhar que a Mestra já dita as regras do meu sangue neste internato, ela me exorciza na hora.)"

    victor "Emília, tem certeza? Eu não quero machucar você."

    emilia "A-Apenas vá logo antes que eu perca a coragem! É um sacrifício solene pela paz da academia...!"

    play sound "audio/heartbeat.ogg"

    "Aproximo-me devagar. O cheiro dela é uma mistura embriagante de lírios, incenso e algo quente e luminoso que faz minhas presas latejarem."

    "Quando cravo os dentes de leve em sua pele, Emília solta um suspiro abafado, segurando com força na manga do meu casaco para não cair."

    emilia "Ah...! P-Pelos céus... então é assim que..."

    call executar_transe_sangue("emilia") from _call_executar_transe_sangue_7

    $ alimentar_de_heroina("emilia", qtd_sangue=45, ganho_vinculo=20, ganho_afeto=15)
    $ confianca_emilia += 15
    $ pacto_emilia_ativo = True

    call restaurar_fundo_local_atual
    show expression obter_sprite_victor("ferido_sorriso") as victor at sprite_esquerda with dissolve
    show emilia uniforme corada timida meio corpo at sprite_direita with dissolve

    emilia "Pronto... você se alimentou. Minha pele ainda arde, mas... você manteve a sua palavra."
    emilia "Lembre-se do nosso pacto, Victor: enquanto eu estiver ao seu lado, você não tocará em nenhum outro estudante desta academia."

    victor "Obrigado, Emília. Eu não vou esquecer esse sacrifício."

    "O sangue de Emília acalma a Besta em meu peito como água benta sobre brasas ardentes."
    "Mas o aroma denso de mirra e cera litúrgica agora impregna meu colarinho. Se Elara ou a minha Mestra sentirem esse cheiro nos corredores, as consequências serão perigosas."

    hide emilia with dissolve
    hide victor with dissolve
    jump entrar_local_exploracao_bs

label evento_valeria_safra_rara:
    $ local_atual = "caldeiras"
    call restaurar_fundo_local_atual

    if renpy.loadable("audio/insistent_bass.ogg"):

        play music "audio/insistent_bass.ogg" fadein 2.0

    "O vapor das caldeiras silva nos canos enferrujados.{w=0.3} O cheiro de metal quente mistura-se à fumaça do cigarro de Valéria."

    "Jogo uma bolsa de sangue vazia sobre o caixote de ferro que serve de balcão."

    victor "Esse último lote tem gosto de plástico velho e anticoagulante, Val.{w=0.3} Não tem nada melhor no estoque?"

    show valeria cinica pirulito meio corpo at sprite_padrao with dissolve

    valeria "Olha só para você...{w=0.3} Chegou no fim da semana inteiro.{w=0.4} Confesso que apostei contra."

    valeria "O fornecimento do hospital tá cercado pelos cães de guarda do Grêmio.{w=0.3} Mas como os nossos negócios têm rendido frutos..."

    show valeria perfil sorriso provocador meio corpo at sprite_padrao with dissolve

    valeria "Acho que você merece acesso ao catálogo restrito."

    menu:

        "\"Direto ao ponto, Valéria.\"":

            $ coragem += 2

            $ reagir_escolha("valeria", "autoridade")

            $ notificar_rpg("🔥 POSTURA FIRME", "+2 Coragem | Negociação sem rodeios", "#ff5500")

            show valeria cinica confiante meio corpo at sprite_padrao with dissolve

            valeria "Sem preliminares, né?{w=0.3} Gosto assim.{w=0.4} Quem enrola muito nas caldeiras acaba virando carvão."

        "\"Quanto vai me custar dessa vez?\"":

            $ intelecto += 2

            $ reagir_escolha("valeria", "lucro")

            $ notificar_rpg("💰 PRAGMATISMO", "+2 Intelecto | Foco no custo-benefício", "#00ffcc")

            show valeria cinica confiante meio corpo at risada_deboche

            valeria "Heh.{w=0.3} Gosto quando você já abre a carteira antes de ouvir a oferta.{w=0.4} Cliente prático é cliente que volta."

        "\"Vai me vender sangue vencido de novo?\"":

            $ charme += 2

            $ reagir_escolha("valeria", "sarcasmo")

            $ notificar_rpg("✨ PROVOCAÇÃO", "+2 Charme | Humor ácido nos fundos", "#ff66cc")

            show valeria deboche sonolenta meio corpo at risada_deboche

            valeria "Ei!{w=0.3} Meus produtos têm selo de procedência das caldeiras, seu mal-agradecido.{w=0.4} Mas relaxa... O que tenho hoje nunca viu uma embalagem plástica."

    show valeria sorriso provocante pirulito meio corpo at sprite_padrao with dissolve

    valeria "Sangue da melhor qualidade.{w=0.4} Sem intermediários...{w=0.3} e direto da fonte."

    "Ela apoia o quadril contra a mesa de metal, deslizando o indicador pela gola da jaqueta até a curvatura do pescoço."

    "A artéria ali pulsa forte, visível sob a pele pálida e quente."

    valeria "Mas vai com calma, querido...{w=0.4} Essa safra que você vai beber é edição limitada e bem rara.{w=0.3} E o preço acompanha a exclusividade."

    valeria "Dinheiro compra sangue diluído de calouro em jejum, bolsista... Mas a minha safra particular? Você vai ter que pagar com algo que a reitoria não consiga imprimir."

    valeria "E sem deixar marcas onde a clientela possa ver amanhã...{w=0.3} ou eu cobro taxa de indenização por danos à vitrine da empresa."

    victor "O preço não é dinheiro, Valéria.{w=0.3} O preço é você."

    "Empurro as notas de volta para a gaveta e coloco um frasco condensado de essência rara sobre a chapa de metal. Valéria solta um riso curto, quase sem ar, e passa o trinco pesado do escritório."

    if renpy.loadable("audio/heartbeat.ogg"):

        play sound "audio/heartbeat.ogg"

    "Aproximo-me devagar.{w=0.3} Minhas mãos seguram sua cintura com firmeza, sentindo o calor do corpo dela contra o frio do meu peito."

    "As presas tocam a pele quente...{w=0.3} e o primeiro rasgo libera um surto de nicotina, adrenalina pura e eletricidade."

    show valeria deboche sonolenta meio corpo at pulo_susto

    valeria "Nngh...!{w=0.4} E-Ei...!"

    "A pose de comerciante inabalável dura exatamente três segundos.{w=0.3} Os dedos dela cravam nas minhas costas e a respiração se perde num gemido rouco."

    valeria "O contrato...{w=0.3} era só uma dose rápida, Vane...{w=0.4} Quem te deu permissão pra... ahn... pra me puxar desse jeito...?"

    valeria "Isso aí...{w=0.3} isso aí vai ter custo adicional...{w=0.3} seu aproveitador..."

    $ alimentar_de_heroina("valeria", qtd_sangue=50, ganho_vinculo=25, ganho_afeto=20)

    $ coragem += 5

    $ charme += 5

    $ safra_rara_valeria = True

    # --- REPERCUSSÃO NOS BASTIDORES COM ALMA DE PERSONA ---

    "Mais tarde, nos corredores da academia..."

    show elara uniforme arrogante meio corpo at sprite_padrao with dissolve

    elara "Francamente, Victor...{w=0.3} Cheirando a fuligem de caldeira, nicotina barata e ambição clandestina?"

    elara "Achei que o seu paladar estivesse refinando...{w=0.3} mas vejo que continua frequentando o fast-food do subsolo."

    hide elara with dissolve

    show lility meio corpo desdenhando at sprite_padrao with dissolve

    mestra "Os antigos caçavam monarcas em seus tronos dourados...{w=0.3} e o meu protegido vai buscar sustento no pescoço de uma contrabandista de ferro-velho."

    show lility comportada sorriso meio corpo at sprite_padrao with dissolve

    mestra "Pelo menos me diga que a tal 'safra rara' valeu o risco, VV.{w=0.3} Seria patético ter um servo sem paladar refinado."

    hide lility with dissolve

    call restaurar_fundo_local_atual

    jump menu_encontro_valeria

