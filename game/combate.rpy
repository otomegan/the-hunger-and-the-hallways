# ==============================================================================
# COMBATE.RPY - MOTOR UNIVERSAL DE LUTA E DRENAGEM (SEM DUPLICATAS)
# ==============================================================================

# ==========================================
# 1. TELA DE HUD DO INIMIGO + TIMER (QTE)
# ==========================================
screen hud_combate_zona_vermelha():
    zorder 90
    frame:
        xalign 0.5 yalign 0.08
        background "#220000dd"
        padding (20, 10)
        vbox:
            xalign 0.5 spacing 6
            text "⚔️ [nome_inimigo!u] - HP: [hp_inimigo]/[hp_inimigo_max]" color "#ff4444" bold True size 22 xalign 0.5
            bar value hp_inimigo range hp_inimigo_max xysize (400, 18)
            text "👤 Victor - HP: [hp_jogador]/[hp_jogador_max] | Fome: [fome_sangue]%" color "#ffffff" size 16 xalign 0.5

    timer tempo_reacao action Jump("inimigo_ataca_por_tempo") repeat False

# ==========================================
# 2. MOLDE UNIVERSAL DE LUTA
# ==========================================
default combate_pode_fugir = True

default victor_sangramento = 0
default inimigo_em_guarda = False

label iniciar_combate(nome, sprite_base, sprite_atk, hp_max, dano, tempo=4.5, tipo_sangue="gremio", historia_continua=False, pode_fugir=True, sprite_derrota=""):
    $ nome_inimigo = nome
    $ img_inimigo_base = sprite_base
    $ img_inimigo_ataque = sprite_atk
    $ img_inimigo_derrota = sprite_derrota

    # Resolução dinâmica e inteligente da pose de derrota
    if not img_inimigo_derrota and sprite_base:
        python:
            _sb = str(sprite_base).strip()
            _cands = [
                f"{_sb} derrota",
                f"{_sb} derrota alt",
                f"{_sb} derrotado",
            ]
            _suffixes = [
                ' ereto', ' neutro', ' olhos', ' flutuando', ' chave', ' terno', ' cranio', ' pesadelo',
                ' arma', ' neutro espada', ' espada tranca', ' avanco', ' em pe', ' manto sagrado',
                ' marinheiro', ' runa testa alt', ' runa testa', ' combate pose', ' lamina',
                ' guarda', ' inclinada', ' suspensa', ' asas abertas', ' erguendo frasco',
                ' frasco verde arma', ' espinhos runa', ' sorriso agressivo', ' deboche'
            ]
            for _suf in _suffixes:
                if _sb.endswith(_suf) or _suf in _sb:
                    _clean = _sb[:-len(_suf)] if _sb.endswith(_suf) else _sb.replace(_suf, '')
                    _cands.extend([
                        f"{_clean} derrota",
                        f"{_clean} derrotado",
                        f"{_clean} avanco derrota",
                        f"{_clean} flutuando derrota",
                        f"{_clean} asas abertas derrota",
                        f"{_clean} correntes terno derrota",
                        f"{_clean} curvado derrota",
                        f"{_clean} frasco verde derrota",
                    ])
            if _sb.endswith(' espada'):
                _cands.append(f"{_sb[:-len(' espada')]} derrota")
            if "marionete" in _sb:
                _cands.append("inimigo marionete fios sangue flutuando derrota")
            if "esqueleto colegial" in _sb:
                _cands.append("inimigo esqueleto colegial curvado derrota")
            if "esqueleto nobre" in _sb:
                _cands.append("inimigo esqueleto nobre espinhos runa derrota")
            if "alquimista" in _sb:
                _cands.append("inimigo fundao alquimista frasco verde derrota")
            if "gargula elite" in _sb:
                _cands.append("inimigo gargula elite celestial asas abertas derrota")
            if "gargula pedra" in _sb:
                _cands.append("inimigo gargula pedra dragao derrota")
            if "executora conselho ruiva" in _sb:
                _cands.append("inimigo executora conselho ruiva derrota")
            if "ghoul zumbi" in _sb:
                _cands.extend(["inimigo colegial ghoul zumbi derrota", "inimigo colegial ghoul zumbi avanco derrota"])
            if "vampiro ghoul" in _sb:
                _cands.extend(["inimigo vampiro ghoul agachado faca derrota", "inimigo vampiro ghoul agachado faca derrota alt"])
            if "loira" in _sb:
                _cands.extend(["loira do banheiro derrota", "loira banheiro derrota"])
            if "elara" in _sb:
                _cands.extend(["elara derrotada", "elara derrotada encarando"])

            for _ct in _cands:
                if renpy.has_image(_ct, exact=True):
                    img_inimigo_derrota = _ct
                    break

    $ hp_inimigo = hp_max
    $ hp_inimigo_max = hp_max
    $ dano_inimigo = dano
    if store.clima_diario_id == "nevoa_carmesim":
        $ dano_inimigo = int(dano * 1.25)
        $ notificar_rpg("🌫️ NÉVOA CARMESIM", "A anomalia ruge fortalecida pela névoa (+25% Dano Inimigo)!", "#ff4444")
    if store.status_escola == "histeria":
        $ dano_inimigo = int(dano_inimigo * 1.20)
        $ notificar_rpg("🔥 HISTERIA DA ACADEMIA", "O pânico generalizado torna os golpes inimigos brutais (+20% Dano)!", "#ff2244")
    $ tempo_reacao = max(3.0, float(tempo))
    if store.efeito_estimulante_ativo:
        $ tempo_reacao += 2.5
        $ notificar_rpg("💉 REFLEXOS ACELERADOS", "Dose Estimulante ativa: +2.5s de tempo de reação!", "#00ffcc")
    $ tipo_sangue_inimigo = tipo_sangue
    $ combate_historia_continua = historia_continua
    $ combate_pode_fugir = pode_fugir
    $ victor_sangramento = 0
    $ inimigo_em_guarda = False
    $ ampola_prata_ativa = False
    $ defesa_tampao_combate = 0
    $ extorquiu_combate_atual = False

    # Trilha Sonora Dinâmica de Batalha por Inimigo / Chefe
    python:
        _musica_batalha = "steel_loop"
        _nome_l = str(nome).lower() if nome else ""
        if "loira" in _nome_l or "espelho" in _nome_l:
            _musica_batalha = "batalha_loira_banheiro"
        elif "hachishaku" in _nome_l:
            _musica_batalha = "batalha_hachishakusama"
        elif "cain" in _nome_l:
            _musica_batalha = "the_hunger_of_ancient_gods"
        elif "phillip" in _nome_l:
            _musica_batalha = "the_cold_decree"
        elif "elara" in _nome_l:
            _musica_batalha = "elara_tema"
        elif "fada" in _nome_l:
            _musica_batalha = "at_the_green_fairy"
        th_musica(_musica_batalha, 1.0)

    # Oculta sprites de cena prévios para evitar duplicatas visuais na arena de batalha
    $ _tag_candidata = sprite_base.split()[0] if sprite_base else ""
    if _tag_candidata and renpy.showing(_tag_candidata):
        $ renpy.hide(_tag_candidata)
    python:
        for _t in ("nora", "inimigo", "fada", "elara", "cain", "phillip", "victor", "emilia", "valeria", "loira"):
            if renpy.showing(_t):
                renpy.hide(_t)

    if img_inimigo_base != "":
        show expression img_inimigo_base as inimigo at sprite_padrao with vpunch
    $ th_bark_inimigo(nome_inimigo, "saudacao")
    
    "⚠️ Passos rápidos nas sombras...{w=0.3} [nome_inimigo] bloqueia o seu caminho na Zona Vermelha!"
    jump loop_turno_combate

