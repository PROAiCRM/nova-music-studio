# NOVA 083 — owner staged-candidate isolated acceptance gate

**State:** QA packaged and independently unit-tested in assistant environment. **Owner Mac NOT YET RUN; Safari/iPhone NOT accepted; live NOVA 064 unchanged**.

### Exact latest owner result
```text
NOVA082_PACKAGE_SOURCE_PIN_PASS files=52 changed=3
NOVA082_MAC_FROZEN_PIN_PASS files=52
NOVA082_DECISION=PINNED_FUNCTIONAL_CANDIDATE_STAGED_DEPLOY_BLOCKED
CHANGED=app/index.html,nova-local.js,nova034-producer.js
CANDIDATE=/Users/a1111/AION_PROJECTS/NOVA_082_PRODUCT_CANDIDATE/candidate
LIVE_MUTATION=ZERO GEN_POST=ZERO SONGS_READ=ZERO TAILSCALE_MUTATION=ZERO
SAFE_TO_DEPLOY=NO_SAFARI_AND_BACKUP_OWNER_GATE_PENDING
```

### NOVA 083 deliverable
Artifact: `NOVA_083_ISOLATED_ACCEPTANCE_GATE.zip`, SHA256 `6c7694d7c4ebcc98ef24b5ddaca9f44d68f84b48ef3efcd895d92c57c8e8e233`.

The owner Mac command:
```bash
cd "$HOME/Downloads" && unzip -n NOVA_083_ISOLATED_ACCEPTANCE_GATE.zip && bash "$HOME/Downloads/NOVA_083_ISOLATED_ACCEPTANCE_GATE/RUN_083_SAFE_GATE.command"
```

Checks before creating any report:
- Source pins: 52 original source hashes matched against downloaded NOVA 082 package, and 52 staged candidate hashes against original 082 build and actual staged manifest; only three previously approved files differ.
- Runs the existing `NOVA082_UNIT_PASS count=15` JavaScript VM regression suite.
- Starts the **existing, unchanged** 082 GET-only static preview handler bound to a random ephemeral 127.0.0.1 port. In 14 HTTP assertions validates static HTML/JS/SW/manifest/icon GET 200, cache no-store and CSP, blocked API GET 503, blocked POST 405, unknown path 404; stops the owned temporary listener.
- Writes a new immutable 0600 file `~/AION_PROJECTS/NOVA_083_ISOLATED_ACCEPTANCE_GATE/NOVA_083_QA_REPORT.json` with only SHA and synthetic QA statuses. If directory already exists, fails before writing.
- No POST to music engine 8791 or app 18804, no Tailscale mutations, no personal music/IndexedDB reads, no SW changes, no user song generation and no private cloud secrets sent.
- 7 integrated safety unit tests PASS in assistant runtime; package manifest 5 files and ZIP CRC PASS. In Chromium isolated inline document, the home and Create page rendered with no JavaScript page errors, but about:blank has **no IndexedDB access** and cannot prove real Safari PWA storage or authentic browser navigation.
- This is QA-only, **not another candidate build or deployment**.

Expected on Mac:
`NOVA083_DECISION=STAGED_SOURCE_JS_AND_HTTP_SAFE_PASS_SAFARI_DEVICE_GATES_PENDING`, `SAFE_TO_DEPLOY=NO`.

### After local QA
On Mac, open isolated preview from existing NOVA 082 without backend:
```bash
bash "$HOME/Downloads/NOVA_082_PRODUCT_CANDIDATE/OPEN_082_ISOLATED_PREVIEW.command"
```
Then `open -a Safari "http://127.0.0.1:18982/#create"` in second terminal. Manually check synthetic idea 350 accepted / 351 rejected, draft genre undo after browser refresh, separate lyrics and a safe unavailable generator prompt. Isolated origin storage differs from both actual 18804 app and iPhone Tailscale PWA; do not use real private songs or delete any browser cache.

**Deployment still blocked** pending real Safari and existing iPhone Safari/installed-PWA full-backup gate, full request contract and commercial sound quality acceptance. Do not alter main branch or deploy private export.

## Owner Mac execution — PASS (2026-10-19)

```text
NOVA083_PACKAGE_SHA_PASS files=5
NOVA083_STAGE_MANIFEST=PASS files=52 changed=3
NOVA083_REAL_JS_HANDLER_TESTS=PASS count=15
NOVA083_LOCAL_HTTP_SANDBOX=PASS checks=14
NOVA083_DECISION=STAGED_SOURCE_JS_AND_HTTP_SAFE_PASS_SAFARI_DEVICE_GATES_PENDING
LIVE_MUTATION=ZERO GENERATION_POST=ZERO USER_MEDIA_READ=ZERO
SAFE_TO_DEPLOY=NO
REPORT=/Users/a1111/AION_PROJECTS/NOVA_083_ISOLATED_ACCEPTANCE_GATE/NOVA_083_QA_REPORT.json
```

This verifies static source pins, mocked JS logic and GET-only isolation on **owner Mac**. It **does not** establish actual Mac Safari behavior, browser IndexedDB persistence, physical iPhone Safari/PWA preservation, original media backup validation, generated song quality, or readiness to deploy. Next step is manually opening the safe isolated NOVA 082 preview on 127.0.0.1:18982 and checking controlled synthetic drafts without touching live site, then identifying outstanding gates. Do not launch a generating backend or deploy the candidate without further checks.
