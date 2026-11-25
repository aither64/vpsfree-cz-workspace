# Nov24 admin Incidents — independent final review

Decision: **one Blocking and two Important source findings**. The completed packet has been reviewed in all four lanes; it is not ready for acceptance until the findings are corrected or disposed of under the mandatory review policy. Remaining verification and release prerequisites below are not passing evidence.

## Findings

### F1 — Blocking — PHP History is rejected by its own capability gate

GENERAL; RISK/consumer compatibility. Commit `73cd5d37`, present in reviewed backend `74c0af3a`.

[`webui/forms/admin_incidents.forms.php:65`](../../../worktrees/2026-10-30-oomd-abuse-policy/vpsadmin/webui/forms/admin_incidents.forms.php) unconditionally requires `sort` in both Index descriptions. The actual `IncidentPolicyEvaluation::Index` declares only `direction`, as do the final raw schema and generated clients. Consequently `admin_incidents_resource(true)` returns null against the very API delivered in this package, and every administrator History request displays unavailable instead of loading history.

The same mismatch occurs in parameter forwarding at line83 and the History sort control at lines146/162. The regression description at `webui/tests/Regression/AdminIncidentOverviewTest.php:339` invents the unsupported parameter, so its successful render does not validate the actual interface.

Correction: make `sort` capability/forwarding/control Exposure-only; History keeps direction only. Use the genuine exported History description in the focused regression and demonstrate that the capability gate and request work without `sort`. Root has allocated owner4's narrow remediation; it is not included in this immutable-source review.

### F2 — Important — Daily transaction links target a nonexistent PHP page

GENERAL/consumer correctness. Commit `74c0af3a`.

`api/models/incident_policy_read_projection.rb:384` prepares `?page=transaction_chains&action=show&id=...`. The delivered PHP dispatcher supports `page=transactions` (`webui/public/index.php:176`), and its selected-chain route is `?page=transactions&chain=<id>`. Both new daily formats therefore direct an administrator away from the transaction evidence when they follow Transaction details.

Correction: prepare the existing `page=transactions&chain=...` URL, retaining null-link behavior for invalid/missing bases. Add a focused prepared-link assertion tied to that real route. Owner1 retains the fix. This needs no new route or transport.

### F3 — Important — Terminal unconfirmed stops remain labelled queued

RISK/COMPATIBILITY; GENERAL. Commit `74c0af3a`.

`api/models/incident_policy_read_projection.rb:245`–249 derives failed/fatal/resolved chain outcomes but omits terminal `done` (state2) without confirmed Stop evidence. A retained queued stop whose physical chain is done but whose Stop record is missing, unsuccessful or incomplete falls through to `queued`. Overview consequently reports pending rather than uncertain priority; History filtered to uncertain misses it.

The existing supported recovery rule in `IncidentEscalation#reconcile_actions!` (`api/models/incident_escalation.rb:346`–354) explicitly classifies this terminal/unconfirmed case uncertain. Reads must represent it without requiring reconciliation to mutate the action first.

Correction: derive uncertain for stop + done physical chain + absent confirmed completion, preserving suppressed/success precedence and shared-owner chain identity. Cover the terminal/unconfirmed read case without a reconciliation call or persistence. This restores existing semantics; it does not add an engine state or broaden the product.

No other source findings were established. All three findings were reported promptly to root. Subsequent working-file remediations are excluded: this report evaluates the exact packet objects.

## Identity, method and scope

Verified `dev-session current` = `2026-10-30-oomd-abuse-policy`; both identity environment variables absent. Live same-session roster44 confirms reviewer0, thread `01a18d34-69d3-74d2-ae70-df2584ed8a12`, saved `gpt-6.1-sol/xhigh/read_only`, execution `full_access`. Independent, no source authorship, settings overrides, fallback or nested reviewers.

Applied installed mandatory-change-review and GENERAL, ARCHITECTURE/REPETITION, SCOPE/PROPORTIONALITY, RISK/COMPATIBILITY. Overall HIGH because of admin privacy/authority and public API/client composition. Read current packet, plan/state, design A/B/C/D, repository guidance and applicable API synchronization, localization/locked terminology, testing, KB and documentation procedures. React terminology is locked to `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`; its guide was inspected from that immutable Git source.

The implementation traces the actual approved outcome: admin Overview/Reports/History in PHP and React, all current matched pairs rather than only thresholds, plus the daily report. The shared projection and endpoint-local pagination have current consumers and avoid per-VPS fan-out or a shared paginator rewrite. Most cross-repository growth is generated output, API/gettext metadata, tests and the two visible interfaces. No speculative registry, snapshot service, transport fallback, enforcement change or new persistence subsystem was introduced. I found no additional architecture or proportionality finding; F3 is a concrete divergence at the SQL/read boundary, not a reason for a broad refactor.