label loop_turno_combate:
    $ renpy.block_rollback()

    $ hp_inimigo = max(0, hp_inimigo)
    $ hp_jogador = max(0, hp_jogador)

    # 1. Verifica vitória e dispara o Menu de Rendição / Golpe Crítico (Estilo Persona)
    if hp_inimigo <= 0:
        hide screen hud_combate_zona_vermelha
        $ esquiva_estimulante_ativa = False
        $ efeito_estimulante_ativo = False
        $ victor_sangramento = 0
        $ inimigo_em_guarda = False
        $ ampola_prata_ativa = False
        $ defesa_tampao_combate = 0
        if combate_historia_continua:
            hide inimigo with dissolve
            return "vitoria_historia"
        jump executar_golpe_critico_persona

    # 2. Verifica derrota
    if hp_jogador <= 0:
        hide screen hud_combate_zona_vermelha
        $ esquiva_estimulante_ativa = False
        $ efeito_estimulante_ativo = False
        $ victor_sangramento = 0
        $ inimigo_em_guarda = False
        $ ampola_prata_ativa = False
        $ defesa_tampao_combate = 0
        $ extorquiu_combate_atual = False
        if combate_historia_continua:
            hide inimigo with dissolve
            return "derrota_historia"
        jump interceptar_derrota_combate

    if img_inimigo_base != "":
        show expression img_inimigo_base as inimigo at sprite_padrao
    show screen hud_combate_zona_vermelha

    menu:
        "🗡️ Ataque Rápido (Corte Seco / Sem Custo)":
            hide screen hud_combate_zona_vermelha
            $ th_sfx("corte_rapido")
            with hpunch
            $ _base_atk = getattr(store, "ataque_jogador", 20)
            $ _bonus_cor = getattr(store, "coragem", 0) * 2
            $ _bonus_int = getattr(store, "intelecto", 0) if getattr(store, "analisou_inimigo", False) else 0
            $ _buff_dano = getattr(store, "buff_sanguineo_dano", 0)
            $ _bonus_liturgico = 15 if (getattr(store, "sangue_liturgico_ativo", False) and getattr(store, "tipo_sangue_inimigo", "") in ["corrompido", "inorganico", "gargula"]) else 0
            $ _bonus_prata = 18 if getattr(store, "ampola_prata_ativa", False) else 0
            $ _bonus_elixir = getattr(store, "buff_ataque_elixir", 0)
            $ dano_rapido = max(18, _base_atk + _bonus_cor + _bonus_int + _buff_dano + _bonus_liturgico + _bonus_prata + _bonus_elixir)

            if inimigo_em_guarda:
                $ inimigo_em_guarda = False
                if getattr(store, "ampola_prata_ativa", False):
                    $ hp_inimigo -= dano_rapido
                    $ th_bark_inimigo(nome_inimigo, "dor")
                    "A prata líquida corrói a guarda férrea de [nome_inimigo], estilhaçando o bloqueio com um golpe pleno! (-[dano_rapido] HP)"
                else:
                    $ dano_rapido = max(8, int(dano_rapido * 0.55))
                    $ hp_inimigo -= dano_rapido
                    $ hp_jogador = max(0, hp_jogador - 12)
                    with hpunch
                    $ th_bark_inimigo(nome_inimigo, "risada")
                    "O adversário antecipou sua lâmina com uma guarda férrea (-45%% Dano) e desferiu um contra-ataque no ricochete! (-12 HP para Victor)"
                    if hp_jogador <= 0:
                        $ esquiva_estimulante_ativa = False
                        $ efeito_estimulante_ativo = False
                        $ victor_sangramento = 0
                        $ inimigo_em_guarda = False
                        $ ampola_prata_ativa = False
                        $ defesa_tampao_combate = 0
                        $ extorquiu_combate_atual = False
                        if combate_historia_continua:
                            hide inimigo with dissolve
                            return "derrota_historia"
                        jump interceptar_derrota_combate
            else:
                if tipo_sangue_inimigo == "inorganico" and not getattr(store, "ampola_prata_ativa", False):
                    $ dano_rapido = max(8, int(dano_rapido * 0.70))
                    "(A couraça inorgânica reduz cortes convencionais em 30%%!)"
                elif tipo_sangue_inimigo == "inorganico" and getattr(store, "ampola_prata_ativa", False):
                    "(A prata líquida dissolve a couraça mineral sem perder impacto!)"
                $ hp_inimigo -= dano_rapido
                if _bonus_liturgico > 0:
                    "O sangue litúrgico em suas veias incendeia a lâmina contra a abominação! (+15 Dano Sagrado)"
                $ th_bark_inimigo(nome_inimigo, "dor")
                "Você avança com um corte afiado em [nome_inimigo]! (-[dano_rapido] HP)"
            jump turno_do_inimigo

        "🩸 Garras de Sangue (Dilacerar Predatório / -20 Fome)" if fome_sangue >= 20:
            hide screen hud_combate_zona_vermelha
            $ th_bark("victor", "garras")
            $ fome_sangue -= 20
            $ th_sfx("golpe_esforco")
            if renpy.loadable("audio/sfx/blade_slash_heavy.ogg"):
                play sound "audio/sfx/blade_slash_heavy.ogg"
            elif renpy.loadable("audio/blade_slash_heavy.ogg"):
                play sound "audio/blade_slash_heavy.ogg"
            with vpunch
            $ _dano_base_abissal = calcular_dano_garras_abissais()
            $ _buff_dano = getattr(store, "buff_sanguineo_dano", 0)
            $ _bonus_ocultista_garras = 12 if (getattr(store, "buff_sanguineo_turnos", 0) > 0 and getattr(store, "buff_sanguineo_tipo", "") in ("ocultista", "ocultismo") and getattr(store, "tipo_sangue_inimigo", "") == "corrompido") else 0
            $ _bonus_liturgico = 15 if (getattr(store, "sangue_liturgico_ativo", False) and getattr(store, "tipo_sangue_inimigo", "") in ["corrompido", "inorganico", "gargula"]) else 0
            $ _bonus_prata = 18 if getattr(store, "ampola_prata_ativa", False) else 0
            $ dano_garras = _dano_base_abissal + _buff_dano + _bonus_ocultista_garras + _bonus_liturgico + _bonus_prata
            if "garras_sedentas" in store.perks_desbloqueados and store.fome_sangue < 50:
                $ dano_garras += 20
                $ notificar_rpg("🩸 GARRAS SEDENTAS", "Dano amplificado pela fome extrema! (+20 Dano)", "#ff0044")

            if inimigo_em_guarda:
                $ inimigo_em_guarda = False
                if getattr(store, "ampola_prata_ativa", False):
                    $ hp_inimigo -= dano_garras
                    "Suas garras banhadas em prata partem a guarda de [nome_inimigo] sem perda de força!"
                else:
                    $ dano_garras = max(15, int(dano_garras * 0.60))
                    $ hp_inimigo -= dano_garras
                    "A guarda do oponente absorveu parte do impacto bestial (-40%% Dano)!"
            else:
                if tipo_sangue_inimigo == "inorganico" and not getattr(store, "ampola_prata_ativa", False):
                    $ dano_garras = max(12, int(dano_garras * 0.75))
                    "(A densidade mineral do alvo resiste às garras!)"
                $ hp_inimigo -= dano_garras

            "Suas veias fervem em chamas carmesim!"
            $ th_bark_inimigo(nome_inimigo, "dor")
            "Você rasga [nome_inimigo] com ferocidade inumana! (-[dano_garras] HP)"
            jump turno_do_inimigo

        "⚡ Usar Dispositivo de Choque ([dispositivo_choque]x) (Descarga / Atordoa)" if dispositivo_choque > 0:
            hide screen hud_combate_zona_vermelha
            $ dispositivo_choque -= 1
            $ _dano_choque = 50 if tipo_sangue_inimigo == "inorganico" else 30
            $ hp_inimigo -= _dano_choque
            $ inimigo_em_guarda = False
            with flash
            if tipo_sangue_inimigo == "inorganico":
                "A descarga elétrica sobrecarrega as runas minerais de [nome_inimigo]! (+50 Dano Eletrostático!)"
            else:
                "O arco voltaico explode no peito de [nome_inimigo]! (-30 HP)"
            "Ele é arremessado contra a parede e perde o turno de ação!"
            jump loop_turno_combate

        "🩹 Aplicar Curativo ([kit_curativo]x) (+30 HP)" if kit_curativo > 0 and hp_jogador < hp_jogador_max:
            hide screen hud_combate_zona_vermelha
            $ kit_curativo -= 1
            $ hp_jogador = min(hp_jogador_max, hp_jogador + 30)
            "Você estanca os cortes mais profundos às pressas! (+30 HP)"
            jump turno_do_inimigo

        "🩹 Aplicar Gaze Consagrada ([gaze_consagrada]x) (+40 HP / Estanca Miasmas e Sangramento)" if gaze_consagrada > 0 and (hp_jogador < hp_jogador_max or sequelas_ativas or victor_sangramento > 0):
            hide screen hud_combate_zona_vermelha
            $ gaze_consagrada -= 1
            $ hp_jogador = min(hp_jogador_max, hp_jogador + 40)
            $ victor_sangramento = 0
            if sequelas_ativas:
                $ curar_sequela(sequelas_ativas[0]["id"])
            $ notificar_rpg("🩹 GAZE CONSAGRADA", "+40 HP restaurados, sangramento estancado e sequela tratada!", "#44ff88")
            "Você aplica a gaze embebida em pó de prata e giz! O sangramento cessa e a carne se fecha. (+40 HP)"
            jump turno_do_inimigo

        "💉 Injetar Dose Estimulante ([dose_estimulante]x) (+2.5s QTE / 50%% Esquiva)" if dose_estimulante > 0 and not esquiva_estimulante_ativa:
            hide screen hud_combate_zona_vermelha
            $ dose_estimulante -= 1
            $ tempo_reacao += 2.5
            $ esquiva_estimulante_ativa = True
            $ notificar_rpg("💉 ESTIMULANTE INJETADO", "+2.5s no timer e 50%% de esquiva ativados!", "#00ffff")
            "A agulha pneumática estala contra seu braço! O mundo desacelera e seus reflexos atingem o ápice."
            jump loop_turno_combate

        "🗡️ Revestir Lâmina com Prata Líquida ([ampola_prata]x) (+18 Dano / Rompe Guarda)" if ampola_prata > 0 and not ampola_prata_ativa:
            hide screen hud_combate_zona_vermelha
            $ ampola_prata -= 1
            $ ampola_prata_ativa = True
            $ notificar_rpg("🗡️ PRATA LÍQUIDA ATIVA", "+18 Dano na luta, ignora armadura mineral e rompe guarda!", "#d8e6ff")
            "Você quebra o lacre da ampola e banha sua lâmina com prata fumegante. O metal sibila sedento contra aberrações e executores."
            jump loop_turno_combate

        "💊 Usar Coagulantes Sintéticos ([tampao_hemostatico]x) (+20 HP / +6 Defesa na luta)" if tampao_hemostatico > 0 and (hp_jogador < hp_jogador_max or victor_sangramento > 0 or defesa_tampao_combate <= 0):
            hide screen hud_combate_zona_vermelha
            $ tampao_hemostatico -= 1
            $ hp_jogador = min(hp_jogador_max, hp_jogador + 20)
            $ victor_sangramento = 0
            $ defesa_tampao_combate = 6
            $ notificar_rpg("💊 COAGULANTES ATIVOS", "+20 HP | Sangramento estancado | +6 Defesa!", "#44ffaa")
            "Você aplica o composto sintético sobre os cortes; a espuma sela as veias e endurece como blindagem tática (+20 HP / +6 Defesa)."
            jump turno_do_inimigo

        "🩸 Beber Bolsa de Sangue ([bolsa_sangue_filtrado]x) (+35%% Saciedade)" if bolsa_sangue_filtrado > 0 and fome_sangue < 100:
            hide screen hud_combate_zona_vermelha
            $ bolsa_sangue_filtrado -= 1
            $ fome_sangue = min(100, fome_sangue + 35)
            with flash_red
            "Você engole a dose fria de sangue filtrado...{w=0.3} A sede recua temporariamente. (+35%% Saciedade)"
            jump turno_do_inimigo

        "🗡️ Cravar Estaca de Prata ([estaca_prata]x) (60 Dano Verdadeiro / -8 HP ao empunhar)" if estaca_prata > 0:
            hide screen hud_combate_zona_vermelha
            $ estaca_prata -= 1
            $ hp_jogador = max(1, hp_jogador - 8)
            $ hp_inimigo -= 60
            $ th_sfx("blade_slash_heavy")
            $ th_bark_inimigo(nome_inimigo, "morte" if hp_inimigo <= 0 else "dor")
            with hpunch
            with vpunch
            $ notificar_rpg("🗡️ ESTACA DE PRATA EMPUNHADA", "60 Dano Verdadeiro | -8 HP por queimar a carne vampírica!", "#ffffff")
            "Você crava a estaca de prata consagrada direto contra o núcleo de [nome_inimigo]! O metal queima sua própria pele (-8 HP), mas estilhaça a essência da criatura (-60 Dano)!"
            if hp_inimigo <= 0:
                jump pos_combate_drenagem
            jump turno_do_inimigo

        "⚡ Injetar Adrenalina Militar ([adrenalina_militar]x) (+25 HP / +4.0s no QTE)" if adrenalina_militar > 0:
            hide screen hud_combate_zona_vermelha
            $ adrenalina_militar -= 1
            $ hp_jogador = min(hp_jogador_max, hp_jogador + 25)
            $ tempo_reacao += 4.0
            $ th_sfx("heartbeat")
            $ notificar_rpg("⚡ ADRENALINA INJETADA", "+25 HP restaurados e +4.0s no timer de reação!", "#38bdf8")
            "Você dispara o êmbolo da ampola militar em sua coxa! Seu coração troa em velocidade máxima e o tempo desacelera."
            jump loop_turno_combate

        "💨 Detonar Granada de Fumaça ([granada_fumaca]x) (Fuga 100%% Segura / 0 Dano)" if granada_fumaca > 0 and combate_pode_fugir and not combate_historia_continua:
            hide screen hud_combate_zona_vermelha
            $ granada_fumaca -= 1
            $ esquiva_estimulante_ativa = False
            $ efeito_estimulante_ativo = False
            $ victor_sangramento = 0
            $ inimigo_em_guarda = False
            $ ampola_prata_ativa = False
            $ defesa_tampao_combate = 0
            $ extorquiu_combate_atual = False
            $ area_alerta_emboscada = False
            $ rastro_olfativo_atual = None
            $ th_sfx("vento_frio")
            hide inimigo with dissolve
            $ notificar_rpg("💨 FUGA TÁTICA PERFEITA", "Cortina de fumaça detonada! Fuga 100% segura sem perda de vida.", "#aaaaaa")
            "Você puxa a cavilha e lança a granada de fósforo no chão! Uma densa fumaça cinzenta cega o adversário enquanto você recua em silêncio absoluto."
            return "fuga"

        "🏃 Fugir para o Mapa (-12 HP na escapada)" if combate_pode_fugir and not combate_historia_continua:
            hide screen hud_combate_zona_vermelha
            $ esquiva_estimulante_ativa = False
            $ efeito_estimulante_ativo = False
            $ victor_sangramento = 0
            $ inimigo_em_guarda = False
            $ ampola_prata_ativa = False
            $ defesa_tampao_combate = 0
            $ extorquiu_combate_atual = False
            $ hp_jogador -= 12
            hide inimigo with dissolve
            if hp_jogador <= 0:
                "Suas forças se esvaem enquanto você tenta rastejar pelas sombras..."
                jump interceptar_derrota_combate
            if hp_jogador <= 35 and renpy.random.randint(1, 100) <= 50:
                $ aplicar_sequela("trauma_fuga", "Paranoia de Emboscada", "Victor teme ser seguido a cada passo nas sombras.", "-1 Passo por turno até descansar")
            "Você recua pelas sombras sofrendo um corte de raspão! (-12 HP)"
            return "fuga"

