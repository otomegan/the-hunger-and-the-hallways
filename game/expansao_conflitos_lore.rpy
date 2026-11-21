# ==============================================================================
# EXPANSÃO CANÔNICA DE CONFLITOS & LORE: THE HUNGER AND THE HALLWAYS
# Cenas de Perímetro, Identidades Ocultas, Horror Cósmico e Subtexto Gótico
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. A FRONTEIRA DE FERRO & O NOME ESQUECIDO (Lility nos Portões à Noite)
# ------------------------------------------------------------------------------
label ev_lility_fronteira_portoes:
    $ ev_fronteira_portoes_lility_visto = True
    $ local_atual = "portoes_praca"
    call restaurar_fundo_local_atual
    play music "audio/where_the_room_turns_blue.ogg" if_changed fadein 1.5

    "A névoa noturna rasteja pelas lajes frias da praça frontal. As altas grades de ferro fundido se erguem contra o céu chumbo, separando os domínios de São Cipriano das buzinas e faróis distantes da metrópole."

    "A um palmo dos portões monumentais, vejo uma silhueta esguia. O vestido negro ondula na brisa úmida. Ela está imóvel, encarando as luzes da cidade lá fora como quem fita um quadro inacabado."

    "Aproximo-me com passos cautelosos. Noto que os pés dela não cruzam a linha da soleira de pedra cinzenta."

    "'Lyra...?' — chamo em voz baixa."

    "Nenhuma resposta. Ela continua estática, com os olhos fixos na neblina, como se aquela palavra fosse apenas o ruído do vento nas folhas."

    "Senhorita Lyra von Blut?"

    "Desta vez, ela se vira com uma lentidão quase coreografada. Os olhos carmesins brilham sob os cílios longos; nos lábios pálidos, surge um sorriso de escárnio refinado."

    show lility sorrindo de lado sorrindo at sprite_direita with dissolve
    $ th_bark("lility", "noite_fora")

    mestra "Ah... É assim que esses vermes de uniforme branco me chamam atualmente nos livros de presença, não é? Quase esqueci."

    show lility meio corpo desdenhando at sprite_direita with dissolve
    $ th_voz("lility/lyra_bark_genealogia")
    mestra "Lyra von Blut... Um título vulgar para tempos vulgares, Victor. A fidalga menor da Silésia com dote atrasado... O sangue nestas veias conquistava reinos antes desta escola ter uma única pedra."

    show lility comportada sorriso meio corpo at sprite_direita with dissolve
    $ th_voz("climax/lility_portoes_nome")
    mestra "Para você, lacaio, meu nome não cabe em papéis de mortais. Você me deve a respiração e a fome. Pode me chamar de 'Mestra'... ou, se algum dia merecer minha indulgência, talvez eu lhe permita sussurrar 'Lili' quando as luzes se apagarem."

    "Com um sorriso desdenhoso, ela ergue a mão direita e estende a ponta dos dedos delicados além da linha imaginária entre as duas colunas do portão."

    play sound "audio/sfx/stinger_zona_vermelha.ogg"
    with flash_red
    "No instante em que a ponta da unha cruza a soleira, runas carmesins explodem sob a pele do pulso dela. Faíscas de fogo mágico estalam como chicotes invisíveis, queimando a carne pálida com um sibilo de ferro quente."

    show lility presas agressiva meio corpo at sprite_direita with dissolve
    $ th_bark("lility", "grilhao_dor")
    mestra "Tsk... O Grilhão de Elara. Ela acha que me colocou uma coleira ao cercar os portões, o subsolo e o salão do Conselho. Uma medida temporária enquanto tenta remendar a barreira do Eclipse."

    show lility comportada sorriso meio corpo at sprite_direita with dissolve
    mestra "Mas enquanto os cães da guarda patrulham a ala central, a periferia deste pátio ainda pertence a quem sabe andar nas sombras."

    menu:
        "Você não teme o julgamento que Elara prometeu quando a barreira ceder?":
            $ intelecto += 1
            show lility meio corpo gelida at sprite_direita with dissolve
            $ th_bark("lility", "elara_desdem")
            mestra "Julgamento? Da herdeira da Casa von Weiss? Os von Weiss compraram títulos de imperadores mortais com ouro roubado e acham que isso limpa o cheiro de plebe de suas veias. Ela dita regras porque o Grão-Duque financia o sangue dos calouros... Mas no instante em que o selo romper, descobrirá que decretos de papel não calam a primeira presa."
            $ notificar_rpg("🧠 DEDUÇÃO", "+1 Intelecto | Compreensão do conflito político", "#38bdf8")

        "Tocar o pulso dela para dividir a dor da runa queimada":
            $ vinculo_sangue_lility = min(100, vinculo_sangue_lility + 15)
            $ status_lility.afeto += 2
            "Seguro a mão dela. A pele onde a runa estalou está em brasa. Quando meus dedos tocam a cicatriz incandescente, o calor drena para o meu próprio braço, deixando apenas uma linha rubra fumegante."
            show lility com vergonha olhando de lado at sprite_direita with dissolve
            mestra "Tolo... Dividir a marca de um Grilhão não o torna um cavaleiro protetor. Apenas faz com que o laço aperte dois pescoços em vez de um... Ainda assim, admito que sua lealdade é de um refinamento quase irritante."
            $ notificar_rpg("🩸 VÍNCULO CARMESIM", "+15 Vínculo com a Mestra | +2 Afeto", "#ff2244")

        "Perguntar sobre a noite em que ela foi flagrada no subsolo":
            $ conhecimento_oculto += 1
            show lility sorrindo de lado sorrindo at sprite_direita with dissolve
            mestra "Elara me encontrou diante do sarcófago nas catacumbas antes da primeira quarentena. A tola presumiu que eu estava faminta, tentando sugar o sangue da tumba... Ela não tem a menor ideia do que dorme sob aquelas lajes. E é melhor que continue cega."
            $ notificar_rpg("📜 MISTÉRIO DO SUBSOLO", "+1 Conhecimento Oculto", "#ffd700")

    "Ela recolhe a mão para dentro das dobras do vestido negro, fitando os portões uma última vez."
    hide lility with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 2. PREDADORA NAS SOMBRAS DO CLAUSTRO (Interceptação Noturna)
