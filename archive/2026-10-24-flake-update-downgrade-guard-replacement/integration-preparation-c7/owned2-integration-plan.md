# Lead-owned integration plan for the two refreshed consumers

This is a command plan, not an executing integration driver. Explicit user
approval covers both repositories' master targets. The focused independent
review and subsequent feature publication are still required. Do not acquire a
claim while either is pending.

| Repository | Detached prepared target | Expected target | Intended feature head | Prior remote feature lease |
| --- | --- | --- | --- | --- |
| haveapi | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/integration-haveapi` | `1103a3a14b1dc6dec17fc4859df80220a54f111d` | `39909094649b1d14a23f00615775ca7136acf4fd` | `c7bfc1aa5af956b6057be8e623f9035c00ccb268` |
| vpsfree-cz-configuration | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/integration-vpsfree-cz-configuration` | `bec5556f6c60414e482550dd735321ebe3c3703b` | `25258cd3f483f0116dbab35c7acf89b16eff4bbc` | `5f0f4466adb175ed4fcac9b6d5c8909e87a1fec1` |

Both targets currently have the expected detached HEAD and empty full porcelain.
The declared environments are each repository's default `nix develop` shell.
Ordinary fresh dependency/hook preparation has not yet run in these two targets.
The prepared no-argument command is:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/integration-preparation-c7/prepare-owned2-hooks.sh
```

Use a fresh watcher because fresh gem installation has uncertain duration. Capture
its full aggregate log at `integration-preparation-c7/owned2-target-hook-preparation.log`
and preserve the exit status. It runs no tests, refreshes no locks and performs no
merge/push. Stop and escalate an unexpected local kernel build. It installs and
signs ordinary Overcommit hooks after the exact target configurations and custom
hook sources have been read. Hook setup may update common Git hook/signature
metadata; no other owner is mutating these two repositories.

After preparation, review and publication, integrate one repository at a time.
The lead acquires one schema-1 repository claim for the exact registered project,
reads authoritative held status, then performs only the short critical section:

1. Recheck the exact local feature head and reviewed full range/diff, empty source
   and target porcelain, target detached HEAD and canonical SSH origin. Fresh SSH
   default and feature refs must equal the table's target and intended final head.
   Any movement requires release and assessment before changing the prepared patch.
2. In the matching detached target, use the declared shell and ordinary hooks:
   `nix develop --no-write-lock-file -c git merge --ff-only <intended-feature-head>`.
   Inspect the complete hook output as well as the status; a post-merge hook can
   fail even if Git exits zero. Do not push after such a failure.
3. Confirm target HEAD and tree equal the reviewed feature exactly, index is
   clean, full porcelain is empty and the source lock is unchanged. Then push
   normally over SSH:
   `nix develop --no-write-lock-file -c git push origin HEAD:refs/heads/master`.
4. Prove the exact remote master and feature heads using canonical SSH
   `git ls-remote --symref git@github.com:vpsfreecz/<project>.git HEAD refs/heads/master refs/heads/2026-10-24-flake-update-downgrade-guard-replacement`.
   Reconcile any uncertain push or hook effect while actively owning the claim.
   Release and verify the claim immediately once the critical section is safe,
   before CI observations or record writing.

If trust, dependencies or other preparation needs intervention, stop commands,
inspect the current HEAD/index/lock/remote effects and release before repairing
outside the claim. Do not hold ownership while waiting for review/tests or input.
No cleanup, branch deletion, lifecycle, deployment or machine action is included.

The other five consumers' target/environment/hook preparation was explicitly
handed to implementer1 through the lead. Their source heads remain unchanged.
