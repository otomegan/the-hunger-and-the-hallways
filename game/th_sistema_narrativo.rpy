# ==============================================================================

# TH_SISTEMA_NARRATIVO.RPY

# Ferramentas narrativas e mecânicas psicológicas de Victor Vane:

# Regras de Victor, Livro de Dívidas, Boatos, Cartão de Transição e Balanço do Dia.

# ==============================================================================



# --- Personagens narrativos do Ato I -----------------------------------------

define diretor_ambrosio = Character("Diretor Ambrósio", color="#d9c9a3")

define nora = Character("Nora", color="#c9a0a0")

define reflexo = Character("Reflexo", color="#8fb3c9")

define voz_na_escuridao = Character("???", color="#c20000")



# --- As quatro regras escritas no verso da carta de bolsa --------------------

define th_regras_texto = [

    "1. Não dever nada a ninguém.",

    "2. Nunca confiar em quem sorri antes de pedir.",

    "3. Nunca ser o último a saber.",

    "4. Nunca ser descartável.",

]



# --- Estado narrativo e psicológico ------------------------------------------

default livro_de_dividas = []          # o que Victor deve (cobranças pendentes)

default livro_de_creditos = []         # o que devem a Victor

default regras_quebradas = []          # números das regras já quebradas

default livro_de_boatos = []           # rumores colhidos (alimentam lendas urbanas)

default registro_dividas_ativas = {}   # dicionário id -> objeto DividaAtiva



default recusou_ajuda_dia1 = False

default sondou_emilia_dia1 = False

default assinou_doacao_dia1 = ""       # "assinou", "leu" ou "recusou"

default emprestou_caneta_nora = False

default destino_teo = ""               # "assumiu", "denunciou" ou "abandonou"

default divida_monitores = 0

default informante_elara = False

default grilhao_compartilhado = False

default vendeu_ronda_emilia = False

default resposta_valeria_dia2 = ""      # "pagou", "vendeu" ou "recusou"



# --- Funções do Sistema Narrativo --------------------------------------------

