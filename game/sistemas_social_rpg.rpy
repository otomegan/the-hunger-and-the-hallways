# ==============================================================================

# SISTEMAS_SOCIAL_RPG.RPY — ENGENHARIA SOCIAL TÁTICA (INSPIRAÇÃO HAREM HEAVEN)

# 100% sincronizado com definitions.rpy, calendario.rpy e custom_screens.rpy

# ==============================================================================



# Variáveis Globais de Talentos (Perks) e Pontos de Especialização de Victor

default pontos_talento_victor = 1

default perks_desbloqueados = set()

default historico_tatico_feniks = []



# ==============================================================================

# 1. MODO ATMOSFÉRICO & LIMPO (SEM POPUPS FLUTUANTES OU TIMERS INVASIVOS)

# ==============================================================================

init -2 python:

    def notificar_rpg(titulo, descricao, cor_borda=None):

        """

        Modo Atmosférico Limpo:

        Suprime popups e janelas flutuantes na tela para preservar o clima de suspense

        e terror gótico sem poluição visual. Os eventos são registrados silenciosamente

        no histórico interno e podem ser checados na Central Tática / Vínculos.

        """

        try:

            if hasattr(store, "historico_tatico_feniks") and isinstance(store.historico_tatico_feniks, list):

                _t_clean = str(titulo).replace("%%", "%")
                _d_clean = str(descricao).replace("%%", "%")
                store.historico_tatico_feniks.append(f"{_t_clean}: {_d_clean}")

                if len(store.historico_tatico_feniks) > 30:

                    store.historico_tatico_feniks.pop(0)

        except Exception:

            pass

        return None

    th_notificar_recibo = notificar_rpg





# ==============================================================================

# 2. FRAMEWORK DE ENTIDADES PSICOLÓGICAS DAS HEROÍNAS (SINCRONIZADO)

# ==============================================================================