label inimigo_ataca_por_tempo:
    hide screen hud_combate_zona_vermelha
    "Você hesitou na mira!{w=0.3} A hesitação custa caro na Zona Vermelha!"
    jump turno_do_inimigo

label turno_do_inimigo:
    # Processa Sangramento contínuo de Victor se ativo
    if getattr(store, "victor_sangramento", 0) > 0:
        $ store.victor_sangramento -= 1
        $ hp_jogador = max(0, hp_jogador - 5)
        $ notificar_rpg("🩸 SANGRAMENTO ATIVO", "Ferida aberta vertendo sangue (-5 HP)!", "#ff2244")
        "O sangue escorre quente por suas vestes... (-5 HP de Sangramento | [victor_sangramento] turnos restantes)"
        if hp_jogador <= 0:
            if combate_historia_continua:
                hide inimigo with dissolve
                return "derrota_historia"
            jump interceptar_derrota_combate

    if hp_inimigo > 0:
        if store.esquiva_estimulante_ativa:
            $ _esquivou = renpy.random.random() < 0.5
            if _esquivou:
                $ esquiva_estimulante_ativa = False
                $ efeito_estimulante_ativo = False
                with dissolve
                $ notificar_rpg("⚡ ESQUIVA PERFEITA", "Reflexos do Estimulante esquivaram do golpe!", "#00ffff")
                "Graças ao estimulante rúnico, você prevê a trajetória do ataque e se esquiva no último milissegundo!"
                jump loop_turno_combate
            else:
                $ esquiva_estimulante_ativa = False
                $ efeito_estimulante_ativo = False

        if img_inimigo_ataque != "":
            show expression img_inimigo_ataque as inimigo at bote_ataque
        $ th_bark_inimigo(nome_inimigo, "ataque")

        $ _def_total = getattr(store, "defesa_jogador", 5) + getattr(store, "buff_sanguineo_defesa", 0) + getattr(store, "defesa_tampao_combate", 0)
        $ _dano_final = max(6, dano_inimigo - _def_total)
        $ _sorteio_habilidade = renpy.random.randint(1, 100)

        # -------------------------------------------------------------
        # ARQUÉTIPOS TÁTICOS POR TIPO DE SANGUE / FACÇÃO
        # -------------------------------------------------------------
        if tipo_sangue_inimigo == "gremio":
            if _sorteio_habilidade <= 35 and not inimigo_em_guarda:
                $ inimigo_em_guarda = True
                with hpunch
                $ _dano_sonda = max(5, int(dano_inimigo * 0.5) - _def_total)
                $ hp_jogador = max(0, hp_jogador - _dano_sonda)
                "[nome_inimigo] assume uma {color=#00e5ff}Postura de Guarda e Riposte{/color} com a lâmina erguida! (-[_dano_sonda] HP)"
                "⚠️ (O próximo ataque de Victor sofrerá redução e acionará um contra-ataque de prata imediato!)"
            elif _sorteio_habilidade >= 70:
                with vpunch
                $ _dano_perfurante = max(8, dano_inimigo - int(_def_total * 0.5))
                $ hp_jogador = max(0, hp_jogador - _dano_perfurante)
                $ victor_sangramento = 2
                "[nome_inimigo] desfere uma {color=#ff2244}Estocada Perfurante de Prata{/color} que atravessa sua guarda! (-[_dano_perfurante] HP)"
                "🩸 (Você sofreu Sangramento: -5 HP por 2 turnos!)"
            else:
                with hpunch
                $ hp_jogador = max(0, hp_jogador - _dano_final)
                "[nome_inimigo] avança com um golpe de esgrima refinado! (-[_dano_final] HP)"

        elif tipo_sangue_inimigo == "corrompido":
            if _sorteio_habilidade <= 35:
                with vpunch
                $ _d1 = max(4, int(dano_inimigo * 0.55) - _def_total)
                $ hp_jogador = max(0, hp_jogador - _d1)
                with hpunch
                $ _d2 = max(4, int(dano_inimigo * 0.55) - _def_total)
                $ hp_jogador = max(0, hp_jogador - _d2)
                $ _dtot = _d1 + _d2
                "[nome_inimigo] entra em {color=#ff0044}Frenesi Voraz{/color} e desfere duas garras brutais em sequência rápida! (-[_dtot] HP total)"
            elif _sorteio_habilidade >= 75:
                with flash_red
                $ _dano_abismo = max(5, int(dano_inimigo * 0.5))
                $ hp_jogador = max(0, hp_jogador - _dano_abismo)
                $ tempo_reacao = max(2.6, tempo_reacao - 0.7)
                "[nome_inimigo] solta um {color=#aa00ff}Uivo Enlouquecedor do Abismo{/color}! As paredes vibram e o pânico entorpece sua visão!"
                "🌀 (-[_dano_abismo] HP | Seus reflexos vacilam: -0.7s no timer de reação do próximo turno!)"
            else:
                with hpunch
                $ hp_jogador = max(0, hp_jogador - _dano_final)
                "[nome_inimigo] ataca com fúria animalesca! (-[_dano_final] HP)"

        elif tipo_sangue_inimigo == "inorganico":
            if _sorteio_habilidade <= 40:
                with vpunch
                $ _dano_pesado = max(10, int(dano_inimigo * 1.30) - _def_total)
                $ hp_jogador = max(0, hp_jogador - _dano_pesado)
                "[nome_inimigo] canaliza runas ancestrais e desfere um {color=#ff8800}Impacto Esmagador de Pedra{/color}! O assoalho racha sob o golpe! (-[_dano_pesado] HP)"
                if len(getattr(store, "sequelas_ativas", [])) < 3 and renpy.random.randint(1, 100) <= 45:
                    $ aplicar_sequela("trauma_impacto", "Trauma Torácico", "Costelas trincadas pelo impacto violento de granito.", "-15 HP Máximo até tratar com Gaze Consagrada")
            else:
                with hpunch
                $ hp_jogador = max(0, hp_jogador - _dano_final)
                "[nome_inimigo] desfere um golpe rígido e contundente! (-[_dano_final] HP)"

        elif tipo_sangue_inimigo == "humano":
            if _sorteio_habilidade <= 35:
                with flash
                $ _dano_acido = max(6, int(dano_inimigo * 0.70))
                $ hp_jogador = max(0, hp_jogador - _dano_acido)
                $ fome_sangue = max(0, fome_sangue - 10)
                "[nome_inimigo] arremessa um {color=#44ff44}Frasco de Reagente Cáustico{/color} aos seus pés! A fumaça queima suas veias e dissipa sua energia carmesim!"
                "🧪 (-[_dano_acido] HP | -10%% de Fome de Sangue eliminados pelo ácido rúnico!)"
            elif _sorteio_habilidade >= 70:
                with hpunch
                $ _dano_tiro = max(8, dano_inimigo - int(_def_total * 0.3))
                $ hp_jogador = max(0, hp_jogador - _dano_tiro)
                "[nome_inimigo] assume postura firme e dispara à queima-roupa com precisão cirúrgica! (-[_dano_tiro] HP)"
            else:
                with hpunch
                $ hp_jogador = max(0, hp_jogador - _dano_final)
                "[nome_inimigo] desfere um golpe agressivo! (-[_dano_final] HP)"

        else:
            with hpunch
            $ hp_jogador = max(0, hp_jogador - _dano_final)
            "[nome_inimigo] contra-ataca com ferocidade brutal! (-[_dano_final] HP)"

        # Risco de Sequela Crítica se o golpe final foi muito pesado (>= 28 de dano real)
        if _dano_final >= 28 and len(getattr(store, "sequelas_ativas", [])) < 3 and renpy.random.randint(1, 100) <= 30:
            $ aplicar_sequela("trauma_impacto", "Trauma Torácico", "Costelas trincadas pelo impacto violento.", "-15 HP Máximo até tratar com Gaze Consagrada")

    jump loop_turno_combate

