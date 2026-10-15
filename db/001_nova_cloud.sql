-- NOVA 013 private sync MVP. Run ONLY after owner consent in an isolated new Supabase project.
-- No destructive statements. Database remains editable; migration audit required.
create table if not exists public.nova_songs (
  user_id uuid not null references auth.users(id) on delete cascade,
  song_id text not null check (char_length(song_id) between 1 and 128 and song_id ~ '^[A-Za-z0-9_.-]+$'),
  payload jsonb not null check (jsonb_typeof(payload)='object'),
  audio_path text,
  audio_sha256 text check (audio_sha256 is null or audio_sha256 ~ '^[a-f0-9]{64}$'),
  created_at timestamptz not null default now(),
  primary key(user_id,song_id),
  constraint audio_path_belongs_to_owner check (audio_path is null or audio_path like (user_id::text || '/%'))
);
alter table public.nova_songs enable row level security;
create policy "nova_select_own" on public.nova_songs for select to authenticated using (user_id = (select auth.uid()));
create policy "nova_insert_own" on public.nova_songs for insert to authenticated with check (user_id = (select auth.uid()));
-- NO UPDATE / DELETE policies: never replace or delete users' songs through this pilot.
insert into storage.buckets (id,name,public,file_size_limit,allowed_mime_types)
values ('nova-audio','nova-audio',false,26214400,
  array['audio/mp4','audio/mpeg','audio/wav','audio/x-wav','audio/aac','audio/ogg','audio/flac','application/octet-stream'])
on conflict (id) do nothing;
-- Fail closed if a bucket with this name existed and was public.
do $$ begin
  if exists(select 1 from storage.buckets where id='nova-audio' and public=true) then
    raise exception 'NOVA audio bucket must be private';
  end if;
end $$;
create policy "nova_audio_read_own" on storage.objects for select to authenticated
using (bucket_id='nova-audio' and (storage.foldername(name))[1] = (select auth.uid())::text);
create policy "nova_audio_insert_own" on storage.objects for insert to authenticated
with check (bucket_id='nova-audio' and (storage.foldername(name))[1] = (select auth.uid())::text);
-- No public read, update, or delete on storage objects.