init python:



    def th_musica(nome, fade=1.5):
        """Toca música tolerando subpastas (audio/musicas/), extensões (.mp3, .ogg, .wav) e aliases narrativos."""
        # Mapeamento de conveniência narrativa
        alias_map = {
            "tema_quarto": "tema_quarto",
            "quarto": "tema_quarto",
            "elara": "tema_de_elara",
            "tema_elara": "tema_de_elara",
            "emilia": "the_keepers_ledger",
            "tema_emilia": "the_keepers_ledger",
            "valeria": "midnight_in_the_underpass",
            "tema_valeria": "midnight_in_the_underpass",
            "bar": "midnight_in_the_underpass",
            "fundao": "midnight_in_the_underpass",
            "caldeiras": "iron_lungs",
            "tema_caldeiras": "iron_lungs",
            "conselho": "tema_conselho_estudantil",
            "gremio": "tema_conselho_estudantil",
            "principal": "the_crimson_chamber",
            "tema_principal": "the_crimson_chamber",
            "valsa": "tema_da_valsa",
            "batalha": "steel_loop",
            "phillip": "the_cold_decree",
            "tema_phillip": "the_cold_decree",
            "resurreicao_cain": "catactic_requiem",
            "batalha_cain_2": "funeral_in_the_catacombs",
            "cain_segunda_forma": "the_hunger_of_ancient_gods",
            "investigacao": "pulsao_sombra",
            "investigacao_2": "tema_investigativo_2",
            "transe_lility": "obscura",
            "transe_sangue": "sighs_in_the_dark",
            "batalha_loira": "batalha_loira_banheiro",
            "loira_banheiro": "batalha_loira_banheiro",
            "loira": "batalha_loira_banheiro",
            "batalha_hachishaku": "batalha_hachishakusama",
            "hachishaku": "batalha_hachishakusama",
            "hachishakusama": "batalha_hachishakusama",
            "menu": "menu_musica",
            "tema_menu": "menu_musica",
        }
        nome_resolvido = alias_map.get(nome.lower(), nome)

        candidatos = []
        for base in (nome_resolvido, nome):
            clean = base.strip()
            variants = [clean, clean.lower(), clean.capitalize(), clean.replace(" ", "_"), clean.replace("_", "-")]
            for v in variants:
                for ext in (".mp3", ".ogg", ".wav"):
                    candidatos.append(f"audio/musicas/{v}{ext}")
                    candidatos.append(f"audio/{v}{ext}")
                    candidatos.append(f"audio/ambiente/{v}{ext}")
                    candidatos.append(f"audio/sfx/{v}{ext}")

        for cand in candidatos:
            if renpy.loadable(cand):
                renpy.music.play(cand, fadein=fade, if_changed=True)
                return True

        if config.developer:
            renpy.notify(f"Áudio ausente: {nome}")
        return False

    def th_sfx(nome):
        """Toca efeito sonoro da subpasta audio/sfx/ ou raiz audio/ tolerando variações de nome e formato."""
        candidatos = []
        clean = nome.strip()
        aliases = {
            "gaveta": "sfx_vasculhar_gaveta_abrir",
            "vasculhar": "sfx_vasculhar_gaveta_abrir",
            "mexer_objetos": "sfx_vasculhar_objetos_mexer",
            "espada": "sfx_lamina_espada_corte",
            "adaga": "sfx_lamina_corte_rapido",
            "corte_rapido": "sfx_lamina_corte_rapido",
            "chicote": "sfx_chicote_sangue_estalo",
            "chicote_sangue": "sfx_chicote_sangue_estalo",
            "pistola": "sfx_tiro_pistola_seco",
            "tiro": "sfx_tiro_pistola_seco",
            "escopeta": "sfx_tiro_escopeta_reverberacao",
            "tiro_escopeta": "sfx_tiro_escopeta_reverberacao",
            "choque": "sfx_eletricidade_arco_choque",
            "shock": "sfx_eletricidade_arco_choque",
            "eletrochoque": "sfx_eletricidade_arco_choque",
            "flesh_burn": "sfx_eletricidade_arco_choque",
            "sussurros_espelho": "sfx_sussurros_espelho_banheiro",
            "explosao": "sfx_explosao_caldeira_impacto",
            "golpe_esforco": "sfx_combate_golpe_esforco",
            "rosnado": "sfx_besta_rosnado_ameaca",
            "monstro_triplo": "sfx_monstro_rosnar_triplo",
            "besta_dano": "sfx_besta_dano_gemido",
            "gosma": "sfx_aberracao_gosma_rastejar",
            "aberracao": "sfx_aberracao_gosma_rastejar",
            "ghoul": "sfx_ghoul_gargarejo_fome",
            "zumbi_morte": "sfx_zumbi_morte_estertor",
            "borbulhar": "sfx_sangue_viscoso_borbulhar",
            "mordida": "sfx_fratura_osso_mordida",
            "drenar": "sfx_fratura_osso_mordida",
            "uivo_nevoeiro": "sfx_nevoeiro_uivo_criatura",
            "item_coletado": "sfx_ui_item_coletado",
            "dossie": "sfx_dossie_carta_deslizar",
            "inventario": "sfx_inventario_abrir_pasta",
            "moedas": "sfx_moedas_ouro_transacao",
            "moedas_ouro": "sfx_moedas_ouro_transacao",
            "moedas_tilintar": "sfx_moedas_tilintar",
            "dado": "sfx_dado_rolagem_rpg",
            "frasco": "sfx_frasco_alquimia_vidro",
            "alquimia": "sfx_frasco_alquimia_vidro",
            "distorcao": "sfx_psiquico_distorcao_sanidade",
            "pena": "sfx_pena_anotacao_pista",
            "anotacao": "sfx_pena_anotacao_pista",
            "passos_gravilha": "sfx_passos_gravilha_patio",
            "passos_madeira": "sfx_passos_madeira_ranger",
            "passos_marmore": "sfx_passos_madeira_ranger",
            "passos": "sfx_passos_madeira_ranger",
            # Novos SFX táteis, mecânicos e de interação:
            "click": "sfx_click_seco",
            "click_seco": "sfx_click_seco",
            "sharpclick": "sfx_click_seco",
            "lanterna": "sfx_lanterna_click",
            "lanterna_click": "sfx_lanterna_click",
            "interruptor": "sfx_lanterna_click",
            "powerup": "sfx_rpg_afeto_levelup",
            "rpgpowerup": "sfx_rpg_afeto_levelup",
            "levelup": "sfx_rpg_afeto_levelup",
            "afeto_up": "sfx_rpg_afeto_levelup",
            "splash": "sfx_splash_sangue_tinta",
            "tinta": "sfx_splash_sangue_tinta",
            "paint_splash": "sfx_splash_sangue_tinta",
            "sangue_splash": "sfx_splash_sangue_tinta",
            "whoosh": "sfx_distorted_whoosh_vampirico",
            "whoosh_distorcido": "sfx_distorted_whoosh_vampirico",
            "esquiva": "sfx_distorted_whoosh_vampirico",
            "caixa_registradora": "sfx_caixa_registradora_valeria",
            "cash_register": "sfx_caixa_registradora_valeria",
            "taxa_valeria": "sfx_caixa_registradora_valeria",
            "desembrulhar": "sfx_desembrulhar_doce_curativo",
            "doce": "sfx_desembrulhar_doce_curativo",
            "curativo_gaze": "sfx_desembrulhar_doce_curativo",
            "unwrapping": "sfx_desembrulhar_doce_curativo",
            "amassar_lata": "sfx_amassar_lata_caldeiras",
            "lata": "sfx_amassar_lata_caldeiras",
            "cracking_can": "sfx_amassar_lata_caldeiras",
            "vento_frio": "sfx_distorted_whoosh_vampirico",
            "vasculhar_gaveta_abrir": "sfx_vasculhar_gaveta_abrir",
            "vasculhar_objetos_mexer": "sfx_vasculhar_objetos_mexer",
        }
        if clean.lower() in aliases:
            clean = aliases[clean.lower()]

        variants = [clean, clean.lower(), f"sfx_{clean.lower()}"]
        for v in variants:
            for ext in (".ogg", ".wav", ".mp3"):
                candidatos.append(f"audio/sfx/{v}{ext}")
                candidatos.append(f"audio/{v}{ext}")
                candidatos.append(f"audio/ambiente/{v}{ext}")
                candidatos.append(f"audio/voice/{v}{ext}")

        for cand in candidatos:
            if renpy.loadable(cand):
                renpy.sound.play(cand)
                return True
        return False

    def th_stinger(nome):
        """Toca stinger musical dramático (2.2s a 4.5s) no canal dedicado 'stinger' (mixer sfx)."""
        stinger_aliases = {
            "afeto": "stinger_afeto_up",
            "afeto_up": "stinger_afeto_up",
            "love": "stinger_afeto_up",
            "duvida": "stinger_duvida_alerta",
            "duvida_alerta": "stinger_duvida_alerta",
            "alerta": "stinger_duvida_alerta",
            "suspeita": "stinger_duvida_alerta",
            "pista": "stinger_pista_oculta",
            "pista_oculta": "stinger_pista_oculta",
            "oculto": "stinger_pista_oculta",
            "revelacao": "stinger_pista_oculta",
            "zona_vermelha": "stinger_zona_vermelha",
            "perigo": "stinger_zona_vermelha",
            "hostil": "stinger_zona_vermelha",
            "jumpscare": "stinger_jumpscare_anomalia",
            "anomalia": "stinger_jumpscare_anomalia",
            "susto": "stinger_jumpscare_anomalia",
            "terror": "stinger_jumpscare_anomalia",
            "fome": "stinger_fome_frenesi",
            "frenesi": "stinger_fome_frenesi",
            "fome_frenesi": "stinger_fome_frenesi",
            "sede": "stinger_fome_frenesi",
            "vitoria": "stinger_vitoria_combate",
            "vitoria_combate": "stinger_vitoria_combate",
            "win": "stinger_vitoria_combate",
            "triunfo": "stinger_vitoria_combate",
            "morte": "stinger_morte_definitiva",
            "morte_definitiva": "stinger_morte_definitiva",
            "gameover": "stinger_morte_definitiva",
            "fim": "stinger_morte_definitiva",
            "sombra": "stinger_jumpscare_anomalia",
            "sombra_passando": "stinger_jumpscare_anomalia",
        }
        clean = str(nome).strip().lower()
        resolved = stinger_aliases.get(clean, clean)
        if not resolved.startswith("stinger_"):
            resolved = f"stinger_{resolved}"

        candidatos = [
            f"audio/sfx/{resolved}.ogg",
            f"audio/{resolved}.ogg",
            f"audio/sfx/{nome}.ogg",
            f"audio/{nome}.ogg"
        ]

        for cand in candidatos:
            if renpy.loadable(cand):
                try:
                    renpy.music.set_volume(1.0, channel="stinger")
                    renpy.music.play(cand, channel="stinger", loop=False)
                except Exception:
                    renpy.sound.play(cand)
                return True

        if config.developer:
            renpy.notify(f"Stinger ausente: {nome}")
        return False



    def th_aviso(titulo, texto, cor="#ffcc66"):

        """Exibe card lateral de aviso narrativo e registra no log tático."""

        try:

            if hasattr(store, "historico_tatico_feniks") and isinstance(store.historico_tatico_feniks, list):

                _t_clean = str(titulo).replace("%%", "%")
                _txt_clean = str(texto).replace("%%", "%")
                store.historico_tatico_feniks.append(f"{_t_clean}: {_txt_clean}")

                if len(store.historico_tatico_feniks) > 30:

                    store.historico_tatico_feniks.pop(0)

        except Exception:

            pass

        renpy.show_screen("th_aviso", titulo, texto, cor)



    class DividaAtiva:

        def __init__(self, id_divida, credor, descricao, tipo_custo="livre", valor_custo=0, recompensa_texto="Honra preservada", quitada=False):

            self.id = id_divida

            self.credor = credor

            self.descricao = descricao

            self.tipo_custo = tipo_custo

            self.valor_custo = valor_custo

            self.recompensa_texto = recompensa_texto

            self.quitada = quitada



        @property
        def credor_display(self):
            if self.credor in ["Lility", "Mestra", "Lili", "Lyra"]:
                return getattr(store, "nome_display_mestra", "Mestra")
            return self.credor

        @property

        def pode_quitar(self):

            if self.quitada:

                return False

            if self.tipo_custo == "dinheiro":

                return store.dinheiro_jogador >= self.valor_custo

            elif self.tipo_custo == "sucata":

                return store.sucata_eletronica >= self.valor_custo

            elif self.tipo_custo == "giz":

                return store.giz_protecao >= self.valor_custo

            elif self.tipo_custo == "informacao_elara":

                return getattr(store, "relatorio_gremio_obtido", False) or getattr(store, "conhecimento_oculto", 0) >= 2

            elif self.tipo_custo == "mapa_emilia":

                return getattr(store, "conhecimento_oculto", 0) >= 1

            elif self.tipo_custo == "oferenda_lility":

                return store.dose_absinto >= 1 or getattr(store, "tem_partitura_runica", False)

            elif self.tipo_custo == "institucional":

                return store.dinheiro_jogador >= self.valor_custo or getattr(store, "relatorio_gremio_obtido", False)

            elif self.tipo_custo == "livre":

                return False

            return False



        @property

        def custo_descricao(self):

            if self.tipo_custo == "dinheiro":

                return f"${self.valor_custo} (Você tem: ${store.dinheiro_jogador})"

            elif self.tipo_custo == "sucata":

                return f"{self.valor_custo}x Sucata (Você tem: {store.sucata_eletronica})"

            elif self.tipo_custo == "giz":

                return f"{self.valor_custo}x Giz (Você tem: {store.giz_protecao})"

            elif self.tipo_custo == "informacao_elara":

                relat = "Relatório em mãos" if getattr(store, "relatorio_gremio_obtido", False) else f"2x Conhecimento (Tem: {getattr(store, 'conhecimento_oculto', 0)})"

                return f"Relatório de Patrulha ou 2x Conhecimento Oculto ({relat})"

            elif self.tipo_custo == "mapa_emilia":

                return f"1x Conhecimento Oculto compartilhado (Você tem: {getattr(store, 'conhecimento_oculto', 0)})"

            elif self.tipo_custo == "oferenda_lility":

                abs_tem = store.dose_absinto >= 1

                part_tem = getattr(store, "tem_partitura_runica", False)

                status_abs = "1x Absinto" if abs_tem else ("Partitura Rúnica" if part_tem else "Requer 1x Absinto ou Partitura")

                return f"Oferenda Nobre ({status_abs})"

            elif self.tipo_custo == "institucional":

                relat = "Relatório em mãos" if getattr(store, "relatorio_gremio_obtido", False) else f"Requer ${self.valor_custo}"

                return f"${self.valor_custo} ou Relatório Político do Grêmio ({relat} | Tem: ${store.dinheiro_jogador})"

            return "Obrigação em aberto (Resolução narrativa no campus)"



        def quitar(self):

            if not self.pode_quitar or self.quitada:

                return False



            if self.tipo_custo == "dinheiro":

                store.dinheiro_jogador -= self.valor_custo

            elif self.tipo_custo == "sucata":

                store.sucata_eletronica -= self.valor_custo

            elif self.tipo_custo == "giz":

                store.giz_protecao -= self.valor_custo

            elif self.tipo_custo == "informacao_elara":

                if getattr(store, "relatorio_gremio_obtido", False):

                    store.relatorio_gremio_obtido = False

                else:

                    store.conhecimento_oculto = max(0, store.conhecimento_oculto - 2)

            elif self.tipo_custo == "mapa_emilia":

                store.conhecimento_oculto = max(0, store.conhecimento_oculto - 1)

            elif self.tipo_custo == "oferenda_lility":

                if store.dose_absinto >= 1:

                    store.dose_absinto -= 1

                elif getattr(store, "tem_partitura_runica", False):

                    store.tem_partitura_runica = False



            self.quitada = True



            if self.tipo_custo == "institucional":

                if getattr(store, "relatorio_gremio_obtido", False):

                    store.relatorio_gremio_obtido = False

                else:

                    store.dinheiro_jogador = max(0, store.dinheiro_jogador - self.valor_custo)



            # Aplica efeitos ao quitar dependendo do credor (sem duplicidade em store.status_*.afeto)

            if "Valéria" in self.credor or "Valeria" in self.credor:

                store.afeto_valeria += 2

                if self.id == "divida_valeria_sangue_fiado":

                    notificar_rpg("📜 FIADO QUITADO COM VALÉRIA", "+2 Afeto de Valéria | Balcão de fiado liberado novamente!", "#66ff66")

                else:

                    store.dinheiro_jogador += 60

                    notificar_rpg("📜 DÍVIDA PAGA COM VALÉRIA", "+2 Afeto de Valéria | Respeito comercial nos porões!", "#66ff66")

            elif "Conselho" in self.credor or self.id == "divida_taxa_atrasada":

                store.exposicao = max(0, store.exposicao - 6)

                store.atrasos_taxa_consecutivos = 0

                if getattr(store, "divida_monitores", 0) > 0:

                    store.divida_monitores = max(0, store.divida_monitores - min(store.divida_monitores, self.valor_custo))

                if any(s.get("id") == "taxa_inadimplente" for s in getattr(store, "sequelas_ativas", [])):

                    curar_sequela("taxa_inadimplente")

                notificar_rpg("📜 TAXA REGULARIZADA", "Inadimplência removida | -6%% Exposição no Conselho!", "#00ffcc")

            elif "Elara" in self.credor:

                store.exposicao = max(0, store.exposicao - 20)

                store.afeto_elara += 1

                notificar_rpg("📜 DÍVIDA PAGA COM ELARA", "-20%% Exposição | Conselho Estudantil satisfeito!", "#00ffcc")

            elif "Emília" in self.credor or "Emilia" in self.credor:

                store.afeto_emilia += 2

                store.humanidade = min(100, store.humanidade + 3)

                notificar_rpg("📜 PROMESSA CUMPRIDA COM EMÍLIA", "+2 Afeto de Emília | +3 Humanidade preservada!", "#88ccff")

            elif ("Lility" in self.credor or "Mestra" in self.credor or "Lili" in self.credor):

                store.afeto_mestra += 2

                store.vinculo_sangue_lility = min(100, store.vinculo_sangue_lility + 15)

                notificar_rpg("📜 DÍVIDA HONRADA COM A MESTRA", f"+2 Afeto com {getattr(store, 'nome_display_mestra', 'Mestra')} | +15 Vínculo Carmesim!", "#aa00ff")

            elif "Monitores" in self.credor:

                store.exposicao = max(0, store.exposicao - 15)

                notificar_rpg("📜 DÍVIDA PAGA COM OS MONITORES", "Boletim de infração arquivado (-15%% Exposição)!", "#ffcc00")

            elif "Escola" in self.credor:

                store.humanidade = min(100, store.humanidade + 3)

                store.exposicao = max(0, store.exposicao - 25)

                notificar_rpg("📜 CONTRATO INSTITUCIONAL QUITADO", "Victor liquidou suas obrigações com a Academia (+3 Humanidade / -25%% Exposição)!", "#00ffcc")

            else:

                store.humanidade = min(100, store.humanidade + 2)

                notificar_rpg("📜 DÍVIDA QUITADA", "Victor honrou sua palavra (+2 Humanidade).", "#00ffcc")



            for idx, item_str in enumerate(store.livro_de_dividas):

                if self.credor in item_str and not item_str.startswith("~~"):

                    store.livro_de_dividas[idx] = f"~~{item_str}~~ [QUITADA]"

                    break



            return True



    def th_dever(credor, motivo, id_divida=None, tipo_custo="livre", valor_custo=0, recompensa=None):

        registro = f"{credor} — {motivo}"

        if registro not in store.livro_de_dividas:

            store.livro_de_dividas.append(registro)



        if not id_divida:

            if "Emília" in credor or "Emilia" in credor:

                id_divida = "divida_emilia_mapa"

                tipo_custo = "mapa_emilia"

                recompensa = "+2 Afeto com Emília | +3 Humanidade"

            elif "Monitores" in credor:

                id_divida = "divida_monitores_frasco"

                tipo_custo = "dinheiro"

                valor_custo = 120

                recompensa = "Arquiva boletim de infração | -15% Exposição"

            elif "Elara" in credor:

                id_divida = "divida_elara_bolsas"

                tipo_custo = "informacao_elara"

                recompensa = "-20% Exposição | Alívio da vigilância do Grêmio"

            elif ("Lility" in credor or "Mestra" in credor or "Lili" in credor):

                id_divida = "divida_lility_vida"

                tipo_custo = "oferenda_lility"

                recompensa = "+2 Afeto com a Mestra | +15 Vínculo Carmesim"

            elif "Valéria" in credor or "Valeria" in credor:

                id_divida = "divida_valeria_favores"

                tipo_custo = "sucata"

                valor_custo = 2

                recompensa = "+2 Afeto de Valéria | Respeito nos porões"

            elif "Escola" in credor:

                id_divida = "divida_escola_bolsa"

                tipo_custo = "institucional"

                valor_custo = 480

                recompensa = "+3 Humanidade | -25% Exposição"

            else:

                id_divida = f"divida_{len(store.registro_dividas_ativas) + 1}"

                recompensa = "+2 Humanidade"



        if not recompensa:

            recompensa = "+2 Humanidade"



        if id_divida not in store.registro_dividas_ativas:

            store.registro_dividas_ativas[id_divida] = DividaAtiva(

                id_divida, credor, motivo, tipo_custo, valor_custo, recompensa

            )



        th_aviso("DÍVIDA REGISTRADA", f"{credor}: {motivo}", "#ffcc66")



    def sincronizar_dividas_ativas():

        for d_str in store.livro_de_dividas:

            if ("Emília" in d_str or "Emilia" in d_str) and "divida_emilia_mapa" not in store.registro_dividas_ativas:

                th_dever("Emília", "um mapa da escola", "divida_emilia_mapa", "mapa_emilia", 0, "+2 Afeto com Emília | +3 Humanidade")

            elif "Monitores" in d_str and "divida_monitores_frasco" not in store.registro_dividas_ativas:

                th_dever("Os Monitores", "ressarcimento do frasco da ala médica", "divida_monitores_frasco", "dinheiro", 120, "Arquiva boletim de infração | -15% Exposição")

            elif "Elara" in d_str and "divida_elara_bolsas" not in store.registro_dividas_ativas:

                th_dever("Elara", "duas bolsas extras (relatórios sobre o subsolo)", "divida_elara_bolsas", "informacao_elara", 0, "-20% Exposição | Alívio da vigilância do Grêmio")

            elif ("Lility" in d_str or "Mestra" in d_str) and "divida_lility_vida" not in store.registro_dividas_ativas:

                th_dever("Mestra", "a minha vida (uma 'prorrogação')", "divida_lility_vida", "oferenda_lility", 0, "+2 Afeto com a Mestra | +15 Vínculo Carmesim")

            elif ("Valéria" in d_str or "Valeria" in d_str) and "divida_valeria_favores" not in store.registro_dividas_ativas:

                th_dever("Valéria", "favores de contrabando nas caldeiras", "divida_valeria_favores", "sucata", 2, "+2 Afeto de Valéria | Respeito nos porões")

            elif "Escola" in d_str and "divida_escola_bolsa" not in store.registro_dividas_ativas:

                th_dever("A Escola", "a bolsa integral e o termo de admissão", "divida_escola_bolsa", "institucional", 480, "+3 Humanidade | -25% Exposição")



    def th_credito(devedor, motivo):

        registro = f"{devedor} — {motivo}"

        if registro not in livro_de_creditos:

            livro_de_creditos.append(registro)

        th_aviso("ALGUÉM TE DEVE", f"{devedor}: {motivo}", "#88ddaa")



    def th_boato(texto):

        if texto not in livro_de_boatos:

            livro_de_boatos.append(texto)

            th_aviso("BOATO COLHIDO", texto, "#99aaff")



    def th_quebrar_regra(n):

        if n not in regras_quebradas and 1 <= n <= len(th_regras_texto):

            regras_quebradas.append(n)

            th_aviso(f"REGRA {n} QUEBRADA", th_regras_texto[n - 1], "#ff5566")



    def obter_status_doom_texto():

        doom = getattr(store, 'ruina_cain', 10)

        if doom >= 85:

            return f'DOOM: {doom}%  ·  O Despertar Sob as Pedras é Iminente', '#ff2244'

        elif doom >= 70:

            return f'DOOM: {doom}%  ·  O Véu se Rompe — Névoa e Histeria no Campus', '#ff4444'

        elif doom >= 50:

            return f'DOOM: {doom}%  ·  A Deterioração Avança — Toque de Recolher', '#ff8800'

        elif doom >= 25:

            return f'DOOM: {doom}%  ·  Murmúrios no Subsolo — O Mundo se Desgasta', '#ffcc00'

        else:

            return f'DOOM: {doom}%  ·  Calmaria Aparente — O Pulso das Profundezas', '#88ccff'



    def th_cartao(dia, periodo):

        zonas = {

            'Manhã': ('ZONA AZUL — segurança relativa', '#66aaff'),

            'Tarde': ('ZONA AMARELA — vigilância', '#ffcc44'),

            'Noite': ('ZONA VERMELHA — perigo letal', '#ff3344'),

        }

        zona, cor = zonas.get(periodo, ('', '#ffffff'))

        doom_texto, doom_cor = obter_status_doom_texto()

        renpy.show_screen('th_cartao_periodo', dia, periodo, zona, cor, doom_texto, doom_cor)

        renpy.pause(2.0, hard=False)

        renpy.hide_screen('th_cartao_periodo')



