# P2-C source and fake-adapter evidence

Status: source/fake implementation committed at
`a12c01ee4babf72cf0994d6b49f2f8b834e2be5e`, ready for lead acceptance.
The exact-path D commit window is closed; index was verified empty and all owned
paths clean before release. Implementer2 retains fixes. The lead closed the
writing pass before commit. No production Pi creation, lifecycle, profile
activation, auth or model operation was run or enabled. The session stays open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

## Source and ownership

- D worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace`.
- Initiative base: `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
- Accepted reader slice: `063c4a4b151aff3d8d8d16712c688e4a9fa9ac9c`.
- Accepted guard slice: `67e08f2f10faa288aefb7e97e2d3eb19d8819eb6` over
  `4f390101de7ca5047d9e41faa0b483088d591185`.
- Parent at refreshed source checkpoint: `6a3631ef6ee225d7c532f62bd5f0222bb6fc582d`
  over P3 `a74ae62bfb57cdb1858381a8c66855e2ab9f2b5b`. P2 adds the supplied
  real supervisor handler's main registration. All 11 recorded P4 Go input hashes
  match the retained verification snapshot; its source commit needs no test rerun.
- Final P2-C range: `6a3631ef6ee225d7c532f62bd5f0222bb6fc582d` to
  `a12c01ee4babf72cf0994d6b49f2f8b834e2be5e`, one 29-file commit.
- Exact owned paths and SHA-256 values: `/tmp/p2c-source-checkpoint.json`.
  `/tmp/p2c-commit-receipt.json` verifies all 29 committed blobs against those
  hashes, full parent/head, inventory, and terminal index/owned-path state.
  Peer P3/P4/P5/P6/P7 source and index entries are excluded.
- Message file: `/tmp/p2c-commit-message`; normal exact-path staging and
  `git commit --only -F` completed with no hook bypass.
  No hook framework/configuration or active commit hooks are declared in D.
  Normal Git invocation remains required; no hook bypass is requested.

The scope is complete schema-4 receipt/companion/journal/completion/tracking
support, immutable P4 selection projection, durable binding/live publication,
P3 authoritative original-input proof, retained root proof and member-ready CAS,
Ruby tracking handoff and package guards. `piCreationSchema:4` describes these
implemented formats; it enables no native or browser capability.

The workspace-host source hunks are stable and were reported ready to close.
No additional host edit is planned without a concrete fix or lead continuation.

## Contract behavior

The accepted receipt precedes effects. Companion, journal and creating binding
precede tracking and native-create intent. The original native/input IDs survive
replay. Native-create intent without a result, missing native/history/input proof,
Unknown and terminal NotSubmitted stay held; none dispatch another Create/Send.
Root readiness retains selected members explicitly creating.

Member publication checks the full typed P3 CreationProof and original Accepted
input, including context/settings/reference/message witness, after trusted roster
admission. It writes binding CAS before same-generation projection. Exact partial
projection replay completes the same revision; ordinary dispatch remains held
until the current binding/projection match.

The immutable completion stores `initialSubmissionDigest`. Pi cache retirement
removes only the mutable receipt, retaining existing request/completion/journal.
Later root proof reconstructs the original complete P3 reference and uses Lookup
plus current native verification. Historical completion revisions require full
unchanged creation/options/reserved tuple/lead/tracking proof; first publication
requires equality, and live authority remains exactly current. Member CAS cannot
precede completed root journal/evidence.

## Verification

All Go/Ruby commands use the cached declared environment:

```sh
nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command ...
```

Go uses `-mod=readonly`. No partial P7 flake evaluation, pin/vendor mutation,
live lifecycle fixture or known P1 queue-failure rerun was used.

| Check | Result |
| --- | --- |
| Session full package after format declaration | Passed, 3.904 s |
| Agentteams full package in retained batch | Passed, 10.368 s |
| Original 12 durable crash boundaries and Unknown/NotSubmitted batch | Passed, package 17.987 s; fresh Luna/low watcher wall 36.978 s |
| Larger retained-root/member/legacy web batch | One fixture failure in package 44.430 s; generation-negative mutation equalled the valid fixture generation |
| Exact corrected generation case | Passed, 1.085 s |
| Entire authoritative member-proof group after correction | Passed, 15.638 s |
| Retired cache -> first member CAS -> unchanged historical root proof | Passed with selection/journal checks, web 1.092 s |
| Wrong/missing root native history | Passed, 2.224 s |
| Fresh actual acceptance fences before native Create; receipt-only and final-ready portal-memory loss | Passed, 2.081 s |
| Immutable replay/options/epoch, forged ready tracking and package change after runtime lock wait | Passed, 0.706 s |
| Incomplete five-field Pi receipt, null/legacy/oversized input refusal and journal strictness | Passed, web 0.111 s / session 0.048 s |
| Typed schema-4 manifest cannot emit null repository scope | Passed, 0.023 s |
| Actual supplied supervisor command negative arguments and unregistered browser Pi refusal | Passed, command 0.061 s / web 0.073 s |
| Ruby host full-shape/target/retained/orphan/no-runtime fixtures | 6 tests, 71 assertions, passed, 0.210 s |
| Ruby manifest and legacy writer byte-preservation/refusal fixtures | 3 tests, 42 assertions, passed, 0.080 s |
| Ruby syntax, Go formatting and owned whitespace | Passed |

