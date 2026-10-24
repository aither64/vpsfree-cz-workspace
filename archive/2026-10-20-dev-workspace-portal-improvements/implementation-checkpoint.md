---
lifecycle: active
---

# Portal improvements

## Current phase

Source implementation complete; final workspace runtime pin queued on ownership.
A and C are committed, published and locally checked. B implementation, focused
checks and combined pins remain in progress. A Playwright interaction fixture is
prepared for post-review execution against actual served assets. Independent review, deployment and merge have
not occurred.

## Phase checklist

- [x] Verify session identity, scope and team access.
- [x] Architect design and implementation boundaries.
- [x] Portal and team catalog packages, technical docs and quick checks.
- [ ] Final workspace runtime pin and committed exact-range inventory (in progress).
- [ ] Commit inventory and mandatory independent final review.
- [ ] Long verification and published feature branches.
- [ ] Deployment if requested; integration only with explicit approval.

## Backlog

| Owner | Expected result and acceptance | Dependencies / checks |
| --- | --- | --- |
| architect0 | Completed design.md with portal requests, catalog extension, add-member fix and accepted interfaces | Read current sources and docs; no application edits |
| implementer0 | Portal reliability, custom conversation paths, files/artifact UI, team labels and add-member race | Accepted design.md; targeted checks and logical commits |
| implementer1 | codex-web history, durable sender and conversation presentation primitives | Accepted design.md; targeted checks and logical commits |
| implementer1 (next independent package) | Workspace team default and 3–6 implementer variants | Accepted design; config/docs/checks |
| reviewer0 | Final correctness, security, history and migration conclusions | Completed committed deliverable and passing quick checks |
| lead | Tracking, acceptance, wording, resource coordination and handoff | Assess member reports; keep selected runtime usable |

## Repositories

Registered worktrees under `worktrees/2026-10-20-dev-workspace-portal-improvements/`:

- dev-workspace, base `2c29b8019f35f86563ef9725aba7073533eafe67`, final B
  `86db71d595defd1d44878b5c0f99297749263787`; clean/published SSH branch,
  seven logical commits after fixup consolidation, no migrations and one shared
  pin stream. B claim explicitly released; final independent review pending.
- codex-web, base `738b064a564d4f0050c676a742996cbe7680519c`; A committed and
  published `f977598e0227cf997c2faad7d2153272bc0d5651` then
  `441ebeea0eb3befa91006e2e3de9c73eab1ca32c`. Lead verified clean worktree,
  complete two-commit series and exact SSH remote feature head. No migrations,
  superseded approaches or repeated pin streams. Independent review remains.
- workspace, initial base `44285bbb`, C final reviewed-candidate base `df73a12b`,
  published source head `21f5c9f096850ec3571e46b597d8a57004d2d4e1`;
  final runtime package pin awaits B publication.

Initial tracking commit: `900b71f6`. Tracking repository claim
`744fec75-2d33-4155-9587-bd8d4248d465` verified released after that commit.

## Evidence and risks

- Post-review browser command is prepared, not run; preserved as
  [postreview-browser-command.sh](postreview-browser-command.sh). It asserts exact
  clean B head86db71d, uses pinned Playwright1.59.1/Node24.19.0/Go1.26.6 and
  Chromium1217, absent fixture provider catalog, and an overlay for four generated
  review assets from the repository's exact Nix output. Module/executable paths
  and EmbedFiles verified read-only; no source edit/build/browser launch occurred.
  Reviewed-head changes require refreshing the command assertion. Any store roots
  needed at execution are operation-scoped and not yet created.

- Final workspace pin claim `c9de29dc-931d-4a7e-84f9-5781ce2b3f25` is waiting,
  verified by implementer and lead. C owner has exact remote B proof and lock
  baseline; no pin mutations until authoritative grant. Session notification
  resumes the same assignment. Independent review waits for complete final pin.

