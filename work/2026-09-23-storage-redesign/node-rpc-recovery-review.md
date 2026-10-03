# Node RPC recovery — review preparation

## Status and request

Retained reviewer0 completed all four HIGH-risk lanes on148ef..7da, with
no Blocking and two Important findings. Both requested narrow fixes are
verified under step9 and folded into runtime d82a6cc1; the separate fixture
290f1ef0 is unchanged. Declared lint/full Node634/0 pass at final bytes.
One existing disposable remote-restore integration is running under source
hold; actual broker/payload acceptance remains pending.

The user selected Node recovery before the retained storage-profile trial and
directed implementation. Fix cleanup error precedence and ambiguous channel
retirement, prevent expected storage-status RPC failures from killing nodectld,
and prove restart-persistent fixture settings plus restored/next-backup data.
See the [saved brief](design.md#node-rpc-cleanup-and-remote-restore-recovery-slice-2026-10-03),
[original failure diagnosis](api-remote-restore-ci.md) and [state](state.md).

## Ownership, scope and compatibility

Session `2026-09-23-storage-redesign`, workspace `/home/aither/workspace/ai/vpsfree.cz`.
Repository: `worktrees/2026-09-23-storage-redesign/vpsadmin`; branch
`2026-09-23-storage-redesign`. Starting head:
`46b3bf6f9549eaf579053bc296ebf19c417bb848`.
Cached default and merge base before this slice:
`878a0d10c86060ed2ce62027223832371ca5e49e`.

Intended split: one Node runtime/spec/documentation commit; one existing
remote-restore fixture commit with persistent queue settings and payload proof.
Runtime ownership is RpcClient, NodeBunny and StorageStatus in libnodectld.
Existing RpcClient consumers include startup configuration, pool/VPS/storage
status, user maps, export setup, console authentication and accounting. Required
and optional publishers continue through NodeBunny's existing recovery gate.

No wire, schema, dependency, production queue-default or provider/generic
changes. This is an internal Ruby error/recovery contract; old Nodes retain the
defect. Deploying or reverting requires no schema conversion, but reverting
does not repair an interrupted chain. Original broker-timeout cause remains
unknown. No manual unlock, populated-cluster boot, production deployment,
default integration, quiet, repair-ready or APPLY authority is included.

## Review selection and history

HIGH risk: Node daemon behavior, channel/consumer lifetime, recovery and storage
data preservation. All four lanes apply: general, architecture/repetition,
scope/proportionality and risk/compatibility. Retained reviewer0 is independent,
review-purpose, read-only GPT-6.1 Sol/xhigh; preserve saved settings without
override or nested reviewers. Reverify ready roster before assignment.

The original 21-commit Admin series and its whole-history review are recorded in
[the Admin packet](storage-profile-admin-review.md). The new complete branch
inventory must account for the two intended commits and final diff; unchanged
functional review evidence must not be presented as a rerun.

This slice adds no migrations. The complete feature branch retains, in order,
`20260924210000_add_storage_integrity_foundation` and
`20260926100000_add_bounded_storage_capture_indexes`. Both were published and
externally consumed in disposable/retained trials; no production application or
default merge is established. Preserve their versions and additive schema.
Confirm their blobs at the final head and require an explicit history/migration
conclusion from the reviewer.

## Verification gates

Before review: focused three-file component specs, targeted lint, CI selector
checks and the existing full libnodectld suite in an isolated test environment.
Include actual commands, held hashes, results and failures here once available.

First frozen six-file selection at Admin46: incomplete, exit1/761.69s;
33 examples/3 failures, root lint unrun, source/lock parity1. The two completed
NodeBunny failures were a missing controlled-transport `write` sink and a
channel allocated before the creation snapshot. A malformed-catalog fixture
then returned updates indefinitely: String indexing accepted the chosen value
and the catalog skipped it instead of raising. The lead authorized signals to
the exact owned RSpec process after preserving evidence; the watcher confirmed
automatic disposable DB shutdown/removal and no remaining owned process.
Private evidence: `/tmp/node-rpc-focus.v7_htrdd`. Narrow spec-only corrections
are assigned; runtime/RpcClient-spec bytes remain held. This run supplies no
passing suite evidence. See the [fixture note](../../notes/vpsadmin/2026-10-03-node-recovery-spec-fixtures.md).

After the two spec corrections, the fresh selection completed 39 examples with
one failure, exit1/18.455s, source/lock parity1. Bunny's continuation timeout
reads `Transport#write_timeout`; that accessor was absent from the controlled
double. The declared lint/full-suite stages were skipped. One spec-only
correction is assigned; all runtime bytes remain unchanged. No process or
disposable database remains. Evidence: `/tmp/node-rpc-quick.v97da9ft`.

With the finite transport accessor, the focused selection passed39/0 in17.746s.
Declared root RuboCop1.85 then failed10 offenses in57.009s: unsupported
`disable-next` syntax left intentional Exception rescues unsuppressed, and an
explicit Struct keyword-init argument was redundant under Ruby3.4. Full Node
suite unrun; source/lock parity1 and no remaining process. The two runtime
files are released for that exact syntax/comment correction, with all other
bytes held. Evidence: `/tmp/node-rpc-quick-final.umt7rxet`. The parent corrected
its log modes to0600 under0700 and will set the parent driver's umask before
opening future logs; the child's umask alone did not control those files.

The portable directive/Struct correction was verified by fresh Luna/low
`node_rpc_full_declared_46`: driver exit0/54.107s, declared root RuboCop1.85
exit0/14.904s and full libnodectld618 examples/0 failures exit0/38.756s.
All nine authored sources plus six dependency/flake hashes and the empty index
matched before/after. Private evidence `/tmp/node-rpc-full-z7bkokjv` is
0700/0600; no command or automatic TestDb remains. The full suite includes the
39 focused examples, so it proves the final corrected runtime/spec bytes.

The docs/fixture authoring checkpoint now consists of nine distinct paths: six
runtime/spec paths, `docs/node-rpc.md`, its `docs/README.md` entry and the single
existing restore scenario. The lead applied the owning English writing pass
and accepted the two docs unchanged. Actual broker/VM/payload evidence remains
pending; the final static selector/fixture-derivation/Nixfmt batch is running.

Run specs through `.#libnodectld`. The component bundle does not declare
RuboCop; run its six-path lint through the root `.#vpsadmin` bundle used by
hooks. The existing [component-shell note](../../notes/vpsadmin/2026-08-04-libnodectld-rubocop-root-shell.md)
records this tool ownership. Reject an inherited database URL or configured
API database before loading the spec helper, and use the supported automatic
disposable test database with a short private temporary directory.

After committed review and finding resolution, a fresh Luna/low watcher runs
only `storage/restore-after-reinstall-remote`. Require daemon restart proof,
effective zero transfer delays, A/B destination payloads, reinstall sentinel
absence, restored B, subsequent C backup and incremental history, terminal
chains and normal lock release. Keep diagnostics private and bounded. The test
does not prove arbitrary live-send crash replay or the retained public cluster's
refresh/release. Populated-cluster acceptance remains a separate next phase.

## Final static checks and source conformance

Fresh Luna/low `node_rpc_static_46` passed three stages at the same nine-source
and six-dependency manifest: CI selector18 runs/77 assertions/0 failures/errors/
skips (8.439s); actual existing fixture drvPath evaluation (65.653s); owning
root-shell Nixfmt check (7.696s), all exit0, total82.342s/parity1/indexempty.
Evidence `/tmp/node-rpc-static-_0ax6je9` is0700/0600, no owned process remains.
The eval produced `g64p9i2mpfdx47p4zmvl65b6viyigyj0` fixture JSON derivation;
its public log mentions a source-metadata derivation during evaluation. No guest
configuration closure or VM was realized, and no kernel build was reported.

Architect0's bounded public-source conformance found no accepted-design
mismatch. Persistent delays, custom ordinary startup without common transient
queue repatch, graceful restart identity/keyed scalar interface, transfer
input snapshots/output.execute.status, original restored receive path and GUID,
single-tree/branch history, readonly A/B/C and normal lock-release proofs match
actual sources. Normal transaction close clears signatures, so the persisted
input projection proves envelope contents, not retained cryptographic signature
verification. This is design conformance, not independent review or runtime proof.

The first normal commit launch failed the API localization hook before creating
a commit: the nested API bundle selected root lock context while frozen mode
was inherited from the private root bundle-exec launch. Other hooks passed.
All eight staged source hashes are unchanged. The corrected launch uses the
owning Nix shell's normal root bundle and direct Git without bundle-exec/RUBYOPT
preloading or private frozen bundle context; all hooks remain enabled.
Evidence `/tmp/node-rpc-commits-26bn4c5f/runtime.log` retains the failure.

## Exact final source and complete branch inventory

Fetched SSH default/base: `148ef0eaed0459c825f1ba94b8dad2b9f3311b2f`.
Final head: `7da85b7a16851ebf08e655ee12fd918762cff991`.
Tree: `4ae8a7a55950f1e0345def3d4d67c7ed6b6de2de`.
Clean tracked/index state; preexisting untracked `webui/.phpunit.cache/` preserved.
Complete diff:210 paths,23392 insertions/452 deletions. Full binary/full-index
SHA256 `7c776e4e7d0efbb0cafc6e51a37a88f0b7f8723f00e9df5d00c4d4d142f5329f`.

The two new owning commits are `84fa8a501220ba82b69f57a1d1fe73fccd33f91c`
(runtime/spec/docs8paths,1003+/131-) and `7da85b7a16851ebf08e655ee12fd918762cff991`
(existing fixture1path,321+/89-). Both original normal commits passed all
pre-commit hooks and commit-msg hooks; TextWidth warned about its preferred
60/72-column widths, while every line satisfies the workspace80-column limit.
Their pre-rebase heads `46894de1`/`fdc9be376` remain at
`backup/2026-09-23-storage-redesign-before-node-recovery-master-refresh`.
Hook evidence: `/tmp/node-rpc-commits-26bn4c5f/runtime-corrected.log`, `fixture.log`.
No hook was bypassed. The nine tested source hashes are unchanged in the commits.

Fetched upstream advanced by two dependency commits on four non-overlapping
paths: API packaged `parallel`2.2.0->2.3.0 and WebUI dependency updates.
No runtime/default/module/Node/dev-shell/test/flake input changed in that delta.
Normal Nix/Git replay retains all23 messages/patches (`range-diff` all`=`), and
the complete feature binary patch is byte-identical before/after. Every tested
source/dependency guard path is unchanged; final composition guards additionally
include the four upstream dependency files. The actual packaged API dependency
update is retained, so final scoped fixture graph evaluation is
required before review/integration; broader checker limitations remain visible. Existing full Node proof carries only as
source/environment equivalence; it is not a claimed new-head suite rerun.

Complete base-to-head series:

1. `6562e1410a31bcd93dfa4d4658c01dd8ba651373` — storage: establish integrity schema and freeze bootstrap
2. `9d215ffcd5d987cefa3466a2b4c11122480f1968` — storage: journal observer writes across API and NodeCtld
3. `0771b0b32bd94451d7a1131ca83a1564f5e895d5` — storage: add advisory inventory and reconciliation
4. `3e1e67e779ed23ea55efafb401d862bc37a32388` — storage: add authenticated freeze API and WebUI
5. `9ee0d3cdc8602042a54df36ab590b46c851445fc` — storage: prove strict snapshot dispatch in test mode
6. `9780d44c9f933c5911f98972fd4e118635d114c9` — storage: document integrity evidence and observer limits
7. `75eaff4118f5d248dfb810a57e9ab603237f8227` — nodectld: observe bounded local storage activity
8. `0a637077345ee801babd49a840e63c100bf95094` — storage: preserve exact GUIDs in signed inventory
9. `2ea6d33c4edc3d9b43faf37970b3f5ec0192bae2` — storage: sample node and osctld activity around inventory
10. `8590a38dcdb1bfd13fbfe3652b289096c617108a` — storage: accept capped settled intents in activity reports
11. `0d2423359e2dccd141092e64b4c2527900ebf388` — Distinguish completed rollbacks in DB capture overlap
12. `1d49cf42fb4cf832d682ec7676fe515acb09c286` — Keep storage reconciliation replay cold and offline
13. `cebff346190345a3ae5a7f4681ced254cd059547` — api: canonicalize captured storage GUID decimals
14. `7201c64fd68fbb34a58bfdd954fa2a35480b1048` — storage: version offline coverage conservatively
15. `8c39211016dcad8d7e8e4aafa246ba79994da98e` — Bound storage reconciler capture to current evidence
16. `af4dd3a2618606adc0d323bf8d9c5f567496dc70` — Restore pooled DB isolation after storage capture
17. `ece32c604ab2159bfe2ab2a18866541164b33325` — api: avoid fixture IP address collisions
18. `72f1b5245da2e432ea71e58e9384f9e44ca639ca` — Use the shared transient node exchange for inventory
19. `0b476b9b7b2f5f4b6330cf82e777d7c035a199bb` — flake: vpsadminos 8e44a5124 -> 8d05dc3ae
20. `8b292278f66478276db5e3c9e554de77c70b2c06` — api: support bounded scheduler intervals and task refresh
21. `e882caebe8a220bdd4667fd285f7cf83c66e0d16` — api: serialize dataset plan membership and retain shared templates
22. `84fa8a501220ba82b69f57a1d1fe73fccd33f91c` — nodectld: retire failed RPC channels through connection recovery
23. `7da85b7a16851ebf08e655ee12fd918762cff991` — tests: verify remote restore payloads across persistent queue settings

History disposition: the new slice has no fixup/follow-up implementation commits,
obsolete alternative retirement engine, transition shim, duplicate dependency
update or migration. Runtime, actual-Bunny regressions and owning contract docs
form one behavior; scenario-specific persistent restart/payload evidence forms
the separate fixture behavior. The preceding21 patches remain equal to their
already-reviewed supported feature series. Inspect the complete23 history and
final diff, and explicitly conclude whether obsolete history remains rather
than treating prior review as a new functional rerun.

Migration provenance remains the two published/externally consumed additive
versions recorded above. Their exact blobs and core-schema blob are unchanged
from46. No new migration/schema/wire/publicCLI/dependency/pin/OS/provider change
is introduced by the two Node commits. Their deployment does not require a
schema conversion or fleet-wide coordinated update; old Nodes retain the bug.
Reverting does not repair already-interrupted transaction state. Normal recovery
and original strict/capture/quiet/APPLY boundaries remain intact.

## Final-head evaluation selection

An added whole-flake no-build probe failed exit1/1.247s at
`/tmp/node-rpc-rebased-zr42m3rs`: Nix rejects `overlays.list` because it is a list,
not a function. That exact output is unchanged at old46 and fetched148ef master;
no Node commit changes the flake. This is a baseline whole-flake checker
compatibility limitation, not a passing check or a Node source defect. The
selected owning fixture derivation evaluation remains the actual scoped
composition gate. A first utility launched zero checks after obtaining
no-current outside the exact tracking cwd; the lead reconfirmed current at the
literal session tracking directory, both markers absent, and added that check
to the guard. The fresh correctly-bound evaluation watcher is running.

No broad flake-output fix or hook bypass is included. The baseline limitation
must remain visible in review/rollout evidence; actual fixture realization and
remote-restore acceptance are still pending after review.

Final scoped evaluation passed under fresh Luna/low
`node_rpc_final_fixture_eval_bound`: exit0/57.757s, actual fixture evaluation
56.357s, exact-current/HEAD7da/indexempty/19hash parity1. Private evidence:
`/tmp/node-rpc-final-eval-v3f5cyby` (0700/0600). This is derivation/configuration
evaluation only; no native fixture invocation, broker/guest or payload success.
All intended application changes are committed; the complete branch is ready
for independent review, with the baseline whole-flake checker failure visible.

Review request: inspect the actual148ef..7da23-commit series and final210-path
Git diff, preserving prior unaffected functional review evidence without claiming
new functional reruns. Concentrate all four lanes on the two new Node commits
and their consumers/compatibility, and provide explicit complete-history and
migration conclusions. Assess docs placement/content and the existing fixture's
persistent config, actual restart, data/history and bounded-diagnostic claims.
Return severity-ordered source-backed findings and residual gates. No source
edits, tests/builds, private evidence/credentials, network, refs or runtime action.


## Independent review outcome

Retained reviewer0, ready/review/read_only gpt-6.1-sol/xhigh, independently
reviewed actual148ef0ea..7da85b7a with all four HIGH-risk lanes. Exact clean
head/tree/full-index diff matched the packet. No tests/builds/network/private
artifacts/source/ref/runtime actions were performed by the reviewer.

No Blocking findings. Two Important findings, both in runtime commit84fa8a50:

- **Required publisher compatibility:** NodeBunny.acquire_publisher at219-222
  and385-389 gives every required publisher RECOVERY_WAIT30. StorageStatus's
  submitter and MountReporter do not catch RecoveryTimeout, so a recovery or
  occupied gate beyond30 seconds kills nodectld under Thread.abort_on_exception.
  Scope this bound to explicit RPC waits, retain ordinary required-publisher
  recovery semantics, and cover a representative existing consumer. Keep
  retirement proof and bounded RPC cancellation; no broad telemetry rescue.
- **Cleanup error ownership:** RpcClient.run at20-32 reads ambient `$!` in
  ensure. Inside an enclosing rescue, that can be an already-handled error
  even after a successful body. Cleanup-only typed/unexpected/signal errors
  are then incorrectly suppressed. Record this invocation's constructor/body
  exception locally; retain original identity/backtrace and nonlocal control
  flow. Cover enclosing rescue and re-raising the same outer exception.

Other conclusions: no fixture finding; persistent per-node settings, graceful
restart/scalars, A/B/C readonly payload/history, reinstall absence, restored B,
S2/S3 transfer inputs/results, receive history/GUID/branch/tree assertions conform.
Existing Bunny retirement retains exact tokens, old-transport/reader/consumer
proof and registry gates; late requests are not acknowledged by generation only.

Whole-history conclusion: all23 replay mappings are equal; complete210-path
delta and binary hash match. No obsolete retirement engine, fixup stream,
repeated input updates or unsupported branch shim. Exactly the two previously
consumed additive migrations remain in order with unchanged schema blobs;
**no new migrations in the Node recovery slice**. Prior unaffected functional
reviews remain evidence without being relabeled as fresh reruns.

Integration is held. The lead requested a saved narrow remediation brief from
architect0; implementation and focused verification are pending. The original
acknowledgement-timeout trigger remains unknown. Neither controlled-transport
specs nor the planned settled-operation restart scenario prove arbitrary
live-transfer crash recovery or populated-cluster release. No default merge,
production deployment, unlock, strict/quiet/repair/APPLY authority follows.


### Frozen direct correction and verification

Implementer0 released exactly five files at unchanged7da85b7a/indexempty:
NodeBunny and RpcClient runtime, their existing specs, docs/node-rpc.md.
No consequential design deviation: internal recovery_timeout:nil preserves
ordinary publisher waiting; RPC explicitly passes the finite budget. Local
constructor/body error state replaces ambient $!. Actual StorageStatus batch
retention/publication, owner contention, bounded timeout/cancellation/keyword
consumption and enclosing-rescue/signals/nonlocal exits are covered.
55 focused examples are authored (22NodeBunny,26RpcClient,7StorageStatus).

Final five-file manifest: /tmp/node-rpc-review-remediation-manifest.sha256,
SHA25688c6fa0e2eaf20e835f9dcf91b6e16e40eef54f07414bfdede3aca606ad593fd.
Only member syntax/whitespace checks have run. Lead direct source inspection
and main prose pass accept the frozen correction. Fresh Luna/low owns the
focus/declaredlint/full batch; results and normal owning fold remain pending.
These are direct requested fixes under mandatory-review step9; no unaffected
review lane is rerun or new scope accepted.


First direct-remediation focused batch at7da85b7a stopped on55examples/1failure,
exit1/18.630s (total20.081s/parity1). Evidence remains at
/tmp/node-rpc-review-fixes-xp7ieeh5. Declared lint and full suite were unrun.
The lead read the failure and owning source: the new explicit-RPC-opt-in spec
called protected response= outside RpcClient's lexical context; the actual
reply callback uses it within the owning class. Released only that existing
spec for explicit test access to the unchanged protected setter. Runtime/docs
and all other files/index remain held. No operation remains; original failure
is preserved, and passing prior cases do not clear the failed example.


Corrected focused verification PASS55examples/0failures,19.636s. Declared
RuboCop1.85 then failed with exactly2 autocorrectable test argument/key
alignment offenses,13.399s; total35.129s/parity1. Full Node stage unrun.
Private evidence /tmp/node-rpc-review-fixes-final-c_1ufkiq; parent corrected
expected.json mode0644 to0600 (directory already0700). Released only those
existing NodeBunny spec alignment lines; runtime/docs/otherfiles/index held.
Next fresh watcher selects declared lint then full Node, which includes all55
focused cases; no separate focus repeat for a whitespace-only correction.


The next declared lint gate stopped at1 remaining ClosingParenthesisIndentation
offense in the same nested test expectation,13.436s/total14.834/parity1.
Full Node unrun; private /tmp/node-rpc-review-lint-full-l60o9740. Parent read
the actual cop's column11 requirement and released only that closing whitespace.
No logic/runtime change; earlier55/0 remains the corresponding focused proof.
Source/index hold and mandatory-review step9 remain in force.


Final direct-remediation source gate PASS: fresh Luna/low
node_rpc_declared_final_suite ran declared rootRuboCop1.85 (4files/0offenses,
13.275s) then full Node634examples/0failures (35.803s), total51.225s/parity1.
Private evidence /tmp/node-rpc-review-verified-ck0mwrka,0700/0600. No owned
operation remains. The full suite includes all55 focused cases at final
whitespace-corrected bytes; earlier55/0 and each diagnosed failure are retained
separately. Controlled Bunny fixture-close IOError diagnostics are expected
failure-path output, not an additional daemon/real-broker observation.

Lead focused inspection confirms exact requested narrower publisher contract
and local primary-error ownership. Both Important findings are resolved under
mandatory-review step9; no new mechanism or affected-lane rereview is needed.
The normal owning runtime fold and unchanged separate fixture replay are
executing with hooks. Actual remote-restore integration is still unrun.


Normal owning fold complete: runtime d82a6cc1cf25e6e23671ae095880a4478a9d4e18,
separate fixture290f1ef07972e53c2b5154dbfa8b088802bde619,
treea2de421a02cc0add7a256273133b5dab9a2b2f32. All pre-commit and commit-message hooks passed in owning
Nix environment. First21/e882 parent unchanged; separate fixture's full binary
patch is identical and range-diff equals. Final19 protected hashes match tested
bytes; tracked/index clean and preexisting PHP cache preserved. Backup
backup/2026-09-23-storage-redesign-before-node-review-remediation retains7da.

Final complete inventory:23 commits/210paths/210 files changed, 23740 insertions(+), 454 deletions(-); full-index binary
SHA256f2abad5545f2e5b0daefcec7c0aca6a7e013be077b49ba200cb28bc4ba74565e. Exactly the tested five-path372+/26-
correction differs from the reviewed7da. Both consumed migration versions and
core schema blobs are unchanged; no new Node-slice migrations. Original full
independent review plus direct step9 verification remain evidence; no fresh
unaffected full-review claim.

Fresh Luna/low node_rpc_remote_restore_290f owns ONE existing disposable
storage/restore-after-reinstall-remote via /tmp/nrvm.0qykahy0/run.py atclean290f,
emptyindex/19hash/binding guards. It uses newprivate state plus no-destructive
evidence retention; native runner owns disposable cleanup. Outcome pending,
source/index held. No registered retained-cluster or release operation is run.

## Final integration and publication

Exact remediated290f passed the single existing remote-restore integration:
exit0/1610.195s/parity1, all4 examples and actual A/B/C payload/history assertions.
Private evidence `/tmp/nrvm.0qykahy0`; parent confirmed clean tracked/index and
zero exact-state VM processes. The complete23-commit source remains the final
inventory above, with original independent148ef..7da review and directstep9
fixes, not a full reviewer rerun. Normal owning-shell exact-lease SSH publication
and remote readback completed at290f; master148ef unchanged. New CI started; no
CI success or recovered original broker trigger is inferred from this local run.
