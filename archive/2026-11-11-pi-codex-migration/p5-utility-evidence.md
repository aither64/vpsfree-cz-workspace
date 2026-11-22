# P5 utility adapter source checkpoint

Status: seven owned files committed and checked; main-agent writing pass closed
and D index window released. Await lead source-package acceptance. H0/P5 fixes
ownership remains with implementer3; no additional package is queued. This is
compositional evidence, not complete native utility readiness.

Session: `2026-11-11-pi-codex-migration`.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace`.
Initial checked HEAD: `563f6be3ae0498c4b4e9d5fffe0c8844f4555e75`, plus the exact
owned source and concurrent P3 source identified below. Final exact source range:
`6d2730282d871383dfc56d05143830e29ecfe619..0e8c0fb5b1357a3810df9f35b1dfe040a874fa41`.
The final parent contains actual P3 API commit
`2dd2af9499fa64602bfce94c20a17b6e41139eca`. Current/env binding and retained
Sol/xhigh/workspace_write were verified again before committing; both
DEV_SESSION environment variables were absent.

## Source and contracts

Lead released this one dependent package after accepting P5-I at
`e457834e23a2bda09e528ac8c532c16e912c33b2`. The accepted TEAM-I/design.md
utility and read-authority contracts apply. Implementer1 directly confirmed
the actual exported types before dependent edits, the Controller/admission
ordering, successful pre-input Create state `initialized`/Persisted false,
and the independent Accepted callback/report race. Architect0 and lead accepted
the original terminal Lookup correction and compositional current milestone.

Exact owned files:

```text
docs/pi-teams.md
portal/internal/monitoroperation/pi_operation.go
portal/internal/monitoroperation/pi_runtime.go
portal/internal/monitoroperation/pi_runtime_test.go
portal/internal/monitoroperation/pi_service.go
portal/internal/pihosttools/utility.go
portal/internal/pihosttools/utility_test.go
```

The new typed `PiRuntimeAdapter` consumes actual `piruntime.UtilityController`,
`UtilityAuthority`, `UtilityReadAuthority`, `UtilityRef`, `UtilityGrant` and
`UtilitySubmissionDigest`. Existing persisted DTOs are converted at that seam;
there is no local substitute for the native API, digest or receipt engine.
No P3/session/central/H0/packaging source is owned or edited here.

- The same Manager is composed with the adapter as utility effect/read authority.
  Controller calls hold no outer transition/runtime admission; Manager invokes
  its configured authority once per effect. Existing Domain admission/verifier
  runs without a short monitor lock across the native callback. Missing ports
  remain unavailable; no registration or capability metadata is changed.
- Create intent is claimed durably once before CreateUtility. A lost reply with
  no saved mapping remains held, without another creation call. The exact returned
  mapped ref, generation and settings are checked and saved before any input.
  Successful pre-input state must be initialized and not yet persisted.
- The actual P3 digest over original ref/input/settings is saved in the existing
  operation before Bind/Send. Only the invocation that newly reserves that input
  may send. Every later Launch call uses original-ref Lookup only, including a
  lost/unavailable Bind. There is no load, resume, inferred capability or new ID.
- Lookup uses separate current-runtime read admission and the original saved ref.
  Validate tagged schema2/utility owner, full utility/root identity, original
  generation, input/settings/digest and authoritative terminal witness or positive
  pre-acceptance refusal. A receipt still Unknown remains held. Exact terminal
  Lookup can resolve a domain Unknown; Accepted and terminal NotSubmitted remain
  immutable. Final publication compares the unchanged snapshot under the short
  operation lock. Recovery never infers current worker activity or settlement.
- P3 confirmed callbacks can precede Send's reply/domain projection. The configured
  report handler captures exact trusted HostCall.Runtime and utility/input, then
  uses Lookup reconciliation before the existing immutable report slot write.
  It neither waits for Send nor holds effect/store locks across Lookup. Invalid
  model arguments cannot supply runtime/input authority. Default tool projection
  remains absent; transport registration is still a separate owner gate.
- Cancel never calls unload. Explicit admitted unload requires positive verified
  exit and still does not settle. Durable terminal report plus source/worker exit
  remains incomplete until all registered resources/callbacks/tools and inventory
  are positively drained. The existing report/settlement store remains authoritative.

## Exact source and quick checks

Final seven-file source manifest:
[p5-utility-final-source-sha256.txt](p5-utility-final-source-sha256.txt), SHA256
`43540723328e5c12dfbf6c3a629783dce7723c447e190811e2bdab8e70df49f6`.
Final relevant P3 input manifest:
[p5-utility-final-dependencies-sha256.txt](p5-utility-final-dependencies-sha256.txt),
SHA256 `745596e5c3ae54bd8fcaf3bb5eb087bcbf4c23549524cb1e286bd1f6b0d8a97e`.
The shared working tree was dirty; these bind owned/relevant inputs and the
committed base, not a complete immutable whole-package snapshot.

All Go checks used the exact cached D environment
`/nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv` and explicit
`-mod=readonly`. No current-flake evaluation or implicit lock update was launched.
These known short package checks ran inline; no long or uncertain native test
was launched. All commands are terminal.

| Check | Result / evidence |
| --- | --- |
| Initial typed adapter fixtures | Passed, monitoroperation 1.966s. |
| Full affected package regressions | monitoroperation 7.996s, pihosttools 0.020s; [log](p5-utility-go.log). |
| Final strict-Create focused check | Initially compile-blocked by concurrent P3 conversation.go missing encoding/json; [failure](p5-utility-final-focused.log). No owner takeover or duplicate command to repair reporting. |
| Final affected fixtures after P3 coherent compile | Passed, monitoroperation 2.965s; [log](p5-utility-final-focused-fixed.log). |
| Isolated committed parent plus exact seven-file overlay | Passed, monitoroperation focused adapter tests 2.846s; [log](p5-utility-committed-parent-check.log). Builds and runs without uncommitted peer source. |
| Owned Go formatting and whitespace | Passed; no changes from gofmt listing and no git diff --check errors. |

Commands:

```sh
nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command \
  go -C portal test -mod=readonly ./internal/monitoroperation ./internal/pihosttools -count=1
nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command \
  go -C portal test -mod=readonly ./internal/monitoroperation -run '^TestPiRuntimeAdapter' -count=1
```

The full-suite owned source is retained in
[p5-utility-full-check-source-sha256.txt](p5-utility-full-check-source-sha256.txt),
SHA256 `4d9a63382e1f599d61f35a5445736585cc8ce4cb2b75bb34d9bd0b1c596e59ac`.
Subsequent code changes were confined to the new adapter and its focused tests:
strict pre-input Create result checks and invalid report/unload refusal before
native access. The final focused pass covers these changes. Other owned code
remained equal to the full-suite snapshot. Unchanged full packages and Node
factories were not rerun. Previous accepted P5-I evidence remains applicable
to its unchanged codecs, policy, factories and legacy behavior.

Six focused adapter tests and their fault subcases cover real exported type
compatibility; frozen grant/ref/digest-before-Send; single-send and lost replies;
held read under a permitted newer current runtime generation without changing
the original receipt; missing admission and stale generation with zero effects;
wrong create mapping/settings/generation/persistence; wrong receipt owner/root/
generation/input/settings/witness; both original Unknown-to-terminal resolutions;
terminal immutability; stale publication after cancellation; lost Bind never
retrying; early report before domain projection; explicit report retry identity;
and durable report plus exit retaining the callback-drain capacity hold.

## Dependencies and final integration gate

Architect0 clarified the source dependency and saved it in design.md: a real,
buildable committed P3 parent containing UtilityController, UtilityAuthority,
UtilityReadAuthority, ref/grant types and UtilitySubmissionDigest is sufficient
for this inert adapter commit. This adapter has no direct Manager construction
or method-body dependency. The parent and adapter must build without uncommitted
dependencies, and the exact checked API/helper inputs must be preserved or their
verification applicability reconciled before commit. The lead granted the sole
short index window after P2's factory commit; its source requirements were met
and the window is now closed. No substitute export, stub, harness or registration
was added.

At the final parent, committed utility_types.go, types.go, receipts.go, manager.go
and callback_types.go exactly matched the checked relevant input hashes. Only
conversation.go differed from the final dependency manifest (checked SHA256
`7a0248206a640af4921dc96416bcf15db87b379cd87bc26f70031868a5b76604`,
committed/current SHA256
`69b17b3b3a33f99f9bc98bc9fdd445b2d67de40b43aeacdc61a93334f86be33d`).
No equivalence was inferred. A git archive of exact parent
`6d2730282d871383dfc56d05143830e29ecfe619` with only the frozen seven-file overlay
compiled and passed the adapter-focused suite in 2.846s. That check reconciles
the changed dependency and proves this package builds using committed actual
exports without uncommitted peer inputs. It ran from disposable source copy
`/tmp/p5-utility-committed-parent-c4riq97p`, recorded in
`p5-utility-committed-snapshot.txt`. A tool-process launch was rejected before
execution; the single successful check was launched afterward from the verified
session directory. No running or uncertain command remains.

The fixture implements the real exported interface and uses the real digest
helper, not a native engine. Actual Manager utility methods/shared engine,
tagged-root and native flow remain required before functionality or production
composition. Implementer1 owns that implementation, exact owner/root checks,
native callback transport and utility-specific integration.

The earlier owner P3 Manager/Unix/pinned-SDK evidence remains its own component
proof. This packet does not extend that evidence to a complete admitted utility
flow. Lead/architect0 explicitly require real admitted utility
create/load/bind/send/lookup/report/drain against the actual worker in owner1's
existing harness/normal final post-review integration window. No duplicated
framing/Nix harness, production fake API or test-only export was added here.

P2 still owns central current-package writer/read authority, preflight/actual
older-candidate compatibility and registrations. Missing those ports refuses.
No installed launch, native utility, credentials, model/auth, profile, service,
session lifecycle, deployment or merge action was run. No repository/machine
claim is held. No automatic cleanup or lifecycle action is authorized.

## Documentation and history

`docs/pi-teams.md` remains the feature-contract home: exact typed composition,
current read authority versus original receipt generation, no-resend recovery,
early explicit reporting and complete-drain limits. Lead read the amendment
and closed the context-owning writing pass with admission and terminal-Lookup
wording only; final document SHA256 is
`d4388591d42aee0a295089dfe6313118d1f54975934cc22ab8ab8b8bc9cfb2f5`.
No code or strings changed through that pass. Session records own temporary
heads/checks/dependency holds; no duplicate rollout guide was created.

No new record format, database/conversation migration, converter, retirement,
cleanup, removal or default switch is introduced. Existing communication forward
codec/rollback obligations from P5-I remain unchanged. Domain Unknown resolution
does not modify or replace P3 receipt bytes or logical IDs. Source is committed,
undeployed and not externally consumed by this package. One logical source commit
was made; lead owns final combined history/migration review and independent
review invocation.

## Final commit and index receipt

Commit: `0e8c0fb5b1357a3810df9f35b1dfe040a874fa41`.
Parent: `6d2730282d871383dfc56d05143830e29ecfe619`.
Subject: `pi: connect monitor utilities to the typed runtime API`.
Exactly the seven paths above were staged and committed, with 867 insertions
and 10 deletions. Staged, committed and current source/prose SHA256 values all
match final manifest
`43540723328e5c12dfbf6c3a629783dce7723c447e190811e2bdab8e70df49f6`.

Before staging, exact parent and empty index were verified. Commit used a
temporary message file and normal `git commit --only -F ... -- <exact paths>`.
No declared hook framework or active executable hook was present; no hook bypass
was used. Owned paths were clean and the index empty after the completed commit.
P3/P2/B2 and all other peer source remained untouched. No partial push or merge
was performed.

The window was immediately released to the lead via report_to_lead message
`e1cc3397-e31c-4a2b-a0a1-763eb3e5ecf3`; raw receipt is
`p5-utility-commit-receipt.json`. Source package is reported for acceptance, with
H0/P5 fixes ownership retained and capacity available after acceptance. No next
package is queued; actual Manager/native/central proofs remain required.

Stable session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
