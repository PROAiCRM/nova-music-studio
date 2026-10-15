# NOVA 014 — Release gates

| Gate | Evidence and criterion | Status |
|---|---|---|
| G0 Visual | Same NUMERA 014 visual tokens as NOVA 013 | CANDIDATE |
| G1 Public repo | PROAiCRM/nova-music-studio public main and source | BLOCKED: repo creation tool unavailable |
| G2 Pages | Settings: main/(root); real HTTPS 200; iPhone page opens | NOT RUN |
| G3 Browser media | Import, play, reload and backup/restore on Mac Safari | PARTLY PROVEN earlier NOVA 012 |
| G4 iPhone media | Import, reload, play, backup/restore on iOS Safari | NOT RUN |
| G5 Private storage | Owner-controlled NEW project, private bucket, RLS, no privileged keys in web | NOT PROVISIONED |
| G6 RLS negative tests | User A cannot read/insert/download User B; anon blocked; own access works; no UPDATE/DELETE | NOT RUN |
| G7 Sync | Two real test users and two devices; SHA-256 round trip, conflict safety | NOT RUN |
| G8 Provider | ACE Music documented, cost/legal terms, server-side secret, real API generation | BLOCKED / NOT CONNECTED |

Never confuse a mock-server PASS with real provider PASS. Do not change AION or NUMERA repositories, remap their domains, or upload personal songs during G5/G6.
