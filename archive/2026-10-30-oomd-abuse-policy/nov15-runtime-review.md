# Runtime incident policy — independent FINAL source review

Two findings in the frozen reviewed source; no additional Blocking, Important or Advisory findings identified. Both were promptly reported, accepted by lead and assigned to owner0. This report does not certify their successor fixes.

1. **RUNTIME-R1 — Blocking; architecture/repetition.** vpsadmin api/lib/vpsadmin/api/resources/incident_report.rb:64–80 and127–143, commit84b7e07da9abcb1c143b509eab2511c43b882ac2. The expanded member visibility predicate is independently copied into Index and Show, including registered-source epoch and notice action-epoch rules. A later privacy fix in only one copy can leave direct detail exposing a report excluded from listing/counts. This is newly expanded authorization duplication, which the architecture reference classifies Blocking. Smallest correction: one owning visibility relation/helper, used by Index/query/count and Show before their existing with_restricted authorization; retain administrator bypass and ordinary manual-history semantics. Focused source/notice Index/count/Show parity proves the intended boundary. Lead accepted and assigned the narrow extraction; no broader framework needed.

2. **RUNTIME-R2 — Important; general/coverage fidelity.** vpsadmin tests/suite/alerts/incident-escalation.nix:139–141, same84b7e07d. The retained physical scenario expects exactly3 administrator history reports. Its three ordinary events now also create a warning notice and a confirmed-stop notice. Both notices use codenameoomd and are intentionally returned to the administrator, so successful implemented behavior reaches5 reports, not3. Smallest correction: distinguish/assert3 ordinary reports and the expected warning/stop_completed notices, preserving transferred-owner empty history and both known-content sentinel assertions. Do not change production filtering or remove notices to satisfy the old assertion. Lead accepted and assigned this correction after the frozen R1 check. This is a source-proven failure case, not a claim that the new physical scenario was run.

## Review identity and scope

Retained reviewer0 / gpt-6.1-sol / xhigh / read_only; independent, no overrides/fallback/nested agents. Bound tracking-cwd current returned2026-10-30-oomd-abuse-policy; both environment markers absent, consistent with exact trusted developer binding. Live roster confirmed ready/review and thread01a18d34-69d3-74d2-ae70-df2584ed8a12. Read mandatory skill and all four lane references, current scope/design/plan and package packets, relevant workspace routing and local guidance. Read-only source, history, archive and existing evidence inspection; no tests/builds/CI/runtime/publication/lifecycle/source or Git mutation.

Frozen complete reviewed ranges, all under worktrees/2026-10-30-oomd-abuse-policy:
- vpsadmin:537b0b7c4ce1d8a930c5fd24b8f4317271ae4f02..1a0935b2f0ed0c31d00d645922b88396dbdb2c7c.
- vpsfree-cz-configuration:5c67e6a010462a850fb6258c486eeef4490c27d5..0be59e51d8473ca0b26b4a9cfe49ca3fe6818fcb.
- Go:af9a819ca35f6de5556092679b4df7cb72e7aa89..87745f1f54b8928620893c6b64cc1ef3a4f2b90a.
- Rust:823a4f8450fce4947310fc81bcdebdca91d9ffae..3f1b352785e5ccce3fd73f2a19102dbf72bb495c.
- TypeScript:2da950a98fa13468b36d03b13fb5e81cca206e0e..3b98b045684528d0c38cc2abfef012ebf75e3e5a; packed source05c443c43d22cbd67422f53414f022c3a9ac072b.
- Templates:2cfd218d9152888feea4109f064459078ea9f76e..6f95fc255d87d850b157935ac5d2f085a4390ac8.
- KB:cb7825245ea786fb0f51c469d1a7dc5c6a1ececc..5cfb702685810c45eca3bc7d44c579baaff1c83e.
- React:88ac13b89d6421c914cd57e18153de1fee6fc7b7..8ce6baac538061d5b51b84c09044947a22004435.

