# ==============================================================================
# SISTEMA WORLD OF HORROR: RUÍNA DE CAIN, MISTÉRIOS MODULARES E SEQUELAS
# Inspirado na arquitetura de Paweł Koźmiński (panstasz)
# ==============================================================================

init -1 python:
    class MisterioCaso:
        def __init__(self, id_caso, titulo, icone, local_foco, pistas_totais, recompensa_nome, descricao):
            self.id = id_caso
            self.titulo = titulo
            self.icone = icone
            self.local_foco = local_foco
            self.pistas_totais = pistas_totais
            self.pistas_coletadas = 0
            self.resolvido = False
            self.desfecho_final = None   # "A", "B", "C"
            self.recompensa_nome = recompensa_nome
            self.descricao = descricao

        @property
        def progresso_texto(self):
            if self.resolvido:
                return f"RESOLVIDO (FINAL {self.desfecho_final})"
            return f"{self.pistas_coletadas}/{self.pistas_totais} Pistas"

        def coletar_pista(self, detalhe=None):
            if not self.resolvido:
                if self.pistas_coletadas == 0:
                    GerenciadorRuina.abrir_caso(self.id)
                self.pistas_coletadas = min(self.pistas_totais, self.pistas_coletadas + 1)
                txt = f"{self.titulo}: ({self.pistas_coletadas}/{self.pistas_totais})"
                if detalhe:
                    txt += f" — {detalhe}"
                th_stinger("pista")
                th_sfx("pena")
                notificar_rpg("🔍 PISTA ENCONTRADA", txt, "#ffcc00")
                if self.pistas_coletadas >= self.pistas_totais:
                    notificar_rpg("🗝️ CLÍMAX DO MISTÉRIO", f"Confronto decisivo disponível em {self.local_foco.upper()}!", "#ff4444")

        def concluir(self, desfecho="A"):
            if self.resolvido:
                return
            self.resolvido = True
            self.desfecho_final = desfecho
            GerenciadorRuina.fechar_caso(self.id, f"Mistério Concluído: {self.titulo}")
            notificar_rpg("🏆 CASO ENCERRADO", f"{self.titulo}: Desfecho {desfecho}! [[{self.recompensa_nome}]] obtido! (-8%% DOOM)", "#00ffcc")

    # Registro Global dos 5 Grandes Mistérios de São Cipriano
    MISTERIOS_ACADEMIA = {
        "hachishaku": MisterioCaso(
            "hachishaku",
            "A Mulher de Oito Pés",
            "👻",
            "cemiterio_nevoa",
            3,
            "Relíquia do Sal Consagrado",
            "Uma silhueta colossal de chapéu de palha com risada abafada ronda as lápides e o pátio na névoa da meia-noite."
        ),
        "loira_banheiro": MisterioCaso(
            "loira_banheiro",
            "O Espelho da Dama do Banheiro",
            "🪞",
            "banheiro_abandonado",
            3,
            "Chave de Contenção de Espelhos",
            "O espelho trincado do 2º andar sussurra o nome dos alunos marcados para a próxima doação forçada."
        ),
        "lote_necrotico": MisterioCaso(
            "lote_necrotico",
            "O Lote Necrótico das Caldeiras",
            "🧪",
            "caldeiras",
            3,
            "Filtro Alquímico Purificado",
            "Bolsas de sangue adulteradas com resíduos alquímicos transformam operários em ghouls carniceiros no subsolo."
        ),
        "partitura_carnal": MisterioCaso(
            "partitura_carnal",
            "A Partitura Carnal de Lyra von Blut",
            "🎹",
            "sala_musica",
            3,
            "Partitura Rúnica Proibida",
            "Um manuscrito proibido que ressoa com a pulsação do sarcófago nas profundezas e destrava os segredos do piano."
        ),
        "inquerito_inquisicao": MisterioCaso(
            "inquerito_inquisicao",
            "Os Arquivos Mortos da Diretoria",
            "📜",
            "salao_gremio",
            3,
            "Arquivos Confidenciais de Doações",
            "A lista confidencial de sacrifícios da diretoria que liga o colégio ao pacto de sangue com as famílias vampíricas."
        )
    }

    # Alias global para compatibilidade de chamadas
    misterios_woh = MISTERIOS_ACADEMIA

    DOOM_PERIODO = {'Manhã': 1.0, 'Tarde': 1.0, 'Noite': 1.5}
    DOOM_PRESSAO_CASO = 0.75
    DOOM_REDUCAO_CASO = 8
    DOOM_PISO_INCL = 2.5
    DOOM_DEGRAUS = [(75, 'histeria'), (50, 'toque_recolher'), (25, 'inquietante'), (0, 'normal')]

    def reiniciar_misterios_woh():
        """Reseta o progresso de todos os casos e anomalias para um Novo Jogo."""
        store.doom_casos_abertos = {}
        store.doom_alertas = []
        store.doom_resto = 0.0
        store.degrau_25_alertado = False
        store.degrau_50_alertado = False
        store.degrau_75_alertado = False
        for m in MISTERIOS_ACADEMIA.values():
            m.pistas_coletadas = 0
            m.pistas_detalhes = []
            m.resolvido = False
            m.desfecho_final = None

    class GerenciadorRuina:
        @staticmethod
        def doom_piso(dia):
            return int(10 + DOOM_PISO_INCL * (dia - 1))

        @staticmethod
        def abrir_caso(id_caso):
            if getattr(store, "doom_casos_abertos", None) is None:
                store.doom_casos_abertos = {}
            if id_caso not in store.doom_casos_abertos:
                store.doom_casos_abertos[id_caso] = getattr(store, "dia_atual", 1)

        @staticmethod
        def fechar_caso(id_caso, motivo="Mistério Concluído"):
            if getattr(store, "doom_casos_abertos", None) is not None:
                store.doom_casos_abertos.pop(id_caso, None)
            GerenciadorRuina.reduzir_ruina(DOOM_REDUCAO_CASO, motivo)

        @staticmethod
        def adicionar_ruina(qtd, motivo="Avanço da Sombra", silencioso=False):
            dia = getattr(store, "dia_atual", 1)
            store.ruina_cain = min(100, store.ruina_cain + qtd)
            store.ruina_cain = max(store.ruina_cain, GerenciadorRuina.doom_piso(dia))
            if qtd > 0 and not silencioso:
                notificar_rpg("⚡ ECO DA CRIPTA", f"+{qtd}%% DOOM ({store.ruina_cain}%% Total) — {motivo}", "#ff2244")
            GerenciadorRuina.verificar_degraus()

        @staticmethod
        def reduzir_ruina(qtd, motivo="Ritual Sagrado"):
            dia = getattr(store, "dia_atual", 1)
            novo = store.ruina_cain - qtd
            store.ruina_cain = max(GerenciadorRuina.doom_piso(dia), novo)
            notificar_rpg("🕊️ CONTENÇÃO RÚNICA", f"-{qtd}%% DOOM ({store.ruina_cain}%% Total) — {motivo}", "#66ff66")
            GerenciadorRuina.verificar_degraus()

        @staticmethod
        def avancar_ruina_periodo():
            """
            DOOM v2: O avanço cósmico é impulsionado pelo tempo e pela negligência de anomalias.
            Regra Universal: Fim de jogo exclusivamente por DOOM >= 100%.
            """
            periodo_atual = getattr(store, "periodo", "Noite")
            taxa = DOOM_PERIODO.get(periodo_atual, 1.0)
            if periodo_atual in ["Noite", "Madrugada"]:
                casos_abertos = getattr(store, "doom_casos_abertos", {})
                taxa += DOOM_PRESSAO_CASO * len(casos_abertos)
            if getattr(store, "clima_diario_id", "") == "nevoa_carmesim":
                taxa *= 1.5

            # Fome extrema não acelera o DOOM cósmico, castiga Victor com Frenesi e Tensão
            if store.fome_sangue < 15:
                th_stinger("fome")
                store.tensao_jogador = min(100, getattr(store, "tensao_jogador", 0) + 10)
                notificar_rpg("⚠️ FRENESI ATIVO", "A Besta ruge nas entranhas! Tensão extrema (+10) e risco iminente de colapso!", "#ff4444")

            store.doom_resto = getattr(store, "doom_resto", 0.0) + taxa
            inteiro = int(store.doom_resto)
            store.doom_resto -= inteiro
            if inteiro > 0:
                GerenciadorRuina.adicionar_ruina(inteiro, f"Pulso do Tempo ({periodo_atual})", silencioso=True)

            GerenciadorRuina.verificar_degraus()
            return store.ruina_cain >= 100

        @staticmethod
        def verificar_degraus():
            r = store.ruina_cain
            # Recalcula o status_escola bidirecionalmente (sobe e desce)
            for limite, estado in DOOM_DEGRAUS:
                if r >= limite:
                    store.status_escola = estado
                    break

            if getattr(store, "doom_alertas", None) is None:
                store.doom_alertas = []
            novos = [lim for lim, _ in DOOM_DEGRAUS if lim > 0 and r >= lim and lim not in store.doom_alertas]
            if novos:
                store.doom_alertas.extend(novos)
                maior = max(novos)
                if maior == 75:
                    store.degrau_75_alertado = True
                    th_stinger("zona_vermelha")
                    th_sfx("distorcao")
                    renpy.notify("⚠️ AVISO: O DOOM atingiu 75%! Névoa fétida e histeria tomam a Academia!")
                elif maior == 50:
                    store.degrau_50_alertado = True
                    th_stinger("duvida")
                    renpy.notify("⚠️ AVISO: O DOOM atingiu 50%! O Conselho decretou Toque de Recolher!")
                elif maior == 25:
                    store.degrau_25_alertado = True
                    th_stinger("duvida")
                    renpy.notify("⚠️ AVISO: O DOOM atingiu 25%! Murmúrios inquietantes nos corredores.")

        @staticmethod
        def obter_descricao_status():
            st = store.status_escola
            if st == "histeria":
                return "🔥 HISTERIA TOTAL (Inimigos +20% Dano / Névoa Tóxica)"
            elif st == "toque_recolher":
                return "⚖️ TOQUE DE RECOLHER (Executores de Elara Patrulhando)"
            elif st == "inquietante":
                return "🕯️ INQUIETANTE (Custos +20% / Murmúrios no Subsolo)"
            return "NORMALIDADE APARENTE (O Pulso das Profundezas é Calmo)"

    def aplicar_sequela(id_sequela, nome, descricao, penalidade_texto):
        for seq in store.sequelas_ativas:
            if seq["id"] == id_sequela:
                return
        store.sequelas_ativas.append({
            "id": id_sequela,
            "nome": nome,
            "descricao": descricao,
            "penalidade": penalidade_texto
        })
        if id_sequela in ("anemia_recente", "queimadura_prata", "trauma_impacto"):
            _ids_ativos = [s["id"] for s in store.sequelas_ativas]
            _pen_hp = (15 if "anemia_recente" in _ids_ativos else 0) + (15 if "queimadura_prata" in _ids_ativos else 0) + (15 if "trauma_impacto" in _ids_ativos else 0)
            store.hp_jogador_max = max(55, 100 - _pen_hp)
            store.hp_jogador = min(store.hp_jogador, store.hp_jogador_max)
        notificar_rpg("🩸 SEQUELA ADQUIRIDA", f"{nome}: {penalidade_texto}", "#ff4444")

    def curar_sequela(id_sequela):
        store.sequelas_ativas = [s for s in store.sequelas_ativas if s["id"] != id_sequela]
        if id_sequela in ("anemia_recente", "queimadura_prata", "trauma_impacto"):
            _ids_ativos = [s["id"] for s in store.sequelas_ativas]
            _pen_hp = (15 if "anemia_recente" in _ids_ativos else 0) + (15 if "queimadura_prata" in _ids_ativos else 0) + (15 if "trauma_impacto" in _ids_ativos else 0)
            store.hp_jogador_max = max(55, 100 - _pen_hp)
            if id_sequela == "anemia_recente":
                store.turnos_anemia_recente = 0
        notificar_rpg("🩹 SEQUELA TRATADA", f"Condição {id_sequela} neutralizada com sucesso.", "#00ffcc")

    def testar_pericia_rpg(atributo_nome, dificuldade=12):
        """Executa um teste d20 no estilo World of Horror."""
        import random
        th_sfx("dado")
        val_atrib = getattr(store, atributo_nome, 10)
        d20 = random.randint(1, 20)
        total = val_atrib + d20
        sucesso = total >= dificuldade
        return sucesso, total

    # ==============================================================================
    # 5. SISTEMA DE MODIFICADORES DIÁRIOS DE CLIMA & TENSÃO (DAILY MODIFIERS)
    # ==============================================================================
    CLIMAS_ACADEMIA = {
        "inspecao_gremio": {
            "nome": "Inspeção Rígida do Conselho",
            "icone": "⚔️",
            "desc": "Elara paga $240 por relatórios | +10% Exposição em infrações",
            "efeito_curto": "Executores em ronda | Relatórios do Grêmio valem 2x"
        },
        "campanha_doacao": {
            "nome": "Campanha Semestral de Sangue",
            "icone": "🩸",
            "desc": "Predação tem 85% de sucesso e +45% Sede | Flagrante custa +30% Exposição",
            "efeito_curto": "Pátio e Banheiro cheios | Predação fácil, flagrante severo"
        },
        "nevoa_carmesim": {
            "nome": "Névoa Carmesim do Abismo",
            "icone": "🌫️",
            "desc": "Inimigos batem +25%, mas dropam o dobro de moedas | DOOM avança +2%",
            "efeito_curto": "DOOM acelerado (+2%) | Inimigos perigosos com dobro de loot"
        },
        "toque_recolher": {
            "nome": "Toque de Recolher Estrito",
            "icone": "🌙",
            "desc": "Mercado Negro tem -20% de desconto | Dormir à noite gera +15% Exposição",
            "efeito_curto": "Mercado Negro 20% off | Dormitório vigiado à noite"
        },
        "chuva_vitrais": {
            "nome": "Chuva Fria nos Vitrais",
            "icone": "🌧️",
            "desc": "Heroínas começam com 4 de Paciência | Foco em diálogos internos",
            "efeito_curto": "Heroínas têm 4 de Paciência | Alunos recolhidos em salas"
        },
        "calmaria_tensa": {
            "nome": "Calmaria Ilusória",
            "icone": "🕯️",
            "desc": "Dia calmo na academia. Victor regenera +15 HP ao acordar.",
            "efeito_curto": "Dia neutro e estável | +15 HP passivo ao amanhecer"
        }
    }

    def sortear_modificador_diario():
        chaves = list(CLIMAS_ACADEMIA.keys())
        clima_ant = getattr(store, "clima_diario_id", "")
        # Anti-repetição consecutiva: garante dinamismo e variedade diária
        pool_sorteio = [c for c in chaves if c != clima_ant] if len(chaves) > 1 else chaves
        escolhido_id = renpy.random.choice(pool_sorteio)
        info = CLIMAS_ACADEMIA[escolhido_id]
        store.clima_diario_id = escolhido_id
        store.clima_diario_nome = info["nome"]
        store.clima_diario_icone = info["icone"]
        store.clima_diario_desc = info["desc"]

        # Sincroniza e reseta o estado chuvoso com precisão diária (evita travamento perpétuo)
        store.eh_dia_chuvoso = (store.clima_diario_id in ["chuva_vitrais", "chuva", "chuva_acida", "nevoeiro_sangue"] or getattr(store, "chuva_forcada_evento", False))

        if store.clima_diario_id == "calmaria_tensa":
            store.hp_jogador = min(store.hp_jogador_max, store.hp_jogador + 15)

        if store.clima_diario_id == "nevoa_carmesim":
            store.ruina_cain = min(100, store.ruina_cain + 2)

        # Ajusta paciência inicial das heroínas respeitando seus valores base
        paciencias_base = {
            "lility": 4,
            "valeria": 4,
            "elara": 3,
            "emilia": 3
        }
        for name, p_base in paciencias_base.items():
            h = getattr(store, f"status_{name}", None)
            if h is not None:
                if store.clima_diario_id == "chuva_vitrais":
                    h.paciencia_max = p_base + 1
                    h.paciencia = h.paciencia_max
                else:
                    h.paciencia_max = p_base
                    h.paciencia = min(p_base, h.paciencia)

        notificar_rpg(f"{store.clima_diario_icone} CLIMA DO DIA", f"{store.clima_diario_nome}: {info['efeito_curto']}", "#ffcc00")
