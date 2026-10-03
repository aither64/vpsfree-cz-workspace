# Group apps under one dynamic system attribute

Adding a second `apps.${system}.name` declaration to a Nix flake can fail during
evaluation with `dynamic attribute 'x86_64-linux' already defined`. Parsing alone
does not catch the duplicate dynamic prefix.

Use one `apps.${system}` attribute set containing the app entries. Keep each
app's `type` and `program` unchanged. Validate the expression through the owning
flake's normal app evaluation or smoke command, as well as parsing/formatting.

In [the storage-profile initiative](../../work/2026-09-23-storage-redesign/state.md),
the first no-VM smoke failed before configuration evaluation. The app grouping
was corrected without changing runtime source, dependency inputs or the lock.
The fresh smoke result is recorded in the initiative; the correction itself
provides no VM or guest-runtime evidence.