init -1 python:

    class HeroinaStatus:

        def __init__(self, id_heroina, nome, cor_tag, var_afeto, var_duvida, var_humor, var_vinculo, paciencia_max=3, resistencia_base=50):

            self.id = id_heroina

            self._nome = nome

            self.cor = cor_tag

            self._var_afeto = var_afeto

            self._var_duvida = var_duvida

            self._var_humor = var_humor

            self._var_vinculo = var_vinculo

            self.tensao = 0

            self.submissao = 0

            self.resistencia = resistencia_base

            self.paciencia_max = paciencia_max

            self.paciencia = paciencia_max

            self.strikes = 0

            self.max_strikes = 2

            self.bloqueada_hoje = False

            self.alavancagens = []



        @property
        def nome(self):
            if getattr(self, "id", None) == "lility":
                return getattr(store, "nome_display_mestra", "Mestra")
            if hasattr(self, "_nome") and self._nome:
                return self._nome
            raw_nome = getattr(self, "__dict__", {}).get("nome", None)
            if raw_nome:
                self._nome = raw_nome
                return raw_nome
            id_map = {
                "lility": "Mestra",
                "emilia": "Emília",
                "elara": "Elara",
                "valeria": "Valéria"
            }
            res = id_map.get(getattr(self, "id", ""), "Heroína")
            self._nome = res
            return res

        @nome.setter
        def nome(self, valor):
            self._nome = valor

        # Sincronização Bidirecional com as variáveis do definitions.rpy
        @property
        def afeto(self):
            var = getattr(self, "_var_afeto", None)
            if not var:
                var = "afeto_mestra" if getattr(self, "id", "") == "lility" else f"afeto_{getattr(self, 'id', '')}"
            return getattr(store, var, 0)

        @afeto.setter
        def afeto(self, valor):
            var = getattr(self, "_var_afeto", None)
            if not var:
                var = "afeto_mestra" if getattr(self, "id", "") == "lility" else f"afeto_{getattr(self, 'id', '')}"
            setattr(store, var, valor)

        @property
        def vinculo_sangue(self):
            var = getattr(self, "_var_vinculo", None)
            if not var:
                var = "vinculo_sangue_lility" if getattr(self, "id", "") == "lility" else f"vinculo_sangue_{getattr(self, 'id', '')}"
            return getattr(store, var, 0)

        @vinculo_sangue.setter
        def vinculo_sangue(self, valor):
            var = getattr(self, "_var_vinculo", None)
            if not var:
                var = "vinculo_sangue_lility" if getattr(self, "id", "") == "lility" else f"vinculo_sangue_{getattr(self, 'id', '')}"
            setattr(store, var, max(0, valor))

        # Alias de conveniência para suportar tanto .vinculo quanto .vinculo_sangue
        @property
        def vinculo(self):
            return self.vinculo_sangue

        @vinculo.setter
        def vinculo(self, valor):
            self.vinculo_sangue = valor

        @property
        def duvida(self):
            var = getattr(self, "_var_duvida", None)
            if not var:
                var = "duvida_mestra" if getattr(self, "id", "") == "lility" else f"duvida_{getattr(self, 'id', '')}"
            return getattr(store, var, 0)

        @duvida.setter
        def duvida(self, valor):
            var = getattr(self, "_var_duvida", None)
            if not var:
                var = "duvida_mestra" if getattr(self, "id", "") == "lility" else f"duvida_{getattr(self, 'id', '')}"
            setattr(store, var, max(0, valor))

        # Alias de conveniência para suportar tanto .duvida quanto .suspeita
        @property
        def suspeita(self):
            return self.duvida

        @suspeita.setter
        def suspeita(self, valor):
            self.duvida = valor

        @property
        def humor(self):
            var = getattr(self, "_var_humor", None)
            if not var:
                var = "humor_mestra" if getattr(self, "id", "") == "lility" else f"humor_{getattr(self, 'id', '')}"
            return getattr(store, var, "neutra")

        @humor.setter
        def humor(self, valor):
            var = getattr(self, "_var_humor", None)
            if not var:
                var = "humor_mestra" if getattr(self, "id", "") == "lility" else f"humor_{getattr(self, 'id', '')}"
            setattr(store, var, valor)



        def resetar_turno(self, novo_dia=False):

            bonus_paciencia = 1 if ("voz_tranquilizadora" in store.perks_desbloqueados and self.id in ["emilia", "elara"]) else 0

            self.paciencia = self.paciencia_max + bonus_paciencia

            self.tensao = max(0, self.tensao - 10)

            if novo_dia:

                self.strikes = 0

                self.bloqueada_hoje = False

        def recuperar_turno(self, novo_dia=False):

            return self.resetar_turno(novo_dia)



        def gastar_paciencia(self, qtd=1):

            self.paciencia = max(0, self.paciencia - qtd)

            if self.paciencia == 0:

                notificar_rpg("⏳ PACIÊNCIA ESGOTADA", f"{self.nome} perdeu a paciência com você neste período.", "#ffaa00")

            return self.paciencia > 0



        def aplicar_strike(self, motivo=""):

            self.strikes += 1

            if self.strikes >= self.max_strikes:

                self.bloqueada_hoje = True

                notificar_rpg("🚫 PORTA FECHADA [[STRIKE MÁXIMO]]", f"{self.nome} se recusa a falar com você pelo resto do dia!", "#ff3333")

            else:

                notificar_rpg(f"⚠️ ALERTA SOCIAL ({self.strikes}/{self.max_strikes})", f"{self.nome} se irritou: {motivo}", "#ff8800")



        def adicionar_alavancagem(self, nome_segredo):

            if nome_segredo not in self.alavancagens:

                self.alavancagens.append(nome_segredo)

                notificar_rpg("🗝️ NOVA ALAVANCAGEM OBTIDA", f"Segredo contra {self.nome}: {nome_segredo}", "#ffcc00")



# Instâncias Globais das 4 Heroínas (Apontando para as variáveis reais do jogo)

default status_lility = HeroinaStatus("lility", "Lility", "#c20000", "afeto_mestra", "duvida_mestra", "humor_mestra", "vinculo_sangue_lility", paciencia_max=4, resistencia_base=80)

default status_elara = HeroinaStatus("elara", "Elara", "#ffffff", "afeto_elara", "duvida_elara", "humor_elara", "vinculo_sangue_elara", paciencia_max=3, resistencia_base=65)

default status_emilia = HeroinaStatus("emilia", "Emília", "#5c85d6", "afeto_emilia", "duvida_emilia", "humor_emilia", "vinculo_sangue_emilia", paciencia_max=3, resistencia_base=40)

default status_valeria = HeroinaStatus("valeria", "Valéria", "#2eb82e", "afeto_valeria", "duvida_valeria", "humor_valeria", "vinculo_sangue_valeria", paciencia_max=4, resistencia_base=50)





