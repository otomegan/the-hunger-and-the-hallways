# ==============================================================================
# SISTEMAS_SINERGIA_AVANCADA.RPY — MÓDULO DE SINERGIA ENTRE SISTEMAS
# ==============================================================================
# 1. Alucinações da Besta (Miragens de Abstinência em 0 < fome_sangue < 20%)
# 2. Faro Cruzado das Heroínas (Banquete Oculto + Corrupção + Exposição)
# 3. 4 Passivas da Linhagem Pré-Diluviana (Ressonância Nív. 2, 4, 6 e 8)
# 4. Encomendas Clandestinas nas Caldeiras (+ Contrato de Emergência Queima de Arquivo)
# 5. Ecos do Passado / Herança de Sangue (persistent.eco_*)
# ==============================================================================

# --- VARIÁVEIS DE ESTADO (100% COMPATÍVEIS COM SAVES ANTIGOS) ---
default encomenda_caldeiras_ativa = None
default encomenda_caldeiras_pronta = False
default encomenda_caldeiras_concluida_hoje = False
default reacao_olfativa_banquete_periodo = {}
default hipnotizou_mob_periodo = False
default resgatou_ecos_sangue_partida = False
default encontro_eh_miragem = False

# --- TRANSFORM DEDICADO PARA SILHUETA DE MIRAGEM (PRESERVA ESCALA 2K/4K) ---
transform silhueta_miragem:
    xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 1.0 ysize 980 fit "contain"
    matrixcolor BrightnessMatrix(-0.78) * SaturationMatrix(0.15)
    alpha 0.88
    block:
        easein 0.7 alpha 0.82 xoffset -3
        easeout 0.7 alpha 0.95 xoffset 3
        repeat

