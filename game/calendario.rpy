# ==============================================================================
# CALENDARIO.RPY — SISTEMA DOOM DINÂMICO & DIAS LIVRES DE SOBREVIVÊNCIA
# ==============================================================================
# Como funciona:
#   1. Os Dias 1 e 2 funcionam como o Prólogo Narrativo guiado (Ato I).
#   2. A partir do Dia 3, a progressão é LIVRE! O jogador gerencia seus dias,
#      investigações, itens e relacionamento com as heroínas.
#   3. Os Grandes Eventos Marcantes (Baile de Máscaras, Assalto ao Cofre, etc.)
#      são ativados dinamicamente pelos THRESHOLDS DO DOOM (deterioração do mundo),
#      e NÃO por um calendário fixo de 21 dias!
#   4. Se o DOOM atingir 100%, o Despertar da Entidade e o Eclipse Final começam!
# ==============================================================================

# Registro dos eventos guiados do Prólogo (Ato I: Dia 1 e Dia 2 Manhã)
# Obs: evt_d02_tarde (Triagem na Enfermaria) e evt_d02_noite (Halo no Banheiro)
# disparam organicamente APENAS quando o jogador visita esses locais no mapa!
define calendario_eventos = {
    (1, "Manhã"): "evt_d01_manha",
    (1, "Tarde"): "evt_d01_tarde",
    (1, "Noite"): "evt_d01_noite",
    (2, "Manhã"): "evt_d02_manha",
}

# Rastreamento dos marcos de DOOM já acionados nesta partida
default marcos_doom_disparados = []

init python:
    def verificar_evento_por_threshold_doom():
        """
        Verifica se a Deterioração do Mundo (DOOM) e o calendário atingiram marcos
        históricos importantes com cadência balanceada (máximo 1 grande marco guiado por dia).
        """
        doom = getattr(store, "ruina_cain", 10)
        disparados = getattr(store, "marcos_doom_disparados", [])
        dia = getattr(store, "dia_atual", 1)
        periodo_atual = getattr(store, "periodo", "Manhã")

        # O prólogo (Dias 1 e 2) tem prioridade antes dos thresholds livres
        if dia < 3:
            return None

        # 1. Threshold Final: Despertar Absoluto / Eclipse Total (Regra Universal: Fim apenas por DOOM 100%)
        if doom >= 100:
            return "evt_d21_noite"

        # 2. Regra de Espaçamento Mínimo: No máximo 1 grande marco guiado por dia!
        # Isso impede que eventos narrativos ocorram em sequência atropelando o jogador.
        ultimo_dia = getattr(store, "dia_ultimo_marco_narrativo", 0)
        if dia <= ultimo_dia:
            return None

        # 3. Progressão Narrativa Cronológica dos Marcos de História (Agenda Híbrida: DOOM ou Dia ou Progresso):
        # Marco Dia 6: Clima Tenso nos Corredores (Inquietante)
        if (doom >= 25 or dia >= 7) and dia >= 4 and periodo_atual in ["Tarde", "Noite"] and "marco_30_tenso" not in disparados:
            disparados.append("marco_30_tenso")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d06_tarde"

        # Marco Dia 7: Calouro no Armário (Teste de Autocontrole)
        if (doom >= 30 or dia >= 8) and dia >= 5 and periodo_atual == "Noite" and getattr(store, "fome_sangue", 100) < 75 and "marco_35_calouro_armario" not in disparados:
            disparados.append("marco_35_calouro_armario")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d07_noite"

        # Marco Dia 8: Emboscada Hachishaku (se ainda viva)
        if (doom >= 35 or dia >= 8) and dia >= 5 and periodo_atual == "Noite" and not getattr(store, "derrotou_hachishaku", False) and "marco_25_caldeiras_sussurro" not in disparados:
            disparados.append("marco_25_caldeiras_sussurro")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d05_noite"

        # Marco Dia 8: Autópsia das Cinzas (com Emília)
        if (doom >= 38 or dia >= 9) and dia >= 6 and periodo_atual in ["Manhã", "Tarde"] and "marco_40_autopsia_cinzas" not in disparados:
            disparados.append("marco_40_autopsia_cinzas")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d08_manha"

        # Marco Dia 9: Marcas do Grilhão (Consequência de Exposição)
        if (doom >= 42 or dia >= 11 or getattr(store, "exposicao", 0) >= 45) and dia >= 7 and periodo_atual == "Noite" and "marco_44_marcas_grilhao" not in disparados:
            disparados.append("marco_44_marcas_grilhao")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d09_noite"

        # Marco Dia 10: O Bar da Fada Verde & Mercado Negro Descoberto
        _dict_casos = getattr(store, "MISTERIOS_ACADEMIA", getattr(store, "misterios_woh", {}))
        _pistas_lote = getattr(_dict_casos.get("lote_necrotico", None), "pistas_coletadas", 0)
        if (doom >= 45 or dia >= 11 or _pistas_lote >= 2) and dia >= 7 and periodo_atual == "Noite" and "marco_48_fada_verde" not in disparados:
            disparados.append("marco_48_fada_verde")
            store.tem_passe_fada_verde = True
            store.desbloqueou_mercado_negro = True
            store.mercado_negro_aberto_hoje = True
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d10_noite"

        # Marco Dia 11: Detetive nos Portões
        if (doom >= 48 or dia >= 12) and dia >= 8 and periodo_atual in ["Tarde", "Noite"] and "marco_52_detetive_portoes" not in disparados:
            disparados.append("marco_52_detetive_portoes")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d11_tarde"

        # Marco Dia 12: Acordo dos Dutos
        if (doom >= 52 or dia >= 13) and dia >= 9 and periodo_atual == "Noite" and getattr(store, "desbloqueou_mercado_negro", False) and "marco_55_acordo_dutos" not in disparados:
            disparados.append("marco_55_acordo_dutos")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d12_noite"

        # Marco Dia 13: Emboscada do Chá (Consequência direta de D12)
        if "marco_55_acordo_dutos" in disparados and periodo_atual in ["Manhã", "Tarde"] and "marco_58_emboscada_cha" not in disparados:
            disparados.append("marco_58_emboscada_cha")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d13_manha"

        # Marco Dia 14: Véspera do Baile
        if (doom >= 58 or dia >= 14) and dia >= 10 and periodo_atual == "Noite" and "marco_62_vespera_baile" not in disparados:
            disparados.append("marco_62_vespera_baile")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d14_noite"

        # Marco Dia 15: O Baile de Máscaras (Ápice do Ato II)
        if (doom >= 62 or dia >= 15) and dia >= 11 and periodo_atual == "Noite" and "marco_66_baile_mascaras" not in disparados:
            disparados.append("marco_66_baile_mascaras")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d15_noite"

        # Marco Dia 16: Crise de Abstinência
        if (doom >= 68 or dia >= 16) and dia >= 12 and periodo_atual == "Noite" and "marco_70_crise_abstinencia" not in disparados:
            disparados.append("marco_70_crise_abstinencia")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d16_noite"

        # Marco Dia 17: Lorde Phillip
        if (doom >= 72 or dia >= 17) and dia >= 13 and periodo_atual in ["Tarde", "Noite"] and "marco_75_lorde_phillip" not in disparados:
            disparados.append("marco_75_lorde_phillip")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d17_tarde"

        # Marco Dia 18: Expurgo da Gárgula
        if (doom >= 76 or dia >= 18) and dia >= 14 and periodo_atual == "Noite" and "marco_80_expurgo_gargula" not in disparados:
            disparados.append("marco_80_expurgo_gargula")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d18_noite"

        # Marco Dia 19: Assalto ao Cofre
        _chaves = getattr(store, "fragmentos_chave_cripta", 0)
        if (doom >= 80 or dia >= 19 or _chaves >= 3) and dia >= 15 and periodo_atual == "Noite" and "marco_85_assalto_cofre" not in disparados:
            disparados.append("marco_85_assalto_cofre")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d19_noite"

        # Marco Dia 20: Pré-Eclipse
        if (doom >= 88 or dia >= 20) and dia >= 16 and periodo_atual == "Noite" and "marco_90_pre_eclipse" not in disparados:
            disparados.append("marco_90_pre_eclipse")
            store.dia_ultimo_marco_narrativo = dia
            return "evt_d20_noite"

        return None

