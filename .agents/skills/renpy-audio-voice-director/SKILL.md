---
name: renpy-audio-voice-director
description: Expert game sound design and voice direction skill for Ren'Py. Covers OGG Vorbis mastering, voice barks integration, audio channels, SFX spatial acoustics, Gemini TTS generation, and local neural voice fallback.
---

# Ren'Py Audio & Voice Director Skill

Comprehensive audio engineering and sound design guidelines tailored for *The Hunger and the Hallways*.

## 1. Technical Audio Mastering Standard (OGG Vorbis)

All game audio assets (voice barks, SFX, atmospheres, and dialogue) MUST comply with:
- **Format:** `.ogg` (Vorbis).
- **Sampling Rate:** `44100 Hz` (44.1 kHz).
- **Channels:** `2 Channels (Stereo)`.
- **Quality / Bitrate:** Vorbis Quality `6` (`-q:a 6`, ~192 kbps).
- **Peak Normalization:** Normalized to `-1.5 dBFS` to prevent digital clipping across speakers and headphones.
- **Envelopes:** Smooth `12ms - 30ms` fade-in and fade-out to prevent pop/click transients at the start or end.
- **Tail Hiss Removal:** Always trim post-speech vocoder noise bursts (especially the last ~130ms in AI TTS generation) before normalization.

### FFmpeg Standard Conversion Command:
```bash
ffmpeg -y -i input.wav -af "afade=t=in:ss=0:d=0.015,areverse,afade=t=in:ss=0:d=0.03,areverse,volume=1.35,loudnorm=I=-16:TP=-1.5:LRA=11" -ar 44100 -ac 2 -c:a libvorbis -q:a 6 output.ogg
```

## 2. Ren'Py Audio Channel Architecture

- **Voice Barks:** ALWAYS play on dedicated `channel="barks"`.
  - ⚠️ **CRITICAL:** NEVER play voice barks on `channel="voice"` before dialogue statements (`say`), because Ren'Py automatically stops the native voice channel when rendering a new dialogue text box!
- **Sound Effects (SFX):** Play on `channel="sound"` via `th_sfx("nome")` or `play sound "audio/arquivo.ogg"`.
- **Music (OST):** Play on `channel="music"` via `play music "audio/faixa.ogg" fadein 1.5`.
  - ⚠️ **RULE:** Never delete or overwrite any of the 40 OST music tracks in `game/audio/`.

## 3. Voice Generation & Fallback Hierarchy

Follow the project's permanent voice rotation system:
1. **Gemini TTS Online:**
   - Primary Key: Configured in environment / GEMINI.md
   - Secondary Key: Configured in environment / GEMINI.md
   - Models: `gemini-3.8-flash-tts` -> `gemini-3.8-flash-lite-tts` -> `gemini-3.1-flash-tts-preview`
2. **Local Neural Fallback (Offline & Zero Cost):**
   - Kokoro ONNX (`scratch/kokoro/`) or Edge-TTS.
   - Voice Casting:
     - **Lility:** `Kore` / `af_bella`
     - **Elara:** `Aoede` / `af_sarah`
     - **Emília:** `Leda` / `af_nicole`
     - **Valéria:** `Zephyr` / `af_sky`
     - **Victor:** `Algieba` / `am_michael`
     - **Diretor:** `en-US-RogerNeural` (Edge-TTS)
     - **Policiais:** `en-US-GuyNeural` (Edge-TTS)

## 4. Organic Foley vs Descriptive Speech Rule

When creating creature, monster, animal, or environmental sounds:
- Never feed descriptive sound directions into TTS models without verifying the output, as TTS will speak the words aloud.
- Use authentic biological/foley recordings (e.g. real canine growls for Hellhounds, real shoe strikes on marble, real boiling steam for boilers) rather than synthetic approximations.

