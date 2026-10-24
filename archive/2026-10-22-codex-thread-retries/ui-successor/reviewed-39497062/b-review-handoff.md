# B presentation milestone handoff

Session: 2026-10-22-codex-thread-retries. B owner: implementer1.
Committed and SSH-published final:
`39497062e0da98a70386355384fa922c0eaa0168`.
Tested/committed tree: `28a9d72044dc3ffa7eb4f817cbb2c4d6c9614d18`.
Base: `bf6d4b0c49600c15e17fe71248807ef43424e932`.
Deployed predecessor: `7b8c646974df72e0df3e576d10f09d79823ae004`.
Source is clean and frozen for retained independent affected review.

`b-final.json` binds all eight commits, source metadata, Go/Nix/vendor selection,
tested tree, consumer graph and evidence hashes. `b-final-history.json` lists the
complete series. `b-full-final.patch`, `b-deployed-final.patch`, both range-diffs
and `b-lineage-proof.json` establish the final diff and retained boundaries.
The original core/capability/runtime commits are exact; retention and both
incident2 patches have identical stable patch IDs. Only final A selection
changes their pre-presentation product tree. Deployed refs/bundles/receipts remain.
The deployed SHA is not a literal ancestor after approved pin consolidation.
No migration, retry schema or generic ledger format changes are introduced.

One A stream selects published `f86290673d752c77b56c70228c3d26aced75e177`.
No policy sidecar, controller, action authority or runtime guard expansion is
implemented in this milestone. Manual delivery remains independent of optional
policy/activity metadata. Without the optional provider, the new controls stay
unavailable. Presentation API fixtures do not prove backend dispatch.

Docs: `docs/workspace-portal.md` and `docs/turn-retry-recovery.md` contain the
lead-approved copy and retain native/admission/schedule/uncertainty warnings.
`b-visible-copy.md` records the direct main-agent writing pass.

Quick checks passed (`b-final-quick.log`, `b-final-syntax.log`): Node syntax,
paging contract, all 17 read-cycle cases; actual shipped-client HTTP/import
harness and incident2 plan delivery/runtime contention selectors, 5.965s;
browser fixture Go compilation, 0.042s. `quick-commands.md` has exact commands.
Earlier command-selection failures and the stale baseline source assertion are
retained in the parent tracking logs. They were corrected through supported
harness selection and the stronger current callback assertion, without product
relaxation.

Next: lead assigns retained affected review, then one fresh watcher runs only
`capture.sh`. It verifies frozen head/clean source, enters the repository's
locked Nix shell and portal scope, and selects the single controlled Playwright
fixture with 240s timeout. `environment.json` / `b-toolchain.stdout` bind the
resolved Nix Go, Node, Playwright and browser paths. Screenshots go to
`ui-successor/screenshots`. Browser time is frozen before navigation; the first
capacity capture stays at 3 starts / 15s / 70s elapsed. The fixture covers
root/member desktop/mobile, short/empty/long layout, footer stability, timer,
keyboard, focus, history, dismissal/reload/new-chain and Settings interactions.
No screenshot run has started. User visual acceptance precedes policy backend
expansion, long checks or deployment. No W/C edits or lifecycle actions occurred.

CI run 40012270221 was in progress at one final-head snapshot. All recent
superseded runs were complete; no cancellation, wait or rerun was needed.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
