# ==============================================================================
# SISTEMAS_TRIADE_FLASH.RPY — EXPANSÃO MODULAR "TRÍADE FLASH"
# ==============================================================================
# Módulo 1 (The Inseminator): Radar de Emboscada Furtiva & QTE Pulso Cardíaco
# Módulo 2 (SimBro): Upgrades Permanentes do Covil & Rede Clandestina do Fundão
# Módulo 3 (Elena): Corrupção Abissal Dinâmica & Captura Não-Letal com Sequelas
# ==============================================================================

# --- VARIÁVEIS DE ESTADO (MÓDULO 1: FURTIVIDADE ESCALONADA E CADÊNCIA) ---
default cursor_emboscada = 0.0
default direcao_cursor = 1
default emboscada_zona_min = 36
default emboscada_zona_max = 64
default emboscada_velocidade = 4.2
default emboscada_chance_finta = 0
default emboscada_cooldown_finta = 0
default emboscada_aviso_finta = 0
default cacadas_realizadas_hoje = 0
default area_alerta_emboscada = False
default pulso_cardiaco = 50
default progresso_drenagem = 0

# --- VARIÁVEIS DE ESTADO (MÓDULO 2: INFRAESTRUTURA E REDE DO FUNDÃO) ---
default upgrades_instalados = {
    "alambique_runico": False,
    "isolamento_acustico": False,
    "escutas_dutos": False,
    "enfermaria_clandestina": False,
}

default risco_rede_fundao = 0

# --- VARIÁVEIS DE ESTADO (MÓDULO 3: CORRUPÇÃO ABISSAL E CAPTURAS) ---
default capturas_sofridas_ciclo = 0

