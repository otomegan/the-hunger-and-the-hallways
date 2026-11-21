

define protagonist = Character("Victor", color="#e0e0e0")

define protagonista = Character("Victor", color="#e0e0e0")

define victor = Character("Victor", color="#e0e0e0")

default nome_display_mestra = "Mestra"
default segredo_lility_revelado = False
default apelido_lili_desbloqueado = False

define mestra = Character("[nome_display_mestra]", color="#c20000")

define lility = Character("[nome_display_mestra]", color="#c20000")

define elara = Character("Elara", color="#ffffff")

define emilia = Character("Emília", color="#5c85d6")

define filha_exorcista = Character("Emília", color="#5c85d6")

define valeria = Character("Valéria", color="#2eb82e")

define phillip = Character("Lorde Phillip", color="#8c9ba5")

define cain = Character("Cain", color="#8a0303")

define fada_verde = Character("A Fada Verde", color="#00ff66")

define hachishaku = Character("Mulher Gigante", color="#cccccc")

define loira_banheiro = Character("Loira do Banheiro", color="#ff3333")

define dama_espelho = Character("Dama do Espelho", color="#ff4466")

define rival_ghoul = Character("Rival Ghoul", color="#aa2222")

define alquimista_renegado = Character("Alquimista Renegado", color="#2eb82e")

define inquisidor_tatico = Character("Inquisidor Tático", color="#b3b3cc")

define marionete_sangue = Character("Marionete de Sangue", color="#aa0033")
define voz_do_quadro = Character("O Banquete da Fundação", color="#c29b38")
define aluno_pintado = Character("Estudante Aprisionado", color="#778899")

define flash = Fade(0.05, 0.0, 0.15, color="#ffffff")

define flash_red = Fade(0.05, 0.0, 0.20, color="#aa0000")

define flash_green = Fade(0.05, 0.0, 0.20, color="#00aa44")

transform luz_zona_amarela:

    matrixcolor TintMatrix("#faede1") * BrightnessMatrix(-0.02) * SaturationMatrix(0.98)

transform luz_zona_vermelha:

    matrixcolor TintMatrix("#e8d0d0") * BrightnessMatrix(-0.05) * ContrastMatrix(1.03)

transform luz_sombra_noturna:

    matrixcolor TintMatrix("#d8e2f0") * BrightnessMatrix(-0.06) * ContrastMatrix(1.03)

transform pulso_frenesi_vermelho:

    alpha 0.0

    block:
        easein 0.45 alpha 0.45

        easeout 0.45 alpha 0.08

        repeat

screen overlay_frenesi_vermelho():

    zorder 75

    add Solid("#bb0000") at pulso_frenesi_vermelho

transform sprite_padrao:

    xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 1.0 ysize 980 fit "contain"
    function aplicar_filtro_ambiente

    block:
        easein 1.8 yzoom 1.014 xzoom 1.004 yoffset 2

        easeout 1.8 yzoom 1.0 xzoom 1.0 yoffset 0

        repeat

transform sprite_esquerda:

    xpos 0.25 xanchor 0.5 ypos 1.0 yanchor 1.0 ysize 980 fit "contain"
    function aplicar_filtro_ambiente

    block:
        easein 1.9 yzoom 1.014 xzoom 1.004 yoffset 2

        easeout 1.9 yzoom 1.0 xzoom 1.0 yoffset 0

        repeat

transform sprite_direita:

    xpos 0.75 xanchor 0.5 ypos 1.0 yanchor 1.0 ysize 980 fit "contain"
    function aplicar_filtro_ambiente

    block:
        easein 1.7 yzoom 1.014 xzoom 1.004 yoffset 2

        easeout 1.7 yzoom 1.0 xzoom 1.0 yoffset 0

        repeat

transform sprite_colossal:

    xalign 0.5 yalign 1.0 ysize 1080 fit "contain"
    function aplicar_filtro_ambiente

    block:
        easein 1.0 yzoom 1.025 xzoom 1.012 yoffset 4

        easeout 1.0 yzoom 1.0 xzoom 1.0 yoffset 0

        repeat

transform inimigo_ofegante:

    xalign 0.5 yalign 1.0 ysize 980 fit "contain"
    function aplicar_filtro_ambiente

    block:
        easein 0.75 yzoom 1.03 xzoom 1.015 yoffset 5

        easeout 0.75 yzoom 1.0 xzoom 1.0 yoffset 0

        repeat

transform entidade_flutuando:

    xalign 0.5 yalign 1.0 ysize 1020 fit "contain"
    function aplicar_filtro_ambiente

    block:
        ease 2.0 yoffset -18 yzoom 1.01

        ease 2.0 yoffset 0 yzoom 1.0

        repeat

transform pulo_susto:

    yanchor 1.0 ypos 1.0 ysize 980 fit "contain"
    function aplicar_filtro_ambiente

    easein 0.1 yoffset -25

    easeout 0.1 yoffset 0

    block:
        easein 1.8 yzoom 1.014 xzoom 1.004 yoffset 2

        easeout 1.8 yzoom 1.0 xzoom 1.0 yoffset 0

        repeat

transform risada_deboche:

    yanchor 1.0 ypos 1.0 ysize 980 fit "contain"
    function aplicar_filtro_ambiente

    ease 0.12 yoffset -8

    ease 0.12 yoffset 0

    ease 0.12 yoffset -8

    ease 0.12 yoffset 0

    block:
        easein 1.8 yzoom 1.014 xzoom 1.004 yoffset 2

        easeout 1.8 yzoom 1.0 xzoom 1.0 yoffset 0

        repeat

transform bote_ataque:

    xalign 0.5 yalign 1.0 ysize 980 fit "contain"
    function aplicar_filtro_ambiente

    linear 0.08 zoom 1.18 yoffset 30

    linear 0.12 zoom 1.0 yoffset 0

    block:
        easein 0.75 yzoom 1.03 xzoom 1.015 yoffset 5

        easeout 0.75 yzoom 1.0 xzoom 1.0 yoffset 0

        repeat

transform inimigo_caido:

    xalign 0.5 yalign 1.0 ysize 980 fit "contain"
    function aplicar_filtro_ambiente

    linear 0.25 yoffset 120 matrixcolor TintMatrix("#666666")

# ==============================================================================
# ANIMAÇÕES ATL DE TOQUE E REAÇÃO DINÂMICA (POKE & TOUCH)
# ==============================================================================

transform atl_poke_suave:
    easein 0.10 yoffset 10 zoom 1.01
    easeout 0.15 yoffset 0 zoom 1.00

transform atl_poke_recuo:
    easein 0.05 xoffset -14 yoffset 6
    easeout 0.08 xoffset 14 yoffset -6
    easein 0.06 xoffset -6
    easeout 0.08 xoffset 0 yoffset 0

transform atl_poke_bounce:
    easein 0.08 yoffset -16 zoom 1.018
    easeout 0.12 yoffset 5 zoom 0.99
    easein 0.08 yoffset 0 zoom 1.0

transform atl_neutro:
    pass

default anim_toque_lility = atl_neutro
default anim_toque_emilia = atl_neutro
default anim_toque_valeria = atl_neutro
default anim_toque_elara = atl_neutro

# ==============================================================================
# NOVOS SPRITES EXPRESSIVOS & MODALIDADES DE TOQUE (HEROÍNAS)
# ==============================================================================

# --- LILITY (LYRA VON BLUT) ---
image lility carinho na cabeca = "images/lility/lility carinho na cabeca.webp"
image lility carinho cabeca = "images/lility/lility carinho na cabeca.webp"
image lility com a mao levantada = "images/lility/lility com a mao levantada.webp"
image lility mao levantada = "images/lility/lility com a mao levantada.webp"
image lility sorrindo e com bochechas vermelhas = "images/lility/lility sorrindo e com bochechas vermelhas.webp"
image lility bochechas vermelhas = "images/lility/lility sorrindo e com bochechas vermelhas.webp"
image lility sorrindo bochechas vermelhas = "images/lility/lility sorrindo e com bochechas vermelhas.webp"

# --- EMÍLIA VON KARSTEN ---
image emilia fofa toque no rosto = "images/emilia/emilia fofa toque no rosto.webp"
image emilia fofa toque rosto = "images/emilia/emilia fofa toque no rosto.webp"
image emilia toque rosto = "images/emilia/emilia fofa toque no rosto.webp"
image emilia com vergonha segurando a cruz = "images/emilia/emilia com vergonha segurando a cruz.webp"
image emilia segurando cruz = "images/emilia/emilia com vergonha segurando a cruz.webp"
image emilia cruz vergonha = "images/emilia/emilia com vergonha segurando a cruz.webp"

# --- PRESIDENTE ELARA VON WEISS ---
image elara ativando grilhao de sangue e encarando = "images/elara/elara ativando grilhao de sangue e encarando.webp"
image elara grilhao encarando = "images/elara/elara ativando grilhao de sangue e encarando.webp"
image elara ativando grilhao de sangue = "images/elara/elara ativando grilhao de sangue.webp"
image elara ativando grilhao = "images/elara/elara ativando grilhao de sangue.webp"
image elara apos ativar grilhao do sangue = "images/elara/elara apos ativar grilhao do sangue.webp"
image elara grilhao disparado = "images/elara/elara apos ativar grilhao do sangue.webp"
image elara meio corpo com vergonha olhando pro lado = "images/elara/elara meio corpo com vergonha olhando pro lado.webp"
image elara vergonha lado = "images/elara/elara meio corpo com vergonha olhando pro lado.webp"
image elara rubor perfil = "images/elara/elara meio corpo com vergonha olhando pro lado.webp"
image elara envergonhada afastado = "images/elara/elara envergonhada afastado.webp"
image elara envergonhada afastada = "images/elara/elara envergonhada afastado.webp"

# --- VALÉRIA (MERCADORA DAS CALDEIRAS) ---
image valeria cobrando toque = "images/valeria/valeria cobrando toque.webp"
image valeria cobrando = "images/valeria/valeria cobrando toque.webp"
image valeria afastando e ativando armadilha = "images/valeria/valeria afastando e ativando armadilha.webp"
image valeria armadilha = "images/valeria/valeria afastando e ativando armadilha.webp"
image valeria meio corpo sorriso de pura felicidade = "images/valeria/valeria meio corpo sorriso de pura felicidade.webp"
image valeria felicidade = "images/valeria/valeria meio corpo sorriso de pura felicidade.webp"
image valeria sorriso pura felicidade = "images/valeria/valeria meio corpo sorriso de pura felicidade.webp"
image valeria meio corpo determinada = "images/valeria/valeria meio corpo determinada.webp"
image valeria determinada = "images/valeria/valeria meio corpo determinada.webp"
image valeria meio corpo entediada cansada = "images/valeria/valeria meio corpo entediada cansada.webp"
image valeria entediada cansada = "images/valeria/valeria meio corpo entediada cansada.webp"
image valeria entediada = "images/valeria/valeria meio corpo entediada cansada.webp"
image valeria meio corpo exausta = "images/valeria/valeria meio corpo exausta.webp"
image valeria exausta = "images/valeria/valeria meio corpo exausta.webp"
image valeria meio corpo irritada = "images/valeria/valeria meio corpo irritada.webp"
image valeria irritada = "images/valeria/valeria meio corpo irritada.webp"
image valeria meio corpo mal humorada = "images/valeria/valeria meio corpo mal humorada.webp"
image valeria mal humorada = "images/valeria/valeria meio corpo mal humorada.webp"
image valeria meio corpo maquiavelica = "images/valeria/valeria meio corpo maquiavelica.webp"
image valeria maquiavelica = "images/valeria/valeria meio corpo maquiavelica.webp"
image valeria meio corpo melancolica = "images/valeria/valeria meio corpo melancolica.webp"
image valeria melancolica = "images/valeria/valeria meio corpo melancolica.webp"
image valeria meio corpo preocupada = "images/valeria/valeria meio corpo preocupada.webp"
image valeria preocupada = "images/valeria/valeria meio corpo preocupada.webp"
image valeria meio corpo vergonha = "images/valeria/valeria meio corpo vergonha.webp"
image valeria vergonha = "images/valeria/valeria meio corpo vergonha.webp"
image valeria meio corpo confusa = "images/valeria/valeria meio corpo confusa.webp"
image valeria confusa = "images/valeria/valeria meio corpo confusa.webp"
image valeria meio corpo desconfiada = "images/valeria/valeria meio corpo desconfiada.webp"
image valeria desconfiada = "images/valeria/valeria meio corpo desconfiada.webp"
image valeria meio corpo desprezando = "images/valeria/valeria meio corpo desprezando.webp"
image valeria desprezando = "images/valeria/valeria meio corpo desprezando.webp"

default dia_atual = 1

default periodo = "Manhã"

default local_atual = "dormitorio"

default andar_atual = "terreo"

default nivel_barulho_exposicao = 0

default modo_exploracao_livre = False

default saudou_heroina_visita = False
default saudou_enfermeira_visita = False
default coleta_enfermeira_hoje = False
default drenou_enfermeira_hoje = False

default emilia_curativo_feito_visita = False

default passos_restantes_periodo = 3
default limite_visitas_periodo = 3
default visitas_restantes_periodo = 3
default locais_visitados_neste_periodo = []
default deslocando_pelo_mapa = False
default ev_carteira_nora_visto = False
default dia_ultimo_marco_narrativo = 0

default proximo_marco_historia = ""

default dia_proximo_marco = 3

default loc_mestra = "sala_musica"

default loc_emilia = "biblioteca"

default loc_elara = "salao_gremio"

default loc_valeria = "caldeiras"

default hp_jogador = 100

default hp_jogador_max = 100

default fome_sangue = 100

default max_sangue = 100

default humanidade = 75

default exposicao = 0

default tensao_psicologica = 0

default turnos_anemia_recente = 0
default reagiu_exposicao_lility_visita = False
default reagiu_exposicao_emilia_visita = False
default reagiu_exposicao_elara_visita = False
default reagiu_exposicao_valeria_visita = False

default coragem = 1

default intelecto = 1

default charme = 1

default sensibilidade_sobrenatural = 1

default dominio_jogador = 0
default subterfugio = 2

default conhecimento_oculto = 0

default energia_mistica = 50

default ataque_jogador = 20

default defesa_jogador = 5

default afeto_mestra = 0

default afeto_emilia = 0

default afeto_filha_exorcista = 0

default afeto_elara = 0

default afeto_valeria = 0

default duvida_mestra = 0

default duvida_emilia = 0

default duvida_elara = 0

default duvida_valeria = 0

default humor_mestra = "neutra"

default humor_emilia = "timida"

default humor_elara = "severa"

default humor_valeria = "cinica"

default expressao_lility = "lility comportada sorriso meio corpo"

default expressao_emilia = "emilia uniforme calma meio corpo"

default expressao_valeria = "valeria cinica pirulito meio corpo"

default expressao_elara = "elara uniforme arrogante meio corpo"

default cliques_irritantes_lility = 0

default toques_valeria = 0

default toques_emilia = 0

default toques_elara = 0

default ressonancia_pre_diluviana = 0

default quebras_de_mascara = 0

default drenou_membro_gremio = False

default punicoes_gremio_ativas = 0

default bebeu_sangue_emilia = False

# ==============================================================================
# ENQUADRAMENTO INSTITUCIONAL & METADADOS ADULTOS (18+ COMPLIANCE)
# Todos os acadêmicos e pesquisadores de São Cipriano são maiores de idade comprovados.
# ==============================================================================
define IDADE_PERSONAGENS = {
    "victor": 20,
    "emilia": 20,
    "elara": 21,
    "valeria": 21,
    "lility": 21, # Idade aparente civil (Origem ancestral)
    "clara": 28,
    "ambrosio": 58,
}

default confianca_emilia = 0

default pacto_emilia_ativo = False

default safra_rara_valeria = False

default covil_sala_musica_ativo = False

default conhece_misterio_quadros = False
default investigou_desaparecidos_emilia = False
default quadro_banquete_resolvido = False
default cracha_aluno_desaparecido = False
default pigmento_alma_coletado = False
default pista_cofre_quadro = False
default entregou_cracha_emilia = False
default vendeu_pigmento_valeria = False

default vinculo_sangue_lility = 0

default vinculo_sangue_emilia = 0

default vinculo_sangue_valeria = 0

default vinculo_sangue_elara = 0

default rastro_olfativo_atual = None

default reagiu_olfato_turno = False

default encontro_agendado_heroina = None

default encontro_agendado_periodo = None

default encontro_agendado_local = None

default encontro_agendado_dia = 0

default encontro_concluido_hoje = False

default ruina_cain = 10
default doom_resto = 0.0
default doom_casos_abertos = {}
default doom_alertas = []

default status_escola = "normal"

default degrau_25_alertado = False

default degrau_50_alertado = False

default degrau_75_alertado = False

default sequelas_ativas = []

default dinheiro_jogador = 200

default dispositivo_choque = 1

default giz_protecao = 1

default sucata_eletronica = 1

default bolsa_sangue_filtrado = 1

default bolsa_sangue_adulterado = 0

default kit_curativo = 1

default dose_absinto = 0

default filtro_runico = 0

default gaze_consagrada = 0

default dose_estimulante = 0

# Novos produtos táticos e de sobrevivência do Mercado Negro
default cracha_falso = 0
default ampola_prata = 0
default tampao_hemostatico = 0
default incenso_mirra = 0
default sais_vigilia = 0
default amuleto_estanho = 0

# Presentes clandestinos e artigos de luxo (entregáveis às heroínas)
default presente_flores = 0
default presente_perfume = 0
default presente_colar = 0
default presente_roupa = 0
default presente_anel = 0
default presentes_entregues_heroinas = {}
default presenteou_heroina_hoje = {}
default valeria_usando_jaqueta_presente = False

# Flags de loja rotativa diária, travas de exploração e combate tático
default mercado_negro_vitrine_hoje = []
default mercado_negro_estoque_hoje = {}
default enfermaria_bolsas_hoje = 0
default enfermaria_kits_hoje = 0
default relatorio_entregue_hoje = False
default inspecao_elara_hoje = False
default usou_incenso_hoje = False
default usou_sais_hoje = False
default ampola_prata_ativa = False
default defesa_tampao_combate = 0
default extorquiu_combate_atual = False

# Sistema de Cobrança Periódica (Termo nº 112 / Taxa Compulsória de Alojamento)
default periodos_ate_cobranca = 6
default cobranca_vencida_pendente = False
default atrasos_taxa_consecutivos = 0
default cobrancas_pagas_total = 0

default efeito_estimulante_ativo = False

default esquiva_estimulante_ativa = False

default alimentou_lility_periodo = False

default oferendas_lility_entregues = 0

default confissoes_lility_realizadas = 0

default relatorio_gremio_obtido = False

default clima_diario_id = "calmaria_tensa"
default eh_dia_chuvoso = False
default chuva_forcada_evento = False

default clima_diario_nome = "Calmaria Ilusória"

default clima_diario_icone = "🕯️"

default clima_diario_desc = "Dia calmo na academia. Victor regenera +15 HP ao amanhecer."

default desbloqueou_banheiro_abandonado = False

default tem_passe_fada_verde = False

default fragmentos_chave_cripta = 0

default desbloqueou_cripta_cofre = False

default desbloqueou_mercado_negro = False
default mercado_negro_desbloqueado = False

default investigacoes_caldeiras = 0

default mercado_negro_aberto_hoje = True

init python:

    def sortear_abertura_mercado_negro():
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """Sorteia se o Mercado Negro abre no dia: 70% chance de aberto, 30% chance de fechado por precaução."""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        rolo = renpy.random.randint(1, 100)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        store.mercado_negro_aberto_hoje = (rolo > 30)

        return store.mercado_negro_aberto_hoje

    PRECOS_BASE_MERCADO_VALERIA = {
        "bolsa_sangue_filtrado": 120,
        "kit_curativo": 70,
        "bolsa_sangue_adulterado": 55,
        "giz_protecao": 65,
        "sucata_eletronica": 55,
        "dose_absinto": 115,
        "filtro_runico": 135,
        "gaze_consagrada": 155,
        "dispositivo_choque": 165,
        "dose_estimulante": 175,
        "cracha_falso": 160,
        "ampola_prata": 145,
        "tampao_hemostatico": 110,
        "incenso_mirra": 130,
        "sais_vigilia": 125,
        "amuleto_estanho": 195,
        "presente_flores": 85,
        "presente_perfume": 135,
        "presente_colar": 175,
        "presente_roupa": 220,
        "presente_anel": 260,
    }

    def _escolher_ponderado_vitrine(candidatos_pesos, excluir):
        disponiveis = [(item_id, peso) for item_id, peso in candidatos_pesos if item_id not in excluir and peso > 0]
        if not disponiveis:
            return None
        total = sum(p for _, p in disponiveis)
        alvo = renpy.random.uniform(0, total)
        acum = 0.0
        for item_id, peso in disponiveis:
            acum += peso
            if acum >= alvo:
                return item_id
        return disponiveis[-1][0]

    def sortear_vitrine_mercado_negro():
        """
        Gera a prateleira híbrida diária da Valéria:
        - Essenciais fixos limitados: 1x Bolsa Filtrada (+ Fiado) e 1x Kit Curativo
        - 5 slots rotativos únicos: 2x Suprimentos, 1x Contrabando Tático, 1x Avançado/Raro, 1x Presente de Luxo
        """
        clima = getattr(store, "clima_diario_id", "")
        dia = getattr(store, "dia_atual", 1)

        estoque = {
            "bolsa_sangue_filtrado": 1,
            "kit_curativo": 1,
        }
        usados = set()
        vitrine = []

        # Tier 1: 2 slots Comuns / Suprimentos
        pool_comum = [
            ("bolsa_sangue_adulterado", 3 if getattr(store, "fome_sangue", 100) < 45 else 2),
            ("giz_protecao", 3 if clima == "inspecao_gremio" else 2),
            ("sucata_eletronica", 2),
            ("dose_absinto", 1.5),
            ("tampao_hemostatico", 2),
        ]
        qtd_padrao_comum = {
            "bolsa_sangue_adulterado": 2,
            "giz_protecao": 2,
            "sucata_eletronica": 2,
            "dose_absinto": 1,
            "tampao_hemostatico": 1,
        }
        for _ in range(2):
            escolhido = _escolher_ponderado_vitrine(pool_comum, usados)
            if escolhido:
                usados.add(escolhido)
                estoque[escolhido] = qtd_padrao_comum.get(escolhido, 1)
                vitrine.append({
                    "id": escolhido,
                    "tier": "suprimento",
                    "mod_preco": 1.0,
                    "tag_lote": "",
                })

        # Tier 2: 1 slot Tático de Campo
        pool_tatico = [
            ("cracha_falso", 3 if clima == "inspecao_gremio" or getattr(store, "exposicao", 0) >= 45 else 2),
            ("ampola_prata", 3 if clima == "nevoa_carmesim" else 2),
            ("incenso_mirra", 2),
            ("sais_vigilia", 2),
            ("dispositivo_choque", 2),
        ]
        tatico = _escolher_ponderado_vitrine(pool_tatico, usados)
        if tatico:
            usados.add(tatico)
            estoque[tatico] = 1
            vitrine.append({
                "id": tatico,
                "tier": "tatico",
                "mod_preco": 1.0,
                "tag_lote": "",
            })

        # Tier 3: 1 slot Avançado / Promoção de Lote
        pool_avancado = [
            ("filtro_runico", 2),
            ("gaze_consagrada", 2),
            ("dose_estimulante", 2),
        ]
        if dia >= 5:
            pool_avancado.append(("amuleto_estanho", 2 if clima == "nevoa_carmesim" else 1.2))
        avancado = _escolher_ponderado_vitrine(pool_avancado, usados)
        if avancado:
            usados.add(avancado)
            estoque[avancado] = 1
            rolo_lote = renpy.random.randint(1, 100)
            mod_p = 1.0
            tag_l = ""
            if rolo_lote <= 20:
                mod_p = 0.80
                tag_l = "🏷️ LOTE -20%%"
            elif rolo_lote >= 86:
                mod_p = 1.15
                tag_l = "🔥 ESCASSEZ +15%%"
            vitrine.append({
                "id": avancado,
                "tier": "raro",
                "mod_preco": mod_p,
                "tag_lote": tag_l,
            })

        # Tier 4 (5º Slot): 1 Presente Clandestino & Luxo
        pool_presentes = [
            ("presente_flores", 3),
            ("presente_perfume", 2.5),
            ("presente_colar", 2.0),
            ("presente_roupa", 1.8),
            ("presente_anel", 1.6 if dia >= 4 else 0.7),
        ]
        presente_slot = _escolher_ponderado_vitrine(pool_presentes, usados)
        if presente_slot:
            usados.add(presente_slot)
            estoque[presente_slot] = 1
            vitrine.append({
                "id": presente_slot,
                "tier": "luxo",
                "mod_preco": 1.0,
                "tag_lote": "🎁 LUXO",
            })

        store.mercado_negro_vitrine_hoje = vitrine
        store.mercado_negro_estoque_hoje = estoque
        return vitrine

    def obter_multiplicador_valeria():
        mult = 1.0
        if getattr(store, "status_escola", "normal") == "inquietante":
            mult = 1.2
        elif getattr(store, "clima_diario_id", "") == "toque_recolher":
            mult = 0.8
        st_val = getattr(store, "status_valeria", None)
        if st_val and getattr(st_val, "afeto", 0) >= 6:
            mult *= 0.90
        return mult

    def calcular_preco_valeria(id_item, mod_slot=1.0):
        base = PRECOS_BASE_MERCADO_VALERIA.get(id_item, 100)
        return max(10, int(round(base * obter_multiplicador_valeria() * mod_slot)))

    def calcular_valor_cobranca_academica():
        if getattr(store, "divida_monitores", 0) > 0:
            return 135
        return 100

    def paciente_inadimplente_taxa():
        return any(s.get("id") == "taxa_inadimplente" for s in getattr(store, "sequelas_ativas", []))

    def obter_agio_enfermaria(valor_base):
        if paciente_inadimplente_taxa():
            return int(round(valor_base * 1.25))
        return int(valor_base)

default tem_partitura_runica = False

default tem_relicario_sangue = False

default tem_chave_contencao = False

default rumor_mulher_gigante = False

default rumor_loira_banheiro = False

