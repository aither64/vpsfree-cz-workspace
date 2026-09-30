# Final committed-change review packet

## Assignment

- Initiative: `2026-09-30-portal-review-improvements`
- Requested review: final whole-branch readiness review of every committed
  change and complete base-to-head history in all four changed repositories.
- Overall risk: **high**. The changes touch OAuth credentials and sessions,
  reverse-proxy trust, repository working-tree content, host/container startup,
  cross-project Nix pins, deployment/recovery and shared internal DNS.
- Reviewer: retained independent `reviewer0`, purpose `review`, read-only
  access, saved `gpt-6-sol` model and xhigh effort. Do not override its saved
  settings.
- Lanes: general; architecture and repetition; scope and proportionality; risk
  and compatibility.
- Required workflow: read
  `~/.codex/skills/mandatory-change-review/SKILL.md` and all four selected lane
  references. Review directly without subagents.

This review supersedes every earlier incremental or affected-lane review. Start
from each base below, inspect the complete series and final diff, and explicitly
conclude whether obsolete unmerged history or transitional migrations remain.
Return findings ordered by severity with file/line and commit references where
possible. If there are no findings, say so and list residual risks or remaining
verification gaps.

## Requested outcome and acceptance criteria

The user requested a connected portal and development-cluster update:

1. Use exact `gpt-6.1-sol` for new workspace lead, implementer and reviewer
   defaults while retaining existing roster settings, Astra/xhigh architects,
   Luna/low verification watchers and the established effort policy.
2. Keep loaded repository diffs in the DOM after scrolling and provide bounded
   **Load all diffs** behavior for native browser Find.
3. Label the repository remote **Origin**, with GitHub as the only supported
   provider for commit, comparison and workflow enrichment.
4. Capture immutable staged and unstaged/untracked repository reviews with the
   existing review UI and bounded memory/reader use.
5. Preselect added-member model/effort from role policy while preserving
   explicit overrides and incomplete-pair validation.
6. Apply live Codex model and reasoning effort as one draft pair so polling
   cannot revert the first selection while the second is being changed.
7. Add the exact reviewed `vpsadmin-webui` source to the vpsAdmin bridge cluster
   beside the legacy PHP UI, with persistent credentials/session state and an
   automatically started `newadmin` container.
8. Make the approved React hostname resolvable through the existing internal
   aitherdev frontend by preparing one private-zone CNAME and a monotonic SOA
   serial. Publishing the four shared DNS copies is outside the current
   aitherdev-only deployment authorization.

Acceptance requires no credential/token exposure, exact model/source pins,
compatible old manifests and disabled cluster configurations, continued PHP/API
availability, bounded snapshot behavior, correct boot ordering, an idempotent
OAuth seed, a clean final history and documented forward recovery. Final long
builds and the corrected services update follow this review.

## Exact repositories, histories and final diffs

All four feature refs are published and match the clean local heads listed
below. The complete file inventory is in [final-diff-inventory.md](final-diff-inventory.md).
These heads are candidates for deployment. Default-branch integration is still
unapproved; the workspace will need a current-master compatibility/rebase gate
before any fast-forward integration, while retaining the actual deployed refs.

### Generic `dev-workspace`

- Worktree: `worktrees/2026-09-30-portal-review-improvements/dev-workspace`
- Base: `7c133c562ac51076c1f45af46e180f8bfbabe836`
- Head: `50af66d9cfc1be07dcc4cb084de4887dd97a343c`

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
6. `50af66d9cfc1be07dcc4cb084de4887dd97a343c` — label the repository URL
   `Origin` while retaining provider-specific GitHub links.

Final diff: 30 files, 3,486 insertions and 362 deletions. Each commit owns one
product unit. Corrections to clean-filter fixtures and failed-preview retry
behavior were folded into their owning unmerged commits. No obsolete reader,
snapshot protocol, provider shim or fixup commit remains.

### vpsFree `dev-workspace` extension

- Worktree:
  `worktrees/2026-09-30-portal-review-improvements/vpsfree-dev-workspace`
