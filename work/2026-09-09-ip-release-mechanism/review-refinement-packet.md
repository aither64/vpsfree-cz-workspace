# IP release selection and member-view refinement review

Use /home/aither/.codex/skills/mandatory-change-review/SKILL.md and your assigned
lane reference. Perform the review directly with fresh context; no subagents,
edits, external mutations, credentials, screenshots or lifecycle operations.

## Scope and acceptance

Review the committed refinement delta from vpsAdmin a75bb80d5, in the context
of its eight-commit series. First six prerequisite commits remain identical;
their prior complete reviews are recorded in review-split-results.md and
review-bulk-remove-results.md. Do not invent broader mechanisms for them.
Inspect the final API and WebUI commits and changed consumers. General review
must also verify that the eight-commit split remains intact and messages describe
the final behavior.

The accepted plan is the opening section of plan.md. User decisions:

- No custom campaign label/text. Translate campaign ID for admins; members see
  only their own release date, addresses/status/reasons/actions and Notice history.
- Keep the exact Notice history label. Split sidebar navigation/management;
  show relevant initial/reminder/release actions, handling partial notifications.
- Blank narrow checkbox header, full-width reason textarea with placeholder.
- Multi-select networks, locations, families; optional numeric user; access
  public/private/both. Defaults public IPv4. Select only user-owned unused IPs.
- No campaign size cap. Expected scale hundreds; 500-address pages. Explicit
  all-matches selection spans the preview snapshot and preserves exclusions and
  settings across pages. Do not add async selection, delayed submission,
  automatic release, mail delivery checks, or arbitrary campaign limits.
- Only explicit admin release, at any time regardless of date or notices.
  Editable policy after mail. Keep changed-owner safety, accounting and DNS
  cleanup-first behavior. Members get explicit response whitelists, no campaign
  metadata or release-attempt diagnostics. Raw safe assignment ID avoids
  expanding a historical IP association to a replacement owner.
- User authorized disposable cluster reset, but prefer preserving review data.
  No merge, screenshots, session archival/deletion/stop or messages to others.

## Repositories and commit ownership

All are under /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism,
on branch 2026-09-09-ip-release-mechanism.

Exact final heads are appended below after commit preparation. vpsAdmin base
564cc80ea5d4420d0f2441c996fb0df2f82bb39c; previous head a75bb80d5d4ce76e95c766199bc35e798fab956e.
API commit owns model/endpoint/schema changes, specs, DNS fixture input and docs.
WebUI commit owns selection helper, forms, CSS/catalogs and browser/unit tests.
The schemas and tests support their respective behavior; no generic pagination,
Lockable or TransactionChain infrastructure changes in this delta.

Notification overlay unchanged 715c063396fa49277852b98d36347c8bec5160d3,
base 6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333. It consumes the same request and
reminder event contract with public-IPv4-only scarcity context, text and HTML.
KB base 8789cc1f5aeb3b19cbff13f741d6dd9960f14567; companion commit only pins
vpsAdmin and validates existing documentation controls. Preserve OS 6bdf458.
HaveAPI 0.29.8 supplies standard pagination max 1000; campaign address actions
default to 500 and no longer override the standard range. No HaveAPI changes.

## Verification and documented constraints

- PHP full suite: 95 tests/396 assertions pass. Selection covers 1101 entries,
  off-page preservation, all/none, owner isolation, forged IDs.
- API/model/concurrency suite: 71 examples, one overly strict response-key
  assertion failed on standard HaveAPI _meta. Fixed expectation explicitly
  checks allowed metadata keys. Other 70 passed.
- Focused final API tests: 4/0 seed 64991, including explicit limit=500 for
  candidate, campaign, admin/member address lists (501 entries over two pages),
  owner response whitelist and seven-day defaults; 2m50s plus loading.
- Filter/private mail focused test passed; API model tests cover private quota,
  export/host exclusions, partial mailer-disabled recipients and actions.
- Migration up/unique active claim/down: 2/0 seed 5735. Schema regenerated from
  preceding core schema; only removed label column differs from prior schema.
- Ruby lint (10 files), PHP formatting, API locale health, WebUI locale health,
  CI selector 16 tests/55 assertions and git diff checks pass. Commit hooks run.
- Long browser integration has not started for this refinement. Baseline full
  browser scenario and all API Specs/KB managed CI passed. Previous selected CI
  run was still in progress, no recorded failed current result.

Owning documentation: vpsadmin/docs/ip-release.md, indexed by docs/README.md;
existing docs/ip-locking.md explains unchanged prerequisite contracts. Read the
rollout/accounting audit and rollback sections. Schema and API are unmerged;
reset disposable earlier-feature schemas rather than adding compatibility guards.
Deploy matching API and WebUI, refresh discovery. Existing released vpsAdmin does
not have these endpoints. No node protocol or coordinated OS update needed.

Latest reported live error was confirmed in Nginx logs: campaign Index succeeds
at limit25, but old a75 campaign Address Index rejects explicit limit500. New
source removes the cap; final deployment and a real browser check are pending.

Risk: high (member isolation, API contract and persisted schema), all four lanes,
gpt-6-astra/xhigh. Report Blocking/Important/Advisory findings with evidence;
when none, say so and identify remaining test gaps or accepted residual risks.

## Committed heads for this review

- vpsAdmin 9840cdf08b9dbdb825bac0da04aa74281d3c4e2a; API 3fb0ab7f5,
  WebUI 9840cdf08. Exactly eight commits, first six unchanged. Published.
- KB e098f68845397a510dd4ed6638f0d50e8f52428c; full bin/check passes,
  including managed page/control and existing image inventory validation.
- Overlay remains 715c063396fa49277852b98d36347c8bec5160d3.

All intended code and pin changes are committed. Tracking documents remain in
working tree per the workspace's consolidated-checkpoint rule.
