# ==============================================================================
# TELA_SAVE_DOSSIE.RPY — TELA DE SAVE / LOAD GÓTICA (CONCEITO B — DOSSIÊ)
# ==============================================================================
# Interface de Gravação e Carregamento em Grid Matemático Rígido de 3 Colunas:
# - Coluna 1 (Esquerda, x: 36..416): Logo animada (370x215) + 5 botões de navegação
# - Coluna 2 (Centro, x: 440..1300): Placa (620x96) + Grade 2x3 (405x240) + Paginação (88x74)
# - Coluna 3 (Direita, x: 1330..1880): Painel Dossiê em fixed absoluto (550x1020)
# ==============================================================================

default save_slot_inspecionado = 1
default limite_dias = 21

init -1 python:
    def registrar_metadados_dossie_save(d):
        """Grava os sinais vitais, dia, período e local no JSON nativo de cada save."""
        d["dia"] = getattr(store, "dia_atual", 1)
        d["limite"] = getattr(store, "limite_dias", 21)
        d["periodo"] = getattr(store, "periodo", "Manhã")
        d["local"] = getattr(store, "local_atual", "dormitorio")
        d["hp"] = getattr(store, "hp_jogador", 100)
        d["hp_max"] = getattr(store, "hp_jogador_max", 100)
        d["fome"] = getattr(store, "fome_sangue", 100)
        d["humanidade"] = getattr(store, "humanidade", 75)
        d["exposicao"] = getattr(store, "exposicao", 0)

    if registrar_metadados_dossie_save not in config.save_json_callbacks:
        config.save_json_callbacks.append(registrar_metadados_dossie_save)

    config.thumbnail_width = 456
    config.thumbnail_height = 256

    NOMES_LOCAIS_DOSSIE = {
        "dormitorio": "Dormitório Masculino",
        "biblioteca": "Biblioteca Gótica",
        "salao_gremio": "Salão do Grêmio Estudantil",
        "sala_musica": "Sala de Música Interditada",
        "enfermaria": "Enfermaria da Academia",
        "caldeiras": "Caldeiras & Mercado Negro",
        "bar_fada_verde": "Bar da Fada Verde",
        "banheiro_abandonado": "Banheiro Antigo (2º Andar)",
        "cemiterio_nevoa": "Cemitério da Névoa",
        "catacumbas": "Catacumbas Subterrâneas",
        "patio": "Pátio Central",
        "portoes": "Portões da Academia",
        "sala_ocultismo": "Sala de Ocultismo Hermético",
        "laboratorio": "Laboratório de Alquimia",
        "jardim_inverno": "Jardim de Inverno & Capela",
    }

    def formatar_local_dossie(chave_local):
        if not chave_local:
            return "Academia São Cipriano"
        return NOMES_LOCAIS_DOSSIE.get(chave_local, str(chave_local).replace("_", " ").title())

    def img_hud_save(nome_png, xysize=None, cor_fallback="#14161fee", matrixcolor=None):
        """Retorna o displayable escalado ou fallback seguro com suporte a BrightnessMatrix."""
        caminho = f"gui/hud_save/{nome_png}"
        if renpy.loadable(caminho):
            kwargs = {}
            if xysize:
                kwargs["xysize"] = xysize
                kwargs["fit"] = "fill"
            if matrixcolor:
                kwargs["matrixcolor"] = matrixcolor
            if kwargs:
                return Transform(caminho, **kwargs)
            return caminho
        if xysize:
            return Solid(cor_fallback, xysize=xysize)
        return Solid(cor_fallback)

    def dossie_json(slot_id, chave, valor_padrao=None):
        """Retorna metadados do JSON de forma resiliente para qualquer slot."""
        try:
            val = FileJson(slot_id, key=chave, empty=valor_padrao, missing=valor_padrao)
            return val if val is not None else valor_padrao
        except Exception:
            return valor_padrao

    def formatar_rotulo_slot(slot_id):
        if not FileLoadable(slot_id):
            return "SLOT LIVRE"
        s_dia = dossie_json(slot_id, "dia", None)
        if s_dia is not None:
            try:
                return "DIA %02d" % int(s_dia)
            except Exception:
                return f"DIA {s_dia}"
        return f"REGISTRO #{slot_id}"

    def formatar_mensagem_confirmacao(msg):
        """Traduz mensagens padrão do Ren'Py para português gótico imersivo com busca por palavras-chave."""
        msg_str = str(msg or "")
        msg_lower = msg_str.lower()
        if "overwrite" in msg_lower or "sobrescrever" in msg_lower:
            return "Tem certeza de que deseja sobrescrever esta gravação?"
        if "delete" in msg_lower or "apagar" in msg_lower or "excluir" in msg_lower:
            return "Tem certeza de que deseja apagar esta gravação?"
        if "load" in msg_lower or "carregar" in msg_lower:
            return "Tem certeza de que deseja carregar esta gravação?"
        if "quit" in msg_lower or "sair" in msg_lower:
            return "Tem certeza de que deseja sair do jogo?"
        if "main menu" in msg_lower or "menu principal" in msg_lower:
            return "Deseja retornar ao Menu Principal? O progresso não salvo será perdido."
        if "replay" in msg_lower or "reprodução" in msg_lower:
            return "Tem certeza de que deseja encerrar a reprodução?"
        if "reload" in msg_lower or "recarregamento" in msg_lower:
            return "O recarregamento lento redefinirá o estado do jogo. Continuar?"
        return msg_str

