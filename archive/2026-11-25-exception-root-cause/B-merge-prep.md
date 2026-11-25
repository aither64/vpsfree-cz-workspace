# Unlocked merge preparation — package B

Ready; preparation mutation window returned to lead. No repository claim was
acquired, and no merge, default-branch update/push, rebase, new test, CI wait,
SDK work or lifecycle/cleanup action occurred. All preparation commands settled.

User approval, quoted by lead: "if api specs pass then that's enough verification
and you can merge it". Lead interpreted this as vpsadmin/master integration and
accepted API run 45641819759 attempt 1; B owns preparation only. No further
verification gate is introduced.

## Exact snapshot and checkout

- Repository: `git@github.com:vpsfreecz/vpsadmin.git`; canonical common Git directory
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git`.
- Target checkout: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-exception-root-cause/vpsadmin-merge-target`.
- Fresh target/remote master: `81e930b25fa3252d7e849aff4819e663cec37b07`.
- Exact reviewed local/remote feature: `6c16d04555e79c7789ac7213da2064c540afc83c`,
  branch `2026-11-25-exception-root-cause`.
- Target is freshly created detached HEAD at the target SHA; final
  `git status --porcelain=v1 --untracked-files=all` output was empty.
- Fresh fetch and SSH ls-remote agreed on both refs. Ancestor check exited 0;
  feature fast-forwards from this target without rebase.

Complete series matches [R1](review.md) and [R2](review-policy.md): runtime fix
`da7724abdc080e59820cc4f0812ce1a41b3fc5df`, then documentation rule
`6c16d04555e79c7789ac7213da2064c540afc83c`. Four changed files, 75 insertions /
37 deletions. R2's delta is AGENTS.md and docs/api-schema-export.md only.
No migrations, obsolete/fixup history, repeated dependency/generated update
streams or transitional compatibility paths remain. The declaration-neutral
client exemption is accepted. B's CI receipt stays bound to runtime da7724ab;
no CI-at-documentation-head claim is made.

## Prepared environment and hooks

Read workspace Git/coordination/commits procedures, current repository guidance,
and the selected package's complete `workspace-host coordination guide`:
`/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0`, coordination
catalog `sha256:93fcabc6aee6f3c80605723e4cbe7dacc4f18277da0f09e67549badf97b5ca22`.
Identity/current and both environment markers matched; live roster confirmed
implementer0's bound thread and saved workspace_write access.

The fresh target's ignored `.gems` and `api/.gems` symlink to the corresponding
prepared directories in sibling `vpsadmin`; ignored root/API Gemfile.lock files
were copied from that source. Gemfiles, flake inputs and hook configuration/plugins
are identical between target base and reviewed feature. Existing feature checkout
and refs remain retained; no dependency reinstall campaign was needed.

In target cwd, `nix develop .#vpsadmin --command bash -euc ...` completed ordinary
`bundle exec overcommit --install`, `overcommit --sign`, `overcommit --sign
pre-commit`, root `bundle check` and explicit API-bundle `bundle check`, all exit 0.
Configuration signed, every custom plugin signature verified, both dependency
sets satisfied. Ruby 3.4.12, Bundler 4.1.1, Overcommit 0.76.0, root RuboCop 1.85.1,
nixfmt and php-cs-fixer were available. No hook bypass or hook test run occurred.
Worktree creation session 81442 and setup session 61804 completed successfully.

Shortest ready prefix for the lead is **from target cwd**:
`nix develop .#vpsadmin --command bash <lead-owned-driver>`.
Enter Nix before acquiring ownership; acquire the one repository claim inside the
lead's prepared driver so shell dependency setup stays outside its critical section.
Lead performs fresh ref/cleanliness checks, ordinary fast-forward/hooks, SSH push
and remote proof under its short claim, then releases before records or cleanup.
If target/feature moved or a hook needs intervention, return to unlocked preparation.
B has not executed that driver or acquired ownership.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-exception-root-cause/>.
