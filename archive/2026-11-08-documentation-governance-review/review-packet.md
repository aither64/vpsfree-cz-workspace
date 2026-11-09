# Final independent review packet

Session: 2026-11-08-documentation-governance-review. Lead owns this packet;
reviewer0 is retained, independent, read-only, saved Sol/xhigh, lowest eligible
review-purpose member, ready verified ~09:46 UTC 2026-11-09. No settings override.
Read installed mandatory-change-review skill and references for general, scope
and proportionality, risk and compatibility. Risk classification: high because
reorganized operating/upgrade guides include mail queues, notification effects
and irreversible cleanup recovery. This is documentation/instructions only;
apply those lanes to preservation and scope, not unrelated application audits.
No architecture lane: no implementation logic or executable interface changes.

## Outcome and scope

User asked to investigate README pollution and mixing lasting docs with rollout
procedures, improve writing rules/review, assess a writer role, then explicitly
requested a concrete file/directory structure and said "ok, implement it".
Implement the accepted convention and targeted examples. No new writer role,
runtime/catalog/telemetry, package activation, operational execution or integration.
Use design.md (D2 release), plan.md and state.md as context. All intended source
changes are committed, all worktrees clean, quick checks pass, feature branches
published. Complete source/range review precedes required longer docs checks.

## Repositories, full series and final diffs

Worktree root: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-08-documentation-governance-review/
Every branch is 2026-11-08-documentation-governance-review. All remotes are canonical
SSH. No PRs are required by the affected repo rules.

| Repository / target | Owned base | Exact final head / single owned commit |
| --- | --- | --- |
| dev-workspace / master | d2cb9975a88079d79f361c5b4c65836ba0835821 | 6587c4c1cedabee95bcc52f4667e7d33e3a82859 — docs: define documentation homes and README scope |
| workspace / master | 992ce14f295c16bcf395f25107b1fd60f0923ad8 | 1a3a10d9c9e5ef7ef7da05dc42459cf6871b6d4d — docs: map documentation homes and editor packages |
| vpsfree-dev-workspace / master | f8da821e3c76e26e73aa9d89a712eab0e0faa319 | 0c7168f352f6d4f11c46368e702b9356d81012c6 — review: require documentation routing and fidelity evidence |
| vpsadminos / staging | 4bfed8ba8ddfec49e5a3909df5ede733ea762c99 | 6154dbcd5eaea4a505168f2a7f4fdc25aed4c96d — docs: route specialist guidance out of the README |
| vpsfree-cz-configuration / master | 9e25b996034f8e05f4858dc5ec1f1246a516b109 | f3149765d2db49c5556983df2954cd368a7b0800 — docs: separate configuration reference from operations |

For each range, inspect git log --reverse BASE..HEAD and git diff BASE..HEAD.
Each owned range is exactly the one commit listed. Logical separate repositories
remain separately reviewable. Example moves bundle necessary index/nav/anchor
changes with the moved content; no unrelated behavior is bundled.

Workspace remote master was 1134fb3c833f8d835d5f59dc53867bce0d5dae7c while shared
local master/registered base was 992ce14f. Complete remote-to-feature history:
1. 4af26b17f77d136c9252e3a8d0d01ec8a7cd45b0 — workspace: archive 2026-11-03-lead-wakeup-delivery
2. 992ce14f295c16bcf395f25107b1fd60f0923ad8 — workspace: archive 2026-11-06-portal-message-delivery
3. 1a3a10d9c9e5ef7ef7da05dc42459cf6871b6d4d — owned feature commit above.
The first two are inherited shared-master tracking, not authored feature changes;
preserve them. Assess ancestry/history using metadata/stats, do not read another
session's record/file contents. They are not obsolete branch iterations.
Generic/site/config/vpsAdminOS remote targets matched their bases on owners'
prepublication fetches. Current shared tracking may advance independently;
refresh/rebase appropriately before integration, which remains unapproved.

No migrations in any owned range; none merged/released/deployed/externally
consumed. No repeated dependency/channel/input/generated update streams, no
pin changes, obsolete authored approaches or temporary compatibility paths.
Prepublication amendments are consolidated; nothing from this feature deployed.
Require your explicit whole-branch history/migration/update-stream conclusion.

## Documentation inventory and preservation

- Generic directory/README contract → developers/agents, authoring policy →
  dev-workspace skills/dev-session-documentation/SKILL.md#directory-and-readme-convention;
  human guide docs/dev-sessions.md links canonical tree. Existing subsystem and
  renderer equivalents, content-only directories and local receipt policy retained.
- Supported upgrades/moves → maintainers/agents, preservation policy → generic
  skill keep-knowledge/reconcile sections: explicit retirement evidence for old
  state/restoration/rollback, preserve unknown applicability and old anchors.
- Site mappings → agents/maintainers, local routing → workspace
  docs/agent-instructions/documentation.md. vpsAdminOS subsystem/configs reference
  equivalents, operations/upgrades, shared session rollout records, notes. Config
  AGENTS ban on deployment receipts/reports/screenshots/traces/generated artifacts
  remains authoritative; optional generic docs/deployments does not apply there.
