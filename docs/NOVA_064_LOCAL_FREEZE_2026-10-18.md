# NOVA Music Studio — local baseline freeze (2026-10-18)

**State:** OWNER-ACCEPTED LOCAL BASELINE / SOURCE ARCHIVE IN PROGRESS. This branch is a release index, **not** proof that all current Mac source files or private media are backed up on GitHub.

## Baseline
- UI and application: **NOVA 064 Final Creative**, with previous NOVA 062 / 061 retained for rollback.
- Mac CPU generator: **ACE-Step via local service on port 8791**.
- NOVA local gateway: **port 18804**, private Tailscale HTTPS, only while Mac is running.
- Mobile: iPhone Safari and installed web app; Mac: browser-based desktop interface.
- Owner confirmed songs/projects persist and song generation/playback work, subject to Mac/Tailscale availability.
- No external generator, cloud sync or independent always-on hosting in this frozen baseline.

## Explicit non-goals
Do not change approved visual styles, overwrite published GitHub Pages/main, reset Tailscale Serve, clear Safari/PWA IndexedDB, delete existing source archives, or commit private music/secrets/model weights.

## Mac sources to capture, on owner's machine
- `~/Downloads/NOVA_064_FINAL_PRIVATE_STAGE/source_copy` (complete runtime code)
- `~/Downloads/NOVA_064_FINAL_CREATIVE_LAB/` (build manifest)
- `~/Downloads/NOVA_064_FINAL_PRIVATE_STAGE/` (preview manifest / local private results)
- `~/Downloads/NOVA_064_FINAL_CREATIVE_GATE/` (build/release scripts)
- `~/Downloads/NOVA_FINAL_GENERATION_RELEASE_UAKjVLpD/NOVA/` (original launcher and code)
- `~/Downloads/NOVA_019_CPU_ENGINE/` (local model/runtime, keep **local only**)
- iPhone: fresh **FULL BACKUP** exported in Files, outside GitHub (not automatically accessible to Mac).

## Safeguards
- Keep live 18804 and engine 8791 untouched during freeze.
- Do not delete/move original Downloads or Desktop sources before verified second copy and restart on Mac.
- Code-only export is distinct from private music, history, config and model data.
- Before any public-source commit, review export for secrets and personal content. User media/model weights must never be committed.
- Desktop cleanup is **not approved** solely because this document exists.

## Future work (NOT implemented in this freeze)
Lyrics generation, audio editing/stems, cover generation, richer style controls, always-on remote backend / cloud migration, and commercial/licence/security reviews.

## GitHub release scope
This branch starts with a documentation-only checkpoint. The **current NOVA 064 runtime source will be added only after** code-only export from the owner's Mac, verification and review. Existing main/GitHub Pages intentionally remain unchanged.
