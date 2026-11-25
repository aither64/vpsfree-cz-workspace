# Hosted advisory diagnostic — committed review packet

Prepared 2026-11-14 by implementer0. **Published once after review and D1 closure.**
No local API examples ran. Hosted diagnostic outcomes are root-owned and pending
at this owner handoff; no terminal pass/failure is claimed. This diagnostic ref must be retained and is not a merge candidate.

## Scope and exact source

Implement the [architect-owned hosted brief](design.md#hosted-two-example-diagnostic--current-package-2026-11-14)
after the accepted STOP of the local matching-software attempt. One fixed hosted
job tests only the two original failed IDs and seeds, sequentially, stopping at
input mismatch or first example failure. No application, spec, helper, selector,
API, schema, dependency declaration, pin, ordinary workflow or default branch
change is included. No local API examples, project build or guest/image launch occurred.

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-api-advisory-diagnostic`
- Diagnostic branch: `2026-11-14-api-advisory-diagnostic`
- Parent/direct base: `7919441ccb8e9587ad0afc84674b074ca9c5a880`
- Frozen head: `dbe74d30dd9b880691762494abc1158169d58ac0`
- Tree: `535f5aca9c42f5d68655c6988092aedfe34efaf2`
- Tracked status: clean; one direct commit, exactly two added files.
- Direct complete range: `7919441..dbe74d30`, [full diff](nov14-diagnostic-final.diff),
  [commit details](nov14-diagnostic-direct-series.txt), [machine receipt](nov14-diagnostic-final-receipt.json).

The two files are `.github/workflows/api-advisory-diagnostic.yml` (233 lines)
and `.github/diagnostics/api-advisory-frozen.lock` (350 lines, 8283 bytes).
The lock is copied byte-for-byte from independently recovered originals; SHA256
`7e2f9babb3b733a438ab5a77c8bf813ae53a32025df1ce55990a2270fec69e51`. Parser proof is 122 unique gem/version pairs,
130 platform specifications because prism has nine variants. No lock content was
normalized, regenerated or rewritten.

## Complete inherited history and migrations

Complete inherited range: `2d0946c4e699aa61092228d8a7cb275477ee46d0..dbe74d30dd9b880691762494abc1158169d58ac0`.
[Full five-commit details](nov14-diagnostic-inherited-series.txt) and
[whole inherited path inventory](nov14-diagnostic-inherited-inventory.txt):

- `ee48c91c1348ee335fe2d384d2dffa4b73bde95f api: share escalation across registered incident types`
- `fb6d1f22bc4e00e28923fe13a10b1e6bac4762f9 webui: show registered incident escalation settings`
- `ef8901db845c52784c331cf20edb9157f20b66d1 docs: explain isolated MariaDB locking settings`
- `7919441ccb8e9587ad0afc84674b074ca9c5a880 api: localize ordinary oomd incident reports`
- `dbe74d30dd9b880691762494abc1158169d58ac0 ci: isolate advisory examples with frozen diagnostic inputs`

All product paths and all existing workflows are byte-identical to parent7919:
`git diff --exit-code 7919441 HEAD -- .` with only the two diagnostic additions
excluded returned0. Published7919 worktree remains clean at tree
`f4a9d5b18805b23f8c22a493ce4b2f74b508f161`.

The [retained backend review](nov13-backend-review.md#exact-reviewed-repository-range)
cleared all four lanes for exact2d09..7919; its
[migration conclusion](nov13-backend-review.md#migration-conclusion) remains
unchanged. The direct diagnostic range has **no migrations**. The inherited
single additive migration `20261030180000_add_incident_escalation.rb` and core
schema remain byte-identical to reviewed7919/oldf60, with no abandoned draft,
existence guard or new predecessor path. Recorded migration execution is owned
disposable local/hosted fixture DBs only; no merge/release/production deployment or
externally persisted predecessor demonstrated. No migration execution is claimed
for this diagnostic.

One diagnostic commit introduces its final workflow and frozen input directly;
no superseded approach, fixup, repeated dependency/pin/update stream or transitional
migration remains. The four inherited product commits stay as already reviewed,
published and consumer-bound; no product source clearance is being reopened.

## Trigger and immutable-action proof

[SSH preparation evidence](nov14-diagnostic-ssh-preparation.txt) proves canonical
`git@github.com:vpsfreecz/vpsadmin.git`, default master2d09, published feature7919,
and no existing remote diagnostic ref at preparation time. Fresh publication
before/after proof below re-established that same boundary, followed by one push.

Only one new commit is to be pushed, with its parent already published7919.
GitHub [new-branch diff semantics](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#git-diff-comparisons)
use a two-dot comparison against the parent of the deepest new commit. The
resulting diff has only the two paths above. All13 workflow event definitions and
actual path filters were inspected: [trigger inventory](nov14-diagnostic-trigger-inspection.json).
None of the12 ordinary workflows matches; the new diagnostic alone has the exact
branch push trigger. There are no PR/tag/schedule/manual/reusable interfaces, no
matrix, no workflow_run listener, no arbitrary selector and no auto-cancellation.
Deletion events are guarded. Read-only contents permission and both checkouts'
`persist-credentials: false` prevent persisted Git credentials. No deployment or
custom transport is used. [Captured comparison](nov14-diagnostic-capture-comparison.txt)
binds direct base/head.

Latest official repository release metadata and tag resolution were checked:

- checkout v7.0.1 → `3d3c42e5aac5ba805825da76410c181273ba90b1`
- ruby/setup-ruby v1.338.0 → `b3aaceaef7e0ee231b499e7b5f49c03fc1d32199`
- upload-artifact v7.0.2 → `cf430e030ddbb5b0abf93d22962f4752f3646cd9`

All equal the original-run candidates and are currently compatible official
Node24 actions for hosted Ubuntu26.04. Metadata, exact action.yml and READMEs are
retained as `nov14-diagnostic-action-*`; no older-version exception is needed.

## Gates, failure behavior and evidence

The workflow first checks out its event SHA solely to retain the digest-checked
lock outside checkout. It then checks out exact7919 and restores the same lock to
ignored `api/Gemfile.lock`. Source HEAD and lock digest are checked before/after
each example. BUNDLE_FROZEN is set before the setup-ruby cache action.

Hard gates: Ubuntu26.04; Ruby3.4.12; Bundler2.6.9; frozen full graph; all plugins;
RACK_ENV=test; SPEC_MODE=full; BUNDLE_WITHOUT=development; jobs4/retry3; exact
Ubuntu MariaDB server/client/common/core and libmariadb3/dev/dev-compat
`1:11.8.6-5ubuntu0.1`; actual server/client11.8.6; actual temporary DB
REPEATABLE-READ and innodb_snapshot_isolation0. Available package versions are
recorded before exact installation. Missing exact inputs stop with zero examples.

The hosted image build/kernel drift is recorded and accepted only as a
controlled software comparison, not original Ubuntu-image equivalence. No alternate
Ruby/SQL versions, package search, global helper, container or compilation workaround
is added. Ordinary frozen-gem native-extension setup is the permitted setup path.

Exact separate processes from api/, using existing automatic DB startup/cleanup:

1. `bundle exec rspec 'spec/api/resources/security_advisory_spec.rb[1:3:1]' --seed 42376 --format documentation --format json --out "$EVIDENCE_DIR/matching-software-operations.json"`
2. `bundle exec rspec 'spec/api/plugins/outage_reports/security_advisory_spec.rb[1:3:1]' --seed 55119 --format documentation --format json --out "$EVIDENCE_DIR/matching-software-plugins.json"`

No continue-on-error. Each native RSpec exit is preserved through tee; ordinary
step success dependencies skip the second after a first failure. Always-run
outcome/evidence steps use the neutral absent-exit marker, with actual step
outcomes/logs authoritative for skipped or interrupted execution. One seven-day artifact
contains identities, exact lock, package/gem/OS/image/DB inputs, gate outputs,
example stdout/stderr, native exits and native JSON when produced. Standard action
setup output also remains in the native job log. No credential dump, complete
environment dump, dependency directory or cache archive is uploaded. Timeout is
incomplete evidence, never an application diagnosis. Budget30minutes; expected
10–20minutes, without a duration guarantee.

Both pass would establish isolated nonreproduction only. Original fulloperations
243/1 seed42376 and fullplugins337/1 seed55119 failures in terminal run43528601962
remain unresolved; distinct coreoperations243/0 is not relabeled or pooled.
Existing failure/native input evidence remains in
[diagnosis](nov14-api-failure-diagnosis.md) and
[input recovery](nov14-ci-input-recovery.json). Primary43528601963/native99295
is an independent lead-owned unresolved fence; no observation or action on it
occurred in this package.

## Quick checks and normal hooks

Final workflow/static input checks passed:

- YAML parse and fixed trigger/job/permission/deletion/budget/no-continue inspection.
- `nix shell --inputs-from . nixpkgs#actionlint nixpkgs#shellcheck -c actionlint .github/workflows/api-advisory-diagnostic.yml`: actionlint1.7.12, exit0.
- All seven extracted inline scripts: `bash -n` and `shellcheck --shell=bash`,
  ShellCheck0.11.0, exit0; actionlint includes workflow expression checking.
- Exact lock hash/size, both recovered-copy comparison,122 unique gem/version proof.
- All13 workflow triggers/path filters; exact two-file staged diff/whitespace.
- Normal `nix develop --offline --command ... git commit -F <temporary-message>`:
  [terminal commit log](nov14-diagnostic-commit-final.log), native38255 exit0;
  Nixfmt, MigrationSpecs, API/WebUI locale health all pass, commit-msg hooks pass.
  TextWidth warns on two message lines over72; all lines meet repository limit80.

Preparation failures are retained: worktree post-checkout signature gate repaired
by verified Overcommit --sign; first commit exit1 for missing API hook bundle
[log](nov14-diagnostic-commit.log), then read-only reuse of existing matching
cached7919 API bundle through an own ignored symlink and copied ignored lock.
No original bundle/source mutation, API tests, hook bypass or dependency restore.
The root hook shell allocated53MiB ignored gems; lint tools substituted3.8MiB
compressed/14.4MiB store outputs. No heavy local allocation.

The local hook bundle uses project Nix Ruby3.4.9 and the original cached hook lock;
that is **not** represented as matching diagnostic runtime. Only static/hook
checks ran locally. Hosted runtime gates are now root-owned; this packet does not
infer their results from initial run status.
Earlier draft actionlint caught an unavailable runner context; this was moved to
GITHUB_ENV initialization. The standalone shell checker initially needed an explicit
Bash dialect; final checks use it. Failed evidence is retained, not promoted.

## Review and documentation placement

Lead reports completed retained reviewer0 all-four-lane review of original298a8746:
no Blocking/Important, sole AdvisoryD1. The exact two-line wording correction
was folded into the owning commit; no reviewer rerun is requested. Lead closed mandatory step9 by direct inspection and released the one push. The named
lead-owned report is nov14-hosted-diagnostic-review.md.

Original reviewed head298a8746837ccf1bea6e375f120746ed51244443/tree
2a3460b17a97747eed7e6cb7d2769ab89c830025 is retained under
`refs/retained/2026-10-30-oomd-abuse-policy/api-advisory-diagnostic-298a8746`;
[original evidence snapshot](nov14-diagnostic-reviewed-298a8746/nov14-hosted-diagnostic-packet.md).
[Exact old-to-new diff](nov14-diagnostic-d1-old-to-new.diff) and
[range-diff](nov14-diagnostic-d1-range-diff.txt) contain only the comment and marker:
`no native exit recorded; see step outcome/logs`. The comment covers skipped or
interrupted execution. No command, step, gate, classifier or assertion changed.
Timeout remains incomplete evidence.

Affected YAML/workflow/actionlint plus the single affected inline Bash/ShellCheck
and whitespace checks pass (native58285 exit0). Normal Nix amend hooks pass;
[log](nov14-diagnostic-d1-commit.log), inner exit0 recorded in
nov14-diagnostic-d1-commit.exit. Native49091 returned1 only from the outer login
shell logout's unbound variable after that success. Commit log, exact resulting
Git head/parent and clean status reconcile the completed effects; no retry or
hook bypass occurred. Existing generic72-column warnings remain within the
repository80-column limit. No unrelated quick checks or API tests were repeated.

Temporary operational decision/evidence belongs in this session packet and
architect brief, with workflow-local scope text. No permanent product reference,
API, KB, deployment or upgrade documentation change is useful for a dedicated
nonmerge diagnostic. No documentation moves or factual product changes occurred.
The source/schema/export/client/KB input streams remain exact7919: retained export
schema SHA f919dcebf8ce5453dce6b0eb09e718f72664b5137443bb8e2064ff6452470ca7,
provenance d9f839fac6bf45c5d92d7a7a83cc49a5328a5c136bd7e11539b5c955a5208bdd,
tooling lock2e9a124eff7b80d6fd57cd0f03cb2809847c67cc7f1af6364911c3622d7242a0.
No generator, client, React or KB refresh is required or performed.

## One publication and CI observation handoff

Lead closed D1 by direct inspection and released exactdbe/tree535f. Fresh canonical
SSH evidence and explicit default/product fetch prove defaultmaster2d09,
publishedproduct7919 and absent diagnostic ref before push. Exact7919 parent,
one new commit/two-path diff,7e2f lock and reviewed trigger fanout matched.
No rebase or source mutation occurred.

One ordinary `nix develop --offline --command git push origin dbe74d30dd9b880691762494abc1158169d58ac0:refs/heads/2026-11-14-api-advisory-diagnostic`
returned0 (native75997). Independent SSH afterward proves diagnostic=dbe while
default2d09 and product7919 remain unchanged. [Publication receipt](nov14-diagnostic-publication-receipt.json),
[exact argv](nov14-diagnostic-publication-argv.json),
[before SSH](nov14-diagnostic-publication-before.ssh.txt),
[after SSH](nov14-diagnostic-publication-after.ssh.txt),
[push log](nov14-diagnostic-publication-push.log) and
[comparison](nov14-diagnostic-publication-comparison.txt) are retained.

One initial exact-head inventory made two provider reads: one branch/head-filtered
push-run query and one exact-run/attempt job query. It returned only diagnostic
run **43551864218 attempt1**, workflow417981819, job132315936018; run and job were
initiallyin_progress at2026-11-14T03:30:07Z, with no conclusion. This is automatic
selection evidence, not runtime acceptance. [Raw identities/native argv](nov14-diagnostic-initial-ci-handoff.json),
[initial run JSON](nov14-diagnostic-initial-runs-1.json) and
[initial jobs JSON](nov14-diagnostic-initial-jobs.json) are retained.

CI observation was transferred to **ROOT** in report
3543d2c7-ce1e-4226-a6a8-7999052d8c44. Owner0 launched no watcher and performs no
further CI queries. All local commands/effects are terminal; hosted run terminal
observation is root-owned. Primary43528601963/native99295 was not queried/joined.
No rerun/dispatch/cancellation, alternate software/topic/predecessor attempt,
consumer refresh, source/default rewrite, merge, deletion or lifecycle action.
Session remains open; original failure status is unchanged pending diagnosis.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
