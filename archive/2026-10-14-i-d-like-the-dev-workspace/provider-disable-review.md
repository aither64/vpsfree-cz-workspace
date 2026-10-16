# Affected final review: provider and Disable amendment

No Blocking findings. One Important finding requires a fix or an explicit recorded decision before long verification of this amendment.

## Important: a stale saved ID can falsely confirm replacement cleanup

General/API and risk lanes; portal/internal/web/static/browser-notifications.js:94-99,112-138 at 1a57ae9a038516fd4e435591ea3853de098fa8fb.

A saved registrationId is preferred over the current subscription's endpoint digest even when a new registration's outcome is unknown. After an old subscription expires, its saved ID can remain. Enable creates a replacement subscription and /register commits its new server record, but the response is lost. The catch leaves the old saved ID intact. Disable then deletes only the old record, unsubscribes the replacement, clears the old ID and cleanup selector, and reports fully Disabled while the replacement registration/outbox can remain on the server.

I reproduced this with the actual shipped module in a read-only Node VM: seed an old 64-hex saved ID with no local subscription; let Enable subscribe and the mocked server accept a different ID before throwing a lost-response error; click Disable. Its POST selects the old ID, the replacement record remains, local absence is confirmed, no cleanup selector remains, and the UI says Disabled on this browser. No real subscription, network request or filesystem write was made.

Retain and verify cleanup identity for the current subscription when its registration outcome is uncertain; do not assume an older saved ID proves that record absent. Preserve any still-required old-ID cleanup within the existing bounded design rather than discarding it. Add this replacement-subscription + pre-existing saved-ID + lost-register-response case, including reload/failed deletion. Current lost-reply tests begin without an older saved ID, so they miss the mismatch. This is inside the accepted independent-cleanup and truthful-full-disable contract.

## Other affected conclusions

The server's additive deletion selector is appropriately bounded and scoped: POST only; exactly one present non-null lowercase 64-hex registrationId or endpointDigest; unknown fields rejected; current package admission and exact trusted Host/Origin checks retained. Lookup uses the existing current-workspace private store, filters exact origin, computes SHA-256 of the exact endpoint, and removes only matching registrations and their outbox entries. Absent matches succeed idempotently. It creates no registration, changes no provider admission policy, and performs no outbound/DNS operation. Existing ID-only clients remain supported.

The new provider is only exact jmt17.google.com. The same authoritative host map serves registration and guarded transport, preserving HTTPS/443, checked public literal dialing, original-host TLS validation, redirect/proxy refusal, deadlines and response bounds. Exact-version official-source evidence and the native Chromium 147.0.7727.15 observed hostname support the bounded host addition; no wildcard or endpoint rewriting was introduced. Staging ownership is not delivery proof.

Browser cleanup generally attempts local unsubscribe after failed server cleanup, verifies local absence instead of trusting unsubscribe's boolean, retains one ID/digest selector for explicit retry, and blocks Enable while cleanup remains pending. The selector is origin-local and contains no endpoint or keys. Read, retry, unsupported/denied/offline and local-unknown behavior are covered by focused contracts. Storage failure remains the documented limitation for retry after reload. Apart from the stale-ID finding, the implementation stays proportional: one additive deletion lookup over the bounded store, no new server index/schema or cleanup framework.

Feature and operations docs reflect the provider and cleanup contract, link exact upstream evidence, and keep disposable probe/rollout evidence in session records. The stale-ID outcome contradicts the documented full-disable claim and must be reconciled.

## Exact history and migration conclusion

Reviewed affected amendment e414ed31806d2b91620d5e5fad8b5b5ee56e07ac -> 1a57ae9a038516fd4e435591ea3853de098fa8fb, and complete current runtime feature series ba8669b14536f72b559abc912bba8eac430111e4 -> 1a57ae9a038516fd4e435591ea3853de098fa8fb.

Worktree is clean; HEAD is the supplied head and its direct parent is ba8669b. The complete own series contains exactly one owning feature commit. Initial-registration ancestry is upstream 273a08c/ba8669b followed by that final feature. Amendment changes exactly the eight inventoried provider/Disable/docs/tests paths. provider-disable-amendment.patch matches the exact Git diff byte-for-byte, SHA256 7e878b6d7e8246e561c4a4c2e1d29851a9c39082d18741666bf12491d27f9f30.

No obsolete unmerged approaches, fixup series or repeated dependency/channel/generated update streams remain in this runtime history. Module declarations, source imports and vendorHash remain together in the one owning commit; the amendment adds only standard-library hashing and changes no external dependency/import closure, vendorHash, flake or Codex pin.

No database, lifecycle, roster or runtime-contract migrations. Private notification schema 1 and optional strict receipt boolean remain unchanged with their previously reviewed compatibility/provenance. The browser cleanup selector is an additive bounded origin-local record; there is no server format conversion or transitional schema. Existing ID deletion clients remain supported, and unsupported older servers can leave server cleanup pending while local cleanup proceeds. Per packet, no product state has been merged/released/deployed/externally consumed. Disposable native probes are verification fixtures, not a supported state predecessor.

Workspace/configuration still select e414ed3, as expected while this source review/publication is held. They need a final mechanical pin/history refresh after remediation and source publication; this review does not certify composition at 1a57ae9.

## Verification limits and next action

Retained reviewer0 identity/settings verified: GPT-6.1 Sol/xhigh/read_only, independent, no nested agents. Covered affected general/API, risk/provider, architecture and scope concerns using the mandatory workflow, without rerunning unchanged title/receipt/observer lanes.

Read inventory, exact patch, architect addendum, provider verification and exact-version source evidence; inspected source, tests/docs and complete history. Quick PASS evidence (Go 0.416s, 13 actual-module Node contracts, syntax/gofmt/diff) comes from the packet. I ran only the read-only stale-ID reproduction with declared Nix Node 24.19.0, not a long suite.

Prior e414ed3 full-package/CI and Firefox real-provider acceptance/zero-tab worker receipt remain evidence for that revision. Chromium post-amendment provider/worker delivery and physical/macOS OS display remain unproved. After finding reconciliation, proceed under the existing workflow to final-revision long/native checks, publication and composition refresh. No push, deployment, merge, reservation release or session lifecycle action was performed or authorized by this review.

Lead should save this report as provider-disable-review.md and record the finding disposition.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
