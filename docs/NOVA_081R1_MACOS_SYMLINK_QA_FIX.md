# NOVA 081R1 — macOS symlink false positive fix

**Status (2026-10-19):** new local QA package built and verified; owner Mac rerun PENDING; NOVA 064 unchanged.

## Actual Mac failure, NOVA 081

Mac user ran the original `NOVA_081_CANDIDATE_BEHAVIOR_GATE`. The SHA manifest passed, but 7 of 12 QA tests failed on the same `qa081.Block: SOURCE_SYMLINK_BLOCKED` (4 FAIL, 3 ERROR). Tests use `tempfile.TemporaryDirectory()`, normally located under `/var/folders/...` on macOS. `/var` is a macOS system symlink to `/private/var`; the original `checked()` iterated every ancestor of each test fixture, incorrectly treating this system alias as an untrusted project symlink. Its `pp != p.anchor` check was ineffective because `pp` is a Path and `p.anchor` a string.

**Interpretation:** the *QA tool* failed before reaching candidate behavior testing. It does **not** indicate a failed user project, corrupt archive, candidate tampering or a production NOVA regression.

## Isolated correction

New private package `NOVA_081R1_CANDIDATE_QA_FIX.zip`, SHA256:
`b382e4076648f59c75daa8fedbde28253299e10ecd50b8364a23204aefcb0d8f`.

- Only changes the QA path traversal logic. Allows specifically `/var -> /private/var` and `/tmp -> /private/tmp` if they resolve to those exact canonical OS directories.
- **All other symlinks**, including user-created ancestor links, source root links, links inside `app/`, file links and a trusted alias whose destination changed, are BLOCKED. Path traversal is rejected.
- The original pinned NOVA 064 JS fixture, isolated JavaScript VM logic, source SHA comparisons, candidate SHA manifest, six-file audit gates, original NOVA 080 code candidate, design, backend, PWA storage and user media remain untouched.
- Safe skip/no-overwrite if `NOVA_081_QA_REPORT.json` already exists; no report overwrite workaround.
- **19/19 unit/integration tests PASS** (prior 12 + 7 new macOS-link and symlink-abuse tests), clean ZIP unpack verification PASS, deliberate file tampering detection PASS, Python syntax PASS, Bash syntax PASS and Node syntax PASS. These are tests in the assistant container, **not Mac Safari E2E**.
- No POST, no generation, no restart, no Tailscale Serve mutation, no modification of live NOVA 064 or GitHub main.

## Owner command

```bash
cd "$HOME/Downloads" &&
unzip -n NOVA_081R1_CANDIDATE_QA_FIX.zip &&
bash "$HOME/Downloads/NOVA_081R1_CANDIDATE_QA_FIX/RUN_081R1_CANDIDATE_QA.command"
```

Expected after the user's 080 source pin and stage remain unchanged:
`NOVA081R1_DECISION=CANDIDATE_UI_CLICK_GUARD_PASS_DEPLOY_BLOCKED`.

If the Mac outcome is different, inspect the actual error and sanitized report; **do not bypass a symlink/security gate**. This QA tests only the Creative Studio Prepare click flow; keyboard/API entry paths, genre restore, client/server lyrics, Safari IndexedDB and paid release gates remain open.

**Safe to deploy NOVA 080: NO.**