All assigned lanes completed against these immutable ranges. Later A working-tree remediation was excluded from this review.

## Distinct lane conclusions

**Scope/proportionality:** compared the user's configurable trusted-Ruby policy request and later approved history/mail/contributor/readability requirements with complete diffstats and delivered milestones. The large combined volume includes retained shared escalation, generated snapshots/output, UI/tests/catalogs and previously reviewed KB runtime repair. The current mechanisms have concrete consumers: one bounded trusted source adapter, value-only event callback, existing settings and action audit, five-slot evidence, existing incident views and generated SDKs. No speculative rule builder, second production source/action, policy store, dashboard, transport or read/retry execution is introduced. B's17-line policy and KB's screenshot-only copy are proportionate; retained schema/recovery and compatibility work are necessary safety constraints. No further subsystem or optional hardening project is required.

**General:** inspected the complete series/final changed paths and actual event→report→ordinary and aggregate mail consumers, API/null/filter contracts, PHP/React presentation, relevant regression source and native receipts. First-event localized text is stored under the locked owner after dedup; later reads/retries do not regenerate it. Runtime errors preserve source with a bounded diagnostic rather than choose permissive policy. Current unknown limits/status are not filled from historical evaluations; counts remain numeric/live. Notice kind and six mail states remain separate. R2 prevents treating the prepared physical test as ready without correction. Prior narrow source and UI reviews were reused only for unchanged behavior, not as certification of the runtime policy.

**Architecture/repetition:** backend DSL/engine owns qualification, counts, serialization, ceilings, cooldown and effects; configuration supplies only the trusted declaration/callback. The callback context contains deeply frozen captured values rather than models, and result validation is finite and explicit. Reads and action/mail recovery have no callback invocation. Existing action JSON owns immutable contributor and normalized policy facts, avoiding a second projection/store. Specific-definition absence alone selects generic mail; preference, translation, rendering and sending failures do not. SDK/provider and React adapter responsibilities remain separate. R1 is the required exception: authorization must have one owner. No other current-scope shared abstraction or extraction is required.

**Risk/compatibility:** inspected owner/epoch and source qualification, pending versus dispatched effects, error/suppression paths, contributor slots/links, trigger deletion and schema/API readers. Deterministic rechecks cannot promote the saved action; digest mismatch suppresses undispatched work while queued/uncertain effects retain identity. Saved action policy supports confirmed-stop recovery after trigger deletion without inventing historical base limits or calling Ruby. Missing pending source suppresses. Generated notices are excluded from qualification/counts, ordinary Result/chain processing and ordinary pending sender. Ordinary New's nullable chain/processed acknowledgment and per-mail savepoint behavior remain; ordinary mail preparation does not precede stop preparation. Mail state derives from the SMTP transaction and does not prove inbox delivery. Contributor selection is bounded, deterministic, immutable across retries, preserves unavailable slots without replacement, and removes unauthorized descriptions/times/links. URLs use the configured HTTP(S) WebUI base and existing authenticated routes with no credentials. Same-owner/epoch checks remain authoritative, subject to R1's duplication correction.

Any site Ruby file deliberately changes current threshold/status outputs to null, including constant/observe callbacks. This is not universal backward compatibility. PHP and React handle unknown values, dated none/recorded/error history and permission ceilings separately. Retained and regenerated Go scalar outputs still collapse null to0/empty; the documented unsupported dynamic interpretation is an accepted boundary, not fixed by this generation. Required readers must preserve unknown or stop interpreting those fields before Ruby activation. Null-preserving Rust/TS consumers and capability checks do not establish deployment or permissions. Rollback requires compatible nullable-setting/notice-aware code, retained audit/schema and reconciliation; arbitrary older binaries are unsafe.

B's actual shared API/supervisor configDirectory and generic child-symlink transport carry the file; task processes use API configuration. There is no activated configuration claim. The initial callback matches builtin behavior in supported modes, with existing audited overrides and mode/exemption ceilings preserved.

