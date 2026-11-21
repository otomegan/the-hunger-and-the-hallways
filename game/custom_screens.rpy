# ==============================================================================

# CUSTOM_SCREENS.RPY - MAPA, BLACK SURVIVAL, INVENTÁRIO, STATUS E TOQUE

# ==============================================================================

default aba_mapa_subsolo = False

default debug_mostrar_hitboxes = False

default tentou_visitar_manha_hoje = False

default cliques_sono_lility = 0

default perguntou_punicao_elara = 0

# ==============================================================================

# 1. TELA DE PAUSE / ESTADO DE VICTOR VANE E RELACIONAMENTOS

# ==============================================================================

screen status_victor_pause():

    tag menu

    modal True

    zorder 95

    add Solid("#0a0a0ff4")

    frame:

        align (0.5, 0.5)

        xysize (1760, 960)

        background "#12131aee"

        padding (35, 30)

        vbox:

            spacing 18

            # Cabeçalho

            hbox:

                xfill True

                text "🩸 DOSSIÊ DE ESTADO — VICTOR VANE (DIA [dia_atual] • SOBREVIVÊNCIA - [periodo!u])" size 30 bold True color "#ff4444"

                textbutton "✖ FECHAR / VOLTAR" action Return() xalign 1.0 text_size 24 text_color "#00ffcc" text_hover_color "#ffffff"

            null height 5

            hbox:

                spacing 40

                # COLUNA 1: Retrato Dinâmico da Fase de Victor

                frame:

                    xysize (460, 800)

                    background "#1a1c26"

                    padding (20, 20)

                    vbox:

                        spacing 12

                        xalign 0.5

                        text "ASPECTO ATUAL" size 22 bold True color "#88ccff" xalign 0.5

                        add obter_sprite_victor("serio") xalign 0.5 yalign 1.0 ysize 560 fit "contain"

                        text obter_descricao_fase_victor() size 16 color "#e0e0e0" xalign 0.5 text_align 0.5

                # COLUNA 2: Status Vitais e Atributos de RPG

                frame:

                    xysize (580, 800)

                    background "#1a1c26"

                    padding (25, 20)

                    vbox:

                        spacing 14

                        text "📊 SINAIS VITAIS E RUÍNA" size 24 bold True color "#ffcc00"

                        vbox:

                            spacing 4

                            text "❤️ Vida (HP): [hp_jogador] / [hp_jogador_max]" size 19 color "#ffffff"

                            bar value hp_jogador range hp_jogador_max xysize (520, 18)

                        vbox:

                            spacing 4

                            text "🩸 Saciedade de Sangue: [fome_sangue]% (Frenesi abaixo de 20%)" size 19 color "#ff6666"

                            bar value fome_sangue range 100 xysize (520, 18)

                        vbox:

                            spacing 4

                            text "🧠 Humanidade: [humanidade] / 100" size 19 color "#88ccff"

                            bar value humanidade range 100 xysize (520, 18)

                        vbox:

                            spacing 4

                            text "🎭 Exposição da Máscara: [exposicao]% (Alerta do Grêmio)" size 19 color "#cc88ff"

                            bar value exposicao range 100 xysize (520, 18)

                        vbox:

                            spacing 4

                            text "⚡ DOOM: [ruina_cain]% (DOOM Clock)" size 19 bold True color ("#ff1111" if ruina_cain >= 75 else ("#ff8800" if ruina_cain >= 50 else ("#ffcc00" if ruina_cain >= 25 else "#88ccff")))

                            bar value ruina_cain range 100 xysize (520, 18)

                        null height 4

                        text "⚔️ ATRIBUTOS E CONHECIMENTO" size 22 bold True color "#00ffcc"

                        grid 2 4:

                            spacing 12

                            text "🦁 Coragem: [coragem]" size 18 color "#ffffff"

                            text "📘 Intelecto: [intelecto]" size 18 color "#ffffff"

                            text "✨ Charme: [charme]" size 18 color "#ffffff"

                            text "👁️ Sensibilidade: [sensibilidade_sobrenatural]" size 18 color "#ffffff"

                            text "👑 Domínio: [dominio_jogador]" size 18 color "#ff9999"

                            text "🕯️ Ocultismo: [conhecimento_oculto]" size 18 color "#ccccff"

                            text "🔮 Ressonância: [ressonancia_pre_diluviana]" size 18 color "#ff5555"

                            text "💰 Carteira: $[dinheiro_jogador]" size 18 color "#66ff66"

                        null height 8

                        text "📌 Punições do Grêmio Ativas: [punicoes_gremio_ativas]" size 17 color "#ffaaaa"

                        if ritual_corte_vinculo_desbloqueado:

                            text "📌 Ritual do Corte do Vínculo: Desbloqueado" size 17 color "#88ccff"

                        else:

                            text "📌 Ritual do Corte do Vínculo: Bloqueado" size 17 color "#777777"

                # COLUNA 3: Relacionamentos (Afeto, Dúvida e Humor)

                frame:

                    xysize (580, 800)

                    background "#1a1c26"

                    padding (25, 20)

                    vbox:

                        spacing 16

                        text "💞 VÍNCULOS E FACÇÕES" size 24 bold True color "#ff66aa"

                        # Lility

                        frame:

                            xfill True background "#2a1218" padding (15, 12)

                            vbox:

                                spacing 4

                                $ _titulo_dossie_m = obter_titulo_dossie_mestra()
                                text "[_titulo_dossie_m]" size 20 bold True color "#ff4444"

                                text "Afeto: [afeto_mestra] | 🩸 Vínculo: [vinculo_sangue_lility] (Origem Primordial) | Dúvida: [duvida_mestra] | Humor: [humor_mestra!c]" size 16 color "#e0e0e0"

                                $ _vis_m, _rum_m = heroina_revelada_no_mapa("lility")
                                if _vis_m:
                                    $ _nome_loc_m = obter_nome_local(loc_mestra)
                                    text ("🔍 [RUMOR] Local Detectado: [_nome_loc_m!u]" if _rum_m else "Local Atual Detectado: [_nome_loc_m!u]") size 15 color "#ff9999"
                                else:
                                    text "Local Atual: ❓ Não rastreada (Sonde rumores ou aumente afeto)" size 15 color "#777788"

                        # Emília

                        frame:

                            xfill True background "#121e2e" padding (15, 12)

                            vbox:

                                spacing 4

                                text "✝️ Emília von Karsten (Exorcista Bolsista)" size 20 bold True color "#5c85d6"

                                if pacto_emilia_ativo:

                                    text "Afeto: [afeto_emilia] | 🩸 Vínculo: [vinculo_sangue_emilia] (Pacto Sagrado) | Suspeita: [duvida_emilia] | Humor: [humor_emilia!c]" size 16 color "#e0e0e0"

                                else:

                                    text "Afeto: [afeto_emilia] | 🔒 Vínculo: Bloqueado (Requer Pacto de Sangue) | Suspeita: [duvida_emilia] | Humor: [humor_emilia!c]" size 16 color "#e0e0e0"

                                $ _vis_e, _rum_e = heroina_revelada_no_mapa("emilia")
                                if _vis_e:
                                    $ _nome_loc_e = obter_nome_local(loc_emilia)
                                    text ("🔍 [RUMOR] Local Detectado: [_nome_loc_e!u]" if _rum_e else "Local Atual Detectado: [_nome_loc_e!u]") size 15 color "#88ccff"
                                else:
                                    text "Local Atual: ❓ Não rastreada (Sonde rumores ou aumente afeto)" size 15 color "#777788"

                        # Valéria

                        frame:

                            xfill True background "#122618" padding (15, 12)

                            vbox:

                                spacing 4

                                text "🧪 Valéria (Mercadora das Caldeiras)" size 20 bold True color "#2eb82e"

                                if safra_rara_valeria:

                                    text "Afeto: [afeto_valeria] | 🩸 Vínculo: [vinculo_sangue_valeria] (Safra Rara Ativa) | Dúvida: [duvida_valeria] | Humor: [humor_valeria!c]" size 16 color "#e0e0e0"

                                else:

                                    text "Afeto: [afeto_valeria] | 🔒 Vínculo: Bloqueado (Requer Negociar Safra Rara) | Dúvida: [duvida_valeria] | Humor: [humor_valeria!c]" size 16 color "#e0e0e0"

                                $ _vis_v, _rum_v = heroina_revelada_no_mapa("valeria")
                                if _vis_v:
                                    $ _nome_loc_v = obter_nome_local(loc_valeria)
                                    text ("🔍 [RUMOR] Local Detectado: [_nome_loc_v!u]" if _rum_v else "Local Atual Detectado: [_nome_loc_v!u]") size 15 color "#88ff88"
                                else:
                                    text "Local Atual: ❓ Não rastreada (Sonde rumores ou aumente afeto)" size 15 color "#777788"

                        # Elara

                        frame:

                            xfill True background "#241d29" padding (15, 12)

                            vbox:

                                spacing 4

                                text "⚖️ Presidente Elara (Conselho Estudantil)" size 20 bold True color "#ffffff"

                                if elara_subjugada_no_cofre:

                                    text "Afeto: [afeto_elara] | 🩸 Vínculo: [vinculo_sangue_elara] (Presidente Subjugada) | Dúvida: [duvida_elara] | Humor: [humor_elara!c]" size 16 color "#e0e0e0"

                                else:

                                    text "Afeto: [afeto_elara] | 🔒 Vínculo: Bloqueado (Requer Derrota no Cofre) | Dúvida: [duvida_elara] | Humor: [humor_elara!c]" size 16 color "#e0e0e0"

                                $ _vis_el, _rum_el = heroina_revelada_no_mapa("elara")
                                if _vis_el:
                                    $ _nome_loc_el = obter_nome_local(loc_elara)
                                    text ("🔍 [RUMOR] Local Detectado: [_nome_loc_el!u]" if _rum_el else "Local Atual Detectado: [_nome_loc_el!u]") size 15 color "#dcb8ff"
                                else:
                                    text "Local Atual: ❓ Não rastreada (Sonde rumores ou aumente afeto)" size 15 color "#777788"

                        if rastro_olfativo_atual:

                            text "👃 Aroma Ativo no Casaco: " + obter_descricao_aroma(rastro_olfativo_atual) size 14 bold True color "#cc88ff"

                        if encontro_agendado_heroina:

                            text "🌙 Encontro Agendado: [encontro_agendado_heroina!u] ([encontro_agendado_local!u] - [encontro_agendado_periodo])" size 14 bold True color "#ffcc00"

                        null height 10

                        hbox:

                            spacing 20 xalign 0.5

                            textbutton "🎒 Abrir Inventário" action ShowMenu("inventario_victor") text_size 20 text_color "#ffcc00"

                            textbutton "⚙️ Opções / Salvar" action ShowMenu("save") text_size 20 text_color "#ffffff"

# ==============================================================================

# 2. TELA DE INVENTÁRIO E BANCADA PORTÁTIL (CONSUMÍVEIS, MATERIAIS E CHAVES)

# ==============================================================================

screen inventario_victor():

    tag menu

    modal True

    zorder 95

    add Solid("#0a0a0ff4")

    frame:

        align (0.5, 0.5)

        xysize (1600, 900)

        background "#12161fee"

        padding (35, 30)

        vbox:

            spacing 20

            hbox:

                xfill True

                text "🎒 INVENTÁRIO E EQUIPAMENTOS DE VICTOR — Carteira: $[dinheiro_jogador]" size 28 bold True color "#ffcc00"

                textbutton "📜 LIVRO DE DÍVIDAS" action ShowMenu("central_tatica_feniks", "dividas") text_size 22 text_color "#ff9933" text_hover_color "#ffffff" yalign 0.5

                textbutton "✖ FECHAR" action Return() xalign 1.0 text_size 24 text_color "#00ffcc"

            text "❤️ HP: [hp_jogador]/[hp_jogador_max] | 🩸 Saciedade: [fome_sangue]% | 🧠 Humanidade: [humanidade] | 🎭 Exposição: [exposicao]%" size 20 color "#cccccc"

            hbox:

                spacing 35

                # COLUNA 1: Itens Consumíveis (Uso Imediato)

                frame:

                    xysize (500, 700)

                    background "#1a202c"

                    padding (20, 20)

                    vbox:

                        spacing 15

                        text "🧪 CONSUMÍVEIS (CLIQUE PARA USAR)" size 22 bold True color "#66ff66"

                        frame:

                            xfill True background "#242c3d" padding (12, 10)

                            vbox:

                                text "🩸 Bolsa de Sangue Filtrado ([bolsa_sangue_filtrado]x)" size 19 bold True color "#ff6666"

                                text "Recupera +35%% de Saciedade sem perder Humanidade." size 15 color "#cccccc"

                                if bolsa_sangue_filtrado > 0:

                                    textbutton "▶ Consumir Agora" action [

                                        SetVariable("bolsa_sangue_filtrado", bolsa_sangue_filtrado - 1),

                                        SetVariable("fome_sangue", min(100, fome_sangue + 35)),

                                        Notify("Você consumiu uma Bolsa de Sangue Filtrado (+35% Saciedade).")

                                    ] text_size 17 text_color "#00ffcc"

                        frame:

                            xfill True background "#242c3d" padding (12, 10)

                            vbox:

                                text "🩹 Kit de Curativos Médicos ([kit_curativo]x)" size 19 bold True color "#88ccff"

                                text "Estanca ferimentos de combate (+30 HP)." size 15 color "#cccccc"

                                if kit_curativo > 0 and hp_jogador < hp_jogador_max:

                                    textbutton "▶ Aplicar Curativo" action [

                                        SetVariable("kit_curativo", kit_curativo - 1),

                                        SetVariable("hp_jogador", min(hp_jogador_max, hp_jogador + 30)),

                                        Notify("Você enfaixou seus ferimentos (+30 HP).")

                                    ] text_size 17 text_color "#00ffcc"

                        frame:

                            xfill True background "#242c3d" padding (12, 10)

                            vbox:

                                text "🍸 Dose de Absinto Esmeralda ([dose_absinto]x)" size 19 bold True color "#00ff88"

                                text "Aguça a percepção (+1 Sensibilidade Sobrenatural / +1 Coragem)." size 15 color "#cccccc"

                                if dose_absinto > 0:

                                    textbutton "▶ Beber Dose" action [

                                        SetVariable("dose_absinto", dose_absinto - 1),

                                        SetVariable("sensibilidade_sobrenatural", sensibilidade_sobrenatural + 1),

                                        SetVariable("coragem", coragem + 1),

                                        Notify("O Absinto queima na garganta (+1 Sensibilidade / +1 Coragem)!")

                                    ] text_size 17 text_color "#00ffcc"

                # COLUNA 2: Materiais Táticos e Crafting (Estilo Black Survival)

                frame:

                    xysize (500, 700)

                    background "#1a202c"

                    padding (20, 20)

                    vbox:

                        spacing 15

                        text "🛠️ HARDWARE E ARTILHARIA RÚNICA" size 22 bold True color "#00ffcc"

                        text "⚡ Dispositivos de Choque Rúnico: [dispositivo_choque]x" size 19 color "#ffffff"

                        text "🖍️ Giz de Proteção Rúnico: [giz_protecao]x" size 19 color "#ffffff"

                        text "⚙️ Sucata Eletrônica: [sucata_eletronica]x" size 19 color "#ffffff"

                        null height 6

                        text "🔧 MONTAGEM RÁPIDA (CRAFTING):" size 20 bold True color "#ffcc00"

                        viewport:

                            scrollbars "vertical"

                            mousewheel True

                            draggable True

                            ysize 380

                            vbox:

                                spacing 8

                                frame:

                                    xfill True background "#242c3d" padding (10, 8)

                                    vbox:

                                        spacing 3

                                        text "⚡ Montar Dispositivo de Choque" size 16 bold True color "#ffffff"

                                        text "1x Sucata + 1x Giz (Possui: [dispositivo_choque])" size 13 color "#aaaaaa"

                                        if sucata_eletronica >= 1 and giz_protecao >= 1:

                                            textbutton "🛠️ COMBINAR PEÇAS" action [

                                                SetVariable("sucata_eletronica", sucata_eletronica - 1),

                                                SetVariable("giz_protecao", giz_protecao - 1),

                                                SetVariable("dispositivo_choque", dispositivo_choque + 1),

                                                Notify("⚡ Dispositivo de Choque Rúnico montado com sucesso!")

                                            ] text_size 15 text_color "#00ffcc"

                                        else:

                                            text "Materiais insuficientes" size 13 color "#ff5555"

                                frame:

                                    xfill True background "#242c3d" padding (10, 8)

                                    vbox:

                                        spacing 3

                                        text "🧪 Montar Filtro Rúnico de Bolso" size 16 bold True color "#ffffff"

                                        text "1x Sucata + 1x Giz (Possui: [filtro_runico])" size 13 color "#aaaaaa"

                                        if sucata_eletronica >= 1 and giz_protecao >= 1:

                                            textbutton "🛠️ COMBINAR PEÇAS" action [

                                                SetVariable("sucata_eletronica", sucata_eletronica - 1),

                                                SetVariable("giz_protecao", giz_protecao - 1),

                                                SetVariable("filtro_runico", filtro_runico + 1),

                                                Notify("🧪 Filtro Rúnico de Bolso montado!")

                                            ] text_size 15 text_color "#00ffcc"

                                        else:

                                            text "Materiais insuficientes" size 13 color "#ff5555"

                                frame:

                                    xfill True background "#242c3d" padding (10, 8)

                                    vbox:

                                        spacing 3

                                        text "🩹 Consagrar Gaze Protetora" size 16 bold True color "#ffffff"

                                        text "1x Kit Curativo + 1x Giz (Possui: [gaze_consagrada])" size 13 color "#aaaaaa"

                                        if kit_curativo >= 1 and giz_protecao >= 1:

                                            textbutton "🛠️ ABENÇOAR GAZE" action [

                                                SetVariable("kit_curativo", kit_curativo - 1),

                                                SetVariable("giz_protecao", giz_protecao - 1),

                                                SetVariable("gaze_consagrada", gaze_consagrada + 1),

                                                Notify("🩹 Gaze Consagrada abençoada!")

                                            ] text_size 15 text_color "#00ffcc"

                                        else:

                                            text "Materiais insuficientes" size 13 color "#ff5555"

                                frame:

                                    xfill True background "#242c3d" padding (10, 8)

                                    vbox:

                                        spacing 3

                                        text "💉 Sintetizar Dose Estimulante" size 16 bold True color "#ffffff"

                                        text "1x Sucata + 1x Absinto (Possui: [dose_estimulante])" size 13 color "#aaaaaa"

                                        if sucata_eletronica >= 1 and dose_absinto >= 1:

                                            textbutton "🛠️ SINTETIZAR DOSE" action [

                                                SetVariable("sucata_eletronica", sucata_eletronica - 1),

                                                SetVariable("dose_absinto", dose_absinto - 1),

                                                SetVariable("dose_estimulante", dose_estimulante + 1),

                                                Notify("💉 Dose Estimulante sintetizada!")

                                            ] text_size 15 text_color "#00ffcc"

                                        else:

                                            text "Materiais insuficientes" size 13 color "#ff5555"

                                frame:

                                    xfill True background "#242c3d" padding (10, 8)

                                    vbox:

                                        spacing 3

                                        text "🛡️ Traçar Selo de Ocultação" size 16 bold True color "#ffffff"

                                        text "1x Giz de Proteção -> Reduz -15%% de Exposição" size 13 color "#aaaaaa"

                                        if giz_protecao >= 1 and exposicao > 0:

                                            textbutton "🖍️ USAR GIZ (-15%% EXPOSIÇÃO)" action [

                                                SetVariable("giz_protecao", giz_protecao - 1),

                                                SetVariable("exposicao", max(0, exposicao - 15)),

                                                Notify("As runas dissipam os vestígios de sangue (-15% Exposição).")

                                            ] text_size 15 text_color "#00ffcc"

                # COLUNA 3: Itens-Chave e Relíquias da História

                frame:

                    xysize (460, 700)

                    background "#1a202c"

                    padding (20, 20)

                    vbox:

                        spacing 15

                        text "🗝️ RELÍQUIAS E DOCUMENTOS" size 22 bold True color "#ff99cc"

                        if tem_partitura_runica:

                            text "🎼 Partitura Rúnica: Obtida" size 18 color "#66ff66"

                        else:

                            text "🎼 Partitura Rúnica: Não encontrada" size 18 color "#777777"

                        if tem_relicario_sangue:

                            text "🏺 Relicário de Sangue Puro: Obtido" size 18 color "#66ff66"

                        else:

                            text "🏺 Relicário de Sangue Puro: No Cofre" size 18 color "#777777"

                        if tem_chave_contencao:

                            text "🗝️ Chave de Contenção: Obtida" size 18 color "#66ff66"

                        else:

                            text "🗝️ Chave de Contenção: Com Elara" size 18 color "#777777"

                        if ritual_corte_vinculo_desbloqueado:

                            text "📜 Grimório do Corte do Vínculo: Copiado" size 18 color "#66ff66"

                        else:

                            text "📜 Grimório do Corte do Vínculo: Bloqueado" size 18 color "#777777"

                        if rumor_loira_banheiro:

                            text "🪞 Rumor da Loira do Banheiro: Descoberto" size 18 color "#ffcc00"

                        else:

                            text "🪞 Rumor da Loira do Banheiro: Desconhecido" size 18 color "#777777"

                        null height 20

                        textbutton "👤 Ver Estado de Victor e Afetos" action ShowMenu("status_victor_pause") text_size 20 text_color "#88ccff"

# ==============================================================================

# 3. TELA DO MAPA TÁTICO INTERATIVO EXPANDIDO (12 ÁREAS: 7 SUPERFÍCIE + 5 SUBSOLO)

# ==============================================================================

# ==============================================================================
# TRANSFORMS E ESTILOS DINÂMICOS DO MAPA (ANIMAÇÕES NATIVAS DO REN'PY)
# ==============================================================================

# ==============================================================================
# TRANSFORMS E ESTILOS DINÂMICOS DO MAPA TÁTICO (ARQUITETURA GÓTICA NATIVA)
# ==============================================================================

transform mapa_camera_viva:
    subpixel True
    zoom 1.04 xalign 0.5 yalign 0.5
    block:
        ease 7.0 xalign 0.47 yalign 0.53 zoom 1.06
        ease 7.0 xalign 0.53 yalign 0.47 zoom 1.04
        repeat

transform mapa_filtro_subsolo:
    subpixel True
    matrixcolor TintMatrix("#2a3b5c") * BrightnessMatrix(-0.22) * ContrastMatrix(1.25)
    zoom 1.06 xalign 0.5 yalign 0.5
    block:
        ease 8.0 xalign 0.48 yalign 0.52
        ease 8.0 xalign 0.52 yalign 0.48
        repeat

transform pino_mapa_anim:
    subpixel True
    on idle:
        easein 0.15 zoom 1.0 yoffset 0
    on hover:
        easein 0.15 zoom 1.08 yoffset -5

transform alerta_marco_pulsante:
    alpha 1.0
    ease 0.5 alpha 0.3
    ease 0.5 alpha 1.0
    repeat

transform painel_dock_entrada:
    subpixel True
    on show:
        alpha 0.0 yoffset 15
        easeout 0.2 alpha 1.0 yoffset 0

# Animação tática de passada / investigação estilo Black Survival (pacing cadenciado e atmosférico)
transform bs_investigar_passo:
    subpixel True
    xalign 0.5 yalign 0.5
    xanchor 0.5 yanchor 0.5
    # Passo firme à frente com leve inclinação de corpo (0.24s)
    easeout_cubic 0.24 zoom 1.08 yoffset 12
    # Breve retenção de foco / vasculhar na penumbra (0.08s)
    pause 0.08
    # Retorno amortecido e elegante à postura inicial (0.26s)
    easein_quad 0.26 zoom 1.00 yoffset 0

default info_local_hover = None

init python:
    def heroina_revelada_no_mapa(heroina_id):
        """
        Determina se o ícone e localização da heroína aparecem no mapa tático.
        - Estágio 1 (Conhecidos / Suspeita): Ocultos. Victor não sabe a rotina delas.
        - Descoberta Temporária: 'Sondar Rumores dos Corredores' com figurantes (mobs)
          revela o paradeiro apenas naquele período (tag [RUMOR]).
        - Desbloqueio Permanente (Recompensa de Médio Prazo): Exige Estágio 2 de relacionamento
          ou marcos profundos de lealdade/pacto/vínculo, recompensando a dedicação do jogador.
        """
        # 1. Rumores temporários obtidos de figurantes (mobs) no período atual
        if getattr(store, "rumores_heroina_periodo", {}).get(heroina_id, False):
            return True, True

        # 2. Desbloqueio Permanente por Vínculo Profundo (Estágio 2+ / Confiança Conquistada)
        if heroina_id == "lility":
            vinculo = getattr(store, "vinculo_sangue_lility", 0)
            estagio = getattr(store, "estagio_mestra", 1)
            # Lility: Requer Estágio 2 (Marco 1 concluído no Piano com Afeto 8+) ou Vínculo Primordial 35+
            if estagio >= 2 or vinculo >= 35:
                return True, False

        elif heroina_id == "emilia":
            st = getattr(store, "status_emilia", None)
            duvida = st.duvida if st else 0
            estagio = getattr(store, "estagio_emilia", 1)
            pacto = getattr(store, "pacto_emilia_ativo", False)
            # Emília: Requer Estágio 2 (Marco 1 concluído na Biblioteca) ou Pacto Sagrado com Dúvida <= 2
            if estagio >= 2 or (pacto and duvida <= 2):
                return True, False

        elif heroina_id == "elara":
            st = getattr(store, "status_elara", None)
            duvida = st.duvida if st else 0
            estagio = getattr(store, "estagio_elara", 1)
            subjugada = getattr(store, "elara_subjugada_no_cofre", False)
            relatorio = getattr(store, "relatorio_gremio_obtido", False)
            afeto_el = getattr(store, "afeto_elara", 0)
            # Elara: Requer Estágio 2, Subjugação no Cofre, ou Estágio 1 maduro (Relatório + Dúvida <= 1 + Afeto >= 8)
            if estagio >= 2 or subjugada:
                return True, False
            if relatorio and duvida <= 1 and afeto_el >= 8:
                return True, False

        elif heroina_id == "valeria":
            estagio = getattr(store, "estagio_valeria", 1)
            divida_paga = getattr(store, "divida_fundao_paga", False)
            afeto_v = getattr(store, "afeto_valeria", 0)
            safra = getattr(store, "safra_rara_valeria", False)
            # Valéria: Requer Estágio 2, Safra Rara Ativa, ou Afeto 8+ com Dívida do Fundão Liquidada
            if estagio >= 2 or safra:
                return True, False
            if afeto_v >= 8 and divida_paga:
                return True, False

        return False, False

    def obter_dados_pino_mapa(id_local):
        """
        Retorna dinamicamente: (cor_borda, cor_fundo, tags_extras, texto_climax, tem_marco)
        de acordo com presença de heroína, bloqueio metroidvania ou clímax de caso WOH.
        """
        presenca_txt = ""
        cor_borda = "#8a7344" # Dourado gótico envelhecido padrão
        cor_fundo = "#0e111ae6"
        tem_marco = False

        loc_m = getattr(store, "loc_mestra", "")
        loc_e = getattr(store, "loc_emilia", "")
        loc_el = getattr(store, "loc_elara", "")
        loc_v = getattr(store, "loc_valeria", "")

        vis_m, rum_m = heroina_revelada_no_mapa("lility")
        vis_e, rum_e = heroina_revelada_no_mapa("emilia")
        vis_el, rum_el = heroina_revelada_no_mapa("elara")
        vis_v, rum_v = heroina_revelada_no_mapa("valeria")

        if id_local == loc_m and id_local == loc_e and vis_m and vis_e:
            cor_borda = "#ffd700"
            cor_fundo = "#2a1e05f0"
            presenca_txt = f"⚡ Emília & {nome_display_mestra} presentes!"
            tem_marco = verificar_marco_disponivel("lility") or verificar_marco_disponivel("emilia")
        elif id_local == loc_m and vis_m:
            cor_borda = "#ff2244"
            cor_fundo = "#2d0912f0"
            presenca_txt = f"🔍 [RUMOR] {nome_display_mestra} avistada" if rum_m else f"🩸 {nome_display_mestra} presente"
            tem_marco = verificar_marco_disponivel("lility")
        elif id_local == loc_e and vis_e:
            cor_borda = "#4da6ff"
            cor_fundo = "#0d1f38f0"
            presenca_txt = "🔍 [RUMOR] Emília avistada" if rum_e else "✝️ Emília presente"
            tem_marco = verificar_marco_disponivel("emilia")
        elif id_local == loc_el and vis_el:
            cor_borda = "#e6b8ff"
            cor_fundo = "#23122ef0"
            presenca_txt = "🔍 [RUMOR] Elara avistada" if rum_el else "👑 Elara presente"
            tem_marco = verificar_marco_disponivel("elara")
        elif id_local == loc_v and vis_v and id_local in ["caldeiras", "sala_caldeiras", "bar_fada_verde"]:
            cor_borda = "#2eb82e"
            cor_fundo = "#0e2616f0"
            presenca_txt = "🔍 [RUMOR] Valéria avistada" if rum_v else "💰 Valéria presente"
            tem_marco = verificar_marco_disponivel("valeria")

        # Verifica se há Clímax de Caso (3/3 pistas) pronto no local
        climax_txt = ""
        if "loira_banheiro" in MISTERIOS_ACADEMIA and id_local == "banheiro_abandonado" and MISTERIOS_ACADEMIA["loira_banheiro"].pistas_coletadas >= 3 and not getattr(store, "derrotou_loira_banheiro", False):
            cor_borda = "#ff0055"
            climax_txt = "⚠️ CLÍMAX: A LOIRA DO ESPELHO!"
        elif "hachishaku" in MISTERIOS_ACADEMIA and id_local == "cemiterio_nevoa" and MISTERIOS_ACADEMIA["hachishaku"].pistas_coletadas >= 3 and not getattr(store, "derrotou_hachishaku", False) and getattr(store, "periodo", "") == "Noite":
            cor_borda = "#ff0055"
            climax_txt = "⚠️ CLÍMAX: HACHISHAKU-SAMA!"
        elif "lote_necrotico" in MISTERIOS_ACADEMIA and id_local in ["caldeiras", "sala_caldeiras"] and MISTERIOS_ACADEMIA["lote_necrotico"].pistas_coletadas >= 3 and not getattr(store, "caso_lote_necrotico_resolvido", False):
            cor_borda = "#ff0055"
            climax_txt = "⚠️ CLÍMAX: LOTE NECRÓTICO!"
        elif "partitura_carnal" in MISTERIOS_ACADEMIA and id_local == "sala_musica" and MISTERIOS_ACADEMIA["partitura_carnal"].pistas_coletadas >= 3 and not getattr(store, "caso_partitura_resolvido", False):
            cor_borda = "#ff0055"
            climax_txt = "⚠️ CLÍMAX: PARTITURA CARNAL!"
        elif "inquerito_inquisicao" in MISTERIOS_ACADEMIA and id_local == "salao_gremio" and MISTERIOS_ACADEMIA["inquerito_inquisicao"].pistas_coletadas >= 3 and not getattr(store, "caso_inquerito_resolvido", False) and getattr(store, "periodo", "") in ["Tarde", "Noite"]:
            cor_borda = "#ff0055"
            climax_txt = "⚠️ CLÍMAX: ARQUIVOS DA INQUISIÇÃO!"
        elif id_local == "biblioteca" and getattr(store, "periodo", "") == "Noite" and getattr(store, "conhece_misterio_quadros", False) and not getattr(store, "quadro_banquete_resolvido", False):
            cor_borda = "#ffaa00"
            climax_txt = "🖼️ ANOMALIA: O BANQUETE DE 1889!"

        return cor_borda, cor_fundo, presenca_txt, climax_txt, tem_marco

# Tela Auxiliar de Pino Estilizado com Moldura de Borda Dupla Gótica
screen componente_pino_mapa(id_local, xpos_val, ypos_val, icone, titulo_curto, subtitulo_curto, titulo_completo, desc_drops, desc_lore, trancado=False, msg_trancado=""):
    $ cor_borda, cor_fundo, presenca_txt, climax_txt, tem_marco = obter_dados_pino_mapa(id_local)
    $ borda_final = "#555566" if trancado else cor_borda
    $ fundo_final = "#111217cc" if trancado else cor_fundo

    button:
        xpos xpos_val ypos ypos_val
        at pino_mapa_anim
        background borda_final
        hover_background "#00ffcc"
        padding (2, 2)
        hovered SetVariable("info_local_hover", (
            ("🔒 " if trancado else f"{icone} ") + titulo_completo,
            msg_trancado if trancado else desc_drops,
            (f"{presenca_txt}  •  " if presenca_txt else "") + (climax_txt if climax_txt else desc_lore),
            tem_marco or bool(climax_txt),
            borda_final
        ))
        unhovered SetVariable("info_local_hover", None)
        action [SetVariable("local_atual", id_local), SetVariable("deslocando_pelo_mapa", True), Hide("mapa_tatico_escola"), Jump("entrar_local_exploracao_bs")]

        frame:
            background fundo_final
            padding (12, 7)
            vbox:
                spacing 2
                hbox:
                    spacing 7
                    yalign 0.5
                    text (f"🔒 {titulo_curto}" if trancado else f"{icone} {titulo_curto}") substitute False:
                        size 16 bold True
                        color ("#888899" if trancado else "#ffffff")
                        outlines [(1, "#000000", 0, 0)]

                    if presenca_txt:
                        text "●" size 16 color cor_borda yalign 0.5
                    if tem_marco or climax_txt:
                        text "🌟" size 15 yalign 0.5 at alerta_marco_pulsante

                # Linha compacta de status sob o nome do prédio
                if climax_txt:
                    text climax_txt size 11 bold True color "#ff4466" outlines [(1, "#000000", 0, 0)] substitute False
                elif presenca_txt:
                    text presenca_txt size 11 bold True color "#ffd700" outlines [(1, "#000000", 0, 0)] substitute False
                else:
                    text subtitulo_curto size 11 color ("#666677" if trancado else "#99aabb") outlines [(1, "#000000", 0, 0)] substitute False

screen mapa_tatico_escola():
    modal True
    zorder 90

    # --- 1. FUNDO COM VÍDEOS EM LOOPING DINÂMICO & CLIMA ---
    if aba_mapa_subsolo:
        add "mapa animado subsolo"
    else:
        $ eh_chuvoso = verificar_esta_chovendo()
        if eh_chuvoso:
            add "mapa animado chuva"
        elif clima_diario_id == "neblina_noturna" or (periodo == "Noite" and ruina_cain >= 30):
            add "mapa animado neblina noite"
        elif periodo == "Manhã":
            add "mapa animado manha"
        elif periodo == "Tarde":
            add "mapa animado tarde"
        else:
            add "mapa animado neblina noite"

    # Vinheta atmosférica suave
    add Solid("#05060b44")

    # --- 2. HEADER TÁTICO EM 2 NÍVEIS (SEM CONFLITO E SEM CORTAR NAS BORDAS) ---
    frame:
        xalign 0.5 yalign 0.0
        xfill True
        background "#080a10f2"
        padding (28, 10)
        vbox:
            spacing 6
            # NÍVEL 1: Status Vitais + Relógio + Atalhos da Central Feniks
            hbox:
                xfill True
                hbox:
                    spacing 16 yalign 0.5
                    text "📅 DIA [dia_atual] ([periodo!u])" size 17 bold True color "#ffffff"
                    if periodo == "Noite":
                        text "🔴 ZONA VERMELHA" size 16 bold True color "#ff3344"
                    elif periodo == "Tarde":
                        text "🟡 ZONA AMARELA" size 16 bold True color "#ffcc33"
                    else:
                        text "🔵 ZONA AZUL" size 16 bold True color "#33aaff"

                    $ cor_visitas_mapa = "#00ffcc" if visitas_restantes_periodo >= 2 else ("#ffcc00" if visitas_restantes_periodo == 1 else "#ff3344")
                    text "⏳ Visitas: [visitas_restantes_periodo]/[limite_visitas_periodo]" size 16 bold True color cor_visitas_mapa
                    text "👣 Passos: [passos_restantes_periodo]/3" size 16 color "#88e0ff"
                    text "❤️ [hp_jogador]/[hp_jogador_max]" size 16 color "#ffffff"
                    text "🩸 Sede: [fome_sangue]%" size 16 color "#ff6666"
                    text "🧠 Hum: [humanidade]" size 16 color "#88ccff"
                    text "🎭 Exp: [exposicao]%" size 16 color "#cc88ff"
                    text "💰 $[dinheiro_jogador]" size 16 color "#66ff66"
                    text "⚡ DOOM: [ruina_cain]%" size 16 bold True color ("#ff2244" if ruina_cain >= 50 else "#ffcc00")

                hbox:
                    xalign 1.0 yalign 0.5 spacing 14
                    textbutton "👤 STATUS":
                        action ShowMenu("central_tatica_feniks", "status")
                        text_size 15 text_bold True text_color "#00ffcc" text_hover_color "#ffffff"
                    textbutton "🎒 ITENS":
                        action ShowMenu("central_tatica_feniks", "inventario")
                        text_size 15 text_bold True text_color "#ffcc00" text_hover_color "#ffffff"
                    textbutton "📋 CASOS":
                        action ShowMenu("quadro_misterios_woh")
                        text_size 15 text_bold True text_color "#ff99ff" text_hover_color "#ffffff"
                    textbutton "📜 DÍVIDAS":
                        action ShowMenu("central_tatica_feniks", "dividas")
                        text_size 15 text_bold True text_color "#ff9933" text_hover_color "#ffffff"
                    if config.developer:
                        textbutton "🛠️ DEBUG":
                            action Show("painel_debug_interno")
                            text_size 15 text_bold True text_color "#00ff88" text_hover_color "#ffffff"

            # Linha divisória dourada sutil
            frame:
                xfill True
                ysize 1
                background "#8a734455"
                padding (0, 0)

            # NÍVEL 2: Seletor de Planta (Superfície vs Subsolo) + Clima do Dia
            hbox:
                xfill True
                hbox:
                    spacing 20 yalign 0.5
                    textbutton ("▣ 🏛️ PLANTA I: SUPERFÍCIE (11 SETORES)" if not aba_mapa_subsolo else "▢ 🏛️ PLANTA I: SUPERFÍCIE (11 SETORES)"):
                        action [SetVariable("aba_mapa_subsolo", False), SetVariable("info_local_hover", None)]
                        text_size 18 text_bold True
                        text_color ("#00ffcc" if not aba_mapa_subsolo else "#777788")
                        text_hover_color "#ffffff"

                    text "│" size 18 color "#444455" yalign 0.5

                    textbutton ("▣ 🕳️ PLANTA II: SUBSOLO & EXTERIOR (6 SETORES)" if aba_mapa_subsolo else "▢ 🕳️ PLANTA II: SUBSOLO & EXTERIOR (6 SETORES)"):
                        action [SetVariable("aba_mapa_subsolo", True), SetVariable("info_local_hover", None)]
                        text_size 18 text_bold True
                        text_color ("#ff4466" if aba_mapa_subsolo else "#777788")
                        text_hover_color "#ffffff"

                hbox:
                    xalign 1.0 yalign 0.5 spacing 18
                    text "[clima_diario_icone] [clima_diario_nome]" size 15 color "#ffd700" yalign 0.5
                    if any([verificar_marco_disponivel("lility"), verificar_marco_disponivel("emilia"), verificar_marco_disponivel("valeria"), verificar_marco_disponivel("elara")]):
                        text "🌟 EVENTO DE MARCO DISPONÍVEL!" size 15 bold True color "#ffff00" yalign 0.5 at alerta_marco_pulsante

    # ==========================================================================
    # 3. PINOS ESTILIZADOS DA SUPERFÍCIE (Ancorados sobre os Prédios Reais)
    # ==========================================================================
    if not aba_mapa_subsolo:

        # 1. Gabinete do Grêmio & Diretoria (Torre Central do Relógio)
        use componente_pino_mapa(
            "salao_gremio", 820, 145, "⚖️", "Gabinete do Grêmio", "1º Andar Nobre • Vigilância",
            "Gabinete do Grêmio & Diretoria",
            "Drops: Reduzir Exposição (-15%), Relatórios ($120-$240), Caso 5: Arquivos Mortos",
            "Sede política e administrativa do conselho estudantil e da diretoria."
        )

        # 2. Biblioteca Gótica & Galeria dos Esquecidos (Catedral Oeste)
        use componente_pino_mapa(
            "biblioteca", 320, 235, "📚", "Biblioteca Gótica", "2º Andar • Pesquisa & Quadros",
            "Biblioteca Gótica & Galeria dos Esquecidos",
            "Drops: Giz Rúnico, Conhecimento Oculto, Pistas da Partitura Carnal",
            "Acervo secular de tomos encadernados e arquivos históricos da Academia • Contém o quadro 'O Banquete de 1889'."
        )

        # 3. Sala de Música Interditada (Conservatório Leste)
        use componente_pino_mapa(
            "sala_musica", 1280, 270, "🎹", "Sala de Música", "2º Andar Leste • Teclas & Vitrais",
            "Sala de Música Interditada",
            "Drops: Transe de Sangue (+60% a +100% Sede), Caso 4: Partitura Carnal",
            "Conservatório abandonado sob vitrais antigos. O som de teclas ecoa ao longe."
        )

        # 4. Pátio das Árvores Centenárias (Bosque Interno)
        use componente_pino_mapa(
            "patio_arvore", 800, 340, "🌳", "Pátio das Árvores", "Jardim Norte • Carvalhos",
            "Pátio dos Carvalhos Centenários",
            "Drops: Giz Rúnico, Moedas Perdidas, Kit Médico, Pistas da Mulher Gigante",
            "Alameda sombria entre a Catedral e a encosta do Cemitério."
        )

        # 5. Sala de Ocultismo & Alquimia (Ala Oeste)
        use componente_pino_mapa(
            "sala_ocultismo", 140, 410, "🕯️", "Clube de Ocultismo", "2º Andar Oeste • Alquimia",
            "Sala de Ocultismo & Alquimia",
            "Drops: +1 Conhecimento Oculto, +1 Intelecto, Giz de Proteção Rúnico",
            "Antigo laboratório vitoriano usado por veteranos esotéricos."
        )

        # 6. Pátio Central & Fonte Gótica (Exatamente sobre a Fonte do Claustro)
        use componente_pino_mapa(
            "patio_fonte", 980, 520, "⛲", "Pátio & Fonte Gótica", "Claustro Central • Coleta",
            "Pátio Central & Fonte Gótica",
            "Drops: Rumores dos Alunos (Uniforme Preto), Moedas, Pistas",
            "Coração social da academia • Posto da Campanha de Doação de Sangue."
        )

        # 7. Banheiro Abandonado (Ala Leste Interditada)
        use componente_pino_mapa(
            "banheiro_abandonado", 1380, 545, "🪞", "Banheiro 2º Andar", "Ala Interditada • Espelho",
            "Banheiro Abandonado do 2º Andar",
            "Drops: Caso 1: O Enigma da Loira do Banheiro (-12% DOOM), Giz Rúnico",
            "Sanitário interditado onde o espelho trincado sangra à meia-noite.",
            trancado=(not desbloqueou_banheiro_abandonado),
            msg_trancado="🔒 BLOQUEADO: Investigue relatos sobre desaparecimentos ou ouça rumores para liberar."
        )

        # 8. Dormitório de Victor (Pavilhão de Tijolos à Esquerda)
        use componente_pino_mapa(
            "dormitorio", 110, 620, "🛏️", "Dormitório de Victor", "3º Andar • Refúgio Seguro",
            "Dormitório de Victor Vane (Refúgio Seguro)",
            "Ações: Descansar (+25 HP / Curar Sequelas), Consultar Regras (0 Passos)",
            "🔵 ZONA TOTALMENTE SEGURA: Refúgio inviolável dia, tarde e noite. Não consome passos."
        )

        # 9. Portões & Praça Monumental (Sobre os Portões de Ferro)
        use componente_pino_mapa(
            "portoes_praca", 640, 685, "⛩️", "Portões da Academia", "Fachada Sul • Ronda Policial",
            "Portões de Ferro & Praça Monumental",
            "Drops: Suborno Policial (-20% Exposição), Caso 2: Hachishaku-sama",
            "Limite físico do Grilhão de Sangue • Viaturas e neblina noturna."
        )

        # 10. Rua Externa & Avenida do Campus (Asfalto Inferior Esquerdo)
        use componente_pino_mapa(
            "rua_portao", 310, 815, "🚗", "Avenida do Campus", "Perímetro Urbano • Bonde",
            "Rua Externa & Avenida do Campus",
            "Drops: Sucata Eletrônica, Dinheiro ($60-$130), Absinto, Curativos",
            "Calçadas molhadas e comércio fechado além das muralhas góticas."
        )

        # 11. Enfermaria da Academia (Ala Médica • Dra. Clara Vance)
        use componente_pino_mapa(
            "enfermaria", 530, 440, "🏥", "Enfermaria do Campus", "Ala Médica • Dra. Clara",
            "Enfermaria da Academia São Cipriano",
            "Ações: Consultar Dra. Clara, Curar Sequelas, Bolsas Filtradas ($100), Kits Médicos",
            "Posto oficial da Campanha de Saúde Comunitária e gerência do Rebanho Seguro."
        )

    # ==========================================================================
    # 4. PINOS ESTILIZADOS DO SUBSOLO & EXTERIOR OCULTO (6 SETORES)
    # ==========================================================================
    else:

        # 11. Cemitério Antigo & Bosque da Névoa (Norte / Acesso Superior)
        use componente_pino_mapa(
            "cemiterio_nevoa", 280, 180, "🪦", "Cemitério da Névoa", "Colina Norte • Necrópole",
            "Cemitério Antigo & Bosque da Névoa",
            "Drops: Caso 2: A Mulher de Oito Pés (-12% DOOM), Giz, Sangue Adulterado",
            "Mausoléu da família von Karsten • Alçapão para as Catacumbas."
        )

        # 12. Mercado Negro das Caldeiras (Ala de Contrabando Oeste)
        use componente_pino_mapa(
            "caldeiras", 220, 560, "🛒", "Mercado Negro", "Subsolo 1 • Loja & Bancada",
            "Mercado Negro das Caldeiras",
            "Drops: Loja de Sangue Filtrado, Passe da Fada Verde, Bancada de Crafting",
            "Esconderijo iluminado por tochas de fogo azul alquímico.",
            trancado=(not desbloqueou_mercado_negro or not mercado_negro_aberto_hoje),
            msg_trancado=("🔒 FECHADO HOJE: O Mercado suspendeu atividades hoje por precaução." if desbloqueou_mercado_negro else f"🔒 OCULTO: Vasculhe as Caldeiras Centrais ({investigacoes_caldeiras}/5 buscas) para achar a passagem.")
        )

        # 13. Caldeiras Centrais da Academia (Centro / Máquinas Térmicas)
        use componente_pino_mapa(
            "sala_caldeiras", 720, 460, "🔥", "Caldeiras Centrais", "Subsolo 1 • Fornalhas a Vapor",
            "Caldeiras Centrais da Academia",
            "Drops: Sucata Eletrônica, Sangue Adulterado, Caso 3: O Lote Necrótico",
            "Coração térmico da escola • Vasculhe 5x para descobrir o Mercado Negro."
        )

        # 14. Bar da Fada Verde (Speakeasy / Ala Sul Subterrânea)
        use componente_pino_mapa(
            "bar_fada_verde", 800, 680, "🧚", "Bar da Fada Verde", "Subsolo 1 • Taverna Oculta",
            "Bar da Fada Verde (Speakeasy Subterrâneo)",
            "Drops: Doses de Absinto Esmeralda, Dinheiro, Rumores do Conselho",
            "Reduto boêmio de luzes neon verde e contrabandistas.",
            trancado=(not tem_passe_fada_verde),
            msg_trancado="🔒 BARRADO: Obtenha o Passe Clandestino do Fundão para ter acesso."
        )

        # 15. Catacumbas & Esgoto Colonial (Ala Leste / Galerias de Ossos)
        use componente_pino_mapa(
            "catacumbas", 1300, 280, "⚔️", "Catacumbas & Esgoto", "Subsolo 2 • Zona de Caça",
            "Catacumbas & Esgoto Colonial",
            "Drops: Fragmentos da Chave da Cripta (1 a 3), Espólios de Combate, Sangue",
            "🔴 Zona Letal Contínua • Galerias de ossos sobre o sarcófago ancestral."
        )

        # 16. Cripta Ancestral & Cela de Nora (Câmara de Contenção Mais Profunda)
        use componente_pino_mapa(
            "cripta_cofre", 1400, 600, "🔒", f"Cripta & Cofre ({fragmentos_chave_cripta}/3)", "Subsolo Profundo • Cobaia 31",
            "Cripta Ancestral & Cela de Vidro (Nora)",
            "Drops: Encontro com Nora (Cobaia 31), Chave dos Dutos, Cofre dos Fundadores",
            "Câmara octogonal de obsidiana que guarda os segredos mais sombrios.",
            trancado=(not desbloqueou_cripta_cofre),
            msg_trancado=f"🔒 SELO INVIOLÁVEL: Encontre os 3 Fragmentos Rúnicos nas Catacumbas ({fragmentos_chave_cripta}/3 obtidos)."
        )

    # ==========================================================================
    # 5. DOCK TÁTICO INFERIOR (PAINEL DE INSPEÇÃO COM BORDA DINÂMICA)
    # ==========================================================================
    if info_local_hover is not None:
        frame:
            at painel_dock_entrada
            xalign 0.02 yalign 0.96
            xsize 1050
            background info_local_hover[4]
            padding (2, 2)
            frame:
                xfill True
                background "#090b12f6"
                padding (20, 12)
                vbox:
                    spacing 4
                    hbox:
                        spacing 14
                        text info_local_hover[0] size 21 bold True color "#ffffff" substitute False
                        if len(info_local_hover) > 3 and info_local_hover[3]:
                            text "🌟 [[EVENTO / ANOMALIA ATIVA NESTE SETOR!]]" size 15 bold True color "#ffff00" yalign 0.5 at alerta_marco_pulsante
                    text info_local_hover[1] size 15 color "#66e0ff" substitute False
                    text info_local_hover[2] size 14 color "#cccccc" substitute False
    else:
        frame:
            xalign 0.02 yalign 0.96
            xsize 1050
            background "#8a734488"
            padding (1, 1)
            frame:
                xfill True
                background "#090b12dd"
                padding (18, 12)
                hbox:
                    spacing 15
                    text "🧭 DOSSIÊ DE NAVEGAÇÃO:" size 16 bold True color "#d4af37" yalign 0.5
                    text "Aponte para qualquer setor para inspecionar recursos, travas e presenças. Clique para deslocar Victor." size 15 color "#bbbbbb" yalign 0.5

    # Botões de Ação Rápida no Canto Inferior Direito
    hbox:
        xalign 0.98 yalign 0.96
        spacing 12

        $ _vis_m_quarto, _ = heroina_revelada_no_mapa("lility")
        $ _vis_e_quarto, _ = heroina_revelada_no_mapa("emilia")
        $ _m_no_quarto = (loc_mestra == "dormitorio" and _vis_m_quarto)
        $ _e_no_quarto = (loc_emilia == "dormitorio" and _vis_e_quarto)

        button:
            at pino_mapa_anim
            background ("#ffd700" if (_e_no_quarto and _m_no_quarto) else ("#4da6ff" if _e_no_quarto else ("#ff2244" if _m_no_quarto else "#3b4d77"))) hover_background "#00ffcc"
            padding (2, 2)
            action [SetVariable("local_atual", "dormitorio"), SetVariable("deslocando_pelo_mapa", True), Hide("mapa_tatico_escola"), Jump("entrar_local_exploracao_bs")]
            frame:
                background "#101624f2"
                padding (16, 12)
                if _e_no_quarto and _m_no_quarto:
                    text f"🛏️ Quarto (⚡ Emília & {nome_display_mestra})" size 16 bold True color "#ffd700"
                elif _e_no_quarto:
                    text "🛏️ Quarto (✝️ Emília)" size 16 bold True color "#88ccff"
                elif _m_no_quarto:
                    text f"🛏️ Quarto (🩸 {nome_display_mestra})" size 16 bold True color "#ff7788"
                else:
                    text "🛏️ Ir ao Quarto" size 16 bold True color "#88ccff"

        button:
            at pino_mapa_anim
            background "#882233" hover_background "#ff4466"
            padding (2, 2)
            action [Hide("mapa_tatico_escola"), Jump("avancar_turno_mapa")]
            frame:
                background "#240a10f2"
                padding (18, 12)
                text "⏳ Encerrar [periodo]" size 16 bold True color "#ffcccc"

screen hud_exploracao_bs():

    zorder 75

    frame:

        xalign 0.5 yalign 0.93

        background "#111116f2"

        padding (28, 16)

        hbox:

            spacing 30

            if local_atual != "dormitorio":
                textbutton "👣 VASCULHAR / DAR PASSO ([passos_restantes_periodo])":
                    text_size 22 text_color "#ffcc00" text_hover_color "#ffffff"
                    action Jump("investigar_passo_bs")
            else:
                # Interações Exclusivas com Heroínas no Dormitório (Zona Segura - 0 Passos)
                if loc_emilia == "dormitorio" and loc_mestra == "dormitorio":
                    textbutton "⚡ O EMBATE DO DORMITÓRIO (EMÍLIA & [nome_display_mestra!u])":
                        text_size 19 text_bold True text_color "#ffd700" text_hover_color "#ffffff"
                        action [Hide("hud_exploracao_bs"), Jump("evento_embate_dormitorio_lility_emilia")]
                    textbutton "✝️ CONVERSAR COM EMÍLIA (NO QUARTO)":
                        text_size 18 text_bold True text_color "#88ccff" text_hover_color "#ffffff"
                        action [Hide("hud_exploracao_bs"), Jump("menu_encontro_emilia_dormitorio")]
                    textbutton "🩸 APROXIMAR-SE DE [nome_display_mestra!u] (NO QUARTO)":
                        text_size 18 text_bold True text_color "#ff7788" text_hover_color "#ffffff"
                        action [Hide("hud_exploracao_bs"), Jump("menu_encontro_lility_dormitorio")]
                elif loc_emilia == "dormitorio":
                    textbutton "✝️ CONVERSAR COM EMÍLIA (NO QUARTO)":
                        text_size 20 text_bold True text_color "#88ccff" text_hover_color "#ffffff"
                        action [Hide("hud_exploracao_bs"), Jump("menu_encontro_emilia_dormitorio")]
                elif loc_mestra == "dormitorio":
                    textbutton "🩸 APROXIMAR-SE DE [nome_display_mestra!u] (NO QUARTO)":
                        text_size 20 text_bold True text_color "#ff4466" text_hover_color "#ffffff"
                        action [Hide("hud_exploracao_bs"), Jump("menu_encontro_lility_dormitorio")]

                $ _qtd_p = getattr(store, "passos_restantes_periodo", 3)
                if _qtd_p >= 3:
                    textbutton "🛏️ REPOUSO PROFUNDO (+45 HP | 3 Passos)":
                        text_size 20 text_color "#88ffcc" text_hover_color "#ffffff"
                        action Jump("acao_descansar_dormitorio")
                elif _qtd_p == 2:
                    textbutton "🛏️ DESCANSO LONGO (+30 HP | 2 Passos)":
                        text_size 20 text_color "#88ccff" text_hover_color "#ffffff"
                        action Jump("acao_descansar_dormitorio")
                elif _qtd_p == 1:
                    textbutton "🛏️ COCHILO BREVE (+15 HP | 1 Passo)":
                        text_size 20 text_color "#e6b8ff" text_hover_color "#ffffff"
                        action Jump("acao_descansar_dormitorio")
                else:
                    textbutton "🛏️ COLAPSO POR EXAUSTÃO (+5 HP | Esgotado)":
                        text_size 20 text_color "#ff8888" text_hover_color "#ffffff"
                        action Jump("acao_descansar_dormitorio")
                textbutton "📖 CONSULTAR DIÁRIO & REGRAS":
                    text_size 20 text_color "#e6b8ff" text_hover_color "#ffffff"
                    action Jump("consultar_regras_dormitorio")
                if "obter_ecos_sangue_ativos" in globals() and obter_ecos_sangue_ativos() and not getattr(store, "resgatou_ecos_sangue_partida", False):
                    textbutton "🔮 ECO DE SANGUE":
                        text_size 19 text_bold True text_color "#cc88ff" text_hover_color "#ffffff"
                        action Jump("ativar_ecos_sangue_dormitorio")
            if local_atual in ["caldeiras", "sala_caldeiras"]:

                textbutton "🛠️ BANCADA DE CRAFTING":

                    text_size 20 text_color "#00ffcc" text_hover_color "#ffffff"

                    action ShowMenu("bancada_crafting")

            if local_atual in ["biblioteca", "sala_ocultismo"] and getattr(store, "tarefa_academica_pendente", False) and getattr(store, "passos_restantes_periodo", 0) > 0:
                textbutton "📚 CUMPRIR TAREFA ESCOLAR":
                    text_size 19 text_bold True text_color "#88ccff" text_hover_color "#ffffff"
                    action [Hide("hud_exploracao_bs"), Jump("acao_cumprir_tarefa_academica")]

            if local_atual == "biblioteca" and periodo == "Noite" and not getattr(store, "quadro_banquete_resolvido", False):
                textbutton "🖼️ GALERIA DOS ESQUECIDOS":
                    text_size 20 text_color "#ff4466" text_hover_color "#ffffff"
                    action [Hide("hud_exploracao_bs"), Jump("evento_galeria_quadros_anomalia")]

            if local_atual == "enfermaria":
                textbutton "💉 CONSULTAR COM ENFERMEIRA CLARA":
                    text_size 20 text_color "#77ddcc" text_hover_color "#ffffff"
                    action [Hide("hud_exploracao_bs"), Jump("acao_consultar_enfermaria")]

            if local_atual == "caldeiras":
                textbutton "🛒 MERCADO NEGRO (VALÉRIA)":
                    text_size 20 text_color "#66ff66" text_hover_color "#ffffff"
                    action [Hide("hud_exploracao_bs"), Jump("acao_mercado_negro_valeria")]

            textbutton "🎒 INVENTÁRIO":

                text_size 20 text_color "#00ffcc" text_hover_color "#ffffff"

                action ShowMenu("inventario_victor")

            if getattr(store, "visitas_restantes_periodo", 3) > 0 or local_atual == "dormitorio":
                textbutton ("🗺️ MUDAR ÁREA" if local_atual == "dormitorio" else "🗺️ MUDAR ÁREA (⏳ [visitas_restantes_periodo]x)"):
                    text_size 20 text_color "#ffffff" text_hover_color "#ff6666"
                    action Jump("abrir_mapa_tatico")
            else:
                textbutton "⏳ ENCERRAR [periodo!u] (Visitas Esgotadas)":
                    text_size 20 text_color "#ffcc00" text_hover_color "#ff4444"
                    action Jump("avancar_com_sino_academia")

            textbutton "⏳ PASSAR TURNO":

                text_size 20 text_color "#ff6666" text_hover_color "#ffffff"

                action Jump("avancar_turno_mapa")

# ==============================================================================

# 5. LOJA DO MERCADO NEGRO DE VALÉRIA E BANCADA

# ==============================================================================

screen bancada_crafting():

    tag menu

    modal True

    zorder 85

    frame:

        xalign 0.5 yalign 0.5

        xysize (1060, 720)

        background "#101620f4"

        padding (32, 24)

        vbox:

            spacing 12

            text "🛠️ BANCADA DE ENGENHARIA OCULTA & CRAFTING (CALDEIRAS)" size 26 bold True color "#00ffcc"

            # Barra de Inventário de Componentes

            frame:

                xfill True

                background "#1a2332"

                padding (16, 10)

                hbox:

                    spacing 18

                    text "⚙️ Sucata: [sucata_eletronica]" size 16 bold True color "#ffffff"

                    text "🖍️ Giz: [giz_protecao]" size 16 bold True color "#ffffff"

                    text "🩹 Kits Curativo: [kit_curativo]" size 16 bold True color "#ffffff"

                    text "🍾 Absinto: [dose_absinto]" size 16 bold True color "#ffffff"

                    text "☣️ Sangue Adulterado: [bolsa_sangue_adulterado]" size 16 color "#ffaa55"

            viewport:

                scrollbars "vertical"

                mousewheel True

                draggable True

                ysize 490

                vbox:

                    spacing 14

                    # RECEITA 1: Dispositivo de Choque Rúnico

                    frame:

                        xfill True

                        background "#182230"

                        padding (14, 12)

                        vbox:

                            spacing 5

                            hbox:

                                spacing 10

                                text "⚡ Dispositivo de Choque Rúnico" size 20 bold True color "#ffeb3b"

                                text "(Em estoque: [dispositivo_choque])" size 16 color "#88a0b0"

                            text "Custo: 1x Sucata Eletrônica + 1x Giz de Proteção" size 15 color "#a0c0d0"

                            text "Efeito em Combate: Causa 30 de Dano direto e Atordoa o inimigo, cancelando o próximo contra-ataque." size 14 italic True color "#c0c0c0"

                            if sucata_eletronica >= 1 and giz_protecao >= 1:

                                textbutton "🛠️ CONSTRUIR DISPOSITIVO DE CHOQUE":

                                    action [

                                        SetVariable("sucata_eletronica", sucata_eletronica - 1),

                                        SetVariable("giz_protecao", giz_protecao - 1),

                                        SetVariable("dispositivo_choque", dispositivo_choque + 1),

                                        Notify("⚡ Dispositivo de Choque Rúnico construído com sucesso!")

                                    ]

                                    text_size 16 text_color "#00ffcc" text_bold True

                            else:

                                text "Materiais insuficientes (Requer 1x Sucata e 1x Giz)" size 15 color "#ff5555"

                    # RECEITA 2: Filtro Rúnico de Bolso

                    frame:

                        xfill True

                        background "#182230"

                        padding (14, 12)

                        vbox:

                            spacing 5

                            hbox:

                                spacing 10

                                text "🧪 Filtro Rúnico de Bolso" size 20 bold True color "#4fc3f7"

                                text "(Em estoque: [filtro_runico])" size 16 color "#88a0b0"

                            text "Custo: 1x Sucata Eletrônica + 1x Giz de Proteção" size 15 color "#a0c0d0"

                            text "Efeito: Purifica Bolsas de Sangue Adulterado (turvo) em Sangue Filtrado Puro (+35%% Saciedade / 0 perda de Humanidade)." size 14 italic True color "#c0c0c0"

                            if sucata_eletronica >= 1 and giz_protecao >= 1:

                                textbutton "🛠️ MONTAR FILTRO RÚNICO":

                                    action [

                                        SetVariable("sucata_eletronica", sucata_eletronica - 1),

                                        SetVariable("giz_protecao", giz_protecao - 1),

                                        SetVariable("filtro_runico", filtro_runico + 1),

                                        Notify("🧪 Filtro Rúnico de Bolso montado com sucesso!")

                                    ]

                                    text_size 16 text_color "#00ffcc" text_bold True

                            else:

                                text "Materiais insuficientes (Requer 1x Sucata e 1x Giz)" size 15 color "#ff5555"

                    # RECEITA 3: Gaze Consagrada

                    frame:

                        xfill True

                        background "#182230"

                        padding (14, 12)

                        vbox:

                            spacing 5

                            hbox:

                                spacing 10

                                text "🩹 Gaze Consagrada" size 20 bold True color "#81c784"

                                text "(Em estoque: [gaze_consagrada])" size 16 color "#88a0b0"

                            text "Custo: 1x Kit de Curativos + 1x Giz de Proteção" size 15 color "#a0c0d0"

                            text "Efeito: Restaura +40 HP (Vida) e estanca ferimentos e hemorragias místicas imediatamente." size 14 italic True color "#c0c0c0"

                            if kit_curativo >= 1 and giz_protecao >= 1:

                                textbutton "🛠️ CONSAGRAR GAZE PROTETORA":

                                    action [

                                        SetVariable("kit_curativo", kit_curativo - 1),

                                        SetVariable("giz_protecao", giz_protecao - 1),

                                        SetVariable("gaze_consagrada", gaze_consagrada + 1),

                                        Notify("🩹 Gaze Consagrada preparada e abençoada!")

                                    ]

                                    text_size 16 text_color "#00ffcc" text_bold True

                            else:

                                text "Materiais insuficientes (Requer 1x Kit Curativo e 1x Giz)" size 15 color "#ff5555"

                    # RECEITA 4: Dose Estimulante Rúnica

                    frame:

                        xfill True

                        background "#182230"

                        padding (14, 12)

                        vbox:

                            spacing 5

                            hbox:

                                spacing 10

                                text "💉 Dose Estimulante Rúnica" size 20 bold True color "#ba68c8"

                                text "(Em estoque: [dose_estimulante])" size 16 color "#88a0b0"

                            text "Custo: 1x Sucata Eletrônica + 1x Dose de Absinto" size 15 color "#a0c0d0"

                            text "Efeito em Combate: Desacelera a percepção sensorial (+2.5s de timer QTE) e concede 50%% de chance de esquiva." size 14 italic True color "#c0c0c0"

                            if sucata_eletronica >= 1 and dose_absinto >= 1:

                                textbutton "🛠️ SINTETIZAR DOSE ESTIMULANTE":

                                    action [

                                        SetVariable("sucata_eletronica", sucata_eletronica - 1),

                                        SetVariable("dose_absinto", dose_absinto - 1),

                                        SetVariable("dose_estimulante", dose_estimulante + 1),

                                        Notify("💉 Dose Estimulante Rúnica sintetizada!")

                                    ]

                                    text_size 16 text_color "#00ffcc" text_bold True

                            else:

                                text "Materiais insuficientes (Requer 1x Sucata e 1x Dose de Absinto)" size 15 color "#ff5555"

            null height 6

            textbutton "🔙 Fechar Bancada" action Return() xalign 0.5 text_size 18 text_color "#ffffff" text_hover_color "#ff6666"

# 6. TELAS DE CLICK E REAÇÃO (TOUCH REACTION - ENCONTROS NO MAPA)

# ==============================================================================

# --- 6.1 LILITY ACORDADA ---

screen interacao_toque_lility():

    modal True

    zorder 85

    add expressao_lility at sprite_padrao, anim_toque_lility

    $ cor_debug = "#ff000055" if debug_mostrar_hitboxes else None

    frame:

        xalign 0.5 yalign 0.08 background "#220000dd" padding (18, 8)

        text "✋ MODO DE PROXIMIDADE: [nome_display_mestra.upper()] (Paciência: [status_lility.paciencia]/[status_lility.paciencia_max])" size 18 color "#ffaaaa"

    # Cabeça / Cabelo

    button:

        xpos 840 ypos 120 xysize (240, 140)

        background cor_debug

        action Jump("tocou_cabeca_lility")

    # Rosto / Bochecha

    button:

        xpos 860 ypos 265 xysize (200, 120)

        background cor_debug

        action Jump("tocou_rosto_lility")

    # Busto / Tronco

    button:

        xpos 830 ypos 400 xysize (260, 240)

        background cor_debug

        action Jump("tocou_peito_lility")

    vbox:

        xalign 0.95 yalign 0.85 spacing 12

        textbutton "👁️ Mostrar/Ocultar Áreas" action ToggleVariable("debug_mostrar_hitboxes")

        textbutton "🔙 Parar de Tocar" action Jump("menu_encontro_lility")

# --- 6.2 LILITY DORMINDO (EVENTO MATINAL) ---

screen interacao_lility_dormindo():

    modal True

    zorder 85

    add "images/cenas/cena lility dormindo na sala de musica de manha.webp" size (1920, 1080)

    $ cor_debug = "#ff000055" if debug_mostrar_hitboxes else None

    button:

        xpos 760 ypos 220 xysize (350, 180)

        background cor_debug

        action Jump("toque_sono_cabeca")

    button:

        xpos 780 ypos 410 xysize (320, 170)

        background cor_debug

        action Jump("toque_sono_bochecha")

    button:

        xpos 740 ypos 590 xysize (380, 220)

        background cor_debug

        action Jump("toque_sono_ombros")

    vbox:

        xalign 0.95 yalign 0.85 spacing 12

        textbutton "👁️ Mostrar/Ocultar Áreas" action ToggleVariable("debug_mostrar_hitboxes")

        textbutton "🤫 Sair na ponta dos pés" action Jump("sair_sem_acordar_lility")

# --- 6.3 EMÍLIA VON KARSTEN ---

screen interacao_toque_emilia():

    modal True

    zorder 85

    add expressao_emilia at sprite_padrao, anim_toque_emilia

    $ cor_debug = "#0088ff55" if debug_mostrar_hitboxes else None

    frame:

        xalign 0.5 yalign 0.08 background "#102038dd" padding (18, 8)

        text "✋ MODO DE PROXIMIDADE: EMÍLIA (Paciência: [status_emilia.paciencia]/[status_emilia.paciencia_max])" size 18 color "#88ccff"

    # Cabeça / Cabelo

    button:

        xpos 840 ypos 120 xysize (240, 130)

        background cor_debug

        action Jump("tocou_cabeca_emilia")

    # Óculos / Rosto

    button:

        xpos 860 ypos 255 xysize (200, 120)

        background cor_debug

        action Jump("tocou_oculos_emilia")

    # Crucifixo de Prata no Pescoço
    button:
        xpos 860 ypos 390 xysize (200, 160)
        background cor_debug
        action Jump("tocou_crucifixo_emilia")

    # Mãos Devotas / Rosário
    button:
        xpos 850 ypos 560 xysize (220, 160)
        background cor_debug
        action Jump("tocou_mao_emilia")

    vbox:

        xalign 0.95 yalign 0.85 spacing 12

        textbutton "👁️ Mostrar/Ocultar Áreas" action ToggleVariable("debug_mostrar_hitboxes")

        textbutton "🔙 Parar de Tocar" action Jump("menu_encontro_emilia")

# --- 6.4 VALÉRIA (MERCADORA DO SUBSOLO) ---

screen interacao_toque_valeria():

    modal True

    zorder 85

    add expressao_valeria at sprite_padrao, anim_toque_valeria

    $ cor_debug = "#00ff4455" if debug_mostrar_hitboxes else None

    frame:

        xalign 0.5 yalign 0.08 background "#102818dd" padding (18, 8)

        text "✋ MODO DE PROXIMIDADE: VALÉRIA (Paciência: [status_valeria.paciencia]/[status_valeria.paciencia_max])" size 18 color "#88ff88"

    # Cabelo / Pirulito

    button:

        xpos 840 ypos 130 xysize (240, 190)

        background cor_debug

        action Jump("tocou_cabeca_valeria")

    # Suspensórios / Cintura (Taxa de $50)

    button:

        xpos 830 ypos 360 xysize (260, 220)

        background cor_debug

        action Jump("tocou_corpo_valeria")

    # Bolsos / Mochila (Armadilha de Choque)

    button:

        xpos 780 ypos 590 xysize (340, 200)

        background cor_debug

        action Jump("tocou_bolso_valeria")

    vbox:

        xalign 0.95 yalign 0.85 spacing 12

        textbutton "👁️ Mostrar/Ocultar Áreas" action ToggleVariable("debug_mostrar_hitboxes")

        textbutton "🔙 Parar de Tocar" action Jump("menu_encontro_valeria")

# --- 6.5 PRESIDENTE ELARA ---

screen interacao_toque_elara():

    modal True

    zorder 85

    add expressao_elara at sprite_padrao, anim_toque_elara

    $ cor_debug = "#ffffff55" if debug_mostrar_hitboxes else None

    frame:

        xalign 0.5 yalign 0.08 background "#281828dd" padding (18, 8)

        text "✋ MODO DE PROXIMIDADE: PRESIDENTE ELARA (Paciência: [status_elara.paciencia]/[status_elara.paciencia_max])" size 18 color "#ffccff"

    # Rosto / Cabelo

    button:

        xpos 850 ypos 140 xysize (220, 190)

        background cor_debug

        action Jump("tocou_rosto_elara")

    # Uniforme / Ombros

    button:

        xpos 830 ypos 340 xysize (260, 290)

        background cor_debug

        action Jump("tocou_elara_reacao")

    vbox:

        xalign 0.95 yalign 0.85 spacing 12

        textbutton "👁️ Mostrar/Ocultar Áreas" action ToggleVariable("debug_mostrar_hitboxes")

        textbutton "🔙 Parar de Tocar" action Jump("menu_encontro_elara")

# ==============================================================================

# 7. CARREGAMENTO DE TODOS OS 12 LOCAIS E SISTEMA DE ENCONTRO COM MOBS

# ==============================================================================

label avancar_com_sino_academia:
    hide screen hud_exploracao_bs
    hide screen mapa_tatico_escola
    hide screen hud_sobrevivencia
    scene black with dissolve
    play sound "audio/sfx/sfx_passos_madeira_ranger.ogg"
    "As doze badaladas da torre central ecoam pesadas pelas abóbadas da Academia São Cipriano..."
    "O tempo da [periodo] se esgotou. Os corredores começam a mudar de vigília e a penumbra avança."
    jump avancar_turno_mapa

label abrir_mapa_tatico:
    if getattr(store, "visitas_restantes_periodo", 3) <= 0:
        jump avancar_com_sino_academia

    hide screen hud_exploracao_bs

    hide screen hud_sobrevivencia

    python:
        store.eh_dia_chuvoso = (getattr(store, "clima_diario_id", "") in ["chuva_vitrais", "chuva", "chuva_acida", "nevoeiro_sangue"] or getattr(store, "chuva_forcada_evento", False))
        sfx_mapa_escolhido = "audio/sfx/sfx_mapa_ambiente_manha.ogg" if periodo == "Manhã" else ("audio/sfx/sfx_mapa_ambiente_tarde.ogg" if periodo == "Tarde" else "audio/sfx/sfx_mapa_ambiente_neblina_noite.ogg")
        if store.eh_dia_chuvoso:
            sfx_mapa_escolhido = "audio/sfx/sfx_mapa_ambiente_chuva.ogg"
        if aba_mapa_subsolo:
            sfx_mapa_escolhido = "audio/sfx/sfx_mapa_ambiente_subsolo.ogg"

        if renpy.music.get_playing(channel="ambient") != sfx_mapa_escolhido:
            renpy.music.play(sfx_mapa_escolhido, channel="ambient", loop=True, fadein=1.5)

    call screen mapa_tatico_escola

    jump abrir_mapa_tatico

# ==============================================================================
# SUBROTINA UNIFICADA DE CENÁRIOS: RESTAURAR FUNDO CONTEXTUAL (ZERO DESCOMPASSO)
# ==============================================================================
label restaurar_fundo_local_atual:
    $ _eh_chuv = verificar_esta_chovendo()
    $ store.eh_dia_chuvoso = _eh_chuv
    if local_atual == "dormitorio":
        if periodo == "Noite":
            scene bg animado dormitorio quarto noite luar with dissolve
        elif _eh_chuv:
            scene bg animado dormitorio quarto chuva with dissolve
        elif periodo == "Manhã":
            scene bg animado dormitorio quarto manha raio sol with dissolve
        else:
            scene bg animado dormitorio quarto tarde sol with dissolve
    elif local_atual == "patio_fonte":
        if periodo == "Noite":
            scene bg animado patio claustro fonte noite with dissolve
        elif _eh_chuv:
            scene bg animado patio claustro fonte chuva with dissolve
        elif periodo == "Manhã":
            scene bg animado patio claustro fonte dia with dissolve
        else:
            scene bg animado patio claustro fonte entardecer with dissolve
    elif local_atual == "portoes_praca":
        if periodo == "Noite":
            scene bg animado entrada academia portoes nevoeiro noite with dissolve
        elif _eh_chuv:
            scene bg animado entrada academia portoes chuva with dissolve
        elif periodo == "Manhã":
            scene bg animado entrada academia portoes manha with dissolve
        else:
            scene bg animado entrada academia portoes entardecer sol with dissolve
    elif local_atual == "biblioteca":
        if periodo == "Noite":
            scene bg animado biblioteca gotica mesas noite with dissolve
        elif _eh_chuv:
            scene bg animado biblioteca gotica mesas chuva with dissolve
        else:
            scene bg animado biblioteca gotica mesas manha with dissolve
    elif local_atual == "sala_ocultismo":
        scene bg animado sala aula ocultismo alquimia verde with dissolve
    elif local_atual == "enfermaria":
        if periodo == "Noite":
            scene bg animado enfermaria noite with dissolve
        elif _eh_chuv:
            scene bg animado enfermaria chuva with dissolve
        elif periodo == "Manhã":
            scene bg animado enfermaria manha with dissolve
        else:
            scene bg animado enfermaria tarde with dissolve
    elif local_atual == "salao_gremio":
        if periodo == "Noite":
            scene bg animado gabinete diretor noite candelabro with dissolve
        elif _eh_chuv:
            scene bg animado gabinete diretor chuva with dissolve
        elif periodo == "Tarde":
            scene bg animado gabinete diretor entardecer sol with dissolve
        else:
            scene bg animado gabinete diretor dia cortinas with dissolve
    elif local_atual == "sala_musica":
        if periodo == "Noite" and clima_diario_id in ["chuva_vitrais", "chuva", "chuva_acida", "nevoeiro_sangue"]:
            scene bg animado sala musica piano vitral chuva at luz_sombra_noturna with dissolve
        elif periodo == "Noite":
            scene bg animado sala musica piano noite with dissolve
        elif _eh_chuv:
            scene bg animado sala musica piano vitral chuva with dissolve
        else:
            scene bg animado sala musica piano vitral sol with dissolve
    elif local_atual == "banheiro_abandonado":
        scene bg animado banheiro abandonado luz vermelha piscando with dissolve
    elif local_atual == "caldeiras":
        scene bg animado caldeiras esconderijo tocha azul e fogo with dissolve
    elif local_atual == "sala_caldeiras":
        scene bg animado corredor industrial subsolo vapor with dissolve
    elif local_atual == "bar_fada_verde":
        scene bg animado bar grunge luzes neon with dissolve
    elif local_atual == "cemiterio_nevoa":
        if periodo == "Noite":
            scene bg animado cemiterio noite with dissolve
        elif _eh_chuv:
            scene bg animado cemiterio chuva with dissolve
        else:
            scene bg animado cemiterio manha with dissolve
    elif local_atual == "catacumbas":
        scene bg animado catacumbas corredor tochas with dissolve
    elif local_atual == "cripta_cofre":
        scene bg animado cripta cela vidro runas fechada with dissolve
    elif local_atual == "patio_arvore":
        if periodo == "Noite":
            scene bg animado patio arvore postes noite with dissolve
        elif _eh_chuv:
            scene bg animado patio arvore chuva with dissolve
        elif periodo == "Manhã":
            scene bg animado patio arvore dia claro with dissolve
        else:
            scene bg animado patio arvore entardecer dourado with dissolve
    elif local_atual == "rua_portao":
        if periodo == "Noite":
            scene bg animado rua portao academia noite with dissolve
        elif _eh_chuv:
            scene bg animado rua avenida campus chuva with dissolve
        elif periodo == "Manhã":
            scene bg animado rua portao academia manha with dissolve
        else:
            scene bg animado rua portao academia tarde with dissolve
    else:
        if periodo == "Noite":
            scene bg animado corredor zona vermelha luzes de sangue with dissolve
        elif _eh_chuv:
            scene bg animado corredor academia chuva with dissolve
        elif periodo == "Tarde":
            scene bg animado corredor academia entardecer sol with dissolve
        else:
            scene bg animado corredor academia cortina sol with dissolve
    return

label entrar_local_exploracao_bs:

    stop ambient fadeout 1.2

    hide screen mapa_tatico_escola
    show screen hud_sobrevivencia

    # Verificação de Travas Narrativas de Acesso

    if local_atual == "banheiro_abandonado" and not desbloqueou_banheiro_abandonado:

        $ deslocando_pelo_mapa = False
        $ notificar_rpg("🔒 ACESSO BLOQUEADO", "A porta do sanitário do 2º andar está interditada pela reitoria.", "#ff4444")

        jump abrir_mapa_tatico

    elif local_atual == "bar_fada_verde" and not tem_passe_fada_verde:
        $ deslocando_pelo_mapa = False
        show mob veterana fundao at sprite_direita with dissolve
        $ th_voz("mobs/mob_aluna_delinquente_provocacao")
        "Aluna Veterana do Fundão" "Ei, bolsista... Perdeu a mesada para o Conselho de novo? Dá meia-volta se não tiver o passe, ou entra no beco cego se quiser contrabando de verdade."
        hide mob with dissolve
        $ notificar_rpg("🔒 ACESSO BARRADO", "Os contrabandistas do Fundão exigem o Passe Clandestino de Valéria para entrar.", "#ff4444")
        jump abrir_mapa_tatico

    elif local_atual == "cripta_cofre" and not desbloqueou_cripta_cofre:

        $ deslocando_pelo_mapa = False
        $ notificar_rpg("🔒 SELO INVIOLÁVEL", "A tumba ancestral permanece selada ([fragmentos_chave_cripta]/3 fragmentos rúnicos).", "#ff4444")

        jump abrir_mapa_tatico

    elif local_atual == "caldeiras" and not desbloqueou_mercado_negro:

        $ deslocando_pelo_mapa = False
        $ notificar_rpg("🔒 ESCONDERIJO OCULTO", "Você ainda não localizou a entrada do Mercado Negro ([investigacoes_caldeiras]/5 buscas nas Caldeiras).", "#ff4444")

        jump abrir_mapa_tatico

    elif local_atual == "caldeiras" and not mercado_negro_aberto_hoje:

        $ deslocando_pelo_mapa = False
        $ notificar_rpg("🔒 MERCADO FECHADO", "O Mercado Negro suspendeu as operações hoje para despistar as rondas do Grêmio.", "#ff8844")

        jump abrir_mapa_tatico

    # Processamento do Custo de Visita por Período (Plano A)
    if getattr(store, "deslocando_pelo_mapa", False):
        $ deslocando_pelo_mapa = False
        if local_atual != "dormitorio":
            $ visitas_restantes_periodo = max(0, getattr(store, "visitas_restantes_periodo", 3) - 1)
            if local_atual not in getattr(store, "locais_visitados_neste_periodo", []):
                $ locais_visitados_neste_periodo.append(local_atual)
            if local_atual in ["patio_fonte", "patio_arvore", "portoes_praca", "rua_portao", "cemiterio_nevoa", "jardim_estufas", "bosque_obscuro"]:
                play sound "audio/sfx/sfx_passos_gravilha_patio.ogg"
            else:
                play sound "audio/sfx/sfx_passos_madeira_ranger.ogg"
            if visitas_restantes_periodo > 0:
                $ notificar_rpg("⏳ VISITA DE SETOR", f"Restam {visitas_restantes_periodo} visitas neste período.", "#ffd700")
            else:
                $ notificar_rpg("⏳ ÚLTIMA VISITA!", f"Esta é sua última visita nesta {periodo}! Ao sair, o período se encerrará.", "#ff4444")
        else:
            play sound "audio/sfx/sfx_passos_madeira_ranger.ogg"
            $ notificar_rpg("🛏️ REFÚGIO SEGURO", "Você retornou ao dormitório. Este quarto é inviolável e não consome visitas.", "#88ccff")

    # Se a Fome de Sangue cair abaixo de 20%, alerta de Frenesi Iminente (Voz Interna Estilo Persona 5)!

    if fome_sangue <= 0:
        with flash_red
        with vpunch
        "🩸 [[FOME CRÍTICA A ZERO]]: A besta interior devorou seus sentidos! Qualquer criatura encontrada no corredor será atacada em frenesi incontrolável!"
    elif fome_sangue < 20:
        with flash_red
        "Sua garganta queima como brasas vivas...{w=0.3} O som dos batimentos cardíacos dos estudantes ao redor ecoa alto demais."
        "(Tentar bancar o estudante calmo agora é um blefe perigoso.{w=0.4} Se eu não conseguir sangue rápido, a fome vai rasgar a Máscara por mim.)"

    $ eh_dia_chuvoso = verificar_esta_chovendo()
    $ store.eh_dia_chuvoso = eh_dia_chuvoso

    # O áudio atmosférico (chuva e cenários) é gerenciado automaticamente de forma contínua pelo sistema_som_ambiente.rpy

    if local_atual == "dormitorio":

        if eh_dia_chuvoso:

            scene bg animado dormitorio quarto chuva with dissolve

        elif periodo == "Manhã":

            scene bg animado dormitorio quarto manha raio sol with dissolve

        elif periodo == "Tarde":

            scene bg animado dormitorio quarto tarde sol with dissolve

        else:

            scene bg animado dormitorio quarto noite luar with dissolve

        if renpy.loadable("audio/musicas/tema_quarto.mp3"):
            play music "audio/musicas/tema_quarto.mp3" if_changed fadein 1.5
        elif renpy.loadable("audio/Safe_Within_the_Blue_2.ogg"):
            play music "audio/Safe_Within_the_Blue_2.ogg" if_changed fadein 1.5

        # Gestão de Presença Visual e Interações das Heroínas no Dormitório (Zona Segura)
        if loc_emilia == "dormitorio" and loc_mestra == "dormitorio":
            show emilia uniforme seria investigativa meio corpo at sprite_esquerda with dissolve
            show lility meio corpo desdenhando at sprite_direita with dissolve
            if not getattr(store, "ev_embate_dormitorio_lility_emilia_visto", False):
                jump evento_embate_dormitorio_lility_emilia
        elif loc_emilia == "dormitorio":
            hide lility with dissolve
            show emilia uniforme calma meio corpo at sprite_direita with dissolve
        elif loc_mestra == "dormitorio":
            hide emilia with dissolve
            show lility comportada sorriso meio corpo at sprite_direita with dissolve
            if periodo == "Noite" and getattr(store, "status_lility", None) and status_lility.afeto >= 6 and getattr(store, "estagio_mestra", 1) >= 2 and not getattr(store, "ev_visita_dormitorio_lility_visto", False):
                jump ev_visita_noturna_lility_dormitorio
        else:
            hide emilia with dissolve
            hide lility with dissolve

    elif local_atual == "patio_fonte":

        if eh_dia_chuvoso:

            scene bg animado patio claustro fonte chuva with dissolve

        elif periodo == "Manhã":

            scene bg animado patio claustro fonte dia with dissolve

        elif periodo == "Tarde":

            scene bg animado patio claustro fonte entardecer with dissolve

        else:

            scene bg animado patio claustro fonte noite with dissolve

        if renpy.loadable("audio/Safe_Within_the_Blue.ogg"):

            play music "audio/Safe_Within_the_Blue.ogg" if_changed fadein 1.5

    elif local_atual == "portoes_praca":

        if eh_dia_chuvoso:

            scene bg animado entrada academia portoes chuva with dissolve

        elif periodo == "Manhã":

            scene bg animado entrada academia portoes manha with dissolve

        elif periodo == "Tarde":

            scene bg animado entrada academia portoes entardecer sol with dissolve

        else:

            scene bg animado entrada academia portoes nevoeiro noite with dissolve

        if renpy.loadable("audio/suspense_sombrio.ogg"):
            play music "audio/suspense_sombrio.ogg" if_changed fadein 1.5

        if periodo == "Noite" and loc_mestra == "portoes_praca" and not getattr(store, "ev_fronteira_portoes_lility_visto", False):
            jump ev_lility_fronteira_portoes

    elif local_atual == "biblioteca":

        if not investigou_caderno_emilia_dia2:

            jump evento_emilia_caderno_doacoes_dia2

        # Gatilho Inicial Orgânico: A Carteira Vazia de Nora e os Prontuários (com aviso de Clara e Emília)
        if dia_atual >= 3 and not getattr(store, "ev_carteira_nora_visto", False):
            $ ev_carteira_nora_visto = True
            if "marco_15_carteira_nora" not in marcos_doom_disparados:
                $ marcos_doom_disparados.append("marco_15_carteira_nora")
            jump evt_d03_manha

        if periodo == "Noite":
            scene bg animado biblioteca gotica mesas noite with dissolve
        elif eh_dia_chuvoso:
            scene bg animado biblioteca gotica mesas chuva with dissolve
        else:
            scene bg animado biblioteca gotica mesas manha with dissolve

        if renpy.loadable("audio/The_Unfinished_Lesson.ogg"):

            play music "audio/The_Unfinished_Lesson.ogg" if_changed fadein 1.5

    elif local_atual == "sala_ocultismo":

        scene bg animado sala aula ocultismo alquimia verde with dissolve

        if renpy.loadable("audio/obscura.ogg"):

            play music "audio/obscura.ogg" if_changed fadein 1.5

    elif local_atual == "enfermaria":
        if periodo == "Noite":
            scene bg animado enfermaria noite with dissolve
        elif eh_dia_chuvoso:
            scene bg animado enfermaria chuva with dissolve
        elif periodo == "Manhã":
            scene bg animado enfermaria manha with dissolve
        else:
            scene bg animado enfermaria tarde with dissolve
        $ th_musica("Safe_Within_the_Blue", 1.5)

        if dia_atual >= 2 and periodo in ["Manhã", "Tarde"] and not getattr(store, "ev_triagem_dia2_visto", False):
            jump evt_d02_tarde

        $ emilia_sabe_vampiro = getattr(store, "pacto_emilia_ativo", False) or getattr(store, "estagio_emilia", 1) >= 2 or (getattr(store, "status_emilia", None) and (status_emilia.vinculo_sangue > 0 or status_emilia.afeto >= 5))
        if periodo in ["Manhã", "Tarde"] and emilia_sabe_vampiro and not getattr(store, "ev_triagem_enfermaria_visto", False):
            jump ev_c02_triagem_enfermaria

        if getattr(store, "ev_triagem_enfermaria_visto", False) and not getattr(store, "ev_rastro_nora_enfermaria_visto", False) and (ruina_cain >= 15 or renpy.random.randint(1, 100) <= 50):
            jump ev_rastro_oculto_nora_enfermaria

    elif local_atual == "salao_gremio":

        if MISTERIOS_ACADEMIA["inquerito_inquisicao"].pistas_coletadas >= 3 and not caso_inquerito_resolvido and periodo in ["Tarde", "Noite"]:

            jump evento_inquerito_inquisicao_climax

        if eh_dia_chuvoso:
            scene bg animado gabinete diretor chuva with dissolve
        elif periodo == "Noite":
            scene bg animado gabinete diretor noite candelabro with dissolve
        elif periodo == "Tarde":
            scene bg animado gabinete diretor entardecer sol with dissolve
        else:
            scene bg animado gabinete diretor dia cortinas with dissolve

        if renpy.loadable("audio/musicas/tema_conselho_estudantil.mp3"):
            play music "audio/musicas/tema_conselho_estudantil.mp3" if_changed fadein 1.5
        elif renpy.loadable("audio/The_Cold_Decree.ogg"):
            play music "audio/The_Cold_Decree.ogg" if_changed fadein 1.5

    elif local_atual == "sala_musica":

        if not primeiro_transe_lility_realizado:

            jump evento_primeiro_transe_lility

        if MISTERIOS_ACADEMIA["partitura_carnal"].pistas_coletadas >= 3 and not caso_partitura_resolvido:

            jump evento_partitura_carnal_climax

        # Evento Especial Clímax de Meio/Fim de Jogo: A Valsa das Sombras (Lility no Vestido Antigo ao Piano)
        # Requer: Dia 12+, Entardecer/Noite, Afeto alto (>= 10, Estágio 2+) e ainda não realizada
        if dia_atual >= 12 and periodo in ["Tarde", "Noite"] and getattr(store, "status_lility", None) and status_lility.afeto >= 10 and getattr(store, "estagio_mestra", 1) >= 2 and not getattr(store, "valsa_com_lility_realizada", False):
            if "marco_20_partitura_lility" not in marcos_doom_disparados:
                $ marcos_doom_disparados.append("marco_20_partitura_lility")
            jump evt_d04_tarde

        if periodo == "Manhã" and not tentou_visitar_manha_hoje:

            $ tentou_visitar_manha_hoje = True

            if renpy.random.randint(1, 100) <= 45:

                jump evento_rng_lility_dormindo_manha

        if periodo == "Noite" and clima_diario_id in ["chuva_vitrais", "chuva", "chuva_acida", "nevoeiro_sangue"]:
            scene bg animado sala musica piano vitral chuva at luz_sombra_noturna with dissolve
        elif periodo == "Noite":
            scene bg animado sala musica piano noite with dissolve
        elif eh_dia_chuvoso:
            scene bg animado sala musica piano vitral chuva with dissolve
        else:
            scene bg animado sala musica piano vitral sol with dissolve

        if renpy.loadable("audio/musicas/the_crimson_chamber.mp3"):
            play music "audio/musicas/the_crimson_chamber.mp3" if_changed fadein 1.5
        elif renpy.loadable("audio/The_Crimson_Chamber.ogg"):
            play music "audio/The_Crimson_Chamber.ogg" if_changed fadein 1.5

        if periodo == "Noite" and clima_diario_id in ["chuva_vitrais", "chuva", "chuva_acida", "nevoeiro_sangue"] and not getattr(store, "ev_janela_lility_visto", False):
            jump ev_c01_janela_lility

        if not getattr(store, "ev_escuta_decreto_elara_visto", False) and (ruina_cain >= 15 or renpy.random.randint(1, 100) <= 40):
            jump ev_c08_escuta_decreto_elara

    elif local_atual == "banheiro_abandonado":

        if MISTERIOS_ACADEMIA["loira_banheiro"].pistas_coletadas >= 3 and not derrotou_loira_banheiro:

            jump evento_loira_banheiro_anomalia

        if not getattr(store, "ev_halo_espelho_banheiro_visto", False):
            jump evt_d02_noite

        scene bg animado banheiro abandonado luz vermelha piscando with dissolve

        if renpy.loadable("audio/pulsao_sombra.ogg"):

            play music "audio/pulsao_sombra.ogg" if_changed fadein 1.5

    elif local_atual == "caldeiras":

        if not conheceu_valeria_caldeiras:

            jump evento_conhecer_valeria_caldeiras

        if MISTERIOS_ACADEMIA["lote_necrotico"].pistas_coletadas >= 3 and not caso_lote_necrotico_resolvido:

            jump evento_lote_necrotico_anomalia

        scene bg animado caldeiras esconderijo tocha azul e fogo with dissolve

        if renpy.loadable("audio/at_the_green_fairy.ogg"):

            play music "audio/at_the_green_fairy.ogg" if_changed fadein 1.5

    elif local_atual == "sala_caldeiras":

        # Áudio ambiente das caldeiras gerenciado exclusivamente pelo canal ambient (MP4 OGG)

        if MISTERIOS_ACADEMIA["lote_necrotico"].pistas_coletadas >= 3 and not caso_lote_necrotico_resolvido:

            jump evento_lote_necrotico_anomalia

        $ sortear_bg_caldeiras()

        if bg_caldeiras_atual == "bg animado corredor industrial subsolo vapor":

            scene bg animado corredor industrial subsolo vapor with dissolve

        elif bg_caldeiras_atual == "bg animado caldeiras oficina fornalha brasa":

            scene bg animado caldeiras oficina fornalha brasa with dissolve

        else:

            scene bg animado corredor industrial caldeira subsolo vapor with dissolve

        if renpy.loadable("audio/Iron_Lungs.ogg"):

            play music "audio/Iron_Lungs.ogg" if_changed fadein 1.5

        elif renpy.loadable("audio/at_the_green_fairy.ogg"):

            play music "audio/at_the_green_fairy.ogg" if_changed fadein 1.5

        # Se a fome estiver crítica (< 30), Victor desaba nas Caldeiras em busca de sangue sem plateia
        if fome_sangue < 30 and not getattr(store, "ev_fome_sem_plateia_valeria_visto", False):
            jump ev_c15_fome_sem_plateia_valeria

        # Investigação para localização do Mercado Negro (requer 5 buscas nas Caldeiras)

        if not desbloqueou_mercado_negro:

            $ investigacoes_caldeiras += 1

            if investigacoes_caldeiras == 1:

                "🔍 [[BUSCA NAS CALDEIRAS (1/5)]]: Por entre o vapor escaldante das tubulações, você nota pegadas furtivas com resíduos de graxa fresca e cinzas."

                $ notificar_rpg("🔍 PISTA DO MERCADO NEGRO", "Pegadas suspeitas detectadas nas Caldeiras (1/5).", "#00ffcc")

            elif investigacoes_caldeiras == 2:

                "🔍 [[BUSCA NAS CALDEIRAS (2/5)]]: Atrás de uma válvula de descarte, você encontra bitucas de cigarro mentolado e um símbolo mercantil talhado no metal."

                $ notificar_rpg("🔍 PISTA DO MERCADO NEGRO", "Rastro de contrabando localizado (2/5).", "#00ffcc")

            elif investigacoes_caldeiras == 3:

                "🔍 [[BUSCA NAS CALDEIRAS (3/5)]]: O eco abafado de risadas e tilintar de garrafas ressoa por trás de uma grade de ventilação trancada por correntes."

                $ notificar_rpg("🔍 PISTA DO MERCADO NEGRO", "Ruídos clandestinos mapeados (3/5).", "#00ffcc")

            elif investigacoes_caldeiras == 4:

                "🔍 [[BUSCA NAS CALDEIRAS (4/5)]]: Você mapeia a rota de desvio das rondas do Conselho. A entrada do esconderijo está a poucos metros!"

                $ notificar_rpg("🔍 PISTA DO MERCADO NEGRO", "Rota de acesso quase decifrada (4/5).", "#00ffcc")

            else:

                $ desbloqueou_mercado_negro = True
                $ mercado_negro_desbloqueado = True

                "🛒 [[MERCADO NEGRO DESCOBERTO! (5/5)]]: Você empurra uma chapa de aço solta atrás da fornalha principal! Uma escadaria oculta desce até o esconderijo de Valéria!"

                $ notificar_rpg("🛒 MERCADO NEGRO LOCALIZADO", "O Mercado Negro de Valéria foi revelado no Mapa Tático!", "#2eb82e")

    elif local_atual == "bar_fada_verde":

        scene bg animado bar grunge luzes neon with dissolve

        if renpy.loadable("audio/musicas/midnight_in_the_underpass.mp3"):
            play music "audio/musicas/midnight_in_the_underpass.mp3" if_changed fadein 1.5
        elif renpy.loadable("audio/bar-da-fada-verde.ogg"):
            play music "audio/bar-da-fada-verde.ogg" if_changed fadein 1.5

    elif local_atual == "cemiterio_nevoa":

        if MISTERIOS_ACADEMIA["hachishaku"].pistas_coletadas >= 3 and not derrotou_hachishaku and periodo == "Noite":

            jump evento_hachishaku_anomalia

        if periodo == "Noite":
            scene bg animado cemiterio noite with dissolve
        elif eh_dia_chuvoso:
            scene bg animado cemiterio chuva with dissolve
        else:
            scene bg animado cemiterio manha with dissolve

        if renpy.loadable("audio/funeral_in_the_catacombs.ogg"):

            play music "audio/funeral_in_the_catacombs.ogg" if_changed fadein 1.5

    elif local_atual == "catacumbas":

        $ sortear_bg_catacumbas()

        if bg_catacumbas_atual == "bg animado catacumbas corredor runas tochas":

            scene bg animado catacumbas corredor runas tochas with dissolve

        elif bg_catacumbas_atual == "bg animado catacumbas cofre velas verdes":

            scene bg animado catacumbas cofre velas verdes with dissolve

        else:

            scene bg animado catacumbas corredor tochas with dissolve

        if renpy.loadable("audio/funeral_in_the_catacombs.ogg"):

            play music "audio/funeral_in_the_catacombs.ogg" if_changed fadein 1.5

    elif local_atual == "cripta_cofre":

        scene bg animado cripta cela vidro runas fechada with dissolve

        if renpy.loadable("audio/catactic_requiem.ogg"):

            play music "audio/catactic_requiem.ogg" if_changed fadein 1.5

    elif local_atual == "patio_arvore":

        if eh_dia_chuvoso:

            scene bg animado patio arvore chuva with dissolve

        elif periodo == "Manhã":

            scene bg animado patio arvore dia claro with dissolve

        elif periodo == "Tarde":

            scene bg animado patio arvore entardecer dourado with dissolve

        else:

            scene bg animado patio arvore postes noite with dissolve

        if renpy.loadable("audio/Safe_Within_the_Blue.ogg"):

            play music "audio/Safe_Within_the_Blue.ogg" if_changed fadein 1.5

    elif local_atual == "rua_portao":

        if eh_dia_chuvoso:

            scene bg animado rua avenida campus chuva with dissolve

        elif periodo == "Manhã":

            scene bg animado rua portao academia manha with dissolve

        elif periodo == "Tarde":

            scene bg animado rua portao academia tarde with dissolve

        else:

            scene bg animado rua portao academia noite with dissolve

        if renpy.loadable("audio/suspense_sombrio.ogg"):
            play music "audio/suspense_sombrio.ogg" if_changed fadein 1.5

    else:
        if periodo == "Noite":
            scene bg animado corredor zona vermelha luzes de sangue with dissolve
        elif eh_dia_chuvoso:
            scene bg animado corredor academia chuva with dissolve
        elif periodo == "Tarde":
            scene bg animado corredor academia entardecer sol with dissolve
        else:
            scene bg animado corredor academia cortina sol with dissolve

    call screen hud_exploracao_bs

    jump abrir_mapa_tatico

label consultar_regras_dormitorio:
    hide screen hud_exploracao_bs
    "Você senta na beirada da cama estreita e revisa as 4 Regras de Sobrevivência anotadas no verso do cartão de bolsista:"
    "1. Não seja visto bebendo sangue vivo sob a luz do sol."
    "2. Não confronte guardas ou veteranos na Zona Vermelha sem armas de prata ou choque."
    "3. Se a fome atingir o limite crítico (<20%%), o frenesi assumirá o controle."
    "4. Ao toque de recolher ou em perigo mortal, tranque-se no Dormitório. Este quarto é solo inviolável."
    jump entrar_local_exploracao_bs

label acao_descansar_dormitorio:
    hide screen hud_exploracao_bs

    python:
        _p_rest = getattr(store, "passos_restantes_periodo", 3)
        if _p_rest >= 3:
            _hp_recup = 45
            _chance_seq = 100
            _red_exp = 5
            _tipo_desc = "Repouso Profundo"
        elif _p_rest == 2:
            _hp_recup = 30
            _chance_seq = 70
            _red_exp = 0
            _tipo_desc = "Descanso Longo"
        elif _p_rest == 1:
            _hp_recup = 15
            _chance_seq = 0
            _red_exp = 0
            _tipo_desc = "Cochilo Breve"
        else:
            _hp_recup = 5
            _chance_seq = 0
            _red_exp = 0
            _tipo_desc = "Colapso por Exaustão"

        # Penalidade de Pesadelos da Fome
        _penalidade_fome = False
        if store.fome_sangue < 25:
            _penalidade_fome = True
            _hp_recup = max(0, _hp_recup - 10)

        store.hp_jogador = min(store.hp_jogador_max, store.hp_jogador + _hp_recup)
        if _red_exp > 0:
            store.exposicao = max(0, store.exposicao - _red_exp)

    $ limpar_rastro_olfativo("Banho Frio & Troca de Roupas no Quarto")

    if _penalidade_fome:
        "🩸 [[PESADELOS DA FOME]]: Sua garganta ardeu em espasmos febris de abstinência durante a noite. O descanso foi perturbador (-10 HP da recuperação prevista)."

    if _p_rest >= 3:
        $ notificar_rpg("🛏️ REPOUSO PROFUNDO", f"+{_hp_recup} HP | -5% Exposição | Sequela Tratada", "#00ffcc")
        "Você tranca a porta reforçada, trata cuidadosamente cada corte com água fria e dorme por longas horas ininterruptas. Victor desperta com as forças renovadas (+[_hp_recup] HP | -5%% Exposição | Aromas e vestígios neutralizados)."
    elif _p_rest == 2:
        $ notificar_rpg("🛏️ DESCANSO LONGO", f"+{_hp_recup} HP | Aromas Neutralizados", "#88ccff")
        "Você retorna cedo ao dormitório, limpa os vestígios da ronda e desfruta de um sono tranquilo nas cobertas (+[_hp_recup] HP | Aromas e vestígios neutralizados)."
    elif _p_rest == 1:
        $ notificar_rpg("🛏️ COCHILO BREVE", f"+{_hp_recup} HP | Tempo Limitado", "#e6b8ff")
        "Com pouco tempo restante antes da troca de guarda, você consegue apenas um cochilo rápido e superficial na cama estreita (+[_hp_recup] HP | Aromas neutralizados)."
    else:
        $ notificar_rpg("⚠️ COLAPSO POR EXAUSTÃO", f"+{_hp_recup} HP | Esgotado", "#ff4444")
        "Você desaba de roupa e botas sobre as cobertas, completamente exausto e ensanguentado após esgotar todo o seu tempo nos corredores. O descanso foi curto, dolorido e agitado (+[_hp_recup] HP | Sem tempo para tratar ferimentos graves)."

    if sequelas_ativas:
        if _chance_seq >= 100 or (_chance_seq > 0 and renpy.random.randint(1, 100) <= _chance_seq):
            $ _seq_curada = sequelas_ativas[0]["nome"]
            $ curar_sequela(sequelas_ativas[0]["id"])
            "🩹 [[RECUPERAÇÃO FÍSICA]]: O repouso permitiu tratar e cicatrizar a condição: [_seq_curada]!"
        elif _p_rest <= 1:
            "⚠️ [[FERIMENTOS NÃO TRATADOS]]: O tempo de descanso foi insuficiente para fechar suas sequelas graves. Você ainda precisa de cuidados médicos ou de um repouso prolongado para se curar."

    if periodo == "Noite" and clima_diario_id == "toque_recolher":
        "🛡️ [[REFÚGIO TOTALMENTE SEGURO]]: As trancas do quarto suportam as batidas dos inspetores no corredor. Seu quarto permanece inviolável (0%% de risco)."

    # Sinergias de Vigília e Proteção no Dormitório
    if loc_emilia == "dormitorio" and loc_mestra == "dormitorio":
        "🛡️ [[TRÉGUA SAGRADA E OBSCURA]]: Emília senta-se na escrivaninha murmurando suas orações em silêncio, enquanto [nome_display_mestra] repousa na penumbra da janela vigiando a porta. Sob os olhares vigilantes de ambas, nenhum perigo ousa se aproximar (+10 Humanidade | Tensão Mental Reduzida)."
        $ humanidade = min(100, humanidade + 10)
        $ tensao_psicologica = max(0, tensao_psicologica - 15)
    elif loc_emilia == "dormitorio":
        "✝️ [[VIGÍLIA SAGRADA]]: Emília acomoda a cadeira de pinho junto à porta trancada, segurando o breviário: 'Durma em paz, Victor. Nenhum inspetor ou criatura passará por esta porta enquanto eu velar por você.' Seu descanso é revigorante e protegido (+10 Humanidade | Tensão Mental Reduzida)."
        $ humanidade = min(100, humanidade + 10)
        $ tensao_psicologica = max(0, tensao_psicologica - 15)
    elif loc_mestra == "dormitorio":
        "🩸 [[VIGÍLIA CARMESIM]]: [nome_display_mestra] observa seu leito da penumbra com olhos rubros que penetram a escuridão absoluta. Sob a proteção de uma presença milenar, os pesadelos recuam (+5 Saciedade | Tensão Reduzida)."
        $ fome_sangue = min(100, fome_sangue + 5)
        $ tensao_psicologica = max(0, tensao_psicologica - 10)

    $ passos_restantes_periodo = 0
    jump avancar_turno_mapa

# ==============================================================================
# 5.2B INTERAÇÕES COM HEROÍNAS NO DORMITÓRIO (ZONA SEGURA - 0 PASSOS)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. ENCONTRO NO QUARTO: EMÍLIA
# ------------------------------------------------------------------------------
label menu_encontro_emilia_dormitorio:
    hide screen hud_exploracao_bs

    if loc_mestra == "dormitorio":
        show emilia uniforme seria investigativa meio corpo at sprite_esquerda with dissolve
        show lility meio corpo desdenhando at sprite_direita with dissolve
        "Emília mantém os olhos fixos na figura de [nome_display_mestra] na penumbra antes de se virar para você, com os nós dos dedos apertando o crucifixo de prata."
        $ th_bark("emilia", "suspeita")
        emilia "Victor... Mantenha a guarda alta. Com ela neste quarto, qualquer descuido pode ser fatal."
    else:
        hide lility with dissolve
        show emilia uniforme calma meio corpo at sprite_direita with dissolve
        if periodo == "Manhã":
            $ th_bark("emilia", "manha_cansada")
        else:
            $ th_bark("emilia", "chamado")
        emilia "Victor... Que alívio ver você retornar em segurança. Feche bem o trinco da porta."

    menu:
        "🍵 Aceitar caneca de infusão de camomila e mirra" if not getattr(store, "tomou_cha_emilia_periodo", False):
            $ tomou_cha_emilia_periodo = True
            $ humanidade = min(100, humanidade + 5)
            $ tensao_psicologica = max(0, tensao_psicologica - 15)
            $ th_bark("emilia", "cura")
            show emilia uniforme calma meio corpo at (sprite_esquerda if loc_mestra == "dormitorio" else sprite_direita) with dissolve
            emilia "Eu preparei esta infusão com folhas da capela e água fervida. O aroma é amargo, mas acalma as palpitações e limpa a mente dos sussurros do corredor."
            "Você segura a caneca de barro aquecida entre as mãos. O vapor aromático de mirra e camomila alivia o nó apertado em sua garganta (+5 Humanidade | Tensão Mental Reduzida)."
            if loc_mestra == "dormitorio":
                show lility sorrindo de lado sorrindo at sprite_direita with dissolve
                $ th_bark("lility", "deboche")
                mestra "Ervas da capela e infusões mornas... Que comovente, noviça. Mas quando a sede verdadeira queimar as vísceras dele, nenhuma folha de mirra substituirá uma garganta pulsante."
                show emilia uniforme severa meio corpo at sprite_esquerda with dissolve
                emilia "A alma dele não se curvará aos seus caprichos, monstro."
            $ notificar_rpg("✝️ INFUSÃO BENZIDA", "+5 Humanidade | Tensão Reduzida", "#88ccff")
            jump menu_encontro_emilia_dormitorio

        "🩹 Pedir que examine seus ferimentos com Gaze Consagrada" if (hp_jogador < hp_jogador_max or sequelas_ativas) and not getattr(store, "emilia_curou_gaze_periodo", False):
            $ emilia_curou_gaze_periodo = True
            show emilia uniforme seria investigativa meio corpo at (sprite_esquerda if loc_mestra == "dormitorio" else sprite_direita) with dissolve
            $ th_voz("climax/emilia_marco_curativo")
            emilia "Sente-se na cama, Victor. Deixe-me ver esses cortes antes que a infecção ou o miasma das catacumbas se instalem."
            "Com dedos firmes e delicados, Emília aplica unguento benzido e enrola gaze consagrada sobre suas lacerações."
            if sequelas_ativas:
                $ _seq_curada = sequelas_ativas[0]["nome"]
                $ curar_sequela(sequelas_ativas[0]["id"])
                "🩹 [[RECUPERAÇÃO MILAGROSA]]: A gaze consagrada purifica o ferimento: [_seq_curada] foi completamente cicatrizada!"
            $ hp_jogador = min(hp_jogador_max, hp_jogador + 35)
            if loc_mestra == "dormitorio":
                show lility presas agressiva meio corpo at sprite_direita with dissolve
                mestra "Cuidado ao amarrar esse linho, criança... Se o sangue dele escorrer no assoalho, temo que meus caninos perderão a paciência."
                show emilia uniforme confiante meio corpo at sprite_esquerda with dissolve
                emilia "Minhas mãos não tremem diante de sombras. Victor está sob a proteção da Aurora."
            $ notificar_rpg("🩹 GAZE CONSAGRADA", "+35 HP Restaurados | Sequela Tratada", "#55aaff")
            jump menu_encontro_emilia_dormitorio

        "🩹 Gaze Consagrada (Compressas já aplicadas neste período)" if getattr(store, "emilia_curou_gaze_periodo", False) and (hp_jogador < hp_jogador_max or sequelas_ativas):
            show emilia uniforme calma meio corpo at (sprite_esquerda if loc_mestra == "dormitorio" else sprite_direita) with dissolve
            $ th_bark("emilia", "chamado")
            emilia "O linho benzido precisa de algumas horas para agir na sua carne ferida, Victor. Não tenho mais gaze pura comigo neste turno; deite-se na cama e descanse."
            jump menu_encontro_emilia_dormitorio

        "🤫 Conversar sobre as suspeitas do Conselho e Lorde Phillip" if not getattr(store, "conversou_heroina_periodo", {}).get("emilia_dormitorio", False):
            $ conversou_heroina_periodo["emilia_dormitorio"] = True
            show emilia uniforme seria triste meio corpo at (sprite_esquerda if loc_mestra == "dormitorio" else sprite_direita) with dissolve
            $ th_bark("emilia", "suspeita")
            emilia "Meu pai... Lorde Phillip reuniu os prelados ontem à noite. Ele decretou que qualquer bolsista com índices anormais de hemoglobina será transferido para os calabouços da Fundação."
            emilia "Ele desconfia que algo entrou na ala dos dormitórios. Estar trancada aqui com você é perigoso... mas sinto que este quarto é o único lugar da academia onde ainda posso respirar sem falsidade."
            menu:
                "Você nunca estará sozinha nisso, Emília. Eu protejo você também.":
                    $ status_emilia.afeto += 1
                    $ humanidade = min(100, humanidade + 3)
                    show emilia uniforme corada timida meio corpo at (sprite_esquerda if loc_mestra == "dormitorio" else sprite_direita) with dissolve
                    $ th_bark("emilia", "timida")
                    emilia "Obrigada, Victor... Ouvir isso de você me dá forças para continuar rezando."
                    $ notificar_rpg("✝️ LAÇO DE CONFIANÇA", "+1 Afeto Emília | +3 Humanidade", "#88ccff")
                "Seu pai sabe a verdade sobre a Fundação e as feras?":
                    $ intelecto += 1
                    $ conhecimento_oculto = getattr(store, "conhecimento_oculto", 0) + 1
                    show emilia uniforme seria investigativa meio corpo at (sprite_esquerda if loc_mestra == "dormitorio" else sprite_direita) with dissolve
                    emilia "Ele sabe mais do que confessa no púlpito. O Tratado de 1892 foi assinado com sangue e ouro... Há segredos nos arquivos que nem eu tive coragem de ler por inteiro."
                    $ notificar_rpg("🗝️ SEGREDO ECLESIÁSTICO", "+1 Intelecto | +1 Conhecimento Oculto", "#ffcc00")
                    jump menu_encontro_emilia_dormitorio

        "🤫 Já conversou com Emília no quarto neste período" if getattr(store, "conversou_heroina_periodo", {}).get("emilia_dormitorio", False):
            show emilia uniforme calma meio corpo at (sprite_esquerda if loc_mestra == "dormitorio" else sprite_direita) with dissolve
            $ th_bark("emilia", "chamado")
            emilia "Já conversamos bastante por este turno, Victor. Se ficarmos cochichando a noite inteira, os vigilantes do corredor desconfiarão."
            jump menu_encontro_emilia_dormitorio

        "🩸 A Tensão da Sede no Quarto Fechado" if fome_sangue < 25:
            show emilia uniforme chocada meio corpo at (sprite_esquerda if loc_mestra == "dormitorio" else sprite_direita) with dissolve
            $ th_bark("emilia", "alerta")
            "O cheiro do sangue vivo e pulsante de Emília preenche as quatro paredes estreitas do quarto. Seus caninos latejam com violência e suas têmporas ardem em febre."
            emilia "Victor... seus olhos... Você está tremendo. A fome está devorando você por dentro, não está?"
            menu:
                "Recuar e segurar as mãos contra o peito: 'Fique longe de mim, Emília... Eu não quero machucar você.'":
                    $ humanidade = min(100, humanidade + 5)
                    $ status_emilia.afeto += 2
                    show emilia uniforme calma meio corpo at (sprite_esquerda if loc_mestra == "dormitorio" else sprite_direita) with dissolve
                    $ th_bark("emilia", "consolo")
                    "Emília se aproxima devagar, sem medo, e repousa a mão quente e delicada sobre seu punho gelado."
                    emilia "Mesmo faminto, você escolheu proteger a minha vida... Você continua sendo o Victor. Segure firme na fé."
                    $ notificar_rpg("✝️ HUMANIDADE PRESERVADA", "+5 Humanidade | +2 Afeto com Emília", "#88ccff")
                "Confessar a dor do tormento: 'O cheiro do seu pescoço é quase insuportável...'":
                    $ tensao_psicologica = max(0, tensao_psicologica - 10)
                    show emilia uniforme seria triste meio corpo at (sprite_esquerda if loc_mestra == "dormitorio" else sprite_direita) with dissolve
                    emilia "Eu sei... A maldição é cruel. Mas resista, Victor. Se você ceder ao sangue de um inocente, nunca mais conseguirá olhar nos olhos de ninguém."
                    $ notificar_rpg("🛡️ VONTADE DE FERRO", "Tensão Mental Reduzida", "#ffd700")
                    jump menu_encontro_emilia_dormitorio

        "🌟 [[EVENTO DE MARCO DISPONÍVEL!]] Avançar Relação com Emília" if verificar_marco_disponivel("emilia"):
            if estagio_emilia == 1:
                jump evento_marco_emilia_1
            else:
                jump evento_marco_emilia_2

        "🎁 Entregar Presente Clandestino" if not getattr(store, "presenteou_heroina_hoje", {}).get("emilia", False) and (presente_flores + presente_perfume + presente_colar + presente_roupa + presente_anel) > 0:
            call fluxo_entregar_presente_heroina("emilia") from _call_presente_emilia_dorm
            jump menu_encontro_emilia_dormitorio

        "🚪 Retornar ao Quarto":
            jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 2. ENCONTRO NO QUARTO: LILITY
# ------------------------------------------------------------------------------
label menu_encontro_lility_dormitorio:
    hide screen hud_exploracao_bs

    if loc_emilia == "dormitorio":
        show emilia uniforme seria investigativa meio corpo at sprite_esquerda with dissolve
        show lility meio corpo sorriso malicioso at sprite_direita with dissolve
        "[nome_display_mestra] cruza as pernas elegantemente na borda da cama de Victor, ignorando o olhar de ódio da noviça."
        $ th_bark("lility", "deboche")
        mestra "Aproxima-se de mim na frente da sua vigilante sagrada, Victor? Que audácia deliciosa."
    else:
        hide emilia with dissolve
        show lility comportada sorriso meio corpo at sprite_direita with dissolve
        if fome_sangue <= 20:
            $ th_bark("lility", "fome_critica")
        else:
            $ th_bark("lility", "padrao")
        mestra "Enfim a sós, meu protegido. O ar deste quarto de bolsista é modesto, mas ao menos nos poupa dos olhares intrometidos do Conselho."

    if periodo == "Noite" and getattr(store, "status_lility", None) and status_lility.afeto >= 6 and getattr(store, "estagio_mestra", 1) >= 2 and not getattr(store, "ev_visita_dormitorio_lility_visto", False):
        jump ev_visita_noturna_lility_dormitorio

    menu:
        "🍷 Transe Noturno & Aconchego Carmesim no Leito" if not getattr(store, "transe_lility_periodo", False):
            $ transe_lility_periodo = True
            show lility provocante at sprite_direita with dissolve
            $ th_bark("lility", "prazer")
            mestra "Venha aqui, Victor... Deite a cabeça por alguns instantes. Meu corpo pode ser frio como mármore sepulcral, mas o silêncio que trago emudece até o mais desesperado dos pensamentos."
            "Você se aproxima do leito estreito. [nome_display_mestra] passa as unhas afiadas com lentidão calculada pela sua nuca, anestesiando a fadiga e a queimação dos nervos."
            $ tensao_psicologica = max(0, tensao_psicologica - 20)
            $ charme += 1
            if loc_emilia == "dormitorio":
                show emilia uniforme severa meio corpo at sprite_esquerda with dissolve
                $ th_bark("emilia", "alerta")
                emilia "Victor! Não permita que ela enfeitiça sua mente com carícias amaldiçoadas!"
                show lility meio corpo desdenhando at sprite_direita with dissolve
                mestra "Shh... O rapaz precisa de repouso, noviça. Vá rezar no seu canto e cale a boca."
            $ notificar_rpg("🩸 TRANSE NO LEITO", "Tensão Aliviada | +1 Charme", "#ff4466")
            jump menu_encontro_lility_dormitorio

        "🩸 Comunhão de Sangue na Escuridão (Aplacador de Sede)" if fome_sangue < 35 and not getattr(store, "alimentou_lility_periodo", False):
            $ alimentou_lility_periodo = True
            show lility sorrindo de lado sorrindo at sprite_direita with dissolve
            $ th_bark("lility", "dentes")
            mestra "Seus lábios estão secos e sua pulsação bate como o tambor de um condenado... A fome é um mestre impiedoso, não é?"
            "[nome_display_mestra] ergue o dedo indicador e, com um golpe seco do próprio canino afiado, faz brotar uma única gota de sangue carmesim espesso e reluzente."
            mestra "Beba da minha seiva antes que você enlouqueça e devore quem não deve. É um presente do meu pacto."
            "Você lambe a gota carmesim. Um calor elétrico e poderoso explode em sua garganta, saciando instantaneamente a queimação que ameaçava o seu controle (+30 Fome de Sangue | Saciedade de Vitae)."
            $ fome_sangue = min(100, fome_sangue + 30)
            if loc_emilia == "dormitorio":
                show emilia uniforme chocada meio corpo at sprite_esquerda with dissolve
                emilia "Victor... Não! Beber do sangue de uma vampira sela o seu destino para sempre!"
                show lility presas agressiva meio corpo at sprite_direita with dissolve
                mestra "Se ele não bebesse agora, o pescoço rasgado seria o seu, cordeirinha. Seja grata."
            $ notificar_rpg("🩸 VITA DE LILITY", "+30 Saciedade | Sede Aplacada", "#ff2244")
            jump menu_encontro_lility_dormitorio

        "♟️ Discutir as Fraquezas do Conselho e as Rotas da Ronda":
            show lility meio corpo desdenhando at sprite_direita with dissolve
            $ th_bark("lility", "deboche")
            mestra "Elara pensa que suas sentinelas controlam tudo com pranchetas e apitos. Mas os burocratas são previsíveis como autômatos de corda."
            mestra "Entre as duas e as três da manhã, as caldeiras liberam vapor pela tubulação leste. Esse vapor cega os cães de guarda e abafa passos. Use isso a seu favor."
            $ conhecimento_oculto = getattr(store, "conhecimento_oculto", 0) + 1
            $ exposicao = max(0, exposicao - 5)
            $ notificar_rpg("♟️ TÁTICA DA NOITE", "+1 Conhecimento Oculto | -5% Exposição", "#ffd700")
            jump menu_encontro_lility_dormitorio

        "🌟 [[EVENTO DE MARCO DISPONÍVEL!]] Avançar Relação com a [nome_display_mestra]" if verificar_marco_disponivel("lility"):
            if estagio_mestra == 1:
                jump evento_marco_lility_1
            else:
                jump evento_marco_lility_2

        "🎁 Entregar Presente Clandestino" if not getattr(store, "presenteou_heroina_hoje", {}).get("lility", False) and (presente_flores + presente_perfume + presente_colar + presente_roupa + presente_anel) > 0:
            call fluxo_entregar_presente_heroina("lility") from _call_presente_lility_dorm
            jump menu_encontro_lility_dormitorio

        "🚪 Retornar ao Quarto":
            jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# 3. O GRANDE EMBATE NO DORMITÓRIO: EMÍLIA VS LILITY
# ------------------------------------------------------------------------------
label evento_embate_dormitorio_lility_emilia:
    $ ev_embate_dormitorio_lility_emilia_visto = True
    hide screen hud_exploracao_bs

    $ local_atual = "dormitorio"
    call restaurar_fundo_local_atual
    play music "audio/obscura.ogg" if_changed fadein 1.5

    "Empurro a porta pesada de madeira do meu quarto esperando apenas o silêncio habitual do dormitório. Em vez disso, o ar dentro do cômodo parece congelado sob uma carga eletrizante."

    "O aroma de camomila e mirra fervida de um pequeno bule sobre a escrivaninha colide violentamente com o perfume gélido de rosas velhas e cripta secular."

    show emilia uniforme seria investigativa meio corpo at sprite_esquerda with dissolve
    show lility meio corpo desdenhando at sprite_direita with dissolve

    "De pé junto à mesa, Emília segura seu relicário de prata com tanta força que os nós de seus dedos estão alvos como caliça. À sua frente, reclinada no poste de pinho do meu beliche com a indiferença de uma rainha no trono, está minha mestra."

    $ th_voz("climax/emilia_embate_lility")
    emilia "Você não deveria estar aqui, criatura! O Decreto de Restrição de Lorde Phillip e o Tratado da Fundação impõem o seu confinamento absoluto na ala leste!"

    show lility sorrindo de lado sorrindo at sprite_direita with dissolve
    $ th_voz("climax/lility_embate_emilia")
    mestra "Diga-me, Emília... Você reza com tanta devoção para salvar a alma de Victor, mas o que oferece a ele? Sermões sobre penitência e martírio enquanto a carne dele se decompõe de fome?"

    show emilia uniforme severa meio corpo at sprite_esquerda with dissolve
    emilia "Ofereço a salvação e a honra de continuar humano! Este quarto é o refúgio dele, não um covil para suas manipulações perversas!"

    show lility presas agressiva meio corpo at sprite_direita with dissolve
    mestra "Refúgio? Quatro paredes de tábua compensada e uma tranca que se rompe com um sopro... Ele sobreviveu até hoje porque aprendeu o peso do sangue, não porque decorou os seus hinos hipócritas."

    "Ambas cravam os olhos em mim simultaneamente. A respiração ofegante de Emília e o silêncio mortal da minha mestra exigem uma postura imediata."

    menu:
        "✝️ Apoiar Emília: 'Mestra, este é o meu dormitório. Respeite os limites do Grilhão.'":
            $ status_emilia.afeto += 2
            $ status_lility.afeto = max(0, status_lility.afeto - 1)
            $ humanidade = min(100, humanidade + 5)
            show emilia uniforme seria triste meio corpo at sprite_esquerda with dissolve
            $ th_voz("climax/emilia_aviso_relicario")
            emilia "Obrigada, Victor... Um pulso frio não o condenará, mas deixar que ela devore sua humanidade o fará. Segure a cruz de prata antes que os sinos dobrem."
            show lility meio corpo gelida at sprite_direita with dissolve
            $ th_bark("lility", "ciume")
            mestra "Patético. Defendendo quem o prenderia numa cela no primeiro uivo que der... Não se esqueça de quem o alimentou primeiro, Vane."
            $ notificar_rpg("✝️ APOIO A EMÍLIA NO QUARTO", f"+2 Afeto Emília | +5 Humanidade | -1 Afeto com {nome_display_mestra}", "#55aaff")

        "🩸 Apoiar a [nome_display_mestra]: 'Emília, abaixe o relicário. Ela não me atacou e você vai acordar os inspetores do corredor.'":
            $ status_lility.afeto += 2
            $ status_emilia.afeto = max(0, status_emilia.afeto - 1)
            $ fome_sangue = min(100, fome_sangue + 10)
            show lility comportada sorriso meio corpo at sprite_direita with dissolve
            $ th_bark("lility", "prazer")
            mestra "Ouviu o rapaz, noviça? Ele prefere a verdade nua e crua ao conforto covarde dos seus sermões."
            show emilia uniforme chocada meio corpo at sprite_esquerda with dissolve
            $ th_bark("emilia", "lagrima")
            emilia "Você está cego, Victor... A influência dela já contaminou a sua mente mais do que eu temia. Não diga que não avisei."
            $ notificar_rpg("🩸 APOIO À MESTRA NO QUARTO", f"+2 Afeto com {nome_display_mestra} | +10 Saciedade | -1 Afeto Emília", "#ff2244")

        "⚡ Impor Autoridade: 'SILÊNCIO AS DUAS! Este quarto é MEU. Nem a Igreja nem os Antigos mandam sob este teto!'":
            $ coragem = getattr(store, "coragem", 0) + 2
            $ intelecto += 1
            $ status_emilia.afeto += 1
            $ status_lility.afeto += 1
            $ tensao_psicologica = max(0, tensao_psicologica - 15)
            show emilia uniforme chocada meio corpo at sprite_esquerda with dissolve
            show lility meio corpo chocada at sprite_direita with dissolve
            "Minha voz ressoa firme contra as paredes de madeira, quebrando a contenda no ato. Bato a mão sobre a mesa com determinação inquestionável."
            "Por alguns segundos, nenhuma das duas ousa respirar. O silêncio estala no quarto como vidro sob pressão."
            show emilia uniforme corada timida meio corpo at sprite_esquerda with dissolve
            $ th_bark("emilia", "timida")
            emilia "Victor... Me perdoe. Eu não pretendia profanar o seu abrigo com desavenças."
            show lility sorrindo de lado sorrindo at sprite_direita with dissolve
            $ th_bark("lility", "risada")
            mestra "Ora... O cordeiro aprendeu a mostrar os dentes para as duas pastoras. Isso é fascinante, Victor. Talvez haja algo digno de ser preservado sob esse uniforme cinzento, afinal."
            $ notificar_rpg("⚡ AUTORIDADE NO DORMITÓRIO", "+2 Coragem | +1 Intelecto | +1 Afeto com Ambas!", "#ffd700")

        "🍵 Pacificação Improvável: 'Se nenhuma de vocês vai me matar agora... sentem-se. Vamos dividir o chá.'":
            $ humanidade = min(100, humanidade + 5)
            $ tensao_psicologica = max(0, tensao_psicologica - 20)
            $ status_emilia.afeto += 1
            $ status_lility.afeto += 1
            show emilia uniforme chocada meio corpo at sprite_esquerda with dissolve
            show lility meio corpo confusa at sprite_direita with dissolve
            "Emília quase derruba a caneca de barro de espanto diante da minha proposta absurda. [nome_display_mestra] arregala os olhos por um segundo antes de explodir numa gargalhada cristalina."
            $ th_bark("lility", "risada")
            mestra "Dividir chá de camomila com uma noviça da inquisição no beliche de um bolsista? A audácia do seu desespero chega a ser adorável, Victor."
            show emilia uniforme calma meio corpo at sprite_esquerda with dissolve
            $ th_bark("emilia", "consolo")
            emilia "Você realmente é imprevisível... Mas tem razão. Gritar aqui só colocará a ronda na sua porta."
            "Uma trégua armada e tensa se estabelece no quarto. As armas se recolhem, ainda que as desconfianças permaneçam vivas (+5 Humanidade | Tensão Mental Dissipada | +1 Afeto com Ambas)."
            $ notificar_rpg("🍵 TRÉGUA DO CHÁ NO QUARTO", "+5 Humanidade | Tensão Dissipada | +1 Afeto Ambas", "#88ffcc")

    jump entrar_local_exploracao_bs

# ==============================================================================
# 5.3 MERCADO NEGRO DAS CALDEIRAS — VALÉRIA (SISTEMA DE BALCÃO VIVO & DIÁLOGO)
# ==============================================================================
label acao_mercado_negro_valeria:
    hide screen hud_exploracao_bs
    $ id_mob_atual = "valeria"
    $ sprite_mob_atual = "valeria cinica confiante meio corpo"
    $ nome_mob_atual = "Valéria"

    # Mostra Valéria respirando no falso Live2D (sprite_direita) com filtro de iluminação
    show valeria cinica confiante meio corpo at sprite_direita with dissolve
    if not getattr(store, "valeria_caldeiras_revelacao_ouvida", False):
        $ valeria_caldeiras_revelacao_ouvida = True
        $ th_voz("climax/valeria_caldeiras_revelacao")
        valeria "Aqui embaixo sob os canos de vapor, nobreza não compra pão, Vane. Só sucata, prata e aço frio te mantêm respirando."
    elif periodo == "Noite" and renpy.random.randint(1, 100) <= 50:
        $ th_voz("climax/valeria_aviso_grimm")
        valeria "Cuidado com as costas perto das caldeiras depois da meia-noite. A graxa naquelas válvulas não é óleo... é sangue coagulado."
    else:
        $ th_bark("valeria", "padrao")
        valeria "Procurando algo que a Diretoria confiscaria, Vane? Pague à vista ou pague em favores nas caldeiras."

label menu_loja_valeria_loop:
    if not getattr(store, "mercado_negro_vitrine_hoje", None):
        $ sortear_vitrine_mercado_negro()

    # Abre a vitrine tática visual com o grid de ícones 4x2 e Valéria à direita
    $ inicializar_abertura_loja("valeria")
    call screen vitrine_loja_tatica("valeria")
    $ _ret_val = _return

    if _ret_val == "pedir_fiado":
        $ bolsa_sangue_filtrado += 1
        $ th_dever("Valéria", "1x Bolsa de Sangue fiada (pagar 2x Sucatas de compensação)", "divida_valeria_sangue_fiado", "sucata", 2, "+2 Afeto de Valéria")
        $ th_sfx("frasco")
        show valeria cinica confiante meio corpo at sprite_direita with dissolve
        valeria "Toma a bolsa. Mas não se esqueça: agora você me deve duas sucatas, Vane."
        $ notificar_rpg("🩸 BOLSA FIADA", "Dívida contraída com Valéria: 2x Sucatas", "#ffaa00")
        jump menu_loja_valeria_loop

    if _ret_val == "sair_loja":
        hide valeria with dissolve
        jump entrar_local_exploracao_bs

    $ _est_hoje = getattr(store, "mercado_negro_estoque_hoje", {})
    $ _vit_hoje = getattr(store, "mercado_negro_vitrine_hoje", [])

    $ preco_sangue = calcular_preco_valeria("bolsa_sangue_filtrado")
    $ preco_kit = calcular_preco_valeria("kit_curativo")
    $ preco_passe = int(round(260 * obter_multiplicador_valeria()))

    $ _est_bolsa = _est_hoje.get("bolsa_sangue_filtrado", 0)
    $ _est_kit = _est_hoje.get("kit_curativo", 0)

    $ _s0 = _vit_hoje[0] if len(_vit_hoje) > 0 else None
    $ _s1 = _vit_hoje[1] if len(_vit_hoje) > 1 else None
    $ _s2 = _vit_hoje[2] if len(_vit_hoje) > 2 else None
    $ _s3 = _vit_hoje[3] if len(_vit_hoje) > 3 else None
    $ _s4 = _vit_hoje[4] if len(_vit_hoje) > 4 else None

    python:
        def _rotulo_slot_valeria(slot_info):
            if not slot_info:
                return None, None, 0, 0
            sid = slot_info["id"]
            qtd = _est_hoje.get(sid, 0)
            if qtd <= 0:
                return None, None, 0, 0
            obj = CATALOGO_ITENS.get(sid)
            preco = calcular_preco_valeria(sid, slot_info.get("mod_preco", 1.0))
            tag = (" [" + slot_info["tag_lote"] + "]") if slot_info.get("tag_lote") else ""
            if obj:
                return f"{obj.icone} {obj.nome} (${preco} | Estoque: {qtd}x){tag}", obj, preco, qtd
            return None, None, 0, 0

        _txt_s0, _obj_s0, _p_s0, _q_s0 = _rotulo_slot_valeria(_s0)
        _txt_s1, _obj_s1, _p_s1, _q_s1 = _rotulo_slot_valeria(_s1)
        _txt_s2, _obj_s2, _p_s2, _q_s2 = _rotulo_slot_valeria(_s2)
        _txt_s3, _obj_s3, _p_s3, _q_s3 = _rotulo_slot_valeria(_s3)
        _txt_s4, _obj_s4, _p_s4, _q_s4 = _rotulo_slot_valeria(_s4)

    $ reg_dividas = getattr(store, "registro_dividas_ativas", {})
    $ divida_quitada = (
        ("divida_valeria_sangue_fiado" in reg_dividas and reg_dividas["divida_valeria_sangue_fiado"].quitada)
        or ("divida_valeria_favores" in reg_dividas and reg_dividas["divida_valeria_favores"].quitada)
    )
    $ confia_em_victor = (status_valeria.vinculo_sangue >= 15 or status_valeria.afeto >= 8 or divida_quitada)

    menu:
        "🩸 [[ESSENCIAL]] Bolsa de Sangue Filtrado ($[preco_sangue] | Restam [_est_bolsa]x hoje)" if _est_bolsa > 0:
            if dinheiro_jogador >= preco_sangue:
                $ dinheiro_jogador -= preco_sangue
                $ bolsa_sangue_filtrado += 1
                $ store.mercado_negro_estoque_hoje["bolsa_sangue_filtrado"] = max(0, _est_bolsa - 1)
                $ th_sfx("moedas_ouro")
                show valeria cinica pirulito meio corpo at sprite_direita with dissolve
                valeria "Bolsa intacta e lacrada. Beba longe dos fiscais da ronda se não quiser problemas."
                $ notificar_rpg("🩸 BOLSA ADQUIRIDA", f"-${preco_sangue} Créditos | +1 Bolsa Filtrada (Estoque esgotado hoje)", "#00ffcc")
            else:
                show valeria cinica confiante meio corpo at sprite_direita with dissolve
                valeria "Está sem $[preco_sangue] no bolso, Vane. Ou você traz as moedas, ou assume no fiado ali embaixo."
            jump menu_loja_valeria_loop

        "🩸 Pedir Bolsa Fiada a Valéria (Assumir Dívida: pagar 2x Sucatas depois)" if dinheiro_jogador < preco_sangue and ("divida_valeria_sangue_fiado" not in registro_dividas_ativas or registro_dividas_ativas["divida_valeria_sangue_fiado"].quitada):
            $ bolsa_sangue_filtrado += 1
            $ th_dever("Valéria", "1x Bolsa de Sangue fiada (pagar 2x Sucatas de compensação)", "divida_valeria_sangue_fiado", "sucata", 2, "+2 Afeto de Valéria")
            $ th_sfx("frasco")
            show valeria cinica confiante meio corpo at sprite_direita with dissolve
            valeria "Toma a bolsa. Mas não se esqueça: agora você me deve duas sucatas, Vane."
            $ notificar_rpg("🩸 BOLSA FIADA", "Dívida contraída com Valéria: 2x Sucatas", "#ffaa00")
            jump menu_loja_valeria_loop

        "🩹 [[ESSENCIAL]] Kit de Curativos Médicos ($[preco_kit] | Restam [_est_kit]x hoje)" if _est_kit > 0:
            if dinheiro_jogador >= preco_kit:
                $ dinheiro_jogador -= preco_kit
                $ kit_curativo += 1
                $ store.mercado_negro_estoque_hoje["kit_curativo"] = max(0, _est_kit - 1)
                $ th_sfx("moedas_ouro")
                show valeria amigavel neutra meio corpo at sprite_direita with dissolve
                valeria "Gaze, esparadrapo e álcool hospitalar desviado da enfermaria. Bem mais barato que lá em cima, né?"
                $ notificar_rpg("🩹 KIT ADQUIRIDO", f"-${preco_kit} Créditos | +1 Kit de Curativos no inventário", "#00ffcc")
            else:
                valeria "Falta crédito para o kit ($[preco_kit]), garoto."
            jump menu_loja_valeria_loop

        "[_txt_s0]" if _txt_s0 is not None:
            if dinheiro_jogador >= _p_s0:
                $ dinheiro_jogador -= _p_s0
                $ _obj_s0.adicionar(1)
                $ store.mercado_negro_estoque_hoje[_obj_s0.id] = max(0, _q_s0 - 1)
                $ th_sfx("moedas_ouro")
                show valeria cinica confiante meio corpo at sprite_direita with dissolve
                valeria "Negócio fechado. Guardando o recibo no único lugar seguro: na memória."
                $ notificar_rpg(f"{_obj_s0.icone} COMPRA NO LOTE", f"-${_p_s0} | +1 {_obj_s0.nome}", "#00ffcc")
            else:
                valeria "Precisa de $[_p_s0] para levar [_obj_s0.nome], bolsista. Vai cavar uns armários."
            jump menu_loja_valeria_loop

        "[_txt_s1]" if _txt_s1 is not None:
            if dinheiro_jogador >= _p_s1:
                $ dinheiro_jogador -= _p_s1
                $ _obj_s1.adicionar(1)
                $ store.mercado_negro_estoque_hoje[_obj_s1.id] = max(0, _q_s1 - 1)
                $ th_sfx("moedas_ouro")
                show valeria cinica pirulito meio corpo at sprite_direita with dissolve
                valeria "Mercadoria quente da bancada. Faz bom proveito disso antes que o toque de recolher aperte."
                $ notificar_rpg(f"{_obj_s1.icone} COMPRA NO LOTE", f"-${_p_s1} | +1 {_obj_s1.nome}", "#00ffcc")
            else:
                valeria "Sem $[_p_s1] na mão, o lote fica no caixote."
            jump menu_loja_valeria_loop

        "[_txt_s2]" if _txt_s2 is not None:
            if dinheiro_jogador >= _p_s2:
                $ dinheiro_jogador -= _p_s2
                $ _obj_s2.adicionar(1)
                $ store.mercado_negro_estoque_hoje[_obj_s2.id] = max(0, _q_s2 - 1)
                $ th_sfx("moedas_ouro")
                show valeria cinica suspensorios meio corpo at sprite_direita with dissolve
                valeria "Peça rara para quem entra em Zona Vermelha. Não perde a cabeça lá dentro, Vane."
                $ notificar_rpg(f"{_obj_s2.icone} CONTRABANDO TÁTICO", f"-${_p_s2} | +1 {_obj_s2.nome}", "#00ffcc")
            else:
                valeria "Falta cacife para esse brinquedo ($[_p_s2]). Volta com moedas."
            jump menu_loja_valeria_loop

        "[_txt_s3]" if _txt_s3 is not None:
            if dinheiro_jogador >= _p_s3:
                $ dinheiro_jogador -= _p_s3
                $ _obj_s3.adicionar(1)
                $ store.mercado_negro_estoque_hoje[_obj_s3.id] = max(0, _q_s3 - 1)
                $ th_sfx("moedas_ouro")
                show valeria cinica pirulito meio corpo at sprite_direita with dissolve
                valeria "Consegui desviar uma unidade única desse lote. Aproveita antes que outro comprador leve."
                $ notificar_rpg(f"{_obj_s3.icone} LOTE RARO ADQUIRIDO", f"-${_p_s3} | +1 {_obj_s3.nome}", "#ffd700")
            else:
                valeria "Item raro sai caro mesmo ($[_p_s3]). Guarda uma reserva se quiser levar."
            jump menu_loja_valeria_loop

        "[_txt_s4]" if _txt_s4 is not None:
            if dinheiro_jogador >= _p_s4:
                $ dinheiro_jogador -= _p_s4
                $ _obj_s4.adicionar(1)
                $ store.mercado_negro_estoque_hoje[_obj_s4.id] = max(0, _q_s4 - 1)
                $ th_sfx("moedas_ouro")
                show valeria leve sorriso pirulito meio corpo at sprite_direita with dissolve
                valeria "Olha só o cavalheiro comprando artigo fino no meio de um apocalipse... Vai agradar quem com isso, hein?"
                $ notificar_rpg(f"{_obj_s4.icone} PRESENTE ADQUIRIDO", f"-${_p_s4} | +1 {_obj_s4.nome}", "#ff99cc")
            else:
                valeria "Luxo custa caro ($[_p_s4]), garoto. Primeiro paga suas contas."
            jump menu_loja_valeria_loop

        "🎟️ Comprar Passe Clandestino do Fundão ($[preco_passe])" if not tem_passe_fada_verde and confia_em_victor and dinheiro_jogador >= preco_passe:
            $ dinheiro_jogador -= preco_passe
            $ tem_passe_fada_verde = True
            $ th_sfx("moedas_ouro")
            show valeria casaco verde sorriso meio corpo at sprite_direita with dissolve
            valeria "Toma o passe da Fada Verde. Só não cause confusão lá embaixo, Vane. Minha reputação está em jogo."
            $ notificar_rpg("🎟️ PASSE ADQUIRIDO", f"-${preco_passe} Créditos | Acesso desbloqueado ao Bar da Fada Verde!", "#ffd700")
            jump menu_loja_valeria_loop

        "🏗️ [[ GESTÃO DO COVIL & CONTRABANDO ]] (Reformas das Caldeiras e Informantes)":
            call screen painel_gestao_caldeiras(em_call=True)
            jump menu_loja_valeria_loop

        "Retornar à exploração das Caldeiras":
            hide valeria with dissolve
            jump entrar_local_exploracao_bs

# ------------------------------------------------------------------------------
# AÇÃO ACADÊMICA: CUMPRIR TAREFA ESCOLAR HONESTAMENTE
# ------------------------------------------------------------------------------
label acao_cumprir_tarefa_academica:
    hide screen hud_exploracao_bs
    $ passos_restantes_periodo = max(0, passos_restantes_periodo - 1)
    $ intelecto += 1
    $ tarefa_academica_pendente = False
    $ th_sfx("vasculhar_gaveta_abrir")
    "Você se acomoda em uma mesa isolada, espalhando folhas de pergaminho, pena e o tinteiro de ferro da Academia."
    "Durante a hora seguinte, você redige suas teses e análises sobre '[nome_tarefa_academica]' com disciplina cirúrgica."
    "Ao selar a folha com cera escura e depositá-la na urna de entregas acadêmicas, sua fachada como estudante exemplar se fortalece perante os mestres e o Grêmio."
    $ notificar_rpg("📚 TAREFA CONCLUÍDA", "+1 Intelecto | Fachada Escolar Preservada | 1 Passo Gasto", "#88ccff")
    jump entrar_local_exploracao_bs

label acao_consultar_enfermaria:
label menu_enfermaria_academia:
    hide screen hud_exploracao_bs
    $ local_atual = "enfermaria"
    call restaurar_fundo_local_atual
    $ emilia_sabe_vampiro = getattr(store, "pacto_emilia_ativo", False) or getattr(store, "estagio_emilia", 1) >= 2 or (getattr(store, "status_emilia", None) and (status_emilia.vinculo_sangue > 0 or status_emilia.afeto >= 5))
    if periodo in ["Manhã", "Tarde"] and emilia_sabe_vampiro and not getattr(store, "ev_triagem_enfermaria_visto", False):
        jump ev_c02_triagem_enfermaria

    $ id_mob_atual = "mob_enfermeira"
    $ sprite_mob_atual = "mob enfermeira neutra"
    $ nome_mob_atual = "Enfermeira Clara"

    show mob enfermeira neutra at sprite_direita with dissolve

    if not getattr(store, "saudou_enfermeira_visita", False):
        $ saudou_enfermeira_visita = True
        $ th_bark_mob("abordagem")

        if humanidade < 35 or fome_sangue < 20:
            mob_enfermeira "F-Fique longe do armário de sedativos, Vane! Pegue as chaves da câmara de sangue... só não rasgue a minha garganta!"
        elif periodo == "Noite":
            mob_enfermeira "A enfermaria fecha após as oito, Vane... Se os monitores do Grêmio virem você aqui a esta hora, vão achar que veio saquear os estoques de plasma."
        elif humanidade < 65:
            mob_enfermeira "Nenhum pulso sob o estetoscópio, pele fria como gelo e pupilas dilatadas... A Presidente Elara me avisou que seu quadro clínico havia mudado."
        else:
            mob_enfermeira "Arregace a manga, senhor Vane... Um doador raro como você ganha abono de falta e uma xícara de chá doce depois da agulha."
    else:
        mob_enfermeira "Precisa de mais alguma coisa no dispensário ou curativos, senhor Vane?"

label menu_enfermaria_loop:
    # Abre o dispensário tático com Dra. Clara Vance e o grid hospitalar 4x2
    $ inicializar_abertura_loja("enfermaria")
    call screen vitrine_loja_tatica("enfermaria")
    $ _ret_enf = _return

    if _ret_enf == "sair_loja":
        hide mob enfermeira with dissolve
        jump entrar_local_exploracao_bs

    $ _p_enf_bolsa = obter_agio_enfermaria(165)
    $ _p_enf_kit = obter_agio_enfermaria(105)
    $ _p_enf_seq = obter_agio_enfermaria(140)
    $ _p_enf_hemo = int(round(90 * (0.80 if paciente_inadimplente_taxa() else 1.0)))
    $ _rest_bolsas_enf = max(0, 1 - getattr(store, "enfermaria_bolsas_hoje", 0))
    $ _rest_kits_enf = max(0, 1 - getattr(store, "enfermaria_kits_hoje", 0))
    $ _sequelas_medicas = [s for s in getattr(store, "sequelas_ativas", []) if s.get("id") != "taxa_inadimplente"]

    menu:
        "🛒 Reabrir Dispensário da Enfermaria (Vitrine Tática)":
            jump menu_enfermaria_loop
        "🩸 Comprar Bolsa de Sangue Filtrado ($[_p_enf_bolsa] | Ágio Oficial — [_rest_bolsas_enf]x/dia)" if _rest_bolsas_enf > 0:
            if dinheiro_jogador >= _p_enf_bolsa:
                $ dinheiro_jogador -= _p_enf_bolsa
                $ bolsa_sangue_filtrado += 1
                $ enfermaria_bolsas_hoje += 1
                show mob enfermeira desconfiada at sprite_direita with dissolve
                $ th_voz("climax/enfermeira_climax_03_suborno")
                mob_enfermeira "O ágio clínico cobre meu silêncio e o lacre da câmara fria. Esconda sob o sobretudo antes que o Conselho cheque o inventário."
                $ notificar_rpg("🩸 BOLSA ADQUIRIDA (ENFERMARIA)", f"-${_p_enf_bolsa} Créditos | +1 Bolsa Filtrada (Limite diário atingido)", "#00ffcc")
            else:
                show mob enfermeira neutra at sprite_direita with dissolve
                mob_enfermeira "Sem $[_p_enf_bolsa] créditos para a taxa clínica, não posso abrir o refrigerador hoje, Sr. Vane."
            jump menu_enfermaria_loop

        "🩹 Comprar Kit de Curativos e Sutura ($[_p_enf_kit] | [_rest_kits_enf]x/dia)" if _rest_kits_enf > 0:
            if dinheiro_jogador >= _p_enf_kit:
                $ dinheiro_jogador -= _p_enf_kit
                $ kit_curativo += 1
                $ enfermaria_kits_hoje += 1
                show mob enfermeira sorrindo at sprite_direita with dissolve
                mob_enfermeira "Bandagens hospitalares e fio estéril. A tabela da Fundação não é generosa como os desvios do subsolo."
                $ notificar_rpg("🩹 KIT ADQUIRIDO (ENFERMARIA)", f"-${_p_enf_kit} Créditos | +1 Kit de Curativos (Limite diário atingido)", "#00ffcc")
            else:
                mob_enfermeira "Você precisa de $[_p_enf_kit] créditos para este conjunto cirúrgico."
            jump menu_enfermaria_loop

        "🩹 Tratar Sequela Física com Curativos e Antisséptico ($[_p_enf_seq])" if _sequelas_medicas and dinheiro_jogador >= _p_enf_seq:
            $ dinheiro_jogador -= _p_enf_seq
            $ hp_jogador = min(hp_jogador_max, hp_jogador + 20)
            $ _seq_curada = _sequelas_medicas[0]["nome"]
            $ curar_sequela(_sequelas_medicas[0]["id"])
            show mob enfermeira sorrindo at sprite_direita with dissolve
            mob_enfermeira "Curativos trocados e sutura higienizada. Tente não arrebentar esses pontos nos corredores."
            $ notificar_rpg("🩹 SEQUELA TRATADA", f"Condição [[{_seq_curada}]] neutralizada | -${_p_enf_seq} | +20 HP", "#00ffcc")
            jump menu_enfermaria_loop

        "🔬 Permitir Coleta para Hemograma (+$[_p_enf_hemo] / -15 HP / +10%% Exposição)" if not getattr(store, "coleta_enfermeira_hoje", False) and hp_jogador > 20:
            if any(s.get("id") == "anemia_recente" for s in getattr(store, "sequelas_ativas", [])):
                show mob enfermeira desconfiada at sprite_direita with dissolve
                $ th_voz("climax/enfermeira_recusa_anemia_completa")
                mob_enfermeira "De jeito nenhum, Sr. Vane. Seus lábios estão lívidos e sua pressão arterial mal registra no esfigmomanômetro."
                mob_enfermeira "Se eu espetar essa veia com esse quadro de anemia aguda, você desmaia na maca antes de receber seus créditos. Descanse por alguns turnos e alimente-se antes de doar novamente."
                $ notificar_rpg("⚠️ RECUSA CLÍNICA", "Bloqueado: Condição de Anemia Recente ativa!", "#ff4444")
            else:
                $ coleta_enfermeira_hoje = True
                $ dinheiro_jogador += _p_enf_hemo
                $ hp_jogador = max(15, hp_jogador - 15)
                $ exposicao = min(100, exposicao + 10)
                $ aplicar_sequela("anemia_recente", "Anemia Traumática Recente", "Extração de sangue Rh-Nulo na enfermaria.", "-15 HP Máximo / Fraqueza transitória")
                $ store.turnos_anemia_recente = 2
                show mob enfermeira desconfiada at sprite_direita with dissolve
                $ th_voz("climax/enfermeira_climax_02_sangue_dourado")
                mob_enfermeira "Inacreditável... Sangue Rh-nulo puro, fundido a uma vitae antediluviana. A coleta vai deixá-lo tonto por algumas horas, mas o Conselho paga pela amostra."
                "A agulha de prata drena um frasco a vácuo inteiro das suas veias. Uma tontura gelada percorre seus joelhos (-15 HP)."
                $ notificar_rpg("🔬 AMOSTRA COLETADA", f"+${_p_enf_hemo} Créditos | -15 HP | +10%% Exposição | Sequela: Anemia Recente (2 turnos)", "#ffd700")
            jump menu_enfermaria_loop

        "🩺 Olhar os calouros descansando sob as cortinas":
            $ th_voz("climax/enfermeira_climax_04_campanha")
            mob_enfermeira "Não dê atenção ao bolsista atrás da cortina amarela. Duas bolsas de O-negativo em jejum sempre deixam os calouros tontos... A Presidente Elara precisa manter o estoque abastecido."
            "Atrás da cortina amarela, um estudante magro e pálido geme fracamente, segurando o algodão manchado contra a dobra do braço:"
            $ th_voz("mobs/mob_calouro_anemico_apelo")
            "Calouro Anêmico" "Por favor... não me empurrem atrás da cortina de novo. Eu não tenho mais sangue para passar em outro exame..."
            jump menu_enfermaria_loop

        "🩸 Drenagem Furtiva (Alimentar-se da Enfermeira / Banquete Clínico)" if fome_sangue < 70 and not getattr(store, "drenou_enfermeira_hoje", False):
            $ drenou_enfermeira_hoje = True
            with vpunch
            with flash_red
            $ th_sfx("heartbeat")
            show mob enfermeira medo at sprite_direita with dissolve
            $ th_bark_mob("mordida")
            mob_enfermeira "Ahn...! Direto na carótida... A seringa era para as suas veias... não para a minha garganta..."

            "Num reflexo predatório fulminante, você encurrala a hematologista contra a bancada de medicamentos. O cheiro de éter e iodopovidona se mistura ao calor da artéria pulsando sob seus dedos."
            "Suas presas perfuram a carótida com precisão cirúrgica. O sangue da médica é frio, denso e analítico, anestesiando a queimação na sua garganta e clareando seus pensamentos."

            $ fome_sangue = min(100, fome_sangue + 30)
            $ hp_jogador = min(hp_jogador_max, hp_jogador + 20)
            $ intelecto += 1
            $ humanidade = max(0, humanidade - 2)
            $ exposicao = min(100, exposicao + 10)
            $ GerenciadorRuina.adicionar_ruina(3, "Transe Sanguíneo na Enfermaria")

            # Transição para o Transe Hipnótico da Vítima
            show mob enfermeira transe at sprite_direita with dissolve
            "Antes que Clara possa gritar ou desabar, você fixa os olhos nos dela. A pulsação carmesim do sangue ancestral nubla sua consciência com um torpor dócil."
            mob_enfermeira "O... ar... Apenas uma queda de pressão... Tenho que... repor os lotes de soro..."

            # Aparição e Reação de Victor pós-transe hipnótico
            show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve
            victor "(O sangue dela tem o amargor do café forte e o cálculo frio da Fundação... mas acalmou a Besta a tempo.)"
            show expression obter_sprite_victor("confiante") as victor at sprite_esquerda with dissolve
            victor "(O transe hipnótico apagou cada segundo. Quando ela despertar dessa névoa, vai achar que teve apenas um desmaio por exaustão do plantão.)"
            "Você passa o polegar pelos lábios, limpando o filete escarlate, e ajeita o estetoscópio no jaleco de Clara enquanto ela repousa dócil e semiconsciente sobre a mesa."

            $ notificar_rpg("🩸 BANQUETE CLÍNICO", "+30%% Saciedade | +20 HP | +1 Intelecto | -2 Humanidade | Clara hipnotizada", "#ff2244")
            $ saudou_enfermeira_visita = False
            hide victor with dissolve
            hide mob with dissolve
            jump entrar_local_exploracao_bs

        "Retornar à exploração da Enfermaria":
            $ saudou_enfermeira_visita = False
            hide mob with dissolve
            jump entrar_local_exploracao_bs

# ==============================================================================

# 8. O "PASSO" DE INVESTIGAÇÃO (HEROÍNA -> MOB FIGURANTE -> COMBATE -> LOOT)

# ==============================================================================

label investigar_passo_bs:
    if local_atual == "dormitorio":
        "O dormitório é um refúgio seguro isolado das patrulhas. Aqui você não precisa gastar passos para vasculhar corredores."
        jump entrar_local_exploracao_bs

    hide screen hud_exploracao_bs

    if passos_restantes_periodo <= 0:

        "O tempo deste período se esgotou enquanto você explorava os corredores."

        jump avancar_turno_mapa

    $ passos_restantes_periodo -= 1
    if passos_restantes_periodo == 0:
        $ notificar_rpg("⏳ TEMPO ESGOTADO", "Você gastou o último passo deste período! O toque de recolher se aproxima.", "#ff4444")
    if local_atual in ["patio_fonte", "patio_arvore", "portoes_praca", "rua_portao", "cemiterio_nevoa", "jardim_estufas"]:
        $ th_sfx("passos_gravilha")
    elif local_atual in ["biblioteca", "sala_ocultismo", "salao_gremio", "enfermaria", "caldeiras"]:
        $ th_sfx("vasculhar_gaveta_abrir")
    else:
        $ th_sfx("passos_madeira")

    # Animação cinematográfica de lunge / passada estilo Black Survival
    show layer master at bs_investigar_passo
    $ renpy.pause(0.58, hard=True)
    show layer master

    # 1. VERIFICA SE HÁ HEROÍNA NA SALA (50% de chance)

    $ rolo_encontro_heroina = renpy.random.randint(1, 100)

    if rolo_encontro_heroina <= 50:

        if loc_mestra == local_atual:

            "Ao avançar pela penumbra da sala, você sente o aroma inconfundível de mirra e sangue antigo."

            jump menu_encontro_lility

        elif loc_emilia == local_atual:

            "Seus passos ecoam pelo piso e você avista Emília organizando anotações de investigação."

            jump menu_encontro_emilia

        elif loc_valeria == local_atual:

            "Entre a fumaça e a luz baixa, Valéria apoia o cotovelo na bancada contando notas de dinheiro."

            jump menu_encontro_valeria

        elif loc_elara == local_atual:

            "O som frio de saltos sobre o mármore anuncia a presença da Presidente Elara inspecionando o setor."

            jump menu_encontro_elara

    # 1.5. ENCONTRO NARRATIVO COM NORA VASQUES NA CRIPTA DE VIDRO (COBAIA 31)

    if local_atual == "cripta_cofre" and not getattr(store, "nora_estabilizada_cripta", False) and not getattr(store, "nora_misericordia_concedida", False):

        jump encontro_nora_cela_cripta

    # 1.8. ENCONTROS NARRATIVOS ORGÂNICOS / WORLD OF HORROR (TEO & COBAIA 31)
    # Estritamente no corredor e em horário letivo diurno (Manhã/Tarde), nunca à noite ou no pátio!
    if local_atual in ["corredor_academia", "corredores_principais"] and periodo in ["Manhã", "Tarde"] and not getattr(store, "ev_divida_teo_fase1_visto", False) and (ruina_cain >= 10 or dia_atual >= 1) and renpy.random.randint(1, 100) <= 35:
        jump ev_c03_divida_teo_corredor

    if local_atual == "enfermaria" and getattr(store, "ev_triagem_enfermaria_visto", False) and not getattr(store, "ev_rastro_nora_enfermaria_visto", False):
        jump ev_rastro_oculto_nora_enfermaria

    # Ganchos Orgânicos dos 4 Novos Eventos de Alto DOOM (Fases III & IV — Estritamente no local canônico!)
    if local_atual == "biblioteca" and not getattr(store, "ev_c16_investigacao_lyra_visto", False) and ruina_cain >= 30 and periodo in ["Tarde", "Noite"]:
        jump ev_c16_investigacao_genealogica_lyra

    if local_atual == "catacumbas" and not getattr(store, "ev_c17_inundacao_agua_negra_visto", False) and ruina_cain >= 60:
        jump ev_c17_inundacao_agua_negra

    if local_atual == "patio_fonte" and not getattr(store, "ev_c18_vigilia_executores_visto", False) and ruina_cain >= 70 and periodo == "Noite":
        jump ev_c18_vigilia_executores_sombra

    if local_atual == "enfermaria" and not getattr(store, "ev_c19_laudo_clara_visto", False) and (ruina_cain >= 50 or getattr(store, "drenou_enfermeira_hoje", False)) and periodo in ["Tarde", "Noite"]:
        jump ev_c19_laudo_sincope_clara

    # 2. SORTEIO DE ENCONTRO COM FIGURANTE (MOBU KYARA / SEM ROSTO) — 35% de chance (ou 60% se em Frenesi!)

    $ chance_mob = 60 if fome_sangue < 25 else 35

    if renpy.random.randint(1, 100) <= chance_mob and local_atual not in ["sala_musica", "cripta_cofre"]:

        jump encontro_mob_figurante

    # 2.5. ALUCINAÇÃO SENSORIAL DA SEDE CRÍTICA (Frenesi < 20%)

    if fome_sangue < 20 and renpy.random.randint(1, 100) <= 30:

        jump alucinacao_fome_critica_bs

    # 3. SORTEIO GERAL DE BLACK SURVIVAL (COMBATE vs. EVENTO .ITO vs. LOOT vs. RUMOR)

    $ rolo_bs = renpy.random.randint(1, 100)

    $ limite_combate = 65 if local_atual in ["catacumbas", "cripta_cofre"] else (45 if periodo == "Noite" else (25 if periodo == "Tarde" else 10))

    if rolo_bs <= limite_combate:

        jump emboscada_aleatoria_bs

    elif rolo_bs <= min(80, limite_combate + 25):

        jump micro_evento_ito_corredor

    elif rolo_bs <= (95 if "olhos_no_escuro" in getattr(store, "perks_desbloqueados", ()) else 88):

        jump loot_aleatorio_bs

    else:

        jump pista_ambiental_bs

label loot_aleatorio_bs:
    $ th_sfx("vasculhar_objetos_mexer")

    $ sorteio_item = renpy.random.randint(1, 100)

    if local_atual == "dormitorio":

        if sorteio_item <= 60:

            $ sucata_eletronica += 1

            "🔍 (LOOT ENCONTRADO): Você desmonta uma fonte queimada no fundo do armário e obtém (+1 Sucata Eletrônica)!"

        else:

            $ kit_curativo += 1

            "🔍 (LOOT ENCONTRADO): Você acha gazes limpas no armário do corredor (+1 Kit de Curativos)!"

    elif local_atual in ["biblioteca", "sala_ocultismo"]:

        if sorteio_item <= 60:

            $ giz_protecao += 1

            if local_atual == "sala_ocultismo":
                "🔍 (LOOT ENCONTRADO): Dentro de uma gaveta do Clube de Ocultismo, você recolhe (+1 Giz de Proteção Rúnico)!"
            else:
                "🔍 (LOOT ENCONTRADO): Escondido atrás de um tomo antigo nas estantes da Biblioteca, você recolhe (+1 Giz de Proteção Rúnico)!"

        else:

            $ conhecimento_oculto += 1

            "🔍 (PISTA OCULTA): Você lê um registro censurado sobre o eclipse anterior (+1 Conhecimento Oculto)."

    elif local_atual in ["caldeiras", "sala_caldeiras", "bar_fada_verde"]:

        if sorteio_item <= 35:

            $ sucata_eletronica += 1

            "🔍 (LOOT ENCONTRADO): Você recolhe cabos de cobre e capacitores perto da fornalha (+1 Sucata Eletrônica)!"

        elif sorteio_item <= 60:

            $ achado_grana = renpy.random.randint(30, 65)

            $ dinheiro_jogador += achado_grana

            "🔍 (LOOT ENCONTRADO): Você encontra uma carteira escondida atrás dos dutos (+$[achado_grana])!"

        elif sorteio_item <= 80:

            $ dose_absinto += 1

            "🔍 (LOOT ENCONTRADO): Uma garrafa lacrada de Absinto Esmeralda estava sob o balcão (+1 Dose de Absinto)!"

        else:

            $ bolsa_sangue_adulterado += 1

            "🔍 (LOOT ENCONTRADO): Perto dos tubos de descarte, você recupera uma bolsa de sangue clandestino (+1 Sangue Adulterado)! Use um Filtro Rúnico na Bancada para purificá-lo com segurança."

    elif local_atual == "catacumbas" and fragmentos_chave_cripta < 3 and renpy.random.randint(1, 100) <= 60:

        $ fragmentos_chave_cripta += 1

        if fragmentos_chave_cripta == 1:

            "🗝️ [[FRAGMENTO DA CHAVE DAS PROFUNDEZAS (1/3)]]: Entre os ossos e terra úmida de uma sepultura violada, você desenterra uma haste de prata e obsidiana com ranhuras em espiral."

            $ notificar_rpg("🗝️ CHAVE DAS PROFUNDEZAS", "Primeiro fragmento rúnico recuperado (1/3)!", "#00ffcc")

        elif fragmentos_chave_cripta == 2:

            "🗝️ [[FRAGMENTO DA CHAVE DAS PROFUNDEZAS (2/3)]]: Atrás de uma gárgula partida, você encontra um cilindro de latão marcado com glifos de contenção. Ele ressoa com a primeira peça!"

            $ notificar_rpg("🗝️ CHAVE DAS PROFUNDEZAS", "Segundo fragmento rúnico recuperado (2/3)!", "#00ffcc")

        else:

            $ desbloqueou_cripta_cofre = True

            "🗝️ [[SELO COMPLETO DAS PROFUNDEZAS (3/3)]]: Sob o altar em ruínas, você recupera a engrenagem mística! As três peças estalam e se fundem com um brilho carmesim! O Cofre de Contenção mais profundo agora está acessível no Subsolo!"

            $ notificar_rpg("🔑 CRIPTA DESBLOQUEADA", "A Tumba Selada das Profundezas foi destrancada no Mapa!", "#ffd700")

    elif local_atual in ["cemiterio_nevoa", "catacumbas", "cripta_cofre"]:

        if sorteio_item <= 30:

            $ achado_grana = renpy.random.randint(45, 95)

            $ dinheiro_jogador += achado_grana

            "🔍 (LOOT ENCONTRADO): Você encontra moedas antigas entre os escombros (+$[achado_grana])!"

        elif sorteio_item <= 55:

            $ kit_curativo += 1

            "🔍 (LOOT ENCONTRADO): Você encontra suprimentos médicos de um explorador caído (+1 Kit de Curativos)!"

        elif sorteio_item <= 75:

            $ giz_protecao += 1

            "🔍 (LOOT ENCONTRADO): Você recolhe um giz consagrado intacto (+1 Giz de Proteção Rúnico)!"

        else:

            $ bolsa_sangue_adulterado += 1

            "🔍 (LOOT ENCONTRADO): Entre as frestas úmidas das catacumbas, você desenterra (+1 Sangue Adulterado)! Pode ser purificado com um Filtro Rúnico."

    elif local_atual == "patio_arvore":

        if sorteio_item <= 42:

            $ giz_protecao += 1

            "🔍 (LOOT ENCONTRADO): Sob as copas das árvores centenárias, você recolhe fragmentos de (+1 Giz de Proteção Rúnico)!"

        elif sorteio_item <= 72:

            $ achado_grana = renpy.random.randint(30, 75)

            $ dinheiro_jogador += achado_grana

            "🔍 (LOOT ENCONTRADO): Entre as folhas caídas da alameda, você encontra moedas de alunos distraídos (+$[achado_grana])!"

        elif sorteio_item <= 90:

            $ kit_curativo += 1

            "🔍 (LOOT ENCONTRADO): Você encontra um estojo de primeiros socorros abandonado em um banco de pedra (+1 Kit de Curativos)!"

        else:

            $ presente_flores += 1

            $ notificar_rpg("🎁 ACHADO RARO", "Lírios Negros intactos recolhidos junto às raízes (+1).", "#c0a0ff")

            "🔍 (LOOT ENCONTRADO): Entre o musgo úmido das raízes, você colhe um raro (+1 Buquê de Lírios Negros) quase intacto!"

    elif local_atual == "rua_portao":

        if sorteio_item <= 40:

            $ sucata_eletronica += 1

            "🔍 (LOOT ENCONTRADO): Próximo aos postes e fiação externa da avenida, você recolhe cabos de cobre (+1 Sucata Eletrônica)!"

        elif sorteio_item <= 70:

            $ achado_grana = renpy.random.randint(40, 90)

            $ dinheiro_jogador += achado_grana

            "🔍 (LOOT ENCONTRADO): Você acha uma nota dobrada junto ao meio-fio molhado (+$[achado_grana])!"

        elif sorteio_item <= 85:

            $ dose_absinto += 1

            "🔍 (LOOT ENCONTRADO): Um frasco lacrado de bebida deixado por contrabandistas perto do ponto de ônibus (+1 Dose de Absinto)!"

        else:

            $ kit_curativo += 1

            "🔍 (LOOT ENCONTRADO): Suprimentos médicos descartados perto de uma ambulância estacionada (+1 Kit de Curativos)!"

    else:

        if sorteio_item <= 50:

            $ achado_grana = renpy.random.randint(35, 80)

            $ dinheiro_jogador += achado_grana

            "🔍 (LOOT ENCONTRADO): Você vasculha os armários do setor e recupera (+$[achado_grana])!"

        else:

            $ giz_protecao += 1

            "🔍 (LOOT ENCONTRADO): Você recolhe um fragmento de (+1 Giz de Proteção Rúnico)!"

    if "olhos_no_escuro" in getattr(store, "perks_desbloqueados", ()):

        $ bonus_olhos = renpy.random.randint(15, 35)

        $ dinheiro_jogador += bonus_olhos

        $ notificar_rpg("👁️ OLHOS NO ESCURO", f"+${bonus_olhos} recolhido nas sombras da sala.", "#44ddff")

        "👁️ (Olhos no Escuro): Seus sentidos apurados revelam (+$[bonus_olhos]) escondidos na penumbra!"

    call screen hud_exploracao_bs

    jump abrir_mapa_tatico

label pista_ambiental_bs:

    # 1. Checagem contextual de pistas para os Casos de Horror (World of Horror)

    if local_atual in ["cemiterio_nevoa", "patio_fonte", "portoes_praca", "patio_arvore", "rua_portao"] and not MISTERIOS_ACADEMIA["hachishaku"].resolvido and MISTERIOS_ACADEMIA["hachishaku"].pistas_coletadas < 3:

        if MISTERIOS_ACADEMIA["hachishaku"].pistas_coletadas == 0:

            $ MISTERIOS_ACADEMIA["hachishaku"].coletar_pista("Pegadas desproporcionais e galhos estalados na copa das árvores.")

            "🕯️ [[PISTA DO CASO — A MULHER DE OITO PÉS (1/3)]]: Sob a névoa fria, você encontra pegadas de barro desproporcionais e galhos quebrados a quase três metros de altura. Um riso oco — 'Po... po... po...' — estremece o ar antes de sumir."

        elif MISTERIOS_ACADEMIA["hachishaku"].pistas_coletadas == 1:

            $ MISTERIOS_ACADEMIA["hachishaku"].coletar_pista("Entalhe na lápide sobre fraqueza contra barreira de sal.")

            "🕯️ [[PISTA DO CASO — A MULHER DE OITO PÉS (2/3)]]: Em uma lápide gótica rachada, você decifra um aviso entalhado: 'A aparição colossal persegue quem carrega sangue duplo. Ela não ultrapassa círculos consagrados com sal.' Pista registrada!"

        else:

            $ MISTERIOS_ACADEMIA["hachishaku"].coletar_pista("Fita rasgada do chapéu de palha com ectoplasma e cinzas.")

            "🕯️ [[PISTA DO CASO — A MULHER DE OITO PÉS (3/3)]]: Presa aos espinhos da grade, você recolhe a fita rasgada do chapéu de palha da assombração! A presença dela foi fixada no CEMITÉRIO DA NÉVOA à Noite!"

    elif local_atual in ["caldeiras", "sala_caldeiras", "bar_fada_verde"] and not MISTERIOS_ACADEMIA["lote_necrotico"].resolvido and MISTERIOS_ACADEMIA["lote_necrotico"].pistas_coletadas < 3:

        if MISTERIOS_ACADEMIA["lote_necrotico"].pistas_coletadas == 0:

            $ MISTERIOS_ACADEMIA["lote_necrotico"].coletar_pista("Bolsas descartadas com resíduo cáustico esverdeado nos drenos.")

            "🧪 [[PISTA DO CASO — O LOTE NECRÓTICO (1/3)]]: Perto da fornalha, você encontra bolsas de sangue vazias contendo um lodo esverdeado e borbulhante. O cheiro é de ácido sulfúrico e reagente clandestino."

        elif MISTERIOS_ACADEMIA["lote_necrotico"].pistas_coletadas == 1:

            $ MISTERIOS_ACADEMIA["lote_necrotico"].coletar_pista("Fórmula química adulterada da Turma do Fundão.")

            "🧪 [[PISTA DO CASO — O LOTE NECRÓTICO (2/3)]]: Atrás de um tonel de óleo, você acha uma fórmula manuscrita: 'Misturar solvente necrosado barateia a cota. Se os novatos enlouquecerem na fome, ninguém vai suspeitar.' Pista anotada!"

        else:

            $ MISTERIOS_ACADEMIA["lote_necrotico"].coletar_pista("Rastro químico até a ala de válvulas secundárias.")

            "🧪 [[PISTA DO CASO — O LOTE NECRÓTICO (3/3)]]: Manchas fosforescentes revelam o laboratório do Alquimista Renegado! O confronto decisivo está disponível nas CALDEIRAS!"

    elif local_atual in ["biblioteca", "sala_musica"] and not MISTERIOS_ACADEMIA["partitura_carnal"].resolvido and MISTERIOS_ACADEMIA["partitura_carnal"].pistas_coletadas < 3:

        if MISTERIOS_ACADEMIA["partitura_carnal"].pistas_coletadas == 0:

            $ MISTERIOS_ACADEMIA["partitura_carnal"].coletar_pista("Primeira folha manuscrita com notas em sangue seco.")

            "🎹 [[PISTA DO CASO — A PARTITURA CARNAL (1/3)]]: Dentro de uma partitura sacra do século dezenove, você encontra a primeira folha de um réquiem antigo com tinta cor de ferrugem. O compasso faz seus ouvidos zumbirem."

        elif MISTERIOS_ACADEMIA["partitura_carnal"].pistas_coletadas == 1:

            $ MISTERIOS_ACADEMIA["partitura_carnal"].coletar_pista("Anotação sobre as três estrofes que acordam o piano.")

            "🎹 [[PISTA DO CASO — A PARTITURA CARNAL (2/3)]]: Na estante de música, um registro diz: 'A melodia pré-diluviana da Mestra só ressoa quando as três estrofes se juntam.' Suas veias pulsam em resposta."

        else:

            $ MISTERIOS_ACADEMIA["partitura_carnal"].coletar_pista("O terceiro movimento do réquiem recuperado.")

            "🎹 [[PISTA DO CASO — A PARTITURA CARNAL (3/3)]]: Você recupera o movimento final do réquiem! A Partitura Carnal está completa para ser executada na SALA DE MÚSICA!"

    elif local_atual in ["salao_gremio", "sala_ocultismo"] and not MISTERIOS_ACADEMIA["inquerito_inquisicao"].resolvido and MISTERIOS_ACADEMIA["inquerito_inquisicao"].pistas_coletadas < 3:

        if MISTERIOS_ACADEMIA["inquerito_inquisicao"].pistas_coletadas == 0:

            $ MISTERIOS_ACADEMIA["inquerito_inquisicao"].coletar_pista("Atas do colégio com 14 páginas arrancadas.")

            "📜 [[PISTA DO CASO — OS ARQUIVOS MORTOS (1/3)]]: No arquivo do Ocultismo, você descobre que faltam 14 páginas do ano em que o sarcófago subterrâneo começou a verter sangue."

        elif MISTERIOS_ACADEMIA["inquerito_inquisicao"].pistas_coletadas == 1:

            $ MISTERIOS_ACADEMIA["inquerito_inquisicao"].coletar_pista("Fatura bancária sigilosa da diretoria para a Inquisição.")

            "📜 [[PISTA DO CASO — OS ARQUIVOS MORTOS (2/3)]]: Um recibo secreto comprova repasses da diretoria humana para agentes da Inquisição comprarem o silêncio da polícia."

        else:

            $ MISTERIOS_ACADEMIA["inquerito_inquisicao"].coletar_pista("Chave da gaveta confidencial de Elara no Grêmio.")

            "📜 [[PISTA DO CASO — OS ARQUIVOS MORTOS (3/3)]]: Você descobre a combinação do cofre de arquivos do Grêmio! Os documentos confidenciais estão acessíveis no SALÃO DO GRÊMIO à Tarde ou Noite!"

    elif local_atual == "banheiro_abandonado" and not MISTERIOS_ACADEMIA["loira_banheiro"].resolvido and MISTERIOS_ACADEMIA["loira_banheiro"].pistas_coletadas < 3:

        if MISTERIOS_ACADEMIA["loira_banheiro"].pistas_coletadas == 0:

            $ MISTERIOS_ACADEMIA["loira_banheiro"].coletar_pista("Reflexo distorcido e manchas de sangue sob a pia de porcelana.")

            "🪞 [[PISTA DO CASO — O ESPELHO DA DAMA DO BANHEIRO (1/3)]]: Ao examinar a pia quebrada, a água pinga em tom avermelhado. No espelho trincado, você vê por um instante um reflexo loiro que não se move com você."

        elif MISTERIOS_ACADEMIA["loira_banheiro"].pistas_coletadas == 1:

            $ MISTERIOS_ACADEMIA["loira_banheiro"].coletar_pista("Diário úmido de uma aluna desaparecida atrás do encanamento.")

            "🪞 [[PISTA DO CASO — O ESPELHO DA DAMA DO BANHEIRO (2/3)]]: Atrás do cano enferrujado, você resgata um diário úmido: 'Ela sussurra do vidro quando a luz falha... Ela quer sangue de quem tem medo.' Pista registrada!"

        else:

            $ MISTERIOS_ACADEMIA["loira_banheiro"].coletar_pista("Pedaço de vidro ritualístico que vibra ao toque.")

            "🪞 [[PISTA DO CASO — O ESPELHO DA DAMA DO BANHEIRO (3/3)]]: Você recupera o fragmento central do espelho! A entidade está pronta para se manifestar no BANHEIRO ABANDONADO!"

    elif not rumor_loira_banheiro and renpy.random.randint(1, 100) <= 50:

        $ rumor_loira_banheiro = True

        "🕯️ [[RUMOR DESCOBERTO]]: Dois estudantes cochicham ao longe sobre o banheiro interditado do segundo andar, onde o espelho trincado responde a quem chama pela 'Loira' à meia-noite."

    elif not rumor_mulher_gigante and renpy.random.randint(1, 100) <= 50:

        $ rumor_mulher_gigante = True

        "🕯️ [[RUMOR DESCOBERTO]]: Um calouro jura ter visto a silhueta da Mulher Gigante de vestido branco rondando as lápides do cemitério à noite."

    elif renpy.random.randint(1, 100) <= 40:

        $ conhecimento_oculto += 1

        "🔍 (OBSERVAÇÃO TÁTICA): Você nota inscrições rúnicas quase imperceptíveis gravadas no rodapé das paredes, reforçando a contenção da Máscara (+1 Conhecimento Oculto)."

    else:

        "Apenas o som distante dos seus próprios passos e o cheiro de cera fria nos corredores... Nenhum perigo imediato."

    call screen hud_exploracao_bs

    jump abrir_mapa_tatico

label emboscada_aleatoria_bs:

    if humanidade < 35 and local_atual in ["caldeiras", "sala_caldeiras", "catacumbas"] and renpy.random.randint(1, 100) <= 40:

        "Um vulto ameaçador emerge da escuridão, mas ao avistar seus olhos carmesim de Predador puro e sua silhueta monstruosa, a criatura solta um ganido de pavor e recua para os dutos!"

        $ notificar_rpg("👑 TERROR PREDATÓRIO (FASE 3)", "Inimigo recuou diante da sua aura monstruosa!", "#ff5555")

        jump entrar_local_exploracao_bs

    $ sorteio_mob = renpy.random.randint(1, 26)

    if sorteio_mob == 1:
        call iniciar_combate("Vampira Executora do Conselho", "inimigo vampira conselho espada tranca", "inimigo vampira conselho espada tranca ataque", 135, 24, 3.8, "gremio", False) from _call_iniciar_combate

    elif sorteio_mob == 2:
        call iniciar_combate("Marionete de Fios de Sangue", "inimigo marionete fios sangue flutuando", "inimigo marionete fios sangue ataque", 125, 22, 3.6, "corrompido", False) from _call_iniciar_combate_1

    elif sorteio_mob == 3:
        call iniciar_combate("Esqueleto Nobre Rúnico", "inimigo esqueleto nobre correntes terno", "inimigo esqueleto nobre correntes ataque", 120, 20, 4.0, "inorganico", False) from _call_iniciar_combate_2

    elif sorteio_mob == 4:
        call iniciar_combate("Alquimista Renegado do Fundão", "inimigo fundao alquimista frasco verde arma", "inimigo fundao alquimista frasco verde ataque", 130, 22, 3.8, "humano", False) from _call_iniciar_combate_3

    elif sorteio_mob == 5:
        call iniciar_combate("Cão de Sangue (Hellhound)", "inimigo hellhound cao sangue olhos", "inimigo hellhound cao sangue bote ataque", 145, 26, 3.4, "corrompido", False) from _call_iniciar_combate_4

    elif sorteio_mob == 6:
        call iniciar_combate("Inquisidor Tático", "inimigo inquisidor tatico balestra", "inimigo inquisidor tatico balestra ataque", 135, 24, 3.6, "humano", False) from _call_iniciar_combate_5

    elif sorteio_mob == 7:
        call iniciar_combate("Estudante Vampira Renegada", "inimigo estuadante vampira ruiva", "inimigo estuadante vampira ruiva ataque", 125, 23, 3.6, "gremio", False) from _call_iniciar_combate_vampira_ruiva

    elif sorteio_mob == 8:
        call iniciar_combate("Executor da Lâmina Branca", "inimigo executor com espada cabelo branco", "inimigo executor com espada cabelo branco ataque", 140, 26, 3.5, "gremio", False) from _call_iniciar_combate_executor_branco

    elif sorteio_mob == 9:
        call iniciar_combate("Rival Ghoul Hostil", "inimigo rival ghoul ameaca aberta", "inimigo rival ghoul ameaca aberta ataque", 130, 23, 3.6, "corrompido", False) from _call_iniciar_combate_rival_ameaca

    elif sorteio_mob == 10:
        call iniciar_combate("Vampira Duelista do Conselho", "inimigo vampira conselho florete chiquinhas", "inimigo vampira conselho florete chiquinhas ataque", 135, 24, 3.7, "gremio", False) from _call_iniciar_combate_florete_chiquinhas

    elif sorteio_mob == 11:
        call iniciar_combate("Vampira da Rapieira Albina", "inimigo vampira conselho rapieira albina", "inimigo vampira conselho rapieira albina ataque", 140, 25, 3.6, "gremio", False) from _call_iniciar_combate_rapieira_albina

    elif sorteio_mob == 12:
        call iniciar_combate("Executora do Conselho (Adaga Rubra)", "inimigo executora conselho adaga sangue", "inimigo executora conselho adaga sangue ataque", 150, 26, 3.5, "gremio", False) from _call_iniciar_combate_adaga_sangue

    elif sorteio_mob == 13:
        call iniciar_combate("Executor do Conselho (Machado Carmesim)", "inimigo executor conselho ruivo machado", "inimigo executor conselho ruivo machado ataque", 160, 28, 3.5, "gremio", False) from _call_iniciar_combate_ruivo_machado

    elif sorteio_mob == 14:
        call iniciar_combate("Executor do Conselho (Espada Solar)", "inimigo executor conselho loiro espada", "inimigo executor conselho loiro espada ataque", 145, 26, 3.6, "gremio", False) from _call_iniciar_combate_loiro_espada

    elif sorteio_mob == 15:
        call iniciar_combate("Executor do Conselho (Lâmina Negra)", "inimigo executor conselho preto espada lamina", "inimigo executor conselho preto espada ataque", 150, 27, 3.5, "gremio", False) from _call_iniciar_combate_preto_espada

    elif sorteio_mob == 16:
        call iniciar_combate("Gárgula de Pedra Dragão", "inimigo gargula pedra dragao", "inimigo gargula pedra dragao ataque", 165, 27, 3.5, "inorganico", False) from _call_iniciar_combate_gargula_pedra

    elif sorteio_mob == 17:
        call iniciar_combate("Besta Urso Acorrentado", "inimigo urso monstruoso acorrentado cranio", "inimigo urso monstruoso acorrentado ataque", 175, 29, 3.4, "corrompido", False) from _call_iniciar_combate_urso_acorrentado

    elif sorteio_mob == 18:
        call iniciar_combate("Mecânico Pesado do Fundão", "inimigo fundao mecanico pesado", "inimigo fundao mecanico pesado ataque", 155, 25, 3.6, "humano", False) from _call_iniciar_combate_mecanico_pesado

    elif sorteio_mob == 19:
        call iniciar_combate("Capanga de Escopeta do Fundão", "inimigo fundao mascara gas escopeta", "inimigo fundao mascara gas escopeta disparo ataque", 145, 25, 3.5, "humano", False) from _call_iniciar_combate_escopeta_fundao

    elif sorteio_mob == 20:
        call iniciar_combate("Ghoul Garota Corrompida", "inimigo ghoul garota corrompida garras", "inimigo ghoul garota corrompida ataque", 135, 24, 3.6, "corrompido", False) from _call_iniciar_combate_ghoul_garota_corrompida

    elif sorteio_mob == 21:
        call iniciar_combate("Acadêmica das Teias", "inimigo colegial ghoul teia", "inimigo colegial ghoul teia ataque", 130, 23, 3.7, "corrompido", False) from _call_iniciar_combate_colegial_teia

    elif sorteio_mob == 22:
        call iniciar_combate("Abominação Sombra do Pesadelo", "inimigo sombra boca peito pesadelo", "inimigo sombra boca peito ataque", 160, 28, 3.4, "corrompido", False) from _call_iniciar_combate_sombra_pesadelo

    elif sorteio_mob == 23:
        call iniciar_combate("Rival Ghoul das Garras", "inimigo rival ghoul combate", "inimigo rival ghoul combate ataque", 140, 25, 3.6, "corrompido", False) from _call_iniciar_combate_rival_combate

    elif sorteio_mob == 24:
        call iniciar_combate("Vampiro Delinquente Rebelde", "inimigo vampiro delinquente sorriso agressivo", "inimigo vampiro delinquente ataque", 135, 24, 3.6, "gremio", False) from _call_iniciar_combate_vampiro_delinquente

    elif sorteio_mob == 25:
        call iniciar_combate("Estudante Vampiro Delinquente", "inimigo vampiro estudante delinquente ameaca", "inimigo vampiro estudante delinquente ataque", 130, 23, 3.6, "gremio", False) from _call_iniciar_combate_estudante_delinquente

    else:
        call iniciar_combate("Esqueleto Rúnico da Academia", "inimigo esqueleto colegial runa testa", "inimigo esqueleto colegial ataque", 125, 21, 3.9, "inorganico", False) from _call_iniciar_combate_esqueleto_colegial

    if _return != "fuga":

        if getattr(store, "extorquiu_combate_atual", False):

            $ extorquiu_combate_atual = False

        else:

            if getattr(store, "tipo_sangue_inimigo", "humano") in ["corrompido", "inorganico"]:

                $ recompensa_dinheiro = renpy.random.randint(25, 55)

            else:

                $ recompensa_dinheiro = renpy.random.randint(30, 75)

            $ dinheiro_jogador += recompensa_dinheiro

            "💰 Você vasculha os espólios do confronto e recupera $[recompensa_dinheiro]!"

    jump entrar_local_exploracao_bs

# ==============================================================================

# ENCONTRO COM NORA VASQUES (COBAIA 31) NA CRIPTA DE VIDRO

# ==============================================================================

label encontro_nora_cela_cripta:

    scene bg animado cripta cela vidro runas fechada with dissolve

    if renpy.loadable("audio/catactic_requiem.ogg"):

        play music "audio/catactic_requiem.ogg" if_changed fadein 1.5

    "No centro da abóbada de pedra da cripta, cercada por tubos de cobre e válvulas sibilantes, ergue-se uma cápsula cilíndrica de vidro espesso selada com glifos rúnicos."

    "Dentro do líquido alquímico âmbar, suspensa por correntes de contenção, está a aluna do alfinete 31 — Nora Vasques."

    show nora neutra at sprite_padrao with dissolve

    "O uniforme preto rasgado nas mangas. As marcas recentes de agulhas e bisturis nos braços comprovam as extrações forçadas do Grêmio. O líquido borbulha lentamente, mantendo-a em um torpor agonizante."

    if getattr(store, "emprestou_caneta_nora", False):

        "Ao sentir a vibração dos meus passos contra o mármore frio, os olhos claros de Nora tremulam e se abrem debilmente. Ela ergue a mão pálida, apoiando as pontas dos dedos contra a parede de vidro."

        $ th_voz("climax/nora_climax_03_cela_cripta")
        nora "...V-Victor...? É você...? O bolsista... do primeiro dia..."

        show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

        protagonist "Nora... O que eles fizeram com você?!"

        nora "O Grêmio... Elara e os executores de casaco branco... Eles não me mataram naquela noite... Eles me trouxeram para cá..."

        nora "Eles usaram o meu sangue para tentar domesticar a Besta... Mas o miasma do Antediluviano causou uma revolta violenta nas minhas veias... Eu perdi o controle naquela noite no corredor... e quase matei você..."
        nora "Elara me trancou aqui para sustentar a barreira... Solta, eu dilaceraria doze estudantes por quinzena num frenesi cego... Alguém sempre paga a conta do sangue desta escola..."
        "A lembrança do gabinete de Elara me atinge: 'Isso é conter? É sustentar. A escola respira por ela. Doze bolsas de calouros não saciariam o que Nora se tornou... Eu escolhi quem não tinha quem perguntasse.'"

        "A voz dela ressoa abafada pelas ranhuras acústicas da câmara."

        nora "Eu sabia que não duraria muito tempo... Antes de me trancarem nesta redoma, eu escondi a Chave-Mestra dos Dutos de Ventilação... Ela caiu no ralo de drenagem sob a base desta cela..."

        $ th_voz("nora/nora_bark_aviso_cain")
        nora "Mas isso... isso está queimando a minha mente... A Besta quer rasgar o vidro... Por favor... não me deixe virar um monstro sem alma..."

    else:

        "Ao sentir a presença de um predador, Nora desperta em sobressalto, batendo debilmente os nós dos dedos contra o vidro espesso."

        nora "...Q-Quem está aí...? Mais um carrasco do Conselho com frascos de teste...?"

        show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

        protagonist "Calma. Eu não sou do Conselho Estudantil."

        nora "Você... você fede a sangue recém-convertido... Mas ainda tem olhos de gente. Por favor... o líquido desta cuba queima como ácido rúnico... Eu não aguento mais os testes de Elara..."

        nora "Eles pretendem drenar o que sobrou de mim para abrir as travas do cofre principal..."

    menu:

        "[[ALQUIMIA & SANGUE]] Estabilizar os sinais de Nora (Requer 1 Filtro Rúnico ou Kit Médico e 10 HP do seu sangue)" if filtro_runico >= 1 or kit_curativo >= 1:

            if filtro_runico >= 1:

                $ filtro_runico -= 1

                $ item_usado_nora = "Filtro Rúnico"

            else:

                $ kit_curativo -= 1

                $ item_usado_nora = "Kit de Curativos"

            $ hp_jogador = max(1, hp_jogador - 10)

            $ humanidade = min(100, humanidade + 10)
            $ GerenciadorRuina.adicionar_ruina(15, "Estabilização da Cripta de Nora")
            $ nora_estabilizada_cripta = True

            $ tem_chave_dutos_nora = True

            with flash_red

            $ th_sfx("heartbeat")

            "Conecto o [item_usado_nora] na válvula de purga lateral e corto a palma da minha mão. Deixo meu sangue vivo escorrer pelos dutos de alimentação para neutralizar a toxina ácida do Grêmio (-10 HP)."

            "O líquido âmbar clareia. As convulsões de Nora cessam e uma respiração calma preenche seus pulmões."

            show nora neutra at sprite_padrao with dissolve

            nora "...A queimação... parou... Minha mente... está limpa pela primeira vez em semanas..."

            if getattr(store, "emprestou_caneta_nora", False):

                nora "Você me salvou duas vezes, Victor. Uma com uma caneta... e outra com a sua própria vida."

            else:

                nora "Eu nunca esperei que alguém neste inferno sacrificasse a própria vitae por uma cobaia descartada..."

            "Nora aponta para a grade inferior de escape, onde a água desceu. Sob a fresta de ferro, retiro uma chave pesada de latão polido: a Chave-Mestra dos Dutos de Ventilação!"

            $ notificar_rpg("🗝️ COBAIA 31 SALVA", "+10 Humanidade | Chave dos Dutos Obtida! Nora estabilizada.", "#00ffcc")

            protagonist "Descanse agora, Nora. Assim que eu acertar as contas com Elara e abrir este cofre, eu voltarei para tirar você daqui."

            nora "Tome cuidado... Os dutos passam por cima do salão dos guardas do Grêmio... Use a chave para contorná-los..."

        "[[MISERICÓRDIA]] Conceder a morte definitiva e poupá-la do sofrimento (+Humanidade / +Saciedade)":

            $ humanidade = min(100, humanidade + 5)

            $ fome_sangue = min(100, fome_sangue + 40)

            $ nora_misericordia_concedida = True
            $ GerenciadorRuina.adicionar_ruina(15, "Drenagem da Cripta de Nora")
            $ tem_chave_dutos_nora = True

            with flash_red

            $ th_sfx("heartbeat")

            nora "...Obrigada... Por favor... não me deixe acordar no Vazio como uma abominação do Antediluviano..."

            "Giro a válvula de drenagem emergencial e conecto o fluxo ao meu próprio grilhão. Sorvo a agonia e o resto de vitae de Nora, garantindo-lhe uma partida rápida, sem dor e sem o tormento da fome eterna."

            "A expressão torturada de Nora finalmente descansa em uma paz serena enquanto a câmara se esvazia."

            "No fundo do duto de drenagem da cápsula, o metal reluz: encontro a Chave-Mestra dos Dutos de Ventilação que ela escondera."

            $ notificar_rpg("🕊️ MISERICÓRDIA CONCEDIDA", "+5 Humanidade | +40% Saciedade | Chave dos Dutos Recuperada.", "#88ccff")

            protagonist "Descanse em paz, Nora. A sua dívida com esta escola acabou."

        "[[INDIFERENÇA]] Deixar a cápsula intacta e recuar (-5 Humanidade)":

            $ humanidade = max(0, humanidade - 5)

            "Não posso me dar ao luxo de gastar meus próprios recursos ou vitae com uma aluna que já foi consumida pelo sistema."

            protagonist "Não posso intervir nisso agora. Seria suicídio."

            nora "...Não... Por favor... Não me deixe no escuro..."

            "Dou as costas para o cilindro de vidro enquanto as bolhas voltam a subir, abafando os sussurros de desespero da aluna."

            $ notificar_rpg("⚠️ INDIFERENÇA FRIA", "-5 Humanidade | Cobaia 31 abandonada.", "#ff5555")

    hide nora with dissolve

    hide victor with dissolve

    jump entrar_local_exploracao_bs

# ==============================================================================

# 8.1 INTERAÇÃO COM OS FIGURANTES "SEM ROSTO" (MOBU KYARA) E QUEBRA DE MÁSCARA

# ==============================================================================

label encontro_mob_figurante:

    $ encontro_eh_miragem = False
    $ sortear_mob_por_local(local_atual, periodo)
    $ _zona_mob = obter_zona_perigo_atual(local_atual, periodo)
    $ _zona_mob_up = _zona_mob.upper()

    # Sorteia Miragem de Abstinência ANTES de exibir o figurante humano (apenas quando 0 < fome_sangue < 20)
    if 0 < fome_sangue < 20 and "miragem_abstinencia" in PERFIS_ALVO_EMBOSCADA and renpy.random.randint(1, 100) <= 35:
        $ encontro_eh_miragem = True
        $ _perfil_mob = "miragem_abstinencia"
        $ nome_mob_atual = "Vulto Trêmulo no Fim do Corredor"
        show screen overlay_frenesi_vermelho
        show expression sprite_mob_atual as mob_npc at silhueta_miragem with dissolve
        $ th_sfx("distorcao")
        "👤 [[VULTO NAS SOMBRAS]]: A névoa da sede crítica distorce o corredor... Uma silhueta trêmula parece respirar junto aos armários de metal."
        if pode_ler_pulso_sanguineo():
            "🔮 [[LEITURA DE PULSO]]: Seus sentidos sobrenaturais disparam um alerta — o vulto à frente não tem batimento cardíaco nem calor arterial! É uma Miragem de Abstinência."
    else:
        $ _perfil_mob = resolver_perfil_emboscada(id_mob_atual, tipo_mob_atual)
        show expression sprite_mob_atual as mob_npc at sprite_padrao with dissolve

        $ th_bark_mob("abordagem")

        "👤 [[FIGURANTE ENCONTRADO]]: Você cruza o caminho de [nome_mob_atual]."

        # =========================================================================

        # MECÂNICA DE FRENESI (FOME DE SANGUE < 20) E TESTE DE AUTOCONTROLE

        # =========================================================================

        if fome_sangue <= 0:
            show screen overlay_frenesi_vermelho
            $ th_sfx("heartbeat")
            with flash_red
            with vpunch
            "🩸 [[FRENESI TOTAL E INEVITÁVEL — FOME DE SANGUE A ZERO!]]"
            "A Besta interior devorou completamente sua consciência humana! As artérias carótidas de [nome_mob_atual] pulsam como sinos ensurdecedores e o miasma da fome consome sua visão com uma névoa carmesim absoluta!"
            "Não há teste de resistência mental possível. O monstro salta na jugular da presa em pleno corredor!"
            jump resolver_ataque_frenesi_involuntario

        elif fome_sangue < 20:

            show screen overlay_frenesi_vermelho

            $ th_sfx("heartbeat")

            with flash_red

            with vpunch

            "🩸 [[FRENESI DE SANGUE CRÍTICO — SACIEDADE [fome_sangue]%%!]]:"

            "As artérias no pescoço de [nome_mob_atual] pulsam como tambores ensurdecedores! O odor do sangue quente queima suas narinas e suas presas saltam involuntariamente!"

            # Teste de Autocontrole baseado em Humanidade e Coragem

            $ margem_autocontrole = (humanidade // 2) + (coragem * 10)

            $ rolo_autocontrole = renpy.random.randint(1, 100)

            if rolo_autocontrole > margem_autocontrole:

                "🧠 [[FALHA NO TESTE DE AUTOCONTROLE!]] (Resistência Mental: [margem_autocontrole]%% vs Rolagem: [rolo_autocontrole])"

                "A besta carmesim assume o comando absoluto dos seus membros! O verniz da razão desaba e você se lança sobre a presa em pleno corredor!"

                jump resolver_ataque_frenesi_involuntario

            else:

                "🧠 [[SUCESSO NO TESTE DE AUTOCONTROLE!]] (Resistência Mental: [margem_autocontrole]%% vs Rolagem: [rolo_autocontrole])"

                "Cravando as unhas nas próprias palmas até verter sangue, você força a mente a sufocar o impulso predatório por alguns instantes! Mas a fome devoradora ainda ruge em suas têmporas..."

    $ _dados_emb = PERFIS_ALVO_EMBOSCADA.get(_perfil_mob, PERFIS_ALVO_EMBOSCADA["calouro"])

    label menu_opcoes_mob_figurante:

    menu:

        "🔮 [[DISSIPAR MIRAGEM DE ABSTINÊNCIA]] Afastar-se da alucinação (0 HP / 0%% Exposição)" if encontro_eh_miragem and pode_ler_pulso_sanguineo():
            hide screen overlay_frenesi_vermelho
            hide mob_npc with dissolve
            "Você fecha os olhos, controla a respiração e estilhaça o delírio da fome. Onde parecia haver uma presa, há apenas um armário de aço vazio e sombras imóveis."
            $ notificar_rpg("🔮 MIRAGEM DISSIPADA", "Ilusão de abstinência neutralizada pelos seus sentidos sobrenaturais.", "#cc88ff")
            jump entrar_local_exploracao_bs

        "👁️ Aproximar-se devagar para inspecionar o vulto" if encontro_eh_miragem:
            hide screen overlay_frenesi_vermelho
            hide mob_npc with dissolve
            $ th_sfx("distorcao")
            $ tensao_psicologica = min(100, getattr(store, "tensao_psicologica", 0) + 5)
            "Você dá dois passos cautelosos para a frente — e a figura se desfaz instantaneamente em um armário metálico torto e um cabideiro vazio."
            "Um calafrio percorre sua espinha: a sede está começando a pregar peças na sua mente (+5 Tensão Mental | 0%% Exposição)."
            jump entrar_local_exploracao_bs

        "👁️ [[PRESENÇA ABISSAL]] Hipnotizar e Saquear (+$60 | 0%% Exposição | 1x/Período)" if ressonancia_pre_diluviana >= 8 and not getattr(store, "hipnotizou_mob_periodo", False) and not encontro_eh_miragem:
            hide screen overlay_frenesi_vermelho
            $ hipnotizou_mob_periodo = True
            $ dinheiro_jogador += 60
            $ th_sfx("distorcao")
            $ th_sfx("moedas")
            show expression obter_sprite_mob(id_mob_atual, "transe hipnotico") as mob_npc at sprite_padrao with dissolve
            with flash_red
            "Um único brilho carmesim atravessa suas pupilas. O olhar de [nome_mob_atual] se esvazia instantaneamente sob o peso da sua Presença Abissal."
            "Sem uma única palavra ou sinal de luta, a vítima entrega +$60 em créditos e continua caminhando como se nada tivesse acontecido (0%% Exposição)."
            $ notificar_rpg("👁️ PRESENÇA ABISSAL", "+$60 saqueados sob hipnose instantânea | 0% Exposição", "#cc66ff")
            hide mob_npc with dissolve
            jump entrar_local_exploracao_bs

        "💬 Conversar e sondar informações locais (+Conhecimento / +Intelecto)" if not encontro_eh_miragem:

            hide screen overlay_frenesi_vermelho

            $ th_bark_mob("conversa")

            "[nome_mob_atual]" "\"[fala_mob_atual]\""

            $ conhecimento_oculto += 1

            if renpy.random.randint(1, 100) <= 40:

                $ intelecto += 1

                "📘 Você conecta o relato às suas anotações (+1 Conhecimento Oculto / +1 Intelecto)."

            else:

                "🕯️ Você memoriza a informação (+1 Conhecimento Oculto)."

            hide mob_npc with dissolve

            call screen hud_exploracao_bs

            jump abrir_mapa_tatico

        "🧤 [[MÃO LEVE]] Bater carteira / Furto furtivo (Teste de Subterfúgio D10)" if (not encontro_eh_miragem) and tipo_mob_atual in ["aluno", "veterano", "doador"]:
            hide screen overlay_frenesi_vermelho
            $ rolo_punga = renpy.random.randint(1, 10) + getattr(store, "subterfugio", 2)
            if rolo_punga >= 6:
                $ grana_punga = renpy.random.randint(25, 55)
                $ dinheiro_jogador += grana_punga
                $ th_sfx("moedas")
                "Você passa rente a [nome_mob_atual] com passos fluidos e silenciosos. Seus dedos ágeis deslizam para dentro do bolso do uniforme sem produzir o menor ruído."
                "Você puxa um maço de notas antes de se distanciar nas sombras (+$[grana_punga] surrupiados com sucesso)."
                $ notificar_rpg("🧤 PUNGA FURTIVA", f"+${grana_punga} surrupiados sem alerta!", "#00ffcc")
            else:
                $ exposicao = min(100, exposicao + 15)
                show expression obter_sprite_mob(id_mob_atual, "medo") as mob_npc at sprite_padrao with dissolve
                $ th_bark_mob("mordida")
                "[nome_mob_atual]" "\"E-ei! Tira a mão do meu bolso! Socorro, tem alguém me roubando nos corredores!\""
                "Você recua abruptamente enquanto passos apressados ecoam no fim do corredor (+15%% Exposição)."
                $ notificar_rpg("🚨 FLAGRANTE DE FURTO", "+15% Exposição | Aluno em pânico", "#ff4444")
            hide mob_npc with dissolve
            jump entrar_local_exploracao_bs

        "🔍 Sondar Rumores dos Corredores (Localização de Alvos / Rondas)" if not encontro_eh_miragem:
            hide screen overlay_frenesi_vermelho
            $ th_bark_mob("conversa")
            $ _heroina_alvo = renpy.random.choice(["elara", "emilia", "valeria", "lility"])
            $ rumores_heroina_periodo[_heroina_alvo] = True
            if _heroina_alvo == "elara":
                $ _loc_nome = obter_nome_local(loc_elara)
                "[nome_mob_atual]" "\"Vi a Presidente Elara passando com uma prancheta de auditoria em direção a [_loc_nome]... É melhor andar na linha.\""
            elif _heroina_alvo == "emilia":
                $ _loc_nome = obter_nome_local(loc_emilia)
                "[nome_mob_atual]" "\"A noviça Emília foi vista carregando água benta e anotações perto de [_loc_nome]. Ela parecia bastante apreensiva.\""
            elif _heroina_alvo == "valeria":
                $ _loc_nome = obter_nome_local(loc_valeria)
                "[nome_mob_atual]" "\"Ouvi dizer que Valéria está negociando peças e contrabando pelas bandas de [_loc_nome]. Mas você não ouviu isso de mim.\""
            else:
                $ _loc_nome = obter_nome_local(loc_mestra)
                "[nome_mob_atual]" "\"Dizem que as luzes da ala de [_loc_nome] piscaram e fez um frio de congelar a espinha... Aposto que Lyra von Blut está por lá.\""
            $ notificar_rpg("🔍 RUMOR MARCADO NO MAPA", f"Alvo localizado em {_loc_nome} neste período!", "#ffd700")
            hide mob_npc with dissolve
            jump entrar_local_exploracao_bs

        "📝 Coagir Tarefa Acadêmica (Forçar Aluno a Fazer seu Trabalho)" if (not encontro_eh_miragem) and getattr(store, "tarefa_academica_pendente", False) and tipo_mob_atual in ["aluno", "veterano", "doador"]:
            hide screen overlay_frenesi_vermelho
            show expression obter_sprite_mob(id_mob_atual, "medo") as mob_npc at sprite_padrao with dissolve
            $ th_sfx("heartbeat")
            with flash_red
            "Você encurrala [nome_mob_atual] contra os armários de ferro. Seus caninos despontam por um milésimo de segundo e sua sombra parece engolir a luz da lâmpada."
            "Com a voz sussurrada e fria, você estende o tema do seu dever escolar: '[nome_tarefa_academica]'."
            "[nome_mob_atual]" "\"E-eu faço! Eu entrego assinado com a sua matrícula na caixa de depósito da biblioteca antes do toque de recolher! Por favor, não me machuque!\""
            $ tarefa_academica_pendente = False
            $ humanidade = max(0, humanidade - 2)
            $ notificar_rpg("📝 TAREFA COAGIDA", "Obrigação concluída sem gastar passos | -2 Humanidade", "#ffaa55")
            hide mob_npc with dissolve
            jump entrar_local_exploracao_bs

        "🧛 [[MORDIDA FURTIVA — Tier [_dados_emb['tier']] | Zona [_zona_mob_up]]] Emboscar no ponto cego (Banquete Oculto)" if not area_alerta_emboscada:
            hide screen overlay_frenesi_vermelho
            $ renpy.block_rollback()
            call screen radar_emboscada_furtiva(perfil_id=_perfil_mob, zona=_zona_mob, nome_exibicao=nome_mob_atual)
            $ _res_emboscada = _return
            $ store.sedativo_ativo_bote = False

            if _perfil_mob == "miragem_abstinencia":
                if _res_emboscada == "miragem_dissipada":
                    hide mob_npc with dissolve
                    "No último segundo, você reconhece a ausência de pulso e recua antes de se ferir. A silhueta se desfaz em poeira e sombras."
                    $ notificar_rpg("🔮 MIRAGEM DISSIPADA", "Você evitou a armadilha da abstinência (0 HP perdido | 0% Exposição).", "#cc88ff")
                    jump entrar_local_exploracao_bs
                else:
                    $ cacadas_realizadas_hoje += 1
                    $ area_alerta_emboscada = True
                    $ _pen_exp_mir = aplicar_reducao_isolamento_exposicao(22)
                    $ exposicao = min(100, exposicao + _pen_exp_mir)
                    $ hp_jogador = max(1, hp_jogador - 10)
                    $ th_sfx("golpe_esforco")
                    with hpunch
                    with vpunch
                    hide mob_npc with dissolve
                    "Você salta em fúria cega contra o vulto... e suas presas se chocam violentamente contra a porta fria de um armário metálico!"
                    "O estrondo reverbera por toda a ala enquanto sangue da sua própria gengiva escorre pelo queixo! Era apenas uma Miragem de Abstinência."
                    "Estudantes abrem portas assustados ao ouvir o baque e ver você ajoelhado no corredor!"
                    "⚠️ ([[ALUCINAÇÃO DA BESTA]] 0%% Sangue | -10 HP | +[_pen_exp_mir]%% Exposição | Corredores em Alerta)"
                    $ notificar_rpg("🌀 ALUCINAÇÃO DA BESTA", f"Miragem atacada! 0% Sangue | -10 HP | +{_pen_exp_mir}% Exposição", "#ff3344")
                    jump checar_quebra_mascara_gremio

            $ cacadas_realizadas_hoje += 1

            if _res_emboscada == "sucesso_furtivo":
                # O mob reage com medo ao bote silencioso no ponto cego
                show expression obter_sprite_mob(id_mob_atual, "medo") as mob_npc at sprite_padrao with dissolve
                $ th_sfx("heartbeat")
                $ th_bark_mob("mordida")
                with flash_red
                with vpunch

                $ _desc_banquete = aplicar_banquete_oculto(tipo_mob_atual, silencioso=True)
                $ registrar_progresso_encomenda_bote(_perfil_mob)
                $ _saque_emb = _dados_emb.get("dinheiro", 0)
                if _saque_emb > 0:
                    $ dinheiro_jogador += _saque_emb
                    $ th_sfx("moedas")
                    $ notificar_rpg("👁️ BOTE SILENCIOSO", f"Alvo Tier {_dados_emb['tier']} drenado sem rastros (0% Exposição | +${_saque_emb})!", "#00ffcc")
                else:
                    $ notificar_rpg("👁️ BOTE SILENCIOSO", f"Emboscada perfeita em Tier {_dados_emb['tier']} (0% Exposição)!", "#00ffcc")

                # Após beber o sangue, a vítima entra em transe hipnótico entorpecente
                show expression obter_sprite_mob(id_mob_atual, "transe hipnotico") as mob_npc at sprite_padrao with dissolve

                "Você aguarda o exato instante em que a ronda do corredor se afasta e encurrala [nome_mob_atual] no ponto cego entre os pilares."
                "Antes que qualquer som escape, suas presas cravam na jugular com precisão cirúrgica, drenando a seiva vital sem deixar rastros."
                if _saque_emb > 0:
                    "Enquanto o corpo de [nome_mob_atual] cede sob o transe, seus dedos deslizam pelo bolso do casaco e recolhem +$[_saque_emb] em créditos."
                "O corpo de [nome_mob_atual] amolece, os olhos perdem o foco e sua respiração desacelera em um devaneio dócil e submisso."
                "🩸 [_desc_banquete]"

                if "diretor" in str(id_mob_atual).lower():
                    "O Diretor Ambrósio balbucia trêmulo no chão, com a gravata torta e os olhos embaçados: 'E-Elara... Elara saberá disso... O Conselho não perdoa...'"
                    $ exposicao = min(100, exposicao + 15)
                    $ GerenciadorRuina.adicionar_ruina(2, "Diretor Ambrósio Drenado")
                    $ notificar_rpg("⚠️ DIRETOR DRENADO", "+15% Exposição | +2% Deterioração | Alerta do Grêmio", "#ffaa00")

                # Flagrante caso alguma heroína esteja no mesmo local
                if loc_emilia == local_atual:
                    $ duvida_emilia += 4
                    $ th_bark("emilia", "flagrante")
                    show emilia uniforme surpresa meio corpo at sprite_esquerda with dissolve
                    emilia "V-Victor?! O que... o que você acabou de fazer nas sombras com aquele colega?!"
                    emilia "Eu vi suas presas... e havia sangue no pescoço dele! O que você está escondendo de mim?!"
                    hide emilia with dissolve
                elif loc_elara == local_atual:
                    $ punicoes_gremio_ativas += 1
                    $ hp_jogador = max(10, hp_jogador - 20)
                    $ th_bark("elara", "flagrante")
                    show elara irritada e com desprezo at sprite_esquerda with dissolve
                    elara "Alimentando-se em plena área comum como um parasita selvagem, Sr. Vane?!"
                    elara "O Grilhão de Sangue cobra cada transgressão à ordem deste campus. Curve-se!"
                    with vpunch
                    "⚡ O Grilhão de Sangue queima suas veias (-20 HP | +1 Punição do Grêmio)!"
                    hide elara with dissolve
                elif loc_mestra == local_atual:
                    if fome_sangue <= 20:
                        $ th_bark("lility", "fome_critica")
                    else:
                        $ th_bark("lility", "padrao")
                    show lility comportada sorriso meio corpo at sprite_esquerda with dissolve
                    mestra "Furtivo e contido, meu lacaio... Beber apenas algumas gotas para conter a sede. Poupa o rebanho, mas não sacia o apetite de um verdadeiro predador."
                    hide lility with dissolve
                elif loc_valeria == local_atual:
                    $ th_bark("valeria", "padrao")
                    show valeria cinica pirulito meio corpo at sprite_esquerda with dissolve
                    valeria "Belo bote silencioso, Vane. Mas não vai deixar manchas no meu setor, ou vou cobrar taxa de limpeza na sua conta."
                    hide valeria with dissolve

                hide mob_npc with dissolve
                jump checar_quebra_mascara_gremio

            else:
                # FALHA NO BOTE: 0% de sangue, fuga limpa, bloqueio da área no período, exposição severa e retaliação física!
                $ area_alerta_emboscada = True
                show expression obter_sprite_mob(id_mob_atual, "medo") as mob_npc at sprite_padrao with dissolve
                $ th_bark_mob("mordida")
                with hpunch

                $ _pen_exp_base = 24 if _zona_mob == "azul" else (14 if _zona_mob == "vermelha" else 18)
                $ _pen_exp_bote = aplicar_reducao_isolamento_exposicao(_pen_exp_base)
                $ exposicao = min(100, exposicao + _pen_exp_bote)
                $ _dano_retaliacao = _dados_emb.get("dano_falha", 0)
                $ _txt_retaliacao = _dados_emb.get("texto_retaliacao", "")

                "No último instante, [nome_mob_atual] percebe sua sombra se movendo atrás dos pilares e se desvencilha em pânico!"

                if _dano_retaliacao > 0:
                    $ hp_jogador = max(1, hp_jogador - _dano_retaliacao)
                    $ th_sfx("golpe_esforco")
                    with vpunch
                    "[_txt_retaliacao] (-[_dano_retaliacao] HP)"

                if _zona_mob == "vermelha":
                    $ GerenciadorRuina.adicionar_ruina(2, "Alarme de Emboscada Frustrada na Zona Vermelha")
                    $ notificar_rpg("🚨 ALVO ESCAPOU (ZONA VERMELHA)", f"0% Sangue | +{_pen_exp_bote}% Exposição | +2% Deterioração | Corredores em Alerta", "#ff3344")
                    "[nome_mob_atual] dispara pelo corredor gritando por ajuda antes que você consiga uma única gota de sangue! O alarme ecoa até as profundezas."
                    "⚠️ ([[ALVO ESCAPOU]] 0%% Sangue | +[_pen_exp_bote]%% Exposição | +2%% Deterioração | Emboscadas bloqueadas neste período)"
                else:
                    $ duvida_emilia += 1
                    $ notificar_rpg(f"🚨 ALVO ESCAPOU (ZONA {_zona_mob_up})", f"0% Sangue | +{_pen_exp_bote}% Exposição | +1 Suspeita Emília | Corredores em Alerta", "#ff3344")
                    "[nome_mob_atual] dispara pelo corredor gritando por testemunhas antes que você consiga uma única gota de sangue! Os rumores se espalham imediatamente."
                    "⚠️ ([[ALVO ESCAPOU]] 0%% Sangue | +[_pen_exp_bote]%% Exposição | +1 Suspeita de Emília | Emboscadas bloqueadas neste período)"

                hide mob_npc with dissolve
                jump checar_quebra_mascara_gremio

        "🚫 [[MORDIDA FURTIVA BLOQUEADA — CORREDORES EM ALERTA]] (Aguarde o próximo período)" if area_alerta_emboscada:
            "Os corredores ainda fervem em alvoroço após sua última emboscada frustrada. Monitores e estudantes andam em estado de alerta — tentar outro bote furtivo agora seria suicídio."
            jump menu_opcoes_mob_figurante

        "🩸 [[ATAQUE DE FRENESI!]] Drenar brutalmente até o fim (+65%% Sangue / +30%% Exposição / -8 Humanidade / Flagrante Grave)" if not encontro_eh_miragem:

            hide screen overlay_frenesi_vermelho

            jump resolver_ataque_frenesi_execucao

        "💰 Pressionar / Extorquir ou Subornar Figurante" if (not encontro_eh_miragem) and tipo_mob_atual in ["aluno", "veterano", "doador", "policial"]:

            hide screen overlay_frenesi_vermelho

            if tipo_mob_atual == "policial":

                if dinheiro_jogador >= 80:

                    $ dinheiro_jogador -= 80

                    $ exposicao = max(0, exposicao - 20)

                    $ th_bark_mob("suborno")

                    "Você desliza $80 para o bolso de [nome_mob_atual], que queima o boletim de ocorrência noturno (-20%% Exposição)."

                else:

                    "[nome_mob_atual]" "\"Sem dinheiro para o café, garoto? Circulando antes que eu te leve pra delegacia.\""

            else:

                $ grana_extorquida = renpy.random.randint(40, 85)

                $ dinheiro_jogador += grana_extorquida

                $ dominio_jogador += 1

                $ humanidade = max(0, humanidade - 1)

                "Seus olhos frios intimidam [nome_mob_atual], que entrega a carteira tremendo (+$[grana_extorquida] / +1 Domínio / -1 Humanidade)."

            hide mob_npc with dissolve

            call screen hud_exploracao_bs

            jump abrir_mapa_tatico

        "🚶 Ignorar e seguir caminho":

            hide screen overlay_frenesi_vermelho

            hide mob_npc with dissolve

            call screen hud_exploracao_bs

            jump abrir_mapa_tatico

label resolver_ataque_frenesi_involuntario:

    hide screen overlay_frenesi_vermelho

    "Suas garras e presas rasgam o pescoço de [nome_mob_atual] antes de qualquer comando voluntário!"

    jump resolver_ataque_frenesi_execucao

label resolver_ataque_frenesi_execucao:

    hide screen overlay_frenesi_vermelho

    # Pulo predatório: a presa é tomada pelo pânico
    show expression obter_sprite_victor("frenesi") as victor at sprite_esquerda with dissolve
    show expression obter_sprite_mob(id_mob_atual, "medo") as mob_npc at sprite_padrao with dissolve
    $ th_bark_mob("mordida")

    if renpy.loadable("audio/blade_slash_heavy.ogg"):

        play sound "audio/blade_slash_heavy.ogg"

    with vpunch

    with flash_red

    
    # Após o ataque violento e a ingestão voraz, o mob fica em choque/transe antes de desabar
    show expression obter_sprite_mob(id_mob_atual, "transe hipnotico") as mob_npc at sprite_padrao with dissolve
    $ fome_sangue = min(100, fome_sangue + 65)

    $ exposicao = min(100, exposicao + 30)

    $ humanidade = max(0, humanidade - 8)

    $ quebras_de_mascara += 1

    "Suas garras prendem [nome_mob_atual] contra a parede fria! Você bebe vorazmente até o corpo desabar inconsciente no piso, coberto de sangue e com feridas de presas escancaradas!"

    "🚨 [[QUEBRA GRAVE DA MÁSCARA]]: (+65%% Saciedade | +30%% Exposição | -8 Humanidade | +1 Quebra de Máscara!)"
    hide victor with dissolve

    # Flagrante imediato caso alguma heroína esteja no setor

    if loc_emilia == local_atual:

        $ duvida_emilia += 8
        $ th_bark("emilia", "flagrante")

        show emilia uniforme surpresa meio corpo at sprite_esquerda with dissolve

        emilia "VICTOR!! MEU DEUS... N-NÃO PODE SER!! O QUE VOCÊ FEZ COM ELE?!"

        emilia "Suas presas... o sangue escorrendo pelo seu queixo... Você estava devorando um ser humano?!"

        emilia "As lendas sobre o ghoul do campus... sempre foi você?!"

        hide emilia with dissolve

    elif loc_elara == local_atual:

        $ punicoes_gremio_ativas += 2

        $ hp_jogador = max(5, hp_jogador - 35)
        $ th_bark("elara", "flagrante")

        show elara muito irritada at sprite_esquerda with dissolve

        elara "UM ATAQUE ANIMALESCO DESCARADO DENTRO DO MEU CAMPUS?!"

        elara "O Conselho Estudantil não tolerará uma besta ensandecida desfilando pelo pátio! Ativação punitiva de Grau Dois no Grilhão de Sangue!"

        with vpunch

        with flash_red

        "⚡ O Grilhão de Sangue esmaga seu tórax em resposta à ordem de Elara (-35 HP | +2 Punições do Grêmio)!"

        hide elara with dissolve

    elif loc_mestra == local_atual:

        $ afeto_mestra += 1

        show lility meio corpo maravilhada at sprite_esquerda with dissolve

        mestra "Magnífico, Victor! Ouça o silêncio da presa desfalecendo... Foi para isso que concedi meu sangue a você. Deixe o falso verniz da humanidade queimar!"

        hide lility with dissolve

    elif loc_valeria == local_atual:

        show valeria cinica pirulito meio corpo at sprite_esquerda with dissolve

        valeria "Puta merda, Victor... Olha o estrago no chão. Se a perícia da polícia bater aqui por causa dessa poça, você vai me pagar o triplo em sucata."

        hide valeria with dissolve

    hide mob_npc with dissolve

    jump checar_quebra_mascara_gremio

label checar_quebra_mascara_gremio:

    hide screen overlay_frenesi_vermelho

    # Se a Exposição atingir 80%+, o Conselho Estudantil envia Executores imediatamente!

    if exposicao >= 80:

        if renpy.loadable("audio/Authority_Breach.ogg"):

            play music "audio/Authority_Breach.ogg" if_changed fadein 1.0

        "🚨 [[ALERTA DE QUEBRA DA MÁSCARA — EXPOSIÇÃO CRÍTICA ([exposicao]%%)!]]"

        "O alarme silencioso do Conselho Estudantil ressoa no seu Grilhão de Sangue! Uma Executora Puro-Sangue de uniforme branco intercepta você!"

        call iniciar_combate("Executora de Contenção da Máscara", "inimigo executora conselho ruiva espada", "inimigo executora conselho ruiva espada ataque", 170, 28, 3.4, "gremio", False) from _call_iniciar_combate_6

        $ exposicao = 45

        $ punicoes_gremio_ativas += 1

        "Você sobrevive à emboscada punitiva do Conselho, reduzindo sua Exposição imediata para 45%%, mas o Grilhão cobra seu preço!"

    call screen hud_exploracao_bs

    jump abrir_mapa_tatico

# ==============================================================================

# 9. ENCONTROS ALEATÓRIOS COM AS HEROÍNAS E CLICK & REAÇÃO (FORA DA CAMPANHA)

# ==============================================================================

# --- 9.1 ENCONTRO COM LILITY ---

label menu_encontro_lility:

    hide screen hud_exploracao_bs

    call verificar_reacao_olfativa("lility") from _call_verificar_reacao_olfativa
    $ verificar_reacao_olfativa_heroina("lility")

    call verificar_encontro_agendado("lility", local_atual) from _call_verificar_encontro_agendado

    if status_lility.bloqueada_hoje:

        $ th_bark("lility", "irritada")

        show lility presas agressiva meio corpo at sprite_padrao with dissolve

        mestra "Eu avisei que não quero vê-lo perto de mim pelo resto da noite, lacaio. Saia antes que eu o parta em dois."

        jump entrar_local_exploracao_bs

    if exposicao >= 60 and not getattr(store, "reagiu_exposicao_lility_visita", False):
        $ store.reagiu_exposicao_lility_visita = True
        $ th_bark("lility", "exposicao")
        show lility meio corpo mal humorada at sprite_padrao with dissolve
        mestra "O metal deste grilhão está queimando a minha carne, Victor... Você está deixando rastros desleixados pelos corredores."
        mestra "Os cães do Grêmio e os sentinelas da Igreja já farejaram o seu sangue. Se continuar agindo como uma presa descuidada, serei eu mesma quem cortará a sua garganta para abafar o escândalo."
        $ notificar_rpg("⚡ GRILHÃO EM CHAMAS", f"Exposição Crítica (>=60%): {nome_display_mestra} sente o perigo na própria carne!", "#ff2244")
        $ status_lility.resistencia = min(100, status_lility.resistencia + 5)
    elif fome_sangue <= 20:
        $ th_bark("lility", "fome_critica")
        show lility comportada sorriso meio corpo at sprite_padrao with dissolve
    elif ruina_cain >= 50 and not getattr(store, "avisou_doom_lility_hoje", False):
        $ store.avisou_doom_lility_hoje = True
        $ th_bark("lility", "cain_eco")
        show lility comportada sorriso meio corpo at sprite_padrao with dissolve
    else:
        $ th_bark("lility", "padrao")
        show lility comportada sorriso meio corpo at sprite_padrao with dissolve

    # Eventos Orgânicos / Reativos da Mestra Lility
    if local_atual == "portoes_praca" and periodo == "Noite" and not getattr(store, "ev_fronteira_portoes_lility_visto", False):
        jump ev_lility_fronteira_portoes

    if local_atual in ["patio_arvore", "biblioteca"] and periodo == "Noite" and not getattr(store, "ev_interceptacao_ponto_cego_lility_visto", False):
        jump ev_interceptacao_lility_ponto_cego

    if local_atual == "dormitorio" and periodo == "Noite" and getattr(store, "status_lility", None) and status_lility.afeto >= 6 and getattr(store, "estagio_mestra", 1) >= 2 and not getattr(store, "ev_visita_dormitorio_lility_visto", False):
        jump ev_visita_noturna_lility_dormitorio

    if local_atual == "sala_musica" and periodo == "Noite" and clima_diario_id in ["chuva_vitrais", "chuva", "chuva_acida", "nevoeiro_sangue"] and not getattr(store, "ev_janela_lility_visto", False):
        jump ev_c01_janela_lility

    if loc_emilia == local_atual and local_atual == "biblioteca" and periodo == "Noite" and not getattr(store, "ev_embate_noturno_lility_emilia_visto", False):
        jump ev_embate_noturno_lility_emilia

    if loc_valeria == local_atual and local_atual == "patio_arvore" and not getattr(store, "ev_negociacao_lility_valeria_visto", False):
        jump ev_negociacao_sombra_lility_valeria

    menu:
        "🌟 [[EVENTO DE MARCO DISPONÍVEL!]] Avançar Relação com [nome_display_mestra]" if verificar_marco_disponivel("lility"):

            if estagio_mestra == 1:

                jump evento_marco_lility_1

            else:

                jump evento_marco_lility_2

        "🎁 Entregar Presente Clandestino":

            call fluxo_entregar_presente_heroina("lility") from _call_presente_lility_enc

            jump menu_encontro_lility

        "✋ Aproximar-se / Modo de Toque (Click & Reação)":
            if status_lility.paciencia <= 0:
                $ th_sfx("click")
                $ th_bark("lility", "irritada")
                mestra "Já disse que estou farta de proximidade por este período, Victor. Afaste-se."
                jump menu_encontro_lility
            hide lility
            $ expressao_lility = "lility comportada sorriso meio corpo"
            call screen interacao_toque_lility
            jump menu_encontro_lility

        "🩸 Pedir Audiência para Alimentação no Covil (O Preço do Sangue)":

            jump menu_alimentacao_covil_lility

        "📜 Deixar Bilhete Clandestino (Agendar Encontro Noturno na Sala de Música)" if encontro_agendado_heroina is None and periodo != "Noite":

            $ agendar_encontro_clandestino("lility", "sala_musica", "Noite")

            show lility sorrindo de lado sorrindo at sprite_padrao with dissolve

            mestra "Um bilhete secreto marcando hora no meu piano? Que atrevimento delicioso... Estarei esperando nas sombras."

            jump menu_encontro_lility

        "💬 Conversar com [nome_display_mestra] (Paciência: [status_lility.paciencia]/[status_lility.paciencia_max])" if status_lility.paciencia > 0 and not getattr(store, "conversou_heroina_periodo", {}).get("lility", False):
            $ conversou_heroina_periodo["lility"] = True
            $ status_lility.gastar_paciencia(1)

            menu:

                "\"Como você suporta ficar confinada nesta sala de música há tanto tempo?\"":

                    $ intelecto += 1

                    $ reagir_escolha("lility", "morbido")

                    show lility meio corpo desdenhando at sprite_padrao with dissolve

                    mestra "Tempo...{w=0.3} Uma invenção tola dos mortais para justificar a própria pressa."

                    show lility comportada sorriso meio corpo at sprite_padrao with dissolve

                    mestra "Um século trancada aqui não é nada para quem viu civilizações inteiras afundarem na lama.{w=0.4} O tédio... só é perigoso quando me dá vontade de brincar."

                "\"Elara realmente tem controle total sobre você com esse Grilhão?\"":

                    $ coragem += 1

                    $ reagir_escolha("lility", "autoridade")

                    if punicoes_gremio_ativas >= 1:
                        show lility meio corpo gelida at sprite_padrao with dissolve
                        mestra "O metal arde na minha carne porque você foi descuidado nos corredores, Victor. Mas não confunda a dor passageira de um feitiço de sangue com subserviência."

                    show lility meio corpo desdenhando at sprite_padrao with dissolve

                    mestra "Aquela boneca de porcelana do Conselho? Nós temos problemas muito maiores até o Eclipse do que os latidos de uma cã de uniforme branco que se acha rainha."

                    show lility confiante sorriso meio corpo at risada_deboche

                    mestra "Deixe que ela finja que manda em mim.{w=0.4} A coleira dela aperta o pescoço... mas quem controla a sede lá embaixo somos nós."

                "\"Espero que o meu sangue não esteja deixando a 'Mestra' mimada demais.\"":

                    $ charme += 1

                    $ reagir_escolha("lility", "sarcasmo")

                    show lility superior sarcasmo meio corpo at risada_deboche

                    mestra "Mimada?{w=0.3} Ora, que cachorrinho audacioso."

                    mestra "Agradeça por eu não ter arrancado o seu braço como aperitivo hoje, VV.{w=0.4} Mas continue insolente... Eu prefiro servos com garras a capachos submissos."

                    jump menu_encontro_lility

        "💬 Já conversou com [nome_display_mestra] neste período" if getattr(store, "conversou_heroina_periodo", {}).get("lility", False):
            show lility comportada sorriso meio corpo at sprite_padrao with dissolve
            $ th_bark("lility", "deboche")
            mestra "Já desperdiçamos palavras demais sob esta luz, lacaio. Guarde o fôlego para quando a noite exigir mais de você."
            jump menu_encontro_lility

        "⚖️ Pressionar [nome_display_mestra] com Domínio (Duelo Social / Exigir Respostas)" if status_lility.paciencia > 0:

            $ alav_usar = status_lility.alavancagens[0] if status_lility.alavancagens else None

            $ sucesso, motivo = tentar_acao_social(status_lility, dificuldade=45, atributo_usado="dominio", valor_atributo=dominio_jogador, alavancagem_usada=alav_usar)

            if sucesso:

                show lility com vergonha olhando de lado at sprite_padrao with dissolve

                mestra "Ora, ora... quem ensinou meu cachorrinho a rosnar com tanta convicção? Talvez haja mais sangue primordial em você do que imaginei."

                $ ressonancia_pre_diluviana += 1

                $ afeto_mestra += 1

            else:

                show lility presas agressiva meio corpo at sprite_padrao with dissolve

                mestra "Não ouse tentar impor sua vontade contra sua criadora, lacaio. Lembre-se de onde veio sua coleira."

                jump menu_encontro_lility

        "👣 Continuar Investigando a Área":
            $ th_bark("lility", "despedida")
            hide lility with dissolve

            jump entrar_local_exploracao_bs

label menu_alimentacao_covil_lility:

    hide screen hud_exploracao_bs

    # Verificação de Sangue Litúrgico (Rivalidade Inquisitorial)

    if getattr(store, "sangue_liturgico_ativo", False):

        show lility presas agressiva meio corpo at sprite_padrao with vpunch

        mestra "Que asco intolerável... O aroma de mirra e eucaristia daquela caçadora dos von Karsten está impregnado na sua garganta!"

        mestra "Você ousa pedir o meu sangue sagrado enquanto ainda digere o veneno da Igreja?! Afaste-se de mim antes que eu queime as suas vísceras!"

        $ duvida_mestra += 2

        $ status_lility.duvida += 2

        jump menu_encontro_lility

    if status_lility.bloqueada_hoje:

        show lility presas agressiva meio corpo at sprite_padrao with dissolve

        mestra "Dê mais um passo e eu mesma arranco a sua garganta, lacaio. Saia daqui!"

        jump menu_encontro_lility

    if alimentou_lility_periodo:

        show lility meio corpo mal humorada at sprite_padrao with dissolve

        mestra "Você já bebeu das minhas veias neste período, cachorrinho. Uma dama não é uma torneira pública. Deixe meu sangue assentar antes de me incomodar de novo."

        jump menu_encontro_lility

    if fome_sangue >= 85:

        show lility meio corpo entediada at sprite_padrao with dissolve

        mestra "Você não está à beira da loucura, Victor. Suas veias não tremem, sua respiração está calma. Não desperdice o meu sangue por puro capricho. Volte quando a fome realmente arder."

        jump menu_encontro_lility

    show lility comportada sorriso meio corpo at sprite_padrao with dissolve

    mestra "Você veio até o meu piano suplicando pelo meu pulso... Mas sabe muito bem que nada neste mundo é gratuito, calouro. O que você me trouxe em troca?"

    menu:

        "🍾 Oferecer Dose de Absinto Esmeralda (1x Absinto) — Oferenda de Luxo" if dose_absinto >= 1:

            $ dose_absinto -= 1

            $ alimentou_lility_periodo = True

            $ oferendas_lility_entregues += 1

            $ alimentar_de_heroina("lility", qtd_sangue=100, ganho_vinculo=15, ganho_afeto=2)

            $ afeto_mestra = status_lility.afeto

            $ vinculo_sangue_lility = status_lility.vinculo_sangue

            show lility meio corpo maravilhada at sprite_padrao with dissolve

            mestra "Absinto destilado nas panelas de cobre das caldeiras... O aroma da artemísia quase disfarça a fuligem deste colégio decadente."

            show lility comportada sorriso meio corpo at sprite_padrao with dissolve

            mestra "Você tem modos afinal, calouro. Aprendeu rápido que uma dama não oferece seu néctar a quem chega de mãos abanando."

            "Ela recebe a dose com dedos delicados, provando uma gota na ponta da língua antes de estender o pulso alvo como mármore."

            call executar_transe_sangue("lility") from _call_executar_transe_sangue

            call restaurar_fundo_local_atual from _call_restaurar_fundo_lility_1

            show lility confiante sorriso meio corpo at sprite_padrao with dissolve

            mestra "Beba devagar... saboreie o calor de quem ainda se importa se você respira amanhã. Agora você carrega meu odor."

            jump menu_encontro_lility

        "🎼 Oferecer Partitura Rúnica (Relíquia Antiga) — Oferenda Magna" if tem_partitura_runica and oferendas_lility_entregues == 0:

            $ tem_partitura_runica = False

            $ oferendas_lility_entregues += 1

            $ alimentou_lility_periodo = True

            $ alimentar_de_heroina("lility", qtd_sangue=100, ganho_vinculo=25, ganho_afeto=3)

            $ afeto_mestra = status_lility.afeto

            $ vinculo_sangue_lility = status_lility.vinculo_sangue

            show lility vulneravel timida meio corpo at sprite_padrao with dissolve

            mestra "A partitura... Minhas notas originais, traçadas antes de Elara me trancar nesta sala carcomida..."

            "Pela primeira vez, a máscara de soberba da minha mestra treme. Seus olhos carmesins fixam as pautas amareladas com uma nostalgia quase dolorosa."

            show lility comportada sorriso meio corpo at sprite_padrao with dissolve

            mestra "Talvez você não seja apenas um cão assustado afinal, Victor. Aproxime-se. Deixe que eu te recompense como um verdadeiro aliado merece."

            call executar_transe_sangue("lility") from _call_executar_transe_sangue_1
            call restaurar_fundo_local_atual from _call_restaurar_fundo_lility_2

            show lility confiante sorriso meio corpo at sprite_padrao with dissolve

            mestra "O sangue que corre entre nós hoje tem o sabor de eras passadas... Uma aliança viva."

            jump menu_encontro_lility

        "📜 Entregar Inteligência sobre Elara (Relatório Político)" if relatorio_gremio_obtido or MISTERIOS_ACADEMIA["inquerito_inquisicao"].pistas_coletadas >= 1:

            $ relatorio_gremio_obtido = False

            $ alimentou_lility_periodo = True

            $ exposicao = max(0, exposicao - 10)

            $ alimentar_de_heroina("lility", qtd_sangue=70, ganho_vinculo=10, ganho_afeto=1)

            $ afeto_mestra = status_lility.afeto

            $ vinculo_sangue_lility = status_lility.vinculo_sangue

            show lility meio corpo desdenhando at sprite_padrao with dissolve

            mestra "Então a puritana de branco anda deslocando os cães do conselho para vigiar o perímetro leste? Previsível... Ela sempre teme o que não pode controlar."

            show lility comportada sorriso meio corpo at sprite_padrao with dissolve

            mestra "Informação de qualidade vale mais do que ouro nos corredores, Victor. Venha. Você conquistou o seu pagamento de hoje."

            call executar_transe_sangue("lility") from _call_executar_transe_sangue_2
            call restaurar_fundo_local_atual from _call_restaurar_fundo_lility_3

            show lility confiante sorriso meio corpo at sprite_padrao with dissolve

            mestra "Aproveite bem a saciedade. E continue de olhos e ouvidos bem abertos nos corredores de Elara."

            jump menu_encontro_lility

        "🩸 Suplicar de Mãos Vazias: A Confissão Íntima (-2 Humanidade / +60%% Saciedade)":

            $ alimentou_lility_periodo = True

            $ confissoes_lility_realizadas += 1

            $ humanidade = max(0, humanidade - 2)

            $ alimentar_de_heroina("lility", qtd_sangue=60, ganho_vinculo=10, ganho_afeto=1)

            $ afeto_mestra = status_lility.afeto

            $ vinculo_sangue_lility = status_lility.vinculo_sangue

            show lility meio corpo desdenhando at sprite_padrao with dissolve

            mestra "Veio de mãos abanando, cachorrinho? Sem uma garrafa, sem um relatório, tremendo de fome diante do meu piano..."

            show lility meio corpo sorriso malicioso at sprite_padrao with dissolve

            mestra "Se quer que eu abra minhas veias por misericórdia pura, terá que pagar com algo mais caro do que moedas, Victor. Quero a verdade."

            mestra "Diga-me... qual foi a sensação exata no seu peito quando aquele seu professor covarde sorriu para você e te empurrou para a sarjeta?"

            menu:

                "“Senti que a decência humana era uma piada inventada por fracos.” (+Intelecto / -1 Humanidade)":

                    $ intelecto += 1

                    $ humanidade = max(0, humanidade - 1)

                    show lility meio corpo desdenhando at sprite_padrao with dissolve

                    mestra "Uma conclusão amarga, mas lúcida. A fraqueza é a única praga que os homens nunca conseguem expurgar."

                "“Senti vontade de vê-lo engolir os próprios dentes no chão do laboratório.” (+Coragem / +1 Ressonância)":

                    $ coragem += 1

                    $ ressonancia_pre_diluviana += 1

                    show lility presas agressiva meio corpo at sprite_padrao with dissolve

                    mestra "A fúria de quem foi traído... É essa chama que me impediu de deixar você morrer ontem à noite."

                "“Senti apenas frio. E a certeza de que nunca mais dependeria da piedade de ninguém.” (+Afeto / +Vínculo)":

                    $ afeto_mestra += 1

                    $ vinculo_sangue_lility = min(100, vinculo_sangue_lility + 5)

                    show lility vulneravel timida meio corpo at sprite_padrao with dissolve

                    mestra "Frio... É um velho conhecido meu. Uma solidão que não se apaga nem depois de séculos."

            "[nome_display_mestra] aproxima os dedos do meu queixo, forçando meu olhar ao encontro do dela, antes de deslizar a manga e expor a veia pulsante."

            call executar_transe_sangue("lility") from _call_executar_transe_sangue_3
            call restaurar_fundo_local_atual from _call_restaurar_fundo_lility_4

            show lility confiante sorriso meio corpo at sprite_padrao with dissolve

            mestra "Beba, Victor. Suas feridas e seus pecados agora correm comigo."

            jump menu_encontro_lility

        "⚡ Suplicar de Mãos Vazias: Transe Violento (-15 HP / -3 Humanidade / +2 Ressonância / +80%% Saciedade)":

            $ alimentou_lility_periodo = True

            $ hp_jogador = max(1, hp_jogador - 15)

            $ humanidade = max(0, humanidade - 3)

            $ ressonancia_pre_diluviana += 2

            $ alimentar_de_heroina("lility", qtd_sangue=80, ganho_vinculo=5, ganho_afeto=0)

            $ afeto_mestra = status_lility.afeto

            $ vinculo_sangue_lility = status_lility.vinculo_sangue

            show lility presas agressiva meio corpo at sprite_padrao with dissolve

            mestra "Quer o meu sangue sem concessões, sem palavras e sem oferendas? Então aguente o peso do que está pedindo!"

            "Ela agarra minha nuca com força inumana e pressiona o pulso aberto contra meus lábios com violência febril."

            $ th_sfx("heartbeat")

            with flash_red

            with vpunch

            "O sangue ancestral entra como chumbo líquido na minha garganta! O impacto é tão avassalador que meus joelhos batem com estrondo na madeira carcomida do chão."

            "Visões de cidades submersas e colunas ciclópeas colidem no meu crânio com a violência de uma avalanche! Minha mente vacila no limiar do colapso."

            call executar_transe_sangue("lility") from _call_executar_transe_sangue_4
            call restaurar_fundo_local_atual from _call_restaurar_fundo_lility_5

            show lility meio corpo desdenhando at sprite_padrao with dissolve

            mestra "Levante-se, lacaio. Se não for capaz de suportar um trago cru do meu poder, não durará uma semana neste colégio."

            jump menu_encontro_lility

        "🔙 Voltar":

            jump menu_encontro_lility

label tocou_cabeca_lility:
    if afeto_mestra >= 6:
        $ th_sfx("splash")
        $ status_lility.gastar_paciencia(1)
        $ anim_toque_lility = atl_poke_suave
        if not tocou_heroina_periodo.get("lility", False):
            $ tocou_heroina_periodo["lility"] = True
            $ th_bark("lility", "toque_orelha")
            $ expressao_lility = "lility carinho na cabeca"
            $ afeto_mestra += 1
            $ humor_mestra = "provocadora"
            show expression expressao_lility at sprite_padrao, atl_poke_suave with dissolve
            mestra "Hmph... Fazendo cafuné na própria dona, cachorrinho? Vou permitir só porque suas mãos estão quentes."
            $ notificar_rpg("✋ TOQUE AFETUOSO", f"+1 Afeto com {nome_display_mestra} (Limite por período atingido)", "#cc66ff")
        else:
            $ expressao_lility = "lility carinho na cabeca"
            show expression expressao_lility at sprite_padrao, atl_poke_suave with dissolve
            mestra "Já sentiu o calor dos meus cabelos por hoje, Victor. Deixe um pouco de audácia para mais tarde."
    else:
        $ th_sfx("click")
        $ status_lility.gastar_paciencia(1)
        $ anim_toque_lility = atl_poke_recuo
        $ th_bark("lility", "irritada")
        $ expressao_lility = "lility com a mao levantada"
        show expression expressao_lility at sprite_padrao, atl_poke_recuo with dissolve
        mestra "O que pensa que está fazendo? Não sou um animal de estimação para receber carinho na cabeça."

    if status_lility.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_lility = "lility com a mao levantada"
        mestra "Minha tolerância com as suas distrações chegou ao fim por hoje, Victor. Volte aos seus afazeres."
        jump menu_encontro_lility

    call screen interacao_toque_lility
    jump menu_encontro_lility

label tocou_rosto_lility:
    $ th_sfx("click")
    $ status_lility.gastar_paciencia(1)
    $ anim_toque_lility = atl_poke_recuo
    $ th_bark("lility", "irritada")
    if afeto_mestra >= 8:
        $ expressao_lility = "lility sorrindo e com bochechas vermelhas"
    else:
        $ expressao_lility = "lility com a mao levantada"
    show expression expressao_lility at sprite_padrao, atl_poke_recuo with dissolve
    mestra "Cuidado onde encosta, Victor... Minhas presas estão muito perto dos seus dedos."

    if status_lility.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_lility = "lility com a mao levantada"
        mestra "Basta de ousadia por este período. Dê um passo para trás."
        jump menu_encontro_lility

    call screen interacao_toque_lility
    jump menu_encontro_lility

label tocou_peito_lility:
    $ th_sfx("click")
    $ status_lility.gastar_paciencia(2)
    $ anim_toque_lility = atl_poke_recuo
    $ cliques_irritantes_lility += 1
    if cliques_irritantes_lility == 1:
        $ th_bark("lility", "toque_broche")
        $ expressao_lility = "lility com a mao levantada"
        show expression expressao_lility at sprite_padrao, atl_poke_recuo with dissolve
        with vpunch
        mestra "Perdeu o juízo junto com a sua humanidade, lacaio? Encoste a mão aí de novo sem permissão e voltará para o quarto com quatro dedos."
    else:
        $ expressao_lility = "lility presas agressiva meio corpo"
        show expression expressao_lility at sprite_padrao, atl_poke_recuo with dissolve
        with hpunch
        $ hp_jogador = max(1, hp_jogador - 15)
        $ humor_mestra = "feroz"
        mestra "Eu avisei! Parece que meu cachorrinho precisa aprender limites através da dor! (-15 HP)"

    if status_lility.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_lility = "lility com a mao levantada"
        mestra "Minha paciência se esgotou por completo. Afaste-se antes que eu me esqueça do nosso pacto."
        jump menu_encontro_lility

    call screen interacao_toque_lility
    jump menu_encontro_lility

# Evento Matinal — Lility Dormindo

label evento_rng_lility_dormindo_manha:

    scene lility cena dormindo with fade

    if renpy.loadable("audio/sighs_in_the_dark.ogg"):

        play music "audio/sighs_in_the_dark.ogg" if_changed fadein 1.5

    "A luz pálida da manhã atravessa a janela empoeirada. Exausta pela vigília noturna, [nome_display_mestra] apagou profundamente sobre o sofá."

    $ cliques_sono_lility = 0

    call screen interacao_lility_dormindo
    jump lility_acorda_assustada

label toque_sono_cabeca:

    $ cliques_sono_lility += 1

    $ afeto_mestra += 1

    "Deslizo os dedos pelos cabelos carmesim dela. Dormindo, ela solta um suspiro baixo e inclina a cabeça na direção do calor da minha mão."

    if cliques_sono_lility >= 3:

        jump lility_acorda_assustada

    call screen interacao_lility_dormindo
    jump lility_acorda_assustada

label toque_sono_bochecha:

    $ cliques_sono_lility += 1

    "Toco a bochecha fria dela. Ela murmura baixinho durante o sono: '...Está tão silencioso... não deixe a água subir...'"

    if cliques_sono_lility >= 3:

        jump lility_acorda_assustada

    call screen interacao_lility_dormindo
    jump lility_acorda_assustada

label toque_sono_ombros:

    $ cliques_sono_lility += 1

    $ humanidade = min(100, humanidade + 2)

    "Ajeito meu blazer sobre os ombros dela para protegê-la do vento frio da manhã (+2 Humanidade)."

    if cliques_sono_lility >= 3:

        jump lility_acorda_assustada

    call screen interacao_lility_dormindo
    jump lility_acorda_assustada

label lility_acorda_assustada:
    $ local_atual = "sala_musica"
    call restaurar_fundo_local_atual

    $ th_bark("lility", "timida")

    show lility meio corpo chocada at pulo_susto

    mestra "O-o quê?! Há quanto tempo você está parado aí, seu insolente?!"

    show lility com vergonha olhando de lado at sprite_padrao with dissolve

    mestra "Eu não estava dormindo! Estava apenas... meditando com os olhos fechados! Saia daqui antes que eu drene você!"

    jump entrar_local_exploracao_bs

label sair_sem_acordar_lility:

    "Saio na ponta dos pés, deixando-a descansar em paz."

    jump entrar_local_exploracao_bs

# --- 9.2 ENCONTRO COM EMÍLIA ---

label menu_encontro_emilia:

    hide screen hud_exploracao_bs

    call verificar_reacao_olfativa("emilia") from _call_verificar_reacao_olfativa_1
    $ verificar_reacao_olfativa_heroina("emilia")

    call verificar_encontro_agendado("emilia", local_atual) from _call_verificar_encontro_agendado_1

    if humanidade < 35:

        $ th_bark("emilia", "irritada")

        show emilia uniforme seria investigativa meio corpo at sprite_padrao with dissolve

        emilia "Victor... Dê um passo para trás. A pupila dilatada, a retração na gengiva... A máscara humana está cedendo. O que você andou fazendo nos corredores?"

        $ status_emilia.duvida += 1

        $ notificar_rpg("⚠️ PÂNICO INQUISITORIAL", "Emília notou seus traços de monstro (+1 Suspeita)!", "#ff4444")

    elif status_emilia.bloqueada_hoje:

        $ th_bark("emilia", "irritada")

        show emilia uniforme seria investigativa meio corpo at sprite_padrao with dissolve

        emilia "Por favor, Victor... preciso de espaço para rezar e pensar no que está acontecendo nesta escola. Não se aproxime de mim por hoje."

        jump entrar_local_exploracao_bs

    else:

        if exposicao >= 60 and not getattr(store, "reagiu_exposicao_emilia_visita", False):
            $ store.reagiu_exposicao_emilia_visita = True
            $ th_bark("emilia", "exposicao")
            show emilia uniforme seria investigativa meio corpo at sprite_padrao with dissolve
            emilia "Victor... Por favor, mantenha distância agora. Há patrulhas do Grêmio e sentinelas da ordem do meu pai inspecionando cada corredor."
            emilia "O seu nome está circulando nos despachos disciplinares... Você foi visto em locais proibidos. Se virem nós dois conversando a sós, nem mesmo a cruz da minha família poderá livrar você da inquisição."
            $ notificar_rpg("👁️ VIGILÂNCIA OSTENSIVA", "Exposição Crítica (>=60%): Emília está sob vigilância rígida (+1 Dúvida)!", "#ffaa00")
            $ status_emilia.duvida = min(10, status_emilia.duvida + 1)

        elif not saudou_heroina_visita:
            $ saudou_heroina_visita = True
            if fome_sangue <= 20:
                $ th_bark("emilia", "fome_critica")
            elif ruina_cain >= 50 and not getattr(store, "avisou_doom_emilia_hoje", False):
                $ store.avisou_doom_emilia_hoje = True
                $ th_bark("emilia", "doom")
            else:
                $ th_bark("emilia", "padrao")
            show emilia uniforme calma meio corpo at sprite_padrao with dissolve

        else:

            show emilia uniforme calma meio corpo at sprite_padrao

    # Eventos Orgânicos / DOOM de Emília (Gatilhos estritamente locais para evitar descompasso de cenários)
    if local_atual == "biblioteca" and loc_mestra == "biblioteca" and periodo == "Noite" and not getattr(store, "ev_embate_noturno_lility_emilia_visto", False):
        jump ev_embate_noturno_lility_emilia

    if local_atual == "dormitorio" and periodo in ["Manhã", "Tarde"] and not getattr(store, "ev_voce_nao_come_visto", False):
        jump ev_c05_voce_nao_come

    if local_atual == "sala_ocultismo" and (ruina_cain >= 20 or status_emilia.afeto >= 6 or getattr(status_emilia, "duvida", 0) >= 15) and not getattr(store, "ev_lista_rh_nulo_visto", False):
        jump ev_c06_lista_rh_nulo

    menu:
        "🩹 Pedir que Emília trate suas feridas com Gaze Consagrada" if (sequelas_ativas or hp_jogador < hp_jogador_max) and not getattr(store, "emilia_curou_hoje", False):
            $ emilia_curou_hoje = True
            $ hp_jogador = min(hp_jogador_max, hp_jogador + 35)
            if sequelas_ativas:
                $ _seq = sequelas_ativas[0]["nome"]
                $ curar_sequela(sequelas_ativas[0]["id"])
                $ notificar_rpg("🩹 SEQUELA CURADA", f"Emília purificou a sequela [[{_seq}]]!", "#44ff88")
            show emilia uniforme seria triste meio corpo at sprite_padrao with dissolve
            $ th_voz("climax/emilia_marco_curativo")
            emilia "Fique quieto... A gaze sagrada queima na carne corrompida, mas impede que a podridão alcance o seu coração."
            $ notificar_rpg("✝️ CUIDADO SAGRADO", "+35 HP restaurados | Purificação Sagrada", "#88ccff")
            jump menu_encontro_emilia

        "🖼️ Entregar crachá de Danilo Ramos resgatado do mundo pintado" if getattr(store, "cracha_aluno_desaparecido", False) and not getattr(store, "entregou_cracha_emilia", False):
            jump entregar_cracha_emilia

        "🌟 [[EVENTO DE MARCO DISPONÍVEL!]] Avançar Relação com Emília" if verificar_marco_disponivel("emilia"):

            if estagio_emilia == 1:

                jump evento_marco_emilia_1

            else:

                jump evento_marco_emilia_2

        "✝️ [[O CONFRONTO DA CAÇADORA]]: Selar o Pacto de Sangue com Emília" if not pacto_emilia_ativo and estagio_emilia >= 2:

            jump evento_emilia_pacto_sangue

        "🎁 Entregar Presente Clandestino":

            call fluxo_entregar_presente_heroina("emilia") from _call_presente_emilia_enc

            jump menu_encontro_emilia

        "✋ Aproximar-se / Modo de Toque (Click & Reação)":
            if status_emilia.paciencia <= 0:
                $ th_sfx("click")
                $ th_bark("emilia", "timida")
                emilia "Victor... agora não. Minha cabeça está latejando com o incenso da capela e as anotações do dia. Dê-me um período para respirar."
                jump menu_encontro_emilia
            hide emilia
            $ expressao_emilia = "emilia uniforme calma meio corpo"
            call screen interacao_toque_emilia
            jump menu_encontro_emilia

        "🩸 Pedir o Sustento Sagrado (Pacto de Sangue von Karsten)" if pacto_emilia_ativo and status_emilia.paciencia > 0:

            $ status_emilia.gastar_paciencia(1)

            show emilia uniforme corada timida meio corpo at sprite_padrao with dissolve

            emilia "Aqui não, Victor. Tem duas janelas com vista para o claustro e a ronda do Conselho passa em cinco minutos. Venha atrás do biombo da biblioteca... E traga o lenço. Isto não vai para os registros."

            "Emília afasta a gola do uniforme com firmeza contida. Quando cravo os caninos com cautela em sua pele alva, o calor do sangue sagrado queima como licor puro, afastando todo o gelo da minha garganta."

            call executar_transe_sangue("emilia") from _call_executar_transe_sangue_5

            $ alimentar_de_heroina("emilia", qtd_sangue=45, ganho_vinculo=15, ganho_afeto=5)

            hide cena with dissolve
            call restaurar_fundo_local_atual from _call_restaurar_fundo_emilia_1

            show emilia uniforme corada timida meio corpo at sprite_padrao with dissolve
            emilia "Ah...! Pelos céus... Mantenha o controle... Já basta, Victor... Alguém pode ouvir os passos no corredor..."
            jump menu_encontro_emilia

        "📜 Deixar Bilhete Clandestino (Agendar Encontro Noturno no Clube de Ocultismo)" if pacto_emilia_ativo and encontro_agendado_heroina is None and periodo != "Noite":

            $ agendar_encontro_clandestino("emilia", "sala_ocultismo", "Noite")

            show emilia com vergonha arrumando o oculos e olhando para o lado e fofa at sprite_padrao with dissolve

            emilia "Um bilhete direto sob o meu caderno? Victor... se a patrulha de Elara intercepta isso, o inquérito cai sobre nós dois. Mas... estarei lá antes que tranquem a ala leste. Seja pontual."

            jump menu_encontro_emilia

        "💬 Conversar com Emília (Paciência: [status_emilia.paciencia]/[status_emilia.paciencia_max])" if status_emilia.paciencia > 0 and not getattr(store, "conversou_heroina_periodo", {}).get("emilia", False):
            $ conversou_heroina_periodo["emilia"] = True
            $ status_emilia.gastar_paciencia(1)

            if hp_jogador < hp_jogador_max and not emilia_curativo_feito_visita:

                $ emilia_curativo_feito_visita = True

                $ hp_jogador = min(hp_jogador_max, hp_jogador + 20)

                show emilia uniforme seria investigativa meio corpo at sprite_padrao with dissolve

                emilia "Victor...!{w=0.3} Você está ferido de novo."

                show emilia uniforme sorriso amigavel meio corpo at sprite_padrao with dissolve

                emilia "Fique parado um instante...{w=0.3} Deixe-me trocar esse curativo antes que infeccione.{w=0.4} Pronto... Não faça essa cara de dor. (+20 HP)"

                $ reagir_escolha("emilia", "compaixao")

            else:

                show emilia uniforme calma meio corpo at sprite_padrao with dissolve

                emilia "Sobre o que você gostaria de conversar, Victor?"

            menu:

                    "\"Alguma novidade sobre os desaparecimentos nos corredores?\"":

                        $ intelecto += 1

                        $ reagir_escolha("emilia", "ocultismo")

                        show emilia uniforme ajeitando oculos meio corpo at sprite_padrao with dissolve

                        emilia "Três novos registros só esta semana...{w=0.3} A direção arquivou todos como 'evasão voluntária'."

                        show emilia uniforme seria investigativa meio corpo at sprite_padrao with dissolve

                        emilia "Ninguém foge do colégio de madrugada sem levar as próprias malas, Victor.{w=0.4} Algo está se alimentando aqui dentro."

                        if not desbloqueou_banheiro_abandonado:

                            $ desbloqueou_banheiro_abandonado = True

                            emilia "O último rastro levava para a ala fechada do segundo andar... Mais especificamente para o antigo banheiro interditado."

                            show emilia com olhar investigativo at sprite_padrao with dissolve

                            emilia "Encontraram respingos de sangue coagulado diante do grande espelho rachado. Por favor, Victor... me prometa que você não vai se aproximar daquele lugar."

                            $ notificar_rpg("🪞 NOVA ÁREA DESCOBERTA", "Banheiro Abandonado (2º Andar) liberado no Mapa Tático!", "#ff88aa")

                    "\"Ouvi rumores sobre um banheiro interditado no segundo andar...\"" if not desbloqueou_banheiro_abandonado:

                        $ intelecto += 1

                        $ desbloqueou_banheiro_abandonado = True

                        $ reagir_escolha("emilia", "ocultismo")

                        show emilia uniforme seria investigativa meio corpo at sprite_padrao with dissolve

                        emilia "Você não deveria saber sobre isso, Victor...!{w=0.3} A ala foi isolada porque encontraram um calouro em transe hipnótico diante do espelho."

                        show emilia com olhar investigativo at sprite_padrao with dissolve

                        emilia "Ele murmurava sobre uma silhueta loira de olhos vermelhos presa atrás do vidro... O conselho quer abafar o caso, mas a porta está apenas encostada."

                        $ notificar_rpg("🪞 NOVA ÁREA DESCOBERTA", "Banheiro Abandonado (2º Andar) liberado no Mapa Tático!", "#ff88aa")

                    "\"Você parece exausta, Emília. Dormiu alguma coisa essa noite?\"":

                        $ afeto_emilia += 1

                        $ reagir_escolha("emilia", "gentileza")

                        show emilia com vergonha arrumando o oculos e olhando para o lado e fofa at sprite_padrao with dissolve

                        emilia "Duas horas.{w=0.3} Três se contar o tempo em que fiquei encarando o teto contando as badaladas do relógio da capela."

                        show emilia uniforme sorriso timido meio corpo at sprite_padrao with dissolve

                        emilia "Estava cruzando os horários das rondas com os relatórios de evasão e transferências...{w=0.4} Mas... obrigada por notar. As pessoas nesta academia só reparam quando você para de funcionar."

                    "\"Anotando mais detalhes sobre mim no seu caderninho secreto?\"":

                        $ charme += 1

                        $ reagir_escolha("emilia", "sarcasmo")

                        show emilia uniforme ajeitando oculos meio corpo at sprite_padrao with dissolve

                        emilia "Não é segredo, Victor.{w=0.3} É metodologia investigativa."

                        show emilia com vergonha arrumando o oculos e olhando para o lado e fofa at sprite_padrao with dissolve

                        emilia "Há três páginas com a sua rotina: os horários em que sai do dormitório, os desvios perto das caldeiras e a frequência com que suas mãos tremem.{w=0.4} Se eu não monitorar onde você pisa, serei eu quem terá que assinar seu laudo de transferência."

            if "olhar_compassivo" in perks_desbloqueados and status_emilia.duvida > 0:

                $ status_emilia.duvida = max(0, status_emilia.duvida - 1)

                $ notificar_rpg("💙 OLHAR COMPASSIVO", "Seu olhar sereno acalmou as suspeitas de Emília (-1 Dúvida).", "#88ccff")

                jump menu_encontro_emilia

        "💬 Já conversou com Emília neste período" if getattr(store, "conversou_heroina_periodo", {}).get("emilia", False):
            show emilia uniforme seria investigativa meio corpo at sprite_padrao with dissolve
            $ th_bark("emilia", "suspeita")
            emilia "Victor, precisamos ser discretos... Se os vigilantes do meu pai nos virem conversando por tanto tempo no mesmo turno, suspeitarão de algo. Falamos no próximo período."
            jump menu_encontro_emilia

        "⚖️ Sondar Pistas da Inquisição (Duelo Social de Charme)" if status_emilia.paciencia > 0:

            $ alav_usar = status_emilia.alavancagens[0] if status_emilia.alavancagens else None

            $ sucesso, motivo = tentar_acao_social(status_emilia, dificuldade=35, atributo_usado="charme", valor_atributo=charme, alavancagem_usada=alav_usar)

            if sucesso:

                show emilia com vergonha e fofa at sprite_padrao with dissolve

                emilia "B-bem... meu pai me enviou alguns relatórios sobre o selo do subsolo... Se prometer não contar a ninguém, posso compartilhar uma anotação com você..."

                $ conhecimento_oculto += 1

                $ status_emilia.afeto += 1

            else:

                show emilia com olhar investigativo at sprite_padrao with dissolve

                emilia "Por que você está tão interessado nos segredos da Inquisição, Victor? Isso não parece curiosidade de um estudante comum..."

                jump menu_encontro_emilia

        "👣 Continuar Investigando a Área":
            $ th_bark("emilia", "despedida")
            hide emilia with dissolve
            $ saudou_heroina_visita = False
            $ emilia_curativo_feito_visita = False
            $ reagiu_exposicao_emilia_visita = False
            jump entrar_local_exploracao_bs

label tocou_cabeca_emilia:
    $ toques_emilia += 1
    if not tocou_heroina_periodo.get("emilia", False):
        if status_emilia.duvida <= 2:
            $ th_sfx("splash")
            $ status_emilia.gastar_paciencia(1)
            $ anim_toque_emilia = atl_poke_suave
            $ tocou_heroina_periodo["emilia"] = True
            $ th_bark("emilia", "toque_calor")
            $ afeto_emilia += 1
            $ humanidade = min(100, humanidade + 1)
            $ expressao_emilia = "emilia fofa toque no rosto"
            show expression expressao_emilia at sprite_padrao, atl_poke_suave with dissolve
            emilia "Victor... Sua mão está fria, mas é um toque limpo, sem o miasma da cripta... Não esperava que você fosse buscar refúgio em mim."
            $ notificar_rpg("✋ CARINHO GENTIL", "+1 Afeto Emília | +1 Humanidade (Limite por período atingido)", "#88ccff")
        else:
            $ th_sfx("click")
            $ status_emilia.gastar_paciencia(1)
            $ anim_toque_emilia = atl_poke_recuo
            $ th_bark("emilia", "timida")
            $ expressao_emilia = "emilia com vergonha segurando a cruz"
            show expression expressao_emilia at sprite_padrao, atl_poke_recuo with dissolve
            emilia "Victor, recue um passo. Não encoste sem permissão enquanto o meu caderno tiver tantas perguntas sem resposta sobre você."
    else:
        $ th_sfx("splash")
        $ status_emilia.gastar_paciencia(1)
        $ anim_toque_emilia = atl_poke_suave
        $ th_bark("emilia", "timida")
        $ expressao_emilia = "emilia fofa toque no rosto"
        show expression expressao_emilia at sprite_padrao, atl_poke_suave with dissolve
        emilia "Victor... já basta de toques por este turno. O monitor da ala leste passa por aqui a qualquer instante. Guarde o decoro."

    if status_emilia.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_emilia = "emilia com vergonha segurando a cruz"
        emilia "Victor... meu limite para conversas acabou por agora. Preciso reorganizar as notas da autópsia e os registros da capela. Falamos mais tarde."
        jump menu_encontro_emilia

    call screen interacao_toque_emilia
    jump menu_encontro_emilia

label tocou_oculos_emilia:
    $ th_bark("emilia", "toque_oculos")
    if not tocou_heroina_periodo.get("emilia", False) and status_emilia.duvida <= 1 and afeto_emilia >= 4:
        $ th_sfx("splash")
        $ status_emilia.gastar_paciencia(1)
        $ anim_toque_emilia = atl_poke_suave
        $ tocou_heroina_periodo["emilia"] = True
        $ afeto_emilia += 1
        $ expressao_emilia = "emilia fofa toque no rosto"
        show expression expressao_emilia at sprite_padrao, atl_poke_suave with dissolve
        emilia "Os óculos estavam tortos? A armação de prata vive cedendo quando passo a noite na biblioteca... Não chegue tão perto sem avisar. Minhas anotações exigem concentração."
        $ notificar_rpg("👓 AJUSTE DE ÓCULOS", "+1 Afeto de Emília (Limite por período atingido)", "#88ccff")
    else:
        $ th_sfx("click")
        $ status_emilia.gastar_paciencia(1)
        $ anim_toque_emilia = atl_poke_recuo
        $ expressao_emilia = "emilia com vergonha arrumando o oculos e olhando para o lado e fofa"
        show expression expressao_emilia at sprite_padrao, atl_poke_recuo with dissolve
        emilia "Cuidado com a armação, Victor. Se entortar as hastes, fico meia hora calibrando as lentes diante dos manuscritos..."

    if status_emilia.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_emilia = "emilia com vergonha segurando a cruz"
        emilia "Victor, dê um passo para trás. Não consigo me concentrar com você me sondando dessa forma. Conversaremos em outro momento."
        jump menu_encontro_emilia

    call screen interacao_toque_emilia
    jump menu_encontro_emilia

label tocou_crucifixo_emilia:
    $ th_sfx("click")
    $ status_emilia.gastar_paciencia(2)
    $ anim_toque_emilia = atl_poke_recuo
    $ th_bark("emilia", "irritada")
    with hpunch
    $ hp_jogador = max(1, hp_jogador - 5)
    $ duvida_emilia += 1
    $ humor_emilia = "preocupada"
    $ expressao_emilia = "emilia com vergonha segurando a cruz"
    show expression expressao_emilia at sprite_padrao, atl_poke_recuo with dissolve
    "Ao roçar os dedos no crucifixo de prata benta no colarinho dela, meu sangue de Ghoul reage com uma queimadura aguda! (-5 HP)"
    emilia "Victor?! Você queimou os dedos só de encostar na minha prata consagrada... Por que a sua pele reagiu assim?"

    if status_emilia.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_emilia = "emilia com vergonha segurando a cruz"
        emilia "Isso é assustador demais... Eu preciso me afastar e rezar, Victor. Por favor, dê um passo para trás."
        jump menu_encontro_emilia

    call screen interacao_toque_emilia
    jump menu_encontro_emilia

label tocou_mao_emilia:
    $ th_sfx("splash")
    $ status_emilia.gastar_paciencia(1)
    $ anim_toque_emilia = atl_poke_suave
    $ th_bark("emilia", "toque_mao")
    if not tocou_heroina_periodo.get("emilia", False) and afeto_emilia >= 4:
        $ tocou_heroina_periodo["emilia"] = True
        $ afeto_emilia += 1
        $ humanidade = min(100, humanidade + 1)
        $ expressao_emilia = "emilia com vergonha segurando a cruz"
        show expression expressao_emilia at sprite_padrao, atl_poke_suave with dissolve
        emilia "S-Segurar as minhas mãos...? O terço está frio, Victor... mas os seus dedos são tão calorosos. Não me faça perder o foco da oração..."
        $ notificar_rpg("🙏 TOQUE NAS MÃOS", "+1 Afeto Emília | +1 Humanidade (Limite por período atingido)", "#88ccff")
    else:
        $ expressao_emilia = "emilia com vergonha segurando a cruz"
        show expression expressao_emilia at sprite_padrao, atl_poke_suave with dissolve
        emilia "Victor... cuidado ao segurar o rosário. Os elos de prata benzida marcam a pele se você puxar com pressa."

    if status_emilia.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_emilia = "emilia com vergonha segurando a cruz"
        emilia "Minhas mãos estão tremendo... Preciso ficar a sós com a minha oração por agora, Victor."
        jump menu_encontro_emilia

    call screen interacao_toque_emilia
    jump menu_encontro_emilia

# --- 9.3 ENCONTRO COM VALÉRIA ---

label menu_encontro_valeria:

    hide screen hud_exploracao_bs

    call verificar_reacao_olfativa("valeria") from _call_verificar_reacao_olfativa_2
    $ verificar_reacao_olfativa_heroina("valeria")

    call verificar_encontro_agendado("valeria", local_atual) from _call_verificar_encontro_agendado_2

    if status_valeria.bloqueada_hoje:

        $ th_bark("valeria", "irritada")

        show valeria deboche sonolenta meio corpo at sprite_padrao with dissolve

        valeria "Hoje não tem negócio nem conversa fiada, bolsista. Volta amanhã quando meu humor melhorar."

        jump entrar_local_exploracao_bs

    if exposicao >= 60 and not getattr(store, "reagiu_exposicao_valeria_visita", False):
        $ store.reagiu_exposicao_valeria_visita = True
        $ th_bark("valeria", "exposicao")
        show valeria meio corpo desconfiada at sprite_padrao with dissolve
        valeria "Ei, bolsista... você tá quente demais. Tem lanterna da ronda batendo no duto de ventilação lá em cima por sua causa."
        valeria "Se você trouxer lanterna de capitão pro meu ponto de contrabando, eu vou te cobrar o triplo por qualquer gota de sangue. Abaixa essa tua exposição antes que sobre pra mim."
        $ notificar_rpg("🚨 RISCO DE APREENSÃO", "Exposição Crítica (>=60%): Valéria desconfia do seu rastro (+1 Dúvida)!", "#ffaa00")
        $ status_valeria.duvida = min(10, status_valeria.duvida + 1)

    elif not saudou_heroina_visita:
        $ saudou_heroina_visita = True
        if fome_sangue <= 20:
            $ th_bark("valeria", "fome_critica")
        elif ruina_cain >= 50 and not getattr(store, "avisou_doom_valeria_hoje", False):
            $ store.avisou_doom_valeria_hoje = True
            $ th_bark("valeria", "doom")
        else:
            $ th_bark("valeria", "padrao")
        show valeria cinica pirulito meio corpo at sprite_padrao with dissolve

    else:

        show valeria cinica pirulito meio corpo at sprite_padrao

    # Eventos Orgânicos / Fome Crítica de Valéria
    if local_atual in ["caldeiras", "sala_caldeiras"] and fome_sangue < 30 and not getattr(store, "ev_fome_sem_plateia_valeria_visto", False):
        jump ev_c15_fome_sem_plateia_valeria

    if loc_mestra == local_atual and local_atual == "patio_arvore" and not getattr(store, "ev_negociacao_lility_valeria_visto", False):
        jump ev_negociacao_sombra_lility_valeria

    menu:
        "🧪 Vender as lascas de Pigmento de Alma coletadas da pintura viva" if getattr(store, "pigmento_alma_coletado", False) and not getattr(store, "vendeu_pigmento_valeria", False):
            jump negociar_pigmento_valeria

        "🌟 [[EVENTO DE MARCO DISPONÍVEL!]] Avançar Relação com Valéria" if verificar_marco_disponivel("valeria"):

            if estagio_valeria == 1:

                jump evento_marco_valeria_1

            else:

                jump evento_marco_valeria_2

        "🧪 [[SAFRA RARA]]: Negociar Sangue Direto da Fonte com Valéria" if not safra_rara_valeria and estagio_valeria >= 2:

            jump evento_valeria_safra_rara

        "📦 [[ENCOMENDA DAS CALDEIRAS]]: Entregar Lote de Manutenção (2x Sucata + 1x Sangue Adulterado)" if sucata_eletronica >= 2 and bolsa_sangue_adulterado >= 1:

            $ sucata_eletronica -= 2

            $ bolsa_sangue_adulterado -= 1

            $ dinheiro_jogador += 250

            $ dose_estimulante += 1

            $ divida_monitores = max(0, getattr(store, "divida_monitores", 0) - 400)

            $ afeto_valeria += 2

            $ status_valeria.afeto += 2

            show valeria cinica confiante meio corpo at sprite_padrao with dissolve

            valeria "Peças de cobre intactas e uma bolsa clandestina inteira... Você é eficiente, bolsista."

            valeria "Aqui seus duzentos e cinquenta contos, uma dose de estimulante do meu estoque e abati quatrocentos da sua dívida com os babacas do Grêmio."

            $ notificar_rpg("💰 ENCOMENDA ENTREGUE", "+$250 | +1 Dose Estimulante | -400 Dívida | +2 Afeto Valéria", "#00ffcc")

            jump menu_encontro_valeria

        "🎁 Entregar Presente Clandestino":

            call fluxo_entregar_presente_heroina("valeria") from _call_presente_valeria_enc

            jump menu_encontro_valeria

        "✋ Aproximar-se / Modo de Toque (Taxa de Ousadia)":
            if status_valeria.paciencia <= 0:
                $ th_sfx("click")
                $ th_bark("valeria", "padrao")
                valeria "Minha paciência comercial acabou por este turno, bolsista. Sem atendimento vip por agora."
                jump menu_encontro_valeria
            hide valeria
            $ expressao_valeria = "valeria cinica pirulito meio corpo"
            call screen interacao_toque_valeria
            jump menu_encontro_valeria

        "🩸 Comprar Safra Rara Direto da Fonte ($150 / Peçonha Elétrica)" if safra_rara_valeria and status_valeria.paciencia > 0:

            if dinheiro_jogador >= 150:

                $ dinheiro_jogador -= 150

                $ status_valeria.gastar_paciencia(1)

                show valeria provocante at sprite_padrao with dissolve

                valeria "Negócio fechado, sócio.{w=0.3} Puxa a grade dos fundos e não deixa marca no meu pescoço."

                "Quando minhas presas tocam sua artéria pulsante, a adrenalina, o café e a nicotina do sangue de Valéria explodem na minha língua."

                $ alimentar_de_heroina("valeria", qtd_sangue=50, ganho_vinculo=20, ganho_afeto=5)

                show valeria corada_transe at sprite_padrao with dissolve

                valeria "Nngh...{w=0.3} Caramba, Vane... essa mordida foi mais profunda que da última vez...{w=0.4} Você tá me deixando mole nas pernas..."

            else:

                show valeria deboche sonolenta meio corpo at risada_deboche

                valeria "Sem dinheiro na mão, sem safra no balcão, Victor.{w=0.3} Minha artéria não aceita 'fiado'.{w=0.4} Volta quando a sua carteira fizer barulho."

                "Minha garganta arde...{w=0.3} Ter que engolir o deboche comercial dela de estômago vazio é uma humilhação necessária."

                jump menu_encontro_valeria

        "📜 Deixar Bilhete Clandestino (Agendar Encontro Noturno nas Caldeiras)" if safra_rara_valeria and encontro_agendado_heroina is None and periodo != "Noite":

            $ agendar_encontro_clandestino("valeria", "caldeiras", "Noite")

            show valeria cinica confiante meio corpo at sprite_padrao with dissolve

            valeria "Encontro noturno marcado no meu território? Se você não faltar, eu reservo a melhor torneira das caldeiras pra você, sócio."

            jump menu_encontro_valeria

        "🛒 Negociar no Mercado Negro (Comprar Produtos)":
            jump acao_mercado_negro_valeria

        "💬 Conversar com Valéria (Paciência: [status_valeria.paciencia]/[status_valeria.paciencia_max])" if status_valeria.paciencia > 0 and not getattr(store, "conversou_heroina_periodo", {}).get("valeria", False):
            $ conversou_heroina_periodo["valeria"] = True
            $ status_valeria.gastar_paciencia(1)

            menu:

                "\"Como você consegue operar o Mercado Negro debaixo do nariz do Grêmio?\"":

                    $ intelecto += 1

                    $ reagir_escolha("valeria", "astucia")

                    show valeria cinica confiante meio corpo at sprite_padrao with dissolve

                    valeria "Regra número um dos negócios, sócio:{w=0.3} até os santos precisam de quem tire o lixo da capela."

                    show valeria leve sorriso pirulito meio corpo at sprite_padrao with dissolve

                    valeria "A Presidente finge que não me vê, e eu garanto que os vampiros desesperados comprem daqui em vez de morderem os monitores nos corredores.{w=0.4} Todo mundo ganha."

                "\"As caldeiras não sufocam você? Esse lugar parece um forno.\" ":

                    $ coragem += 1

                    $ reagir_escolha("valeria", "lucro")

                    show valeria casaco verde sorriso meio corpo at sprite_padrao with dissolve

                    valeria "O calor espanta os frouxos e o barulho dos pistões abafa qualquer conversa que não deva vazar."

                    show valeria cinica pirulito meio corpo at sprite_padrao with dissolve

                    valeria "Prefiro o cheiro de ferrugem e vapor do que a hipocrisia engomada dos andares de cima.{w=0.3} Aqui embaixo o jogo é limpo: pagou, levou."

                "\"Esse pirulito na boca é para disfarçar o cheiro de fumaça ou o medo dos monstros?\"":

                    $ charme += 1

                    $ reagir_escolha("valeria", "sarcasmo")

                    show valeria deboche sonolenta meio corpo at risada_deboche

                    valeria "Heh.{w=0.3} Medo de monstro? Bolsista, eu já fechei contrato com criaturas que fariam você molhar o uniforme."

                    show valeria sorriso provocante pirulito meio corpo at sprite_padrao with dissolve

                    valeria "O pirulito é só charme da gerência.{w=0.4} E garanto que o sabor é bem melhor do que as besteiras que você fala."

                    jump menu_encontro_valeria

        "💬 Já conversou com Valéria neste período" if getattr(store, "conversou_heroina_periodo", {}).get("valeria", False):
            show valeria cinica pirulito meio corpo at sprite_padrao with dissolve
            $ th_bark("valeria", "padrao")
            valeria "Ei, tempo é dinheiro e saliva custa caro. Já trocamos as ideias deste turno. Volta depois se quiser comprar algo ou tiver mercadoria nova."
            jump menu_encontro_valeria

        "⚖️ Negociar Termos Duros (Duelo Social de Intelecto / Comissão)" if status_valeria.paciencia > 0:

            $ alav_usar = status_valeria.alavancagens[0] if status_valeria.alavancagens else None

            $ sucesso, motivo = tentar_acao_social(status_valeria, dificuldade=40, atributo_usado="intelecto", valor_atributo=intelecto, alavancagem_usada=alav_usar)

            if sucesso:

                show valeria cinica confiante meio corpo at sprite_padrao with dissolve

                $ bonus_extorsao = 30 if "presenca_opressora" in perks_desbloqueados else 0

                $ total_comissao = 50 + bonus_extorsao

                $ dinheiro_jogador += total_comissao

                valeria "Arg! Tá bom, você é mais esperto do que aparenta. Fica com essa comissão e não espalha meus custos operacionais. (+[total_comissao] moedas)"

                $ notificar_rpg("💰 NEGOCIAÇÃO LUCRATIVA", f"+${total_comissao} obtidos com Valéria!", "#66ff66")

            else:

                show valeria deboche sonolenta meio corpo at sprite_padrao with dissolve

                valeria "Tentar passar a perna na contrabandista que comanda as caldeiras? Você tem coragem, mas não tem cérebro, sócio."

                jump menu_encontro_valeria

        "👣 Continuar Investigando a Área":
            $ th_bark("valeria", "despedida")
            hide valeria with dissolve
            $ saudou_heroina_visita = False
            $ emilia_curativo_feito_visita = False
            $ reagiu_exposicao_valeria_visita = False
            jump entrar_local_exploracao_bs

label tocou_cabeca_valeria:
    $ th_sfx("click")
    $ status_valeria.gastar_paciencia(1)
    $ anim_toque_valeria = atl_poke_recuo
    $ th_bark("valeria", "toque_cabelo")
    $ expressao_valeria = "valeria meio corpo mal humorada"
    show expression expressao_valeria at sprite_padrao, atl_poke_recuo with dissolve
    valeria "Ei, ei, sem bagunçar o penteado, bolsista. Não sou gato de rua pra ganhar cafuné de graça."

    if status_valeria.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_valeria = "valeria meio corpo entediada cansada"
        valeria "Chega de enrolação, bolsista. Minha paciência com você acabou por este turno. Vai produzir algo útil."
        jump menu_encontro_valeria

    call screen interacao_toque_valeria
    jump menu_encontro_valeria

label tocou_corpo_valeria:
    $ th_bark("valeria", "toque_taxa")
    $ toques_valeria += 1
    if toques_valeria == 1:
        $ th_sfx("click")
        $ status_valeria.gastar_paciencia(1)
        $ anim_toque_valeria = atl_poke_suave
        $ expressao_valeria = "valeria cobrando toque"
        show expression expressao_valeria at sprite_padrao, atl_poke_suave with dissolve
        valeria "Olhar a vitrine é de graça, lacaio. Mas encostar na mercadoria tem taxa de conveniência: se a mão escorregar de novo, cobro cinquentinha por toque."
    elif dinheiro_jogador >= 50:
        $ th_sfx("splash")
        $ th_sfx("caixa_registradora")
        $ status_valeria.gastar_paciencia(1)
        $ anim_toque_valeria = atl_poke_bounce
        $ dinheiro_jogador -= 50
        $ dominio_jogador += 1
        if not tocou_heroina_periodo.get("valeria", False):
            $ tocou_heroina_periodo["valeria"] = True
            $ afeto_valeria += 1
            $ humor_valeria = "lucrativa"
            $ expressao_valeria = "valeria meio corpo sorriso de pura felicidade"
            show expression expressao_valeria at sprite_padrao, atl_poke_bounce with dissolve
            valeria "Cinquenta na conta! Gosto de clientes que sabem o que querem e pagam à vista. (-$50 / +1 Domínio / +1 Afeto)"
            $ notificar_rpg("💰 TAXA DE CONVENIÊNCIA", "-$50 | +1 Afeto Valéria (Limite por período atingido)", "#66ff88")
        else:
            $ humor_valeria = "lucrativa"
            $ expressao_valeria = "valeria meio corpo sorriso de pura felicidade"
            show expression expressao_valeria at sprite_padrao, atl_poke_bounce with dissolve
            valeria "Mais cinquentinha no cofre? Valeu pela gorjeta, parceiro, mas já atingiu a cota de atrevimento por hoje."
            $ notificar_rpg("💰 TAXA PAGA", "-$50 | +1 Domínio (Afeto inalterado neste turno)", "#66ff88")
    else:
        $ th_sfx("click")
        $ status_valeria.gastar_paciencia(1)
        $ anim_toque_valeria = atl_poke_recuo
        with hpunch
        $ hp_jogador = max(1, hp_jogador - 10)
        $ expressao_valeria = "valeria meio corpo desprezando"
        show expression expressao_valeria at sprite_padrao, atl_poke_recuo with dissolve
        valeria "Opa! Sem fundos, sem mãos bobas, garoto. Aqui no subsolo ninguém leva nada no fiado! (-10 HP)"

    if status_valeria.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_valeria = "valeria meio corpo entediada cansada"
        valeria "Tempo esgotado, garoto! Mesmo com grana na mão, minha cota de paciência pro seu atrevimento fechou a conta por este turno."
        jump menu_encontro_valeria

    call screen interacao_toque_valeria
    jump menu_encontro_valeria

label tocou_bolso_valeria:
    $ th_sfx("click")
    $ status_valeria.gastar_paciencia(2)
    $ anim_toque_valeria = atl_poke_recuo
    $ th_bark("valeria", "toque_choque")
    with hpunch
    $ hp_jogador = max(1, hp_jogador - 10)
    $ expressao_valeria = "valeria afastando e ativando armadilha"
    show expression expressao_valeria at sprite_padrao, atl_poke_recuo with dissolve
    "Uma ratoeira alquímica na mochila de poções dispara uma faísca nos seus dedos! (-10 HP)"
    valeria "Hahaha! Achou mesmo que ia bater a carteira da maior contrabandista desta academia?"

    if status_valeria.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_valeria = "valeria meio corpo entediada cansada"
        valeria "Mão leve comigo não se cria! Acabou a palhaçada por hoje, volta pro seu canto antes que eu te cobre taxa de risco."
        jump menu_encontro_valeria

    call screen interacao_toque_valeria
    jump menu_encontro_valeria

# --- 9.4 ENCONTRO COM ELARA ---

label menu_encontro_elara:

    hide screen hud_exploracao_bs

    call verificar_reacao_olfativa("elara") from _call_verificar_reacao_olfativa_3
    $ verificar_reacao_olfativa_heroina("elara")

    call verificar_encontro_agendado("elara", local_atual) from _call_verificar_encontro_agendado_3

    if status_elara.bloqueada_hoje:

        $ th_bark("elara", "irritada")

        show elara irritada e com desprezo at sprite_padrao with dissolve

        elara "Retire-se da sala do Grêmio, lacaio. Sua presença ofensiva encerrou qualquer tolerância oficial por hoje."

        jump entrar_local_exploracao_bs

    if exposicao >= 60 and not getattr(store, "reagiu_exposicao_elara_visita", False):
        $ store.reagiu_exposicao_elara_visita = True
        $ th_bark("elara", "exposicao")
        show elara irritada e com desprezo at sprite_padrao with dissolve
        elara "Bolsista Vane. O nível de exposição das suas atividades noturnas ultrapassou qualquer limite aceitável."
        elara "A ronda policial da avenida e os inspetores do conselho já cruzaram com a sua descrição duas vezes. A disciplina desta academia não tolerará um lacaio descuidado. Apague seus rastros imediatamente, ou meu próximo despacho será sua ordem de expurgo."
        $ notificar_rpg("⚖️ ADVERTÊNCIA DISCIPLINAR", "Exposição Crítica (>=60%): Elara impõe repressão formal (+1 Dúvida)!", "#ff4444")
        $ status_elara.duvida = min(10, status_elara.duvida + 1)

    elif not saudou_heroina_visita:
        $ saudou_heroina_visita = True
        if fome_sangue <= 20:
            $ th_bark("elara", "fome_critica")
        elif ruina_cain >= 50 and not getattr(store, "avisou_doom_elara_hoje", False):
            $ store.avisou_doom_elara_hoje = True
            $ th_bark("elara", "doom")
        else:
            $ th_bark("elara", "padrao")
        show elara uniforme arrogante meio corpo at sprite_padrao with dissolve

    else:

        show elara uniforme arrogante meio corpo at sprite_padrao

    # Eventos Orgânicos / DOOM da Presidente Elara
    if local_atual == "salao_gremio" and (ruina_cain >= 25 or exposicao >= 20 or getattr(status_elara, "duvida", 0) >= 20) and not getattr(store, "ev_relatorio_odores_elara_visto", False):
        jump ev_c12_relatorio_odores_elara

    menu:
        "🌟 [[EVENTO DE MARCO DISPONÍVEL!]] Avançar Relação com Elara" if verificar_marco_disponivel("elara"):

            if estagio_elara == 1:

                jump evento_marco_elara_1

            else:

                jump evento_marco_elara_2

        "⚖️ [[AUDITORIA DO GRÊMIO]]: Prestar Contas e Selar Fissura Rúnica (-1 Giz de Proteção)" if giz_protecao >= 1 and exposicao > 15:

            $ giz_protecao -= 1

            $ exposicao = max(0, exposicao - 25)

            $ salvo_conduto_noturno = True

            $ afeto_elara += 2

            $ status_elara.afeto += 2

            show elara uniforme observando meio corpo at sprite_padrao with dissolve

            elara "Eficiente, Sr. Vane. O relatório dos monitores aponta que o umbral das catacumbas foi selado pelo seu traço de giz."

            elara "Engavetei dois autos de infração que citavam o seu nome e emiti um salvo-conduto noturno provisório. Mantenha a discrição."

            $ notificar_rpg("📜 SALVO-CONDUTO CONCEDIDO", "-25%% Exposição | Salvo-Conduto Ativo | +2 Afeto Elara", "#00ffcc")

            jump menu_encontro_elara

        "🎁 Entregar Presente Clandestino":

            call fluxo_entregar_presente_heroina("elara") from _call_presente_elara_enc

            jump menu_encontro_elara

        "✋ Aproximar-se / Modo de Toque (Click & Reação)":
            if status_elara.paciencia <= 0:
                $ th_sfx("click")
                $ th_bark("elara", "irritada")
                elara "Não se aproxime mais, Sr. Vane. Minha paciência com a sua presença esgotou-se por este período."
                jump menu_encontro_elara
            hide elara
            $ expressao_elara = "elara uniforme arrogante meio corpo"
            call screen interacao_toque_elara
            jump menu_encontro_elara

        "🩸 Provar do Sangue da Nobreza (A Presidente Subjugada)" if elara_subjugada_no_cofre and status_elara.paciencia > 0:

            $ status_elara.gastar_paciencia(1)

            show elara sorriso_cinico at sprite_padrao with dissolve

            elara "Aproxime-se sem pressa, Victor. Dois dedos abaixo da clavícula, como combinamos. Tranque a porta do Grêmio."

            "O sangue de Elara desce quente e aristocrático, como um vinho encorpado que clareia meus sentidos de predador."

            $ alimentar_de_heroina("elara", qtd_sangue=45, ganho_vinculo=15, ganho_afeto=5)

            show elara bochechas rosadas at sprite_padrao with dissolve

            elara "Sua conduta foi... satisfatória. Mas não se acostume a banquetear na mesa do Conselho Estudantil sem apresentar resultados."

            jump menu_encontro_elara

        "📜 Deixar Bilhete Clandestino (Agendar Reunião Secreta Noturna no Grêmio)" if elara_subjugada_no_cofre and encontro_agendado_heroina is None and periodo != "Noite":

            $ agendar_encontro_clandestino("elara", "salao_gremio", "Noite")

            show elara uniforme observando meio corpo at sprite_padrao with dissolve

            elara "Um bilhete de audiência noturna fora do expediente? Muito bem, Sr. Vane. Se você não se atrasar, estarei à sua espera para tratar de assuntos confidenciais."

            jump menu_encontro_elara

        "💬 Conversar com Elara (Paciência: [status_elara.paciencia]/[status_elara.paciencia_max])" if status_elara.paciencia > 0 and not getattr(store, "conversou_heroina_periodo", {}).get("elara", False):
            $ conversou_heroina_periodo["elara"] = True
            $ status_elara.gastar_paciencia(1)

            menu:

                "\"A segurança da academia continua sob o seu controle absoluto?\"":

                    $ coragem += 1

                    $ reagir_escolha("elara", "disciplina")

                    show elara uniforme observando meio corpo at sprite_padrao with dissolve

                    elara "A ordem só existe porque eu a mantenho com punho de ferro, Sr. Vane.{w=0.3} Um único milímetro de hesitação e as catacumbas engoliriam este campus antes do meio-dia."

                "\"Manter a 'Máscara' intacta deve custar mais do que você admite.\"":

                    $ intelecto += 1

                    $ reagir_escolha("elara", "intelecto")

                    show elara uniforme serena meio corpo at sprite_padrao with dissolve

                    elara "Pelo menos você tem olhos na cara.{w=0.3} Proteger o rebanho da verdade é a parte mais exaustiva da liderança."

                    elara "Eles dormem tranquilos achando que os desaparecimentos são boatos...{w=0.4} e é exatamente assim que deve continuar."

                "\"A Presidência não oferece nem um cafezinho para os servos da casa?\"":

                    $ charme += 1

                    $ reagir_escolha("elara", "sarcasmo")

                    show elara encarando com arrogancia e desprezo at sprite_padrao with dissolve

                    elara "Isto aqui é o centro de comando do Conselho Estudantil, Sr. Vane, não uma cafeteria de conveniência.{w=0.4} Aprenda o seu lugar antes que eu decida apertar o seu Grilhão."

                    jump menu_encontro_elara

        "💬 Já conversou com Elara neste período" if getattr(store, "conversou_heroina_periodo", {}).get("elara", False):
            show elara uniforme arrogante meio corpo at sprite_padrao with dissolve
            $ th_bark("elara", "autoridade")
            elara "Mantenha a compostura e retorne às suas obrigações, bolsista. O Conselho não tolera conversas ociosas repetidas durante a mesma ronda de inspeção."
            jump menu_encontro_elara

        "📑 Entregar Relatório Formal de Segurança da Academia (Receber Pagamento)" if not getattr(store, "relatorio_entregue_hoje", False):

            $ valor_pago = 240 if clima_diario_id == "inspecao_gremio" else 120
            if paciente_inadimplente_taxa():
                $ valor_pago = int(round(valor_pago * 0.80))

            $ dinheiro_jogador += valor_pago

            $ exposicao = max(0, exposicao - 15)

            $ relatorio_gremio_obtido = True
            $ relatorio_entregue_hoje = True

            if clima_diario_id == "inspecao_gremio":

                show elara uniforme serena meio corpo at sprite_padrao with dissolve

                elara "Com o bloqueio do Conselho ativo hoje, seus relatórios de inteligência são inestimáveis, Sr. Vane. Tome o pagamento em dobro."

                $ notificar_rpg("💰 PAGAMENTO EM DOBRO", f"+${valor_pago} pagos pelo Conselho Estudantil! (-15%% Exposição)", "#00ffcc")

            else:

                show elara uniforme observando meio corpo at sprite_padrao with dissolve

                if paciente_inadimplente_taxa():
                    elara "Relatório minucioso, Sr. Vane. O Conselho reteve vinte por cento da verba devido à sua pendência na tesouraria."
                else:
                    elara "Relatório minucioso, Sr. Vane. Aqui está a sua verba oficial de manutenção."

                $ notificar_rpg("💰 RECOMPENSA DO GRÊMIO", f"+${valor_pago} recebidos pelo relatório! (-15%% Exposição)", "#66ff66")

                jump menu_encontro_elara

        "⚖️ Prestar Contas / Inspeção de Conduta (-15%% Exposição)" if not getattr(store, "inspecao_elara_hoje", False):

            $ inspecao_elara_hoje = True
            $ exposicao = max(0, exposicao - 15)

            if drenou_membro_gremio:

                show elara irritada e com desprezo at sprite_padrao with dissolve

                elara "Sinto o cheiro do sangue dos meus executores em você, Victor. Sugar a própria espécie como um parasita faminto é repulsivo."

                $ reagir_escolha("elara", "disciplina")

            else:

                show elara uniforme observando meio corpo at sprite_padrao with dissolve
                $ th_voz("climax/elara_aviso_expedicao")
                elara "Sua presença no toque de recolher foi registrada, Victor. Mantenha as presas guardadas e talvez o Conselho não exija a sua execução. (-15%% Exposição)"
                $ reagir_escolha("elara", "intelecto")

                jump menu_encontro_elara

        "⚖️ Enfrentar Interrogatório com Intelecto e Postura (Duelo Social)" if status_elara.paciencia > 0:

            $ alav_usar = status_elara.alavancagens[0] if status_elara.alavancagens else None

            $ sucesso, motivo = tentar_acao_social(status_elara, dificuldade=50, atributo_usado="intelecto", valor_atributo=intelecto, alavancagem_usada=alav_usar)

            if sucesso:

                show elara uniforme observando meio corpo at sprite_padrao with dissolve

                elara "Impressionante como você mantém a frieza sob a autoridade do Conselho. Talvez você não seja apenas um lacaio descartável afinal..."

                $ exposicao = max(0, exposicao - 20)

                $ status_elara.duvida = max(0, status_elara.duvida - 1)

                $ notificar_rpg("🕊️ SUSPEITAS DISSIPADAS", "Elara reduziu a vigilância sobre você (-20%% Exposição / -1 Dúvida)!", "#ffffff")

            else:

                show elara encarando com arrogancia e desprezo at sprite_padrao with dissolve

                elara "Suas justificativas são inconsistentes, Sr. Vane. Seus passos serão vigiados de perto a partir de agora."

                $ exposicao = min(100, exposicao + 15)

                $ notificar_rpg("⚠️ VIGILÂNCIA REFORÇADA", "+15%% Exposição na Máscara!", "#ff3333")

                jump menu_encontro_elara

        "👣 Continuar Investigando a Área":
            $ th_bark("elara", "despedida")
            hide elara with dissolve
            $ saudou_heroina_visita = False
            $ emilia_curativo_feito_visita = False
            $ reagiu_exposicao_elara_visita = False
            jump entrar_local_exploracao_bs

label tocou_rosto_elara:
    if not elara_subjugada_no_cofre:
        $ th_sfx("click")
        $ status_elara.gastar_paciencia(1)
        $ anim_toque_elara = atl_poke_recuo
        $ th_bark("elara", "irritada")
        $ expressao_elara = "elara ativando grilhao de sangue e encarando"
        show expression expressao_elara at sprite_padrao, atl_poke_recuo with dissolve
        elara "Você tem ideia da distância hierárquica entre os seus dedos sujos e o rosto da Presidente do Conselho, Sr. Vane?"
    else:
        $ th_sfx("splash")
        $ status_elara.gastar_paciencia(1)
        $ anim_toque_elara = atl_poke_suave
        $ th_bark("elara", "toque_corada")
        $ expressao_elara = "elara meio corpo com vergonha olhando pro lado"
        show expression expressao_elara at sprite_padrao, atl_poke_suave with dissolve
        if not tocou_heroina_periodo.get("elara", False):
            $ tocou_heroina_periodo["elara"] = True
            $ afeto_elara += 1
            $ notificar_rpg("✋ TOQUE OUSADO", "+1 Afeto Elara (Limite por período atingido)", "#ffffff")
        elara "N-não toque no meu rosto com tanta familiaridade na frente dos quadros do Conselho..."

    if status_elara.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_elara = "elara ativando grilhao de sangue e encarando"
        elara "Basta! Minha tolerância para esta quebra de protocolo chegou ao limite neste período. Afaste-se."
        jump menu_encontro_elara

    call screen interacao_toque_elara
    jump menu_encontro_elara

label tocou_elara_reacao:
    if not elara_subjugada_no_cofre:
        $ toques_elara += 1
        if toques_elara == 1:
            $ th_sfx("click")
            $ th_bark("elara", "toque_bracadeira")
            $ status_elara.gastar_paciencia(1)
            $ anim_toque_elara = atl_poke_recuo
            $ expressao_elara = "elara ativando grilhao de sangue e encarando"
            show expression expressao_elara at sprite_padrao, atl_poke_recuo with dissolve
            elara "Recolha a sua mão imediatamente, lacaio. Quem lhe deu a ilusão de que tem permissão para encostar no meu uniforme branco?"
        else:
            $ th_sfx("click")
            $ status_elara.gastar_paciencia(2)
            $ anim_toque_elara = atl_poke_recuo
            with vpunch
            $ hp_jogador = max(1, hp_jogador - 25)
            $ punicoes_gremio_ativas += 1
            $ expressao_elara = "elara ativando grilhao de sangue"
            show expression expressao_elara at sprite_padrao, atl_poke_recuo with dissolve
            "Com um estalar de dedos enluvados, o Grilhão de Sangue queima no seu peito! (-25 HP)"
            $ expressao_elara = "elara apos ativar grilhao do sangue"
            show expression expressao_elara at sprite_padrao with dissolve
            elara "Já que a sua criadora não lhe ensinou etiqueta, a dor ensinará."
    else:
        $ th_sfx("splash")
        $ th_bark("elara", "toque_submissa")
        $ status_elara.gastar_paciencia(1)
        $ anim_toque_elara = atl_poke_bounce
        $ dominio_jogador += 1
        if not tocou_heroina_periodo.get("elara", False):
            $ tocou_heroina_periodo["elara"] = True
            $ afeto_elara += 1
            $ notificar_rpg("👑 SUBMISSÃO TÁTICA", "+1 Afeto Elara (Limite por período atingido)", "#ffffff")
        $ expressao_elara = "elara envergonhada afastado"
        show expression expressao_elara at sprite_padrao, atl_poke_bounce with dissolve
        elara "Não me toque assim aqui dentro... Se os membros do Grêmio entrarem e virem isso... ahn..."

    if status_elara.paciencia <= 0:
        $ th_sfx("click")
        $ expressao_elara = "elara ativando grilhao de sangue e encarando"
        elara "Chega, Sr. Vane. Se continuar com essa postura, serei obrigada a registrar uma ocorrência formal. O expediente de audiência está encerrado por agora."
        jump menu_encontro_elara

    call screen interacao_toque_elara
    jump menu_encontro_elara

# ==============================================================================

# 10. CONTROLADOR DO RELÓGIO DE 21 DIAS E RETORNO À HISTÓRIA PRINCIPAL

# ==============================================================================

label avancar_turno_mapa:

    hide screen hud_exploracao_bs

    hide screen mapa_tatico_escola

    # Degradação passiva da Saciedade acelerada pela Ruína de Cain

    if ruina_cain >= 75:

        $ fome_sangue = max(0, fome_sangue - 14)

    elif ruina_cain >= 50:

        $ fome_sangue = max(0, fome_sangue - 10)

    elif ruina_cain >= 25:

        $ fome_sangue = max(0, fome_sangue - 8)

    else:

        $ fome_sangue = max(0, fome_sangue - 5)   # Ritmo calmo e tolerante na Fase 1 (Sussurro Adormecido)

    # Avanço dinâmico da Ruína de Cain (DOOM Clock estilo World of Horror)

    $ cain_despertou = GerenciadorRuina.avancar_ruina_periodo()

    if cain_despertou or ruina_cain >= 100:

        $ ruina_cain = 100
        play sound "audio/sfx/sfx_explosao_caldeira_impacto.ogg"
        with vpunch
        "O chão de pedra estremece... O Progenitor está abrindo os olhos sob as fundações."
        "A terra treme violentamente sob as fundações da academia! O ar fica espesso e gélido..."

        "As rachaduras no solo sangram luz carmesim. A entidade adormecida nas profundezas despertou!"

        jump evt_d21_noite

    # O ciclo atmosférico de períodos continua normalmente

    $ alimentou_lility_periodo = False
    $ transe_lility_periodo = False
    $ emilia_curou_gaze_periodo = False
    $ tomou_cha_emilia_periodo = False
    $ conversou_heroina_periodo = {}
    $ tocou_heroina_periodo = {}
    $ rumores_heroina_periodo = {}
    $ reagiu_exposicao_lility_visita = False
    $ reagiu_exposicao_emilia_visita = False
    $ reagiu_exposicao_elara_visita = False
    $ reagiu_exposicao_valeria_visita = False
    $ area_alerta_emboscada = False
    $ reacao_olfativa_banquete_periodo = {}
    $ hipnotizou_mob_periodo = False
    $ odor_mascarado_turnos = max(0, getattr(store, "odor_mascarado_turnos", 0) - 1)
    if getattr(store, "buff_ataque_elixir_turnos", 0) > 0:
        $ store.buff_ataque_elixir_turnos -= 1
        if store.buff_ataque_elixir_turnos == 0:
            $ store.buff_ataque_elixir = 0
    # A virada de dia acontece quando o período que acaba de encerrar era "Noite" (Noite -> Manhã do dia seguinte)
    $ for _h in [status_lility, status_elara, status_emilia, status_valeria]: _h.recuperar_turno(novo_dia=(periodo == "Noite"))

    # Decaimento da Sequela de Anemia Recente
    if getattr(store, "turnos_anemia_recente", 0) > 0:
        $ turnos_anemia_recente -= 1
        if turnos_anemia_recente == 0:
            $ curar_sequela("anemia_recente")
            $ notificar_rpg("🩸 MEDULA RECUPERADA", "O organismo repôs o volume de sangue: Anemia neutralizada.", "#00ffcc")

    # Gerenciamento de Obrigações Acadêmicas & Fachada Escolar
    if getattr(store, "tarefa_academica_pendente", False):
        $ prazo_tarefa_periodos = max(0, getattr(store, "prazo_tarefa_periodos", 1) - 1)
        if prazo_tarefa_periodos == 0:
            $ tarefa_academica_pendente = False
            $ faltas_academicas = getattr(store, "faltas_academicas", 0) + 1
            if faltas_academicas == 1:
                $ exposicao = min(100, exposicao + 15)
                $ notificar_rpg("⚠️ ADVERTÊNCIA ESCOLAR", "Você não entregou a tarefa a tempo! O Conselho afixou seu nome no Mural (+15% Exposição).", "#ffaa00")
            elif faltas_academicas == 2:
                $ _multa_acad = min(dinheiro_jogador, 50)
                $ dinheiro_jogador -= _multa_acad
                $ notificar_rpg("📉 RETENÇÃO DE BOLSA", f"Reincidência acadêmica! O Grêmio reteve -${_multa_acad} dos seus fundos escolares.", "#ff5555")
            else:
                $ exposicao = min(100, exposicao + 20)
                $ aplicar_sequela("intimacao_disciplinar", "Intimação Disciplinar", "O Conselho Estudantil abriu inquérito sobre sua conduta.", "-1 Passo até prestar esclarecimentos")
                $ notificar_rpg("🚨 CONVOCAÇÃO DISCIPLINAR", "Inadimplência grave! A Presidente Elara emitiu uma intimação formal para seu comparecimento.", "#ff2244")
    else:
        $ ciclo_academico_contador = getattr(store, "ciclo_academico_contador", 0) + 1
        if ciclo_academico_contador >= 4 and dia_atual >= 2:
            $ ciclo_academico_contador = 0
            $ sortear_nova_tarefa_academica()
            $ notificar_rpg("📚 NOVA OBRIGAÇÃO ACADÊMICA", f"{nome_tarefa_academica} (Prazo: {prazo_tarefa_periodos} períodos)", "#88ccff")

    $ _estava_em_sobrevivencia = (dia_atual >= 3)

    if periodo == "Manhã":

        $ periodo = "Tarde"

    elif periodo == "Tarde":

        $ periodo = "Noite"

    else:

        $ periodo = "Manhã"

        $ dia_atual += 1

        $ tentou_visitar_manha_hoje = False
        $ coleta_enfermeira_hoje = False
        $ drenou_enfermeira_hoje = False
        $ saudou_enfermeira_visita = False
        $ relatorio_entregue_hoje = False
        $ inspecao_elara_hoje = False
        $ enfermaria_bolsas_hoje = 0
        $ enfermaria_kits_hoje = 0
        $ usou_incenso_hoje = False
        $ usou_sais_hoje = False
        $ presenteou_heroina_hoje = {}
        $ avisou_doom_lility_hoje = False
        $ avisou_doom_elara_hoje = False
        $ avisou_doom_emilia_hoje = False
        $ avisou_doom_valeria_hoje = False
        $ cacadas_realizadas_hoje = 0
        $ encomenda_caldeiras_concluida_hoje = False
        $ sincronizar_estoque_diario_lojas()

        $ sortear_modificador_diario()

        $ sortear_abertura_mercado_negro()
        $ sortear_vitrine_mercado_negro()

        if dia_atual >= 3:
            $ processar_turno_simbro()

        if dia_atual % 3 == 0:

            $ pontos_talento_victor += 1

            $ notificar_rpg("🌟 PONTO DE TALENTO", f"+1 Ponto de Talento por sobreviver até o Dia {dia_atual}!", "#ffcc00")

    if _estava_em_sobrevivencia:
        $ periodos_ate_cobranca -= 1
        if periodos_ate_cobranca <= 0:
            $ cobranca_vencida_pendente = True
            $ periodos_ate_cobranca = 6
            $ notificar_rpg("📑 COBRANÇA EMITIDA", f"O Conselho exige ${calcular_valor_cobranca_academica()} neste turno.", "#ff8844")

    # Decaimento dos buffs temporários do Banquete Oculto

    $ processar_decaimento_buffs_turno()

    # Penalidade da Sequela Paranoia do Executor (se exposicao >= 75%)

    if exposicao >= 75:

        $ aplicar_sequela("paranoia_executor", "Paranoia do Executor", "O Grêmio apertou o cerco pelos corredores.", "-1 Passo de Exploração por turno")

        $ passos_restantes_periodo = 2
        $ limite_visitas_periodo = 2

    else:

        $ passos_restantes_periodo = 3
        $ limite_visitas_periodo = 3

        if "paranoia_executor" in [s["id"] for s in getattr(store, "sequelas_ativas", [])]:

            $ curar_sequela("paranoia_executor")

    $ visitas_restantes_periodo = limite_visitas_periodo
    $ locais_visitados_neste_periodo = []
    $ deslocando_pelo_mapa = False

    $ verificar_reatividade_fase_no_turno()

    # O calendário decide se este período tem cena de história ou mapa livre.

    jump slot_atual

# ==============================================================================

# 11. TELA DE GALERIA DE MEMÓRIAS E REPLAY DE EVENTOS

# ==============================================================================

screen galeria_memorias():

    tag menu

    modal True

    zorder 95

    add "images/wallpapers static/bg menu principal piano cidade lua sangue.webp" size (1920, 1080)

    add Solid("#08080ee6")

    frame:

        align (0.5, 0.5)

        xysize (1740, 940)

        background "#12131aee"

        padding (35, 30)

        vbox:

            spacing 20

            hbox:

                xfill True

                text "🎞️ GALERIA DE MEMÓRIAS & MARCOS ÍNTIMOS" size 32 bold True color "#ff4444"

                textbutton "✖ [[ VOLTAR ]]" action Return() xalign 1.0 text_size 24 text_color "#00ffcc"

            text "Desbloqueie eventos especiais atingindo os Marcos de Afeto e Horário com cada heroína ao longo dos seus dias de sobrevivência." size 18 color "#aaaaaa"

            # Grade 4x2 com os 8 Marcos Principais das Heroínas

            grid 4 2:

                spacing 25

                xalign 0.5

                # --- 1. LILITY MARCO 1 ---

                frame:

                    xysize (390, 360) background "#1e1218" padding (15, 15)

                    vbox:

                        spacing 8 xalign 0.5

                        text ("🩸 Lili — Marco I" if apelido_lili_desbloqueado else "🩸 Mestra — Marco I") size 20 bold True color "#ff6666" xalign 0.5

                        if persistent.mem_lility_1:

                            add "lility sedutora provocante corpo inteiro" xalign 0.5 ysize 190 fit "contain"

                            text "A Coleira de Veludo" size 16 color "#ffffff" xalign 0.5

                            textbutton "▶ Rever Memória" action Replay("evento_marco_lility_1", locked=False) xalign 0.5 text_size 18 text_color "#00ffcc"

                        else:

                            null height 60

                            text "🔒 BLOQUEADO" size 22 bold True color "#555555" xalign 0.5

                            text "Requisito: Afeto [nome_display_mestra] 3+\nVisitar Sala de Música à Noite" size 15 color "#888888" xalign 0.5 text_align 0.5

                # --- 2. LILITY MARCO 2 ---

                frame:

                    xysize (390, 360) background "#1e1218" padding (15, 15)

                    vbox:

                        spacing 8 xalign 0.5

                        text ("🩸 Lili — Marco II" if apelido_lili_desbloqueado else "🩸 Mestra — Marco II") size 20 bold True color "#ff6666" xalign 0.5

                        if persistent.mem_lility_2:

                            add "lility sorrindo com rosto rosado" xalign 0.5 ysize 190 fit "contain"

                            text "Sede Invertida no Piano" size 16 color "#ffffff" xalign 0.5

                            textbutton "▶ Rever Memória" action Replay("evento_marco_lility_2", locked=False) xalign 0.5 text_size 18 text_color "#00ffcc"

                        else:

                            null height 60

                            text "🔒 BLOQUEADO" size 22 bold True color "#555555" xalign 0.5

                            text "Requisito: Estágio 2 + Afeto 6+\nVisitar Sala de Música à Noite" size 15 color "#888888" xalign 0.5 text_align 0.5

                # --- 3. EMÍLIA MARCO 1 ---

                frame:

                    xysize (390, 360) background "#121c2c" padding (15, 15)

                    vbox:

                        spacing 8 xalign 0.5

                        text "✝️ Emília — Marco I" size 20 bold True color "#88ccff" xalign 0.5

                        if persistent.mem_emilia_1:

                            add "emilia com vergonha e fofa" xalign 0.5 ysize 190 fit "contain"

                            text "Cicatrizes Entre Estantes" size 16 color "#ffffff" xalign 0.5

                            textbutton "▶ Rever Memória" action Replay("evento_marco_emilia_1", locked=False) xalign 0.5 text_size 18 text_color "#00ffcc"

                        else:

                            null height 60

                            text "🔒 BLOQUEADO" size 22 bold True color "#555555" xalign 0.5

                            text "Requisito: Afeto Emília 3+\nEncontrar de Manhã ou Tarde" size 15 color "#888888" xalign 0.5 text_align 0.5

                # --- 4. EMÍLIA MARCO 2 ---

                frame:

                    xysize (390, 360) background "#121c2c" padding (15, 15)

                    vbox:

                        spacing 8 xalign 0.5

                        text "✝️ Emília — Marco II" size 20 bold True color "#88ccff" xalign 0.5

                        if persistent.mem_emilia_2:

                            add "emilia camisa aberta nsfw corada" xalign 0.5 ysize 190 fit "contain"

                            text "Calor Humano no Quarto" size 16 color "#ffffff" xalign 0.5

                            textbutton "▶ Rever Memória" action Replay("evento_marco_emilia_2", locked=False) xalign 0.5 text_size 18 text_color "#00ffcc"

                        else:

                            null height 60

                            text "🔒 BLOQUEADO" size 22 bold True color "#555555" xalign 0.5

                            text "Requisito: Estágio 2 + Afeto 6+\nQualquer horário" size 15 color "#888888" xalign 0.5 text_align 0.5

                # --- 5. VALÉRIA MARCO 1 ---

                frame:

                    xysize (390, 360) background "#122418" padding (15, 15)

                    vbox:

                        spacing 8 xalign 0.5

                        text "🧪 Valéria — Marco I" size 20 bold True color "#66ff66" xalign 0.5

                        if persistent.mem_valeria_1:

                            add "valeria perfil sorriso provocador meio corpo" xalign 0.5 ysize 190 fit "contain"

                            text "Contrato de Exclusividade" size 16 color "#ffffff" xalign 0.5

                            textbutton "▶ Rever Memória" action Replay("evento_marco_valeria_1", locked=False) xalign 0.5 text_size 18 text_color "#00ffcc"

                        else:

                            null height 60

                            text "🔒 BLOQUEADO" size 22 bold True color "#555555" xalign 0.5

                            text "Requisito: Afeto Valéria 2+\nVisitar Caldeiras ou Bar" size 15 color "#888888" xalign 0.5 text_align 0.5

                # --- 6. VALÉRIA MARCO 2 ---

                frame:

                    xysize (390, 360) background "#122418" padding (15, 15)

                    vbox:

                        spacing 8 xalign 0.5

                        text "🧪 Valéria — Marco II" size 20 bold True color "#66ff66" xalign 0.5

                        if persistent.mem_valeria_2:

                            add "valeria shorts cropped descolada corpo inteiro" xalign 0.5 ysize 190 fit "contain"

                            text "Dona do Submundo" size 16 color "#ffffff" xalign 0.5

                            textbutton "▶ Rever Memória" action Replay("evento_marco_valeria_2", locked=False) xalign 0.5 text_size 18 text_color "#00ffcc"

                        else:

                            null height 60

                            text "🔒 BLOQUEADO" size 22 bold True color "#555555" xalign 0.5

                            text "Requisito: Estágio 2 + Afeto 5+\nDomínio 2+" size 15 color "#888888" xalign 0.5 text_align 0.5

                # --- 7. ELARA MARCO 1 ---

                frame:

                    xysize (390, 360) background "#221a28" padding (15, 15)

                    vbox:

                        spacing 8 xalign 0.5

                        text "⚖️ Elara — Marco I" size 20 bold True color "#eebbff" xalign 0.5

                        if persistent.mem_elara_1:

                            add "elara encarando de forma astuta" xalign 0.5 ysize 190 fit "contain"

                            text "Inspeção a Portas Fechadas" size 16 color "#ffffff" xalign 0.5

                            textbutton "▶ Rever Memória" action Replay("evento_marco_elara_1", locked=False) xalign 0.5 text_size 18 text_color "#00ffcc"

                        else:

                            null height 60

                            text "🔒 BLOQUEADO" size 22 bold True color "#555555" xalign 0.5

                            text "Requisito: Afeto Elara 2+\nEncontrar no Gabinete" size 15 color "#888888" xalign 0.5 text_align 0.5

                # --- 8. ELARA MARCO 2 ---

                frame:

                    xysize (390, 360) background "#221a28" padding (15, 15)

                    vbox:

                        spacing 8 xalign 0.5

                        text "⚖️ Elara — Marco II" size 20 bold True color "#eebbff" xalign 0.5

                        if persistent.mem_elara_2:

                            add "elara com prazer" xalign 0.5 ysize 190 fit "contain"

                            text "A Coroa Subjugada" size 16 color "#ffffff" xalign 0.5

                            textbutton "▶ Rever Memória" action Replay("evento_marco_elara_2", locked=False) xalign 0.5 text_size 18 text_color "#00ffcc"

                        else:

                            null height 60

                            text "🔒 BLOQUEADO" size 22 bold True color "#555555" xalign 0.5

                            text "Requisito: Estágio 2 + Afeto 5+\n(Ou Subjugá-la no Cofre)" size 15 color "#888888" xalign 0.5 text_align 0.5

# ==============================================================================

# 12. LABELS DOS EVENTOS DE MARCO (MILESTONES ESTILO FEMBOY FUTA HOUSE)

# ==============================================================================

# --- LILITY MARCO 1: A COLEIRA DE VELUDO ---

label evento_marco_lility_1:
    $ local_atual = "sala_musica"
    call restaurar_fundo_local_atual

    if renpy.loadable("audio/musicas/the_crimson_chamber.mp3"):
        play music "audio/musicas/the_crimson_chamber.mp3" if_changed fadein 1.5
    elif renpy.loadable("audio/The_Crimson_Chamber.ogg"):
        play music "audio/The_Crimson_Chamber.ogg" if_changed fadein 1.5

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show lility sedutora provocante corpo inteiro at sprite_direita with dissolve

    "🌟 [[EVENTO DE MARCO I — MESTRA]]: Ela tranca a porta dupla da Sala de Música e se aproxima devagar, deslizando os dedos frios pelo meu colarinho."

    $ th_voz("climax/lility_marco_01_coleira")
    mestra "Você tem vindo me procurar mesmo quando sua sede não está no limite, Victor. Está começando a gostar da coleira... ou veio testar minha paciência?"

    menu:

        "Ajoelhar-se e deixar que ela conduza o Transe (+Submissão / +Saciedade Máxima / +Afeto)":

            $ fome_sangue = 100

            $ afeto_mestra += 2

            show lility sorrindo com olhos penetrantes at sprite_direita with dissolve

            mestra "Bom garoto. Quando você para de lutar contra o que somos, o gosto do meu sangue fica muito mais doce."

        "Segurar o pulso dela contra o piano e exigir beber de pé (+Domínio / +Coragem / +Afeto)":

            $ dominio_jogador += 2

            $ coragem += 1

            $ fome_sangue = min(100, fome_sangue + 50)

            $ afeto_mestra += 2

            show expression obter_sprite_victor("confiante") as victor at sprite_esquerda with dissolve

            show lility com vergonha olhando de lado at sprite_direita with vpunch

            mestra "O-ora, seu insolente...! Prendendo o pulso da sua própria criadora? Hmph... Beba logo antes que eu mude de ideia!"

    $ estagio_mestra = 2

    $ persistent.mem_lility_1 = True

    $ renpy.end_replay()

    $ apelido_lili_desbloqueado = True
    $ nome_display_mestra = "Lili"
    "🔓 [[MEMÓRIA DESBLOQUEADA NA GALERIA: 'A Coleira de Veludo' — O vínculo se aprofundou! A Mestra permitiu o apelido íntimo 'Lili' e avançou para o Estágio 2!]]"

    jump menu_encontro_lility

# --- LILITY MARCO 2: SEDE INVERTIDA NO PIANO ---

label evento_marco_lility_2:
    $ local_atual = "sala_musica"
    call restaurar_fundo_local_atual

    if renpy.loadable("audio/gothic_waltz.ogg"):

        if renpy.loadable("audio/musicas/tema_da_valsa.mp3"):
            play music "audio/musicas/tema_da_valsa.mp3" if_changed fadein 1.5
        else:
            play music "audio/gothic_waltz.ogg" if_changed fadein 1.5

    show expression obter_sprite_victor("pensando") as victor at sprite_esquerda with dissolve

    show lility vulneravel timida meio corpo at sprite_direita with dissolve

    "🌟 [[EVENTO DE MARCO II — LILI]]: Sobre o piano de cauda, a respiração de Lili falha. O isolamento do Grilhão finalmente cobra seu preço."

    $ th_voz("climax/lility_marco_02_piano")
    mestra "Victor... Não se afaste hoje. O silêncio desta sala está alto demais."

    menu:

        "Puxá-la para perto e oferecer seu próprio pescoço (+Domínio / +Ressonância / +Afeto)":

            with flash_red

            $ dominio_jogador += 2

            $ ressonancia_pre_diluviana += 2

            $ afeto_mestra += 3

            show lility sorrindo com rosto rosado at sprite_direita with dissolve

            mestra "Seu coração humano... é tão quente e barulhento... Fique exatamente assim até o amanhecer."

        "Abraçá-la em silêncio até ela adormecer (+Humanidade / +Afeto)":

            $ humanidade = min(100, humanidade + 5)

            $ afeto_mestra += 3

            show lility sorrindo feliz at sprite_direita with dissolve

            mestra "Você é um péssimo monstro, Victor Vane... e a única coisa neste século que não me dá tédio."

    $ estagio_mestra = 3

    $ persistent.mem_lility_2 = True

    $ renpy.end_replay()

    "🔓 [[MEMÓRIA DESBLOQUEADA NA GALERIA: 'Sede Invertida no Piano' — Lili atingiu o Estágio Máximo!]]"

    jump menu_encontro_lility

# --- EMÍLIA MARCO 1: CICATRIZES ENTRE ESTANTES ---

label evento_marco_emilia_1:
    $ local_atual = "biblioteca"
    call restaurar_fundo_local_atual

    if renpy.loadable("audio/musicas/the_keepers_ledger.mp3"):
        play music "audio/musicas/the_keepers_ledger.mp3" if_changed fadein 1.5
    elif renpy.loadable("audio/The_Unfinished_Lesson.ogg"):
        play music "audio/The_Unfinished_Lesson.ogg" if_changed fadein 1.5

    show expression obter_sprite_victor("padrao") as victor at sprite_esquerda with dissolve

    show emilia com vergonha arrumando o oculos e olhando para o lado e fofa at sprite_direita with dissolve

    "🌟 [[EVENTO DE MARCO I — EMÍLIA]]: No fundo restrito da biblioteca, Emília fecha o caderno de anotações quando me aproximo."

    $ th_voz("climax/emilia_marco_01_estantes")
    emilia "V-Victor... Percebi que sempre procuro você pelos corredores antes de começar minhas rondas. Isso é imprudente para uma exorcista..."

    menu:

        "Segurar a mão dela sobre a mesa: 'Você não precisa carregar tudo sozinha.' (+Humanidade / +Afeto)":

            $ humanidade = min(100, humanidade + 4)

            $ afeto_emilia += 2

            show emilia sorriso com vergonha de frente at sprite_direita with dissolve

            emilia "Quando você segura minha mão assim... até esqueço que estamos cercados por monstros."

        "Aproximar o rosto e provocá-la suavemente (+Charme / +Domínio)":

            $ charme += 1

            $ dominio_jogador += 1

            $ afeto_emilia += 2

            show expression obter_sprite_victor("charmoso") as victor at sprite_esquerda with dissolve

            show emilia com vergonha e fofa at sprite_direita with dissolve

            emilia "M-muito perto, Victor! Se alguém entrar na fileira de livros agora, o que vão pensar de nós?!"

    $ estagio_emilia = 2

    $ persistent.mem_emilia_1 = True

    $ renpy.end_replay()

    "🔓 [[MEMÓRIA DESBLOQUEADA NA GALERIA: 'Cicatrizes Entre Estantes' — Emília avançou para o Estágio 2!]]"

    jump menu_encontro_emilia

# --- EMÍLIA MARCO 2: CALOR HUMANO NO QUARTO ---

label evento_marco_emilia_2:
    $ local_atual = "dormitorio"
    call restaurar_fundo_local_atual

    if renpy.loadable("audio/musicas/the_keepers_ledger.mp3"):
        play music "audio/musicas/the_keepers_ledger.mp3" if_changed fadein 1.5
    elif renpy.loadable("audio/where_the_room_turns_blue.ogg"):
        play music "audio/where_the_room_turns_blue.ogg" if_changed fadein 1.5

    show expression obter_sprite_victor("padrao") as victor at sprite_esquerda with dissolve

    show emilia camisa aberta nsfw timida at sprite_direita with dissolve

    "🌟 [[EVENTO DE MARCO II — EMÍLIA]]: Após uma patrulha sob a chuva fria, Emília seca o sobretudo no meu dormitório, com a camisa entreaberta para tratar um arranhão no ombro."

    $ th_voz("climax/emilia_marco_02_quarto")
    emilia "Não olhe tanto, Victor... Só vim aqui porque o seu quarto é o único lugar desta academia onde consigo respirar em paz."

    menu:

        "Cuidar do ferimento dela com delicadeza e beijar seu ombro (+Humanidade / +Afeto)":

            $ humanidade = min(100, humanidade + 5)

            $ afeto_emilia += 3

            show expression obter_sprite_victor("sorrindo") as victor at sprite_esquerda with dissolve

            show emilia camisa aberta nsfw corada at sprite_direita with dissolve

            emilia "Victor... Se for você... eu não me importo de baixar a minha guarda por completo hoje."

        "Puxá-la para a cama e tomar a iniciativa (+Domínio / +Afeto)":

            $ dominio_jogador += 2

            $ afeto_emilia += 3

            show expression obter_sprite_victor("confiante") as victor at sprite_esquerda with dissolve

            show emilia excitada encarando com a cabeca inclinada at sprite_direita with dissolve

            emilia "Ahn... Suas mãos estão tão firmes hoje, Victor... Feche a porta com chave..."

    $ estagio_emilia = 3

    $ persistent.mem_emilia_2 = True

    $ renpy.end_replay()

    "🔓 [[MEMÓRIA DESBLOQUEADA NA GALERIA: 'Calor Humano no Quarto' — Emília atingiu o Estágio Máximo!]]"

    jump menu_encontro_emilia

# --- VALÉRIA MARCO 1: CONTRATO DE EXCLUSIVIDADE ---

label evento_marco_valeria_1:
    $ local_atual = "caldeiras"
    call restaurar_fundo_local_atual

    if renpy.loadable("audio/musicas/midnight_in_the_underpass.mp3"):
        play music "audio/musicas/midnight_in_the_underpass.mp3" if_changed fadein 1.5
    elif renpy.loadable("audio/at_the_green_fairy.ogg"):
        play music "audio/at_the_green_fairy.ogg" if_changed fadein 1.5

    show expression obter_sprite_victor("confiante") as victor at sprite_esquerda with dissolve

    show valeria perfil sorriso provocador meio corpo at sprite_direita with dissolve

    "🌟 [[EVENTO DE MARCO I — VALÉRIA]]: Valéria gira o pirulito entre os dedos e senta sobre a bancada de metal das caldeiras, bloqueando minha saída."

    $ th_voz("climax/valeria_marco_01_socio")
    valeria "Sabe, bolsista, você já gastou tempo e dinheiro demais aqui embaixo para continuar sendo apenas um cliente comum."

    menu:

        "Imprensá-la na bancada: 'Então mude meu status para sócio majoritário.' (+Domínio / +Afeto)":

            $ dominio_jogador += 2

            $ afeto_valeria += 2

            $ th_bark("valeria", "monopolio_virada")

            show valeria shorts cropped descolada corpo inteiro at sprite_direita with dissolve

            valeria "Hahaha! Olha só a audácia do garoto! Fechado, sócio. A partir de hoje você tem acesso VIP à mercadoria."

        "Negociar descontos e proteção mútua (+Intelecto / +$100 / +Afeto)":

            $ intelecto += 1

            $ dinheiro_jogador += 100

            $ afeto_valeria += 2

            show valeria frascos sorriso meio corpo at sprite_direita with dissolve

            valeria "Gosto de um homem com visão de negócios. Toma aqui sua participação nos lucros da semana (+$100)."

    $ estagio_valeria = 2

    $ persistent.mem_valeria_1 = True

    $ renpy.end_replay()

    "🔓 [[MEMÓRIA DESBLOQUEADA NA GALERIA: 'Contrato de Exclusividade' — Valéria avançou para o Estágio 2!]]"

    jump menu_encontro_valeria

# --- VALÉRIA MARCO 2: DONA DO SUBMUNDO ---

label evento_marco_valeria_2:
    $ local_atual = "bar_fada_verde"
    call restaurar_fundo_local_atual

    if renpy.loadable("audio/musicas/midnight_in_the_underpass.mp3"):
        play music "audio/musicas/midnight_in_the_underpass.mp3" if_changed fadein 1.5
    elif renpy.loadable("audio/bar-da-fada-verde.ogg"):
        play music "audio/bar-da-fada-verde.ogg" if_changed fadein 1.5

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show valeria shorts cropped seria corpo inteiro at sprite_direita with dissolve

    "🌟 [[EVENTO DE MARCO II — VALÉRIA]]: Após o expediente do Bar da Fada Verde, Valéria tira a jaqueta pesada e destranca o depósito privado nos fundos."

    $ th_voz("climax/valeria_marco_02_bar")
    valeria "Não conto isso pra ninguém, Victor... mas quando o Eclipse chegar, você é a única pessoa nesta cidade que eu não deixaria para trás."

    menu:

        "Tomar o pirulito dela e beijá-la no balcão (+Domínio / +Afeto)":

            $ dominio_jogador += 2

            $ afeto_valeria += 3

            $ th_bark("valeria", "fada_verde")

            show valeria sorriso provocante pirulito meio corpo at sprite_direita with dissolve

            valeria "Mmm... Dessa vez eu nem vou te cobrar os cinquenta dólares de taxa, parceiro."

    $ estagio_valeria = 3

    $ persistent.mem_valeria_2 = True

    $ renpy.end_replay()

    "🔓 [[MEMÓRIA DESBLOQUEADA NA GALERIA: 'Dona do Submundo' — Valéria atingiu o Estágio Máximo!]]"

    jump menu_encontro_valeria

# --- ELARA MARCO 1: INSPEÇÃO A PORTAS FECHADAS ---

label evento_marco_elara_1:
    $ local_atual = "salao_gremio"
    call restaurar_fundo_local_atual

    if renpy.loadable("audio/musicas/tema_de_elara.mp3"):
        play music "audio/musicas/tema_de_elara.mp3" if_changed fadein 1.5
    elif renpy.loadable("audio/The_Cold_Decree.ogg"):
        play music "audio/The_Cold_Decree.ogg" if_changed fadein 1.5

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show elara encarando de forma astuta at sprite_direita with dissolve

    "🌟 [[EVENTO DE MARCO I — ELARA]]: Elara dispensa os guardas do Conselho e fecha as cortinas do Gabinete."

    $ th_voz("climax/elara_marco_01_inspecao")
    elara "Você é uma contradição ambulante, Sr. Vane. Carrega o sangue rebelde de Lyra von Blut, mas mantém a postura diante da minha mesa. Aproxime-se para a inspeção do Grilhão."

    menu:

        "Sustentar o olhar dela a centímetros de distância (+Domínio / +Coragem / +Afeto)":

            $ dominio_jogador += 2

            $ coragem += 1

            $ afeto_elara += 2

            show expression obter_sprite_victor("confiante") as victor at sprite_esquerda with dissolve

            show elara bochechas rosadas at sprite_direita with dissolve

            elara "Que petulância... Se qualquer outro lacaio me olhasse com essa fome, já estaria sem cabeça. Mas em você... é intrigante."

        "Curvar-se com elegância impecável (+Charme / -20%% Exposição / +Afeto)":

            $ charme += 1

            $ exposicao = max(0, exposicao - 20)

            $ afeto_elara += 2

            show expression obter_sprite_victor("charmoso") as victor at sprite_esquerda with dissolve

            show elara sorrindo com rosto arrogante at sprite_direita with dissolve

            elara "Pelo menos você aprende rápido como tratar uma soberana."

    $ estagio_elara = 2

    $ persistent.mem_elara_1 = True

    $ renpy.end_replay()

    "🔓 [[MEMÓRIA DESBLOQUEADA NA GALERIA: 'Inspeção a Portas Fechadas' — Elara avançou para o Estágio 2!]]"

    jump menu_encontro_elara

# --- ELARA MARCO 2: A COROA SUBJUGADA ---

label evento_marco_elara_2:
    $ local_atual = "salao_gremio"
    call restaurar_fundo_local_atual

    if renpy.loadable("audio/musicas/tema_de_elara.mp3"):
        play music "audio/musicas/tema_de_elara.mp3" if_changed fadein 1.5
    elif renpy.loadable("audio/Authority_Breach.ogg"):
        play music "audio/Authority_Breach.ogg" if_changed fadein 1.5

    show expression obter_sprite_victor("serio") as victor at sprite_esquerda with dissolve

    show elara bochechas rosadas at sprite_direita with dissolve

    "🌟 [[EVENTO DE MARCO II — ELARA]]: À meia-noite no Gabinete, a armadura fria da Presidente cede quando ficamos a sós."

    $ th_voz("climax/elara_marco_02_coroa")
    elara "Passei um século dando ordens nesta academia, Victor... Por que perto de você eu sinto que a coleira mudou de mãos?"

    menu:

        "Tomar o controle sobre a cadeira da Presidência (+Domínio / +Afeto)":

            $ dominio_jogador += 3

            $ afeto_elara += 3

            show expression obter_sprite_victor("charmoso") as victor at sprite_esquerda with dissolve

            show elara com prazer at sprite_direita with dissolve

            elara "Ahn... Victor... Se os executores ouvirem a voz da Presidente falhando assim... você será o meu fim..."

    $ estagio_elara = 3

    $ persistent.mem_elara_2 = True

    $ renpy.end_replay()

    "🔓 [[MEMÓRIA DESBLOQUEADA NA GALERIA: 'A Coroa Subjugada' — Elara atingiu o Estágio Máximo!]]"

    jump menu_encontro_elara

# ==============================================================================

# TELA WORLD OF HORROR: QUADRO DE MISTÉRIOS & RUÍNA DA CRIPTA

# ==============================================================================

screen quadro_misterios_woh():

    tag menu

    modal True

    zorder 95

    add Solid("#090b10f6")

    frame:

        align (0.5, 0.5)

        xysize (1640, 920)

        background "#10131cee"

        padding (35, 25)

        vbox:

            spacing 18

            hbox:

                xfill True

                vbox:

                    spacing 4

                    text "📋 INVESTIGAÇÃO DE LENDAS URBANAS & DOOM & DETERIORAÇÃO" size 28 bold True color "#ffcc00"

                    text "Inspiração: World of Horror (panstasz) — Casos Modulares & Apocalipse Iminente" size 16 color "#aaaaaa"

                textbutton "✖ FECHAR" action Return() xalign 1.0 text_size 24 text_color "#00ffcc"

            # Painel do DOOM Clock & Status da Escola

            frame:

                xfill True background "#1a202c" padding (20, 14)

                vbox:

                    spacing 8

                    hbox:

                        spacing 25

                        text "⚡ DOOM & DETERIORAÇÃO (DOOM CLOCK): [ruina_cain]%%" size 22 bold True color ("#ff2244" if ruina_cain >= 50 else "#ff9955")

                        text "ESTADO DA ACADEMIA: " + GerenciadorRuina.obter_descricao_status() size 18 color "#00ffcc"

                    bar value ruina_cain range 100 xysize (1560, 20)

                    hbox:

                        spacing 20

                        text "🩸 SEQUELAS / PARANOIAS ATIVAS:" size 16 bold True color "#ff6666"

                        if sequelas_ativas:

                            for seq in sequelas_ativas:

                                text "⚠️ " + seq["nome"] + " (" + seq["penalidade"] + ")" size 15 color "#ff9999"

                        else:

                            text "Nenhuma sequela física ou perturbação mental ativa." size 15 color "#88cc88"

            null height 5

            text "🔍 CASOS E LENDAS URBANAS EM ANDAMENTO:" size 22 bold True color "#66ff66"

            # Grade dos 5 Mistérios

            viewport:

                scrollbars "vertical" mousewheel True draggable True

                xfill True ysize 530

                vbox:

                    spacing 15

                    for m_id, obj_m in MISTERIOS_ACADEMIA.items():

                        frame:

                            xfill True background "#1e2536" padding (20, 16)

                            hbox:

                                spacing 20 xfill True

                                vbox:

                                    spacing 6 xsize 1150

                                    hbox:

                                        spacing 10

                                        text "[obj_m.icone] [obj_m.titulo]" size 22 bold True color "#ffffff"

                                        text "• Foco: [obj_m.local_foco!u]" size 17 color "#ffccaa"

                                        text "• " + obj_m.progresso_texto size 17 bold True color ("#66ff66" if obj_m.resolvido else "#ffcc00")

                                    text "[obj_m.descricao]" size 16 color "#cccccc"

                                    text "Recompensa de Selamento: [obj_m.recompensa_nome]" size 15 color "#00ffcc"

                                vbox:

                                    xalign 1.0 yalign 0.5 spacing 8

                                    if obj_m.resolvido:

                                        text "✔ CASO SELADO" size 18 bold True color "#66ff66" xalign 1.0

                                    elif local_atual == obj_m.local_foco:

                                        if passos_restantes_periodo > 0:

                                            textbutton "🔎 INVESTIGAR NESTE LOCAL (1 PASSO)":

                                                action [Return(), Jump("investigar_passo_bs")]

                                                text_size 17 text_bold True text_color "#ffcc00" text_hover_color "#ffffff"

                                                tooltip "Gasta 1 Passo de Ação para vasculhar a área e desvendar pistas deste mistério."

                                        else:

                                            text "Passos esgotados neste turno" size 15 color "#ff5555" xalign 1.0

                                    else:

                                        text "Vá até [obj_m.local_foco!u] para investigar" size 15 color "#777777" xalign 1.0

# ==============================================================================

# ALUCINAÇÃO DA SEDE CRÍTICA & BANCO DE MICRO-EVENTOS .ITO (WORLD OF HORROR)

# ==============================================================================

label alucinacao_fome_critica_bs:

    show screen overlay_frenesi_vermelho

    $ th_stinger("fome")

    $ th_sfx("heartbeat")

    with flash_red

    with vpunch

    "⚠️ [[ALUCINAÇÃO DA SEDE CRÍTICA]]: Suas têmporas pulsam furiosamente! O ar ao redor parece tingido de escarlate..."

    "Das sombras do corredor, uma silhueta contorcida de garras compridas avança direto contra o seu pescoço!"

    $ rolo_aluc = renpy.random.randint(1, 20) + getattr(store, "sensibilidade_sobrenatural", 1)

    if rolo_aluc >= 11:

        "🧠 [[LUCIDEZ RECUPERADA]] (Sensibilidade: [rolo_aluc] vs Dificuldade 11):"

        "Você cerra os punhos e crava as unhas nas palmas até sentir a dor crua! A visão se estilhaça em fumaça..."

        "Não era um carrasco. Apenas uma cortina pesada balançando sob o vento da janela e dois alunos que se afastam apressados."

        hide screen overlay_frenesi_vermelho with dissolve

        jump entrar_local_exploracao_bs

    else:

        "💥 [[DELÍRIO PREDATÓRIO]] (Falha no Teste de Sensibilidade: [rolo_aluc] vs Dificuldade 11):"

        "Cego pelo pânico da Besta, você desfere um golpe desesperado contra o vazio! O impacto esmaga um armário de metal num estrondo violento!"

        $ exposicao = min(100, exposicao + 18)

        $ hp_jogador = max(10, hp_jogador - 5)

        hide screen overlay_frenesi_vermelho with dissolve

        "Alunos gritam no andar superior e passos apressados de monitores começam a ecoar! (+18%% Exposição | -5 HP de impacto)"

        jump entrar_local_exploracao_bs

label micro_evento_ito_corredor:

    python:
        _mapa_pool_ito = {
            "biblioteca": ["manuscrito_biblioteca"],
            "sala_ocultismo": ["gravador_k7"],
            "caldeiras": ["dutos_contrabando"],
            "sala_caldeiras": ["dutos_contrabando"],
            "catacumbas": ["capela_esquecida"],
            "cripta_cofre": ["capela_esquecida"],
            "banheiro_abandonado": ["espelho_trincado"],
            "salao_gremio": ["professores_trancada", "espelho_trincado"],
            "corredor_academia": ["professores_trancada", "dutos_contrabando", "espelho_trincado"],
            "corredores_principais": ["professores_trancada", "dutos_contrabando", "espelho_trincado"],
            "corredor_interditado": ["dutos_contrabando", "espelho_trincado"],
        }
        _pool_local_ito = _mapa_pool_ito.get(local_atual, [])
        sorteio_ito = renpy.random.choice(_pool_local_ito) if _pool_local_ito else None

    if sorteio_ito is None:
        jump loot_aleatorio_bs

    if sorteio_ito == "professores_trancada":

        "🚪 [[MICRO-EVENTO]]: A Sala dos Professores Trancada."

        "Você se depara com a porta de carvalho maciço do corpo docente. Uma corrente com cadeado pesado impede a entrada, mas papéis importantes estão espalhados sobre a mesa visível pela fresta."

        menu:

            "🔓 [[INTELECTO]] Tentar forçar o mecanismo com um arame fino (Dificuldade 10)":

                $ teste = renpy.random.randint(1, 20) + getattr(store, "intelecto", 1)

                if teste >= 10:

                    $ dinheiro_jogador += 140

                    $ conhecimento_oculto += 1

                    "✨ [[SUCESSO]]: O trinco cede com um clique seco! Você encontra envelopes confidenciais com créditos e anotações sigilosas (+$140 | +1 Conhecimento Oculto)."

                else:

                    $ exposicao = min(100, exposicao + 15)

                    "⚠️ [[FALHA]]: A gazua entorta na tranca, disparando um alarme elétrico discreto! (+15%% Exposição)."

            "👁️ [[SENSIBILIDADE]] Espiar pela fresta com visão predatória (-5%% Saciedade)":

                $ fome_sangue = max(0, fome_sangue - 5)

                $ conhecimento_oculto += 2

                "Seus olhos captam anotações rasuradas sobre as transferências misteriosas de alunos (+2 Conhecimento Oculto)."

            "🚶 Ignorar e seguir em frente discretamente":

                "Você decide não se expor a riscos desnecessários."

    elif sorteio_ito == "gravador_k7":

        "📼 [[MICRO-EVENTO]]: O Gravador K7 no Clube de Ocultismo."

        "Sob uma pilha de cinzas de incenso, uma fita magnética ainda gira lentamente num aparelho K7 antigo. Uma voz sussurra ladainhas em uma língua pré-diluviana que faz seu sangue ferver."

        menu:

            "🎧 Ouvir a gravação até o final (+3 Ocultismo / +3%% Ruína)":

                $ conhecimento_oculto += 3

                $ GerenciadorRuina.adicionar_ruina(3, "Gravação Oculta Escutada")

                "As frases penetram em sua mente como agulhas de gelo. Você compreende segredos cósmicos terríveis (+3 Conhecimento Oculto | +3%% Ruína)."

            "🔥 Queimar a fita magnética com fósforos (+5 Humanidade)":

                $ humanidade = min(100, humanidade + 5)

                "O fogo consome o plástico e o sussurro cala-se em agonia. Você preserva sua sanidade (+5 Humanidade)."

            "💼 Guardar a fita para vender a Valéria (+100 créditos)":

                $ dinheiro_jogador += 100

                "Valéria adora quinquilharias com resíduos de éter (+$100 créditos)."

    elif sorteio_ito == "dutos_contrabando":

        "📦 [[MICRO-EVENTO]]: A Entrega Clandestina nos Dutos."

        "Você flagra um monitor de uniforme branco recebendo uma caixa lacrada de um homem encapuzado vindo dos dutos de ventilação."

        menu:

            "🗡️ [[CORAGEM]] Intimidar o monitor nas sombras (Dificuldade 10)":

                $ teste = renpy.random.randint(1, 20) + getattr(store, "coragem", 1)

                if teste >= 10:

                    $ dose_absinto += 1

                    $ dinheiro_jogador += 80

                    "✨ [[SUCESSO]]: O monitor empalidece diante do seu olhar de predador e deixa a caixa para trás! (+1 Absinto | +$80)."

                else:

                    $ exposicao = min(100, exposicao + 15)

                    "⚠️ [[FALHA]]: O comparsa do duto arremessa uma lata de graxa e ambos fogem alertando a ronda! (+15%% Exposição)."

            "🤫 Chantagear o monitor por silêncio em troca de créditos":

                $ dinheiro_jogador += 120

                $ exposicao = min(100, exposicao + 8)

                "Ele enfia notas amassadas no seu bolso e some pelo corredor (+$120 créditos | +8%% Exposição)."

            "🚶 Manter a cobertura e recuar":

                "Você memoriza os rostos e deixa o contrabando passar."

    elif sorteio_ito == "capela_esquecida":

        "⛪ [[MICRO-EVENTO]]: A Capela Antiga Subterrânea."

        "Um nicho esquecido atrás dos arquivos guarda um altar de pedra com um crucifixo de ferro e cinzas de mirra."

        menu:

            "🕊️ Ajoelhar-se diante do altar sagrado (+10 Humanidade / -10 HP Queimadura)":

                $ humanidade = min(100, humanidade + 10)

                $ hp_jogador = max(10, hp_jogador - 10)

                "O solo consagrado queima a sua pele de vampiro, mas a oração resgata fragmentos da sua alma (+10 Humanidade | -10 HP)."

            "📜 [[CONHECIMENTO OCULTO]] Estudar as inscrições nas lápides (Dificuldade 9)":

                $ teste = renpy.random.randint(1, 20) + getattr(store, "conhecimento_oculto", 1)

                if teste >= 9:

                    $ conhecimento_oculto += 2

                    "Você decifra a linhagem dos fundadores que ergueram este colégio sobre as catacumbas (+2 Conhecimento Oculto)."

                else:

                    "As letras estão desgastadas demais pelo tempo."

            "💍 Saquear a relíquia cerimonial do altar (+1 Giz de Proteção / +1 Gaze)":

                $ giz_protecao += 1

                $ gaze_consagrada += 1

                "Você recolhe os itens rituais antes que os monitores percebam (+1 Giz | +1 Gaze Consagrada)."

    elif sorteio_ito == "espelho_trincado":

        "🪞 [[MICRO-EVENTO]]: O Reflexo Distorcido no Corredor."

        "Um grande espelho de moldura dourada trincado ao meio exibe um reflexo que não replica seus movimentos com exatidão..."

        menu:

            "👁️ [[SENSIBILIDADE]] Focar a visão através da fenda de vidro (Dificuldade 10)":

                $ teste = renpy.random.randint(1, 20) + getattr(store, "sensibilidade_sobrenatural", 1)

                if teste >= 10:

                    $ conhecimento_oculto += 2

                    "✨ [[SUCESSO]]: O reflexo revela a silhueta da Presidente Elara conferindo o cofre no andar superior (+2 Conhecimento Oculto)."

                else:

                    $ hp_jogador = max(10, hp_jogador - 8)

                    "⚠️ [[FALHA]]: Uma onda psíquica rebenta do espelho, causando uma vertigem cortante (-8 HP)."

            "🔨 Despedaçar o vidro com um fragmento de ferro (-6%% Ruína / +12%% Exposição)":

                $ ruina_cain = max(0, ruina_cain - 6)

                $ exposicao = min(100, exposicao + 12)

                with hpunch

                "O estilhaçar do espelho purifica a anomalia do setor, mas o barulho ecoa pela ala (-6%% Ruína | +12%% Exposição)."

            "🚶 Desviar o olhar e seguir em frente":

                "Você ignora o chamado espectral do vidro."

    else:

        "📖 [[MICRO-EVENTO]]: O Manuscrito Esquecido na Biblioteca."

        "Entre tomos empoeirados, você descobre folhas arrancadas de um diário acadêmico de 1890 com fórmulas alquímicas."

        menu:

            "🔬 [[INTELECTO]] Decifrar as fórmulas rúnicas (Dificuldade 10)":

                $ teste = renpy.random.randint(1, 20) + getattr(store, "intelecto", 1)

                if teste >= 10:

                    $ conhecimento_oculto += 2

                    $ dominio_jogador = getattr(store, "dominio_jogador", 0) + 1

                    "✨ [[SUCESSO]]: Você compreende o método antigo de contenção de aberrações (+2 Conhecimento Oculto | +1 Domínio)."

                else:

                    "As rasuras em latão impedem a compreensão exata."

            "🖍️ Usar Giz de Proteção para purificar as folhas (-1 Giz / -5%% Ruína)":

                if giz_protecao >= 1:

                    $ giz_protecao -= 1

                    $ ruina_cain = max(0, ruina_cain - 5)

                    "O traço rúnico dissolve o miasma contaminado das páginas (-1 Giz | -5%% DOOM)."

                else:

                    "Você não possui Giz de Proteção no inventário."

            "🚶 Deixar o livro na estante":

                "Você fecha o tomo com cuidado e o devolve ao esconderijo."

    jump entrar_local_exploracao_bs

# ==============================================================================
# 16. COBRANÇA PERIÓDICA DO CONSELHO & PRESENTES CLANDESTINOS (ECONOMIA & VÍNCULOS)
# ==============================================================================

label evento_cobranca_taxa_academica:
    $ cobranca_vencida_pendente = False
    $ _valor_taxa = calcular_valor_cobranca_academica()
    $ _parcial_taxa = min(dinheiro_jogador, max(20, int(round(_valor_taxa * 0.40))))

    if periodo == "Noite":
        scene bg animado dormitorio quarto noite luar with dissolve
    elif periodo == "Tarde":
        scene bg animado dormitorio quarto tarde sol with dissolve
    else:
        scene bg animado dormitorio quarto manha raio sol with dissolve

    play sound "audio/sfx/sfx_dossie_carta_deslizar.ogg"
    $ th_stinger("duvida")
    $ th_voz("mobs/mob_diretor_f1")

    "Um envelope lacrado com cera negra desliza por baixo da fresta da porta do dormitório antes mesmo de o corredor despertar."
    if divida_monitores > 0:
        show elara burocrata formal meio corpo at sprite_padrao with dissolve
        $ th_bark("elara", "ordem")
        elara "Ordem direta da tesouraria do Conselho, Sr. Vane. A parcela compulsória de amortização e manutenção venceu hoje: $[_valor_taxa]."
        elara "Abateremos o valor da sua dívida se pagar agora. Caso contrário, seu nome entra em inadimplência formal na enfermaria e no expediente."
    else:
        "No timbre oficial lê-se: 'Guia de Manutenção e Quota de Permanência — Dia [dia_atual] ([periodo]). Valor devido ao Conselho Estudantil: $[_valor_taxa]'."

    menu:
        "💳 Quitar integralmente ($[_valor_taxa])" if dinheiro_jogador >= _valor_taxa:
            $ dinheiro_jogador -= _valor_taxa
            $ cobrancas_pagas_total += 1
            $ atrasos_taxa_consecutivos = 0
            if divida_monitores > 0:
                $ divida_monitores = max(0, divida_monitores - _valor_taxa)
            if any(s.get("id") == "taxa_inadimplente" for s in getattr(store, "sequelas_ativas", [])):
                $ curar_sequela("taxa_inadimplente")
            if "divida_taxa_atrasada" in store.registro_dividas_ativas:
                $ store.registro_dividas_ativas["divida_taxa_atrasada"].quitada = True
            play sound "audio/sfx/sfx_moedas_ouro_transacao.ogg"
            $ notificar_rpg("📜 COBRANÇA QUITADA", f"-${_valor_taxa} pagos ao Conselho | Situação regularizada.", "#00ffcc")
            if divida_monitores > 0:
                elara "Contabilizado. Sua pendência remanescente caiu para $[divida_monitores]. Não se atrase no próximo ciclo."
            else:
                "Você deposita o envelope selado na caixa coletora do corredor. O selo verde de quitação pisca discreto na tranca."

        "🩸 Acordo de Extração Sanguínea ($[_parcial_taxa] + -15 HP seguro + +8 Tensão)" if hp_jogador > 20:
            $ dinheiro_jogador = max(0, dinheiro_jogador - _parcial_taxa)
            $ hp_jogador = max(20, hp_jogador - 15)
            $ tensao_psicologica = min(100, tensao_psicologica + 8)
            $ cobrancas_pagas_total += 1
            $ atrasos_taxa_consecutivos = 0
            if divida_monitores > 0:
                $ divida_monitores = max(0, divida_monitores - _parcial_taxa)
            if any(s.get("id") == "taxa_inadimplente" for s in getattr(store, "sequelas_ativas", [])):
                $ curar_sequela("taxa_inadimplente")
            if "divida_taxa_atrasada" in store.registro_dividas_ativas:
                $ store.registro_dividas_ativas["divida_taxa_atrasada"].quitada = True
            play sound "audio/sfx/sfx_frasco_alquimia_vidro.ogg"
            $ th_bark("victor", "dor_leve")
            $ notificar_rpg("🩸 ACORDO CORPORAL ACEITO", f"-${_parcial_taxa}, -15 HP e +8 Tensão pela cota parcial.", "#ffaa44")
            "Um frasco esterilizado acompanha a guia anexa. Você entrega o pouco dinheiro que resta e compensa a diferença com uma punção silenciosa no antebraço."
            if divida_monitores > 0:
                elara "Metade moeda, metade matéria-prima para os laboratórios. Por ora, aceitamos a compensação."

        "⚠️ Declarar Inadimplência (+10%% Exposição, +12 Tensão, -2 Humanidade, Sequela)":
            if exposicao < 74:
                $ exposicao = min(74, exposicao + 10)
            else:
                $ exposicao = min(78, exposicao + 3)
            $ tensao_psicologica = min(100, tensao_psicologica + 12)
            $ humanidade = max(0, humanidade - 2)
            $ atrasos_taxa_consecutivos += 1
            $ aplicar_sequela("taxa_inadimplente", "Inadimplente do Conselho", "Restrição administrativa por atraso nas taxas.", "+25%% na Enfermaria e -20%% em relatórios do Grêmio")
            $ store.registro_dividas_ativas["divida_taxa_atrasada"] = DividaAtiva("divida_taxa_atrasada", "Conselho", f"Taxa Acadêmica em Atraso (${_valor_taxa})", tipo_custo="dinheiro", valor_custo=_valor_taxa, recompensa_texto="Remove Inadimplência e -6%% Exposição")
            play sound "audio/sfx/sfx_psiquico_distorcao_sanidade.ogg"
            $ th_stinger("duvida")
            $ th_bark("victor", "divida")
            $ notificar_rpg("⚠️ INADIMPLÊNCIA REGISTRADA", f"Dívida de ${_valor_taxa} aberta no Livro | Enfermaria +25%% até quitar.", "#ff4444")
            if divida_monitores > 0:
                elara "Que seja, Victor.{w=0.4} Seu crachá acaba de receber restrição administrativa na enfermaria e na tesouraria até quitar essa pendência."
            else:
                "Você rasga o protocolo sem pagar. Poucos segundos depois, o visor do corredor acusa seu registro como INADIMPLENTE no sistema interno."

    hide elara with dissolve
    return

label fluxo_entregar_presente_heroina(alvo_id="emilia"):
    if getattr(store, "presenteou_heroina_hoje", {}).get(alvo_id, False):
        if alvo_id == "lility":
            show lility meio corpo desdenhando at sprite_padrao with dissolve
            lility "Você já trouxe um mimo hoje, meu querido.{w=0.3} Não tente comprar minha paciência duas vezes sob o mesmo sol."
        elif alvo_id == "valeria":
            show valeria cinica pirulito meio corpo at sprite_padrao with dissolve
            valeria "Calma lá, figurão. Já recebi meu agrado de hoje. Guarda o resto pro inventário de amanhã."
        elif alvo_id == "elara":
            show elara uniforme arrogante meio corpo at sprite_padrao with dissolve
            elara "Um gesto por dia já extrapola o decoro aceitável neste prédio, Sr. Vane."
        else:
            show emilia com vergonha arrumando o oculos e olhando para o lado at sprite_padrao with dissolve
            emilia "V-Victor, você já me deu algo hoje...{w=0.4} não gaste tudo comigo em um só dia."
        return

    $ _total_presentes = presente_flores + presente_perfume + presente_colar + presente_roupa + presente_anel
    if _total_presentes <= 0:
        "🎒 Você confere os bolsos internos do casaco, mas não carrega nenhum presente clandestino no momento. Verifique o lote de luxo da Loja Clandestina de Valéria ou o Pátio da Árvore."
        return

    $ _mapa_presentes_ui = {
        "presente_flores": "Buquê de Lírios Negros",
        "presente_perfume": "Perfume Âmbar & Sândalo",
        "presente_colar": "Colar de Prata & Granada",
        "presente_roupa": "Traje Fino / Jaqueta Sob Medida",
        "presente_anel": "Anel de Ônix & Selo Prateado",
    }

    menu:
        "Que presente entregar agora?"

        "💐 Buquê de Lírios Negros (x[presente_flores])" if presente_flores >= 1:
            $ _item_escolhido = "presente_flores"
            $ presente_flores -= 1

        "🌸 Perfume Âmbar & Sândalo (x[presente_perfume])" if presente_perfume >= 1:
            $ _item_escolhido = "presente_perfume"
            $ presente_perfume -= 1

        "📿 Colar de Prata & Granada (x[presente_colar])" if presente_colar >= 1:
            $ _item_escolhido = "presente_colar"
            $ presente_colar -= 1

        "👗 Traje Fino / Jaqueta Sob Medida (x[presente_roupa])" if presente_roupa >= 1:
            $ _item_escolhido = "presente_roupa"
            $ presente_roupa -= 1

        "💍 Anel de Ônix & Selo Prateado (x[presente_anel])" if presente_anel >= 1:
            $ _item_escolhido = "presente_anel"
            $ presente_anel -= 1

        "↩️ Guardar para depois":
            return

    if not isinstance(getattr(store, "presentes_entregues_heroinas", None), dict):
        $ store.presentes_entregues_heroinas = {}
    if not isinstance(getattr(store, "presenteou_heroina_hoje", None), dict):
        $ store.presenteou_heroina_hoje = {}

    $ _lista_hist = list(store.presentes_entregues_heroinas.get(alvo_id, []))
    $ _ja_recebeu = (_item_escolhido in _lista_hist)
    if not _ja_recebeu:
        $ _lista_hist.append(_item_escolhido)
        $ store.presentes_entregues_heroinas[alvo_id] = _lista_hist
    $ store.presenteou_heroina_hoje[alvo_id] = True

    play sound "audio/sfx/sfx_ui_item_coletado.ogg"

    if _ja_recebeu:
        if alvo_id == "emilia":
            $ status_emilia.paciencia = min(status_emilia.paciencia_max, status_emilia.paciencia + 1)
            $ status_emilia.tensao = max(0, status_emilia.tensao - 5)
            show emilia uniforme calma meio corpo at sprite_padrao with dissolve
            $ th_bark("emilia", "timida")
            emilia "Outro exemplar idêntico ao anterior?{w=0.4} Obrigada pelo carinho constante, Victor... mas por favor, não gaste tudo comigo. Já guardei o primeiro com muita devoção."
        elif alvo_id == "lility":
            $ status_lility.tensao = max(0, status_lility.tensao - 5)
            show lility comportada sorriso meio corpo at sprite_padrao with dissolve
            $ th_bark("lility", "risada")
            lility "Repetindo agrados em série, pequeno mortal?{w=0.4} Minha eternidade não se compra com mimos duplicados. Guarde seus recursos para não morrer nos corredores."
        elif alvo_id == "valeria":
            $ status_valeria.paciencia = min(status_valeria.paciencia_max, status_valeria.paciencia + 1)
            show valeria leve sorriso pirulito meio corpo at sprite_padrao with dissolve
            $ th_bark("valeria", "padrao")
            valeria "Outro desse?{w=0.3} Valeu pelo estoque extra, parceiro, mas negócio é negócio. Não adianta empilhar mimo pra tentar me amaciar."
        else:
            $ status_elara.tensao = max(0, status_elara.tensao - 5)
            show elara uniforme observando meio corpo at sprite_padrao with dissolve
            $ th_bark("elara", "aprovacao")
            elara "Você já me entregou um item idêntico antes, Sr. Vane.{w=0.4} O Conselho preza por eficiência, não redundância de cortesias. Afeto não se adquire por atacado."
        $ notificar_rpg("🎁 PRESENTE REPETIDO", f"{_mapa_presentes_ui.get(_item_escolhido, 'Presente')} entregue novamente (+1 Paciência/Alívio | Afeto inalterado).", "#88ccff")
        return

    # Reações exclusivas da primeira entrega (4 heroínas x 5 itens = 20 reações)
    if alvo_id == "emilia":
        if _item_escolhido == "presente_flores":
            call ev_presente_emilia_flores from _call_ev_emilia_flores
        elif _item_escolhido == "presente_perfume":
            $ status_emilia.afeto += 1
            $ status_emilia.duvida = max(0, status_emilia.duvida - 1)
            $ tensao_psicologica = max(0, tensao_psicologica - 6)
            show emilia com vergonha arrumando o oculos e olhando para o lado at sprite_padrao with dissolve
            $ th_stinger("afeto")
            $ th_bark("emilia", "timida")
            emilia "P-perfume de verdade...?{w=0.4} As irmãs da Ordem diriam que é vaidade demais para os nossos votos, mas... o cheiro acalma o medo lá fora."
            $ notificar_rpg("🧴 AGRADO À EXORCISTA", "+1 Afeto de Emília | -1 Suspeita | -6 Tensão", "#88ccff")
        elif _item_escolhido == "presente_colar":
            $ status_emilia.afeto += 1
            $ status_emilia.duvida = max(0, status_emilia.duvida - 1)
            show emilia uniforme calma meio corpo at sprite_padrao with dissolve
            $ th_bark("emilia", "consolo")
            emilia "Prata polida sem o selo da Inquisição...{w=0.4} Por um segundo temi o peso do metal, mas vindo de você não parece uma armadilha."
            emilia "Vou usá-lo por baixo da gola do uniforme. Só entre nós dois."
            $ notificar_rpg("📿 SIGILO DA PRATA", "+1 Afeto de Emília | -1 Suspeita", "#88ccff")
        elif _item_escolhido == "presente_roupa":
            $ status_emilia.afeto += 2
            $ tensao_psicologica = max(0, tensao_psicologica - 10)
            show emilia uniforme corada timida meio corpo at sprite_padrao with dissolve
            $ th_stinger("afeto")
            $ th_bark("emilia", "consolo")
            emilia "Esse tecido é tão macio...{w=0.4} meu suéter reserva rasgou no subsolo semana passada e eu estava congelando nas rondas."
            emilia "Obrigada, Victor. Sério mesmo."
            $ notificar_rpg("🧥 CONFORTO NA VIGÍLIA", "+2 Afeto de Emília | -10 Tensão", "#88ccff")
        else:
            if status_emilia.afeto >= 8 and getattr(store, "estagio_emilia", 1) >= 2:
                call ev_presente_anel_pacto("emilia") from _call_ev_anel_emilia
            else:
                $ presente_anel += 1
                if _item_escolhido in store.presentes_entregues_heroinas.get("emilia", []):
                    $ store.presentes_entregues_heroinas["emilia"].remove(_item_escolhido)
                show emilia uniforme corada timida meio corpo at sprite_padrao with dissolve
                $ th_bark("emilia", "timida")
                emilia "Um anel de promessa...?{w=0.5} Victor... um voto carrega um peso sagrado demais para quem cresceu dentro da capela. Nós mal sobrevivemos aos últimos dias... não posso aceitar um compromisso desses agora."
                $ notificar_rpg("💍 VOTO PREMATURO RECUSADO", "Emília achou cedo demais para aceitar uma aliança (Item preservado no inventário).", "#ffaa00")

    elif alvo_id == "lility":
        if _item_escolhido == "presente_flores":
            $ status_lility.duvida += 1
            show lility meio corpo desdenhando at sprite_padrao with dissolve
            $ th_bark("lility", "deboche")
            lility "Lírios murchos de jardim mortal?{w=0.4} Não sou uma donzela de convento para ser cortejada com flores que apodrecem em dois dias, Victor."
            $ notificar_rpg("💐 DESDÉM DA CRIADORA", f"{nome_display_mestra} desdenhou o buquê perecível (+1 Dúvida | Afeto inalterado).", "#ffaa00")
        elif _item_escolhido == "presente_perfume":
            call ev_presente_lility_perfume from _call_ev_lility_perfume
        elif _item_escolhido == "presente_colar":
            $ status_lility.afeto += 1
            $ status_lility.vinculo_sangue = min(100, status_lility.vinculo_sangue + 4)
            show lility provocante pose corpo inteiro at sprite_padrao with dissolve
            $ th_stinger("afeto")
            $ th_bark("lility", "prazer")
            lility "Uma corrente fina de prata disfarçada de galanteria?{w=0.4} Cuidado, Victor... eu gosto de inverter quem coloca a coleira no pescoço de quem."
            $ notificar_rpg("📿 JOIA DE DOMÍNIO", f"+1 Afeto com {nome_display_mestra} | +4 Vínculo", "#cc66ff")
        elif _item_escolhido == "presente_roupa":
            $ status_lility.afeto += 2
            $ tensao_psicologica = max(0, tensao_psicologica - 5)
            show lility comportada sorriso meio corpo at sprite_padrao with dissolve
            $ th_bark("lility", "padrao")
            lility "Corte impecável. Para alguém acuado por inspetores escolares, você ainda conserva certo refinamento aristocrático."
            $ notificar_rpg("🧥 CORTE NOBRE", f"+2 Afeto de {nome_display_mestra} | -5 Tensão", "#cc66ff")
        else:
            if status_lility.afeto >= 8 and getattr(store, "estagio_mestra", 1) >= 2:
                call ev_presente_anel_pacto("lility") from _call_ev_anel_lility
            else:
                $ presente_anel += 1
                if _item_escolhido in store.presentes_entregues_heroinas.get("lility", []):
                    $ store.presentes_entregues_heroinas["lility"].remove(_item_escolhido)
                show lility encarando com sorriso cabeca de lado at sprite_padrao with dissolve
                $ th_bark("lility", "risada")
                lility "Um anel de submissão?{w=0.4} Você ainda é jovem e volúvel demais para tentar me amarrar a uma aliança de sangue. Prove seu valor antes de me oferecer joias eternas."
                $ notificar_rpg("💍 AUDÁCIA RECUSADA", f"{nome_display_mestra} achou Victor neófito demais para selar alianças eternas (Item preservado no inventário).", "#ffaa00")

    elif alvo_id == "valeria":
        if _item_escolhido == "presente_flores":
            $ status_valeria.duvida = max(0, status_valeria.duvida - 1)
            show valeria cinica pirulito meio corpo at sprite_padrao with dissolve
            $ th_bark("valeria", "padrao")
            valeria "Flores para uma traficante de caldeira?{w=0.3} Olha, é brega pra caramba... mas essas pétalas noturnas dão uma tintura calmante de primeira."
            $ notificar_rpg("💐 MATÉRIA-PRIMA RARA", "-1 Suspeita de Valéria | Afeto inalterado", "#66ff88")
        elif _item_escolhido == "presente_perfume":
            $ status_valeria.afeto += 1
            show valeria perfil sorriso provocador meio corpo at sprite_padrao with dissolve
            $ th_bark("valeria", "provocacao")
            valeria "Âmbar com sândalo escuro...{w=0.4} você tem nariz bom, novato. Melhor do que ficar cheirando ozônio e formol nesse porão."
            $ notificar_rpg("🧴 ESTILO NO PORÃO", "+1 Afeto de Valéria", "#66ff88")
        elif _item_escolhido == "presente_colar":
            $ status_valeria.afeto += 1
            show valeria leve sorriso pirulito meio corpo at sprite_padrao with dissolve
            $ th_stinger("afeto")
            $ th_bark("valeria", "segredo")
            "Ela morde de leve a borda do pingente antes de prendê-lo por cima da gola."
            valeria "Prata legítima 925. Se você tá tentando comprar crédito na minha mesa, parabéns... funcionou mais do que eu queria admitir."
            $ notificar_rpg("📿 CRÉDITO COM VALÉRIA", "+1 Afeto de Valéria", "#66ff88")
        elif _item_escolhido == "presente_roupa":
            call ev_presente_valeria_roupa from _call_ev_valeria_roupa
        else:
            if status_valeria.afeto >= 8 and getattr(store, "estagio_valeria", 1) >= 2:
                call ev_presente_anel_pacto("valeria") from _call_ev_anel_valeria
            else:
                $ presente_anel += 1
                if _item_escolhido in store.presentes_entregues_heroinas.get("valeria", []):
                    $ store.presentes_entregues_heroinas["valeria"].remove(_item_escolhido)
                show valeria casaco verde sorriso meio corpo at sprite_padrao with dissolve
                $ th_bark("valeria", "transe")
                valeria "Calma lá, parceiro.{w=0.4} Eu sou mercadora, não donzela de romance barato. Um anel de compromisso desses? Guarda isso no bolso até a gente ter um contrato de verdade."
                $ notificar_rpg("💍 NEGÓCIO PREMATURO", "Valéria recusou selar aliança matrimonial antes da hora (Item preservado no inventário).", "#ffaa00")

    else:
        if _item_escolhido == "presente_flores":
            $ status_elara.afeto += 1
            show elara uniforme observando meio corpo at sprite_padrao with dissolve
            $ th_bark("elara", "hesitacao")
            elara "Espécimes ornamentais fora da estufa do pátio...{w=0.4} Descarte protocolar? Tudo bem. Deixe sobre o canto direito da escrivaninha por enquanto."
            $ notificar_rpg("💐 ETIQUETA FRIA", "+1 Afeto de Elara", "#ffffff")
        elif _item_escolhido == "presente_perfume":
            $ status_elara.afeto += 1
            show elara bochechas rosadas at sprite_padrao with dissolve
            $ th_bark("elara", "corada")
            elara "Fragrância sob medida é um excesso desnecessário no horário letivo, Sr. Vane.{w=0.4} Mas reconheço que neutraliza o odor férrico das rondas."
            $ notificar_rpg("🧴 CONCESSÃO DE ELARA", "+1 Afeto de Elara", "#ffffff")
        elif _item_escolhido == "presente_colar":
            call ev_presente_elara_colar from _call_ev_elara_colar
        elif _item_escolhido == "presente_roupa":
            $ status_elara.afeto += 2
            $ status_elara.duvida = max(0, status_elara.duvida - 1)
            show elara sorriso frio meio corpo at sprite_padrao with dissolve
            $ th_stinger("afeto")
            $ th_bark("elara", "aprovacao")
            elara "Sobriedade e caimento impecável, sem emblemas vulgares.{w=0.4} Raro ver alguém da sua posição entender o código estético do Conselho."
            $ notificar_rpg("🧥 POSTURA APROVADA", "+2 Afeto de Elara | -1 Suspeita", "#ffffff")
        else:
            if status_elara.afeto >= 8 and getattr(store, "estagio_elara", 1) >= 2:
                call ev_presente_anel_pacto("elara") from _call_ev_anel_elara
            else:
                $ presente_anel += 1
                if _item_escolhido in store.presentes_entregues_heroinas.get("elara", []):
                    $ store.presentes_entregues_heroinas["elara"].remove(_item_escolhido)
                show elara uniforme autoritaria meio corpo at sprite_padrao with dissolve
                $ th_bark("elara", "hesitacao")
                elara "Isto viola completamente o decoro e a hierarquia institucional.{w=0.4} Guarde este anel, Sr. Vane. Nossa relação deve ser pautada pelo dever e rigor, ao menos por enquanto."
                $ notificar_rpg("💍 PROTOCOLO INSTITUCIONAL", "Elara recusou o anel por quebra de decoro estudantil (Item preservado no inventário).", "#ffaa00")

    return

# ------------------------------------------------------------------------------
# 5 MICRO-EVENTOS REATIVOS DE PRESENTES (MÍDIA EXISTENTE)
# ------------------------------------------------------------------------------

label ev_presente_emilia_flores:
    $ status_emilia.afeto += 1
    $ status_emilia.duvida = max(0, status_emilia.duvida - 1)
    $ humanidade = min(100, humanidade + 3)
    $ tensao_psicologica = max(0, tensao_psicologica - 8)
    show emilia com vergonha arrumando o oculos e olhando para o lado at sprite_padrao with dissolve
    $ th_stinger("afeto")
    $ th_bark("emilia", "presente_flores")
    "Emília segura o buquê com os dedos trêmulos, como se as pétalas pudessem se desfazer ao toque das luvas desgastadas."
    emilia "Faz anos que ninguém me traz flores que não sejam para colocar em um altar vazio, Victor...{w=0.4} Achei que você só olhasse para os mapas e as feridas."
    "Ela aproxima uma flor prateada da folha marcada do próprio livro de orações, pressionando-a ali entre as páginas como marcador."
    emilia "Quando essa noite finalmente passar...{w=0.3} prometa que você ainda vai se lembrar de como as coisas vivas cheiram sem sangue por perto."
    $ notificar_rpg("💐 MARCA-PÁGINAS DA CAPELA", "+1 Afeto de Emília | -1 Suspeita | +3 Humanidade | -8 Tensão", "#88ccff")
    return

label ev_presente_lility_perfume:
    $ status_lility.afeto += 2
    $ status_lility.vinculo_sangue = min(100, status_lility.vinculo_sangue + 5)
    show lility sorrindo com rosto rosado at sprite_padrao with dissolve
    $ th_stinger("afeto")
    $ th_bark("lility", "prazer")
    "[nome_display_mestra] destampa o frasco escuro sem pressa e encosta o aplicador direto na curvatura fria do próprio pulso antes de estender o braço até o seu rosto."
    lility "Âmbar e sândalo amargo...{w=0.4} Ah, Victor. Eu conhecia uma destilaria em Praga que só vendia essa fórmula para quem sabia sangrar em silêncio."
    show lility provocante pose corpo inteiro at sprite_padrao with dissolve
    lility "Agora você marcou a própria assinatura na minha pele por esta noite.{w=0.4} Vamos ver se aguenta sentir esse perfume toda vez que eu passar atrás de você na escuridão."
    $ notificar_rpg("🧴 ASSINATURA DE SANGUE", f"+2 Afeto com {nome_display_mestra} | +5 Vínculo Carmesim", "#cc66ff")
    return

label ev_presente_elara_colar:
    $ status_elara.afeto += 2
    $ status_elara.duvida = max(0, status_elara.duvida - 2)
    $ exposicao = max(0, exposicao - 8)
    show elara em choque at sprite_padrao with dissolve
    $ th_stinger("pista")
    $ th_bark("elara", "presente_colar")
    "Elara congela com a corrente fina suspensa entre os dedos por dois segundos inteiros — algo raro na presidente cuja postura nunca falha."
    show elara bochechas rosadas at sprite_padrao with dissolve
    elara "Você sabe o que está fazendo, Sr. Vane?{w=0.4} Presentear um membro do alto Conselho sem nota fiscal constitui violação direta do código."
    "Mesmo assim, ela vira ligeiramente o pescoço e afasta os cabelos claros para fechar o fecho prateado junto à clavícula."
    elara "Arquivarei três notificações de patrulha referentes ao seu setor hoje à noite.{w=0.4} Considere... um ajuste discricionário de relatório."
    $ notificar_rpg("📿 AJUSTE DE PROTOCOLO", "+2 Afeto de Elara | -2 Suspeita | -8%% Exposição", "#ffffff")
    return

label ev_presente_valeria_roupa:
    $ valeria_usando_jaqueta_presente = True
    $ status_valeria.afeto += 2
    $ status_valeria.duvida = max(0, status_valeria.duvida - 2)
    $ tampao_hemostatico += 1
    show valeria jaqueta pins corpo inteiro at sprite_padrao with dissolve
    $ th_stinger("afeto")
    $ th_bark("valeria", "presente_jaqueta")
    "Valéria joga fora o antigo jaleco remendado sobre uma caixa de munição e veste a jaqueta nova ali mesmo, ajustando os bolsos ocultos na barra."
    valeria "Caramba... forro reforçado contra estilhaço e quatro bolsos costurados por dentro?{w=0.4} Agora sim a gente conversa na mesma língua, sócio!"
    valeria "Toma aqui um protótipo de tampão hemostático da minha bancada pessoal por conta da casa.{w=0.3} E pode contar com uma mercadora bem mais generosa daqui pra frente."
    $ notificar_rpg("🧥 NOVA PATENTE NA CALDEIRA", "+2 Afeto de Valéria | -2 Suspeita | +1 Tampão Hemostático", "#66ff88")
    return

label ev_presente_anel_pacto(alvo_id="emilia"):
    $ th_stinger("afeto")
    play sound "audio/sfx/sfx_moedas_ouro_transacao.ogg"

    if alvo_id == "emilia":
        $ status_emilia.afeto += 3
        $ status_emilia.duvida = max(0, status_emilia.duvida - 3)
        $ status_emilia.vinculo_sangue = min(100, status_emilia.vinculo_sangue + 15)
        $ humanidade = min(100, humanidade + 6)
        show emilia uniforme corada timida meio corpo at sprite_padrao with dissolve
        $ th_bark("emilia", "reza")
        "Emília deixa o anel deslizar até o dedo anelar esquerdo devagar, como quem firma uma confissão que jamais entraria nos autos da igreja."
        emilia "Se o seu sangue despertar por completo e os caçadores baterem à nossa porta...{w=0.4} eu não vou recuar do seu lado, Victor. Prometa o mesmo por mim."
        $ notificar_rpg("💍 PACTO SILENCIOSO COM EMÍLIA", "+3 Afeto | -3 Suspeita | +15 Vínculo | +6 Humanidade", "#88ccff")

    elif alvo_id == "lility":
        $ status_lility.afeto += 3
        $ status_lility.vinculo_sangue = min(100, status_lility.vinculo_sangue + 20)
        $ fome_sangue = min(100, fome_sangue + 10)
        show lility sorrindo com rosto rosado at sprite_padrao with dissolve
        $ th_bark("lility", "pacto_anel")
        "[nome_display_mestra] toma a sua mão antes mesmo de você fechar a caixa e desliza o anel frio sobre a própria pele pálida."
        lility "Um selo digno de linhagem antiga.{w=0.4} De hoje em diante, nenhum outro parasita nesta escola ousa reclamar o que eu já marquei como meu."
        $ notificar_rpg("💍 JURAMENTO CARMESIM", f"+3 Afeto com {nome_display_mestra} | +20 Vínculo | +10 Saciedade", "#cc66ff")

    elif alvo_id == "valeria":
        $ status_valeria.afeto += 3
        $ status_valeria.vinculo_sangue = min(100, status_valeria.vinculo_sangue + 15)
        $ ampola_prata += 1
        show valeria casaco verde sorriso meio corpo at sprite_padrao with dissolve
        $ th_bark("valeria", "segredo")
        "Valéria gira o anel contra a luz alaranjada da lâmpada de bancada, então deixa escapar um sorriso genuíno que quebra toda a fachada mercenária."
        valeria "Beleza, Victor... sem mais letras miúdas entre a gente.{w=0.4} Se cairmos nessa escola, caímos juntos. Leva essa ampola rara de prata que eu guardava pro pior dia."
        $ notificar_rpg("💍 SOCIEDADE SELADA COM VALÉRIA", "+3 Afeto | +15 Vínculo | +1 Ampola de Prata Líquida", "#66ff88")

    else:
        $ status_elara.afeto += 3
        $ status_elara.duvida = max(0, status_elara.duvida - 3)
        $ status_elara.vinculo_sangue = min(100, status_elara.vinculo_sangue + 15)
        $ exposicao = max(0, exposicao - 10)
        show elara bochechas rosadas at sprite_padrao with dissolve
        $ th_bark("elara", "aprovacao")
        "Elara tranca a porta do salão antes de aceitar o aro prateado, mantendo-o oculto na palma fechada como um segredo de Estado."
        elara "Nenhuma ata oficial mencionará esta noite, Victor.{w=0.4} Mas quando o Conselho iniciar a purga final... você tem a minha palavra reservada."
        $ notificar_rpg("💍 ACORDO RESERVADO COM ELARA", "+3 Afeto | -3 Suspeita | +15 Vínculo | -10%% Exposição", "#ffffff")

    return

