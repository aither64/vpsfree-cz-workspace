# Final independent machine-claim and native-fixture review

## Findings and disposition

No Blocking findings. One Important finding remains open at the exact reviewed
runtime head. No separate Advisory finding.

### M1 — Important — Inspection failures can hide schema-2 claims from the reader gate

Lane: risk/compatibility, with general error handling. Feature commit
`30d3c195e47a371308b3203850c135b277479e8a` adds the schema-2 reader requirement.

`libexec/workspace-coordination-claims.rb:11-13` returns an empty schema-1 store
when `File.exist?(claims.json)` is false; line 153 independently skips the
capability check on that predicate. `File.exist?` suppresses ordinary stat/path
inspection errors such as EACCES. An inaccessible `coordination` parent can
therefore hide a retained schema-2 envelope rather than report an inspection
failure. The rescue around parsing cannot catch a suppressed error.

The adjacent ledger reader at `workspace-coordination.rb:158-163` also treats
`File.exist? || File.symlink?` false as empty state; `require_compatible!:675`
then skips the ledger check on another existence predicate. Normal switch
preparation and candidate compatibility calls do not acquire the ledger lock
that validates this directory. An otherwise compatible predecessor without the
new typed-reader contract can consequently pass the new forward-reader gate
while schema-2 history remains hidden.

This is material even with only released/canceled history: the exact predecessor
strict reader rejects schema-2 envelopes, including empty envelopes. A configured
held-profile guard may independently refuse a particular aitherdev transition,
but the generic runtime supports an empty legacy machine catalog and null profile
target. For that supported configuration, the no-claim profile path at
`workspace-coordination-host.rb:497` can likewise return when the ledger is hidden.
There is no general independent mitigation. This is an ordinary permissions/I/O
or configuration failure, without hostile local manipulation. No actual unsafe
selection, lost state or fault-injection result is claimed by this source trace.

Smallest requested remedy: make the owning claims/ledger presence and read
boundary treat only genuine ENOENT as absent. Reuse strict `lstat`/private-read
handling and propagate other inspection/read failures before package effects;
ensure subsequent existence shortcuts cannot erase that distinction. Keep
ordinary absent stores and existing schema-1 behavior. Add focused absent versus
root/traversal/EIO regressions through candidate/pre-effect admission, preserving
retained bytes. No collector, bulk rewrite, schema/API change or unrelated
inventory hardening is requested.

The lead independently inspected the cited paths, accepted M1 as Important and
assigned this exact bounded fix to A. This report reviews immutable `30d3c195`
only; subsequent work in progress is **not inspected, certified or closed here**.
The requested correction can be closed by focused direct inspection and checks
under mandatory-change-review step 9. A new design or compatibility boundary
requires affected follow-up; an automatic full reviewer rerun is unnecessary.

Otherwise no additional source issue was established in the assigned lanes.
M1 needs verified remediation or an explicit recorded decision before continuing
under the skill. This report does not clear that open gate, certify native or
packaged behavior, or grant publication, deployment, integration or lifecycle
permission.

## Identity, settings and method

Retained independent reviewer `reviewer0`, thread
`01a19ca7-8da1-7e63-852f-72d8332c553a`, purpose `review`,
`gpt-6.1-sol` / `xhigh` / `read_only`. Fresh live roster revision 27 confirmed
these exact saved settings and ready state. No override, fallback, nested agent
or substantive authorship.

Before accessing session records, `dev-session current` from the bound tracking
directory returned `2026-11-02-session-temporary-service-cleanup`. Both environment
markers were present and matched that slug and
`/home/aither/workspace/ai/vpsfree.cz`, also matching the trusted developer binding.

Applied mandatory-change-review directly after reading its full skill and all
four references: general, architecture/repetition, scope/proportionality and
risk/compatibility. Consulted applicable workspace/repository instructions and
procedures, current state, complete packet, design contract, owning documentation,
committed diffs/history, actual consumers, tests and receipts. Documentation and
handoff guidance places this report here; the lead retains coordination updates.
Overall risk is **High**: persistent ownership, cross-project protocol, package
selection and forward recovery, with deployment consequences.