# ==========================================
# 3. ESCOLHA PÓS-COMBATE: DRENAR OU POUPAR
# ==========================================
# ==============================================================================
# 2.5. SISTEMA PERSONA: POSTURA QUEBRADA & HOLD-UP DE RENDIÇÃO
# ==============================================================================
label executar_golpe_critico_persona:
    if getattr(store, "img_inimigo_derrota", "") != "" and renpy.has_image(img_inimigo_derrota, exact=True):
        show expression img_inimigo_derrota as inimigo at sprite_padrao with dissolve
    elif img_inimigo_base != "":
        show expression img_inimigo_base as inimigo at inimigo_caido
    $ th_bark_inimigo(nome_inimigo, "derrota")
    with hpunch
    $ notificar_rpg("💥 POSTURA QUEBRADA", f"{nome_inimigo} está atordoado! HOLD-UP ATIVO!", "#ff0044")
    "A postura de [nome_inimigo] quebrou completamente! Ele desaba de joelhos, ofegante e desarmado diante de você."

    menu:
        "🩸 Predador em Movimento (Finalização Sanguínea / Menu de Drenagem)":
            "Você avança sobre a presa vulnerável com instinto predatório implacável!"
            jump pos_combate_drenagem

        "💥 All-Out Attack (Massacre Impiedoso / +Ressonância / Dano de Área)":
            with flash_red
            if renpy.loadable("audio/sfx/blade_slash_heavy.ogg"):
                play sound "audio/sfx/blade_slash_heavy.ogg"
            elif renpy.loadable("audio/blade_slash_heavy.ogg"):
                play sound "audio/blade_slash_heavy.ogg"
            $ th_bark("victor", "garras")
            stop music fadeout 0.3
            $ th_stinger("vitoria")
            $ ressonancia_pre_diluviana += 2
            $ notificar_rpg("⚡ ALL-OUT ATTACK", "+2 Ressonância Pré-Diluviana | Oponente esmagado!", "#ff2244")
            "Você e as sombras do corredor convergem em uma sequência avassaladora de estocadas e garras, pulverizando a resistência do alvo!"
            hide inimigo with dissolve
            return "vitoria_all_out"

        "💰 Extorquir & Intimidar (Cobrar Resgate em Créditos e Suprimentos)":
            $ saque_extra = renpy.random.randint(55, 105)
            $ dinheiro_jogador += saque_extra
            $ extorquiu_combate_atual = True
            $ exposicao = min(100, exposicao + 5)
            if renpy.random.randint(1, 100) <= 40:
                $ bolsa_sangue_filtrado += 1
                $ _bolsa_msg = "+1 Bolsa de Sangue Filtrado"
            else:
                $ bolsa_sangue_adulterado += 1
                $ _bolsa_msg = "+1 Bolsa de Sangue Adulterado"
            $ notificar_rpg("💵 EXTORSÃO BEM-SUCEDIDA", f"+${saque_extra} Créditos | {_bolsa_msg}", "#00ffcc")
            "Você encosta a lâmina fria na garganta de [nome_inimigo]. Sem hesitar, ele esvazia os bolsos e entrega uma bolsa escondida antes de rastejar para o escuro."
            hide inimigo with dissolve
            return "vitoria_extorquiu"

