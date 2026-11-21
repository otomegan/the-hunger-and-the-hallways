# ==============================================================================
# ANIMAÇÕES E TRANSFORMS PARA CENAS ÍNTIMAS (LEWD & TRANSE)
# THE HUNGER AND THE HALLWAYS - REN'PY 8.X
# ==============================================================================
# Técnicas acessíveis para solo dev:
# 1. ATL Nativo ("Falso Live2D" com CG estática)
# 2. CG em Camadas (Layered CG com alternância de frames/expressões)
# 3. Micro-loops em Vídeo .webm (Movie VP9 sem áudio)
# ==============================================================================

init -1:

    # ==========================================================================
    # 1. TRANSFORMS ATL ("FALSO LIVE2D" & IMPACTOS CORPÓREOS)
    # ==========================================================================

    # Pulsação rítmica simulando respiração pesada / ofegante contínua
    transform cena_lewd_ofegante:
        xalign 0.5 yalign 0.5
        block:
            easein 0.85 yzoom 1.018 xzoom 1.008 yoffset 6
            easeout 0.85 yzoom 1.0 xzoom 1.0 yoffset 0
            repeat

    # Respiração acelerada para momentos de ápice / alta tensão
    transform cena_lewd_ofegante_rapida:
        xalign 0.5 yalign 0.5
        block:
            easein 0.42 yzoom 1.025 xzoom 1.012 yoffset 9
            easeout 0.42 yzoom 1.0 xzoom 1.0 yoffset 0
            repeat

    # Pequeno solavanco com zoom e recuo simulando impacto corporal / estocada
    transform estocada_impacto:
        xalign 0.5 yalign 0.5
        easein 0.08 zoom 1.035 yoffset 10
        easeout 0.18 zoom 1.0 yoffset 0

    # Impacto mais vigoroso com ligeira rotação e recuo rápido
    transform estocada_forte:
        xalign 0.5 yalign 0.5
        parallel:
            easein 0.06 zoom 1.05 yoffset 14
            easeout 0.16 zoom 1.0 yoffset 0
        parallel:
            easein 0.06 rotate 0.5
            easeout 0.16 rotate 0.0

    # Tremor de espasmo / arrepio no clímax
    transform tremor_climax:
        xalign 0.5 yalign 0.5
        linear 0.04 xoffset 4 yoffset -3
        linear 0.04 xoffset -4 yoffset 3
        linear 0.04 xoffset 3 yoffset -2
        linear 0.04 xoffset -3 yoffset 2
        linear 0.04 xoffset 0 yoffset 0
        pause 0.2
        repeat 4

    # Pulso sensual lento (para preliminares / aproximação / sussurros)
    transform pulso_sensual_lento:
        xalign 0.5 yalign 0.5
        block:
            easein 1.4 zoom 1.012 yoffset 4
            easeout 1.4 zoom 1.0 yoffset 0
            repeat

    # Flash vermelho sutil para ápices de transe de sangue / êxtase
    transform flash_red:
        Solid("#8b0000")
        alpha 0.0
        linear 0.08 alpha 0.55
        linear 0.25 alpha 0.0


# ==============================================================================
# 2. EXEMPLOS DE DECLARAÇÃO DE CGs EM CAMADAS (LAYERED CG LOOPS)
# ==============================================================================
# Exemplo de loop facial (alternância suave de 3 variações da mesma CG)
# Descomente e ajuste os caminhos quando os assets forem gerados:
#
# image cg_lility_climax_loop:
#     "images/cg/lility_climax_f1.webp"
#     0.45
#     "images/cg/lility_climax_f2.webp"
#     0.35
#     "images/cg/lility_climax_f3.webp"
#     0.45
#     repeat


# ==============================================================================
# 3. EXEMPLO DE REPRODUÇÃO DE VÍDEO .WEBM (VP9 SEM ÁUDIO)
# ==============================================================================
# image cg_lility_transmutacao_loop = Movie(
#     play="images/cg/lility_transmutacao.webm",
#     size=(1920, 1080),
#     loop=True
# )


# ==============================================================================
# 4. TEMPLATE DE CENA ÍNTIMA COM ATL & DESIGN DE SOM
# ==============================================================================
# Este label serve como gabarito de roteiro e direção de palco sensorial:

label template_cena_intima_exemplo:
    # 1. Preliminar / Respiração lenta
    scene black with dissolve
    if renpy.loadable("audio/musicas/sighs_in_the_dark.mp3"):
        play music "audio/musicas/sighs_in_the_dark.mp3" fadein 2.0
    elif renpy.loadable("audio/sighs_in_the_dark.ogg"):
        play music "audio/sighs_in_the_dark.ogg" fadein 2.0
    
    # Exibe a CG aplicando a respiração rítmica
    # scene cg_exemplo at cena_lewd_ofegante with dissolve
    "A proximidade torna o ar pesado... cada respiração ecoa entre as paredes frias."

    # 2. Escalada do ritmo / Batimentos aceleram
    # show cg_exemplo at cena_lewd_ofegante_rapida with dissolve
    "O compasso se perde. A pele queima contra o frio da pedra."

    # 3. Ponto de impacto / Estocada
    # show cg_exemplo at estocada_impacto
    # with hpunch
    # play sound "audio/sfx/sfx_impacto_corpo.ogg"
    "Um suspiro escapar descompassado no instante do toque."

    # 4. Ápice / Clímax
    # show cg_exemplo at tremor_climax
    # show layer master at flash_red
    # with vpunch
    "O transe atinge o ápice, dissolvendo o restante do controle."

    return

