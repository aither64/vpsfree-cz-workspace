---
lifecycle: complete
---

# API exception from newadmin

## Current status

Ready for user deployment. Both repositories were integrated by fast-forward
and their remote master branches equal the exact reviewed/tested feature heads:

- API: f9beb46e5206864bca9d37672e1419cf03661467.
- Configuration: 074b62fe4ca99bcb6e0b2cd186e43f039c666b36.

API Specs run 37151153953 succeeded at f9: all 27 jobs passed, including topic
coverage. Full/core limits are 60 minutes; coverage remains 10. Local persisted
regressions passed 72 examples after proving 3 original-source failures.
Independent reviews passed with no findings, including complete-history and
no-migration conclusions. Original authentication source/specs are unchanged.

Both final API1/API2 builds passed at configuration 074, generation
2026-10-03--22-46-01, selecting exact f9. Actual metadata and built switch scripts
were checked without activation. Only services revision/hash/timestamp changed;
all unrelated pins/follows remain intact. Full 18-commit API changelog retained;
mandatory hooks passed.

Integration CI was not awaited. User owns production deployment and acceptance.
Both feature refs, feature/integration worktrees and evidence are retained;
lifecycle remains active and session open. No production/dry activation or
session cleanup occurred. Next action: user's scoped API1/API2 rollout from
[handoff](rollout.md). See [verification](verification.md),
[review](review.md), [integration proof](integration-result.json).

## Phase checklist

- [x] Investigation/design: idle cleanup and refresh trace established.
- [x] API fix and persisted regressions: red 3/3, green 72/0.
- [x] Requested full/core Specs timeout:60 minutes, separate coherent commit.
- [x] Complete branch history/migrations and independent final reviews: no findings.
- [x] Final channel pin generated, validated and both feature refs published.
- [x] Verification:27/27 Specs jobs and both exact-tree API builds passed.
- [x] Both remote master branches fast-forwarded to exact final heads.
- [x] Operator handoff prepared; session/worktrees/refs retained.
- [ ] Production rollout and browser acceptance: user-owned.

## Evidence

Email dated 2026-10-03 16:47:13 +0200 reports `NoMethodError` on
`GET /v7.0/users/current`, with Origin `https://newadmin.vpsfree.cz`.
The API is `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`; the exception is at
`api/lib/vpsadmin/api/operations/user_session/resume_oauth2.rb:40`:
`oauth.single_sign_on.token.valid_to < user_session.token.valid_to`.
The raw email remains in the uploaded private input location outside Git.

### Root cause and trigger

- `api/models/single_sign_on.rb:26-31`: `close` destroys the token and sets
  `token_id` to null, retaining the SSO row and its authorization links. The
  nullable token reference is intentional in migration
  `20231216155818_add_single_sign_ons.rb`.
- `api/lib/vpsadmin/api/tasks/user_session.rb:20-31`: cleanup removes an
  expired access token while retaining an open OAuth session with a valid
  refresh token. Lines 46-50 close an expired SSO independently.
- `api/lib/vpsadmin/api/authentication/oauth2_config.rb:257-294`: refresh
  creates a fresh access token without requiring or restoring a live SSO token.
- `ResumeOAuth2:35-41` then checks the SSO row but dereferences its missing
  token. Reaching this block also establishes that the session is
  `renewable_auto`. Authentication fails before the current-user action runs.
- WebUI reference `aa2f60b89df65d2f987be48784ed42bab7010833` on local
  `origin/main`: `bff/server.js:155-179` refreshes on session bootstrap;
  `:257-273` supplies the access token through `/session.json`;
  `src/app/auth.tsx:124-130` invokes `fetchCurrentUser`, which requests
  `/users/current` in `src/lib/api/users.ts:19-24`.

An idle interval long enough for SSO expiration, followed by cleanup and BFF
refresh, is a complete source-supported path to this failure. Explicit SSO
revocation can create the same tokenless SSO state. The email cannot prove which
event occurred for this request. The inspected WebUI revision has not been
established as the exact deployed frontend/BFF revision.

