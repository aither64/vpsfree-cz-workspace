# Final integration preparation

Package H, implementer1, prepared at `2026-11-25T15:27:50Z`. No integration
approval, repository claim, merge, default push or activation was executed.
No feature head/source/pin or E immutable snapshot changed. No product build/test
was run; declared target shells and hook dependencies were prepared only.

## Exact sources and fresh targets

| Repository / canonical origin | Fresh target master | Approved-for-review feature head | Prepared integration checkout |
| --- | --- | --- | --- |
| dev-workspace / `git@github.com:aither64/dev-workspace.git` | `91cafd4c0c50ffb7208498a605707c4c3b1b1174` | `f6d60bf87002fb1896599f35f0284743c16d7e6f` | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/.merge-targets/dev-workspace` |
| configuration / `git@github.com:vpsfreecz/vpsfree-cz-configuration.git` | `9bdb0c68b47ceebde450fcdf018727b382cacc09` | `fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81` | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/.merge-targets/vpsfree-cz-configuration` |
| workspace / `git@github.com:aither64/vpsfree-cz-workspace.git` | `e7b876f69aca4554d52a3ac19ed097263847ad43` | `30b74dc3278728ab36197e0d2ef2cf76c66cf791` | existing shared `/home/aither/workspace/ai/vpsfree.cz`, kept on master |

Fresh origin fetches still equal the accepted bases. Target is an ancestor of
each exact feature; each final series contains one commit, no migrations or
unreviewed baseline changes. Existing review/mechanical-refresh receipts own
history and verification; no parent review or tests were repeated.

Runtime/configuration checkouts were created with ordinary
`git --git-dir=CANONICAL worktree add --detach PATH EXACT_TARGET`. Both are clean
and detached at their exact target, with canonical common Git directory/origin.
Detached targets avoid occupying another master checkout; after an approved
fast-forward they can push `HEAD:refs/heads/master` normally. No workspace master
checkout was created elsewhere. Raw target observations: `/tmp/archive-failure-h-targets.json`.
Leave these checkouts in place; H performs no cleanup.

## Environments, hooks and trust

Current runtime/configuration AGENTS and routed Git, commits, verification and
coordination instructions apply. The selected installed package remains1zn;
its unchanged coordination guide/policy was already read in full and governs the
claim section. Current site deployment and transition guides remain as recorded
in rollout; this package grants no deployment action.

- Runtime target: declared `nix develop --no-write-lock-file` works; Git2.54.0,
  Ruby3.4.9. Repository declares no hook framework and has no active hook entries
  (only `.sample` files). Log `/tmp/archive-failure-h-runtime-environment.log`.
- Configuration target: ordinary post-checkout hook passed by creating the target
  within the already prepared declared configuration shell. Its own declared shell
  then prepared local ignored gems; `bundle check`, Overcommit0.76.0 and Nixfmt1.5.0
  are ready under Ruby3.4.12. Log `/tmp/archive-failure-h-config-environment.log`.
- Configuration uses existing shared Overcommit hooks; target configuration trust
  was signed normally with `bundle exec overcommit --sign`. Signature verification
  stays enabled (`overcommit.configuration.verifysignatures=1`), with no bypass
  variables/options. Effective hook policy was read, not executed as a test;
  `/tmp/archive-failure-h-config-hook-policy.json` records trusted configuration
  and enabled hooks.
- Fast-forward merges make no commit, so pre-commit and commit-message hooks do
  not run again; they already passed on the final generated feature commit.
  Git runs the existing post-merge hook on fast-forward, and normal push runs
  pre-push. Current effective PostMerge/PrePush have no enabled checks; keep their
  ordinary wrappers and trust checks active. Nixfmt/RuboCop remain configured for
  commit preparation. No hooks or signature settings were disabled.
- A post-merge hook failure can accompany Git exit0. Lead must inspect the actual
  merge/hook diagnostics before push. A failure/intervention returns to unlocked
  preparation after command effects are known; never repair while holding a claim.

