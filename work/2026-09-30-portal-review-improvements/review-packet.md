# Final committed-change review packet

## Review assignment

- Initiative: `2026-09-30-portal-review-improvements`
- Overall risk: **high**. The changes handle repository working-tree content,
  OAuth credentials and secret files, reverse-proxy trust boundaries, live
  session settings, cross-project Nix inputs, deployment and recovery.
- Reviewer: retained `reviewer0`, purpose `review`, read-only access,
  `gpt-6-sol`, xhigh effort. Use its saved settings without overrides.
- Recheck lanes: general, architecture and repetition, scope and
  proportionality, and risk and compatibility for the browser retry behavior
  and final pin graph. The earlier whole-branch review covered all four lanes;
  the immutable-result and deterministic Git fixture corrections were reviewed
  separately.
- Required workflow: read
  `~/.codex/skills/mandatory-change-review/SKILL.md` and all four selected lane
  references. Perform the review directly without subagents.

The earlier four-lane whole-branch review found one Important issue in cluster
build provenance and one documentation Advisory. Both were addressed in the
rewritten extension cluster commit, and an affected-lane recheck found no
Blocking or Important issue. A live Playwright run then found an implicit
failed-preview retry in the generic repository browser. That bounded product
fix is folded into the owning Load all commit; the subsequent generic commits
were replayed without changing their final behavior, and downstream amendments
refresh exact pins. Inspect the complete final histories and diffs again for
branch readiness, with attention to this retry behavior and the pin graph.
Return findings ordered by severity with file/line and commit references where
possible. Explicitly conclude whether obsolete branch history or transitional
migrations remain.

## Requested outcome and acceptance criteria

The user requested these connected changes:

1. Use exact `gpt-6.1-sol` for new workspace lead, implementer and reviewer
   defaults while retaining existing roster settings, GPT-6 Astra architects,
   GPT-6 Luna/low watchers and existing effort policy.
2. Keep repository diff editors/content loaded after scrolling and provide a
   bounded **Load all diffs** action so browser Find can search loaded content.
3. Replace GitHub-specific origin labeling with **Origin**, while retaining
   GitHub link enrichment as the only supported provider.
4. Capture immutable staged and unstaged/untracked repository reviews with the
   same review UI and bounded resource use.
5. Preselect model and reasoning effort when adding members from role policy,
   while preserving explicit overrides and incomplete-pair validation.
6. Apply live Codex model and effort as one draft pair so polling cannot revert
   the model before the effort is selected.
7. Add the reviewed `vpsadmin-webui` source to the vpsAdmin development cluster
   as an optional bridge-only React Web UI beside the existing PHP UI, then
   enable it at `newadmin.aitherdev.int.vpsfree.cz` in this workspace.

Acceptance requires correct behavior and failure handling, no secret exposure,
the existing PHP UI/API remaining usable, exact source/model pins, compatible
old manifests and callers, and documented deployment/recovery boundaries.
The first long Playwright run exposed the retry behavior; focused corrected
browser verification passed. Final-head full Playwright, package builds and
live bridge/OAuth checks follow this recheck.

## Affected repositories and final histories

### Generic `dev-workspace`

- Worktree: `worktrees/2026-09-30-portal-review-improvements/dev-workspace`
- Base: `7c133c562ac51076c1f45af46e180f8bfbabe836`
- Head: `41c648cd92cb324037778be165e45e17c46bbc75`
- Published feature ref: `origin/2026-09-30-portal-review-improvements`

Complete series, oldest first:

1. `f00a0e5d46f5dd0a4707ab23bbfc3eb4a9db755a` — derive added-member settings
   from role policy.
2. `4f500a50360c7507164de41787ed199a1d8c5183` — manage live model/effort as one
   draft pair.
3. `8c250986d560b13df7f09deeceaa7e19008aef9f` — retain loaded editors and add
   bounded Load all diffs.
4. `7ccb6ba350594b69f80675d056b7fa80c496dc67` — separate generic origin data
   from GitHub-only enrichment.
5. `41c648cd92cb324037778be165e45e17c46bbc75` — immutable staged and
   unstaged/untracked captures.