## SDK, pin and fixture checks

Independently matched all three committed raw schema/provenance/tooling-lock hashes:
efff42fbd937ae5c6cc8c0f75c19cf28cc3f95382576cfd175f48e74e1ef97b7 /
619ebab3710b19c56619ecdaf04f2ea6cdb046498f51257cf89b1351c48da4e6 /
2e9a124eff7b80d6fd57cd0f03cb2809847c67cc7f1af6364911c3622d7242a0.
Inspected representative generated selectors, nullable inputs/outputs and handwritten wire/consumer tests. The provider remains responsible for primitive validation and server choice refusal. Go's bounded OAuth projection remains explicit; generator1ef9b204/runtime ownership are retained, with no emitter expansion. Rust688 and TS677 generated-file manifest hashes match actual files. The copied Rust runtime is unchanged in this branch.

TS archive341951B SHA25624cf8549246e5beb14652639b911768041e3bd38197fa2a7ac7dbaee8604cb43 and npm SHA512 integrity independently match React manifest, lock and provenance. All1364 installed SDK archive entries match; no symlink/traversal entries. Runtimehaveapi-client0.32.0 remains unchanged. This supports development only; a published registry SDK with matching final manifest/lock/provenance remains mandatory before React merge.

KB's five pins agree on A1a0935. Independently compared the full lock graph: only the vpsadmin node changes; every other node/edge, including OS6bdf458f, is retained. The screenshot fixture bytes equal B exactly; the topology-specific module shares them across API/supervisor/database setup, while generic topologies retain absent-file fallback. The fixture is not proof that a running service loaded it. No fingerprint/media/scenario changes or fresh screenshot certification occur here.

## Complete history and migration conclusions

Independent full-series and final-diff inventories support these dispositions:
- A: four coherent purposes84b7e07d backend/runtime/schema/mail,8a907832 ordinary localization,38cb2f2c PHP/catalogs,1a0935b2 independent MariaDB documentation. Superseded static/runtime fixes are folded into owning changes. No authored dependency/channel/pin stream or obsolete transitional implementation remains. The findings above do not change that original history assessment.
- B: one two-path feature commit0be59e51, no obsolete or repeated input stream; no migrations.
- Go: one generated-input/output commit56aa960c plus handwritten tests/docs87745f1f. One final generation stream, no obsolete schema/pin or migrations.
- Rust: generated2c5d7474 plus handwritten3f1b3527. One final generation stream, no obsolete runtime/output iteration or migrations.
- TS: generated6d5a7f35, handwritten/source05c443c4, artifact delivery3b98b045. The third commit adds only the final archive/provenance outside the npm whitelist; the source/delivery split serves the actual immutable HTTPS consumer. No obsolete archive stream in final history; consumed prior refs/evidence remain separate. No migrations.
- Templates: one final coherent6f95fc25, with earlier README/contributor/nil-time iterations folded. Flake/pins unchanged, no repeated stream or migrations.
- KB:91d349c8 runtime repair,9e0dcff9 sole final backend pin,5cfb7026 screenshot fixture/docs/check registration. Runtime paths independently compare byte-identical to accepted edf5c326; earlier tracker/K1/ack-loss review limits remain. One consolidated pin stream, no fixup/transitional format history or migrations. Existing schema1/2 and incomplete-run recovery contracts remain untouched.
- React:ee9f1036 single final SDK selection,628476b3 app/tests/catalogs/owning docs,8ce6baac historical evidence/media. No obsolete SDK selection or fixup stream, no migrations. Four retained PNGs remain historical fixtures, not current runtime proof.