# ==============================================================================
# PARALAXE TRIPLA REUTILIZÁVEL PARA TELAS DE ARQUIVO / MENU
# ==============================================================================
screen fundo_paralaxe_dossie(escurecer=True):
    # Camada 1: Vídeo da Lua Sangrando em Looping (Paralaxe Sutil)
    if renpy.loadable("images/menu/bg_menu_lua_sangrando.webm"):
        add Movie(play="images/menu/bg_menu_lua_sangrando.webm", size=(1920, 1080), loop=True) at menu_paralaxe_video
    elif renpy.loadable("images/wallpapers static/bg menu principal piano cidade lua sangue.jpg"):
        add "images/wallpapers static/bg menu principal piano cidade lua sangue.jpg":
            size (1920, 1080)
    else:
        add Solid("#07080f")

    # Camada 2: Sala Gótica com Arcos e Luz Noturna (Paralaxe Média)
    if renpy.loadable("images/menu/menu_sala_meio.png"):
        add "images/menu/menu_sala_meio.png" at menu_paralaxe_meio

    # Camada 3: Piano de Cauda em Primeiro Plano (Paralaxe Forte)
    if renpy.loadable("images/menu/menu_piano_frente.png"):
        add "images/menu/menu_piano_frente.png" at menu_paralaxe_frente

    # Véu Translúcido Escuro para Alta Legibilidade dos Cartões
    if escurecer:
        add Solid("#06070cd4")

# ==============================================================================
# COMPONENTE DA LOGO MULTICAMADAS ANIMADA (CONTIDA EM 315x170)
# ==============================================================================
screen logo_animada_dossie():
    fixed:
        xsize 315
        ysize 170

        # Camada 1: Lua mais fundo com pulsação mística suave
        if renpy.loadable("images/menu/logo_organizado/menu_logo_lua.png"):
            add "images/menu/logo_organizado/menu_logo_lua.png":
                zoom 0.26
                at logo_pulsar_lua

        # Camada 2: Glifos arcanos estáticos
        if renpy.loadable("images/menu/logo_organizado/menu_logo_glifos_parados.png"):
            add "images/menu/logo_organizado/menu_logo_glifos_parados.png":
                zoom 0.26

        # Camada 3: Glifos internos em rotação orbital contínua
        if renpy.loadable("images/menu/logo_organizado/menu_logo_glifos_rodam_square.png"):
            add "images/menu/logo_organizado/menu_logo_glifos_rodam_square.png":
                zoom 0.26
                pos (151, 68)
                at logo_girar_continuo

        # Camada 4: Adorno inferior pontiagudo
        if renpy.loadable("images/menu/logo_organizado/menu_logo_parte_baixo.png"):
            add "images/menu/logo_organizado/menu_logo_parte_baixo.png":
                zoom 0.26

        # Camada 5: Tipografia metálica em relevo (The Hunger and the Hallways)
        if renpy.loadable("images/menu/logo_organizado/menu_logo_letras.png"):
            add "images/menu/logo_organizado/menu_logo_letras.png":
                zoom 0.26