# --- Transforms e Efeitos Visuais --------------------------------------------

transform th_cartao_anim:

    alpha 0.0 xoffset -80

    easein 0.35 alpha 1.0 xoffset 0

    pause 1.4

    easeout 0.35 alpha 0.0 xoffset 80



transform th_espelho_flip:

    xzoom -1.0

    matrixcolor TintMatrix("#a8c4e0")

    alpha 0.85



transform th_aviso_anim:

    alpha 0.0 xoffset 420

    easein 0.3 alpha 1.0 xoffset 0

    pause 2.8

    easeout 0.4 alpha 0.0 xoffset 420



# --- Telas da Interface Narrativa --------------------------------------------

screen th_cartao_periodo(dia, periodo, zona, cor, doom_texto, doom_cor):

    zorder 150

    modal False

    key 'dismiss' action Return()

    frame at th_cartao_anim:

        background Solid('#000000d9')

        xfill True

        ysize 250

        yalign 0.45

        vbox:

            xalign 0.5

            yalign 0.5

            spacing 6

            text 'DIA [dia]  ·  [periodo]' size 76 color '#ffffff' xalign 0.5

            text '[zona]' size 28 color cor xalign 0.5

            text '[doom_texto]' size 22 color doom_cor xalign 0.5 bold True



screen th_aviso(titulo, texto, cor="#ffcc66"):

    zorder 140

    frame at th_aviso_anim:

        background Solid("#000000cc")

        xalign 0.99

        yalign 0.2

        xsize 560

        padding (28, 18)

        vbox:

            spacing 6

            text "[titulo]" size 26 color cor bold True

            text "[texto]" size 22 color "#e8e8e8"

    timer 3.6 action Hide("th_aviso")



