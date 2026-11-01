# Final source review: portal delivery recovery

Review outcome: **three Important findings; no Blocking findings**. Fix or
explicitly accept the Important findings before continuing to long integration
checks. No source changes were made by the reviewer.

## Findings

### Important I1 — Composer resubmission retains a stale definitely-unsent state

`dev-workspace`, commit `4d2c7069`,
`portal/internal/web/static/app.js:5593` and `:5600`.

After a `message_not_sent` response, entering the same text/attachments in the
composer matches the saved `unsent` attempt. This path saves that attempt
unchanged and retains `state: "unsent"` in memory before calling
`sendingClient.message`. The receipt therefore says **Not sent.** while the
request is in flight. Reloading after dispatch but before the response preserves
that false claim, even when the server has admitted or accepted the message.
This is especially relevant now that admitted HTTP sends intentionally finish
after browser disconnection.

The separate receipt-retry path correctly persists `unknown` before dispatch at
`:5423`; the composer path needs the same invariant. Preserve the ID and all
bindings, durably retire a previous `unsent` classification before dispatch, and
show `sending` in memory. Add a focused regression for composer resubmission
after a proven refusal and reload/response loss during that retry.

Reviewer reproduction used the existing composer VM fixture with a saved
`unsent` attempt. After the HTTP stub was entered, it reported:

```json
{"calls":1,"persisted":"unsent","inMemory":"unsent"}
```

Origin: general, architecture/repetition, risk/compatibility. The native same-ID
ledger still prevents an automatic second mutation; the defect is incorrect
delivery certainty and recovery presentation.

### Important I2 — Browser storage failure falsely declares an uncertain original unsent

`dev-workspace`, commit `4d2c7069`,
`portal/internal/web/static/app.js:5425`.

`retryMessageReceipt` accepts both `unknown` and `unsent` receipts. If saving the
retry record fails, it unconditionally constructs an error with `notSent: true`.
For an already uncertain original, proving that this new retry did not run does
not prove that the original message was never delivered. The shared failure
presentation consequently tells the user **The message was not sent. Try
again.** while the original receipt correctly remains unknown. Storage quota or
storage access failure is sufficient to trigger this discrepancy.

Keep the storage diagnostic, but retain uncertain delivery guidance for an
unknown original. Set definitive `notSent` only when the original itself is
known unsent. Cover the failed-storage path for both starting states.

Reviewer reproduction with the existing submission-notice VM fixture, an
unknown original and a failing store returned:

```json
{"receipt":"unknown","banner":"The message was not sent. Try again."}
```

Origin: general, risk/compatibility.

### Important I3 — Late queue-start failures bypass the new feedback generation

`dev-workspace`, commit `4d2c7069`,
`portal/internal/web/static/app.js:5520`, with the existing caller at `:5675`.

The freshness check only runs when a caller supplies an operation token.
Queue-start still writes to the same global composer notice without starting or
passing a token. Queue-start can overlap a composer send: neither
`submitMessage` nor the send-button disabled state checks `queueStartInFlight`.
If the newer send succeeds and the older queue-start subsequently fails, that
old failure restores the stale composer error. This contradicts the new
documented guarantee that late older operations cannot restore it.

Bind queue-start's feedback to its operation generation as well, or move its
feedback to an independently owned queue notice. Preserve the distinction
between explicit operation completion and transcript observation when doing so.
Add a controlled late queue-start rejection after a newer successful send.

Reviewer reproduction evaluated the actual queue-start listener and new notice
functions with the existing VM fixture. It started queue-start, accepted a newer
composer operation, and then rejected queue-start. Final state:

```json
{"hidden":false,"textContent":"Late older queue-start failure"}
```

Origin: general, architecture/repetition.

## Reviewed range and history conclusions

- `codex-web`: `11ec57d2203fc735696fe75a837d47da55a5c6af` through
  `2c4c3460ac6d109699d05115b0ebb9e6eb3410df`. Complete series: one commit,
  `codex: preserve retryable sends before write admission`.
- `dev-workspace`: `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734` through
  `8ccdd2e43b6bb78ce474e19c69d232442db2562a`. Complete series:
  `4d2c7069e5fb3ef2414ce56a232feea20850cd74` (portal behavior, tests and docs),
  then `8ccdd2e43b6bb78ce474e19c69d232442db2562a` (dependency selection).

