# vpsadminos/staging integration preparation

Functional preparation is complete. GitHub SSH authentication failed during
publication, but the subsequent bounded diagnostic authenticated successfully
with the default file key. Feature republication and fresh remote proof remain
lead-owned. No repository claim was acquired by implementer0, and implementer0
did not merge or push staging. Lead owns integration.

## Exact history

- Reviewed old range:
  `8ce6234db194ccb934db724c7262aeab7fd26915..4642beb9c37c558e1d0b74e285fecdda16d62eca`.
- Refreshed range:
  `a5ad64f818a7a208e5f2308295c14c6a776eea6d..05201326975fc19d20a545c52f651cce0420dbc9`.
- One commit in each range: `osctl-oomd: ignore queued misses after pruning`.
  `git range-diff` reports `=`. Ordered stable patch IDs are identical:
  `03c4fef73a0a3b73624a7c37b0d7fc077164bbc1`.
- Complete `git diff --binary --full-index` SHA-256 for both ranges:
  `342195c7798b58cce628ec498397e6387141b97b559cda699691a0dc3374383c`.
- Both final diffs contain two files, 101 insertions and one deletion. No
  migrations, obsolete commits, API/protocol changes or deployment lineage.
- Old head remains at local
  `backup/2026-10-30-osctld-oomd-investigation-reviewed`. Published feature was
  last proven at the old head; the refreshed local branch is clean.
- The new base changes only osctl-exporter packaged Rack 3.2.7 to 3.2.8.
  `flake.lock`, oomd source/specs and dependency inputs are unchanged.
- Lead reports independent acceptance of the refreshed history/equivalence.
  The session comparison is captured for the exact new range.

## Checks and prepared target

Feature checkout:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-osctld-oomd-investigation/vpsadminos`.

Detached target checkout:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-osctld-oomd-investigation/vpsadminos-integration`.
Its clean HEAD is `a5ad64f818a7a208e5f2308295c14c6a776eea6d`.

- Refreshed focused killer specs: 14 examples, zero failures; component suite:
  41 examples, zero failures. Log: [oomd-patched-ruby-checks.log](oomd-patched-ruby-checks.log).
- Reused exact patched Ruby output:
  `/nix/store/z30vypx0r6mgbfs0a86m6vd3s7pk07sb-ruby-3.4.11`, from
  `/nix/store/bfxm7qnf2wj1kcrklzd5r4yn78jnvz56-ruby-3.4.11.drv`.
  It was restored as an isolated build, retained by `oomd-patched-ruby`.
- Scoped RuboCop passes both files. `overcommit --diff a5ad64f...` passes
  Nixfmt and RuboCop; [oomd-refreshed-hooks.log](oomd-refreshed-hooks.log).
- Target root bundle dependencies are satisfied. Overcommit 0.73.0 is loaded
  from the existing feature `.gems` bundle. Configuration/plugin signatures were
  registered normally after inspecting unchanged `.overcommit.yml` and Nixfmt
  plugin. No hooks were disabled or bypassed.
- Target's actual `post-merge 0` and empty-input `pre-push` hook commands each
  exited zero. All PostMerge hooks are disabled by the unchanged configuration;
  ordinary merge still invokes the installed hook. Installed hook inventory:
  [oomd-target-hooks.txt](oomd-target-hooks.txt).
- [oomd-prepared-env.sh](oomd-prepared-env.sh) contains explicit PATH, GEM_HOME
  and GEM_PATH from the declared component Nix shell; its profile is retained by
  `oomd-component-shell`. Set BUNDLE_GEMFILE to the feature checkout's root
  Gemfile. No Nix entry or dependency installation is needed under a claim.

## Authentication boundary and resumption

Ordinary ambient Git and the prepared environment initially failed GitHub SSH
public-key authentication. SSH_AUTH_SOCK was absent and no current-user agent
was found. That absence did **not** establish the cause: a later single bounded
`ssh -vvv -T -o BatchMode=yes` test successfully offered, signed with and
authenticated using `/home/aither/.ssh/id_ed25519`. GitHub identified the account
as `aither64`; exit 1 reflects GitHub's lack of shell access, not failed auth.
The public fingerprint was
`SHA256:38gX47C2LkQgccktDtHa27hPk8wXo3kXLMGUQSnswK0`.
The private-key file was inspected only through metadata: regular non-symlink,
0600, user 1000, mtime 2024-03-16; directory 0700. No certificate exists.
GIT_SSH/GIT_SSH_COMMAND/GIT_SSH_VARIANT and repository SSH overrides were unset.

The original successful push log contains no authentication trace or agent
environment, so its exact identity source cannot be proved retrospectively.
The earlier rejection's cause remains unknown; a transient rejection is observed,
not explained. No evidence links it to Nix, garbage collection or a removed key.
No credentials, peer files, trust settings or services were changed. Evidence:
[github-ssh-diagnosis.log](github-ssh-diagnosis.log). No agent restoration or other
authentication mutation is justified by the current successful trace.

The failed fetch did not reach its subsequent lease-push. Original feature CI
runs were both completed; no superseded run needed cancellation. The lead retains
exclusive Git ownership. Existing vpsadminos/staging merge approval remains
applicable; ordinary SSH transport should be freshly verified before resumption.

Before a claim: use the prepared environment,
freshly fetch and verify staging remains the prepared base, publish the equivalent
feature with an exact old-head lease, verify remote refs and cancel only obsolete
queued/in-progress runs for this same feature branch. If staging moved again,
return to unlocked preparation.

```sh
source /home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-osctld-oomd-investigation/oomd-prepared-env.sh
export BUNDLE_GEMFILE=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-osctld-oomd-investigation/vpsadminos/Gemfile
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-osctld-oomd-investigation/vpsadminos
git fetch origin
test "$(git rev-parse origin/staging)" = a5ad64f818a7a208e5f2308295c14c6a776eea6d
bundle exec git push --force-with-lease=refs/heads/2026-10-30-osctld-oomd-investigation:4642beb9c37c558e1d0b74e285fecdda16d62eca origin 2026-10-30-osctld-oomd-investigation
```

Lead then acquires the single repository claim. In the same prepared environment,
recheck clean target HEAD, exact feature and fresh remote staging under the claim;
perform ordinary fast-forward and SSH push only if all still match:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-osctld-oomd-investigation/vpsadminos-integration
git fetch origin
test -z "$(git status --porcelain)"
test "$(git rev-parse HEAD)" = a5ad64f818a7a208e5f2308295c14c6a776eea6d
test "$(git rev-parse origin/staging)" = a5ad64f818a7a208e5f2308295c14c6a776eea6d
test "$(git rev-parse 2026-10-30-osctld-oomd-investigation)" = 05201326975fc19d20a545c52f651cce0420dbc9
bundle exec git merge --ff-only 05201326975fc19d20a545c52f651cce0420dbc9
# Inspect actual post-merge hook outcome before pushing.
test "$(git rev-parse HEAD)" = 05201326975fc19d20a545c52f651cce0420dbc9
bundle exec git push origin HEAD:refs/heads/staging
git ls-remote --heads origin refs/heads/staging
```

Verify exact remote head and release the claim before CI or records. Stop,
reconcile effects and release before repairing stale preparation or hooks.
No cleanup, deployment or session lifecycle action is authorized by this receipt.