default derrotou_loira_banheiro = False

default primeiro_transe_lility_realizado = False

default investigou_caderno_emilia_dia2 = False

default conheceu_valeria_caldeiras = False

default persistent.mem_loira_banheiro = False

default derrotou_hachishaku = False

default ritual_corte_vinculo_desbloqueado = False

default caso_lote_necrotico_resolvido = False

default caso_partitura_resolvido = False

default caso_inquerito_resolvido = False

default protegeu_colega_dia1 = False

default investigou_carteira_vazia = False

default investigou_lote_contaminado = False

default viu_partitura_lility = False

default alianca_emilia_valeria = False

default ouviu_acordo_elara_valeria = False

default emilia_conhece_a_verdade = False

default elara_subjugada_no_cofre = False

default lility_percebeu_compaixao = False

default persistent.ciclos_mortes = 0

default persistent.eco_conhece_senha_cofre = False

default persistent.eco_sabe_identidade_lility = False

default persistent.eco_aviso_sangue_adulterado = False

default nome_inimigo = "Inimigo"

default img_inimigo_base = ""

default img_inimigo_ataque = ""
default img_inimigo_derrota = ""

default hp_inimigo = 50

default hp_inimigo_max = 50

default dano_inimigo = 15

default tempo_reacao = 5.0

default tipo_sangue_inimigo = "gremio"

default combate_historia_continua = False

screen hud_sobrevivencia():
    zorder 120

    # ==========================================================================
    # ANDAR 1: BARRA TÁTICA MÁSTER DE SOBREVIVÊNCIA (1920x48)
    # ==========================================================================
    frame:
        xalign 0.5
        yalign 0.0
        xsize 1920
        ysize 48
        background (Transform("gui/hud_superior/barra_top_1.png", fit="fill") if renpy.loadable("gui/hud_superior/barra_top_1.png") else Solid("#0a0a0ff4"))
        padding (16, 5, 16, 5)

        hbox:
            xfill True
            yalign 0.5
            spacing 14

            # 1. Calendário e Período
            $ _limite_max = getattr(store, "limite_dias", 21)
            text "🏆 [periodo!u] (Dia [dia_atual]/[_limite_max])":
                size 16
                bold True
                color "#d4af37"
                yalign 0.5
                outlines [(1, "#000000ee", 0, 0)]

            # 2. Indicador Dinâmico de Zona
            if getattr(store, "local_atual", "") == "dormitorio":
                frame:
                    background "#002244dd"
                    padding (6, 2)
                    yalign 0.5
                    text "🛡️ REFÚGIO" size 13 bold True color "#33ccff"
            elif periodo == "Noite":
                frame:
                    background "#550005dd"
                    padding (6, 2)
                    yalign 0.5
                    text "🔴 ZONA VERMELHA" size 13 bold True color "#ff5555"
            elif periodo == "Tarde":
                frame:
                    background "#443300dd"
                    padding (6, 2)
                    yalign 0.5
                    text "🟡 ZONA AMARELA" size 13 bold True color "#ffcc00"
            else:
                frame:
                    background "#002244dd"
                    padding (6, 2)
                    yalign 0.5
                    text "🔵 ZONA AZUL" size 13 bold True color "#33aaff"

            # 3. Vida (HP)
            hbox:
                spacing 5
                yalign 0.5
                text "❤️" size 16 yalign 0.5
                bar:
                    value hp_jogador
                    range hp_jogador_max
                    xsize 88
                    ysize 12
                    yalign 0.5
                    left_bar Solid("#22cc55")
                    right_bar Solid("#1a221a")
                text "[hp_jogador]/[hp_jogador_max]" size 16 color "#e2e8f0" yalign 0.5

            # 4. Sede de Sangue (Fome)
            hbox:
                spacing 5
                yalign 0.5
                text "🩸" size 16 yalign 0.5
                bar:
                    value fome_sangue
                    range 100
                    xsize 88
                    ysize 12
                    yalign 0.5
                    left_bar Solid("#cc1122" if fome_sangue >= 20 else "#ff0000")
                    right_bar Solid("#220a0d")
                text "[fome_sangue]%" size 16 color ("#ff4444" if fome_sangue < 20 else "#e2e8f0") yalign 0.5 bold (fome_sangue < 20)

            if 0 < fome_sangue < 20:
                text "[[⚠️ SEDE CRÍTICA]]" size 14 color "#ff3344" bold True yalign 0.5

            # 5. Métricas Psicológicas e Carteira
            text "🧠 [humanidade]" size 16 color "#88ccff" yalign 0.5 tooltip "Humanidade"
            text "🎭 [exposicao]%" size 16 color "#cc88ff" yalign 0.5 tooltip "Exposição"
            text "💰 $[dinheiro_jogador]" size 16 color "#66ff66" yalign 0.5 tooltip "Carteira"

            # 6. Taxa Acadêmica
            if dia_atual >= 3:
                $ _v_cob_hud = calcular_valor_cobranca_academica()
                if paciente_inadimplente_taxa():
                    text "⚠️ INADIMPLENTE" size 14 color "#ff3344" bold True yalign 0.5
                else:
                    text "⏳ Taxa: [periodos_ate_cobranca]p ($[_v_cob_hud])":
                        size 14
                        color ("#ff5555" if dinheiro_jogador < _v_cob_hud and periodos_ate_cobranca <= 2 else ("#ffcc00" if periodos_ate_cobranca <= 2 else "#cccccc"))
                        bold True
                        yalign 0.5

            # 7. DOOM (Ruína de Cain)
            text "⚡ DOOM: [ruina_cain]%":
                size 16
                bold True
                color ("#ff1111" if ruina_cain >= 75 else ("#ff8800" if ruina_cain >= 50 else ("#ffcc00" if ruina_cain >= 25 else "#88ccff")))
                yalign 0.5
                tooltip "DOOM: Deterioração"

            # 8. Clima Diário
            text "[clima_diario_icone] [clima_diario_nome]":
                size 15
                color "#ffd700"
                bold True
                yalign 0.5
                tooltip clima_diario_desc

            # 9. Debug (se ativo)
            if config.developer:
                textbutton "🛠️ DEBUG":
                    action Show("painel_debug_interno")
                    text_size 13
                    text_color "#00ff88"
                    text_hover_color "#ffffff"
                    yalign 0.5

    # ==========================================================================
    # ANDAR 2: ARCO SUSPENSO DE ATALHOS GÓTICOS (680x42 em ypos 46)
    # ==========================================================================
    frame:
        xalign 0.5
        ypos 46
        xsize 680
        ysize 42
        background (Transform("gui/hud_superior/botoes_atalho_2.png", fit="fill") if renpy.loadable("gui/hud_superior/botoes_atalho_2.png") else Solid("#0c0f18ee"))
        padding (8, 2)

        hbox:
            align (0.5, 0.5)
            spacing 24

            textbutton "👤 STATUS":
                action ShowMenu("central_tatica_feniks", "status")
                text_size 15
                text_bold True
                text_color "#60a5fa"
                text_hover_color "#ffffff"
                yalign 0.5

            textbutton "📋 CASOS":
                action ShowMenu("quadro_misterios_woh")
                text_size 15
                text_bold True
                text_color "#f87171"
                text_hover_color "#ffffff"
                yalign 0.5

            textbutton "🎒 ITENS":
                action ShowMenu("central_tatica_feniks", "inventario")
                text_size 15
                text_bold True
                text_color "#fbbf24"
                text_hover_color "#ffffff"
                yalign 0.5

            textbutton "📜 DÍVIDAS":
                action ShowMenu("central_tatica_feniks", "dividas")
                text_size 15
                text_bold True
                text_color "#c084fc"
                text_hover_color "#ffffff"
                yalign 0.5

            if modo_exploracao_livre:
                textbutton "🗺️ MAPA":
                    action Show("mapa_tatico_escola")
                    text_size 15
                    text_bold True
                    text_color "#34d399"
                    text_hover_color "#ffffff"
                    yalign 0.5

