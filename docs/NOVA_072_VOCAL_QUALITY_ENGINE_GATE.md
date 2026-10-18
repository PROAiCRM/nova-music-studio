# NOVA 072 — Vocal Quality Engine, isolated quality gate (2026-10-18)

**Status: BUILT_AND_STATIC_TESTED / REAL_MAC_INFERENCE_PENDING / COMMERCIAL_AUDIO_GATE=BLOCKED.**

New local archive: `NOVA_072_VOCAL_QUALITY_ENGINE.zip`. Its SHA-256 at creation: `1f31c26236099ffc8298d916cb0937d237770d405f6bf1a98acfad2550b7c5d4`. It is a stand-alone owner Mac test tool, not a public deployment or overwrite of NOVA 064.

## Substantive fixes after NOVA 071
- On automatic-lyrics profile A, **preserve lyrics returned by ACE-Step LM** when handing LM audio codes to the synthesizer; block if the generated lyrics are empty.
- On explicit-Russian-lyrics profiles B/C, **verify the LM returned exactly the supplied Russian verses and chorus**, block synthesis if text drifted to avoid pairing LM audio codes with mismatched lyrics.
- B and C use identical parameters except LM size, B largest installed LM and C smallest installed LM; block C if only one LM tier exists. A (automatically generated lyrics) uses same LM tier as B.
- Extend native /synth JSON size guard from 256 KB to 16 MB with LM audio codes, keep loopback-only and user-confirmed POST routes. /lm limit remains 256KB; no automatic retry.
- Native /props and GGUF inventory; local Russian lyrics workbench and separate subjective WAV listening scorecard; read-only WAV SHA/PCM validation.
- **41 automated integration/unit tests PASS**, independent clean-room audit without engine correctly blocked audition, live route unchanged; ZIP and SHA verified.
- **NOT TESTED** real ACE-Step inference, natural Russian words, perceptual vocals, latency on owner's Intel Mac or installed iPhone.
- Official ACE-Step 1.5 model card identifies MIT and commercial permission. Still check exact distributed weights, dependencies, copyright, security and business rights before commercial publication.

## Next owner step
Download into Mac Downloads, then:
```bash
cd "$HOME/Downloads" && unzip -n NOVA_072_VOCAL_QUALITY_ENGINE.zip && bash "$HOME/Downloads/NOVA_072_VOCAL_QUALITY_ENGINE/RUN_072_AUDIT.command"
```
Result path `~/AION_PROJECTS/NOVA_072_VOCAL_QUALITY_ENGINE/QUALITY_AUDIT_072.json`. This GET-only preflight is safe for live environment. Do not run any real quality test unless native engine /props confirms models and NOVA currently idle. Subsequent WAV B trial needs separate typed authorization and may take a long time on Mac.

No user tracks, models, tokens, macOS keychain, iPhone IndexedDB, LIVE 18804 gateway, engine 8791, or Tailscale state are written by the audit. The original NOVA 064 code-only export still needs owner upload and source review; NOVA 064 commercial gate is not passed.
