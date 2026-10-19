# NOVA 081 — candidate behavior gate (2026-10-19)

**Status:** packaged local QA for staged NOVA 080 candidate, 12 synthetic/dynamic VM tests PASS, package integrity PASS; **owner Mac run pending; deployment blocked**.

## Based on
- Owner's Mac NOVA 080 report: `STATIC_SOURCE_AUDIT_PASS_BUT_OWNER_GATES_PENDING`; 21 tests PASS, six source files SHA matches, 2 findings.
- Owner's Mac NOVA 080 stage: `CODE_ONLY_STAGED_PINNED_ONE_LINE_FIX`; only `app/index.html` changed, SW/Storage/Live unchanged.
- Pinned original Creative Studio script SHA256 `5ddb7eb035c42ed85e4a76d542dc810a213a2530a38d2c4a65feea5a0c0d83b6`.

## What new QA actually does
- Tests the exact archived original inline NOVA 064 JS and staged candidate in isolated Node VM with fake document events and inaccessible storage, **no networking or music generation**.
- Dynamic test matrix: unmodified ideas 350/351 ASCII chars, applied-creative ideas 350/351 chars, blank idea; verifies that **raw 351 used to pass** click handler, but candidate blocks click with warning/focus; no accidental rejection of 350.
- Verifies six candidate files against both NOVA 080 audit and staged `CANDIDATE_080_MANIFEST.json` SHA256s; every file except `app/index.html` must be byte-identical, script exactly one expression change; rejects unauthorized edits, source drift, unknown audit findings, missing source, symlinks, and report overwrite.
- Validates candidate Python source syntax and webmanifest; writes report only under `~/AION_PROJECTS/NOVA_081_CANDIDATE_BEHAVIOR_GATE/NOVA_081_QA_REPORT.json` after successful checks.
- 12 automated tests PASS locally including negative cases and no overwrites; ZIP integrity and SHA manifest PASS. No access to full owner Mac code/media before execution.

**Private package:** `NOVA_081_CANDIDATE_BEHAVIOR_GATE.zip`, sha256 `8295de8cd19272dcba735db59532053afe9404865f0fb94a73a877791f4bb89d`.

## Owner Mac command
```bash
cd "$HOME/Downloads" && unzip -n NOVA_081_CANDIDATE_BEHAVIOR_GATE.zip && bash "$HOME/Downloads/NOVA_081_CANDIDATE_BEHAVIOR_GATE/RUN_081_CANDIDATE_QA.command"
```

Expected successful status: `NOVA081_DECISION=CANDIDATE_UI_CLICK_GUARD_PASS_DEPLOY_BLOCKED`.
Please attach the JSON report if Mac blocks or pass output differs from expectations.

**Limitations and blockers:** This tests only the **click handler** of Prepare. Other keyboard/programmatic paths cannot be declared safe without full browser E2E and server source audit. The global `nova064.creative.original-genre` storage key issue remains unsolved and deliberately unchanged; all original music/sessions remain untouched. Native `lyrics` support has been shown only in isolated ACE-Step 076, not live 064. No production deploy, Tailscale change, POST /lm or /synth, PWA storage migration, model weights download or GitHub `main` mutation in this phase.

**Commercial readiness:** NOT READY. Do not claim quality or functional mobile/desktop release before protected owner acceptance.