A migrations in order: exact base predecessor20261006120000; original20261030180000 AddIncidentEscalation, SHA f1e6bc75aeffb14d2d14676a908fc4332d7f42f79ee29fe54f48def8e2756c7a; additive20261115120000 AddIncidentPolicyEvaluations, SHA b9d894772f61c65dd40952db0eacc04783cbc940144377f1a783d34b2a4a441c. Independently checked original bytes equal retained7919441 and final core schema matches the additive fields/indexes. No existence guards, destructive conversion, invented evaluation backfill or guessed override reset. Known disposable/export/source/client consumption does not prove external durable schema consumption. That remains unestablished; retaining the original unchanged plus additive successor is a justified conservative lineage, not evidence of production use or proof the predecessor was never applied. Feature publication is distinct from merge/release/deployment. No obsolete migration whose sole purpose is upgrading an abandoned rewritten schema was identified.

The separate diagnostic branch remains retained experiment/evidence; it is outside product integration and was neither reopened nor re-certified.

## Documentation placement and preservation — seven questions

1. Entry points: API docs/README links docs/incident-escalation.md; configuration's existing API README links the owning reference; client README/development guides and React handbook/work-log entry points reach their respective contracts. Template README retains its repeated-incident anchor and concise owning-reference pointer. KB cluster README reaches runtime contract and capture setup.
2. Audience/home: backend policy/ownership/mail/upgrade facts stay in the API reference; site distribution/editing in configuration; wire/null/SDK and UI behavior in consumer guides; capture setup in KB; exact run/hash/failure evidence in session records or the permitted React dated work log.
3. Lifetime: reusable explanations remain understandable independently of rollout status. Temporary SDK provenance is clearly the currently selected development input, with a distinct registry-merge prerequisite; execution receipts do not become product instructions.
4. Fidelity: documented unknown-current versus historical facts, settings precedence, actual rendered-language labels/timezones, SMTP limits, pending/dispatched recovery and exact development SDK input agree with source. Scoped quicks are not labeled full integration/browser/runtime success; R2 identifies the stale prepared test expectation.
5. Preservation: compared moved repeated-incident README facts with the owning backend section. Specific/generic selection, suppression/failure no-fallback, rendered-language label, original count/time, notice-time deterministic settings, confirmed autostart consequence/manual start, separate individual notifications and required backend/template pairing survive. No recovery prerequisite was discarded.
6. Upgrade/rollback: additive schemas, preserved non-null overrides, restart/config-identity consistency, reader-first any-Ruby activation, Go scalar limitation and retained-schema/compatible-code rollback are explicit. Dispatched effects cannot be recalled; completed stops are not undone. KB old incomplete runs retain their owning source/claims; no conversion or retirement is inferred.
7. Authority/meaning: backend owns engine/template interface; consumers link and explain their own representation. Protected EN/CS meanings, footer/greetings/advice/links and semantic IDs are retained. The local incident-article additions describe behavior rather than instructing a WebUI action; manual enumeration found no newly introduced imperative requiring a navigation annotation. Original article commands and links remain. All-page source/release inventory and revision proof remain pending rather than inferred from body-only fetches.

No additional documentation placement/preservation correction is required beyond fixing R2's source/evidence mismatch.

## Evidence limits and disposition

Read retained native results rather than running checks. A's136 application examples,14 DB-free exporter examples,2 migration examples, separate2 deletion and2 site controls are successful for their actual scopes; they are not one invented aggregate. Earlier20/1 mail batch and repaired/remaining controls remain distinct. B loader/finalizer equivalence is not DB/bootstrap/fleet proof. C regeneration/package/wire controls are not live API or full Rust matrix/MSRV/package acceptance. E's107 focused tests/types/docs/prefetch/source proof do not establish a final frontend/BFF build or real browser/backend behavior. Template renders/checker and actual producer controls are distinct. KB projections/allow-missing and retained media do not prove current loaded policy, new captures, visual acceptance or strict final-media Check.

Original full-topic CI failures, isolated nonreproduction and primary-scenario uncertainty remain as recorded; this review does not turn them green or settle native effects. Old runtime/claim and immutable INCOMPLETE evidence are unchanged.

