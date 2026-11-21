---
name: renpy-world-of-horror-rpg
description: Expert survival horror RPG architect for Ren'Py 8.x in The Hunger and the Hallways. Use when scripting Ruína de Cain (Doom clock 0-100%), modular mysteries (MisterioCaso), Clues gathering, Climax anomalies, Daily Weather (clima_diario_id), Vitality / Sanity / Blood Thirst thresholds, and tactical map investigation economy.
---

# Ren'Py World of Horror RPG Mechanics: The Hunger and the Hallways

This skill governs the survival horror RPG loop of *The Hunger and the Hallways*, inspired by Paweł Koźmiński's *World of Horror* (panstasz), integrating the systems in `game/sistemas_world_of_horror.rpy`, `game/calendario.rpy`, and `game/custom_screens.rpy`.

---

## 1. Core Survival Stats & Thresholds

Victor's survival state is governed by four interdependent psychological and biological meters:

| Atributo | Variável Store | Faixa | Efeito Crítico |
|---|---|---|---|
| **Ruína de Cain (Doom)** | `store.ruina_cain` | 0 – 100% | Em 25%, 50% e 75% surgem anomalias no mapa. Em 100% ocorre o *Apocalipse de Cain* (Game Over). |
| **Fome de Sangue (Thirst)**| `store.fome_sangue` | 0 – 100% | < 25%: Fome extrema, alucinações visuais e perda de controle. 100%: Saciedade predatória (+Bônus em Combate). |
| **Razão / Sanidade** | `store.sanidade` | 0 – 100 | Em 0: Surto psicótico vampírico, falha em testes de dedução e bloqueio de escolhas racionais. |
| **Vitalidade (HP)** | `store.hp_jogador` | 0 – 100 | Em 0: Morte física ou captura pela Ronda Noturna / Grêmio. |

### Regras de Ouro de Sobrevivência
1. **Passagem do Tempo:** Cada investigação de local ou evento gasta 1 período (`avancar_periodo()`), escalando a Ruína (`ruina_cain += 1` ou `+2` se houver anomalia ativa).
2. **Drenagem Diária:** No fim da noite, a pensão e o metabolismo de Victor exigem sangue (`fome_sangue -= 15`). Se a fome cair abaixo de 20%, ele é obrigado a caçar ou drenar heroínas/mobs.
3. **Notificação HUD:** Sempre use `notificar_rpg(titulo, mensagem, cor)` para comunicar alterações ao jogador na tela.

---

## 2. Arquitetura Modular de Mistérios (`MisterioCaso`)

Os 5 Grandes Mistérios da Academia São Cipriano são instanciados no dicionário `MISTERIOS_ACADEMIA`:

```python
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
```

### Casos Registrados
1. `"hachishaku"`: *A Mulher de Oito Pés* (Local: `cemiterio_nevoa` | 3 Pistas | Clímax: `evento_hachishaku_anomalia`)
2. `"loira_banheiro"`: *O Espelho da Dama do Banheiro* (Local: `banheiro_abandonado` | 3 Pistas | Clímax: Confronto no Espelho)
3. `"lote_necrotico"`: *O Lote Necrótico Clandestino* (Local: `sala_caldeiras` | 3 Pistas | Clímax: `evento_lote_necrotico_anomalia`)
4. `"quadro_banquete"`: *O Banquete Dentro da Moldura* (Local: `biblioteca` | 3 Pistas | Clímax: Destruição com Ácido)
5. `"sociedade_gargula"`: *O Pacto dos Telhados* (Local: `portoes_praca` / `salao_gremio` | 3 Pistas)

### Como Scriptar a Coleta de Pistas
```renpy
# Exemplo de investigação com teste de atributo e coleta de pista
menu:
    "🔍 Examinar os registros de internação da enfermaria":
        if intelecto >= 3:
            $ MISTERIOS_ACADEMIA["lote_necrotico"].coletar_pista("Planilha com nomes de calouros anêmicos")
            "Encontro uma lista com carimbo falso do Grêmio..."
        else:
            $ ruina_cain += 2
            $ notificar_rpg("⚠️ TEMPO PERDIDO", "Você não entendeu os códigos químicos. (+2% Ruína)", "#ff4444")
            "As anotações parecem grego... Perdi minutos preciosos."
```

---

## 3. Clima Diário & Presságios (`clima_diario_id`)

A cada novo dia, `sortear_clima_diario()` define o presságio atmosférico que afeta gameplay, paciência das heroínas e estética visual:

| ID Clima | Nome | Efeito Mecânico | Cenários Visuais |
|---|---|---|---|
| `"chuva_vitrais"` | *Chuva Fria nos Vitrais* | +1 Paciência inicial em todas as heroínas. Áudio `sfx_chuva_ambiente.ogg` nos cenários abertos. | `bg animado ... chuva` |
| `"nevoa_carmesim"` | *Névoa Carmesim Tóxica* | +25% Dano de todos os inimigos em combate; +2% Ruína de Cain automática. | `bg animado ... nevoeiro noite` |
| `"vento_uivante"` | *Vento Uivante nas Torres* | -1 Paciência em Lility e Elara (nervosismo); sussurros no banheiro. | `bg animado ... entardecer sol` |
| `"lua_sangue"` | *Lua de Sangue do Eclipse* | Custo de habilidades vampíricas reduzido em 50%; Fome sobe mais rápido. | `bg animado ... orb vermelha` |

---

## 4. Integração com o Mapa Tático & Exploração

O mapa tático (`mapa_tatico_escola` em `custom_screens.rpy`) deve sempre refletir:
1. **Ícones de Investigação:** Casos com pistas ativas exibem `🔍` sobre o pin do local.
2. **Ícones de Clímax:** Quando `pistas_coletadas >= pistas_totais`, o pin pisca em vermelho `⚔️ CLÍMAX`.
3. **Sons Atmosféricos:** Ao abrir o mapa, o som do ambiente local pausa e toca `sfx_mapa_ambiente_noturno.ogg`; ao retornar à cena, o som atmosférico específico da sala é restaurado com fade suave de 2.0s.