# ------------------------------------------------------------------------------
label ev_interceptacao_lility_ponto_cego:
    $ ev_interceptacao_ponto_cego_lility_visto = True
    call restaurar_fundo_local_atual
    play sound "audio/sfx/sfx_passos_madeira_ranger.ogg"

    "Caminho pela penumbra noturna, contornando a ala leste. As luzes principais dos corredores estão apagadas para economizar a rede elétrica da Academia, deixando apenas manchas azuladas projetadas pelos vitrais altos."

    "De repente, uma mão gelada como mármore surge da escuridão e se fecha com força de torno em volta do meu colarinho."

    play sound "audio/sfx/sfx_impacto_corpo.ogg"
    with vpunch
    "Sou puxado bruscamente para trás de uma coluna de sustentação. Minhas costas batem na pedra áspera."

    show lility presas agressiva meio corpo at sprite_padrao with dissolve
    $ th_voz("climax/lility_ponto_cego")

    mestra "Silêncio... Nem um suspiro, meu cachorrinho."

    "A respiração gélida toca meu pescoço. O perfume de lírios secos e sangue antigo enche o ar confinado atrás da pilastra."

    "A menos de cinco metros de onde estamos, o som rítmico de solas de borracha ecoa pelo piso. Uma patrulha de dois monitores de branco passa com lanternas halógenas varrendo o chão."

    "Os passos se afastam até desaparecerem na direção do pátio central."

    show lility sorrindo de lado sorrindo at sprite_padrao with dissolve
    mestra "Cães cegos... Guiados por lanternas de pilha enquanto a verdadeira noite passa ao lado deles."

    show lility meio corpo sorriso malicioso at sprite_padrao with dissolve
    mestra "Você demorou para visitar o meu piano hoje, Victor. O Grilhão me impede de cruzar os salões nobres da Presidente, mas nada me impede de caçar na minha própria periferia... e você cheira a sangue vivo."

    menu:
        "Ceder ao Transe de Sangue Furtivo na escuridão":
            $ fome_sangue = min(100, fome_sangue + 50)
            $ vinculo_sangue_lility = min(100, vinculo_sangue_lility + 15)
            $ status_lility.afeto += 2
            $ humanidade = max(0, humanidade - 2)
            show lility presas agressiva meio corpo at sprite_padrao with dissolve
            "Inclino a cabeça, expondo a pulsação da carótida nas sombras. Minha mestra sorri; suas presas afundam sem aviso, perfurando com uma doçura gélida que anestesia a dor."
            "O êxtase da troca carmesim percorre minha espinha enquanto os passos distantes da ronda ainda vibram no piso (+50%% Saciedade | +15 Vínculo | -2 Humanidade)."
            $ notificar_rpg("🩸 TRANSE NAS SOMBRAS", "+50% Saciedade | +15 Vínculo Carmesim | -2 Humanidade", "#ff2244")

        "Peça com educação, mestra. Eu não sou um frasco de transfusão que você aborda no escuro.":
            $ dominio_jogador = getattr(store, "dominio_jogador", 0) + 1
            $ status_lility.afeto += 1
            show lility meio corpo desdenhando at sprite_padrao with dissolve
            "Sustento o olhar carmesim dela sem recuar um milímetro. Por um instante, as presas dela se retraem e um brilho de divertimento genuíno dança em seus olhos."
            mestra "Olhe só... A cria acha que aprendeu a morder. Muito bem, Victor. Da próxima vez deixarei um convite formal debaixo do seu travesseiro... Mas não espere gentileza."
            $ notificar_rpg("👑 DOMÍNIO AFIRMADO", "+1 Domínio | Respeito mútuo afirmado", "#ffd700")

        "Alertar sobre os refletores da torre e recuar com cautela":
            $ intelecto += 1
            $ exposicao = max(0, exposicao - 10)
            show lility comportada sorriso meio corpo at sprite_padrao with dissolve
            "Os refletores da torre norte varrem este corredor a cada três minutos. Se nos pegarem aqui, o Grêmio terá o pretexto que procura."
            mestra "Prudente até o último fio de cabelo... Você sobreviveria muito tempo na corte antiga, Victor. Vamos nos mover antes que as luzes nos alcancem."
            $ notificar_rpg("🧠 CAUTELA", "+1 Intelecto | -10% Exposição", "#38bdf8")

    hide lility with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 3. VIGÍLIA À MEIA-NOITE NO BELICHE (Quarto de Victor no Dormitório)
# ------------------------------------------------------------------------------
label ev_visita_noturna_lility_dormitorio:
    $ ev_visita_dormitorio_lility_visto = True
    $ local_atual = "dormitorio"
    call restaurar_fundo_local_atual
    play music "audio/sighs_in_the_dark.ogg" if_changed fadein 1.5

    "Acordo no meio da madrugada com um arrepio súbito nas omoplatas. O ar do quarto está gélido, condensando minha respiração em pequenas nuvens de vapor cinzento."

    "Sob a luz prateada da lua que atravessa a persiana entreaberta, há alguém sentada na borda da minha escrivaninha de madeira compensada."

    show lility comportada sorriso meio corpo at sprite_direita with dissolve
    $ th_bark("lility", "padrao")

    "Ela segura entre os dedos longos o pedaço de folha pautada que colei ao lado do beliche: o papel onde anotei as quatro regras de sobrevivência a lápis."

    mestra "Regra número um: 'Não olhar nos olhos dela por mais de três segundos'... Que conselho pueril, Victor. Seus olhos já pertenciam a mim no segundo em que a porta do piano bateu."

    show lility meio corpo desdenhando at sprite_direita with dissolve
    mestra "Regra número dois: 'Manter a tranca de ferro fechada após o toque de recolher'. Como se fechaduras forjadas por ferreiros humanos contivessem uma presença que aprendeu a andar antes de Roma queimar."

    mestra "Mas a última... A regra número quatro é a única que realmente importa: 'Nunca se tornar descartável'."

    "Ela dobra a folha com uma delicadeza quase reverente e a deixa sobre o livro de anatomia."

    mestra "Foi por essa única linha que você sobreviveu naquela noite no corredor. Quando Nora perdeu a cabeça e quase arrancou a sua garganta, você não implorou nem rezou para santos... Você apenas cravou as unhas no chão e brigou por cada segundo de ar."

    show lility sorrindo de lado sorrindo at sprite_direita with dissolve
    $ th_voz("climax/lility_visita_quarto_01")
    mestra "Aquela fome desesperada de viver... Confesso que quase senti inveja de um mortal."

    menu:
        "Você já se sentiu descartável algum dia, Mestra?":
            $ status_lility.afeto += 3
            show lility com vergonha olhando de lado at sprite_direita with dissolve
            "Um silêncio pesado preenche o quarto. Por um breve instante, a altivez de predadora cede lugar a uma melancolia profunda, como uma estátua esquecida sob séculos de poeira."
            $ th_voz("climax/lility_visita_quarto_02")
            mestra "Quando os reis que juraram me proteger queimaram as próprias bibliotecas para apagar o meu nome... sim. Ser esquecida é a forma mais refinada de descarte que a humanidade inventou. Não cometa o mesmo erro comigo, Victor."
            $ notificar_rpg("🖤 REVELAÇÃO ÍNTIMA", "+3 Afeto com a Mestra", "#ff88aa")

        "Convidá-la a sentar ao lado do beliche e dividir o calor do quarto":
            $ vinculo_sangue_lility = min(100, vinculo_sangue_lility + 20)
            show lility sorrindo de lado sorrindo at sprite_direita with dissolve
            "Sento-me na beira do colchão fino e afasto o cobertor. Ela se aproxima em silêncio absoluto. O corpo dela não tem calor biológico, mas a proximidade do seu vestido exala um torpor magnético que afasta toda a dor da semana."
            mestra "Um leito de bolsista em um castelo em ruínas... Curioso como as jaulas mais simples são as que guardam as conversas mais perigosas."
            $ notificar_rpg("🩸 LAÇO CARMESIM", "+20 Vínculo com a Mestra", "#ff2244")

        "Se os inspetores do terceiro andar virem você aqui, o Grêmio lacrará este quarto.":
            $ intelecto += 1
            show lility meio corpo desdenhando at sprite_direita with dissolve
            mestra "Os inspetores deste corredor estão sonhando com medalhas de honra e ceias quentes. Ninguém acorda enquanto eu desejar que durmam... Mas você tem razão. Nosso jogo precisa de plateia na hora certa."
            $ notificar_rpg("🧠 NOÇÃO TÁTICA", "+1 Intelecto", "#38bdf8")

    show lility comportada sorriso meio corpo at sprite_direita with dissolve
    mestra "Descanse os ossos, lacaio. O sangue de amanhã precisará de força para resistir ao que está por vir."
    hide lility with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 4. A DAMA DO ABISMO E A NOVIÇA DA LUZ (Embate Noturno Emília vs Lility)
