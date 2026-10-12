# Compact attachment menu deployment

Deployed to aitherdev on 2026-09-13. The + menu is beside Send and Create
session. The permanent upload-limit sentence is removed, empty attachment areas
are hidden, and selected file cards/progress/removal remain available. Server
limits still apply. Exact pushed feature heads are in menu-revisions.json.

- User profile generation 34:
  /nix/store/65zp6sd9qrmzz572x62ia1d2brmfd07f-dev-workspace-0.2.0.
- System generation 2026-09-13--10-05-18:
  /nix/store/m3f33jsmi18b3p7xkzzpj2k4lb6wdq4s-nixos-system-aitherdev-26.05.20260911.21a67dc.
- Previous profile 33 and system 2026-09-13--00-25-38 remain available for
  rollback. Upload state and Codex protocol are unchanged.
- Workspace/configuration pin contract, package and system builds, dry-activate,
  normal workspace-host switch and confctl switch all passed. No kernel rebuild.
- Both configured health checks passed. Portal, router, Codex and nginx are
  active. Codex 0.154.0 kept MainPID 1090021.
- Authenticated HTTPS health, index, this initiative page and versioned menu
  assets returned 200; unauthenticated health returned 401. An 8 MiB live file
  passed three chunk checksums, completion, exact download and deletion.
- All 11 Firefox acceptance checks passed at 1280 and 390 CSS pixels, including
  both forms, shared/fallback composers, keyboard and native dismissal, menu
  placement without layout growth, warmed forward/rollback caches, picker/drop,
  removal, exact sent bytes, limits errors and attachment-only initial submission.
- All four mandatory review lanes completed; both Important findings and the
  Advisory finding are fixed. Provider and workspace nix flake check passed;
  package Go/Ruby tests and all configured current-head CI passed. Workspace and
  configuration repositories have no feature-branch workflow runs.

All owned browser fixtures and temporary input files were removed. Project
tracked worktrees are clean; existing configuration tool caches remain for
follow-up work. Branches remain unmerged and the initiative remains active.
No archive, deletion or session stop is scheduled.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-12-portal-file-uploads/