- Optional editor package → lead/implementer, team procedure → workspace
  docs/agent-teams.md#optional-documentation-editor-package. Existing capacity only,
  protected facts/commands and factual owner, main-agent prose, independent author
  separation preserved. No role or extra review stage added.
- Routing packet → coordinator, maintained agent instructions → site review skill
  workflow step 5. Seven acceptance questions + explicit placement/preservation
  conclusion → independent reviewer, site references/general-review.md#documentation.
  Existing timing/exemptions/settings/lanes/severities/narrow-fix/history remain.
- vpsAdminOS ZFS suite → developers, how-to → docs/os/testing.md#explicit-zfs-full-suite;
  exact commands/profiles, explicit opt-in, exclusion from -t ci, isolated run state.
  Updater → maintainers, operations → docs/operations/flake-updates.md; preserves
  all graph guard/cache/failure/publication behavior and pinned confctl authority.
  README grouped navigation retains legacy anchors; MkDocs navigation added.
- Configuration overview → config maintainer, reference → configs/vpsadmin/api/README.md;
  provider validation/historical ownership/evidence disclosure/partial success
  and lasting mail deletion/retry/dedup/notification limits → abuse-notices.md.
  Checks/RT investigation/select-missing-entry recovery → operations/vpsadmin-abuse-notices.md.
- mx2 policy/checks/deployment prerequisites/persistent queue cautions → operator,
  runbook → operations/mx2.md; source-state replacement/restoration/both queues →
  operations/upgrades/mx2-centos-to-nixos.md. Old/new queue recovery preserved.
- Retention policy/irreversible cleanup recovery/separate archive compaction →
  operator, runbook → operations/aitherdev-disk-retention.md; legacy executable
  adoption/backups/restoration → upgrades/aitherdev-declarative-cleanup.md.
  Unknown transition retirement preserved; no executed-operation receipts added.
  OAuth runbook untouched. Root links/old anchors + operations index/MkDocs updated.

New canonical default-branch links become available after approved integration;
source-local equivalents were checked against these exact worktrees. No temporary
feature-branch URLs replace maintained links. Public behavior must remain readable
without private session records. Apply the proposed seven review questions to
these concrete changes as well as examining the new instruction wording itself.

## Quick checks and limits

All final owned ranges passed git diff --check and all worktrees are clean.
Lead directly applied site-writing/English-humanizer to affected prose before
commits. Corrections incorporated: canonical rendered workflow URL, directory
nesting, single procedural RT home, redundant execution disclaimers removed.

- Generic: repository Nix develop ran Markdown link/fence inspection covering
  four policy/guide files, 25 local/source-mapped links/anchors. One unchanged
  external writing URL not fetched. Generic/workspace have no declared hook
  framework or active custom hooks; commits obeyed git commit -F.
- Workspace: pinned repository Ruby ran test/agent_instructions_test.rb,
  10 tests/217 assertions, no failures/errors/skips. Full shell setup failed
  on unrelated Savannah config.sub HTTP 404; finished command, then bounded
  pinned Ruby-only environment succeeded. No source workaround/behavior changes.
- Site: nix shell --inputs-from . nixpkgs#ruby -c ruby test/skill_policy_test.rb,
  5 tests/72 assertions pass; four existing reference links checked; no hook
  framework. Check CI 42595237520 auto-started on publication, not yet monitored.
- vpsAdminOS: exact ZFS fenced command block comparison; normalized original/new
  updater paragraph comparison; all Markdown targets/fragments/legacy anchors and
  MkDocs nav targets pass. Active Overcommit config inspected and signed normally;
  narrowed pinned nixpkgs overcommit/nixfmt/ruby environment; precommit + message
  hooks pass. Full shell setup client canceled and completion reconciled; no
  kernel build or ZFS suite. No branch CI runs.
- Configuration: full provider sections preserved except heading depth, all 12
  original command fences exact, entire mx2 transition paragraph exact, protected
  Aitherdev clauses preserved, 22 local links/fragments/legacy anchors + nav valid;
  OAuth byte-identical. Repo Ruby/Psych parsed nav, bundle check passed; active
  precommit/message hooks passed in repo Nix develop. No push-triggered CI.

After accepted final review, lead will run watcher-owned docs rendering with
repository-pinned MkDocs for vpsAdminOS/configuration and monitor already-triggered
CI for exact heads. Avoid runtime/schema/VM/kernel suites solely for documentation
moves. Generic AGENTS lists packaged nix flake check; assess proportionality to
pure skill/guide text and use automatic feature CI evidence where present rather
than launching redundant unrelated system suites. The source is not installed
policy: generic/site package rollout is a separate authorization/delivery action.

## Required reviewer result

Write work/2026-11-08-documentation-governance-review/final-review.md (review/evidence
only) and report_to_lead with actual identity/settings, reviewed exact ranges,
ordered findings/severities/lanes, explicit scope and placement/preservation
conclusions, whole-history/no-migrations/update-stream conclusion and check gaps.
Remain read-only on application source; no nested reviewers. No other session
access, runtime mutation, merge/deployment, or package lifecycle action.
