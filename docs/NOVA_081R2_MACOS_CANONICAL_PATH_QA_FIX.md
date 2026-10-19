# NOVA 081R2 — macOS canonical path fix (2026-10-19)

**Status:** QA TOOL REPAIRED AND PACKAGED · 21/21 TESTS PASS IN CLEAN EXTRACTION · OWNER MAC RUN PENDING · NO DEPLOYMENT.

## The actual owner Mac failure

NOVA 081R1 failed a single test: `test_canonical_system_alias_can_be_allowed` raised `SOURCE_SYMLINK_BLOCKED`, after 18 other tests passed.

On macOS temporary test directories are often under `/var/folders/...`, whereas their canonical filesystem names are `/private/var/folders/...`. The 081R1 helper `permitted_system_alias()` erroneously compared `p.resolve(strict=True)` with an **unresolved** trusted target. For the synthetic macOS alias test, the expected target could contain the `/var` spelling; this caused an invalid mismatch even though both names referred to the same directory.

## Targeted repair

The only functional code change in `qa081.py`:

```python
return target is not None and p.is_symlink() and p.resolve(strict=True)==target.resolve(strict=True)
```

Allowed entries remain hardcoded to `/var -> /private/var` and `/tmp -> /private/tmp` when canonical destinations match. **Do not permit arbitrary project symlinks.** The test mocks extra trusted aliases only within isolated unit tests.

New regressions:
- alias-to-alias-chain expected to resolve to same underlying canonical directory;
- user-created symlink below a trusted alias must still be blocked.

Existing checks for source-root symlinks, nested `app/` links, file links, path traversal, unknown findings, manifest drift, and report overwrite are preserved.

## Verified work

- 21 tests PASS in current tool environment, independently repeated after clean ZIP unpack (21 PASS).
- SHA manifest verification PASS (7 tracked files), ZIP CRC PASS (8 archive entries).
- Node JavaScript syntax, Python compilation, Bash syntax PASS.
- Existing NOVA 080 candidate, original NOVA 064, active API 8791/18804, Tailscale, music library, Safari/PWA IndexedDB, and GitHub `main` unchanged.
- **Not verified yet:** 081R2 on owner's physical Mac; Mac Safari UI and cross-project state. Do not claim user release readiness.

Private package artifact: `NOVA_081R2_CANDIDATE_QA_CANONICAL_FIX.zip`; SHA256 `f6079c5a2f51ae7d7dfe942972bf73d683b01a63d4f1518021d22af11b6e433f`.

## Owner action

```bash
cd "$HOME/Downloads" && unzip -n NOVA_081R2_CANDIDATE_QA_CANONICAL_FIX.zip && bash "$HOME/Downloads/NOVA_081R2_CANDIDATE_QA_CANONICAL_FIX/RUN_081R2_CANDIDATE_QA.command"
```

Expected after tests: `NOVA081R2_DECISION=CANDIDATE_UI_CLICK_GUARD_PASS_DEPLOY_BLOCKED`. If blocked again, inspect actual error without disabling symlink checks or deploying candidate.

**Next work:** after actual Mac pass, review complete NOVA 080 audit JSON before attempting project-scoped genre storage and native lyrics workflow; do not deploy yet.