label start:
    $ dia_atual = 1
    $ periodo = "Manhã"
    $ modo_exploracao_livre = False
    $ marcos_doom_disparados = []
    $ dia_ultimo_marco_narrativo = 0
    $ clima_diario_id = "calmaria_tensa"
    $ eh_dia_chuvoso = False
    $ chuva_forcada_evento = False
    $ reiniciar_misterios_woh()
    jump slot_atual

label slot_atual:
    # 1. Verificação de DOOM Máximo (100%): O Despertar da Entidade Oculta
    if ruina_cain >= 100:
        $ modo_exploracao_livre = False
        jump evt_d21_noite

    # 2. Exibição do HUD a partir da noite do Dia 1
    if dia_atual > 1 or periodo == "Noite":
        show screen hud_sobrevivencia

    # 3. Verifica se algum marco do DOOM deve ser acionado neste período
    $ _evento_threshold = verificar_evento_por_threshold_doom()
    if _evento_threshold:
        $ modo_exploracao_livre = False
        jump expression _evento_threshold

    # 4. Prólogo narrativo guiado (Ato I: Dia 1 e Dia 2 Manhã)
    $ _evento_do_slot = calendario_eventos.get((dia_atual, periodo))
    if _evento_do_slot:
        $ modo_exploracao_livre = False
        jump expression _evento_do_slot

    # 5. Exploração livre estilo RPG (Black Survival / World of Horror)
    jump slot_livre

label slot_livre:
    $ modo_exploracao_livre = True
    $ passos_restantes_periodo = 3
    $ limite_visitas_periodo = 2 if "paranoia_executor" in [s["id"] for s in getattr(store, "sequelas_ativas", [])] else 3
    $ visitas_restantes_periodo = limite_visitas_periodo
    $ locais_visitados_neste_periodo = []
    $ deslocando_pelo_mapa = False
    $ emilia_curou_gaze_periodo = False
    $ tomou_cha_emilia_periodo = False
    $ transe_lility_periodo = False
    $ conversou_heroina_periodo = {}
    $ tocou_heroina_periodo = {}
    $ rumores_heroina_periodo = {}
    $ for _h in [status_lility, status_elara, status_emilia, status_valeria]: _h.recuperar_turno(novo_dia=(periodo == "Manhã"))
    if periodo == "Manhã":
        $ sincronizar_estoque_diario_lojas()
    $ sortear_posicoes_heroinas()
    if getattr(store, "cobranca_vencida_pendente", False) and dia_atual >= 3:
        call evento_cobranca_taxa_academica from _call_cobranca_taxa_academica
    $ _bark_ciclo = obter_bark_transicao_persona()
    scene black with dissolve
    "[_bark_ciclo]"
    jump abrir_mapa_tatico

label fim_de_evento:
    # Todo label de história termina aqui: avança UM período e consome fome
    jump avancar_turno_mapa
