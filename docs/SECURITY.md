# NOVA — Security and privacy safeguards

1. GitHub Pages is public. Anything in the repository and its static assets can be read by anyone. Never store music libraries, private prompts, authentication credentials or secrets here.
2. For a future NEW, dedicated cloud backend, use a **private** `nova-audio` storage bucket; client routes must authenticate with a user JWT and only publishable/anon keys may be embedded in web assets. Never embed a `service_role` or ACE Music key.
3. Draft `db/001_nova_cloud.sql` intentionally permits `SELECT`/`INSERT` for a user's own metadata and audio, not `UPDATE`/`DELETE`. Validate with at least two isolated test identities and anonymous access before any real music upload.
4. Audit all existing policies before applying the SQL. A permissive policy on the same tables/storage bucket could bypass the proposed policies. Use a **new empty Supabase project** for the pilot; do not reuse another project's database.
5. An in-browser JWT stored in `sessionStorage` is still exposed to malicious scripts/XSS. Before a commercial launch add proper session lifetime/refresh, security headers, output sanitization audits, abuse/rate limits, logging and a recovery procedure.
6. On auth or network errors, the application must continue to offer its local library. Sync is opt-in and must not overwrite or delete local tracks.
7. GitHub Pages may require a Pages deploy action even with branch source. Check the real Pages build; do not claim a live site until it's published.
