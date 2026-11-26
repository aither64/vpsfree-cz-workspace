# I4 React delivery and review packet

Status: **source complete, ready for lead acceptance and independent review**.
Long/full-suite/build/browser checks and publication remain held for that review.
Integration remains blocked on an authorized published TypeScript SDK release.
Implementer3 retains follow-up, browser/capture and review-fix ownership.

## Exact source and scope

- Initiative: `2026-11-25-backup-disable-design`; accepted D3 design/plan beside this record.
- Repository: `git@github.com:vpsfreecz/vpsadmin-webui.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-backup-disable-design/vpsadmin-webui`.
- Branch: `dev/disable-backups`.
- Base: `e311b1c0af0f50fa4c6f6ce83c514c1a866eb042`.
- Final head: `9e6ed96a49de2f6b65bb3e730047c428b77185f4`.
- Tree: `95e476edc0859e14ce59f4f5c22a30e04c29131d`.
- Complete series: one commit, `9e6ed96a storage: add administrator backup cleanup`.
- Base-to-head diff: **19 files, +815/-10**; [exact diff](i4-logs/final.diff), [series](i4-logs/final-series.txt).
- Clean worktree/index. No push, PR, CI registration, release, merge, deployment,
  machine claim, temporary server or lifecycle action occurred. No command remains running.

The requested feature is administrator-only cleanup with default-on preservation,
all-primary-snapshot scope and retained backup history, including datasets whose
plans are already gone. The page submits exactly one generated SDK action with
only `recursive` and `backup_first`; the ordinary action-state receipt is handed
to the existing task controller. There is no custom phase/continuation/cancellation
protocol. Accepted work continues after browser exit. Existing preflight, durable
request generation, task binding, pending state, duplicate-submit prevention,
known-rejection retry and ambiguous-outcome reconciliation are reused.

The actual administrator identity and permission-filtered server action/input
capability gate cleanup. The shared plans page includes the no-plan state. The
confirmation names the dataset and explicit existing-subtree scope, defaults
preservation on, explains every open target, normal-transfer preservation failure,
time, manual/source-only snapshot loss and no new live-state snapshot. Both the
list and ordinary plan-removal confirmation explain that snapshots remain. The
VPS root card links to the actual `/app` or `/admin` dataset plans route with
`recursive=true`, without inventing an admin Backup Center.

## File and ownership inventory

| Scope | Files |
| --- | --- |
| Generated action boundary and capability | `src/lib/api/datasets.ts`, `datasets.test.ts` |
| Shared ordinary mutation/confirmation | `DatasetBackupCleanup.tsx`, its component tests; `DatasetPlansPage.tsx` and its tests |
| Existing VPS entry | `VpsStorageRootDatasetCard.tsx`; assertions in existing `vps_storage_tab_mounts.spec.ts` |
| Bilingual copy | English/Czech `storage.ts`, using lead-finalized D3 copy and locked terminology |
| Browser source | `dataset_backup_cleanup.spec.ts`, strict E2E inventory and tsconfig entry |
| Documentation | Requirements/evidence, workflows, action contracts, SDK dependency/local-install guide and dated work log |

Shared-page consumers are dataset and NAS plan routes under app/admin, plus the
Backup Center's embedded dataset plans workspace. All use the same control. The
vpsAdmin API owns authorization and destructive storage semantics; I1 owns that
implementation. I3 owns generated types and transport operations. The WebUI
adapter calls the actual generated method; it does not handwrite SDK members or
bypass the API. No backend sources were edited by I4.

The single commit bundles this one UI feature with its requested nondestructive
plan-removal explanation, entry link, supporting tests and documentation. There
is no independently introduced subsystem or dependency update stream.

## Candidate and complete input identity

The manifest/lock/provenance still select the prior **published registry 0.6.0**,
which lacks this action. Development uses the verified **local** 0.6.0 candidate:

- Archive: `i3-ts-candidate-final-50aa37ae/vpsadmin-typescript-client-0.6.0.tgz` in this session.
- SDK source: `6d4941bbf617a0d1e1c131a2bf14ca6476389809`; base `b619eb8324bfe80c7b225f698fb83efe97639c83`.
- SHA-256: `671b54f52da297cd465c1b7516841a859c84099ab30d776e5086802559d19a10`.
- Integrity: `sha512-pX/rP/o+7idHacYBFZcbRkhwonUNDi9kzVBtgClhBTrb6R1xim4/z1uk9dxN2Gm3RyjoXK14BXKPlYog584UnA==`.
- Actual final API source: `50aa37aede8926965598f4f8fb0782dce377afb6`.
- Schema SHA-256: `cbe3a7ca90d7f1c94e2b769058b1c32a570e36fd92f55cf48a4302d4e50dc05d`.
- Raw provenance SHA-256: `31545e703ae6142f5d4ffce87b581a30685cecbb89662eff3ad25fedb00441c0`.
- Exporter lock SHA-256: `dd5db5ca44bb69ca2ae0244515103146f17b7621f12ca34c3dec6950f4455aaf`.
- Profile: API 7.0/protocol 2.0, full six plugins, English, mount `/`.
- HaveAPI generator: `1ef9b204ba45bb261d3334be5c555cc1856b713b` / 0.32.2,
  source digest `c21f17af40295bdd633f846ef9099bfb3d7a3c52aa1b581a802b5c42d7b426e7`.
- Generator shared Ruby source digest: `d704e6c155f9f2ec82bdf627857bdc23aa08a1d2133806df1f8ed5beb2d8c439`.
- Provider tooling: Prettier 3.9.10, config digest `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356`;
  Node 24.21.0/npm 11.19.0/Ruby 3.4.11/TypeScript 6.0.3.
- UI tooling: its locked Nix Node 24.21.0/npm 11.19.0, TypeScript 5.9.3;
  transport `haveapi-client@0.32.0`; locked terminology API `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`.

[Provider receipt](i4-logs/final-candidate-receipt.json) and [installed graph proof](i4-logs/final-sdk-graph.json)
bind the exact archive. The complete installed graph is retained in
[final-installed-package-lock.json](i4-logs/final-installed-package-lock.json).
Manifest and lock were byte-compared unchanged. **All 409 non-SDK installed
entries match the canonical lock's version, resolution and integrity; zero
required entries are missing. All 1,392 installed SDK files match the archive.**
Canonical lock SHA-256 is `eee6460485c5aea039721b682839b58d44ce19b7acb3e42f50c59650cd9d429d`;
final installed graph SHA-256 is `9050f8e30508c000115a51151101a62b180543a361b0ba5be817c5e0cbd3a6eb`.

The initial documented `--package-lock=false` install drifted unrelated local
dependencies. Its inventory/checks are retained as `d3-initial-drifted-*` and are
not the final environment claim. Restoring `npm ci`, then installing with
`--no-save --package-lock=true --ignore-scripts` kept only the SDK overlay. The
owning guide now records that verified recipe, approved by lead's direct writing
pass. No dependency versions or locks were committed for this correction.

The first validated D3 archive was `f0b9e758…` from SDK `7393632…`, actually
exported from historical API `5526c99…`. Input equivalence to final API was
established by identical API/exporter trees. I4 independently compared it with
the final archive: all 1,392 file identities present; **1,390 byte-identical files**,
with changes confined to `schema/provenance.json` and `tools/generator.json`.
All JavaScript, declarations and schema are identical. See
[comparison](i4-logs/final-candidate-comparison.json). The final candidate now
names the actual final API source; no historical export commit is claimed merged.

## Checks, scope of reuse and remaining verification

| Check | Result / exact boundary | Evidence |
| --- | --- | --- |
| Five focused adapter/SDK/component/page suites | **64 passed**, canonical non-SDK graph plus first D3 archive | [canonical-unit.log](i4-logs/d3-canonical-unit.log) |
| `npm run ci:quick` | **Passed**, canonical graph; toolchain, docs, lint/format, localization, CSP, pages/structure/overlays/mutations, app/tooling/E2E/BFF core types | [canonical-ci-quick.log](i4-logs/d3-canonical-ci-quick.log) |
| Final archive consumer wire tests | **30 passed**, final candidate; dataset adapter and actual HaveAPI wire suites | [final-candidate-wire.log](i4-logs/final-candidate-wire.log) |
| Final documentation audit | **Passed**, 298 docs / 76 requirements; inventory 270 routes / 79 modules | [final-candidate-docs.log](i4-logs/final-candidate-docs.log) |
| Archive/graph/manifests | **Passed**, exact identities above | Graph/comparison receipts |
| `git diff --check` | **Passed** | No whitespace errors |