- Base: `6a0a2eb873e7cb376092c74bdf82fc2c51c349da`
- Head: `8e04f2626a3abd492768f15ae8d843c8e527f2cd`

Complete series, oldest first:

1. `1d76d6032b40cd5fb035c26a6b9c94c4aa48e109` — optional React WebUI cluster
   service, credential lifecycle, OAuth seed, edge/private proxying, immutable
   source provenance and tests.
2. `67bfbbd653694e13e8d5aee53ef0f8e283694bf5` — select the reviewed generic
   portal runtime.
3. `e0f98557d688d8561be97d3dc6b1964a0304e383` — select the final generic
   Origin-label refinement.
4. `8e04f2626a3abd492768f15ae8d843c8e527f2cd` — start the optional React
   container on boot and assert enabled ordering and disabled absence.

Final diff: 13 files, 1,236 insertions and 49 deletions. Cluster behavior and
dependency selection remain separate for review/revert. The generated nested
cluster lock stays absent so unrelated vpsAdminOS/status inputs retain their
existing resolution contract; the root lock owns exact API/WebUI/runtime pins.

The live cluster exposed that the first implementation left
`container@newadmin.service` linked but not wanted by `machines.target`. The
final tree sets `containers.newadmin.autoStart = true` and asserts enabled
autostart, seed ordering and disabled absence. This focused post-deployment fix
is separate: the deployed `1d76d60`/`67bfbbd` chain must remain available as
actual consumption provenance. A conflicting consolidation produced `11161424`
with an identical final tree; its local and remote refs were restored to
`8e04f262` using checked updates. No selected package used the consolidated
chain. Earlier unsupported Nix option and mutable provenance-sidecar approaches
were removed before the first deployment. No unused boot compatibility path
remains.

### Coordination workspace policy and site configuration

- Worktree: `worktrees/2026-09-30-portal-review-improvements/workspace`
- Review base: `034eb08ea56e75f8a582179b8c13bd9b3109d29e`
- Head: `45cce0a87d3f0c8d2b404ce7188d8fa0d9098154`

Complete series, oldest first:

1. `e00505e30c7e1a0e982534a3b8c3afed5152c24c` — exact GPT-6.1 Sol policy,
   assertions and policy documentation.
2. `bcba17a00335874eaa8ffe664a279637a0ab01ee` — enable the bridge-only React
   site/domain.
3. `99e387511cd9d6beac2b9cbb4a7c49306b394ab5` — select the extension, generic
   portal, API and WebUI graph.
4. `0e00eab555f9a41136f13cad0f82662f5c2f717b` — select `llm-agents`
   `af40d966` and its exact `bun2nix`/`nixpkgs` closure for Codex 0.159.2.
5. `45cce0a87d3f0c8d2b404ce7188d8fa0d9098154` — select final generic
   `50af66d9` and extension `8e04f262` heads while preserving the Codex closure.

Final diff: 8 files, 99 insertions and 44 deletions. Policy, site enablement,
initial composition, Codex runtime and final pin refresh are independently
reviewable. The final lock retains exact generic `50af66d9`, extension
`8e04f262` and `llm-agents` `af40d966`; the final pin commit contains no
unrelated node change.

### `vpsfree-cz-configuration`

- Worktree:
  `worktrees/2026-09-30-portal-review-improvements/vpsfree-cz-configuration`
- Base: `ee99382c8c448a15347052a6964030f838cb0381`
- Head: `d24b251531a9a482b8f1b5dd81540da85981189f`

Complete series:

1. `d24b251531a9a482b8f1b5dd81540da85981189f` — add
   `newadmin.aitherdev.int` as one CNAME to the existing development frontend
   and advance the private-zone serial from `2026092800` to `2026093000`.

Final diff: one file, two insertions and one deletion. No public DNS, input,
system-host or deployment-target code changes. The commit deliberately prepares
the shared-zone candidate without publishing it.

### Read-only exact dependencies

