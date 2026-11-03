# vpsadminos staging integration preparation

Preparation only; no claim, merge or default-branch push has been performed.
The lead owns verification acceptance, merge claim, final check, fast-forward,
SSH push, remote proof and immediate claim release.

- Repository: `git@github.com:vpsfreecz/vpsadminos.git`.
- Target: `refs/heads/staging`.
- Prepared target path:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-fedora-45-image-build/vpsadminos-staging-integration`.
- Reviewed feature: `refs/heads/2026-11-03-fedora-45-image-build`, exact
  `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
- Fresh fetched target/base: `5918f94e5e4eef3733b60aca4e03c1a6c0d43748`.
- Full history: one logical `image-scripts: add fedora-45` commit, three files,
  29 insertions and one deletion. No migrations, obsolete history or repeated
  update streams. Independent final review passed on this exact range.
- Selected guide read in full: installed `share/dev-workspace/coordination.md`
  from `/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`.
  Coordination catalog SHA-256:
  `b17a5618c6ce3988022bd02962d4dad95d735568fc4b2717ce462364e41eab6d`.

Preparation passed. Target is clean and detached at the exact base. Ordinary
post-checkout hook completed during creation, and explicit post-merge/pre-push
hook entrypoints accepted target configuration trust without a merge or push.
Full setup output: [integration-worktree-preparation.log](integration-worktree-preparation.log)
and [integration-hook-preparation.log](integration-hook-preparation.log).
The target is detached so final integration uses `HEAD:refs/heads/staging`;
no other session checkout/branch is reused.

## Lead commands after all verification is accepted

Use the repository's already-prepared Nix environment and active hooks. From
a fresh Bash command shell, source the captured minimal hook environment
before taking a claim:

```sh
source /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-fedora-45-image-build/integration-hook-environment.sh
```

This captures only command PATH and Ruby/Bundler paths, from the successful
repository `nix develop` command. It reuses the feature worktree's existing
`.gems`; hooks run against the target with `git -C`. No hook bypass or trust
override is set. If any prepared tool path has since been collected, restore
the Nix environment before claiming. Avoid installing Bundler or restoring
development packages under the merge claim.

Immediately before claim acquisition, fetch and verify the prepared baseline.
Under the exact held vpsadminos claim, inspect target cleanliness, exact feature
head, and fresh remote target. Refuse stale baseline/changed head and release
before repairing outside ownership. Expected values are listed above.

Then, from the prepared environment:

```sh
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-fedora-45-image-build/vpsadminos-staging-integration merge --ff-only dd188397abe37d0bc33f4c5dfb3605206ce5e326
```

Inspect all ordinary hook output and reconcile any nonzero/uncertain effects
before continuing. A zero Git merge status alone does not establish post-merge
hook success.

```sh
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-fedora-45-image-build/vpsadminos-staging-integration push origin HEAD:refs/heads/staging
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-fedora-45-image-build/vpsadminos-staging-integration ls-remote origin refs/heads/staging
```

Prove exact remote staging equals the intended final feature head, then release
the exact claim and verify released status before CI, records or checkout
cleanup. Do not create a merge commit, use force push, delete feature refs, or
perform any session lifecycle action. Retain original failure/verification
receipts. User integration approval is recorded by the lead; this file supplies
no additional approval or authority.
