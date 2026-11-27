# Codex monitor boundary: final source review

## Scope and range

Investigation `2026-11-24-monitor-session-ownership`: [plan](plan.md),
[design](design.md), [state](state.md). Review `dev-workspace` at
`worktrees/2026-11-24-monitor-session-ownership/dev-workspace`, absolute from
workspace root. Complete base-to-head range:

- Base `e61d3b7e59f07f89df50d23e23d7800d4b13cabf` (`origin/master` at creation).
- Head and only commit `df3a66d4ea507dacd953c5a9813088666589d65d`,
  `monitor: distinguish Codex pre-dispatch refusals`.
- Reproduce the full diff with `git diff <base>..<head>`; clean at receipt check.
  No migrations, dependency updates, generated files, published intermediate
  approach or repeated update streams. Adapter contract, regression and docs
  belong to the same boundary change.

## Acceptance and risk

High: authenticated native thread, retained authorities and exactly-once
launch and delivery boundaries. Lanes: general, architecture and repetition,
scope and proportionality, risk and compatibility. Reviewer: retained
`reviewer0`, GPT-6.2 Sol/xhigh, independent, saved read-only role. Local host
operator is trusted; model-facing fields must not establish authority.

The same trusted lead must reach real monitor handling without shell selectors;
member/stale/ambiguous roots and foreign operation IDs must not gain authority.
Keep the complete inventory uniqueness check and exact retained status/resolve
and utility recovery. Separate inventory, request shape and ownership denials
from uncertainty after dispatch without disclosing inner errors. Confirm
`local|ci` is the existing semantic contract and the adapter does not rewrite
requests. Rejecting a known foreign ID earlier cannot replace service-side
revalidation. Compare fresh native and historical native CI start replay, as
well as direct CI status/launch semantics and retry. Check whether added
complexity is needed for the user request.

No new Pi lead monitor, daemon replacement mechanism, lineage/policy migration,
package selection, or change to the affected session. Current reader accepts a
valid mixed archive fixture; older binary can still fail until normal authorized
reconciliation. The historical caller metadata was not recovered. No blame on
shell vars or compaction based on the replay alone.

## Documentation and consumers

- `docs/dev-sessions.md#monitor-long-verification` and installed
  `skills/dev-session-monitor/SKILL.md`: lead how-to, canonical source sample,
  fallback vs unchanged-ID recovery; compare to MCP schema and validator.
- `docs/workspace-portal.md#runtime-monitor-operations`: adapter reference,
  selected CLI and daemon-start helper distinction; linked to operations
  procedure `docs/team-reporting-upgrade.md`. README links the owning guides.
- The selected `dev-workspace` runtime owns both MCP helper and CLI; native
  Codex supplies outer MCP metadata, and the host profile selects the CLI.
  No change to codex-web/native protocol or site pins and no activation claim.

## Checks and next gate

Implementation owner reports scoped Go monitor and operation checks, historical
native CI replay and tagged compile passed; no tagged execution before review.
The disposable full JSON-RPC envelope exercises valid mixed schema, exact
binding, stale/member/foreign cases, old vs current diagnostics, sources,
retained direct observer recovery, and lost reply with stable runtime-ci
registration. Tagged `TestNativeMonitorOperation` exercises actual pinned
native launch and lead receipt/history with synthetic provider and commands;
selected `passed`, `busy` and `lost-reply` cases to run after independent review
against exact reviewed managed build. Simulated continuation is not actual
native compaction. No production session or existing check is used.

Return severities and exact file/line references, tested scope/gaps, a placement
and preservation conclusion for docs, and explicit whole-branch obsolete
history, no repeated streams and migration-lineage conclusions.

## Aitherdev follow-up: refreshed source and paired-pin final review

Use [the full three-repository Git receipt](rollout-review-range.diff) for exact
commit messages and diffs. These all have one commit; each pin is in its owning
repository and has no interim lock edits, generated-stream duplicates or
migrations. All feature refs published with exact remote proof. Targets are
`master`, with complete explicit user confirmation requested but not yet recorded.

| Repository | Reviewed final base | Final feature head |
| --- | --- | --- |
| dev-workspace | `d15735fa9695aaed3cb45c073e01b8ef4e6904c8` | `46a547dce36e5f341b737e378fb721f8ac770f8e` |
| workspace | `c6534049f84fea7a017e9ad8828a96236ba8c748` | `83c20c7c700bc5f6db910cb79ffe0dbc62d9d31d` |
| vpsfree-cz-configuration | `1c81a4d76857e9ccbd638a6a0f29e50d39f6fc41` | `d4e80199ceca98ea63375dffc6f6a056beb13dbc` |

