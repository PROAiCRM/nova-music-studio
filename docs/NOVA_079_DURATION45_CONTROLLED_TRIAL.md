# NOVA 079 — controlled duration-only local model trial

**State (2026-10-18):** BINARY-SAFE ISOLATED PACKAGE READY; REAL MAC RUN AND LISTENING PENDING; no release changes.

## Rationale
Owner's genuine NOVA 076 29.6-second WAV proved integration but was abruptly truncated at the end of a lyric phrase. NOVA 078 private A/B/C mastering reduced true peak and faded the ending, but fade is not a naturally completed composition. The next scientific A/B test varies **one single generation parameter**:

- Baseline NOVA 076: `duration=30` seconds.
- Candidate NOVA 079: `duration=45` seconds.
- Same 0.6B Q8 LM, Turbo Q4_K_M DiT, caption, explicit Russian lyrics, seed=20261018, bpm=102, steps=8, shift=3, WAV16.
- No new weights downloaded and no modification to models.

## Safety gates
- Read-only preflight verifies original NOVA 076 WAV SHA256 = `a90bc4d8414b7142e525dae77431c2e987f2663fbd5ffc42689c08335471e917` and previous result indicates successful real WAV creation with same SHA. Original file not overwritten.
- Exact ACE-Step binary and GGUF model selection from active live 8791 process are checked without mutation.
- New owned child ace-server binds to **127.0.0.1:18979** only. One confirmed POST /lm, then at most one POST /synth. No automatic retry.
- Live 8791/18804, Tailscale, desktop app, iPhone PWA, IndexedDB, tracks and published GitHub main remain unchanged.
- Owner explicitly types `NOVA079 DURATION45 WAV` before new generation; test output is isolated under `~/AION_PROJECTS/NOVA_079_DURATION_45_AUDITION/`.
- Any preflight or runtime failure fails closed; no removal or reuse of NOVA 072, 075 or 076 run markers.

## Quality and verification
Private file `NOVA_079_DURATION_45_AUDITION.zip`, package SHA256 `c7f4e87c528b15f9fdb2560b5cb49f4a436b34fd86a0e242d7093daf89f7b041`.

**45 automated tests PASS** including synthetic complete LM→synth WAV and failure paths, 4 new read-only original golden-WAV integrity gates, strict 16-hex IDs, and no POST to the live server. ZIP and SHA integrity PASS. Synthetic test output is not proof that Mac created real 45s audio.

Mac commands:
```bash
cd "$HOME/Downloads" && unzip -n NOVA_079_DURATION_45_AUDITION.zip && bash "$HOME/Downloads/NOVA_079_DURATION_45_AUDITION/RUN_079_PREFLIGHT.command"
```
Then only if preflight passes and no other song is generating, owner may manually run:
```bash
bash "$HOME/Downloads/NOVA_079_DURATION_45_AUDITION/RUN_079_REAL_WAV_OWNER_ONLY.command"
```

**Listening acceptance**: check whether the extra 15 seconds provides a meaningful end to the chorus and audible breath/word clarity without worsening musicality or timbre. If 45 sec still ends abruptly, do not call it a fix; plan an explicit musical outro in a future candidate. No commercial sound quality claim is supported yet.

## Related real-audio local comparator
NOVA 078 private ZIP includes A original and B/C physically rendered WAV derivatives. Measurement evidence: source -12.2 LUFS, +0.1 dBTP; B -14.1 LUFS/-1.6 dBTP; C -15.2 LUFS/-1.3 dBTP. B/C require blind listening approval; they are not new model output. **Private WAVs must not be published to this public GitHub repository.**
