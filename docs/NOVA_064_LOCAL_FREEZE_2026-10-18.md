# NOVA Music Studio — local baseline freeze (2026-10-18)

**State:** OWNER-ACCEPTED LOCAL BASELINE / LOCAL SNAPSHOT INDEPENDENTLY VERIFIED / RESTART AND OTHER-PROJECT GATES PENDING. This branch is a release index, **not** proof that the current Mac runtime source or user media have been uploaded to GitHub.

## Baseline
- UI and application: **NOVA 064 Final Creative**, with NOVA 062 / 061 retained for rollback.
- Mac CPU generator: **ACE-Step via local service at 127.0.0.1:8791**.
- Private NOVA local gateway: **127.0.0.1:18804**, exposed only through the owner's private Tailscale HTTPS, dependent on the Mac remaining on.
- Client: iPhone Safari and installed web app; Mac browser-based interface.
- Owner reports generation, player, music and project persistence work locally.
- No standalone remote backend, cloud sync or independent always-on generator in this release.

## Local snapshot evidence
- Snapshot destination: `~/AION_PROJECTS/NOVA_064_LOCK_20261018` on the **same Mac**.
- First archive attempt NOVA 068 stopped on Tailscale topology-status comparison; do **not** treat its partial result as a completed backup.
- NOVA 069 resumed that archive safely and reported:
  - `NOVA_069_DECISION=LOCAL_SNAPSHOT_RECOVERED_SHA256_PASS_RESTART_PENDING`
  - `COPY_FILES_VERIFIED=148804`, `EXISTING_REUSED=148802`, `NEW_COPIED=2`
  - `HTTPS_CHANGED=NO`, `ORIGINALS_DELETED=ZERO`, `GENERATION_POST=ZERO`
  - `SAFE_TO_DELETE_DESKTOP=NO_RESTART_AND_PROJECT_GATE_PENDING`
- NOVA-only GitHub export generated on Mac: `~/Downloads/NOVA_064_CODE_ONLY_FOR_GITHUB_20261018.zip`; **not yet independently reviewed or committed**.
- **Independent snapshot verification by owner (2026-10-18):** `NOVA_068_VERIFY=FULL_COPY_SHA256_PASS`; `FILES_VERIFIED=148805`; `FROZEN_RUNTIME_SOURCE=/Users/a1111/AION_PROJECTS/NOVA_064_LOCK_20261018/local/runtime_source`; `GITHUB_CODE_EXPORT=READY_FOR_REVIEW`; source and desktop deletion gates remain blocked.
- Next gates: inspect and validate code-only export, safely test launch from archived location without changing live Tailscale routes, and verify other Desktop project dependencies individually.

## Preservation rules
1. **Do not delete Desktop or Downloads originals** from this checkpoint. Desktop root standalone files were **not included** in folder-only archive. Other projects' symlinks and references may still target Desktop.
2. Existing NOVA 064 HTTPS `18804` and engine `8791` are live; freeze scripts must not kill/restart/switch them, generate songs or alter PWA IndexedDB.
3. The snapshot is **one additional copy on the same Mac**, not an off-device disaster-recovery backup; make a separate external/encrypted copy for actual hardware-loss protection.
4. Do **not** upload full snapshot, generated songs, models, tokens, `.env` files, secret settings, or private server results to this **public** repository.
5. Full backup exported from iPhone Files remains a separate user-held artifact, not automatically copied by the Mac snapshot.

## Deferred product work (not part of freeze)
Lyrics generation, audio editing/stems, cover generation, richer style controls, a remote generator/always-on backend, commercial licensing, payments, and security / load testing.

## GitHub release scope
This branch holds a **documentation-only release index** until the owner supplies the **code-only** ZIP for independent review. Existing `main` and GitHub Pages intentionally remain unchanged. Do not claim GitHub contains a complete restorable NOVA 064 build yet.