# ==============================================================================
# TELAS NATIVAS SAVE / LOAD + GRID 2x3 + DOSSIÊ LATERAL
# ==============================================================================
screen save():
    tag menu
    use arquivo_dossie_screen(modo="save")

screen load():
    tag menu
    use arquivo_dossie_screen(modo="load")

screen arquivo_dossie_screen(modo="load"):
    modal True
    zorder 90

    # Atalhos para fechar e retornar
    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    use fundo_paralaxe_dossie(escurecer=True)

    $ eh_save = (modo == "save")
    $ titulo_topo = "GRAVAR REGISTRO" if eh_save else "CARREGAR REGISTRO"
    $ acao_principal_txt = "GRAVAR REGISTRO" if eh_save else "CARREGAR REGISTRO"

    # ==========================================================================
    # COLUNA 1 (ESQUERDA, x: 42 a 362): LOGO ANIMADA + 5 BOTÕES GÓTICOS
    # ==========================================================================
    # Contêiner fixo da logo no topo esquerdo (impossível transbordar para a coluna 2)
    frame:
        xpos 45
        ypos 24
        xysize (315, 170)
        background None
        padding (0, 0)
        use logo_animada_dossie

    # Pilha vertical dos botões laterais (xpos 42 ypos 214, spacing 12, xysize 320x68)
    vbox:
        xpos 42
        ypos 214
        spacing 12

        if not main_menu:
            button:
                xysize (320, 68)
                background img_hud_save("btn_nav_hover.png" if eh_save else "btn_nav_idle.png", xysize=(320, 68))
                hover_background img_hud_save("btn_nav_hover.png", xysize=(320, 68))
                action ShowMenu("save")
                text "SALVAR":
                    align (0.5, 0.5)
                    size 20
                    bold True
                    color ("#ffffff" if eh_save else "#cbd5e1")
                    outlines [(2, "#000000dd", 0, 0)]

        button:
            xysize (320, 68)
            background img_hud_save("btn_nav_hover.png" if not eh_save else "btn_nav_idle.png", xysize=(320, 68))
            hover_background img_hud_save("btn_nav_hover.png", xysize=(320, 68))
            action ShowMenu("load")
            text "CARREGAR":
                align (0.5, 0.5)
                size 20
                bold True
                color ("#ffffff" if not eh_save else "#cbd5e1")
                outlines [(2, "#000000dd", 0, 0)]

        button:
            xysize (320, 68)
            background img_hud_save("btn_nav_idle.png", xysize=(320, 68))
            hover_background img_hud_save("btn_nav_hover.png", xysize=(320, 68))
            action ShowMenu("galeria_memorias")
            text "GALERIA":
                align (0.5, 0.5)
                size 20
                bold True
                color "#cbd5e1"
                outlines [(2, "#000000dd", 0, 0)]

        button:
            xysize (320, 68)
            background img_hud_save("btn_nav_idle.png", xysize=(320, 68))
            hover_background img_hud_save("btn_nav_hover.png", xysize=(320, 68))
            action ShowMenu("preferences")
            text "OPÇÕES":
                align (0.5, 0.5)
                size 20
                bold True
                color "#cbd5e1"
                outlines [(2, "#000000dd", 0, 0)]

        button:
            xysize (320, 68)
            background img_hud_save("btn_nav_idle.png", xysize=(320, 68))
            hover_background img_hud_save("btn_nav_hover.png", xysize=(320, 68))
            action Return()
            text "VOLTAR":
                align (0.5, 0.5)
                size 20
                bold True
                color "#fda4af"
                outlines [(2, "#000000dd", 0, 0)]

    # ==========================================================================
    # COLUNA 2 (CENTRO, x: 455 a 1267): BANNER, GRADE 2x3 E PAGINAÇÃO ROMANA
    # ==========================================================================
    # Placa Ornamental Superior Centralizada (460x74 em xpos 631 ypos 18)
    frame:
        xpos 631
        ypos 18
        xysize (460, 74)
        background img_hud_save("header_banner_save.png", xysize=(460, 74))
        padding (10, 6)
        text "[titulo_topo]":
            align (0.5, 0.5)
            size 20
            bold True
            color "#f8fafc"
            outlines [(2, "#000000ee", 0, 0)]

    # Grade 2 Colunas x 3 Linhas (xpos 455 ypos 116, xspacing 22 yspacing 10)
    grid 2 3:
        xpos 455
        ypos 116
        xspacing 22
        yspacing 10

        for i in range(1, 7):
            $ slot_id = i
            $ carregavel = FileLoadable(slot_id)
            $ selecionado = (store.save_slot_inspecionado == slot_id)
            $ rotulo_card = formatar_rotulo_slot(slot_id)

            vbox:
                spacing 3
                xalign 0.5

                # Cartão Clicável com Seleção em Dois Passos (395x222 com fixed interno)
                button:
                    xysize (395, 222)
                    padding (0, 0)
                    background img_hud_save(
                        "slot_save_selected.png" if selecionado
                        else ("slot_save_normal.png" if carregavel else "slot_save_empty.png"),
                        xysize=(395, 222)
                    )
                    hover_background img_hud_save("slot_save_dourado.png", xysize=(395, 222))
                    action SetVariable("save_slot_inspecionado", slot_id)

                    fixed:
                        xfill True
                        yfill True

                        # Título centralizado na plaquinha superior da moldura (ypos 10, size 17)
                        text "[rotulo_card]":
                            xalign 0.5
                            ypos 10
                            size 17
                            bold True
                            color ("#4ade80" if selecionado else ("#e2e8f0" if carregavel else "#64748b"))
                            outlines ([(1, "#000000cc", 0, 0)] if carregavel else [])

                        # Miniatura 16:9 da Cena Gravada perfeitamente contida no visor interno
                        if carregavel:
                            add FileScreenshot(slot_id):
                                xalign 0.5
                                ypos 48
                                xysize (355, 162)
                        else:
                            frame:
                                xalign 0.5
                                ypos 48
                                xysize (355, 162)
                                background "#08090fbb"
                                text "— Sem Memória Gravada —":
                                    align (0.5, 0.5)
                                    size 14
                                    color "#475569"

                # Data e Hora do Salvamento abaixo do Cartão
                text FileTime(slot_id, format=_("{#file_time}%A, %H:%M"), empty="Slot Disponível"):
                    xalign 0.5
                    size 13
                    color ("#f1f5f9" if selecionado else "#94a3b8")
                    outlines [(1, "#000000cc", 0, 0)]

    # Paginação Inferior em Losangos Romanos (xpos 584 ypos 888, 64x52)
    hbox:
        xpos 584
        ypos 888
        spacing 6
        $ lista_paginas = [
            ("auto", "AUTO"),
            ("quick", "RÁPIDO"),
            ("1", "I"),
            ("2", "II"),
            ("3", "III"),
            ("4", "IV"),
            ("5", "V"),
            ("6", "VI")
        ]
        for pg_id, pg_label in lista_paginas:
            $ pg_ativa = (str(FileCurrentPage()) == str(pg_id))
            button:
                xysize (64, 52)
                background img_hud_save("btn_pagina_active.png" if pg_ativa else "btn_pagina_idle.png", xysize=(64, 52))
                hover_background img_hud_save("btn_pagina_active.png", xysize=(64, 52))
                action [FilePage(pg_id), SetVariable("save_slot_inspecionado", 1)]
                text "[pg_label]":
                    align (0.5, 0.5)
                    size 13
                    bold True
                    color ("#ffffff" if pg_ativa else "#94a3b8")
                    outlines [(1, "#000000cc", 0, 0)]

    # ==========================================================================
    # COLUNA 3 (DIREITA, x: 1330 a 1850): PAINEL DOSSIÊ EM FIXED ABSOLUTO
    # ==========================================================================
    $ insp_ok = FileLoadable(store.save_slot_inspecionado)
    $ d_dia = dossie_json(store.save_slot_inspecionado, "dia", 1)
    $ d_lim = dossie_json(store.save_slot_inspecionado, "limite", 21)
    $ d_per = dossie_json(store.save_slot_inspecionado, "periodo", "Manhã")
    $ d_loc = formatar_local_dossie(dossie_json(store.save_slot_inspecionado, "local", "dormitorio"))
    $ d_hp  = dossie_json(store.save_slot_inspecionado, "hp", 100)
    $ d_hpm = dossie_json(store.save_slot_inspecionado, "hp_max", 100)
    $ d_fome = dossie_json(store.save_slot_inspecionado, "fome", 100)
    $ d_hum = dossie_json(store.save_slot_inspecionado, "humanidade", 75)
    $ d_exp = dossie_json(store.save_slot_inspecionado, "exposicao", 0)

    $ c_hp = getattr(store, "hp_jogador", 100)
    $ c_hpm = getattr(store, "hp_jogador_max", 100)
    $ c_fome = getattr(store, "fome_sangue", 100)
    $ c_hum = getattr(store, "humanidade", 75)
    $ c_exp = getattr(store, "exposicao", 0)

    $ pode_agir = (FileCurrentPage() != "auto") if eh_save else insp_ok

    frame:
        xpos 1330
        ypos 26
        xysize (520, 990)
        background img_hud_save("painel_dossie.png", xysize=(520, 990))
        padding (0, 0)

        fixed:
            xfill True
            yfill True

            # Título do Dossiê
            text "Dossiê":
                xalign 0.5
                ypos 18
                size 26
                bold True
                color "#f8fafc"
                outlines [(2, "#000000ee", 0, 0)]

            # Miniatura Ampliada 16:9 em Alta Resolução (xalign 0.5 ypos 78 xysize 440x248)
            if insp_ok:
                add FileScreenshot(store.save_slot_inspecionado):
                    xalign 0.5
                    ypos 78
                    xysize (440, 248)
            else:
                frame:
                    xalign 0.5
                    ypos 78
                    xysize (440, 248)
                    background "#07080fdd"
                    text "Selecione um registro para inspecionar\nou grave o progresso atual.":
                        align (0.5, 0.5)
                        text_align 0.5
                        size 15
                        color "#64748b"

            # Bloco de Local / Dia (abaixo da miniatura)
            if insp_ok:
                text "Dia [d_dia]/[d_lim] - [d_per]":
                    xalign 0.5
                    ypos 348
                    size 23
                    bold True
                    color "#ef4444"
                    outlines [(2, "#000000dd", 0, 0)]

                text "[d_loc]":
                    xalign 0.5
                    ypos 380
                    size 19
                    color "#f1f5f9"
                    outlines [(1, "#000000dd", 0, 0)]
            else:
                text "Slot #[store.save_slot_inspecionado] Livre":
                    xalign 0.5
                    ypos 352
                    size 22
                    bold True
                    color "#94a3b8"

                text "Nenhuma gravação neste registro.":
                    xalign 0.5
                    ypos 384
                    size 16
                    color "#64748b"

            # Bloco Barra de Status (ypos 432 a 610)
            text "Barra de Status":
                xalign 0.5
                ypos 432
                size 20
                bold True
                color "#f87171"
                outlines [(1, "#000000cc", 0, 0)]

            if insp_ok:
                vbox:
                    xpos 62
                    ypos 472
                    spacing 10

                    hbox:
                        spacing 10
                        yalign 0.5
                        add img_hud_save("stat_hp.png") xysize (24, 24) yalign 0.5
                        text "HP: [d_hp]/[d_hpm]" size 18 color "#f1f5f9" yalign 0.5 outlines [(1, "#000000", 0, 0)]

                    hbox:
                        spacing 10
                        yalign 0.5
                        add img_hud_save("stat_fome.png") xysize (24, 24) yalign 0.5
                        text "Fome: [d_fome]%" size 18 color "#f1f5f9" yalign 0.5 outlines [(1, "#000000", 0, 0)]

                    hbox:
                        spacing 10
                        yalign 0.5
                        add img_hud_save("stat_humanidade.png") xysize (24, 24) yalign 0.5
                        text "Humanidade: [d_hum]" size 18 color "#f1f5f9" yalign 0.5 outlines [(1, "#000000", 0, 0)]

                    hbox:
                        spacing 10
                        yalign 0.5
                        add img_hud_save("stat_exposicao.png") xysize (24, 24) yalign 0.5
                        text "Exposição: [d_exp]%" size 18 color "#f1f5f9" yalign 0.5 outlines [(1, "#000000", 0, 0)]
            else:
                vbox:
                    xpos 62
                    ypos 472
                    spacing 10

                    hbox:
                        spacing 10
                        yalign 0.5
                        add img_hud_save("stat_hp.png") xysize (24, 24) yalign 0.5
                        text "HP: [c_hp]/[c_hpm] (Estado Atual)" size 18 color "#94a3b8" yalign 0.5 outlines [(1, "#000000", 0, 0)]

                    hbox:
                        spacing 10
                        yalign 0.5
                        add img_hud_save("stat_fome.png") xysize (24, 24) yalign 0.5
                        text "Fome: [c_fome]% (Estado Atual)" size 18 color "#94a3b8" yalign 0.5 outlines [(1, "#000000", 0, 0)]

                    hbox:
                        spacing 10
                        yalign 0.5
                        add img_hud_save("stat_humanidade.png") xysize (24, 24) yalign 0.5
                        text "Humanidade: [c_hum] (Estado Atual)" size 18 color "#94a3b8" yalign 0.5 outlines [(1, "#000000", 0, 0)]

                    hbox:
                        spacing 10
                        yalign 0.5
                        add img_hud_save("stat_exposicao.png") xysize (24, 24) yalign 0.5
                        text "Exposição: [c_exp]% (Estado Atual)" size 18 color "#94a3b8" yalign 0.5 outlines [(1, "#000000", 0, 0)]

            # Botões de Ação Fixos na Base Interna do Dossiê (nunca saem da moldura)
            button:
                xalign 0.5
                ypos 730
                xysize (380, 74)
                background img_hud_save("btn_acao_primario.png", xysize=(380, 74))
                hover_background img_hud_save("btn_acao_primario.png", xysize=(380, 74), matrixcolor=BrightnessMatrix(0.18))
                action (FileSave(store.save_slot_inspecionado) if eh_save else FileLoad(store.save_slot_inspecionado))
                text "[acao_principal_txt]":
                    align (0.5, 0.5)
                    size 18
                    bold True
                    color ("#ffffff" if pode_agir else "#64748b")
                    outlines [(2, "#000000dd", 0, 0)]

            button:
                xalign 0.5
                ypos 820
                xysize (350, 66)
                background img_hud_save("btn_acao_apagar.png", xysize=(350, 66))
                hover_background img_hud_save("btn_acao_apagar.png", xysize=(350, 66), matrixcolor=BrightnessMatrix(0.18))
                action FileDelete(store.save_slot_inspecionado)
                text "APAGAR":
                    align (0.5, 0.5)
                    size 17
                    bold True
                    color ("#e2e8f0" if insp_ok else "#475569")
                    outlines [(2, "#000000dd", 0, 0)]