# ==============================================================================

# 3. MATRIZ DE PREFERÊNCIAS MORAIS (CRITICAL HITS SOCIAIS) & DUELOS SOCIAIS

# ==============================================================================

init python:

    OPINIOES_HEROINAS = {

        "lility":  {"morbido": 2, "autoridade": 2, "compaixao": -2, "sarcasmo": 1, "submissao": 1},

        "elara":   {"morbido": -2, "autoridade": -1, "disciplina": 2, "intelecto": 2, "sarcasmo": -1},

        "emilia":  {"morbido": -2, "compaixao": 2, "gentileza": 2, "agressao": -2, "ocultismo": 1},

        "valeria": {"lucro": 2, "sarcasmo": 2, "moralismo": -2, "astucia": 2, "autoridade": 1}

    }



    def reagir_escolha(id_heroina, tag_tematica):
        status = getattr(store, f"status_{id_heroina}", None)
        if not status:
            return
        afinidade = OPINIOES_HEROINAS.get(id_heroina, {}).get(tag_tematica, 0)

        # Se a heroína estiver altamente desconfiada (dúvida >= 4), as defesas dela bloqueiam o afeto
        if status.duvida >= 4:
            if afinidade >= 2:
                status.duvida = max(0, status.duvida - 2)
                status.resistencia = max(0, status.resistencia - 10)
                status.tensao += 5
                th_stinger("afeto")
                notificar_rpg("🛡️ DESCONFIANÇA AMORTECIDA", f"{status.nome} gostou da resposta, mas ainda vigia seus passos (-2 Dúvida / Afeto bloqueado por suspeita)!", "#ffaa00")
            elif afinidade == 1:
                status.duvida = max(0, status.duvida - 1)
                status.resistencia = max(0, status.resistencia - 5)
                th_stinger("afeto")
                notificar_rpg("👍 APROVAÇÃO CAUTELOSA", f"{status.nome} concordou com cautela (-1 Dúvida).", "#00ffcc")
            elif afinidade == -1:
                status.duvida += 1
                status.resistencia = min(100, status.resistencia + 5)
                th_stinger("duvida")
                notificar_rpg("⚠️ DIVERGÊNCIA", f"{status.nome} estreitou os olhos (+1 Dúvida).", "#ffaa00")
            elif afinidade <= -2:
                status.afeto = max(0, status.afeto - 1)
                status.duvida += 2
                status.resistencia = min(100, status.resistencia + 15)
                status.gastar_paciencia(1)
                status.aplicar_strike("Postura incompatível e suspeita")
                th_stinger("duvida")
                th_bark(id_heroina, "duelo_falha")
                notificar_rpg("⚡ GAFE GRAVE [[FALHA CRÍTICA]]", f"{status.nome} confirmou suas piores suspeitas (-1 Afeto / +2 Dúvida / +1 Strike)!", "#ff3333")
            return

        # Comportamento padrão quando a dúvida está sob controle (dúvida < 4)
        if afinidade >= 2:
            status.afeto += 1
            status.tensao += 6
            status.resistencia = max(0, status.resistencia - 10)
            status.duvida = max(0, status.duvida - 1)
            th_stinger("afeto")
            th_bark(id_heroina, "crit")
            notificar_rpg("🎯 SINTONIA PERFEITA [[CRIT!]]", f"{status.nome} conectou-se com suas palavras (+1 Afeto / -10 Resistência / -1 Dúvida)!", "#ff0066")

        elif afinidade == 1:
            if status.resistencia <= 30:
                status.afeto += 1
                th_stinger("afeto")
                notificar_rpg("👍 AFINIDADE CRESCENTE", f"{status.nome} sentiu firmeza nas suas palavras (+1 Afeto).", "#00ffcc")
            else:
                status.resistencia = max(0, status.resistencia - 8)
                status.duvida = max(0, status.duvida - 1)
                th_stinger("afeto")
                notificar_rpg("👍 REAÇÃO POSITIVA", f"{status.nome} aprovou sua postura (-8 Resistência).", "#00ffcc")

        elif afinidade == -1:
            status.duvida += 1
            status.resistencia = min(100, status.resistencia + 5)
            th_stinger("duvida")
            notificar_rpg("⚠️ DIVERGÊNCIA", f"{status.nome} franziu o cenho com reserva (+1 Dúvida / +5 Resistência).", "#ffaa00")

        elif afinidade <= -2:
            status.afeto = max(0, status.afeto - 1)
            status.duvida += 2
            status.resistencia = min(100, status.resistencia + 15)
            status.gastar_paciencia(1)
            status.aplicar_strike("Postura ofensiva ou incompatível")
            th_stinger("duvida")
            th_bark(id_heroina, "duelo_falha")
            notificar_rpg("⚡ GAFE GRAVE [[FALHA CRÍTICA]]", f"{status.nome} repeliu sua atitude (-1 Afeto / +2 Dúvida / +1 Strike)!", "#ff3333")



    def tentar_acao_social(heroina, dificuldade, atributo_usado, valor_atributo, alavancagem_usada=None):

        # 1. Verifica se usou Alavancagem (Chantagem/Segredo)

        if alavancagem_usada and alavancagem_usada in heroina.alavancagens:

            heroina.alavancagens.remove(alavancagem_usada)

            heroina.resistencia = max(0, heroina.resistencia - 35)

            heroina.submissao += 2

            notificar_rpg("⚖️ ALAVANCAGEM USADA!", f"Você usou '{alavancagem_usada}' contra {heroina.nome}!", "#ffcc00")

            return (True, "chantagem_bem_sucedida")



        # 2. Bônus de Perks de Victor

        bonus_perk = 0

        if "lingua_de_prata" in store.perks_desbloqueados and atributo_usado == "charme":

            bonus_perk += 20

        if "presenca_opressora" in store.perks_desbloqueados and atributo_usado in ["coragem", "dominio", "dominio_jogador"]:

            bonus_perk += 20

        if store.humanidade < 35 and atributo_usado in ["coragem", "dominio", "dominio_jogador"]:

            bonus_perk += 15  # Fase 3 Predador intimida mais fácil



        # 3. Modificador de Fome e Palidez Vampírica (Elegibilidade Social estilo LS2B)

        bonus_fome = 0

        if store.fome_sangue >= 80 and atributo_usado == "charme":

            bonus_fome += 15  # Pele corada, olhar sereno, voz aveludada

        elif store.fome_sangue < 30:

            if atributo_usado == "charme":

                bonus_fome -= 20  # Tremores, pupila dilatada, cheiro predatório afasta aproximação suave

            elif atributo_usado in ["coragem", "dominio", "dominio_jogador"]:

                bonus_fome += 20  # Terror visceral da fera faminta intimida com facilidade



        modificador_sorte = renpy.random.randint(-5, 15)

        poder_victor = (valor_atributo * 15) + bonus_perk + bonus_fome + modificador_sorte

        dificuldade_total = dificuldade + (heroina.resistencia * 0.4) - (heroina.afeto * 2)



        if poder_victor >= dificuldade_total:

            heroina.resistencia = max(0, heroina.resistencia - 15)

            heroina.tensao += 10

            notificar_rpg("✨ SUCESSO SOCIAL!", f"{heroina.nome} cedeu à sua abordagem ({atributo_usado.upper()})!", "#00ffcc")

            return (True, "sucesso")

        else:

            heroina.gastar_paciencia(1)

            heroina.duvida += 1

            heroina.aplicar_strike(f"Falha em teste de {atributo_usado}")

            th_stinger("duvida")

            notificar_rpg("❌ PRESSÃO FRACASSOU", f"{heroina.nome} manteve a guarda e aumentou a desconfiança!", "#ff4444")

            return (False, "falha")