Complete original-range review is finished. R1 must be fixed before long integration; R2 must be corrected or explicitly dispositioned before relying on that scenario. Lead's step9 direct narrow-remediation inspection/checks can close both within the reviewed contract, without a confirmation-only reviewer round. No other required source change was identified. Corrected exact-head hosted/runtime/browser and KB capture/strict gates remain subsequent work. No deployment, merge, registry release, KB production write or lifecycle authority is supplied.

Lead preserves this read-only report as nov15-runtime-review.md. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/

---

## Lead receipt and remediation tracking

Exact reviewer report retained from native message `7cdcf6c4-7af7-490c-85fa-8804ed01f85e`;
reviewer authored no files. Original reviewed ranges and findings above are immutable
evidence; the following records lead-owned remediation, not a second review.

## RUNTIME-R1 — Blocking, architecture and repetition

At frozen A `84b7e07d` / final head `1a0935b2`,
`api/lib/vpsadmin/api/resources/incident_report.rb:64–80` and `127–143` duplicate
the expanded member epoch/notice authorization predicate in Index and Show.
A future privacy correction to one copy could leave listing and direct access
inconsistent. The reviewer classifies this newly expanded authorization
duplication as Blocking under the architecture lane.

Requested correction: one owning IncidentReport visibility relation/helper,
used by Index/query/count and Show with existing restricted authorization.
Preserve admin bypass, ordinary manual history and both registered-source and
linked-notice action epoch rules. Keep/extend API parity examples for the same
old-epoch source and notice across listing/count/detail.

Lead inspected both copies and accepted the finding. Implementer0 owns the
bounded correction under `c6d60cd5-5ccd-4c8f-9a11-fe1a0ff9c8ba`, including scoped
lint/tests, normal-hook commit and exact old-to-new evidence. No public contract
change or framework expansion is intended. The reviewer continues against the
frozen original range; root directly verifies this narrow remediation under
mandatory-review step9. Publication/export/downstream input refresh waits the
remaining review findings, avoiding intermediate streams.

Status: source/spec correction prepared in three files, complete diff SHA256
`03c5611230e7ded8cc6a84f88bc8b8ec05d7c0ace485f5b35aa4071bbe3fdea8` on A1a0935.
Lead inspected the moved unchanged predicate, preserved restricted authorization
and parity assertions. Scoped three-file RuboCop and whitespace pass. Sole fresh
watcher `5dd5b2ad-76b4-4a13-8792-e1f2c090c580` runs the two existing API examples,
seed50834, via `nov15-runtime-r1-command.sh` (SHA256 `5bdc68123971c693677724ed3b5821dd920c73ed6a902decc3ef414b503499c8`).
Installed Luna/low/full-access policy and native thread
`01a1e11f-c1c3-7a52-bce5-1443aa23b511` verified. Exact command completed with
native94303 exit0 in176 seconds; both examples passed, zero failures/pending.
No operation-owned work remains. Source correction is verified; final committed
identity and narrow successor inspection are pending.

## RUNTIME-R2 — Important, general and coverage fidelity

Frozen A `84b7e07d`, `tests/suite/alerts/incident-escalation.nix:139–141`, still
expects exactly three administrator history reports for codename oomd. The
scenario now creates three ordinary source reports plus a warning and a
confirmed-stop notice, all included by admin Index. The stale assertion cannot
validate the implemented five-record history.

Lead inspected the assertion and accepted the finding. Under `79aa1230`, owner0
will correct the existing final assertion to distinguish the three ordinary
reports and both notice kinds, preserving the transferred-owner empty history
and data sentinel checks. Product API behavior remains unchanged. Source edit
follows the R1 check's terminal outcome to preserve its frozen input. Appropriate
Nix/script source checks precede normal commits; no physical integration run is
claimed or released before review. This is a direct narrow step9 remediation.