init python:

    def _notificar_triade(titulo, descricao, cor="#00ffcc"):
        """Usa o toast estilizado notificar_rpg se disponível, com fallback seguro."""
        if hasattr(store, "notificar_rpg"):
            store.notificar_rpg(titulo, descricao, cor)
        else:
            renpy.notify(f"{titulo}: {descricao}")

    # ==========================================================================
    # MÓDULO 1 — EMBOSCADA FURTIVA ESCALONADA (ALVO × ZONA × FADIGA) E PULSO
    # ==========================================================================
    PERFIS_ALVO_EMBOSCADA = {
        "doador": {
            "nome": "Calouro Doador Debilitado",
            "tier": 1,
            "vel_base": 3.6,
            "largura_base": 30,
            "finta": 0,
            "dano_falha": 0,
            "dinheiro": 0,
            "texto_retaliacao": ""
        },
        "calouro": {
            "nome": "Estudante Calouro",
            "tier": 1,
            "vel_base": 4.2,
            "largura_base": 26,
            "finta": 0,
            "dano_falha": 0,
            "dinheiro": 0,
            "texto_retaliacao": ""
        },
        "veterano": {
            "nome": "Estudante Veterano",
            "tier": 2,
            "vel_base": 5.8,
            "largura_base": 20,
            "finta": 6,
            "dano_falha": 5,
            "dinheiro": 0,
            "texto_retaliacao": "No reflexo, o veterano acerta uma cotovelada pesada no seu rosto antes de disparar corredor abaixo!"
        },
        "medico": {
            "nome": "Enfermeira da Fundação",
            "tier": 2,
            "vel_base": 6.0,
            "largura_base": 18,
            "finta": 8,
            "dano_falha": 6,
            "dinheiro": 0,
            "texto_retaliacao": "A enfermeira reage com precisão clínica, cortando seu antebraço com um bisturi de bolso antes de fugir gritando!"
        },
        "ocultista": {
            "nome": "Veterano do Clube de Ocultismo",
            "tier": 2,
            "vel_base": 6.6,
            "largura_base": 16,
            "finta": 12,
            "dano_falha": 8,
            "dinheiro": 15,
            "texto_retaliacao": "O ocultista arremessa pó de giz consagrado e sal negro contra seus olhos, queimando sua pele enquanto recua!"
        },
        "professor": {
            "nome": "Docente Supervisor",
            "tier": 3,
            "vel_base": 7.4,
            "largura_base": 14,
            "finta": 15,
            "dano_falha": 10,
            "dinheiro": 20,
            "texto_retaliacao": "O docente golpeia sua têmpora com a lanterna de metal e dispara o apito disciplinar pelo corredor!"
        },
        "fundao": {
            "nome": "Veterano da Turma do Fundão",
            "tier": 3,
            "vel_base": 8.2,
            "largura_base": 13,
            "finta": 20,
            "dano_falha": 12,
            "dinheiro": 40,
            "texto_retaliacao": "Com reflexos de beco, o contrabandista saca um canivete e rasga seu ombro antes de sumir entre os dutos!"
        },
        "diretor": {
            "nome": "Diretor da Academia",
            "tier": 4,
            "vel_base": 9.0,
            "largura_base": 10,
            "finta": 25,
            "dano_falha": 14,
            "dinheiro": 35,
            "texto_retaliacao": "O diretor dispara um amuleto de choque do Conselho contra seu peito e grita pelos Executores de Branco!"
        },
        "policial": {
            "nome": "Oficial de Ronda / Detetive",
            "tier": 4,
            "vel_base": 9.8,
            "largura_base": 9,
            "finta": 30,
            "dano_falha": 18,
            "dinheiro": 25,
            "texto_retaliacao": "Com treinamento tático imediato, o oficial acerta suas costelas com o bastão retrátil e aciona o rádio de alerta!"
        },
    }

    LOCAIS_ZONA_VERMELHA = (
        "catacumbas", "cripta_cofre", "banheiro_abandonado", "cemiterio_nevoa", "subsolo_profundo"
    )
    LOCAIS_ZONA_AMARELA = (
        "caldeiras", "sala_caldeiras", "bar_fada_verde", "salao_gremio", "portoes_praca", "rua_portao"
    )

    def resolver_perfil_emboscada(id_mob="", tipo_mob=""):
        """Mapeia qualquer um dos 17 figurantes de MOBS_LORE_DATABASE ao seu perfil de dificuldade."""
        id_low = (id_mob or "").lower()
        tipo_low = (tipo_mob or "").lower()

        if "policial" in id_low or tipo_low == "policial":
            return "policial"
        if "diretor" in id_low or tipo_low == "diretor":
            return "diretor"
        if "fundao" in id_low or tipo_low == "fundao":
            return "fundao"
        if "professor" in id_low or tipo_low == "professor":
            return "professor"
        if "ocultista" in id_low or tipo_low in ("ocultista", "ocultismo"):
            return "ocultista"
        if "enfermeira" in id_low or tipo_low == "medico":
            return "medico"
        if "veteran" in id_low or tipo_low == "veterano":
            return "veterano"
        if tipo_low == "doador" or "calouro c" in id_low:
            return "doador"
        return "calouro"

    def obter_zona_perigo_atual(local=None, periodo_atual=None):
        """Determina a zona de perigo ('azul', 'amarela' ou 'vermelha') pelo local e período atuais."""
        loc = (local if local is not None else getattr(store, "local_atual", "corredor_academia")) or ""
        per = (periodo_atual if periodo_atual is not None else getattr(store, "periodo", "Manhã")) or "Manhã"

        if per == "Noite" or loc in LOCAIS_ZONA_VERMELHA:
            return "vermelha"
        if per == "Tarde" or loc in LOCAIS_ZONA_AMARELA:
            return "amarela"
        return "azul"

    def configurar_emboscada(perfil_id="calouro", zona="amarela"):
        """Calcula velocidade, largura da Zona de Sombra e chance de Finta combinando Alvo × Zona × Fadiga."""
        dados = PERFIS_ALVO_EMBOSCADA.get(perfil_id, PERFIS_ALVO_EMBOSCADA["calouro"])
        zona_norm = (zona or "amarela").lower()

        if "azul" in zona_norm:
            mod_vel, mod_larg, mod_finta = 0.0, 0, 0
        elif "vermelha" in zona_norm:
            mod_vel, mod_larg, mod_finta = 3.5, -7, 10
        else:
            mod_vel, mod_larg, mod_finta = 1.6, -4, 4

        fadiga_dia = getattr(store, "cacadas_realizadas_hoje", 0) * 1.5
        sens_total = getattr(store, "sensibilidade_sobrenatural", 0) + getattr(store, "buff_sanguineo_sensibilidade", 0)
        bonus_sentidos = min(10, max(0, sens_total))
        # Passiva Passo das Sombras (Ressonância >= 4): +6% de largura na Zona de Sombra
        bonus_passo_sombras = 6 if getattr(store, "ressonancia_pre_diluviana", 0) >= 4 else 0
        # Bônus do Sedativo Clínico Concentrado: +10% de largura de acerto
        bonus_sedativo = 10 if getattr(store, "sedativo_ativo_bote", False) else 0

        vel_final = min(16.0, round(dados["vel_base"] + mod_vel + fadiga_dia, 2))
        largura_final = max(6, min(50, int(dados["largura_base"] + mod_larg + bonus_sentidos + bonus_passo_sombras + bonus_sedativo)))
        finta_final = min(45, dados["finta"] + mod_finta)

        centro = renpy.random.randint(28, 72)
        z_min = max(5, int(centro - (largura_final / 2.0)))
        z_max = min(95, z_min + largura_final)
        # Garante largura mínima exata caso encoste na borda superior
        if (z_max - z_min) < 6:
            z_min = max(5, z_max - 6)

        store.cursor_emboscada = 0.0
        store.direcao_cursor = 1
        store.emboscada_velocidade = vel_final
        store.emboscada_zona_min = z_min
        store.emboscada_zona_max = z_max
        store.emboscada_chance_finta = finta_final
        store.emboscada_cooldown_finta = 14
        store.emboscada_aviso_finta = 0

    def tick_cursor_emboscada():
        """Avança o cursor da emboscada com suporte a Finta (inversão de direção com cooldown justo)."""
        if getattr(store, "emboscada_aviso_finta", 0) > 0:
            store.emboscada_aviso_finta -= 1

        if getattr(store, "emboscada_cooldown_finta", 0) > 0:
            store.emboscada_cooldown_finta -= 1
        elif store.emboscada_chance_finta > 0 and 20.0 <= store.cursor_emboscada <= 80.0:
            prob_tick = max(1, store.emboscada_chance_finta // 5)
            if renpy.random.randint(1, 100) <= prob_tick:
                store.direcao_cursor *= -1
                store.emboscada_cooldown_finta = 18  # ~0.63s de intervalo mínimo entre fintas
                store.emboscada_aviso_finta = 16
                if hasattr(store, "th_sfx"):
                    store.th_sfx("click")

        store.cursor_emboscada += store.emboscada_velocidade * store.direcao_cursor
        if store.cursor_emboscada >= 100.0:
            store.cursor_emboscada = 100.0
            store.direcao_cursor = -1
        elif store.cursor_emboscada <= 0.0:
            store.cursor_emboscada = 0.0
            store.direcao_cursor = 1

    def atualizar_cursor_emboscada(velocidade=6):
        """Wrapper legado mantido por compatibilidade."""
        store.emboscada_velocidade = float(velocidade)
        store.emboscada_chance_finta = 0
        tick_cursor_emboscada()

    def atualizar_pulso_drenagem(modo_teste=False):
        # Em Sede Crítica (fome < 20%), tremor de ansiedade faz o pulso oscilar de forma errática
        if (not modo_teste) and getattr(store, "fome_sangue", 100) < 20:
            queda = renpy.random.randint(2, 6)
        else:
            queda = 3
        store.pulso_cardiaco = max(0, store.pulso_cardiaco - queda)
        if 60 <= store.pulso_cardiaco <= 85:
            store.progresso_drenagem = min(100, store.progresso_drenagem + 8)
        elif store.pulso_cardiaco > 85:
            if not modo_teste:
                delta_exp = 1
                if store.upgrades_instalados.get("isolamento_acustico", False):
                    delta_exp = 0 if (store.progresso_drenagem % 2 == 0) else 1
                store.exposicao = min(100, store.exposicao + delta_exp)
            store.progresso_drenagem = min(100, store.progresso_drenagem + 3)

    def pulsar_ritmo_drenagem():
        store.pulso_cardiaco = min(100, store.pulso_cardiaco + 14)
        if hasattr(store, "th_sfx"):
            store.th_sfx("heartbeat")

    # ==========================================================================
    # MÓDULO 2 — GESTÃO DO COVIL DAS CALDEIRAS E REDE DO FUNDÃO (SIMBRO)
    # ==========================================================================
    CATALOGO_UPGRADES_BASE = {
        "alambique_runico": {
            "nome": "Alambique de Filtragem Rúnica",
            "icone": "🧪",
            "custo_dinheiro": 300,
            "custo_sucata": 2,
            "desc": "Purifica automaticamente 1 Bolsa de Sangue Adulterado em Filtrado a cada amanhecer."
        },
        "isolamento_acustico": {
            "nome": "Isolamento Acústico de Cobre",
            "icone": "🔇",
            "custo_dinheiro": 450,
            "custo_sucata": 3,
            "desc": "Reduz em 30% os ganhos de Exposição em combates e caçadas noturnas."
        },
        "escutas_dutos": {
            "nome": "Rede de Escutas nos Dutos",
            "icone": "📡",
            "custo_dinheiro": 600,
            "custo_sucata": 4,
            "desc": "Antecipa rondas, reduz o risco da rede e contém o avanço da Deterioração Subterrânea."
        },
        "enfermaria_clandestina": {
            "nome": "Enfermaria Clandestina nas Caldeiras",
            "icone": "🩹",
            "custo_dinheiro": 350,
            "custo_sucata": 2,
            "desc": "Regenera +15 HP adicionais a cada novo amanhecer."
        },
    }

    class AgenteFundao(renpy.python.RevertableObject):
        def __init__(self, id_agente, nome, especialidade):
            self.id_agente = id_agente
            self.nome = nome
            self.especialidade = especialidade
            self.estamina = 100
            self.tarefa_atual = "descanso"

    def comprar_upgrade_base(chave):
        dados = CATALOGO_UPGRADES_BASE.get(chave)
        if not dados:
            return
        if store.upgrades_instalados.get(chave, False):
            _notificar_triade("🛠️ JÁ INSTALADO", f"{dados['nome']} já opera no covil.", "#aaaaaa")
            return
        din = getattr(store, "dinheiro_jogador", 0)
        suc = getattr(store, "sucata_eletronica", 0)
        if din >= dados["custo_dinheiro"] and suc >= dados["custo_sucata"]:
            store.dinheiro_jogador -= dados["custo_dinheiro"]
            store.sucata_eletronica -= dados["custo_sucata"]
            store.upgrades_instalados[chave] = True
            if hasattr(store, "th_sfx"):
                store.th_sfx("moedas_ouro")
            _notificar_triade("🛠️ COVIL APRIMORADO", f"{dados['nome']} instalado com sucesso!", "#00ffcc")
        else:
            if hasattr(store, "th_sfx"):
                store.th_sfx("click")
            _notificar_triade("⚠️ RECURSOS INSUFICIENTES", f"Requer ${dados['custo_dinheiro']} e {dados['custo_sucata']} Sucatas.", "#ff5555")

    def alterar_tarefa_agente(idx, nova_tarefa):
        if 0 <= idx < len(store.equipe_fundao):
            store.equipe_fundao[idx].tarefa_atual = nova_tarefa
            if hasattr(store, "th_sfx"):
                store.th_sfx("click")

    def processar_turno_simbro():
        """Processa os bônus passivos da base e a rede de informantes na virada para Manhã (Dia 3+)."""
        # 1. Upgrades Permanentes
        if store.upgrades_instalados.get("alambique_runico", False) and getattr(store, "bolsa_sangue_adulterado", 0) > 0:
            store.bolsa_sangue_adulterado -= 1
            store.bolsa_sangue_filtrado = getattr(store, "bolsa_sangue_filtrado", 0) + 1
            _notificar_triade("🧪 ALAMBIQUE RÚNICO", "1 Bolsa Adulterada purificada em Sangue Filtrado!", "#00ffcc")

        if store.upgrades_instalados.get("enfermaria_clandestina", False):
            hp_max_atual = getattr(store, "hp_jogador_max", 100)
            if store.hp_jogador < hp_max_atual:
                store.hp_jogador = min(hp_max_atual, store.hp_jogador + 15)
                _notificar_triade("🩹 ENFERMARIA CLANDESTINA", "Soro noturno regenerou +15 HP!", "#55ff99")

        if store.upgrades_instalados.get("escutas_dutos", False):
            if hasattr(store, "ruina_cain") and store.ruina_cain > 0:
                store.ruina_cain = max(0, store.ruina_cain - 1)
            store.risco_rede_fundao = max(0, store.risco_rede_fundao - 3)
            _notificar_triade("📡 ESCUTAS NOS DUTOS", "Rondas antecipadas: -1% Deterioração | -3% Risco da Rede.", "#88ccff")

        # 2. Produção das Células de Informantes do Fundão
        din_ganho = 0
        suc_ganha = 0
        sangue_ganho = 0
        res_linhagem = getattr(store, "ressonancia_pre_diluviana", 0)
        tem_faro_submundo = (res_linhagem >= 2)
        tem_passo_sombras = (res_linhagem >= 4)
        for ag in store.equipe_fundao:
            if ag.tarefa_atual == "descanso":
                ag.estamina = min(100, ag.estamina + 35)
                store.risco_rede_fundao = max(0, store.risco_rede_fundao - 5)
            elif ag.estamina >= 25:
                ag.estamina -= 25
                bonus_esp = (ag.tarefa_atual == ag.especialidade)
                if ag.tarefa_atual == "dinheiro":
                    ganho = 140 if bonus_esp else 100
                    store.dinheiro_jogador += ganho
                    din_ganho += ganho
                    delta_r = 8
                    store.risco_rede_fundao = min(100, store.risco_rede_fundao + (max(1, delta_r // 2) if tem_passo_sombras else delta_r))
                elif ag.tarefa_atual == "sucata":
                    qtd = (2 if bonus_esp else 1) + (1 if tem_faro_submundo else 0)
                    store.sucata_eletronica += qtd
                    suc_ganha += qtd
                    delta_r = 5
                    store.risco_rede_fundao = min(100, store.risco_rede_fundao + (max(1, delta_r // 2) if tem_passo_sombras else delta_r))
                elif ag.tarefa_atual == "sangue":
                    store.bolsa_sangue_adulterado = getattr(store, "bolsa_sangue_adulterado", 0) + 1
                    sangue_ganho += 1
                    delta_r = 10 if bonus_esp else 14
                    store.risco_rede_fundao = min(100, store.risco_rede_fundao + (max(1, delta_r // 2) if tem_passo_sombras else delta_r))
            else:
                # Célula exausta descansa automaticamente para recuperar fôlego
                ag.estamina = min(100, ag.estamina + 20)

        resumo = []
        if din_ganho > 0:
            resumo.append(f"+${din_ganho}")
        if suc_ganha > 0:
            resumo.append(f"+{suc_ganha} Sucata")
        if sangue_ganho > 0:
            resumo.append(f"+{sangue_ganho} Bolsa Adulterada")
        if resumo:
            _notificar_triade("📦 REDE DO FUNDÃO", "Coleta matinal: " + " | ".join(resumo), "#ffcc66")

        # 3. Checagem de Batida do Grêmio (Heat >= 85%)
        if store.risco_rede_fundao >= 85:
            confisco = min(store.dinheiro_jogador, 200)
            store.dinheiro_jogador -= confisco
            delta_exp = 7 if store.upgrades_instalados.get("isolamento_acustico", False) else 10
            store.exposicao = min(100, store.exposicao + delta_exp)
            store.risco_rede_fundao = 30
            _notificar_triade("🚨 BATIDA DO GRÊMIO", f"Caldeiras vasculhadas! -${confisco} confiscados | +{delta_exp}% Exposição.", "#ff3344")

    # ==========================================================================
    # MÓDULO 3 — CORRUPÇÃO ABISSAL E ESCALONAMENTO DE PODER (ELENA)
    # ==========================================================================
    def obter_corrupcao_abissal():
        """Retorna de 0 a 100 o índice de corrupção predatória de Victor."""
        base_desumanidade = max(0, 100 - getattr(store, "humanidade", 75))
        bonus_ressonancia = getattr(store, "ressonancia_pre_diluviana", 0) * 6
        return min(100, base_desumanidade + bonus_ressonancia)

    def calcular_dano_garras_abissais():
        """Quanto mais corrompido Victor está, mais devastadoras são as Garras de Sangue."""
        corrupcao = obter_corrupcao_abissal()
        dominio = getattr(store, "dominio_jogador", 0)
        return int(38 + (corrupcao * 0.40) + (dominio * 3))

    def aplicar_reducao_isolamento_exposicao(valor_base):
        """
        Aplica amortecimento multiplicativo de Exposição:
        -30% pelo upgrade Isolamento Acústico e -30% pela passiva Voz da Coroa (Ressonância >= 6),
        mantendo piso mínimo de 1 quando valor_base > 0 para nunca zerar o risco da Máscara.
        """
        if valor_base <= 0:
            return 0
        fator = 1.0
        if store.upgrades_instalados.get("isolamento_acustico", False):
            fator *= 0.70
        if getattr(store, "ressonancia_pre_diluviana", 0) >= 6:
            fator *= 0.70
        return max(1, int(round(valor_base * fator)))

default equipe_fundao = [
    AgenteFundao("olheiro", "Célula de Calouros Olheiros", "sucata"),
    AgenteFundao("contrabandista", "Veteranos do Mercado Negro", "dinheiro"),
    AgenteFundao("enfermaria", "Auxiliares Subornados da Enfermaria", "sangue"),
]

# ==============================================================================
# TELAS INTERATIVAS — MÓDULO 1 (RADAR DE EMBOSCADA & PULSO CARDÍACO)
# ==============================================================================

screen radar_emboscada_furtiva(perfil_id="calouro", zona="amarela", nome_exibicao=None, modo_teste=False):
    modal True
    zorder 210
    on "show" action Function(configurar_emboscada, perfil_id, zona)

    timer 0.035 repeat True action Function(tick_cursor_emboscada)

    $ _dados_emb = PERFIS_ALVO_EMBOSCADA.get(perfil_id, PERFIS_ALVO_EMBOSCADA["calouro"])
    $ _titulo_alvo = nome_exibicao if nome_exibicao else _dados_emb["nome"]
    $ _zona_up = (zona or "amarela").upper()
    $ _cor_zona = "#33aaff" if _zona_up == "AZUL" else ("#ff3344" if _zona_up == "VERMELHA" else "#ffcc33")
    $ _na_zona = (emboscada_zona_min <= cursor_emboscada <= emboscada_zona_max)
    $ _larg_px = max(12, int(620 * ((emboscada_zona_max - emboscada_zona_min) / 100.0)))
    $ _pos_zona_px = int(620 * (emboscada_zona_min / 100.0))
    $ _pos_cursor_px = max(0, min(614, int(620 * (cursor_emboscada / 100.0)) - 3))
    $ _cursor_int = int(round(cursor_emboscada))
    $ _leitura_ativa = pode_ler_pulso_sanguineo() if "pode_ler_pulso_sanguineo" in globals() else False
    $ _eh_miragem_ui = (perfil_id == "miragem_abstinencia")
    $ _pulso_txt, _pulso_cor = obter_leitura_pulso_alvo(perfil_id) if _leitura_ativa and "obter_leitura_pulso_alvo" in globals() else ("", "#cccccc")

    if modo_teste:
        key "K_SPACE" action If(_na_zona,
            true=[Hide("radar_emboscada_furtiva"), Function(_notificar_triade, "👁️ TESTE BOTE: SUCESSO", f"Acerto em {_titulo_alvo} (Tier {_dados_emb['tier']} | Zona {_zona_up}) — 0% Exposição!", "#00ffcc")],
            false=[Hide("radar_emboscada_furtiva"), Function(_notificar_triade, "🚨 TESTE BOTE: ALVO ESCAPOU", f"Falha em {_titulo_alvo} — 0% Sangue | Retaliação -{_dados_emb['dano_falha']} HP | Área em Alerta!", "#ff4444")])
    else:
        key "K_SPACE" action If(_na_zona, true=Return("sucesso_furtivo"), false=Return("falha_fuga"))

    add Solid("#05050acc")

    frame:
        xalign 0.5 yalign 0.5
        xysize (800, 455 if _leitura_ativa else 415)
        background "#0e0c14f5"
        padding (32, 24)

        vbox:
            spacing 12
            xalign 0.5

            text "👁️ BOTE FURTIVO — [_titulo_alvo]" size 25 color "#ff3344" bold True xalign 0.5

            hbox:
                spacing 18
                xalign 0.5
                text "Ameaça: Tier [_dados_emb['tier']]" size 16 bold True color "#ffaa66"
                text "|" size 16 color "#555566"
                text "Área: ZONA [_zona_up]" size 16 bold True color _cor_zona
                text "|" size 16 color "#555566"
                text "Caçadas Hoje: [cacadas_realizadas_hoje]" size 16 color "#bbbbcc"

            if _leitura_ativa and _pulso_txt:
                frame:
                    xalign 0.5
                    background ("#2a0a2ef0" if _eh_miragem_ui else "#161a28f0")
                    padding (14, 6)
                    text "[_pulso_txt]" size 15 bold True color _pulso_cor xalign 0.5

            text "Crave as presas quando a agulha cruzar a ZONA DE SOMBRA ([emboscada_zona_min]%% a [emboscada_zona_max]%%)!" size 17 color "#e0e0e8" xalign 0.5

            # Barra Visual Dinâmica (Trilho + Zona de Sombra Exata + Agulha Branca Móvel)
            fixed:
                xysize (620, 46)
                xalign 0.5
                add Solid("#1b1a24") xysize (620, 34) yalign 0.5
                add Solid("#00cc8888") xpos _pos_zona_px yalign 0.5 xysize (_larg_px, 34)
                add Solid("#00ffaa" if _na_zona else "#ffffff") xpos _pos_cursor_px ypos 0 xysize (6, 46)

            if emboscada_aviso_finta > 0:
                text "⚠️ O ALVO OLHOU PARA TRÁS! (FINTA — DIREÇÃO INVERTIDA!)" size 18 bold True color "#ffbb33" xalign 0.5
            elif _na_zona:
                text "🟢 ZONA DE SOMBRA ATIVA — BOTE SILENCIOSO!" size 19 bold True color "#00ffcc" xalign 0.5
            else:
                text "🔴 PONTO EXPOSTO: [_cursor_int]%% (Erro = Fuga, 0%% Sangue e Alerta!)" size 17 bold True color "#ff7766" xalign 0.5

            hbox:
                spacing 16
                xalign 0.5
                textbutton "🩸 [[ CRAVAR AS PRESAS AGORA! (ESPAÇO) ]]":
                    padding (24, 12)
                    background ("#006644" if _na_zona else "#660011")
                    hover_background ("#009966" if _na_zona else "#aa0022")
                    text_size 18
                    text_bold True
                    text_color "#ffffff"
                    if modo_teste:
                        action If(_na_zona,
                            true=[Hide("radar_emboscada_furtiva"), Function(_notificar_triade, "👁️ TESTE BOTE: SUCESSO", f"Acerto em {_titulo_alvo} (Tier {_dados_emb['tier']} | Zona {_zona_up}) — 0% Exposição!", "#00ffcc")],
                            false=[Hide("radar_emboscada_furtiva"), Function(_notificar_triade, "🚨 TESTE BOTE: ALVO ESCAPOU", f"Falha em {_titulo_alvo} — 0% Sangue | Retaliação -{_dados_emb['dano_falha']} HP | Área em Alerta!", "#ff4444")])
                    else:
                        action If(_na_zona, true=Return("sucesso_furtivo"), false=Return("falha_fuga"))

                if _eh_miragem_ui and _leitura_ativa:
                    textbutton "🛑 [[ DISSIPAR MIRAGEM ]]":
                        padding (18, 12)
                        background "#331a44"
                        hover_background "#552a70"
                        text_size 17
                        text_bold True
                        text_color "#eeccff"
                        if modo_teste:
                            action [Hide("radar_emboscada_furtiva"), Function(_notificar_triade, "🔮 MIRAGEM DISSIPADA", "Você reconheceu a ilusão de abstinência a tempo (0 HP perdido | 0% Exposição)!", "#cc88ff")]
                        else:
                            action Return("miragem_dissipada")

                if modo_teste:
                    textbutton "✖ Fechar":
                        padding (18, 12)
                        background "#22222c"
                        text_size 18
                        action Hide("radar_emboscada_furtiva")


screen qte_pulso_sangue(nome_alvo="Alvo", modo_teste=False):
    modal True
    zorder 210
    on "show" action [SetVariable("pulso_cardiaco", 50), SetVariable("progresso_drenagem", 0)]

    if modo_teste:
        timer 0.1 repeat True action [
            Function(atualizar_pulso_drenagem, True),
            If(progresso_drenagem >= 100,
                true=[Hide("qte_pulso_sangue"), Function(_notificar_triade, "💓 TESTE PULSO: PERFEITO", "Transe Perfeito concluído (+15% Saciedade | +1 Humanidade)!", "#00ffcc")],
                false=If(pulso_cardiaco <= 0,
                    true=[Hide("qte_pulso_sangue"), Function(_notificar_triade, "⚠️ TESTE PULSO: ESCAPOU", "Pulso zerado! O alvo rompeu o transe.", "#ff8800")],
                    false=NullAction()))
        ]
    else:
        timer 0.1 repeat True action [
            Function(atualizar_pulso_drenagem, False),
            If(progresso_drenagem >= 100,
                true=Return("transe_perfeito"),
                false=If(pulso_cardiaco <= 0,
                    true=Return("transe_escapou"),
                    false=NullAction()))
        ]

    key "K_SPACE" action Function(pulsar_ritmo_drenagem)

    $ _em_sintonia = (60 <= pulso_cardiaco <= 85)
    $ _alto_demais = (pulso_cardiaco > 85)

    add Solid("#0a0205cc")

    frame:
        xalign 0.5 yalign 0.5
        xysize (780, 410)
        background "#16060cf5"
        padding (32, 28)

        vbox:
            spacing 14
            xalign 0.5

            text "💓 CADÊNCIA DO TRANSE: [nome_alvo]" size 26 color "#ff2266" bold True xalign 0.5
            if (not modo_teste) and fome_sangue < 20:
                text "⚠️ TREMOR DE ABSTINÊNCIA ATIVO! (Sede Crítica oscila a pressão arterial de forma errática!)" size 15 bold True color "#ff6644" xalign 0.5
            text "Mantenha o batimento entre 60%% e 85%%! Zerar o pulso faz a presa escapar; passar de 85%% gera ruído." size 16 color "#e0d4d8" xalign 0.5

            text ("Pressão Arterial: [pulso_cardiaco]%% " + ("(SINTONIA PERFEITA!)" if _em_sintonia else ("(PERIGO: RUÍDO!)" if _alto_demais else "(PULSO FRACO!)"))) size 17 bold True color ("#00ffcc" if _em_sintonia else ("#ff3333" if _alto_demais else "#ffbb55"))

            fixed:
                xysize (660, 32)
                add Solid("#221018") xysize (660, 32)
                # Zona de Êxtase (60% a 85% de 660px -> xpos 396, width 165)
                add Solid("#00cc8866") xpos 396 ypos 0 xysize (165, 32)
                bar:
                    value pulso_cardiaco
                    range 100
                    xysize (660, 32)
                    left_bar Solid("#00ffaa" if _em_sintonia else ("#ff2222" if _alto_demais else "#cc5577"))
                    right_bar Solid("#00000000")

            text "Sincronia da Drenagem ([progresso_drenagem]%%)" size 17 color "#88ffee"
            bar:
                value progresso_drenagem
                range 100
                xysize (660, 26)
                left_bar Solid("#00ddaa")
                right_bar Solid("#1a1a24")

            null height 6

            hbox:
                spacing 24
                xalign 0.5
                textbutton "💓 [[ PULSAR RITMO (ESPAÇO) ]]":
                    padding (26, 12)
                    background "#880033"
                    hover_background "#cc0055"
                    text_size 19
                    text_bold True
                    text_color "#ffffff"
                    action Function(pulsar_ritmo_drenagem)

                textbutton "⚠️ [[ RASGAR VEIA (BRUTAL) ]]":
                    padding (20, 12)
                    background "#3a0a10"
                    hover_background "#66111c"
                    text_size 18
                    text_color "#ffaaaa"
                    if modo_teste:
                        action [Hide("qte_pulso_sangue"), Function(_notificar_triade, "🩸 TESTE PULSO: BRUTAL", "Drenagem violenta encerrada.", "#ff4444")]
                    else:
                        action Return("transe_violento")

                if modo_teste:
                    textbutton "✖ Fechar":
                        padding (16, 12)
                        background "#22222c"
                        text_size 17
                        action Hide("qte_pulso_sangue")


# ==============================================================================
# TELA DE GESTÃO DO COVIL & REDE DO FUNDÃO (MÓDULO 2 — SIMBRO)
# ==============================================================================

screen painel_gestao_caldeiras(em_call=False, z_camada=210):
    modal True
    zorder 210

    add Solid("#06070ce8")

    frame:
        align (0.5, 0.5)
        xysize (1620, 880)
        background "#11121af5"
        padding (30, 26)

        vbox:
            spacing 16

            hbox:
                xfill True
                text "🏗️ GESTÃO DO COVIL & REDE CLANDESTINA DO FUNDÃO" size 28 bold True color "#ffbb55"
                textbutton "✖ [[ FECHAR ]]":
                    xalign 1.0
                    text_size 22
                    text_bold True
                    text_color "#ff6666"
                    action (Return() if em_call else Hide("painel_gestao_caldeiras"))

            hbox:
                spacing 30
                text "💵 Créditos: $[dinheiro_jogador]" size 20 bold True color "#66ff99"
                text "⚙️ Sucata Eletrônica: [sucata_eletronica]x" size 20 bold True color "#88ccff"
                text "🩸 Bolsas Adulteradas: [bolsa_sangue_adulterado]x | Filtradas: [bolsa_sangue_filtrado]x" size 19 color "#ff8899"
                text "🚨 Risco de Batida do Grêmio: [risco_rede_fundao]%%" size 20 bold True color ("#ff3344" if risco_rede_fundao >= 65 else "#ffcc44")

            hbox:
                spacing 24

                # COLUNA ESQUERDA: UPGRADES PERMANENTES DO COVIL
                frame:
                    xysize (760, 710)
                    background "#181a24ee"
                    padding (20, 18)

                    vbox:
                        spacing 14
                        text "🛠️ INFRAESTRUTURA PERMANENTE (CALDEIRAS & COVIL)" size 21 bold True color "#00ffcc"

                        for _chave in ["alambique_runico", "isolamento_acustico", "escutas_dutos", "enfermaria_clandestina"]:
                            $ _upg = CATALOGO_UPGRADES_BASE[_chave]
                            $ _ativo = upgrades_instalados.get(_chave, False)
                            frame:
                                xfill True
                                background ("#132a22" if _ativo else "#202230")
                                padding (14, 12)
                                vbox:
                                    spacing 6
                                    hbox:
                                        xfill True
                                        text "[_upg['icone']] [_upg['nome']]" size 19 bold True color ("#00ffaa" if _ativo else "#ffffff")
                                        if _ativo:
                                            text "✅ ATIVO" size 17 bold True color "#00ffaa" xalign 1.0
                                        else:
                                            textbutton "CONSTRUIR ($[_upg['custo_dinheiro']] | [_upg['custo_sucata']] Suc.)":
                                                xalign 1.0
                                                background "#3a2810"
                                                hover_background "#664418"
                                                padding (12, 6)
                                                text_size 15
                                                text_bold True
                                                text_color "#ffdd88"
                                                action Function(comprar_upgrade_base, _chave)
                                    text "[_upg['desc']]" size 15 color "#cccccc"

                # COLUNA DIREITA: CÉLULAS DE INFORMANTES DO FUNDÃO + ENCOMENDAS CLANDESTINAS
                frame:
                    xysize (760, 710)
                    background "#181a24ee"
                    padding (20, 18)

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 12
                            xsize 700
                            text "🕵️ CÉLULAS DE CONTRABANDO (TURMA DO FUNDÃO)" size 21 bold True color "#ffaa44"
                            text "A produção das células ocorre a cada amanhecer (Dia 3+). Se o Risco de Batida atingir 85%%, o Grêmio confisca recursos!" size 15 color "#bbbbcc"

                            for _idx, _ag in enumerate(equipe_fundao):
                                frame:
                                    xfill True
                                    background "#202230"
                                    padding (14, 10)
                                    vbox:
                                        spacing 6
                                        hbox:
                                            xfill True
                                            text "[_ag.nome]" size 18 bold True color "#ffffff"
                                            text "Especialidade: [_ag.especialidade!u]" size 14 color "#88ccff" xalign 1.0

                                        hbox:
                                            spacing 12
                                            text "Estamina: [_ag.estamina]%%" size 15 color ("#00ffaa" if _ag.estamina >= 50 else "#ff6655")
                                            bar value _ag.estamina range 100 xysize (200, 14) yalign 0.5
                                            text "Ordem: [_ag.tarefa_atual!u]" size 15 bold True color "#ffcc66"

                                        hbox:
                                            spacing 8
                                            for _t_id, _t_rot in [("descanso", "🛌 Descansar"), ("dinheiro", "💵 Fundos"), ("sucata", "⚙️ Sucata"), ("sangue", "🩸 Sangue")]:
                                                textbutton "[_t_rot]":
                                                    padding (10, 5)
                                                    background ("#005544" if _ag.tarefa_atual == _t_id else "#2c2e3e")
                                                    hover_background "#444860"
                                                    text_size 14
                                                    text_color ("#00ffcc" if _ag.tarefa_atual == _t_id else "#cccccc")
                                                    action Function(alterar_tarefa_agente, _idx, _t_id)

                            # SEÇÃO DE ENCOMENDAS CLANDESTINAS DE VALÉRIA
                            if "CATALOGO_ENCOMENDAS_CALDEIRAS" in globals():
                                null height 4
                                text "📜 ENCOMENDAS CLANDESTINAS DE VALÉRIA (1 CONTRATO/DIA)" size 19 bold True color "#66ffaa"

                                if getattr(store, "encomenda_caldeiras_concluida_hoje", False):
                                    frame:
                                        xfill True
                                        background "#16261d"
                                        padding (12, 10)
                                        text "✅ Cota diária de encomendas concluída hoje. Novas ordens amanhã ao amanhecer." size 15 color "#88ffaa"
                                elif getattr(store, "encomenda_caldeiras_ativa", None):
                                    $ _enc_id = encomenda_caldeiras_ativa
                                    $ _enc = CATALOGO_ENCOMENDAS_CALDEIRAS[_enc_id]
                                    $ _enc_ok = encomenda_pode_ser_concluida()
                                    frame:
                                        xfill True
                                        background ("#153024" if _enc_ok else ("#30151c" if _enc.get("emergencia") else "#222436"))
                                        padding (12, 10)
                                        vbox:
                                            spacing 6
                                            hbox:
                                                xfill True
                                                text "[_enc['icone']] CONTRATO ATIVO: [_enc['titulo']]" size 17 bold True color ("#00ffaa" if _enc_ok else "#ffcc66")
                                                text ("✅ PRONTO!" if _enc_ok else "⏳ EM ANDAMENTO") size 14 bold True color ("#00ffaa" if _enc_ok else "#ffaa66") xalign 1.0
                                            text "[_enc['desc']]" size 14 color "#dddddd"
                                            text "Recompensa: [_enc['recompensa_txt']]" size 14 color "#88ffcc"
                                            hbox:
                                                spacing 12
                                                if _enc_ok:
                                                    textbutton "🏆 [[ RESGATAR RECOMPENSA ]]":
                                                        padding (14, 6)
                                                        background "#006644"
                                                        hover_background "#009966"
                                                        text_size 15 text_bold True text_color "#ffffff"
                                                        action Function(concluir_encomenda_caldeiras)
                                                textbutton "✖ Cancelar":
                                                    padding (10, 6)
                                                    background "#332228"
                                                    text_size 14 text_color "#ffaaaa"
                                                    action [SetVariable("encomenda_caldeiras_ativa", None), SetVariable("encomenda_caldeiras_pronta", False)]
                                else:
                                    for _ek in obter_encomendas_disponiveis():
                                        $ _ed = CATALOGO_ENCOMENDAS_CALDEIRAS[_ek]
                                        frame:
                                            xfill True
                                            background ("#33141a" if _ed.get("emergencia") else "#202230")
                                            padding (10, 8)
                                            vbox:
                                                spacing 4
                                                hbox:
                                                    xfill True
                                                    text "[_ed['icone']] [_ed['titulo']]" size 16 bold True color ("#ff5566" if _ed.get("emergencia") else "#ffffff")
                                                    textbutton "ACEITAR":
                                                        xalign 1.0
                                                        padding (10, 4)
                                                        background ("#661122" if _ed.get("emergencia") else "#2a3848")
                                                        hover_background "#446688"
                                                        text_size 14 text_bold True text_color "#ffffff"
                                                        action Function(aceitar_encomenda_caldeiras, _ek)
                                                text "[_ed['desc']]  •  [_ed['recompensa_txt']]" size 13 color "#cccccc"

                            null height 4
                            $ _corrup_ui = obter_corrupcao_abissal()
                            frame:
                                xfill True
                                background "#241018"
                                padding (12, 10)
                                vbox:
                                    spacing 4
                                    text "🩸 ÍNDICE DE CORRUPÇÃO ABISSAL DE VICTOR: [_corrup_ui]%%" size 17 bold True color "#ff4477"
                                    text "Dano Base Garras de Sangue: [calcular_dano_garras_abissais()] | Capturas neste ciclo: [capturas_sofridas_ciclo]/2" size 14 color "#ddbbcc"


# ==============================================================================
# MÓDULO 3 — INTERCEPTADOR DE DERROTA NÃO-LETAL COM SEQUELAS (ELENA)
# ==============================================================================

label interceptar_derrota_combate:
    # Lutas de história obrigatórias, chefes sem fuga, exposição máxima ou reincidência levam à Morte Definitiva
    if getattr(store, "combate_historia_continua", False) or (not getattr(store, "combate_pode_fugir", True)) or capturas_sofridas_ciclo >= 2 or exposicao >= 100:
        jump morte_definitiva

    $ capturas_sofridas_ciclo += 1
    hide screen hud_combate_zona_vermelha
    hide inimigo with dissolve

    # Limpa estados temporários da arena
    $ esquiva_estimulante_ativa = False
    $ efeito_estimulante_ativo = False
    $ victor_sangramento = 0
    $ inimigo_em_guarda = False
    $ ampola_prata_ativa = False
    $ defesa_tampao_combate = 0
    $ extorquiu_combate_atual = False

    stop music fadeout 1.2
    $ th_sfx("heartbeat")
    scene black with fade

    if tipo_sangue_inimigo == "gremio":
        "Meus joelhos cedem sob a lâmina disciplinar do executor de uniforme branco. Antes que a escuridão me engula, sinto elos frios de prata se fecharem ao redor dos meus pulsos."
        $ punicoes_gremio_ativas = getattr(store, "punicoes_gremio_ativas", 0) + 1
        $ _exp_cap = aplicar_reducao_isolamento_exposicao(15)
        $ exposicao = min(100, exposicao + _exp_cap)
        $ hp_jogador = min(getattr(store, "hp_jogador_max", 100), 30)
        $ aplicar_sequela("marca_grilhao_executor", "Marca do Grilhão de Prata", "Um selo punitivo do Grêmio foi gravado em seu pulso durante a detenção.", "Vigilância elevada do Conselho (+1 Punição)")
        "Acordo jogado nos degraus gelados do Bloco Norte antes da alvorada, com o cheiro metálico de prata queimada na pele."
        "🚨 [[CAPTURA DO GRÊMIO]]: HP restaurado para 30 | +1 Punição do Grêmio | +[_exp_cap]%% Exposição."

    elif tipo_sangue_inimigo == "corrompido":
        "As garras da aberração rompem minha defesa. Caído sobre os ladrilhos úmidos, o sangue negro e espesso da criatura escorre sobre meus lábios."
        $ humanidade = max(0, humanidade - 8)
        $ ressonancia_pre_diluviana = getattr(store, "ressonancia_pre_diluviana", 0) + 2
        $ hp_jogador = min(getattr(store, "hp_jogador_max", 100), 25)
        $ aplicar_sequela("faro_contaminado", "Faro Contaminado", "O miasma abissal se alojou atrás dos seus olhos após a derrota.", "Corrupção Abissal ampliada (-8 Humanidade)")
        "Desperto horas depois no dormitório sem lembrar como rastejei de volta. Algo ancestral pulsa mais forte nas minhas veias."
        "🩸 [[CORRUPÇÃO ABISSAL]]: -8 Humanidade | +2 Ressonância Pré-Diluviana | HP restaurado para 25."

    else:
        "Caio de joelhos no corredor sombrio. Lâminas consagradas e o peso das botas esmagam minhas costelas antes que eu consiga desaparecer pela escadaria de serviço."
        $ _perda_din = min(dinheiro_jogador, 120)
        $ dinheiro_jogador -= _perda_din
        $ aplicar_sequela("queimadura_prata", "Queimadura de Prata", "Cicatrizes de prata consagrada impedem sua regeneração completa.", "-15 HP Máximo até ser tratada na Enfermaria")
        $ hp_jogador = min(getattr(store, "hp_jogador_max", 85), 25)
        "Arrasto-me de volta ao quarto perdendo sangue e recursos, mas vivo para cobrar essa dívida."
        "⚠️ [[DERROTA NÃO-LETAL]]: -$[_perda_din] perdidos | Sequela: Queimadura de Prata | HP restaurado para 25."

    $ local_atual = "dormitorio"

    # Limpa o frame de 'call iniciar_combate' da pilha para evitar vazamento de call stack
    python:
        try:
            renpy.pop_call()
        except Exception:
            pass

    jump avancar_turno_mapa