The five commits are independently reviewable product units. Corrections made
during implementation were folded into their owning commits. The post-review
packaged check exposed a timing-dependent clean-filter positive control. The
final snapshot commit now uses a deterministic `hash-object --path` control
and a test-local Git wrapper that rejects forbidden reader commands during both
captures. A subsequent Playwright run found that an IntersectionObserver read
could silently retry a failed preview before the user selected Retry. The
Load all commit now leaves failed records alone for automatic reads while
preserving explicit retry and priority file actions. The browser fixture
checks failure injection and the submodule notice selector; asset versions
advance together. No fixup commit, superseded protocol, schema version,
dual path or abandoned compatibility shim remains. Final diff: 30 files,
3,480 insertions and 362 deletions.

### vpsFree `dev-workspace` extension

- Worktree: `worktrees/2026-09-30-portal-review-improvements/vpsfree-dev-workspace`
- Base: `6a0a2eb873e7cb376092c74bdf82fc2c51c349da`
- Head: `67bfbbd653694e13e8d5aee53ef0f8e283694bf5`
- Published feature ref: `origin/2026-09-30-portal-review-improvements`

Complete series, oldest first:

1. `1d76d6032b40cd5fb035c26a6b9c94c4aa48e109` — optional React Web UI cluster
   service, credential lifecycle, OAuth seed, proxying, immutable build-source
   provenance, status and tests.
2. `67bfbbd653694e13e8d5aee53ef0f8e283694bf5` — exact generic runtime pin to
   the reviewed portal branch.

The cluster implementation and its downstream dependency pin remain separate
for review and revert. The generated nested cluster `flake.lock` was deliberately
omitted because that subflake previously floated unrelated vpsAdminOS/status
inputs; the root lock owns the exact selected API/WebUI/runtime resolution.
An automatically triggered check against the first published head found that
the selected NixOS module exposes `RequiresMountsFor` through `unitConfig`. The
one-line correction was folded into the owning unmerged cluster commit. The
reviewer's Important finding about post-build `webui-source.json` publication
was also folded into that commit: selected-result labels now carry revision,
dirty state and source kind together with machines, and old sidecars are
ignored. The last pin commit was amended only to select the corrected generic
test revision. Final diff: 13 files, 1,213 insertions and 40 deletions.

### Coordination workspace policy and site configuration

- Worktree: `worktrees/2026-09-30-portal-review-improvements/workspace`
- Base after required rebase: `034eb08ea56e75f8a582179b8c13bd9b3109d29e`
- Head: `99e387511cd9d6beac2b9cbb4a7c49306b394ab5`
- Published feature ref: `origin/2026-09-30-portal-review-improvements`

Complete series, oldest first:

1. `e00505e30c7e1a0e982534a3b8c3afed5152c24c` — exact GPT-6.1 Sol policy,
   catalog assertions and owning policy documentation.
2. `bcba17a00335874eaa8ffe664a279637a0ab01ee` — site domain and bridge cluster
   enablement, with a focused deployment-contract test.
3. `99e387511cd9d6beac2b9cbb4a7c49306b394ab5` — exact extension, generic,
   selected API and WebUI lock resolution.

The behavior, site enablement and generated dependency composition are separate
commits. The final lock resolves exact generic `41c648cd` and extension
`67bfbbd6` revisions. Final diff: 8 files, 89 insertions and 34 deletions.

## Migration and obsolete-history inventory

There are **no new database or persisted-format migrations** in these feature
branches. The React client uses the OAuth schema already present in selected
vpsAdmin API revision `5c76e3290481b297dcd0baa76d246133f0353d8f` and adds a
runtime idempotent seed. Its nine upstream migrations since the former pinned
API revision are `20260818115900`, `20260818120000`, `20260821120000`,
`20260821210000`, `20260823100000`, `20260909170000`, `20260914120000`,
`20260914180000` and `20260914190000`. They are already merged in vpsAdmin;
their production release, deployment and external-use status is unknown.
The selected new disposable cluster can initialize on this API. This
initiative does not claim that an older API generation can read its database
after those migrations run.

