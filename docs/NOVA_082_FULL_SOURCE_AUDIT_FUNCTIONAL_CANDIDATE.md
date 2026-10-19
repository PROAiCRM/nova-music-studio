# NOVA 082 — actual NOVA 064 code review and functional candidate

**Status: private staged-code ZIP built and clean-room verified, owner Mac stage NOT YET EXECUTED. LIVE NOVA 064 unchanged. Commercial/music/Safari release BLOCKED.**

## Source provenance
The owner uploaded the actual 2026-10-18 code-only archive NOVA_064_CODE_ONLY_FOR_GITHUB_20261018.zip (54 ZIP entries: 52 source files plus original source SHA manifest and README). All 52 source hashes matched the uploaded manifest. This is code-only, not live Mac data, song library, model weights or result folders.

## Findings (confirmed from complete source, not assumptions)
1. Creative Studio 064 had only a capture-phase click guard when directive applied. Core `async function prepare()` lacked a length guard and `songCaption()` trimmed idea at 350; programmatic/other entry paths could persist silently truncated ideas.
2. A single localStorage `nova064.creative.original-genre` key was not draft-scoped. Undo could retrieve an unrelated earlier original genre across edits/reloads.
3. The 034 Producer Director silently used `idea.slice(0,420)` even after the project was prepared, risking loss of context between Create and Generate.
4. Create saved `lyrics:trim(f.lyrics,7500)` although native model/UI request limits are 8000; title saved at 80 although input maxlength is 85.
5. Hip-Hop and Synthwave were absent from the Producer Director mapping; both defaulted to Pop.
6. **Correction to earlier assumptions:** original NOVA 064 ALREADY has a separate lyrics input, saves project lyrics in IndexedDB, opens a separate generation lyrics field, sends lyrics via Producer Director request and local_engine.py to ACE-Step C++. The feature requires end-to-end validation and quality tuning, **not a new architecture from scratch**.
7. Source contains actual Supabase *publishable* configuration and private Tailscale hostname. The publishable key is not a service-role secret, but this public repository requires privacy/permissions review; **DO NOT publish unfiltered complete owner source**. The user WAV, projects, GGUF, private results and tokens are not included.

## Implemented NOVA 082 code-only candidate — three files
- `app/index.html`: fail-closed exact idea >350 guard inside actual prepare() before saving; retains secondary click guard; no silent trim in songCaption; validates lyrics >8000 and preserves up to 8000; title 85; safe draft-bound Creative Studio undo (exact original/applied idea, title and applied genre) with old unscoped key ignored and not deleted.
- `nova-local.js`: correct Hip-Hop/Synthwave genre mapping only.
- `nova034-producer.js`: no silent 420-character description clipping; explicit fail-closed bound on final LM prompt; dedicated hiphop and synthwave directions.

All other 49 source files (including `local_server.py`, `local_engine.py`, `sw.js`, `nova-pwa.js`, manifest and user storage code) byte-identical to exported baseline. All original CSS blocks unchanged, no redesign.

## Verification evidence
- 15/15 new actual JS VM unit tests PASS: Prepare 350/351 and zero IDB write on reject; genre apply/undo after mock reload; draft isolation; original legacy storage not read/deleted; separate lyrics payload; Hip-Hop/Synthwave; unchanged CSS/cache/backend.
- 39/39 selected existing Python local engine/gateway unit tests PASS.
- Existing Node tests for Producer Director 034, Nova Guard 032 and cover artwork PASS.
- 52-source-file SHA match; 113-file package manifest; clean ZIP unpack and independent manifest check PASS.
- Synthetic owner-Mac staging performed under temporary HOME with pinned copied originals: STAGE PASS; second stage correctly rejected `CANDIDATE_DEST_ALREADY_EXISTS_NO_OVERWRITE`.
- Isolated HTTP server returns GET for static assets and **no POST**; intended localhost port 18982, separate blank origin/storage.
- Browser Chromium navigation **BLOCKED_BY_ADMINISTRATOR** in current tool environment; no real Mac Safari or physical iPhone testing done.
- Original historical global test suite had **7 errors** because some launcher commands were deliberately absent from the code-only export and **2 failures** checking an old worker-cache version. Those baseline errors were not corrected by changing the app code or misreported as passing.

Private user-download artifact: NOVA_082_PRODUCT_CANDIDATE.zip, verified SHA256 `1fda46cb254a7681bca2fc9fd72300abfb6fc4181792ee1bbebc39efa16e6984`. It is NOT published in full on this public GitHub branch.

## Mac owner next step (safe, code only)
```bash
cd "$HOME/Downloads" && unzip -n NOVA_082_PRODUCT_CANDIDATE.zip && bash "$HOME/Downloads/NOVA_082_PRODUCT_CANDIDATE/RUN_082_SAFE_STAGE.command"
```
Only if original `~/AION_PROJECTS/NOVA_064_LOCK_20261018/local/runtime_source` exactly matches the exported 52 hashes, this stages an isolated non-running candidate under `~/AION_PROJECTS/NOVA_082_PRODUCT_CANDIDATE/candidate` and writes `NOVA_082_STAGE_REPORT.json`. Never writes to live 8791/18804, iPhone/Safari IndexedDB, Tailscale Serve or user MP3.

Optional static preview: `OPEN_082_ISOLATED_PREVIEW.command` opens GET-only local origin 127.0.0.1:18982 and cannot submit generation.

**SAFE_TO_DEPLOY=NO.** Owner Mac browser QA, native request validation and true iPhone history/backup preservation + SW upgrade remain mandatory. Real commercial vocal quality not achieved yet.
