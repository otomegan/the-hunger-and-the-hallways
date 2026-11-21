# ==============================================================================
# SISTEMAS_AVANCADOS.RPY — MICRO-FRAMEWORK DE ITENS, UI FENIKS E PAINEL DE DEBUG
# Compatível com Ren'Py 8 / Python 3 e integrado ao calendario.rpy e definitions.rpy
# ==============================================================================

# ==============================================================================
# 1. MICRO-FRAMEWORK ORIENTADO A OBJETOS PARA ITENS, LOJA E CRAFTING
# ==============================================================================
init -1 python:
    class ItemJogo:
        def __init__(self, id_item, nome, icone, categoria, descricao, var_global, preco=0, usavel=False, efeito_texto=""):
            self.id = id_item
            self.nome = nome
            self.icone = icone
            self.categoria = categoria  # "consumivel", "material", "reliquia"
            self.descricao = descricao
            self.var_global = var_global  # Conecta direto às variáveis do definitions.rpy!
            self.preco = preco
            self.usavel = usavel
            self.efeito_texto = efeito_texto

        @property
        def quantidade(self):
            val = getattr(store, self.var_global, 0)
            if isinstance(val, bool):
                return 1 if val else 0
            return val

        def adicionar(self, qtd=1):
            val = getattr(store, self.var_global, 0)
            if isinstance(val, bool):
                setattr(store, self.var_global, True)
            else:
                setattr(store, self.var_global, max(0, val + qtd))

        def remover(self, qtd=1):
            val = getattr(store, self.var_global, 0)
            if isinstance(val, bool):
                setattr(store, self.var_global, False)
            else:
                setattr(store, self.var_global, max(0, val - qtd))

    # Catálogo Mestre Sincronizado com definitions.rpy
    CATALOGO_ITENS = {
        "bolsa_sangue": ItemJogo(
            "bolsa_sangue", "Bolsa de Sangue Filtrado", "🩸", "consumivel",
            "Sangue humano refrigerado do mercado negro. Sacia a sede sem ferir inocentes.",
            "bolsa_sangue_filtrado", preco=120, usavel=True,
            efeito_texto="+35%% Saciedade | Sem perda de Humanidade"
        ),
        "bolsa_sangue_adulterado": ItemJogo(
            "bolsa_sangue_adulterado", "Bolsa de Sangue Adulterado", "☣️", "consumivel",
            "Sangue clandestino recolhido nos esgotos e caldeiras. Turvo e contaminado.",
            "bolsa_sangue_adulterado", preco=55, usavel=True,
            efeito_texto="Consumo Direto: +35%% Saciedade | -2 Humanidade | +5%% Exposição"
        ),
        "kit_curativo": ItemJogo(
            "kit_curativo", "Kit de Curativos Médicos", "🩹", "consumivel",
            "Gazes, antisséptico e linha de sutura para fechar cortes de garras e lâminas.",
            "kit_curativo", preco=70, usavel=True,
            efeito_texto="+30 HP (Vida)"
        ),
        "dose_absinto": ItemJogo(
            "dose_absinto", "Dose de Absinto Esmeralda", "🍸", "consumivel",
            "Destilado alucinógeno do Bar da Fada Verde. Abre a visão para o véu sobrenatural.",
            "dose_absinto", preco=115, usavel=True,
            efeito_texto="+1 Sensibilidade Sobrenatural | +1 Coragem"
        ),
        "giz_protecao": ItemJogo(
            "giz_protecao", "Giz de Proteção Rúnico", "🖍️", "material",
            "Giz consagrado com pó de prata. Usado em crafting ou para apagar rastros da Máscara.",
            "giz_protecao", preco=65, usavel=True,
            efeito_texto="Uso Direto: -15%% Exposição | Material de Crafting"
        ),
        "sucata_eletronica": ItemJogo(
            "sucata_eletronica", "Sucata Eletrônica", "⚙️", "material",
            "Capacitores, fios de cobre e baterias recolhidos nos armários e nas caldeiras.",
            "sucata_eletronica", preco=55, usavel=False,
            efeito_texto="Material para montar Dispositivos de Choque"
        ),
        "dispositivo_choque": ItemJogo(
            "dispositivo_choque", "Dispositivo de Choque Rúnico", "⚡", "combate",
            "Descarga de alta voltagem gravada com runas. Paralisa inimigos na Zona Vermelha.",
            "dispositivo_choque", preco=165, usavel=False,
            efeito_texto="Combate: Causa 30 de Dano (50 vs inorgânico) e Atordoa por 1 turno"
        ),
        "filtro_runico": ItemJogo(
            "filtro_runico", "Filtro Rúnico de Bolso", "🧪", "consumivel",
            "Serpentina filtrante rúnica. Purifica bolsas de sangue adulterado em sangue puro.",
            "filtro_runico", preco=135, usavel=True,
            efeito_texto="Purifica 1x Sangue Adulterado em Sangue Filtrado Puro"
        ),
        "gaze_consagrada": ItemJogo(
            "gaze_consagrada", "Gaze Consagrada", "🩹", "consumivel",
            "Ataduras embebidas em infusão de prata e pó de giz bento. Fecha cortes profundos.",
            "gaze_consagrada", preco=155, usavel=True,
            efeito_texto="+40 HP (Vida) | Estanca Hemorragias Sobrenaturais"
        ),
        "dose_estimulante": ItemJogo(
            "dose_estimulante", "Dose Estimulante Rúnica", "💉", "consumivel",
            "Seringa pneumática de absinto destilado. Desacelera o tempo e aguça os reflexos.",
            "dose_estimulante", preco=175, usavel=True,
            efeito_texto="Combate: +2.5s Timer de Reação | 50%% Chance de Esquiva"
        ),
        "cracha_falso": ItemJogo(
            "cracha_falso", "Crachá Reserva de Monitor", "🎭", "consumivel",
            "Credencial falsificada por Valéria com selo magnético do Conselho.",
            "cracha_falso", preco=160, usavel=True,
            efeito_texto="-25%% Exposição e apaga rastro olfativo fora de combate"
        ),
        "ampola_prata": ItemJogo(
            "ampola_prata", "Ampola de Prata Líquida", "🗡️", "combate",
            "Reagente alquímico corrosivo que reveste a lâmina de Victor em batalha.",
            "ampola_prata", preco=145, usavel=False,
            efeito_texto="Combate: +18 Dano na luta, ignora armadura mineral e rompe guarda"
        ),
        "tampao_hemostatico": ItemJogo(
            "tampao_hemostatico", "Coagulantes Sintéticos", "💊", "consumivel",
            "Composto militar estéril que fecha artérias abertas e cria película protetora.",
            "tampao_hemostatico", preco=110, usavel=True,
            efeito_texto="+20 HP e remove Sangramento (Combate: +6 Defesa no confronto)"
        ),
        "incenso_mirra": ItemJogo(
            "incenso_mirra", "Incenso de Mirra & Enxofre", "🕯️", "consumivel",
            "Vareta consagrada que acalma o frenesi mental longe das vigílias da capela.",
            "incenso_mirra", preco=130, usavel=True,
            efeito_texto="1x/dia (se Humanidade < 75): -25 Tensão Psicológica | +3 Humanidade"
        ),
        "sais_vigilia": ItemJogo(
            "sais_vigilia", "Sais Alquímicos de Vigília", "☕", "consumivel",
            "Estimulante seco de anfetamina rúnica usado por contrabandistas em rondas longas.",
            "sais_vigilia", preco=125, usavel=True,
            efeito_texto="1x/dia: +1 Passo neste turno e +15 HP (+10 Tensão)"
        ),
        "amuleto_estanho": ItemJogo(
            "amuleto_estanho", "Selo de Estanho Quebrado", "🧿", "consumivel",
            "Talismã antigo raspado com runas de atraso para desacelerar o Pulso das Profundezas.",
            "amuleto_estanho", preco=195, usavel=True,
            efeito_texto="-4%% DOOM (Deterioração) | Custo: +8 Tensão Psicológica"
        ),
        "presente_flores": ItemJogo(
            "presente_flores", "Buquê de Lírios Negros", "💐", "presente",
            "Lírios escuros de haste fria amarrados em fita de linho cru.",
            "presente_flores", preco=85, usavel=False,
            efeito_texto="Presente (1x/dia por heroína) — Alta afinidade com Emília"
        ),
        "presente_perfume": ItemJogo(
            "presente_perfume", "Perfume Âmbar & Sândalo", "🌸", "presente",
            "Frasco de vidro lapidado com essência noturna que encobre o cheiro de sangue.",
            "presente_perfume", preco=135, usavel=False,
            efeito_texto="Presente (1x/dia por heroína) — Alta afinidade com a Mestra e Elara"
        ),
        "presente_colar": ItemJogo(
            "presente_colar", "Colar de Prata & Granada", "📿", "presente",
            "Corrente discreta de prata 925 com pedra rubra talhada à mão.",
            "presente_colar", preco=175, usavel=False,
            efeito_texto="Presente (1x/dia por heroína) — Alta afinidade com Elara"
        ),
        "presente_roupa": ItemJogo(
            "presente_roupa", "Traje Fino / Jaqueta Sob Medida", "👗", "presente",
            "Peça clandestina de corte impecável: couro reforçado e tecido escuro nobre.",
            "presente_roupa", preco=220, usavel=False,
            efeito_texto="Presente (1x/dia por heroína) — Alta afinidade com Valéria e Emília"
        ),
        "presente_anel": ItemJogo(
            "presente_anel", "Anel de Ônix & Selo Prateado", "💍", "presente",
            "Aliança pesada de prata envelhecida com pedra de ônix polida.",
            "presente_anel", preco=260, usavel=False,
            efeito_texto="Presente de Compromisso — Cena especial se Afeto >= 6"
        ),
        "partitura_runica": ItemJogo(
            "partitura_runica", "Partitura Rúnica", "🎼", "reliquia",
            "Composição pré-diluviana recuperada no delírio da Fada Verde.",
            "tem_partitura_runica", preco=0, usavel=False,
            efeito_texto="Relíquia da Mestra"
        ),
        "relicario_sangue": ItemJogo(
            "relicario_sangue", "Relicário de Sangue Puro", "🏺", "reliquia",
            "Artefato ancestral guardado no Cofre de Contenção do Grêmio.",
            "tem_relicario_sangue", preco=0, usavel=False,
            efeito_texto="Chave do Selo Primordial (Clímax do Eclipse)"
        ),
        "chave_contencao": ItemJogo(
            "chave_contencao", "Chave de Contenção", "🗝️", "reliquia",
            "Chave mestra de Elara que controla os selos subterrâneos.",
            "tem_chave_contencao", preco=0, usavel=False,
            efeito_texto="Acesso à Câmara Subterrânea Mais Profunda"
        ),
        "grimorio_corte": ItemJogo(
            "grimorio_corte", "Páginas do Corte do Vínculo", "📜", "reliquia",
            "Transcrição do grimório inquisitorial de Lorde Phillip von Karsten.",
            "ritual_corte_vinculo_desbloqueado", preco=0, usavel=False,
            efeito_texto="Habilita o Rompimento do Grilhão no Eclipse Final"
        ),
        "soro_hemograma": ItemJogo(
            "soro_hemograma", "Soro Hemostático Hospitalar", "💉", "consumivel",
            "Injeção clínica que regenera hemácias e neutraliza traumas de punção.",
            "soro_hemograma", preco=110, usavel=True,
            efeito_texto="+15 HP e cura sequelas físicas (como Anemia Recente)"
        ),
        "elixir_carmesim": ItemJogo(
            "elixir_carmesim", "Elixir Carmesim de Sangue Puro", "🍷", "consumivel",
            "Destilado de vitae densa e concentrada para combates extremos.",
            "elixir_carmesim", preco=150, usavel=True,
            efeito_texto="+50%% Sede | -1 Humanidade | +12 Dano de Ataque (2 turnos)"
        ),
        "kit_gazua": ItemJogo(
            "kit_gazua", "Kit de Gazua de Precisão", "🗝️", "consumivel",
            "Ferramentas flexíveis alemãs de destrancamento silencioso.",
            "kit_gazua", preco=95, usavel=False,
            efeito_texto="Arromba fechaduras e armários sem disparar alarmes"
        ),
        "soro_purificador": ItemJogo(
            "soro_purificador", "Soro Purificador Antisséptico", "🧪", "consumivel",
            "Solução salina bacteriostática enriquecida com prata ionizada.",
            "soro_purificador", preco=140, usavel=True,
            efeito_texto="Converte 1x Sangue Adulterado em Sangue Filtrado Puro"
        ),
        "neutralizador_odor": ItemJogo(
            "neutralizador_odor", "Neutralizador de Odor Rúnico", "🌫️", "consumivel",
            "Spray aromático alquímico de mirra que suprime todo rastro corporal.",
            "neutralizador_odor", preco=120, usavel=True,
            efeito_texto="Mascara seu cheiro por 2 turnos contra o Faro Cruzado"
        ),
        "adrenalina_militar": ItemJogo(
            "adrenalina_militar", "Adrenalina Militar de Alta Pureza", "⚡", "consumivel",
            "Ampola de epinefrina pura para emergências médicas ou de fuga.",
            "adrenalina_militar", preco=180, usavel=True,
            efeito_texto="+25 HP imediato | +4.0 segundos no tempo de reação QTE"
        ),
        "cartao_clonado": ItemJogo(
            "cartao_clonado", "Cartão Magnético Clonado", "💳", "consumivel",
            "Credencial pirata com código de liberação dos monitores seniores.",
            "cartao_clonado", preco=250, usavel=False,
            efeito_texto="Permite passar por catracas restritas do campus"
        ),
        "sedativo_clinico": ItemJogo(
            "sedativo_clinico", "Sedativo Clínico Concentrado", "💧", "consumivel",
            "Gotas de ação rápida para amortecer sentidos e reflexos de alvos.",
            "sedativo_clinico", preco=130, usavel=True,
            efeito_texto="Amplia a Zona de Sombra do próximo Bote Furtivo em +10%%"
        ),
        "granada_fumaca": ItemJogo(
            "granada_fumaca", "Granada de Fumaça Alquímica", "💨", "combate",
            "Cápsula de dispersão densa de fósforo e enxofre.",
            "granada_fumaca", preco=175, usavel=True,
            efeito_texto="Combate: Fuga Imediata 100%% Segura | Fora: Remove Alerta de Área"
        ),
        "espelho_obsidian": ItemJogo(
            "espelho_obsidian", "Espelho de Obsidiana Rúnica", "🪞", "consumivel",
            "Vidro vulcânico antigo polido que dissipa perturbações do abismo.",
            "espelho_obsidian", preco=260, usavel=True,
            efeito_texto="-2%% DOOM | Revela a posição de todas as heroínas no mapa hoje"
        ),
        "fita_k7_amaldicoada": ItemJogo(
            "fita_k7_amaldicoada", "Fita K7 com Sussurros Subterrâneos", "📼", "consumivel",
            "Gravação magnética captada perto dos túneis da caldeira profunda.",
            "fita_k7_amaldicoada", preco=0, usavel=True,
            efeito_texto="-6%% DOOM (Deterioração) ao decodificar frequências sonoras"
        ),
        "prontuario_nora": ItemJogo(
            "prontuario_nora", "Prontuário Médico de Nora Vance", "📋", "reliquia",
            "Documentos confidenciais da Dra. Vance sobre o projeto de linhagem.",
            "prontuario_nora", preco=0, usavel=False,
            efeito_texto="Relíquia de Lore: Desbloqueia deduções sobre Nora e Rh-Nulo"
        ),
        "pigmento_alma": ItemJogo(
            "pigmento_alma", "Pigmento de Alma (Safra 1889)", "✨", "consumivel",
            "Pó mineral fluorescente coletado em resíduos de rituais antigos.",
            "pigmento_alma", preco=0, usavel=True,
            efeito_texto="Uso Direto: Converte-se em 2 unidades de Giz de Proteção Rúnico"
        ),
        "estaca_prata": ItemJogo(
            "estaca_prata", "Estaca de Prata Consagrada", "🗡️", "combate",
            "Arma ritual forjada para neutralizar entidades e gárgulas ancestrais.",
            "estaca_prata", preco=290, usavel=False,
            efeito_texto="Combate: Causa 60 de Dano Verdadeiro (custa 8 HP ao golpear)"
        ),
    }

    def usar_item_catalogo(id_item):
        item = CATALOGO_ITENS.get(id_item)
        if not item or item.quantidade <= 0:
            renpy.notify("Você não possui este item.")
            return

        if id_item == "bolsa_sangue":
            item.remover(1)
            store.fome_sangue = min(100, store.fome_sangue + 35)
            renpy.notify("🩸 Bolsa de Sangue Filtrado consumida (+35% Saciedade).")
        elif id_item == "kit_curativo":
            if store.hp_jogador >= store.hp_jogador_max:
                renpy.notify("Sua vida já está no máximo!")
                return
            item.remover(1)
            store.hp_jogador = min(store.hp_jogador_max, store.hp_jogador + 30)
            renpy.notify("🩹 Curativo aplicado (+30 HP).")
        elif id_item == "dose_absinto":
            item.remover(1)
            store.sensibilidade_sobrenatural += 1
            store.coragem += 1
            renpy.notify("🍸 Dose de Absinto consumida (+1 Sensibilidade / +1 Coragem)!")
        elif id_item == "bolsa_sangue_adulterado":
            if store.fome_sangue >= 100:
                renpy.notify("Você não sente sede no momento!")
                return
            item.remover(1)
            store.fome_sangue = min(100, store.fome_sangue + 35)
            store.humanidade = max(0, store.humanidade - 2)
            store.exposicao = min(100, store.exposicao + 5)
            renpy.notify("☣️ Sangue adulterado ingerido... Amargo e corrompido (+35% Sede / -2 Humanidade / +5% Exposição).")
        elif id_item == "giz_protecao":
            if store.exposicao <= 0:
                renpy.notify("Sua Exposição já está em 0%!")
                return
            item.remover(1)
            store.exposicao = max(0, store.exposicao - 15)
            renpy.notify("🖍️ Selo de ocultação traçado (-15% Exposição).")
        elif id_item == "filtro_runico":
            if store.bolsa_sangue_adulterado <= 0:
                renpy.notify("Você não possui nenhuma Bolsa de Sangue Adulterado para purificar!")
                return
            item.remover(1)
            store.bolsa_sangue_adulterado -= 1
            store.bolsa_sangue_filtrado += 1
            renpy.notify("🧪 Sangue purificado com sucesso! (+1 Bolsa Filtrada Pura).")
        elif id_item == "gaze_consagrada":
            if store.hp_jogador >= store.hp_jogador_max and not store.sequelas_ativas:
                renpy.notify("Sua vida já está no máximo e não há sequelas ativas!")
                return
            item.remover(1)
            store.hp_jogador = min(store.hp_jogador_max, store.hp_jogador + 40)
            if store.sequelas_ativas:
                curar_sequela(store.sequelas_ativas[0]["id"])
            renpy.notify("🩹 Gaze Consagrada aplicada (+40 HP / Sequelas tratadas).")
        elif id_item == "dose_estimulante":
            item.remover(1)
            store.efeito_estimulante_ativo = True
            store.esquiva_estimulante_ativa = True
            renpy.notify("💉 Estimulante injetado! (+2.5s de Reação & 50% Esquiva no próximo confronto).")
        elif id_item == "cracha_falso":
            if store.exposicao <= 0 and not getattr(store, "rastro_olfativo_atual", None):
                renpy.notify("Você já está limpo e com Exposição em 0%.")
                return
            item.remover(1)
            store.exposicao = max(0, store.exposicao - 25)
            store.rastro_olfativo_atual = None
            store.reagiu_olfato_turno = False
            renpy.notify("🎭 Crachá utilizado (-25% Exposição & rastro olfativo disfarçado).")
        elif id_item == "tampao_hemostatico":
            if store.hp_jogador >= store.hp_jogador_max and getattr(store, "victor_sangramento", 0) <= 0:
                renpy.notify("Sua vida já está cheia e não há sangramento ativo!")
                return
            item.remover(1)
            store.hp_jogador = min(store.hp_jogador_max, store.hp_jogador + 20)
            store.victor_sangramento = 0
            renpy.notify("💊 Coagulantes aplicados (+20 HP / sangramento estancado).")
        elif id_item == "incenso_mirra":
            if getattr(store, "usou_incenso_hoje", False):
                renpy.notify("Você já queimou incenso de mirra hoje. Aguarde o amanhecer.")
                return
            if store.humanidade >= 75 and getattr(store, "tensao_psicologica", 0) <= 0:
                renpy.notify("Sua mente e humanidade estão estáveis no momento (requer Hum < 75 ou Tensão > 0).")
                return
            item.remover(1)
            store.usou_incenso_hoje = True
            store.tensao_psicologica = max(0, getattr(store, "tensao_psicologica", 0) - 25)
            if store.humanidade < 75:
                store.humanidade = min(100, store.humanidade + 3)
            renpy.notify("🕯️ Incenso queimado (-25 Tensão Mental / +3 Humanidade).")
        elif id_item == "sais_vigilia":
            if getattr(store, "usou_sais_hoje", False):
                renpy.notify("Limite diário atingido: os sais já forçaram seu pulso hoje.")
                return
            item.remover(1)
            store.usou_sais_hoje = True
            store.passos_restantes_periodo = getattr(store, "passos_restantes_periodo", 0) + 1
            store.visitas_restantes_periodo = getattr(store, "visitas_restantes_periodo", 0) + 1
            store.hp_jogador = min(store.hp_jogador_max, store.hp_jogador + 15)
            store.tensao_psicologica = min(100, getattr(store, "tensao_psicologica", 0) + 10)
            renpy.notify("☕ Sais inalados (+1 Passo no turno / +15 HP / +10 Tensão).")
        elif id_item == "amuleto_estanho":
            if getattr(store, "ruina_cain", 0) <= 4:
                renpy.notify("A Deterioração (DOOM) já está em nível mínimo!")
                return
            item.remover(1)
            GerenciadorRuina.reduzir_ruina(4, "Selo de Estanho Quebrado")
            store.tensao_psicologica = min(100, getattr(store, "tensao_psicologica", 0) + 8)
            renpy.notify("🧿 Selo partido: -4% DOOM (+8 Tensão Psicológica).")
        elif id_item == "soro_hemograma":
            if store.hp_jogador >= store.hp_jogador_max and not store.sequelas_ativas:
                renpy.notify("Sua saúde já está plena e não há sequelas físicas.")
                return
            item.remover(1)
            store.hp_jogador = min(store.hp_jogador_max, store.hp_jogador + 15)
            if store.sequelas_ativas:
                curar_sequela(store.sequelas_ativas[0]["id"])
            renpy.notify("💉 Soro hemostático aplicado (+15 HP / sequela tratada).")
        elif id_item == "elixir_carmesim":
            item.remover(1)
            store.fome_sangue = min(100, store.fome_sangue + 50)
            store.humanidade = max(0, store.humanidade - 1)
            store.buff_ataque_elixir = 12
            store.buff_ataque_elixir_turnos = 2
            renpy.notify("🍷 Elixir Carmesim consumido (+50% Sede / -1 Humanidade / +12 Dano por 2 turnos)!")
        elif id_item == "soro_purificador":
            if getattr(store, "bolsa_sangue_adulterado", 0) > 0:
                item.remover(1)
                store.bolsa_sangue_adulterado -= 1
                store.bolsa_sangue_filtrado += 1
                renpy.notify("🧪 Sangue purificado (+1 Bolsa Filtrada Pura).")
            elif store.sequelas_ativas:
                item.remover(1)
                curar_sequela(store.sequelas_ativas[0]["id"])
                renpy.notify("🧪 Toxinas neutralizadas do organismo!")
            else:
                renpy.notify("Você não possui bolsas adulteradas ou intoxicação para purificar!")
                return
        elif id_item == "neutralizador_odor":
            item.remover(1)
            store.odor_mascarado_turnos = 2
            renpy.notify("🌫️ Neutralizador de odor aplicado (Faro Cruzado mascarado por 2 turnos).")
        elif id_item == "adrenalina_militar":
            item.remover(1)
            store.hp_jogador = min(store.hp_jogador_max, store.hp_jogador + 25)
            store.tempo_reacao += 4.0
            renpy.notify("⚡ Adrenalina injetada (+25 HP / +4.0s de reação no QTE)!")
        elif id_item == "sedativo_clinico":
            item.remover(1)
            store.sedativo_ativo_bote = True
            renpy.notify("💧 Sedativo preparado (+10% de largura na Zona de Sombra do próximo Bote)!")
        elif id_item == "granada_fumaca":
            item.remover(1)
            store.area_alerta_emboscada = False
            store.rastro_olfativo_atual = None
            renpy.notify("💨 Granada de fumaça detonada (Alerta de área dissipado e rastro apagado)!")
        elif id_item == "espelho_obsidian":
            item.remover(1)
            GerenciadorRuina.reduzir_ruina(2, "Espelho de Obsidiana")
            store.rumores_heroina_periodo = {"lility": True, "elara": True, "emilia": True, "valeria": True}
            renpy.notify("🪞 Espelho de Obsidiana ativado: -2% DOOM e heroínas reveladas no mapa hoje!")
        elif id_item == "fita_k7_amaldicoada":
            item.remover(1)
            GerenciadorRuina.reduzir_ruina(6, "Fita K7 Amaldiçoada")
            store.tensao_psicologica = min(100, getattr(store, "tensao_psicologica", 0) + 12)
            renpy.notify("📼 Frequências decodificadas: -6% DOOM (+12 Tensão Mental).")
        elif id_item == "pigmento_alma":
            item.remover(1)
            store.giz_protecao = getattr(store, "giz_protecao", 0) + 2
            renpy.notify("✨ Pigmento refinado: +2 unidades de Giz de Proteção Rúnico!")

    def comprar_item_catalogo(id_item):
        item = CATALOGO_ITENS.get(id_item)
        if not item:
            return
        if store.dinheiro_jogador >= item.preco:
            store.dinheiro_jogador -= item.preco
            item.adicionar(1)
            renpy.notify(f"💰 Comprado: +1 {item.nome} (-${item.preco})")
        else:
            renpy.notify("❌ Dinheiro insuficiente na carteira!")


