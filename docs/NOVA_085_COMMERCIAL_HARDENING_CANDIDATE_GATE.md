# NOVA 085 — Commercial hardening, isolated functional candidate (2026-10-19)

**Status:** PRIVATE CANDIDATE BUILT & CLEAN-ROOM VERIFIED · Mac owner stage NOT YET RUN · LIVE NOVA 064 UNCHANGED · COMMERCIAL RELEASE BLOCKED.

## Actual baseline and scope

Based on the owner's code-only 064 export (52 SHA-verified source files) and the Mac-staged NOVA 082 candidate (52 SHA-verified source files), whose safe stage and NOVA083 QA were confirmed on the owner's Mac. The protected NOVA082 artistic interface and styling are frozen. No change to installed media, Mac inference service, IndexedDB, PWA service worker, Tailscale or GitHub main.

## New engineering fixes actually authored and validated

1. Browser title, metadata and footer: remove old internal NUMERA/NOVA version references; maintain original 082 CSS byte-for-byte.
2. iOS/desktop identity: resize the **previously generated NOVA icon** into genuine PNG 180/192/512; update Apple touch icon, webmanifest and local server's exact static-asset whitelist. This is a candidate icon asset, not a deployed iPhone icon.
3. Privacy minimization: GET /api/nova/local/jobs and /job now use a strict public_job() whitelist, never exposing internal idempotency_key, request_sha256, or future fields accidentally. This is **not authentication or authorization**.
4. Persistence reliability: journal writes use unpredictable exclusive temp files mode 0600, explicit flush+fsync and os.replace, plus best-effort directory fsync. Test injects a failed replace and verifies old journal bytes survive unchanged.
5. Explainable lyrics: Producer Director preview warns in Russian when a text is too syllable-dense, a chorus/outro is unmarked, or 15/30sec is only an excerpt. No user lyrics mutation, generation parameter mutation or auto-submit.

**Changed from 082:** app/index.html, local_server.py, nova-local.js, manifest.webmanifest, tests/test_local.py; new icons nova-180.png, nova-192.png, nova-512.png (8 entries changed/added). All remaining original source files stay unchanged, including the proven engine file local_engine.py and the existing sw.js and IndexedDB routines.

## Verifications

- Source delta: 52 original pinned files, 55 candidate files, exactly eight altered/new paths.
- 31/31 existing Python engine/gateway tests PASS, including origin policy, HTTPS origin, idempotency, MP3 SHA, reset safety and mocked engine results.
- 10/10 new reliability/privacy/icon/visual styling tests PASS; 2/2 synthetic stage/no-overwrite tests PASS.
- Chromium static DOM visual smoke on 320, 390, 768, 1440 px: no horizontal overflow; Home/Create present; separate lyrics and Creative Studio present. Exact 082 CSS block hash unchanged. **This is about:blank and IndexedDB denied, NOT real Safari/iPhone acceptance.**
- JavaScript syntax, Python syntax, whole ZIP SHA+CRC, and complete tests from a clean extraction PASS.
- Private downloadable package: NOVA_085_COMMERCIAL_HARDENING.zip, SHA256 `a03d1415938a203ed81573209605df3ed73d9e967293509168926c9b386ebea0` (70 ZIP entries, 69 content-manifest files).

## Mac owner command — safe stage, never deploy

```bash
cd "$HOME/Downloads" && unzip -n NOVA_085_COMMERCIAL_HARDENING.zip && bash "$HOME/Downloads/NOVA_085_COMMERCIAL_HARDENING/RUN_085_SAFE_STAGE.command"
```

The runner verifies 69 package files; executes 10 new and 31 existing offline tests; verifies the owner's 52 source files in `~/AION_PROJECTS/NOVA_082_PRODUCT_CANDIDATE/candidate`, then copies only 55 SHA-pinned candidate files to `~/AION_PROJECTS/NOVA_085_COMMERCIAL_HARDENING/candidate`. Never writes to source or live. A second run refuses to overwrite. Expected `NOVA085_DECISION=ISOLATED_CANDIDATE_STAGED_RELEASE_BLOCKED`.

## Commercial blockers (explicitly NOT solved by 085)

- Auth/session isolation and real tenant/RLS policies for multiple customers. A single owner Tailnet web server with a publishable Supabase client config cannot be announced as public-safe.
- Physical iPhone Safari and standalone PWA gates, backup and restore of full music library (iPhone and Mac storage origins are independent).
- Safe versioned SW asset upgrade and rollback without deleting IndexedDB.
- Improved music model quality. First real WAV from NOVA076 proved LM→synth works with 0.6B Q8 LM and Turbo Q4 DiT, **not commercial-quality vocals**. Need controlled 4B / higher-precision/SFT comparisons and blind human listening.
- Music copyright/licensing, user consent, payments, support, external remote hosting and performance testing.

**NO_RELEASE / NO_LIVE_SWITCH.** Detailed local Russian reports included inside the package: RELEASE_GATES_085.md, VISUAL_AUDIT_085.md and README_FIRST.md. No private music, model weights, owner personal project files, Supabase configuration or full code published to this public GitHub branch.
