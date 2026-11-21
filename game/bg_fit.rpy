# ==============================================================================
# BG_FIT.RPY — AJUSTE AUTOMÁTICO DE FUNDOS ESTÁTICOS (2K -> TELA DO JOGO)
# ==============================================================================
# O jogo roda em 1920x1080 (gui.init). Imagens 2K (2560x1440) eram desenhadas em
# tamanho real a partir do canto superior esquerdo, então pareciam "com zoom".
# Aqui cada fundo estático é registrado já escalado para preencher a tela
# (fit "cover": mantém proporção e corta o excesso, sem distorcer).
# Vale para arquivos cujo nome começa com "bg " ou "mapa " ou que estejam numa
# pasta com "wallpapers" no caminho. Vídeos (.webm) já usam Movie(size=...) em
# definitions.rpy. Sprites não são afetados.
# ==============================================================================
init 1 python:
    import os as _os
    _EXT_IMG = (".webp", ".png", ".jpg", ".jpeg")
    for _caminho in renpy.list_files():
        _baixo = _caminho.lower()
        if not _baixo.startswith("images/") or not _baixo.endswith(_EXT_IMG):
            continue
        _base = _os.path.splitext(_os.path.basename(_caminho))[0]
        _eh_fundo = _base.lower().startswith(("bg ", "mapa ", "cena ")) or "wallpapers" in _baixo or "cenas" in _baixo
        if not _eh_fundo or "motions" in _baixo:
            continue
        renpy.image(
            tuple(_base.split()),
            Transform(_caminho, xysize=(config.screen_width, config.screen_height), fit="cover"),
        )
