# NOVA 077 — real WAV audio-quality baseline (2026-10-18)

**Status:** first owner-Mac true ACE-Step generation PASS; objective uploaded WAV measurement PASS; **human vocal quality and commercial release still pending**.

Owner provided real `NOVA_076_RUSSIAN_VOCAL_REAL.wav` generated in isolated ACE-Step trial NOVA 076. Owner log confirmed `NOVA076_LM_ACK=VALID_ID`, `NOVA076_ISOLATED_SYNTH_POST=ONE`, `NOVA076_AUDIO=REAL_WAV_CREATED_LISTEN_PENDING`, and no POST to live 8791/18804 gateway.

## Verified objective baseline

| Measurement | Value |
|---|---|
| PCM type | Stereo 16-bit WAV, 48,000 Hz |
| Exact duration | 29.600 seconds |
| File bytes | 5,683,244 |
| Whole-file RMS | -15.29 dBFS |
| Sample peak | -0.00027 dBFS, almost digital full-scale |
| PCM16 absolute extreme samples | 30 (possible headroom/clipping issue; not proof of audible distortion) |
| Samples at >= 0.99 full scale | 44 |
| Last 100 ms RMS | -14.26 dBFS; segment ends audibly non-silent |
| Last stereo frame amplitude | -0.1220, -0.1762 |
| SHA-256 of owner-uploaded WAV | `a90bc4d8414b7142e525dae77431c2e987f2663fbd5ffc42689c08335471e917` |

The audio file remains PRIVATE and is **NOT** committed to this public repository. The above measurements come from a verified, provided attachment in conversation. No clip remediation or alternate generation has yet been verified.

## Engineering and listening findings

- **Native engine integration:** A genuine WAV was produced. The previously blocking hex-ID client defect has been resolved in the isolated test.
- **End truncation:** NOVA 076 sets `duration:30`, but WAV is 29.6 sec with a nonzero final frame. This is a preview without a compositionally finished outro or fade. Change the musical form or audition a suitably longer duration rather than treating a fade as equivalent to generating a complete song.
- **Dynamics:** Near-zero dBFS peak suggests very limited sample headroom. Hard clipping/artifact visibility cannot be established by sample extremeness alone. Check output gain, true peak and distortion before professional mastering.
- **Vocal quality:** the WAV supports intelligibility/aesthetics listening but RMS/peak alone cannot objectively establish natural timbre, phoneme accuracy or human-rated Russian word intelligibility. These require real human comparison.
- **Installed weights on owner Mac:** LM `acestep-5Hz-lm-0.6B-Q8_0.gguf`, DiT `acestep-v15-turbo-Q4_K_M.gguf`. Bigger LM and higher-precision/SFT DiT are future isolated options, but no sonic superiority on this Mac has been proven.
- **Reference audio remains unchanged**. No switch of live NOVA 064, Apple client data, public GitHub main or Tailscale.

## Next controlled acceptance gates

1. Preserve original WAV and its hash. Compare identical prompt/lyrics/seed at matched playback loudness.
2. Require a complete phrase ending and intelligible Russian words; use blind listening ratings (words 1–5, vocal timbre 1–5, musical appeal 1–5, artifacts 1–5, would-replay 1–5).
3. Test larger LM **one variable at a time** only with new free weights, sufficient Mac RAM/disk, and estimated CPU time.
4. Independently test higher-precision DiT (Q8_0) and/or SFT; do not assume Turbo with 50 steps yields better sound. GPU/server commercial strategy deferred.
5. Check licensing, rights, safeguarding and real owner-tested iPhone Mac flows before announcing commercial release.

**Status: REAL_GENERATION=PASS · TECHNICAL_WAV_BASELINE=PASS · COMMERCIAL_AUDIO_GATE=BLOCKED.**