# Prioridade init 5 garante execução APÓS definitions.rpy, sistemas_social_rpg.rpy e sistemas_triade_flash.rpy
init 5 python:

    def _notificar_sinergia(titulo, descricao, cor="#00ffcc"):
        if hasattr(store, "notificar_rpg"):
            store.notificar_rpg(titulo, descricao, cor)
        else:
            renpy.notify(f"{titulo}: {descricao}")

    # ==========================================================================
    # 1. PERFIL DE ALUCINAÇÃO PARA SEDE CRÍTICA (0 < fome_sangue < 20%)
    # ==========================================================================
    if "PERFIS_ALVO_EMBOSCADA" in globals():
        PERFIS_ALVO_EMBOSCADA["miragem_abstinencia"] = {
            "nome": "Vulto Trêmulo no Fim do Corredor",
            "tier": 2,
            "vel_base": 7.5,
            "largura_base": 14,
            "finta": 25,
            "dano_falha": 10,
            "dinheiro": 0,
            "texto_retaliacao": "Seus caninos rasgam apenas o aço congelado de um armário vazio enquanto o delírio da fome estala em seu crânio!"
        }

    def pode_ler_pulso_sanguineo():
        """Verdadeiro se Victor tem Sensibilidade >= 2 (incluindo buff sanguíneo) ou Faro do Submundo (Ressonância >= 2)."""
        sens = getattr(store, "sensibilidade_sobrenatural", 0) + getattr(store, "buff_sanguineo_sensibilidade", 0)
        res = getattr(store, "ressonancia_pre_diluviana", 0)
        return (sens >= 2) or (res >= 2)

    def obter_leitura_pulso_alvo(perfil_id="calouro"):
        """Retorna a assinatura sensorial do sangue do alvo quando pode_ler_pulso_sanguineo() está ativo."""
        if perfil_id == "miragem_abstinencia":
            return ("🔮 MIRAGEM DETECTADA: Sem pulso arterial! Apenas sombras e metal frio — NÃO ATAQUE!", "#ff44ff")
        mapa_pulso = {
            "doador": ("🩸 Pulso Fraco/Anêmico: +20% Saciedade | 0% Exposição base (baixo risco).", "#88ccff"),
            "calouro": ("🩸 Pulso Jovem Regular: +30% Saciedade | -2 Humanidade.", "#aaddff"),
            "veterano": ("🩸 Pulso Calejado: +30% Saciedade | +5 Defesa em combate (2 turnos).", "#99ddaa"),
            "medico": ("🩸 Pulso Clínico: +30% Saciedade | +20 HP imediato | +1 Intelecto.", "#66ffcc"),
            "ocultista": ("🔮 Pulso Carregado de Éter: +30% Saciedade | +2 Sensibilidade | +1 Ocultismo | +12 Dano Garras vs Corrompido.", "#cc88ff"),
            "professor": ("📘 Pulso Cafeinado: +25% Saciedade | +2 Intelecto (2 turnos) | +$20.", "#ffdd88"),
            "fundao": ("🔥 Pulso Adrenérgico: +35% Saciedade | +8 Dano | +1 Coragem | +$40 saqueados.", "#ffaa55"),
            "diretor": ("👑 Pulso Aristocrático: +30% Saciedade | +2 Intelecto | +1 Domínio | Alerta do Conselho.", "#ff8866"),
            "policial": ("🚨 Pulso Tático Armado: +35% Saciedade | +10 Dano | +2 Coragem | +$25 (Finta Extrema).", "#ff5566"),
        }
        return mapa_pulso.get(perfil_id, ("🩸 Pulso Humano Comum.", "#cccccc"))

    # ==========================================================================
    # 2. PASSIVAS DA LINHAGEM PRÉ-DILUVIANA (RESSONÂNCIA NÍV. 2, 4, 6 E 8)
    # ==========================================================================
    def obter_passivas_linhagem_ativas():
        res = getattr(store, "ressonancia_pre_diluviana", 0)
        ativas = []
        if res >= 2:
            ativas.append(("Faro do Submundo (Nív. 2)", "Lê o pulso sanguíneo/miragens no Bote Furtivo e +1 Sucata nas coletas do Fundão."))
        if res >= 4:
            ativas.append(("Passo das Sombras (Nív. 4)", "+6% de largura na Zona de Sombra do Bote Furtivo e -50% risco gerado pela rede."))
        if res >= 6:
            ativas.append(("Voz da Coroa (Nív. 6)", "-30% de Exposição adicional em falhas de emboscada, drenagens e batidas (mín. 1%)."))
        if res >= 8:
            ativas.append(("Presença Abissal (Nív. 8)", "Libera [HIPNOTIZAR E SAQUEAR] em figurantes (+$60 | 0% Exposição | 1x/período)."))
        return ativas

    def obter_proxima_passiva_linhagem():
        res = getattr(store, "ressonancia_pre_diluviana", 0)
        if res < 2:
            return f"Próxima Passiva: Faro do Submundo (Ressonância {res}/2)"
        if res < 4:
            return f"Próxima Passiva: Passo das Sombras (Ressonância {res}/4)"
        if res < 6:
            return f"Próxima Passiva: Voz da Coroa (Ressonância {res}/6)"
        if res < 8:
            return f"Próxima Passiva: Presença Abissal (Ressonância {res}/8)"
        return "Todas as 4 Passivas Pré-Diluvianas despertas!"

    # ==========================================================================
    # 3. FARO CRUZADO DAS HEROÍNAS (BANQUETE OCULTO + CORRUPÇÃO + EXPOSIÇÃO)
    # ==========================================================================
    def verificar_reacao_olfativa_heroina(heroina_id):
        """
        Dispara reação temática da heroína ao sangue ativo do Banquete Oculto (buff_sanguineo_tipo),
        Exposição ou Corrupção Abissal. Executada no máximo 1x por período por heroína (anti-farm).
        """
        # Se neutralizador de odor rúnico estiver ativo, o faro cruzado é totalmente mascarado
        if getattr(store, "odor_mascarado_turnos", 0) > 0:
            return

        if not isinstance(getattr(store, "reacao_olfativa_banquete_periodo", None), dict):
            store.reacao_olfativa_banquete_periodo = {}

        if store.reacao_olfativa_banquete_periodo.get(heroina_id, False):
            return

        turnos_buff = getattr(store, "buff_sanguineo_turnos", 0)
        tipo_sangue = (getattr(store, "buff_sanguineo_tipo", "") or "").lower() if turnos_buff > 0 else ""
        exp = getattr(store, "exposicao", 0)
        drenou_gremio = getattr(store, "drenou_membro_gremio", False)
        corrupcao = obter_corrupcao_abissal() if "obter_corrupcao_abissal" in globals() else 0

        OCULTISTAS = ("ocultista", "ocultismo", "veterano_ocultista")
        FUNDAO = ("fundao", "veterano_fundao", "viciado_fundao")
        OFICIAIS = ("policial", "diretor", "professor", "monitor_gremio")

        disparou = False
        bebeu_emilia = getattr(store, "bebeu_sangue_emilia", False) or (tipo_sangue in ("emilia", "sacro", "clero"))

        if heroina_id == "elara":
            if drenou_gremio:
                disparou = True
                if hasattr(store, "status_elara") and store.status_elara is not None:
                    store.status_elara.paciencia = max(0, store.status_elara.paciencia - 2)
                store.duvida_elara = getattr(store, "duvida_elara", 0) + 2
                if hasattr(store, "th_bark"):
                    store.th_bark("elara", "canibalismo")
                _notificar_sinergia(
                    "❄️ CANIBALISMO DE CASTA (ELARA)",
                    "Elara detectou o sangue de seus próprios executores em você (-2 Paciência | +2 Dúvida).",
                    "#ff4444"
                )
            elif bebeu_emilia:
                disparou = True
                store.duvida_elara = getattr(store, "duvida_elara", 0) + 1
                if hasattr(store, "th_bark"):
                    store.th_bark("elara", "sangue_clero")
                _notificar_sinergia(
                    "❄️ JULGAMENTO SANGUÍNEO (ELARA)",
                    "Elara farejou prata consagrada e o clero em suas veias (+1 Dúvida).",
                    "#ffffff"
                )
            elif tipo_sangue in OFICIAIS or exp >= 60:
                disparou = True
                if hasattr(store, "status_elara") and store.status_elara is not None:
                    store.status_elara.paciencia = max(0, store.status_elara.paciencia - 1)
                store.duvida_elara = getattr(store, "duvida_elara", 0) + 1
                if hasattr(store, "th_bark"):
                    store.th_bark("elara", "desconfiada")
                _notificar_sinergia(
                    "❄️ FARO ARISTOCRÁTICO (ELARA)",
                    "Elara farejou sangue oficial ou exposição elevada em seu uniforme (-1 Paciência | +1 Dúvida).",
                    "#ffffff"
                )

        elif heroina_id == "emilia":
            if tipo_sangue in OCULTISTAS or tipo_sangue in FUNDAO or corrupcao >= 65:
                disparou = True
                store.duvida_emilia = getattr(store, "duvida_emilia", 0) + 1
                if hasattr(store, "th_bark"):
                    store.th_bark("emilia", "faro_profano")
                _notificar_sinergia(
                    "✝️ REAÇÃO DO CRUCIFIXO (EMÍLIA)",
                    "O crucifixo de prata aqueceu perto da sua aura profana (+1 Suspeita de Emília).",
                    "#5c85d6"
                )

        elif heroina_id == "valeria":
            if tipo_sangue in FUNDAO or tipo_sangue == "policial":
                disparou = True
                store.risco_rede_fundao = max(0, getattr(store, "risco_rede_fundao", 0) - 15)
                if hasattr(store, "status_valeria") and store.status_valeria is not None:
                    store.status_valeria.paciencia = min(store.status_valeria.paciencia_max + 1, store.status_valeria.paciencia + 1)
                if hasattr(store, "th_bark"):
                    store.th_bark("valeria", "faro_ousadia")
                _notificar_sinergia(
                    "💚 FARO DO SUBMUNDO (VALÉRIA)",
                    "Valéria aprovou o sangue quente de quem circula pelas ruas (-15% Risco da Rede | +1 Paciência).",
                    "#2eb82e"
                )

        elif heroina_id == "lility":
            if drenou_gremio:
                disparou = True
                store.afeto_mestra = getattr(store, "afeto_mestra", 0) + 1
                if hasattr(store, "th_bark"):
                    store.th_bark("lility", "faro_gremio")
                _notificar_sinergia(
                    "🩸 PRESA DO CONSELHO (MESTRA)",
                    "A Mestra gargalha ao sentir o sangue dos cães de Elara em suas presas (+1 Afeto).",
                    "#ff0055"
                )
            elif bebeu_emilia:
                disparou = True
                if hasattr(store, "th_bark"):
                    store.th_bark("lility", "faro_clero")
                _notificar_sinergia(
                    "🩸 REPUGNÂNCIA SACRA (MESTRA)",
                    "A Mestra rejeita o cheiro de prata e incenso eclesiástico em suas veias.",
                    "#aa0022"
                )
            elif tipo_sangue in OCULTISTAS or tipo_sangue in ("diretor", "policial", "monitor_gremio"):
                disparou = True
                store.afeto_mestra = getattr(store, "afeto_mestra", 0) + 1
                store.ressonancia_pre_diluviana = getattr(store, "ressonancia_pre_diluviana", 0) + 1
                nome_m = getattr(store, "nome_display_mestra", "Mestra")
                if hasattr(store, "th_bark"):
                    store.th_bark("lility", "prazer")
                _notificar_sinergia(
                    f"🩸 RESSONÂNCIA ANCESTRAL ({nome_m.upper()})",
                    f"{nome_m} saboreia no ar a potência do sangue caçado (+1 Afeto | +1 Ressonância).",
                    "#c20000"
                )

        if disparou:
            store.reacao_olfativa_banquete_periodo[heroina_id] = True

    # ==========================================================================
    # 4. ENCOMENDAS CLANDESTINAS NAS CALDEIRAS (CONTRATOS DE RISCO + EMERGÊNCIA)
    # ==========================================================================
    CATALOGO_ENCOMENDAS_CALDEIRAS = {
        "extracao_ocultista": {
            "titulo": "Extração Etérea",
            "icone": "🔮",
            "emergencia": False,
            "desc": "Cace 1 Veterano do Clube de Ocultismo via Bote Furtivo com sucesso.",
            "recompensa_txt": "+1 Bolsa Filtrada | -20% Risco da Rede | +1 Paciência Valéria"
        },
        "limpeza_sucata": {
            "titulo": "Saque nas Sombras",
            "icone": "⚙️",
            "emergencia": False,
            "desc": "Entregue 4 Sucatas Eletrônicas na bancada de Valéria.",
            "recompensa_txt": "+$250 | +1 Giz de Proteção | +1 Paciência Valéria"
        },
        "cacada_fundao": {
            "titulo": "Acerto de Contas",
            "icone": "🔥",
            "emergencia": False,
            "desc": "Subjugue 1 Veterano da Turma do Fundão via Bote Furtivo sem testemunhas.",
            "recompensa_txt": "+1 Dose de Absinto | +1 Ressonância | +1 Paciência Valéria"
        },
        "queima_arquivo": {
            "titulo": "Queima de Arquivo (URGENTE)",
            "icone": "🚨",
            "emergencia": True,
            "desc": "Entregue 1x Giz de Proteção Rúnico para apagar os rastros do Grêmio nas Caldeiras.",
            "recompensa_txt": "-35% Risco de Batida da Rede | +1 Paciência Valéria"
        },
    }

    def obter_encomendas_disponiveis():
        """Retorna lista de chaves de contratos visíveis no painel das Caldeiras."""
        chaves = ["extracao_ocultista", "limpeza_sucata", "cacada_fundao"]
        if getattr(store, "risco_rede_fundao", 0) >= 60 or getattr(store, "encomenda_caldeiras_ativa", None) == "queima_arquivo":
            chaves.insert(0, "queima_arquivo")
        return chaves

    def aceitar_encomenda_caldeiras(chave):
        if chave not in CATALOGO_ENCOMENDAS_CALDEIRAS:
            return
        if getattr(store, "encomenda_caldeiras_concluida_hoje", False):
            _notificar_sinergia("📜 LIMITE DIÁRIO", "Valéria já fechou a cota de contratos clandestinos de hoje. Volte amanhã!", "#ffaa44")
            return
        store.encomenda_caldeiras_ativa = chave
        store.encomenda_caldeiras_pronta = False
        if hasattr(store, "th_sfx"):
            store.th_sfx("click")
        dados = CATALOGO_ENCOMENDAS_CALDEIRAS[chave]
        _notificar_sinergia("📜 CONTRATO ACEITO", f"{dados['titulo']}: {dados['desc']}", "#ffcc66")

    def registrar_progresso_encomenda_bote(perfil_id):
        """Marca o contrato ativo como pronto quando o alvo correto é drenado em Bote Furtivo."""
        chave = getattr(store, "encomenda_caldeiras_ativa", None)
        if not chave or getattr(store, "encomenda_caldeiras_pronta", False):
            return False

        p = (perfil_id or "").lower()
        if chave == "extracao_ocultista" and p in ("ocultista", "ocultismo", "veterano_ocultista"):
            store.encomenda_caldeiras_pronta = True
            _notificar_sinergia("📜 ENCOMENDA PRONTA!", "Extração Etérea cumprida! Resgate sua recompensa no Painel do Covil.", "#00ffcc")
            return True
        if chave == "cacada_fundao" and p in ("fundao", "veterano_fundao"):
            store.encomenda_caldeiras_pronta = True
            _notificar_sinergia("📜 ENCOMENDA PRONTA!", "Acerto de Contas cumprido! Resgate sua recompensa no Painel do Covil.", "#00ffcc")
            return True
        return False

    def encomenda_pode_ser_concluida():
        chave = getattr(store, "encomenda_caldeiras_ativa", None)
        if not chave or getattr(store, "encomenda_caldeiras_concluida_hoje", False):
            return False
        if chave == "limpeza_sucata":
            return getattr(store, "sucata_eletronica", 0) >= 4
        if chave == "queima_arquivo":
            return getattr(store, "giz_protecao", 0) >= 1
        return bool(getattr(store, "encomenda_caldeiras_pronta", False))

    def concluir_encomenda_caldeiras():
        chave = getattr(store, "encomenda_caldeiras_ativa", None)
        if not chave:
            return False
        if getattr(store, "encomenda_caldeiras_concluida_hoje", False):
            _notificar_sinergia("📜 LIMITE DIÁRIO", "Apenas 1 encomenda clandestina pode ser resgatada por dia.", "#ffaa44")
            return False
        if not encomenda_pode_ser_concluida():
            _notificar_sinergia("⚠️ CONTRATO PENDENTE", "Os requisitos do contrato ainda não foram cumpridos!", "#ff5555")
            return False

        if chave == "extracao_ocultista":
            store.bolsa_sangue_filtrado = getattr(store, "bolsa_sangue_filtrado", 0) + 1
            store.risco_rede_fundao = max(0, getattr(store, "risco_rede_fundao", 0) - 20)
        elif chave == "limpeza_sucata":
            store.sucata_eletronica -= 4
            store.dinheiro_jogador = getattr(store, "dinheiro_jogador", 0) + 250
            store.giz_protecao = getattr(store, "giz_protecao", 0) + 1
        elif chave == "cacada_fundao":
            store.dose_absinto = getattr(store, "dose_absinto", 0) + 1
            store.ressonancia_pre_diluviana = getattr(store, "ressonancia_pre_diluviana", 0) + 1
        elif chave == "queima_arquivo":
            store.giz_protecao -= 1
            store.risco_rede_fundao = max(0, getattr(store, "risco_rede_fundao", 0) - 35)

        # Parceria comercial com Valéria: restaura +1 Paciência e toca bark de negócios no canal 'barks'
        if hasattr(store, "status_valeria") and store.status_valeria is not None:
            store.status_valeria.paciencia = min(store.status_valeria.paciencia_max + 1, store.status_valeria.paciencia + 1)

        if renpy.loadable("audio/voice/valeria/valeria_bark_negocios.ogg"):
            renpy.sound.play("audio/voice/valeria/valeria_bark_negocios.ogg", channel="barks")
        elif hasattr(store, "th_bark"):
            store.th_bark("valeria", "padrao")

        if hasattr(store, "th_sfx"):
            store.th_sfx("caixa_registradora")

        dados = CATALOGO_ENCOMENDAS_CALDEIRAS[chave]
        store.encomenda_caldeiras_ativa = None
        store.encomenda_caldeiras_pronta = False
        store.encomenda_caldeiras_concluida_hoje = True
        _notificar_sinergia(f"📜 CONTRATO CONCLUÍDO: {dados['titulo']}", dados["recompensa_txt"], "#2eb82e")
        return True

    # ==========================================================================
    # 5. ECOS DO PASSADO / HERANÇA DE SANGUE (NEW GAME+ / persistent.eco_*)
    # ==========================================================================
    def registrar_eco_sangue(tipo_eco):
        if tipo_eco == "cofre":
            persistent.eco_conhece_senha_cofre = True
        elif tipo_eco == "lility":
            persistent.eco_sabe_identidade_lility = True
        elif tipo_eco == "sangue_adulterado":
            persistent.eco_aviso_sangue_adulterado = True

    def obter_ecos_sangue_ativos():
        ecos = []
        if getattr(persistent, "eco_aviso_sangue_adulterado", False):
            ecos.append(("🧪 Eco do Lote Contaminado", "Memória do frasco envenenado das caldeiras (libera aviso profético para Nora)."))
        if getattr(persistent, "eco_conhece_senha_cofre", False):
            ecos.append(("🗝️ Eco do Cofre do Grêmio", "Lembrança dos mecanismos internos da Câmara de Contenção de Elara."))
        if getattr(persistent, "eco_sabe_identidade_lility", False):
            ecos.append(("🩸 Eco da Linhagem Primordial", "Sussurro ancestral da verdadeira origem sob os vitrais da Sala de Música."))
        return ecos


