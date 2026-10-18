# NOVA 076 — upstream hex job ID compatibility fix (2026-10-18)

**Status:** SOURCE REGRESSION FIX BUILT; 41 OFFLINE/SYNTHETIC TESTS PASS; USER MAC REAL AUDITION PENDING; COMMERCIAL AUDIO BLOCKED.

## Root cause found in upstream source and our client

**Upstream implementation** [ServeurpersoCom/acestep.cpp tools/ace-server.cpp](https://github.com/ServeurpersoCom/acestep.cpp/blob/master/tools/ace-server.cpp) explicitly documents "Job IDs are random 64-bit hex strings", and function `job_make_id()` serializes `rng()` using `snprintf(..., "%016llx", ...)`, producing **exactly 16 lowercase hex characters**.

Both NOVA 072 and NOVA 075 clients **incorrectly accepted only decimal IDs**, with regex `[0-9]{1,12}`. The NOVA 075 controller also restricted `GET /job?id=...` to decimal characters. This is a **verified client-side contract defect**, consistent with the user's real `ENGINE_BAD_JOB_ACK`. The actual old response JSON content was not saved; the local sanitized `LM_ACK_SHAPE_075.json` must be inspected before asserting it is the specific cause of that Mac trial.

The previous NOVA 075 Mac result:
```text
NOVA075_ISOLATED_SERVER_CHILD_STARTED=YES PORT=18975
NOVA075_ISOLATED_LM_POST=ONE
NOVA075_DECISION=BLOCKED_NO_AUTO_RETRY
NOVA075_BLOCKED_CODE=ENGINE_BAD_JOB_ACK
NOVA075_RESULT=/Users/a1111/AION_PROJECTS/NOVA_075_ISOLATED_WAV_RECOVERY/ISOLATED_TRIAL_075/RESULT_075.json
NOVA075_LIVE_SERVER_POST=ZERO LIVE_GATEWAY_POST=ZERO TAILSCALE_MUTATION=ZERO
```
No real WAV was created.

## NOVA 076 package

`NOVA_076_HEX_JOB_ID_RECOVERY.zip`, SHA-256 `d39af4d5a7d25c6cfb894264122ec891e5a2e6b35dc39d91c5041bfd5424bb1c`.

- 41 automated tests PASS, independent mock pipeline LM → Synth → PCM WAV; SHA-256 manifest PASS, ZIP integrity PASS, Python and bash syntax checks PASS. Mock WAV is **not** a real audio-quality result.
- Accept job IDs matching exactly `[0-9a-f]{16}`; applies to both `POST /lm`/`POST /synth` ack parser and `GET /job?id=<hex16>` URL filter.
- Before any real new POST, a **GET-only** preflight checks the previously written NOVA 075 sanitized `LM_ACK_SHAPE_075.json` and result: requires HTTP 200, top-level `id`, JSON string ID, and no server `error`. If not confirmed, **fail-closed**, no new trial.
- Separate owner-confirmed single-shot process on localhost port **18976**, CPU-only, using the existing GGUF models read-only. Keeps former NOVA 072/075 one-shot markers untouched. Stages in `~/AION_PROJECTS/NOVA_076_HEX_JOB_ID_RECOVERY/`.
- No POST to live engine 8791 or gateway 18804, no Tailscale changes, no edits to Mac/iPhone app, local music, GitHub `main`, or GGUF weights.

## Owner Mac instructions

1. Download the ZIP into `~/Downloads` and run:
```bash
cd "$HOME/Downloads" && unzip -n NOVA_076_HEX_JOB_ID_RECOVERY.zip && bash "$HOME/Downloads/NOVA_076_HEX_JOB_ID_RECOVERY/RUN_076_PREFLIGHT.command"
```
2. Only after `NOVA076_PREFLIGHT=ISOLATED_SERVER_READY_FOR_OWNER_ONLY_TRIAL` and when no other music generation is running, optionally:
```bash
bash "$HOME/Downloads/NOVA_076_HEX_JOB_ID_RECOVERY/RUN_076_REAL_WAV_OWNER_ONLY.command"
```
Confirm `NOVA076 ISOLATED WAV` when prompted. There is **no automatic retry**. Only the new owned test process is stopped at completion; 8791 and 18804 remain untouched.

If preflight blocks with `PREVIOUS_075_ACK_NOT_RECOGNIZED_ID_DO_NOT_RESUBMIT`, inspect the 075 ACK report rather than triggering another costly test.

## Commercial gate

NOT_READY_FOR_COMMERCIAL_AUDIO. A completed 30-second WAV with clear Russian words and listenable vocals must be independently generated and evaluated. Larger LM/DiT weights may improve quality after reproducible trials, but are not presently installed or proven.
