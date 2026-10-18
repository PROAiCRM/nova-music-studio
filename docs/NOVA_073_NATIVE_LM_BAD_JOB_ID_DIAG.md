# NOVA 073 — Native ACE-Step /lm job-id failure diagnostic (2026-10-18)

**Status: LOCAL_FORENSICS_PACKAGE_TESTED; USER_MAC_NOT_YET_EXECUTED; REAL_WAV_NOT_CREATED.**

Owner Mac NOVA 072 audit reported:
- Native ACE-Step `127.0.0.1:8791` healthy, `/props` available.
- LM `acestep-5Hz-lm-0.6B-Q8_0.gguf`.
- DiT `acestep-v15-turbo-Q4_K_M.gguf`.
- No second LM tier.
- Owner approved one real B trial via typed `NOVA072 REAL B`.
- Trial failed **after attempted POST /lm** with `BLOCKED_REASON=BAD_ENGINE_JOB_ID`, before WAV synthesis.

The official acestep.cpp API documents a successful asynchronous LM submission as `{"id":"1"}`; the NOVA 072 Python parser expects a dictionary and numeric `id` of 1–12 digits. However, **the actual malformed response was not captured** by the client, and it is unknown whether the LM job entered the native queue. We must not reinterpret the error as a known backend bug or simply increase retry count.

**NOVA 073:** stand-alone `NOVA_073_ENGINE_REPLY_DIAG.zip` (~8 KB), 15 safety/integration tests PASS, ZIP test and SHA manifest PASS. GET-only /health and /props, listener command basename via lsof, local previous-failure-marker presence, bounded redacted counts of existing logs if present. No POST, no guessing/polling arbitrary job IDs, no song/media read, no job cancellation, no model download or route change. Writes only `~/AION_PROJECTS/NOVA_073_ENGINE_REPLY_DIAG/NOVA_073_READONLY_REPORT.json`, fails closed if report already exists. Does not modify or clear previous NOVA 072 one-shot marker.

Next owner Mac action:
```bash
cd "$HOME/Downloads" && unzip -n NOVA_073_ENGINE_REPLY_DIAG.zip && bash "$HOME/Downloads/NOVA_073_ENGINE_REPLY_DIAG/RUN_073_READONLY.command"
```

Observe result before any re-POST or patch to NOVA 064. Once actual error/response is known, adapt response handling fail-closed and prove WAV audio improvement by listening.

**NOVA 064**, live localhost gateway 18804, Tailscale and user tracks unchanged. **COMMERCIAL_AUDIO_RELEASE=BLOCKED.**