# ==============================================================================
# LABEL DO DORMITÓRIO: RESGATAR ECOS DE SANGUE (1x POR PARTIDA)
# ==============================================================================
label ativar_ecos_sangue_dormitorio:
    hide screen hud_exploracao_bs
    $ _ecos_list = obter_ecos_sangue_ativos()
    if not _ecos_list or getattr(store, "resgatou_ecos_sangue_partida", False):
        "O silêncio do dormitório permanece imóvel. Nenhum eco novo ressoa no seu sangue."
        jump entrar_local_exploracao_bs

    $ resgatou_ecos_sangue_partida = True
    $ _bonus_eco = min(2, len(_ecos_list))
    $ conhecimento_oculto = getattr(store, "conhecimento_oculto", 0) + _bonus_eco
    $ sensibilidade_sobrenatural = getattr(store, "sensibilidade_sobrenatural", 0) + _bonus_eco
    $ th_sfx("distorcao")
    with flash_red

    "Ao apoiar as mãos frias sobre a escrivaninha do dormitório, uma vertigem súbita atravessa suas têmporas — memórias que não pertencem a este dia, gravadas diretamente na memória do seu sangue."
    "Fragmentos de ciclos passados se alinham em sua mente como páginas rasgadas de um diário já lido:"

    python:
        _resumo_ecos = " • ".join([e[0] for e in _ecos_list])

    "🔮 [[ECOS DESPERTOS]]: [_resumo_ecos]"
    $ _notificar_sinergia("🔮 HERANÇA DE SANGUE", f"+{_bonus_eco} Conhecimento Oculto | +{_bonus_eco} Sensibilidade Sobrenatural", "#cc88ff")
    "Seus sentidos se aguçam no escuro. Você já conhece o cheiro das armadilhas antes mesmo de cruzar o corredor (+[_bonus_eco] Conhecimento Oculto | +[_bonus_eco] Sensibilidade Sobrenatural)."

    jump entrar_local_exploracao_bs