# ==============================================================================

# 4. ÁRVORE DE TALENTOS & PERKS DE VICTOR VANE (3 RAMOS)

# ==============================================================================

init -1 python:

    CATALOGO_PERKS = {

        # RAMO 1: HUMANIDADE & EMPATIA

        "coracao_firme": {

            "nome": "🛡️ Coração Firme",

            "ramo": "Humanidade",

            "desc": "Conter a sede pós-combate concede +2 de Humanidade em vez de +1.",

            "custo": 1

        },

        "voz_tranquilizadora": {

            "nome": "🕊️ Voz Tranquilizadora",

            "ramo": "Humanidade",

            "desc": "Emília e Elara têm +1 de Paciência máxima em todos os períodos.",

            "custo": 1

        },

        "olhar_compassivo": {

            "nome": "💙 Olhar Compassivo",

            "ramo": "Humanidade",

            "desc": "Conversar amigavelmente com Emília reduz -1 ponto de Suspeita/Dúvida dela.",

            "custo": 1

        },

        # RAMO 2: SUBTERFÚGIO & INVESTIGAÇÃO

        "passos_silenciosos": {

            "nome": "👣 Passos Silenciosos",

            "ramo": "Subterfúgio",

            "desc": "Mordidas furtivas em figurantes geram metade da Exposição (+6%% em vez de +12%%).",

            "custo": 1

        },

        "lingua_de_prata": {

            "nome": "🐍 Língua de Prata",

            "ramo": "Subterfúgio",

            "desc": "Concede +20 de bônus em todos os Duelos Sociais baseados em Charme.",

            "custo": 1

        },

        "olhos_no_escuro": {

            "nome": "👁️ Olhos no Escuro",

            "ramo": "Subterfúgio",

            "desc": "Aumenta a chance de encontrar Loot e dinheiro ao vasculhar salas.",

            "custo": 1

        },

        # RAMO 3: DOMÍNIO DO PREDADOR

        "garras_sedentas": {

            "nome": "🩸 Garras Sedentas",

            "ramo": "Predador",

            "desc": "Ataques em combate causam +20 de dano extra quando a Saciedade está abaixo de 50%%.",

            "custo": 1

        },

        "presenca_opressora": {

            "nome": "👑 Presença Opressora",

            "ramo": "Predador",

            "desc": "Concede +20 de bônus em Duelos Sociais de Coragem/Domínio e +$30 em extorsões.",

            "custo": 1

        },

        "hipnose_lility": {

            "nome": "🌀 Hipnose Ancestral",

            "ramo": "Predador",

            "desc": "Permite apagar 20%% de Exposição da Máscara usando o sangue de lacaio.",

            "custo": 1

        }

    }



    def desbloquear_perk(id_perk):

        perk = CATALOGO_PERKS.get(id_perk)

        if not perk:

            return

        if id_perk in store.perks_desbloqueados:

            renpy.notify("Este talento já está ativo!")

            return

        if store.pontos_talento_victor >= perk["custo"]:

            store.pontos_talento_victor -= perk["custo"]

            store.perks_desbloqueados.add(id_perk)

            notificar_rpg("🌟 TALENTO DESBLOQUEADO!", perk["nome"], "#ffcc00")

        else:

            renpy.notify("❌ Pontos de Talento insuficientes!")



    def usar_hipnose_lility():

        if "hipnose_lility" not in store.perks_desbloqueados:

            renpy.notify("Você não possui o talento Hipnose Ancestral desbloqueado!")

            return

        if store.fome_sangue < 25:

            renpy.notify("Saciedade de sangue insuficiente para alimentar a hipnose (requer 25%).")

            return

        store.fome_sangue -= 25

        store.exposicao = max(0, store.exposicao - 20)

        notificar_rpg("🌀 HIPNOSE ANCESTRAL", "Memórias dos guardas apagadas! (-20%% Exposição / -25%% Fome)", "#aa00ff")





