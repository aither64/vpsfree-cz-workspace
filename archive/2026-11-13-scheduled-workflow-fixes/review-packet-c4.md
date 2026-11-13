# C4 final review: repository-locked confctl in both workflows

All intended changes are committed, published and quick-checked; both source
trees/indexes are clean. Lead independently inspected exact final series,
diffstats, workflow deltas and locked provider revision. Read owner packets
[org](evidence-c4-implementer1.md) and [vpsFree](evidence-c4-implementer0.md),
current design.md C4, and latest user correction. Prior C3 source review and
package acceptance remain authoritative for unchanged providerff5e0177.

## Governing request

User: "there's not supposed to be any pin in the workflow. we have flake.lock
for that"; explicitly fix both named configuration repositories. The earlier
YAML-only adoption was wrong authority and is superseded as final architecture.
Keep merged history; implement correction additively. Normal flake.nix URL
declarations stay unchanged. Only flake.lock selects the confctl revision.

Both mkConfigDevShell tools shells already prepend the declared provider's
package to PATH. Remove CONFCTL_FLAKE and nested nix-shell provider overrides;
use plain confctl inside existing declared-shell blocks for updates and final
guard. No exported replacement pin, registry, custom package output, wrapper
framework or confctl source edit. Preserve flags/hooks/auth/events/finalguard/
ordinary push, vpsFree B1 saved shell and selected-only message policy.

## Exact complete final ranges

Worktrees beneath
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/`.

| Repository | Base | Final head | Complete series |
| --- | --- | --- | --- |
| vpsadminos-org-configuration | `04b85313c0fe30be13e73c19acaa2760283e7874` | `15352aeb13c4011b5dd1a1f78d1fdcb08f7c2420` | `cde440b16d65d597caf5e223dd25ba760d584645` inputs: update confctl to ff5e0177; `15352ae` ci: use the locked confctl input |
| vpsfree-cz-configuration | `07a85cae5fdb4525e4ce2cca28a05a0888be8e0c` | `7d9807e021e6106d628c021da45f5f55077b2e9c` | `0e66bd37ec51d5997a126e381fef68cc31438cba` inputs: update confctl to ff5e0177; `7d9807e` ci: use confctl from the locked repository input |

Each owns only flake.lock and .github/workflows/daily-update.yml. Org54+/20-;
vpsFree18+/19-. Normal declared-shell confctl inputs update --commit confctl
generated each isolated lock commit. Separate workflow commit preserves input-
update history conventions; generated messages remain as generated. No obsolete
unmerged approach or redundant input stream: one final normal confctl lock update
per repo. Previously merged C1/B1/C2/C3 and generated defaults remain protected.
Org base includes C3's actual generated f8c8aa3/04b8531; vpsFree C3 run was a no-op.
**No migrations**; no schema or deployed-system changes.

## Interfaces, graph and compatibility

Previously normal locks selected vpsFree7bee58a5/orgaf164b44, while YAML overrode
them. Both normal locks now select accepted publishedff5e017780a35fb97b549db2a51b570193867c3b.
Only confctl and its owned dependency graph advance: OS67fcc173, Nixpkgs8b8c811c,
OS unstablef13ff45a and expected owned nodes. Semantic logical-path comparisons
preserve unrelated root inputs, production channel selections and follows;
review actual diffs/receipts rather than generated node IDs. flake.nix and gem
locks are byte-unchanged. No channel owns confctl; no channel/registry was added.

All three org and five vpsFree confctl calls remain in existing tools shells.
vpsFree retains initial profile producer/every consumer; llm's removed wrapper
Nix-only accept-flake-config flag moves to its existing nix develop invocation,
never to confctl. Org's tools default to the adopted provider Nixpkgs, so Ruby
changes3.3.10 to3.4.9. Fresh isolated compatible native bundle/hooks prepared;
old caches/target dependencies preserved. vpsFree's rootstable Ruby overlay
remains3.4.11; actual adopted environment/hook identities recorded. Provider
library adoption adds existing configuration-info metadata for future generated
systems; configuration channel/machine inventories evaluate. No node/kernel
build or production deployment. Recovery is additive source/input reverts,
preserving sole-lock authority and required guard behavior; no reintroduced YAML
pin or rewritten merged history.

## Quick checks and documentation

- Both: normal generated lock update, semantic graph scope/follows preservation,
  unchanged normal URL, absence of workflow override, exact allowed workflow
  delta, JSON/YAML/Bash/actionlint1.7.12, normal hooks and clean SSH publication.
- Org:5Bash bodies; channel and11machine inventory evaluate; fresh declared
  Ruby3.4.9/Bundler4.0.7 bundle, normal hooks, utility batch50.4s exit0.
- vpsFree:7Bash bodies/profile coverage; inventory evaluation; adopted
  Ruby3.4.11/Bundler4.1.0.beta3/Overcommit0.76, fresh quick batch36s exit0.

Actual declared package derivation6nq336f5 matches accepted C3 output
`/nix/store/v4b3r3r8102kyf92lidwvk62plpjs13j-confctl` and source
`/nix/store/1qw3c7q3r67drrv0z4vmac9g70pvxyf5-source` atff5e0177.
Full provider source/input/NAR graph receipts are linked from owning evidence.
Accepted225RSpec/110RuboCop/packaged mixed-selection+rewind proof is reused at
that exact identity, not rerun. No old environment is represented as new proof.

No new user-facing prose/interface/runbook is needed: ordinary declaration+
lock+workflow commands state tool authority directly. Existing confctl input
guide/C3 message docs remain accurate. Discovery, actual per-run/native/store
identities and recovery state belong in session evidence. No docs move, lost
entry point/prerequisite/recovery path or upgrade-support retirement.

## Held acceptance and review assignment

After final review, focused declared-environment proof records actual executable,
sole-lock source/package identity, native bundle and real final check-update
through that executable. Adopted final lock versus exported HEAD lock proves
no-change wiring, not changed ancestry. Reuse exact C3 changed/rewind proof.
vpsFree saved profile retains tool/Ruby across representative fixture mutation.
No provider suite repetition or unnecessary generation. Then target preparation,
approved ff-only integration and fresh final master workflows in both repos.
Earlier C3 hosted success is historical and cannot satisfy C4 acceptance.

Retained reviewer0 Sol/xhigh/read_only, thread01a1d53b-f8ca-7383-8a79-41928077c6df.
All four lanes; conservative high risk for actual tool authority/config dependency
and generated master publication. Independently inspect full ranges, semantic
graph/callers/history/migrations/update streams/docs. Read-only; no tests/builds,
edits, nested reviewers, claims or lifecycle operations.