Status: exactly four Ruby assertion lines replace the stale size assertion;
ordinary count3 and exact warning/stop_completed kinds imply the intended total5.
Trigger IDs must belong to the ordinary rows. Lead compared the actual trigger
accessor and original-owner scenario context; new-owner empty history and both
data sentinels remain unchanged. Combined correction diff SHA256
`1316da3fd2e3bee60c57133232b48c44163f790de3e357495a0161ef3f78802e` is inspected
under step9. Nix parse/format and extracted local Ruby body syntax pass; the
syntax check substitutes only two unchanged Nix email JSON interpolations and
does not recheck imported common code. No physical scenario pass is claimed.
Normal-hook consolidation and final committed tree proof remain pending.

## Lead closure of RUNTIME-R1 and RUNTIME-R2

Both findings are closed under mandatory-review step9 at corrected clean A
`1ada4b072229cb332492478cf754e0dd926d42fa`, tree
`728a2740516e95e87cc71b492b74f57848216403`. Root independently reconstructed
the reviewed-to-final diff SHA256 `1316da3fd2e3bee60c57133232b48c44163f790de3e357495a0161ef3f78802e`
and the three-file R1 diff SHA256 `03c5611230e7ded8cc6a84f88bc8b8ec05d7c0ace485f5b35aa4071bbe3fdea8`.
They match the inspected correction and actually tested source exactly.
The final tree equals normal-hook snapshot `c5fabff95e93871f0ca0be5cae3936aeafb8762d`.
Only the owning API purpose changes; the other three commits are patch-equal.
Migration/schema/tooling inputs are unchanged. Full receipt and corrected range:
`nov15-runtime-remediation-final.json`, `nov15-runtime-corrected-final-branch.diff`.

This closes source findings, not remaining physical integration/browser/capture
gaps. No new design, public contract or behavior outside the reviewed correction
was introduced, so no confirmation-only review rerun is required. Fresh final
export e522d266 binds corrected source and will determine the necessary client
freshness evidence; original export/review artifacts remain intact.


## 2026-11-16 affected fixture-lease review — cb8c214d

Retained reviewer0 (gpt-6.1-sol/xhigh/read_only, thread
01a18d34-69d3-74d2-ae70-df2584ed8a12) completed assignment7b55b20d,
turn01a1e4fc-c6c0-7593-944e-a5170c1ac718. No overrides, fallback or nested
reviewers. General, architecture/repetition and scope/proportionality lanes
found no Blocking, Important or Advisory findings. Root accepts source clearance
for original-context validation, not hosted CI success or final readiness.

Exact range15ed330232aeeaff70738f546b317870abf54011..cb8c214dba62731c93dafb102072444bcc77cc4e,
tree d9234850e0ccbefc20e3b205af359e10ae2c3d03. Two test files/128additions;
delta SHA978e324b0f66222e7e9d04dba2099edb3801804426328f2b813634b1b4168b4a,
full537b..cb8 diff SHA1bec3f708a49fb0d2a81b007b7003aa8cdfeca0d01611415e6a82910c2ab4fcd.
Reviewer independently verified receiptfbd76b52/all34artifacts and tested blobs.

The fixture guard retains only the captured connection on its owning example
thread while its transaction is open. Other releases delegate; query-cache and
other-pool cleanup still execute. Reviewer inspected actual HaveAPI0.32.2,
AR8.1.4.1 and RSpec3.13.7/Mocks3.13.8 lifetime/teardown: partial doubles restore
before outer rollback, which stays with AR/spec_helper. No transaction commit,
sharing or replacement is introduced. Existing no_transaction/concurrency users
retain real committed/request-release behavior. Four real HTTP/connection controls
are proportionate; no additional fixture framework or product fix is needed.
Original-helper3/2failure and candidate4/0pass evidence were read independently.

