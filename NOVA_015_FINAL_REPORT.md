# NOVA 015 — Final report

Date: 2026-10-15

## Product state

- Source is based on NOVA 014.2 and retains the NUMERA Native 014 visual canon.
- Project creation, ACE Music return flow, audio import, local player, library, SHA-256 backup/restore, and local-storage QA are present in `index.html`.
- Cloud sync is opt-in: it requires interactive Supabase sign-in plus an explicit upload or download click. It has no background network activity on page load.
- Sync uses a private owner-prefixed storage path, per-song SHA-256 verification, insert-only metadata/audio, duplicate detection, bounded batches, and fail-closed conflict/corruption handling. Local originals are neither replaced nor deleted by sync.

## Publication

- Repository: https://github.com/PROAiCRM/nova-music-studio
- GitHub Pages address: https://proaicrm.github.io/nova-music-studio/ (confirmed HTTPS `200` with HSTS).
- Product source commit: `4234c697f3ed485d5f565c525c5fb68fc15820c5`.
- Deployment head at HTTPS verification: `7eb21cc42755ba04869bdc55c602ba464ed645e4`.

## Automated evidence

- `python3 -m unittest discover -s tests -v`: PASS.
- Static release audit: 6/6 checks passed (HTML, no server secret signatures, no media/key/env payloads, private bucket/RLS SQL markers, Pages entry file).
- Mock cloud E2E: PASS for sign-in, upload, metadata/audio deduplication, download, SHA-256 corruption rejection, interrupted-metadata recovery, and conflicting-orphan refusal.
- Interface regression: PASS for 48 viewport/theme/route combinations; no horizontal overflow, JavaScript exceptions, or background Supabase traffic.
- UI smoke: PASS for 12 viewport/route combinations.

## Security confirmation

- Source scan found no service-role key, private key, GitHub token, or real audio file.
- Browser code contains only the Supabase publishable key; no privileged key is embedded.
- `nova-audio` SQL declares a private bucket plus authenticated owner-only select/insert policies and no update/delete policy.
- HTTPS reachability was confirmed for the project REST endpoint and Supabase MCP endpoint (both returned expected unauthenticated `401`). No production rows, objects, users, or migrations were changed by NOVA 015.

## Remaining owner verification

- Live schema, Auth settings, RLS policies, Storage policies, and advisors require a project-management Supabase OAuth/CLI session; no migration was replayed without that access.
- Real two-device Mac ↔ iPhone verification cannot be substituted by emulation. Use the published `qa/` test screen with a separate test account and synthetic WAV, then clean up its test object and metadata.
- Do not import personal music until the owner has passed that real-device test and retained a full local backup.
