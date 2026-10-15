-- NOVA owner security audit. READ ONLY: run after applying 001 in a dedicated test project.
-- Inspect every result. If any unexpected public/grant or extra policy appears, block activation.
select schemaname, tablename, rowsecurity, forcerowsecurity
from pg_tables where schemaname='public' and tablename='nova_songs';

select schemaname, tablename, policyname, permissive, roles, cmd, qual, with_check
from pg_policies
where (schemaname='public' and tablename='nova_songs')
   or (schemaname='storage' and tablename='objects')
order by schemaname, tablename, policyname;

select id, name, public, file_size_limit, allowed_mime_types
from storage.buckets where id='nova-audio';

select grantee, privilege_type
from information_schema.role_table_grants
where table_schema='public' and table_name='nova_songs'
order by grantee, privilege_type;
-- This audit alone does not prove tenant isolation. Run live A/B/anon negative tests.
