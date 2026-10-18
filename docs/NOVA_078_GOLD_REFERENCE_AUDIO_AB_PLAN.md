# NOVA 078 — GOLD REFERENCE LAB · real-audio A/B/C

**Date:** 2026-10-18. **Release state:** PRIVATE AUDIO A/B COMPARISON READY · OWNER LISTENING PENDING · LIVE NOVA 064 UNCHANGED · COMMERCIAL AUDIO NOT APPROVED.

## Baseline
The source is a **genuine owner-uploaded 29.6-second** ACE-Step WAV generated in the isolated NOVA 076 trial, not a synthetic mock. It is stereo PCM16 48 kHz. SHA256 of original: `a90bc4d8414b7142e525dae77431c2e987f2663fbd5ffc42689c08335471e917`. No user WAV is uploaded to this public repository.

## Actual local audio files (private download package, NOT in GitHub)
- **A original**: byte-identical NOVA 076 source, -12.2 LUFS integrated, +0.1 dBTP true peak; abrupt non-silent ending.
- **B transparent master**: -1.65 dB gain and a 1.15-second terminal technical fade, no EQ. -14.1 LUFS integrated, -1.6 dBTP, LRA ~12.0 LU.
- **C clarity experiment**: highpass 31 Hz; mild 310 Hz -1 dB, 2.7 kHz +1.15 dB, 6.8 kHz -0.45 dB EQ; -2.5 dB gain; same technical fade. -15.2 LUFS, -1.3 dBTP, LRA ~12.2 LU.
- B/C are stereo 24-bit 48kHz PCM, original unmodified. 24-bit output after processing does not retroactively improve 16-bit source resolution.

All metrics derived from actual files with FFmpeg ebur128 and independent PCM analysis. Last 100ms changes from -14.26 dBFS original to -41.21 / -42.13 dBFS B/C. This fixes a technical *abrupt demo truncation* but not the missing compositionally complete outro.

## Audition tool and verification
A standalone, offline HTML blind-label X/Y/Z listening page with synchronized A/B/C positions, approximate equalized playback loudness to -15.2 LUFS, 5 criteria per sample and an opt-in local JSON scorecard save. No connection to 8791, 18804, Tailscale, iPhone PWA, external servers, commercial accounts or user songs.

- Package file `NOVA_078_GOLD_REFERENCE_LAB.zip`, SHA256 `fbfb87c243cda221c9abe3a19b2d71900e1dd785d747c47f69b48f99984218e9`.
- Local script test suite: **18/18 PASS**.
- JS syntax check: PASS with Node.
- Clean ZIP unpack + SHA-256 + WAV consistency check: PASS (14 manifest-tracked files).
- Deliberate WAV tamper: detection and blocking PASS.
- Browser UI dynamic Safari test: **NOT TESTED** (test browser environment blocked local navigation). Owner Mac listening required.
- No real new model inference in NOVA 078. Mastered variants are processed audio samples, not better AI vocal generation.

## Engineering work plan and release gates
1. Measure and rate Russian word recognizability (two independent listeners, >=90% of words without lyrics shown), naturalness, musicality, artifacts, replayability.
2. Edit unnatural lyric phrasing and test syllabic line length and stress in an isolated 45–60 second generation; preserve old seed/lyrics as comparison source.
3. Test complete musical outro rather than cutting at the 30-second API boundary.
4. One variable at a time: existing LM 0.6B Q8 to larger 4B Q8 (not downloaded/installed); existing Turbo DiT Q4_K_M to Q8 or SFT (not downloaded/installed); first verify model licences and Mac RAM/time.
5. Only after true quality gain, integrate full `lyrics` and hex job ID fixes into a separate protected NOVA candidate; keep 064 live and old IndexedDB/media untouched.
6. Commercial gate remains blocked on listener acceptance, licensing review, desktop/iPhone owner gates, privacy and resilience.

**No claim of one-hour background model training or commercial-grade sound.** NOVA 078 produces tangible comparators and measurable output now; real improved singer pronunciation requires a new isolated generation on owner Mac and a human listening gate.
