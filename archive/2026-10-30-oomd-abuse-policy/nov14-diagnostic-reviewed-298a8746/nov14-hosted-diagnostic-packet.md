# Hosted advisory diagnostic — committed review packet

Prepared 2026-11-14 by implementer0. **Not pushed; no diagnostic examples run.**
The first push is execution and remains held for retained independent review and
lead release. This diagnostic ref must be retained and is not a merge candidate.

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
- Frozen head: `298a8746837ccf1bea6e375f120746ed51244443`
- Tree: `2a3460b17a97747eed7e6cb7d2769ab89c830025`
- Tracked status: clean; one direct commit, exactly two added files.
- Direct complete range: `7919441..298a874`, [full diff](nov14-diagnostic-final.diff),
  [commit details](nov14-diagnostic-direct-series.txt), [machine receipt](nov14-diagnostic-final-receipt.json).

The two files are `.github/workflows/api-advisory-diagnostic.yml` (233 lines)
and `.github/diagnostics/api-advisory-frozen.lock` (350 lines, 8283 bytes).
The lock is copied byte-for-byte from independently recovered originals; SHA256
`7e2f9babb3b733a438ab5a77c8bf813ae53a32025df1ce55990a2270fec69e51`. Parser proof is 122 unique gem/version pairs,
130 platform specifications because prism has nine variants. No lock content was
normalized, regenerated or rewritten.

## Complete inherited history and migrations

Complete inherited range: `2d0946c4e699aa61092228d8a7cb275477ee46d0..298a8746837ccf1bea6e375f120746ed51244443`.
[Full five-commit details](nov14-diagnostic-inherited-series.txt) and
[whole inherited path inventory](nov14-diagnostic-inherited-inventory.txt):

- `ee48c91c1348ee335fe2d384d2dffa4b73bde95f api: share escalation across registered incident types`
- `fb6d1f22bc4e00e28923fe13a10b1e6bac4762f9 webui: show registered incident escalation settings`
- `ef8901db845c52784c331cf20edb9157f20b66d1 docs: explain isolated MariaDB locking settings`
- `7919441ccb8e9587ad0afc84674b074ca9c5a880 api: localize ordinary oomd incident reports`
- `298a8746837ccf1bea6e375f120746ed51244443 ci: isolate advisory examples with frozen diagnostic inputs`

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
and no existing remote diagnostic ref at preparation time. Recheck that exact
boundary before a later released push; no push has been attempted.

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
outcome/evidence steps mark missing examples as not run. One seven-day artifact
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
checks ran locally. The workflow's hard runtime gates are unexecuted until release.
Earlier draft actionlint caught an unavailable runner context; this was moved to
GITHUB_ENV initialization. The standalone shell checker initially needed an explicit
Bash dialect; final checks use it. Failed evidence is retained, not promoted.

## Review and documentation placement

Recommend all four lanes for this affected diagnostic (conservative High risk for
hosted code/credential and immutable-input execution boundaries). Retained reviewer0
remains independent, saved Sol/xhigh; lead owns assignment and final disposition.
Require explicit direct-range and inherited-history/migration conclusions, scope,
frozen checkout/lock, gate/skip/exit/artifact, credential and trigger inspection.
Do not re-clear unchanged product source merely to confirm inheritance.

Temporary operational decision/evidence belongs in this session packet and
architect brief, with workflow-local scope text. No permanent product reference,
API, KB, deployment or upgrade documentation change is useful for a dedicated
nonmerge diagnostic. No documentation moves or factual product changes occurred.
The source/schema/export/client/KB input streams remain exact7919: retained export
schema SHA f919dcebf8ce5453dce6b0eb09e718f72664b5137443bb8e2064ff6452470ca7,
provenance d9f839fac6bf45c5d92d7a7a83cc49a5328a5c136bd7e11539b5c955a5208bdd,
tooling lock2e9a124eff7b80d6fd57cd0f03cb2809847c67cc7f1af6364911c3622d7242a0.
No generator, client, React or KB refresh is required or performed.

Next action is retained independent review and lead execution release. After that,
one exact new run may be observed under separately assigned ownership; no observer
has been launched and no provider live query occurred here.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