label pos_combate_drenagem:
    stop music fadeout 0.3
    $ th_stinger("vitoria")
    if getattr(store, "img_inimigo_derrota", "") != "" and renpy.has_image(img_inimigo_derrota, exact=True):
        show expression img_inimigo_derrota as inimigo at sprite_padrao with dissolve
    elif img_inimigo_base != "":
        show expression img_inimigo_base as inimigo at inimigo_caido
    "O golpe final quebra a postura do adversário!{w=0.3} [nome_inimigo] desaba de joelhos, subjugado."

    if store.clima_diario_id == "nevoa_carmesim":
        $ achado_nevoa = renpy.random.randint(60, 120)
        $ dinheiro_jogador += achado_nevoa
        $ notificar_rpg("🌫️ DESPOJOS DA NÉVOA", f"+${achado_nevoa} recolhidos dos restos corrompidos pela névoa!", "#aa00ff")

    if tipo_sangue_inimigo == "inorganico":
        "A forma de [nome_inimigo] começa a se desfazer em poeira rúnica."
        menu:
            "🔮 Absorver Essência Mística (+1 Ressonância)":
                $ ressonancia_pre_diluviana += 1
                $ notificar_rpg("🔮 ESSÊNCIA ABSORVIDA", "+1 Ressonância Pré-Diluviana!", "#aa00ff")
                hide inimigo with dissolve
                "O sangue pré-diluviano em suas veias consome a energia residual do guardião!"
                return "vitoria_absorveu"
            "🚶 Deixar os restos e avançar":
                hide inimigo with dissolve
                return "vitoria"

    "O cheiro metálico de sangue quente inunda o ar do corredor...{w=0.4} Sua garganta queima com a Fome incontrolável de Ghoul."
    "(O inimigo está caído à sua mercê... O sangue chama como um tambor no seu crânio. Drenar ou conter?)"

    menu:
        "🧛 Drenar o Sangue de [nome_inimigo] (+Sangue / +Poder / -Humanidade)":
            $ renpy.block_rollback()
            call screen qte_pulso_sangue(nome_inimigo)
            $ _res_pulso = _return
            $ th_sfx("heartbeat")
            $ th_sfx("mordida")
            $ th_sfx("borbulhar")
            with flash_red

            if tipo_sangue_inimigo == "gremio":
                $ _ganho_fome = 20 if _res_pulso == "transe_escapou" else (55 if _res_pulso == "transe_perfeito" else 40)
                $ fome_sangue = min(100, fome_sangue + _ganho_fome)
                $ ressonancia_pre_diluviana += 2
                $ humanidade = max(0, humanidade - (1 if _res_pulso == "transe_perfeito" else 2))
                $ drenou_membro_gremio = True
                $ punicoes_gremio_ativas += 1
                $ notificar_rpg("🩸 DRENAGEM DO GRÊMIO", f"+{_ganho_fome}% Saciedade | +2 Ressonância", "#ff4444")
                "Você crava as presas no inimigo caído, sugando a essência vampírica dele!"
                "⚠️ (+[_ganho_fome] Fome de Sangue | +2 Ressonância | Elara sentirá o cheiro deste tabu!)"

            elif tipo_sangue_inimigo == "corrompido":
                $ _ganho_fome = 18 if _res_pulso == "transe_escapou" else (50 if _res_pulso == "transe_perfeito" else 35)
                $ fome_sangue = min(100, fome_sangue + _ganho_fome)
                $ ressonancia_pre_diluviana += 3
                $ humanidade = max(0, humanidade - (2 if _res_pulso == "transe_perfeito" else 3))
                $ notificar_rpg("🩸 SANGUE CORROMPIDO", f"+{_ganho_fome}% Saciedade | +3 Ressonância", "#aa00ff")
                "Você bebe o sangue denso e envenenado pela energia das catacumbas!"
                "⚠️ (+[_ganho_fome] Fome de Sangue | +3 Ressonância)"

            elif tipo_sangue_inimigo == "humano":
                $ _ganho_fome = 25 if _res_pulso == "transe_escapou" else (65 if _res_pulso == "transe_perfeito" else 50)
                $ _exp_hum = aplicar_reducao_isolamento_exposicao(15)
                $ fome_sangue = min(100, fome_sangue + _ganho_fome)
                $ ressonancia_pre_diluviana += 1
                $ humanidade = max(0, humanidade - (0 if _res_pulso == "transe_perfeito" else 1))
                $ exposicao = min(100, exposicao + _exp_hum)
                $ notificar_rpg("🩸 DRENAGEM HUMANA", f"+{_ganho_fome}% Saciedade | +{_exp_hum}% Exposição", "#ff8800")
                "Você se alimenta vorazmente do oponente caído, absorvendo sua vitalidade."
                "⚠️ (+[_ganho_fome] Fome de Sangue | +1 Ressonância | +[_exp_hum] Exposição na Máscara)"

            if _res_pulso == "transe_perfeito":
                $ notificar_rpg("💓 TRANSE PERFEITO", "Cadência cardíaca impecável: +15% Saciedade extra e +1 Humanidade preservada!", "#00ffcc")
            elif _res_pulso == "transe_escapou":
                $ _exp_esc = aplicar_reducao_isolamento_exposicao(8)
                $ exposicao = min(100, exposicao + _exp_esc)
                $ notificar_rpg("⚠️ TRANSE ROMPIDO", f"O alvo se debateu antes da conclusão: metade da saciedade | +{_exp_esc}% Exposição!", "#ff5555")

            hide inimigo with dissolve
            return "vitoria_drenou"

        "🛡️ Conter a sede e poupar o derrotado (+Humanidade / Acalma o Abismo)":
            $ bonus_hum = 2 if "coracao_firme" in store.perks_desbloqueados else 1
            $ humanidade = min(100, humanidade + bonus_hum)
            if renpy.random.randint(1, 100) <= 35:
                $ GerenciadorRuina.reduzir_ruina(1, "Sede Contida")
            $ notificar_rpg("🕊️ SEDE CONTIDA", f"+{bonus_hum} Humanidade preservada!", "#88ccff")
            hide inimigo with dissolve
            "Você força suas presas a recuarem e mantém o controle sobre a maldição."
            return "vitoria_poupou"

# ==========================================
# 4. MORTE / GAME OVER
# ==========================================
# ATENÇÃO: este label é alcançado com 'jump' de dentro de um 'call'. Um 'return'
# aqui voltaria para a cena que chamou o combate (a história continuava como se
# o jogador tivesse vencido!). Por isso o fluxo termina em full_restart().
label morte_definitiva:
    hide screen hud_combate_zona_vermelha
    hide screen hud_sobrevivencia
    stop music fadeout 1.0
    $ th_stinger("morte")
    scene black with fade
    "Você sucumbiu aos perigos dos corredores..."
    $ persistent.ciclos_mortes += 1
    menu:
        "Carregar um jogo salvo":
            call screen load
            jump morte_definitiva
        "Voltar ao menu principal":
            $ renpy.full_restart()