# ==============================================================================

# 5. REATIVIDADE DO MAPA À FASE DE HUMANIDADE DE VICTOR

# ==============================================================================

init python:

    def verificar_reatividade_fase_no_turno():

        """Chamado em avancar_turno_mapa para aplicar os efeitos de Fase 1, 2 e 3 e rotinas de tempo."""

        for h in [store.status_lility, store.status_elara, store.status_emilia, store.status_valeria]:

            h.resetar_turno(novo_dia=(store.periodo == "Manhã"))



        # Redefine reação olfativa para o novo período

        store.reagiu_olfato_turno = False



        # Verifica se furou encontro clandestino agendado na noite anterior

        verificar_encontro_perdido()



        # Sincroniza alavancagens descobertas na história

        if store.ouviu_acordo_elara_valeria:

            store.status_elara.adicionar_alavancagem("Acordo Secreto com as Caldeiras")

            store.status_valeria.adicionar_alavancagem("Fornecimento de Sedativos ao Grêmio")

        if store.viu_partitura_lility:

            store.status_lility.adicionar_alavancagem("Melodia Incompleta do Dilúvio")



        # Efeito de Fase 2 (Desgastado) e Fase 3 (Predador)

        if store.humanidade < 35 and store.periodo == "Manhã":

            store.exposicao = min(100, store.exposicao + 5)

            notificar_rpg("🎭 MÁSCARA RACHANDO (FASE 3)", "Sua palidez e olhos carmesim assustam os alunos (+5%% Exposição).", "#cc88ff")





