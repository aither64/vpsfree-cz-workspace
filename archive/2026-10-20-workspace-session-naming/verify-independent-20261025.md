# Prepared independent checks; creation remains blocked

[verify-independent-20261025.py](verify-independent-20261025.py) is prepared only.
It has not run and has no release. Main inspects it before writing a separate
release and selecting a fresh Luna watcher. The existing
[remaining driver](verify-remaining-20261025.md) and all original evidence remain
unchanged and unreleased. A/B/C sources and refs stay frozen; C113d/7510 is stale.
USER deployment HOLD remains active.

This operation can collect independent evidence while preserving the known
failed creation check. It cannot produce full runtime flake success, creation
acceptance or readiness for use. Even an independent run exit0 retains
`creationAcceptance: FAILED`, `fullReadinessBlocked: true` and
`fullRuntimeFlake: NOT RUN` in its result.

The future release must use this shape. This example is not a release:

```json
{
  "schema": 1,
  "purpose": "independent-checks-creation-blocked-20261025",
  "approved": true,
  "client": "801099102ef9af4a82c1f3853c53d6b442ecd4dc",
  "runtime": "529e075ad07e2d967a8af4902584e37527115454",
  "preceding_result": {
    "path": "verification-source-20261025-801099-529e075a/result.json",
    "sha256": "cff16ecb819775a88e53f6e5c06417b1e05ac1249c8c7ede14100924efff7952"
  },
  "blocked_decision": {
    "path": "forward-review-20261025/creation-blocked-decision.json",
    "sha256": "d26473ea68b87cd5bf11cf497119e5a58152986a1c52169fb95f11272041c90a"
  }
}
```

The driver validates the actual closed result directly: exact A801/B529 heads,
integer top-level exitCode1, timezone-bearing finishedAt, exactly six unique
steps (client-source, client-source-root, native, message-delivery-browsers,
creation-inputs, creation). Only creation must have exitCode1; the other five
must have0. The unchanged restoredSourceProof must match final A source/NAR/catalog
and name its retained root. Unknown/missing/duplicate shapes refuse before any
command. There is no fabricated success receipt.

It also validates the separate main
[blocked decision](forward-review-20261025/creation-blocked-decision.json): schema1,
purpose creation-blocked-decision-20261025, exact client/runtime and same
preceding_result path/hash; failedCheck.name/drv/status must preserve the exact
unresolved failure. fullReadinessBlocked, independentChecksOnly and deploymentHold
must be true; creationRerunAuthorized and fullRuntimeFlakeAuthorized must be false.
All three original artifacts are copied byte-for-byte into the exclusive run
directory, and their hashes are checked before/after commands.

After main release only, the future watcher invokes:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming/verify-independent-20261025.py \
  --release forward-review-20261025/independent-verification-release.json \
  --output verification-independent-20261025-801099-529e075a
```

The output must be new beneath this session. Directories are0700 and files0600.
The exact current session and clean A801/B529 HEAD/tree identities are guarded
before/after commands. Failure stops the operation; no retries or generic timeout
are added. Every command retains argv/cwd/status/time/log/SHA and a structured
step receipt. Raw derivation JSON stays private; no environment is printed.

The selected sequence is:

1. Capture B's entire check-name/drv mapping and complete recursive JSONv4 inputs,
   before the collector uses B's Nix shell.
2. Run the existing final529 collection probe with its exact expected head.
3. Capture A's entire check mapping and recursive inputs, then run
   `nix flake check --no-write-lock-file --print-build-logs` in A.
4. In B, run `nix build --no-link --no-write-lock-file --print-build-logs --max-jobs 1`
   for `.#checks.x86_64-linux.package`, then session-archive-lifecycle.
5. Use the same B build command once over every check ATTR returned by the
   captured mapping except session-creation. The package/archive ATTRS remain
   in this complete independent selection; Nix may reuse their exact results.

Capture uses `nix eval --json --no-write-lock-file .#checks.x86_64-linux --apply
'checks: builtins.mapAttrs (_: drv: drv.drvPath) checks'` followed by
`nix derivation show --recursive` over all returned drv paths, including creation
for input evidence only. Before building anything it requires session-creation to
map to `/nix/store/c4p49c13v4jf9skfjjsai7xrj9yj502m-vm-test-run-dev-workspace-session-creation.drv`.
Complete selected/excluded name/drv lists are retained. The driver refuses any
selected alias or transitive dependency on that failed derivation.

It never runs B nix flake check or a standalone creation command. The final B
subset is explicitly independent-only, never a full-flake or readiness pass.
There are no C/system builds, fetch/rebase, claims, deployment copy/activation,
profile selection, default-branch or session lifecycle operations.

Preparation validation is syntax/AST only. No driver invocation, functional test,
Nix query/evaluation/fetch/build/check, CI query or raw failure-log diagnosis was
performed. Main owns release and later acceptance decisions.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/>.
