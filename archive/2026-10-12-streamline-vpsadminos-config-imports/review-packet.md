# Independent final review packet (awaiting committed source head)

Session: `2026-10-12-streamline-vpsadminos-config-imports`, exact bound workspace
`/home/aither/workspace/ai/vpsfree.cz`. User authorized implementation of the
accepted plan, not merging/deployment/production KB publication.

## Outcome and acceptance

Modern stable imports follow the guest's evaluated nixpkgs release; exact
releases use `nixosModules.containers."26.05"`; underscores remain compatible;
unstable remains explicit. Both modern generic names are the same selector.
Unknown releases fail before build/activation with known keys and guidance.
Generated stable flakes use `containerStable`; version pins, stateVersion,
compatibility settings, raw modules and legacy aliases retain their contracts.

Read `plan.md` and architect-owned `design.md` for accepted interface and checks.
No containerAuto, channel-suffix guessing, unknown=>unstable fallback, daemon
changes, production pin update or coordinated all-machine deployment is wanted.

## Review lanes and policy

Use `/home/aither/.codex/skills/mandatory-change-review/SKILL.md`, all four lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Risk is high because modern generic Nix module behavior changes intentionally
and the documentation covers guest upgrade/rollback and persistence. Reviewer0
is retained Sol/xhigh, read-only, independent. Do not override saved settings,
edit source, spawn nested reviewers, or run integration tests. Inventory the
complete series/final diff and explicitly conclude history and migration
soundness. Preserve the narrow-fix workflow.

## Source scope and lineage

Canonical repo `repos/vpsadminos.git`, feature worktree
`worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos`.
Initial/base revision `1150e37b1cc997b1728f2fda806a3433ef55b798`, upstream `staging`.
Final head, complete commit list and final diff will be attached after quick
checks pass and commit. No database or on-disk migrations exist. No repeated
production dependency/channel update streams; production flake.lock unchanged.
Historical nixpkgs fixtures are exact test-only24.11/25.11 revisions and hashes.

Code/tests/project guide belong together as one bounded feature commit: tests
and docs validate the same new public module contract. The image test extension
validates its ordinary/impermanence generated-config consumers and preserves
existing boot/network/DNS/rebuild coverage. No obsolete branch iteration was
published/deployed/externally consumed; earlier test fixture fixes are folded
into this owning initial feature commit.

Legacy downstream consumers discovered during planning: both configuration
repositories' profiles/ct.nix use `nixosConfigurations` module aliases. Preserve
these latest-stable/unstable values, so no configuration-repo edits are needed.
Standalone downloaded files must remain usable without companion imports.
The nested `containers` output is a deliberate documented convention extension:
import leaves; focused leaf tests replace reliance on shallow flake validation.

## Committed KB deliverable

Shared workspace master contains coordination plan/design at50f733ed and six
candidate pages/source snapshots/localized schema-5 manifests at2784facf.
Review only session-owned paths at that commit; unrelated workspace/index
changes are outside scope. Candidate files are under `kb-candidate/`; exact
source text/revision/checksum records under `kb-review-source/`; summaries in
`release-changes.yml`; manifests `kb-release-{cs,en}.yml` (3pages each).
`kb.diff` and `kb-review.md` are readable convenience artifacts. Main agent owns
writing skill pass with English and Czech profiles; all executable examples
match by language. Four historical-page pins/stateVersions remain unchanged.
New/changed visible navigation is limited to the English Impermanence Features
instruction using the existing `vps.features.open` path already bound to that
page; existing rescue/mount/UserData paths were inspected. No WebUI code change
or screenshot/managed-page contract expansion was undertaken. Evaluate any
remaining baseline annotation gap against the accepted import-only scope and
report concrete findings; do not silently turn this into a general KB rewrite.

## Verification and delivery limits

Source known quick parse/format/bash/whitespace passed. MkDocs passed; one
pre-existing nav warning for unrelated os/faulted-write-ci-handoff.md.
Candidate checksums/schema-5 manifest generation passed;14Nix expressions parsed,
2unchanged flake-URI command arguments excluded; bilingual parity passed.
Historical source fetches passed; first evaluator hit getFlake's store-string
context restriction in test fixtures (fixed before commit); no selector result
was inferred from that failure. The corrected full module matrix passed all outputs, including real24.11/25.11/
26.05 and all8original-file comparisons. The next template check found a plain-
path getFlake source lacked revision metadata; a test provenance correction is
being applied. Remaining template/standalone/KB/hooks results will be attached
before review starts.