- B committed/published seven logical changes: final codex-web pin, team labels,
  authorized source actions, artifact browser, early index, retained Add-member
  selection, conversation presentation/recovery and combined browser fixture.
  Complete 33-file diff (+1077/-118) and full series captured for final review.
- B actual-pin quick checks passed: Go web/teamruntime/agentteams targeted source,
  Markdown, artifact, index, Add, response loss, browser client and journal/
  registration cases (6.098s/0.261s/0.026s); further browser-client/ack race/mixed
  index cases (0.403s). JS syntax and exact Go/Nix pin contract pass. Initial list
  measured 2.040618ms with optional activity blocked. Count6 bounded64KiB journal
  and direct-registration zero-native-child/no-role-argv fixtures pass.
- Runtime Go module `v0.0.0-20261020202523-441ebeea0eb3`, Nix narHash
  `sha256-qMUd2iPGB92SwpVLfJ4/Ivwk+ptCCjwQM1k+0/lo9n0=`, vendor hash validated.
  Codex and sibling locks unchanged. Final workspace source pin assigned C owner.
- Browser fixture is written/syntax checked, not executed. It uses real served
  assets and controlled API cases; response-loss Go fixture retains a disposable
  fake native client and does not prove live App Server restart recovery. Exact
  production POST502 root cause remains unknown. No visual/deployed claim made.

- B focused Go source/download, team projection and initial index checks pass; delayed
  Add-member contract passes exact settings, duplicate prevention and error
  retention. Fresh policy watcher derived Go vendor hash
  `sha256-UNZdTl4+G5tq9qROX5GOioy9THx15nI+SBcxrGpfXk0=` for the final A pin.
- Accepted bounded index contract: keep integer runningClusters and add
  runningClustersKnown. Explicit false means unknown and hides/reset new UI
  labels; absent flag uses legacy behavior. Baseline UI hides integer0 fallback,
  avoiding null/undefined labels. Preserve real failure notices, same-identity
  measured cache and no control/notification freshness grants. B owns mixed
  reader/identity regression; architect recorded concrete baseline evidence.

- C committed instruction-size correction separately from the team family:
  `d7430e559f1d6a85e73d0e3600681affefd56907`,
  `21f5c9f096850ec3571e46b597d8a57004d2d4e1`, after clean rebase onto local
  workspace master `df73a12b`. Published exact remote feature head verified by
  implementer; worktree clean and workspace claim explicitly released.
  Catalog evaluation/full policy jq, 9 instruction tests (166 assertions), Ruby
  syntax and Nix formatting pass. Final AGENTS16,313 bytes (baseline16,756),
  preserving rules/table/precedence and original16,384-byte size assertion.
  Combined generated metadata and largest count6 journal checks still pending.

- A quick checks passed with pinned Go/gcc and Node: conversation presentation,
  paging, attachment, handler/message/queue/origin tests; durable same-ID send,
  receipt/acknowledgement and unknown-outcome cases; 26 browser/paging/refresh/sync
  checks and JS syntax. No long tests launched. Claim `34eecb1b-2683-47bb-a48f-3cd1552ee102`
  explicitly released revision3. B assigned the exact final A pin in Go/Nix.
- C uses held workspace claim `5fe098ea-de49-4d28-a76e-f1aed27dd648`.
  Instruction checks found existing AGENTS discovery-size overflow (draft 16,819
  bytes vs 16,384 bound). Lead authorized bounded wording-only compression with
  exact replacement prose; preserve every rule/link and keep size assertion.
  C owner applies/validates it; no shared-root instructions or live policy edits.

- B coded independent source/artifact/index slices. Initial focused source and
  browser checks passed; expanded raw-download tests exposed a route restriction
  and fixture policy typo, under correction by B. New shared presentation wiring
  awaits final actual codex-web pin.
- Add-member race diagnosed: success reloads page; model options/defaults are
  rebuilt and no duplicate-submit guard exists. B is retaining form/options,
  refreshing roster in place and validating/capturing the displayed selection.