# ------------------------------------------------------------------------------
label ev_embate_noturno_lility_emilia:
    $ ev_embate_noturno_lility_emilia_visto = True
    $ local_atual = "biblioteca"
    call restaurar_fundo_local_atual
    play music "audio/obscura.ogg" if_changed fadein 1.5

    "A biblioteca noturna é um labirinto de carvalho escuro e poeira secular. Entro pelo corredor das enciclopédias e estanco os passos imediatamente."

    "Entre duas estantes de tomo canônico, a luz tênue de um candelabro ilumina duas figuras frente a frente."

    show emilia uniforme seria triste meio corpo at sprite_esquerda with dissolve
    show lility presas agressiva meio corpo at sprite_direita with dissolve

    "Emília está com uma das mãos segurando firmemente o relicário de prata sobre o peito. Seus nós dos dedos estão brancos pela pressão. À sua frente, Lyra apoia as costas numa prateleira de pergaminhos, com um sorriso insolente que desdenha do crucifixo."

    $ th_voz("climax/emilia_embate_lility")
    emilia "Você não deveria estar aqui, criatura. O Decreto de Restrição de Lorde Phillip e o Tratado da Fundação impõem o seu confinamento absoluto na ala leste."

    show lility meio corpo desdenhando at sprite_direita with dissolve
    mestra "Ah, a pequena noviça do coro... Sua fé é admirável, criança, mas sua leitura jurídica é deplorável. O Grilhão de Elara proíbe os salões nobres do Conselho e as saídas da muralha. Esta ala abandonada é solo neutro."

    show lility sorrindo de lado sorrindo at sprite_direita with dissolve
    $ th_voz("climax/lility_embate_emilia")
    mestra "Diga-me, Emília... Você reza com tanta devoção para salvar a alma de Victor, mas o que oferece a ele? Sermões sobre penitência e martírio enquanto a carne dele se decompõe de fome?"

    show emilia uniforme severa meio corpo at sprite_esquerda with dissolve
    emilia "Ofereço a salvação e o direito de continuar humano! Você só quer um cão que lamba o chão por onde você passa e sacie sua decadência milenar!"

    show lility presas agressiva meio corpo at sprite_direita with dissolve
    mestra "Uma coleira banhada em água benta continua sendo uma coleira, noviça."

    menu:
        "Emília tem razão, mestra. Guarde o veneno e respeite o espaço dos outros.":
            $ status_emilia.afeto += 2
            $ status_lility.afeto = max(0, status_lility.afeto - 1)
            show emilia uniforme seria triste meio corpo at sprite_esquerda with dissolve
            $ th_voz("climax/emilia_aviso_relicario")
            emilia "Obrigada, Victor... Um pulso frio não o condenará, mas deixar que ela devore sua humanidade o fará. Segure a cruz de prata antes que os sinos dobrem."
            show lility meio corpo gelida at sprite_direita with dissolve
            mestra "Patético. Defendendo quem o prenderia numa cela assim que seus caninos crescessem mais dois milímetros... Não se esqueça de quem o alimentou primeiro, Vane."
            $ notificar_rpg("✝️ APOIO A EMÍLIA", "+2 Afeto Emília | -1 Afeto com a Mestra", "#55aaff")

        "Ela está dentro do perímetro permitido, Emília. Guarde o relicário.":
            $ status_lility.afeto += 2
            $ status_emilia.afeto = max(0, status_emilia.afeto - 1)
            show lility comportada sorriso meio corpo at sprite_direita with dissolve
            mestra "Ouviu o rapaz, noviça? Ele prefere a verdade nua e crua ao conforto hipócrita dos seus hinos."
            show emilia uniforme chocada meio corpo at sprite_esquerda with dissolve
            emilia "Você está cego, Victor... A influência dela já contaminou a sua mente mais do que eu temia."
            $ notificar_rpg("🩸 APOIO A LILITY", "+2 Afeto com a Mestra | -1 Afeto Emília", "#ff2244")

        "Parem as duas! Nenhuma de vocês tem o direito de decidir o meu destino como se eu não estivesse aqui!":
            $ coragem = getattr(store, "coragem", 0) + 1
            $ intelecto += 1
            show emilia uniforme seria triste meio corpo at sprite_esquerda with dissolve
            show lility meio corpo maravilhada at sprite_direita with dissolve
            "Ambas se calam diante do meu tom firme. Por um segundo, a tensão estala no ar como pólvora fria."
            emilia "Victor... eu só não quero ver você se perder."
            mestra "Hmph... Ele rosna para as duas donas da coleira. Talvez haja algo digno de ser preservado sob esse uniforme cinzento, afinal."
            $ notificar_rpg("⚡ POSTURA INDEPENDENTE", "+1 Coragem | +1 Intelecto | Respeito mútuo forçado", "#ffd700")

    hide emilia with dissolve
    hide lility with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 5. A COBRANÇA NO PÁTIO DA ÁRVORE (Valéria vs Lility / Pagamento de Giz)
# ------------------------------------------------------------------------------
label ev_negociacao_sombra_lility_valeria:
    $ ev_negociacao_lility_valeria_visto = True
    $ local_atual = "patio_arvore"
    call restaurar_fundo_local_atual
    play music "audio/steel_loop.ogg" if_changed fadein 1.5

    "No canto escuro do Pátio da Árvore, atrás dos canteiros de hera venenosa, ouço passos pesados subindo do poço de exaustão das caldeiras."

    "Valéria surge limpando as mãos de graxa em uma estopa, carregando uma maleta reforçada com travas de bronze. Lyra a aguarda na penumbra das raízes antigas."

    show valeria cinica suspensorios meio corpo at sprite_esquerda with dissolve
    show lility meio corpo desdenhando at sprite_direita with dissolve

    valeria "Aqui está o lote especial de giz rúnico das catacumbas, senhorita 'Lyra'. O frete até a superfície custa caro quando o Grilhão de Elara assa os seus pezinhos se descer três degraus."

    show lility presas agressiva meio corpo at sprite_direita with dissolve
    mestra "Controle o tom da sua língua de ratazana dos porões. Entregue o estojo."

    valeria "Entregar de graça? Sessenta créditos na bucha, alteza. A fornalha roda a carvão, não a fidalguia falida da Baviera."

    "Lyra nem se dá ao trabalho de procurar moedas no vestido de veludo. Ela se vira lentamente para mim com um olhar de comando absoluto:"

    show lility meio corpo mal humorada at sprite_direita with dissolve
    mestra "Pague a garota, Victor. Não tenho paciência para negociar com engrenagens."

    menu:
        "Pagar a encomenda da senhorita Lyra ($60 Créditos)" if dinheiro_jogador >= 60:
            $ dinheiro_jogador -= 60
            $ status_valeria.afeto += 2
            $ status_lility.afeto += 2
            show valeria casaco verde sorriso meio corpo at sprite_esquerda with dissolve
            $ th_voz("climax/valeria_marco_partilha")
            valeria "Meio a meio no contrabando do Conselho. Não fique ganancioso, Victor, ou eu vendo o seu rastro para os cães da guarda. O giz é de vocês."
            show lility comportada sorriso meio corpo at sprite_direita with dissolve
            mestra "Conveniente. Pegue o giz e leve para o meu piano, Victor. Um lacaio prestativo poupa aborrecimentos desnecessários."
            $ notificar_rpg("💰 ACORDO QUITADO", "-$60 Créditos | +2 Afeto Valéria | +2 Afeto com a Mestra", "#00ffcc")

        "Auditar a entrega: o lacre da Fundação está violado (-$30)" if intelecto >= 2 and dinheiro_jogador >= 30:
            $ dinheiro_jogador -= 30
            $ status_valeria.afeto += 1
            $ status_lility.afeto += 2
            show valeria cinica pirulito meio corpo at sprite_esquerda with dissolve
            "O lacre de chumbo está rompido, Valéria. Você abriu esse estojo nas caldeiras. Pela regra do mercado negro, entrega violada tem 50%% de desconto."
            valeria "Droga, Vane... Você tem olho de agiota. Trinta créditos e estamos quites."
            show lility sorrindo de lado sorrindo at sprite_direita with dissolve
            mestra "Magnífico. O rapaz aprendeu a lidar com os abutres. Entregue o pacote e volte para o seu buraco, garota."
            $ notificar_rpg("🧠 AUDITORIA PRECISA", "-$30 Créditos | +2 Afeto com a Mestra", "#ffd700")

        "Não tenho dinheiro. Oferecer serviço braçal nas Caldeiras para quitar a dívida":
            $ status_valeria.afeto += 3
            $ status_lility.afeto += 1
            $ energia_jogador = max(0, getattr(store, "energia_jogador", 100) - 20)
            show valeria cinica confiante meio corpo at sprite_esquerda with dissolve
            valeria "Gostei da proposta, Vane! Desça até a fornalha número quatro amanhã e limpe a tubulação de vapor. O giz fica entregue por conta da sua mão de obra."
            show lility meio corpo desdenhando at sprite_direita with dissolve
            mestra "Trabalho braçal para quitar a minha despesa... Humilhante, mas prático. Honre sua palavra com a mecânica, Victor."
            $ notificar_rpg("🔧 TRABALHO DE COMPENSAÇÃO", "Dívida quitada com serviço | +3 Afeto Valéria", "#f59e0b")

    hide valeria with dissolve
    hide lility with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 6. O EUFEMISMO DA CONTENÇÃO Nº 31 (O Rastro de Nora na Enfermaria)
