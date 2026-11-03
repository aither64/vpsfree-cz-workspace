# Nullable channel revision

Owner: implementer1. Phase: implementation, focused regression evaluation and
hooked commit complete. Commit: `52fba5ee5aac2e171375a780d3860a86e71e5d65`.
Exclusive Git/config writer authority is released to the lead. All owned
commands and the verification utility have completed with no uncertain effects.

The lead authorized this independent package from the root-cause report and
direct brief. Session identity and retained `workspace_write` access match the
bound session. The lead transferred sole Git/config writer authority for this
package. Both owned paths are committed and the worktree and index are clean.

`os/modules/installer/cd-dvd/channel.nix` now omits the `.git-revision` write
when `system.vpsadminos.revision` is null. For a known revision, the existing
`echo -n` command and value are preserved. No empty or invented revision is
substituted. The existing nullable option, source selection, framework metadata
transport, original image commits, and other files are unchanged by this package.
No production deployment is involved. Existing channels with known revisions
retain their format; rollback only restores the prior null evaluation failure.

`tests/channel-revision-eval.nix` follows the existing standalone Nix evaluation
convention. It imports the actual channel module and the real version option
declarations, enables channel registration, forces real `pkgs.runCommand`
channel derivation evaluation, and checks the generated revision-write commands
for null and a known SHA. It checks the channel consumer and complete generated
command rather than reimplementing the conditional under test.

Direct command from the vpsAdminOS repository root (no flake registration needed):

```sh
nix eval --impure --raw --file tests/channel-revision-eval.nix
```

Both owned Nix files passed parsing, and Nixfmt passed under the repository's
`nix develop` shell. The shell restored missing development dependencies before
the first check; no kernel build was observed. One fresh `gpt-6-luna` / `low`
watcher ran the exact evaluation command once after the lead confirmed the
max-one utility slot was free. It passed with exit 0 in 27 seconds and printed
`channel derivations handle unknown and known revisions`. The utility has
finished, so its slot is free. Pinned and installed catalog digest:
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`.
The matching native utility specifies full access and approval policy `never`.
Evaluation log: `/tmp/redhat-channel-revision-eval.log`; exit receipt:
`/tmp/redhat-channel-revision-eval.exit`.

The focused commit used a temporary message file with `git commit -F` under
`nix develop --command`. Pre-commit Nixfmt and all commit-message hooks passed;
signature verification remained enabled and no bypass was used. Post-hook
whitespace and clean-status checks passed. The original image head
`3307df52ea5bf875e1d8a23318a64f569d8b3ebc` remains an ancestor. There are no
migrations or obsolete intermediate commits in this package.

The evaluated source was that original image head plus the two owned edits.
Their post-commit SHA-256 hashes are unchanged from the watcher's tested input:

- `os/modules/installer/cd-dvd/channel.nix`:
  `ae6178ea0e3d45a45bada780e553ed06d71113f7e142d6013252bd1254cd5091`
- `tests/channel-revision-eval.nix`:
  `431e875666abd15c9103de57f80e1d92ae56c812b5a261844fc878abdd452603`

No broad system build, image tests, push, merge, or production deployment is
authorized for this package. The lead owns whole-deliverable review and later
release verification. No product documentation change is useful for restoring
this internal option contract; the direct regression command is documented here
and in the test itself.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)
