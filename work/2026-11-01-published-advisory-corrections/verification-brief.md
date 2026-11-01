# Expanded post-review verification brief

Release recorded: full review + prescribed E fixes reconciled; affected API
baseline refresh-review.md has NO findings. Modern batch already PASS on1c847;
API/client/strictKB batch passed on c8ef/beeb. The final two-entry endpoint
inventory correction is committed and directly reconciled at4cf/4109. A subsequent
legacy attempt found a healthy API rejected by obsolete HTML-title matching.
The helper-only successor0111/fd9267 has completed independent affected review
with no findings; its strict KB and later scoped layout successor acceptance
passed. Final source is API49f5/KB5276 after independent layout review, all18real
legacy cases passed. No further unchanged checks are authorized by this record.
Runtime API evidence is retained for
proven identical effective inputs under review-reconciliation.md/api-acceptance.md;
do not repeat unchanged API/client/modern long suites. The conditions below are fulfilled.

Launch only after the NEW expanded committed-deliverable independent review is
complete and Blocking/Important findings are fixed or explicitly dispositioned.
The earlier paused review is incomplete and not this gate. Use reviewed final
heads, updating this brief if a relevant fix changes inputs. No production data,
credentials, deployment/default integration/session lifecycle operation.

## Inputs and utility policy

Own worktrees under /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-published-advisory-corrections/.

- vpsadmin49f5a29e5a7d85559d06d31496acb5c08895bcda
- security-advisories0b771120bb2a878c012512b685208124c2b4263b
- KB contracts5276b64b9cab0d29bc14968730eccf88c230059d, pins API head above
- modern vpsadmin-webui1c8478bceb3943645ec06ccde895ee4b0985873f over
  main63d484fc070dbee633d32624de545e834d483701, dev/published-advisory-corrections,
  draftPR122; exact current-base quick/capture evidence in implementer1.md.

Use fresh pinned-policy Luna/low operation utilities, explicit danger-full-access/
never, exact absolute guidance/commands and canonical working directory. One
utility at a time; no nested agents/discovery/retry/diagnosis/edits by watcher.
Skill: /home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/skills/dev-session-monitor/SKILL.md.
Watcher launches/owns tool handles and full logs, returns exit/CI status, exact
revision/command/time/path and failures/remaining processes. Parent diagnoses and
assigns source fixes to existing owner. No blind reruns. On unavailable delegation,
report once and use minimal parent monitoring instead of utility loops.

## Bounded batch 1: real API, client and contract

Purpose: silent/all-state corrections and lifecycle authorization/preconditions,
real transaction/savepoint rollback and writer/delete races, atomic node membership
projections, six-action draft-sync protection/recovery, exact-source KB impact.
Expected tens of minutes for full plus core: a prior HTTP-heavy core RSpec run
took11m33s. Use standard commands only. Stop at first actionable failed command
and return evidence; successful exact-input commands need no repetition unless
new input/finding justifies it. Do not use a generic quiet-output timeout.

From vpsadmin root (Nix API shell enters api/):

VPSADMIN_PLUGINS=all nix develop .#api -c bundle exec rspec spec/models/security_advisory_spec.rb spec/models/security_advisory_concurrency_spec.rb spec/api/resources/security_advisory_spec.rb spec/api/plugins/outage_reports/security_advisory_spec.rb

VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec spec/models/security_advisory_spec.rb spec/models/security_advisory_concurrency_spec.rb spec/api/resources/security_advisory_spec.rb

Run full/core sequentially with normal isolated automatic MariaDB. Preserve actual
REPEATABLE-READ/test snapshot settings, no DB-default changes or disposable-schema
guards. Named rollback tests must execute after the observed original CI failures.

From security-advisories root:

nix develop -c bundle exec rspec

From vpsfree-kb-contracts root, strict pinned source (no mutable source override):

nix develop -c bin/check

If strict KB fails, retain first evidence and assign bounded base/final comparison
to owner. Do not fix unrelated fingerprints/media/provenance/page content or use
--allow-missing as acceptance. No cluster/capture/wiki fetch/staging/publication.

## Bounded batch 2: legacy browser acceptance

From vpsadmin root:

./test-runner.sh test 'webui#security-advisories'

Covers real existing admin form workflow plus API, published/retracted edits,
explicit membership changes/partial omission, timestamp/null/CVE preservation,
stale guards/projections and confirmed silent retract/delete. VM/build duration
uncertain; preserve exact derivation/input/runner receipts and full logs.
Stop and report unexpected local Linux kernel builds; no kernel/config change is
authorized. Silence is not failure; return concrete escalation and keep unfinished
operations owned. Use only own test runner/guest, never another session cluster.

## Bounded batch 3: modern application and artifact checks

Use pinned Nix root and final committed modern head, existing project scripts.
Full suite/build and selected browser/package outputs follow final review:

npm test
npm run build

npm run e2e -- e2e/specs/app/security_advisories_admin.spec.ts e2e/specs/app/security_advisory_update_mutations.spec.ts --project=chromium

npm run e2e -- e2e/specs/admin/security_advisory_nodes_mobile_actions.spec.ts e2e/specs/admin/security_advisory_outages_mobile_actions.spec.ts --project=mobile-chrome

nix build .#frontend .#bff .#checks.x86_64-linux.provenance .#checks.x86_64-linux.source-contents .#checks.x86_64-linux.package-contents

Use existing wrapper/own free local port and pinned Nix Chromium on NixOS as
already reconciled for captures. No production credentials or live mutation
scripts. Include implemented cs/en desktop/mobile confirmation/error cases.
Mobile WebKit testMatch excludes these files; zero tests is not coverage.
The prior narrow synthetic captures establish appearance, not real API cascade,
mail or transaction behavior. Actual API evidence belongs to batch1/2.
No general UI/BFF/dependency migration or unrelated acceptance campaign.

## Exact CI evidence

Collect exact-head run/job conclusions, failed logs/artifacts BEFORE any rerun.
Respect complete full/core API topic coverage aggregate. Watcher can monitor
existing run IDs without replaying them. Cancel only superseded active runs on
our exact branches after follow-up pushes, never current-head/other-session runs.
CI success grants no default integration/deployment/lifecycle authority.

Vpsadmin0111: API41351014848,CI41351014860,i18n41351014847,
RuboCop41351014858,WebUI PHPUnit41351014871.
Client0b771120: RSpec41336065180,RuboCop41336065173 (completed success).
KBfd9267: Check41351185161,Managed page runtime41351185245.
Modern1c847 draftPR122: CI41339759463,Playwright smoke41339759427.
Superseded218e/21c5/b02c active runs were canceled and reconciled in the receipts.
Prior old-head API rollback and metadata
failures diagnosed/fixed, retained in package-a-expanded.md; do not call them
unrelated baseline or rely on a green rerun without final named regressions.