## Exact reviewed ranges

Each range's complete commit series and final diff was inspected, not just its latest commit. All heads/trees matched and worktrees were initially clean. Backend working files subsequently received explicitly allocated disjoint fixes; immutable `74c0` remained the review source.

| Repository/worktree | Base | Head | Tree |
| --- | --- | --- | --- |
| vpsadmin | 4062a8da3314aa7b48170b0d6f441446bad9b207 | 74c0af3aef3ec9124ca89ce7669ccd9b99633495 | c2e2de2d3e3a63cc14f122f0f43641cb0898e569 |
| vpsadmin-go-client | 5934903568862a95b688479f0b13e11e4a36692f | 8708f170bd99522ac147fceadee9e7db6305c772 | 82bcef44a48c31e7692cc4af8434ba75b39cf755 |
| vpsadmin-rust-client | 15db0ffd95ccd34247de9f839c906d860afb1b69 | 2b49891cd22e08a945bff2cf4cff25b2b9903bf2 | b1430ae9a72645ad3c332674bcdca1c4b99a7de4 |
| vpsadmin-typescript-client | d8cb484748db8687554822772a98a1f873414d65 | aed11d01c0d1436293f45a1a4e83d88421375bc1 | 2b1fa2c5093d3c6cdbe36b71e499f2bb6f67831f |
| vpsadmin-typescript-client-development-artifacts | aed11d01c0d1436293f45a1a4e83d88421375bc1 | b619eb8324bfe80c7b225f698fb83efe97639c83 | 47cc9b5f663048638c6d7f267d157e77c37e217e |
| vpsadmin-webui | 4499f90fe11df0e4df6f23e5fa54829e2254ec1b | c27d70dbd4e96540de4d58027bfa6fce09a4df15 | 0e96635640b98aee93e2ef208909ad081ce9ca95 |
| vpsfree-notification-templates | 64665b3944da4ebf5045ef00f403e410ce88e3ad | 7af51cd6164fd5aad7633f39f6cf4e7ef64c18a7 | e1872cbc645947495160b0b6a13a56cb5b2689d4 |
| vpsfree-kb-contracts | c064b4fe87d66486c5eb8f43cb278a464d8574ab | 75a721e14e07ae86975089fbdbb58a686d490550 | e196f5fa12226ab9ba9b2377508b9e651a21b638 |

## Whole history, streams and migrations

The new purposes are PHP73cd + API74c0; Go8708; Rust2b498; TS generated18fb + candidate identityaed11; artifactb619; React SDK5c291 + UIc27d; daily7af51; KB75a721. Their supporting tests, translations and owning docs follow those purposes. No obsolete iteration/fixup or redundant repeated unmerged input stream remains in these reviewed ranges. Each client has one final generation stream, React one SDK selection, KB one final source alignment. TS release identity and immutable archive retention are independently reviewable purposes.

The registered artifact obligation is expressly included: whole-default `d8cb..b619` contains the same `18fb/aed11` TS prefix plus artifactb619. That prefix is not a second implementation or duplicate update stream. The archive commit must remain in delivery accounting; the old development0.4 artifacts and supported consumer identities remain unchanged.

Every new range has **no migrations**. Backend `api/db/schema.rb` and its migration inventory are unchanged. Consumed/merged migration `20261030180000_add_incident_escalation.rb` retains SHA256 `2eec970fb3620ad25f3ac01c06a9eae61af2d208f88184e995c74b8ad2ba2c1e`; obsolete20261115120000 is absent. No transitional migration, schema guards, persisted-format stream or rewritten integrated predecessor is introduced. Prior deployed/consumed histories retain their original identities; none establishes runtime success for these successors.

## Contracts and verification conclusions

API authorization is applied to both Index actions and their metadata, with member/support denial cases. Exposure uses normal live Resource references; History retains original IDs and nullable current names for deleted associations. No raw snapshots, private errors, selector bodies, recipients or mail bodies escape the projection. GETs do not evaluate selectors, reconcile or write. Counts use saved matches/current-owner epochs and cutoff detection windows. One SQL collection selects count/page/order facts together; paging occurs globally before presentation. New config capture and read enrichment do not change DailyReport's transaction/isolation/recipients.

Saved thresholds/decisions, current restrictions, mail-server acceptance and confirmed physical stops are separate. Native confirmed-stop identity is shared across policy rows. F3 qualifies the terminal-outcome coverage. PHP and React preserve existing Reports/member/per-VPS behavior; capability-gated development against older APIs is sound apart from F1. React uses actual generated operations, typed primitive/null output guards and endpoint-local URL/offset state, with no raw transport fallback.

