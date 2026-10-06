# Retained-selection and stopped DNS recovery review

## Assignment and requested outcome

Review the completed, committed provider deliverable in all four HIGH-risk
lanes: general, architecture/repetition, scope/proportionality, and
risk/compatibility. The change controls retained guest boot selections,
persisted state, recovery, deployment ordering and rollback. Retained reviewer0
is independent, ready/review/read_only, with saved gpt-6.1-sol/xhigh settings.
Use those settings without overrides and perform the review directly.

Read the canonical mandatory-change-review skill and all four lane references,
the applicable workspace/provider guidance, [plan](plan.md), [state](state.md),
the current [design brief](design.md#provider-correction-brief-retained-selections-and-stopped-dns-recovery),
and the individual [retained rollout](storage-profile-rollout.md). Verify the
exact session from the literal tracking CWD before accessing its records.

The outcome is a provider that distinguishes a full build candidate from
successfully applied guest selections and can repair the demonstrated DNS-only
residency gap while stopped, preserving copied services, actual Nodes, disks,
the original copy ledger and pending hold. Inspect implementation, consumers,
failure ordering, docs, coverage and complete history. Report findings and an
explicit history/state-format/migration conclusion; do not assume clearance.

Session `2026-09-23-storage-redesign`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. No tests/builds/network/private evidence
reads, edits, ref/index writes or runtime actions are assigned to the reviewer.
No nested reviewer or subagent. Public committed source/Git/records suffice.

## Original independently reviewed branch

Provider worktree:
`worktrees/2026-09-23-storage-redesign/vpsfree-dev-workspace-storage-profile`.

- Actual fetched base/default: `e1bb5cf3ad37c5ef31445a68ab85f53db2858777`.
- Final HEAD: `bcc0532255e58749d2b41bb500c820d672b142df`.
- Tree: `e727da779c31b72a65f819af290cf3844b113f83`.
- Complete range: two commits, 11 paths, 2094 insertions/76 deletions.
- Full binary/full-index final diff SHA256:
  `0937d791946bfcf6a0d92e9a7e34022c5b108307cc5e8da7952193bc6ed85f7f`.
- [Complete final diff](storage-profile-retained-selection-reviewed-bcc-final.diff) and
  [inventory with source hashes](storage-profile-retained-selection-reviewed-bcc-inventory.json).
- Tracked/index/untracked state is clean. Normal commit hooks were not bypassed;
  this repository declares no hook framework or custom hooks path.

Complete commits, oldest first:

| Commit | Purpose and disposition |
| --- | --- |
| `cd81e83f91a552eb0138e58cb76312784a2988df` | Previously reviewed admission observations, fresh payload routing and supporting real-AR regressions. Published and consumed by the selected host package and copied services closure; retain this independently reviewable owner. |
| `bcc0532255e58749d2b41bb500c820d672b142df` | Candidate/applied bookkeeping and provenance-bound recovery, with owning tests/docs and the added DNS assertion in the existing native scenario. New and not deployed. |

Upstream already contains the original policy, maintenance, profile and native
commits. They were not replayed or duplicated here. The earlier admission
correction was reduced to its exact residual four-path patch on the current
base; its earlier [review](storage-profile-admission-review.md) remains evidence.
The new correction addresses the producer bookkeeping defect and its held-state
recovery together: both use the same applied selection, provenance and full
boot-before-release contract. Supporting unit/native tests and README stay with
that owner. No fixup, repeated input stream or abandoned alternate mechanism is
present in the inventoried series. Independently assess that conclusion and
the interaction with the already consumed admission commit.

## Demonstrated failure and design boundaries

Targeted update published a full freshly built result-config before copying
and activating only the requested guest. The selected DNS descriptors could
therefore change without their closures becoming resident. OSVM preserves
existing NixOS disks but direct-boots the selected toplevel's init. A subsequent
services-only maintenance copy faithfully retained those unproved DNS choices.

The retained trial failed copied-start at DNS readiness, exit1/985.14s/parity0.
The runner shut down its guests; the hold remains starting_copied. The lead's
earlier comparison proved actual Node selections but omitted DNS residency.
Desired descriptor equality was insufficient. The cause of an earlier runner
loss remains unknown. Private boot/operation artifacts are evidence references,
not assigned reviewer inputs; do not infer payload loss or historical inode
continuity from them.

The saved brief accepts these bounded contracts:

1. Existing result-config is a build candidate. One private applied-config.json
   envelope records retained descriptors, source/proof references and one
   nullable in-flight operation. Publish pending before effects; promote only
   the target after actual exact current-system/closure/root proof. Services
   finishes its existing restart/Node refresh first. Untouched legacy guests
   remain unknown; no build, stale ready file or timeout supplies their proof.
2. Ordinary cold boot requires a complete non-pending applied selection. A
   freshly built candidate checks requested routing/layout without advancing
   retained payloads. NixOS may vary only toplevel/kernel/initrd/rootDisk.image;
   direct vpsAdminOS may vary only toplevel/kernel/initrd/squashfs. All retained
   layout/resources/network/mount fields remain exact.
3. Public maintenance-recover-config SLUG --residency-evidence PATH is
   metadata-only under the existing lifecycle lock and stopped checks. It
   accepts only copied/starting_copied with a completed services copy, restores
   configured NixOS DNS descriptors from one prior successful full boot and
   keeps services and every Node descriptor completely equal to their proof.
4. Recovery preserves exact predecessor bytes/digest, original config roots
   and evidence in private immutable history. It derives/roots the new next
   itself, publishes the v2 hold last, and validates the derivation on retries.
   Same evidence is idempotent; changed evidence refuses. Phase/copy bindings
   and pending state remain intact; no old masked boot after recovery.
5. Historical continuity is trusted operator evidence from original retained
   paths/sizes/mtimes, cold copies and actual successful boot/update/copy source
   records, with no known contradictory replacement/reset/restore/truncation.
   Historical device/inode is unmeasured and not backfilled. Current stopped
   dev/inode/size bind this attempt and are rechecked under lock/before boot.
6. Full copied boot, seed/API/Supervisor readiness, normal Node refresh and
   every exact guest selection/closure proof precede applied completion and
   hold release. Recovery alone supplies only a boot-eligible selection.

No operator-composed runtime JSON, whole-old rollback, old services boot after
new seed, force/reset/import, private helper, record surgery, early release,
new phase, OSVM/generic recovery engine, or automatic unknown-state inference.
The trusted local-operator boundary in provider AGENTS remains applicable;
ordinary ownership/path/serialization and guest boundaries still matter.

## Formats, migrations, inputs and consumers

There are **no database migrations** in this provider range. There is an
intentional persisted-format evolution: maintenance record1 remains readable;
explicit supported transitions write record2, which can reference its exact
immutable predecessor and recovery. Applied envelope is version1. Masks,
preserving seed and residency/recovery evidence remain version1; canonical
runtime remains schema1/policy3. Old v1 helpers/adoption reject v2, including
released records. Universal old-provider fencing for other clusters carrying
only applied metadata is not provided. Supported rollback requires a reviewed
reader preserving the applied-selection contract. Assess these limits explicitly.

Companion Admin is exact `290f1ef07972e53c2b5154dbfa8b088802bde619` in
`worktrees/2026-09-23-storage-redesign/vpsadmin`, tracked/index clean with the
documented preexisting PHPUnit cache. Its two additive, published and
disposable/retained-consumed migrations remain unchanged and outside this
provider change:

- 20260924210000 foundation, blob `7d929052f314d5a821b2ce65345680c0740b1b0c`.
- 20260926100000 capture indexes, blob `d60868e615024c70fb4b87b736a2466ceb8349db`.
- Core schema blob `e9aa952df7b94451c5491c965d22962265c8f545`.

At the original bcc review, both provider flakes were byte-identical to e1bb.
The direct rooting fix adds pkgs.nix and the new test invocation to flake.nix;
input declarations, flake.lock and all dependency nodes/follows remain unchanged. Generic6a972b9/Codex32775,
default disabled API5c76/OS158 and every other dependency/follow remain unchanged.
Enabled checks use explicit same-session Admin290f; no default enabled profile
or production compatibility claim. No API/OSVM/Node wire/schema change is added.

Owning interfaces/consumers to inspect: provider bin/devcluster public commands,
maintenance.rb validator/state writer, shared runtime.sh lifecycle/GC-root
wrappers, devcluster_runner.rb construction/boot boundary, OSVM retained-disk
and direct-boot interface, test.nix's immutable guest script packaging, and the
root mkPackage composition. Canonical runtime policy stays with generic, not a
new provider copy. Existing provider transition-adopt must preserve/refuse this
state appropriately. README is the lasting feature/recovery/rollback home;
the lead applied its final prose pass. Individual trial results remain here and
in the rollout record.

## Original quick verification

Final eight source hashes are in the inventory. Fresh Luna/low watcher ran
four stages against frozen cd81-plus-correction bytes, then the normal commit
preserved every tested byte. Overall exit0/1259.483s/parity1, no remaining
operation or reported unexpected kernel build:

| Stage | Result |
| --- | --- |
| Pinned nix shell Ruby maintenance/commands/runner tests | Exit0/465.321s; 28 runs/222 assertions, 37/426, 13/35; all zero failures/errors/skips. Total78/683. |
| Existing nix flake check --print-build-logs --no-write-lock-file | Exit0/687.491s. Logs contain repeated upstream Minitest summaries and existing skips; no deduplicated aggregate is claimed. |
| Actual API290f candidate config drvPath evaluation | Exit0/54.039s. |
| Actual API290f resident config drvPath evaluation | Exit0/52.037s. |

Bash/Ruby/Nix syntax, Nix formatting and diff checks passed. The runner unit
suite prints its deliberately stuck graceful-shutdown fixture diagnostic while
passing; that is not a real guest operation. Prior admission47/0 and Node634/0
plus remote-restore4/4 are retained scoped evidence; they were not rerun here.
No new native guest has run. The whole-flake Admin overlays.list baseline
limitation and the separate unresolved API request500s remain recorded.

## Native and deployment gates after review

After findings are handled, run only the owning existing retained-services
native example, now with one DNS root. Real old full boot proves old DNS,
payload and absence of its distinct new candidate closure. The fixture seals
a separate synthetic legacy selection containing new/un-copied DNS before
prepare/masked boot; the combined config is never claimed booted. Stop/reap
precedes recovery. Assert the bad next changes only DNS back to old while new
copied services/ledger/pending phase remain exact, then retain forced seed
interruption, boot identity, protected SQL/sentinel and disk/payload checks.
This proves services plus one DNS only, starting_copied/released0. Six-machine
unit cases own exact Node preservation. No unrelated VM matrix or canonical
host-migration rerun is requested.

Then feature publication, generated root provider pin, applicable composition
checks, existing root/default package proof and actual packaged helper/contract
bytes precede external idle activation. The active lead cannot run a switch
that quiesces this session. Selected s7y4/q49 lacks this new command; existing
copied kyryi8 services already contains the corrected admission guest scripts.
Worktree/source edits cannot change selected host tools. No default integration
is authorized by review or the continuing storage trial.

After verified activation: recheck stopped ownership/evidence/disks; public
metadata recovery; existing copied-start/full seed/refresh/release; actual
guest-script and protected original DB/file/quota comparisons; only then the
previously approved provision/payload/history/rotation/automatic/repeat and
retirement/re-enrollment sequence. No public recovery/provision acceptance,
physical quiet, production strict, repair or APPLY is established by these
quick checks. Do not await CI.

## Completed review and finding disposition

Retained reviewer0 completed report
`ef116da3-cd14-4ca3-a7b4-9a612d229cc0` against the exact range and tree above,
using saved gpt-6.1-sol/xhigh/read_only settings. All four HIGH-risk lanes were
covered. No Blocking finding; one Important and one Advisory. Public source,
Git objects and coordination records only were inspected; no reviewer tests,
Nix, private runtime reads or operations were performed.

**Important, architecture/risk: host boot payload retention.**
`bin/devcluster:1684–1688,1704,1728–1733` roots config JSON. A raw
`nix-store --add` object does not register the store paths named inside its JSON.
An earlier raw maintenance-next object is a supported prior-boot source, so
moving candidate/result roots can leave old DNS boot files unretained on the
host. Guest GC roots protect only the guest store. A parent read-only reference
query of the actual prior JSON returned exit0 and empty references. The finding was open at that checkpoint. Its direct remediation and disposition
are recorded below; the original review itself was not rerun.

**Advisory, scope/lifetime: cumulative roots.** Digest-named roots accumulate
for distinct update/build configs; existing stop cleanup does not reconcile
these against current provenance or history. The lead accepts the retention cost, now documented in the owning README. No automatic pruning or removal of pending/history roots is
authorized in this correction.

Other lane conclusions preserve the candidate/applied ownership, pending-before-
effects and per-target promotion, fixed stopped DNS recovery, exact Node/services
selection, immutable predecessor and hold-last publication. The fixture correctly
distinguishes genuine prior boot from its synthetic never-booted legacy selection.
The complete two-commit history is coherent with no obsolete implementation or
fixup stream. There are no provider SQL migrations; maintenance1→2 and new applied1
are intentional persisted-format evolution. The companion Admin migration and
schema blobs match the packet and their earlier consumption remains unchanged.
Existing pins/defaults and prior scoped proof are preserved, without a new VM,
public recovery or populated-cluster acceptance claim.

The requested narrow rooting fix is subject to focused lead inspection/checks
under mandatory review step9. If implementation changes the public contract or
recovery ownership, only affected step10 lanes will be reassigned.

## Direct review remediation and final committed branch, 2026-10-05

The lead resolved Important finding1 under mandatory review step9 with focused
inspection and actual checks. No reviewer rerun was requested: explicit
per-item roots correct the reported lifetime omission within the reviewed
selection/recovery boundary. Canonical policy, private versions, public recovery
interface and guest release proof are unchanged. The cumulative-root Advisory
is accepted and documented; no pruning was added.

The shared registrar validates existing non-derivation items, creates an
indirect root and requires the exact root symlink plus a successful Nix query
containing `ROOT -> ITEM`. Payload projection and per-item JSON identities are
shared by public commands and the native fixture. Rooting precedes effects and
copy/applied/v2 publication; failure retains pending/predecessor state. Recovery
roots corrected selections, while historical JSON remains separate evidence;
an identical retry rechecks roots. Distinct source items containing equal JSON
bytes keep distinct roots. Existing legacy roots remain untouched.

Earlier command assertion failures, private-store cleanup errors and query
format errors remain in state/design history. The final fresh watcher passed
all four stages in 1092.449s, parity1, with no kernel build or remaining handle:

| Stage | Result |
| --- | --- |
| Actual-Nix private store regression | 0/27.022s; 6 runs/141 assertions, no failures/errors/skips. |
| Full existing provider flake check | 0/956.702s; affected complete files: maintenance31/236, commands42/478, runner13/35, store6/141, all passing. Existing upstream skips/repeated summaries are not combined into a deduplicated total. Git identity diagnostics occurred before the final passing status. |
| Exact Admin290f candidate eval | 0/54.039s. |
| Exact Admin290f resident eval | 0/54.038s. |

This proves Nix registration/reachability through the owning roots without
candidate/result dependency references. No GC-survival run is claimed. Normal
owning amendment preserved every tested byte; no hook was bypassed. Backup
`backup/2026-09-23-storage-redesign-provider-before-host-roots` retains bcc.

Final complete base `e1bb5cf3ad37c5ef31445a68ab85f53db2858777` to head `b7488807e95ad3d79febccf021d47a6afaee2b4d`, tree
`73fb0a2344976bbf50657b0780ac178ed6385e3d`: two coherent commits and 13 final paths.
Full binary/index digest `591f878c8198429cd7dfa6050fe8fc6b53ffa4038838e3f180805e77b6a70072`.
[Current final inventory](storage-profile-retained-selection-inventory.json)
and [current complete diff](storage-profile-retained-selection-final.diff).
cd81 admission remains unchanged/published/consumed; the owning second commit
contains the final rooting remediation rather than an obsolete fixup stream.
No input update, abandoned recovery mechanism, SQL migration or new format
iteration was introduced. Original independent whole-history/migration
conclusions remain evidence at their original bcc scope; direct remediation
inspection records the final inventory here.

Native DNS acceptance is now permitted at this exact clean head. It remains
unexecuted; publication/package/activation and actual public recovery/provision
remain separate pending gates. The session and retained refs remain open.

## Narrow native evidence/readiness amendment, 2026-10-05

After the b748 native failed at stage2, the missing original counter/disk
baseline prevented distinguishing the exact failed predicate. Implementer0
added bounded private baseline/comparison evidence and the accepted initial
counted-service prerequisite in the same existing Ruby fixture. API, Supervisor
and scheduler are checked separately with all-of semantics; the final copied
wait still requires only API/Supervisor. Existing timer shutdown now checks each
stop/inactive result. No equality, original data read or lifecycle guard was
removed. The failed run's cause remains unknown.

Lead directly inspected the one-path diff and Ruby3.4.9 syntax/diff passed.
Normal owning amend produced `77dd0d0447f48c8d8e667257cef2276738d053a0`, tree
`31986d97cfdae91a4de5daedadad13ce95c44d85`; unchanged runtime and inputs retain
b748 local-check proof. Original ef116da3 independent review and host-root
step9 disposition remain evidence; no independent rereview is claimed. The
[current inventory](storage-profile-retained-selection-inventory.json) and
[final diff](storage-profile-retained-selection-final.diff) reflect the exact
new complete two-commit branch. The fresh short native passed0/1018.533s/
parity1: one example, stage6, scenario_completed1, hold_released0; all six saved
preservation comparisons were equal and parent-owned process metadata was empty.
This services+one-DNS fixture does not prove actual full-cluster release or GC
survival. Feature publication/readback is exact77dd; default e1bb unchanged.

## Mechanical consumer and package proof, 2026-10-05

One generated provider pin at root `e5ba1912..de915cd1` changes two flakes,
5+/5-, exactly four provider metadata leaves. Generic6a, Codex32775, all other
nodes/follows/defaults and constructor/source are unchanged. The complete
[consumer inventory](storage-profile-retained-selection-consumer-inventory.json)
and [diff](storage-profile-retained-selection-consumer.diff) record its single
coherent commit/no-migrations result. This is the skill's mechanical dependency
exemption, not an independent composition rerun.

Fresh Luna/low package batch passed0/260.657s/parity1 at de915/provider77dd/
Admin290f. Existing four checks252.368s, default8.038s and byte proof0; all nine
equality flags plus profile loader passed, schema1/policy3/providers2 unchanged.
Exact output zwdv/tools n2ki is built, unselected. Current installed s7y4/q49
still has old maintenance bytes. Final source-equivalent tracking replay,
publication and comparison precede external idle activation; actual cluster
recovery/release/preservation/payload gates remain separate.

Final source-equivalent replay onto published coordination-only09da produced
root3dfda5c6/tree61859531. Patch/message/flake hashes and range-diff are equal;
default outPath evaluates to the exact built zwdv package (7.492s), and final
no-build passed (4.083s). Feature publication/readback and exact09da..3df
comparison are complete. This retains de915 build evidence without a new
independent review/build/VM claim. Package is unselected; actual recovery and
new default integration remain pending.

## Fresh-master composition checkpoint, 2026-10-05

User-requested freshness check found root master88a’s nested generic3ed/Codex3d07
upload update. Root-only replay produced c754/treeaedb on88a: exact upstream
flake.nix exceptproviderURL77dd, generated four provider leaves, every other
node/follow equal. Range-diff! reflects the URL hunk’s upstream attrset; message
and intended selection remain unchanged. Provider77dd/mastere1bb/Admin290f
remain exact. This mechanical dependency composition is exempt from a new
substantive review; original ef116da3/direct-step9/native evidence is carried
only within its original unchanged-source/input scope. No SQL migration or
new private format is introduced by the root pin.

Fresh waited package batch passed0/254.433s/parity1, existing four checks plus
default build and all nine actual-source equalities/schema1policy3providers2.
New3fzi/wg7 is unselected. Prior3df/zwdv package proof is historical; initial
un-waited0 launch is zero-check incomplete evidence. Publication/readback and
comparison base88a/headc754 completed, master88a unchanged, CI not awaited.
Actual activation/recovery/full-cluster/preservation/profile payload and
retirement gates remain pending. See the current consumer inventory/state;
this reconciliation is parent evidence, not an independent review rerun.

## Activation and default integration, 2026-10-05

User reported activation and conditionally authorized workspace-default merges,
keeping storage features separate. Selected3fzi/wg7/source/contract/Codex/four-
service proof passed, and public same-session status remained stopped/bridge/
starting_copied. Architect0 found no concrete remaining workspace source gate
for unchanged reviewed/tested inventories. Provider master77dd and workspace
masterc754 FF/normalSSH/readbacks completed; captured review/comparison bases
remain e1bb and88a. All seven held feature heads remain unchanged. No review
rerun, CI wait, source delta, cluster mutation or new SQL/state-format change
was introduced by integration. Actual retained recovery/trial remains unproved.