# ==============================================================================
# 2. COMPONENTES DE UI ESTILO FENIKS (TOOLTIPS DINÂMICOS & ABAS UNIFICADAS)
# ==============================================================================
default aba_central_feniks = "status"

# Componente Feniks 1: Tooltip Flutuante que acompanha o Mouse ou Rodapé
screen tooltip_feniks(texto_dica):
    if texto_dica:
        zorder 150
        frame:
            xalign 0.5 yalign 0.96
            background "#0a0c14f4"
            padding (22, 10)
            hbox:
                spacing 10
                text "💡" size 20 yalign 0.5
                text "[texto_dica]" size 19 color "#00ffcc" yalign 0.5

# Componente Feniks 2: Central Tática em Abas (Substitui janelas soltas por abas rápidas)
screen central_tatica_feniks(aba_inicial="status"):
    tag menu
    modal True
    zorder 96
    on "show" action SetVariable("aba_central_feniks", aba_inicial)

    $ dica_atual = GetTooltip()

    add Solid("#07080df2")

    frame:
        align (0.5, 0.48)
        xysize (1780, 940)
        background "#12131aee"
        padding (30, 25)

        vbox:
            spacing 16

            # Barra de Navegação por Abas (Estilo Feniks Tabbed UI)
            hbox:
                xfill True
                spacing 18

                textbutton "👤 [[ ESTADO DE VICTOR ]]":
                    action SetVariable("aba_central_feniks", "status")
                    text_size 22 text_bold True
                    text_color ("#00ffcc" if aba_central_feniks == "status" else "#888888")
                    tooltip "Visualiza o aspecto físico atual, sinais vitais e atributos de RPG de Victor."

                textbutton "🎒 [[ INVENTÁRIO & CRAFTING ]]":
                    action SetVariable("aba_central_feniks", "inventario")
                    text_size 22 text_bold True
                    text_color ("#ffcc00" if aba_central_feniks == "inventario" else "#888888")
                    tooltip "Gerencia consumíveis, materiais rúnicos, relíquias e montagem de itens."

                textbutton "💞 [[ VÍNCULOS & FACÇÕES ]]":
                    action SetVariable("aba_central_feniks", "vinculos")
                    text_size 22 text_bold True
                    text_color ("#ff66aa" if aba_central_feniks == "vinculos" else "#888888")
                    tooltip "Inspeciona Afeto, Dúvida, Paciência, Resistência e Alavancagens das 4 heroínas."

                textbutton "🌟 [[ TALENTOS ([pontos_talento_victor]) ]]":
                    action SetVariable("aba_central_feniks", "talentos")
                    text_size 22 text_bold True
                    text_color ("#ffff00" if aba_central_feniks == "talentos" else "#888888")
                    tooltip "Visualiza e desbloqueia os Talentos e Perks de Victor nos 3 Ramos (Humanidade, Subterfúgio, Predador)."

                textbutton "📜 [[ LIVRO DE DÍVIDAS ]]":
                    action SetVariable("aba_central_feniks", "dividas")
                    text_size 22 text_bold True
                    text_color ("#ff9933" if aba_central_feniks == "dividas" else "#888888")
                    tooltip "Caderno de honra e débitos de Victor: veja o que deve a cada facção e quite seus favores."

                if getattr(store, "desbloqueou_mercado_negro", False) or getattr(store, "mercado_negro_desbloqueado", False):
                    textbutton "🏗️ [[ COVIL ]]":
                        action Show("painel_gestao_caldeiras", em_call=False, z_camada=98)
                        text_size 22 text_bold True
                        text_color "#ffaa44"
                        tooltip "Gerencia reformas permanentes das Caldeiras e as células clandestinas do Fundão."

                textbutton "🎞️ [[ GALERIA DE MEMÓRIAS ]]":
                    action ShowMenu("galeria_memorias")
                    text_size 22 text_bold True
                    text_color "#ff6666"
                    tooltip "Abre a Galeria de Memórias desbloqueadas para rever cenas especiais."

                if config.developer:
                    textbutton "🛠️ [[ DEBUG ]]":
                        action Show("painel_debug_interno")
                        text_size 22 text_bold True
                        text_color "#00ff66"
                        tooltip "Abre o Painel de Testes Interno (Pular Dias, Editar Status e Itens)."

                textbutton "✖ [[ FECHAR ]]":
                    action Return()
                    xalign 1.0 text_size 22 text_bold True text_color "#ffffff"

            null height 4

            # --- CONTEÚDO DA ABA 1: ESTADO DE VICTOR ---
            if aba_central_feniks == "status":
                hbox:
                    spacing 35
                    frame:
                        xysize (480, 780) background "#1a1c26" padding (20, 20)
                        vbox:
                            spacing 10 xalign 0.5
                            text "ASPECTO DE VICTOR VANE" size 22 bold True color "#88ccff" xalign 0.5
                            add obter_sprite_victor("serio") xalign 0.5 yalign 1.0 ysize 560 fit "contain"
                            text obter_descricao_fase_victor() size 16 color "#e0e0e0" xalign 0.5 text_align 0.5

                    frame:
                        xysize (1200, 780) background "#1a1c26" padding (28, 22)
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            vbox:
                                spacing 14
                                xsize 1110
                                text "📊 SINAIS VITAIS — DIA [dia_atual] • SOBREVIVÊNCIA ([periodo!u])" size 25 bold True color "#ffcc00"

                                vbox:
                                    spacing 4
                                    text "❤️ Vida (HP): [hp_jogador] / [hp_jogador_max]" size 19 color "#ffffff"
                                    bar value hp_jogador range hp_jogador_max xysize (1080, 18)

                                vbox:
                                    spacing 4
                                    text "🩸 Saciedade de Sangue: [fome_sangue]%% (Abaixo de 20%% = Sede Crítica / Frenesi & Miragens)" size 19 color "#ff6666"
                                    bar value fome_sangue range 100 xysize (1080, 18)

                                vbox:
                                    spacing 4
                                    text "🧠 Humanidade: [humanidade] / 100 (Fase 1 >= 65 | Fase 2 >= 35 | Fase 3 < 35)" size 19 color "#88ccff"
                                    bar value humanidade range 100 xysize (1080, 18)

                                vbox:
                                    spacing 4
                                    text "🎭 Exposição da Máscara: [exposicao]%% (80%%+ aciona Executores do Conselho)" size 19 color "#cc88ff"
                                    bar value exposicao range 100 xysize (1080, 18)

                                vbox:
                                    spacing 4
                                    text "⚡ DOOM: [ruina_cain]%% (Deterioração do Mundo — O Pulso das Profundezas)" size 19 bold True color ("#ff1111" if ruina_cain >= 75 else ("#ff8800" if ruina_cain >= 50 else ("#ffcc00" if ruina_cain >= 25 else "#88ccff")))
                                    bar value ruina_cain range 100 xysize (1080, 18)

                                null height 4
                                text "⚔️ ATRIBUTOS E CONHECIMENTO OCULTO" size 22 bold True color "#00ffcc"
                                grid 4 2:
                                    spacing 22
                                    text "🦁 Coragem: [coragem]" size 19 color "#ffffff"
                                    text "📘 Intelecto: [intelecto]" size 19 color "#ffffff"
                                    text "✨ Charme: [charme]" size 19 color "#ffffff"
                                    text "👁️ Sensibilidade: [sensibilidade_sobrenatural]" size 19 color "#ffffff"
                                    text "👑 Domínio: [dominio_jogador]" size 19 color "#ff9999"
                                    text "🕯️ Ocultismo: [conhecimento_oculto]" size 19 color "#ccccff"
                                    text "🔮 Ressonância: [ressonancia_pre_diluviana]" size 19 color "#ff5555"
                                    text "💰 Carteira: $[dinheiro_jogador]" size 19 color "#66ff66"

                                # PASSIVAS DA LINHAGEM PRÉ-DILUVIANA
                                if "obter_passivas_linhagem_ativas" in globals():
                                    null height 6
                                    $ _passivas_lin = obter_passivas_linhagem_ativas()
                                    $ _prox_passiva = obter_proxima_passiva_linhagem()
                                    frame:
                                        xfill True background "#24141e" padding (16, 12)
                                        vbox:
                                            spacing 6
                                            hbox:
                                                xfill True
                                                text "🩸 PASSIVAS DA LINHAGEM PRÉ-DILUVIANA" size 19 bold True color "#ff5577"
                                                text "[_prox_passiva]" size 14 color "#ddbbcc" xalign 1.0 yalign 0.5
                                            if _passivas_lin:
                                                for _p_nome, _p_desc in _passivas_lin:
                                                    text "• [_p_nome]: [_p_desc]" size 15 color "#f0dce4"
                                            else:
                                                text "Nenhuma passiva desperta ainda. Eleve sua Ressonância Pré-Diluviana através de Transes, Combates e Banquetes Ocultos." size 14 italic True color "#aaaaaa"

                                # ECOS DE SANGUE (HERANÇA PERSISTENTE)
                                if "obter_ecos_sangue_ativos" in globals():
                                    $ _ecos_ui = obter_ecos_sangue_ativos()
                                    frame:
                                        xfill True background "#181528" padding (16, 12)
                                        vbox:
                                            spacing 6
                                            text "🔮 ECOS DE SANGUE (HERANÇA DE CICLOS ANTERIORES)" size 18 bold True color "#cc88ff"
                                            if _ecos_ui:
                                                for _e_tit, _e_desc in _ecos_ui:
                                                    text "• [_e_tit]: [_e_desc]" size 14 color "#e0d0ff"
                                            else:
                                                text "Nenhum Eco de Sangue gravado ainda. Segredos profundos descobertos permanecem através de novas partidas." size 14 italic True color "#9999aa"

            # --- CONTEÚDO DA ABA 2: INVENTÁRIO DINÂMICO (MICRO-FRAMEWORK) ---
            elif aba_central_feniks == "inventario":
                hbox:
                    spacing 30
                    # Lista Dinâmica de Consumíveis e Materiais
                    frame:
                        xysize (1120, 780) background "#1a202c" padding (25, 20)
                        viewport:
                            scrollbars "vertical" mousewheel True draggable True
                            vbox:
                                spacing 14
                                text "🧪 CONSUMÍVEIS E MATERIAIS TÁTICOS" size 24 bold True color "#66ff66"

                                for id_it, obj_it in CATALOGO_ITENS.items():
                                    if obj_it.categoria in ["consumivel", "material", "combate", "presente"] and (obj_it.categoria != "presente" or obj_it.quantidade > 0):
                                        frame:
                                            xfill True background ("#2d2236" if obj_it.categoria == "presente" else ("#2f2424" if obj_it.categoria == "combate" else "#242c3d")) padding (16, 12)
                                            hbox:
                                                xfill True
                                                spacing 16
                                                if "obter_icone_item_loja" in globals():
                                                    add obter_icone_item_loja(id_it, 56) yalign 0.5
                                                vbox:
                                                    spacing 4
                                                    text "[obj_it.icone] [obj_it.nome] (x[obj_it.quantidade])" size 20 bold True color ("#ff99cc" if obj_it.categoria == "presente" else "#ffffff")
                                                    text "[obj_it.descricao]" size 15 color "#cccccc"
                                                    text "Efeito: [obj_it.efeito_texto]" size 15 color ("#ffcc66" if obj_it.categoria == "presente" else "#00ffcc")

                                                if obj_it.usavel and obj_it.quantidade > 0:
                                                    textbutton "▶ [[ USAR ]]":
                                                        action Function(usar_item_catalogo, id_it)
                                                        xalign 1.0 yalign 0.5 text_size 20 text_color "#ffcc00"
                                                        tooltip "Usa 1x [obj_it.nome] imediatamente."

                    # Painel de Crafting e Relíquias
                    frame:
                        xysize (560, 780) background "#1a202c" padding (25, 18)
                        vbox:
                            spacing 10
                            text "🔧 BANCADA DE CRAFTING RÁPIDO" size 22 bold True color "#ffcc00"
                            viewport:
                                scrollbars "vertical"
                                mousewheel True
                                draggable True
                                ysize 350
                                vbox:
                                    spacing 8
                                    # 1. Choque
                                    frame:
                                        xfill True background "#242c3d" padding (10, 8)
                                        vbox:
                                            spacing 3
                                            text "⚡ Dispositivo de Choque Rúnico ([dispositivo_choque])" size 16 bold True color "#ffffff"
                                            text "Custo: 1x Sucata ([sucata_eletronica]) + 1x Giz ([giz_protecao])" size 13 color "#aaaaaa"
                                            if sucata_eletronica >= 1 and giz_protecao >= 1:
                                                textbutton "🛠️ [[ MONTAR CHOQUE ]]":
                                                    action [
                                                        SetVariable("sucata_eletronica", sucata_eletronica - 1),
                                                        SetVariable("giz_protecao", giz_protecao - 1),
                                                        SetVariable("dispositivo_choque", dispositivo_choque + 1),
                                                        Notify("⚡ +1 Dispositivo de Choque montado!")
                                                    ]
                                                    text_size 15 text_color "#00ffcc"
                                            else:
                                                text "Materiais insuficientes" size 13 color "#ff5555"

                                    # 2. Filtro Rúnico
                                    frame:
                                        xfill True background "#242c3d" padding (10, 8)
                                        vbox:
                                            spacing 3
                                            text "🧪 Filtro Rúnico de Bolso ([filtro_runico])" size 16 bold True color "#ffffff"
                                            text "Custo: 1x Sucata ([sucata_eletronica]) + 1x Giz ([giz_protecao])" size 13 color "#aaaaaa"
                                            if sucata_eletronica >= 1 and giz_protecao >= 1:
                                                textbutton "🛠️ [[ MONTAR FILTRO ]]":
                                                    action [
                                                        SetVariable("sucata_eletronica", sucata_eletronica - 1),
                                                        SetVariable("giz_protecao", giz_protecao - 1),
                                                        SetVariable("filtro_runico", filtro_runico + 1),
                                                        Notify("🧪 +1 Filtro Rúnico de Bolso montado!")
                                                    ]
                                                    text_size 15 text_color "#00ffcc"
                                            else:
                                                text "Materiais insuficientes" size 13 color "#ff5555"

                                    # 3. Gaze Consagrada
                                    frame:
                                        xfill True background "#242c3d" padding (10, 8)
                                        vbox:
                                            spacing 3
                                            text "🩹 Gaze Consagrada ([gaze_consagrada])" size 16 bold True color "#ffffff"
                                            text "Custo: 1x Kit Curativo ([kit_curativo]) + 1x Giz ([giz_protecao])" size 13 color "#aaaaaa"
                                            if kit_curativo >= 1 and giz_protecao >= 1:
                                                textbutton "🛠️ [[ CONSAGRAR GAZE ]]":
                                                    action [
                                                        SetVariable("kit_curativo", kit_curativo - 1),
                                                        SetVariable("giz_protecao", giz_protecao - 1),
                                                        SetVariable("gaze_consagrada", gaze_consagrada + 1),
                                                        Notify("🩹 +1 Gaze Consagrada abençoada!")
                                                    ]
                                                    text_size 15 text_color "#00ffcc"
                                            else:
                                                text "Materiais insuficientes" size 13 color "#ff5555"

                                    # 4. Dose Estimulante
                                    frame:
                                        xfill True background "#242c3d" padding (10, 8)
                                        vbox:
                                            spacing 3
                                            text "💉 Dose Estimulante Rúnica ([dose_estimulante])" size 16 bold True color "#ffffff"
                                            text "Custo: 1x Sucata ([sucata_eletronica]) + 1x Absinto ([dose_absinto])" size 13 color "#aaaaaa"
                                            if sucata_eletronica >= 1 and dose_absinto >= 1:
                                                textbutton "🛠️ [[ SINTETIZAR DOSE ]]":
                                                    action [
                                                        SetVariable("sucata_eletronica", sucata_eletronica - 1),
                                                        SetVariable("dose_absinto", dose_absinto - 1),
                                                        SetVariable("dose_estimulante", dose_estimulante + 1),
                                                        Notify("💉 +1 Dose Estimulante preparada!")
                                                    ]
                                                    text_size 15 text_color "#00ffcc"
                                            else:
                                                text "Materiais insuficientes" size 13 color "#ff5555"

                            null height 6
                            text "🗝️ RELÍQUIAS DA CAMPANHA" size 20 bold True color "#ff99cc"
                            for id_rel, obj_rel in CATALOGO_ITENS.items():
                                if obj_rel.categoria == "reliquia":
                                    hbox:
                                        spacing 10
                                        text "[obj_rel.icone] [obj_rel.nome]:" size 17 color "#ffffff"
                                        if obj_rel.quantidade > 0:
                                            text "OBTIDO" size 17 bold True color "#66ff66"
                                        else:
                                            text "Pendente" size 17 color "#777777"

            # --- CONTEÚDO DA ABA 3: VÍNCULOS E FACÇÕES (INSPIRAÇÃO LS2B) ---
            elif aba_central_feniks == "vinculos":
                vbox:
                    spacing 10 xalign 0.5
                    hbox:
                        spacing 25 xalign 0.5
                        if rastro_olfativo_atual:
                            text "👃 [[AROMA ATIVO NO CASACO]]: " + obter_descricao_aroma(rastro_olfativo_atual) size 16 bold True color "#cc88ff"
                        else:
                            text "👃 [[AROMA NO CASACO]]: Limpo e Discreto" size 16 color "#88ccaa"

                        if encontro_agendado_heroina:
                            text "🌙 [[ENCONTRO AGENDADO]]: [encontro_agendado_heroina!u] em [encontro_agendado_local!u] ([encontro_agendado_periodo])" size 16 bold True color "#ffcc00"
                        else:
                            text "📜 [[ENCONTROS]]: Nenhum bilhete pendente" size 16 color "#888888"

                    grid 2 2:
                        spacing 20 xalign 0.5
                        # Lility
                        frame:
                            xysize (830, 360) background "#2a1218" padding (20, 14)
                            vbox:
                                spacing 5
                                $ _tit_dossie_m = obter_titulo_dossie_mestra()
                                text "[_tit_dossie_m]" size 22 bold True color "#ff4444"
                                text "Estágio: [estagio_mestra]/3 | Afeto: [afeto_mestra] | 🩸 Vínculo: [status_lility.vinculo_sangue] (Ativo - Criadora) | Dúvida: [duvida_mestra] | Humor: [humor_mestra!c]" size 16 color "#ffffff"
                                text "⏳ Paciência: [status_lility.paciencia]/[status_lility.paciencia_max] | 🛡️ Resistência: [status_lility.resistencia] | 🔥 Tensão: [status_lility.tensao] | ⚠️ Strikes: [status_lility.strikes]/2" size 15 color "#ffccaa"
                                $ _vis_m, _rum_m = heroina_revelada_no_mapa("lility")
                                if _vis_m:
                                    $ _nome_loc_m = obter_nome_local(loc_mestra)
                                    text ("🔍 [RUMOR] Localização: [_nome_loc_m!u]" if _rum_m else "Localização no Turno: [_nome_loc_m!u]") size 15 color "#ff9999"
                                else:
                                    text "Localização: ❓ Não rastreada (Sonde rumores ou aumente afeto)" size 15 color "#777788"
                                if status_lility.alavancagens:
                                    text "🗝️ Alavancagens: " + ", ".join(status_lility.alavancagens) size 14 color "#ffff66"
                                else:
                                    text "🗝️ Alavancagens: Nenhuma descoberta" size 14 color "#888888"
                                if verificar_marco_disponivel("lility"):
                                    text "🌟 EVENTO DE MARCO DISPONÍVEL NA SALA DE MÚSICA (NOITE)!" size 16 bold True color "#ffff00"

                        # Emília
                        frame:
                            xysize (830, 360) background "#121e2e" padding (20, 14)
                            vbox:
                                spacing 5
                                text "✝️ Emília von Karsten (Exorcista Bolsista)" size 22 bold True color "#5c85d6"
                                if pacto_emilia_ativo:
                                    text "Estágio: [estagio_emilia]/3 | Afeto: [afeto_emilia] | 🩸 Vínculo: [status_emilia.vinculo_sangue] (Pacto Sagrado) | Suspeita: [duvida_emilia] | Humor: [humor_emilia!c]" size 16 color "#ffffff"
                                else:
                                    text "Estágio: [estagio_emilia]/3 | Afeto: [afeto_emilia] | 🔒 Vínculo: Bloqueado (Requer Pacto de Sangue) | Suspeita: [duvida_emilia] | Humor: [humor_emilia!c]" size 16 color "#e0a080"
                                text "⏳ Paciência: [status_emilia.paciencia]/[status_emilia.paciencia_max] | 🛡️ Resistência: [status_emilia.resistencia] | 🔥 Tensão: [status_emilia.tensao] | ⚠️ Strikes: [status_emilia.strikes]/2" size 15 color "#88ccff"
                                $ _vis_e, _rum_e = heroina_revelada_no_mapa("emilia")
                                if _vis_e:
                                    $ _nome_loc_e = obter_nome_local(loc_emilia)
                                    text ("🔍 [RUMOR] Localização: [_nome_loc_e!u]" if _rum_e else "Localização no Turno: [_nome_loc_e!u]") size 15 color "#88ccff"
                                else:
                                    text "Localização: ❓ Não rastreada (Sonde rumores ou aumente afeto)" size 15 color "#777788"
                                if status_emilia.alavancagens:
                                    text "🗝️ Alavancagens: " + ", ".join(status_emilia.alavancagens) size 14 color "#ffff66"
                                else:
                                    text "🗝️ Alavancagens: Nenhuma descoberta" size 14 color "#888888"
                                if verificar_marco_disponivel("emilia"):
                                    text "🌟 EVENTO DE MARCO DISPONÍVEL!" size 16 bold True color "#ffff00"

                        # Valéria
                        frame:
                            xysize (830, 360) background "#122618" padding (20, 14)
                            vbox:
                                spacing 5
                                text "🧪 Valéria (Mercadora das Caldeiras)" size 22 bold True color "#2eb82e"
                                if safra_rara_valeria:
                                    text "Estágio: [estagio_valeria]/3 | Afeto: [afeto_valeria] | 🩸 Vínculo: [status_valeria.vinculo_sangue] (Safra Rara Ativa) | Dúvida: [duvida_valeria] | Humor: [humor_valeria!c]" size 16 color "#ffffff"
                                else:
                                    text "Estágio: [estagio_valeria]/3 | Afeto: [afeto_valeria] | 🔒 Vínculo: Bloqueado (Requer Negociar Safra Rara) | Dúvida: [duvida_valeria] | Humor: [humor_valeria!c]" size 16 color "#e0a080"
                                text "⏳ Paciência: [status_valeria.paciencia]/[status_valeria.paciencia_max] | 🛡️ Resistência: [status_valeria.resistencia] | 🔥 Tensão: [status_valeria.tensao] | ⚠️ Strikes: [status_valeria.strikes]/2" size 15 color "#aaffaa"
                                $ _vis_v, _rum_v = heroina_revelada_no_mapa("valeria")
                                if _vis_v:
                                    $ _nome_loc_v = obter_nome_local(loc_valeria)
                                    text ("🔍 [RUMOR] Localização: [_nome_loc_v!u]" if _rum_v else "Localização no Turno: [_nome_loc_v!u]") size 15 color "#88ff88"
                                else:
                                    text "Localização: ❓ Não rastreada (Sonde rumores ou aumente afeto)" size 15 color "#777788"
                                if status_valeria.alavancagens:
                                    text "🗝️ Alavancagens: " + ", ".join(status_valeria.alavancagens) size 14 color "#ffff66"
                                else:
                                    text "🗝️ Alavancagens: Nenhuma descoberta" size 14 color "#888888"
                                if verificar_marco_disponivel("valeria"):
                                    text "🌟 EVENTO DE MARCO DISPONÍVEL!" size 16 bold True color "#ffff00"

                        # Elara
                        frame:
                            xysize (830, 360) background "#241d29" padding (20, 14)
                            vbox:
                                spacing 5
                                text "⚖️ Presidente Elara (Conselho Estudantil)" size 22 bold True color "#ffffff"
                                if elara_subjugada_no_cofre:
                                    text "Estágio: [estagio_elara]/3 | Afeto: [afeto_elara] | 🩸 Vínculo: [status_elara.vinculo_sangue] (Presidente Subjugada) | Dúvida: [duvida_elara] | Humor: [humor_elara!c]" size 16 color "#ffffff"
                                else:
                                    text "Estágio: [estagio_elara]/3 | Afeto: [afeto_elara] | 🔒 Vínculo: Bloqueado (Requer Derrota no Cofre) | Dúvida: [duvida_elara] | Humor: [humor_elara!c]" size 16 color "#e0a080"
                                text "⏳ Paciência: [status_elara.paciencia]/[status_elara.paciencia_max] | 🛡️ Resistência: [status_elara.resistencia] | 🔥 Tensão: [status_elara.tensao] | ⚠️ Strikes: [status_elara.strikes]/2" size 15 color "#e0c0ff"
                                $ _vis_el, _rum_el = heroina_revelada_no_mapa("elara")
                                if _vis_el:
                                    $ _nome_loc_el = obter_nome_local(loc_elara)
                                    text ("🔍 [RUMOR] Localização: [_nome_loc_el!u]" if _rum_el else "Localização no Turno: [_nome_loc_el!u]") size 15 color "#dcb8ff"
                                else:
                                    text "Localização: ❓ Não rastreada (Sonde rumores ou aumente afeto)" size 15 color "#777788"
                                if status_elara.alavancagens:
                                    text "🗝️ Alavancagens: " + ", ".join(status_elara.alavancagens) size 14 color "#ffff66"
                                else:
                                    text "🗝️ Alavancagens: Nenhuma descoberta" size 14 color "#888888"
                                if verificar_marco_disponivel("elara"):
                                    text "🌟 EVENTO DE MARCO DISPONÍVEL!" size 16 bold True color "#ffff00"

            # --- CONTEÚDO DA ABA 4: TALENTOS & PERKS DE VICTOR ---
            elif aba_central_feniks == "talentos":
                vbox:
                    spacing 14
                    hbox:
                        spacing 25
                        text "🌟 ÁRVORE DE ESPECIALIZAÇÃO VAMPÍRICA" size 24 bold True color "#ffcc00"
                        text "Pontos de Talento Disponíveis: [pontos_talento_victor]" size 20 bold True color "#00ffcc"
                        if "hipnose_lility" in perks_desbloqueados:
                            textbutton "🌀 [[ ATIVAR HIPNOSE ANCESTRAL (-20%% Exposição) ]]":
                                action Function(usar_hipnose_lility)
                                text_size 16 text_bold True text_color "#ff66ff"
                                tooltip "Consome 25%% de Saciedade de Sangue para apagar 20%% de Exposição na Máscara."

                    hbox:
                        spacing 20
                        # Ramo 1: Humanidade
                        frame:
                            xysize (550, 710) background "#121e2a" padding (18, 16)
                            viewport:
                                scrollbars "vertical" mousewheel True draggable True
                                vbox:
                                    spacing 12
                                    text "🕊️ RAMO 1: HUMANIDADE & EMPATIA" size 20 bold True color "#88ccff"
                                    text "Foco em conter a sede, recuperar a confiança das alunas e preservar a alma." size 14 color "#aaaaaa"
                                    null height 4
                                    for id_p, p_data in CATALOGO_PERKS.items():
                                        if p_data["ramo"] == "Humanidade":
                                            frame:
                                                xfill True background "#1a2a3a" padding (12, 10)
                                                vbox:
                                                    spacing 4
                                                    hbox:
                                                        text "[p_data['nome']]" size 17 bold True color "#ffffff"
                                                        if id_p in perks_desbloqueados:
                                                            text " [[ ATIVO ]]" size 15 bold True color "#66ff66" xalign 1.0
                                                    text "[p_data['desc']]" size 14 color "#cccccc"
                                                    if id_p not in perks_desbloqueados:
                                                        textbutton "🔓 [[ DESBLOQUEAR (1 PT) ]]":
                                                            action Function(desbloquear_perk, id_p)
                                                            text_size 15 text_color "#ffcc00"

                        # Ramo 2: Subterfúgio
                        frame:
                            xysize (550, 710) background "#1e1828" padding (18, 16)
                            viewport:
                                scrollbars "vertical" mousewheel True draggable True
                                vbox:
                                    spacing 12
                                    text "👣 RAMO 2: SUBTERFÚGIO & INVESTIGAÇÃO" size 20 bold True color "#cc88ff"
                                    text "Foco em apagar rastros, roubar pistas no escuro e persuadir inquisidoras." size 14 color "#aaaaaa"
                                    null height 4
                                    for id_p, p_data in CATALOGO_PERKS.items():
                                        if p_data["ramo"] == "Subterfúgio":
                                            frame:
                                                xfill True background "#2a203a" padding (12, 10)
                                                vbox:
                                                    spacing 4
                                                    hbox:
                                                        text "[p_data['nome']]" size 17 bold True color "#ffffff"
                                                        if id_p in perks_desbloqueados:
                                                            text " [[ ATIVO ]]" size 15 bold True color "#66ff66" xalign 1.0
                                                    text "[p_data['desc']]" size 14 color "#cccccc"
                                                    if id_p not in perks_desbloqueados:
                                                        textbutton "🔓 [[ DESBLOQUEAR (1 PT) ]]":
                                                            action Function(desbloquear_perk, id_p)
                                                            text_size 15 text_color "#ffcc00"

                        # Ramo 3: Domínio do Predador
                        frame:
                            xysize (550, 710) background "#2a1215" padding (18, 16)
                            viewport:
                                scrollbars "vertical" mousewheel True draggable True
                                vbox:
                                    spacing 12
                                    text "🩸 RAMO 3: DOMÍNIO DO PREDADOR" size 20 bold True color "#ff5555"
                                    text "Foco em poder de abate nas catacumbas, intimidação violenta e controle mental." size 14 color "#aaaaaa"
                                    null height 4
                                    for id_p, p_data in CATALOGO_PERKS.items():
                                        if p_data["ramo"] == "Predador":
                                            frame:
                                                xfill True background "#3a1a1e" padding (12, 10)
                                                vbox:
                                                    spacing 4
                                                    hbox:
                                                        text "[p_data['nome']]" size 17 bold True color "#ffffff"
                                                        if id_p in perks_desbloqueados:
                                                            text " [[ ATIVO ]]" size 15 bold True color "#66ff66" xalign 1.0
                                                    text "[p_data['desc']]" size 14 color "#cccccc"
                                                    if id_p not in perks_desbloqueados:
                                                        textbutton "🔓 [[ DESBLOQUEAR (1 PT) ]]":
                                                            action Function(desbloquear_perk, id_p)
                                                            text_size 15 text_color "#ffcc00"

            # --- CONTEÚDO DA ABA 5: LIVRO DE DÍVIDAS DE VICTOR ---
            elif aba_central_feniks == "dividas":
                $ sincronizar_dividas_ativas()
                hbox:
                    spacing 30

                    # Coluna Esquerda: As Regras de Victor & Código de Conduta
                    frame:
                        xysize (520, 780)
                        background "#161822"
                        padding (22, 20)
                        vbox:
                            spacing 14
                            text "📜 CÓDIGO PESSOAL DE VICTOR" size 22 bold True color "#ffcc00"
                            text "“Eu não fujo de dívidas. Mas me recuso a ser descartável de novo.”" size 15 italic True color "#aaaaaa"

                            null height 6
                            text "AS 4 REGRAS NO VERSO DA BOLSA:" size 17 bold True color "#ffffff"

                            vbox:
                                spacing 10
                                for i, regra in enumerate(th_regras_texto):
                                    frame:
                                        xfill True
                                        background ("#2d181c" if (i + 1) in regras_quebradas else "#1c2230")
                                        padding (12, 10)
                                        vbox:
                                            spacing 3
                                            if (i + 1) in regras_quebradas:
                                                text ("{s}%s{/s}" % regra) size 16 color "#ff7777" strikethrough True
                                                text "⚠️ REGRA VIOLADA PELAS CIRCUNSTÂNCIAS" size 13 bold True color "#ff5555"
                                            else:
                                                text regra size 16 bold True color "#e8e8e8"
                                                text "✅ PRESERVADA INTACTA" size 13 color "#66ff66"

                            null height 10
                            text "FILOSOFIA DE SOBREVIVÊNCIA:" size 17 bold True color "#88ccff"
                            text "Na antiga universidade, Victor confiou cegamente em seu orientador e levou a culpa por uma fraude para salvar o nome da instituição. Em São Cipriano, cada favor pendente é uma corda no pescoço. Quitar suas dívidas preserva a sua Humanidade e afasta chantagens dos predadores." size 14 color "#bbbbbb"

                    # Coluna Direita: Lista de Dívidas Ativas e Botões de Quitação
                    frame:
                        xysize (1150, 780)
                        background "#161822"
                        padding (22, 20)
                        vbox:
                            spacing 12
                            hbox:
                                xfill True
                                text "⚖️ LIVRO DE DÍVIDAS & OBRIGAÇÕES ATIVAS" size 22 bold True color "#ff9933"
                                $ dividas_pendentes_count = len([d for d in registro_dividas_ativas.values() if not d.quitada])
                                text "Pendências Abertas: [dividas_pendentes_count]" size 17 bold True color ("#ff5555" if dividas_pendentes_count > 0 else "#66ff66") xalign 1.0

                            text "Selecione uma obrigação aberta para honrar seu compromisso entregando moedas, materiais ou inteligência." size 15 color "#aaaaaa"
                            if dia_atual >= 3:
                                $ _vc_div = calcular_valor_cobranca_academica()
                                $ _saldo_mon = getattr(store, "divida_monitores", 0)
                                frame:
                                    xfill True background "#1f1c28" padding (12, 8)
                                    hbox:
                                        xfill True
                                        text "⏳ Cobrança Periódica: Faltam [periodos_ate_cobranca] período(s) — Parcela: $[_vc_div]" size 15 bold True color ("#ff8888" if dinheiro_jogador < _vc_div else "#ffcc66")
                                        if _saldo_mon > 0:
                                            text "Termo nº 112 restante: $[_saldo_mon]" size 14 color "#ffaa55" xalign 1.0
                            null height 4

                            viewport:
                                scrollbars "vertical"
                                mousewheel True
                                draggable True
                                ysize 520
                                vbox:
                                    spacing 12
                                    if not registro_dividas_ativas:
                                        frame:
                                            xfill True background "#1c202d" padding (20, 20)
                                            text "Nenhuma dívida registrada até o momento. Victor está com as mãos livres." size 17 color "#888888" xalign 0.5
                                    else:
                                        for id_div, d in registro_dividas_ativas.items():
                                            frame:
                                                xfill True
                                                background ("#1a2d1e" if d.quitada else "#202535")
                                                padding (16, 14)
                                                hbox:
                                                    spacing 18
                                                    vbox:
                                                        spacing 4
                                                        xsize 760
                                                        hbox:
                                                            spacing 10
                                                            text "[d.credor_display!u]" size 19 bold True color ("#88ff88" if d.quitada else "#ffeb3b")
                                                            if d.quitada:
                                                                text "✅ [[ QUITADA & HONRADA ]]" size 15 bold True color "#66ff66"
                                                            else:
                                                                text "⏳ [[ COBRANÇA PENDENTE ]]" size 15 bold True color "#ff8800"

                                                        text "Motivo: [d.descricao]" size 15 color "#ffffff"
                                                        text "Condição de Quitação: [d.custo_descricao]" size 14 color "#00ffff"
                                                        text "Recompensa: [d.recompensa_texto]" size 13 italic True color "#aaaaaa"

                                                    vbox:
                                                        xalign 1.0 yalign 0.5
                                                        if d.quitada:
                                                            text "Obrigação Cumprida" size 15 color "#888888"
                                                        elif d.pode_quitar:
                                                            textbutton "⚖️ [[ QUITAR DÉBITO ]]":
                                                                action Function(d.quitar)
                                                                text_size 16 text_bold True text_color "#00ffcc" text_hover_color "#ffffff"
                                                                tooltip "Gasta os recursos necessários para liquidar este compromisso."
                                                        else:
                                                            text "Recursos insuficientes" size 14 color "#ff5555"

                            # Barra Inferior: Créditos a Receber
                            null height 4
                            frame:
                                xfill True
                                background "#12141c"
                                padding (12, 10)
                                hbox:
                                    spacing 15
                                    text "🤝 FAVORES A RECEBER:" size 16 bold True color "#88ddaa"
                                    if not livro_de_creditos:
                                        text "Ninguém lhe deve favores diretos no momento." size 15 color "#777777"
                                    else:
                                        for c in livro_de_creditos:
                                            text "• [c]" size 15 color "#e0e0e0"

    use tooltip_feniks(dica_atual)