# ==============================================================================
# POP-UP DE CONFIRMAÇÃO GÓTICO PERSONALIZADO (SOBRESCREVER / APAGAR SAVE)
# ==============================================================================
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    # Atalhos para fechar ou cancelar
    key "game_menu" action no_action
    key "K_ESCAPE" action no_action

    # Fundo escurecido semi-transparente
    add Solid("#040509dd")

    $ msg_traduzida = formatar_mensagem_confirmacao(message)

    frame:
        align (0.5, 0.5)
        xysize (760, 320)
        background Frame(img_hud_save("slot_save_normal.png"), 40, 45)
        padding (40, 32)

        vbox:
            spacing 26
            align (0.5, 0.5)

            text msg_traduzida:
                xalign 0.5
                text_align 0.5
                size 22
                bold True
                color "#f8fafc"
                outlines [(2, "#000000ee", 0, 0)]
                xsize 660

            hbox:
                xalign 0.5
                spacing 44

                button:
                    xysize (240, 62)
                    background img_hud_save("btn_acao_primario.png", xysize=(240, 62))
                    hover_background img_hud_save("btn_acao_primario.png", xysize=(240, 62), matrixcolor=BrightnessMatrix(0.18))
                    action yes_action
                    text "CONFIRMAR":
                        align (0.5, 0.5)
                        size 17
                        bold True
                        color "#ffffff"
                        outlines [(2, "#000000dd", 0, 0)]

                button:
                    xysize (240, 62)
                    background img_hud_save("btn_acao_apagar.png", xysize=(240, 62))
                    hover_background img_hud_save("btn_acao_apagar.png", xysize=(240, 62), matrixcolor=BrightnessMatrix(0.18))
                    action no_action
                    text "CANCELAR":
                        align (0.5, 0.5)
                        size 17
                        bold True
                        color "#cbd5e1"
                        outlines [(2, "#000000dd", 0, 0)]
