# Root rebase before Overcommit configuration exists

Related initiative:
`work/2026-07-13-security-advisory-automation/`

Rebasing the root history of the new security-advisories repository can run
Overcommit's post-checkout hook at a replay point before `.overcommit.yml`
exists. The hook then reports `Errno::ENOENT` for that file even though Git can
complete the rebase successfully.

Run the rebase inside the repository's `nix develop` shell, inspect the final
exit status and worktree, then run the complete RSpec and RuboCop checks on the
final tree. Do not treat the transient hook message alone as a failed rebase.