Keep coordination commands outside configuration's Ruby3.4.12 GEM environment:
the installed dev-session wrapper is Ruby3.4.9. Run target Git steps through the
already warmed declared shell, for example:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/.merge-targets/vpsfree-cz-configuration
nix develop --no-write-lock-file -c git merge --ff-only fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81
nix develop --no-write-lock-file -c git push origin HEAD:refs/heads/master
```

These commands are for the approved lead section below, not executed by H.
Shell preparation is complete outside ownership. Unexpected dependency/hook work
at execution is a reason to stop, reconcile and release before repair.

## Shared workspace preservation

Shared checkout is master at e7. Index has no staged changes; flake.nix/flake.lock
have no working-tree changes. There are211 unrelated dirty tracked paths; none
were edited or staged. Feature touches only the two clean flake paths. Logical
index entries SHA-256 `109d64c6198dc32dc7552229efc79777576e391266743529ec1ee6f9eb2c2214`
and index flags SHA-256 `fe0ced9cac7d03b5c01cdc9b01e430b1dd2352b0b75e0df81f78b4b0aaa5bb0a`
matched before/after target preparation. H never changed shared branch/index/files;
this evidence file is its assigned session record. Snapshot
`/tmp/archive-failure-h-shared-before.json` is evidence, not authority to discard
later concurrent work.

## Lead's later short claim section

Preconditions: explicit user integration approval for each named repository/master;
mandatory isolated VM and all E results accepted; final review/mechanical refresh
accepted; final feature/target heads and environments still match. Deployment
approval does not supply integration approval. Root owns all authority/freshness
and mutation drivers. Use one repository-only claim at a time and release it
before CI, records or cleanup. Keep machine ownership separate.

Prepare one fresh UUID request per repository before acquisition:

```json
{"schema":1,"requestId":"FRESH_UUID","label":"Integrate approved archive preparation fix","repositories":["REPOSITORY"],"machines":[]}
```

`REPOSITORY` is `dev-workspace`, `vpsfree-cz-configuration`, or `workspace`.
Ordinary commands, run with exact verified session identity:

```sh
dev-session coordination acquire 2026-11-25-archive-failure-investigation --as-is --request REQUEST_FILE --json
dev-session coordination claim-status 2026-11-25-archive-failure-investigation --as-is --id CLAIM_UUID --json
```

Only held status admits the section. A queued request owns nothing. Immediately
before merge, for each clean detached target recheck these facts (substitute the
exact row's BASE and FEATURE; run Git in its prepared target/environment):

```sh
git remote get-url origin
git rev-parse HEAD
git status --porcelain=v1
git rev-parse refs/heads/2026-11-25-archive-failure-investigation
git ls-remote origin refs/heads/master
git merge-base --is-ancestor BASE FEATURE
```

Require canonical origin, HEAD=BASE, empty status, feature ref=FEATURE and fresh
remote master=BASE. A changed baseline/source, dirty target or hook intervention
means stop and release once effects are known; reconcile outside ownership, not
under the claim. Do not silently merge a moved/unreviewed default.

Then use the exact feature from the table:

```sh
git merge --ff-only FEATURE
git rev-parse HEAD
git status --porcelain=v1
git push origin HEAD:refs/heads/master
git ls-remote origin refs/heads/master
```

Inspect merge/hook results before push, require local HEAD=FEATURE and clean
target, then require fresh remote master=FEATURE. Push is SSH, non-force, with
ordinary hooks. Reconcile rejected/interrupted/uncertain mutations by actual
local/remote refs before releasing; a process exit is not remote proof.

For shared workspace, obtain its repository claim **first**, then try its tracking
lock without waiting:

```sh
exec 9>/home/aither/workspace/ai/vpsfree.cz/.git/dev-session-tracking.lock
flock -n 9
```

If busy, release the workspace claim immediately rather than wait. If acquired,
hold both through fresh remote/feature/master checks, `git merge --ff-only 30b74dc3278728ab36197e0d2ef2cf76c66cf791`,
normal `git push origin master:refs/heads/master` and exact remote proof. Recheck
master=e7, clean flake paths and preserve unrelated logical index/flags/files;
stage nothing and do not reset/stash/clean/switch the shared branch. The claim
does not replace this lock. Do not acquire it in H or before approval.

After each repository's verified section, inspect exact claim status, release
through its owner command and verify released status, before records/CI/cleanup:

```sh
dev-session coordination release 2026-11-25-archive-failure-investigation --as-is --id CLAIM_UUID --json
dev-session coordination claim-status 2026-11-25-archive-failure-investigation --as-is --id CLAIM_UUID --json
```

For shared workspace, release the tracking FD after the protected section as
well (`flock -u 9`; close FD9). No unconditional error trap should release an
uncertain mutation. No further repository claim may remain held while waiting
for tests, approval, records or the next integration.

No merge approval is present at H handoff. E's isolated VM remains the delivery
dependency; its owner supplies that result. Prepared targets and hooks are ready
for fresh lead checks without a new source/test iteration.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-archive-failure-investigation/
