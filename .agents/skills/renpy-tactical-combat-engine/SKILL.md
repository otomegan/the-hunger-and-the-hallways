---
name: renpy-tactical-combat-engine
description: Turn-based horror combat designer and balance engineer for Ren'Py 8.x in The Hunger and the Hallways. Use when scripting enemy encounters, QTE reaction timers, Persona-style surrender/drain finishers, vampire skills, damage formulas, and battle sound effects.
---

# Ren'Py Tactical Combat Engine: The Hunger and the Hallways

This skill governs the turn-based horror combat and feeding system of *The Hunger and the Hallways*, implemented in `game/combate.rpy`.

---

## 1. Estrutura Padrão de Batalha (`label iniciar_combate`)

Todo combate é iniciado através de uma única assinatura universal com validações automáticas de sprites, som e QTE:

```renpy
call iniciar_combate(
    nome="Alquimista Renegado",
    sprite_base="inimigo fundao alquimista frasco verde arma",
    sprite_atk="inimigo fundao alquimista frasco verde ataque",
    hp_max=80,
    dano=18,
    tempo=7.0,                 # Tempo em segundos do timer QTE
    tipo_sangue="alquimico",   # "gremio", "alquimico", "monstro", "corrompido"
    historia_continua=False,   # Se True, derrota não causa Game Over, retorna flag
    pode_fugir=True            # Se False, botão de recuo fica desabilitado
)
```

### Protocolo de Limpeza Visual
Ao iniciar combate, o motor oculta automaticamente todos os sprites de personagens de diálogos anteriores (`nora`, `inimigo`, `fada`, `elara`, `cain`, `victor`, etc.) para evitar poluição visual na arena.

---

## 2. Ações do Jogador & Equilíbrio de Fome

O menu de turno (`loop_turno_combate`) disponibiliza ações que balanceiam consumo de Fome de Sangue, Coragem e Itens:

| Ação | Custo | Fórmula de Dano | Efeito Tático |
|---|---|---|---|
| **🗡️ Ataque Rápido** | Sem Custo | `max(20, base_atk + coragem*2 + intelecto + buff)` | Golpe veloz básico. Não consome recursos. |
| **🩸 Garras de Sangue** | -15 Fome | `45 + ressonancia*4 + dominio*3 + buff` | Dilaceração predatória pesada. +20 Dano extra se Fome < 50% (*Garras Sedentas*). |
| **⚡ Dispositivo Choque** | 1x Item | 30 Dano Fixo | Atordoa o inimigo, cancelando o próximo contra-ataque. |
| **💉 Dose Estimulante** | 1x Item | 0 Dano | Concede +4.0s no timer de reação QTE e 50% de chance de esquiva. |
| **🏃 Tentar Recuar** | -10 Sanidade | 0 Dano | Fuga desesperada. Requer `combate_pode_fugir == True`. |

---

## 3. Mecânica do Timer QTE (`tempo_reacao`)

1. A tela `hud_combate_zona_vermelha` possui um `timer tempo_reacao action Jump("inimigo_ataca_por_tempo")`.
2. Se o jogador hesitar e o timer expirar:
   - O inimigo desfere um ataque de oportunidade gratuito com `with vpunch`.
   - Victor perde HP e o turno é reiniciado com pressão psicológica.
3. Se o item **Dose Estimulante** estiver ativo, o tempo de reação recebe `+4.0s` extras com aviso na tela.

---

## 4. Finalizadores Críticos Estilo Persona (`executar_golpe_critico_persona`)

Quando o HP do inimigo chega a zero (`hp_inimigo <= 0`), o combate entra no estado de Rendição:

```renpy
menu:
    "🩸 DRENAR ATÉ A ÚLTIMA GOTA (Execução Predatória / Saciedade Total)":
        # Restaura +40 Fome, mas reduz -5 Humanidade e aumenta +3 Ruína
        $ fome_sangue = min(100, fome_sangue + 40)
        $ humanidade = max(0, humanidade - 5)
        $ ruina_cain += 3
        play sound "audio/hellhound_rosnar.ogg"
        with vpunch
        "Seus dentes cravam fundo... O calor da artéria esvazia o corpo até virar casca seca."

    "💉 EXTRAÇÃO CIRÚRGICA (Dose Moderada / Poupar Vida)":
        # Restaura +20 Fome, obtém 1x Frasco de Sangue e preserva Humanidade
        $ fome_sangue = min(100, fome_sangue + 20)
        $ frascos_sangue += 1
        "Você drena o suficiente para acalmar a fera sem cruzar a linha da matança."

    "🔍 INTERROGAR (Exigir Pistas e Alavancagens)":
        # Se for membro do Grêmio ou Fundão, concede pistas para os mistérios
        $ MISTERIOS_ACADEMIA[caso_ativo].coletar_pista("Confissão sob coerção do inimigo")
```

---

## 5. Regras de Som e ATL em Combate

1. **Trilha BGM:** Sempre use `audio/steel_loop.ogg` ou `audio/Authority_Breach.ogg` no canal `music` com `fadein 1.0`.
2. **Impactos:** Use `play sound "audio/blade_slash_heavy.ogg"` com `with hpunch` em ataques com lâmina, e `with vpunch` em ataques de garras ou monstros.
3. **Voice Barks de Inimigos:** Dispare `th_bark_inimigo(nome_inimigo, "dor")` quando o inimigo for ferido, mantendo o feedback de áudio imersivo.