Unaffected service/UI/native-Job/capacity conclusions are reused from the retained
reports, including `review-capacity.md`. `review-capacity-remediation.md` records
the lead's step-9 C1 closure; the exact committed correction shares the existing
fail-closed JSON traversal and preserves its requested scope. This does not
substitute earlier review for review of the new machine feature or native fixture.
Prior reports remain unchanged.

## Scope and substantive content

Compared the actual user decision with the diffstat and delivered milestones
before detailed hardening. The user explicitly accepted logical machine claims
and authorized implementation/deployment after the separate proposal. This is a
distinct fifth runtime commit, with 16 runtime paths and 1,158 insertions/73
deletions, plus the extension resolver and four workspace policy paths. Tests
and documentation account for much of that surface. Records show a frozen
contract, completed source packages, quick results and exact local composition;
this is delivered substantive work rather than only planning activity.

The selected boundary is canonical configuration-repository origin plus exact
configured Machine.name, including an FQDN. The optional configured shared label
intentionally joins identities across repositories/names. Human display uses
single colons and byte-wise percent escaping; internal identity uses one runtime
canonical tuple hash. No machine-id, SSH/DNS/native identity probe, physical
overlap discovery, new registry/worker or per-command remote gate was introduced.
The accepted residual is cooperative logical locking: different logical identities
can refer to one physical machine unless operators configure shared identity.
That residual does not call for the rejected probing subsystem.

Architecture fits the existing owners. Runtime `MachineIdentity` owns keys and
display, `MachinePolicy` owns finite immutable legacy/profile equivalence, and
`MachineSource` extends the existing registered-repository proof. Claims, scheduler
conflicts, compatibility and status use the same normalization. The extension
supplies only exact configured metadata through the existing protocol-1 adapter;
the consuming workspace supplies its profile identity and old-resource bridge.
Validation on both protocol sides has a concrete boundary purpose. I found no
additional architecture/repetition or disproportionate-scope finding.

Inspected the runtime and extension constructors, installed file paths, CLI
dispatch, profile callers, legacy scheduling and portal projections. Exact-ID
retry precedes resolution and preserves released receipts. New admission resolves
outside the ledger mutex, rechecks bounded local registration/config/ref evidence
inside it, and compares all active source-pair mappings before insertion. Waiting
grants re-resolve while preserving the original audit revision. Adapter-ID or
non-equivalent identity drift refuses; an installed bridge creates contention
without transferring a hold. `verify-machine` is read-only and checks an owning
held binding once for an intended batch. Profile admission reuses that proof.

The adapter uses immutable local Git revision metadata, exact attribute selection,
offline Nix evaluation, disabled IFD and disabled lock writes/updates. It does not
force machinesJson, build a generation or inspect a target. Strict names/labels,
duplicate/extra fields, source revision, output bounds and wrong-selector handling
were inspected. Package paths select an installed adapter ID rather than a
caller executable. Private diagnostics remain bounded; public claim projections
retain string arrays rather than exposing typed source/protocol payloads.

Legacy conflict normalization covers new claims, existing claims, active jobs and
unreleased reservations without rewriting saved keys, snapshots, attempts or
artifacts. Candidate checks preserve needed bridges and reject ownership
collisions. The consuming policy retains the entire old catalog and maps
`machine:vpsfree:aitherdev` to the documented repository/name tuple. First upgrade
therefore retains the old schema-1 hold, system first and ordinary profile switch
second; no bootstrap or ownership transfer is introduced. This is source-path
compatibility reasoning, not an executed upgrade.

The trusted local operator boundary remains intact; ordinary I/O, concurrency,
wrong identity, malformed remote/protocol input and uncertain effects remain
review concerns. Original unregistered-service exclusions and separate session
lifecycle permissions remain unchanged.

## Bounded native fixture

Compared reviewed/remediated `d1872f5d` with `8230ee8d`: only
`test/creation_transport.py` and `nix/tests/session-creation.nix` change, 197
insertions/17 deletions. Production capacity inputs and C1 remediation are equal.
The fixture adds four UUID-tagged ordinary managed POSTs through the existing
disposable portal socket/Origin, compares real native full/tiny ascending pages,
replays a saved tail after another steer, and replaces the actual portal PID
before another steer. It reads the wrapper's atomic record and recomputes its
compact count/digest; it never manufactures retry authority. Prior native entry-ID
prefix equality and exact client-ID/text/order assertions preserve causal scope.

