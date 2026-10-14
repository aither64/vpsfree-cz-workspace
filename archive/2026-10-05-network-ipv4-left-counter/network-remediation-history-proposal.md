# Network availability review remediation

Status: draft for lead decision. No commits, rebase, push or repinning has run.

## Frozen checks

Run `bash run-implementer-remediation-quick1.sh` from this tracking directory
through a fresh watcher in the parent execution context. The wrapper verifies
the exact session identity and source/helper hashes, logs each result under
`remediation-quick1-*`, and stops on the first failure.

- V root Nix shell: syntax and scoped RuboCop for the two changed Ruby files,
  with the declared exclusions honored.
- W Nix shell: Node syntax check of the changed legacy browser scenario.
- V API Nix shell, all plugins: existing VPS update spec, using the automatic
  isolated database only when neither DATABASE_URL nor database.yml is present.
- W Nix shell: six focused unit files, including suggestion-hook regressions
  and the expanded network-editor cases.
- W Nix shell: full ci:quick, including design-documentation audit, scoped lint,
  formatting, localization audits and application/tooling/browser/BFF types.

These checks do not run browser scenarios, concurrency-tagged integration,
configuration builds, capture generation or lifecycle actions. No locale/schema
generation is needed. Work-log evidence will be reconciled after actual results.

## Intended owned splits

- API: `api/models/transaction_chains/vps/update.rb`, its existing update spec,
  and `docs/ip-locking.md`; discover the existing transferred-export set before
  parent IP reservations and cover endpoint admission/continuity.
- Legacy UI: `tests/playwright/webui/specs/admin-cluster.spec.cjs`; target the
  enabled cell's actual boolean icon without adding UI text.
- React UI: NetworksPage source/tests, useProgressiveSuggestedIpQueries
  source/new hook tests, `docs/design/API_CONTRACTS.md`, and the final dated
  work-log reconciliation after checks. UserNetworkPage and its ledger are fixed.

## Consolidation proposal

After passing checks and the lead's explicit instruction, create focused fixup
commits with normal hooks for API 819d66b0, legacy UI 6b3628af, and W 811742f5.
Autosquash the V fixups onto its two existing logical commits from base
`c4d9b50f4e74417ed37b5fe410cca3ec1addc24e`; autosquash W onto its existing
single logical commit from `02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51`.
This removes the obsolete incomplete guard and unsupported browser assertion
from the reviewable feature series. It does not alter migration content.

The branches are published feature refs and unmerged. Any approved rewrite must
retain the exact previous remote heads as force-with-lease expectations, preserve
the original authors, and verify the final trees and cleaned complete histories.
Do not rewrite a default branch. The lead owns the exact history/push commands.

Publish only the selected final feature heads after the history decision. Then
regenerate the C application pins through confctl and the K exact V pin through
its canonical workflow. Existing pin commits reference the original reviewed
source heads and cannot certify corrected source until regenerated. Preserve
generated messages and all unrelated inputs; do not edit flake.lock manually.

Migration 20261006120000_add_network_enabled remains unchanged, with predecessor
20260914190000_add_node_kernel_evidence_checkpoints. Its original review lineage
was sound; no merge, release, deployment or external consumption is claimed.
The lead's final packet must carry the new exact heads and pin diffs for renewed
review reconciliation before longer verification.