Full series/history conclusion: the inherited app_helper/spec_helper were unchanged
from537b through15ed. cb8 fixes a distinct shared-test-infrastructure defect and is
independently reviewable/revertible, so retaining it separately is justified.
Root adopts that conclusion; no API-purpose fold or head rewrite is needed.
No obsolete implementation, repeated pin/generated/dependency stream or transitional
compatibility path is added. Five purposes remain API/runtime, localization, PHP,
MariaDB docs and fixture lifetime. Prior whole-branch conclusions stand for unchanged
bytes. Both original20261030180000 and additive20261115120000 migrations, core schema,
flake/Gemfile/lock inputs equal15ed; no new migration. Conservative durable-consumption
provenance is unchanged and unestablished. No new export/SDK scope follows from the
test-only delta; earlier actual API/consumer obligations remain.

Documentation conclusion: the adjacent helper comment and regression spec are
sufficient durable explanation for maintainers. Existing diagnosis.md/receipt own
execution evidence; no product reference/README change or recovery-path retirement
is needed. No placement or preservation finding.

Residual limits: originalCI43873056467 remainsFAILED; isolated2pass and ordered39
failure are distinct. Exact historical preceding-connection chronology is unproved;
original full-role453/487 not yet validated oncb8. Local Ruby3.4.9/MariaDB11.4 differ
fromCI3.4.12/11.8.6. Actual15edSMTP/Nix evidence is not relabeled successor proof.
Root subsequently registered sole40-example validationb723de0e; its outcome is
recorded in state.md when available. No merge/deployment/publication/pin/lifecycle
permission is conveyed by this review.


## 2026-11-16 narrow localization fixture correction — 024ab881

Root accepts the sole `cb8c214d..024ab881` correction under mandatory-review
step 9. It initializes real `Vps` column accessors inside the existing fixture
before constructing the unchanged strict instance double. All five original
locale, restoration and thread assertions are byte-identical. No production,
authorization, persistence, dependency or test-selection behavior changes, and
no new design or public contract requires another affected reviewer turn.
The inline comment explains the cold-accessor invariant at its owning fixture.

Root independently verified receipt `nov16-api43911462363-attempt1/final-receipt.json`
SHA256 `d70b144163e9226f38de82213f1bf9dc8c5ec7b4927d7fcb0a51dd358a9617aa`
and all 64 artifact hashes. The controlled baseline reproduces exactly the five
CI example IDs; the corrected native JSON passes those five and two interface
controls, 7/0/0 with no outside errors, in 15.841389942 seconds. Unknown methods
remain rejected. Local Ruby, MariaDB and connection_pool differences remain
explicit; this is actual-interface evidence, not whole-environment equivalence.
Both failed CI modes retain their original results.

Final clean head `024ab881be181fad839751de9efe60a44fecbe39`, tree
`dbfbe6b5313150ca5a1135f295e36e4f2d4ed1a5`, exactly equals normally hooked tested
pre-consolidation `1c2cfe4b23bf69be36b787a01250772fc524be05`. Root verified the
one-file delta SHA256 `9585b1d90854ac9d2314a40713fbafb579499adbc2760734bc8ed603b7d2f121`
and full historical-base diff SHA256
`1724744c81a1ed22df39096832aa5ed3071c41a1526a2feb4ee429d225b35987`.
Complete range-diff retains five purposes: only localization changes; four
other patches are byte-equal, including the separate fixture-lease correction.
All 41 preservation refs resolve correctly. Migration/schema/dependency bytes
remain equal, retaining the independent prior lineage conclusion and its unknown
production-consumption limit. No obsolete sixth fixup remains in the final series.

Prior independent review remains accepted for unchanged scope. This disposition
does not relabel old SMTP/Nix outputs as successor evidence or claim hosted
success on 024ab881. Feature publication is released under35104973 with fresh
canonical default25b and exact old-featurecb8 lease guards; default integration
remains unauthorized and unready. Owner3 continuation92a357b5 depends on actual
canonical successor readback before changing its sole pin.