# ------------------------------------------------------------------------------
label ev_rastro_oculto_nora_enfermaria:
    $ ev_rastro_nora_enfermaria_visto = True
    $ local_atual = "enfermaria"
    call restaurar_fundo_local_atual
    play music "audio/obscura.ogg" if_changed fadein 1.5

    "Aproveito um momento em que a Enfermeira Clara Vance se afasta para o biombo de curativos e me aproximo do armário de aço arquivador."

    "Entre as pastas de transferências de alunos do último mês, meus dedos encontram uma guia de remessa interna timbrada com o selo do Conselho Estudantil:"

    "📋 REQUISIÇÃO CONTÁBIL E MÉDICA — PROTOCOLO SIGILOSO #31"
    "Paciente: Nora Vasques (Bolsista de Monitoria / Removida do Convívio)"
    "Condição Clínica: 'Surto de fúria hemolítica incontrolável decorrente de contaminação por miasma'."
    "Observação da Presidência: 'Confinada na cápsula de contenção da Cripta. Risco crítico de colapso de barreira: solta, ela dilaceraria doze estudantes por quinzena'."
    "Destino da Entrega: Câmara Subterrânea de Isolamento (Cripta Ancestral / Subsolo Profundo)"

    "Um calafrio gélido percorre minhas veias."

    "Quando confrontei a Presidente Elara sobre o desaparecimento de Nora, as palavras exatas dela ecoam na minha memória:"

    $ th_bark("elara", "nora_desvio")
    elara "O prontuário dos sujeitos de teste está selado por decreto da presidência, Bolsista Vane. Continue fazendo perguntas sobre Nora e dividirá a ala de isolamento com ela."

    "Ela nunca disse que Nora estava morta. Ela usou o vocabulário asséptico da burocracia para esconder a verdade: trancou a garota viva numa cápsula de vidro no fundo da Cripta, transformando-a em um filtro vivo para conter a fúria canibal que a escola não consegue curar!"

    play sound "audio/sfx/sfx_psiquico_distorcao_sanidade.ogg"
    $ th_voz("climax/nora_cripta_sussurro")
    "Nas profundezas do meu pensamento, o eco daquele sussurro agonizante da Cripta retorna como uma assombração: 'Victor... os jalecos brancos... eles tiraram o tutano dos meus ossos. Não deixe Elara te trancar na Enfermaria Quatro!'"

    $ intelecto += 1
    $ conhecimento_oculto += 1
    $ notificar_rpg("🔍 PISTA CRUCIAL", "+1 Intelecto | +1 Conhecimento Oculto | Segredo de Nora descoberto!", "#ffd700")

    "Se houver uma maneira de purificar a corrupção do miasma que enlouqueceu Nora, talvez ela possa ser salva..."
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 7. A JANELA ABERTA NO DILÚVIO & O LAPSO DO PASSADO (Lility)
# ------------------------------------------------------------------------------
label ev_c01_janela_lility:
    $ ev_janela_lility_visto = True
    $ local_atual = "sala_musica"
    if periodo == "Noite":
        scene bg animado sala musica piano vitral chuva at luz_sombra_noturna with dissolve
    else:
        scene bg animado sala musica piano vitral chuva with dissolve
    play music "audio/weeping_cello.ogg" if_changed fadein 1.5

    "A chuva torrencial açoita os vitrais góticos da Sala de Música com a violência de um naufrágio. O som dos trovões graves faz as cordas do piano de cauda vibrarem sozinhas em harmônicos dissonantes."

    show lility comportada sorriso meio corpo at sprite_padrao with dissolve
    $ th_bark("lility", "padrao")

    mestra "Abra os trincos de bronze, Victor. Deixe o ar entrar."

    "Puxo as alavancas pesadas. Uma lufada de vento gélido e gotículas de chuva invade a sala, agitando as partituras espalhadas sobre o tapete persa."

    show lility meio corpo melancolica at sprite_padrao with dissolve
    mestra "Ouça a tempestade... Quarenta minutos de chuva contínua e a cidade dos homens já se afoga em esgotos transbordados e blecautes."

    "Comento sobre os manuscritos que Emília encontrou sobre a queda das dinastias antigas de vampiros durante o grande dilúvio."

    "Os olhos da minha mestra se estreitam. O tom dela muda sutilmente — não como quem leu um livro de história, mas como quem sentiu a terra tremer sob os pés:"

    show lility sorrindo de lado sorrindo at sprite_padrao with dissolve
    mestra "Os templos não cheiravam a incenso sagrado como aquela noviça pensa... Cheiravam a cinzas úmidas e óleo de mirra barato. E os reis que juravam imortalidade gritaram exatamente como camponeses quando as comportas cederam..."

    "Ela para no meio da frase. Seus olhos encontram os meus e ela percebe o lapso da testemunha viva."

    "Um sorriso sedutor, predador e perigoso dança em seus lábios carmesins:"

    show lility comportada sorriso meio corpo at sprite_padrao with dissolve
    mestra "Esqueça o passado, Victor. O passado é poeira cinzenta... O presente tem sangue fresco esperando por nós."

    menu:
        "Estarei ao seu lado, Mestra. O presente é o que importa.":
            $ vinculo_sangue_lility = min(100, vinculo_sangue_lility + 15)
            $ status_lility.afeto += 2
            show lility presas agressiva meio corpo at sprite_padrao with dissolve
            mestra "Então segure firme a borda deste vitral... e deixe o frio moldar a sua nova forma."
            $ notificar_rpg("🩸 JURAMENTO NO DILÚVIO", "+15 Vínculo Carmesim | +2 Afeto", "#ff2244")

        "Guardar na memória a confirmação de que ela viveu aquela era":
            $ intelecto += 1
            $ conhecimento_oculto += 1
            show lility comportada sorriso meio corpo at sprite_padrao with dissolve
            mestra "Sempre o arquiteto que analisa as fundações... Continue observando, Victor. Talvez você entenda por que este castelo está condenado."
            $ notificar_rpg("🧠 DEDUÇÃO OCULTA", "+1 Intelecto | +1 Conhecimento Oculto", "#38bdf8")

    hide lility with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 8. TRIAGEM DA CAMPANHA DE SAÚDE (Enfermeira Clara Vance - Mutação Vampírica)
