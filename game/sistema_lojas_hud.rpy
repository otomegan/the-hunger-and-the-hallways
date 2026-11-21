# ==============================================================================
# SISTEMA_LOJAS_HUD.RPY — VITRINE VISUAL 9-SLICE (CALDEIRAS & ENFERMARIA)
# ==============================================================================
# Interface visual gótica tática com suporte aos 11 moldes 9-Slice em
# 'game/gui/hud_loja/' e 24 ícones em 'game/gui/items/'.
# Layout assimétrico 60/40: Vitrine 4x2 com subpainel de detalhes à esquerda,
# e sprite da vendedora + balão 'caixa_fala_loja.png' à direita.
# ==============================================================================

default loja_item_selecionado = "bolsa_sangue"
default loja_aba_modo = "comprar"  # "comprar" ou "vender"
default loja_fala_vendedora = ""
default loja_pagina_atual = 0
default estoque_lojas_hoje = {}

# Variáveis default para o inventário expandido (compatível com saves antigos)
default soro_hemograma = 0
default elixir_carmesim = 0
default kit_gazua = 0
default soro_purificador = 0
default neutralizador_odor = 0
default adrenalina_militar = 0
default cartao_clonado = 0
default sedativo_clinico = 0
default granada_fumaca = 0
default espelho_obsidian = 0
default fita_k7_amaldicoada = 0
default prontuario_nora = 0
default pigmento_alma = 0
default estaca_prata = 0
default odor_mascarado_turnos = 0
default sedativo_ativo_bote = False
default buff_ataque_elixir = 0
default buff_ataque_elixir_turnos = 0

