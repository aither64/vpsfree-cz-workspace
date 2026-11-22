# P4 provider policy and settings package

Owner: implementer5. Source package ready for lead acceptance, 2026-11-12.
Independent final review and combined readiness remain lead-owned. This package
does not claim production provider capability or completion of native fallback.

Current P4 stream includes the identity fix
**`fc02306ab8e66f85fdae06519b1c907dc1728120`** after the original package commit
`f8cd2941626eac5fbe8e12c4e5a3fee9e309735a`. Both are unmerged/unreleased and
must be consolidated into the same logical P4 stream before final review, under
the lead's shared-history window. No account projection/API continuation is
included or implicitly released. The original inventory/checkpoint below remains
historical evidence; the final identity-file bytes are those in the fix commit.

## Identity correction and final package checkpoint

Implementer2's real creation-selection fixture found that the original P4
validators incorrectly reused the catalog's lowercase/max-63 identifier rule
for execution identities. This rejected canonical absolute workspace paths and
64-character lowercase-hex session/member incarnations before policy freeze.
The original fake fixture's short invented identities failed to expose it.
This was a P4 source/fixture defect, not a missing provider entitlement or
P2 admission failure.

The narrow fix separates execution validation: bounded canonical absolute
workspace, existing session-compatible slug syntax, exact 64-lowerhex
incarnations, and retained member/lead address syntax. Catalog validators and
all-chain route availability remain unchanged. The main fixture now uses
`/fixture` and realistic incarnations; regression cases cover valid long slug,
lead/member identities, malformed/noncanonical workspace, short/uppercase
incarnations, invalid member address and unchanged catalog identifier bounds.
The wrong-session case uses a different valid incarnation to retain its scope
assertion.

- Fix parent: `9a4f44e9c64106bc36d65fead1be881412c778c3`.
- Fix head: `fc02306ab8e66f85fdae06519b1c907dc1728120`.
- Exact inventory: `catalog.go`, `policy.go`, `piproviders_test.go` beneath
  `portal/internal/piproviders/`; 46 additions, 7 deletions.
- Focused repository path-flake check passed:
  `nix develop path:. --command sh -c 'gofmt -w portal/internal/piproviders/catalog.go portal/internal/piproviders/policy.go portal/internal/piproviders/piproviders_test.go && cd portal && go test -mod=readonly ./internal/piproviders'`
  (`ok .../internal/piproviders 0.077s`).
- Ordinary Git-filtered flake evaluation had stopped before testing because
  another package referenced untracked `nix/pi-worker.nix`. No peer staging or
  P7 edit was used. The path flake evaluated current source successfully; the
  retained cached D shell derivation supplied by implementer2 is available for
  any later necessary focused check. No repeated unchanged check ran afterward.
- One intermediate regression run exposed the malformed old wrong-session
  fixture; that test was corrected to use another valid incarnation and the
  focused suite then passed.
- Frozen source SHA-256/Git blobs, exact staged/committed inventory and owned/
  staged whitespace passed. Fresh parent/index were verified; normal tempfile
  `git commit -F` used no bypass. Index was empty and ownership released promptly.
  No P4 process, peer staging, push or broader test remains.

Fix manifest:
`/tmp/p4-identity-fix-manifest-2026-11-11-pi-codex-migration.json` (disposable).
No format/schema migration, auth/credential read, account projection or fallback
execution was added. New production policy state still has no deployed/released
P4 predecessor. Lead owns acceptance, consolidation, final review and any
separately accepted account-binding continuation. P4 retains fix capacity until
accepted and has accepted no other executing package.

## Exact revisions and inventory

