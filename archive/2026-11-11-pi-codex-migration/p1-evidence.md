# P1: neutral conversation seam

Owner implementer0. Package implementation, 2026-11-12; lead owns acceptance
and final combined review. P1 follows the lead-accepted concrete
[implementation contract](implementation-contracts.md) and P1 section of
[design.md](design.md). No Pi/P0 execution or admission claim is made here.

## Source and scope

- Repository: `git@github.com:aither64/codex-web.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/codex-web`.
- Branch: `2026-11-11-pi-codex-migration`.
- Base/fresh `origin/master`: `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`.
- Committed head: `f9b9b4831b23aab5ddf61316eefdd02edca1cc7c`.
- Published SSH feature ref has that exact head, independently confirmed with
  `git ls-remote`; no default-branch integration was performed.
- Series: one focused commit, `conversation: add neutral backend adaptation`.
  No native schema, migration, catalog, receipt-storage or dependency update;
  no conversion/retirement work. Native `codex/` and browser assets are unchanged.

`conversation/backend/` owns independent public presentation DTOs, identity,
nullable operation groups, explicit send outcomes and typed errors, with only
the standard-library `context` import. Parent `backend.go` adds neutral
resolver/target/options and keeps the old constructor. `legacy.go` preserves
the existing public Codex-typed interfaces and structs. `backend_codex.go` and
`backend_codex_projection.go` adapt original native behavior into common
`handler.go` dispatch; upload/retry helpers use the neutral private target.

The native adapter runs transform, attachment observation and presentation on
the original native transcript/page, then projects once. Optional native page,
bound prompt, pending-revision and deletion-completion support remains nullable.
Send retry keeps its original preflight order without treating its boolean as
acceptance. Typed errors retain their native causes. Empty/unrecognized send
outcomes fail without claiming acceptance, non-submission or retry permission.

One narrow compatibility exception was agreed directly with architect2 and
recorded in the contract: an unexported constructor-provenance marker preserves
the old attachment-free queue-reconciliation acknowledgement when the original
client has no completion interface. New neutral targets refuse unsupported
reconciliation; attachment-aware legacy deletion still requires completion.
This does not select a backend from browser data or invent native support.

## Checks

Declared hooks: no hook framework/configured hook path or active non-sample
hook in this worktree; no hook was disabled. The initial plan/state tracking
commit preceded source work. Code and docs were committed with a file-based
message. D sources and dependency pins were not edited.

All commands use C's package-derived Nix environment:
`nix develop .#packages.x86_64-linux.default --command ...`.

| Check | Result |
| --- | --- |
| Exact Python `import jsonschema` | Passed inline after environment watcher diagnostic quoting was found inconclusive; no claim based on that diagnostic |
| `go test -mod=readonly ./conversation/... ./cmd/codex-web-example -count=1` | Passed; final focused run conversation 0.126 s, example 0.019 s |
| `node --check conversation/assets/conversation.js` | Passed |
| `node --test test/*_browser_contract_test.cjs` | All 110 existing browser tests passed, about 1.8 s |
| `python3 test/codex_protocol_contract.py --coverage-only codex/client.go` | Passed; native corpus unchanged |
| `go list` imports for `./conversation/backend` | `context` only |
| Formatting / `git diff --check` | Passed; clean worktree after commit |
| Root Go unit coverage | Exact-head CI's declared default flake check runs `go test ./...` and passed. A separate local root run was requested before launch, then marked redundant if not already started; no local result is claimed |
| GitHub [Check run 43194005586](https://github.com/aither64/codex-web/actions/runs/43194005586), attempt 1, exact committed head | Success; 09:43:37–09:45:02 UTC. Workflow executes `nix flake check --print-build-logs`, including default and generic-source checks |

New coverage includes an external neutral backend importing no native client,
existing browser route operations, denied versus unsupported support, identity
and origin refusal, original request IDs across generation changes, unknown and
invalid send outcomes, optional-slot absence and native callback object/order.
Exported DTO projection checks compare populated and empty native wire values;
nil/empty collections remain distinct. An external fixture compiles original
Client/Target/Options and optional interfaces. Existing presentation/citation,
cursor/error logging, send cancellation, prompt token, pending revision and
attachment deletion tests pass through the shared path.

Early focused checks caught private-helper test adaptations and a page-error
logging regression during extraction. These were fixed before the committed
head; page failures retain the previous sanitized log boundary.

## Acceptance handoff

P1 source, technical docs, quick checks, feature publication and exact-head CI
are complete and ready for lead acceptance. No local full-flake or native/live
integration check was launched. The existing GitHub workflow ran its declared
flake check automatically on the feature push. No independent final
review is claimed: the lead owns the completed-deliverable review boundary and
combined packet. No default merge, deployment, profile activation, live account
or session lifecycle action was performed or authorized by this package.

The maintained embedding docs are README's neutral-handler link and
`docs/reference.md#conversation-backend-adapters`. The context-owning implementer
applied the English writing workflow while preserving API identifiers and
compatibility/recovery facts.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