- `codex-web`: `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`
- `vpsadmin`: `5c76e3290481b297dcd0baa76d246133f0353d8f`
- `vpsadmin-webui`: `534caa83a5f97d2b40b4a126886649b14dc9e8d3`

Their session worktrees are clean and have no initiative diff. The WebUI
worktree exists to exercise the documented local-source override during the
final cluster services update.

## Migration and obsolete-history inventory

There are **no new database migrations or persisted-format migrations** in the
four changed branches. The React client uses the OAuth schema already present
in selected vpsAdmin revision `5c76e329`. Its nine upstream API migrations
since the former selected revision are `20260818115900`, `20260818120000`,
`20260821120000`, `20260821210000`, `20260823100000`, `20260909170000`,
`20260914120000`, `20260914180000` and `20260914190000`. They are already
merged in vpsAdmin; production release, deployment and external-use status is
unknown. This initiative initializes a disposable development database at the
selected schema and does not claim rollback to an older API after those
migrations run.

The runtime OAuth seed is idempotent and is not a schema migration. Repeated
live execution completed successfully. The DNS serial change is required
protocol state; after publication, correction/removal must use a newer serial
instead of rolling the zone file back to a lower serial.

No obsolete unapplied implementation remains. Unsupported `requiresMountsFor`
use, mutable provenance sidecar, early Git porcelain/status snapshot selection
and implicit failed-preview retry were removed before deployment. The separate
Origin-label and boot-fix commits remain because they correct the externally
consumed composition. The final workspace consumer amendment replaces only an
unselected pin commit, preserving deployed parent `0e00eab5`.

## Commit split and deliberate boundaries

- Behavior, site configuration, generated dependency selection and DNS remain
  separate commits because they have different owners, verification and revert
  paths.
- GitHub is the only enrichment provider. Generic Origin naming does not add
  another forge.
- Existing team members retain saved settings; only new defaults change.
- Snapshot data is process-local, immutable, quota bounded and evictable. It
  does not persist repository content or invoke filters/textconv/external diff.
- Native browser Find searches loaded DOM content; Load all does not implement
  a separate search system.
- Unstaged gitlinks expose frozen, bounded, unverified metadata without claiming
  clean/dirty state.
- React remains bridge-only and separate from PHP. Disabled configurations add
  no new container/unit. Recovery can disable React while retaining the
  compatible API/schema, credentials and BFF state.
- The workspace profile transition is forward-only through the guarded helper.
- Shared internal DNS publication is not authorized by the user's aitherdev
  deployment direction. The exact pending consumers are
  `cz.vpsfree/containers/prg/int.ns1`,
  `cz.vpsfree/containers/brq/int.ns1`,
  `cz.vpsfree/containers/prg/int.mon1` and
  `cz.vpsfree/containers/prg/int.mon2`.
- No default-branch integration is authorized.

## Cross-project ownership and compatibility

- `aither64/dev-workspace` owns portal APIs, manifests and browser behavior;
  consumers are the vpsFree extension and final workspace package.
- `vpsfreecz/dev-workspace` owns the cluster provider CLI, Nix interface,
  credential/provenance behavior and status contract; the workspace package is
  its consumer.
- `vpsfreecz/vpsadmin-webui` owns the frontend/BFF/module contract; this change
  consumes exact reviewed source without editing it.
- `vpsfreecz/vpsfree-cz-configuration` owns the internal zone. Four independent
  authoritative consumers render that zone with their own FQDN. Cluster guest
  dnsmasq already has the hostname but does not publish host/VPN resolution.

Portal interfaces are additive and old manifests remain valid. Staged/unstaged
comparison IDs are ephemeral and old runtimes ignore them. The enabled cluster
path requires the selected compatible API/WebUI pair; the disabled path retains
old PHP/API behavior. Autostart changes only enabled services-VM boot wiring.
No coordinated vpsAdminOS node update is required. The one-record DNS change is
backward compatible, with normal one-hour positive/negative caching after
authorized publication.

## Documentation

Lasting behavior is documented in:

