# NOVA 071 — Audio Quality Lab (2026-10-18)

## Purpose and status

A separate, local, **unreleased** ACE-Step C++ audio-quality experiment. It does not change the owner-approved NOVA 064 desktop/iPhone UI, Safari/PWA storage, installed WAV/MP3, live gateway `18804`, private Tailscale Serve, or CPU engine `8791`.

**The generator/model weights have NOT yet been modified. A “WOW” vocal result is NOT claimed.** Actual audio must be synthesized and listened to on the owner's Mac before any NOVA integration.

## Concrete completed work

A downloadable local tool package `NOVA_071_AUDIO_QUALITY_LAB.zip` was generated and locally verified. It contains:
- a read-only audit that checks `/health`, native ACE-Step `/props` and legacy `/v1/models`, plus GGUF model filenames in the dedicated existing `NOVA_019_CPU_ENGINE` folder (no model download);
- three immutable test requests: A (automatic lyrics), B (explicit Russian Verse/Chorus lyrics), C (same lyrics with lower LM temperature);
- genre/instrument description separated from the sung Russian words in distinct `caption` and `lyrics` fields, explicit `vocal_language=ru`, 30-second target, fixed seed, WAV16 output, serial batch size 1;
- Turbo parameter profile `8 steps / shift 3 / guidance 1`, separate Base/SFT `50 steps / shift 1 / guidance 1`, applied only when a compatible variant is inventoried;
- a separately owner-approved single-job native `/lm` → `/synth` WAV audition with run-once idempotency, no automatic job retry, no private song access or upload, and fail-closed backend identity checks;
- an offline file-picker listening/scorecard page and basic PCM WAV sample rate/peak/RMS/clipping checks.

**Validation:** 29 unit/integration tests PASS with synthetic engine responses; package SHA-256 and ZIP integrity PASS; Python/Bash/JS syntax checks PASS. **Not tested:** real ACE-Step inference on Mac, audible Russian lyric clarity, model variant capability, audio improvement.

## Next owner gate

On the Mac, first run `NOVA_071_AUDIO_QUALITY_LAB/RUN_071_AUDIT.command` and inspect `~/AION_PROJECTS/NOVA_071_AUDIO_QUALITY_LAB/QUALITY_AUDIT_071.json`. The command makes only local GET calls and creates local report/test requests.

If the native `/props` API is confirmed with available LM/DiT models, the owner may run the **separate manually confirmed** single profile B audition using `RUN_071_AUDITION_OWNER_ONLY.command` when NOVA is idle. On a legacy backend, no POST is permitted and integration must be adapted to the actual source API.

After genuine audio and owner evaluation, review Mac-only `local_server.py` source before considering a pinned, reversible isolated candidate. No live route switch without separate owner approval.

## Tech documentation used
- [ACE-Step C++ ARCHITECTURE](https://github.com/ServeurpersoCom/acestep.cpp/blob/master/docs/ARCHITECTURE.md)
- [ACE-Step 1.5 inference](https://ace-step.github.io/ACE-Step-1.5/en/INFERENCE)

## Privacy
Source code and QA metadata only are appropriate for GitHub after review. No GGUF weights, songs, model downloads, personal prompts, tokens or user results are part of this commit.