screen th_regras_victor():

    modal True

    zorder 160

    add Solid("#000000cc")

    key "dismiss" action Return()

    frame:

        background Solid("#d8c9a0")

        xalign 0.5

        yalign 0.5

        xsize 1000

        padding (70, 56)

        vbox:

            spacing 22

            text "Verso da carta de bolsa — a lápis" size 26 color "#5b4a2a" italic True

            for regra in th_regras_texto:

                text regra size 34 color "#2a2118"

            null height 10

            textbutton "Dobrar a carta e guardá-la":

                action Return()

                xalign 1.0

                text_size 28

                text_color "#5b4a2a"

                text_hover_color "#000000"



screen th_balanco_dia(titulo):

    modal True

    zorder 170

    add Solid("#000000ee")

    key "dismiss" action Return()

    vbox:

        xalign 0.5

        yalign 0.5

        xsize 1600

        spacing 40

        text "[titulo]" size 58 color "#ffffff" xalign 0.5

        hbox:

            xalign 0.5

            spacing 70

            vbox:

                xsize 480

                spacing 12

                text "REGRAS DE VICTOR" size 28 color "#ffcc66"

                for i, regra in enumerate(th_regras_texto):

                    if (i + 1) in regras_quebradas:

                        text ("{s}%s{/s}" % regra) size 22 color "#777777"

                    else:

                        text regra size 22 color "#e8e8e8"

            vbox:

                xsize 480

                spacing 12

                text "LIVRO DE DÍVIDAS" size 28 color "#ffcc66"

                if not livro_de_dividas:

                    text "Nenhuma. Por enquanto." size 22 color "#aaaaaa"

                for d in livro_de_dividas:

                    text ("• %s" % d) size 22 color "#e8e8e8"

                if livro_de_creditos:

                    null height 8

                    text "ME DEVEM" size 24 color "#88ddaa"

                    for c in livro_de_creditos:

                        text ("• %s" % c) size 22 color "#e8e8e8"

            vbox:

                xsize 480

                spacing 12

                text "BOATOS DO CORREDOR" size 28 color "#99aaff"

                if not livro_de_boatos:

                    text "Ainda ninguém falou comigo." size 22 color "#aaaaaa"

                for b in livro_de_boatos:

                    text ("• %s" % b) size 22 color "#e8e8e8"

        textbutton "Continuar":

            action Return()

            xalign 0.5

            text_size 32

            text_color "#00ffcc"

            text_hover_color "#ffffff"