# ==============================================================================

# 6. ENGENHARIA DE RELACIONAMENTO & LS2B (EIXO DUPLO, SCENT SYSTEM & DATES)

# ==============================================================================

init python:

    def alimentar_de_heroina(id_heroina, qtd_sangue=40, ganho_vinculo=15, ganho_afeto=3):

        """

        Consome sangue direto da fonte de uma das 4 heroínas.

        Fortalece o Vínculo Carmesim (Kink/Predação), sacia a fome e impregna

        o casaco de Victor com o aroma característico da garota (Scent System).

        """

        store.fome_sangue = min(100, store.fome_sangue + qtd_sangue)

        store.rastro_olfativo_atual = id_heroina

        store.reagiu_olfato_turno = False



        # Mecânica de Sangue Litúrgico e Choque Místico de Linhagem

        if id_heroina == "emilia":

            store.bebeu_sangue_emilia = True

            store.sangue_liturgico_ativo = True

            notificar_rpg("✨ SANGUE LITÚRGICO", "As bênçãos da Inquisição ardem em suas veias (+15 Dano Sagrado contra aberrações)!", "#ffdd44")

        elif id_heroina == "lility":

            store.alimentou_lility_periodo = True

            if getattr(store, "sangue_liturgico_ativo", False):

                store.sangue_liturgico_ativo = False

                store.hp_jogador = max(10, store.hp_jogador - 10)

                store.ruina_cain = min(100, store.ruina_cain + 5)

                notificar_rpg("⚡ CHOQUE MÍSTICO", f"O sangue primordial de {getattr(store, 'nome_display_mestra', 'Mestra')} expeliu o veneno sagrado (-10 HP / +5% Deterioração)!", "#ff2244")



        status = getattr(store, f"status_{id_heroina}", None)

        if status:

            status.vinculo_sangue += ganho_vinculo

            status.afeto += ganho_afeto

            status.tensao = min(100, status.tensao + 15)

            status.resistencia = max(0, status.resistencia - 10)



            nome_h = getattr(status, "nome", None) or id_heroina.capitalize()

            notificar_rpg("🩸 PACTO CARMESIM", f"Você bebeu de {nome_h}. (+{qtd_sangue}%% Saciedade / +{ganho_vinculo} Vínculo)", "#ff2244")

            notificar_rpg("👃 FARO PREDATÓRIO", f"O cheiro de {nome_h} ficou impregnado no seu corpo!", "#cc88ff")



    def limpar_rastro_olfativo(motivo="Banho e Troca de Casaco"):

        """Limpa o aroma impregnado na roupa de Victor para evitar ciúmes/suspeitas."""

        antigo = store.rastro_olfativo_atual

        store.rastro_olfativo_atual = None

        store.reagiu_olfato_turno = False

        if antigo:

            notificar_rpg("🧼 VESTÍGIOS LIMPOS", f"{motivo}: Aromas de outras presas neutralizados.", "#00ffcc")



    def agendar_encontro_clandestino(id_heroina, local, periodo="Noite"):

        """Agenda um encontro clandestino noturno (Date System estilo LS2B)."""

        if store.encontro_agendado_heroina:

            renpy.notify("Você já possui um encontro clandestino agendado para hoje!")

            return False



        store.encontro_agendado_heroina = id_heroina

        store.encontro_agendado_local = local

        store.encontro_agendado_periodo = periodo

        store.encontro_agendado_dia = store.dia_atual

        store.encontro_concluido_hoje = False



        status = getattr(store, f"status_{id_heroina}", None)

        nome_h = status.nome if status else id_heroina.capitalize()

        notificar_rpg("📜 BILHETE CLANDESTINO", f"Encontro agendado com {nome_h} ({local.upper()} - {periodo.upper()})!", "#ffcc00")

        return True



    def verificar_encontro_perdido():

        """Verifica se Victor furou o encontro clandestino marcado para a noite anterior."""

        if store.encontro_agendado_heroina and not store.encontro_concluido_hoje:

            if store.periodo == "Manhã":

                id_h = store.encontro_agendado_heroina

                status = getattr(store, f"status_{id_h}", None)

                if status:

                    status.aplicar_strike("Deixada esperando sozinha no escuro da noite")

                    status.duvida += 2

                    status.afeto = max(0, status.afeto - 2)

                    notificar_rpg("💔 ENCONTRO FURADO [[PENALIDADE]]", f"{status.nome} esperou por você em vão no frio (-2 Afeto / +2 Dúvida / +1 Strike)!", "#ff3333")

                store.encontro_agendado_heroina = None

                store.encontro_agendado_local = None

                store.encontro_agendado_periodo = None



    def obter_descricao_aroma(id_aroma):

        aromas = {

            "emilia": "Incenso sagrado de mirra e cera de capela",

            "elara": "Perfume nobre de lavanda e pergaminho do Grêmio",

            "valeria": "Fumaça de cigarro mentolado e óleo das caldeiras",

            "lility": "Rosas negras e ozônio pré-diluviano"

        }

        return aromas.get(id_aroma, "Nenhum aroma detectável")





