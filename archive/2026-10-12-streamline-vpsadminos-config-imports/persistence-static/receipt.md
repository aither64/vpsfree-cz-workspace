# Implementer technical receipt

Current product HEAD: `84d2fbe0607aa768b10a5acf5f6e952e423493c5`.
The 14 technical paths in `owned-paths.sha256` are unstaged. Product policy files
are unchanged; `docs/containers/nixos.md` is the lead's preserved draft.
`technical.patch` includes all tracked changes and four new test files.

Static checks passed: 11 Nix files parsed and passed nixfmt --check; both shell
scripts passed bash -n; static source-template callback passed bash -n; the
RSpec template with all conditional bodies and placeholder Nix values passed
Ruby -c; git diff --check passed. Latest stable and 26.05 are byte-equal.
Nested static templates are not evaluated generated-script evidence.
No Nix evaluation/build, runtime, ref/index mutation or commit was performed.

The four raw modules restore full promotion and source the upstream globally
ordered earlyMountScript once through a legacy-only whole-value specialfs
priority-90 override. users retains its other native dependencies and gains
specialfs. Guest mkForce wins. Ordinary/alternative backend code remains
upstream. Selected source prep creates missing directories only, retaining
existing metadata. Declared covering bind prerequisites verify both directory
shape and configured-source/live-target identity; non-bind prerequisites verify
exact mountpoint presence. Root-backed/undeclared sources remain allowed, and
undeclared host absence is not claimed detectable. Selected bind failures exit
the parent activation shell before allocation. No account/map/data repair.

The pure normal check evaluates actual 25.11/26.05/unstable, immutable baseline
1150e37b with its verified narHash, standalone files, full/global order, dry and
mkForce behavior, root/custom/dependent topology and ordinary/backend exact
baseline equivalence. Its generated callback shell harness covers three actual
fixture configurations: declared bind, non-bind filesystem and undeclared/root
source. It runs only doubles and fixture filesystem operations. The allocator
marker is local control-flow evidence. No guest/real mounts occur in this check.

The registered ci-tagged RSpec suite has eight variants: upgrade-25.11,
upgrade-26.05, upgrade-unstable, root-backed-26.05, declared-backing-26.05,
dependent-mount-26.05, fresh-26.05, storage-failures-26.05. It uses prepared old
and candidate closures with fixed guest inputs, stateVersion 22.11 and identical
account/storage definitions across the source transition. It seeds the actual
/nix dataset's exported private source profile. It initializes dynamic accounts,
performs the old live-switch/account-order challenge, checks live/map agreement,
then switches candidate and restarts. It never restarts the known-failing old
configuration, seeds IDs/maps or repairs owners after restart. Snapshot checks
include both accounts' IDs/maps, payload digest, owner, machine-id, state source
metadata, source/target identity, matching repeat activation, options and exact
single mount counts. Initial payload ownership is established only at creation.

The 26.05 negative variant uses complete generated activation and real allocator
traces for missing declared backing, deterministic MS_BIND|MS_REMOUNT on an
unmounted selected target, conflicting target and wrong covering bind. Mount
faults are contained in private namespaces inside the disposable guest. A
positive complete activation supplies executed Perl control evidence; negative
traces require start, source, refusal, executed exit and end with no executed
allocator. Saved passwd/group/maps/payload and independent snapshots must stay
unchanged. This is written coverage, not a runtime pass.

## Proposed parent verification

From the product repository (parent owns watcher/environment setup):

```sh
nix build .#checks.x86_64-linux.nixos-container-persistence --no-link
nix eval --json .#checks.x86_64-linux.nixos-container-persistence.evaluation.assertions
nix develop --profile result/config-imports-dev-shell --command bash tests/nixos-container-eval.sh
./test-runner.sh ls 'dist-config/nixos-persistence-upgrade*'
nix develop --profile result/config-imports-dev-shell --command overcommit --run
nix develop --profile result/config-imports-dev-shell --command mkdocs build
```

The documentation build may retain its previously known unrelated navigation
warning. The lead owns the exact KB consumer session check.

Generated artifacts after the pure build:

```sh
nix eval --raw .#checks.x86_64-linux.nixos-container-persistence.shellFixtures.declared.snippet.outPath
nix eval --raw .#checks.x86_64-linux.nixos-container-persistence.shellFixtures.declared.earlyMountScript.outPath
```

The same attributes exist under `undeclared` and `filesystem`. The check exports
`evaluation.assertions` and `evaluation.shellFixtures` for source/KB order
reconciliation, with no impure session baseline contract. Runtime remains for
reviewed committed deliverables, under the lead's watcher.