No obsolete branch iteration remains in the three final histories. The
unsupported Nix option and the post-build sidecar approach were folded out of
the final cluster commit. Early
uncommitted capture discovery based on Git porcelain/status was rejected after
it could invoke hostile clean filters; the final commit directly uses index
stage/debug metadata and no-follow filesystem stats. Early uncommitted OAuth
seed and credential cleanup issues were corrected before the single cluster
implementation commit. No externally consumed intermediate feature revision is
being preserved.

## Deliberate boundaries and rejected alternatives

- Support GitHub enrichment only. Generic **Origin** naming and provider
  isolation must not imply support for another forge.
- Use the exact requested `gpt-6.1-sol`; do not substitute a catalog model.
  The currently deployed portal account did not list it on 2026-09-30, so
  candidate deployment must recheck model availability and may remain blocked.
- Existing retained team members keep their saved model and effort. Only new
  presets/member defaults change.
- Snapshot captures are process-local and subject to quota/LRU eviction. They do not
  persist repository data and must never mutate Git state or execute filters.
- Native browser Find searches loaded DOM content. **Load all diffs** loads all
  bounded review files; the feature does not replace browser Find.
- Unstaged gitlinks are reported as bounded, frozen, unverified submodule
  metadata without a changed/clean/dirty claim. Staged and committed gitlink
  behavior is unchanged.
- The React cluster service is bridge-only. Enabling it in local mode fails
  before credentials/certificates are created because the browser and BFF do
  not have one reviewed provider origin there.
- The React frontend/BFF is separate from PHP. Disabling it leaves PHP/API
  behavior and its default OAuth client in place; credentials and the distinct
  nondefault React OAuth client are retained for recovery.
- Portal deployment uses the user profile and the supported forward-only
  workspace switch. Do not describe profile rollback as supported.
- No edits are needed in `codex-web`, `vpsadmin` or `vpsadmin-webui`; they were
  inspected as protocol/source dependencies at exact commits.

## Pins and cross-project ownership

- Generic portal owner: `aither64/dev-workspace`, head `41c648cd...`.
  Consumers in this change are the vpsFree extension and final workspace
  package.
- vpsFree cluster provider owner: `vpsfreecz/dev-workspace`, head `67bfbbd6...`.
  Consumer is the workspace package/site configuration.
- vpsAdmin API: exact `5c76e3290481b297dcd0baa76d246133f0353d8f`.
- vpsAdmin WebUI: exact reviewed
  `534caa83a5f97d2b40b4a126886649b14dc9e8d3`; its Nix inputs follow the
  selected API and vpsAdminOS nixpkgs inputs.
- Workspace policy/config consumer: head `99e387511cd9d6beac2b9cbb4a7c49306b394ab5`.

Review representative provider and consumer contracts together: repository
review APIs/manifest compatibility in the generic project, cluster provider
options/status/source metadata in the extension, and exact site/policy inputs
in the workspace.

## Documentation and quick verification

Lasting behavior is documented in generic `docs/workspace-portal.md`, extension
`README.md` and `dev-clusters/vpsadmin/README.md`, workspace `AGENTS.md` and
`docs/agent-teams.md`. Design, rollout constraints and verification remain in
`work/2026-09-30-portal-review-improvements/{design,state}.md`.
User-facing wording received the required writing pass before commit.

Quick checks completed before this review:

- Generic project: `GOFLAGS=-mod=mod go test` for the complete changed
  `internal/repository`, `internal/teamruntime`, `internal/web` and
  `cmd/workspace-portal` packages; repository and web packages also passed
  again after the final snapshot commit. Ruby member-creation tests passed
  (11 runs/73 assertions). Changed Node files pass `node --check`; browser
  contract fixtures and `git diff --check` pass.
- Snapshot fixtures cover immutable staged/unstaged/untracked data, names and
  file types, hostile filters, racy files, quotas/admission, expiry, ownership,
  gitlinks and cleanup.