Independent structural comparison finds only the two new schema resources; all prior resource entries and non-resource description fields are equal. Go/Rust raw inputs equal the TS/export schema SHA `7e2a529787c06944f1ad0cdf3369edd8b4650d79826f3bbda9101af2dfb67628`. Existing generated action/runtime files are preserved; root composition adds the new resources. Go's scalar-null ambiguity is explicitly retained/documented, Rust Option and TS nullable/partial references preserve their supported distinctions. Generated availability never grants server permission.

The artifact is independently hashed:348079 bytes, SHA256 `9cba02754bec157616c66207312f44312e9af36fe5deb05e8e68585615e17ca9`, matching candidate/sourceaed11 and archived schema. React lock changes only root selection and the SDK node; HaveAPI runtime remains0.32.0. KB lock changes only vpsadmin; other11 nodes/edges and explicit OS source remain. Its sole Backups radius-one fingerprint update is explained by the adjacent admin menu call, not changed member intent. Member semantic IDs/routes/pages/capture selectors are preserved; no new KB action instructions or annotation obligations arise.

Inspected recorded quick results and representative synthetic PHP EN desktop/CS narrow and daily HTML1280/390 screenshots. These prove fixture rendering, not actual capability discovery (F1), mail-client compatibility, deployed authorization or real delivery. Narrow daily tables use horizontal overflow; PHP retains the legacy wide-page behavior. React browser interactions/screens remain unexecuted. Existing failure receipts and overlapping test counts remain literal; no totals were fabricated.

## Documentation placement and preservation

All seven GENERAL questions were assessed:

1. Existing backend docs index, template root README/tests README, client README/development docs and React design handbook/work log provide appropriate entry points.
2. API/current-versus-saved/daily/recovery semantics belong in backend `docs/incident-escalation.md`; UI contracts in React API_CONTRACTS/WORKFLOWS/REQ-051; generation/nullability with client owners; command/publication receipts in session evidence. No per-release operational data was moved into configuration or KB product prose.
3. Current references describe supported behavior independently of this rollout; React dated work log appropriately records execution and pending gates.
4. Commands, example routes and capability claims must be corrected for F1/F2, and outcome derivation for F3. Otherwise inspected current/saved/cutoff/SMTP/shared-stop descriptions match the declared implementation; prepared, synthetic and deployed evidence stays distinct.
5. No documentation move loses prerequisites, partial-effect conditions, rollout ordering, data-safety or recovery limits.
6. Compatible backend/schema/readers and capability-gated staggered rollout remain explicit. Existing consumed schema and rollback constraints are preserved; no supported upgrade path is retired.
7. Owning explanations remain authoritative and locally discoverable. Historical0.5 provenance is pinned to4499 rather than relabelled0.6. Locked terminology, bilingual identifiers/placeholders, KB semantic tags and old artifact/source links are preserved. External destinations were not freshly queried.

No new product document bundle or member KB/media rewrite is needed for the bounded unchanged member contract. Documentation is well placed, with factual qualifications F1–F3 and the remaining evidence limits below.

## Remaining acceptance and release limits

- Correct F1–F3, run their focused owner checks and reconcile the final committed histories/consumer pins. Root can inspect narrow remediations under the skill; no automatic whole-review rerun is required unless the contract/design expands.
- Rust generated source has no completed compilation result in this packet. Formatting/provenance/deterministic generation does not establish that new async/blocking modules compile. Before calling that deliverable integration-ready, obtain successful exact-head compilation/test evidence, preferably the already-running ordinary CI matrices rather than a new local restoration campaign. Package/MSRV/docs remain separate unproved gates where required; real-server acceptance is also unrun. The stopped143 local probe is not a pass or waiver.
- React merge still requires a published compatible registry SDK and final manifest/lock/provenance/frontend hash adoption with temporary archive selection removed. Development artifact reproducibility does not satisfy that repository premerge rule.
- Planned narrow React desktop/mobile browser/interaction acceptance remains necessary for visual readiness. No frontend package/system/VM build or deployment was proved by this source review.
- Source/core/full focused checks use their recorded actual dependency environments and scopes. Original failed attempts, absent client full stdout, six WASI warnings and in-progress/queued CI snapshots remain qualified. No old runtime/CI success transfers to these heads.
- No policy-engine/physical StopOverQuota/ZFS, SMTP delivery, KB managed-runtime/media/strict/full-page/staging/production or live-demo success is established here. This report requests no broad runtime campaign.

I performed only read-only source/history/evidence inspection and wrote this requested report. No product test, Nix evaluation/build, browser execution, CI monitoring, source/ref/claim/default/publication/runtime/DB/deployment or lifecycle operation was launched. No active command or uncertain effect remains from review. Existing owners retain technical fixes; root owns acceptance and future authority. Reviewer capacity is returned.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)

