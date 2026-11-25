# SDK main/tag/release preparation — root execution only

Same bound session and live roster44 confirmed; implementer2 retained
Sol/xhigh/workspace_write/full_access. Prior candidate and affected reviewd4bcc0dd
accepted. New user authority reported by lead: “merge it all” and “and yes you can
publish the typescript client”. Root owns claim, default/tag mutations and release
approval. This package performs preparation only. React/config stay frozen.

## Settled tuple and environment

Canonical SSH: git@github.com:vpsfreecz/vpsadmin-typescript-client.git.
Target refs/heads/main = 2da950a98fa13468b36d03b13fb5e81cca206e0e.
Feature refs/heads/2026-10-30-oomd-abuse-policy =
d8cb484748db8687554822772a98a1f873414d65, tree
56cad7425584d4566da2f2c39a311b3fa54dbe2f.
v0.5.0 absent locally/remotely, including peeled ref. Exact default is ancestor;
full four-commit series and binary diff still equal accepted candidate evidence.
No migrations or source/history drift. Exact candidate remains345047B/SHA256
9cf9a37506e5af19611b27956f582e8a4860da1f22fc63941ef5b0c4bdb796d9;
no pack/build/check repeated.

Prepared disposable detached target:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-typescript-client-release-target
HEAD is exact2da950a9, clean tracked/index and no untracked files. Feature remains
clean d8cb. Normal Git identity valid. No repository AGENTS or declared hook
framework at default/feature; core.hooksPath unset; shared hooks directory has no
non-sample hook. No hook bypass/trust modification. Existing environment.json
contains declared resident pinned Git2.56.0, Node24.21.0/npm11.19.0, Ruby3.4.11,
gnutar1.35 paths. Use these directly; do not rerun nix develop/restore optional
interactive-shell closure. Original admission/truncation qualification preserved.

[Preparation facts](preparation.json), [fresh SSH](fresh-ssh.txt), [scoped fetch](fetch.txt),
[target creation](worktree-add.txt). Fetch used empty refmap/no tags/no FETCH_HEAD
and create-only own observation refs. No remote/default/tag/profile mutation,
claim or cleanup. Disposable target remains for root, not removed at handoff.

## Executable normal integration sequence

These commands are prepared instructions, NOT executed here. Root first takes
only the registered vpsadmin-typescript-client repository claim through installed
coordination acquire and verifies held status. Use current guide for exact claim
request/release. No shared tracking lock is needed for this independent repository.
The critical section covers fresh checks, ff merge, normal non-force main push,
remote proof and (if root chooses the same short section) tag creation/push/proof.
Release before Actions status/approval/wait/records. If any fresh tuple moved or hook
requires repair, stop/reconcile and release before repairing outside the claim.
Do not hold the repository waiting on the protected release.

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-typescript-client-release-target
export PATH=/nix/store/xgw813vgzl2q0696sq45adpj0xd690jq-git-2.56.0/bin:/nix/store/f9shc46n2300jbm0h60f6s4m69j0smyp-gnutar-1.35/bin:/nix/store/j1j9b0w3mhpccdli73ycj5w7nf6fkzqz-nodejs-24.21.0/bin:/nix/store/jnjll1yxfq02bdcw5pjf9gl86wh8gfhq-ruby-3.4.11/bin:$PATH
git ls-remote --symref git@github.com:vpsfreecz/vpsadmin-typescript-client.git HEAD refs/heads/main refs/heads/2026-10-30-oomd-abuse-policy refs/tags/v0.5.0 'refs/tags/v0.5.0^{}'
git status --porcelain=v1
git rev-parse HEAD
git rev-parse refs/heads/2026-10-30-oomd-abuse-policy
git merge-base --is-ancestor 2da950a98fa13468b36d03b13fb5e81cca206e0e d8cb484748db8687554822772a98a1f873414d65
```

Require main/HEAD2da950a9, featured8cb, absenttag, targetclean/HEAD2da950a9;
then the normal ff-only merge and non-force push are:

```sh
git merge --ff-only d8cb484748db8687554822772a98a1f873414d65
git rev-parse HEAD 'HEAD^{tree}'
git status --porcelain=v1
git push --porcelain git@github.com:vpsfreecz/vpsadmin-typescript-client.git HEAD:refs/heads/main
git ls-remote git@github.com:vpsfreecz/vpsadmin-typescript-client.git refs/heads/main refs/heads/2026-10-30-oomd-abuse-policy
```

Require resulting target/publicmain exactd8cb/tree56cad and no failed hook despite
Git exit0. Preserve feature/default old refs and original candidate evidence.
Only after main readback and fresh absent-tag proof, create ordinary annotated
version tag (normal Git tag signing configuration remains enabled as applicable):

```sh
git tag -a v0.5.0 d8cb484748db8687554822772a98a1f873414d65 -F /home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/nov23-sdk-0.5-candidate/integration-preparation/tag-message.txt
git push --porcelain git@github.com:vpsfreecz/vpsadmin-typescript-client.git refs/tags/v0.5.0:refs/tags/v0.5.0
git ls-remote git@github.com:vpsfreecz/vpsadmin-typescript-client.git refs/heads/main refs/tags/v0.5.0 'refs/tags/v0.5.0^{}'
```

Require main and tag peeled commitd8cb; retain actual new tag object. A moved/existing
tag or uncertain push requires read-only reconciliation, never force/move/retry blindly.
Root releases its exact claim after terminal remote proof, before any release wait.

## Ordinary protected release

Existing .github/workflows/release.yml, workflow397566387, tagpushv0.5.0 is the
supported automated route. Branch/manual builds never publish. Existing
NPM_RELEASE_ENABLED=true; environment release/id25494232596 requires aither64;
tag filterv*. Current authenticated gh user is aither64 (identity-only read).
These setup observations and previous canonical0.4 successful OIDC run/provenance
are retained in parent directory; npm publisher account settings were not directly
read, no unconditional account-permission guarantee.

Tag build validates source and produces its own immutable Actions archive+receipt.
It may run only once: no full tag rerun. Local accepted archive is retained and not
repacked/rebuilt in this package. A tag-run receipt is distinct from the local
candidate receipt; root must bind exact source/version/archive bytes before
approving the original protected publish artifact. Do not substitute an archive.
No need to change release configuration, workflow or credentials.

Once the actual tag run ID is known through a finite inventory/ordinary operation,
read its pending release approval and approve only matchingrun/head/tag/environment.
Prepared gh API forms (RUN_ID is the actual observed tag run, not branch45232064276):

```sh
gh api repos/vpsfreecz/vpsadmin-typescript-client/actions/runs/RUN_ID/pending_deployments
gh api --method POST repos/vpsfreecz/vpsadmin-typescript-client/actions/runs/RUN_ID/pending_deployments --input /home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/nov23-sdk-0.5-candidate/integration-preparation/release-approval.json
```

No run exists yet; these approval commands have NOT run. Poll/watch is not part
of this preparation. After actual publication, verify exact registry0.5.0 integrity,
archive/source/provenance and required members before releasing React adoption.
Uncertain publish: reconcile registry/originalrun and originalartifact first;
retry only failedpublishjob if needed, never rebuild/repack/movetag/replaceversion.
No npm login/manual fallback attempted.

All preparation handles terminal; no active children/cells/watchers. Native41838
joined0, only SSH/fetch/worktree-read operations. Integration target retained.
Source/Git preparation window/capacity returns ROOT ONLY. No claim/default/tag/
registry/CI/profile/host/demo/lifecycle action performed; session stays open.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