- The corrected filter fixture passed 20 repeated focused runs with the racy
  index test. It proves filter liveness independently of Git stat timing,
  rejects unsafe Git invocations through a test-local PATH guard, and checks
  stage/debug reads on both captures. `gofmt -l` and diff checks passed.
- The first full Playwright run passed five browser subtests and exposed the
  implicit failed-preview retry in the repository review scenario. With the
  correction, the focused live repository scenario passes at final generic
  head `41c648cd`. Changed JavaScript syntax, repository browser contracts,
  asset-version references and diff checks pass. The final-head full six-case
  Playwright suite also passed; its output is at
  `/tmp/portal-review-playwright-41c648c.log`.
- Extension: `test/devcluster_commands_test.rb` passed 5 runs/68 assertions;
  `test/devcluster_status_test.rb` passed 1/16;
  `test/devcluster_webui_seed_test.rb` passed 4/26. Nix parsing, Bash syntax,
  Ruby syntax, `git diff --check`, root lock update, and
  `nix eval --raw .#checks.x86_64-linux.package.drvPath` passed.
- After the provenance correction, focused status fixtures passed 3/45 and
  command fixtures passed 6/94 in the lead environment with the repository's
  tracked runtime contract and default config. Bash and Nix parsing, Ruby
  syntax, documentation-link and whitespace checks passed. The new enabled
  packaged Nix smoke remains for post-review verification.
- Workspace: `ruby test/agent_instructions_test.rb` passed 7 runs/96 assertions;
  `ruby test/deployment_contract_test.rb` passed 4/19; direct generated-catalog
  evaluation and `git diff --check` passed. After final pins,
  `nix eval --raw .#packages.x86_64-linux.default.drvPath` passed.
- All three feature worktrees are clean and their exact heads are published.

Final-head generic Check run `36759668293` passed at `41c648cd`, and extension
Check run `36759784918` passed at `67bfbbd6`, including its packaged
`devcluster-check`. Generic `nix flake check`, workspace package build and
workspace `nix flake check` passed at the exact heads; the workspace candidate
is `/nix/store/j0d65mfyh3wi208iqzqk4cwnshyl473w-dev-workspace-0.2.0`.
The exact locked WebUI frontend and BFF also built at extension head. These
checks establish package and test results; they do not establish a booted
cluster or activated portal. Pending evidence is enabled cluster rendering
and live bridge TLS/OAuth/session/PHP coexistence, user-profile activation,
and the exact candidate account model catalog. The active account currently
does not list `gpt-6.1-sol`, so the accepted deployment gate is unmet.

## Review focus

In addition to normal lane checks, inspect these high-risk points:

- Snapshot selection cannot invoke clean/textconv/external diff/fsmonitor,
  escape the registered repository, follow symlinks, race into a different
  object, exceed per-capture/process reservations, leak active readers, or
  produce a mutable comparison after capture.
- Snapshot IDs and routes enforce session, worktree and repository ownership;
  HTML/JSON paths and unusual names stay inert.
- Polling, restore/cancel and failed writes cannot silently replace a dirty
  model/effort draft or submit a partial pair.
- Added-member defaults use the requested role policy and retain explicit
  override/validation behavior.
- Origin refactoring preserves old manifest/API data and all existing GitHub
  commit/comparison/workflow links while denying unsupported enrichments.
- Credential directories/files have safe permissions, atomic stable creation,
  cleanup on every failure and no secret path through Nix store, environment,
  argv, status or logs.
- OAuth seed collision checks cannot repurpose the PHP/default client and are
  idempotent; service ordering keeps it after DB/general seed and credentials.
- Public edge and private nginx/BFF listener/header/trust rules prevent spoofed
  forwarding data, external access to private listeners and TLS downgrade.
- Disabling/failing React leaves PHP/API available and does not publish stale
  React provenance. Recovery and mixed-version claims match actual behavior.
- A build that publishes `result-config` and then fails must stop before VM
  deployment, while status reports one complete selected result. The old
  `webui-source.json` sidecar has no read or write authority; missing, partial
  or invalid labels fail closed, and the consumer pins the corrected head.
- Commit splits, final histories and documentation contain no obsolete or
  speculative compatibility paths.