init python:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    import random
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def obter_sprite_victor(modo="padrao"):
        """
        Retorna o sprite de Victor de acordo com seu estado de Sede, Fase de Humanidade e Expressao.
        - Fome Critica (<20) ou Frenesi: retorna o sprite de frenesi da fase atual de Victor.
        - FASE 3 (Humanidade < 35): Predador Vampírico / Humano Decadente.
        - FASE 2 (Humanidade 35-64): Lacaio Desgastado / Humano em transição.
        - FASE 1 (Humanidade >= 65): Monitor Bolsista / Uniforme Escolar intacto.
        """
        m = modo.lower().strip() if modo else "padrao"

        # Trava de Frenesi / Sede Crítica (ou requisição explícita de frenesi/furia)
        if store.fome_sangue < 20 or getattr(store, "em_frenesi", False) or m in ["frenesi", "furia", "frenetico"]:
            if "fase3" in m or store.humanidade < 35:
                return "victor fase3 frenesi"
            elif "fase2" in m or store.humanidade < 65:
                return "victor fase2 frenesi"
            else:
                return "victor fase1 frenesi"

        # Suporte para chamadas explicitas de fase
        if "fase3" in m:
            if "frenesi" in m or "furia" in m: return "victor fase3 frenesi"
            if "cansado" in m: return "victor fase3 predador cansado"
            if "chocado" in m: return "victor fase3 predador chocado"
            if "neutro" in m: return "victor fase3 predador neutro"
            if "triste" in m: return "victor fase3 predador triste"
            if "frustrado" in m: return "victor fase3 humano frustrado"
            if "irritado" in m: return "victor fase3 humano irritado"
            if "rindo" in m: return "victor fase3 predador rindo"
            if "postura" in m: return "victor fase3 predador postura"
            if "busto" in m: return "victor fase3 predador busto"
            return "victor fase3 predador serio"

        if "fase2" in m:
            if "frenesi" in m or "furia" in m: return "victor fase2 frenesi"
            if "assustado" in m: return "victor fase2 humano assustado"
            if "cansado" in m: return "victor fase2 humano cansado"
            if "chocado" in m: return "victor fase2 humano chocado"
            if "melancolico" in m: return "victor fase2 humano melancolico"
            if "pretensioso" in m or "olhando_cima" in m: return "victor fase2 humano olhando de cima pretensioso"
            if "presuncoso" in m: return "victor fase2 humano sorriso presuncoso"
            if "sorrindo leve" in m or "sorrindo_leve" in m: return "victor fase2 humano sorrindo leve"
            if "sorrindo" in m: return "victor fase2 humano sorrindo"
            if "surpreso" in m: return "victor fase2 humano surpreso"
            return "victor fase2 humano"

        if "fase1" in m:
            if "frenesi" in m or "furia" in m: return "victor fase1 frenesi"

        # Roteamento dinamico baseado em Humanidade:
        # FASE 3: Humanidade < 35 (Predador / Fim da Linha)
        if store.humanidade < 35:
            if m in ["rindo", "sorrindo", "charmoso", "debochado", "cinico", "riso"]:
                return "victor fase3 predador rindo"
            elif m in ["postura", "combate", "ferido", "ferido_combate", "ferido_determinado", "ferido_sorriso", "acao"]:
                return "victor fase3 predador postura"
            elif m in ["busto", "corpo"]:
                return "victor fase3 predador busto"
            elif m in ["cansado", "exausto", "esgotado"]:
                return "victor fase3 predador cansado"
            elif m in ["chocado", "surpreso", "espanto"]:
                return "victor fase3 predador chocado"
            elif m in ["triste", "melancolico", "abatido", "cabisbaixo"]:
                return "victor fase3 predador triste"
            elif m in ["frustrado", "derrotado"]:
                return "victor fase3 humano frustrado"
            elif m in ["irritado", "furioso", "bravo"]:
                return "victor fase3 humano irritado"
            elif m in ["neutro", "calmo"]:
                return "victor fase3 predador neutro"
            else:
                return "victor fase3 predador serio"

        # FASE 2: Humanidade 35..64 (Lacaio Desgastado / Humano Decadente)
        elif store.humanidade < 65:
            if m in ["assustado", "medo", "pavor", "panico"]:
                return "victor fase2 humano assustado"
            elif m in ["cansado", "exausto", "esgotado", "fadiga"]:
                return "victor fase2 humano cansado"
            elif m in ["chocado", "surpreso", "espanto"]:
                return "victor fase2 humano chocado"
            elif m in ["melancolico", "triste", "cabisbaixo", "abatido"]:
                return "victor fase2 humano melancolico"
            elif m in ["olhando_cima", "pretensioso", "desdenho", "superior"]:
                return "victor fase2 humano olhando de cima pretensioso"
            elif m in ["sorrindo", "alegre", "divertido"]:
                return "victor fase2 humano sorrindo"
            elif m in ["presuncoso", "sorriso_presuncoso", "ironico", "cinico", "debochado"]:
                return "victor fase2 humano sorriso presuncoso"
            elif m in ["sorrindo_leve", "amigavel", "gentil", "sorrindo leve"]:
                return "victor fase2 humano sorrindo leve"
            elif m in ["surpreso"]:
                return "victor fase2 humano surpreso"
            elif m in ["neutro", "padrao", "serio", "calmo"]:
                return "victor fase2 humano"
            # Fallback para expressoes com suporte apenas em uniforme
            elif m in ["falando", "dialogo", "explicando"]:
                return "victor fase1 uniforme falando"
            elif m in ["pensando", "pensativo", "reflexivo", "analitico"]:
                return "victor fase1 uniforme pensando"
            elif m in ["confiante", "seguro"]:
                return "victor fase1 uniforme confiante"
            elif m in ["sem_jeito", "sem jeito", "timido", "envergonhado"]:
                return "victor fase1 uniforme sem jeito"
            elif m in ["constrangido", "embaracado", "hesitante"]:
                return "victor fase1 uniforme constrangido"
            elif m in ["charmoso", "sedutor", "flerte"]:
                return "victor fase1 uniforme charmoso"
            elif m in ["ferido_combate", "ferido combate", "combate"]:
                return "victor fase1 uniforme ferido combate"
            elif m in ["ferido_determinado", "ferido determinado", "determinado", "ferido"]:
                return "victor fase1 uniforme ferido determinado"
            elif m in ["ferido_sorriso", "ferido sorriso", "ironico_ferido"]:
                return "victor fase1 uniforme ferido sorriso"
            else:
                return "victor fase2 humano"

        # FASE 1: Humanidade >= 65 (Monitor Bolsista / Uniforme Escolar)
        else:
            if m in ["furioso", "furia", "raiva"]:
                return "victor fase1 uniforme furioso"
            elif m in ["irritado", "irritado_serio", "irritado serio", "bravo"]:
                return "victor fase1 uniforme irritado serio"
            elif m in ["melancolico", "triste", "cabisbaixo", "abatido"]:
                return "victor fase1 uniforme melancolico"
            elif m in ["sereno", "paz", "tranquilo"]:
                return "victor fase1 uniforme sereno"
            elif m in ["sorriso_canto", "sorriso de canto"]:
                return "victor fase1 uniforme sorriso de canto"
            elif m in ["sorriso_malicioso", "sorriso malicioso", "malicioso"]:
                return "victor fase1 uniforme sorriso malicioso"
            elif m in ["aterrorizado", "panico", "pavor"]:
                return "victor fase1 uniforme aterrorizado"
            elif m in ["desconfiado", "suspeito", "desconfianca"]:
                return "victor fase1 uniforme desconfiado"
            elif m in ["desgosto", "nojo", "repulsa"]:
                return "victor fase1 uniforme desgosto"
            elif m in ["entediado", "tedio"]:
                return "victor fase1 uniforme entediado"
            elif m in ["estranhando", "confuso", "estranho"]:
                return "victor fase1 uniforme estranhando"
            elif m in ["exausto", "cansado", "esgotado"]:
                return "victor fase1 uniforme exausto"
            elif m in ["pensando", "pensativo", "reflexivo", "analitico"]:
                return "victor fase1 uniforme pensando"
            elif m in ["confiante", "seguro"]:
                return "victor fase1 uniforme confiante"
            elif m in ["sorrindo", "amigavel", "gentil", "alegre"]:
                return "victor fase1 uniforme sorrindo"
            elif m in ["falando", "dialogo", "explicando"]:
                return "victor fase1 uniforme falando"
            elif m in ["surpreso", "chocado", "assustado", "espanto"]:
                return "victor fase1 uniforme surpreso"
            elif m in ["sem_jeito", "sem jeito", "timido", "envergonhado"]:
                return "victor fase1 uniforme sem jeito"
            elif m in ["constrangido", "embaracado", "hesitante"]:
                return "victor fase1 uniforme constrangido"
            elif m in ["charmoso", "sedutor", "flerte"]:
                return "victor fase1 uniforme charmoso"
            elif m in ["ferido_combate", "ferido combate", "combate"]:
                return "victor fase1 uniforme ferido combate"
            elif m in ["ferido_determinado", "ferido determinado", "determinado", "ferido"]:
                return "victor fase1 uniforme ferido determinado"
            elif m in ["ferido_sorriso", "ferido sorriso", "ironico_ferido"]:
                return "victor fase1 uniforme ferido sorriso"
            elif m in ["neutro", "calmo", "padrao"]:
                return "victor fase1 uniforme neutro"
            elif m in ["serio", "grave", "firme"]:
                return "victor fase1 uniforme serio"
            else:
                return "victor fase1 uniforme serio"

    def obter_descricao_fase_victor():
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if store.fome_sangue < 20:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            return "FRENESI DE GHOUL (Sede Crítica! Controle mental à beira do colapso)"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        elif store.humanidade >= 65:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            return "FASE 1 — Estudante Humano (Olhar são, batimentos estáveis e empatia preservada)"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        elif store.humanidade >= 35:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            return "FASE 2 — Lacaio Desgastado (Olheiras profundas, pele fria e sede constante)"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        else:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            return "FASE 3 — Predador Carmesim (Instinto monstruoso dominante, presas alongadas)"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def sortear_posicoes_heroinas():
        store.tomou_cha_emilia_periodo = False
        # Lility: O Grilhão proíbe áreas do Conselho (salao_gremio, patio_fonte), exterior (rua_portao) e Subsolo (catacumbas/caldeiras).
        # De Manhã/Tarde fica na Sala de Música; à Noite pode circular furtivamente pelas áreas periféricas/pontos cegos da superfície.
        if store.periodo == "Noite" and random.randint(1, 100) <= 50:
            store.loc_mestra = random.choice(["sala_musica", "patio_arvore", "biblioteca", "portoes_praca", "dormitorio"])
        elif getattr(store, "clima_diario_id", "") in ["chuva_vitrais", "chuva", "chuva_acida", "nevoeiro_sangue"] and random.randint(1, 100) <= 30:
            # Em dias de tempestade pesada ou névoa densa, Lility consegue transitar pelas sombras até o dormitório
            store.loc_mestra = random.choice(["sala_musica", "dormitorio"])
        else:
            store.loc_mestra = "sala_musica"

        # Emília alterna entre Biblioteca, Dormitório/Pátio e Catacumbas
        if store.periodo == "Manhã":
            store.loc_emilia = random.choice(["biblioteca", "dormitorio"])
        elif store.periodo == "Tarde":
            store.loc_emilia = random.choice(["biblioteca", "salao_gremio"])
        else:
            store.loc_emilia = random.choice(["biblioteca", "catacumbas", "patio_arvore", "dormitorio"])

        # Elara alterna entre o Gabinete do Grêmio e inspeções na Biblioteca/Catacumbas
        if store.periodo == "Noite":
            store.loc_elara = random.choice(["salao_gremio", "catacumbas"])
        else:
            store.loc_elara = random.choice(["salao_gremio", "biblioteca"])

        # Valéria alterna entre as Caldeiras e o Bar da Fada Verde
        store.loc_valeria = random.choice(["caldeiras", "bar_fada_verde"])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def obter_bark_transicao_persona():
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        doom = getattr(store, "ruina_cain", 10)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        d = getattr(store, "dia_atual", 1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        p = getattr(store, "periodo", "Manhã")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if doom < 25:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            barks = [

                f"Dia {d} ({p}). Os estudantes passam rindo pelos corredores... Sem desconfiar do perigo invisível que os cerca.",

                f"Dia {d} ({p}). Ainda sinto o gosto de mirra e cinzas na boca. Preciso me manter discreto enquanto investigo.",

                f"Dia {d} ({p}). A rotina de calouro é uma farsa conveniente. Quanto menos me notarem, melhor."

            ]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        elif doom < 50:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            barks = [

                f"Dia {d} ({p}). O ar do colégio parece mais pesado. Uma presença silenciosa perturba os alicerces.",

                f"Dia {d} ({p}). O cheiro de sangue nos corredores parece mais nítido a cada pôr do sol.",

                f"Dia {d} ({p}). As patrulhas do Grêmio estão mais agressivas. A Máscara está começando a rachar."

            ]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        elif doom < 75:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            barks = [

                f"Dia {d} ({p}). A deterioração do campus é visível. O solo nas profundezas pulsa como um coração doente.",

                f"Dia {d} ({p}). A Inquisição e o Conselho estão farejando os mesmos cantos escuros. Algo colossal está se agitando.",

                f"Dia {d} ({p}). Minha sede não perdoa distrações. Cada passo nas caldeiras ou na biblioteca precisa valer a pena."

            ]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        else:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            barks = [

                f"Dia {d} ({p}). O colapso se aproxima (DOOM {doom}%). As sombras sob a escola estão prestes a se libertar.",

                f"Dia {d} ({p}). O céu tem uma mancha carmesim. O que eu não resolver agora, a ruína total resolverá.",

                f"Dia {d} ({p}). O Grilhão queima no peito. A tempestade e a entidade nas profundezas estão despertando."

            ]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        return random.choice(barks)

init python:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    renpy.music.register_channel("ambient", mixer="sfx", loop=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    import os
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    for caminho_relativo in renpy.list_files():
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if caminho_relativo.startswith("images/") and caminho_relativo.lower().endswith((".mp4", ".webm", ".ogv")):
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            nome_cena = os.path.splitext(os.path.basename(caminho_relativo))[0]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            chave_imagem = tuple(nome_cena.split())
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            if "cenas/" in caminho_relativo.lower() or nome_cena.lower().startswith("cena "):
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                renpy.image(

                    chave_imagem,

                    Fixed(

                        Solid("#000000"),

                        Movie(play=caminho_relativo, size=(1920, 1080), loop=False, image=Solid("#000000")),

                        fit_first=False,

                        xsize=1920,

                        ysize=1080

                    )

                )
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            else:
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                renpy.image(chave_imagem, Movie(play=caminho_relativo, size=(1920, 1080), loop=True))

image emilia uniforme seria triste meio corpo = "images/emilia/emilia triste encarando.webp"

image emilia combate espada katana = "images/emilia/corpo inteiro apenas para batalha/emilia exorcista sobretudo corpo inteiro.webp"

# ==============================================================================
# SPRITES & EXPRESSÕES DE LILITY / LYRA VON BLUT (PIPELINE WEBP 92)
# ==============================================================================
image lility gelida = "images/lility/lility meio corpo gelida.webp"
image lility meio corpo gelida = "images/lility/lility meio corpo gelida.webp"
image lility mal humorada = "images/lility/lility meio corpo mal humorada.webp"
image lility meio corpo mal humorada = "images/lility/lility meio corpo mal humorada.webp"
image lility maravilhada = "images/lility/lility meio corpo maravilhada.webp"
image lility meio corpo maravilhada = "images/lility/lility meio corpo maravilhada.webp"
image lility melancolica = "images/lility/lility meio corpo melancolica.webp"
image lility meio corpo melancolica = "images/lility/lility meio corpo melancolica.webp"
image lility muito alegre = "images/lility/lility meio corpo muito alegre e vibrante.webp"
image lility vibrante = "images/lility/lility meio corpo muito alegre e vibrante.webp"
image lility meio corpo muito alegre e vibrante = "images/lility/lility meio corpo muito alegre e vibrante.webp"
image lility sorriso bondoso = "images/lility/lility meio corpo sorriso bondoso.webp"
image lility meio corpo sorriso bondoso = "images/lility/lility meio corpo sorriso bondoso.webp"
image lility sorriso malicioso = "images/lility/lility meio corpo sorriso malicioso.webp"
image lility meio corpo sorriso malicioso = "images/lility/lility meio corpo sorriso malicioso.webp"
image lility vergonhosa = "images/lility/lility meio corpo vergonhosa.webp"
image lility meio corpo vergonhosa = "images/lility/lility meio corpo vergonhosa.webp"
image lility apreensiva = "images/lility/lility meio corpo apreensiva.webp"
image lility meio corpo apreensiva = "images/lility/lility meio corpo apreensiva.webp"
image lility chocada = "images/lility/lility meio corpo chocada.webp"
image lility meio corpo chocada = "images/lility/lility meio corpo chocada.webp"
image lility chorando = "images/lility/lility meio corpo chorando.webp"
image lility meio corpo chorando = "images/lility/lility meio corpo chorando.webp"
image lility confusa = "images/lility/lility meio corpo confusa.webp"
image lility meio corpo confusa = "images/lility/lility meio corpo confusa.webp"
image lility desconfiada = "images/lility/lility meio corpo desconfiada.webp"
image lility meio corpo desconfiada = "images/lility/lility meio corpo desconfiada.webp"
image lility desdenhando = "images/lility/lility meio corpo desdenhando.webp"
image lility meio corpo desdenhando = "images/lility/lility meio corpo desdenhando.webp"
image lility enojada = "images/lility/lility meio corpo enojada.webp"
image lility meio corpo enojada = "images/lility/lility meio corpo enojada.webp"
image lility entediada = "images/lility/lility meio corpo entediada.webp"
image lility meio corpo entediada = "images/lility/lility meio corpo entediada.webp"
image lility exausta = "images/lility/lility meio corpo exausta.webp"
image lility meio corpo exausta = "images/lility/lility meio corpo exausta.webp"
image lility furiosa = "images/lility/lility meio corpo furiosa.webp"
image lility meio corpo furiosa = "images/lility/lility meio corpo furiosa.webp"

image lility olhando com confianca = "images/lility/lility olhando com confianca.webp"
image lility olhando com rosto feliz = "images/lility/lility olhando com confianca.webp"
image lility confiante = "images/lility/lility olhando com confianca.webp"

# Aliases de compatibilidade para sprites antigos descontinuados
image lility superior olhar cima meio corpo = "images/lility/lility meio corpo desdenhando.webp"
image lility superior sarcasmo meio corpo = "images/lility/lility meio corpo desdenhando.webp"
image lility ironica sorriso sarcasmo meio corpo = "images/lility/lility meio corpo sorriso malicioso.webp"
image lility surpresa chocada meio corpo = "images/lility/lility meio corpo chocada.webp"
image lility brava encarando com intensidade = "images/lility/lility meio corpo furiosa.webp"

image lility seria = "images/lility/lility olhando seria.webp"
image lility olhando seria = "images/lility/lility olhando seria.webp"

image lility triste olhando para baixo = "images/lility/lility triste olhando para baixo meio corpo.webp"
image lility triste = "images/lility/lility triste olhando para baixo meio corpo.webp"
image lility triste olhando para baixo meio corpo = "images/lility/lility triste olhando para baixo meio corpo.webp"

image lility triste olhando para baixo corpo inteiro = "images/lility/corpo inteiro/lility triste olhando para baixo.webp"

image lility cena dormindo = Transform("images/cenas/cena lility dormindo na sala de musica de manha.webp", xysize=(1920, 1080), fit="cover")

image cena nora caneta = Transform("images/cenas/cenas de  victor com nora/cena de nora pedindo uma caneta a victor no corredor de manha.webp", xysize=(1920, 1080), fit="cover")
image cena de nora pedindo uma caneta a victor no corredor de manha = "cena nora caneta"

image cena lility provocando = Transform("images/cenas/cena de lility provocando victor na sala de musica de noite.webp", xysize=(1920, 1080), fit="cover")

image cena lility troca sangue = Transform("images/cenas/cena de lility provocando e insinuando a victor na sala de musica de noite antes de realizar a troca de sangue.webp", xysize=(1920, 1080), fit="cover")
image cena de lility provocando e insinuando a victor na sala de musica de noite antes de realizar a troca de sangue = "cena lility troca sangue"

image lility cena piano sala musica = Movie(play="images/Background Wallpapers motions/bg animado sala musica piano noite.webm", size=(1920, 1080), loop=True)

image bg animado inicio sonho premonicao = Fixed(

    Solid("#000000"),

    Movie(play="images/cenas/cenas de victor ao acordar/cena inicio sonho premonicao ceu ferida.webm", size=(1920, 1080), loop=False, image=Solid("#000000")),

    fit_first=False,

    xsize=1920,

    ysize=1080

)

image cena inicio sonho premonicao = Movie(play="images/cenas/cenas de victor ao acordar/cena inicio sonho premonicao ceu ferida.webm", size=(1920, 1080), loop=True)

image cena flashback mentor traicao = Transform("images/cenas/cena flashback mentor aperto mao traicao victor.webp", xysize=(1920, 1080), fit="cover")

image cena contraste castas patio = Movie(play="images/Background Wallpapers motions/bg animado patio arvore entardecer dourado.webm", size=(1920, 1080), loop=True)

image cena deposito extorsao teo = Transform("images/cenas/cena deposito anexo frasco azul extorsao teo.webp", xysize=(1920, 1080), fit="cover")

image cena nora parede loucura = Transform("images/cenas/cenas de  victor com nora/cena parede loucura nora escrevendo.webp", xysize=(1920, 1080), fit="cover")

image cena nora parede encarando = Transform("images/cenas/cenas de  victor com nora/cena parede loucura nora encarando.webp", xysize=(1920, 1080), fit="cover")

image cena animada memoria diluvio lility dia 2 noite = Fixed(

    Solid("#000000"),

    Movie(play="images/cenas/passado lility/cena memoria diluvio lility dia 2 noite video.webm", size=(1920, 1080), loop=False, image=Solid("#000000")),

    fit_first=False,

    xsize=1920,

    ysize=1080

)

image cena memoria diluvio lility dia 2 noite video = Movie(play="images/cenas/passado lility/cena memoria diluvio lility dia 2 noite video.webm", size=(1920, 1080), loop=True)

image cena lility memoria diluvio = Transform("images/cenas/passado lility/cena memoria diluvio lility dia 2 noite.webp", xysize=(1920, 1080), fit="cover")

image cena espelho loira banheiro 1 = Transform("images/cenas/O Halo de Batom no Espelho Dia 2 Noite cena 1.webp", xysize=(1920, 1080), fit="cover")

image cena espelho loira banheiro 2 = Transform("images/cenas/O Halo de Batom no Espelho Dia 2 Noite cena 2.webp", xysize=(1920, 1080), fit="cover")

image cena halo batom espelho 1 = Transform("images/cenas/O Halo de Batom no Espelho Dia 2 Noite cena 1.webp", xysize=(1920, 1080), fit="cover")

image cena halo batom espelho 2 = Transform("images/cenas/O Halo de Batom no Espelho Dia 2 Noite cena 2.webp", xysize=(1920, 1080), fit="cover")

image cena transe emilia = Transform("images/cenas/transe de sangue com emilia.webp", xysize=(1920, 1080), fit="cover")

image cena transe lility 1 = Transform("images/cenas/cenas de transe de sangue lility/transe de sangue com lility 1.webp", xysize=(1920, 1080), fit="cover")

image cena transe lility 2 = Transform("images/cenas/cenas de transe de sangue lility/transe de sangue lility 2.webp", xysize=(1920, 1080), fit="cover")

image cena transe lility 3 = Transform("images/cenas/cenas de transe de sangue lility/transe de sangue lility 3.webp", xysize=(1920, 1080), fit="cover")

image cena transe lility 4 = Transform("images/cenas/cenas de transe de sangue lility/transe de sangue lility 4.webp", xysize=(1920, 1080), fit="cover")

image cena victor pesadelo 1 = Transform("images/cenas/cenas de victor ao acordar/victor apos pesadelo com sonho de lility cena 1.webp", xysize=(1920, 1080), fit="cover")

image cena victor pesadelo 2 = Transform("images/cenas/cenas de victor ao acordar/victor apos pesadelo com sonho de lility cena 2.webp", xysize=(1920, 1080), fit="cover")

image cena victor trem bala = Transform("images/cenas/trem viagem victor/victor observando a atraves da janela do trem.webp", xysize=(1920, 1080), fit="cover")

image cena victor portoes academia = Transform("images/cenas/victor ansioso observando a escola pela primeira vez.webp", xysize=(1920, 1080), fit="cover")

image victor observando a atraves da janela do trem = Transform("images/cenas/trem viagem victor/victor observando a atraves da janela do trem.webp", xysize=(1920, 1080), fit="cover")

image victor ansioso observando a escola pela primeira vez = Transform("images/cenas/victor ansioso observando a escola pela primeira vez.webp", xysize=(1920, 1080), fit="cover")

image cena quase morte nora = Transform("images/cenas/cenas de  victor com nora/cena da quase morte de victor pelas maos de nora.webp", xysize=(1920, 1080), fit="cover")

image cena quase morte encontra lility = Transform("images/cenas/cena da quase morte de victor pelas maos de nora e encontra lility.webp", xysize=(1920, 1080), fit="cover")

image cena quase morte lility ajoelha = Transform("images/cenas/cena da quase morte de victor pelas maos de nora e lility se aproxima e ajoelha.webp", xysize=(1920, 1080), fit="cover")

image cena quase morte lility proposta sangue = Transform("images/cenas/cena da quase morte de victor pelas maos de nora e lility entao faz a proposta de sangue com victor.webp", xysize=(1920, 1080), fit="cover")

image cena da quase morte de victor pelas maos de nora = Transform("images/cenas/cenas de  victor com nora/cena da quase morte de victor pelas maos de nora.webp", xysize=(1920, 1080), fit="cover")

image cena da quase morte de victor pelas maos de nora e encontra lility = Transform("images/cenas/cena da quase morte de victor pelas maos de nora e encontra lility.webp", xysize=(1920, 1080), fit="cover")

image cena da quase morte de victor pelas maos de nora e lility se aproxima e ajoelha = Transform("images/cenas/cena da quase morte de victor pelas maos de nora e lility se aproxima e ajoelha.webp", xysize=(1920, 1080), fit="cover")

image cena da quase morte de victor pelas maos de nora e lility entao faz a proposta de sangue com victor = Transform("images/cenas/cena da quase morte de victor pelas maos de nora e lility entao faz a proposta de sangue com victor.webp", xysize=(1920, 1080), fit="cover")

image cena passado victor 01 = Transform("images/cenas/passado de victor/victor ve sua amiga sendo molestada pelo professor cena 1.jpg", xysize=(1920, 1080), fit="cover")
image cena passado victor 02 = Transform("images/cenas/passado de victor/victor se aproxima do professor e o toca no ombro cena 2.jpg", xysize=(1920, 1080), fit="cover")
image cena passado victor 03 = Transform("images/cenas/passado de victor/victor da um soco na face do professor para proteger sua amiga cena 3.jpg", xysize=(1920, 1080), fit="cover")
image cena passado victor 04 = Transform("images/cenas/passado de victor/victor observa o odio do professor o  encarando e ligando para a policia cena 4.jpg", xysize=(1920, 1080), fit="cover")
image cena passado victor 05 = Transform("images/cenas/passado de victor/a policia chega e prende no lugar pelo chamado do professor cena 5.jpg", xysize=(1920, 1080), fit="cover")
image cena passado victor 06 = Transform("images/cenas/passado de victor/victor e preso pela policia pela acusacao do professor cena 6.jpg", xysize=(1920, 1080), fit="cover")
image cena passado victor 07 = Transform("images/cenas/passado de victor/todos estao na cabine do  delegado cena 7.jpg", xysize=(1920, 1080), fit="cover")
image cena passado victor 08 = Transform("images/cenas/passado de victor/o professor eo delagado apertao a mao e victor fica shocado cena 8.jpg", xysize=(1920, 1080), fit="cover")
image cena passado victor 09 = Transform("images/cenas/passado de victor/victor assina a sua acusacao por pressao cena 9.jpg", xysize=(1920, 1080), fit="cover")
image cena passado victor 10 = Transform("images/cenas/passado de victor/victor assinando sua acusacao perplexo e em shock cena 10.jpg", xysize=(1920, 1080), fit="cover")
image cena passado victor 11 = Transform("images/cenas/passado de victor/victor expulso e pegando um trem  cena 11.jpg", xysize=(1920, 1080), fit="cover")

image cena victor trem carta janela = Transform("images/cenas/trem viagem victor/victor observando a atraves da janela do trem com a carta de recomendacao.jpg", xysize=(1920, 1080), fit="cover")
image cena victor trem lendo carta = Transform("images/cenas/trem viagem victor/victor observando a a carta dentro do trem.jpg", xysize=(1920, 1080), fit="cover")

image cena elara conversa manha = Transform("images/cenas/elara e victor conversando de manha.jpg", xysize=(1920, 1080), fit="cover")
image cena elara mostra pingente nora = Transform("images/cenas/elara mostra pingente 31 de nora.jpg", xysize=(1920, 1080), fit="cover")

image cena lility piano entretida 1 = Transform("images/cenas/encontro com lility tocando piano com vestido clássico/lility tocando piano entretida cena 1.jpg", xysize=(1920, 1080), fit="cover")
image cena lility piano victor entra 2 = Transform("images/cenas/encontro com lility tocando piano com vestido clássico/lility tocando piano entretida e victor entra sem ela perceber cena 2.jpg", xysize=(1920, 1080), fit="cover")
image cena lility piano susto para 3 = Transform("images/cenas/encontro com lility tocando piano com vestido clássico/lility percebe victor e leva um susto e para de tocar o piano cena 3.jpg", xysize=(1920, 1080), fit="cover")
image cena lility piano conversa em pe 4 = Transform("images/cenas/encontro com lility tocando piano com vestido clássico/lility levanta após parar de tocar e conversa um pouco com victor cena 4.jpg", xysize=(1920, 1080), fit="cover")
image cena lility danca inicio 5 = Transform("images/cenas/encontro com lility tocando piano com vestido clássico/lility e victor começam a dançar cena 5.jpg", xysize=(1920, 1080), fit="cover")
image cena lility danca valsa 6 = Transform("images/cenas/encontro com lility tocando piano com vestido clássico/lility e victor dançando cena 6.jpg", xysize=(1920, 1080), fit="cover")
image cena lility danca close 7 = Transform("images/cenas/encontro com lility tocando piano com vestido clássico/close de victor e lility dançando cena 7.jpg", xysize=(1920, 1080), fit="cover")

image cena victor quadro fundador 1 = Transform("images/cenas/primeiro encontro com emilia enquanto observa o quadro do fundador e ela o assusta/victor passa pelo quadro do fundador da escola cena 1.jpg", xysize=(1920, 1080), fit="cover")
image cena victor quadro fundador 2 = Transform("images/cenas/primeiro encontro com emilia enquanto observa o quadro do fundador e ela o assusta/victor encara o quadro do fundador cena 2.jpg", xysize=(1920, 1080), fit="cover")
image cena victor quadro fundador 3 = Transform("images/cenas/primeiro encontro com emilia enquanto observa o quadro do fundador e ela o assusta/victor passa novamente pelo quadro do fundador cena 3.jpg", xysize=(1920, 1080), fit="cover")
image cena victor quadro fundador 4 = Transform("images/cenas/primeiro encontro com emilia enquanto observa o quadro do fundador e ela o assusta/victor se sente observado  pelo quadro do fundador cena 4.jpg", xysize=(1920, 1080), fit="cover")
image cena victor emilia susto 5 = Transform("images/cenas/primeiro encontro com emilia enquanto observa o quadro do fundador e ela o assusta/victor leva um susto de emilia cena 5.jpg", xysize=(1920, 1080), fit="cover")

image cena victor galeria corredor observando = Transform("images/cenas/mistério dos quadros estranhos/Man_viewing_painting_in_corridor_0e4147ce.jpg", xysize=(1920, 1080), fit="cover")
image cena victor emilia investigando quadros = Transform("images/cenas/mistério dos quadros estranhos/victor e emilia encarando os quadros e conversando sobre.jpg", xysize=(1920, 1080), fit="cover")
image cena victor banquete dentro do quadro = Transform("images/cenas/mistério dos quadros estranhos/victor no banquete dentro do quadro.jpg", xysize=(1920, 1080), fit="cover")
image cena victor destruindo quadro acido = Transform("images/cenas/mistério dos quadros estranhos/victor destruindo um quadro com acido.jpg", xysize=(1920, 1080), fit="cover")
image cena victor acha id quadro = Transform("images/cenas/mistério dos quadros estranhos/victor encontrando a ID de um estudante desaparecido no quadro.jpg", xysize=(1920, 1080), fit="cover")
image cena victor examina id close = Transform("images/cenas/mistério dos quadros estranhos/victor encontrando a ID de um estudante desaparecido no quadro e encarando em  close.jpg", xysize=(1920, 1080), fit="cover")

default ultima_cena_transe_lility = None

default cena_transe_lility_atual = "cena transe lility 1"

init python:

    def sortear_cena_transe_lility():
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """Retorna aleatoriamente uma das 4 cenas de transe de sangue da Lility, evitando repetir a ?ltima imediatamente."""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        opcoes = ["cena transe lility 1", "cena transe lility 2", "cena transe lility 3", "cena transe lility 4"]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ultima = getattr(store, "ultima_cena_transe_lility", None)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if ultima in opcoes and len(opcoes) > 1:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            opcoes_filtradas = [c for c in opcoes if c != ultima]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        else:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            opcoes_filtradas = opcoes
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        escolhida = renpy.random.choice(opcoes_filtradas)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        store.ultima_cena_transe_lility = escolhida
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        store.cena_transe_lility_atual = escolhida
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        return escolhida

image cena transe lility = DynamicDisplayable(lambda st, at: (store.cena_transe_lility_atual, None))

label executar_transe_sangue(heroina="lility"):

    with flash_red

    play sound "audio/sfx/heartbeat.ogg"

    $ th_bark(heroina, "transe")

    if heroina == "lility":

        $ sortear_cena_transe_lility()

        show cena transe lility at cena_lewd_ofegante with dissolve

    elif heroina == "emilia":

        show cena transe emilia at pulso_sensual_lento with dissolve

    return

image loira banheiro neutra = "images/Enemy's/loira do banheiro neutra.webp"

image loira banheiro ataque = "images/Enemy's/loira do banheiro ataque.webp"

image loira do banheiro neutra = "images/Enemy's/loira do banheiro neutra.webp"

image loira do banheiro ataque = "images/Enemy's/loira do banheiro ataque.webp"

image loira banheiro derrota = "images/Enemy's/loira do banheiro derrota.webp"

image loira do banheiro derrota = "images/Enemy's/loira do banheiro derrota.webp"

image inimigo fundao mascara gas chave grifo = "images/Enemy's/inimigo fundao mascara gas chave grifo neutro.webp"

image inimigo executor conselho prata espada ereto ataque = "images/Enemy's/inimigo executor conselho prata espada ataque.webp"

image bg banheiro abandonado luz vermelha espelho = Transform("images/wallpapers static/bg banheiro abandonado luz vermelha espelho.webp", xysize=(1920, 1080), fit="cover")

image bg animado banheiro abandonado luz vermelha piscando = Movie(play="images/Background Wallpapers motions/bg animado banheiro abandonado luz vermelha piscando.webm", size=(1920, 1080), loop=True)

image elara shock = "images/elara/elara em choque.webp"
image elara em choque = "images/elara/elara em choque.webp"

image elara bochechas rosadas = "images/elara/elara com as bochechas rosadas.webp"

image bg animado biblioteca gotica mesas manha = Movie(play="images/Background Wallpapers motions/bg animado biblioteca gotica mesas manha.webm", size=(1920, 1080), loop=True)

image bg animado biblioteca gotica mesas noite = Movie(play="images/Background Wallpapers motions/bg animado biblioteca gotica mesas noite.webm", size=(1920, 1080), loop=True)

image bg animado corredor industrial subsolo vapor = Movie(play="images/Background Wallpapers motions/bg animado corredor industrial subsolo vapor.webm", size=(1920, 1080), loop=True)

image bg animado corredor industrial caldeira subsolo vapor = Movie(play="images/Background Wallpapers motions/bg animado corredor industrial caldeira subsolo vapor.webm", size=(1920, 1080), loop=True)

image bg animado caldeiras oficina fornalha brasa = Movie(play="images/Background Wallpapers motions/bg animado caldeiras oficina fornalha brasa.webm", size=(1920, 1080), loop=True)

default ultimo_bg_caldeiras = None

default bg_caldeiras_atual = "bg animado corredor industrial caldeira subsolo vapor"

init python:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def sortear_bg_caldeiras():
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """Retorna aleatoriamente um dos 3 cenários animados das caldeiras industriais, evitando repetir o anterior consecutivamente."""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        opcoes = [

            "bg animado corredor industrial subsolo vapor",

            "bg animado corredor industrial caldeira subsolo vapor",

            "bg animado caldeiras oficina fornalha brasa"

        ]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ultimo = getattr(store, "ultimo_bg_caldeiras", None)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if ultimo in opcoes and len(opcoes) > 1:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            opcoes_filtradas = [c for c in opcoes if c != ultimo]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        else:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            opcoes_filtradas = opcoes
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        escolhido = renpy.random.choice(opcoes_filtradas)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        store.ultimo_bg_caldeiras = escolhido
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        store.bg_caldeiras_atual = escolhido
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        return escolhido

image bg animado catacumbas corredor tochas = Movie(play="images/Background Wallpapers motions/bg animado catacumbas corredor tochas.webm", size=(1920, 1080), loop=True)

image bg animado catacumbas corredor runas tochas = Movie(play="images/Background Wallpapers motions/bg animado catacumbas corredor runas tochas.webm", size=(1920, 1080), loop=True)

image bg animado catacumbas cofre velas verdes = Movie(play="images/Background Wallpapers motions/bg animado catacumbas cofre velas verdes.webm", size=(1920, 1080), loop=True)

image bg animado escadaria catacumbas tochas runas = Movie(play="images/Background Wallpapers motions/bg animado escadaria catacumbas tochas runas.webm", size=(1920, 1080), loop=True)

default ultimo_bg_catacumbas = None

default bg_catacumbas_atual = "bg animado catacumbas corredor tochas"

init python:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def sortear_bg_catacumbas():
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """Retorna aleatoriamente um dos 3 cenários animados das catacumbas, evitando repetir o anterior consecutivamente."""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        opcoes = [

            "bg animado catacumbas corredor tochas",

            "bg animado catacumbas corredor runas tochas",

            "bg animado catacumbas cofre velas verdes"

        ]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ultimo = getattr(store, "ultimo_bg_catacumbas", None)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if ultimo in opcoes and len(opcoes) > 1:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            opcoes_filtradas = [c for c in opcoes if c != ultimo]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        else:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            opcoes_filtradas = opcoes
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        escolhido = renpy.random.choice(opcoes_filtradas)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        store.ultimo_bg_catacumbas = escolhido
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        store.bg_catacumbas_atual = escolhido
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        return escolhido

image bg animado patio arvore dia claro = Movie(play="images/Background Wallpapers motions/bg animado patio arvore dia claro.webm", size=(1920, 1080), loop=True)

image bg animado patio arvore entardecer folhas = Movie(play="images/Background Wallpapers motions/bg animado patio arvore entardecer folhas.webm", size=(1920, 1080), loop=True)

image bg animado patio arvore entardecer dourado = Movie(play="images/Background Wallpapers motions/bg animado patio arvore entardecer dourado.webm", size=(1920, 1080), loop=True)

image bg animado patio arvore postes noite = Movie(play="images/Background Wallpapers motions/bg animado patio arvore postes noite.webm", size=(1920, 1080), loop=True)

image bg animado patio arvore noite postes luz = Movie(play="images/Background Wallpapers motions/bg animado patio arvore noite postes luz.webm", size=(1920, 1080), loop=True)

image bg animado entrada academia portoes manha = Movie(play="images/Background Wallpapers motions/bg animado entrada academia portoes manha.webm", size=(1920, 1080), loop=True)

image bg animado entrada academia portoes entardecer sol = Movie(play="images/Background Wallpapers motions/bg animado entrada academia portoes entardecer sol.webm", size=(1920, 1080), loop=True)

image bg animado entrada academia portoes nevoeiro noite = Movie(play="images/Background Wallpapers motions/bg animado entrada academia portoes nevoeiro noite.webm", size=(1920, 1080), loop=True)

image bg animado rua portao academia manha = Movie(play="images/Background Wallpapers motions/bg animado rua portao academia manha.webm", size=(1920, 1080), loop=True)

image bg animado rua portao academia tarde = Movie(play="images/Background Wallpapers motions/bg animado rua portao academia tarde.webm", size=(1920, 1080), loop=True)

image bg animado rua portao academia noite = Movie(play="images/Background Wallpapers motions/bg animado rua portao academia noite.webm", size=(1920, 1080), loop=True)

image bg animado dormitorio externo sol = Movie(play="images/Background Wallpapers motions/bg animado dormitorio externo sol.webm", size=(1920, 1080), loop=True)

image bg animado dormitorio externo tarde = Movie(play="images/Background Wallpapers motions/bg animado dormitorio externo tarde.webm", size=(1920, 1080), loop=True)

image bg rua portao academia predios dia 2k = Transform("images/wallpapers static/bg rua portao academia predios dia 2k.webp", xysize=(1920, 1080), fit="cover")

image bg portao academia entardecer dourado 2k = Transform("images/wallpapers static/bg portao academia entardecer dourado 2k.webp", xysize=(1920, 1080), fit="cover")

image bg rua portao academia postes noite 2k = Transform("images/wallpapers static/bg rua portao academia postes noite 2k.webp", xysize=(1920, 1080), fit="cover")

image bg patio academia arvores dia ensolarado = Transform("images/wallpapers static/bg patio academia arvores dia ensolarado.webp", xysize=(1920, 1080), fit="cover")

image bg patio academia arvores entardecer sol = Transform("images/wallpapers static/bg patio academia arvores entardecer sol.webp", xysize=(1920, 1080), fit="cover")

image bg patio academia arvores postes noite = Transform("images/wallpapers static/bg patio academia arvores postes noite.webp", xysize=(1920, 1080), fit="cover")

image bg animado patio claustro fonte chuva = Movie(play="images/Background Wallpapers motions/bg animado patio claustro fonte chuva.webm", size=(1920, 1080), loop=True)

image bg animado patio claustro arcos chuva = Movie(play="images/Background Wallpapers motions/bg animado patio claustro arcos chuva.webm", size=(1920, 1080), loop=True)

image bg animado patio arvore chuva = Movie(play="images/Background Wallpapers motions/bg animado patio arvore chuva.webm", size=(1920, 1080), loop=True)

image bg animado biblioteca gotica mesas chuva = Movie(play="images/Background Wallpapers motions/bg animado biblioteca gotica mesas chuva.webm", size=(1920, 1080), loop=True)

image bg animado dormitorio quarto chuva = Movie(play="images/Background Wallpapers motions/bg animado dormitorio quarto chuva.webm", size=(1920, 1080), loop=True)

image bg animado dormitorio externo chuva = Movie(play="images/Background Wallpapers motions/bg animado dormitorio externo chuva.webm", size=(1920, 1080), loop=True)

image bg animado entrada academia portoes chuva = Movie(play="images/Background Wallpapers motions/bg animado entrada academia portoes chuva.webm", size=(1920, 1080), loop=True)

image bg animado sala musica piano vitral chuva = Movie(play="images/Background Wallpapers motions/bg animado sala musica piano vitral chuva.webm", size=(1920, 1080), loop=True)

image bg animado gabinete diretor chuva = Movie(play="images/Background Wallpapers motions/bg animado gabinete diretor chuva.webm", size=(1920, 1080), loop=True)

image bg animado corredor academia chuva = Movie(play="images/Background Wallpapers motions/bg animado corredor academia chuva.webm", size=(1920, 1080), loop=True)

image bg animado cemiterio chuva = Movie(play="images/Background Wallpapers motions/bg animado cemiterio chuva.webm", size=(1920, 1080), loop=True)
image bg animado cemiterio manha = Movie(play="images/Background Wallpapers motions/bg animado cemiterio manha.webm", size=(1920, 1080), loop=True)
image bg animado cemiterio noite = Movie(play="images/Background Wallpapers motions/bg animado cemiterio noite.webm", size=(1920, 1080), loop=True)

image mapa animado chuva = Movie(play="images/Background Wallpapers motions/mapa animado chuva.webm", size=(1920, 1080), loop=True)
image mapa animado manha = Movie(play="images/Background Wallpapers motions/mapa animado manha.webm", size=(1920, 1080), loop=True)
image mapa animado neblina noite = Movie(play="images/Background Wallpapers motions/mapa animado neblina noite.webm", size=(1920, 1080), loop=True)
image mapa animado subsolo = Movie(play="images/Background Wallpapers motions/mapa animado subsolo.webm", size=(1920, 1080), loop=True)
image mapa animado tarde = Movie(play="images/Background Wallpapers motions/mapa animado tarde.webm", size=(1920, 1080), loop=True)

image bg animado rua portao academia chuva = Movie(play="images/Background Wallpapers motions/bg animado rua portao academia chuva.webm", size=(1920, 1080), loop=True)

image bg animado rua avenida campus chuva = Movie(play="images/Background Wallpapers motions/bg animado rua avenida campus chuva.webm", size=(1920, 1080), loop=True)

image bg patio claustro fonte chuva = Transform("images/wallpapers static/bg patio claustro fonte chuva.webp", xysize=(1920, 1080), fit="cover")

image bg arcos claustro patio fonte chuva = Transform("images/wallpapers static/bg arcos claustro patio fonte chuva.webp", xysize=(1920, 1080), fit="cover")

image bg biblioteca gotica mesas chuva = Transform("images/wallpapers static/bg biblioteca gotica mesas chuva.webp", xysize=(1920, 1080), fit="cover")

image bg sala musica piano chuva = Transform("images/wallpapers static/bg sala musica piano chuva.webp", xysize=(1920, 1080), fit="cover")

image bg gabinete diretor chuva = Transform("images/wallpapers static/bg gabinete diretor chuva.webp", xysize=(1920, 1080), fit="cover")

image bg corredor academia chuva = Transform("images/wallpapers static/bg corredor academia chuva.webp", xysize=(1920, 1080), fit="cover")

image bg entrada academia portoes chuva = Transform("images/wallpapers static/bg entrada academia portoes chuva.webp", xysize=(1920, 1080), fit="cover")

image bg dormitorio externo chuva = Transform("images/wallpapers static/bg dormitorio externo chuva.webp", xysize=(1920, 1080), fit="cover")

image bg cemiterio chuva = Transform("images/wallpapers static/bg cemiterio chuva.webp", xysize=(1920, 1080), fit="cover")

image bg patio academia arvores chuva = Transform("images/wallpapers static/bg patio academia arvores chuva.webp", xysize=(1920, 1080), fit="cover")

image bg rua portao academia chuva = Transform("images/wallpapers static/bg rua portao academia chuva.webp", xysize=(1920, 1080), fit="cover")

image bg clube_ocultismo_noite = Movie(play="images/Background Wallpapers motions/bg animado sala aula ocultismo alquimia verde.webm", size=(1920, 1080), loop=True)

image bg gremio_dia = Movie(play="images/Background Wallpapers motions/bg animado gabinete diretor dia cortinas.webm", size=(1920, 1080), loop=True)

image bg sala_musica_noite = Movie(play="images/Background Wallpapers motions/bg animado sala musica piano noite.webm", size=(1920, 1080), loop=True)

image bg caldeiras_noite = Movie(play="images/Background Wallpapers motions/bg animado caldeiras oficina fornalha brasa.webm", size=(1920, 1080), loop=True)

image emilia chocada = "images/emilia/emilia uniforme surpresa meio corpo.webp"

image emilia triste = "images/emilia/emilia triste encarando e com lagrimas.webp"

image emilia determinada = "images/emilia/emilia uniforme confiante meio corpo.webp"

image emilia corada = "images/emilia/emilia uniforme corada timida meio corpo.webp"

image elara sorriso_cinico = "images/elara/elara sorrindo de forma ironica.webp"
image elara sorriso cinico = "images/elara/elara sorrindo de forma ironica.webp"

image lility provocante = "images/lility/lility sorriso presas aberto meio corpo.webp"

image valeria sorriso_negocios = "images/valeria/valeria cinica pirulito meio corpo.webp"
image valeria sorriso negocios = "images/valeria/valeria cinica pirulito meio corpo.webp"

image valeria provocante = "images/valeria/valeria sorriso provocante pirulito meio corpo.webp"

image valeria corada_transe = "images/valeria/valeria descontraida sorriso meio corpo.webp"
image valeria corada transe = "images/valeria/valeria descontraida sorriso meio corpo.webp"
image valeria cinica = "images/valeria/valeria cinica pirulito meio corpo.webp"
image elara arrogante = "images/elara/elara uniforme arrogante meio corpo.webp"

# ==============================================================================
# SPRITES E ALIASES DE EXPRESSOES DE VICTOR (FASES 1, 2 E 3)
# ==============================================================================

# FASE 1: UNIFORME ESCOLAR (PADRAO 2K E EXPRESSOES ADICIONAIS)
image victor uniforme serio = "images/victor/victor fase1 uniforme serio.webp"
image victor uniforme serio 2k = "images/victor/victor fase1 uniforme serio 2k.webp"
image victor uniforme neutro = "images/victor/victor fase1 uniforme neutro.webp"
image victor uniforme charmoso = "images/victor/victor fase1 uniforme charmoso.webp"
image victor uniforme charmoso 2k = "images/victor/victor fase1 uniforme charmoso 2k.webp"
image victor uniforme ferido sorriso = "images/victor/victor fase1 uniforme ferido sorriso.webp"
image victor uniforme ferido sorriso 2k = "images/victor/victor fase1 uniforme ferido sorriso 2k.webp"
image victor uniforme surpreso = "images/victor/victor fase1 uniforme surpreso.webp"
image victor uniforme surpreso 2k = "images/victor/victor fase1 uniforme surpreso 2k.webp"
image victor uniforme pensando = "images/victor/victor fase1 uniforme pensando.webp"
image victor uniforme confiante = "images/victor/victor fase1 uniforme confiante.webp"
image victor uniforme ferido combate = "images/victor/victor fase1 uniforme ferido combate.webp"
image victor uniforme constrangido = "images/victor/victor fase1 uniforme constrangido.webp"
image victor uniforme falando = "images/victor/victor fase1 uniforme falando.webp"
image victor uniforme ferido determinado = "images/victor/victor fase1 uniforme ferido determinado.webp"
image victor uniforme sorrindo = "images/victor/victor fase1 uniforme sorrindo.webp"
image victor uniforme sem jeito = "images/victor/victor fase1 uniforme sem jeito.webp"
image victor uniforme triste = "images/victor/victor fase1 uniforme triste.webp"
image victor uniforme furioso = "images/victor/victor fase1 uniforme furioso.webp"
image victor uniforme irritado serio = "images/victor/victor fase1 uniforme irritado serio.webp"
image victor uniforme melancolico = "images/victor/victor fase1 uniforme melancolico.webp"
image victor uniforme sereno = "images/victor/victor fase1 uniforme sereno.webp"
image victor uniforme sorriso de canto = "images/victor/victor fase1 uniforme sorriso de canto.webp"
image victor uniforme sorriso malicioso = "images/victor/victor fase1 uniforme sorriso malicioso.webp"
image victor uniforme aterrorizado = "images/victor/victor fase1 uniforme aterrorizado.webp"
image victor uniforme desconfiado = "images/victor/victor fase1 uniforme desconfiado.webp"
image victor uniforme desgosto = "images/victor/victor fase1 uniforme desgosto.webp"
image victor uniforme entediado = "images/victor/victor fase1 uniforme entediado.webp"
image victor uniforme estranhando = "images/victor/victor fase1 uniforme estranhando.webp"
image victor uniforme exausto = "images/victor/victor fase1 uniforme exausto.webp"
image victor fase1 frenesi = "images/victor/victor fase1 frenesi.webp"
image victor furia = "images/victor/victor fase1 frenesi.webp"

# FASE 2: HUMANO / DECADENCIA & DESGASTE (LACAIO)
image victor fase2 humano = "images/victor/victor fase2 humano.webp"
image victor fase2 humano assustado = "images/victor/victor fase2 humano assustado.webp"
image victor fase2 humano cansado = "images/victor/victor fase2 humano cansado.webp"
image victor fase2 humano chocado = "images/victor/victor fase2 humano chocado.webp"
image victor fase2 humano melancolico = "images/victor/victor fase2 humano melancolico.webp"
image victor fase2 humano olhando de cima pretensioso = "images/victor/victor fase2 humano olhando de cima pretensioso.webp"
image victor fase2 humano sorrindo = "images/victor/victor fase2 humano sorrindo.webp"
image victor fase2 humano sorriso presuncoso = "images/victor/victor fase2 humano sorriso presuncoso.webp"
image victor fase2 humano surpreso = "images/victor/victor fase2 humano surpreso.webp"
image victor fase2 humano sorrindo leve = "images/victor/victor fase2 humano sorrindo leve.webp"
image victor fase2 frenesi = "images/victor/victor fase2 frenesi.webp"

# FASE 3: PREDADOR VAMPIRICO / HUMANO NO ABISMO
image victor fase3 predador postura = "images/victor/victor fase3 predador postura.webp"
image victor fase3 predador serio = "images/victor/victor fase3 predador serio.webp"
image victor fase3 predador rindo = "images/victor/victor fase3 predador rindo.webp"
image victor fase3 predador busto = "images/victor/victor fase3 predador busto.webp"
image victor fase3 predador cansado = "images/victor/victor fase3 predador cansado.webp"
image victor fase3 predador chocado = "images/victor/victor fase3 predador chocado.webp"
image victor fase3 predador neutro = "images/victor/victor fase3 predador neutro.webp"
image victor fase3 predador triste = "images/victor/victor fase3 predador triste.webp"
image victor fase3 humano frustrado = "images/victor/victor fase3 humano frustrado.webp"
image victor fase3 humano irritado = "images/victor/victor fase3 humano irritado.webp"
image victor fase3 frenesi = "images/victor/victor fase3 frenesi.webp"
image victor fase 3 frenesi = "images/victor/victor fase3 frenesi.webp"

# ALIASES DIRETOS PARA FACILIDADE DE USO NO SCRIPT
image victor frenesi = "images/victor/victor fase1 frenesi.webp"
image victor serio = "images/victor/victor fase1 uniforme serio.webp"
image victor pensando = "images/victor/victor fase1 uniforme pensando.webp"
image victor confiante = "images/victor/victor fase1 uniforme confiante.webp"
image victor sorrindo = "images/victor/victor fase1 uniforme sorrindo.webp"
image victor falando = "images/victor/victor fase1 uniforme falando.webp"
image victor surpreso = "images/victor/victor fase1 uniforme surpreso.webp"
image victor triste = "images/victor/victor fase1 uniforme triste.webp"
image victor sem_jeito = "images/victor/victor fase1 uniforme sem jeito.webp"
image victor sem jeito = "images/victor/victor fase1 uniforme sem jeito.webp"
image victor constrangido = "images/victor/victor fase1 uniforme constrangido.webp"
image victor charmoso = "images/victor/victor fase1 uniforme charmoso.webp"
image victor ferido = "images/victor/victor fase1 uniforme ferido determinado.webp"
image victor ferido combate = "images/victor/victor fase1 uniforme ferido combate.webp"
image victor ferido sorriso = "images/victor/victor fase1 uniforme ferido sorriso.webp"
image victor neutro = "images/victor/victor fase1 uniforme neutro.webp"
image victor furioso = "images/victor/victor fase1 uniforme furioso.webp"
image victor irritado = "images/victor/victor fase1 uniforme irritado serio.webp"
image victor irritado serio = "images/victor/victor fase1 uniforme irritado serio.webp"
image victor melancolico = "images/victor/victor fase1 uniforme melancolico.webp"
image victor sereno = "images/victor/victor fase1 uniforme sereno.webp"
image victor aterrorizado = "images/victor/victor fase1 uniforme aterrorizado.webp"
image victor desconfiado = "images/victor/victor fase1 uniforme desconfiado.webp"
image victor desgosto = "images/victor/victor fase1 uniforme desgosto.webp"
image victor entediado = "images/victor/victor fase1 uniforme entediado.webp"
image victor estranhando = "images/victor/victor fase1 uniforme estranhando.webp"
image victor exausto = "images/victor/victor fase1 uniforme exausto.webp"

image victor vampiro serio = "images/victor/victor fase3 predador serio.webp"
image victor vampiro rindo = "images/victor/victor fase3 predador rindo.webp"
image victor vampiro postura = "images/victor/victor fase3 predador postura.webp"
image victor fase1 estudante amigavel meio corpo = "images/victor/corpo inteiro/victor fase1 estudante amigavel.webp"
image victor fase1 estudante serio meio corpo = "images/victor/corpo inteiro/victor fase1 estudante serio.webp"
image victor fase2 desgastado cabisbaixo meio corpo = "images/victor/corpo inteiro/victor fase2 desgastado cabisbaixo.webp"
image victor fase2 desgastado neutro meio corpo = "images/victor/corpo inteiro/victor fase2 desgastado neutro.webp"

default estagio_mestra = 1

default estagio_emilia = 1

default estagio_valeria = 1

default estagio_elara = 1

default persistent.mem_lility_1 = False

default persistent.mem_lility_2 = False

default persistent.mem_emilia_1 = False

default persistent.mem_emilia_2 = False

default persistent.mem_valeria_1 = False

default persistent.mem_valeria_2 = False

default persistent.mem_elara_1 = False

default persistent.mem_elara_2 = False

init python:

    def verificar_marco_disponivel(heroina):
        """
    Retorna True se o jogador ja atingiu os requisitos de Afeto, Duvida e Condicoes Narrativas
    para destravar o proximo Evento de Marco (Milestone) da heroina.
    Rebalanceado: Requer conquista gradual, confianca mutua e superacao de testes psicologicos.
    """
        if heroina == "lility":
            
            if store.estagio_mestra == 1:
                return (
                store.afeto_mestra >= 8 and
                store.periodo == "Noite" and
                store.fome_sangue <= 70 and
                getattr(store, "conhece_covil_lility", True)
            )
            
            if store.estagio_mestra == 2:
                return (
                store.afeto_mestra >= 18 and
                store.periodo == "Noite" and
                getattr(store, "ressonancia_pre_diluviana", 0) >= 4 and
                getattr(store, "vinculo_sangue_lility", 0) >= 35
            )
        
        elif heroina == "emilia":
            
            if store.estagio_emilia == 1:
                return (
                store.afeto_emilia >= 8 and
                getattr(store, "duvida_emilia", 0) <= 2 and
                getattr(store, "humanidade", 50) >= 40 and
                store.periodo != "Noite"
            )
            
            if store.estagio_emilia == 2:
                return (
                store.afeto_emilia >= 18 and
                getattr(store, "duvida_emilia", 0) <= 3 and
                getattr(store, "conhecimento_oculto", 0) >= 2
            )
        
        elif heroina == "valeria":
            
            if store.estagio_valeria == 1:
                return (
                store.afeto_valeria >= 8 and
                getattr(store, "duvida_valeria", 0) <= 3 and
                (getattr(store, "dinheiro_jogador", 0) >= 150 or getattr(store, "divida_fundao_paga", False))
            )
            
            if store.estagio_valeria == 2:
                return (
                store.afeto_valeria >= 18 and
                getattr(store, "dominio_jogador", 0) >= 2 and
                getattr(store, "duvida_valeria", 0) <= 2
            )
        
        elif heroina == "elara":
            
            if store.estagio_elara == 1:
                return (
                store.afeto_elara >= 8 and
                getattr(store, "duvida_elara", 0) <= 2 and
                getattr(store, "intelecto", 0) >= 2 and
                getattr(store, "exposicao", 0) <= 40
            )
            
            if store.estagio_elara == 2:
                return (
                (store.afeto_elara >= 18 or getattr(store, "elara_subjugada_no_cofre", False)) and
                getattr(store, "duvida_elara", 0) <= 3
            )
        
        return False

define mob_calouro_a = Character("Aluno Calouro (Uniforme Preto)", color="#8899aa")

define mob_caloura_b = Character("Aluna Caloura (Uniforme Preto)", color="#8899aa")

define mob_calouro_c = Character("Calouro Doador (Pálido)", color="#8899aa")

define mob_veterano_a = Character("Aluno Veterano", color="#778899")

define mob_veterana_b = Character("Aluna Veterana", color="#778899")

define mob_veterano_c = Character("Veterana do Ocultismo", color="#8877aa")
define mob_veterana_c = mob_veterano_c
define mob_enfermeira = Character("Enfermeira Clara", color="#77aaaa")

define mob_professor_a = Character("Professor Cansado", color="#999999")

define mob_professora_b = Character("Professora Supervisora", color="#999999")

define mob_policial_a = Character("Policial de Patrulha", color="#557799")

define mob_policial_b = Character("Oficial de Ronda", color="#557799")

define mob_policial_c = Character("Detetive da Metrópole", color="#557799")

define mob_diretor = Character("Diretor da Academia", color="#aaaaaa")

default nome_mob_atual = "Estudante de Uniforme Preto"

default tipo_mob_atual = "aluno"

default sprite_mob_atual = ""

default fala_mob_atual = ""

default id_mob_atual = "mob calouro a"

image mob calouro a = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob calouro a"), None))

image mob caloura b = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob caloura b"), None))

image mob calouro c = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob calouro c"), None))

image mob veterano a = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob veterano a"), None))

image mob veterana b = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob veterana b"), None))

image mob veterano c = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob veterano c"), None))
image mob veterana c = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob veterana c"), None))
image mob veterana fundao = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob veterana fundao"), None))
image mob veterano fundao = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob veterano fundao"), None))
image mob veterano a fundao = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob veterano a fundao"), None))
image mob veterano b fundao = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob veterano b fundao"), None))
image mob veterana ocultista = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob veterana ocultista"), None))
image mob veterano ocultista = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob veterano ocultista"), None))
image mob enfermeira = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob enfermeira"), None))

image mob professor a = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob professor a"), None))

image mob professora b = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob professora b"), None))

image mob policial a = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob policial a"), None))

image mob policial b = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob policial b"), None))

image mob policial c = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob policial c"), None))

image mob diretor = DynamicDisplayable(lambda st, at: (obter_sprite_mob("mob diretor"), None))

init python:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def obter_filtro_matriz_zona():
        """
        Retorna a matriz de cor atmosférica sutil de acordo com a iluminação do cenário e período atual.
        Calibrada para harmonizar todos os personagens (Victor, heroínas e figurantes) com o fundo,
        mantendo fidelidade absoluta dos tons de pele, olhos e vestimentas com intensidade reduzida.
        """
        loc = getattr(store, "local_atual", "dormitorio")
        per = getattr(store, "periodo", "Manhã")

        # Subsolo, cemitério e catacumbas: atmosfera gótica fria e úmida
        if loc in ["cemiterio_nevoa", "catacumbas", "cripta_cofre", "banheiro_abandonado"]:
            if per == "Noite":
                return TintMatrix("#c5cee0") * BrightnessMatrix(-0.10) * ContrastMatrix(1.04)
            return TintMatrix("#ccd4e0") * BrightnessMatrix(-0.06) * SaturationMatrix(0.94)

        if per == "Noite":
            # Noite gótica suave / Luar prateado e leve escurecimento natural
            return TintMatrix("#d8e2f0") * BrightnessMatrix(-0.06) * ContrastMatrix(1.03)
        elif per == "Tarde":
            # Entardecer dourado suave: calor crepuscular delicado sem amarelar a pele
            return TintMatrix("#faede1") * BrightnessMatrix(-0.02) * SaturationMatrix(0.98)

        # Manhã / Dia claro: luz natural límpida
        return IdentityMatrix()

    def aplicar_filtro_ambiente(trans, st, at):
        trans.matrixcolor = obter_filtro_matriz_zona()
        return None

    def obter_sprite_mob(id_mob, expressao=None):
        """
        Carrega o sprite .webp do figurante na mesma proporção dos personagens principais,
        suportando expressões dinâmicas (ex: 'medo', 'transe hipnotico', 'sorrindo', etc.)
        e aplicando o filtro de iluminação da zona e garantindo ancoragem correta.
        """
        id_limpo = id_mob.strip() if id_mob else "mob calouro a"
        
        candidatos = []
        if expressao:
            exp = expressao.strip()
            candidatos.append(f"images/mobs/{id_limpo} {exp}.webp")
            candidatos.append(f"images/mobs/{id_limpo}_{exp}.webp")
            if exp == "transe":
                candidatos.append(f"images/mobs/{id_limpo} transe hipnotico.webp")
            elif exp == "transe hipnotico":
                candidatos.append(f"images/mobs/{id_limpo} transe.webp")
            elif exp in ("ameacadora", "ameaçadora"):
                candidatos.append(f"images/mobs/{id_limpo} ameacadora.webp")
        
        candidatos.append(f"images/mobs/{id_limpo}.webp")
        candidatos.append(f"images/mobs/{id_limpo} neutro.webp")
        
        caminho = None
        for c in candidatos:
            if renpy.loadable(c):
                caminho = c
                break
        
        if caminho:
            return Image(caminho)
        
        
        return Transform("images/victor/corpo inteiro/victor fase1 estudante serio.webp", matrixcolor=TintMatrix("#1a2230") * BrightnessMatrix(-0.65))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    MOBS_LORE_DATABASE = {
        "mob veterano ocultista": {
            "nome": "Aluno Veterano do Ocultismo",
            "tipo": "ocultista",
            1: [
                "Não pise no círculo de giz, calouro... O pêndulo não parou de oscilar na direção das catacumbas a manhã inteira.",
                "Traduza a terceira inscrição na base da estátua do fundador se quiser perder o sono. Não fala sobre educação... fala sobre sacrifício em ano bissexto.",
                "O diário de 1889 menciona um estudante chamado Victor que sobreviveu à primeira drenagem... Mas o retrato dele nas páginas tinha a mesma data de nascimento que a sua."
            ],
            2: [
                "Palidez fascinante, Vane... Suas pupilas estão dilatadas e seu pulso soa igualzinho ao das cobaias dos diários de 1889.",
                "O sal negro que coloquei nas frestas da porta do clube começou a queimar sozinho. Há uma presença ancestral faminta sob os alicerces."
            ],
            3: [
                "E-Esses olhos carmesins... Afaste-se! Nem mesmo o giz consagrado consegue conter um bebedor de sangue verdadeiro!",
                "O selo das catacumbas se rompeu! Não há círculo de proteção que salve este colégio da fome do abismo!"
            ]
        },
        "mob veterana ocultista": {
            "nome": "Aluna Veterana do Ocultismo",
            "tipo": "ocultista",
            1: [
                "Pegue este maço de sálvia seca, aluno transferido... Os quadros do segundo andar adoram rostos novos.",
                "Tirei três cartas para você agora há pouco: A Torre, A Lua e A Morte. O baralho inteiro tremeu quando tentei embaralhar de novo... O destino deste lugar já está selado.",
                "As sombras nos cantos da sala de música não estão acompanhando as notas do piano. Há uma mulher de cabelos de prata cantando um lamento que apenas os condenados escutam."
            ],
            2: [
                "As cartas de tarô não paravam de mostrar O Enforcado para você, Victor... Você cheira a sangue seco e poeira de violino.",
                "A água benta nas pias da capela evaporou sem deixar resíduo. Quando os elementos sagrados recusam este solo, significa que o ritual do colégio está quase completo."
            ],
            3: [
                "A vela verde acabou de apagar...! P-Por favor, poupe a minha vida, eu juro que queimo todas as minhas anotações sobre a cripta!",
                "Não olhe para a lua carmesim lá fora! O eclipse já começou nos planos invisíveis... Quem pisar no pátio agora perde a alma!"
            ]
        },
        "mob veterano fundao": {
            "nome": "Veterano do Fundão",
            "tipo": "fundao",
            1: [
                "Caminho errado, bolsista. A menos que tenha grana para os frascos verdes, volte lá para cima antes que o vapor estrague esse uniforme alinhado.",
                "Se precisa de sangue sem passar pelo prontuário da Dra. Clara, fala baixo. A Valéria tem uns frascos de plasma que 'caíram' do caminhão da mantenedora.",
                "Ouviu o rangido das caldeiras? Não é pressão de vapor, cara... Tem dias em que a fornalha queima ossos em vez de carvão mineral. O cheiro não mente."
            ],
            2: [
                "Caramba, Vane, você tá tremendo igual viciado em abstinência... Tá procurando uma bolsa de sangue barata ou uma dose de Fada Verde?",
                "Os cães do Grêmio desceram até o depósito clandestino ontem. Tivemos que esconder três caixas de contrabando atrás dos tubos de fuligem. A corda tá apertando."
            ],
            3: [
                "Opa, para trás, aberração! A Valéria não me paga o suficiente para eu ter a garganta arrancada por um ghoul faminto!",
                "As válvulas de emergência foram lacradas por ordem da Presidente Elara! Eles vão cozinhar todo mundo vivo aqui embaixo se a quarentena falhar!"
            ]
        },
        "mob veterana fundao": {
            "nome": "Veterana do Fundão",
            "tipo": "fundao",
            1: [
                "Heh, olha só o cordeirinho passeando perto das caldeiras. Mantenha os olhos longe do nosso estoque e vamos nos dar muito bem.",
                "O Grêmio acha que manda em tudo porque tem distintivos de prata. Mas quando falta luz e a névoa sobe, quem sabe navegar pelos dutos somos nós do fundão.",
                "Cuidado com o que bebe no Bar da Fada Verde, gracinha. Tem doses que acalmam a cabeça, e tem doses que te fazem esquecer quem você era antes de entrar aqui."
            ],
            2: [
                "Noite difícil na Zona Vermelha, gracinha? Com olheiras desse tamanho, até os cães do Grêmio Estudantil vão farejar você.",
                "Vi a Valéria trancando o cofre de ferro com três cadeados diferentes hoje cedo. Quando até a chefe do contrabando parece assustada, é hora de afiar os canivetes."
            ],
            3: [
                "M-Merda, olha essas presas! Leva a bolsa de contrabando, leva o dinheiro, só não me morde!",
                "Os Executores de casaco branco fecharam os acessos às caldeiras com grades soldadas! Estamos encurralados igual ratos de porão!"
            ]
        },
        "mob enfermeira": {
            "nome": "Enfermeira Clara",
            "tipo": "medico",
            "genero": "f",
            "descricao": "Hematologista da Fundação Mantenedora e responsável pela enfermaria do campus sob a farsa da Campanha de Saúde Comunitária.",
            1: [
                "Arregace a manga, Sr. Vane. A Campanha de Saúde Comunitária garante créditos extras para bolsistas... e um doador com o seu hemograma vale ouro para a Fundação.",
                "Os relatórios de coagulação da sua amostra indicam uma densidade incompatível com a fisiologia humana comum. O Conselho pagará uma quantia generosa por um tubo adicional.",
                "Mantenha as cortinas fechadas enquanto estiver no leito, Victor. As coletas noturnas não devem ser perturbadas por olhares curiosos dos calouros."
            ],
            2: [
                "Nenhum batimento sob o estetoscópio e temperatura corporal de cadáver... A Presidente Elara me ordenou fornecer bolsas filtradas apenas mediante assinatura no protocolo.",
                "Três calouros deram entrada com choque hipovolêmico grave nesta madrugada. Tive que assinar laudos de 'anemia ferropriva crônica' para evitar intervenção policial externa."
            ],
            3: [
                "Os refrigeradores de plasma foram esvaziados pelos Executores do Conselho! Não me olhe com essas presas, Vane... eu só cumpro ordens médicas!",
                "A Fundação cortou o fornecimento de anticoagulantes! Eles não querem mais bolsas preservadas... querem presas vivas amarradas às macas!"
            ]
        },
        "mob calouro a": {
            "nome": "Aluno Calouro A",
            "tipo": "aluno",
            1: [
                "Assinei a ficha de doação de sangue do Grêmio hoje cedo na enfermaria. Disseram que dá abono de faltas e suco de fruta... Mas voltei para o quarto com as mãos geladas e sem forças.",
                "Você também ouviu os passos rápidos no sótão do dormitório às três da manhã? Fui até o corredor olhar... e vi um dos monitores de branco carregando um saco plástico gotejando.",
                "Não encare os veteranos do Grêmio quando cruzar com eles nos corredores. Um colega meu fez isso semana passada... e no dia seguinte a matrícula dele simplesmente constava como 'anulada'."
            ],
            2: [
                "Meu colega de quarto não desceu para o café hoje. A cama dele estava desmontada e o armário trancado, como se nunca tivesse morado ninguém ali...",
                "Encontrei marcas de arranhões por dentro da maçaneta do meu quarto. Não foram feitas com chave... pareciam unhas de alguém tentando desesperadamente sair antes do amanhecer."
            ],
            3: [
                "Trancaram as saídas dos dormitórios com correntes pesadas! Estão dizendo que quem tentar pular os muros não passa do primeiro arbusto!",
                "Socorro! As luzes do corredor apagaram e tem algo rastejando no teto! Não me deixe sozinho aqui, Vane!"
            ]
        },
        "mob caloura b": {
            "nome": "Aluna Caloura B",
            "tipo": "aluno",
            1: [
                "Você viu como os membros do Conselho Estudantil de uniforme branco olham pra nós de uniforme preto? Não parece olhar de colega... parece que estão escolhendo do cardápio.",
                "Encontrei uma lista rasgada perto da lareira do salão nobre... Tinha nomes de bolsistas com cruzes desenhadas ao lado em tinta vermelha. Seu nome estava na segunda página, Victor.",
                "A água das torneiras do terceiro andar saiu com gosto de ferrugem hoje cedo. Minha colega disse que é encanamento velho... mas parecia ferro cru, como sangue seco diluído."
            ],
            2: [
                "Vi marcas escuras e compridas no piso perto do incinerador antes dos monitores jogarem água sanitária. Disseram que foi tinta de cartaz, mas o cheiro era de ferrugem e ferro puro.",
                "A garota do quarto 204 deixou um bilhete debaixo do meu travesseiro antes de sumir: 'Eles não querem nossas mensalidades, querem nossas veias'. Não consigo dormir desde então."
            ],
            3: [
                "A neblina escura entrou pelas frestas das janelas da biblioteca. Ninguém consegue ligar para os pais... As linhas telefônicas da escola inteira foram cortadas!",
                "O Grêmio começou a levar grupos de cinco alunos de cada vez para o subsolo da capela! Quem entra não volta mais... Por favor, nos tire daqui!"
            ]
        },
        "mob calouro c": {
            "nome": "Calouro Doador C",
            "tipo": "doador",
            1: [
                "Minha cabeça ainda está girando da coleta na enfermaria... Eles colheram duas bolsas inteiras de mim e mandaram eu não sair do dormitório depois das seis.",
                "Eles me deram um comprimido cinza antes de espetarem a agulha... Disseram que era ferro concentrado, mas me deixou dormente... nem senti quando a bolsa encheu até a borda.",
                "O meu braço não para de latejar. A enfermeira disse que meu tipo sanguíneo é 'premiado'... Por que isso soa como uma sentença de morte em vez de um elogio?"
            ],
            2: [
                "Toda vez que o sino do crepúsculo bate, sinto uma fraqueza terrível no peito... Como se algo nas sombras estivesse sugando meu calor à distância.",
                "Nem consigo mais segurar uma caneta sem a mão tremer de anemia. Se eles me chamarem para a enfermaria mais uma vez esta semana, acho que meu coração para."
            ],
            3: [
                "Não sobrou quase ninguém na ala B dos quartos. Quem doa sangue todos os dias simplesmente... deixa de acordar no dia seguinte.",
                "Minha visão tá quase toda escura... Se você for beber de mim, Vane, faça rápido... Não aguento mais sentir essa agonia fria."
            ]
        },
        "mob veterano a": {
            "nome": "Aluno Veterano A",
            "tipo": "veterano",
            1: [
                "Regra número um para não sumir desta escola, calouro: nunca fique sozinho nas escadarias após o pôr do sol. Os alunos ausentes sempre começam como 'afastamento médico' no boletim.",
                "Se você ouvir alguém chamando seu nome de dentro de um armário trancado no subsolo, continue andando. Quem parou para ajudar ano passado hoje é apenas foto desbotada no mural.",
                "Não gaste seu fôlego denunciando nada para a diretoria. O diretor Ambrósio assina qualquer atestado de óbito que a Presidente Elara colocar na mesa dele."
            ],
            2: [
                "Três veteranos do terceiro andar foram transferidos de madrugada sem aviso prévio. A Valéria nas caldeiras sabe para onde foram, mas ela não abre a boca de graça.",
                "Achei uma faca de prata enterrada perto das raízes da árvore do pátio. Tinha símbolos talhados no cabo e sangue seco na lâmina. Alguém tentou se defender aqui."
            ],
            3: [
                "Isto virou um matadouro a céu aberto. O Conselho não está mais nem disfarçando. Se você ainda tem pernas sãs, Vane, ache uma saída antes do Eclipse sangrento!",
                "Barricamos a porta da sala de convivência com armários de ferro, mas eles estão batendo do outro lado com força de aríete! O cerco fechou!"
            ]
        },
        "mob veterana b": {
            "nome": "Aluna Veterana B",
            "tipo": "veterano",
            1: [
                "A carteira com o tampo raspado no fundo da sala de aula? Se quer manter sua bolsa de estudos intacta, finja que aquela cadeira sempre esteve desocupada.",
                "Nora Vasques se sentava exatamente onde você senta no refeitório, Victor. Ela começou a fazer as mesmas perguntas sobre a cripta... antes de ser levada para a 'quarentena'.",
                "Reparou que os sinos da torre tocam sete vezes às seis da tarde? Não é hora canônica. É o sinal para os guardas soltarem as correntes do canil subterrâneo."
            ],
            2: [
                "O pessoal do Clube de Ocultismo encontrou arranhões profundos nas portas corta-fogo. As criaturas não estão mais só nas catacumbas... elas estão subindo.",
                "Vi a senhorita Emília inspecionando as gárgulas do telhado com um rosário de prata e lágrimas nos olhos. Até a menina santa da igreja sabe que o horror aqui não tem perdão."
            ],
            3: [
                "O toque de recolher agora é sob vigilância de lâminas. Vi membros da guarda de branco arrastando sacos pesados em direção ao subsolo da capela.",
                "As janelas do salão nobre foram pintadas de preto por dentro para que ninguém veja o que acontece no jardim durante a madrugada!"
            ]
        },
        "mob veterano c": {
            "nome": "Veterana do Ocultismo C",
            "tipo": "ocultismo",
            1: [
                "As velas verdes que acendemos no clube não tremem com a brisa da janela... Elas só tremem quando aquilo que rasteja abaixo do colégio respira fundo.",
                "O sal consagrado que espalhei nas soleiras das portas estava enegrecido hoje cedo. Algo muito antigo e voraz passou arrastando suas garras pelo piso durante a madrugada.",
                "Se você olhar para o espelho do corredor oeste no ângulo certo, o reflexo demora meio segundo a mais para piscar. Eles estão nos observando do outro lado do vidro."
            ],
            2: [
                "As inscrições rúnicas de proteção nas paredes antigas estão rachando uma a uma. Há uma presença pré-diluviana faminta aqui dentro... e o Grêmio está alimentando ela.",
                "O sangue colhido na enfermaria não está indo para hospitais civis. Eu vi os dutos secretos canalizando o plasma diretamente para os selos de pedra das catacumbas."
            ],
            3: [
                "O véu entre o mundo dos vivos e o abismo rasgou de vez! Ouça o vapor silvando nas paredes... O tributo de sangue está prestes a ser cobrado!",
                "A hora do despertar chegou! As sombras se ergueram das lajes do cemitério e não obedecem a mais ninguém!"
            ]
        },
        "mob professor a": {
            "nome": "Professor Cansado A",
            "tipo": "professor",
            1: [
                "Eu apenas leciono literatura clássica e lanço as notas. As deliberações sigilosas da Presidente Elara com a mantenedora não constam no projeto pedagógico.",
                "Não me entregue redações falando sobre gritos nos porões, Vane. Minha família depende deste salário e o Grêmio lê cada linha corrigida pelos docentes.",
                "Encontrei uma ordem de transferência em branco com a minha assinatura falsificada na gaveta. Eles sabem que eu vi os caminhões frigoríficos... É questão de tempo."
            ],
            2: [
                "Recebi memorando confidencial para abonar o sumiço de quatro alunos da minha turma matutina e não telefonar para as famílias. Eu tenho filhos para criar, rapaz.",
                "Colocaram cadeados industriais na porta do arquivo histórico do colégio. Qualquer docente que tentar consultar as atas de fundação de 1889 será demitido por justa causa."
            ],
            3: [
                "A sala dos professores está quase deserta... Os que fizeram perguntas desapareceram no fim de semana. Tranque-se onde puder, Vane. Não há mais aula alguma.",
                "Queimaram todos os diários de classe na caldeira central! Estão apagando qualquer prova documental de que esses estudantes um dia pisaram aqui!"
            ]
        },
        "mob professora b": {
            "nome": "Professora Supervisora B",
            "tipo": "professor",
            1: [
                "O uso rigoroso do uniforme preto e a disciplina nos corredores são para a própria segurança dos estudantes. Menos bisbilhotice e mais estudo, por favor.",
                "Circular sem crachá de identificação após o toque de silêncio resulta em encaminhamento direto para o comitê disciplinar da Presidente Elara. Esteja avisado.",
                "Boatos sobre 'abstinência' e 'doações forçadas' constituem infração gravíssima contra o regulamento moral. O prestígio da mantenedora é inquestionável."
            ],
            2: [
                "Qualquer estudante propagando boatos sobre incidentes noturnos será suspenso sumariamente. A honorável Presidente Elara mantém a ordem impecável deste colégio.",
                "As rondas de supervisão foram redobradas nos dormitórios femininos. Alunas flagradas fora de suas camas sofrerão retenção preventiva na enfermaria central."
            ],
            3: [
                "O Conselho Estudantil declarou confinamento total. Todos os discentes de uniforme preto devem permanecer recolhidos até a próxima deliberação oficial!",
                "A insubordinação civil será respondida com a força dos Executores de Branco! Recolham-se imediatamente aos seus quartos!"
            ]
        },
        "mob policial a": {
            "nome": "Policial de Patrulha A",
            "tipo": "policial",
            1: [
                "Ronda preventiva nos limites externos da academia. A direção nos garantiu que a disciplina interna é mantida com segurança patrimonial privada.",
                "Não chegue perto das grades do portão leste depois das dez, garoto. Nem a polícia da cidade tem jurisdição para entrar se os cães de guarda forem soltos.",
                "Recebemos ordens expressas da chefia para ignorar disparos ou gritos abafados vindos desta colina. O dinheiro que a Fundação joga na prefeitura cala qualquer sirene."
            ],
            2: [
                "Quinto boletim de desaparecimento de adolescente registrado pelos pais nesta semana... E a delegacia central ordenou engavetar tudo como rebeldia juvenil.",
                "Um colega de patrulha tentou pular o muro após ouvir um pedido de socorro semana passada... No outro dia ele pediu exoneração imediata e se mudou de estado."
            ],
            3: [
                "Nossas viaturas não conseguem atravessar a muralha de névoa ao redor dos portões! O rádio da polícia só capta estática e ganidos... Que inferno é esse lugar?!",
                "O comando da polícia declarou esta colina zona de exclusão militar! Ninguém entra e ninguém sai!"
            ]
        },
        "mob policial b": {
            "nome": "Oficial de Ronda B",
            "tipo": "policial",
            1: [
                "Permaneça dentro dos muros da instituição, garoto. Os bosques ao redor dos muros não são seguros para civis desacompanhados.",
                "Esta névoa não é natural... O medidor de temperatura cai cinco graus sempre que o vento sopra das catacumbas do colégio. Algo está apodrecendo ali embaixo.",
                "Encontrei pegadas descalças na lama que sumiam de repente na base da muralha de pedra de quatro metros. Que tipo de bicho escala isso sem corda?!"
            ],
            2: [
                "Achei restos de tecido ensanguentado com o monograma desta academia perto da boca do lobo na calçada. Alguém lá dentro está lavando as mãos com dinheiro sujo.",
                "Minha lanterna tática descarregou em dois minutos enquanto eu vigiava o cemitério dos fundos. As baterias eram novas... Algo naquele nevoeiro drena energia e calor."
            ],
            3: [
                "Temos ordens superiores para impedir qualquer pessoa de ultrapassar os portões de ferro. A região inteira foi cercada e declarada zona de quarentena biológica!",
                "Atirem em qualquer vulto que se mover no nevoeiro! Seja humano, fera ou aberração de sangue!"
            ]
        },
        "mob policial c": {
            "nome": "Detetive da Metrópole C",
            "tipo": "policial",
            1: [
                "A fundação nobre que banca esta escola tem imunidade política até o pescoço. Enquanto os envelopes chegarem na corregedoria, ninguém pisa aqui.",
                "Tenho fotos confidenciais dos necrotérios municipais... O sangue dos cadáveres recolhidos perto deste rio foi completamente drenado por duas perfurações limpas no pescoço.",
                "Um conselho de quem sobreviveu vinte anos nas ruas imundas desta metrópole, garoto: quem procura a verdade sobre a elite geralmente termina boiando na represa."
            ],
            2: [
                "Rastreei um carregamento clandestino de bolsas de plasma desviado do hospital regional... As caixas foram descarregadas nos fundos desta mesma escola.",
                "A promotoria pública tentou intimar a senhorita von Weiss ontem à tarde. Dois oficiais desapareceram a caminho do colégio e o promotor arquivou o processo hoje de manhã."
            ],
            3: [
                "Isto já passou de investigação policial, rapaz. Isto é um abate encobrido por gente de alta patente. Se você tem apreço pela vida, não confie em ninguém de terno ou jaleco.",
                "Os poderosos desta cidade venderam a alma para o que quer que durma sob estas fundações. Não há justiça vindo lá de fora, Vane. Você está por conta própria."
            ]
        },
        "mob diretor": {
            "nome": "Diretor da Academia",
            "tipo": "diretor",
            1: [
                "Sr. Vane... Tudo neste colégio transcorre dentro da mais perfeita normalidade institucional. A Presidente Elara conduz o Grêmio com esmero admirável.",
                "Não me encare com essa insistência, Sr. Vane! Eu assino os relatórios que me colocam na frente... Eu não sei o que tem nos cofres subterrâneos e prefiro morrer sem saber!",
                "Se a senhorita von Weiss suspeitar que conversei com você sobre os orçamentos da enfermaria, ela manda os executores de casaco branco me limparem da folha de pagamento!"
            ],
            2: [
                "Por favor, não me faça indagações sobre as fichas de matrícula canceladas... Eu sou apenas um administrador assalariado. Se eu desagradar a senhorita Elara, serei descartado.",
                "E-eles instalaram trancas biométricas na minha própria sala da diretoria! Eu nem tenho mais acesso às fichas financeiras da mantenedora... Estou de mãos atadas!"
            ],
            3: [
                "E-ela tomou posse irrestrita do cofre e das chaves mestras... Eu não comando mais nada nesta academia, Sr. Vane! Somos todos reféns daquela tirana de sangue!",
                "O Conselho Estudantil assumiu o controle absoluto sob a lei marcial! Eles não precisam mais de um diretor de fachada... Meu Deus, o que vão fazer comigo?!"
            ]
        }
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def sortear_mob_por_local(local, horario):
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        import random
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        dia = getattr(store, "dia_atual", 1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if dia >= 15:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            ato = 3
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        elif dia >= 8:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            ato = 2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        else:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            ato = 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if local in ["dormitorio", "patio_fonte", "patio_arvore", "biblioteca"]:
            mobs_ids = ["mob calouro a", "mob caloura b", "mob calouro c", "mob veterana b", "mob veterano ocultista", "mob veterana ocultista"]
        elif local in ["sala_musica"]:
            mobs_ids = ["mob veterana b", "mob veterano c", "mob veterana ocultista", "mob caloura b"]
        elif local in ["enfermaria"]:
            mobs_ids = ["mob enfermeira", "mob calouro a", "mob caloura b", "mob veterano c"]
        elif local in ["sala_ocultismo", "banheiro_abandonado"]:
            mobs_ids = ["mob veterano ocultista", "mob veterana ocultista", "mob professor a", "mob veterano a"]
        elif local in ["cemiterio_nevoa"]:
            if horario == "Noite":
                mobs_ids = ["mob veterano ocultista", "mob veterana ocultista", "mob policial b", "mob policial c"]
            else:
                mobs_ids = ["mob veterano ocultista", "mob veterana ocultista", "mob professor a", "mob veterano a"]
        elif local in ["salao_gremio"]:
            mobs_ids = ["mob diretor", "mob professora b"]
        elif local in ["portoes_praca", "rua_portao"]:
            mobs_ids = ["mob policial a", "mob policial b", "mob policial c"]
        elif local in ["caldeiras", "sala_caldeiras", "bar_fada_verde"]:
            mobs_ids = ["mob veterano fundao", "mob veterana fundao", "mob veterano a", "mob calouro c"]
        elif local in ["catacumbas", "cripta_cofre", "subsolo_profundo"]:
            mobs_ids = ["mob veterano ocultista", "mob veterana ocultista", "mob veterano fundao", "mob veterana fundao", "mob professor a"]
        else:
            mobs_ids = ["mob veterano a", "mob veterana b", "mob veterano c", "mob calouro c", "mob professora b"]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        id_escolhido = random.choice(mobs_ids)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        mob_info = MOBS_LORE_DATABASE.get(id_escolhido)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        store.id_mob_atual = id_escolhido
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        store.nome_mob_atual = mob_info["nome"]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        store.tipo_mob_atual = mob_info["tipo"]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        store.sprite_mob_atual = obter_sprite_mob(id_escolhido)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        fala_cand = mob_info.get(ato, mob_info.get(1))
        if isinstance(fala_cand, list):
            fala_base = random.choice(fala_cand)
        else:
            fala_base = fala_cand
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        hum = getattr(store, "humanidade", 75)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if hum < 35:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            if mob_info["tipo"] in ["aluno", "doador", "veterano", "ocultismo"]:
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.fala_mob_atual = f"(O estudante treme incontrolavelmente e recua em pânico diante do brilho carmesim nos seus olhos e das suas presas proeminentes) 'P-por favor... misericórdia... não me machuque!... E-eu só sei que... {fala_base}'"
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            elif mob_info["tipo"] in ["professor", "diretor"]:
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.fala_mob_atual = f"(O docente recua contra a parede com a respiração trêmula ao sentir sua aura monstruosa) 'V-Vane?! O que... o que aconteceu com você?! Seus olhos... fique longe!... {fala_base}'"
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            else:
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.fala_mob_atual = f"(O oficial apoia a mão instintivamente no coldre, suando frio diante da sua presença predatória) 'Parado aí!... Que tipo de aberração é você?!... {fala_base}'"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        elif hum < 65:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            if mob_info["tipo"] in ["aluno", "doador", "veterano", "ocultismo"]:
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.fala_mob_atual = f"(O aluno repara no seu rosto cadavérico e nas olheiras fundas, hesitante) 'Victor? Você tá péssimo, cara... Tem um cheiro estranho de ferro em você... Enfim: {fala_base}'"
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            else:
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.fala_mob_atual = f"(Olhando com desconfiança para sua palidez doentia) 'Você não parece nada bem, rapaz... {fala_base}'"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        else:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            store.fala_mob_atual = fala_base

image lility vulneravel timida meio corpo = "images/lility/lility vulneravel timida meio corpo.webp"

image emilia uniforme seria investigativa meio corpo = "images/emilia/emilia com olhar investigativo.webp"
image emilia com olhar investigativo = "images/emilia/emilia com olhar investigativo.webp"

image elara uniforme serena meio corpo = "images/elara/elara uniforme observando meio corpo.webp"

image elara uniforme autoritaria meio corpo = "images/elara/elara uniforme arrogante meio corpo.webp"

image lility encarando sorrindo com boca fechada = "images/lility/lility encarando sorriindo com boca fechada.webp"
image lility encarando sorriindo com boca fechada = "images/lility/lility encarando sorriindo com boca fechada.webp"

image lility encarando com sorriso cabeça de lado = "images/lility/lility encarando com sorriso cabeca de lado.webp"
image lility encarando com sorriso cabeca de lado = "images/lility/lility encarando com sorriso cabeca de lado.webp"

image lility sorrindo com cabeça inclinada para cima = "images/lility/lility sorrindo com cabeca inclinada para cima.webp"
image lility sorrindo com cabeca inclinada para cima = "images/lility/lility sorrindo com cabeca inclinada para cima.webp"

image emilia com vergonha com a cabeça inclinada = "images/emilia/emilia com vergonha com a cabeca inclinada.webp"
image emilia com vergonha com a cabeca inclinada = "images/emilia/emilia com vergonha com a cabeca inclinada.webp"

image emilia olhando de frente neutra com cabeça inclinada = "images/emilia/emilia olhando de frente neutra com cabeca inclinada.webp"
image emilia olhando de frente neutra com cabeca inclinada = "images/emilia/emilia olhando de frente neutra com cabeca inclinada.webp"

image bg animado corredor academia manha sol = Movie(play="images/Background Wallpapers motions/bg animado corredor academia cortina sol.webm", size=(1920, 1080), loop=True)

default achado_grana = 0

default recompensa_dinheiro = 0

default grana_extorquida = 0

default margem_autocontrole = 50

default rolo_autocontrole = 50

default buff_sanguineo_nome = ""

default buff_sanguineo_tipo = ""

default buff_sanguineo_turnos = 0

default buff_sanguineo_dano = 0

default buff_sanguineo_defesa = 0

default buff_sanguineo_intelecto = 0

default buff_sanguineo_coragem = 0

default buff_sanguineo_sensibilidade = 0

default sangue_liturgico_ativo = False

init python:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    BANQUETE_OCULTO_TABELA = {

        "medico": {
            "nome_buff": "Sangue Antisséptico e Clínico",
            "sede_base": 30,
            "expo_base": 8,
            "humanidade_var": -2,
            "desc": "Sangue antisséptico e clínico (+30%% Saciedade, +20 HP de regeneração imediata e +1 Intelecto por 2 turnos).",
            "dano": 0, "defesa": 0, "intelecto": 1, "coragem": 0, "sensibilidade": 0
        },

        "doador": {

            "nome_buff": "Sangue Anêmico e Frio",

            "sede_base": 20,

            "expo_base": 0,

            "humanidade_var": -1,

            "desc": "Sangue anêmico e frio (+20%% Saciedade, 0%% Exposição adicional). A presa crê que a fraqueza é da coleta da enfermaria.",

            "dano": 0, "defesa": 0, "intelecto": 0, "coragem": 0, "sensibilidade": 0

        },

        "ocultismo": {

            "nome_buff": "Sangue Carregado de Éter",

            "sede_base": 30,

            "expo_base": 12,

            "humanidade_var": -1,

            "desc": "Gosto amargo de mirra e éter (+30%% Saciedade, +2 Sensibilidade Sobrenatural por 2 turnos | +1 Conhecimento Oculto).",

            "dano": 0, "defesa": 0, "intelecto": 0, "coragem": 0, "sensibilidade": 2

        },

        "ocultista": {

            "nome_buff": "Sangue Carregado de Éter",

            "sede_base": 30,

            "expo_base": 12,

            "humanidade_var": -1,

            "desc": "Gosto amargo de mirra e éter (+30%% Saciedade, +2 Sensibilidade Sobrenatural por 2 turnos | +1 Conhecimento Oculto).",

            "dano": 0, "defesa": 0, "intelecto": 0, "coragem": 0, "sensibilidade": 2

        },

        "fundao": {

            "nome_buff": "Sangue Rebelde e Abrasivo",

            "sede_base": 35,

            "expo_base": 14,

            "humanidade_var": -1,

            "desc": "Pulso quente de adrenalina e nicotina (+35%% Saciedade, +8 Dano em Combate e +1 Coragem por 2 turnos).",

            "dano": 8, "defesa": 0, "intelecto": 0, "coragem": 1, "sensibilidade": 0

        },

        "policial": {

            "nome_buff": "Sangue Adrenérgico de Ronda",

            "sede_base": 35,

            "expo_base": 22,

            "humanidade_var": -3,

            "desc": "Pulso febril e veloz (+35%% Saciedade, +10 Dano em Combate e +2 Coragem por 2 turnos | +22%% Exposição).",

            "dano": 10, "defesa": 0, "intelecto": 0, "coragem": 2, "sensibilidade": 0

        },

        "professor": {

            "nome_buff": "Sangue Cafeinado e Rígido",

            "sede_base": 25,

            "expo_base": 14,

            "humanidade_var": -2,

            "desc": "Sabor adstringente de café forte (+25%% Saciedade, +2 Intelecto por 2 turnos).",

            "dano": 0, "defesa": 0, "intelecto": 2, "coragem": 0, "sensibilidade": 0

        },

        "diretor": {

            "nome_buff": "Sangue Aristocrático Estressado",

            "sede_base": 30,

            "expo_base": 20,

            "humanidade_var": -2,

            "desc": "Sangue tenso de quem encobre sacrifícios (+30%% Saciedade, +2 Intelecto e +1 Domínio por 2 turnos).",

            "dano": 0, "defesa": 0, "intelecto": 2, "coragem": 0, "sensibilidade": 0

        },

        "veterano": {

            "nome_buff": "Sangue Calejado e Ácido",

            "sede_base": 30,

            "expo_base": 12,

            "humanidade_var": -2,

            "desc": "Gosto acre e calejado (+30%% Saciedade, +5 Defesa em Combate por 2 turnos).",

            "dano": 0, "defesa": 5, "intelecto": 0, "coragem": 0, "sensibilidade": 0

        },

        "aluno": {

            "nome_buff": "Sangue Jovem Comum",

            "sede_base": 30,

            "expo_base": 12,

            "humanidade_var": -2,

            "desc": "Sangue fresco e quente de estudante comum (+30%% Saciedade | +12%% Exposição | -2 Humanidade).",

            "dano": 0, "defesa": 0, "intelecto": 0, "coragem": 0, "sensibilidade": 0

        }

    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def aplicar_banquete_oculto(tipo_mob, silencioso=False):
        tipo = tipo_mob.lower() if tipo_mob else "aluno"
        dados = BANQUETE_OCULTO_TABELA.get(tipo, BANQUETE_OCULTO_TABELA["aluno"])

        ganho_sede = dados["sede_base"]
        if getattr(store, "clima_diario_id", "") == "campanha_doacao":
            ganho_sede += 15

        ganho_expo = 0 if silencioso else dados["expo_base"]
        if not silencioso and getattr(store, "clima_diario_id", "") == "inspecao_gremio" and ganho_expo > 0:
            ganho_expo += 10

        expo_reduzida_perk = False
        if not silencioso and "passos_silenciosos" in getattr(store, "perks_desbloqueados", ()) and ganho_expo > 0:
            ganho_expo = max(1, ganho_expo // 2)
            expo_reduzida_perk = True

        store.fome_sangue = min(100, store.fome_sangue + ganho_sede)
        if ganho_expo > 0:
            store.exposicao = min(100, store.exposicao + ganho_expo)
        store.humanidade = max(0, store.humanidade + dados["humanidade_var"])

        store.buff_sanguineo_nome = dados["nome_buff"]
        store.buff_sanguineo_tipo = tipo
        store.buff_sanguineo_turnos = 2
        store.buff_sanguineo_dano = dados["dano"]
        store.buff_sanguineo_defesa = dados["defesa"]
        store.buff_sanguineo_intelecto = dados["intelecto"]
        store.buff_sanguineo_coragem = dados["coragem"]
        store.buff_sanguineo_sensibilidade = dados["sensibilidade"]

        if tipo in ("ocultismo", "ocultista"):
            store.conhecimento_oculto += 1
        elif tipo == "diretor":
            store.dominio_jogador = getattr(store, "dominio_jogador", 0) + 1
        elif tipo == "medico":
            store.hp_jogador = min(getattr(store, "hp_jogador_max", 100), getattr(store, "hp_jogador", 100) + 20)

        if silencioso:
            desc_banquete = f"{dados['desc']} (Bote Silencioso: 0%% Exposição)"
        elif expo_reduzida_perk:
            desc_banquete = f"{dados['desc']} (Passos Silenciosos: Exposição +{ganho_expo}%%)"
        else:
            desc_banquete = dados["desc"]
        notificar_rpg("🩸 BANQUETE OCULTO", f"{dados['nome_buff']}: {desc_banquete}", "#ff3333")
        return desc_banquete
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def processar_decaimento_buffs_turno():
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if getattr(store, "buff_sanguineo_turnos", 0) > 0:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            store.buff_sanguineo_turnos -= 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            if store.buff_sanguineo_turnos <= 0:
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                nome_exp = getattr(store, "buff_sanguineo_nome", "")
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.buff_sanguineo_nome = ""
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.buff_sanguineo_tipo = ""
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.buff_sanguineo_dano = 0
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.buff_sanguineo_defesa = 0
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.buff_sanguineo_intelecto = 0
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.buff_sanguineo_coragem = 0
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                store.buff_sanguineo_sensibilidade = 0
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                notificar_rpg("💨 RESÍDUO DISSIPADO", f"O efeito de [[{nome_exp}]] se esvaiu das suas veias.", "#aaaaaa")

default tem_chave_dutos_nora = False

default nora_estabilizada_cripta = False

default nora_misericordia_concedida = False

image bg animado apocalipse cratera orb vermelha = Movie(play="images/Background Wallpapers motions/bg animado apocalipse cratera orb vermelha.webm", size=(1920, 1080), loop=True)

image bg animado bar grunge luzes neon = Movie(play="images/Background Wallpapers motions/bg animado bar grunge luzes neon.webm", size=(1920, 1080), loop=True)

image bg animado bar grunge taverna fogo verde = Movie(play="images/Background Wallpapers motions/bg animado bar grunge taverna fogo verde.webm", size=(1920, 1080), loop=True)

image bg animado caldeiras esconderijo tocha azul e fogo = Movie(play="images/Background Wallpapers motions/bg animado caldeiras esconderijo tocha azul e fogo.webm", size=(1920, 1080), loop=True)

image bg animado caldeiras loja pocoes tocha azul = Movie(play="images/Background Wallpapers motions/bg animado caldeiras loja pocoes tocha azul.webm", size=(1920, 1080), loop=True)

image bg animado corredor academia cortina sol = Movie(play="images/Background Wallpapers motions/bg animado corredor academia cortina sol.webm", size=(1920, 1080), loop=True)

image bg animado corredor academia entardecer sol = Movie(play="images/Background Wallpapers motions/bg animado corredor academia entardecer sol.webm", size=(1920, 1080), loop=True)

image bg animado corredor zona vermelha luzes de sangue = Movie(play="images/Background Wallpapers motions/bg animado corredor zona vermelha luzes de sangue.webm", size=(1920, 1080), loop=True)

image bg animado cripta cela vidro runas fechada = Movie(play="images/Background Wallpapers motions/bg animado cripta cela vidro runas fechada.webm", size=(1920, 1080), loop=True)

image bg animado dormitorio quarto manha raio sol = Movie(play="images/Background Wallpapers motions/bg animado dormitorio quarto manha raio sol.webm", size=(1920, 1080), loop=True)

image bg animado dormitorio quarto noite luar = Movie(play="images/Background Wallpapers motions/bg animado dormitorio quarto noite luar.webm", size=(1920, 1080), loop=True)

image bg animado dormitorio quarto tarde sol = Movie(play="images/Background Wallpapers motions/bg animado dormitorio quarto tarde sol.webm", size=(1920, 1080), loop=True)

image bg animado gabinete diretor dia cortinas = Movie(play="images/Background Wallpapers motions/bg animado gabinete diretor dia cortinas.webm", size=(1920, 1080), loop=True)

image bg animado gabinete diretor entardecer sol = Movie(play="images/Background Wallpapers motions/bg animado gabinete diretor entardecer sol.webm", size=(1920, 1080), loop=True)

image bg animado gabinete diretor noite candelabro = Movie(play="images/Background Wallpapers motions/bg animado gabinete diretor noite candelabro.webm", size=(1920, 1080), loop=True)

image bg animado patio claustro fonte dia = Movie(play="images/Background Wallpapers motions/bg animado patio claustro fonte dia.webm", size=(1920, 1080), loop=True)

image bg animado patio claustro fonte entardecer = Movie(play="images/Background Wallpapers motions/bg animado patio claustro fonte entardecer.webm", size=(1920, 1080), loop=True)

image bg animado patio claustro fonte noite = Movie(play="images/Background Wallpapers motions/bg animado patio claustro fonte noite.webm", size=(1920, 1080), loop=True)

image bg claustro patio fonte noite = Movie(play="images/Background Wallpapers motions/bg animado patio claustro fonte noite.webm", size=(1920, 1080), loop=True)

image bg animado sala aula ocultismo alquimia verde = Movie(play="images/Background Wallpapers motions/bg animado sala aula ocultismo alquimia verde.webm", size=(1920, 1080), loop=True)

image bg animado sala musica piano noite = Movie(play="images/Background Wallpapers motions/bg animado sala musica piano noite.webm", size=(1920, 1080), loop=True)

image bg animado sala musica piano vitral sol = Movie(play="images/Background Wallpapers motions/bg animado sala musica piano vitral sol.webm", size=(1920, 1080), loop=True)

image bg animado corredor escuro sombras = Movie(play="images/Background Wallpapers motions/bg animado corredor zona vermelha luzes de sangue.webm", size=(1920, 1080), loop=True)
image bg animado sala banquete sangue alucinacao = Movie(play="images/Background Wallpapers motions/bg animado gabinete diretor noite candelabro.webm", size=(1920, 1080), loop=True)

image bg animado cidade cyberpunk eclipse sol vermelho = Movie(play="images/Background Wallpapers motions/bg animado cidade cyberpunk eclipse sol vermelho.webm", size=(1920, 1080), loop=True)
image bg cidade cyberpunk eclipse sol vermelho = Movie(play="images/Background Wallpapers motions/bg animado cidade cyberpunk eclipse sol vermelho.webm", size=(1920, 1080), loop=True)

# --- CENÁRIOS ANIMADOS E ESTÁTICOS DA ENFERMARIA (MANHÃ, TARDE, NOITE, CHUVA) ---
image bg animado enfermaria manha = Movie(play="images/Background Wallpapers motions/bg animado enfermaria manha.webm", size=(1920, 1080), loop=True)
image bg animada enfermaria manha = Movie(play="images/Background Wallpapers motions/bg animado enfermaria manha.webm", size=(1920, 1080), loop=True)
image bg enfermaria manha = Transform("images/Background Wallpapers motions/bg enfermaria manha.webp", xysize=(1920, 1080), fit="cover")

image bg animado enfermaria tarde = Movie(play="images/Background Wallpapers motions/bg animado enfermaria tarde.webm", size=(1920, 1080), loop=True)
image bg animada enfermaria tarde = Movie(play="images/Background Wallpapers motions/bg animado enfermaria tarde.webm", size=(1920, 1080), loop=True)
image bg enfermaria tarde = Transform("images/Background Wallpapers motions/bg enfermaria tarde.webp", xysize=(1920, 1080), fit="cover")

image bg animado enfermaria noite = Movie(play="images/Background Wallpapers motions/bg animado enfermaria noite.webm", size=(1920, 1080), loop=True)
image bg animada enfermaria noite = Movie(play="images/Background Wallpapers motions/bg animado enfermaria noite.webm", size=(1920, 1080), loop=True)
image bg enfermaria noite = Transform("images/Background Wallpapers motions/bg enfermaria noite.webp", xysize=(1920, 1080), fit="cover")

image bg animado enfermaria chuva = Movie(play="images/Background Wallpapers motions/bg animado enfermaria chuva.webm", size=(1920, 1080), loop=True)
image bg animada enfermaria chuva = Movie(play="images/Background Wallpapers motions/bg animado enfermaria chuva.webm", size=(1920, 1080), loop=True)
image bg enfermaria chuva = Transform("images/Background Wallpapers motions/bg enfermaria chuva.webp", xysize=(1920, 1080), fit="cover")

image cain ataque espada rubra = "images/cain/corpo inteiro/cain ataque espada rubra.webp"
image phillip ataque lamina carmesim = "images/Phillip/corpo inteiro/phillip ataque lamina carmesim.webp"
image elara foice golpe corte ataque = "images/elara/corpo inteiro elara, apenas para batalha/elara foice golpe corte ataque.webp"
image elara foice corte horizontal ataque = "images/elara/corpo inteiro elara, apenas para batalha/elara foice corte horizontal ataque.webp"

# ==============================================================================
# FLAGS CANÔNICAS DE EXPANSÃO DE CONFLITOS & LORE (LILITY, NORA, ELARA, EMÍLIA, VALÉRIA)
# ==============================================================================
default ev_janela_lility_visto = False
default ev_fronteira_portoes_lility_visto = False
default ev_interceptacao_ponto_cego_lility_visto = False
default ev_visita_dormitorio_lility_visto = False
default ev_embate_dormitorio_lility_emilia_visto = False
default tomou_cha_emilia_periodo = False
default ev_embate_noturno_lility_emilia_visto = False
default ev_negociacao_lility_valeria_visto = False
default ev_triagem_enfermaria_visto = False
default ev_triagem_dia2_visto = False
default ev_halo_espelho_banheiro_visto = False
default ev_rastro_nora_enfermaria_visto = False
default rh_nulo_notificado_direcao = False
default ev_divida_teo_fase1_visto = False
default teo_salvo_segunda_parcela = False
default ev_voce_nao_come_visto = False
default ev_lista_rh_nulo_visto = False
default ev_escuta_decreto_elara_visto = False
default ev_relatorio_odores_elara_visto = False
default ev_fome_sem_plateia_valeria_visto = False
default ev_assinatura_tratado_phillip_visto = False

# ==============================================================================
# CONTROLE DE CADÊNCIA DIÁRIA, DIÁLOGOS DE HEROÍNAS & OBRIGAÇÕES ACADÊMICAS
# ==============================================================================
default emilia_curou_gaze_periodo = False
default transe_lility_periodo = False
default conversou_heroina_periodo = {}
default tocou_heroina_periodo = {}
default rumores_heroina_periodo = {}
default avisou_doom_lility_hoje = False
default avisou_doom_elara_hoje = False
default avisou_doom_emilia_hoje = False
default avisou_doom_valeria_hoje = False
default tarefa_academica_pendente = False
default tipo_tarefa_academica = "ensaio_alquimia"
default nome_tarefa_academica = "Ensaio de Filosofia Hermética & Alquimia dos Fluidos"
default prazo_tarefa_periodos = 0
default faltas_academicas = 0
default ciclo_academico_contador = 0

init -1 python:
    NOMES_LOCAIS = {
        "dormitorio": "Dormitório de Bolsistas",
        "patio_fonte": "Pátio do Claustro",
        "portoes_praca": "Praça dos Portões Centrais",
        "biblioteca": "Biblioteca Central",
        "sala_ocultismo": "Laboratório de Ocultismo",
        "enfermaria": "Enfermaria do Campus",
        "salao_gremio": "Salão do Conselho Estudantil",
        "sala_musica": "Sala de Música & Piano",
        "banheiro_abandonado": "Banheiro Interditado",
        "caldeiras": "Mercado Negro das Caldeiras",
        "sala_caldeiras": "Caldeiras Centrais",
        "bar_fada_verde": "Bar da Fada Verde",
        "cemiterio_nevoa": "Cemitério da Névoa",
        "catacumbas": "Catacumbas & Esgoto",
        "cripta_cofre": "Cripta Ancestral",
        "patio_arvore": "Pátio da Árvore Centenária",
        "rua_portao": "Avenida Externa do Campus"
    }

    def obter_nome_local(id_loc):
        return NOMES_LOCAIS.get(id_loc, str(id_loc).replace("_", " ").title())

init python:
    def sortear_nova_tarefa_academica():
        tarefas = [
            ("ensaio_alquimia", "Ensaio de Filosofia Hermética & Alquimia dos Fluidos", 4),
            ("plantao_biblioteca", "Catalogação dos Tomos Proibidos da Biblioteca", 5),
            ("frequencia_monitoria", "Relatório de Frequência e Monitoria do Conselho", 4),
            ("herbologia_capela", "Herbologia Eclesiástica e Infusões da Capela", 4)
        ]
        escolha = renpy.random.choice(tarefas)
        store.tarefa_academica_pendente = True
        store.tipo_tarefa_academica = escolha[0]
        store.nome_tarefa_academica = escolha[1]
        store.prazo_tarefa_periodos = escolha[2]

# Aliases visuais para cenas canônicas de Emília e Elara
image emilia uniforme severa meio corpo = "images/emilia/emilia com olhar investigativo.webp"
image emilia uniforme chocada meio corpo = "images/emilia/emilia uniforme surpresa meio corpo.webp"
image elara burocrata formal meio corpo = "images/elara/elara uniforme arrogante meio corpo.webp"
image elara sorriso frio meio corpo = "images/elara/elara sorrindo com desprezo encarando.webp"
image elara deboche xicara cha meio corpo = "images/elara/elara sorrindo de forma ironica.webp"
image elara seria autoritaria meio corpo = "images/elara/elara encarando com arrogancia e desprezo.webp"

# ==============================================================================
# DEFINIÇÕES CANÔNICAS DE SFX MASTERIZADOS (30 NOVOS EFEITOS SONOROS)
# ==============================================================================
define audio.sfx_passos_gravilha = "audio/sfx/sfx_passos_gravilha_patio.ogg"
define audio.sfx_passos_madeira = "audio/sfx/sfx_passos_madeira_ranger.ogg"
define audio.sfx_vasculhar_gaveta = "audio/sfx/sfx_vasculhar_gaveta_abrir.ogg"
define audio.sfx_vasculhar_objetos = "audio/sfx/sfx_vasculhar_objetos_mexer.ogg"
define audio.sfx_lamina_espada = "audio/sfx/sfx_lamina_espada_corte.ogg"
define audio.sfx_lamina_adaga = "audio/sfx/sfx_lamina_corte_rapido.ogg"
define audio.sfx_chicote_sangue = "audio/sfx/sfx_chicote_sangue_estalo.ogg"
define audio.sfx_tiro_pistola = "audio/sfx/sfx_tiro_pistola_seco.ogg"
define audio.sfx_tiro_escopeta = "audio/sfx/sfx_tiro_escopeta_reverberacao.ogg"
define audio.sfx_eletrochoque = "audio/sfx/sfx_eletricidade_arco_choque.ogg"
define audio.sfx_explosao_caldeira = "audio/sfx/sfx_explosao_caldeira_impacto.ogg"
define audio.sfx_golpe_esforco = "audio/sfx/sfx_combate_golpe_esforco.ogg"
define audio.sfx_besta_rosnado = "audio/sfx/sfx_besta_rosnado_ameaca.ogg"
define audio.sfx_monstro_triplo = "audio/sfx/sfx_monstro_rosnar_triplo.ogg"
define audio.sfx_besta_gemido = "audio/sfx/sfx_besta_dano_gemido.ogg"
define audio.sfx_aberracao_gosma = "audio/sfx/sfx_aberracao_gosma_rastejar.ogg"
define audio.sfx_ghoul_gargarejo = "audio/sfx/sfx_ghoul_gargarejo_fome.ogg"
define audio.sfx_zumbi_morte = "audio/sfx/sfx_zumbi_morte_estertor.ogg"
define audio.sfx_sangue_borbulhar = "audio/sfx/sfx_sangue_viscoso_borbulhar.ogg"
define audio.sfx_fratura_mordida = "audio/sfx/sfx_fratura_osso_mordida.ogg"
define audio.sfx_nevoeiro_uivo = "audio/sfx/sfx_nevoeiro_uivo_criatura.ogg"
define audio.sfx_item_coletado = "audio/sfx/sfx_ui_item_coletado.ogg"
define audio.sfx_dossie_carta = "audio/sfx/sfx_dossie_carta_deslizar.ogg"
define audio.sfx_inventario_pasta = "audio/sfx/sfx_inventario_abrir_pasta.ogg"
define audio.sfx_moedas_ouro = "audio/sfx/sfx_moedas_ouro_transacao.ogg"
define audio.sfx_moedas_tilintar = "audio/sfx/sfx_moedas_tilintar.ogg"
define audio.sfx_dado_rpg = "audio/sfx/sfx_dado_rolagem_rpg.ogg"
define audio.sfx_frasco_vidro = "audio/sfx/sfx_frasco_alquimia_vidro.ogg"
define audio.sfx_distorcao_psiquica = "audio/sfx/sfx_psiquico_distorcao_sanidade.ogg"
define audio.sfx_pena_anotacao = "audio/sfx/sfx_pena_anotacao_pista.ogg"

# --- REPERTÓRIO COMPLETO DE SPRITES DE ELARA VON WEISS ---
image elara com prazer = "images/elara/elara com prazer.webp"
image elara combate avanco = "images/elara/corpo inteiro elara, apenas para batalha/elara combate avanco.webp"
image elara combate desarmada = "images/elara/corpo inteiro elara, apenas para batalha/elara combate desarmada.webp"
image elara combate salto = "images/elara/corpo inteiro elara, apenas para batalha/elara combate salto.webp"
image elara deboche sarcastica corpo inteiro = "images/elara/corpo inteiro elara, apenas para batalha/elara deboche sarcastica corpo inteiro.webp"
image elara derrotada = "images/elara/elara derrotada.webp"
image elara derrotada ajoelhada = "images/elara/corpo inteiro elara, apenas para batalha/elara derrotada ajoelhada.webp"
image elara derrotada encarando = "images/elara/elara derrotada encarando.webp"
image elara encarando com arrogancia e desprezo = "images/elara/elara encarando com arrogancia e desprezo.webp"
image elara encarando de cima para baixo = "images/elara/elara encarando de cima para baixo.webp"
image elara encarando de forma astuta = "images/elara/elara encarando de forma astuta.webp"
image elara encarando de forma astuta alt = "images/elara/elara encarando de forma astuta alt.webp"
image elara encarando neutra = "images/elara/elara encarando neutra.webp"
image elara encarando neutra com cabeca inclinada = "images/elara/elara encarando neutra com cabeca inclinada.webp"
image elara encarando neutra e de lado = "images/elara/elara encarando neutra e de lado.webp"
image elara encarando sorrindo = "images/elara/elara encarando sorrindo.webp"
image elara foice batalha andando = "images/elara/corpo inteiro elara, apenas para batalha/elara foice batalha andando.webp"
image elara foice batalha arrogante = "images/elara/corpo inteiro elara, apenas para batalha/elara foice batalha arrogante.webp"
image elara foice batalha preparada = "images/elara/corpo inteiro elara, apenas para batalha/elara foice batalha preparada.webp"
image elara foice batalha preparada ataque = "images/elara/corpo inteiro elara, apenas para batalha/elara foice batalha preparada ataque.webp"
image elara irritada e com desprezo = "images/elara/elara irritada e com desprezo.webp"
image elara irritada e com desprezo alt = "images/elara/elara irritada e com desprezo alt.webp"
image elara muito irritada = "images/elara/elara muito irritada.webp"
image elara neutra acenando corpo inteiro = "images/elara/corpo inteiro elara, apenas para batalha/elara neutra acenando corpo inteiro.webp"
image elara neutra encarando = "images/elara/elara neutra encarando.webp"
image elara severa olhar sarcasmo = "images/elara/corpo inteiro elara, apenas para batalha/elara severa olhar sarcasmo.webp"
image elara sorrindo com arrogancia = "images/elara/elara sorrindo com arrogancia.webp"
image elara sorrindo com desprezo encarando = "images/elara/elara sorrindo com desprezo encarando.webp"
image elara sorrindo com rosto arrogante = "images/elara/elara sorrindo com rosto arrogante.webp"
image elara sorrindo de forma ironica = "images/elara/elara sorrindo de forma ironica.webp"
image elara superioridade sorriso corpo inteiro = "images/elara/corpo inteiro elara, apenas para batalha/elara superioridade sorriso corpo inteiro.webp"
image elara uniforme arrogante meio corpo = "images/elara/elara uniforme arrogante meio corpo.webp"
image elara uniforme observando meio corpo = "images/elara/elara uniforme observando meio corpo.webp"

# --- REPERTÓRIO COMPLETO DE SPRITES DE LILITY (LYRA VON BLUT) ---
image lility bracos cruzados seria meio corpo = "images/lility/lility bracos cruzados seria meio corpo.webp"
image lility brava encarando = "images/lility/lility brava encarando.webp"
image lility com receio = "images/lility/lility com receio.webp"
image lility com vergonha = "images/lility/lility com vergonha.webp"
image lility com vergonha olhando de cima = "images/lility/lility com vergonha olhando de cima.webp"
image lility com vergonha olhando de lado = "images/lility/lility com vergonha olhando de lado.webp"
image lility comportada sorriso meio corpo = "images/lility/lility comportada sorriso meio corpo.webp"
image lility confiante sorriso meio corpo = "images/lility/lility confiante sorriso meio corpo.webp"
image lility dinamica sorriso meio corpo = "images/lility/lility dinamica sorriso meio corpo.webp"
image lility encarando brava = "images/lility/lility encarando brava.webp"
image lility encarando com olhar unico = "images/lility/lility encarando com olhar unico.webp"
image lility encarando com sorriso = "images/lility/lility encarando com sorriso.webp"
image lility encarando convencida = "images/lility/lility encarando convencida.webp"
image lility encarando desafiadoramente = "images/lility/lility encarando desafiadoramente.webp"
image lility encarando receosa = "images/lility/lility encarando receosa.webp"
image lility neutra relaxada corpo inteiro = "images/lility/corpo inteiro/lility neutra relaxada corpo inteiro.webp"
image lility olhando de frente = "images/lility/lility olhando de frente.webp"
image lility presas agressiva meio corpo = "images/lility/lility presas agressiva meio corpo.webp"
image lility presas sorriso corpo inteiro = "images/lility/corpo inteiro/lility presas sorriso corpo inteiro.webp"
image lility provocante pose corpo inteiro = "images/lility/corpo inteiro/lility provocante pose corpo inteiro.webp"
image lility receio e com dor = "images/lility/lility receio e com dor.webp"
image lility sedutora provocante corpo inteiro = "images/lility/corpo inteiro/lility sedutora provocante corpo inteiro.webp"
image lility sorrindo alegre = "images/lility/lility sorrindo alegre.webp"
image lility sorrindo com olhar unico = "images/lility/lility sorrindo com olhar unico.webp"
image lility sorrindo com olhos penetrantes = "images/lility/lility sorrindo com olhos penetrantes.webp"
image lility sorrindo com rosto rosado = "images/lility/lility sorrindo com rosto rosado.webp"
image lility sorrindo contente = "images/lility/lility sorrindo contente.webp"
image lility sorrindo de lado sorrindo = "images/lility/lility sorrindo de lado sorrindo.webp"
image lility sorrindo de leve encarando = "images/lility/lility sorrindo de leve encarando.webp"
image lility sorrindo encarando = "images/lility/lility sorrindo encarando.webp"
image lility sorrindo feliz = "images/lility/lility sorrindo feliz.webp"
image lility sorriso presas aberto meio corpo = "images/lility/lility sorriso presas aberto meio corpo.webp"

# --- REPERTÓRIO COMPLETO DE SPRITES DE EMÍLIA ---
image emilia arrumando os oculos com vergonha = "images/emilia/emilia arrumando os oculos com vergonha.webp"
image emilia camisa aberta nsfw corada = "images/emilia/emilia camisa aberta nsfw corada.webp"
image emilia camisa aberta nsfw corpo inteiro = "images/emilia/emilia camisa aberta nsfw corpo inteiro.webp"
image emilia camisa aberta nsfw sentada = "images/emilia/emilia camisa aberta nsfw sentada.webp"
image emilia camisa aberta nsfw timida = "images/emilia/emilia camisa aberta nsfw timida.webp"
image emilia camisa caida nsfw timida = "images/emilia/emilia camisa caida nsfw timida.webp"
image emilia com vergonha = "images/emilia/emilia com vergonha.webp"
image emilia com vergonha arrumando o oculos e olhando para o lado = "images/emilia/emilia com vergonha arrumando o oculos e olhando para o lado.webp"
image emilia com vergonha arrumando o oculos e olhando para o lado e fofa = "images/emilia/emilia com vergonha arrumando o oculos e olhando para o lado e fofa.webp"
image emilia com vergonha e fofa = "images/emilia/emilia com vergonha e fofa.webp"
image emilia com vergonha olhando para baixo = "images/emilia/emilia com vergonha olhando para baixo.webp"
image emilia derrotada = "images/emilia/corpo inteiro apenas para batalha/emilia derrotada.webp"
image emilia encarando seria = "images/emilia/emilia encarando seria.webp"
image emilia encarando seria neutra = "images/emilia/emilia encarando seria neutra.webp"
image emilia excitada encarando = "images/emilia/emilia excitada encarando.webp"
image emilia excitada encarando com a cabeca inclinada = "images/emilia/emilia excitada encarando com a cabeca inclinada.webp"
image emilia excitada encarando com prazer = "images/emilia/emilia excitada encarando com prazer.webp"
image emilia exorcista sobretudo corpo inteiro = "images/emilia/corpo inteiro apenas para batalha/emilia exorcista sobretudo corpo inteiro.webp"
image emilia olhando de frente neutra = "images/emilia/emilia olhando de frente neutra.webp"
image emilia preocupada = "images/emilia/emilia preocupada.webp"
image emilia preocupada olhando para baixo = "images/emilia/emilia preocupada olhando para baixo.webp"
image emilia preocupada olhando pro lado = "images/emilia/emilia preocupada olhando pro lado.webp"
image emilia sobretudo bolsa corpo inteiro = "images/emilia/corpo inteiro apenas para batalha/emilia sobretudo bolsa corpo inteiro.webp"
image emilia sorriso com vergonha = "images/emilia/emilia sorriso com vergonha.webp"
image emilia sorriso com vergonha de frente = "images/emilia/emilia sorriso com vergonha de frente.webp"
image emilia triste encarando = "images/emilia/emilia triste encarando.webp"
image emilia triste encarando e com lagrimas = "images/emilia/emilia triste encarando e com lagrimas.webp"
image emilia uniforme ajeitando oculos meio corpo = "images/emilia/emilia uniforme ajeitando oculos meio corpo.webp"
image emilia uniforme bolsa corpo inteiro = "images/emilia/corpo inteiro apenas para batalha/emilia uniforme bolsa corpo inteiro.webp"
image emilia uniforme calma meio corpo = "images/emilia/emilia uniforme calma meio corpo.webp"
image emilia uniforme confiante meio corpo = "images/emilia/emilia uniforme confiante meio corpo.webp"
image emilia uniforme corada timida meio corpo = "images/emilia/emilia uniforme corada timida meio corpo.webp"
image emilia uniforme gentil meio corpo = "images/emilia/emilia uniforme gentil meio corpo.webp"
image emilia uniforme inclinada fofa meio corpo = "images/emilia/emilia uniforme inclinada fofa meio corpo.webp"
image emilia uniforme neutra bolsa corpo inteiro = "images/emilia/corpo inteiro apenas para batalha/emilia uniforme neutra bolsa corpo inteiro.webp"
image emilia uniforme neutra meio corpo = "images/emilia/emilia uniforme neutra meio corpo.webp"
image emilia uniforme oculos corpo inteiro = "images/emilia/corpo inteiro apenas para batalha/emilia uniforme oculos corpo inteiro.webp"
image emilia uniforme perfil sorriso meio corpo = "images/emilia/emilia uniforme perfil sorriso meio corpo.webp"
image emilia uniforme serena meio corpo = "images/emilia/emilia uniforme serena meio corpo.webp"
image emilia uniforme sorriso amigavel meio corpo = "images/emilia/emilia uniforme sorriso amigavel meio corpo.webp"
image emilia uniforme sorriso timido meio corpo = "images/emilia/emilia uniforme sorriso timido meio corpo.webp"
image emilia uniforme surpresa meio corpo = "images/emilia/emilia uniforme surpresa meio corpo.webp"

# --- REPERTÓRIO COMPLETO DE SPRITES DE VALÉRIA ---
image valeria agachada mao cabelo = "images/valeria/valeria agachada mao cabelo.webp"
image valeria agachada sorriso gentil = "images/valeria/valeria agachada sorriso gentil.webp"
image valeria amigavel neutra meio corpo = "images/valeria/valeria amigavel neutra meio corpo.webp"
image valeria camisa branca suspensorios corpo inteiro = "images/valeria/corpo inteiro/valeria camisa branca suspensorios corpo inteiro.webp"
image valeria casaco caqui descontraida corpo inteiro = "images/valeria/corpo inteiro/valeria casaco caqui descontraida corpo inteiro.webp"
image valeria casaco caqui postura firme corpo inteiro = "images/valeria/corpo inteiro/valeria casaco caqui postura firme corpo inteiro.webp"
image valeria casaco preto botas perfil corpo inteiro = "images/valeria/corpo inteiro/valeria casaco preto botas perfil corpo inteiro.webp"
image valeria casaco verde corpo inteiro = "images/valeria/corpo inteiro/valeria casaco verde corpo inteiro.webp"
image valeria casaco verde gentil meio corpo = "images/valeria/valeria amigavel neutra meio corpo.webp"
image valeria casaco verde sorriso meio corpo = "images/valeria/valeria descontraida sorriso meio corpo.webp"
image valeria cinica confiante meio corpo = "images/valeria/valeria cinica pirulito meio corpo.webp"
image valeria cinica pirulito meio corpo = "images/valeria/valeria cinica pirulito meio corpo.webp"
image valeria cinica suspensorios meio corpo = "images/valeria/valeria cinica suspensorios meio corpo.webp"
image valeria conceito frente costas = "images/valeria/corpo inteiro/valeria conceito frente costas.webp"
image valeria confusa interrogacao = "images/valeria/valeria pensativa perfil meio corpo.webp"
image valeria corpo inteiro botas inclinada = "images/valeria/corpo inteiro/valeria corpo inteiro botas inclinada.webp"
image valeria corpo inteiro botas mao cintura = "images/valeria/corpo inteiro/valeria corpo inteiro botas mao cintura.webp"
image valeria corpo inteiro botas maos bolsos = "images/valeria/corpo inteiro/valeria corpo inteiro botas maos bolsos.webp"
image valeria corpo inteiro botas neutra = "images/valeria/corpo inteiro/valeria corpo inteiro botas neutra.webp"
image valeria deboche sonolenta meio corpo = "images/valeria/valeria deboche sonolenta meio corpo.webp"
image valeria descontraida sorriso meio corpo = "images/valeria/valeria descontraida sorriso meio corpo.webp"
image valeria ficha design conceito = "images/valeria/corpo inteiro/valeria ficha design conceito.webp"
image valeria frascos sorriso meio corpo = "images/valeria/valeria frascos sorriso meio corpo.webp"
image valeria jaqueta pins corpo inteiro = "images/valeria/corpo inteiro/valeria jaqueta pins corpo inteiro.webp"
image valeria jaqueta pins corpo inteiro 2k = "images/valeria/corpo inteiro/valeria jaqueta pins corpo inteiro 2k.webp"
image valeria jaqueta pins corpo inteiro 2k alt = "images/valeria/corpo inteiro/valeria jaqueta pins corpo inteiro 2k alt.webp"
image valeria leve sorriso pirulito meio corpo = "images/valeria/valeria leve sorriso pirulito meio corpo.webp"
image valeria neutra direta meio corpo = "images/valeria/valeria seria neutra meio corpo.webp"
image valeria neutra pirulito meio corpo = "images/valeria/valeria neutra pirulito meio corpo.webp"
image valeria nsfw sem short foco bunda = "images/valeria/corpo inteiro/valeria nsfw sem short foco bunda.webp"
image valeria nsfw sem short foco bunda completo = "images/valeria/corpo inteiro/valeria nsfw sem short foco bunda completo.webp"
image valeria nsfw short foco bunda = "images/valeria/corpo inteiro/valeria nsfw short foco bunda.webp"
image valeria nsfw short foco bunda com jaqueta = "images/valeria/corpo inteiro/valeria nsfw short foco bunda com jaqueta.webp"
image valeria nsfw short foco bunda de lado = "images/valeria/corpo inteiro/valeria nsfw short foco bunda de lado.webp"
image valeria olhar focado meio corpo = "images/valeria/valeria olhar focado meio corpo.webp"
image valeria pensativa perfil meio corpo = "images/valeria/valeria pensativa perfil meio corpo.webp"
image valeria perfil sorriso provocador meio corpo = "images/valeria/valeria perfil sorriso provocador meio corpo.webp"
image valeria seria mochila frascos meio corpo = "images/valeria/valeria seria mochila frascos meio corpo.webp"
image valeria seria neutra meio corpo = "images/valeria/valeria seria neutra meio corpo.webp"
image valeria shorts cropped busto perfil = "images/valeria/valeria shorts cropped busto perfil.webp"
image valeria shorts cropped cinica corpo inteiro = "images/valeria/corpo inteiro/valeria shorts cropped cinica corpo inteiro.webp"
image valeria shorts cropped descolada corpo inteiro = "images/valeria/corpo inteiro/valeria shorts cropped descolada corpo inteiro.webp"
image valeria shorts cropped seria corpo inteiro = "images/valeria/corpo inteiro/valeria shorts cropped seria corpo inteiro.webp"
image valeria sorriso provocante pirulito meio corpo = "images/valeria/valeria sorriso provocante pirulito meio corpo.webp"

# --- SPRITES DE MOBS E FIGURANTES ---
image aluna feminina veterana ocultista = "images/mobs/aluna feminina veterana ocultista.webp"
image aluna feminina veterana ocultista brava = "images/mobs/aluna feminina veterana ocultista brava.webp"
image aluna feminina veterana ocultista medo = "images/mobs/aluna feminina veterana ocultista medo.webp"
image aluna feminina veterana ocultista neutra = "images/mobs/aluna feminina veterana ocultista neutra.webp"
image aluna feminina veterana ocultista sorrindo = "images/mobs/aluna feminina veterana ocultista sorrindo.webp"
image aluna feminina veterana ocultista transe hipnotico = "images/mobs/aluna feminina veterana ocultista transe hipnotico.webp"
image aluna feminina veterana turma do fundao = "images/mobs/aluna feminina veterana turma do fundao.webp"
image aluna feminina veterana turma do fundao brava = "images/mobs/aluna feminina veterana turma do fundao brava.webp"
image aluna feminina veterana turma do fundao medo = "images/mobs/aluna feminina veterana turma do fundao medo.webp"
image aluna feminina veterana turma do fundao neutra = "images/mobs/aluna feminina veterana turma do fundao neutra.webp"
image aluna feminina veterana turma do fundao sorrindo = "images/mobs/aluna feminina veterana turma do fundao sorrindo.webp"
image aluna feminina veterana turma do fundao transe hipnotico = "images/mobs/aluna feminina veterana turma do fundao transe hipnotico.webp"
image aluno masculino veterano a do fundao = "images/mobs/aluno masculino veterano a do fundao.webp"
image aluno masculino veterano a do fundao bravo = "images/mobs/aluno masculino veterano a do fundao bravo.webp"
image aluno masculino veterano a do fundao medo = "images/mobs/aluno masculino veterano a do fundao medo.webp"
image aluno masculino veterano a do fundao neutro = "images/mobs/aluno masculino veterano a do fundao neutro.webp"
image aluno masculino veterano a do fundao sorrindo = "images/mobs/aluno masculino veterano a do fundao sorrindo.webp"
image aluno masculino veterano a do fundao transe hipnotico = "images/mobs/aluno masculino veterano a do fundao transe hipnotico.webp"
image aluno masculino veterano b do fundao = "images/mobs/aluno masculino veterano b do fundao.webp"
image aluno masculino veterano b do fundao bravo = "images/mobs/aluno masculino veterano b do fundao bravo.webp"
image aluno masculino veterano b do fundao medo = "images/mobs/aluno masculino veterano b do fundao medo.webp"
image aluno masculino veterano b do fundao neutro = "images/mobs/aluno masculino veterano b do fundao neutro.webp"
image aluno masculino veterano b do fundao sorrindo = "images/mobs/aluno masculino veterano b do fundao sorrindo.webp"
image aluno masculino veterano b do fundao transe hipnotico = "images/mobs/aluno masculino veterano b do fundao transe hipnotico.webp"
image aluno masculino veterano ocultista = "images/mobs/aluno masculino veterano ocultista.webp"
image aluno masculino veterano ocultista bravo = "images/mobs/aluno masculino veterano ocultista bravo.webp"
image aluno masculino veterano ocultista medo = "images/mobs/aluno masculino veterano ocultista medo.webp"
image aluno masculino veterano ocultista neutro = "images/mobs/aluno masculino veterano ocultista neutro.webp"
image aluno masculino veterano ocultista sorrindo = "images/mobs/aluno masculino veterano ocultista sorrindo.webp"
image aluno masculino veterano ocultista transe hipnotico = "images/mobs/aluno masculino veterano ocultista transe hipnotico.webp"
image enfermeira feminina ameacadora = "images/mobs/enfermeira feminina ameacadora.webp"
image enfermeira feminina desconfiada = "images/mobs/enfermeira feminina desconfiada.png"
image enfermeira feminina irritada = "images/mobs/enfermeira feminina irritada.png"
image enfermeira feminina medo = "images/mobs/enfermeira feminina medo.png"
image enfermeira feminina neutra = "images/mobs/enfermeira feminina neutra.png"
image enfermeira feminina sorrindo = "images/mobs/enfermeira feminina sorrindo.png"
image enfermeira feminina transe hipnotico = "images/mobs/enfermeira feminina transe hipnotico.png"
image mob caloura b brava = "images/mobs/mob caloura b brava.webp"
image mob caloura b irritada = "images/mobs/mob caloura b irritada.webp"
image mob caloura b medo = "images/mobs/mob caloura b medo.webp"
image mob caloura b neutro = "images/mobs/mob caloura b neutro.webp"
image mob caloura b sorrindo = "images/mobs/mob caloura b sorrindo.webp"
image mob caloura b transe = "images/mobs/mob caloura b transe.webp"
image mob caloura b transe hipnotico = "images/mobs/mob caloura b transe hipnotico.webp"
image mob calouro a bravo = "images/mobs/mob calouro a bravo.webp"
image mob calouro a irritado = "images/mobs/mob calouro a irritado.webp"
image mob calouro a medo = "images/mobs/mob calouro a medo.webp"
image mob calouro a neutro = "images/mobs/mob calouro a neutro.webp"
image mob calouro a sorrindo = "images/mobs/mob calouro a sorrindo.webp"
image mob calouro a transe = "images/mobs/mob calouro a transe.webp"
image mob calouro a transe hipnotico = "images/mobs/mob calouro a transe hipnotico.webp"
image mob calouro c bravo = "images/mobs/mob calouro c bravo.webp"
image mob calouro c irritado = "images/mobs/mob calouro c irritado.webp"
image mob calouro c medo = "images/mobs/mob calouro c medo.webp"
image mob calouro c neutro = "images/mobs/mob calouro c neutro.webp"
image mob calouro c sorrindo = "images/mobs/mob calouro c sorrindo.webp"
image mob calouro c transe = "images/mobs/mob calouro c transe.webp"
image mob calouro c transe hipnotico = "images/mobs/mob calouro c transe hipnotico.webp"
image mob diretor encarando = "images/mobs/mob diretor encarando.webp"
image mob diretor encarando medo = "images/mobs/mob diretor encarando medo.webp"
image mob diretor irritado = "images/mobs/mob diretor irritado.webp"
image mob diretor irritado encarando = "images/mobs/mob diretor irritado encarando.webp"
image mob diretor medo = "images/mobs/mob diretor medo.webp"
image mob diretor neutro = "images/mobs/mob diretor neutro.webp"
image mob diretor transe = "images/mobs/mob diretor transe.webp"
image mob diretor transe hipnotico = "images/mobs/mob diretor transe hipnotico.webp"
image mob enfermeira ameacadora = "images/mobs/mob enfermeira ameacadora.webp"
image mob enfermeira brava = "images/mobs/mob enfermeira brava.webp"
image mob enfermeira desconfiada = "images/mobs/mob enfermeira desconfiada.webp"
image mob enfermeira irritada = "images/mobs/mob enfermeira irritada.webp"
image mob enfermeira medo = "images/mobs/mob enfermeira medo.webp"
image mob enfermeira neutra = "images/mobs/mob enfermeira neutra.webp"
image mob enfermeira neutro = "images/mobs/mob enfermeira neutro.webp"
image mob enfermeira sorrindo = "images/mobs/mob enfermeira sorrindo.webp"
image mob enfermeira transe = "images/mobs/mob enfermeira transe.webp"
image mob enfermeira transe hipnotico = "images/mobs/mob enfermeira transe hipnotico.webp"
image mob femenina caloura b = "images/mobs/mob femenina caloura b.webp"
image mob femenina caloura b transe hipnotico = "images/mobs/mob femenina caloura b transe hipnotico.webp"
image mob femenina policial b = "images/mobs/mob femenina policial b.webp"
image mob femenina policial b brava = "images/mobs/mob femenina policial b brava.webp"
image mob femenina policial b incomodada = "images/mobs/mob femenina policial b incomodada.webp"
image mob femenina policial b medo = "images/mobs/mob femenina policial b medo.webp"
image mob femenina policial b sorrindo = "images/mobs/mob femenina policial b sorrindo.webp"
image mob femenina policial b transe hipnotico = "images/mobs/mob femenina policial b transe hipnotico.webp"
image mob femenina professora b = "images/mobs/mob femenina professora b.webp"
image mob femenina professora b brava = "images/mobs/mob femenina professora b brava.webp"
image mob femenina professora b medo = "images/mobs/mob femenina professora b medo.webp"
image mob femenina professora b sorrindo = "images/mobs/mob femenina professora b sorrindo.webp"
image mob femenina professora b transe hipnotico = "images/mobs/mob femenina professora b transe hipnotico.webp"
image mob femenina veterana b = "images/mobs/mob femenina veterana b.webp"
image mob femenina veterana b medo = "images/mobs/mob femenina veterana b medo.webp"
image mob femenina veterana b sorrindo = "images/mobs/mob femenina veterana b sorrindo.webp"
image mob femenina veterana b transe hipnotico = "images/mobs/mob femenina veterana b transe hipnotico.webp"
image mob masculino calouro a = "images/mobs/mob masculino calouro a.webp"
image mob masculino calouro a irritado = "images/mobs/mob masculino calouro a irritado.webp"
image mob masculino calouro a medo = "images/mobs/mob masculino calouro a medo.webp"
image mob masculino calouro a sorrindo = "images/mobs/mob masculino calouro a sorrindo.webp"
image mob masculino calouro a transe hipnotico = "images/mobs/mob masculino calouro a transe hipnotico.webp"
image mob masculino calouro c = "images/mobs/mob masculino calouro c.webp"
image mob masculino calouro c bravo = "images/mobs/mob masculino calouro c bravo.webp"
image mob masculino calouro c medo = "images/mobs/mob masculino calouro c medo.webp"
image mob masculino calouro c sorrindo = "images/mobs/mob masculino calouro c sorrindo.webp"
image mob masculino calouro c transe hipnotico = "images/mobs/mob masculino calouro c transe hipnotico.webp"
image mob masculino diretor encarando = "images/mobs/mob masculino diretor encarando.webp"
image mob masculino diretor encarando medo = "images/mobs/mob masculino diretor encarando medo.webp"
image mob masculino diretor irritado encarando = "images/mobs/mob masculino diretor irritado encarando.webp"
image mob masculino diretor neutro = "images/mobs/mob masculino diretor neutro.webp"
image mob masculino diretor transe hipnotico = "images/mobs/mob masculino diretor transe hipnotico.webp"
image mob masculino policial a = "images/mobs/mob masculino policial a.webp"
image mob masculino policial a bravo = "images/mobs/mob masculino policial a bravo.webp"
image mob masculino policial a medo = "images/mobs/mob masculino policial a medo.webp"
image mob masculino policial a sorrindo = "images/mobs/mob masculino policial a sorrindo.webp"
image mob masculino policial a transe hipnotico = "images/mobs/mob masculino policial a transe hipnotico.webp"
image mob masculino policial c = "images/mobs/mob masculino policial c.webp"
image mob masculino policial c bravo = "images/mobs/mob masculino policial c bravo.webp"
image mob masculino policial c medo = "images/mobs/mob masculino policial c medo.webp"
image mob masculino policial c sorrindo = "images/mobs/mob masculino policial c sorrindo.webp"
image mob masculino policial c transe hipnotico = "images/mobs/mob masculino policial c transe hipnotico.webp"
image mob masculino professor a = "images/mobs/mob masculino professor a.webp"
image mob masculino professor a bravo = "images/mobs/mob masculino professor a bravo.webp"
image mob masculino professor a incomodado = "images/mobs/mob masculino professor a incomodado.webp"
image mob masculino professor a medo = "images/mobs/mob masculino professor a medo.webp"
image mob masculino professor a sorrindo = "images/mobs/mob masculino professor a sorrindo.webp"
image mob masculino professor a transe hipnotico = "images/mobs/mob masculino professor a transe hipnotico.webp"
image mob masculino veterano a = "images/mobs/mob masculino veterano a.webp"
image mob masculino veterano a bravo = "images/mobs/mob masculino veterano a bravo.webp"
image mob masculino veterano a incomodado = "images/mobs/mob masculino veterano a incomodado.webp"
image mob masculino veterano a medo = "images/mobs/mob masculino veterano a medo.webp"
image mob masculino veterano a sorrindo = "images/mobs/mob masculino veterano a sorrindo.webp"
image mob masculino veterano a transe hipnotico = "images/mobs/mob masculino veterano a transe hipnotico.webp"
image mob policial a bravo = "images/mobs/mob policial a bravo.webp"
image mob policial a irritado = "images/mobs/mob policial a irritado.webp"
image mob policial a medo = "images/mobs/mob policial a medo.webp"
image mob policial a neutro = "images/mobs/mob policial a neutro.webp"
image mob policial a sorrindo = "images/mobs/mob policial a sorrindo.webp"
image mob policial a transe = "images/mobs/mob policial a transe.webp"
image mob policial a transe hipnotico = "images/mobs/mob policial a transe hipnotico.webp"
image mob policial b brava = "images/mobs/mob policial b brava.webp"
image mob policial b incomodada = "images/mobs/mob policial b incomodada.webp"
image mob policial b irritada = "images/mobs/mob policial b irritada.webp"
image mob policial b medo = "images/mobs/mob policial b medo.webp"
image mob policial b neutro = "images/mobs/mob policial b neutro.webp"
image mob policial b sorrindo = "images/mobs/mob policial b sorrindo.webp"
image mob policial b transe = "images/mobs/mob policial b transe.webp"
image mob policial b transe hipnotico = "images/mobs/mob policial b transe hipnotico.webp"
image mob policial c bravo = "images/mobs/mob policial c bravo.webp"
image mob policial c irritado = "images/mobs/mob policial c irritado.webp"
image mob policial c medo = "images/mobs/mob policial c medo.webp"
image mob policial c neutro = "images/mobs/mob policial c neutro.webp"
image mob policial c sorrindo = "images/mobs/mob policial c sorrindo.webp"
image mob policial c transe = "images/mobs/mob policial c transe.webp"
image mob policial c transe hipnotico = "images/mobs/mob policial c transe hipnotico.webp"
image mob professor a bravo = "images/mobs/mob professor a bravo.webp"
image mob professor a incomodado = "images/mobs/mob professor a incomodado.webp"
image mob professor a irritado = "images/mobs/mob professor a irritado.webp"
image mob professor a medo = "images/mobs/mob professor a medo.webp"
image mob professor a neutro = "images/mobs/mob professor a neutro.webp"
image mob professor a sorrindo = "images/mobs/mob professor a sorrindo.webp"
image mob professor a transe = "images/mobs/mob professor a transe.webp"
image mob professor a transe hipnotico = "images/mobs/mob professor a transe hipnotico.webp"
image mob professora b brava = "images/mobs/mob professora b brava.webp"
image mob professora b irritada = "images/mobs/mob professora b irritada.webp"
image mob professora b medo = "images/mobs/mob professora b medo.webp"
image mob professora b neutro = "images/mobs/mob professora b neutro.webp"
image mob professora b sorrindo = "images/mobs/mob professora b sorrindo.webp"
image mob professora b transe = "images/mobs/mob professora b transe.webp"
image mob professora b transe hipnotico = "images/mobs/mob professora b transe hipnotico.webp"
image mob veterana b medo = "images/mobs/mob veterana b medo.webp"
image mob veterana b neutro = "images/mobs/mob veterana b neutro.webp"
image mob veterana b sorrindo = "images/mobs/mob veterana b sorrindo.webp"
image mob veterana b transe = "images/mobs/mob veterana b transe.webp"
image mob veterana b transe hipnotico = "images/mobs/mob veterana b transe hipnotico.webp"
image mob veterana c brava = "images/mobs/mob veterana c brava.webp"
image mob veterana c medo = "images/mobs/mob veterana c medo.webp"
image mob veterana c sorrindo = "images/mobs/mob veterana c sorrindo.webp"
image mob veterana c transe = "images/mobs/mob veterana c transe.webp"
image mob veterana c transe hipnotico = "images/mobs/mob veterana c transe hipnotico.webp"
image mob veterana fundao brava = "images/mobs/mob veterana fundao brava.webp"
image mob veterana fundao irritada = "images/mobs/mob veterana fundao irritada.webp"
image mob veterana fundao medo = "images/mobs/mob veterana fundao medo.webp"
image mob veterana fundao neutra = "images/mobs/mob veterana fundao neutra.webp"
image mob veterana fundao sorrindo = "images/mobs/mob veterana fundao sorrindo.webp"
image mob veterana fundao transe = "images/mobs/mob veterana fundao transe.webp"
image mob veterana fundao transe hipnotico = "images/mobs/mob veterana fundao transe hipnotico.webp"
image mob veterana ocultista brava = "images/mobs/mob veterana ocultista brava.webp"
image mob veterana ocultista irritada = "images/mobs/mob veterana ocultista irritada.webp"
image mob veterana ocultista medo = "images/mobs/mob veterana ocultista medo.webp"
image mob veterana ocultista neutra = "images/mobs/mob veterana ocultista neutra.webp"
image mob veterana ocultista sorrindo = "images/mobs/mob veterana ocultista sorrindo.webp"
image mob veterana ocultista transe = "images/mobs/mob veterana ocultista transe.webp"
image mob veterana ocultista transe hipnotico = "images/mobs/mob veterana ocultista transe hipnotico.webp"
image mob veterano a bravo = "images/mobs/mob veterano a bravo.webp"
image mob veterano a fundao bravo = "images/mobs/mob veterano a fundao bravo.webp"
image mob veterano a fundao irritado = "images/mobs/mob veterano a fundao irritado.webp"
image mob veterano a fundao medo = "images/mobs/mob veterano a fundao medo.webp"
image mob veterano a fundao neutro = "images/mobs/mob veterano a fundao neutro.webp"
image mob veterano a fundao sorrindo = "images/mobs/mob veterano a fundao sorrindo.webp"
image mob veterano a fundao transe = "images/mobs/mob veterano a fundao transe.webp"
image mob veterano a fundao transe hipnotico = "images/mobs/mob veterano a fundao transe hipnotico.webp"
image mob veterano a incomodado = "images/mobs/mob veterano a incomodado.webp"
image mob veterano a irritado = "images/mobs/mob veterano a irritado.webp"
image mob veterano a medo = "images/mobs/mob veterano a medo.webp"
image mob veterano a neutro = "images/mobs/mob veterano a neutro.webp"
image mob veterano a sorrindo = "images/mobs/mob veterano a sorrindo.webp"
image mob veterano a transe = "images/mobs/mob veterano a transe.webp"
image mob veterano a transe hipnotico = "images/mobs/mob veterano a transe hipnotico.webp"
image mob veterano b fundao bravo = "images/mobs/mob veterano b fundao bravo.webp"
image mob veterano b fundao irritado = "images/mobs/mob veterano b fundao irritado.webp"
image mob veterano b fundao medo = "images/mobs/mob veterano b fundao medo.webp"
image mob veterano b fundao neutro = "images/mobs/mob veterano b fundao neutro.webp"
image mob veterano b fundao sorrindo = "images/mobs/mob veterano b fundao sorrindo.webp"
image mob veterano b fundao transe = "images/mobs/mob veterano b fundao transe.webp"
image mob veterano b fundao transe hipnotico = "images/mobs/mob veterano b fundao transe hipnotico.webp"
image mob veterano c bravo = "images/mobs/mob veterano c bravo.webp"
image mob veterano c medo = "images/mobs/mob veterano c medo.webp"
image mob veterano c sorrindo = "images/mobs/mob veterano c sorrindo.webp"
image mob veterano fundao bravo = "images/mobs/mob veterano fundao bravo.webp"
image mob veterano fundao irritado = "images/mobs/mob veterano fundao irritado.webp"
image mob veterano fundao medo = "images/mobs/mob veterano fundao medo.webp"
image mob veterano fundao neutro = "images/mobs/mob veterano fundao neutro.webp"
image mob veterano fundao sorrindo = "images/mobs/mob veterano fundao sorrindo.webp"
image mob veterano fundao transe = "images/mobs/mob veterano fundao transe.webp"
image mob veterano fundao transe hipnotico = "images/mobs/mob veterano fundao transe hipnotico.webp"
image mob veterano ocultista bravo = "images/mobs/mob veterano ocultista bravo.webp"
image mob veterano ocultista irritado = "images/mobs/mob veterano ocultista irritado.webp"
image mob veterano ocultista medo = "images/mobs/mob veterano ocultista medo.webp"
image mob veterano ocultista neutro = "images/mobs/mob veterano ocultista neutro.webp"
image mob veterano ocultista sorrindo = "images/mobs/mob veterano ocultista sorrindo.webp"
image mob veterano ocultista transe = "images/mobs/mob veterano ocultista transe.webp"
image mob veterano ocultista transe hipnotico = "images/mobs/mob veterano ocultista transe hipnotico.webp"

# --- SPRITES DE INIMIGOS E ABERRAÇÕES ---
image fada verde ameaca = "images/Enemy's/fada verde ameaca.webp"
image fada verde deboche = "images/Enemy's/fada verde deboche.webp"
image fada verde derrota = "images/Enemy's/fada verde derrota.webp"
image inimigo colegial ghoul teia = "images/Enemy's/inimigo colegial ghoul teia.webp"
image inimigo colegial ghoul teia alt = "images/Enemy's/inimigo colegial ghoul teia alt.webp"
image inimigo colegial ghoul teia ataque = "images/Enemy's/inimigo colegial ghoul teia ataque.webp"
image inimigo colegial ghoul teia derrota = "images/Enemy's/inimigo colegial ghoul teia derrota.webp"
image inimigo colegial ghoul teia derrota alt = "images/Enemy's/inimigo colegial ghoul teia derrota alt.webp"
image inimigo colegial ghoul zumbi ataque = "images/Enemy's/inimigo colegial ghoul zumbi ataque.webp"
image inimigo colegial ghoul zumbi derrota = "images/Enemy's/inimigo colegial ghoul zumbi derrota.webp"
image inimigo colegial ghoul zumbi derrota alt = "images/Enemy's/inimigo colegial ghoul zumbi derrota alt.webp"
image inimigo esqueleto colegial ataque = "images/Enemy's/inimigo esqueleto colegial ataque.webp"
image inimigo esqueleto colegial curvado = "images/Enemy's/inimigo esqueleto colegial curvado.webp"
image inimigo esqueleto colegial derrota = "images/Enemy's/inimigo esqueleto colegial derrota.webp"
image inimigo esqueleto colegial marinheiro = "images/Enemy's/inimigo esqueleto colegial marinheiro.webp"
image inimigo esqueleto colegial runa testa = "images/Enemy's/inimigo esqueleto colegial runa testa.webp"
image inimigo esqueleto colegial runa testa alt = "images/Enemy's/inimigo esqueleto colegial runa testa alt.webp"
image inimigo esqueleto nobre correntes ataque = "images/Enemy's/inimigo esqueleto nobre correntes ataque.webp"
image inimigo esqueleto nobre correntes terno = "images/Enemy's/inimigo esqueleto nobre correntes terno.webp"
image inimigo esqueleto nobre espinhos runa = "images/Enemy's/inimigo esqueleto nobre espinhos runa.webp"
image inimigo esqueleto nobre espinhos runa derrota = "images/Enemy's/inimigo esqueleto nobre espinhos runa derrota.webp"
image inimigo estuadante vampira ruiva = "images/Enemy's/inimigo estuadante vampira ruiva.webp"
image inimigo estuadante vampira ruiva ataque = "images/Enemy's/inimigo estuadante vampira ruiva ataque.webp"
image inimigo estuadante vampira ruiva derrota = "images/Enemy's/inimigo estuadante vampira ruiva derrota.webp"
image inimigo estudante vampira ruiva = "images/Enemy's/inimigo estudante vampira ruiva.webp"
image inimigo estudante vampira ruiva ataque = "images/Enemy's/inimigo estudante vampira ruiva ataque.webp"
image inimigo estudante vampira ruiva derrota = "images/Enemy's/inimigo estudante vampira ruiva derrota.webp"
image inimigo executor com espada cabelo branco = "images/Enemy's/inimigo executor com espada cabelo branco.webp"
image inimigo executor com espada cabelo branco ataque = "images/Enemy's/inimigo executor com espada cabelo branco ataque.webp"
image inimigo executor com espada cabelo branco ataque alt = "images/Enemy's/inimigo executor com espada cabelo branco ataque alt.webp"
image inimigo executor com espada cabelo branco derrota = "images/Enemy's/inimigo executor com espada cabelo branco derrota.webp"
image inimigo executor com espada cabelo branco derrotado = "images/Enemy's/inimigo executor com espada cabelo branco derrotado.webp"
image inimigo executor conselho loiro espada = "images/Enemy's/inimigo executor conselho loiro espada.webp"
image inimigo executor conselho loiro espada ataque = "images/Enemy's/inimigo executor conselho loiro espada ataque.webp"
image inimigo executor conselho loiro espada derrota = "images/Enemy's/inimigo executor conselho loiro espada derrota.webp"
image inimigo executor conselho loiro rapieira = "images/Enemy's/inimigo executor conselho loiro rapieira.webp"
image inimigo executor conselho loiro rapieira derrota = "images/Enemy's/inimigo executor conselho loiro rapieira derrota.webp"
image inimigo executor conselho prata espada = "images/Enemy's/inimigo executor conselho prata espada.webp"
image inimigo executor conselho prata espada ataque = "images/Enemy's/inimigo executor conselho prata espada ataque.webp"
image inimigo executor conselho prata espada derrota = "images/Enemy's/inimigo executor conselho prata espada derrota.webp"
image inimigo executor conselho prata espada derrota alt = "images/Enemy's/inimigo executor conselho prata espada derrota alt.webp"
image inimigo executor conselho prata espada ereto = "images/Enemy's/inimigo executor conselho prata espada ereto.webp"
image inimigo executor conselho preto espada ataque = "images/Enemy's/inimigo executor conselho preto espada ataque.webp"
image inimigo executor conselho preto espada derrotado = "images/Enemy's/inimigo executor conselho preto espada derrotado.webp"
image inimigo executor conselho preto espada lamina = "images/Enemy's/inimigo executor conselho preto espada lamina.webp"
image inimigo executor conselho ruivo machado = "images/Enemy's/inimigo executor conselho ruivo machado.webp"
image inimigo executor conselho ruivo machado ataque = "images/Enemy's/inimigo executor conselho ruivo machado ataque.webp"
image inimigo executor conselho ruivo machado derrota = "images/Enemy's/inimigo executor conselho ruivo machado derrota.webp"
image inimigo executor conselho ruivo machado derrota alte = "images/Enemy's/inimigo executor conselho ruivo machado derrota alte.webp"
image inimigo executor conselho ruivo machado guarda = "images/Enemy's/inimigo executor conselho ruivo machado guarda.webp"
image inimigo executor conselho ruivo machado guarda ataque = "images/Enemy's/inimigo executor conselho ruivo machado guarda ataque.webp"
image inimigo executora conselho adaga guarda alta = "images/Enemy's/inimigo executora conselho adaga guarda alta.webp"
image inimigo executora conselho adaga guarda alta ataque = "images/Enemy's/inimigo executora conselho adaga guarda alta ataque.webp"
image inimigo executora conselho adaga guarda alta derrota = "images/Enemy's/inimigo executora conselho adaga guarda alta derrota.webp"
image inimigo executora conselho adaga sangue = "images/Enemy's/inimigo executora conselho adaga sangue.webp"
image inimigo executora conselho adaga sangue ataque = "images/Enemy's/inimigo executora conselho adaga sangue ataque.webp"
image inimigo executora conselho adaga sangue ataque derrota alt = "images/Enemy's/inimigo executora conselho adaga sangue ataque derrota alt.webp"
image inimigo executora conselho adaga sangue derrota = "images/Enemy's/inimigo executora conselho adaga sangue derrota.webp"
image inimigo executora conselho ruiva derrota = "images/Enemy's/inimigo executora conselho ruiva derrota.webp"
image inimigo executora conselho ruiva espada = "images/Enemy's/inimigo executora conselho ruiva espada.webp"
image inimigo executora conselho ruiva espada ataque = "images/Enemy's/inimigo executora conselho ruiva espada ataque.webp"
image inimigo fundao alquimista erguendo frasco = "images/Enemy's/inimigo fundao alquimista erguendo frasco.webp"
image inimigo fundao alquimista erguendo frasco ataque = "images/Enemy's/inimigo fundao alquimista erguendo frasco ataque.webp"
image inimigo fundao alquimista frasco verde arma = "images/Enemy's/inimigo fundao alquimista frasco verde arma.webp"
image inimigo fundao alquimista frasco verde ataque = "images/Enemy's/inimigo fundao alquimista frasco verde ataque.webp"
image inimigo fundao alquimista frasco verde derrota = "images/Enemy's/inimigo fundao alquimista frasco verde derrota.webp"
image inimigo fundao mascara gas chave grifo ataque = "images/Enemy's/inimigo fundao mascara gas chave grifo ataque.webp"
image inimigo fundao mascara gas chave grifo derrota = "images/Enemy's/inimigo fundao mascara gas chave grifo derrota.webp"
image inimigo fundao mascara gas chave grifo derrotado = "images/Enemy's/inimigo fundao mascara gas chave grifo derrotado.webp"
image inimigo fundao mascara gas chave grifo neutro = "images/Enemy's/inimigo fundao mascara gas chave grifo neutro.webp"
image inimigo fundao mascara gas escopeta = "images/Enemy's/inimigo fundao mascara gas escopeta.webp"
image inimigo fundao mascara gas escopeta alt = "images/Enemy's/inimigo fundao mascara gas escopeta alt.webp"
image inimigo fundao mascara gas escopeta derrota = "images/Enemy's/inimigo fundao mascara gas escopeta derrota.webp"
image inimigo fundao mascara gas escopeta disparo ataque = "images/Enemy's/inimigo fundao mascara gas escopeta disparo ataque.webp"
image inimigo fundao mecanico pesado = "images/Enemy's/inimigo fundao mecanico pesado.webp"
image inimigo fundao mecanico pesado ataque = "images/Enemy's/inimigo fundao mecanico pesado ataque.webp"
image inimigo fundao mecanico pesado derrota = "images/Enemy's/inimigo fundao mecanico pesado derrota.webp"
image inimigo gargula elite celestial asas abertas = "images/Enemy's/inimigo gargula elite celestial asas abertas.webp"
image inimigo gargula elite celestial asas abertas alt = "images/Enemy's/inimigo gargula elite celestial asas abertas alt.webp"
image inimigo gargula elite celestial asas abertas derrota = "images/Enemy's/inimigo gargula elite celestial asas abertas derrota.webp"
image inimigo gargula elite celestial ataque = "images/Enemy's/inimigo gargula elite celestial ataque.webp"
image inimigo gargula pedra dragao = "images/Enemy's/inimigo gargula pedra dragao.webp"
image inimigo gargula pedra dragao ataque = "images/Enemy's/inimigo gargula pedra dragao ataque.webp"
image inimigo gargula pedra dragao derrota = "images/Enemy's/inimigo gargula pedra dragao derrota.webp"
image inimigo ghoul garota corrompida ataque = "images/Enemy's/inimigo ghoul garota corrompida ataque.webp"
image inimigo ghoul garota corrompida garras = "images/Enemy's/inimigo ghoul garota corrompida garras.webp"
image inimigo ghoul garota corrompida garras derrota = "images/Enemy's/inimigo ghoul garota corrompida garras derrota.webp"
image inimigo hachishaku mulher gigante vestido branco = "images/Enemy's/inimigo hachishaku mulher gigante vestido branco.webp"
image inimigo hachishaku mulher gigante vestido branco ataque = "images/Enemy's/inimigo hachishaku mulher gigante vestido branco ataque.webp"
image inimigo hachishaku mulher gigante vestido branco derrota = "images/Enemy's/inimigo hachishaku mulher gigante vestido branco derrota.webp"
image inimigo hellhound cao sangue ataque = "images/Enemy's/inimigo hellhound cao sangue ataque.webp"
image inimigo hellhound cao sangue bote ataque = "images/Enemy's/inimigo hellhound cao sangue bote ataque.webp"
image inimigo hellhound cao sangue olhos = "images/Enemy's/inimigo hellhound cao sangue olhos.webp"
image inimigo hellhound cao sangue olhos derrota = "images/Enemy's/inimigo hellhound cao sangue olhos derrota.webp"
image inimigo inquisidor tatico balestra = "images/Enemy's/inimigo inquisidor tatico balestra.webp"
image inimigo inquisidor tatico balestra ataque = "images/Enemy's/inimigo inquisidor tatico balestra ataque.webp"
image inimigo inquisidor tatico balestra derrota = "images/Enemy's/inimigo inquisidor tatico balestra derrota.webp"
image inimigo marionete fios sangue ataque = "images/Enemy's/inimigo marionete fios sangue ataque.webp"
image inimigo marionete fios sangue avanco = "images/Enemy's/inimigo marionete fios sangue avanco.webp"
image inimigo marionete fios sangue derrota = "images/Enemy's/inimigo marionete fios sangue derrota.webp"
image inimigo marionete fios sangue flutuando = "images/Enemy's/inimigo marionete fios sangue flutuando.webp"
image inimigo marionete fios sangue inclinada = "images/Enemy's/inimigo marionete fios sangue inclinada.webp"
image inimigo marionete fios sangue suspensa = "images/Enemy's/inimigo marionete fios sangue suspensa.webp"
image inimigo rival ghoul ameaca aberta = "images/Enemy's/inimigo rival ghoul ameaca aberta.webp"
image inimigo rival ghoul ameaca aberta ataque = "images/Enemy's/inimigo rival ghoul ameaca aberta ataque.webp"
image inimigo rival ghoul ameaca aberta derrota = "images/Enemy's/inimigo rival ghoul ameaca aberta derrota.webp"
image inimigo rival ghoul combate = "images/Enemy's/inimigo rival ghoul combate.webp"
image inimigo rival ghoul combate ataque = "images/Enemy's/inimigo rival ghoul combate ataque.webp"
image inimigo rival ghoul combate derrota = "images/Enemy's/inimigo rival ghoul combate derrota.webp"
image inimigo rival ghoul garota postura combate = "images/Enemy's/inimigo rival ghoul garota postura combate.webp"
image inimigo rival ghoul garota postura combate ataque = "images/Enemy's/inimigo rival ghoul garota postura combate ataque.webp"
image inimigo rival ghoul garota postura combate derrota = "images/Enemy's/inimigo rival ghoul garota postura combate derrota.webp"
image inimigo rival ghoul guarda punhos = "images/Enemy's/inimigo rival ghoul guarda punhos.webp"
image inimigo rival ghoul guarda punhos derrota = "images/Enemy's/inimigo rival ghoul guarda punhos derrota.webp"
image inimigo rival ghoul loiro ataque = "images/Enemy's/inimigo rival ghoul loiro ataque.webp"
image inimigo rival ghoul loiro derrota = "images/Enemy's/inimigo rival ghoul loiro derrota.webp"
image inimigo rival ghoul loiro derrota alt = "images/Enemy's/inimigo rival ghoul loiro derrota alt.webp"
image inimigo sombra boca peito ataque = "images/Enemy's/inimigo sombra boca peito ataque.webp"
image inimigo sombra boca peito pesadelo = "images/Enemy's/inimigo sombra boca peito pesadelo.webp"
image inimigo urso monstruoso acorrentado ataque = "images/Enemy's/inimigo urso monstruoso acorrentado ataque.webp"
image inimigo urso monstruoso acorrentado cranio = "images/Enemy's/inimigo urso monstruoso acorrentado cranio.webp"
image inimigo urso monstruoso acorrentado cranio derrota = "images/Enemy's/inimigo urso monstruoso acorrentado cranio derrota.webp"
image inimigo vampira conselho espada tranca = "images/Enemy's/inimigo vampira conselho espada tranca.webp"
image inimigo vampira conselho espada tranca ataque = "images/Enemy's/inimigo vampira conselho espada tranca ataque.webp"
image inimigo vampira conselho espada tranca derrota = "images/Enemy's/inimigo vampira conselho espada tranca derrota.webp"
image inimigo vampira conselho florete chiquinhas = "images/Enemy's/inimigo vampira conselho florete chiquinhas.webp"
image inimigo vampira conselho florete chiquinhas ataque = "images/Enemy's/inimigo vampira conselho florete chiquinhas ataque.webp"
image inimigo vampira conselho florete chiquinhas derrota = "images/Enemy's/inimigo vampira conselho florete chiquinhas derrota.webp"
image inimigo vampira conselho rapieira albina = "images/Enemy's/inimigo vampira conselho rapieira albina.webp"
image inimigo vampira conselho rapieira albina ataque = "images/Enemy's/inimigo vampira conselho rapieira albina ataque.webp"
image inimigo vampira conselho rapieira albina derrota = "images/Enemy's/inimigo vampira conselho rapieira albina derrota.webp"
image inimigo vampiro delinquente ataque = "images/Enemy's/inimigo vampiro delinquente ataque.webp"
image inimigo vampiro delinquente derrota = "images/Enemy's/inimigo vampiro delinquente derrota.webp"
image inimigo vampiro delinquente sorriso agressivo = "images/Enemy's/inimigo vampiro delinquente sorriso agressivo.webp"
image inimigo vampiro estudante delinquente ameaca = "images/Enemy's/inimigo vampiro estudante delinquente ameaca.webp"
image inimigo vampiro estudante delinquente ameaca derrota = "images/Enemy's/inimigo vampiro estudante delinquente ameaca derrota.webp"
image inimigo vampiro estudante delinquente ataque = "images/Enemy's/inimigo vampiro estudante delinquente ataque.webp"
image inimigo vampiro ghoul agachado faca derrota = "images/Enemy's/inimigo vampiro ghoul agachado faca derrota.webp"
image inimigo vampiro ghoul agachado faca derrota alt = "images/Enemy's/inimigo vampiro ghoul agachado faca derrota alt.webp"
image inimigo vampiro ghoul cabelo preso = "images/Enemy's/inimigo vampiro ghoul cabelo preso.webp"
image inimigo vampiro ghoul cabelo preso ataque alt = "images/Enemy's/inimigo vampiro ghoul cabelo preso ataque alt.webp"

# --- SPRITES DE NORA ---
image nora atacando descontrolada = "images/nora/nora atacando descontrolada.webp"
image nora atacando descontrolada e frenesi = "images/nora/nora atacando descontrolada e frenesi.webp"
image nora neutra = "images/nora/nora neutra.webp"

# --- SPRITES DE CAIN ---
image cain agachado = "images/cain/corpo inteiro/cain agachado.webp"
image cain ameaca flutuando = "images/cain/corpo inteiro/cain ameaca flutuando.webp"
image cain combate pose = "images/cain/corpo inteiro/cain combate pose.webp"
image cain neutro espada = "images/cain/corpo inteiro/cain neutro espada.webp"

# --- SPRITES DE LORD PHILLIP ---
image phillip combate guarda = "images/Phillip/corpo inteiro/phillip combate guarda.webp"
image phillip derrota = "images/Phillip/corpo inteiro/phillip derrota.webp"
image phillip neutro espada = "images/Phillip/corpo inteiro/phillip neutro espada.webp"
image phillip pensativo espada = "images/Phillip/corpo inteiro/phillip pensativo espada.webp"

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init -1 python:
    def sincronizar_nome_mestra():
        if getattr(store, "apelido_lili_desbloqueado", False) or getattr(store, "estagio_mestra", 1) >= 2:
            store.nome_display_mestra = "Lili"
        else:
            store.nome_display_mestra = "Mestra"
        return store.nome_display_mestra

    def obter_titulo_dossie_mestra():
        if getattr(store, "segredo_lility_revelado", False):
            return "🩸 Lili (Verdadeira Identidade: Lility — A Criadora Pré-Diluviana)"
        elif getattr(store, "apelido_lili_desbloqueado", False) or getattr(store, "estagio_mestra", 1) >= 2:
            return "🩸 Lili (Senhorita Lyra von Blut)"
        else:
            return "🩸 Mestra (Senhorita Lyra von Blut)"

    def verificar_esta_chovendo():
        """
        Retorna True se houver chuva ativa no período atual.
        Para evitar a sensação de chuva perpétua e impedir descompasso de iluminação (dia claro à noite),
        a chuva atua nos períodos diurnos (Manhã e Tarde). À Noite, a tempestade estia em névoa noturna,
        mantendo a iluminação de luar e o fundo noturno correto nos setores da escola.
        """
        if getattr(store, "chuva_forcada_evento", False):
            return True
        clima = getattr(store, "clima_diario_id", "")
        if clima not in ["chuva_vitrais", "chuva", "chuva_acida", "nevoeiro_sangue"]:
            return False
        periodo_atual = getattr(store, "periodo", "Manhã")
        if periodo_atual == "Noite":
            return False
        return True
