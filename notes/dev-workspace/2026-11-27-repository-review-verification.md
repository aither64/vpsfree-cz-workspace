# Repository review diagnosis and browser checks

The livepatch Repository tab failed because automatic selection reached a 2019
Linux base and produced 88,014 changed files. Raising limits would preserve the
wrong comparison. Exact recorded ancestor evidence gave 13 commits and 9 files
for linux-core. The supported review-base setting repaired all 13 Linux views
without changing source refs, lifecycle manifests or saved comparison URLs.

Live acceptance also exposed two harness mistakes: Playwright's setDefaultTimeout
does not change expect's five-second timeout, and the portal source preview uses
CodeMirror, not Monaco. Assertions against actual .cm-editor .cm-content text,
with expect configured for the intended budget, passed. A socket-forwarding harness
must close pending HTTP requests on exit; streaming event requests otherwise keep
Node alive after Chromium closes. These were harness issues, not product defects.

Claim mutation commands are dev-session coordination acquire/release; workspace-host
coordination exposes status/guide/GC. Invoking acquire on workspace-host fails
without mutation. Configuration's Nix shell can also export Ruby gem paths that
conflict with the installed dev-session wrapper. Run session registration from the
normal workspace shell and configuration hooks through its own Nix environment.

Evidence and exact revisions: work/2026-11-27-portal-livepatch-repositories/state.md
and rollout.md. Product behavior is documented in dev-workspace's session/portal
guides; these observations record this investigation's reusable lessons.