# ------------------------------------------------------------------------------
label ev_c02_triagem_enfermaria:
    $ ev_triagem_enfermaria_visto = True
    $ local_atual = "enfermaria"
    call restaurar_fundo_local_atual
    play music "audio/the_hunger_of_ancient_gods.ogg" if_changed fadein 1.5

    "A fila de bolsistas se arrasta pelo corredor da Enfermaria sob a iluminação fluorescente e asséptica. Emília está na ponta da fila, auxiliando os alunos a preencher formulários com um olhar preocupado."

    show emilia uniforme seria triste meio corpo at sprite_esquerda with dissolve
    emilia "Victor... Tome cuidado lá dentro. A Enfermeira Clara Vance está recolhendo amostras para a junta da Fundação. Ela é extremamente meticulosa com os hemogramas."

    hide emilia with dissolve
    show mob enfermeira neutra at sprite_direita with dissolve
    $ th_bark_mob("abordagem")

    mob_enfermeira "Sente-se na cadeira de exames, senhor Vane. Manga esquerda levantada, por favor."

    "Ela posiciona o estetoscópio gelado sobre meu peito. Os segundos passam em um silêncio incômodo. Noto os olhos de Clara se estreitarem sob as lentes dos óculos finos."

    show mob enfermeira desconfiada at sprite_direita with dissolve
    mob_enfermeira "Curioso... O ritmo cardíaco mal atinge vinte batimentos por minuto. E sua temperatura dérmica está em trinta e um graus cravados."

    "Ela aplica uma lanceta de prata na ponta do meu dedo anelar. A gota de sangue que brota preenche o tubo capilar de vidro."

    mob_enfermeira "Seu prontuário de admissão registra sangue Rh-Nulo, sim... Mas sangue humano oxigena e coagula em contato com o ar ambiente!"

    show mob enfermeira medo at sprite_direita with dissolve
    mob_enfermeira "Isto aqui não coagula... As hemácias estão em torpor cristalino, emitindo uma leve fosforescência dourada sob a lâmpada de mercúrio... Você deveria estar em uma maca do IML, senhor Vane. Biologicamente, este tecido está morto!"

    menu:
        "Subornar a Enfermeira com $80 para registrar hemograma normal" if dinheiro_jogador >= 80:
            $ dinheiro_jogador -= 80
            show mob enfermeira sorrindo at sprite_direita with dissolve
            mob_enfermeira "Cinquenta selos e trinta créditos... Muito bem, senhor Vane. Vou lançar este hemograma como O-Positivo com anemia ferropriva. Mas se a Presidente Elara exigir contraprova, você nunca esteve nesta sala."
            show expression obter_sprite_victor("confiante") as victor at sprite_esquerda with dissolve
            victor "(A discrição dela tem preço exato. Enquanto os créditos caírem na gaveta, o segredo da mutação não chega à mesa da presidência.)"
            hide victor with dissolve
            $ notificar_rpg("🤫 RELATÓRIO ADULTERADO", "-$80 Créditos | Mutação acobertada", "#00ffcc")

        "Usar o Olhar Hipnótico para apagar os últimos minutos" if fome_sangue >= 40:
            $ fome_sangue -= 15
            $ exposicao = max(0, exposicao - 15)
            show mob enfermeira transe at sprite_direita with dissolve
            "Concentro minha vontade. O brilho carmesim nos meus olhos reflete nas lentes dela. A expressão de Clara fica vazia, os braços pendem frouxos."
            "Ela carimba o prontuário como 'Apto para Atividades Regulares' em transe completo antes de se sentar na mesa sem se lembrar da gota dourada."
            show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve
            victor "(Os olhos dela estão completamente vidrados... O comando mental apagou o diagnóstico da lanceta. Para a Fundação, continuo sendo apenas um bolsista anêmico.)"
            hide victor with dissolve
            $ notificar_rpg("👁️ HIPNOSE CLÍNICA", "-15% Fome de Sangue | -15% Exposição", "#ffd700")

    hide mob enfermeira with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 9. A SEGUNDA PARCELA DO TERMO Nº 112 (Dívida de Teo no Corredor)
# ------------------------------------------------------------------------------
label ev_c03_divida_teo_corredor:
    $ ev_divida_teo_fase1_visto = True
    # Ancora no corredor da academia para garantir sincronização de fundo
    $ local_atual = "corredor_academia"
    call restaurar_fundo_local_atual
    play music "audio/The_Cold_Decree.ogg" if_changed fadein 1.5

    "No corredor dos armários, dois alunos veteranos com braçadeiras de monitores encurralam Teo contra os cacifos de metal."

    "Monitor A" "O vencimento da segunda parcela do Termo 112 era ao meio-dia, garoto. Se não tem os créditos, a alternativa do Conselho é assinar a autorização de coleta tripla na Enfermaria."

    $ th_voz("mobs/teo_bark_divida_01")
    "Teo" "P-Por favor... Se eu doar mais duas bolsas esta semana, não consigo ficar em pé na aula de botânica! Minha visão está embaçando desde terça-feira..."

    "Monitor B" "A Diretoria não financia fraqueza, bolsista. Assine ou entregue a chave do quarto."

    menu:
        "Intervir e pagar a dívida de Teo ($80 Créditos)" if dinheiro_jogador >= 80:
            $ dinheiro_jogador -= 80
            $ teo_salvo_segunda_parcela = True
            $ humanidade = min(100, humanidade + 5)
            "Aproximo-me com passos firmes e jogo a bolsa de oitenta créditos no peito do monitor."
            "A conta está paga. Soltem o garoto e saiam do corredor antes que eu registre abuso de autoridade com a presidência do Grêmio."
            "Os fiscais contam as moedas de má vontade, bufam e se afastam pelo corredor."
            $ th_voz("mobs/teo_bark_alivio_02")
            "Teo" "V-Victor... Eu não sei como te agradecer. Eu juro que vou trabalhar dobrado nas estufas para te devolver cada centavo!"
            $ notificar_rpg("🛡️ VIDA SALVA", "-$80 Créditos | +5 Humanidade | Teo em débito moral", "#00ffcc")

        "Intimidar os monitores usando a aura predatória do Sangue" if humanidade <= 50:
            $ exposicao = min(100, exposicao + 10)
            $ coragem = getattr(store, "coragem", 0) + 1
            "Dou um passo à frente. O ar ao meu redor fica subitamente pesado; o rangido do metal dos armários vibra sob a pulsação do miasma."
            "O garoto está sob minha responsabilidade. Se derem mais um passo na direção dele, a próxima coleta de sangue será a de vocês nos azulejos."
            "Os dois monitores empalidecem, engolem em seco e recuam tropeçando nos próprios pés."
            $ notificar_rpg("⚡ INTIMIDAÇÃO", "+1 Coragem | +10% Exposição | Fiscais aterrorizados", "#ff2244")

        "Ignorar a cena e seguir em frente":
            $ humanidade = max(0, humanidade - 3)
            "Abaixo a cabeça e continuo caminhando. O som da caneta de Teo tremendo sobre o formulário de doação forçada ecoa atrás de mim."
            $ notificar_rpg("💔 INDIFERENÇA", "-3 Humanidade", "#888888")

    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 10. VOCÊ NÃO COME (Emília Investiga a Degeneração de Victor)
# ------------------------------------------------------------------------------
label ev_c05_voce_nao_come:
    $ ev_c05_voce_nao_come_visto = True
    $ local_atual = "dormitorio"
    call restaurar_fundo_local_atual
    play music "audio/the_keepers_ledger.ogg" if_changed fadein 1.5

    "Entro no refeitório auxiliar do dormitório. Emília está sentada à mesa de pinho com sua xícara de infusão e um caderno encadernado em couro aberto."

    show emilia uniforme seria triste meio corpo at sprite_padrao with dissolve

    emilia "Sente-se um instante, Victor. Por favor."

    "Puxo a cadeira. Ela não toca na própria xícara; seus olhos me analisam com precisão investigativa:"

    emilia "Segunda-feira: bandeja de refeição intacta, pão jogado na lixeira do terceiro andar. Terça-feira: apenas um gole de água da torneira. Quarta-feira: você recusou o almoço dos bolsistas dizendo que estava sem apetite."

    emilia "Você não come nada sólido há quatro dias, Victor. O seu corpo deveria estar desmaiando por hipoglicemia. No entanto, sua força muscular aumentou e suas pupilas reagem à luz como as de uma coruja."

    show emilia uniforme chocada meio corpo at sprite_padrao with dissolve
    emilia "O que você está colocando para dentro do seu corpo quando as luzes se apagam? Responda olhando nos meus olhos."

    menu:
        "Estou sobrevivendo ao veneno desta escola, Emília. Não me faça perguntas que você não suportaria ouvir.":
            $ status_emilia.afeto += 1
            $ intelecto += 1
            show emilia uniforme seria triste meio corpo at sprite_padrao with dissolve
            emilia "Eu suporto a verdade, Victor... O que não suporto é ver você se transformar em mais uma estátua de gelo daquele piano maldito."
            $ notificar_rpg("✝️ VERDADE CRUA", "+1 Intelecto | +1 Afeto Emília", "#38bdf8")

        "Inventar que está passando por um tratamento experimental na Enfermaria":
            $ status_emilia.duvida = getattr(status_emilia, "duvida", 0) + 10
            show emilia uniforme severa meio corpo at sprite_padrao with dissolve
            emilia "Tratamento com a Enfermeira Clara Vance? Aquela mulher é cúmplice de cada atrocidade contábil do Conselho. Se você está confiando a sua saúde a ela, está assinando a sua própria remoção."
            $ notificar_rpg("⚠️ DESCONFIANÇA", "+10 Dúvida de Emília", "#ffaa00")

    hide emilia with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 11. TABELA DE AFINIDADE COM O ESPÉCIME ALFA (O Arquivo de Emília)
