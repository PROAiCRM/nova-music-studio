# NOVA 074 — Active Engine Trace (2026-10-18)

**State:** local read-only forensic package validated; not yet run on owner's Mac. No real WAV, no commercial audio acceptance.

### Observed facts from the user-supplied NOVA 073 report
- /health and /props are OK; listener is one ace-server.
- Four model families present, one each: LM, embedding, DiT, VAE.
- B trial marker exists, no generated WAV or result.
- Twelve historical NOVA_019_CPU_ENGINE logs show no recognized numeric job IDs; this cannot prove the failed request was never queued.
- Actual POST /lm response was not saved and remains unknown. Do not retry B on the live engine.

### NOVA 074 package
- Standalone archive: NOVA_074_ACTIVE_ENGINE_TRACE.zip.
- SHA256: c6ba717b6200869d32478f14db8857470c920d673f433625e0c33a97932e3491.
- 10 automated tests PASS; ZIP and manifest PASS. Synthetic end-to-end verified.
- Only local GET /health and /props; no POST /lm, no GET /job, no model generation or restart.
- Identifies active port 8791 server with lsof; examines active stdout/stderr file descriptors and bounded permitted ACE log tails; compares log modification timestamps to failed B marker.
- Reports only aggregate diagnostic counters, timestamps and ACE log file basenames; no raw log contents, prompts, tracks or secrets.
- Never deletes previous marker, overwrites reports, updates HTTPS/Tailscale, or modifies NOVA 064.

### Owner command
cd "$HOME/Downloads" && unzip -n NOVA_074_ACTIVE_ENGINE_TRACE.zip && bash "$HOME/Downloads/NOVA_074_ACTIVE_ENGINE_TRACE/RUN_074_READ_ONLY.command"

Report: ~/AION_PROJECTS/NOVA_074_ACTIVE_ENGINE_TRACE/NOVA_074_ACTIVE_TRACE_REPORT.json.
Even if logs look normal, queue status remains uncertain without the missing HTTP acknowledgment. When log evidence is inconclusive, the next *separately authorized* quality trial needs a new isolated ace-server on a distinct loopback port and sanitized response capture. Old B must not be retried on 8791.

Commercial quality remains BLOCKED until a genuine owner-listened WAV of intelligible Russian singing exists.