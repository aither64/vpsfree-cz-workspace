# Performance workflow preparation

Implementer3 read-only preparation, 2026-10-25. Substantive application edits
wait for the architect's expanded design and shared CLI/report contract.
Session identity, environment and same-session roster agree on
`2026-10-24-context-copy-performance-tests`; implementer3 retains workspace-write
access. The HaveAPI worktree is clean at the published fixed reference
`b85ec364057f536940d689b09e612512ffffaf82`. No source/index/ref, dependency,
workflow-dispatch, permission or publication mutation was performed.

## Existing workflow findings

Read `.github/workflows/servers-ruby-rspec.yml`, `_ruby-rspec.yml`,
`clients-rust.yml`, `update-nixpkgs.yml` and `release.yml`, plus the workspace
verification procedure and HaveAPI development instructions. The existing Ruby
server workflow covers server/docs/Makefile changes and invokes the shared
Ruby 3.2/3.3/3.4 RSpec matrix. Its separate asset job uses Nix. The Rust workflow
covers Rust/Ruby/server/flake changes and runs generator/runtime/integration
checks. Neither supplies broad API timing comparisons, paired source resolution,
a stable aggregate performance gate or performance-result artifacts.

Existing release artifact upload is pinned to v7.0.2. Most Nix-using workflows
still pin install-nix-action v31.11.2; update-nixpkgs already uses the upstream
31.11.3 spelling. A new performance workflow can use the latest checked refs
below without touching unrelated workflows. No additional setup/cache/download
action has yet been selected. If the design needs another imported action,
verify its latest compatible upstream release before using it.

## Official upstream verification

Queried unauthenticated, read-only official GitHub API `releases/latest`, tag
refs and raw files at resolved commit SHAs. Release identities were checked
again after resolving tag refs. Exact checked timestamps, URLs, tag chains,
complete `action.yml`/README text and their SHA-256 are retained in the linked
JSON. No local Git fetch, checkout or action execution was used.

| Action | Latest official release | Immutable commit | Compatibility relevant to this work |
| --- | --- | --- | --- |
| `actions/checkout` | [v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1) | `3d3c42e5aac5ba805825da76410c181273ba90b1` | Node 24; minimum Actions Runner v2.327.1. Supports explicit SHA/ref and `persist-credentials: false`; recommends `contents: read`. |
| `cachix/install-nix-action` | [31.11.3](https://github.com/cachix/install-nix-action/releases/tag/31.11.3) | `75c75c31ebece974e48ebc36b4ad125bd97bd97b` | Composite Bash action, supports GitHub-hosted Linux. Release updates bundled Nix 2.35.3 to 2.35.4 and certificate bundle. Tag has no `v` prefix. |
| `actions/upload-artifact` | [v7.0.2](https://github.com/actions/upload-artifact/releases/tag/v7.0.2) | `cf430e030ddbb5b0abf93d22962f4752f3646cd9` | Node 24. `retention-days: 30` is within documented 1–90; use unique artifact names, explicit evidence paths and `if-no-files-found: error`. Hidden files are excluded by default. |

Evidence:

- [checkout metadata](workflow-upstream-actions-checkout.json)
- [Nix installer metadata](workflow-upstream-cachix-install-nix-action.json)
- [artifact metadata](workflow-upstream-actions-upload-artifact.json)

Checkout's v7 fork safeguard rejects fork code in `pull_request_target` and
`workflow_run` trusted contexts by default. The accepted plan uses ordinary
`pull_request`, hosted workers, read-only contents, no secrets and no PR comments;
neither trusted-context event nor `allow-unsafe-pr-checkout` is needed. Explicit
full event SHAs, quoted environment variables/structured event input and disabled
credential persistence should remain part of the architect's exact contract.
Do not interpolate event-controlled branch names into shell code.

## Accepted constraints to carry into D implementation

These come from the lead's assignment and accepted plan; exact file boundaries,
CLI/schema names and resolver interfaces remain architect-owned.

- Trigger push, ordinary PR, explicit manual SHAs and weekly Sunday 03:00 UTC
  (`0 3 * * 0`). Use a stable aggregate job even when relevant paths do not change.
  Do path relevance inside jobs rather than skipping the entire workflow through
  top-level path filtering. Missing comparison/input evidence must fail closed.
- PR candidate is the exact event head; baseline is its merge-base with exact
  event base. Feature push compares exact event candidate with the merge-base
  of captured default. Default-branch push uses event before/after. Missing,
  deleted or zero SHAs need explicit failure behavior. No moving-ref substitution.
- Weekly uses the exact immutable accepted reference
  `b85ec364057f536940d689b09e612512ffffaf82`, verifies required ancestry and never
  advances reference or fixed budgets automatically.
- Hosted, fork-safe, `contents: read` only; no secrets, comments or permission
  changes. Always retain success/failure evidence for 30 days. Aggregate must
  reject failed/cancelled/unexpectedly skipped required work. It must remain
  compatible with normal no-relevant-path success.
- Push/PR target 5–10 minutes; hard quick/weekly job ceilings 10/30 minutes.
  Timing regression is greater than both 20% and 0.20 ms/request; inconclusive
  results block. The runner/comparator package owns timing/quality decisions;
  D preserves its exit and complete JSON rather than inventing another gate.
- Preserve exact source/runtime/dependency/report identities. Import any neutral
  harness and fixture from the agreed source once, then resolve both roots from
  frozen event SHAs. No generated SDK compilation belongs in the docs lane.

No build, test, calibration or benchmark campaign was launched during this
preparation. Long or uncertain verification still waits for final committed
review and a lead-authorized fresh pinned verification watcher.

Next action: wait for architect design-ready and the shared runner CLI/report
contract, then implement only the assigned workflow/resolver/Makefile/docs paths.
