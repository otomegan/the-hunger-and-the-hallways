---
name: renpy-intimate-scene-director
description: Expert director for gothic romance, erotic intimacy, and sensory staging in Ren'Py 8.x for The Hunger and the Hallways. Use when scripting ATL camera choreography, rhythmic breathing animations, audio layering (whispers, heartbeats, gasps), intimacy milestones, and dark psychological romance prose.
---

# Ren'Py Intimate Scene Director: The Hunger and the Hallways

This skill establishes the production standard for staging romantic, intimate, and lewd encounters in *The Hunger and the Hallways*, integrating the ATL animations from `game/animacoes_cenas_intimas.rpy` and the sensory sound design principles.

---

## 1. As 4 Fases de Direção de Palco Sensorial

Toda cena íntima importante deve ser orquestrada respeitando a curva dramática de quatro atos:

```
[1. Preliminar] ──> [2. Escalada] ──> [3. Ponto de Impacto] ──> [4. Clímax & Pós-Ato]
  (Respiração)        (Aceleração)         (Estocadas/Mordida)       (Exaustão/Vínculo)
```

### Fase 1: Preliminar / Respiração Lenta
- **ATL:** `cena_lewd_ofegante` (ciclo suave de 4.0s de pulso em escala `1.0` -> `1.02`).
- **Áudio BGM:** `audio/sighs_in_the_dark.ogg` ou `audio/where_the_room_turns_blue.ogg` no canal `music` com `fadein 2.0`.
- **Efeitos SFX:** `th_sfx("heartbeat")` em compasso espaçado.
- **Prose Focus:** Tensão tátil, o contraste da pele fria de Victor contra o calor febril da heroína, o cheiro de suor e sangue nos quartos trancados.

### Fase 2: Escalada do Ritmo / Batimentos Acelerados
- **ATL:** `cena_lewd_ofegante_rapida` (ciclo tenso de 1.8s com leve desvio angular `rotate -0.5` a `0.5`).
- **Áudio SFX:** Sussurros próximos (`th_sfx("sussurros_espelho")` ou voice barks sussurrados da heroína).
- **Prose Focus:** Descompasso respiratório, arrepios, perda de compostura e entrega ao instinto.

### Fase 3: Ponto de Impacto / Estocada & Mordida
- **ATL:** `estocada_impacto` (salto de escala instantâneo em 0.08s com desaceleração elástica e `with hpunch`).
- **Áudio SFX:** Sons de impacto de corpos, arquejo ou suspiro súbito.
- **Dualidade Vampírica:** O momento em que o prazer se confunde com a tentação de afundar as presas na jugular exposta.

### Fase 4: Clímax & Descompressão
- **ATL:** Transição lenta `with dissolve` para fade escuro ou close suave nos olhos.
- **Consequência RPG:** Atualização do Vínculo de Sangue (`vinculo_sangue += 1`), restauração da Sanidade e alívio da Fome.

---

## 2. Biblioteca de Transforms ATL Prontos

Definidos em `game/animacoes_cenas_intimas.rpy`:

```renpy
# Respiração ritmada suave para preliminares
transform cena_lewd_ofegante:
    subpixel True
    linear 2.0 zoom 1.02 yoffset -6
    linear 2.0 zoom 1.00 yoffset 0
    repeat

# Respiração acelerada para o ápice do ato
transform cena_lewd_ofegante_rapida:
    subpixel True
    linear 0.9 zoom 1.035 yoffset -10
    linear 0.9 zoom 1.000 yoffset 0
    repeat

# Estocada de impacto com recuo elástico
transform estocada_impacto:
    subpixel True
    easein 0.08 zoom 1.06 yoffset -15
    easeout 0.25 zoom 1.00 yoffset 0
```

---

## 3. Template de Roteiro e Código

Ao escrever uma cena no script, utilize o seguinte gabarito canônico:

```renpy
label cena_intima_exemplo:
    # 1. Configuração sensorial da cena
    scene black with dissolve
    play music "audio/sighs_in_the_dark.ogg" fadein 2.0
    $ th_sfx("heartbeat")

    "O silêncio do dormitório é quebrado apenas pelo compasso das respirações."
    
    # 2. Entrada da CG com animação de respiração
    scene cg_heroina_toque at cena_lewd_ofegante with dissolve
    
    heroina "Você está demorando demais... Não me faça implorar."

    # 3. Escalada com escolha moral/vampírica
    menu:
        "Entregar-se ao calor humano (Preservar a Máscara)":
            $ status_heroina.afeto += 2
            $ humanidade = min(100, humanidade + 1)
            show cg_heroina_toque at cena_lewd_ofegante_rapida with dissolve
            "Minhas mãos deslizam com cuidado, contendo a força desumana nos nós dos dedos."

        "Beijar o pescoço e roçar as presas na pele (Alimentar o Vínculo)":
            $ status_heroina.vinculo_sangue += 1
            $ status_heroina.afeto += 1
            $ fome_sangue = min(100, fome_sangue + 15)
            show cg_heroina_toque at estocada_impacto
            with hpunch
            "O pulsar da carótida contra meus lábios é uma canção que me arrasta para o abismo."

    # 4. Conclusão
    scene black with fade
    $ notificar_rpg("🔥 VÍNCULO ÍNTIMO", "Laço consolidado. Sanidade restaurada em +20.", "#ff66cc")
    $ sanidade = min(100, sanidade + 20)
    return
```

---

## 4. Diretrizes Literárias Anti-Slop em Cenas Íntimas

1. **Evite Eufemismos Genéricos:** Não use termos como "orbe de paixão", "membro pulsante de desejo" ou metáforas floreadas de IA.
2. **Priorize Sensações Físicas Concretas:** Peso, temperatura, o atrito da pele contra os lençóis de linho áspero da pensão, o gosto metálico de ferro, o tremor dos músculos sob pressão.
3. **Mantenha o Idioleto da Heroína:** Lility permanece sádica e dominante; Elara tenta manter controle racional mesmo quando perde o ar; Emília é vulnerável e hesitante; Valéria trata o momento com cinismo protetor.

