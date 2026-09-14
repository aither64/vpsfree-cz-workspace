# Documentation review packet

Review the downstream documentation phase for initiative 2026-09-13-auth-email.
Workspace: /home/aither/workspace/ai/vpsfree.cz.
Tracking and local review material: work/2026-09-13-auth-email/.
Read plan.md, state.md and kb-impact.md. Do not edit code or launch subagents.

Repository: worktrees/2026-09-13-auth-email/vpsfree-kb-contracts
Branch: 2026-09-13-auth-email
Base: 919577d0c770e47b623c591f8bf0cce4e8d30666
Head: 656d0524f76f2078fb16a8a789a55405f6aba7e5
One cohesive documentation commit: semantic profile control/path, bilingual
account-page bindings, and exact reviewed API pin. No capture/runtime logic
changed. Existing screenshot crops and their contents are unaffected.

The owning vpsAdmin implementation is separately reviewed in four lanes and
pushed at f7a4b68d8695f0958a2badd4e1897915d98cdcae (API commit
24d7897a2a56c061831de7d6d3ecac12c02c3ef3). Production templates are reviewed
and pushed at 06f03bad4294b6f28ca9478e907f43967ebeb7d0. Inspect those sources
as needed to verify documentation claims; their implementation is not being
re-reviewed here.

Outcome: document the opt-in email step on unknown-device password logins when
no effective TOTP/passkey MFA applies and successful device history exists.
Known usable devices are unaffected; retained revoked/expired known records
count as history. Default off and enrollment gate off. Primary email only,
30-minute fixed lifetime, replacement invalidates old code without extension,
three total sends at least one minute apart, five wrong codes, shared budgets.
New password token issuance requires the step; Basic refuses without mail;
existing sessions/tokens/refresh/valid SSO continue. Current-password reauth for
self-service settings. Go get-token helper's explicit incompatibility and the
HaveAPI CLI replacement are documented in the API rollout guide and state.

Local bilingual public-page candidates, not production writes:
- kb-candidates/cs/navody/vps/uzivatele.txt
- kb-candidates/en/manuals/vps/users.txt
- kb-annotation-plan.yml, kb-candidates/review.md
- kb-release-cs.yml and kb-release-en.yml are checksummed schema-5 manifests
  with informative localized revision summaries from release-changes.yml.
These are initiative review artifacts awaiting a consolidated tracking
checkpoint; the complete private production source inventory stays local and
ignored. Only these public pages are changed. Review their finished prose for
factual and bilingual consistency as well as contract coverage.

The canonical workflow was followed: all 114 Czech and 77 English accessible
pages fetched; all-page candidates built with kb-contract-build; two pages
changed, no media/deletions. Focused changed-page count/reciprocal-language/
30-minute checks passed. Four baseline annotation mismatches on unrelated
pages remain, listed in kb-impact.md. Do not require unrelated page rewrites or
blind fingerprint acceptance. Staging preparation may proceed for the checked
account pages, but production is untouched and requires explicit approval.

Quick verification: nix develop -c bin/check passed at this head's contents:
46 controls, 37 paths, 35 capture concepts, 3 semantic selectors; 96 annotation
bindings/9 exceptions; four managed pages/eight variants/12 test bindings/21
samples; all repository contract tests and 120-PNG inventory validation passed.
No bitmap was changed. The API flake pin update initially pulled older nested
OS/Nixpkgs revisions; those were restored via Nix's nested input override. The
final lock diff changes only the intended vpsAdmin node and preserves the
existing vpsAdminOS 6bdf458f classified-retry support.

Selected lane: GENERAL only, as this phase is documentation-only plus an exact
pin to already reviewed implementation. Overall feature risk is high
(authentication); no new authority or deployment design is introduced here.
Use gpt-5.6-sol/xhigh as required by mandatory-change-review. Review committed
history and local AGENTS; report concrete Blocking/Important/Advisory findings
or clearly state none, with residual gaps. Write review-kb.md in tracking.