init 4 python:
    def obter_icone_item_loja(id_item, tamanho=104):
        """Retorna o Transform do ícone 192x192 em 'gui/items/' com fallback seguro."""
        id_str = str(id_item or "")
        candidatos = [
            id_str,
            id_str.replace("_filtrado", ""),
            id_str.replace("_consagrada", ""),
            id_str.replace("_rh_nulo", ""),
            id_str.replace("_1889", ""),
            "bolsa_sangue" if "bolsa_sangue" in id_str else id_str
        ]
        for cand in candidatos:
            caminho = f"gui/items/{cand}.png"
            if renpy.loadable(caminho):
                return Transform(caminho, xysize=(tamanho, tamanho), fit="contain")
        return Solid("#1d2029", xysize=(tamanho, tamanho))

    def frame_hud_loja(nome_png, bx=24, by=24, cor_fallback="#11141df2", tint_hex=None):
        """Carrega frame 9-Slice de 'gui/hud_loja/' com suporte a variações de extensão e fallback."""
        nomes_tentativa = [nome_png]
        if nome_png.endswith(".png"):
            nomes_tentativa.append(nome_png + ".png")
        for cand in nomes_tentativa:
            caminho = f"gui/hud_loja/{cand}"
            if renpy.loadable(caminho):
                disp = Frame(caminho, bx, by)
                if tint_hex:
                    return Transform(disp, matrixcolor=TintMatrix(tint_hex))
                return disp
        return Solid(cor_fallback)

    # --------------------------------------------------------------------------
    # CATÁLOGO EXPANDIDO DE ITENS DAS LOJAS
    # --------------------------------------------------------------------------
    ITENS_LOJA_EXPANDIDOS = {
        # --- FOLHA 1: CONSUMÍVEIS & MATERIAIS ESSENCIAIS ---
        "bolsa_sangue": {
            "nome": "Bolsa de Sangue",
            "titulo_detalhe": "BOLSA DE SANGUE FILTRADO",
            "var": "bolsa_sangue_filtrado",
            "icone_id": "bolsa_sangue",
            "lojas": ["enfermaria", "valeria"],
            "preco_enf": 165,
            "preco_val": 120,
            "tier": 1,
            "estoque_dia": 1,
            "usavel": True,
            "penhoravel": True,
            "efeito": "+35% Saciedade | Sem perda de Humanidade",
            "desc": "Restaura +35% de Saciedade (Fome de Sangue) e estanca pequenos sangramentos sem ferir inocentes.",
            "fala_val": "Bolsa intacta e lacrada. Beba longe dos fiscais da ronda se não quiser problemas com o Grêmio.",
            "fala_enf": "O ágio clínico cobre meu silêncio e o lacre da câmara fria. Esconda sob o sobretudo antes que o Conselho cheque."
        },
        "kit_curativo": {
            "nome": "Kit Curativo",
            "titulo_detalhe": "KIT DE CURATIVOS E SUTURA",
            "var": "kit_curativo",
            "icone_id": "kit_curativo",
            "lojas": ["enfermaria", "valeria"],
            "preco_enf": 105,
            "preco_val": 70,
            "tier": 1,
            "estoque_dia": 2,
            "usavel": True,
            "penhoravel": True,
            "efeito": "Recupera +30 HP (Vida)",
            "desc": "Gazes estéreis, antisséptico forte e linha cirúrgica para fechar cortes profundos fora ou em combate.",
            "fala_val": "Pra costurar o couro depois de brincar nas Zonas Vermelhas. Bem mais barato que lá em cima.",
            "fala_enf": "Material cirúrgico de primeira linha. A Fundação é rígida, mas as bandagens salvam vidas."
        },
        "soro_hemograma": {
            "nome": "Soro Coagulante",
            "titulo_detalhe": "SORO COAGULANTE CLÍNICO",
            "var": "soro_hemograma",
            "icone_id": "soro_hemograma",
            "lojas": ["enfermaria"],
            "preco_enf": 110,
            "preco_val": 85,
            "tier": 1,
            "estoque_dia": 2,
            "usavel": True,
            "penhoravel": True,
            "efeito": "Cura Sequelas Físicas (Anemia/Queimadura) + 15 HP",
            "desc": "Solução intravenosa de ferro e fatores de coagulação que restaura hemácias e cura sequelas de extração.",
            "fala_val": "Ampola hospitalar roubada da Dra. Vance. Boa para limpar hematomas e fraqueza de agulha.",
            "fala_enf": "Estabilizador hemodinâmico. Acelera a regeneração das hemácias após punções rigorosas de doação."
        },
        "elixir_carmesim": {
            "nome": "Sangue Sintético",
            "titulo_detalhe": "SANGUE SINTÉTICO CONCENTRADO",
            "var": "elixir_carmesim",
            "icone_id": "elixir_carmesim",
            "lojas": ["enfermaria", "valeria"],
            "preco_enf": 150,
            "preco_val": 130,
            "tier": 1,
            "estoque_dia": 1,
            "usavel": True,
            "penhoravel": True,
            "efeito": "+50% Saciedade | +12 Ataque (2 turnos) | -1 Humanidade",
            "desc": "Destilado rubro alquímico de alta densidade que ferve as veias com vigor predatório violento.",
            "fala_val": "Bate forte igual coice de mula. Isso rasga a couraça de qualquer sentinela de aço.",
            "fala_enf": "Amostra experimental de altíssima densidade hemática. Use com cautela extrema nos corredores."
        },
        "dose_absinto": {
            "nome": "Dose de Absinto",
            "titulo_detalhe": "ABSINTO ESMERALDA CLANDESTINO",
            "var": "dose_absinto",
            "icone_id": "dose_absinto",
            "lojas": ["valeria", "enfermaria"],
            "preco_enf": 125,
            "preco_val": 115,
            "tier": 1,
            "estoque_dia": 2,
            "usavel": True,
            "penhoravel": True,
            "efeito": "+1 Sensibilidade Sobrenatural | +1 Coragem",
            "desc": "Licor destilado da Fada Verde infusionado com losna amarga que rasga o véu entre o visível e o oculto.",
            "fala_val": "Um gole disso e você enxerga até o que se esconde atrás dos espelhos.",
            "fala_enf": "Álcool destilado medicinal de alta graduação. Confisquei de um bolsista ontem."
        },
        "kit_gazua": {
            "nome": "Kit de Gazua",
            "titulo_detalhe": "ESTOJO DE GAZUA PROFISSIONAL",
            "var": "kit_gazua",
            "icone_id": "kit_gazua",
            "lojas": ["valeria", "enfermaria"],
            "preco_enf": 95,
            "preco_val": 75,
            "tier": 1,
            "estoque_dia": 2,
            "usavel": False,
            "penhoravel": True,
            "efeito": "Arromba portas trancadas e armários silenciosamente",
            "desc": "Jogo de tensionadores e palhetas de aço flexível alemão para destrancar fechaduras sem alarmes.",
            "fala_val": "Chave mestra de quem não pede licença pro Grêmio Estudantil. Abre qualquer gaveta.",
            "fala_enf": "Instrumentos cirúrgicos e pinças sobressalentes. Podem servir para trincos emperrados."
        },
        "sucata_eletronica": {
            "nome": "Sucata Eletrônica",
            "titulo_detalhe": "KIT DE SUCATA ELETRÔNICA",
            "var": "sucata_eletronica",
            "icone_id": "sucata_eletronica",
            "lojas": ["valeria", "enfermaria"],
            "preco_enf": 70,
            "preco_val": 55,
            "tier": 1,
            "estoque_dia": 3,
            "usavel": False,
            "penhoravel": True,
            "efeito": "Material essencial para Crafting e Upgrades do Covil",
            "desc": "Capacitores, bobinas de cobre e relés. Moeda de troca indispensável para a bancada e quitação de fiado.",
            "fala_val": "Lixo pra diretoria, ouro puro na nossa bancada de montagem. Traga isso quando faltar moeda.",
            "fala_enf": "Peças sobressalentes dos aparelhos antigos da ala de esterilização hospitalar."
        },
        "soro_purificador": {
            "nome": "Elixir Azul",
            "titulo_detalhe": "REAGENTE PURIFICADOR RÚNICO",
            "var": "soro_purificador",
            "icone_id": "soro_purificador",
            "lojas": ["enfermaria", "valeria"],
            "preco_enf": 135,
            "preco_val": 120,
            "tier": 1,
            "estoque_dia": 2,
            "usavel": True,
            "penhoravel": True,
            "efeito": "Purifica 1 Bolsa Adulterada OU neutraliza toxinas",
            "desc": "Solução azulada estabilizada com sais de prata coloidal que esteriliza sangue podre em puro.",
            "fala_val": "Uma gota desse ácido neutraliza toxinas pesadas em sangue podre. Vale cada centavo.",
            "fala_enf": "Solução salina bacteriostática enriquecida com prata. Mata contaminantes em segundos."
        },

        # --- FOLHA 2: EQUIPAMENTOS TÁTICOS & INFILTRAÇÃO ---
        "giz_protecao": {
            "nome": "Giz Rúnico",
            "titulo_detalhe": "GIZ DE PROTEÇÃO RÚNICO",
            "var": "giz_protecao",
            "icone_id": "giz_protecao",
            "lojas": ["valeria"],
            "preco_enf": 90,
            "preco_val": 65,
            "tier": 1,
            "estoque_dia": 3,
            "usavel": True,
            "penhoravel": True,
            "efeito": "Uso Direto: -15% Exposição | Ingrediente de Crafting",
            "desc": "Usado para traçar barreiras e selos contra escutas e forças do Eclipse nas Zonas Vermelhas.",
            "fala_val": "Risca o chão com isso nas soleiras e nem os cães de faro da Elara te rastreiam.",
            "fala_enf": "Giz mineral com propriedades cáusticas. Alguns alunos insistem que afasta entidades."
        },
        "dispositivo_choque": {
            "nome": "Dispositivo Choque",
            "titulo_detalhe": "DISPOSITIVO DE CHOQUE RÚNICO",
            "var": "dispositivo_choque",
            "icone_id": "dispositivo_choque",
            "lojas": ["valeria"],
            "preco_enf": 210,
            "preco_val": 165,
            "tier": 2,
            "estoque_dia": 1,
            "usavel": False,
            "penhoravel": True,
            "efeito": "Combate: 30 Dano (50 vs Inorgânico) + Atordoa por 1 turno",
            "desc": "Capacitor artesanal de alta voltagem gravado com runas. Paralisa autômatos e sentinelas de ferro.",
            "fala_val": "Derruba até sentinela de armadura se acertar nos conectores. Causa sobrecarga imediata.",
            "fala_enf": "Desfibrilador de emergência alterado para sobrecarga... Não deixe a segurança ver isso."
        },
        "neutralizador_odor": {
            "nome": "Neutralizador Odor",
            "titulo_detalhe": "BLOQUEADOR OLFATIVO ALQUÍMICO",
            "var": "neutralizador_odor",
            "icone_id": "neutralizador_odor",
            "lojas": ["enfermaria", "valeria"],
            "preco_enf": 115,
            "preco_val": 95,
            "tier": 1,
            "estoque_dia": 2,
            "usavel": True,
            "penhoravel": True,
            "efeito": "Anula o Faro Cruzado das Heroínas por 2 períodos",
            "desc": "Atomizador neutro de essência de mirra e cânfora que elimina o odor metálico de sangue e rastro de caça.",
            "fala_val": "Vai encontrar a Presidente Elara depois de caçar? Borrife isso antes ou ela fareja seu uniforme.",
            "fala_enf": "Neutralizador hospitalar sem fragrância. Excelente para encobrir qualquer cheiro hematológico."
        },
        "adrenalina_militar": {
            "nome": "Adrenalina Tática",
            "titulo_detalhe": "INJETOR DE ADRENALINA TÁTICA",
            "var": "adrenalina_militar",
            "icone_id": "adrenalina_militar",
            "lojas": ["enfermaria", "valeria"],
            "preco_enf": 175,
            "preco_val": 160,
            "tier": 2,
            "estoque_dia": 1,
            "usavel": True,
            "penhoravel": True,
            "efeito": "+25 HP | Reflexos Aguçados (+4.0s no QTE de combate)",
            "desc": "Caneta autoinjetora de epinefrina pura militar para choque traumático e desaceleração do tempo de reação.",
            "fala_val": "Ampola militar lacrada com chumbo. O coração dispara tanto que o mundo parece andar em câmera lenta.",
            "fala_enf": "Uso estritamente de choque cardiorrespiratório. Não abuse disto nos corredores."
        },
        "cartao_clonado": {
            "nome": "Cartão Clonado",
            "titulo_detalhe": "CARTÃO MAGNÉTICO CLONADO",
            "var": "cartao_clonado",
            "icone_id": "cartao_clonado",
            "lojas": ["valeria"],
            "preco_enf": 250,
            "preco_val": 190,
            "tier": 2,
            "estoque_dia": 1,
            "usavel": False,
            "penhoravel": False,
            "efeito": "Libera catracas e portas restritas do segundo andar",
            "desc": "Cópia pirata da credencial magnética dos monitores seniores do Conselho.",
            "fala_val": "Clonado direto do bolso de um monitor bêbado no Fundão. Abre as portas do segundo andar.",
            "fala_enf": "Credencial institucional extraviada... Se a Inquisição vir isso, a investigação recai sobre nós."
        },
        "sedativo_clinico": {
            "nome": "Sedativo Clínico",
            "titulo_detalhe": "FRASCO DE SEDATIVO CLÍNICO",
            "var": "sedativo_clinico",
            "icone_id": "sedativo_clinico",
            "lojas": ["enfermaria", "valeria"],
            "preco_enf": 125,
            "preco_val": 120,
            "tier": 1,
            "estoque_dia": 2,
            "usavel": True,
            "penhoravel": True,
            "efeito": "+10% de largura na Zona de Sombra do próximo Bote",
            "desc": "Gotas sedativas de clorpromazina concentrada que retardam os reflexos de alvos nos corredores.",
            "fala_val": "Duas gotas no lenço e a presa nem percebe você chegando por trás nos corredores.",
            "fala_enf": "Anestésico pré-operatório rigorosamente controlado. Algumas gotas já induzem sonolência profunda."
        },
        "granada_fumaca": {
            "nome": "Granada Fumaça",
            "titulo_detalhe": "GRANADA DE FUMAÇA ALQUÍMICA",
            "var": "granada_fumaca",
            "icone_id": "granada_fumaca",
            "lojas": ["valeria"],
            "preco_enf": 180,
            "preco_val": 140,
            "tier": 1,
            "estoque_dia": 2,
            "usavel": True,
            "penhoravel": True,
            "efeito": "Combate: Fuga Imediata Segura (0 HP) | Remove Alerta de Área",
            "desc": "Cápsula de fósforo e enxofre. Cria uma cortina espessa que cega adversários e apaga rastros.",
            "fala_val": "Puxe o pino e jogue no chão. Uma cortina cinza cobre sua rota e apaga qualquer rastro visual.",
            "fala_enf": "Isso viola todas as normas sanitárias e de combate a incêndio do campus!"
        },
        "espelho_obsidian": {
            "nome": "Espelho Obsidiana",
            "titulo_detalhe": "ESPELHO DE OBSIDIANA RÚNICA",
            "var": "espelho_obsidian",
            "icone_id": "espelho_obsidian",
            "lojas": ["valeria"],
            "preco_enf": 260,
            "preco_val": 210,
            "tier": 2,
            "estoque_dia": 1,
            "usavel": True,
            "penhoravel": True,
            "efeito": "-2% DOOM | Revela a posição das 4 heroínas no mapa hoje",
            "desc": "Vidro vulcânico antigo polido com runas de vidência que dissipa perturbações e projeta as presenças do campus.",
            "fala_val": "Superfície negra como breu. Dizem que reflete os passos e intenções de quem vagueia pela escola.",
            "fala_enf": "Uma peça de colecionador sinistra... Sinto calafrios só de olhar para a moldura."
        },
        "estaca_prata": {
            "nome": "Estaca de Prata",
            "titulo_detalhe": "ESTACA DE PRATA CONSAGRADA",
            "var": "estaca_prata",
            "icone_id": "estaca_prata",
            "lojas": ["valeria"],
            "preco_enf": 290,
            "preco_val": 230,
            "tier": 2,
            "estoque_dia": 1,
            "usavel": False,
            "penhoravel": True,
            "efeito": "Combate: 60 Dano Verdadeiro (custa 8 HP ao empunhar)",
            "desc": "Arma ritual consagrada em prata pura para estilhaçar a carcaça de aberrações e gárgulas ancestrais.",
            "fala_val": "Prata batida no fogo frio. Se cravar no peito de uma abominação, ela não se levanta nunca mais.",
            "fala_enf": "Um instrumento pontiagudo perigosíssimo. Mantenha isso longe de qualquer pessoa desavisada."
        },

        # --- FOLHA 3: RELÍQUIAS & PISTAS NARRATIVAS ---
        "partitura_runica": {
            "nome": "Partitura Rúnica",
            "titulo_detalhe": "PARTITURA RÚNICA PRÉ-DILUVIANA",
            "var": "tem_partitura_runica",
            "icone_id": "partitura_runica",
            "lojas": [],
            "preco_enf": 0,
            "preco_val": 0,
            "tier": 3,
            "estoque_dia": 0,
            "usavel": False,
            "penhoravel": False,
            "efeito": "Relíquia da Mestra Lility",
            "desc": "Pauta musical grafada com acordes ancestrais recuperada no Bar da Fada Verde.",
            "fala_val": "Música antiga... Tem gosto de sangue nobre e eras esquecidas.",
            "fala_enf": "Não parece uma partitura convencional."
        },
        "relicario_sangue": {
            "nome": "Relicário Puro",
            "titulo_detalhe": "RELICÁRIO DE SANGUE PURO",
            "var": "tem_relicario_sangue",
            "icone_id": "relicario_sangue",
            "lojas": [],
            "preco_enf": 0,
            "preco_val": 0,
            "tier": 3,
            "estoque_dia": 0,
            "usavel": False,
            "penhoravel": False,
            "efeito": "Chave do Selo Primordial no Clímax",
            "desc": "Urna ancestral guardada sob as abóbadas do Cofre do Grêmio Estudantil.",
            "fala_val": "O selo dessa urna pulsa com calor e ressonância próprios.",
            "fala_enf": "Um frasco hermético de época medieval."
        },
        "chave_contencao": {
            "nome": "Chave Contenção",
            "titulo_detalhe": "CHAVE DE CONTENÇÃO SUBTERRÂNEA",
            "var": "tem_chave_contencao",
            "icone_id": "chave_contencao",
            "lojas": [],
            "preco_enf": 0,
            "preco_val": 0,
            "tier": 3,
            "estoque_dia": 0,
            "usavel": False,
            "penhoravel": False,
            "efeito": "Acesso às Câmaras Subterrâneas Profundas",
            "desc": "Chave de bronze forjada pelo Grêmio para trancar a cripta mais profunda.",
            "fala_val": "A chave das gaiolas de baixo onde ninguém quer ser esquecido.",
            "fala_enf": "Chave mestra das alas de quarentena severa."
        },
        "grimorio_corte": {
            "nome": "Grimório do Corte",
            "titulo_detalhe": "PÁGINAS DO CORTE DO VÍNCULO",
            "var": "ritual_corte_vinculo_desbloqueado",
            "icone_id": "grimorio_corte",
            "lojas": [],
            "preco_enf": 0,
            "preco_val": 0,
            "tier": 3,
            "estoque_dia": 0,
            "usavel": False,
            "penhoravel": False,
            "efeito": "Habilita o Ritual de Rompimento de Vínculo",
            "desc": "Folhas arrancadas do códice inquisitorial de Lorde Phillip von Karsten.",
            "fala_val": "Páginas proibidas pelo tribunal e pela Inquisição. Queime depois de ler.",
            "fala_enf": "Documentos lacrados da capela e do conselho."
        },
        "fita_k7_amaldicoada": {
            "nome": "Fita K7 Misteriosa",
            "titulo_detalhe": "FITA K7 COM SUSSURROS SUBTERRÂNEOS",
            "var": "fita_k7_amaldicoada",
            "icone_id": "fita_k7_amaldicoada",
            "lojas": [],
            "preco_enf": 0,
            "preco_val": 0,
            "tier": 3,
            "estoque_dia": 0,
            "usavel": True,
            "penhoravel": False,
            "efeito": "Uso Direto: -6% DOOM ao decodificar as frequências",
            "desc": "Gravação magnética captada nas tubulações profundas em 1986 contendo frequências do subsolo.",
            "fala_val": "Uma fita com ruídos que congelam a espinha. Quem gravou isso perdeu o juízo.",
            "fala_enf": "Gravação dos experimentos psiquiátricos da ala abandonada."
        },
        "prontuario_nora": {
            "nome": "Prontuário Nora",
            "titulo_detalhe": "PRONTUÁRIO MÉDICO DE NORA VANCE",
            "var": "prontuario_nora",
            "icone_id": "prontuario_nora",
            "lojas": [],
            "preco_enf": 0,
            "preco_val": 0,
            "tier": 3,
            "estoque_dia": 0,
            "usavel": False,
            "penhoravel": False,
            "efeito": "Dossiê Confidencial sobre Nora e Rh-Nulo",
            "desc": "Documentos lacrados da Dra. Clara Vance revelando o projeto de transfusão e linhagem Rh-Nulo.",
            "fala_val": "Papéis que a Dra. Vance mataria para não ver espalhados nos corredores.",
            "fala_enf": "Onde... onde você conseguiu este arquivo confidencial?!"
        },
        "pigmento_alma": {
            "nome": "Pigmento Alma",
            "titulo_detalhe": "PIGMENTO DE ALMA (SAFRA 1889)",
            "var": "pigmento_alma",
            "icone_id": "pigmento_alma",
            "lojas": [],
            "preco_enf": 0,
            "preco_val": 0,
            "tier": 3,
            "estoque_dia": 0,
            "usavel": True,
            "penhoravel": False,
            "efeito": "Uso Direto: Converte-se em 2x Giz de Proteção Rúnico",
            "desc": "Pó mineral luminescente colhido em resíduos de rituais alquímicos do século XIX.",
            "fala_val": "Pó luminescente muito raro. Ideal para rituais de ocultação.",
            "fala_enf": "Composto fluorescente instável, manuseie com cuidado estéril."
        }
    }

    def sincronizar_estoque_diario_lojas():
        """Inicializa ou renova os estoques diários das lojas ao amanhecer."""
        dia_chave = getattr(store, "dia_atual", 1)
        if store.estoque_lojas_hoje.get("_dia") == dia_chave:
            return
        novo = {"_dia": dia_chave}
        for id_it, dados in ITENS_LOJA_EXPANDIDOS.items():
            for loja in dados["lojas"]:
                novo[f"{loja}_{id_it}"] = dados["estoque_dia"]
        store.estoque_lojas_hoje = novo

    def obter_preco_loja(id_item, tipo_loja="valeria"):
        """Calcula o preço de compra respeitando o ágio clínico ou multiplicador de Valéria."""
        dados = ITENS_LOJA_EXPANDIDOS.get(id_item)
        if not dados:
            return 0
        if tipo_loja == "enfermaria":
            base = dados["preco_enf"]
            if getattr(store, "paciente_inadimplente_taxa", lambda: False)():
                base = int(round(base * 1.25))
        else:
            base = dados["preco_val"]
            if "calcular_preco_valeria" in globals() and id_item in ["bolsa_sangue", "kit_curativo"]:
                var_canon = "bolsa_sangue_filtrado" if id_item == "bolsa_sangue" else "kit_curativo"
                base = calcular_preco_valeria(var_canon)
            else:
                mult = obter_multiplicador_valeria() if "obter_multiplicador_valeria" in globals() else 1.0
                base = max(10, int(round(base * mult)))
        return max(10, base)

    def loja_item_desbloqueado(id_item, tipo_loja):
        dados = ITENS_LOJA_EXPANDIDOS.get(id_item)
        if not dados or dados["tier"] <= 1:
            return True
        if tipo_loja == "enfermaria":
            return getattr(store, "humanidade", 50) >= 50 or getattr(store, "coleta_enfermeira_hoje", False)
        return getattr(store, "status_valeria", None) is not None and (
            getattr(store.status_valeria, "afeto", 0) >= 2 or getattr(store, "encomenda_caldeiras_concluida_hoje", False)
        )

    def obter_lista_itens_loja(tipo_loja="valeria", modo="comprar"):
        itens = []
        if modo == "comprar":
            for it_id, dados in ITENS_LOJA_EXPANDIDOS.items():
                if tipo_loja in dados["lojas"]:
                    itens.append(it_id)
        else:
            for it_id, dados in ITENS_LOJA_EXPANDIDOS.items():
                if dados.get("penhoravel", False):
                    qtd = getattr(store, dados["var"], 0)
                    if qtd > 0:
                        itens.append(it_id)
        return itens

    def executar_transacao_loja(id_item, tipo_loja):
        sincronizar_estoque_diario_lojas()
        dados = ITENS_LOJA_EXPANDIDOS.get(id_item)
        if not dados:
            return

        var_nome = dados["var"]
        qtd_atual = getattr(store, var_nome, 0)
        preco = obter_preco_loja(id_item, tipo_loja)
        din = getattr(store, "dinheiro_jogador", 0)

        if store.loja_aba_modo == "comprar":
            chave_est = f"{tipo_loja}_{id_item}"
            est = store.estoque_lojas_hoje.get(chave_est, 0)
            if not loja_item_desbloqueado(id_item, tipo_loja):
                renpy.notify("🔒 Reputação insuficiente para este lote!")
                return
            if est <= 0:
                store.loja_fala_vendedora = (
                    "Estoque esgotado por hoje, Vane. Volte no próximo amanhecer."
                    if tipo_loja == "valeria" else
                    "Limite de dispensação diária atingido para este item, Sr. Vane."
                )
                renpy.notify("⚠️ Estoque diário esgotado nesta loja!")
                return
            if din < preco:
                if tipo_loja == "valeria":
                    if hasattr(store, "th_bark"):
                        store.th_bark("valeria", "sem_dinheiro")
                    if id_item == "bolsa_sangue":
                        store.loja_fala_vendedora = "Está sem grana, Vane. Mas se a garganta estiver ardendo, posso fazer no fiado."
                    else:
                        store.loja_fala_vendedora = f"Você precisa de ${preco} créditos no bolso para levar isto, Vane."
                else:
                    store.loja_fala_vendedora = f"Sem créditos suficientes (${preco}) no prontuário, a Fundação não autoriza a dispensação."
                renpy.notify("❌ Dinheiro insuficiente na carteira!")
                return

            store.dinheiro_jogador = din - preco
            setattr(store, var_nome, qtd_atual + 1)
            store.estoque_lojas_hoje[chave_est] = est - 1
            if tipo_loja == "valeria":
                if hasattr(store, "th_bark"):
                    store.th_bark("valeria", "negocios")
                store.loja_fala_vendedora = "Negócio fechado. Mais alguma coisa para sobreviver à noite, Vane?"
            else:
                store.loja_fala_vendedora = "Dispensação registrada no sistema clínico. Faça bom uso, Sr. Vane."

            # Sincroniza estoques legados da Enfermaria se aplicável
            if tipo_loja == "enfermaria":
                if id_item == "bolsa_sangue":
                    store.enfermaria_bolsas_hoje = getattr(store, "enfermaria_bolsas_hoje", 0) + 1
                elif id_item == "kit_curativo":
                    store.enfermaria_kits_hoje = getattr(store, "enfermaria_kits_hoje", 0) + 1

            if hasattr(store, "th_sfx"):
                store.th_sfx("moedas_ouro")
            renpy.notify(f"🛍️ Adquirido: +1 {dados['nome']} (-${preco})")

        else:
            # Modo Penhorar / Vender
            if qtd_atual <= 0:
                renpy.notify("Você não possui unidades deste item para penhorar.")
                return
            valor_venda = max(10, preco // 2)
            setattr(store, var_nome, qtd_atual - 1)
            store.dinheiro_jogador = din + valor_venda
            store.loja_fala_vendedora = (
                f"Sucata ou relíquia, tudo tem valor nas Caldeiras. +${valor_venda} na sua mão, Vane."
                if tipo_loja == "valeria" else
                f"Material recebido para a reserva da enfermaria. +${valor_venda} creditados."
            )
            if hasattr(store, "th_sfx"):
                store.th_sfx("moedas_ouro")
            renpy.notify(f"💰 Penhorado: -1 {dados['nome']} (+${valor_venda})")

            # Se a quantidade zerou, move para o próximo item penhorável
            if getattr(store, var_nome, 0) <= 0:
                itens_restantes = obter_lista_itens_loja(tipo_loja, "vender")
                store.loja_item_selecionado = itens_restantes[0] if itens_restantes else None
                if store.loja_item_selecionado and store.loja_item_selecionado in ITENS_LOJA_EXPANDIDOS:
                    d_prox = ITENS_LOJA_EXPANDIDOS[store.loja_item_selecionado]
                    store.loja_fala_vendedora = d_prox["fala_enf"] if tipo_loja == "enfermaria" else d_prox["fala_val"]

    def inicializar_abertura_loja(tipo_loja="valeria"):
        """Garante inicialização limpa ao abrir o dispensário ou mercado negro."""
        sincronizar_estoque_diario_lojas()
        store.loja_aba_modo = "comprar"
        store.loja_pagina_atual = 0
        itens = obter_lista_itens_loja(tipo_loja, "comprar")
        store.loja_item_selecionado = itens[0] if itens else "bolsa_sangue"
        store.loja_fala_vendedora = (
            "Não temos muito estoque esta noite, Victor... Escolha rápido e não desperdice meus recursos."
            if tipo_loja == "enfermaria" else
            "O que vai ser hoje, bolsista? Sangue novo ou algo para sobreviver à noite?"
        )

    def alternar_modo_loja(modo, tipo_loja="valeria"):
        """Alterna instantaneamente entre Comprar e Penhorar com seleção sincronizada."""
        store.loja_aba_modo = modo
        store.loja_pagina_atual = 0
        itens = obter_lista_itens_loja(tipo_loja, modo)
        store.loja_item_selecionado = itens[0] if itens else None
        if store.loja_item_selecionado and store.loja_item_selecionado in ITENS_LOJA_EXPANDIDOS:
            dados = ITENS_LOJA_EXPANDIDOS[store.loja_item_selecionado]
            store.loja_fala_vendedora = dados["fala_enf"] if tipo_loja == "enfermaria" else dados["fala_val"]
        renpy.restart_interaction()

    def selecionar_item_loja(cid, tipo_loja="valeria"):
        """Atualiza o item selecionado e o diálogo temático sem falhas de escopo."""
        store.loja_item_selecionado = cid
        dados = ITENS_LOJA_EXPANDIDOS.get(cid)
        if dados:
            store.loja_fala_vendedora = dados["fala_enf"] if tipo_loja == "enfermaria" else dados["fala_val"]
        renpy.restart_interaction()

# ==============================================================================
# TELA DA VITRINE GÓTICA 9-SLICE (60/40)
# ==============================================================================
screen vitrine_loja_tatica(tipo_loja="valeria"):
    modal True
    zorder 92

    # Atalho de teclado para fechar a tela sem risco de softlock
    key "K_ESCAPE" action Return("sair_loja")

    $ eh_enf = (tipo_loja == "enfermaria")
    $ cor_destaque = "#5ce1e6" if eh_enf else "#4ade80"
    $ cor_nome_npc = "#38bdf8" if eh_enf else "#facc15"
    $ nome_npc = "Enfermeira Clara" if eh_enf else "Valéria"

    # Lista e Paginação Segura contra Deslocamento de Índices
    $ _todos_itens = obter_lista_itens_loja(tipo_loja, store.loja_aba_modo)
    $ _max_pags = max(0, (len(_todos_itens) - 1) // 8) if _todos_itens else 0
    if store.loja_pagina_atual > _max_pags:
        $ store.loja_pagina_atual = _max_pags
    $ _inicio = store.loja_pagina_atual * 8
    $ lista_ids = _todos_itens[_inicio:_inicio+8]

    # Sincronização Segura do Item Selecionado (sempre no store)
    if (store.loja_item_selecionado not in _todos_itens):
        $ store.loja_item_selecionado = _todos_itens[0] if _todos_itens else None

    # Fundo escurecido semi-transparente que preserva o cenário e o sprite animado
    add Solid("#040608b0")

    # ==========================================================================
    # LADO DIREITO (40% DA TELA): CAIXA DE FALA 9-SLICE (SPRITE DA CENA VISÍVEL)
    # ==========================================================================
    # O sprite da personagem já está na cena com o transform 'sprite_direita'
    # respirando e animado; nenhuma imagem estática é desenhada por cima.

    # Caixa de fala da vendedora no canto inferior direito abaixo do sprite
    frame:
        xpos 960
        ypos 810
        xysize (910, 195)
        background frame_hud_loja("caixa_fala_loja.png", 32, 28, "#0b0d14eb")
        padding (30, 20)

        vbox:
            spacing 6
            text "[nome_npc]:" size 26 bold True color cor_nome_npc outlines [(2, "#000000ee", 0, 0)]
            text "\"[store.loja_fala_vendedora]\"" size 23 color "#ffffff" italic True line_spacing 4 outlines [(1, "#000000dd", 0, 0)]

    # ==========================================================================
    # LADO ESQUERDO: INTERFACE TÁTICA 9-SLICE COMPACTADA E HARMONIOSA
    # ==========================================================================
    # Abas superiores projetadas acima da moldura principal + Saldo e Fechar Seguro
    $ bg_aba_comprar = frame_hud_loja("aba_ativa_azul.png" if eh_enf else "aba_ativa_carmesim.png", 18, 14, "#1e293b", tint_hex=("#88ddff" if eh_enf else "#44dd99")) if store.loja_aba_modo == "comprar" else frame_hud_loja("aba_inativa_azul.png" if eh_enf else "aba_inativa_carmesim.png", 18, 14, "#12151f")
    $ bg_aba_penhorar = frame_hud_loja("aba_ativa_azul.png" if eh_enf else "aba_ativa_carmesim.png", 18, 14, "#2d1a1a", tint_hex=("#88ddff" if eh_enf else "#44dd99")) if store.loja_aba_modo == "vender" else frame_hud_loja("aba_inativa_azul.png" if eh_enf else "aba_inativa_carmesim.png", 18, 14, "#12151f")

    hbox:
        xpos 50
        ypos 80
        spacing 12

        button:
            xysize (230, 56)
            background bg_aba_comprar
            action [SetVariable("loja_aba_modo", "comprar"), Function(alternar_modo_loja, "comprar", tipo_loja)]
            text "COMPRAR":
                align (0.5, 0.5) size 21 bold True
                color ("#ffffff" if store.loja_aba_modo == "comprar" else "#7a8291")
                outlines [(2, "#000000cc", 0, 0)]

        button:
            xysize (230, 56)
            background bg_aba_penhorar
            action [SetVariable("loja_aba_modo", "vender"), Function(alternar_modo_loja, "vender", tipo_loja)]
            text "PENHORAR":
                align (0.5, 0.5) size 21 bold True
                color ("#ffffff" if store.loja_aba_modo == "vender" else "#7a8291")
                outlines [(2, "#000000cc", 0, 0)]

        # Indicador de Saldo em Moedas do Jogador
        frame:
            xysize (220, 52)
            background "#090d14dd"
            padding (10, 6)
            yalign 0.5
            hbox:
                align (0.5, 0.5)
                spacing 8
                text "💰 Saldo:" size 16 bold True color "#ffd700"
                text "$[dinheiro_jogador]" size 18 bold True color "#00ffcc"

        # Botão Fechar Sempre Visível (Garante Zero Softlocks)
        button:
            xysize (150, 52)
            background frame_hud_loja("btn_secundario.png", 24, 16, "#3a1216")
            hover_background frame_hud_loja("btn_secundario.png", 24, 16, "#661822")
            yalign 0.5
            action Return("sair_loja")
            text "✖ FECHAR":
                align (0.5, 0.5) size 16 bold True color "#ff9999"

    # MOLDURA PRINCIPAL DA VITRINE À ESQUERDA (9-SLICE COMPACTA: 870x835)
    frame:
        xpos 50
        ypos 144
        xysize (870, 835)
        background frame_hud_loja("painel_vitrine.png", 32, 32, "#0c0e14f4")
        padding (24, 20)

        vbox:
            spacing 10

            # GRADE 4x2 DE SLOTS QUADRADOS COMPACTOS (194x210)
            if not lista_ids and store.loja_aba_modo == "vender":
                frame:
                    xfill True
                    ysize 440
                    background "#0a0c12"
                    text "Você não possui itens penhoráveis na sua mochila no momento." size 18 color "#94a3b8" align (0.5, 0.5)
            else:
                grid 4 2:
                    spacing 10
                    xalign 0.5

                    for idx in range(8):
                        if idx < len(lista_ids):
                            $ cid = lista_ids[idx]
                            $ cdata = ITENS_LOJA_EXPANDIDOS[cid]
                            $ selecionado = (cid == store.loja_item_selecionado)
                            $ liberado = loja_item_desbloqueado(cid, tipo_loja)
                            $ est_loja = estoque_lojas_hoje.get(f"{tipo_loja}_{cid}", 0)
                            $ preco_exibir = obter_preco_loja(cid, tipo_loja) if store.loja_aba_modo == "comprar" else max(10, obter_preco_loja(cid, tipo_loja) // 2)

                            # Célula inteira como botão interativo selecionável com hover
                            button:
                                xysize (194, 210)
                                xalign 0.5
                                padding (8, 6)
                                selected selecionado
                                background frame_hud_loja(
                                    ("slot_selecionado_azul.png" if eh_enf else "slot_selecionado_verde.png") if selecionado else "slot_normal.png",
                                    20 if selecionado else 16,
                                    20 if selecionado else 16,
                                    "#1e293b" if selecionado else "#131620"
                                )
                                hover_background frame_hud_loja(
                                    ("slot_selecionado_azul.png" if eh_enf else "slot_selecionado_verde.png"),
                                    20, 20, "#1a362e"
                                )
                                action [SetVariable("loja_item_selecionado", cid), Function(selecionar_item_loja, cid, tipo_loja)]

                                vbox:
                                    align (0.5, 0.5)
                                    spacing 2

                                    add obter_icone_item_loja(cdata["icone_id"], 108) align (0.5, 0.0)

                                    text "[cdata['nome']]":
                                        xalign 0.5 text_align 0.5 size 15 bold True
                                        color (cor_destaque if selecionado else ("#e2e8f0" if liberado else "#64748b"))
                                        outlines [(1, "#000000", 0, 0)]
                                        xsize 178

                                    if not liberado and store.loja_aba_modo == "comprar":
                                        text "(🔒 Restrito)" xalign 0.5 size 14 color "#f87171"
                                    elif store.loja_aba_modo == "comprar":
                                        text "($[preco_exibir])" xalign 0.5 size 15 bold True:
                                            color (cor_destaque if selecionado else ("#cbd5e1" if est_loja > 0 else "#ef4444"))
                                    else:
                                        text "(+$[preco_exibir])" xalign 0.5 size 15 bold True color "#fbbf24"
                        else:
                            frame:
                                xysize (194, 210)
                                xalign 0.5
                                background "#0a0d1444"
                                text "—" size 24 color "#272f3d" align (0.5, 0.5)

            # BARRA DE PAGINAÇÃO SE HOUVER MAIS DE 8 ITENS
            if len(_todos_itens) > 8:
                hbox:
                    align (0.5, 0.5)
                    spacing 20
                    if store.loja_pagina_atual > 0:
                        button:
                            action SetVariable("loja_pagina_atual", store.loja_pagina_atual - 1)
                            text "◀ Anterior" size 15 color cor_destaque bold True
                    else:
                        text "◀ Anterior" size 15 color "#555566"

                    text "Página [store.loja_pagina_atual + 1] de [_max_pags + 1]" size 15 color "#cccccc"

                    if store.loja_pagina_atual < _max_pags:
                        button:
                            action SetVariable("loja_pagina_atual", store.loja_pagina_atual + 1)
                            text "Próxima ▶" size 15 color cor_destaque bold True
                    else:
                        text "Próxima ▶" size 15 color "#555566"
            else:
                null height 2

            # SUBPAINEL INFERIOR DE DETALHES DO ITEM SELECIONADO (9-SLICE COMPACTO: 230px)
            frame:
                xfill True
                ysize 230
                background frame_hud_loja("painel_detalhes.png", 24, 24, "#121622f5")
                padding (18, 14)

                if store.loja_item_selecionado and store.loja_item_selecionado in ITENS_LOJA_EXPANDIDOS:
                    $ item_sel = ITENS_LOJA_EXPANDIDOS[store.loja_item_selecionado]
                    $ preco_acao = obter_preco_loja(store.loja_item_selecionado, tipo_loja) if store.loja_aba_modo == "comprar" else max(10, obter_preco_loja(store.loja_item_selecionado, tipo_loja) // 2)
                    $ qtd_mochila = getattr(store, item_sel["var"], 0)
                    $ est_item_sel = estoque_lojas_hoje.get(f"{tipo_loja}_{store.loja_item_selecionado}", 0)
                    $ liberado_sel = loja_item_desbloqueado(store.loja_item_selecionado, tipo_loja)

                    hbox:
                        spacing 16

                        # Encaixe esquerdo com o ícone ampliado
                        frame:
                            xysize (150, 150)
                            yalign 0.5
                            padding (8, 8)
                            background frame_hud_loja("slot_normal.png", 16, 16, "#181c28")
                            add obter_icone_item_loja(item_sel["icone_id"], 130) align (0.5, 0.5)

                        # Coluna direita: Título, Descrição, Mochila e Botão Chanfrado
                        vbox:
                            spacing 6
                            xsize 640
                            yalign 0.5

                            hbox:
                                spacing 12
                                yalign 0.5
                                text "[item_sel['titulo_detalhe']]" size 19 bold True color "#ffffff" outlines [(1, "#000000dd", 0, 0)]
                                text "• Mochila: x[qtd_mochila]" size 16 color "#94a3b8" yalign 0.5

                            text "[item_sel['desc']]" size 15 color "#cbd5e1" line_spacing 2 xsize 635

                            null height 2
                            hbox:
                                xfill True
                                # Atalhos secundários discretos à esquerda
                                hbox:
                                    spacing 6
                                    yalign 0.5

                                    if not eh_enf:
                                        textbutton "🏗️ Covil":
                                            padding (10, 6)
                                            background frame_hud_loja("btn_secundario.png", 20, 14, "#1e293b")
                                            text_size 13 text_color "#5eead4" text_bold True
                                            action Show("painel_gestao_caldeiras")

                                    textbutton "🚪 Sair":
                                        padding (12, 6)
                                        background frame_hud_loja("btn_secundario.png", 20, 14, "#2a161c")
                                        text_size 13 text_color "#fda4af" text_bold True
                                        action Return("sair_loja")

                                # Se for Valéria e o jogador estiver sem grana na bolsa de sangue, atalho do Fiado
                                if not eh_enf and store.loja_item_selecionado == "bolsa_sangue" and store.loja_aba_modo == "comprar" and dinheiro_jogador < preco_acao:
                                    if "divida_valeria_sangue_fiado" not in getattr(store, "registro_dividas_ativas", {}) or getattr(store, "registro_dividas_ativas", {})["divida_valeria_sangue_fiado"].quitada:
                                        textbutton "🩸 Fiado":
                                            padding (10, 6)
                                            background frame_hud_loja("btn_secundario.png", 20, 14, "#4d2b1b")
                                            text_size 13 text_color "#ffaa88" text_bold True
                                            action Return("pedir_fiado")

                                # Botão Chanfrado Principal à direita com feedback inteligente
                                $ pode_comprar = (store.loja_aba_modo == "comprar" and est_item_sel > 0 and liberado_sel)
                                $ pode_penhorar = (store.loja_aba_modo == "vender" and qtd_mochila > 0)
                                $ cor_btn_tint = None if (pode_comprar or pode_penhorar) else "#555555"

                                button:
                                    xalign 1.0
                                    xysize (255, 54)
                                    background frame_hud_loja(
                                        "btn_comprar_azul.png" if eh_enf else "btn_comprar_verde.png",
                                        20, 14, "#14532d",
                                        tint_hex=cor_btn_tint
                                    )
                                    hover_background frame_hud_loja(
                                        "btn_comprar_azul.png" if eh_enf else "btn_comprar_verde.png",
                                        20, 14, "#166534",
                                        tint_hex=cor_btn_tint
                                    )
                                    action Function(executar_transacao_loja, store.loja_item_selecionado, tipo_loja)

                                    if store.loja_aba_modo == "comprar":
                                        if not liberado_sel:
                                            text "BLOQUEADO (RESTRITO)" align (0.5, 0.5) size 14 bold True color "#ff9999" outlines [(2, "#000000dd", 0, 0)]
                                        elif est_item_sel <= 0:
                                            text "ESGOTADO HOJE" align (0.5, 0.5) size 15 bold True color "#ff8888" outlines [(2, "#000000dd", 0, 0)]
                                        else:
                                            text "COMPRAR • $[preco_acao]" align (0.5, 0.5) size 16 bold True color "#ffffff" outlines [(2, "#000000dd", 0, 0)]
                                    else:
                                        if qtd_mochila <= 0:
                                            text "SEM ITENS" align (0.5, 0.5) size 15 bold True color "#aaaaaa" outlines [(2, "#000000dd", 0, 0)]
                                        else:
                                            text "PENHORAR • +$[preco_acao]" align (0.5, 0.5) size 16 bold True color "#ffffff" outlines [(2, "#000000dd", 0, 0)]
                else:
                    text "Selecione um item da vitrine acima para inspecionar e negociar." size 18 color "#94a3b8" align (0.5, 0.5)