User reports the error affects multiple users and suspects inactivity. That is
consistent with routine expiration cleanup being the practical trigger; no
unusual account state or explicit logout is needed for the source-supported
idle/cleanup/refresh sequence.

### Recommended correction and verification boundary

Handle a tokenless SSO as closed and skip its renewal; allow independently valid
OAuth authentication to proceed. Capture and check the SSO token before reading
its expiry. Do not recreate a revoked SSO token from an OAuth access request.
Any fix should cover live SSO renewal, closed SSO plus valid access token,
expired SSO cleanup followed by refresh, and close/renew concurrency.

The original investigation used source inspection and an independent architect
trace. Implementation now has persisted regression evidence and independent
review. Production database state and the precise incident cleanup chronology
remain uninspected; no production deployment has been performed.

## Team and repositories

- `architect0` (design, Astra/xhigh, workspace write): independent API trace and
  proposed fix/verification brief in `design.md`.
- Lead: coordination, assignments, records, evidence reconciliation and handoff.
- `implementer0` (Sol/xhigh, workspace write): API fix/regressions, then exact
  configuration channel pin after API review.
- `reviewer0` (Sol/xhigh, read only): mandatory independent review of complete
  API and configuration branches, including explicit no-migration conclusions.
- Canonical bare repositories: `repos/vpsadmin.git`, `repos/vpsadmin-webui.git`,
  `repos/haveapi.git`, `repos/vpsfree-cz-configuration.git`.
- API worktree: `worktrees/2026-10-03-newadmin-exception/vpsadmin`, branch
  `2026-10-03-newadmin-exception`, base
  `148ef0eaed0459c825f1ba94b8dad2b9f3311b2f`.
- Configuration worktree:
  `worktrees/2026-10-03-newadmin-exception/vpsfree-cz-configuration`, same branch,
  initial base `657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da`, final base
  `7e32833aca1cb65902b50f61eb76dd1022691591`, published final head
  `dd5e0b5d1d8a2487d608909676c828934966abdc`.
- Both worktrees are registered in the portal manifest. Initial helper commands
  returned nonzero after checkout: API requires reviewed Overcommit signatures;
  configuration requires local hook gems. No hook bypass. Environment setup is
  delegated to fresh Luna/low watcher `environment_setup_watcher`; implementer
  will finish hook installation/signing after declared dependencies are ready.
- Verified installed catalog digest matches the retained roster:
  `4676433c6831fbaca91da8ffde84891aff6ce065a17c74c2f367f1acf1d15b17`.
  Separate verification-watcher utility policy is Luna/low with one-operation
  lifetime and maximum concurrency one.

## Detailed phase history

The checkpoints below preserve earlier phase decisions; pending states there
are superseded by the current summary and [verification evidence](verification.md).

- Final build at `dd5e0b5d` passed, exit 0 in 78 seconds, both API targets
  generation `2026-10-03--21-30-00`. Lead inspected actual per-target generation
  metadata/output paths and confirmed source revision `af8a9767` and built
  switch scripts without activation. Configuration final head was published
  over SSH, matching remote tracking ref, clean worktree/index. See
  [final build](configuration-final-build-result.json) and
  [output evidence](configuration-final-outputs.json).

- Initial configuration build passed from `e96fbde0`, exit 0 in 120 seconds,
  both targets generation `2026-10-03--21-15-32`. See
  [initial build evidence](configuration-build-result.json). No activation.
- Publication fetch found already-merged monitoring commits `fae43505` and
  `7e32833a`, with no input/lock or API service-target changes. Pin commit
  cleanly rebased onto current master as `dd5e0b5d`; `git range-diff` reports
  equality and full feature diffs are byte-identical. Source/message unchanged,
  clean branch and diff check/declared target inventory pass. Final checkpoint
  is assigned to the same reviewer for general/risk, with earlier unaffected
  lanes retained. Refresh exact-final-tree builds afterward.
