# Package A implementation evidence

Owner: implementer0. Architect brief: [design.md](design.md), package A.
Implementation and assigned quick checks are complete. Independent final review,
combined package B verification, packaged checks and native acceptance remain
lead-owned delivery phases. No integration or deployment was performed.

## Identity and source

- `dev-session current` printed
  `2026-10-29-cross-session-communication-authorization`; both session environment
  variables matched that slug and `/home/aither/workspace/ai/vpsfree.cz`.
- Saved roster: implementer0, thread
  `01a189c3-549d-7080-a702-dfcb7b53ac63`, `gpt-6.1-sol`, `xhigh`,
  `workspace_write`.
- The exact native thread row and its own current turn context confirmed
  `codex-lb`, `gpt-6.1-sol`, `xhigh`, approval `never`, and full execution access.
  The common configuration's Astra default did not replace the member override.
- Worktree: `worktrees/2026-10-29-cross-session-communication-authorization/dev-workspace`.
  Base: `08f3dbb92bc8585929edee85a824d44dfb3b0846`.
- Commit: `ed16c606b8b3a5ae1624e1f8dd5e7bcccf3cc387`,
  `communication: attach verified grant context to deliveries`.
- Exactly three paths committed: `portal/internal/communication/service.go`,
  `authorization_context.go`, and `authorization_context_test.go`. Package B
  changes were left unstaged. No branch changes, rebases or pushes.

## Result and invariants

First preparation merges the registry snapshot under
`dev-workspace/session-communication`, with `kind: application`. The JSON snapshot
contains grant ID, active status, exact A/B identities, message ID, approving
session, faithful stored approval audit text, grant creation time and limited
scope. Peer payload remains solely in its ordinary envelope. The new envelope
retains its transcript classification prefix; existing envelopes are unchanged.

Preparation follows the existing sorted session locks, store lock and fresh
grant/identity checks. Complete encoded options are checked against 64 KiB and
saved before native submission. Existing options and envelopes remain exact
through restart, reconciliation and held retry. Prepared inputs are copied
before adding context. Public API, schema-1 state, capacity admission and native
transport interfaces are unchanged.

The lead inspected and accepted the final runtime context and envelope wording
before commit. Project feature and upgrade documentation are package B's scope;
no duplicate documentation was added by A.

## Quick evidence

In the repository's Nix environment:

```sh
nix develop --command gofmt -w \
  portal/internal/communication/authorization_context.go \
  portal/internal/communication/authorization_context_test.go \
  portal/internal/communication/service.go
nix develop --command go -C portal test -mod=readonly -count=1 \
  -timeout=45s ./internal/communication
git diff --cached --check
```

The communication package passed in 6.191 seconds, including existing native
holds/settings, capacity, revocation, expiration and concurrency checks. New
regressions cover registry-derived context in both directions with one grant,
forged/copied claims to C, safely encoded audit data, pre-RPC durable tuples,
retained settings/context, fresh endpoint identity after sorted locks,
held/resume/revoke, lost-ack restart/revoke, submitting-to-held retry, legacy
prepared/unprepared messages, exact encoded 64 KiB acceptance and one-byte
overflow refusal, and mismatched stored grant refusal. No failed checks.

Scoped staged content was inspected. No hook framework is declared by the
repository; canonical hooks contained no non-sample hooks. The commit ran
normally through `nix develop` with a message file and no bypass. The index and
all package A paths were clean immediately afterward.

## Remaining verification boundary

Exact pinned codex-web source
`v0.0.0-20261029173332-9d337b70987f/codex/client.go` confirms that
`SendWithOptions` sends `additionalContext` separately from user `input` on
both `turn/start` and `turn/steer` and includes it in attempt identity. This is
source inspection, not model-facing native acceptance evidence. Package B owns
the real-path and pinned native tests; execute long checks only after final
committed-deliverable review using the assigned utility watcher.

The brief's combined short check remains:

```sh
nix develop --command go -C portal test -mod=readonly \
  ./internal/communication ./internal/workspacecodex
```

Lead selects focused command/web regressions and post-review packaged/native
commands after package B settles. Package A introduced no migration or changed
trust boundary and has no known blockers or design deviations.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-cross-session-communication-authorization/)

## Later lead acceptance checkpoint

Full actual portal-worker native idle/steer exchange PASSED on published final
4155d0099d03028b43d5f08d225a88156cb4155a (Go12.043s, wall17.9s). CI40975812804
completed successfully on the same head: packaged/focused, archive and creation
passed, host skipped. This closes the earlier pending native/full-suite items;
original commit/check history above remains evidence for its stated range.
See [final handoff](handoff.md), [native result](verification/native-final-result.md)
and [CI result](verification/ci-result.md). No integration/deployment performed.
