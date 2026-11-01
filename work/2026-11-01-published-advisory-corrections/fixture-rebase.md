# Reviewed fixture fix and fresh HaveAPI baseline

Implementation/quick-check receipt; affected compatibility review and real
API/strict-KB acceptance remain pending. No application suite, default merge,
deployment, production correction or lifecycle action was performed.

## Exact old/new ranges

| Repository | Previously reviewed range | New final range |
| --- | --- | --- |
| vpsadmin | `610a96f8ce523afbcd3e4374a70047dbe3264b0d..218e3180896debd3006b9a0583e557286702761d` | `097226b22edf8b59f80b5dfaa55265e9d0cac633..c8efabeb01ccca66b19425ee429e834d23cf3688` |
| vpsfree-kb-contracts | `ce2c8cd9358c3636e5d39343e595df813a0b197f..21c5213256c28f4a65fd582485e07234a02f5f55` | `ce2c8cd9358c3636e5d39343e595df813a0b197f..beeb258c72f84105b73b75fc4837e18b87e81cf2` |

New A: `e200ab369bbc85ee7e5837091379a2899a261688`.
New B/head: `c8efabeb01ccca66b19425ee429e834d23cf3688`.
Both branch names remain `2026-11-01-published-advisory-corrections`. Fresh
SSH push/remote proof and captured comparisons bind these ranges. Worktrees and
indexes are clean. Previous reviewed heads remain reachable via each
repository's local `2026-11-01-published-advisory-corrections-reviewed` branch.

## Actual CI cause and accepted correction

`ci-snapshot-1902.md` records exact source `218e`, failed core-platform-operations
job `124940972367`, native results/environment/manifest and full log. The only
two failures were published/retracted membership examples `[1:4:6]` and `[1:4:7]`
at line 762, because the new API fixture supplied lowercase `cve-2026-9998`.
HaveAPI imports the unchanged model's uppercase CVE format validator before the
model callback can normalize it.

The accepted correction is exactly one fixture string, `CVE-2026-9998`.
Runtime/model/API validation, descriptions, metadata, prose and other tests are
unchanged. The earlier failure is not called baseline drift or waived by a rerun.
No failed-job rerun or local application suite was launched.

## Upstream movement and equivalence

Fresh fetch advanced master by exactly one commit,
`097226b22edf8b59f80b5dfaa55265e9d0cac633`, adopting HaveAPI 0.32.1 documentation
switching. It changes ten API dependency/package/schema-export/documentation
files without overlapping advisory feature paths. The first guard stopped before
any source restoration or rebase; the accepted new baseline was then used.

The reviewed feature patch and fixture patch were saved separately. An alternate
index reconstructed the intended tree from new master plus those patches.
Actual final tree `135f6a75154f1e4387fc912db26a5c6ae1abed08` matches it exactly.
`range-diff` shows only the one accepted fixture hunk in A and marks B equal;
B's full binary diff is also byte-identical. No additional feature change or
obsolete fixup commit remains. Two logical A/B commits and one mechanical D pin
commit remain; no migrations or deployed/merged lineage were rewritten.

The upstream framework input changed, so this patch proof does not replace the
lead's affected compatibility refresh. Earlier long-run results are not claimed
for the new dependency graph.

## Quick checks and pin refresh

Fresh Luna/low watcher `01a19882-31f9-7f70-95a6-e0b26a164114` prepared the
new API bundle, confirmed actual HaveAPI `0.32.1`, and passed metadata/i18n health,
three-file RuboCop and fixture syntax in 78 seconds. Launch used the retained
catalog/native utility and verified danger-full-access/never policy.

Normal root amendment hooks passed, including both i18n checks and root RuboCop;
the parent-owned A amendment/B replay batch completed in 64.17 seconds. Modern
long verification occupied the utility slot during this known bounded hook/pin
work, so parent monitoring used the declared minimal fallback.

D regenerated the selected vpsAdmin input and refreshed the same four source pins
to new head. Pinned-shell JSON/YAML/Nix parsing, full lock-graph equality outside
the selected node, explicit vpsAdminOS `6bdf458fd9105379860234ff33d352e55844f08f`,
all follows/provenance checks and diff checks passed. Five files still differ by
eight insertions/deletions. No strict `bin/check`, capture or page change occurred.

Exact artifacts are under
`/tmp/2026-11-01-published-advisory-corrections-fixture/`: `inputs.json`,
`reviewed-feature.patch`, `fixture.patch`, `range-diff.txt`, `fold-status.json`,
`rebased-quick.log` and hook log; `kb/` holds old five-pin files, generated graph,
quick checks and CI records.

Current source CI IDs: API Specs `41340446069`, CI `41340446005`, i18n
`41340446172`, RuboCop `41340446028`, Webui PHPUnit `41340446196`. They were
listed without waiting. KB current IDs are Check `41340595714` and Managed page
runtime `41340595741`. Old source `218e` runs `41337574315`/`41337574258` are
confirmed completed/cancelled. Old KB `21c5` runtime `41337657793` is also
confirmed completed/cancelled. Only superseded same-branch old-head active runs were selected;
current heads remain. No other session/branch CI was canceled.

Next: retained reviewer's bounded compatibility refresh for the exact new
committed range, then lead release of full/core/plugin/client/strict-KB batch.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/>