- Implementer independently validated the rebase: final lock and generated
  message are byte-identical too, all 64 nodes/follows and the full API changelog
  preserved, current master base followed by one clean flake-lock-only commit,
  no migrations/history residue. Member updated only own configuration report.
- Reviewer passed current final refs in general/risk lanes without findings,
  explicitly preserving previous all-four conclusions after inspecting both
  inherited monitor-only commits. Current whole history remains one coherent
  pin with no obsolete mechanisms and sound no-migration lineage. New-tree
  build is next; earlier build remains historical evidence.

- API feature head `af8a9767` was published over SSH after fetching upstream;
  upstream master remained at `148ef0ea`. Initial ambient-shell push was
  refused by Overcommit signature policy. Repeating in the declared root shell
  after reviewing/signing the same configuration passed, with no hook bypass.
- Configuration generator succeeded in the declared shell and produced
  `e96fbde0c622e3807593e3e59daae0f668045540`, only the expected services lock
  revision/hash/timestamp. Mandatory hooks passed; generated changelog/message
  retained. Lead JSON comparison confirms all other nodes, root/version and
  follows unchanged. `confctl ls` confirms exactly API1/API2.
- Final configuration packet is [configuration review packet](configuration-review-packet.md).
  Retained `reviewer0` passed all four lanes at unchanged saved Sol/xhigh
  settings. Implementer validation passed: all 64 lock nodes retained, only
  services revision/hash/timestamp changed, every follows/unrelated input
  unchanged, exact published API ref and full 17-commit changelog matched.
  Complete configuration series is one generated commit with no obsolete
  history or migrations. See [configuration report](configuration-result.md).
- Exact configuration-pinned WebUI source now resolves after canonical SSH
  fetch and confirms the expected refresh/bootstrap path. See
  [pinned WebUI trace](pinned-webui-trace.md). This is source evidence and does
  not identify the incident's running frontend revision.

- Environment preparation passed: API and root `nix develop` initialization,
  plus configuration `nix develop`, all exited 0 at their recorded bases.
  See [environment result](environment-result.json). No unexpected kernel build
  or remaining setup operation. Implementer is finishing hook signatures and
  regression-first edits; source guard remains unchanged until the red run.
- Red regressions passed their intended failure check: original source produced
  exactly 3 examples / 3 `nil.valid_to` failures, including persisted
  cleanup/refresh/access authentication. See [red result](red-regression-result.json).
  Implementer released to apply guard and finalize quick checks.
- Implementer sandbox denies the Nix daemon socket despite source paths being
  writable. Lead generated cached declared environments with successful
  `nix print-dev-env --offline` for API and root in temporary files outside Git;
  member will source these and evaluate their shell hooks. No access escalation,
  application-edit takeover or hook bypass. API shells enter `api/` automatically;
  verification commands must omit an extra `cd api`.
- Cached declared environments resolved the member tooling restriction. Source
  the generated script once; it already evaluates `shellHook`. Member signed
  reviewed Overcommit configuration/custom hooks, installed hooks and verified
  active hook listing. Touched-file RuboCop passed: 3 files, zero offenses.
- Guard is coded with the existing expiry policy preserved. Fresh Luna/low
  watcher `green_regression_watcher` owns the frozen full resume, cleanup and
  OAuth2 configuration suite run. API commit waits for its result.
- Green verification passed: 72 examples, zero failures, exit 0 across the
  assigned resume, cleanup and OAuth2 configuration suites (77 seconds).
  See [green result](green-regression-result.json). Implementer released to
  create the single coherent API commit with active mandatory hooks.
