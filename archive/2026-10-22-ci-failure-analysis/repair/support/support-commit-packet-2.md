# Support logical-owner commit preparation

Status: preparation only; no Git window, checks rerun, checkout, staging,
commit, ref movement, build or VM selected by this packet.

Recorded UTC: 2026-10-22T21:37:06.875134+00:00. Observed/required parent:
`405a802857093176883e0f173589b433756a9647`, tree
`29b00319a5aedaa44a56d60bc6d0b70083a8ac16`, parent reader
`c2c5a006b49730d8b72d103ff063a1e89bba1ee2`.
Independently verified HEAD, parent, tree, exact four Podman committed paths,
committed/working byte equality, empty index and unchanged five support hashes.
The required fixture dependency is now present. Source remains frozen; no lead
Git window is granted. No reader/runtime edits are required or included.
This packet supersedes only the parent/environment preparation in
support-commit-packet.md; that original receipt is retained unchanged.

## Frozen five-path source

| Path | Bytes | SHA256 |
| --- | ---: | --- |
| `tests/suite/upgrade/common.nix` | 221265 | `47d170c3761dc75ad5a9abe59a22dfa68559cf7e949ad9971bb1a727a92ae3eb` |
| `tests/all-tests.nix` | 10436 | `23181b97cf66510dfbf57da68de883a72f7cc99e7811df2cb9b9b49098c13c01` |
| `tests/suite/upgrade/from-6.12-guests-first-switch.nix` | 459 | `6434d151db1a3b8cf2f5a2f7aee00a02f6ecb0a9e307517d0be204fc1cd028dd` |
| `tests/suite/upgrade/impermanence_first_switch.rb` | 7700 | `9da85be832bf52420267be875c39f47ff621031d9e367f4ebc0ecd957be61a3c` |
| `docs/os/testing.md` | 29222 | `7f357e57bd781f4a58a9b54cfb09d399666956f6b7be2598143f8a3007baa78c` |

The helper already includes the caused empty-file fix; it belongs to this one
initial diagnostic owner, not a later fixup. The source regression driver stays
in session evidence: `check_capture_file.rb` SHA256 `bdd56ef5bb1caa846193f2bae9744755d1b408cc06adf523174a0f8f31dda56c`.
The previously committed datasets/updates docs remain exclusively in c2c5a006;
they are not part of this support commit. Preserve all hotplug/Podman peer files,
ignored gems, source snapshot, roots, prepared JSON and capture1 evidence.

Commit text is exactly [support-commit-message.txt](support-commit-message.txt),
SHA256 `1ac91148121aa23d138b4b11d90a2487016fdce22cbcb6bd4c1eee39a6a1a411`. No invented authorship, sign-off, release version,
component pin or migration is added. This is one distinct manual diagnostic and
its shared registration/docs; no persisted format, API or node update change.

## Available checks and remaining quick gates

- `capture-file-fix-checks.json`: exact helper9da85, actual-function empty-file,
  binary/exact-limit/truncation/missing-file regression passes; same check against
  retained helper72370 reproduces the nil.bytesize failure. Host syntax and
  RuboCop passed. This proves the small helper repair, not a successful VM.
- `documentation-checks.json`: exact testing.md7f357 plus source hashes, whitespace,
  fences and links checked. Lead accepted technical fidelity/style; no rewrite.
- `brief.md` records prepared Nix parse/nixfmt and host/embedded Ruby syntax.
  Exact immutable baseline graph/config/preparation/capture receipts remain
  separate. Capture1 activation succeeded but the old recorder failed after
  pool import: there is no post-switch root/data/API or recovery pass.
- Final hook/check execution is still pending the lead window. In the isolated
  staged tree run normal pre-commit and commit-msg hooks, not a bypass or manual
  lint substitute. Check the actual five-path staged diff and syntax/format below.
  The final all-tests two-case membership has no new runtime/evaluation claim.

Prepared quick commands (not run by this packet), from isolated checkout:

