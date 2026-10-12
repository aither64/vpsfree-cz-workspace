# General review

## Findings

No Blocking or Important findings. No additional issues were found beyond
the prerequisite correction already identified by the coordinating agent.

### Advisory: state the database prerequisite for plugin commands

- Commit: `48a456ceba8bb7c462321ac28429790f50efe969`.
- Location: `docs/plugins.md:67` (committed version).
- The example starts an API development shell and runs plugin Rake tasks,
  but does not state that they load the API and require a configured,
  initialized database. A reader following it in a fresh checkout cannot even
  list the tasks. `api/Rakefile:8` enters the normal API loading path for
  these commands; unlike the i18n task path, it does not avoid database setup.
- Add the prerequisite before the command block. The coordinating agent
  independently reproduced `ActiveRecord::ConnectionNotDefined` and has
  already prepared this exact narrow correction in the working tree. I
  inspected that diff; it addresses the finding. Fold it into the Markdown
  migration commit and run the existing quick documentation checks.

## Reviewed scope

- Repository: `worktrees/2026-09-15-vpsadmin-docs/vpsadmin`.
- Series: `f8fb5b3af225f20b40ad16df49d4f4ceca68fcf7` through
  `48a456ceba8bb7c462321ac28429790f50efe969`.
- Commits: `b3e7118ed78d7316473000c085b9ff216c2de1a4` removes obsolete
  release/OpenVZ material; `48a456ceb` introduces the maintained Markdown
  collection and its entry points.
- Lane: general; direct review with `gpt-6-astra`, `xhigh`, no nested agents.
- Read the review packet, plan/state, repository `AGENTS.md`, commit messages,
  changed documentation, representative removed content, and relevant source.

## Assessment and verification

The series matches the accepted request for ordinary Markdown without a site
renderer. Obsolete documentation removal and the retained-document migration
are independently reviewable commits. Keeping factual corrections with the
new Markdown pages is justified: the replacement collection describes the
current implementation immediately. Both commit messages satisfy the
repository's 80-column requirement.

The README index, root README, AGENTS link, page titles, relative source links,
and storage subpages form a coherent navigation path. The documentation license
and Czech terminology file remain unchanged. The source-link and obsolete-path
search found no current consumers of the removed guides or migration scripts.
The remaining `.mdwn` patterns in CI selection are harmless ignore patterns.
Removed shaping and console instructions describe the retired OpenVZ tooling;
current code uses host-interface CAKE and vpsAdminOS operations. The historical
v3 transition instructions do not describe a current deployment procedure.

Checked transaction construction, scheduling, queue capacity, locks,
confirmations and rollback; lifetime transitions and expiry tasks; plugin
selection, loading, migrations and the Nix shell's automatic `api/` directory
selection; storage creation/removal, transfer selection, rollback, branching
and retention; export formats, URL construction, mounting, readiness, size
units, checksums, streaming and CLI backup behavior. The retained explanations
agree with these implementation paths.

Independent quick checks passed:

- `git diff --check f8fb5b3af..48a456ceb`.
- Initiative `check-docs.py`: 92 local links in 11 Markdown files; anchors,
  index coverage, fences and preserved files pass.
- Commit-message line lengths: no lines exceed 80 columns.

## Residual risks and gaps

- No VM, live ZFS transfer, plugin migration or HTTP-serving test was run by
  this reviewer. Source inspection and document checks are proportionate for
  this documentation-only series. The recorded commit-hook results were
  reviewed, not rerun.
- External bookmarks to removed source paths may break, as explicitly
  accepted in the plan. No deployed documentation site is changed or checked.
- These are focused architecture and operation notes, not comprehensive
  subsystem manuals or instructions for recovering historical v2/v3 systems.
- The main committed review ends at `48a456ceb`; the inspected database
  prerequisite diff is the only subsequent edit assessed here. Its narrow
  remediation needs focused verification, not another review lane or rerun.

No project files were edited by this reviewer.
