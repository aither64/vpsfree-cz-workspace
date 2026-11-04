# Held db90 Nix5 launch and actual inspection boundary

Preparation only, for literal `db90da33765090f34d74280aad273c4dbfc98090` /
tree `93203cc0d5ef40d0425230abb9cf985a69086ea7`. Review is still active and
R040-1 awaits its later edit release. Do not launch this candidate as the final
remedied package. Rebind the prepared files, guards and input receipt to the
actual clean committed successor after the findings package is resolved.
Nothing was evaluated, built, installed or downloaded during this preparation.

The prepared native batch is one conventional `nix build` of exactly frontend,
BFF, provenance, source-contents and package-contents. It uses the literal local
Git flake, no-write-lock-file, IFD false, native JSON output, and ordinary Nix
out-links under the unique session prefix recorded in the preparation receipt.
All output links, including partial successful links after failure, remain
retained through CI/comparison. No cleanup is authorized. Unknown DRVs, store
outputs and NARs must remain unknown until actual evidence supplies them.

After a parent-authorized fresh utility returns native terminal:

1. Preserve command/observer/launch hashes, native log/state/exit and build JSON.
   Check native exit separately from watcher CLI exit, actual UTC/duration and
   exact captured PID/startticks/PGID/SID absence. Do not invent a descendant
   snapshot, signal processes or run the batch again. Bind only the exact
   committed source used by that batch.
2. Parse the five actual build JSON DRV/output records and resolve the five
   ordinary output links. Map targets from actual derivation names and bindings,
   not an assumed ordering. Retain all links. Compare five store derivers/output
   paths against those actual records; no old4ed/db90-success inference.
3. Reuse the existing offline inspection commands with actual paths substituted:
   `nix derivation show --recursive --offline --option allow-import-from-derivation false <five actual DRVs>`;
   `nix path-info --json --offline <five actual outputs and actual literal/filtered sources>`.
   Capture raw JSON/stderr, argv, UTC, exit, duration and hashes once. Account for
   all five roots, every reachable inputDrv edge and source input, with actual
   missing-edge/unreachable counts. This is a complete build-input graph, not a
   runtime closure or a claim that every dependency was newly built.
4. Bind actual immutable-flake metadata/source/locked identities with the known
   offline no-write-lock metadata command, without `nix eval` or a rebuild:
   `nix flake metadata --offline --no-write-lock-file --option allow-import-from-derivation false --json <literal Git ref>`.
   Record actual literal source path/NAR, filtered source path/NAR from frontend
   derivation inputs, and complete committed/effective 11-node locked identity
   and follows-edge graphs. Normalize aliases explicitly; unchanged lock bytes
   alone are not a newly observed effective-graph result. No old/new derivation
   or graph equality is assumed.
5. Inspect both installed build-info files: frontend `build-info.json`, BFF
   `share/vpsadmin-webui-bff/build-info.json`. Require schema1, full actual final
   commit, its first12 characters, dirty=false and source=environment. Bind the
   actual frontend DRV's VITE_BUILD_SHA/VITE_BUILD_DIRTY/VITE_RUNTIME_MODE=bff,
   actual declared public top-level files/assets and all three realized zero-byte
   check markers. Inspect BFF wrapper's exact Node target and direct references
   only; no broad runtime-closure or Node/shell-free claim.
6. Carry `w-040-final-nix-inputs.json` into the actual source comparison: current
   literal committed blobs/modes, worktree, literal source store and filtered
   source store. Compare all23 protected file bytes, the two intentional archive/
   provenance deletions, and relevant final source/doc bindings. Coverage143/140,
   baseline7bdc, sourceRevisionabab, parsed compiler configuration and all140
   surviving deferral records/order retain their prior exact proof. Any review
   correction requires its new final source binding, not a relabelled db90 proof.
7. Bind actual frontend/BFF npmDeps DRVs/cache paths and ordinary npm-config/build/
   install hooks from the realized recursive graph. Frontend fixed hash is
   `sha256-3H/bRfGSY5Mra3MkhjcgBSiP/NciqX0Q58K+zem/i9k=`;
   BFF remains `sha256-pifjCWQ5ShvtQw1V3bAlmutW43nPi93hDVW8Q4HuVMw=`.
   Inspect the actual cache/root lock selected 0.4.0 canonical registry URL/SRI,
   exact HaveAPI0.32 peer/transport records and the accepted public archive
   binding. Preserve all484 unrelated root records and unchanged BFF lock/hash.
   Inspect retained archive/cache bytes without installing, packing or executing
   client/backend calls. Do not infer old0.3 program equality or cache identity.
8. Return one compact actual-inspection receipt plus required raw metadata/graph/
   path-info bindings and hashes, final clean/index-empty/source proof and
   explicit remaining CI/integration limits. Stop/report the first unexpected
   query/input/realization boundary; no automatic retry, repair, new support
   machinery or worklog/source append.

The read-only CI selection is `w-040-final-ci-command-selection.json`: existing
core checks/production-build/browser-script jobs and exactly chromium,
mobile-chrome and mobile-webkit native PR-smoke projects. It is source command
selection, not execution/List/count/CI acceptance. Parent owns review, launch,
CI, publication, conditional integration and all lifecycle decisions.
