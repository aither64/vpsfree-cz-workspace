# Refreshed review disposition

Reviewed exact range: `10bb047513c82d1310e8fcaa797e8772f948dd8a` ..
`543d7ac796fdd06f730e5d2de9a47d4a8d74e7f4`.
Report: [independent affected review](refresh-review.md), retained reviewer0
Sol/xhigh, all four lanes. Original reports remain unchanged.

R5 Important accepted. Lead selected the reviewer's bounded correction: prevent
another explicit copy of a receipt referenced by a saved original, while
preserving exact-ID recovery. No transitive copy graph or migration is added.
Architect disposition is recorded in design.md. Existing ambiguous identities
are retained; the change does not infer delivery or delete unknown receipts.

Direct step9 source inspection confirms current durable incoming-reference
checks at rendering and the resend/enqueue mutation boundaries; resend rechecks
after asynchronous reconciliation. Storage-read uncertainty cannot authorize a
copy. No new visible application strings. The guide explains recovery and the
limit while the incoming link is retained.

Focused regressions cover buffered/legacy replacement targets, reload, no third
identity/order write/draft loss, stale/direct invocation, unavailable storage,
incoming link during reconciliation, saved original-link recovery and exact-ID
replacement retry. Lead identified and requested correction of an initially
ambiguous UI assertion; the final fixture explicitly checks target B's rendered
position and pending-message identity order.

Status: source/test/doc diff and all four hashes inspected; focused Node,
aggregate and Go checks pass. UI-only guard removal fails the precise target-B
assertion, confirming the UI regression is effective. Lead accepted the narrow
repair and authorized final owning fold; exact consolidated-head inventory remains
complete at final head `01218bf9458aefc8971ac4d31d8da415392d0a25`, tree
`af3991b2e88d0b5c024982c118b4367e835a43e3`. Lead verified the final correction
diff exactly equals accepted r5-held.patch (SHA256
`a1f8bb757160a057e2170eb211c32e78aec6ed7e06d5d8d2f74d868ff859f589`).
Five commits remain, with unchanged settings/unread; no obsolete history, repeated
update stream or migration. Post-fold focused quick checks pass (Go2.044s).
Long refreshed verification may now proceed. The reviewer explicitly identifies this guard as a narrow scope
reduction suitable for direct step9 checks, so no rubber-stamp review turn is
required. A transitive-copy design would require affected-lane review and is
outside this disposition.

Final fixture correction: `01218bf9..9293e314` changes only
`portal_improvements_browser_test.cjs` to assert the reviewed durable-capture
contract: clear the captured editor, retain exact text/ID in the saved receipt,
retry the same ID after reload, and preserve a newer draft. The strict per-ID
storage assertion replaces an ineffective optional lookup. Lead inspected this
bounded correction and the passing real-browser evidence; no application,
protocol, pin, Go or guide change is introduced. This remains within direct
step9 verification of the assessed recovery behavior.

Final inventory is `10bb047513c82d1310e8fcaa797e8772f948dd8a..9293e314e6028d71a57595073117b51bdc53c8ff`,
tree `b005a5438eb3649480881f134f770b67dbe2eb0c`: five coherent commits,
settings/unread unchanged, quiet/guide patch-equivalent to012, composer owning
the fixture correction. No obsolete fixups, repeated update streams or
migrations remain. The exact final tracked blobs and modes match the passing
prepared browser snapshot; native verification reuse also has identical
derivation/output and input receipts. See [verification summary](verification-summary.md)
for check scopes and final CI disposition.

Exact final-head CI40143026250 completed successfully: fast/package, creation
and archive passed; host skipped. Lead inspected the raw completed job metadata
and watcher exit0. Post-CI SSH refs confirm final9293e314 and base10bb0475;
the feature worktree remains clean. Ready, awaiting merge approval; no default
integration, deployment or session lifecycle action has been performed.
