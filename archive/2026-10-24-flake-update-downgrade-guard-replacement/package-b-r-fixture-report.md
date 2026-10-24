# Package B exported-check fixture correction

Clean local candidate R is `5436d3d7c36d3d5174eab3c44e3578830749d3db`,
parent `7ba361d22a4aac044cb02abf8397800bcf5726bf`. It replaces the local
packaging commit Q; the feature still has two coherent commits. R has not been
published. All seven consumers still pin published P
`bdaed19e901237e05bd0a779f368e76cb311143f`. Publication and repinning remain held
until the lead accepts the exact exported check and subsequent review.

The lead's serialized watcher has now passed the exact immutable R exported
check: 197 examples, zero failures, zero pending, exit 0, approximately 63
seconds. Coverage/status and retained package/check/source closures are under
`/tmp/flake-update-guard-b-r-rspec-2026-10-24-1`; outer log
[provider-r-rspec.log](provider-r-rspec.log). This resolves the fixture gate.
Publication and the complete consumer pin/history review remain separate gates.
The original frozen command below records the completed operation.

## Retained failures and cause

P's exported check ran 197 examples with one failure: Git could not execute the
generated pre-commit hook because its `/usr/bin/env` shebang is unavailable in
the declared Nix sandbox. Q selected `env` from the declared PATH and asserted
that it was executable, but applied `File.realpath` before writing the shebang.

Q's exported check also ran 197 examples with one failure. The retained
`/tmp/flake-update-guard-b-q-rspec-2026-10-24-1/check-build.stderr` reports the
coreutils usage message before the hook's Ruby starts. Its `status.json` binds
exit 1 to the rspec phase and exact Q
`578cb6fa9a5b2a325a255e8c54423a4551a114ae`. The derivation is
`/nix/store/gpv2rf668dlfa5d3d91164y1cs3zffkm-confctl-rspec-578cb6f.drv`.

A bounded dispatch probe in the declared `nix develop` shell confirmed that
`/nix/store/mhv491ysr5xqajfipq4r18wcqhjw4smz-coreutils-9.11/bin/env` is a symlink
to `coreutils`. Executing the named `env` path with `ruby -e` succeeded; executing
its dereferenced path with the same arguments exited 1 with the matching usage
message. The executable basename selects the multicall applet. This diagnoses
the failed check; it does not replace the exported-check proof.

## Correction and quick checks

R uses `File.expand_path(env_bin)` instead of `File.realpath(env_bin)` and adds
the dispatch-name invariant comment. Q to R changes only these two fixture lines
plus their replacement line. P to R changes only the fixture. Production wrapper,
guard, input graph, docs and environment contract are identical to P.

The hook still runs through real Git. The absolute declared executable remains
asserted; the shebang keeps its `ruby` argument so the simulated caller PATH
chooses Ruby. Preload, BUNDLE settings, gem, interpreter, marker and resulting Git
commit assertions remain intact. No sandbox exception or environment clearing
was added.

Focused RuboCop and `git diff --check` passed in `nix develop`:
[package-b-r-lint.log](package-b-r-lint.log). Ordinary Nixfmt, RuboCop and
commit-message hooks passed during the local amend:
[package-b-r-commit.log](package-b-r-commit.log). The existing commit message
has a soft 72-column warning; its lines satisfy the required 80-column limit.
The worktree is clean. No migrations exist or changed.

Full inventory: [package-b-r-inventory.json](package-b-r-inventory.json).
Narrow deltas: [Q to R](package-b-r-from-q.diff),
[published P to R](package-b-r-from-p.diff). Original P/Q scripts, failure roots,
logs, review reports, outlinks and publication receipts remain unchanged.

## Frozen next operation

The lead's fresh watcher executed this frozen command; the implementer did not
launch a duplicate check:

```sh
B_R_ROOT=/tmp/flake-update-guard-b-r-rspec-2026-10-24-1 \
B_R_REVIEW_RECEIPT=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/review-followup-report.md \
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-b-r-rspec.sh
```

Script SHA256:
`c35e3a51985fad1fa5d647eb2efeaf63b85a7afe83b4c1e46a8995136e639e3d`.
Suggested outer log: `tracking/provider-r-rspec.log`.

The successor script requires clean exact R in both the worktree and canonical
local feature ref, and resolves the immutable `git+file` revision. It retains
metadata, complete archive/source closures and roots, recursive derivations,
actual package/check outlinks and closures, build logs, exact review hash and
status. Success requires all 197 examples, no failures and no pending cases.
No publication, source-suite substitute, sanitizer, sandbox escape, retries or
cleanup occur in the script. Unexpected kernel builds require the watcher's
owned-process interruption and escalation under the verification brief.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/
