# Saved source proof and finalization failure

Aggregate remains **exit1/22.011345s**, error null; sole errors entry
is the duplicate exclusive after.index write. All five Nix operations exited0,
children reaped/groups empty/no signals: metadata7.409s, valid0.096s,
registeredInfo0.098s, retention0.103s, independentNAR0.099s. All39 captures passed
(37 actual0 plus2 declared absent-hooksPath probes1). System second batch was not
launched; no system files or live source/tool/index/Git/store state observed.

Completed source proof: `/nix/store/hgw4ywzp05llp2i9vp8vq011gznign6s-source`,
NAR `sha256-qFaCixWrklErj+rffObnsQddw8el/EgsI4GBQf9VtkA=`, epoch `1793005599`;
Origin/resolved/locked bind exact7476/tree4aa5. Actual raw metadata URL retained
verbatim: `github:aither64/vpsfree-cz-workspace/7476eb48ef1c7609f7d27a13ba4fb4c00d1e4863?narHash=sha256-qFaCixWrklErj%2BrffObnsQddw8el/EgsI4GBQf9VtkA%3D`. All620 exported regular nontracking paths,
bytes/modes/blobs and full35node graph equal committed proof; independent NAR
matches metadata and registered NON_DRV has null deriver/empty references.
One standard root command0 returned exact own source-roots-v1/workspace;
root symlink/target was validated before the completed source proof record.

Both exact fa7 current/team readers and full own Git guards passed before/after.
Committed postflight620/57420 and all index flags match expected final identity.
Existing after.index is raw0c3f, equals before.index, and is already the exact
postflight raw snapshot. Callpath: guard(after) at bind-source.py263 calls A.guard;
consolidate.py166 creates after.index. Finalizer269 attempts the same exclusive
path and fails. No claim is made about its unrecorded second read. The subsequent
partial-effects.json block271 never ran, so its final rootExists/readlink fields
are absent. Earlier validated root facts remain evidenced; current root state is
not newly observed. No essential further observation identified for completed
proof. If parent separately requires a current root snapshot, only lstat/readlink
of that exact owned link is needed; no follow-target/store query or re-registration.

[Complete saved ledger](saved-source-proof-handback-v1.json) SHA256 `cfada80d8ee2d60d47d6b45b3b30d963e545f616377a0f58c3986b9f71513b20` binds
all39 actual command receipts, five Nix exits, full source/graph/NAR/URL/root/current/
Git evidence and all250 verified evidence entries. Parent assesses the
completed proof independently; the failed aggregate stays failed. No code repair,
successor, operation/guard/Nix/root retry or cleanup. Source/Git frozen; session open.