# ==============================================================================

# 7. CENAS NARRATIVAS DE FARO CRUZADO E ENCONTROS AGENDADOS (LS2B)

# ==============================================================================



label verificar_reacao_olfativa(heroina_alvo):

    if rastro_olfativo_atual and rastro_olfativo_atual != heroina_alvo and not reagiu_olfato_turno:

        $ reagiu_olfato_turno = True



        # --- REAÇÕES EMÍLIA ---

        if heroina_alvo == "emilia":

            $ th_bark("emilia", "irritada")

            if rastro_olfativo_atual == "lility":

                show emilia uniforme seria investigativa meio corpo at pulo_susto

                emilia "Victor... esse cheiro pesado no seu casaco... rosas mortas e uma aura fria que faz meu crucifixo queimar... Com que criatura você esteve?!"

                $ status_emilia.duvida += 2

                $ status_emilia.tensao += 10

            elif rastro_olfativo_atual == "valeria":

                show emilia com olhar investigativo at sprite_padrao with dissolve

                emilia "Você cheira a cinzas, tabaco e óleo de máquinas... Victor, você andou se misturando com os contrabandistas das caldeiras?"

                $ status_emilia.duvida += 1

            elif rastro_olfativo_atual == "elara":

                show emilia uniforme seria investigativa meio corpo at sprite_padrao with dissolve

                emilia "Esse aroma nobre de alfazema e cera... é o selo particular da Presidente Elara. Você andou prestando contas a portas fechadas com o Conselho?"

                $ status_emilia.tensao += 5



        # --- REAÇÕES ELARA ---

        elif heroina_alvo == "elara":

            $ th_bark("elara", "ciume")

            if rastro_olfativo_atual == "emilia":

                show elara sorriso_cinico at sprite_padrao with dissolve

                elara "Ora, ora... Mirra, cera de vela de altar e fervor juvenil. Andou assaltando a capela ou a senhorita von Karsten resolveu praticar a caridade com o seu pescoço?"

                $ status_elara.duvida += 1

            elif rastro_olfativo_atual == "valeria":

                show elara encarando com arrogancia e desprezo at sprite_padrao with dissolve

                elara "Ferrugem, fuligem e nicotina barata. Vejo que o seu paladar continua frequentando o fast-food clandestino do subsolo, Sr. Vane."

                $ status_elara.duvida += 1

            elif rastro_olfativo_atual == "lility":

                show elara encarando de forma astuta at sprite_padrao with dissolve

                elara "Um aroma arcaico e asfixiante... Cuidado, bolsista. Se a sua mestra das sombras puxar a coleira com muita força, você pode esquecer de respirar."

                $ status_elara.tensao += 15



        # --- REAÇÕES LILITY ---

        elif heroina_alvo == "lility":

            $ th_bark("lility", "ciume")

            if rastro_olfativo_atual == "emilia":

                show lility provocante at sprite_padrao with dissolve

                lility "Hmm... O cheiro doce de água benta e inocência. O meu cachorrinho gosta de comer direto da mão da Igreja enquanto finge santidade? Cuidado para não engasgar com tanta virtude."

                $ status_lility.tensao += 10

            elif rastro_olfativo_atual == "elara":

                show lility meio corpo desdenhando at sprite_padrao with dissolve

                lility "A tirana do Grêmio perfumou a sua coleira com lavanda? Não me diga que você acha excitante a burocracia dos humanos nobres, Victor..."

            elif rastro_olfativo_atual == "valeria":

                show lility encarando sorrindo com boca fechada at sprite_padrao with dissolve

                lility "Graxa, caldeiras e nicotina... Até os ratos das minhas catacumbas têm mais requinte ao escolher a fonte de sustento, meu doce lacaio."



        # --- REAÇÕES VALÉRIA ---

        elif heroina_alvo == "valeria":

            $ th_bark("valeria", "irritada")

            if rastro_olfativo_atual == "emilia":

                show valeria confusa interrogacao at sprite_padrao with dissolve

                valeria "Ih, rapaz... cheiro de mirra e água benta? Se a caçadora von Karsten te seguiu até aqui, Victor, eu vou te cobrar taxa de risco de vida em dobro!"

            elif rastro_olfativo_atual == "elara":

                show valeria cinica confiante meio corpo at sprite_padrao with dissolve

                valeria "Cheirando a perfume importado do Grêmio e papel timbrado... A Presidente te deu um aumento de bolsa ou veio fiscalizar meu estoque clandestino?"

            elif rastro_olfativo_atual == "lility":

                show valeria seria neutra meio corpo at sprite_padrao with dissolve

                valeria "Caramba... que arrepio no pescoço só de você chegar perto. Quem foi que mordeu você, Vane? Parece que você acabou de sair de um necrotério congelado..."

    return





