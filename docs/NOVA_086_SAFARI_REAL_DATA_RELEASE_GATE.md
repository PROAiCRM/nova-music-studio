# NOVA 086 — actual 085 candidate Safari + release gate (2026-10-19)

**STATUS: LOCAL TOOL PASS; MAC SAFARI/INDEXEDDB NOT YET VERIFIED; SAFE_TO_DEPLOY=NO.**

## Owner Mac result: NOVA 085 staging succeeded
- Original NOVA 082 source pin **52/52**; output NOVA 085 candidate **55/55**.
- Owner Terminal: `NOVA085_DECISION=ISOLATED_CANDIDATE_STAGED_RELEASE_BLOCKED`, 10 new+31 existing tests PASS, `LIVE_MUTATION=ZERO`, `GEN_POST=ZERO`, `USER_MEDIA_READ=ZERO`, `TAILSCALE_MUTATION=ZERO`.
- Candidate at `~/AION_PROJECTS/NOVA_085_COMMERCIAL_HARDENING/candidate`; not deployed to 18804 or iPhone.

## New 086 tool
Local downloadable file `NOVA_086_SAFARI_RELEASE_GATE.zip` SHA256 `05b4017686a9dd059d4d9d54e4dc689ad85dc4b95f62e098c3aaf57400655693`. Manifest **7 SHA-256** files verified; clean ZIP extraction and CRC PASS; **8 unit/safety tests PASS**. Test coverage: pin tamper, unauthorized stage, root symlink, blocked API GET/POST/PUT/PATCH/DELETE, no source leakage, PNG 180/192/512 assets, JS syntax and no cross-origin destructive APIs.

Tool targets **exactly current NOVA 085**: independently SHA-verifies all 55 expected owner-Mac files and requires staged owner report with `safe_to_deploy=false`. Starts a separate GET-only 127.0.0.1 ephemeral origin for Safari. Injects a one-time test JS into an HTTP response, **never changes any 085 file**. Browser test (Mac Safari, not yet run) uses only synthetic idea/lyrics and a synthetic IndexedDB draft on this fresh origin, then reloads and verifies persistence. It shows PASS/BLOCKED and allows copying local JSON; NO POST or proxy to engine/gateway, never touches installed iPhone PWA or Tailscale.

User Mac run:
```bash
cd "$HOME/Downloads" && unzip -n NOVA_086_SAFARI_RELEASE_GATE.zip && bash "$HOME/Downloads/NOVA_086_SAFARI_RELEASE_GATE/RUN_086_MAC_SAFARI.command"
```
Open automatically in Safari; if blocked, manually open `NOVA086_SAFE_URL`; owner copies overlaid JSON result; stop only this preview with Ctrl+C.

**Caveat:** Assistant's headless Chromium `page.goto(http://127.0.0.1/...)` hit `ERR_BLOCKED_BY_ADMINISTRATOR`; a real-browser runtime PASS **is not claimed**, nor is physical Safari/iPhone QA.

## Confirmed source-level release blockers (do not silently fix with risky deploy)
1. `sw.js` in 085 still has `CACHE='nova-r64-final-creative-v1'` with cache-first shell. Must implement a versioned PWA update and rollback using synthetic music before switching a real iPhone; **no IndexedDB.clear/delete / SW reset**.
2. `local_server.py` exposes GET `/api/nova/local/jobs`, `/job?id`, `/audio?id` without a user session or per-job ownership check. Host/Origin checks plus a private Tailnet **are not a multi-tenant auth substitute**. Do not publish a multi-user API until sessions, authorization and tenancy isolation are verified.
3. `MAX_HISTORY=60` prevents adding new generation jobs once history fills; no auto-delete policy should be implemented without a reversible archive.
4. Mac and iPhone PWA browser IndexedDB are distinct; the verified local Mac snapshot does not back up standalone installed iPhone records. Require owner-made FULL BACKUP and off-device restore proof.
5. First real NOVA 076 WAV proves local ACE-Step inference but **not the human-rated quality of Russian vocals** or complete commercial song structure. 4B LM/stronger DiT not tested.
6. Licensing, privacy, subscriptions/billing and sustained server operation remain unresolved.

**NOVA 085 remains staged-only.** All code/QA work stays separate from approved visual design, user media, GitHub public main and current Tailscale Serve. No private tracks or model weights committed to public GitHub.