The final metadata refresh changed no UI runtime/type/schema input. The 64-case
and full quick results are reused within that proven scope, with fresh final
archive wire and documentation checks. No broad or expensive rerun was used to
mask a failure. An initial quick batch stopped at E2E config formatting, corrected
with the declared formatter before the successful batch. Required hooks were
inspected (no declared framework/non-sample active hook/hooksPath); Nix-context
contributor identity was verified before each amendment. No hook was bypassed.

**Not run:** full unit suite, build/Nix release checks, browser execution and
screenshots, live API/storage validation or deployment. Browser source covers
EN/CS, desktop/mobile, planless admin/default-on scope, opt-out/unknown receipt,
member/capability exclusion, ordinary removal explanation, known rejection, and
real app/admin root plans links. Fixture source/captures are not runtime proof.
Long execution remains held until lead-owned independent final review completes;
use a fresh watcher for the related batch, with this graph/archive/head identity.
Browser servers must be registered through `dev-session service run`; keep
Playwright auto-start disabled when pointing it at that owned server.

## Documentation and KB routing/fidelity

| Topic / reader and class | Authoritative location | Evidence / applicability |
| --- | --- | --- |
| Plan removal and administrator cleanup / UI maintainer reference | `WORKFLOWS.md`, `ACTION_CONTRACTS.md` | One ordinary mutation/task, explicit unknown/partial outcome limits |
| Acceptance / reviewer reference | REQ-011/024/048 in `REQUIREMENTS.md`, `EVIDENCE_MATRIX.md` | Unit and browser-source references, no deployed/capture claim |
| SDK contract and repeatable local development / maintainer reference/how-to | `HAVEAPI_CLIENT.md`, reached from design README | Generated members, ordinary metadata, published-release gate, verified lock-preserving overlay recipe |
| Change chronology and verification / repository-required dated record | `docs/work-log/2026-11-25-disable-backups.md` | Current behavior and exact candidate distinguished from publication/deployment |
| Individual input/head/check receipt / session evidence | This record and linked logs | No rollout executed |

No existing documentation was moved or retired. Lasting contracts remain in the
owning design handbook; temporary execution/input details remain here. Lead owns
and finalized EN/CS product copy with the required writing skill, including
normal-transfer preservation failure; lead also approved the entire SDK guide
unchanged after its direct writing pass.

Canonical KB workflow was read. Current `backups.vps.open` and
`backups/vps-backups` bindings reference PHP, not React. Affected-review pages:
CS `navody:vps:zalohy`, `navody:vps:obnova_webu_zo_zalohy`, `navody:vps:exporty`;
EN `manuals:vps:backups`, `manuals:vps:exports`, `manuals:vps:vpsadminos:storage`.
I2 owns PHP landmarks. React synthetic EN/CS desktop/mobile captures are pending
post-review execution. No production KB write or staging claim occurred.

## History, risk and next dependency

No migrations, backend edits, released/deployed/externally consumed new state,
repeated dependency-pin streams or supported D2 compatibility boundary exist.
Superseded unpublished preparation was amended away as lead directed; prior heads
and checks remain in [pre-wiring evidence](i4-logs/pre-wiring-evidence.md),
[historical D2 diff](i4-logs/historical-d2.diff), and
[historical D3 preparation diff](i4-logs/historical-d3-preparation.diff).
Prior exact heads: `b144054198c467b4e4a25a9d1521973a673a77ec`,
`e1bf4004668dd6bf1b430bd43297693c14926adc`,
`8a241695ead4bda8753dc537c98f5def34ac3073`, and implementation before metadata
refresh `92cfe457a53acb4b844e5da0a6fbeebc5d73c35c`. Current history introduces only
D3 behavior. Whole-branch independent history/no-migration conclusions are pending.

Suggested review risk is **High** because the UI starts destructive cleanup and
must retain administrator, receipt and compatibility boundaries. Applicable lanes:
general, architecture/repetition, scope/proportionality and risk/compatibility.
Lead owns reviewer selection/invocation and packet acceptance. There are no new
backend primitives, output protocol, persistent workflow or forced repair paths.

Next: lead accepts this code/review packet and invokes independent review; I4
fixes findings, then runs the held full/build/browser batch and inspects captures.
Before integration the separately authorized published SDK must replace the local
overlay in manifest/lock/provenance, with affected final verification. API and
scheduler readiness is separate. The branch is **not integration-ready** and has
not been published. No approval is inferred for SDK release, integration,
deployment or session lifecycle.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-backup-disable-design/
