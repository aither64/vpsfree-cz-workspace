Important — A retired snooze operation can mutate the replacement offer's state.

In runtime commit `94e3114c6fef510ca21d29efd1741faa848a4147`,
[app.js:2569](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/dev-workspace/portal/internal/web/static/app.js:2569)
reuses one `wizardState` for the logical question while resetting its
offer-specific snooze flags when the token changes. The asynchronous rejection
handler at
[app.js:2642](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/dev-workspace/portal/internal/web/static/app.js:2642)
still closes over that same mutable object and updates it without checking the
offer token. Start snoozing offer A, receive replacement offer B with the same
thread/turn/item/questions, and then let A's request fail. The old rejection
sets B's `snoozeFailed` flag. Further input on B returns at
[app.js:2635](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/dev-workspace/portal/internal/web/static/app.js:2635)
without sending a snooze, so B's automatic resolution timer can expire while
the user is editing answers.

This is a lifetime mismatch: drafts and wizard position should survive offer
replacement, whereas snooze operations and their outcomes belong to one exact
offer. Keep these states separate, or guard asynchronous completion against the
captured token before changing offer state or notices. Also make the explicit
Refresh question action reset or retry a failed snooze for a restored current
offer: currently `snoozeFailed` clears only when the token changes, so refreshing
the same token cannot perform the retry promised by the notice.

Verified with a short Node probe under `nix shell nixpkgs#nodejs`, extracting
the actual snooze function and token-reset statement using `git show 94e3114`.
After the A -> B -> delayed A rejection sequence, invoking B's function produced
`sentTokens: ["offer-A"]` and B retained `snoozeFailed: true`. The probe wrote no
project files. Add coverage for that sequence and for a same-token refresh after
a transient snooze failure.

Important — The shared browser consumer bypasses the new offer contract.

Provider commit `1a0ed38060db44bc3849d7adec481519d78dfa90` adds the optional
`PromptResponder`, but
[handler.go:797](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/codex-web/conversation/handler.go:797)
chooses the safe interface only when the browser supplies a nonempty token.
Omitting it still selects the legacy ID-only methods. The provider's own
`mountConversation` consumer still omits tokens for answers, snoozes and
decisions at
[conversation.js:717](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/codex-web/conversation/assets/conversation.js:717),
[conversation.js:725](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/codex-web/conversation/assets/conversation.js:725)
and
[conversation.js:731](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/codex-web/conversation/assets/conversation.js:731).
This is the complete browser UI mounted by the actual reference application at
[main.go:34](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/codex-web/cmd/codex-web-example/main.go:34).

If its displayed request A is replaced by request B reusing the protocol ID,
an A answer or approval reaches the legacy method and claims B: the check at
[client.go:1414](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/codex-web/codex/client.go:1414)
deliberately skips token comparison for legacy calls. Matching question IDs and
option labels can allow an old answer through even when question text changed;
an approval can similarly apply to B's matching current command item. A portal
document loaded before an upgrade can reach the same fallback. Reload handling
for a token-bearing request against an unsupported responder does not cover
either case.

Require the offer contract at the HTTP boundary and update `mountConversation`
to pass each entry's token for all three actions. Preserve the legacy Go
methods as the direct-call compatibility surface, without letting browser
omission select that surface. Validate the complete shared UI, plus tokenless
old-document requests and ID reuse with changed questions/approval items. The
new tests exercise the optional interface directly but do not cover this real
consumer path.

No Blocking or Advisory findings.

Reviewed the packet, plan/state, local repository rules, Architecture lane,
commit messages and the four exact ranges:

- codex-web: `6335da93acdcc82cc26200d2fbc7f479655aa7c3` -> `1a0ed38060db44bc3849d7adec481519d78dfa90`.
- dev-workspace: `83136101866eb42d9e079f47191308c0549ac9e7` -> `94e3114c6fef510ca21d29efd1741faa848a4147`.
- vpsfree-dev-workspace: `a08a40eeff124bdbcc1ce6b6b06aed1839a9d9fc` -> `7dc4ea2ac169064de0034983377f9f19c23a281d`.
- workspace: `8f31bab` -> `997f4aa2ce7ae58b2be13348036a2d168c71a2b1`.

The provider/runtime/organization/site dependency direction remains clear.
The runtime's concrete `workspacecodex.Client` embeds the provider client and
preserves the optional responder on the HTTP target. Nix and Go provider pins
agree, and both downstream flakes select the reviewed companion heads. Exact
line ranges have one Git owner; Unified and Split share one projection builder
and the same editor/highlighter lifecycle. The archival move and review-model
change remain focused commits. No additional current-scope abstraction or
repetition change is required by this review.

Long browser, packaged/profile and live App Server tests were intentionally not
run. The race and shared browser contract cases above should join those planned
checks. Navigation restoration, out-of-order history responses, split visual
alignment and bounded lazy loading still require the scheduled browser
acceptance; passing helper tests alone does not establish those behaviors.
