# NOVA 087 — safe staged PWA upgrade candidate (2026-10-19)

**Status:** NOVA 086 Mac Safari synthetic IndexedDB 11/11 PASS; NOVA 087 PWA upgrade candidate BUILT AND VERIFIED OFFLINE; Mac stage and actual service-worker migration NOT YET TESTED. SAFE_TO_DEPLOY=NO.

## Confirmed real Mac Safari gate from owner's supplied result
- `NOVA086_ISOLATED_SAFARI_DOM_IDB_V1 status=PASS`: 11/11 (IndexedDB, NOVA branding/apple touch icon, distinct lyrics field, 351 chars rejected, 350 chars prepared and saved, Russian lyrics and draft survive genuine Safari reload and appear in library).
- Tested only a fresh ephemeral localhost origin, `live_mutation=false`, `generation_post=0`, `stage=NOVA085`.
- **This does not verify the existing iPhone-installed PWA database, backup/restore or safe production upgrade.**

## Actual NOVA 087 engineering change
- Entire 55-file NOVA 085 code-only candidate retained. Only `sw.js` and `app/index.html` differ; HTML has **exactly two revised script query URLs** (`nova034-producer.js`, `nova-local.js`) to avoid stale script responses from a cache-first old worker during rollout.
- New worker cache `nova-r87-safe-shell-v1` preloads 13 shell assets via `Request(...,{cache:'reload'})`. Includes 180/192/512px NOVA icons, manifest and all listed app scripts.
- API paths and non-GET requests never go through caching; cross-origin fetch bypassed; navigate is network-first with offline app-shell fallback.
- Does NOT call `skipWaiting` or `clients.claim` to force an active editor to switch workers. Does NOT delete any old caches, alter IndexedDB, uninstall PWA, erase songs or modify Tailscale. Old cache preserved for potential rollback (not a verified full restoration operation).
- The live generator `8791`, Mac gateway `18804`, NOVA064, local music, installed PWA and published `main` remain unchanged. No UI redesign.

## Verified package and offline checks
- Private artifact `NOVA_087_PWA_UPGRADE_SAFE.zip`, SHA256 `c54d15af3f35d89888645900d733197fdd27bfedb9b85870d6b327ea929a7613`, 66 ZIP entries and 65-file manifest, ZIP CRC PASS.
- 7/7 Python stage validation tests PASS (full exact 55-file verify, no overwrite, symlink denial, source SHA drift denial, owner stage report gate).
- Node mocked service worker test PASS: 13 assets precached, query-bust variants, cross-origin and /api/* pass through, non-GET excluded, navigation network-first, no automatic SW takeover or cache deletion.
- JS syntax PASS for new SW, Bash syntax PASS, source pin diff exactly two files, simulated Mac owner-home staging PASS. **This is offline SW logic, NOT genuine iPhone/Safari SW migration E2E.**

## Owner Mac action — staging only, no deploy
```bash
cd "$HOME/Downloads" && unzip -n NOVA_087_PWA_UPGRADE_SAFE.zip && bash "$HOME/Downloads/NOVA_087_PWA_UPGRADE_SAFE/RUN_087_SAFE_STAGE.command"
```

Verifies exact 55-source-file hashes from existing Mac `~/AION_PROJECTS/NOVA_085_COMMERCIAL_HARDENING/candidate` and `NOVA085_STAGE_REPORT.json`, then stages a new protected candidate `~/AION_PROJECTS/NOVA_087_PWA_UPGRADE_SAFE/candidate` and an immutable report `NOVA087_STAGE_REPORT.json`. Does not run web server or update an installed PWA. Expected `NOVA087_DECISION=ISOLATED_PWA_UPGRADE_CANDIDATE_STAGED_NO_DEPLOY`.

## Commercial blocker priorities
1. Validate controlled old→new service worker update on a disposable origin in genuine Safari/iPhone; ensure IndexedDB records persist, no mixed asset versions and restore/rollback.
2. Owner's iPhone installed-PWA user songs: make a fresh FULL BACKUP and verify off-device restoration without clearing anything; do not overwrite live origin.
3. Object-level auth/session ownership for /api/nova/local/jobs/job/audio is missing. Tailnet is not public multiuser protection.
4. Acceptable Russian vocal intelligibility, complete composition outro, higher-quality ACE-Step variant validated with genuine owner playback A/B (NOVA076 proved only engine functional).
5. Privacy/licensing/payments/support before commercial release.

**Explicitly not a commercial release, not permission to clear/uninstall iPhone PWA.** This GitHub document contains no models, songs, keys, media or private server config.
### Final clean-extraction correction
During independent clean extraction, Python regression tests originally depended on a sibling NOVA085 development directory and failed in a standalone unpack. The final private ZIP now includes a **small, non-secret NOVA085 service-worker fixture** and reconstructs the exact old HTML from the new candidate. Repacked ZIP was independently unpacked and verified: 7 Python tests PASS, mocked SW tests PASS, SHA manifest 65 files PASS, ZIP CRC PASS. Original staging from the owner's pinned 085 directory is unchanged, and the entire candidate remains deploy-blocked. Final SHA256: `c54d15af3f35d89888645900d733197fdd27bfedb9b85870d6b327ea929a7613`.