# ------------------------------------------------------------------------------
label ev_c06_lista_rh_nulo:
    $ ev_lista_rh_nulo_visto = True
    $ local_atual = "sala_ocultismo"
    call restaurar_fundo_local_atual
    play music "audio/the_hunger_of_ancient_gods.ogg" if_changed fadein 1.5

    "Encontro Emília na sala de estudos alquímicos desativada. As persianas estão fechadas para bloquear a vista do pátio."

    show emilia uniforme severa meio corpo at sprite_padrao with dissolve
    $ th_voz("climax/emilia_investigacao_genealogica")
    emilia "Estas páginas de registro não foram perdidas... Foram cortadas com bisturi cirúrgico há quarenta anos. Alguém queria a sua linhagem enterrada."

    "Sem dizer uma palavra, ela retira um rolo de pergaminho amarelado de dentro da capa do seu breviário e o desenrola sobre a mesa de pedra."

    emilia "Isto estava guardado no cofre da antiga capela. É o documento confidencial da mantenedora:"

    "«TABELA DE TRIAGEM HEMATOLÓGICA & AFINIDADE COM O ESPÉCIME ALFA (PROTOCOLO 1898)»"

    "Abaixo o olhar sobre a folha. Há quarenta e um nomes catalogados ao longo do último século pelo Conselho:"

    "31. NORA VASQUES — 18 ANOS — GRAU DE RESSONÂNCIA: 88%% (TRANSFERÊNCIA CONCLUÍDA / CONFINADA)"

    "E no topo da página, escrito com tinta fresca recente:"

    "41. VICTOR VANE — 19 ANOS — RH NULO PURO — GRAU DE RESSONÂNCIA: 99.8%% (CATALISADOR MÁXIMO)"

    show emilia uniforme seria triste meio corpo at sprite_padrao with dissolve
    $ th_bark("emilia", "phillip_conflito")
    emilia "Você não foi admitido nesta Academia por acaso, Victor. Seu exame de sangue na matrícula acendeu todos os alertas da Fundação."

    emilia "Nora era a trigésima primeira cobaia de teste... Você é o quadragésimo primeiro. Se você não me ajudar a purificar o que está acontecendo no subsolo, você será o próximo a ser jogado em uma cápsula."

    $ conhecimento_oculto += 2
    $ notificar_rpg("📜 TABELA CONFIDENCIAL", "+2 Conhecimento Oculto | Descoberta do Protocolo 1898", "#ffd700")

    hide emilia with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 12. ESCUTA DO DECRETO DE ELARA (Confronto na Porta da Sala de Música)
# ------------------------------------------------------------------------------
label ev_c08_escuta_decreto_elara:
    $ ev_escuta_decreto_elara_visto = True
    $ local_atual = "sala_musica"
    call restaurar_fundo_local_atual
    play music "audio/Authority_Breach.ogg" if_changed fadein 1.5

    "Aproximo-me da porta de carvalho da Sala de Música. As duas sentinelas de sobretudo branco estão postadas do lado de fora, mas o som das vozes atravessa a madeira."

    "Reconheço a cadência gélida e autoritária da Presidente Elara — controlada, precisa e cortante:"

    "Espreito pela fresta entre a madeira pesada e o batente. Lá dentro, a atmosfera é de puro gelo e contenção marcial."

    show elara seria autoritaria meio corpo at sprite_esquerda with dissolve
    show lility meio corpo desdenhando at sprite_direita with dissolve

    $ th_voz("climax/elara_decreto_marcial")
    "Elara" "A ordem não se mantém com compaixão, senhor Vane. Se o selo rachar, eu queimarei esta academia inteira antes de deixar uma anomalia cruzar os portões."

    "Elara" "Você violou a restrição de perímetro na noite de terça-feira, senhorita von Blut. Nossos sensores etéricos registraram sua presença diante do sarcófago do Espécime Alfa. Foi fome? A fidalga menor da Silésia não resistiu à tentação de tentar sugar a energia do nosso reator biológico?"

    "A risada de Lyra ecoa com o deboche de quem olha para uma criança brincando com fósforos:"

    show lility meio corpo sorriso malicioso at sprite_direita with dissolve
    mestra "Sua barreira de giz e salitre está rachando nas quatro pontas, Elara. Você usa a força vital de dezenas de bolsistas para remendar um muro que vai desabar no instante em que o Eclipse alinhar. 'Sugar o espécime'? Sua mente burocrática é verdadeiramente cega."

    show elara irritada e com desprezo at sprite_esquerda with dissolve
    "Elara" "Seus títulos arcaicos não têm peso perante a Fundação. Se você der mais um passo em direção às catacumbas, eu aumento a prata no Grilhão até suas veias arderem. Mantenha-se na sua ala periférica até o meu comitê decidir sua sentença final."

    hide elara
    hide lility
    with dissolve

    "O som de saltos marchando em direção à porta me força a recuar rapidamente para o vão dos armários antes que Elara saia com seus executores."

    $ intelecto += 1
    $ conhecimento_oculto += 1
    $ notificar_rpg("👂 ESCUTA TÁTICA", "+1 Intelecto | +1 Conhecimento Oculto | O erro de Elara", "#38bdf8")

    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 13. O RELATÓRIO DE ODORES DE ELARA (Gabinete da Presidência)
# ------------------------------------------------------------------------------
label ev_c12_relatorio_odores_elara:
    $ ev_relatorio_odores_elara_visto = True
    $ local_atual = "salao_gremio"
    call restaurar_fundo_local_atual
    play music "audio/The_Cold_Decree.ogg" if_changed fadein 1.5

    "Entro no Gabinete do Grêmio. A Presidente Elara está sentada atrás da mesa de mogno lustrado, com uma xícara de porcelana fumegante e pastas pautadas."

    show elara burocrata formal meio corpo at sprite_padrao with dissolve
    $ th_bark("elara", "submundo")

    elara "Feche a porta e sente-se, senhor Vane. Temos assuntos orçamentários e disciplinares a alinhar."

    show elara sorriso frio meio corpo at sprite_padrao with dissolve
    elara "Nossos inspetores da ronda possuem narizes muito bem treinados, Victor. E o relatório olfativo da sua última semana é uma verdadeira antologia de insubordinação."

    elara "Segunda-feira à noite: cheiro de lírios mortos, cera antiga e mofo da ala de música daquela tal de Lyra von Blut."

    elara "Terça-feira à tarde: graxa de engrenagem, óleo queimado e fuligem das Caldeiras da senhorita Valéria."

    elara "Quarta-feira pela manhã: mirra e água benta do breviário da noviça Emília."

    show elara deboche xicara cha meio corpo at sprite_padrao with dissolve
    elara "Você é um rapaz muito sociável, Victor... ou um predador que está tentando jogar em três tabuleiros diferentes ao mesmo tempo."

    show elara seria autoritaria meio corpo at sprite_padrao with dissolve
    elara "Vou lhe fazer uma proposta formal: torne-se meu informante oficial. Traga-me as anotações de Emília e os passos de Lyra fora do perímetro... e em troca, garanto que sua bolsa de estudos e sua cota limpa na Enfermaria permanecerão intocáveis."

    menu:
        "Aceitar a proposta formal de Elara como Agente Duplo":
            $ status_elara.afeto += 2
            $ exposicao = max(0, exposicao - 20)
            $ dinheiro_jogador += 100
            show elara sorriso frio meio corpo at sprite_padrao with dissolve
            $ th_bark("elara", "relatorio_ok")
            elara "Uma decisão lúcida, senhor Vane. Aqui estão cem créditos para suas despesas operacionais. Não me decepcione."
            $ notificar_rpg("💼 PACTO DA FUNDAÇÃO", "+$100 Créditos | -20% Exposição | +2 Afeto Elara", "#ffd700")

        "Recusar a proposta dizendo que não vende informações de colegas":
            $ coragem = getattr(store, "coragem", 0) + 1
            $ status_elara.duvida = getattr(status_elara, "duvida", 0) + 15
            show elara burocrata formal meio corpo at sprite_padrao with dissolve
            $ th_voz("climax/elara_marco_confissao")
            elara "Eles acham que eu uso esta máscara por poder... É uma jaula para impedir que o medo destrua esta instituição. Lembre-se desta recusa quando as contas da Enfermaria chegarem à sua mesa."
            $ notificar_rpg("🛡️ INDEPENDÊNCIA", "+1 Coragem | +15 Dúvida de Elara", "#ffffff")

    hide elara with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 14. FOME SEM PLATÉIA (Valéria e os Três Goles nas Caldeiras)