The existing model fixture holds the active turn; the test releases it in finally
and checks completion, settings and absence of duplicate turns/inputs. It extends
the existing helper/VM instead of adding another harness, browser helper, target
probe or large-volume campaign. No new source defect was established. Syntax
evidence is not native execution evidence: the actual API/VM assertions remain
unrun, and this small-turn test alone cannot establish arbitrary-volume behavior.

## Complete ranges, history and migration conclusion

All targets below are `master`; these are review boundaries, not integration
approval. Runtime remote: `git@github.com:aither64/dev-workspace.git`.
Complete range:
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79..30d3c195e47a371308b3203850c135b277479e8a`.
Tree `78708075e51ff426a77e0c903dce071ef36c0c20`; 87 files, 6,937 insertions/379
deletions. Complete series:

1. `19dd03b79a2997098934afafbe70c63b978c1ca7` — Resources/Team UI.
2. `f7add7cea8a836810d32688ef2d1cf4cc011af19` — registered service cleanup.
3. `5b4b711748343f4ffe88b96c50d88a9f98eeb04d` — dependent portal/package and lifecycle fixture.
4. `8230ee8d8c55efe996a30d2cfe09f1de6a2171a8` — capacity proof, C1 correction and its native regression.
5. `30d3c195e47a371308b3203850c135b277479e8a` — logical machine claims.

Extension remote: `git@github.com:vpsfreecz/dev-workspace.git`. Complete range
`e4e7e95ed39bf514b33f8f8ae61ba9868de060ae..f8da821e3c76e26e73aa9d89a712eab0e0faa319`;
tree `0dee92a5a0971f250db89520c5d101b5b16bc008`. One coherent resolver/pass-through
commit, four files, 247 insertions/11 deletions.

Workspace remote: `git@github.com:aither64/vpsfree-cz-workspace.git`. Complete
frozen-base range
`7205352c95218562fe0b37dff8b4a3dbf0962eec..48b23aa5641a08cdf0a70294bac02d7ee371c108`;
tree `132e6afc654c499ef9281650a3ff4fb549fc1381`. Three commits:
`96c566aa6423ed6c1a17e71a69bca641646a012f` instructions,
`966da565444266ce01eec6418ecc770a4118f27b` existing selection, and
`48b23aa5641a08cdf0a70294bac02d7ee371c108` machine policy/docs. Whole diff seven
files, 121 insertions/12 deletions; the last commit is four paths, 96/6.

Independently checked complete series/final diffs and consolidation. Original
three runtime commits are exact; machine patch is range-diff `=` against retained
`9a74fde0`. Pre-consolidation `5c147b8a` and final runtime have identical trees.
Workspace's two original patches are `=` against B7. Independently reconstructed
the rebased full tree from Git entry metadata, without writing Git objects or
reading foreign tracking contents: incoming changes are exclusively work/archive/
notes and disjoint from feature paths; result equals bridge tree
`eeab827af4ce4745a3060220d7d91aaa5cc1dc5b`. Historical refs remain outside final
ancestry. **No obsolete source approach, redundant fixup or transitional
implementation remains in the reviewed histories.** The logical commit split
and final-result messages are appropriate.

**No database migrations.** Existing claim envelope 1 and retry state 1 are
intentional supported predecessors. New machine claim envelope 2 and retry state
2 are directly introduced local feature versions, unpublished/unmerged/undeployed
and not externally consumed according to the packet's provenance. No abandoned
intermediate schema or bulk migration is retained. Typed admission atomically
writes claim envelope 2 while preserving old rows; reads do not rewrite. All
schema-2 history requires a compatible reader, subject to M1. Exact predecessor
source evidence confirms schema-2 terminal/empty rejection and unchanged bytes.
Retry lazy conversion and immutable Pending/Snapshot/UUID/charges remain as
previously reviewed. Legacy catalog/ledger/payload and service/lifecycle/recovery
formats retain their versions. Migration lineage is coherent; M1 still needs
its compatibility refusal corrected.

**No repeated dependency/generated stream exists in runtime or extension.**
Their locks are byte-identical to their respective bases. Workspace has one
existing runtime selection stream in `966da565`; configuration has one historical
devWorkspace channel commit, range
`c040c14cdbacc07998700b524996a89306188d7f..59d12a3b980d46f32f694a8cc98d7e965b9b66c8`.
Inspected both pin diffs: they select EE3 only, with no intermediate pin stack.
Those selections are stale for this feature and are explicitly preparation
evidence. They must be replaced/consolidated with actual final published inputs;
there is no supported boundary requiring retention of redundant intermediate pin
commits. Future extension selection is also uncreated. This conclusion accepts
the current clean history and consolidation plan, **not hypothetical final pins
or branch readiness**. Actual final streams still need exact source/NAR/full-graph
equivalence and the ordinary certified-refresh/history proof.

## Immutable source, composition and verification limits

Independently read and hashed these actual source paths:

| Source | NAR |
| --- | --- |
| `/nix/store/x28zskxq9i476fr21xr3r3qy4vbgjkcf-source` | `sha256-C/JaftbMW423xx2RJLzowr3UJYhhwu9yecnLhZeYemk=` |
| `/nix/store/y01y2bs4mar8zq9s72npz3lrmlsjvasa-source` | `sha256-U5y/TEny6nsyXWNlCMktmxTZhpVO0QY4kOo/qgwsapM=` |
| `/nix/store/9gpik372lmiw23kvihv2hmmj9fqf3zdy-source` | `sha256-U9MeFrHGuN5UlG5a6i6+THwdpO2hq5xUn4QLndOEquI=` |

All 679 runtime and 112 extension Git entries matched source bytes, symlink
targets and executable modes, with no extra/missing source entries. All 43
nontracking workspace entries matched; foreign tracking contents were not read.
These bind the clean committed submission; later remediation edits are outside
this immutable review.

Read the actual complete graphs/metadata and compared them independently.
Runtime's nine-node graph including root and extension's 34-node graph equal their
base locks. Lock SHA256 values are respectively `fa808c04...` and `b2282ff7...`.
The effective workspace composition has 35 nodes; only the two explicit provider
source nodes differ from committed selection, all 33 other nodes and every
input edge/follows unchanged. Workspace lock remains `94c9da5e...`. Provider
revisions and NARs equal the sources above. Staged/final effective graphs and
package derivation receipts are identical.

Inspected the actual composed derivation's source, postInstall inputs and policy/
catalog writeText payloads. The legacy catalog is semantically unchanged except
the expected installed adapter command; its full compatibility data matches the
baseline. Profile policy, legacy bridge and machine contract match source. Site
derivation `/nix/store/gf3lpsv34430l2cl43p0srw85rwh2bqm-dev-workspace-0.2.0.drv`
points at exact x28 source and planned output
`/nix/store/0m1lc8rbwrl3i0fgkqlzp1187bplfyk6-dev-workspace-0.2.0`.
That output is evaluated, **not built**. Historical EE3 artifacts certify neither
this composition nor deployment of it.

Inspected and hash-checked the five final quick logs: machine 21/152, claims
32/178, admission 4/13, selected legacy 25/189 and host 6/105; total 88 tests/637
assertions, no failures/errors/skips. Six Ruby syntax checks pass. Tested staged
tree `269468b9dfa036fe05a20611fdf775d7f1de98df` differs from final only by one
extra native entry-ID prefix assertion, with affected syntax rechecked. Earlier
fixture-name collision evidence remains retained; it is not hidden as a pass.
Extension reports 10 tests/89 assertions with actual offline immutable-Git
projection and no skips; workspace deployment-contract checks report 4/19.
These scopes and constructor/policy evaluation support source review, not an
overall package/integration pass.

Real ascending native API/restart proof, corrected service-cleanup VM, full exact
runtime/package/host CI, the two Playwright consumers, extension/package checks,
installed profile/system transition and usability remain outstanding. No native
cleanup or physical deployment success is inferred from component DTOs, syntax,
old artifacts or evaluated derivations. M1's correction still needs its focused
proof. Scope-specific checks stay with the lead; this review does not waive them.

No reviewer tests, builds, Nix evaluations, CI, live/native probes, claims,
publication, deployment, source/Git/store mutations or lifecycle operations were
performed. Read-only hashing/history inspection and this permitted report write
only. Prior reports and ordinary source roots remain untouched. After verified
closure of M1, no other source finding from this review prevents the next required
proof; no operational approval follows that statement.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
