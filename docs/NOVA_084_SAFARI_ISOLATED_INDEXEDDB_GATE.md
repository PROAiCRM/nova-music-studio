# NOVA 084 — real Safari + IndexedDB isolated acceptance gate

**Status (2026-10-19):** owner Mac NOVA 083 PASS, new NOVA 084 selftest packaged, clean extract and 8 tool-unit tests PASS. **True Safari pass still pending.** Live NOVA 064 and private music data remain intact; commercial quality is not accepted.

## Mac owner NOVA 083 result
```text
NOVA083_PACKAGE_SHA_PASS files=5
NOVA083_STAGE_MANIFEST=PASS files=52 changed=3
NOVA083_REAL_JS_HANDLER_TESTS=PASS count=15
NOVA083_LOCAL_HTTP_SANDBOX=PASS checks=14
NOVA083_DECISION=STAGED_SOURCE_JS_AND_HTTP_SAFE_PASS_SAFARI_DEVICE_GATES_PENDING
LIVE_MUTATION=ZERO GENERATION_POST=ZERO USER_MEDIA_READ=ZERO
SAFE_TO_DEPLOY=NO
```

This passes the owner Mac source/logic/HTTP-sandbox gate **but not Safari IndexedDB persistence or release**. The 082 candidate is under `~/AION_PROJECTS/NOVA_082_PRODUCT_CANDIDATE/candidate`.

## Actual NOVA 084 deliverable

`NOVA_084_SAFARI_ISOLATED_E2E.zip` — SHA256 `07400971f01436bfd8180624a7038ccb030920117eee4d2a48f3ef96d18eb03f`.

- Read-only preflight re-verifies all 52 file SHA-256 against the exact owner-staged 082 candidate and requires the genuine NOVA 083 Mac report.
- Runs on **random free 127.0.0.1-only port**, creating a separate browser origin; never connects to or modifies music engine 8791, live gateway 18804, Tailscale, existing iPhone PWA or existing user IndexedDB.
- A GET-only static handler temporarily inserts one external selftest JS script into the **HTTP response only** for an unguessable test URL. Never changes the pinned source files. Local music API GETs return 503 and any POST returns 405. CSP restricts fetch destinations to same test origin.
- The selftest is executed by **actual Mac Safari** after opening its test URL; checks the Create page, browser IndexedDB, separate Russian lyrics field, overlong 351-char rejection, valid 350-char synthetic-project creation, saving test Lyrics, reload, recovery of test draft and lyrics, and Library visibility.
- Writes **one synthetic draft in the fresh test-origin IndexedDB**. It never clears database history, deletes users' songs or reads the live private music library. Browser selftest result is shown as overlay PASS or BLOCKED and copied by the owner; no report POST or external telemetry.
- 8 Python safety tests PASS, Node JS syntax check PASS, ZIP SHA manifest PASS, clean extraction PASS, synthetic owner-home preflight and HTTP listener startup PASS. **Real Mac Safari runtime not yet tested**.

## Owner Mac run (one command)
```bash
cd "$HOME/Downloads" && unzip -n NOVA_084_SAFARI_ISOLATED_E2E.zip && bash "$HOME/Downloads/NOVA_084_SAFARI_ISOLATED_E2E/RUN_084_SAFARI_GATE.command"
```
Safari should open automatically (otherwise use `NOVA084_SAFE_URL=...` printed by the command). Keep Terminal open until browser shows NOVA 084 SAFARI PASS or BLOCKED, then click **Скопировать результат** and paste JSON into chat. Stop only the owned test server by pressing Ctrl+C; **no production service is stopped**.

**NO_DEPLOY** until Safari PASS, separate iPhone installed-app and backup/recovery tests, private API security checks, and real audio-quality acceptance. Passing this test alone is not permission to deploy live NOVA 064.
