# Upstream compatibility refresh — final review packet

All intended adaptations are committed, quick checks pass and the feature
worktree/index are clean. Exact final head:
`543d7ac796fdd06f730e5d2de9a47d4a8d74e7f4`; tree
`5cc40fea941d9742b97aa29cc7ce8a061952a770`. Lead acceptance inventory and
post-consolidation receipt are complete. No long refreshed checks launched.

## Outcome and scope

The four requested portal fixes remain: consistent persistent-setting switches,
New output based on visible rendered content, immutable multiple Send/Steer and
Queue next capture with this tab's ordered dispatch, and quiet routine queue
reads using the shared refresh policy. No merge or deployment is authorized.

Repository: `dev-workspace`, worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/dev-workspace`.
Session: `2026-10-24-workspace-session-ui`; plan/state/design in this directory.
New upstream base: `10bb047513c82d1310e8fcaa797e8772f948dd8a`.
Original base/head: `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734` ..
`064e311e6dc933bc9a0f5d7cd20eaf20eeccbbf9`.

The original reports/ranges remain in review.md, review-followup.md and their
linked artifacts. This is a substantive overlapping baseline adaptation, not
certified equivalence. Review the refreshed final range and all affected
interactions; original unchanged lanes retain their evidence.

## Accepted decisions to assess

- New upstream codex-web pin `872c7ad3962f9fa9b17358244e27f3e3fac59fc5`
  belongs to the new base. Keep its coherent Go/Nix inputs. No provider change
  is authored by this feature.
- Exact typed /message503 message_not_sent/notSent=true proves nonadmission:
  unsent allows same-ID immutable retry, including recovered unknown attempts.
  Persist uncertainty before retry. Positive acceptance/observation wins.
- Fresh tab-owned first-dispatch untyped validation failures retain the finite
  status/text allowlist and failed/new-ID recovery. Unknown/restored/generic
  transport/Queue errors are not proof. Preserve R1–R4 direct repairs.
- Ordinary revised submissions wait behind an unknown buffered head. Explicit
  Send another copy is message-only, reconciles exact original first, confirms
  only if still unknown, retains original/link, substitutes copy at head or
  joins tail for a legacy receipt. Queue unknown retains exact-ID recovery;
  no queue-copy capability. Legacy unknown receipts do not globally hold work.
- Receipt/link/order partial writes preserve reachable identities and pause;
  reload never automatically dispatches or mints another copy. Retain linked
  accepted/observed proof through ACK. A deliberately retired failed target is
  dismissed+failed+absent-order; in-order failed recovery still applies.
- Preserve upstream operation-generation stale-feedback suppression and initial
  Send readiness without restoring the global in-flight capture blocker.
- Local FIFO describes dispatch in this tab, not model consumption or combined
  execution ordering across clients. Older browsers cannot safely be assumed to
  manage new pending dispatch states; prefer compatible forward recovery.

Authoritative rationale/boundary: design.md, “Upstream refresh brief”, linked
proof follow-up and exact post-review verification appendix. Owning explanation:
docs/workspace-portal.md, discoverable from README. Lead directly applied the
required user-facing writing pass after implementer3's technical draft.

## Review policy and provenance

High risk: browser persistence, uncertain delivery and mixed-version recovery.
Retained independent reviewer0, gpt-6.1-sol/xhigh, read_only. No override,
replacement, nested reviewer or fallback. General, architecture/repetition,
scope/proportionality and risk/compatibility lanes all apply; read their skill
references. Review directly and return concrete findings by message.

No database/server/native schema migration. Browser dispatch metadata remains
schema1; legacy receipt encoding extensions preserve existing identities and
links. Server ledger schema3 is unchanged by this feature. No migration was
merged, released, deployed or externally consumed. No feature revision has been
deployed. New baseline admission contracts are upstream-owned. Remote clients
are untrusted; local operator is trusted per repository instructions.

Quick acceptance on the held final adaptation: composer, submission-notice,
paging and aggregate browser-unit contracts against new pinned assets pass;
app/contract/delivery-browser syntax passes. Focused Go wrappers and asset-version
assertions pass (package1.822s). The same suite passes after consolidation.
Focused Go wrappers/asset assertions also pass at final head (package1.700s). Exact log:
implementer1-refresh-evidence/final-quick.log.

Long refreshed checks are deliberately pending final review: verify-refresh.sh
contains exact locked Chromium+Firefox, package and existing admission/native
commands. Existing 37-case real-handler prerequisite passed on the new pin;
refresh-validation-unit.log/.exit, source SHA256
fd20d158b2a31946e1985923eafa137804359cf78ca8716b05ba8d26d6c31b4c.
This proves host handler wiring, not live native admission.

## Final inventory and quick checks

Lead independently inspected complete five-commit series/messages and final
18-path diff inventory (1887 insertions/323 deletions), exact clean final head
and diff whitespace. The implementation is split by the four fixes plus guide:

1. `1cbb47cd67ce0dfaeb35b1f913a299e2f9b47534` settings switches.
2. `b93dac114e9529fa6379df27bbad9a004f4e8714` visible unread plus one final v61
   app cache identity and matching template assertion.
3. `c366a5993537d1cd8736bc9a87a141a493730f05` browser dispatcher, recovery,
   focused tests and independent Go handler proof. These implement one delivery
   contract and its persistence boundaries.
4. `ba79dab3535d15c7e540e8d9f848ec4da5053bfd` quiet healthy queue reads/test.
5. `543d7ac796fdd06f730e5d2de9a47d4a8d74e7f4` final portal guide.

Artifacts: [complete final diff](refresh-final.diff),
[complete final messages](refresh-final-history.txt),
[old/new series range-diff](implementer1-refresh-evidence/old-to-final.range-diff),
[mechanical/adapted range-diff](implementer1-refresh-evidence/mechanical-to-final.range-diff),
[exact adaptation](implementer1-refresh-evidence/final-adaptation.patch),
[provenance](implementer1-refresh-evidence/final-provenance.json).
Original ranges/review reports are retained. Accepted adaptation equals exactly
mechanical852c37d1..final; tree equals pre-autosquash tested tree.

Lead inventory: no obsolete approaches/fixups/transitional migrations, no
repeated dependency/channel/generated update streams. New-base pins are
upstream baseline, not extra feature pin commits; no flake/go pin files change
in final feature diff. Cache URLs advance once. Browser schema1 is separate
from existing receipts; no database/native/server migrations. No feature
revision deployed/released. Require your explicit independent whole-branch
history, migration and update-stream conclusions, even if unchanged lanes reuse
original content review.

Fresh implementer SSH fetch before final commit found origin/master still at
newbase10bb0475. Cached remote feature remains old064e311e. No publication,
integration, deployment or lifecycle action is authorized by this review.