Long integration checks start only after this independent final review. Four
current image-scripts cases planned; a fresh utility watcher owns execution.
No production host/guest was deployed. New public KB examples must wait for
new API availability on public default source and exact staged-page approval.
KB staging is owned by another session with a pending release and is untouched.
Artifact registration currently refuses unfinished creation, while same-session
team assignment/worktree registration function; no metadata rewrite/cleanup.

Rollback: keep prior guest lock and NixOS generations. To use older vpsAdminOS
without grouped exports, revert grouped imports together with the source pin.
Normal guest stateVersion and persistence data are unchanged by this interface.

## Final committed inventory and quick checks

Source final head: `148832fb1cca24983328ef48697a9e1235ebc031`.
Complete base-to-head series: exactly one commit,
`148832fb1 os: select NixOS guest compatibility by release`.
Source final diff: `vpsadminos-final.diff` (13paths,635insertions/25deletions).
All intended code/test/project-doc changes are committed, worktree clean.
There are no obsolete approaches, follow-up residue, migrations, or repeated
production dependency update streams. Historical test fixtures are pinned once.
No feature head has been merged/released/deployed/externally consumed.

KB final committed head: workspace2784facf; complete session-owned series:
50f733ed initial plan/design/registration, then2784facf KB deliverable. Source
snapshot files are exact production text; inherited blank-line whitespace is
retained deliberately for guard hashes. Changed candidate/manifest files pass
whitespace checks. `workspace-kb-final.diff` inventories only that KB commit;
`kb.diff` shows source-to-candidate changes so the substantive edits are clear.

Quick evidence:
- Real module/alias/release matrix: all outputs true, retained in
  `quick-module-eval-attempt-2.log`. Source fixtures fixed prior to commit.
- Four rendered template checks: all true, `quick-templates-eval.log`.
- Channel-correct copied-single-file standalone: exit0,
  `quick-standalone-eval.log`.
- Actionable unknown-release errors: exit0, `quick-negative-eval.log`.
- Exact KB UserData24.11 and Impermanence25.11 evaluated toplevels: exit0,
  `quick-kb-eval.log`; early state path `/persistent/var/lib/nixos`.
- Full declared hooks Nixfmt/RuboCop: exit0, `quick-hooks.log`.
- Hook-enabled source commit passed pre-commit and commit-msg hooks. TextWidth
  emitted72-column advisory warnings; all lines satisfy repository80-column rule.
- Parser/format/shell/whitespace checks passed, documentation build passed.

Final-head template provenance reevaluation is running before review assignment;
its exact output/status will be attached. Do not start review until instructed.

Final-head template provenance check completed exit0 at clean committed
148832fb1cca24983328ef48697a9e1235ebc031; all four template checks true.
`final-template-eval.log` and `.status` prove this check. Generated lock revision
is the actual committed feature head, which contains the release-aware exports.
All required quick checks are complete; independent final review may start now.

## Final prescribed remediation inventory

Review completed on148832fb1/KB2784facf. I1 message-only amendment produces
7e79afd4690ff5abac2554fd2a02ba8e8c97c0b1; old/new trees identical. B1 candidate
remediation63d9495a and companion2d11b2cc8445a695e7862af18ca0a70598afb38b
(basece2c8cd9358c3636e5d39343e595df813a0b197f) contain only requested paired
creation annotations (two per language), bindings/counts/discovery reconciliation
and existing English Features binding. Companion onecommit/3files38+25-, no
migrations/repeated streams/obsolete history. Lead focused inspection under
reviewer's steps9–10 instruction; no new design/public behavior. All quick/static
checks and strict bin/check pass. Full-corpus baseline discrepancy remains only
two unrelated IP-address pages, reproduced before/after; six candidates pass
independent full-discovery/count/hash inspection. See review-reconciliation.md.
Final amended-head templates passallfour; both branches published, not integrated.
