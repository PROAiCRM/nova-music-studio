# NOVA 075 — isolated real WAV recovery gate (2026-10-18)

**Status: BUILT / PACKAGE HASH VERIFIED / 35 MOCK TESTS PASS / OWNER MAC PREFLIGHT PENDING / COMMERCIAL AUDIO BLOCKED.**

## Confirmed client defect

NOVA 072's `plan_profiles()` stripped the `.gguf` suffix from both `lm_model` and `synth_model` using `.removesuffix('.gguf')`. The documented acestep.cpp `AceRequest` model registry requires **exact filenames including .gguf**, for example `acestep-5Hz-lm-0.6B-Q8_0.gguf` and `acestep-v15-turbo-Q4_K_M.gguf`.

This is an independently established **request construction bug**, but the root cause of the previous `BAD_ENGINE_JOB_ID` is **not proven** because NOVA 072 discarded the unexpected HTTP JSON.

## Findings from NOVA 074 Mac report

- `NOVA074_DECISION=NO_CONTEMPORANEOUS_PROCESS_LOG_REQUIRES_ISOLATED_SERVER_TEST`.
- Current engine is one healthy `ace-server` listener, port 8791.
- 21 candidate log files examined; no contemporary redirected process log.
- `POST=ZERO`, `JOB_POLL=ZERO`, `RESTART=ZERO`, `LIVE_MUTATION=ZERO`, `SAFE_TO_RETRY_B=NO`.
- Old owner-approved B marker is preserved and must not be deleted or replayed.

## NOVA 075 deliverable

`NOVA_075_ISOLATED_WAV_RECOVERY.zip`, ZIP SHA-256 `9f4aec2d7a4c127ad23c20f95ce7dbac1d3c12f8629202705245574d94be8ae7`.

- Separate **GET-only** Mac preflight discovers the live server binary and exact GGUF directory via lsof/ps, checks registry and old B marker, and verifies the chosen isolation port is free. Refuses unknown binary locations and symlinks. No commands sent to live server other than GET `/health` and GET `/props`.
- Separate **owner-confirmed** one-time trial launches an isolated `ace-server` child (same binary and existing model files) bound only to `127.0.0.1:18975`, device CPU, with test outputs under `~/AION_PROJECTS/NOVA_075_ISOLATED_WAV_RECOVERY`.
- Trial sends `POST /lm` **only to 18975** using **full GGUF filenames**, stores the sanitized HTTP acknowledgment shape **before** job-id parsing, polls only the returned validated ID, compares returned Russian lyrics verbatim, and conditionally sends one `POST /synth` on 18975. Saves WAV only when PCM checks pass.
- Always stops **only** the isolated owned child. The 8791 engine, 18804 gateway, Tailscale, NOVA 064 UI, iPhone IndexedDB and user music are unchanged; no automatic retry or resets.
- Synthetic pipeline and error-path tests: **35 PASS**; package manifest and ZIP validation PASS. **No genuine Mac WAV yet**; synthetic PCM is not a listening-quality result.

## Mac owner preflight command

```bash
cd "$HOME/Downloads" && unzip -n NOVA_075_ISOLATED_WAV_RECOVERY.zip && bash "$HOME/Downloads/NOVA_075_ISOLATED_WAV_RECOVERY/RUN_075_PREFLIGHT.command"
```

Only on `NOVA075_PREFLIGHT=ISOLATED_SERVER_READY_FOR_OWNER_ONLY_TRIAL`, no other music job in progress, owner may execute `RUN_075_REAL_WAV_OWNER_ONLY.command` and manually type `NOVA075 ISOLATED WAV`. Do not launch it otherwise.

If Mac preflight blocks, inspect just the sanitized block reason. Do not alter the original B marker, re-run existing NOVA 072, or switch public/private routes. **Commercial music quality remains unproven**.

Upstream contract: https://github.com/ServeurpersoCom/acestep.cpp/blob/master/docs/ARCHITECTURE.md

## Owner Mac result — isolated preflight PASS (2026-10-18)

```text
NOVA075_PREFLIGHT=ISOLATED_SERVER_READY_FOR_OWNER_ONLY_TRIAL
ACTIVE_LIVE_PID=83725 ISOLATED_PORT=18975
LM=acestep-5Hz-lm-0.6B-Q8_0.gguf SYNTH=acestep-v15-turbo-Q4_K_M.gguf
POST=ZERO RESTART=ZERO ORIGINAL_MODEL_WRITES=ZERO NOVA064_MUTATION=ZERO
REPORT=/Users/a1111/AION_PROJECTS/NOVA_075_ISOLATED_WAV_RECOVERY/PREFLIGHT_075.json
```

Note: the earlier synthetic test output included paths under `/var/folders/.../T/tmp...`; these are simulated WAV and failures from unit tests, not real audio on owner Mac. The next optional, explicitly confirmed test is `RUN_075_REAL_WAV_OWNER_ONLY.command` when NOVA is idle. No live runtime change and no commercial audio quality acceptance yet.
