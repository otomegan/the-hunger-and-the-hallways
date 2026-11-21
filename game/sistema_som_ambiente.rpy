# ==============================================================================
# SISTEMA DE ÁUDIO ATMOSFÉRICO AUTOMÁTICO DE CENÁRIOS
# ==============================================================================
# Toca automaticamente o áudio de fundo (looping) correspondente a cada cenário
# no canal 'ambient', em paralelo com a trilha musical (BGM), elevando a imersão.
# Cenários silenciosos/acústicos puros (Biblioteca, Sala de Música, Gabinete)
# deixam o canal ambient livre para a trilha sonora brilhar sem poluição.

init -5 python:
    # Registra o canal 'ambient' dedicado para sons de fundo dos cenários
    renpy.music.register_channel("ambient", mixer="sfx", loop=True)

    MAPA_AMBIENTES_BACKGROUNDS = {
        # --- Cratera & Apocalipse ---
        "bg animado apocalipse cratera orb vermelha 1080p": "audio/ambiente/amb_bg_animado_apocalipse_cratera_orb_vermelha_1080p.ogg",
        "bg apocalipse cratera orb vermelha 1080p": "audio/ambiente/amb_bg_animado_apocalipse_cratera_orb_vermelha_1080p.ogg",
        "bg animado apocalipse cratera orb vermelha": "audio/ambiente/amb_bg_animado_apocalipse_cratera_orb_vermelha.ogg",
        "bg apocalipse cratera orb vermelha": "audio/ambiente/amb_bg_animado_apocalipse_cratera_orb_vermelha.ogg",
        "bg animado cratera ruinas academia lua cheia 1": "audio/ambiente/amb_bg_animado_cratera_ruinas_academia_lua_cheia_1.ogg",
        "bg cratera ruinas academia lua cheia 1": "audio/ambiente/amb_bg_animado_cratera_ruinas_academia_lua_cheia_1.ogg",
        "bg animado cratera ruinas academia lua cheia 2": "audio/ambiente/amb_bg_animado_cratera_ruinas_academia_lua_cheia_2.ogg",
        "bg cratera ruinas academia lua cheia 2": "audio/ambiente/amb_bg_animado_cratera_ruinas_academia_lua_cheia_2.ogg",
        "bg cidade cyberpunk eclipse sol vermelho": "audio/ambiente/amb_bg_cidade_cyberpunk_eclipse_sol_vermelho.ogg",

        # --- Banheiro Abandonado ---
        "bg animado banheiro abandonado luz vermelha piscando": "audio/ambiente/amb_bg_animado_banheiro_abandonado_luz_vermelha_piscando.ogg",
        "bg banheiro abandonado luz vermelha piscando": "audio/ambiente/amb_bg_animado_banheiro_abandonado_luz_vermelha_piscando.ogg",

        # --- Bar da Fada Verde & Subsolo Ilícito ---
        "bg animado bar grunge luzes neon": "audio/ambiente/amb_bg_animado_bar_grunge_luzes_neon.ogg",
        "bg bar grunge luzes neon": "audio/ambiente/amb_bg_animado_bar_grunge_luzes_neon.ogg",
        "bg animado bar grunge taverna fogo verde": "audio/ambiente/amb_bg_animado_bar_grunge_taverna_fogo_verde.ogg",
        "bg bar grunge taverna fogo verde": "audio/ambiente/amb_bg_animado_bar_grunge_taverna_fogo_verde.ogg",

        # --- Biblioteca Gótica (Silêncio solene; The_Unfinished_Lesson.ogg brilha sem tochas intrusivas) ---
        "bg animado biblioteca gotica mesas manha": None,
        "bg biblioteca gotica mesas manha": None,
        "bg animado biblioteca gotica mesas noite": None,
        "bg biblioteca gotica mesas noite": None,

        # --- Caldeiras, Oficinas e Fornalhas Subterrâneas (Brasas, Vapor e Fogo Azul) ---
        "bg animado caldeiras esconderijo tocha azul e fogo": "audio/ambiente/amb_bg_animado_caldeiras_esconderijo_tocha_azul_e_fogo.ogg",
        "bg caldeiras esconderijo tocha azul e fogo": "audio/ambiente/amb_bg_animado_caldeiras_esconderijo_tocha_azul_e_fogo.ogg",
        "bg animado caldeiras loja pocoes tocha azul": "audio/ambiente/amb_bg_animado_caldeiras_loja_pocoes_tocha_azul.ogg",
        "bg caldeiras loja pocoes tocha azul": "audio/ambiente/amb_bg_animado_caldeiras_loja_pocoes_tocha_azul.ogg",
        "bg animado caldeiras oficina fornalha brasa": "audio/ambiente/amb_bg_animado_caldeiras_oficina_fornalha_brasa.ogg",
        "bg caldeiras oficina fornalha brasa": "audio/ambiente/amb_bg_animado_caldeiras_oficina_fornalha_brasa.ogg",
        "bg animado caldeiras subsolo fornalha fumaca": "audio/ambiente/amb_bg_animado_caldeiras_subsolo_fornalha_fumaca.ogg",
        "bg caldeiras subsolo fornalha fumaca": "audio/ambiente/amb_bg_animado_caldeiras_subsolo_fornalha_fumaca.ogg",
        "bg animado corredor industrial subsolo vapor": "audio/ambiente/amb_bg_animado_corredor_industrial_subsolo_vapor.ogg",
        "bg corredor industrial subsolo vapor": "audio/ambiente/amb_bg_animado_corredor_industrial_subsolo_vapor.ogg",
        "bg animado corredor industrial caldeira subsolo vapor": "audio/ambiente/amb_bg_animado_corredor_industrial_subsolo_vapor.ogg",
        "bg corredor industrial caldeira subsolo vapor": "audio/ambiente/amb_bg_animado_corredor_industrial_subsolo_vapor.ogg",

        # --- Catacumbas, Criptas e Masmorras (Tochas rúnicas e ressonância ancestral) ---
        "bg animado catacumbas cofre velas verdes": "audio/ambiente/amb_bg_animado_catacumbas_cofre_velas_verdes.ogg",
        "bg catacumbas cofre velas verdes": "audio/ambiente/amb_bg_animado_catacumbas_cofre_velas_verdes.ogg",
        "bg animado catacumbas corredor tochas": "audio/ambiente/amb_bg_animado_catacumbas_corredor_tochas.ogg",
        "bg catacumbas corredor tochas": "audio/ambiente/amb_bg_animado_catacumbas_corredor_tochas.ogg",
        "bg animado catacumbas corredor runas tochas": "audio/ambiente/amb_bg_animado_catacumbas_corredor_tochas.ogg",
        "bg catacumbas corredor runas tochas": "audio/ambiente/amb_bg_animado_catacumbas_corredor_tochas.ogg",
        "bg animado escadaria catacumbas tochas runas": "audio/ambiente/amb_bg_animado_escadaria_catacumbas_tochas_runas.ogg",
        "bg escadaria catacumbas tochas runas": "audio/ambiente/amb_bg_animado_escadaria_catacumbas_tochas_runas.ogg",
        "bg animado masmorra corredor runas tochas": "audio/ambiente/amb_bg_animado_masmorra_corredor_runas_tochas.ogg",
        "bg masmorra corredor runas tochas": "audio/ambiente/amb_bg_animado_masmorra_corredor_runas_tochas.ogg",
        "bg animado cripta cela vidro quebrada runas piscando": "audio/ambiente/amb_bg_animado_cripta_cela_vidro_quebrada_runas_piscando.ogg",
        "bg cripta cela vidro quebrada runas piscando": "audio/ambiente/amb_bg_animado_cripta_cela_vidro_quebrada_runas_piscando.ogg",
        "bg animado cripta cela vidro runas fechada": "audio/ambiente/amb_bg_animado_cripta_cela_vidro_runas_fechada.ogg",
        "bg cripta cela vidro runas fechada": "audio/ambiente/amb_bg_animado_cripta_cela_vidro_runas_fechada.ogg",

        # --- Corredores Internos (Ressonância suave de galeria gótica, sem estalos de fogo) ---
        "bg animado corredor academia cortina sol": "audio/ambiente/amb_bg_animado_corredor_academia_entardecer_sol.ogg",
        "bg corredor academia cortina sol": "audio/ambiente/amb_bg_animado_corredor_academia_entardecer_sol.ogg",
        "bg animado corredor academia entardecer sol": "audio/ambiente/amb_bg_animado_corredor_academia_entardecer_sol.ogg",
        "bg corredor academia entardecer sol": "audio/ambiente/amb_bg_animado_corredor_academia_entardecer_sol.ogg",
        "bg animado corredor zona vermelha luzes de sangue": "audio/ambiente/amb_bg_animado_corredor_zona_vermelha_luzes_de_sangue.ogg",
        "bg corredor zona vermelha luzes de sangue": "audio/ambiente/amb_bg_animado_corredor_zona_vermelha_luzes_de_sangue.ogg",

        # --- Dormitórios (Quarto seguro: acústica serena e limpa) ---
        "bg animado dormitorio quarto dia computador": "audio/ambiente/amb_bg_animado_dormitorio_quarto_manha_raio_sol.ogg",
        "bg dormitorio quarto dia computador": "audio/ambiente/amb_bg_animado_dormitorio_quarto_manha_raio_sol.ogg",
        "bg animado dormitorio quarto manha raio sol": "audio/ambiente/amb_bg_animado_dormitorio_quarto_manha_raio_sol.ogg",
        "bg dormitorio quarto manha raio sol": "audio/ambiente/amb_bg_animado_dormitorio_quarto_manha_raio_sol.ogg",
        "bg animado dormitorio quarto tarde sol": "audio/ambiente/amb_bg_animado_dormitorio_quarto_manha_raio_sol.ogg",
        "bg dormitorio quarto tarde sol": "audio/ambiente/amb_bg_animado_dormitorio_quarto_manha_raio_sol.ogg",
        "bg animado dormitorio quarto noite luar": "audio/ambiente/amb_bg_animado_dormitorio_quarto_noite_luar.ogg",
        "bg dormitorio quarto noite luar": "audio/ambiente/amb_bg_animado_dormitorio_quarto_noite_luar.ogg",
        "bg animado dormitorio esterno tarde": "audio/ambiente/amb_bg_animado_dormitorio_esterno_tarde.ogg",
        "bg dormitorio esterno tarde": "audio/ambiente/amb_bg_animado_dormitorio_esterno_tarde.ogg",
        "bg animado dormitorio externo tarde": "audio/ambiente/amb_bg_animado_dormitorio_esterno_tarde.ogg",
        "bg dormitorio externo tarde": "audio/ambiente/amb_bg_animado_dormitorio_esterno_tarde.ogg",

        # --- Entrada & Portões da Academia ---
        "bg animado entrada academia portoes manha": "audio/ambiente/amb_bg_animado_entrada_academia_portoes_entardecer_sol.ogg",
        "bg entrada academia portoes manha": "audio/ambiente/amb_bg_animado_entrada_academia_portoes_entardecer_sol.ogg",
        "bg animado entrada academia portoes entardecer sol": "audio/ambiente/amb_bg_animado_entrada_academia_portoes_entardecer_sol.ogg",
        "bg entrada academia portoes entardecer sol": "audio/ambiente/amb_bg_animado_entrada_academia_portoes_entardecer_sol.ogg",
        "bg animado entrada academia portoes nevoeiro noite": "audio/ambiente/amb_bg_animado_entrada_academia_portoes_nevoeiro_noite.ogg",
        "bg entrada academia portoes nevoeiro noite": "audio/ambiente/amb_bg_animado_entrada_academia_portoes_nevoeiro_noite.ogg",

        # --- Gabinete do Grêmio & Diretoria (The_Cold_Decree.ogg brilha; noite com candelabro suave) ---
        "bg animado gabinete diretor dia cortinas": None,
        "bg gabinete diretor dia cortinas": None,
        "bg animado gabinete diretor entardecer sol": None,
        "bg gabinete diretor entardecer sol": None,
        "bg animado gabinete diretor por do sol": None,
        "bg gabinete diretor por do sol": None,
        "bg animado gabinete diretor noite candelabro": "audio/ambiente/amb_bg_animado_gabinete_diretor_noite_candelabro.ogg",
        "bg gabinete diretor noite candelabro": "audio/ambiente/amb_bg_animado_gabinete_diretor_noite_candelabro.ogg",
        "bg animado gabinete diretor noite lampada": "audio/ambiente/amb_bg_animado_gabinete_diretor_noite_lampada.ogg",
        "bg gabinete diretor noite lampada": "audio/ambiente/amb_bg_animado_gabinete_diretor_noite_lampada.ogg",

        # --- Enfermaria da Academia (Ambiente clínico, esterilizado e monitor hospitalar) ---
        "bg animado enfermaria manha": "audio/ambiente/amb_bg_animado_enfermaria_manha.ogg",
        "bg animada enfermaria manha": "audio/ambiente/amb_bg_animado_enfermaria_manha.ogg",
        "bg enfermaria manha": "audio/ambiente/amb_bg_animado_enfermaria_manha.ogg",
        "bg animado enfermaria tarde": "audio/ambiente/amb_bg_animado_enfermaria_tarde.ogg",
        "bg animada enfermaria tarde": "audio/ambiente/amb_bg_animado_enfermaria_tarde.ogg",
        "bg enfermaria tarde": "audio/ambiente/amb_bg_animado_enfermaria_tarde.ogg",
        "bg animado enfermaria noite": "audio/ambiente/amb_bg_animado_enfermaria_noite.ogg",
        "bg animada enfermaria noite": "audio/ambiente/amb_bg_animado_enfermaria_noite.ogg",
        "bg enfermaria noite": "audio/ambiente/amb_bg_animado_enfermaria_noite.ogg",
        "bg animado enfermaria chuva": "audio/ambiente/amb_bg_animado_enfermaria_chuva.ogg",
        "bg animada enfermaria chuva": "audio/ambiente/amb_bg_animado_enfermaria_chuva.ogg",
        "bg enfermaria chuva": "audio/ambiente/amb_bg_animado_enfermaria_chuva.ogg",

        # --- Lareira da Sala de Estudo (Fogo real) ---
        "bg animado lareira sala estudo poltrona": "audio/ambiente/amb_bg_animado_lareira_sala_estudo_poltrona.ogg",
        "bg lareira sala estudo poltrona": "audio/ambiente/amb_bg_animado_lareira_sala_estudo_poltrona.ogg",

        # --- Pátio das Árvores Centenárias ---
        "bg animado patio arvore dia claro": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_extendido.ogg",
        "bg patio arvore dia claro": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_extendido.ogg",
        "bg animado patio arvore entardecer dourado": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_dourado.ogg",
        "bg patio arvore entardecer dourado": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_dourado.ogg",
        "bg animado patio arvore entardecer extendido": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_extendido.ogg",
        "bg patio arvore entardecer extendido": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_extendido.ogg",
        "bg animado patio arvore entardecer folhas": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_folhas.ogg",
        "bg patio arvore entardecer folhas": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_folhas.ogg",
        "bg animado patio arvore noite postes luz": "audio/ambiente/amb_bg_animado_patio_arvore_noite_postes_luz.ogg",
        "bg patio arvore noite postes luz": "audio/ambiente/amb_bg_animado_patio_arvore_noite_postes_luz.ogg",
        "bg animado patio arvore postes noite": "audio/ambiente/amb_bg_animado_patio_arvore_postes_noite.ogg",
        "bg patio arvore postes noite": "audio/ambiente/amb_bg_animado_patio_arvore_postes_noite.ogg",

        # --- Pátio & Claustro da Fonte Gótica ---
        "bg animado patio claustro fonte dia": "audio/ambiente/amb_bg_animado_patio_claustro_fonte_dia.ogg",
        "bg patio claustro fonte dia": "audio/ambiente/amb_bg_animado_patio_claustro_fonte_dia.ogg",
        "bg animado patio claustro fonte entardecer": "audio/ambiente/amb_bg_animado_patio_claustro_fonte_entardecer.ogg",
        "bg patio claustro fonte entardecer": "audio/ambiente/amb_bg_animado_patio_claustro_fonte_entardecer.ogg",
        "bg animado patio claustro fonte noite": "audio/ambiente/amb_bg_claustro_patio_fonte_noite.ogg",
        "bg patio claustro fonte noite": "audio/ambiente/amb_bg_claustro_patio_fonte_noite.ogg",
        "bg claustro patio fonte noite": "audio/ambiente/amb_bg_claustro_patio_fonte_noite.ogg",

        # --- Rua Externa & Portão ---
        "bg animado rua portao academia manha": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_extendido.ogg",
        "bg rua portao academia manha": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_extendido.ogg",
        "bg animado rua portao academia tarde": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_dourado.ogg",
        "bg rua portao academia tarde": "audio/ambiente/amb_bg_animado_patio_arvore_entardecer_dourado.ogg",
        "bg animado rua portao academia noite": "audio/ambiente/amb_bg_animado_rua_portao_academia_noite.ogg",
        "bg rua portao academia noite": "audio/ambiente/amb_bg_animado_rua_portao_academia_noite.ogg",

        # --- Cemitério Sombrio ---
        "bg cemiterio nevoeiro postes noite": "audio/ambiente/amb_bg_animado_entrada_academia_portoes_nevoeiro_noite.ogg",

        # --- Sala de Ocultismo & Alquimia ---
        "bg animado sala aula ocultismo alquimia verde": "audio/ambiente/amb_bg_animado_sala_aula_ocultismo_alquimia_verde.ogg",
        "bg sala aula ocultismo alquimia verde": "audio/ambiente/amb_bg_animado_sala_aula_ocultismo_alquimia_verde.ogg",

        # --- Sala de Música (The_Crimson_Chamber.ogg brilha; sem piano concorrente no canal ambient) ---
        "bg animado sala musica piano noite": None,
        "bg sala musica piano noite": None,
        "bg animado sala musica piano vitral sol": None,
        "bg sala musica piano vitral sol": None,

        # --- Cenários Específicos de Chuva (Gotas batendo em vitrais e telhados sem conflito) ---
        "bg animado patio claustro fonte chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg patio claustro fonte chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado patio claustro arcos chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg arcos claustro patio fonte chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado patio arvore chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg patio academia arvores chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado biblioteca gotica mesas chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg biblioteca gotica mesas chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado dormitorio quarto chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg dormitorio quarto chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado dormitorio externo chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg dormitorio externo chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado entrada academia portoes chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg entrada academia portoes chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado sala musica piano vitral chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg sala musica piano vitral chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg sala musica piano chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado gabinete diretor chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg gabinete diretor chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado cemiterio chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg cemiterio chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado corredor academia chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg corredor academia chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado rua avenida campus chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg rua avenida campus chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg animado rua portao academia chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
        "bg rua portao academia chuva": "audio/sfx/sfx_chuva_ambiente.ogg",
    }

    def resolver_audio_ambiente(nome_bg):
        """
        Retorna o caminho do arquivo de áudio ambiente (.ogg) correspondente
        ao nome do background atualmente exibido, com suporte a fallbacks e clima.
        Retorna None explicitamente se o cenário foi projetado para silêncio ambiente.
        """
        if not nome_bg:
            return None

        # 1. Busca direta no mapa de cenários (respeita mapeamento explícito para None)
        if nome_bg in MAPA_AMBIENTES_BACKGROUNDS:
            return MAPA_AMBIENTES_BACKGROUNDS[nome_bg]

        # 2. Cenários de chuva (qualquer um com chuva no nome)
        if "chuva" in nome_bg:
            if renpy.loadable("audio/sfx/sfx_chuva_ambiente.ogg"):
                return "audio/sfx/sfx_chuva_ambiente.ogg"

        # 3. Fallbacks temáticos estritos para aliases narrativos não catalogados
        # (NÃO aplicar fallbacks para biblioteca, música ou gabinete, pois são propositalmente silenciosos)
        if "caldeira" in nome_bg or "fornalha" in nome_bg:
            return "audio/ambiente/amb_bg_animado_corredor_industrial_subsolo_vapor.ogg"
        if "catacumba" in nome_bg or "cripta" in nome_bg:
            return "audio/ambiente/amb_bg_animado_catacumbas_corredor_tochas.ogg"
        if "corredor escuro" in nome_bg or "luzes de sangue" in nome_bg:
            return "audio/ambiente/amb_bg_animado_corredor_zona_vermelha_luzes_de_sangue.ogg"
        if "portao" in nome_bg or "entrada" in nome_bg:
            return "audio/ambiente/amb_bg_animado_entrada_academia_portoes_entardecer_sol.ogg"
        if "patio" in nome_bg or "claustro" in nome_bg:
            return "audio/ambiente/amb_bg_animado_patio_claustro_fonte_dia.ogg"
        if "dormitorio" in nome_bg:
            return "audio/ambiente/amb_bg_animado_dormitorio_quarto_noite_luar.ogg"

        return None

    _ultimo_bg_ambiente = None

    def _gerenciador_audio_ambiente_callback():
        """
        Hook executado a cada interação que detecta o cenário ativo (tag 'bg').
        Realiza crossfade automático de 2.0s para o som ambiente do novo cenário,
        restaurando o som se o canal foi pausado/parado pelo mapa ou telas.
        Se o cenário for silencioso (None), interrompe qualquer som ambiente ativo suavemente.
        """
        global _ultimo_bg_ambiente

        if renpy.showing("bg"):
            attrs = renpy.get_attributes("bg") or ()
            nome_bg = " ".join(["bg"] + list(attrs))
            som_amb = resolver_audio_ambiente(nome_bg)
            tocando = renpy.music.get_playing(channel="ambient")

            if som_amb and renpy.loadable(som_amb):
                # Se o som não estiver tocando ou o cenário mudou, inicia o áudio ambiente
                if tocando != som_amb:
                    _ultimo_bg_ambiente = nome_bg
                    renpy.music.play(som_amb, channel="ambient", loop=True, fadein=2.0, relative_volume=0.60)
            else:
                # Se mudou para um cenário sem som ambiente próprio e algo estava tocando no canal
                if nome_bg != _ultimo_bg_ambiente:
                    _ultimo_bg_ambiente = nome_bg
                    if tocando:
                        renpy.music.stop(channel="ambient", fadeout=1.8)
        else:
            # Se não há background 'bg' ativo (ex: mapas, telas com add ou telas pretas)
            if _ultimo_bg_ambiente is not None:
                _ultimo_bg_ambiente = None
                tocando = renpy.music.get_playing(channel="ambient")
                if tocando and not str(tocando).startswith("audio/sfx/sfx_mapa_ambiente_"):
                    renpy.music.stop(channel="ambient", fadeout=1.8)

    config.interact_callbacks.append(_gerenciador_audio_ambiente_callback)