- Repository D: `git@github.com:aither64/dev-workspace.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace`.
- Branch: `2026-11-11-pi-codex-migration`.
- Initiative base: `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
- Package parent: `daa780d1781df025aa918970310f4fb0f5f66a83` (committed P3 core).
- Package head: **`f8cd2941626eac5fbe8e12c4e5a3fee9e309735a`**.
- Commit: `pi: add provider policy and member settings coordination`.
- Exactly nine new files, 1604 lines including tests/docs: `docs/pi-providers.md`
  and `portal/internal/piproviders/{types,catalog,policy,resolve,settings,fallback,store,piproviders_test}.go`.

| Owned file | Committed Git blob |
| --- | --- |
| `catalog.go` | `f9af056d980f929285abb6f28b886e0ee76eb129` |
| `fallback.go` | `7fb7d511e45588a9db50dcaa589d4e89f4f5fc1d` |
| `piproviders_test.go` | `ffc1b41c323a15e85077c4200776373d30b8bb0c` |
| `policy.go` | `d11a5543a6dda4aba438d815b4102349997f4be3` |
| `resolve.go` | `0f62870d21af74f1e6a8caa43c3cf504a5ab95da` |
| `settings.go` | `e7fbb3125edac01c3991b058115fd921dafef2fd` |
| `store.go` | `881fdf0a7dd96ca51635592738da3060a8de2ed7` |
| `types.go` | `0875b09118009155ca2db8f288aa94a9a42b12f1` |
| `docs/pi-providers.md` | `d830ed3984e461af178bd64fbed49580833974c1` |

Per-file SHA-256 and Git blobs were frozen before staging, checked against the
exact staged entries, and rechecked against committed blobs/current owned files.
The raw manifest is disposable at
`/tmp/p4-commit-manifest-2026-11-11-pi-codex-migration.json`.

## Delivered boundary

Strict trusted catalog/account/physical-route validation; immutable catalog
input digest; exact thinking/capability/gate checks; session default and exact
member-incarnation override/clear; stable per-member policy digest; private
schema-1 CAS desired-state store with no-write reads; requested/effective/observed
physical projections; P3 Configure coordination with revision checks and
unsupported account-switch rejection before the call; pure finite PlanNext.

The planner never sends, changes a frozen receipt, invents an operation ID,
replays tools or activates a virtual router. Accepted/Unknown, partial output,
native-entry presence and effect uncertainty prevent a candidate. Even positive
NotSubmitted/no-effect proof only yields `candidate_execution_unavailable`.
Auth/storage, structured policy and unclassified failures retain explicit holds.
Ordinary available routes are independent of the unverified Daybreak route.

Architect1 confirmed explicit physical `Model.Kind` and the narrow exact failure
evidence map as clarifications of the accepted invariant. There was no material
design deviation or worker/controller/central-route edit. P3 types were confirmed
directly with implementer1; its additive CreationVerifier does not change P4.

## Checks and timing

- Started 10:49 UTC. Concrete source and first compile passed at 10:53.
- First fake fixture run hit P3's in-progress missing `callRaw`/`verifyProcess`
  helpers at 10:56. Exact errors went to implementer1; P4 did not diagnose or
  repair that peer graph. The owner supplied the coherent compile boundary.
- Focused repository-Nix command:
  `nix develop --command sh -c 'gofmt -w portal/internal/piproviders/*.go && cd portal && go test -mod=readonly ./internal/piproviders'`.
  Fake acceptance tests passed at 10:59; final Go-source check passed at
  approximately 11:02 (`ok .../internal/piproviders 0.059s`).
- Tests cover strict JSON and duplicate/reference/account/cycle/capability
  rejection, unverified route refusal, inheritance/clear/incarnation isolation,
  digest bytes and unrelated-member stability, concurrent CAS and source
  revision checks, private/no-write/malformed-state behavior, exact Configure
  revision/outcome/account handling, and finite terminal/effect fallback holds.
- All nine owned paths passed whitespace checks before staging and staged
  `git diff --cached --check`. Normal `git commit -F` used a temporary message
  file. Repository instruction/framework inspection found no declared hook
  framework or installed pre-commit; nothing was bypassed.
- Lead applied required writing/Humanizer directly to technical docs, preserving
  the source contract. No Go changes followed the final focused check. No
  unchanged Go test was repeated for prose alone, as directed.

The focused check used the same-session working source graph, including P3's
then in-progress files; it is not an isolated clean-checkout full integration
claim. P3's committed coherent core and own clean selected checks were separately
reported by its owner. No long suite, credential/auth attempt, real model request,
activation, conversion, lifecycle action, push or merge ran in P4.

P4 was explicitly parked after source readiness while waiting for the committed
P3 parent and lead writing pass. On the granted short D index window, the fresh
parent was exactly `daa780d...`, index was empty, only owned paths were staged,
and the committed inventory/blobs were verified. The index was empty afterward;
ownership was released promptly before preparing this record. No P4 process or
background operation remains. Unrelated dirty source was preserved.

## Review material, compatibility and next dependencies

Risk is high because this introduces persisted desired policy and provider/account
selection contracts. Suggested combined-review lanes: general, architecture,
scope/proportionality, risk/compatibility. Lead owns reviewer selection/invocation
and the complete initiative base-to-final-head series, not this package alone.
The host operator remains trusted; validation covers remote/ordinary malformed
input, wrong scope, concurrent state and uncertain runtime outcomes.

This package has one substantive commit with its associated tests/docs. No
superseded schema, migration, follow-up history or repeated dependency/pin stream
was introduced. **No database/data migrations**, released/deployed predecessor
policy, history conversion or externally consumed P4 state. Schema 1 is new and
unsupported/malformed records refuse; Codex formats/defaults/recovery are unchanged.
No go.mod, dependency, package or configuration pin changed in this package.

Documentation routing: provider/settings/CAS/fallback contract → developers and
runtime integrators, reference → `docs/pi-providers.md` → P4 source/fake tests.
The guide is self-contained and retains failure, partial-success and compatibility
limits. README/index wiring is explicitly P7-owned and remains a dependency;
no shared entry-point edit was included. Individual test/commit evidence stays
in this session record rather than the reusable guide. Lead writing pass closed.

Consumers are the portal creation/settings composition and P3 Configure runtime
boundary; imports are one-way from P4 to piruntime/agentbackend. Current gates:

- P2 supplies authorized exact scope/admission, immutable creation snapshot and
  current desired-digest recheck. Actual catalog/default composition is not wired.
- P7 owns trusted catalog/configuration and documentation index wiring.
- P3 actual startup account map/Configure publication and native per-operation
  retry gate remain separately owned; AccountRef switching is still unsupported.
- Required automatic same-turn fallback remains gated by P3's accepted receipt,
  effect and cumulative-budget fixture. This commit contains no sender/hook or
  native routing activation and does not remove that overall requirement.
- Creation snapshots can freeze full Policy/catalog digest and each member's
  Source/PolicyDigest/primary desired Settings via existing Resolve. They retain
  fallback Chain/Budget/FallbackOn intent. No unaccepted fallback-settings builder
  or digest mapper was added; architect2's amendment remains design-only pending
  lead/design acceptance.
- Real route/account/model availability, including Daybreak, is unverified.

Next: lead accepts the package, sequences combined review and assigns any fixes.
P4 retains capacity for review fixes; no unrelated package is accepted.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>