# ------------------------------------------------------------------------------
label ev_c15_fome_sem_plateia_valeria:
    $ ev_fome_sem_plateia_valeria_visto = True
    $ local_atual = "caldeiras"
    call restaurar_fundo_local_atual
    play music "audio/steel_loop.ogg" if_changed fadein 1.5

    "Desço a escadaria de ferro das Caldeiras com passos trôpegos. O nível da Fome de Sangue caiu perigosamente; minhas gengivas ardem onde as presas empurram a carne."

    "Valéria está ajustando a válvula de vapor da caldeira dois, com uma chave inglesa nas mãos engorduradas. Quando ouve meus passos tropeçando no piso gradeado, ela se vira com o cenho franzido."

    show valeria cinica confiante meio corpo at sprite_padrao with dissolve
    $ th_bark("valeria", "padrao")

    valeria "Ei, Vane, se veio pedir fiado de novo..."

    "Ela para no meio da frase quando a luz da fornalha ilumina meu rosto pálido e as pupilas dilatadas."

    show valeria cinica suspensorios meio corpo at sprite_padrao with dissolve
    $ th_voz("climax/valeria_fome_secreta")
    valeria "Você acha que é o único que pula refeições para não perder a cabeça? Quando as caldeiras rugem, ninguém ouve o seu estômago berrar. Se os cães de branco te virem assim, vão te abater antes do corredor."

    "Ela solta a chave inglesa sobre a bancada com um estrondo metálico, limpa o antebraço com um pano e arregaça a manga de couro cru."

    show valeria amigavel neutra meio corpo at sprite_padrao with dissolve
    valeria "Três goles, Vane. Nem uma gota a mais. Se você rasgar a minha artéria, eu te jogo dentro da fornalha três antes de desmaiar. Entendeu o contrato?"

    play sound "audio/sfx/sfx_impacto_corpo.ogg"
    with vpunch
    "Eu a puxo contra a parede de tijolos. Minhas presas cravam na dobra do braço dela com sofreguidão."

    play sound "audio/sfx/stinger_fome_frenesi.ogg"
    "O primeiro trago desce como fogo líquido, queimando a aridez da garganta."

    valeria "Ugh... Um..."

    play sound "audio/sfx/stinger_fome_frenesi.ogg"
    "O segundo gole restaura a nitidez da visão; o batimento compassado do coração dela guia a sucção."

    valeria "D-Dois... Vai devagar, seu monstro..."

    play sound "audio/sfx/stinger_fome_frenesi.ogg"
    "O terceiro trago é doce, impregnado de ferro e adrenalina pura."

    valeria "Três... e... e meio..."

    "Os joelhos de Valéria fraquejam; suas mãos se apoiam nos meus ombros com os dedos cravados no casaco. Afasto as presas com esforço, respirando pesado."

    $ fome_sangue = min(100, fome_sangue + 45)
    $ vinculo_sangue_valeria = min(100, getattr(store, "vinculo_sangue_valeria", 0) + 25)
    $ status_valeria.afeto += 3
    $ humanidade = max(0, humanidade - 2)

    show valeria cinica pirulito meio corpo at sprite_padrao with dissolve
    $ th_bark("valeria", "toque_submissa")
    valeria "Ufa... Você suga com a força de uma bomba hidráulica, Vane... Mas admito que a fornalha pareceu menos fria por um segundo."

    "Ela enrola uma tira de gaze apertada em volta do braço:"

    valeria "Agora limpe a boca antes de subir. E lembre-se: essa transfusão nunca existiu na minha contabilidade."

    $ notificar_rpg("🩸 BANQUETE NAS CALDEIRAS", "+45% Saciedade | +25 Vínculo Valéria | +3 Afeto | -2 Humanidade", "#ff2244")

    hide valeria with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 15. INVESTIGAÇÃO GENEALÓGICA: QUEM É LYRA VON BLUT? (Biblioteca com Emília)
# ------------------------------------------------------------------------------
label ev_c16_investigacao_genealogica_lyra:
    $ ev_c16_investigacao_lyra_visto = True
    $ local_atual = "biblioteca"
    call restaurar_fundo_local_atual
    play music "audio/obscura.ogg" if_changed fadein 1.5

    "Encontro Emília sentada na ala de heráldica e registros genealógicos da biblioteca. À sua frente repousam três tomos encadernados em couro de novilho com brasões dourados desbotados."

    show emilia uniforme seria triste meio corpo at sprite_padrao with dissolve
    $ th_bark("emilia", "padrao")

    emilia "Victor... Eu estive revisando os cadastros de transferência do Conselho Estudantil a pedido da capelania."

    emilia "Você já ouviu falar daquela moradora reclusa da Sala de Música? Aquela tal de 'Lyra von Blut'?"

    "Sustento a respiração, mantendo a expressão neutra."

    show emilia uniforme severa meio corpo at sprite_padrao with dissolve
    emilia "Von Blut... Que sobrenome mais óbvio e pretensioso. Meu pai sempre dizia que fidalgos de clãs menores empobrecidos adoram inventar nomes pomposos para esconder a falta de terras e dotes."

    emilia "Pois bem: passei a tarde inteira folheando o Livro de Ouro da Nobreza da Baviera, da Silésia e da Boêmia. Não existe nenhum registro histórico de uma família 'von Blut'. O brasão que consta na ficha dela foi desenhado com tinta recente."

    "Ela desliza o dedo por uma anotação em latim medieval na margem de um manuscrito do século dezessete:"

    emilia "Mas em um relato antigo sobre as primeiras concessões de terra desta colina, há uma menção em aramaico arcaico a uma dama pálida que habitava este vale antes da primeira pedra da escola ser erguida. O cronista a chamava apenas por uma raiz: 'Lili...' antes do texto ser raspado com faca."

    show emilia uniforme chocada meio corpo at sprite_padrao with dissolve
    emilia "Quem quer que ela seja, Victor... ela não é uma estudante estrangeira. Ela está usando a escola como disfarce."
    $ segredo_lility_revelado = True
    $ persistent.eco_sabe_identidade_lility = True
    "Lili... Lility. Essa é a verdade por trás do disfarce de Lyra von Blut. Ela é a entidade milenar deste vale."

    menu:
        "Apoiar as suspeitas de Emília e prometer investigar mais a fundo":
            $ status_emilia.afeto += 2
            $ intelecto += 1
            show emilia uniforme seria triste meio corpo at sprite_padrao with dissolve
            emilia "Tome muito cuidado, Victor. Se ela enganou até a burocracia do Conselho, ela é capaz de qualquer coisa."
            $ notificar_rpg("✝️ ALIANÇA INVESTIGATIVA", "+2 Afeto Emília | +1 Intelecto", "#55aaff")

        "Desviar o foco dizendo que é apenas excentricidade de aluna rica":
            $ exposicao = max(0, exposicao - 10)
            show emilia uniforme severa meio corpo at sprite_padrao with dissolve
            emilia "Você sempre tenta justificar o injustificável... Mas os registros não mentem."
            $ notificar_rpg("🤫 DISSIMULAÇÃO", "-10% Exposição", "#38bdf8")

    hide emilia with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 16. O DILÚVIO DO MIASMA (Inundação de Água Negra nas Galerias Inferiores)