Both worktrees were clean at inspection. Their recorded bases are their actual
merge bases with the reviewed heads. I inspected the complete series and final
diffs. No obsolete unmerged approaches, superseded follow-up commits, unused
compatibility paths or fixup history remain. The owner-level source commits
present coherent delivery-recovery behavior with their tests/docs, and the
consumer pin change is separate.

**Pin consolidation:** no repeated update stream exists in these ranges. The
single consumer dependency commit selects the exact reviewed codex-web source
in Go and Nix together, including vendor hash. Native Codex and unrelated flake
inputs do not change. Retaining the previous Go checksum entries is checksum
history, not a second selected dependency or a redundant pin commit. Later
workspace/configuration composition pins are outside these reviewed source
ranges and still need exact selection/contract verification.

**Migration lineage: no migrations.** The native wire protocol and schema-3
submission ledger remain unchanged. Browser `unsent` and `replacementId`
metadata are additive; old decoding ignores them. There is no unapplied branch
migration or schema step to consolidate.

## Lane conclusions and compatibility

General: the provider now records `submitting` immediately before the mutation
write, under the existing writer lock and after context/generation validation.
Earlier uncertain attempts return through reconciliation before this new
admission path, so absence from history does not reset them. The selected
invalid-request/method/parameters RPC refusals have an explicit prepared-state
restoration; transport/write/reply failures remain conservative. HTTP errors
expose delivery state while keeping underlying socket/RPC details in logs.

Architecture: transport evidence and typed errors belong to codex-web; portal
receipt recovery and composer feedback belong to dev-workspace. I inspected the
Go/Nix pins, shared conversation handler/assets, ordinary workspace wrapper,
managed-retry wrapper, member option recovery, cold recovery path and upload
preparation. The provider's private admission callback does not expand the
public native protocol. Findings I1 and I3 identify rules that currently diverge
between real UI callers. No additional shared framework is needed to fix them.

Scope: this is a bounded portal recovery implementation. It introduces no
native deduplication mechanism, background job system or speculative recovery
framework. Replacement submission first retries/reconciles the original,
requires duplicate-aware confirmation, saves the new ID and original linkage
before dispatch, and leaves the current composer draft alone. Retaining the
original record and both identities is appropriate.

Risk/compatibility: authorization, exact-origin checks, trusted conversation
resolution, mutation locking, attachment scope/identity validation and private
ledger permissions remain in place. The detached HTTP operation retains the
request's deadline and server-shutdown cancellation, with resolution release
and mutation-lock lifetime still spanning completion. Existing uncertain native
records remain uncertain. New and old ledgers are compatible; old browser
clients lose the new presentation/replacement affordance but do not gain an
automatic duplicate dispatch. The companion module and Nix source selection
match; rollout should retain that pairing. The trusted host-operator boundary
does not require new hostile-local-filesystem defenses.

Documentation: the changes are discoverable from both README entry points and
keep lasting behavior with its owning project (`codex-web/docs/reference.md`
and `dev-workspace/docs/workspace-portal.md`). Individual rollout details remain
in initiative records. The definitive-unsent and stale-feedback claims need the
implementation corrections above to be accurate for all actual callers.

## Evidence and residual verification gaps

I read the review packet, initiative plan/design/state, ancestor/project
AGENTS guidance, mandatory-change-review and all four lane references. Reviewer
identity: `/root/final_review`, independent standalone fallback under the
provided installed default development reviewer policy, `gpt-6.1-sol/xhigh`;
no retained roster exists for this threadless initiative.

Reviewer checks were limited to committed-source inspection,
`git diff --check` in both ranges, and the three focused Node VM reproductions
above under `nix develop --no-write-lock-file -c node`. No long tests, deployment
or source mutations were performed. The packet's existing focused Go/Node/corpus
results were assessed as supplied evidence rather than rerun wholesale.

After remediation, the committed Chromium/Firefox flow, full packaged/native
suite, representative lost-response/restart checks and matching composed
workspace/configuration deployment contracts remain required. The new browser
flow currently covers successful replacement/reload; it does not cover I1–I3.
No live acceptance/deployment result is claimed by this report, and this review
does not authorize default-branch integration.
