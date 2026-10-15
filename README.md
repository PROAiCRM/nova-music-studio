# NOVA Music Studio — GitHub Pages ready

**Version:** NOVA 014.1 (2026-10-15)  
**UI canon:** NUMERA Native 014 — no restyling.  
**Status:** prepared release; not published on GitHub Pages yet.

The root `index.html` is a static HTML music workspace and manual ACE Music handoff. Supabase private media synchronization requires **explicit login** and clicking Upload/Download. It is **not** a proven commercial service.

## Publishing
1. Create a **new public** GitHub repository `PROAiCRM/nova-music-studio` with a README.
2. Upload these files to a fresh branch (prefer PR and review) and merge into `main` when the owner approves.
3. Settings → Pages → Deploy from a branch → `main` → `/(root)` → Save.
4. Verify actual HTTPS URL `https://proaicrm.github.io/nova-music-studio/`.
5. Configure **Supabase Authentication → URL Configuration** for the public address before exercising real account signup, and verify email redirect behavior. Auth configuration is not verified here.
6. Never upload personal audio files or server-side secrets into the repository.

## Cloud status
- Supabase project `NOVA Music Studio`, isolated in Frankfurt, ACTIVE_HEALTHY.
- `public.nova_songs` with RLS and private `storage` bucket `nova-audio`.
- Transactional SQL tests under simulated A/B/anonymous roles passed for row data and storage objects; **real two-account JWT and HTTP Storage API tests are still pending**.
- `sb_publishable_…` key in HTML is public; it is **not** a service-role secret.
- UI is beta / candidate, cloud synchronization remains opt-in and manual.

## Storage continuity
Each origin gets different IndexedDB. Before moving from a ShipStatic address, make a full backup of the existing NOVA library. Moving to GitHub Pages does not automatically transfer the songs.

## Evidence
See `docs/NOVA_014_1_OWNER_STATUS.md` and `docs/NOVA_RELEASE_SHA256.txt`.