# ------------------------------------------------------------------------------
label ev_c17_inundacao_agua_negra:
    $ ev_c17_inundacao_agua_negra_visto = True
    $ local_atual = "catacumbas"
    call restaurar_fundo_local_atual
    play music "audio/the_hunger_of_ancient_gods.ogg" if_changed fadein 1.5

    "Um estrondo subterrâneo faz as vigas de sustentação gemerem. Pelos ralos das galerias de serviço e pelas frestas dos azulejos, uma água espessa, negra e pútrida começa a borbulhar com violência."

    "O cheiro que invade o corredor é insuportável: sangue decomposto há milênios misturado a salitre e ozônio."

    show valeria cinica suspensorios meio corpo at sprite_padrao with dissolve
    $ th_bark("valeria", "lote_contaminado")

    valeria "Vane! Saia da linha de drenagem! A câmara três do subsolo rompeu as comportas! Essa água vem direto do lençol freático onde a tumba está afundada!"

    "A água negra queima as solas dos meus sapatos como ácido fraco. Ratos cegos e insetos de casca pálida fogem em cardumes pelas paredes, em pânico absoluto."

    valeria "Se essa porcaria alcançar a caldeira principal, a pressão vai estourar o piso do dormitório inteiro! Preciso de ajuda na válvula mestra de exaustão!"

    menu:
        "Arriscar o corpo e ajudar Valéria a girar a válvula incandescente":
            $ status_valeria.afeto += 3
            $ coragem = getattr(store, "coragem", 0) + 1
            $ hp_jogador = max(1, hp_jogador - 15)
            "Agarro a roda de ferro em brasa junto com Valéria. A água negra espirra nos meus braços, queimando a carne pálida, mas forçamos a engrenagem até o trinco bater."
            "A comporta fecha com um estrondo de canhão, desviando a maré pútrida para o poço cego do bosque."
            show valeria casaco verde sorriso meio corpo at sprite_padrao with dissolve
            valeria "Ufa... Essa foi por um triz, Vane. Você tem coragem de sobra para um rapaz de uniforme cinza."
            $ notificar_rpg("🔧 COMPORTA SELADA", "+3 Afeto Valéria | +1 Coragem | -15 HP", "#00ffcc")

        "Usar a força do Sangue Antigo para escorar a comporta com destroços":
            $ vinculo_sangue_valeria = min(100, getattr(store, "vinculo_sangue_valeria", 0) + 15)
            $ fome_sangue = max(0, fome_sangue - 20)
            "Concentro o poder carmesim nas mãos e arrasto uma viga mestra de ferro forjado, calçando a fresta antes que a água transborde."
            show valeria cinica confiante meio corpo at sprite_padrao with dissolve
            valeria "Caramba... Que força anormal é essa? Nem com macaco hidráulico eu levantava essa viga..."
            $ notificar_rpg("⚡ FORÇA ANOMAL", "+15 Vínculo Valéria | -20% Saciedade", "#ff2244")

    hide valeria with dissolve
    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 17. A VIGÍLIA DOS EXECUTORES (A Lei Marcial Noturna de Elara)
# ------------------------------------------------------------------------------
label ev_c18_vigilia_executores_sombra:
    $ ev_c18_vigilia_executores_visto = True
    $ local_atual = "patio_fonte"
    call restaurar_fundo_local_atual
    play music "audio/Authority_Breach.ogg" if_changed fadein 1.5

    "A névoa no Pátio da Fonte é cortada por fachos azuis e brancos de holofotes de mercúrio. O toque de recolher foi elevado à categoria de Lei Marcial."

    "Os monitores comuns foram recolhidos. No lugar deles, patrulham os Executores de Choque do Grêmio: sentinelas de sobretudo branco blindado, máscaras de ferro com fendas de quartzo e rifles de caça com cartuchos de fósforo e prata."

    "Dois executores marcham a menos de dez metros de mim, conduzindo cães de caça com coleiras de cobre que farejam o ar compulsivamente."

    $ th_voz("mobs/executora_bark_lei_marcial")
    "Executor A" "Assinatura biológica detectada na ala leste. Se avistarem qualquer indivíduo com frequência cardíaca abaixo de quarenta batimentos, abram fogo com chumbo de salitre. Ordem expressa da Presidente Elara."

    "Se eu for encurralado por esses homens, serei levado direto para a câmara de dissecação."

    menu:
        "Dissimular-se nas sombras da hera usando furtividade e frieza":
            $ intelecto += 1
            $ exposicao = max(0, exposicao - 15)
            "Prendo a respiração e me fundo à escuridão sob o arco de pedra. O cão rosna na minha direção, mas a névoa úmida dispersa o cheiro do meu sangue antes que o condutor perceba."
            $ notificar_rpg("🌑 FURTIVIDADE PERFEITA", "+1 Intelecto | -15% Exposição", "#38bdf8")

        "Emboscar o sentinela da retaguarda no ponto cego":
            $ coragem = getattr(store, "coragem", 0) + 1
            $ dinheiro_jogador += 60
            $ exposicao = min(100, exposicao + 10)
            "Avanço em silêncio absoluto. Com um golpe preciso na base da nuca, apago o executor de trás e arrasto seu corpo para o duto de folhas secas, confiscando sua bolsa de munição e créditos."
            $ notificar_rpg("⚔️ SENTINELA NEUTRALIZADO", "+1 Coragem | +$60 Créditos | +10% Exposição", "#ffd700")

    jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 18. A AUDITORIA FORENSE DE CLARA VANCE (Ameaça à Enfermaria)
# ------------------------------------------------------------------------------
label ev_c19_laudo_sincope_clara:
    $ ev_c19_laudo_clara_visto = True
    $ local_atual = "enfermaria"
    call restaurar_fundo_local_atual
    play music "audio/the_keepers_ledger.ogg" if_changed fadein 1.5

    "Entro na Enfermaria para fugir da ronda. Clara Vance está debruçada sobre a mesa de fichas com as mãos trêmulas e o rosto pálido como giz."

    show mob enfermeira medo at sprite_direita with dissolve
    $ th_bark_mob("abordagem")

    mob_enfermeira "Victor... Você não deveria estar aqui a esta hora!"

    "Ela tranca a porta de vidro fosco com o trinco duplo:"

    mob_enfermeira "O comitê médico central da Fundação requisitou uma auditoria extraordinária nos prontuários de doação. Eles notaram as minhas baixas de pressão e os laudos rasurados do seu hemograma..."

    mob_enfermeira "Se eles apreenderem o livro-caixa das coletas de sangue amanhã pela manhã, eu perco a minha licença e você será transferido para a cela de isolamento profundo com a cobaia trancada!"

    menu:
        "Invadir a sala de arquivos agora e queimar as fichas originais":
            $ coragem = getattr(store, "coragem", 0) + 1
            $ intelecto += 1
            $ exposicao = max(0, exposicao - 20)
            "Traga o maçarico, Clara. Esta noite haverá um pequeno 'curto-circuito' na gaveta de aço dos arquivos mortos."
            "Clara respira fundo, aliviada, e entrega o frasco de álcool etílico com as mãos trêmulas."
            $ notificar_rpg("🔥 RASTRO APAGADO", "+1 Intelecto | +1 Coragem | -20% Exposição", "#00ffcc")

        "Substituir as lâminas de sangue por amostras sintéticas de coelho":
            $ intelecto += 2
            "Com calma cirúrgica, usamos o centrifugador para diluir soro fisiológico em hemoglobina animal, forjando um laudo perfeitamente banal que despistará os peritos."
            show mob enfermeira sorrindo at sprite_direita with dissolve
            mob_enfermeira "Você pensa rápido demais, senhor Vane... Muito bem. A perícia não encontrará nada além de ferro e água."
            $ notificar_rpg("🧪 FALSIFICAÇÃO CIRÚRGICA", "+2 Intelecto | Auditoria ludibriada", "#38bdf8")

    hide mob enfermeira with dissolve
    jump entrar_local_exploracao_bs