Runtime `range-diff` shows equality to the previously reviewed/remediated patch;
matching stable patch IDs `9163a458501adbb7def4f9280c4b7a0961d31772`. Rebased
focused Go, tagged fixture-unit checks and tag compile passed. Upstream Codex-web
and required CI wiring changed, so earlier exact-package native evidence is
not reused for the rebased package. [Rebased CI](https://github.com/aither64/dev-workspace/actions/runs/45494845460)
is running. Exact workspace metadata, lock comparison/parse and config
confctl mapping, Nix metadata and normal hooks passed. Across configuration
machines only aitherdev's devWorkspace input changed. The paired deployment
contract check passed, and both pins resolve the same runtime SHA and NAR hash
`sha256-93I+jcXM2iZ7DgJziChw35wItrmQxOypBIkyN6SCqTA=`. No deployment, claims,
long local check or runtime activation performed on the refreshed range.

Review the actual runtime equivalence, matching pin scope, config hooks and
public risk/compatibility consequences in the four original lanes. No new
product docs needed for these pin-only consumers; the configuration skill and
runtime operation docs retain the ordinary rollout contract. The separately
approved operation must be system-before-profile and prove the actual running
MCP helper, not just the package selection. Current policy-4/live-2 keeps the
older startup helper in an equivalent switch; no supported targeted reload
found. This is a rollout blocker, not a warrant to claim or activate aitherdev,
force restart, or suspend all workspaces. Pi parity remains out of scope.
Report exact reviewed ranges, severities, documentation/operational limits,
whole-branch obsolete history, repeated streams and migration lineage.

## D2: compiled-helper cutover compatibility

The user has confirmed deployment, activation, the three named `master`
merges, and release. This pass covers committed runtime only, the exact
`d15735fa9695aaed3cb45c073e01b8ef4e6904c8..689572abd0ad66c6d0877ea4c8a4adbdd888c638`
series in [epoch-review-range.diff](epoch-review-range.diff). It contains the
previously reviewed monitor commit `46a547dc` unchanged, followed by one
compatibility commit. Earlier consumer pins are provisional; do not approve
or deploy them as the epoch-3 lineage. No state/journal migration, launcher
change, generated stream or new administrative command. Only the current
compatibility epoch changed in the production descriptor. The runtime and
reporting contracts are documented in `docs/workspace-{portal,updates}.md`;
verify preservation of earlier cutover guidance and fail-safe recovery.

Saved reviewer0, Sol/xhigh, high risk, all four prior lanes. In addition to
full history conclusions, inspect the old source-owned 2→3 switch and future
3→3 compatibility, required helper behavior, legacy 1→2 and write/recovery
fences. Deliberately retain strict alternate-executor recovery equality; an
unfinished original lifecycle must use its original recovery and still fences
an upgrade. Test owner reports focused pinned Ruby 17 cases/235 assertions,
Go contract/MCP/maintenance, tagged fixture-unit and compile checks passed;
old contract red and frozen source 2→2/2→3 comparator checked. No claim of an
actual quiet native cutover or changed selected helper. Call out the smallest
faithful end-to-end process evidence needed before activation, and any fixture
scope worth avoiding. D3 separately resolves the system baseline drift.

## November 26 rebase and deployed-pin equivalence

Review the four complete ranges in [p3-review-range.diff](p3-review-range.diff).
Prior reviews and test receipts remain scoped to their recorded heads.

| Range | Base | Head |
| --- | --- | --- |
| Runtime (two commits) | `e3102d0b7bc0e8904388d8019847df24f233d3b1` | `2a1d58df7c3bb845da4d286ef38989bae01da4a0` |
| Workspace (one pin) | `56aadac5808e9c1d03f2353d8a2708d152f395fd` | `94d89fc5b36b0be8a65f36019049f68da76986b1` |
| D (live-base deployment only) | `109d789f0a4ee875f8bd27a0b72ea76c38ee234a` | `3637ae47905dff5762e43dfd0c6e3b9a7f9a8444` |
| F (configuration integration only) | `0b648b23c76977bc603bd57b671035920314b767` | `ef407ce3b7ffa99055c78b0807f6cdedd9537450` |

All four ranges are committed and quick-checked. Runtime and workspace feature
refs are published. Runtime `range-diff` preserves both patches and stable
patch IDs; upstream Pi flags and reporting policy 4 remain intact. Scoped Ruby
20/292, focused Go, tagged fixture and compile checks passed; exact [hosted
CI](https://github.com/aither64/dev-workspace/actions/runs/45805531497) is in
progress at packet time. Workspace/config paired check passed for both D and F
on the exact SHA and runtime NAR `sha256-mzRZ4p7PCqhWldMNqWNBU6dR6tmLLVRuzLGEIH++MVc=`.
Config hooks, `diff --check`, and independent regeneration verified exact trees.
No unmerged interim pins, repeated pin streams or migrations in these ranges.

D/F are not patch-ID equivalent. D adds the codex-web source change already on
F's base (`2547d535`), and the 28 reachable runtime graph entries agree. The
release question is whether the **deployed feature lineage** D has an equivalent
integrated successor F under the ordinary machine claim, not whether the two
whole systems are equivalent. The reported build-plan projection across 110 hosts
changes only aitherdev's runtime input in each range. The live control reproduces
its installed derivation; D and L share 6579/6584 recursive derivations, with
only configuration metadata, aggregate `/etc`, activation wrapper and toplevel
changed. This is evaluation evidence, not a realized or activated system.
Config evidence is in `/tmp/d3-monitor-config-p3.4TVuQI6N/`; Git diff is copied
above for read-only access. Confirm D/F baseline scope, inherited dependency
coverage, retained mapping and release proof. Do not approve a legacy
`patch_equivalent` certificate. No configuration publishing, package selection
or live effects established by this packet.

Use prior four lanes; focus on refreshed scope and changed dependencies,
not repeating unchanged source review. Preserve the operator guidance for
source-owned, quiescent cutover and verify documentary boundaries. State actual
remaining tests, the exact ranges, whether D→F feature equivalence is supported,
and explicit history/stream/migration conclusions. Current deployment source is
selected epoch-2 `3y9ns5…`, not the old `py81…` or currently serving `gh680…`
helper. The dedicated process cutover fixture and live postchecks remain.

## D5: temporary Pi request discard bridge

High risk: original-request authority, destructive retirement of persistent
selectors, partial-write recovery, and mixed-version host selection. Lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Retained `reviewer0`, GPT-6.2 Sol/xhigh, read-only and independent. The local
operator is trusted as documented in runtime `AGENTS.md`; remote requests
remain untrusted. HTTPS BasicAuth and owner admission are independent of the
request UUID and Origin (the latter is a cross-site mutation check).

Goal: discard only the original accepted failed pre-runtime Pi request without
retry, Runtime Start/Ensure, native Create/Send, tracking fabrication, resource
retirement, or deletion-epoch change. Keep D live and the original claim held.
A real authenticated human confirms in B's original request page; no token,
direct socket/client shortcut, forged confirmation, or general lifecycle
feature. The deployed target T, normal pins, monitor/runtime authorization,
daemon code, native registration, and previously accepted F4 stay unchanged.
See [settled design](design.md#d5--discard-one-never-materialized-pi-request-without-retrying-it)
and [planned guest](verification/d5-compose-plan.md).

- Runtime bridge H checkout: `worktrees/2026-11-24-monitor-session-ownership/dev-workspace-discard-bridge`.
  Exact selected-source base `e3102d0b7bc0e8904388d8019847df24f233d3b1`, sole
  commit `255198028181dfeacb19004b82ef58838a776c1f`, `portal: discard failed
  pre-runtime Pi requests`. Full binary diff `verification/d5a-bridge.yKn1Ym.patch`,
  SHA256 `cb86a109057b7e4cf3262d20b338b5071a8e6745f759ea406e963d14a5061b71`.
  Exact O+patch Git tree `35a1653156cd08f9245c66dabae0c61f15890d21` equals H.
  No superseded branch history, dependency streams, or schema migrations in
  H; independently assess. New pending schema-1 marker/audit belong to B,
  not an on-disk migration. Completed schema-3 mapping is an existing format.
  H is a development ref only: not published, deployed, released, consumed or
  merged. Review scope growth against the single supported transaction, not
  based on an arbitrary line limit. No general pending-journal subsystem.
- Workspace composition K checkout: `worktrees/2026-11-24-monitor-session-ownership/workspace`.
  Base `844ac4dbf768ebced1d27d208f4d5ebaf8b82deb`, sole commit
  `e0858cb839ef0f74f36ed810273f82ff070be979`, `maintenance: package the Pi
  preparation discard bridge`. The [exact K log and diff](verification/d5c-k-review-range.diff)
  contains only `maintenance/2026-11-24-pi-discard/{flake.nix,flake.lock,bridge.patch}`;
  patch hash equals H evidence above and neither root flake nor lock changed.
  No intermediate lock updates or migrations. W0
  `b095ac05040be226258afc16233d76969476f1f6` locks selected O, site extensions
  and dependencies. No-patch actual-source override reproduced installed O
  drv/output. All 1,153 path bytes/modes/symlinks of patched Nix source match H,
  NAR `sha256-60gsUY4JN5omGrifuw1oewN52OaUIBDoeV9gn60Qn7w=`. Parser, nixfmt,
  H whitespace, one generated lock graph and ordinary root-pair check passed.
  Both working-tree subdir and exact K git-archive subdir evaluate to
  `ckyy6i5nx6m2wfp54yq29rpbl8wqr8a6-dev-workspace-0.2.0.drv` →
  `sz1ya8l9qzadcrrajnpwdch3dm7s9h6d-dev-workspace-0.2.0`. Exact archive is the
  proven bounded evaluation (full `git+file:?dir=` eval did not finish within
  its bound). B is not yet realized, guest tested, published or integrated.
  Inspect full compose equivalence/ancestry, input pin and unchanged T.

Quick evidence for H: pinned Go `-mod=readonly` focused web/session/piruntime
checks (discard, creation/readers/admission, shipped client, retained runtime),
Ruby CLI reserve/marker checks (20/162), Ruby host marker-only (1/5), Node
syntax and `creation_settings_browser_test.cjs --discard-contract`, real Go
preparation page handler and `git diff --check` passed. Constructor fault
fixtures exercised each selector retirement, mapping rename/sync uncertainty,
completion/last unlink, marker-only restart, cross-owner stale replay/retry,
unchanged adjacent state and zero Pi Ensure/Create/Send. These are simulated
faults/synthetic cases, not actual power-loss, browser/nginx or live eligibility
proof. Exact O/T preflight and portal tests accept stock terminal mapping with
no worker; a synthetic stock O stopped bundle passed actual O preservation
inventory. No O→B→T guest or live action has run for D5.

Documentation routing: runtime README links `docs/session-preparations.md`
(owner reference/how-to: exact eligibility, confirm, conditionally resume,
private evidence retention) and `docs/workspace-updates.md` (mixed-version
operations: bridge selection, pending fence and forward recovery); check these
links, consistency with the UI/API/CLI and that limitations are preserved.
`design.md` and `state.md` own this particular rollout and approvals. Runtime
portal owns the original preparation action; shell/host share marker presence,
existing T readers own the terminal projection. The dated workspace subflake
is the only consumer of the full reconstructed B source. Inspect actual
admissions, cache/collector exclusion, native absence/retention invariants,
strict disk/compiler boundaries, replay after replacement, authenticated UI and
closure/deployment intent. Return explicit whole-branch history, pin-stream,
migration, documentation and remaining-risk conclusions with file/line refs.

## D5e final follow-up: one-shot privileged startup repair

The user explicitly authorized the original discard and directed continuation
through deployment and merge without another confirmation. The conditional
same-UID channel D5d was rejected and is absent. Keep the original typed hold,
D and T; no extra system unit, public listener, credential handling, hand state
edits, new Pi request, or start/retry. Only the old exact failed request can be
retired. Current [D5e design](design.md#d5e--one-root-authorized-startup-transaction-current-release-brief)
uses the existing root deployment transport (read-only probe returned UID 0
and exact active D), a sealed fixed-path grant, and the selected bridge's
sole preparation-owner writer before normal startup workers. Publish only
after full O→B completion and proven old-portal join; retire only after exact
cancelled mapping, completion audit and confirmed marker cleanup from B.
Root never executes project or mutable user code; the publisher is an
immutable separate artifact, not setuid or a daemon.

- Final runtime sole commit `f62115f94595d5e907c0c1e61b3d907146507b54` on
  O `e3102d0b7bc0e8904388d8019847df24f233d3b1`, tree
  `9022a1a95779e0ad70a708673c8093d6eefa1898`. Whole O→H″ binary/full-index
  [patch](verification/d5e-bridge-Hdoubleprime.FbLrZr.patch) SHA256
  `04210593631926fbd9583bfc0c1716944d3b0eeb56997a73c1012130006dc1c6`.
  [H′→H″ delta](verification/d5e-Hprime-to-Hdoubleprime.PazJOz.patch), SHA256
  `678aa255c655ecbd4d6839c95f5dfcbbc4ebd726c8b2416e8bc3699ce77aba40`.
  H′ `26c46a909f9384ed2a88fa005b7c754a430e1444` folded the reviewed H
  browser-cache key and final-unlink cleanup remediation; the original H→H′
  [delta](verification/d5a-H-to-Hprime.8OIKwd.patch) and check evidence remain.
  No new storage conversion, dependency/native change or T behavior. Existing
  documented pending/audit and root startup grant are additive B-only state.
- Final dated workspace sole commit `00f302df670c511e15e28fab5b91835032177255`
  on `6bb0b6059a6dd96224260703709f7fbd700861d7`; [exact range and log](verification/d5e-k-review-range.diff)
  SHA256 `41355007b3836b6519eccd3d1483b799f0a7d57c1369c039b4ea25a20fd67c07`.
  Exactly four dated paths (`bridge.patch`, `flake.lock`, `flake.nix`, `publisher.go`).
  Root flake/lock and W0 graph unchanged. Nix patched source matched all 1,155
  H″ paths/blobs/modes, NAR `sha256-uelsl6+cIDbeTG5L0yvpR7s+QmgZ509lAv8MY7V+vsc=`.
  Immutable K″ archive `/tmp/d5e-compose.agtdQ8ot/committed/maintenance/2026-11-24-pi-discard`
  matches checkout in builders-disabled eval: B `.drv` `99r1wsjg7g53c7r7n7bjlkg1pd8kydqn`
  → `9n8vp85fa11n1wy801zbl244q8ih12jl`; separate grant publisher `.drv`
  `12q0pjmxm3sga0mc3nril1hp7wxxsmqi` → `d1yhbsylp9x9yg4g9ia36j64sbrz3jdy`.
  Parser, Nixfmt, exact applied-source whitespace/tree diff, Go and synthetic
  namespace checks passed. Publisher requires root+bounded private stdin,
  root-owned no-follow/no-replace objects and exact-byte replay/retirement;
  reader and publisher must agree. Canonical paths, actual portal group,
  independently privileged root operation and real artifacts remain guest proofs.
  Neither output nor guest has run against the live target.

Focused runtime proof: Go discards/creation/reconcile/native-absence (web
10.345s, session .031s, piruntime .039s), cmd compiled, Ruby 2/34;
`diff --check` both ranges. No-grant zero effects, malformed/provenance/claim
rejection, real H′ writer, interrupt/restart, exact marker cleanup and newer
owner isolation; Go uses injected verifier. Verify guest path with actual
managed selected B subprocess, native `profile_claim!(native:true)` no
bootstrap/scope shortcut, exact original identity/generation fields, no
unrelated pre-worker rehydration, bounded refusal (no automatic restart), B
terminal confirmation and stock T continuation. Do not infer end-to-end
claim/service or real power-loss proof from these quick tests.

General/Architecture/Scope/Risk high; retained reviewer0 saved Sol/xhigh.
Same runtime README-linked preparation and workspace-update docs own the
original operation/status and bridge recovery. D5e rationale and this single
machine's scheduled action belong in design/state, not public configuration
or target data. Require full range history (no obsolete unmerged approaches,
stale pin streams or migrations), package/root closure and one-shot exact
ownership and recovery conclusions before the guest, not live authorization.

### D5e final committed endpoints for standalone review

The two direct findings against H″ were applied before long tests: a
positively distinct workspace starts normally, partial/alias conflicts refuse,
and previously drafted browser discard UI/POST are removed. A stale old POST
returns 404 with no mutation. Root-grant startup is the only writer. Preserve
mandatory review of the final sole commits, using the earlier review only for
unchanged baseline context. Retained `reviewer0` could not run the required
same-session command, reported no final readiness, and is parked. Standalone
fallback is the installed default delegated `reviewer`, `gpt-6.1-sol`/xhigh,
fresh context, read-only.

- Final H `9044ec0d0eaa558d207bca632702dc82f342a670` on O `e3102d0b`, tree
  `e4ef96f41ce9dbbb3f49894b147abf4f2868f1cc`; [full binary diff](verification/d5e-bridge-final.ASUUbG.patch)
  SHA256 `5cf6022b7f88ea097825f5bd3c181ae3087b14fc213fb96062899bfd87f39cd5`;
  [H″→H](verification/d5e-Hdoubleprime-to-final.JVVnaC.patch) SHA256
  `00703ad710250c12a19280baa71a987699b9296b3c337c8aeff6c2b6f96acc42`.
  Go quick checks passed 13.455s/.021s/.029s for web/session/piruntime and
  command compiled; Ruby 2/34 unchanged. Six affected frontend/template
  files are byte-identical to O. No old HTTP authority, negative test checks
  the old valid-shaped request returns 404 and creates no work. Final tree
  comparison exact and `git diff --check` clean.
- Final K `5ba7a17176f81835f49da014b33fedcc4effabb3` on `6bb0b6059a6dd96224260703709f7fbd700861d7`,
  tree `9f96e642e2eec4fc60f4527209119913b0a33641`; [full range](verification/d5e-k-final-review-range.diff)
  SHA256 `ab9ead6d3ae96bb07579300daf8e2740f3a39b15895023507af50bc1a45a516f`.
  Only the patch changed from K″; exact applied patch reconstructs all 1,155
  source paths, blobs and modes, publisher/lock/root/site input unchanged.
  Exact archive `/tmp/d5e-final.2rc8ANM1/committed/maintenance/2026-11-24-pi-discard`
  equals untouched checkout projection: B drv `2dr5qnx3bxc072rh78r0a3ni3kwfdybc`
  → `n2192vx80yfylnqqich8839xx20ais7i`, publisher drv `12q0pjmxm3sga0mc3nril1hp7wxxsmqi`
  → `d1yhbsylp9x9yg4g9ia36j64sbrz3jdy`. Actual distributions/guest runs
  unbuilt. See [exact projection](verification/d5e-final-projection.json).
- Separately, the F5 parked review can use the [exact F5 range](verification/f5-review-range.diff).
  F5 is integration-only after verified actual T, never activate it. Review
  renewed D→F5 complete feature lineage and typed mapping, not whole-system
  equality or a legacy `patch_equivalent` claim.

### D5e live follow-up: exact ready-Pi initiating claim

[Bounded design](design.md#d5e-follow-up--authorize-the-original-retained-pi-claim-owner-bounded-correction).
The exact unarmed bridge was verified in a complete guest and selected live.
The live authorized grant was refused at the private extra Codex-thread
predicate, before intent. All original selectors stayed byte-identical, no
marker/audit/terminal mapping appeared, and the exact grant was retired. B
serves unarmed. The original held typed claim is a ready Pi initiating owner,
not the failed Pi request. The ledger marks no Codex-thread owners as bootstrap;
this cannot by itself prove or disqualify a ready Pi native owner for this
private repair. Keep the exact ordinary native:true profile-claim gate, Codex
branch, full present root authority, no-effects and cleanup proofs.

- Runtime H→H+ sole additive commit `3965b0f34a341b7d0e3ebd0760ec58ad4f9698b5`
  on `9044ec0d0eaa558d207bca632702dc82f342a670`; tree
  `cf8238bb712d2d0183d0751773c752147e7c8a40`. Complete [delta](verification/d5e-bridge-H-to-Hplus.15PlYr.patch)
  SHA256 `4ea704dfefd412bf15b79dbe6b7f41bb60c66ff1588e5929ab0c85091427de28`.
  Only `libexec/workspace-host` and `test/workspace_host/profile_transition_test.rb`.
  Positive exact current Pi ownership from stock ready manifest, binding,
  journal/completion, tracking dev/ino and retained runtime generation/authority;
  no generic bootstrap. Ruby quick 3/58 actual stock claim acquisition and
  profile check with mapping seam; exact shipped B reader under both locks
  parsed original, pending and completed-cleanup states. No new format,
  dependency, Go transaction, provider, publisher or native changes.
- K+ composition receipt follows. Keep already deployed K ancestry and
  reconstitute full O→H+ from exact checked dated package recipe, fixed
  publisher/lock retained, no migrations or redundant streams. The sole
  scope is exact Pi initiator proof; no broad identity override or retry.
- Final review must focus on lock/TOCTOU, partial/stale/foreign owner, duplicate
  YAML, same inode/incarnation and authoritative ready generation binding,
  all canonical registry roots for stock preflight and exact issuer selection.
  No live evidence implied by synthetic tests; require ready Pi acquired typed
  claim, actual B refusal, B+ accept/cleanup and normal T with same ownership.