# Verification acceptance

Lead reconciliation,2026-10-29. All intended implementation and diagnostic
changes committed/published and independently reviewed before their long runs.
No production source or dependency pin changed after the original source/pin
reviews; source successor08f3dbb9 is fixture-only and independently reviewed.

## Coverage and exact identities

| Scope | Revision/identity | Evidence and result |
| --- | --- | --- |
| codex-web quick activity/passive transport |9d337b70987fdf1dd42a5d8efff31f755a122550|Passed Test(Activity\|Observer), real passive client identity/empty Prompts |
| codex-web full suite/CI |same9d|Local nix flake check exit0; CI40922501574 success |
| Portal quick attention/notifications |production5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3|Passed Go focused batch; browser75/75 |
|25 named runtime checks |same5f, original exact drv/output inventory|Valid successful outputs observed after first local full-suite batch, including package/complete unique Ruby aggregate/host-idempotency/contracts; retained exact inventory and input graph |
| Creation acceptance |same5f, syy3qnjfyynbc7bhwv36jlch9haycgld drv|Reused successful CI40923422808 job123622465542; exact drv in planned+actual build log, immutable complete source/input graph bound by drv identity |
| Archive acceptance |fixture08f3dbb92bc8585929edee85a824d44dfb3b0846 against exact5f runtime, w3pwbnfc drv|Exit0 in1037s; all8subtests and script finished, cleanup; valid spz3nyvg output rooted |
| Recovery acceptance |exact5f, jbwvzym25xppgjlnqwd6rnva9h5fagdz drv|Exit0 in333s, script329.14s, cleanup0.28s; valid0wj41qx9 output rooted |
| Final source successor CI |08f3dbb9|CI40936446701 success: fast/archive/creation; host skipped by feature policy, prior exact production host validation retained |
| Composed application |workspace398dc7bab, runtime5f/provider9d, wxxdwf6i drv|Build exit0 in730s, exact g650vgjp output rooted |
| Configuration system |b3b933bf6f9fc9f7f533b3f4e06775defd8879da, ia5gh8wr drv|Build exit0 in115s, exact r4rd3qyn output; generation2026-10-29--19-25-31 and rollback metadata verified, copy-only exit0 |

See implementation-evidence.md, deployment-preparation.md, diagnostic review
packet/report and rollout.md for complete bases/heads, locked source graphs,
derivation paths and logs. Exact CI reuse receipt is logs/creation-ci-reuse-receipt.json.
Recovery logs/progress/result: logs/recovery-completion-final.log,
logs/recovery-final-progress.json and logs/recovery-final-result.md.

## Original failure and diagnostic scope

The original local full flake command exited1 in archive initial page hydration;
other creation/recovery VMs were interrupted. An isolated unmodified archive run
repeated that30s response deadline before any archive click/POST. Both failures
remain preserved. No source bug, missing KVM or host-load cause was established.

The reviewed fixture-only diagnostic change preserved the original deadline,
actions and assertions. Native Nix parameterization binds it to exact5f runtime;
independent6071-node graph comparison shares6067 derivations, differing only four
harness nodes. The diagnostic acceptance passed. This is valid coverage of the
same planned production target with improved observational diagnostics, not a
claim that the earlier old-harness flake command exited0 or that timeouts are
explained/harmless. No old archive blind rerun or duplicate creation run required.

The archive watcher's textual failure verdict was incorrect: raw exit0, valid
output and terminal script completion prove success. Its cited intermediate
assertions occur in successful wait_until_succeeds polling. Lead inspected source
and final log and accepted pass, preserving original raw verdict for audit.

## Readiness and post-merge checks

Reviews have no findings and pre-integration coverage above is accepted. System
and application activation and authenticated health/identity effects passed;
exact evidence is in rollout.md. User direction "ok, merge and release aitherdev"
approved all four repositories/master. Final remote heads and deployed ancestry
are verified; aitherdev claim is released and status-verified. No mutation remains.

Post-merge codex-web run40949233152 at9d337b7 passed. Fresh Luna/low utility
observes exact dev-workspace run40949278279 at08f3dbb9; no duplicate local test
batch is required. Workspace398/configb3 exact-head workflow inventories are
empty. Final CI conclusion will be recorded here.

A real organic browser Plan-question/focus/answer exercise remains unperformed;
composed native, portal/API and browser regressions cover the behavior. No live
state was manufactured. Positive naming inference was optional and not launched.
Machine release is complete; future deployment needs new ownership. Session and
branches remain open and retained.