# ==============================================================================
# 3. PAINEL DE DEBUG / TESTER INTERNO (ATALHO SHIFT+D OU F12)
# ==============================================================================
init python:
    def ListenerDebugInterno():
        if config.developer:
            renpy.show_screen("atalho_debug_global")

    config.overlay_screens.append("atalho_debug_global")

screen atalho_debug_global():
    if config.developer:
        key "shift_K_d" action Show("painel_debug_interno")
        key "K_F12" action Show("painel_debug_interno")

screen painel_debug_interno():
    modal True
    zorder 200

    add Solid("#000000dd")

    frame:
        align (0.5, 0.5)
        xysize (1680, 920)
        background "#0d1512"
        padding (30, 25)

        vbox:
            spacing 16
            hbox:
                xfill True
                text "🛠️ PAINEL DE DEBUG & TESTER INTERNO — THE HUNGER & THE HALLWAYS" size 28 bold True color "#00ff88"
                textbutton "✖ [[ FECHAR (SHIFT+D) ]]" action Hide("painel_debug_interno") xalign 1.0 text_size 22 text_color "#ff5555"

            hbox:
                spacing 25

                # COLUNA 1: Salto Temporal (63 Slots do calendario.rpy)
                frame:
                    xysize (520, 800) background "#14201c" padding (18, 15)
                    vbox:
                        spacing 10
                        text "⏳ 1. TELEPORTE TEMPORAL (CALENDARIO.RPY)" size 20 bold True color "#ffcc00"
                        text "Atual: Dia [dia_atual] — [periodo]" size 18 color "#ffffff"

                        hbox:
                            spacing 12
                            textbutton "Manhã" action SetVariable("periodo", "Manhã") text_color ("#00ffcc" if periodo=="Manhã" else "#888888")
                            textbutton "Tarde" action SetVariable("periodo", "Tarde") text_color ("#00ffcc" if periodo=="Tarde" else "#888888")
                            textbutton "Noite" action SetVariable("periodo", "Noite") text_color ("#00ffcc" if periodo=="Noite" else "#888888")

                        text "Escolha o Dia (Sobrevivência Livre):" size 16 color "#cccccc"
                        grid 7 3:
                            spacing 8
                            for d_num in range(1, 22):
                                textbutton "D[d_num]":
                                    action SetVariable("dia_atual", d_num)
                                    text_size 16
                                    text_color ("#00ff88" if dia_atual == d_num else "#aaaaaa")

                        null height 8
                        textbutton "🚀 [[ EXECUTAR SLOT ATUAL (JUMP SLOT_ATUAL) ]]":
                            action [Hide("painel_debug_interno"), Hide("mapa_tatico_escola"), Hide("central_tatica_feniks"), Jump("slot_atual")]
                            text_size 18 text_bold True text_color "#00ffcc"

                        textbutton "🗺️ [[ FORÇAR EXPLORAÇÃO LIVRE NESTE TURNO ]]":
                            action [Hide("painel_debug_interno"), Jump("slot_livre")]
                            text_size 17 text_color "#ffff66"

                        null height 10
                        text "Atalhos de Clímax:" size 17 bold True color "#ff8888"
                        textbutton "▶ Ir para Bar da Fada Verde (D10 Noite / DOOM 40%)" action [SetVariable("dia_atual", 10), SetVariable("periodo", "Noite"), Hide("painel_debug_interno"), Jump("slot_atual")] text_size 16
                        textbutton "▶ Ir para Baile de Máscaras (D15 Noite / DOOM 50%)" action [SetVariable("dia_atual", 15), SetVariable("periodo", "Noite"), Hide("painel_debug_interno"), Jump("slot_atual")] text_size 16
                        textbutton "▶ Ir para Lorde Phillip (D17 Tarde / DOOM 60%)" action [SetVariable("dia_atual", 17), SetVariable("periodo", "Tarde"), Hide("painel_debug_interno"), Jump("slot_atual")] text_size 16
                        textbutton "▶ Ir para Duelo no Cofre (D19 Noite / DOOM 70%)" action [SetVariable("dia_atual", 19), SetVariable("periodo", "Noite"), Hide("painel_debug_interno"), Jump("slot_atual")] text_size 16
                        textbutton "▶ Ir para Eclipse Final / Clímax (DOOM 100%)" action [SetVariable("dia_atual", 21), SetVariable("periodo", "Noite"), Hide("painel_debug_interno"), Jump("slot_atual")] text_size 16

                # COLUNA 2: Status Vitais, Fases e Recursos
                frame:
                    xysize (540, 800) background "#14201c" padding (18, 15)
                    vbox:
                        spacing 10
                        text "🩸 2. EDITOR DE STATUS E FASES DE VICTOR" size 20 bold True color "#ffcc00"

                        hbox:
                            spacing 10
                            text "HP ([hp_jogador]):" size 17 yalign 0.5
                            textbutton "100%%" action SetVariable("hp_jogador", 100)
                            textbutton "-25" action SetVariable("hp_jogador", max(1, hp_jogador - 25))

                        hbox:
                            spacing 10
                            text "Saciedade ([fome_sangue]%%):" size 17 yalign 0.5
                            textbutton "100%%" action SetVariable("fome_sangue", 100)
                            textbutton "Frenesi (10%%)" action SetVariable("fome_sangue", 10)
                            textbutton "0%%" action SetVariable("fome_sangue", 0)

                        hbox:
                            spacing 8
                            text "Humanidade ([humanidade]):" size 17 yalign 0.5
                            textbutton "F1 (80)" action SetVariable("humanidade", 80)
                            textbutton "F2 (50)" action SetVariable("humanidade", 50)
                            textbutton "F3 (15)" action SetVariable("humanidade", 15)

                        hbox:
                            spacing 10
                            text "Exposição ([exposicao]%%):" size 17 yalign 0.5
                            textbutton "0%%" action SetVariable("exposicao", 0)
                            textbutton "+25%%" action SetVariable("exposicao", min(100, exposicao + 25))
                            textbutton "85%% (Alerta)" action SetVariable("exposicao", 85)

                        null height 8
                        text "💰 3. RECURSOS, ITENS E RELÍQUIAS" size 20 bold True color "#ffcc00"
                        textbutton "💵 +$500 na Carteira (Atual: $[dinheiro_jogador])" action SetVariable("dinheiro_jogador", dinheiro_jogador + 500) text_size 17
                        textbutton "🎒 +5 de Todos os Consumíveis e Materiais" action [
                            SetVariable("bolsa_sangue_filtrado", bolsa_sangue_filtrado + 5),
                            SetVariable("kit_curativo", kit_curativo + 5),
                            SetVariable("dose_absinto", dose_absinto + 5),
                            SetVariable("dispositivo_choque", dispositivo_choque + 5),
                            SetVariable("giz_protecao", giz_protecao + 5),
                            SetVariable("sucata_eletronica", sucata_eletronica + 5),
                            Notify("+5 de todos os itens adicionados!")
                        ] text_size 17

                        textbutton "🗝️ Destravar TODAS as Relíquias e Ritual do Corte" action [
                            SetVariable("tem_partitura_runica", True),
                            SetVariable("tem_relicario_sangue", True),
                            SetVariable("tem_chave_contencao", True),
                            SetVariable("ritual_corte_vinculo_desbloqueado", True),
                            SetVariable("dominio_jogador", 5),
                            Notify("Relíquias e Ritual do Corte desbloqueados!")
                        ] text_size 17 text_color "#00ffcc"

                        null height 10
                        text "⚡ 6. TESTES RÁPIDOS — TRÍADE FLASH" size 19 bold True color "#ffaa44"
                        text "Corrupção: [obter_corrupcao_abissal()]%% | Garras: [calcular_dano_garras_abissais()] | Risco: [risco_rede_fundao]%% | Caçadas: [cacadas_realizadas_hoje]" size 14 color "#cccccc"
                        textbutton "👁️ Testar Bote Tier 1 (Calouro • Zona Azul)" action Show("radar_emboscada_furtiva", perfil_id="calouro", zona="azul", modo_teste=True) text_size 15 text_color "#66ccff"
                        textbutton "👁️ Testar Bote Tier 3 (Fundão • Zona Amarela + Finta)" action Show("radar_emboscada_furtiva", perfil_id="fundao", zona="amarela", modo_teste=True) text_size 15 text_color "#ffcc55"
                        textbutton "👁️ Testar Bote Tier 4 (Policial • Zona Vermelha + Finta)" action Show("radar_emboscada_furtiva", perfil_id="policial", zona="vermelha", modo_teste=True) text_size 15 text_color "#ff5566"
                        textbutton "🌀 Testar Miragem de Abstinência (Leitura de Pulso)" action Show("radar_emboscada_furtiva", perfil_id="miragem_abstinencia", zona="vermelha", modo_teste=True) text_size 15 text_color "#dd88ff"
                        textbutton "💓 Testar Pulso Cardíaco (Transe Rítmico)" action Show("qte_pulso_sangue", nome_alvo="Alvo de Teste", modo_teste=True) text_size 15 text_color "#ff66aa"
                        textbutton "🏗️ Abrir Gestão do Covil & Encomendas (SimBro)" action Show("painel_gestao_caldeiras", em_call=False, z_camada=210) text_size 15 text_color "#ffcc66"
                        textbutton "🌅 Simular Virada de Manhã (processar_turno_simbro)" action Function(processar_turno_simbro) text_size 15 text_color "#66ff99"
                        textbutton "🔮 +2 Ressonância (Testar Passivas Nív. 2/4/6/8)" action [SetVariable("ressonancia_pre_diluviana", ressonancia_pre_diluviana + 2), Notify("Ressonância aumentada em +2!")] text_size 15 text_color "#cc88ff"

                # COLUNA 3: Afeto, Marcos e Galeria
                frame:
                    xysize (520, 800) background "#14201c" padding (18, 15)
                    vbox:
                        spacing 12
                        text "💞 4. AFETO, MARCOS E GALERIA" size 20 bold True color "#ffcc00"

                        hbox:
                            spacing 10
                            text "[nome_display_mestra] (Afeto [afeto_mestra] | Est. [estagio_mestra]):" size 16 yalign 0.5
                            textbutton "+3 Afeto" action SetVariable("afeto_mestra", afeto_mestra + 3)
                            textbutton "Marco 1" action [Hide("painel_debug_interno"), Jump("evento_marco_lility_1")]

                        hbox:
                            spacing 10
                            text "Emília (Afeto [afeto_emilia] | Est. [estagio_emilia]):" size 16 yalign 0.5
                            textbutton "+3 Afeto" action SetVariable("afeto_emilia", afeto_emilia + 3)
                            textbutton "Marco 1" action [Hide("painel_debug_interno"), Jump("evento_marco_emilia_1")]

                        hbox:
                            spacing 10
                            text "Valéria (Afeto [afeto_valeria] | Est. [estagio_valeria]):" size 16 yalign 0.5
                            textbutton "+3 Afeto" action SetVariable("afeto_valeria", afeto_valeria + 3)
                            textbutton "Marco 1" action [Hide("painel_debug_interno"), Jump("evento_marco_valeria_1")]

                        hbox:
                            spacing 10
                            text "Elara (Afeto [afeto_elara] | Est. [estagio_elara]):" size 16 yalign 0.5
                            textbutton "+3 Afeto" action SetVariable("afeto_elara", afeto_elara + 3)
                            textbutton "Marco 1" action [Hide("painel_debug_interno"), Jump("evento_marco_elara_1")]

                        null height 6
                        text "🌟 5. ENGENHARIA SOCIAL & TALENTOS" size 18 bold True color "#ffcc00"
                        textbutton "🌟 +3 Pontos de Talento (Atual: [pontos_talento_victor])":
                            action [SetVariable("pontos_talento_victor", pontos_talento_victor + 3), Notify("+3 Pontos de Talento concedidos!")]
                            text_size 16 text_color "#ffff00"

                        textbutton "🔄 Resetar Strikes/Paciência das Heroínas":
                            action [
                                Function(status_lility.resetar_turno, True),
                                Function(status_elara.resetar_turno, True),
                                Function(status_emilia.resetar_turno, True),
                                Function(status_valeria.resetar_turno, True),
                                Notify("Paciência e Strikes de todas as heroínas foram restaurados!")
                            ]
                            text_size 16 text_color "#00ffcc"

                        null height 6
                        textbutton "🔓 [[ DESBLOQUEAR 100%% DA GALERIA DE MEMÓRIAS ]]":
                            action [
                                SetField(persistent, "mem_lility_1", True),
                                SetField(persistent, "mem_lility_2", True),
                                SetField(persistent, "mem_emilia_1", True),
                                SetField(persistent, "mem_emilia_2", True),
                                SetField(persistent, "mem_valeria_1", True),
                                SetField(persistent, "mem_valeria_2", True),
                                SetField(persistent, "mem_elara_1", True),
                                SetField(persistent, "mem_elara_2", True),
                                Notify("Todas as 8 Memórias da Galeria foram desbloqueadas!")
                            ]
                            text_size 18 text_bold True text_color "#ff66aa"

                        textbutton "🔒 Resetar Galeria (Bloquear Tudo)":
                            action [
                                SetField(persistent, "mem_lility_1", False),
                                SetField(persistent, "mem_lility_2", False),
                                SetField(persistent, "mem_emilia_1", False),
                                SetField(persistent, "mem_emilia_2", False),
                                SetField(persistent, "mem_valeria_1", False),
                                SetField(persistent, "mem_valeria_2", False),
                                SetField(persistent, "mem_elara_1", False),
                                SetField(persistent, "mem_elara_2", False),
                                Notify("Galeria resetada.")
                            ]
                            text_size 16 text_color "#888888"