The larger retained batch's sole reported failure was a test-data no-op, not a
relaxed proof check: the negative case assigned generation `8...8` after the new
completed-root fixture also used `8...8`. Changing the negative value to `7...7`
made the exact case and its full proof group pass. The larger batch was not
repeated. The final focused-web script at `/tmp/p2c-final-web-check.sh` was
prepared but never launched; it is not verification evidence.

Watcher evidence: `/tmp/p2c-crash-watch-20261112.log`,
`/tmp/p2c-crash-watch-20261112-result.json`, `/tmp/p2c-crash-source.json`,
`/tmp/p2c-retained-watch.log`, `/tmp/p2c-retained-watch-result.json`, and
`/tmp/p2c-retained-source.json`. Both launched watcher commands are terminal.
No P2 command or operation-owned cell remains running. An identity-directory
launch refusal and an intervening P3-HEAD launch refusal both preceded execution;
neither caused a duplicate test launch.

P4-A is committed at `6a3631ef6ee225d7c532f62bd5f0222bb6fc582d`, with its
index window reported closed. Lead then granted P2 the sole short window; the
fresh parent and empty index were verified before staging. The lead's direct
writing/Humanizer pass in `docs/pi-creation.md` was included unchanged. P2's
window closed immediately after commit/inventory/empty-index verification.

P4's owner fixed the absolute-workspace/64-hex identity mismatch at
`fc02306ab8e66f85fdae06519b1c907dc1728120`. Later canonical-account source
correctly rejected the old synthetic catalog refs. Only P2 fixtures were updated
to canonical mappings, including two native providers sharing the same model ID;
P4 truth, complete fallback chains and member overrides were preserved.

## Actual predecessor entry-point proof

The predecessor archive is exact D base `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
Its `libexec/workspace-host` blob is
`4a2e0aa94439932d5fd971e7206db1df6b53b8ba`, verified equal to the archived file.
The baseline's own test harness called its actual `prepare_profile` method for a
schema-4 receipt and a retained ready journal, through both stable and
`--from-candidate` entry. All four refused before profile selection, quiesce or
configuration and preserved the evidence bytes.

Result: 1 test, 36 assertions, no failures/errors/skips, 0.130510 s. Source,
driver hash and outcomes are retained in `/tmp/p2c-predecessor-source.json` and
`/tmp/p2c-predecessor-result.json`. Disposable source archive:
`/tmp/p2c-predecessor-lyomjnyg`. This is an old-parser refusal witness, not a live
package transition or deployment.

## Documentation, history and remaining gates

Project reference: `docs/pi-creation.md`, linked from `docs/dev-sessions.md`.
It keeps durable behavior, compatibility, failure semantics and lock ordering
with the feature. This evidence file holds temporary execution details. The lead closed the
writing pass and its approved text is committed.

This package introduces new opt-in file formats; it migrates/converts/removes no
old state and changes no default. No schema-4 state from this source was deployed,
released or externally consumed. Accepted earlier reader/guard commits retain
their provenance; branch-history consolidation and whole-deliverable independent
review belong to the lead's final review packet. No merge approval or branch
readiness is claimed.

Full-web readiness remains separate. P1-F fixed the two old queue-stage failures
in C at `ee0c866317419209b859b27a09026d63e722c4c7`; P7 owns final pin consumption.
The full Web suite and long installed checks were not repeated here. Real Pi
creation/composition remains gated on released P3/H0 ownership/permission/native
witness and immutable provider configuration/account support. New team/tool/
runtime-successor maps remain absent until their separate central release.

P6 browser capabilities have a separate required integration dependency in
`design.md`: P2's existing refresh/invalidation owner must inject complete current
P3/runtime/authority/policy/lineage/domain-tool proof. Snapshot/Lookup/GET/render
remain native-free; absent, stale or invalidated observation hides controls.
CanAccept binds the latest proposal/caller/digest/current lineage, and every fresh
action still performs independent admission and Inspect/Apply. The optional pure
adapter does not close that live wiring gate. No source window, poller, production
injection or new package is implied by this clarification.

Next: lead acceptance and independent final review. P2-C execution is terminal;
fixes remain owned. Capacity for a separately released production continuation
was reported conditional on acceptance; no successor package has started.
The next D index window belongs to the lead's P5-I sequencing. No partial push,
merge, deployment or session lifecycle action was performed.