label verificar_encontro_agendado(heroina_alvo, local_visitado):

    if (encontro_agendado_heroina == heroina_alvo and 

        (not encontro_agendado_local or local_visitado == encontro_agendado_local) and

        periodo == encontro_agendado_periodo and 

        dia_atual == encontro_agendado_dia and 

        not encontro_concluido_hoje):



        $ encontro_concluido_hoje = True

        $ encontro_agendado_heroina = None

        $ encontro_agendado_local = None

        $ encontro_agendado_periodo = None



        $ _nome_enc = (nome_display_mestra if heroina_alvo == "lility" else heroina_alvo.capitalize())
        "🌙 [[ENCONTRO CLANDESTINO AGENDADO]]: Você encontra [_nome_enc] esperando no local combinado, envolta nas sombras da noite."



        if heroina_alvo == "emilia":

            show emilia uniforme corada timida meio corpo at sprite_padrao with dissolve

            emilia "Você veio, Victor... Eu estava rezando para que não tivesse sido interceptado pela ronda do meu pai. Aproxime-se... o que combinamos fica apenas entre nós."

            call executar_transe_sangue("emilia") from _call_executar_transe_sangue_8

            $ alimentar_de_heroina("emilia", qtd_sangue=50, ganho_vinculo=20, ganho_afeto=3)

            hide cena with dissolve
            call restaurar_fundo_local_atual
            show emilia uniforme corada timida meio corpo at sprite_padrao with dissolve

        elif heroina_alvo == "elara":

            show elara sorriso_cinico at sprite_padrao with dissolve

            elara "Pontualidade britânica, Victor. Tranque a porta do Grêmio. O que o Conselho não vê, a Inquisição não julga."

            $ alimentar_de_heroina("elara", qtd_sangue=50, ganho_vinculo=20, ganho_afeto=3)

        elif heroina_alvo == "valeria":

            show valeria provocante at sprite_padrao with dissolve

            valeria "Olha ele aí. Trouxe a sua parte do trato? Senta aí no caixote... essa safra reservada é só pra quem sabe fechar contrato no escuro."

            $ alimentar_de_heroina("valeria", qtd_sangue=50, ganho_vinculo=20, ganho_afeto=3)

        elif heroina_alvo == "lility":

            show lility provocante at sprite_padrao with dissolve

            lility "Um encontro marcado no meu próprio covil... Você aprende rápido a cultivar o veneno da noite, meu doce escravo. Venha reclamar a sua herança."

            call executar_transe_sangue("lility") from _call_executar_transe_sangue_9

            $ alimentar_de_heroina("lility", qtd_sangue=50, ganho_vinculo=20, ganho_afeto=3)

            hide cena with dissolve
            call restaurar_fundo_local_atual
            show lility provocante at sprite_padrao with dissolve



        "O encontro secreto foi um sucesso absoluto. (+50%% Saciedade / +20 Vínculo Carmesim / +3 Afeto)."

    return