- generic `docs/workspace-portal.md`;
- extension `README.md` and `dev-clusters/vpsadmin/README.md`;
- workspace `AGENTS.md` and `docs/agent-teams.md`.

Design and verification rationale is in `work/2026-09-30-portal-review-improvements/design.md`.
Current status is in `state.md`; executed deployment evidence is separate in
`rollout.md`. The Origin label uses the established provider terminology and
needs no extra guide paragraph. No KB navigation workflow or screenshot text
changed. User-visible portal wording received the required writing pass before
commit.

## Quick verification before review

- Generic final head: focused Origin/template test passes; complete changed Go
  packages, Ruby role-default tests, Node syntax/browser contracts, snapshot
  fixtures and the final six-case Playwright suite passed at the unchanged
  owning commits. The prior final generic flake check also passed before the
  label-only commit.
- Extension final tree: enabled and disabled full cluster-config evaluations
  passed with the autostart/unit assertions. Nix parsing, exact generic pin,
  `git diff --check` and equality with the validated startup-fix final
  tree pass. Earlier focused runner/status/seed suites and packaged check passed
  at the owning implementation before the autostart correction.
- Workspace final head: `agent_instructions_test.rb` passes 7 runs/96
  assertions; `deployment_contract_test.rb` passes 4/19. `git diff --check`,
  flake metadata and exact generic/extension/llm-agents pin assertions pass.
- Configuration final head: four rendered private zones for
  `ns1.int.prg.vpsfree.cz`, `ns1.int.brq.vpsfree.cz`,
  `mon1.int.prg.vpsfree.cz` and `mon2.int.prg.vpsfree.cz` pass
  `named-checkzone vpsfree.cz`. The diff has one record, serial `2026093000`,
  no duplicate, clean whitespace and no other file.
- Every changed worktree is clean and each remote feature ref equals its local
  head.

The final-head generic/extension/workspace long package checks and four DNS
consumer builds intentionally wait for this mandatory review.

## Existing live evidence and remaining deployment gates

The previous `41c648c`/`67bfbbd`/`0e00eab5` composition is active. It proves:

- Codex 0.159.2 and exact `gpt-6.1-sol` availability;
- one atomic live model/effort write and retained readback;
- immutable staged and unstaged/untracked endpoint captures;
- bridge cluster boot, exact pinned WebUI provenance and PHP coexistence;
- strict-CA TLS, expected certificate names, React static/config/health,
  loopback-only nginx/BFF, nginx validation and API CORS;
- real OAuth login/callback, one-use state rejection, authenticated API access,
  provider token refresh after bounded disposable-session expiry, stable
  session identity across BFF restart, two seed reruns, logout and revocation.

The live start also exposed the missing newadmin autostart edge, which the final
branch corrects. A manual diagnostic start is not proof of the final boot
behavior. After review and long checks, the supported services update must
prove `machines.target` enablement, active container state, retained session and
clean local WebUI-source provenance. The guarded user-profile update must expose
the final Origin label. Ordinary hostname resolution remains pending shared-DNS
publication approval; current service checks use explicit resolution to the
known bridge IP.

## Review focus

In addition to normal lane checks, inspect:

- snapshot selection, ownership, quota/admission, symlink/race/filter avoidance,
  reader cleanup and immutable comparison behavior;
- dirty model/effort draft preservation across polling, failed writes,
  restore/cancel and authorization/idle-gate enforcement;
- role defaults, explicit override validation and retained roster settings;
- old manifest/API compatibility and GitHub-only enrichment boundaries;
- credential permissions/atomicity, no secret path through Nix/store/status/
  logs, seed collision/idempotence and callback/session protections;
- public/private proxy trust, loopback listeners, TLS authority and disabled
  React isolation from PHP/API;
- selected-result provenance fail-closed behavior and exact consumer pins;
- newadmin `autoStart`, `machines.target` membership and seed Requires/After in
  enabled configurations, plus complete absence when disabled;
- DNS owner/type/target, monotonic serial, four actual consumers, caching and
  forward-only correction after publication;
- commit splits and the explicit conclusion that no obsolete history or
  migrations remain.