- Lead inspected C catalog descriptions, docs/default/count/capacity wording;
  current draft cleared for commit after technical quick checks.

- A coded accepted helper APIs and post-attachment presentation hook; focused
  Node browser/paging contracts and JavaScript syntax checks passed in pinned
  Nix tools. Go ordering checks ongoing; not independently reviewed. Failure
  fixtures preserve original attempt ID and suppress unknown notices after
  transcript acknowledgement. Lead inspected current UI wording and shared API documentation before commit.
  B icon labels and source/artifact/add-member guide wording also received the
  lead-owned user-facing-writing pass; technical checks remain outstanding.

- Added bounded B fix: Add member form retains selected role/model/effort after
  success and captures those exact values for submission. Avoid unnecessary
  refetch/default-low race; verify rapid sequential adds with delayed responses
  in disposable fixtures. No live roster edits are part of implementation.

- User extended scope: Full team with two implementers becomes default; add
  variants with three through six implementers. Architect completed capacity/contract
  analysis; independent workspace package assigned to implementer1. B owns tiny
  runtime label projection. Existing roster stays. User confirmed current models
  and efforts for the larger variants.
- B's bounded read-only 502 diagnosis: router had no proxy errors in last 24h;
  nginx had 38 premature-close errors, all GETs, with 17 within one second of
  portal stops. No failed-send timestamp exists, so POST 502 cause is unproven.
  Preserve inline durable recovery; no blind retry or live service change.

- Repository ownership granted and independently verified held: codex-web claim
  `34eecb1b-2683-47bb-a48f-3cd1552ee102`, dev-workspace claim
  `848c84aa-8543-4cf1-a754-763f50b7e496`. Lead independently verified both
  authoritative states as held, revision 2, at 20:18:57 UTC. Implementers are
  resuming their exact assigned packages and own release after safe execution.
- Accepted design refinement: additive `Target.PresentTranscript` executes after
  attachment decoration; existing `TransformTranscript` timing stays intact.
  A owns the shared hook/ordering tests and B uses final displayText for Markdown.

- `dev-session current` returned this exact slug; both environment markers match
  the trusted workspace/session binding.
- Full-team retained roster: architect0 (design, workspace_write), implementer0
  and implementer1 (implementation, workspace_write), reviewer0 (review,
  read_only); all ready. Saved models/efforts retained.
- Submission 502 root cause is unconfirmed. Avoid automatic retries until
  idempotency and durable acceptance behavior are established.
- Shared workspace contains extensive unrelated changes; preserve them and stage
  only this initiative's tracking files under the tracking lock and claim.

## Documentation and next action

[Architect design](design.md) covers the portal requests and both added team
requirements, source boundaries, helper
contracts, compatibility and verification. Both implementation packages are
assigned with saved settings retained. B starts index/files/artifacts while A
implements shared presentation helpers; B then integrates the helpers in its
custom conversation UI. Final codex-web and workspace pins are a dependent task.
Team catalog extension is accepted and assigned: delegated remains the two-
implementer preset and becomes both defaults; delegated_3..6 share role policy,
N+2 specialist slots and derived catalog capacity8. Direct-thread registration
stays capacity0. User confirmed retained models/efforts. Next action: complete
source packages, inspect wording and quick-check evidence, then assemble final
pins and independent review.

Architect findings: the older-history banner is independent of fetch timeouts;
absolute positioning causes overlap. Shared handler emits 503, whereas router
and nginx can emit 502. Exact production error correlation is still unproven.
Index status enrichment has a concrete six-second overall context; initial
HTML membership already renders independently. B owns bounded read-only diagnosis
and response-loss regression, with no blind retry or live restart. Lead applies
final wording before implementation commits. Project docs will own lasting
behavior; session artifacts will retain verification and review evidence.
User added compact right-side X dismissal for temporary message bubbles; included
in the design request. No deployment or lifecycle action is authorized by
completing this work.