```sh
nix-instantiate --parse tests/all-tests.nix >/dev/null
nix-instantiate --parse tests/suite/upgrade/common.nix >/dev/null
nix-instantiate --parse tests/suite/upgrade/from-6.12-guests-first-switch.nix >/dev/null
nixfmt --check tests/all-tests.nix tests/suite/upgrade/common.nix tests/suite/upgrade/from-6.12-guests-first-switch.nix
ruby -c tests/suite/upgrade/impermanence_first_switch.rb
ruby /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/check_capture_file.rb tests/suite/upgrade/impermanence_first_switch.rb
ruby -e 'source = File.read(ARGV.fetch(0)); guest = source.split("FIRST_SWITCH_CAPTURE = <<~" + 39.chr + "CAPTURE" + 39.chr + ".freeze\n", 2).fetch(1).split("\nCAPTURE\n", 2).first; RubyVM::InstructionSequence.compile(guest); puts "embedded guest syntax OK"' tests/suite/upgrade/impermanence_first_switch.rb
bundle exec rubocop tests/suite/upgrade/impermanence_first_switch.rb
git diff --cached --check
```

If final registration eval is selected, obtain only attrNames from
`(builtins.getFlake (toString /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos-support-commit)).testsMeta.x86_64-linux`
with `nix eval --impure --json --option allow-import-from-derivation false
--expr 'builtins.attrNames (...)'`, once with diagnostic environment unset and
once set1, VPSADMINOS_CONFIG empty. Verify the exact two names are absent then
present and ordinary name sets equal. Direct testsMetaOne fallback is not proof
of suite registration. This eval is not required for hook preparation and is
not selected here; uncertain duration goes to a fresh lead watcher. No
realization, IFD, kernel build or VM is permitted by that query.

## Hook-safe serialized isolation method (not executed)

1. After lead grants a window and supplies the completed Podman parent, reverify
   binding, exact HEAD, its reader ancestry and four committed Podman paths.
   Require empty shared index and all five hashes above. Inventory/hash every
   other tracked and ordinary untracked peer path before mutation. Record exact
   original owner bytes and modes under `repair/support/commit-backup/`; retain
   the two new files there through final verification. Refuse unexpected changes.
2. Enter the already prepared declared environment from the primary worktree:
   `nix develop --command bash <the then-selected bounded preparation script>`.
   Retain its selected Ruby and existing installed44-gem hook environment. Set
   GEM_HOME/RUBYLIB to the primary worktree's `.gems` and preserve the selected
   Ruby default gems in GEM_PATH; owner1 proved REXML is otherwise omitted:

   ```sh
   export GEM_HOME=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos/.gems
   export RUBYLIB="$GEM_HOME"
   export GEM_PATH="$GEM_HOME:/nix/store/m0nfdb4mhfgwkgss4ymyqmvviwy30i6y-ruby-3.4.9/lib/ruby/gems/3.4.0"
   ```

   No gem installation or bypass is needed for this environment correction;
   do not rerun a shellHook inside the isolated checkout or silently add tools.
   Verify existing reviewed Overcommit hooks/config/custom Nixfmt signatures;
   never set SKIP, OVERCOMMIT_DISABLE or an alternate bypass hooksPath.
3. Create only the clean detached native worktree
   `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos-support-commit`
   at that exact parent. Copy only the five accepted paths, preserving mode,
   then stage exactly these paths there. Review full staged diff; require no
   other staged paths. Normal post-checkout hooks must run. Do not put checkout,
   Git objects or hooks under a process-wide output file-size RLIMIT: an earlier
   peer preparation failed with signal25 from that limit. Bound retained log
   output separately and preserve its status. If shell/environment setup becomes
   uncertain or over1min, stop for lead's fresh watcher rather than self-launch.
4. Run the focused quick commands and normal commit with
   `git commit -F /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/support-commit-message.txt`.
   Require ordinary pre-commit/commit-msg success. Preserve the exact new commit,
   tree, parent, five-path bytes and hook receipt; inspect no other source changed.
   Report for lead's source-receipt/commit release before touching shared files.
5. Only upon lead's explicit feature-FF release, require shared HEAD still equals
   the recorded parent, empty index and all five original hashes unchanged.
   Restore just the three owned tracked paths to the parent; move just the two
   exact owned untracked files into retained own backup (no broad clean/reset).
   Then `git merge --ff-only <verified-isolated-support-commit>` on the feature
   branch with normal hooks. Keep recovery bytes until five-path equality,
   exact HEAD/index and every peer hash are verified. On any uncertainty stop
   and reconcile effects; never discard peer data or silently retry.
6. Release the lead Git window with exact commit/source/hook/peer proof before
   any isolated-checkout removal. Removal of a clean disposable checkout is a
   separately selected native worktree step, no force/broad cleanup. No push,
   integration/default-branch mutation, new runtime pass, lifecycle action or
   automatic reviewer assignment is authorized by this packet.

The owner1 Podman dependency is verified. Only the subsequent lead Git
window is pending. No source change or architectural deviation is proposed.
