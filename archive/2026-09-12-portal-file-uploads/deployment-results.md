# Upload deployment verification

Deployed to aitherdev on 2026-09-13 from the retained feature worktrees.
No default branches were merged and the initiative remains open.

- User profile 33: `/nix/store/piif11vnfq24is20gpmib5i40kb66k9h-dev-workspace-0.2.0`.
- Confctl generation: `2026-09-13--00-25-38`.
- System: `/nix/store/fllksyvh2nr52am87vs6nj7czwsnl19i-nixos-system-aitherdev-26.05.20260911.21a67dc`.
- Application and host-module pins both select runtime `30bfb2a378138a7fdfe8f6aaa05fcbf8d98037b3`.
- Both builds, exact deployment contract, dry activation and switch passed.
- Both configured system health checks passed. Portal, router, nginx and Codex
  services are active. The shared Codex 0.154.0 process was not restarted.
- Final index, initiative page and upload-module checks passed after removing
  a duplicate built-in plan.md artifact from this initiative manifest.
- HTTPS authentication passed; unauthenticated access returned 401. A live
  8 MiB file transferred in three chunks with checksums, completed, downloaded
  byte-for-byte and was removed. Health passed again after system activation.

The first profile switch was refused because this initiative's earlier creation
attempt remained unfinished. Two exact retries preserved its original goal and
tracking proofs; the second succeeded through the normal CLI. The subsequent
profile switch passed without bypassing the guard. See state.md for evidence.

Browser acceptance covered a 1 GiB transfer with matching SHA-256 and about
53 MiB peak server RSS. Real Codex acceptance verified reading the private file,
rollback/rollforward, a fork reading the same bytes, archive/revive, shared-file
deletion and cleanup through actual session deletion. All current feature CI runs
passed; exact revisions and result links are in final-revisions.json and
ci-results.json. Earlier isolated startup/materialization limitations are recorded
in state.md and were not hidden by replacing a thread.

The previous package and system remain available. All private acceptance fixtures
were cleaned; the real initiative and feature branches remain active for review.
