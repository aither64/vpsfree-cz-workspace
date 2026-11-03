# CentOS package and hook preparation

Completed by implementer0 on 2026-11-03 under the accepted [design](design.md).
Exact session identity matched; saved `workspace_write` access passed a temporary
create/write/read/remove probe in the assigned worktree.

Repository: `vpsadminos`; branch: `2026-11-03-redhat-image-releases`.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-redhat-image-releases/vpsadminos`.
Baseline: `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.

| Image | RELEASE change | Final commit |
| --- | --- | --- |
| centos-9-stream | `9.0-36.el9` to `9.0-38.el9` | `09f209688616b60155e9ac99fa8431a11b9e20a0` |
| centos-10-stream | `10.0-21.el10` to `10.0-23.el10` | `a3c7c77459762d1a45f323de0f3f8dd5d8447323` |

The complete baseline-to-head diff contains exactly two RELEASE lines, one per
image commit; no migrations. POINTVER and URL layout are unchanged. Both scripts
passed `bash -n`; working and committed diffs passed whitespace checks. Commits
used temporary message files with `git commit -F`; installed pre-commit and
commit-msg hooks passed without final warnings. Nixfmt passed; enabled RuboCop
has no applicable Ruby files. The final index is empty and both Rocky edits
remain unstaged. No push, merge, registration retry or long image test was run.

## Hook setup and reusable environment

From the repository root, use `nix develop --command <command>`, for example:

```sh
nix develop --command git commit -F /tmp/<message-file>
```

The default shell was prepared by a fresh `gpt-6-luna`/`low`, full-access watcher
using matching installed/pinned catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`.
Setup passed (exit 0, about three minutes, 44 gems); no kernel build was observed.
Logs: `/tmp/redhat-implementer0-nix-setup.log` and
`/tmp/redhat-implementer0-nix-setup.exit`. No command remains running.

Reviewed `.overcommit.yml` and sole plugin `.git-hooks/pre_commit/nixfmt.rb`, then
ran `overcommit --install`, `overcommit --sign`, `overcommit --list-hooks`, and
`overcommit --sign pre-commit` under that shell. The installed post-checkout hook
also passed with the baseline as old/new head and branch-checkout flag `1`.
Signature verification remains enabled (`overcommit.configuration.verifysignatures=1`);
no bypass/skip/no-verify environment was used. The original registration-time
signature error did not reproduce; the existing signatures were already correct
under this shell and remained unchanged. Its original environment cause is unproven.

Dependency receipt:

- Shell derivation: `/nix/store/5b6vmc0axa4m6pj9c77jdhjrgvyvviav-vpsadminos.drv`.
- Shell output: `/nix/store/clb3g6xxb2alirs5c9nqd8y0kj8fi03k-vpsadminos`.
- Ruby 3.4.11: `/nix/store/z30vypx0r6mgbfs0a86m6vd3s7pk07sb-ruby-3.4.11/bin/ruby`.
- Nixfmt 1.5.0: `/nix/store/7kcwslr98ahgivprci1qfzgmi6mrgjds-nixfmt-1.5.0/bin/nixfmt`.
- `.gems`: Overcommit 0.74.0, RuboCop 1.75.8, Bundler 4.0.23.
- Shell sets `GEM_HOME=$PWD/.gems`, `RUBYLIB=$GEM_HOME`, and prepends its gem bin directory to PATH.
- GEM_PATH: `/nix/store/bmy1s5r1iqjm11l5pd06gifhlyqkbr6d-bundix-master-1b7df693/lib/ruby/gems/3.4.0:/nix/store/z30vypx0r6mgbfs0a86m6vd3s7pk07sb-ruby-3.4.11/lib/ruby/gems/3.4.0`.
- `flake.lock` SHA-256: `604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`.
- Ignored `Gemfile.lock` SHA-256: `881e6831ec46b6a55fd1e1f2e39e70a9eb4967f896dad568bf8b2224b99310ae`.
- Configuration signature: `e3f2ddb1e18d2a523f15e00a16db7d86774bbeb8ab9d8c576ae6c48add48389d`.
- Plugin signature: `88afa3f1dd658c4d8ba603683f332e26814f9e0db33153c438ed6244ebabdc14`.

No project documentation change is needed: existing repository instructions and
the release-update skill cover this operation. The lead owns state reconciliation,
whole-branch review, required image tests and publication. Exclusive Git/config
writer authority is released to the lead for transfer to implementer1.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)