- Member's commit attempt was correctly refused by the socket-backed API i18n
  hook (`EPERM` creating the isolated DB port socket). Lead executed the unchanged
  member-prepared Git commit as a coordination step in the socket-capable cached
  root environment. All mandatory precommit and commit-msg hooks passed; only
  TextWidth's >72-character advisory remains, with <=80 lines satisfying rules.
  Source edits remained wholly implementer-owned; no hook bypass.
- Complete API branch inventory and diff are in
  [API review packet](api-review-packet.md): one coherent commit, clean worktree,
  no superseded approaches, no migrations. `reviewer0` is reviewing all four
  mandatory lanes at saved Sol/xhigh/read-only settings; no fallback or override.
- Implementer owns configuration preparation and resulting generated-diff
  validation. Socket-backed Git/confctl execution is lead coordination; cached
  configuration environment is ready. Pinning remains blocked on API review,
  not on an application-file access failure.
- Independent API review completed with no findings in all four lanes. Reviewer
  explicitly concluded clean complete history/no obsolete mechanisms and sound
  no-migration lineage, including all inherited dependency updates. See
  [review conclusions](review.md). API head is approved for scoped publication
  and exact pin preparation, without merge or deployment approval.

## Next action and limitations

The user can deploy the built final configuration to API1/API2 using the
prepared [rollout](rollout.md). Agent-owned implementation, verification, review,
publication and integration are complete. Production rollout, browser acceptance
and rollback execution are user-owned. Retain the actual prior deployment
generation; old workers may still raise until replaced. No session cleanup is
authorized. Exact incident cleanup chronology and concurrent scheduling remain
unverified; persisted idle/cleanup/refresh behavior is covered by tests.
Hook/tooling restrictions
were resolved through cached declared Nix environments; no bypass. No production
data or operations.

The current API base differs from the old channel pin only by 16 already-merged
dependency-update commits, touching package Gemfiles/gemsets and legacy PHP
dependencies. The independent reviewer inspected that complete inherited delta.
Upstream was fetched before publication and API master remained at the recorded
base.

## Documentation

[Investigation plan](plan.md) and [root cause and correction brief](design.md).
The architect's complete report has been read and reconciled with the lead's
independent source trace. It also identifies why changing the guard to
`sso.usable?` would alter the existing expiry policy; the minimal proposal checks
token presence and preserves existing renewal behavior. No project documentation
change was needed beyond the lasting source invariant comment, as independently
reviewed. Exact rollout/recovery belongs in [manual handoff](rollout.md).
Initial plan/state committed
on shared coordination master as `fbd5f824` after fetching origin; no declared
hook framework or active executable hook was found in that repository.

Stable session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-newadmin-exception/>

## Observer evidence placement

An earlier observer wrote 15 API Specs logs/artifact lists under an untracked
work/ directory in the API worktree. Lead verified the exact same-session capture
identity and relocated the directory intact to api-ci-completion-original-capture
in this tracking directory. No content/source/ref changed and no evidence was
deleted. API tracked tree/index and entire Git status are now clean; final review
record's untracked-log observation remains accurate for its earlier checkpoint.

## Retained integration targets

Dedicated detached target worktrees are prepared with declared environments and
active hooks: worktrees/2026-10-03-newadmin-exception/vpsadmin-integration and
vpsfree-cz-configuration-integration. Their current baselines are148ef0ea and
7e32833a. They will fast-forward to the tested heads only after Specs succeeds.
Retain these worktrees and both feature refs afterward; no session cleanup or
worktree removal is authorized.

## Integration evidence

After exact f9 API Specs success and final builds/reviews, lead fast-forwarded
the prepared API target worktree from148ef0ea to f9 and pushed HEAD:master.
Fresh fetch confirmed remote master equals the exact tested feature head and
feature ancestry. API feature ref and integration target are retained and clean.
Configuration integration follows at the already reviewed/built074 pin.

Both integration targets subsequently fast-forwarded and pushed tested heads
to master. Fresh fetches verified exact remote/default/feature equality and
ancestry. Clean integration worktrees retained; see integration-result.json.
