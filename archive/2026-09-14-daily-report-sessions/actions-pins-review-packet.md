# Final channel pins: review packet

Initiative 2026-09-14-daily-report-sessions; workspace
/home/aither/workspace/ai/vpsfree.cz. Tracking is work/2026-09-14-daily-report-sessions;
all worktrees are worktrees/2026-09-14-daily-report-sessions/PROJECT on the same
named feature branch. Read plan.md/state.md for acceptance and rollout.

## Exact committed configuration series

vpsfree-cz-configuration base 249bed1ee28e69a907edd09ea97a1144dbcdefeb
API pin 6e0021ac74b3bfcb69b09a23a7a0df7c3c869f47
final template pin/head 3f213d5ebf922ab5522690ab28b3fdfa9b3bed1d

Both commits were generated with confctl inputs channel set --commit, using
vpsadmin/vpsadmin and vpsfree-notification-templates/vpsfree-notification-templates.
To consolidate repeated input updates, the clean feature was first rebased to
its unchanged original master base with no replay, then the two final pins were
regenerated. The old published head remains 5036135728832d5c375705e3b69949c33460ff7e
until the explicit leased push after review. Generated messages are unchanged.
No manual lock edits, handwritten config changes, other input moves, merge,
deployment, migration, or session lifecycle actions.

## Pushed source heads and reviewed feature

vpsadmin base 5ac49802f892da6fd37a88c8349b9cc7ea826538,
head 014fbc78422f3660b295add7a50f35cc7acdf0c8;
vpsfree-notification-templates base f944ba03eba5d0d6b58b7eb856f251d1c96f2c11,
head 6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333.

Source implementation/contract packet: actions-review-packet.md.
All four functional sol/xhigh lanes completed with no Blocking/Important or
new Advisory findings; baseline report projection/catalog Advisories are
accepted in actions-review-reconciliation.md. Individual password-change and
failed-login rows include seconds, login/ID, source or mechanism/reason and
recorded client IP. Totals and older-payload guards remain; no new auth policy.
The API full feature also includes four additive report-query indexes.

Only vpsadminServices and vpsfreeNotificationTemplates change. The latter's
vpsadmin input continues to follow vpsadminServices. API1 consumes both, manages
the organization templates and schedules reports; API2 consumes the API source.
No public API/client/protocol/node behavior or coordinated upgrade is required.
The API pin also takes the two upstream scheduled dependency updates between
791ab3aa and 5ac49802, over which the feature was rebased without content changes.

## Evidence and risk

High risk for live-table index rollout and cross-repository/mixed-version pins;
review at xhigh. Required final generated-pin lanes: General and Risk. The
handwritten architecture and scope were reviewed in the functional phase.

Quick checks passed: exact JSON node diff has only the intended two inputs;
all other nodes/top-level lock data unchanged; expected source SHAs and follows
asserted; git diff --check and confctl commit hooks passed. Final actual
text/HTML database specs: 19 examples, zero failures. Template flake check and
remote Check run34849022483 passed; API RuboCop run34849117365 passed. Other API
CI is running/queued. Superseded old-head VM run34840185855 was cancelled.
Delivered-mail integration is running after completed functional review;
final config long builds will start only after these pin reviews.

Old generators/templates remain compatible via absent-hash and absent-events
guards; old templates ignore additive values. API hosts use autoSetup=false;
a later approved rollout must explicitly run vpsadmin-api-migrate-db.service
from the new package once, monitoring locks/I/O. Old code tolerates the added
indexes; rollback may leave them. No activation or production migration now.
Build both cz.vpsfree/vpsadmin/int.api* configurations after review.

Read /home/aither/.codex/skills/mandatory-change-review/SKILL.md and your lane
reference, plus repository AGENTS. Inspect the committed series and actual
consumer topology/pins directly. No code edits or nested agents. Record any
finding with severity and concrete evidence in the assigned tracking artifact.
