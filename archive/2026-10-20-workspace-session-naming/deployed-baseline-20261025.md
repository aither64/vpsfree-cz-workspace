# Selected package baseline audit — 2026-10-25

The reviewed A `6e469863a69c7d35941ca2e15de9514223b58f4f` / B
`37a87a8a81cd3c705b7c5ee4f39338c1db1cc6ce` pair is **not a forward behavior
superset** of the selected package. It would remove newer message-delivery
recovery. Refresh A and B before dependent C builds/activation. This finding
does not block implementer1's separately approved fixture-only diagnostics and
does not release another implementation gate.

## Provenance

[Structured evidence](deployed-baseline-20261025.json) records exact identities,
NAR checks, changed-file inventories, ancestry results and contract hashes.

| Component | Previous L9 baseline | Selected 8ph baseline |
| --- | --- | --- |
| Runtime B | `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734` | `10bb047513c82d1310e8fcaa797e8772f948dd8a` |
| Client A | `11ec57d2203fc735696fe75a837d47da55a5c6af` | `872c7ad3962f9fa9b17358244e27f3e3fac59fc5` |

The selected `/home/aither/bin/workspace-host` wrapper names
`/nix/store/8ph05i3nps8xi1jfs450b16aysc16nvg-dev-workspace-0.2.0`.
`workspace-host coordination guide` independently identifies that selection.
Its derivation is
`/nix/store/idaz4jqnjy572qi03shxa26bkjlrgpq9-dev-workspace-0.2.0.drv`.
Nix's version-4 JSON places it in `derivations`, keyed by basename; its `env.src`
is `/nix/store/r2pxv5h275gk9njy59rbk4ydsjy38hx4-source`.
The derivation also references composed workspace source
`/nix/store/3g4dbw0nzyvc01gfbr08x35slccqnf0v-source` and client source
`/nix/store/gsgyaisj7mc09522i6zarg98cqj2qch3-source`.

The composed `flake.lock` pins both SHAs above; the runtime lock agrees on A.
Actual `nix hash path` results exactly match their locked NAR hashes:
B `sha256-fl8Ib9hLHxlGCjJYiAhIZgURmkclzOaBZ0veJDUCq+k=`;
A `sha256-TWGw+erya1/edYSl8/bqsb/lQNediQvFz30Ijg64PHM=`.
These prove the source identities without guessing from package paths.
Local immutable Git objects contain both SHAs. Each descends from its previous
baseline; neither installed head nor our corresponding candidate is an ancestor
of the other. No fetch or fresh remote-head assertion was made.

Both `/run/current-system` and `/nix/var/nix/profiles/system` resolve to
`/nix/store/n6b9dmmaw83zx80paglrisy0w5rwnfw8-nixos-system-aitherdev-26.05.20261021.da6dc0e`.
The composed workspace Git SHA and system configuration Git SHA are **unknown**.
The parent reports unchanged ordinary native PID 3387667, invocation prefix
84b92 and start 11625793753468; this audit did not reread processes or establish
the active portal executable from that report.

## Behavior that must survive

A adds one commit, `872c7ad`: `codex/client.go` moves send admission beneath the
connection writer lock, rechecks the shared ledger and preserves cancellation
with failed-request transport errors. `MessageNotSentError` distinguishes proven
non-dispatch or explicit protocol refusal from uncertain delivery. A failed
write or absent history never proves non-delivery. History receipts are saved
atomically as accepted. `codex/send_delivery.go:12–50` implements the recovery
classification; `docs/reference.md:46–67` specifies it. The conversation handler
keeps an admitted send alive across browser cancellation within its original
deadline and shutdown, then exposes bounded `message_not_sent` versus
`message_delivery_unknown` responses (`conversation/handler.go:596–651`).

B adds behavior commit `2c847e6d` and dependency selection `10bb0475`.
`portal/internal/web/static/app.js` preserves `unsent` and `replacementId` in
browser attempt storage, allows an explicit new-copy action only after checking
the original and obtaining duplicate-risk confirmation, and keeps both IDs for
reload/retry. It preserves the current draft/attachments and prevents late older
responses from restoring stale composer errors. Initial Send remains disabled
until browser readiness is established. See `docs/workspace-portal.md:449–469`,
`static/app.js:817–832,5388–5480` and `templates/session.html:147`.
Our reviewed branches do not contain these production changes or their tests.

## Compatibility and preserved inputs

Coordination/claim/repository-claim/integration contracts, runtime contract,
installed package metadata, agent-team catalog and coordination/operations guides
are unchanged. Runtime retry capability flags remain 1. Team execution access is
still `full_access`; saved roster settings remain unchanged. The native derivation
is still `/nix/store/zgxck45jn2z9yf70rk6d794pdn6mq3ca-codex-package-0.163.0.drv`.
The naming Luna catalog is byte-identical across old/new/current-candidate A.
The extension remains `767dfd587e346168e1443e65ccdb67ce748f3fe3`, with identical
actual extension source in old/new tool derivations. The composed lock changes
only A/B nodes; catalog deltas are command/skill store-path references, with the
coordination catalog changing only the confctl adapter command path.

Contract equality does not preserve the behavioral differences above. A keeps
ledger schema 3 and older uncertain-attempt meaning; no migration was added.
B's browser fields are additive, but old browser serialization drops them, so
reverting to our older assets would lose their recovery distinction/linkage.
Use compatible forward code/assets; do not clear retained attempts to downgrade.
No provider/model/native upgrade or new state policy is required.

## Smallest refresh and verification boundary

- A owner: preserve at least installed `872c7ad` and replay the naming patch.
  Reconcile shared request plumbing and protocol-corpus extraction deliberately;
  retain send-admission, cancellation, atomic-receipt and shutdown tests alongside
  ephemeral retry/settlement tests.
- B owner: preserve at least installed `10bb0475`, replay naming, archive
  diagnostics and the separately released creation diagnostics, then pin exact
  refreshed A. Assess B37's retirement cancellation adapter against the newer
  A request-error preservation before retaining or dropping it; equivalence is
  not proved by this audit. Preserve browser recovery tests and documentation.
- C owner, only after final A/B publication: refresh the existing configuration
  `dev-workspace/devWorkspace` channel and matching composed nested workspace
  runtime selection, preserving extension/siblings/follows/provider inputs.
  C113d/7510 remain frozen during this audit. No build/activation is released.

Quick checks must cover new A send-admission/delivery tests plus naming, B
message-delivery/composer/submission-notice browser tests plus naming/admission/
retirement and new diagnostics privacy checks. Exact commands/selectors belong
to the owners' refreshed execution packages. After committed final review, use
the lead's watcher for affected native, package, creation and full-flake gates.
Reuse only exact derivation/input verification receipts; matching capability
files or an unchanged test name is insufficient. Retain original failure evidence.

Only immutable source/derivation metadata, local Git and own session records were
used. No other-session tracking/worktrees, fetch/evaluation/build/test/model call,
application/ref/runtime/claim/lifecycle mutation or activation occurred. Evidence
and design files are the only writes. This is consultation, not final review or
merge/deployment approval.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/)