# ==============================================================================

# SISTEMA DE DUBLAGEM PARCIAL E VOICE BARKS (VOICE STUDIO)

# ==============================================================================



init -1 python:

    # Registra canal dedicado 'barks' vinculado ao mixer 'voice'
    # Isso impede que o comando say do Ren'Py corte o áudio no meio da fala
    renpy.music.register_channel("barks", mixer="voice", loop=False, stop_on_mute=True)

    # Registra canal dedicado 'stinger' vinculado ao mixer 'sfx'
    # Permite que acordes e impactos de 2.5s-4.5s toquem simultaneamente com SFX sem interrupção
    renpy.music.register_channel("stinger", mixer="sfx", loop=False, stop_on_mute=True)
    renpy.music.set_volume(1.0, channel="stinger")
    renpy.music.set_volume(1.0, channel="barks")



init python:

    BARKS_VOZ = {

        "lility": {

            "padrao": ["lility_bark_deboche", "lility_bark_cachorrinho", "lility_bark_risada", "lility_bark_inacabada", "lility_bark_fome_antiga", "lility_bark_afeto_alto"],

            "confronto": ["lility_bark_dentes", "lility_bark_ameaca"],

            "decisao": ["lility_bark_inacabada"],

            "irritada": ["lility_bark_ameaca", "lility_bark_tedio"],

            "timida": ["lility_bark_vergonha"],

            "transe": ["lility_bark_transe"],

            "crit": ["lility_bark_crit"],

            "ciume": ["lility_bark_ciume"],

            "aviso": ["lility_bark_aviso"],
            "exposicao": ["lility_bark_exposicao"],
            "rejeicao": ["lility_bark_rejeicao"],
            "prazer": ["lility_bark_prazer"],
            "luta": ["lility_bark_luta"],
            "pesadelo": ["lility_bark_pesadelo"],
            "fome_critica": ["lility_bark_fome_critica"],
            "doom": ["lility_bark_cain_eco"],
            "despedida": ["lility_bark_rejeicao"],
            "flagrante": ["lility_bark_ameaca"],
            "toque_limite": ["lility_bark_dentes"],
            "pacto_anel": ["lility_bark_prazer"],
            "deboche": ["lility_bark_deboche"],
            "dentes": ["lility_bark_dentes"],

            "risada": ["lility_bark_risada", "lility_risada_deboche", "lility_risada_ronronar"],

            # Novas Chaves de Expansão (en-US)
            "elara_desdem": ["lility_bark_elara_desdem"],
            "grilhao_dor": ["lility_bark_grilhao_dor"],
            "faro_gremio": ["lility_bark_faro_gremio"],
            "faro_clero": ["lility_bark_faro_clero"],
            "toque_orelha": ["lility_bark_toque_orelha"],
            "toque_broche": ["lility_bark_toque_broche"],
            "duelo_falha": ["lility_bark_duelo_falha"],
            "noite_fora": ["lility_bark_noite_fora"],
            "afeto_alto": ["lility_bark_afeto_alto"],
            "cain_eco": ["lility_bark_cain_eco"],
            "climax_mortal": ["lility_climax_06_mortal"],
            "climax_06_mortal": ["lility_climax_06_mortal"],

        },

        "elara": {

            "padrao": ["elara_bark_chamado", "elara_bark_risada", "elara_bark_registered", "elara_bark_alianca"],

            "confronto": ["elara_bark_data_point", "elara_bark_ordem", "elara_bark_liability"],

            "decisao": ["elara_bark_someone_pays"],

            "irritada": ["elara_bark_desprezo", "elara_bark_ordem"],

            "timida": ["elara_bark_corada"],

            "transe": ["elara_bark_transe"],

            "crit": ["elara_bark_aprovacao"],

            "ciume": ["elara_bark_ciume"],
            "dor": ["elara_bark_dor"],
            "derrota": ["elara_bark_derrota", "elara_bark_derrota_luta"],
            "hesitacao": ["elara_bark_hesitacao"],
            "alerta": ["elara_bark_alerta"],
            "exposicao": ["elara_bark_exposicao"],
            "fome_critica": ["elara_bark_canibalismo"],
            "doom": ["elara_bark_barreira_falha"],
            "despedida": ["elara_bark_ordem"],
            "flagrante": ["elara_bark_ordem"],
            "toque_corada": ["elara_bark_toque_submissa"],
            "presente_colar": ["elara_bark_toque_bracadeira"],
            "autoridade": ["elara_bark_ordem", "elara_bark_liability"],
            "ordem": ["elara_bark_ordem"],
            "aprovacao": ["elara_bark_aprovacao"],
            "corada": ["elara_bark_corada"],
            "desconfiada": ["elara_bark_liability", "elara_bark_data_point"],

            "risada": ["elara_bark_risada", "elara_risada_desprezo", "elara_risada_divertida"],

            # Novas Chaves de Expansão (en-US)
            "sangue_clero": ["elara_bark_sangue_clero"],
            "canibalismo": ["elara_bark_canibalismo"],
            "relatorio_ok": ["elara_bark_relatorio_ok"],
            "submundo": ["elara_bark_submundo"],
            "barreira_falha": ["elara_bark_barreira_falha"],
            "toque_bracadeira": ["elara_bark_toque_bracadeira"],
            "toque_submissa": ["elara_bark_toque_submissa"],
            "combate_foice": ["elara_bark_combate_foice"],
            "derrota_luta": ["elara_bark_derrota_luta"],
            "alianca": ["elara_bark_alianca"],
            "nora_desvio": ["elara_bark_nora_desvio"],
            "climax_trono": ["elara_climax_04_trono"],
            "climax_04_trono": ["elara_climax_04_trono"],

        },

        "emilia": {

            "padrao": ["emilia_bark_chamado", "emilia_bark_cura", "emilia_bark_risada", "emilia_bark_oracao", "emilia_bark_manha_cansada"],

            "suspeita": ["emilia_bark_suspeita", "emilia_bark_po_nas_maos", "emilia_bark_duvida_alta"],

            "votos": ["emilia_bark_votos"],

            "timida": ["emilia_bark_timida"],

            "irritada": ["emilia_bark_suspeita", "emilia_bark_prata"],

            "alerta": ["emilia_bark_alerta"],
            "exposicao": ["emilia_bark_exposicao"],
            "transe": ["emilia_bark_pacto"],

            "crit": ["emilia_bark_crit"],
            "dor": ["emilia_bark_dor"],
            "consolo": ["emilia_bark_consolo"],
            "reza": ["emilia_bark_reza"],
            "lagrima": ["emilia_bark_lagrima"],
            "fome_critica": ["emilia_bark_fase2_pena"],
            "doom": ["emilia_bark_oracao"],
            "despedida": ["emilia_bark_oracao"],
            "flagrante": ["emilia_bark_alerta"],
            "toque_calor": ["emilia_bark_toque_mao"],
            "presente_flores": ["emilia_bark_consolo"],
            "chamado": ["emilia_bark_chamado"],
            "cura": ["emilia_bark_cura"],

            "risada": ["emilia_bark_risada", "emilia_risada_alivio", "emilia_risada_timida"],

            # Novas Chaves de Expansão (en-US)
            "manha_cansada": ["emilia_bark_manha_cansada"],
            "fase2_pena": ["emilia_bark_fase2_pena"],
            "duvida_alta": ["emilia_bark_duvida_alta"],
            "cacada_inicio": ["emilia_bark_cacada_inicio"],
            "cacada_vitoria": ["emilia_bark_cacada_vitoria"],
            "toque_oculos": ["emilia_bark_toque_oculos"],
            "toque_mao": ["emilia_bark_toque_mao"],
            "faro_profano": ["emilia_bark_faro_profano"],
            "phillip_conflito": ["emilia_bark_phillip_conflito"],
            "cacadora_hostil": ["emilia_bark_cacadora_hostil"],
            "ritual_corte": ["emilia_bark_ritual_corte"],
            "climax_lamento": ["emilia_climax_02_lamento"],
            "climax_02_lamento": ["emilia_climax_02_lamento"],

        },

        "valeria": {

            "padrao": ["valeria_bark_negocios", "valeria_bark_risada", "valeria_bark_who_pays", "valeria_bark_saudacao_01", "valeria_bark_saudacao_02"],

            "provocacao": ["valeria_bark_provocacao", "valeria_bark_price_not_value", "valeria_bark_tres_goles"],

            "toque": ["valeria_bark_toque"],

            "irritada": ["valeria_bark_armadilha", "valeria_bark_bloqueio"],
            "exposicao": ["valeria_bark_exposicao"],
            "transe": ["valeria_bark_safra", "valeria_bark_transe"],

            "crit": ["valeria_bark_crit", "valeria_bark_duelo_crit"],
            "dor": ["valeria_bark_dor"],
            "segredo": ["valeria_bark_segredo"],
            "vitoria": ["valeria_bark_vitoria"],
            "fome_critica": ["valeria_bark_confronto_ghoul"],
            "doom": ["valeria_bark_lote_contaminado"],
            "despedida": ["valeria_bark_negocios"],
            "flagrante": ["valeria_bark_armadilha"],
            "toque_troco": ["valeria_bark_toque_taxa"],
            "presente_jaqueta": ["valeria_bark_monopolio_virada"],

            "risada": ["valeria_bark_risada", "valeria_risada_cinica", "valeria_risada_estalo"],

            # Novas Chaves de Expansão (en-US)
            "saudacao": ["valeria_bark_saudacao_01", "valeria_bark_saudacao_02"],
            "saudacao_01": ["valeria_bark_saudacao_01"],
            "saudacao_02": ["valeria_bark_saudacao_02"],
            "negocios": ["valeria_bark_negocios"],
            "sem_dinheiro": ["valeria_bark_sem_dinheiro"],
            "confronto_ghoul": ["valeria_bark_confronto_ghoul"],
            "lote_contaminado": ["valeria_bark_lote_contaminado"],
            "fada_verde": ["valeria_bark_fada_verde"],
            "toque_cabelo": ["valeria_bark_toque_cabelo"],
            "toque_taxa": ["valeria_bark_toque_taxa"],
            "toque_choque": ["valeria_bark_toque_choque"],
            "toque_submissa": ["valeria_bark_toque_submissa"],
            "faro_ousadia": ["valeria_bark_faro_ousadia"],
            "duelo_crit": ["valeria_bark_duelo_crit"],
            "duelo_falha": ["valeria_bark_duelo_falha"],
            "monopolio_virada": ["valeria_bark_monopolio_virada"],
            "climax_alianca": ["valeria_climax_05_alianca"],
            "climax_05_alianca": ["valeria_climax_05_alianca"],

        },

        "victor": {

            "frenesi": ["victor_bark_frenesi"],

            "garras": ["victor_bark_garras"],

            "ataque": ["victor_bark_ataque"],

            "dano": ["victor_bark_dano"],
            "dor_leve": ["victor_bark_dor_leve"],
            "vitoria": ["victor_bark_vitoria"],
            "regras": ["victor_bark_regras"],
            "furioso": ["victor_bark_furioso"],

            "drenar": ["victor_bark_drenar"],

            "divida": ["victor_bark_divida"],

            "morte": ["victor_bark_morte"],

            "acordar": ["victor_bark_acordar"],

        },

        "outros": {

            "phillip": ["phillip_bark_ameaca"],
            "phillip_dor": ["phillip_bark_dor"],
            "phillip_risada": ["phillip_bark_risada"],

            "cain": ["cain_bark_desafio"],

            "nora": ["nora_bark_loucura"],
            "nora_dor": ["nora_bark_dor"],
            "nora_risada": ["nora_bark_risada"],

            "hachishaku": ["hachishaku_bark_po"],

            "loira": ["loira_bark_espelho"],
            "loira_dor": ["loira_bark_dor"],
            "loira_risada": ["loira_bark_risada"],

            "fada": ["fada_bark_enigma"],
            "fada_dor": ["fada_bark_dor"],
            "fada_risada": ["fada_bark_risada"],

        }

    }



    def th_bark(personagem, tom="padrao"):
        """
        Reproduz um voice bark curto no canal dedicado 'barks' (mixer 'voice') do Ren'Py.
        Verifica com renpy.loadable para evitar erros caso o áudio não exista.
        O canal 'barks' não é interrompido pelo surgimento da caixa de diálogo.
        Suporta sorteio dinâmico anti-repetição entre variantes usando store._ultimo_bark_tocado.
        """
        import random
        dict_char = BARKS_VOZ.get(personagem, {})
        opcoes = dict_char.get(tom, [])

        # Resoluções contextuais dinâmicas para tom == "saudacao" ou "padrao"
        if tom in ("saudacao", "padrao"):
            if personagem == "lility":
                afeto = getattr(store, "afeto_mestra", 0)
                fome = getattr(store, "fome_sangue", 100)
                if fome < 20 and "fome_critica" in dict_char:
                    opcoes = dict_char["fome_critica"]
                elif afeto >= 8 and "afeto_alto" in dict_char:
                    opcoes = dict_char["afeto_alto"] + dict_char.get("padrao", [])
            elif personagem == "elara":
                doom = getattr(store, "doom_clock", 0)
                afeto = getattr(store, "afeto_elara", 0)
                if doom >= 60 and "barreira_falha" in dict_char:
                    opcoes = dict_char["barreira_falha"]
                elif afeto >= 4 and "alianca" in dict_char:
                    opcoes = dict_char["alianca"] + dict_char.get("padrao", [])
            elif personagem == "emilia":
                duvida = getattr(store, "duvida_emilia", 0)
                fase = getattr(store, "fase_victor", 1)
                if duvida >= 3 and "duvida_alta" in dict_char:
                    opcoes = dict_char["duvida_alta"]
                elif fase >= 2 and "fase2_pena" in dict_char:
                    opcoes = dict_char["fase2_pena"] + dict_char.get("padrao", [])
            elif personagem == "valeria":
                afeto = getattr(store, "afeto_valeria", 0)
                if afeto >= 2 and "saudacao_02" in dict_char:
                    opcoes = dict_char["saudacao_02"]
                elif "saudacao_01" in dict_char:
                    opcoes = dict_char["saudacao_01"]

        if not opcoes:
            # Resolução direta pelo nome do tom ou arquivo no disco
            for direct_cand in [tom, f"{personagem}_{tom}", f"{personagem}_bark_{tom}"]:
                for ext in (".ogg", ".wav"):
                    p_cand = f"audio/voice/{personagem}/{direct_cand}{ext}"
                    if renpy.loadable(p_cand):
                        opcoes = [direct_cand]
                        break
                if opcoes:
                    break

        if not opcoes and tom != "padrao":
            opcoes = dict_char.get("padrao", [])
        if not opcoes and tom != "risada":
            opcoes = dict_char.get("risada", [])
        if not opcoes:
            return False

        # Constrói lista de arquivos válidos existentes no disco
        validos = []
        for opt in opcoes:
            for pref in (f"audio/voice/{personagem}/{opt}", f"audio/voice/{opt}", f"audio/{opt}"):
                for ext in (".ogg", ".wav"):
                    cand = f"{pref}{ext}"
                    if renpy.loadable(cand) and cand not in validos:
                        validos.append(cand)
                        break

        # Fallback de segurança se nenhuma opção específica existir
        if not validos:
            for opt_fb in dict_char.get("padrao", []) + dict_char.get("risada", []):
                cand = f"audio/voice/{personagem}/{opt_fb}.ogg"
                if renpy.loadable(cand) and cand not in validos:
                    validos.append(cand)

        if not validos:
            return False

        # Anti-repetição: não repete a mesma faixa consecutiva se houver mais de 1 opção válida
        if not hasattr(store, "_ultimo_bark_tocado") or not isinstance(store._ultimo_bark_tocado, dict):
            store._ultimo_bark_tocado = {}
        ultimo = store._ultimo_bark_tocado.get(personagem)
        cand_escolha = [v for v in validos if v != ultimo] if len(validos) > 1 else validos
        escolhido = random.choice(cand_escolha) if cand_escolha else validos[0]
        store._ultimo_bark_tocado[personagem] = escolhido

        renpy.sound.play(escolhido, channel="barks")
        return True



    BARKS_INIMIGOS = {
        "aluna": {
            "saudacao": ["aluna_bark_saudacao", "aluna_bark_saudacao_2"],
            "ataque": ["aluna_bark_ataque_1", "aluna_bark_ataque_2"],
            "dor": ["aluna_bark_dor", "aluna_bark_dor_2"],
            "risada": ["aluna_bark_risada", "aluna_bark_risada_2"],
            "derrota": ["aluna_bark_derrota_1"],
        },

        "policial": {
            "saudacao": ["policial_bark_saudacao", "policial_bark_saudacao_2"],
            "ataque": ["policial_bark_ataque_1", "policial_bark_ataque_2"],
            "dor": ["policial_bark_dor", "policial_bark_dor_2"],
            "risada": ["policial_bark_risada", "policial_bark_risada_2"],
            "derrota": ["policial_bark_derrota_1"],
        },

        "estudante": {
            "saudacao": ["estudante_bark_saudacao", "estudante_bark_saudacao_2"],
            "ataque": ["estudante_bark_ataque_1", "estudante_bark_ataque_2"],
            "dor": ["estudante_bark_dor", "estudante_bark_dor_2"],
            "risada": ["estudante_bark_risada", "estudante_bark_risada_2"],
            "derrota": ["estudante_bark_derrota_1"],
        },

        "inquisidor": {
            "saudacao": ["inquisidor_bark_saudacao", "inquisidor_bark_saudacao_2"],
            "ataque": ["inquisidor_bark_ataque_1", "inquisidor_bark_ataque_2"],
            "dor": ["inquisidor_bark_dor", "inquisidor_bark_dor_2"],
            "risada": ["inquisidor_bark_risada", "inquisidor_bark_risada_2"],
            "derrota": ["inquisidor_bark_derrota_1"],
        },

        "executora": {
            "saudacao": ["executora_bark_saudacao", "executora_bark_saudacao_2"],
            "ataque": ["executora_bark_ataque_1", "executora_bark_ataque_2"],
            "dor": ["executora_bark_dor", "executora_bark_dor_2"],
            "risada": ["executora_bark_risada", "executora_bark_risada_2"],
            "derrota": ["executora_bark_derrota_1"],
        },

        "alquimista": {
            "saudacao": ["alquimista_bark_saudacao", "alquimista_bark_saudacao_2"],
            "ataque": ["alquimista_bark_ataque_1", "alquimista_bark_ataque_2"],
            "dor": ["alquimista_bark_dor", "alquimista_bark_dor_2"],
            "risada": ["alquimista_bark_risada", "alquimista_bark_risada_2"],
            "derrota": ["alquimista_bark_derrota_1"],
        },

        "capanga": {
            "saudacao": ["capanga_bark_saudacao", "capanga_bark_saudacao_2"],
            "ataque": ["capanga_bark_ataque_1", "capanga_bark_ataque_2"],
            "dor": ["capanga_bark_dor", "capanga_bark_dor_2"],
            "risada": ["capanga_bark_risada", "capanga_bark_risada_2"],
            "derrota": ["capanga_bark_derrota_1"],
        },

        "guarda_prata": {
            "saudacao": ["guarda_prata_bark_saudacao", "guarda_prata_bark_saudacao_2"],
            "ataque": ["guarda_prata_bark_ataque_1", "guarda_prata_bark_ataque_2"],
            "dor": ["guarda_prata_bark_dor", "guarda_prata_bark_dor_2"],
            "risada": ["guarda_prata_bark_risada", "guarda_prata_bark_risada_2"],
            "derrota": ["guarda_prata_bark_derrota_1"],
        },

        "marionete": {
            "saudacao": ["marionete_bark_saudacao", "marionete_bark_saudacao_2"],
            "ataque": ["marionete_bark_ataque_1", "marionete_bark_ataque_2"],
            "dor": ["marionete_bark_dor", "marionete_bark_dor_2"],
            "risada": ["marionete_bark_risada", "marionete_bark_risada_2"],
            "derrota": ["marionete_bark_derrota_1"],
        },

    }



    def resolver_tipo_inimigo(nome):

        nome_l = str(nome).lower() if nome else ""

        # Marionete de Fios de Sangue possui sussurros e risada de boneca macabra
        if "marionete" in nome_l:
            return "marionete"

        # Inimigos não humanos (monstros, mortos-vivos, bestas, gárgulas de pedra e esqueletos sem fala humana)
        if any(w in nome_l for w in [
            "gargula", "gárgula", "esqueleto", "cao de sangue", "cão de sangue", "hellhound",
            "abominacao", "abominação", "espectro", "zumbi", "monstro", "inorganico", "besta", "fera"
        ]):
            return "monstro"

        if getattr(store, "tipo_sangue_inimigo", "") in ["inorganico"] and "marionete" not in nome_l:
            return "monstro"

        if "elara" in nome_l:
            return "elara"
        elif "lility" in nome_l:
            return "lility"
        elif "alquimista" in nome_l:
            return "alquimista"
        elif any(w in nome_l for w in ["capanga", "mecanico", "mecânico", "mascara gas", "máscara gás"]):
            return "capanga"
        elif any(w in nome_l for w in ["capitao da guarda", "capitão da guarda", "guarda do gremio", "guarda do grêmio", "conselho prata", "executor prata"]):
            return "guarda_prata"
        elif any(w in nome_l for w in ["policial", "oficial", "ronda", "detetive"]):
            return "policial"
        elif any(w in nome_l for w in ["inquisidor", "ordem", "sagrado"]):
            return "inquisidor"
        elif any(w in nome_l for w in ["caloura", "veterana", "aluna", "garota"]):
            return "aluna"
        elif any(w in nome_l for w in ["vampira", "executora", "professora", "mulher", "novica", "freira", "dama", "menina"]):
            return "executora"
        else:
            return "estudante"



    def th_bark_inimigo(nome_inimigo, tom="saudacao"):

        """

        Reproduz saudações, sons de dor e risadas dos inimigos e chefes no canal 'barks'.

        Chefes e anomalias exclusivas falam suas frases longas apenas na saudação inicial,
        usando sons de dor apropriados nos ataques recebidos sem repetir o discurso a cada golpe.
        Monstros e inorgânicos não possuem falas humanas de estudantes.

        """

        nome_l = str(nome_inimigo).lower() if nome_inimigo else ""

        tipo = resolver_tipo_inimigo(nome_inimigo)
        if tipo == "monstro":
            # Bestas e cães de sangue rugem/rosnam na saudação
            if any(w in nome_l for w in ["cao de sangue", "cão de sangue", "hellhound"]):
                if tom == "saudacao" and renpy.loadable("audio/sfx/sfx_hellhound_rosnar_gutural.ogg"):
                    renpy.sound.play("audio/sfx/sfx_hellhound_rosnar_gutural.ogg", channel="barks")
                    return True
            return False

        # Linha longa/especial de chefes e heroínas em combate
        if tipo == "elara":
            if tom == "saudacao":
                return th_bark("elara", "ordem")
            elif tom == "ataque":
                return th_bark("elara", "combate_foice")
            elif tom in ("derrota", "morte"):
                return th_bark("elara", "derrota_luta")
            elif tom == "dor":
                return th_bark("elara", "dor")
            elif tom == "risada":
                return th_bark("elara", "risada")

        if tipo == "lility":
            if tom == "saudacao":
                return th_bark("lility", "luta")
            elif tom == "dor":
                return th_bark("lility", "irritada")
            elif tom == "risada":
                return th_bark("lility", "risada")

        if tom == "saudacao":
            if "phillip" in nome_l:
                return th_bark("outros", "phillip")
            elif "cain" in nome_l:
                return th_bark("outros", "cain")
            elif "nora" in nome_l:
                return th_bark("outros", "nora")
            elif "hachishaku" in nome_l:
                return th_bark("outros", "hachishaku")
            elif "loira" in nome_l or "espelho" in nome_l:
                return th_bark("outros", "loira")
            elif "fada" in nome_l:
                return th_bark("outros", "fada")

        # Em combate contínuo (tom de dor, risada, ataque ou derrota), reproduz barks próprios dos chefes
        if "phillip" in nome_l:
            if tom in ["dor", "risada", "ataque", "derrota"]:
                cand = f"audio/voice/outros/phillip_bark_{tom}.ogg"
                if renpy.loadable(cand):
                    renpy.sound.play(cand, channel="barks")
                    return True

        elif "loira" in nome_l or "espelho" in nome_l:
            if tom in ["dor", "risada", "ataque", "derrota"]:
                cand = f"audio/voice/outros/loira_bark_{tom}.ogg"
                if renpy.loadable(cand):
                    renpy.sound.play(cand, channel="barks")
                    return True
        elif "fada" in nome_l:
            if tom in ["dor", "risada", "ataque", "derrota"]:
                cand = f"audio/voice/outros/fada_bark_{tom}.ogg"
                if renpy.loadable(cand):
                    renpy.sound.play(cand, channel="barks")
                    return True
        elif "nora" in nome_l:
            if tom in ["dor", "risada", "ataque", "derrota"]:
                cand = f"audio/voice/outros/nora_bark_{tom}.ogg"
                if renpy.loadable(cand):
                    renpy.sound.play(cand, channel="barks")
                    return True

        if "nora" in nome_l or "hachishaku" in nome_l or "loira" in nome_l or "fada" in nome_l:
            tipo = "executora"
        elif "phillip" in nome_l or "cain" in nome_l:
            tipo = "inquisidor"

        opcoes = BARKS_INIMIGOS.get(tipo, {}).get(tom, [])

        if not opcoes:
            if tom == "derrota":
                opcoes = BARKS_INIMIGOS.get(tipo, {}).get("dor", [])
            elif tom == "ataque":
                opcoes = BARKS_INIMIGOS.get(tipo, {}).get("risada", [])
            else:
                opcoes = BARKS_INIMIGOS.get(tipo, {}).get("saudacao", [])

        if not opcoes:

            return False

        escolhido = renpy.random.choice(opcoes)

        candidatos = [

            f"audio/voice/inimigos/{escolhido}.ogg",

            f"audio/voice/{escolhido}.ogg",

            f"audio/{escolhido}.ogg",

            f"audio/voice/inimigos/{escolhido}.wav"

        ]

        for cand in candidatos:

            if renpy.loadable(cand):

                renpy.sound.play(cand, channel="barks")

                return True

        return False





    def th_bark_mob(acao="abordagem"):
        """
        Reproduz os Voice Barks dinâmicos dos figurantes (mobs) no canal dedicado 'barks'.
        Detecta automaticamente o id do figurante (store.id_mob_atual) e a fase de
        Humanidade/Fome de Victor (F1: >= 65, F2: 35..64, F3: < 35 ou Fome < 20).
        Suporta:
          - "abordagem": saudação de encontro inicial do figurante.
          - "conversa": fala de diálogo/conversa investigativa (variantes 1 e 2).
          - "mordida": reação à mordida/sucção.
          - "suborno": reação ao suborno de guardas/policiais.
        O canal 'barks' garante que as falas não sejam interrompidas pelo diálogo do Ren'Py.
        """
        import random
        mob_slug = getattr(store, "id_mob_atual", "").replace(" ", "_")
        if not mob_slug:
            sprite_atual = str(getattr(store, "sprite_mob_atual", "")).lower()
            nome_atual = str(getattr(store, "nome_mob_atual", "")).lower()
            if "enfermeira" in sprite_atual or "enfermeira" in nome_atual or "clara" in nome_atual:
                mob_slug = "mob_enfermeira"
            elif any(k in sprite_atual or k in nome_atual for k in ["caloura", "veterana", "professora", "aluna", "mulher", "feminina"]):
                mob_slug = "mob_caloura_b"
            else:
                mob_slug = "mob_calouro_a"
        elif "enfermeira" in mob_slug:
            mob_slug = "mob_enfermeira"

        hum = getattr(store, "humanidade", 75)
        fome = getattr(store, "fome_sangue", 100)
        if hum < 35 or fome < 20:
            sufixo = "f3"
        elif hum < 65:
            sufixo = "f2"
        else:
            sufixo = "f1"

        if acao in ("mordida", "suborno"):
            sufixo_acao = "suborno" if ("policial" in mob_slug and acao == "suborno") else "mordida"
            candidatos = [
                f"audio/voice/mobs/{mob_slug}_{sufixo_acao}.ogg",
                f"audio/voice/mobs/{mob_slug}_mordida.ogg",
                f"audio/voice/mobs/{mob_slug}_{sufixo}.ogg",
            ]
        elif acao == "conversa":
            # Pool rotativo de falas conversacionais para evitar repetição
            pool_conversa = [
                f"audio/voice/mobs/{mob_slug}_conversa_1.ogg",
                f"audio/voice/mobs/{mob_slug}_conversa_2.ogg",
            ]
            random.shuffle(pool_conversa)
            candidatos = pool_conversa + [
                f"audio/voice/mobs/{mob_slug}_conversa.ogg",
                f"audio/voice/mobs/{mob_slug}_{sufixo}.ogg",
                f"audio/voice/mobs/{mob_slug}_f1.ogg",
            ]
        else:
            # Abordagem padrão com fallback robusto
            candidatos = [
                f"audio/voice/mobs/{mob_slug}_{sufixo}.ogg",
                f"audio/voice/mobs/{mob_slug}_f1.ogg",
                f"audio/voice/mobs/{mob_slug}_f2.ogg",
                f"audio/voice/mobs/{mob_slug}_f3.ogg",
                f"audio/voice/{mob_slug}_{sufixo}.ogg",
                f"audio/voice/mobs/{mob_slug}_{sufixo}.wav",
            ]

        for cand in candidatos:
            if renpy.loadable(cand):
                renpy.sound.play(cand, channel="barks")
                return True

        return False



    def th_voz(caminho_sem_extensao):

        """

        Reproduz uma linha completa de clímax narrativo no canal 'barks'.

        Aceita o caminho relativo dentro de audio/voice/ ou audio/.

        """

        candidatos = [

            f"audio/voice/{caminho_sem_extensao}.ogg",

            f"audio/{caminho_sem_extensao}.ogg",

            f"audio/voice/{caminho_sem_extensao}.wav"

        ]

        for cand in candidatos:

            if renpy.loadable(cand):

                renpy.sound.play(cand, channel="barks")

                return True

        return False

