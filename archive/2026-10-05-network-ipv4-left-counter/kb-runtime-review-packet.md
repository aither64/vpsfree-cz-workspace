# Portable KB runtime: final committed review

At assignment, all intended source changes were committed, all quick gates
passed, and the three worktrees were clean. Subsequent narrow working
remediations for reported findings are excluded from this original committed
review; reviewer0 uses git show for K. Current dispositions are in
kb-runtime-review-findings.md. This is the final tooling review, separate from earlier
network-feature reviews. No long package or VM operation has been launched by the lead. D's existing
exact-head CI has since completed successfully, without a wait or rerun.

The user requested that vpsfree-kb-contracts work outside this workspace, accepted
the standalone-first plan and directed implementation. The accepted design is
in design.md, including the later artifact-root, update/resume, multicast,
streaming, managed-digest, standalone profile and upstream-reconciliation
clarifications. Review against the final accepted contract, rather than an
explicitly superseded draft. plan.md/state.md record scope and evidence.

## Snapshots and complete histories

Worktree prefix:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/`.

| Owner | Worktree | Exact whole-branch base | Exact head |
| --- | --- | --- | --- |
| K | vpsfree-kb-contracts-runtime | 873758fd6aec0c03f50a94600e0ceab97946f255 | 93a16d6cecb6bc847ec9335a3f170eb8b301ab56 |
| D | dev-workspace | a2bbf2f1c588de7eec0d7d52580a89a9d4bef984 | 51aba080b264c28f5584867b6cf006bf423ae2f3 |
| E | vpsfree-dev-workspace | 0ff827df13e82dfab4b536ff29979280f264e8f5 | d2079f605ae87871037ae73c5e5daf20a3e0d03d |

Fresh full-index binary diffs, complete full-message histories, stats, containing
refs and checksums are kb-runtime-final-{k,d,e}.{diff,history.txt,stat,
containing-refs.txt,sha256}. Independently verify merge bases and clean states.

K: inherited a50f8c1a11ea642edf823f04521f9eaa97132fd2 exact V pin,
then 93a16d6 runtime/capture. Runtime implementation began at a50, but whole
branch review must include the inherited pin. The runtime and capture changes
are coupled: the old implicit client is replaced by the versioned descriptor,
lease and artifact provenance contract, which must agree atomically.

D: c582ee757cd5b55c69db7b030ffd25eae8e5635b lease transport,
then 51aba080 deadline/test supplement. Fresh base a2bb contains upstream
8f0f40a04f5dcf1b590eb4cb8562bfecebe2962d's functional lost-CAS fix.
The local duplicate draft was preserved, never committed, and only the original
lease was rebased with an equal range-diff. The supplement adds the post-proof
deadline check, small deterministic-test seam and three tests in two Go files;
upstream acceptance/loop/comments/assertion are preserved. Review actual CAS,
background versus synchronous proof and executor behavior.

E: ce97027 input declarations/generated lock, then
d2079f605ae87871037ae73c5e5daf20a3e0d03d optional provider. Root partially
staged only the two URL declarations for the first commit; its baseline flake
body is preserved. The second contains provider/package logic, tests and docs.
The final tree exactly equals the checked 23-path candidate. No fixup or
repeated input-generation series remains. Inspect each commit independently.

## Ownership, consumers and acceptance

K owns one portable Linux/Nix launcher, private root-bound state 2, prepared
artifact versus per-start run identities, process/resource receipts, owned
shutdown, retained disks and exact closure preparation, connection/lease 1,
and matching runtime/capture/validate packages. It has no dev-session discovery,
workspace registry dependency or ambient source override. Legacy state remains
untouched; disposable recreation replaces adoption. Numeric multicast port and
actual TCP/UDP claims must isolate resources, including across checkouts.

E owns only optional workspace/session binding and generation/lifecycle guards.
The selected K executable, source receipt and nonmutating snapshot validators
must agree at the exact pin. Imported reads use noncreating wait:false locks;
all lifecycle/build/SSH/claim/live operations belong to the fixed K CLI. Binding
engine_revision is retained creation provenance, not permission to capture a
stale source. Transition compatibility is distinct from capture readiness.

Managed descriptor changes only control.argv; E derives canonical C and managed
M from exact bytes, verifies complete canonical readiness and translates only
descriptor_sha256 C to M. It never overwrites K's canonical descriptor or grants
an alternate digest. Cleanup inventory is positive read-only state/socket
inventory, including while running, without reacquiring the session lock already
held by generic early removal; actual reset retains normal lifecycle/process
proof. Inspect concrete provider and generic consumers, not only unit doubles.

D streams only provider capture-lease through mediated three-way pipes under
the unchanged public dispatcher/generation/catalog/environment contract. No
original peer or authority descriptors escape. Protocol stdout EOF ends a
pending/acquired lease promptly; diagnostic stderr EOF is harmless. Exact owned
children are supervised and reaped before ordinary guard release. Other provider
commands remain buffered. D also retains the upstream reconciliation fix.

The local operator is trusted to administer D/E's development host, as their
AGENTS explain. Ordinary wrong-root/session/path/ownership, concurrency,
interruption and integrity checks remain required. This assumption does not
weaken guest/remote-client boundaries or KB publication approval.

K input graph retains V5d5527a67315c18b595345aa6996d7724c1ed071 and effective
OS6bdf458fd9105379860234ff33d352e55844f08f. E pins K93 and D51 independently,
with no follows/overrides into K. Canonical semantic graph comparison matches
D17 and K45 paths to owning locks and preserves the five unrelated E root
inputs. The selected D codex-web advance is part of D's exact owning graph.

No database migrations in K/D/E. New state 2/artifact/connection-lease 1 are
intentional final contracts; unpublished draft formats have no adoption path.
K/D source branches are published; E is committed locally but GitHub rejected
two feature pushes with Internal Server Error. No installed package was activated, no real
portable/managed cluster has been launched, and no default integration, release
or production consumption is established. Consumption to date is synthetic
private test state and tiny metadata derivations. Local containing refs are
provided; live production provenance is not independently certified. Require
explicit whole-branch obsolete-history and migration/state-lineage conclusions.

## Quick evidence

K clean93 canonical `nix develop --command bin/check` passed (~52 seconds).
Runtime20/112, mocked closure12/51, pinned OSVM driver4/20, export4/18;
Node connection/artifact/proxy checks and retained contract suites passed.
Standalone profile11 pure assertions, four rendered scenario syntax checks,
strict 60-concept/120-variant inventory with 120 existing PNGs passed.
Receipts: kb-runtime-k-canonical* (see kb-runtime-k-result.md for exact names),
quick3/5/8 and frozen final2-source manifest. Failed/unused earlier harnesses
remain honestly recorded. Canonical runtime-source receipt
/nix/store/8h3aayb16fhr7h36r6gvwx5a824rh80k-vpsfree-kb-runtime-source.json
matches exact K93 and all 53 extant checked files. No bitmap freshness or VM
proof follows from these checks.

D final new-base quick: kb-runtime-d-upstream-quick1.*, all five gates0.
Focused Go10 top-level/15 pass events; full web276 top-level/510 pass events,
zero failures and two opt-in browser skips (TestNewSessionSettingsBrowser,
TestQuestionBrowser). Ruby dispatch13/95, zero failures/errors/skips. Original
EOF quick4 had21/211 on identical lease source; new-base Ruby selection is
recorded separately. Go1.26.6/Ruby3.4.9, Nix-only gem receipts. The supplement
was checked before commit with identical final bytes, not relabeled as a new
post-commit execution. Immutable D source is
/nix/store/y7r40b5h4hd44jfzan4kv1zar3rxmyyl-source with exact-source receipt.

E integrated six suites34/215 plus public dispatch5/58 =39/273, zero
failures/errors/skips. Receipts kb-runtime-e-integrated-quick1.*,
kb-runtime-e-public-quick1.*, kb-runtime-e-inputs1.*. Public composition uses
actual immutable D51 dispatch and K93 snapshot validators, with synthetic lease
processes. It covers peer/adapter/dispatcher and stdout loss, harmless stderr,
held guards and early cleanup inventory, not live guest SSH attestation.
Root verified all frozen bytes and final committed tree. Clean E d207 evaluation
kb-runtime-e-eval1.exit0 instantiates six default/compatibility/KB/contract/
metadata/source derivations with unchanged lock/source; no builds. One Nix
system-rename deprecation is recorded, not suppressed.

## Documentation, risks and later gates

Owning docs: K README.md, cluster/README.md, cluster/runtime-contract.md,
docs/webui-change-workflow.md; D docs/workspace-portal.md; E README.md and
new dev-clusters/kb/README.md. Root reconciled final English prose directly.
Temporary rollout/verification receipts stay here, not in feature docs.

Overall risk HIGH: persisted state, host processes/resources, credentials,
destructive lifecycle operations, cross-project protocols, compatibility and
rollback. Reviewer0 is the retained independent read-only reviewer at saved
gpt-6.1-sol/xhigh. Assign GENERAL, architecture/repetition,
scope/proportionality and risk/compatibility under mandatory-change-review.
No nested reviewers, edits, check/build execution, fetch, publication, lifecycle
or package activation. This packet requests final source review, not deployment
approval or visual artifact certification.

After resolving findings, fresh watchers may run package/install checks and four
separate standalone selectors using the generated original-Git-flake profile:
installed-layout, two-instances, resume-update, bilingual-capture. Require actual
nested KVM and genuine capacity; default reserves remain. Outer32Gi/8CPU/root128Gi,
96Gi free inside; host floor272Gi plus uncached closures/build space. Latest
host observation free disk269.6Gi is below that floor; it must be rechecked,
not bypassed. Local fixtures deliberately use portable QEMU DNS/example.test
because the outer guest has no dedicated bridge. Stop unexpected kernel builds.
Sentinels/checksums, all six credential identities, true changed closures and
explicit artifact output root are required. Two approved CS/EN IP-list PNGs
plus validated inventory/results/source receipt may later return to the original
K branch at unchanged V pin, with visual/artifact review; no secrets/transcripts.

No default integration, package activation, production KB writes, deployment,
legacy adoption/cleanup, generic OS changes or existing network-branch movement.
User requested development branches, with W-only PR exception. Earlier V/W/C/K
review limits remain separate, including W's accepted shared OPTIONS timeout.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/

Additional read-only CI observation: D run37639120229 is completed/success at
exact51aba080. The fast job evaluates all checks and builds every check except
host-module-idempotency; host activation VM job skipped by its branch policy.
Workflow source is .github/workflows/check.yml and raw metadata is
kb-runtime-d-ci-observation3.json. This supports package proof without claiming
the skipped host VM or future portable/managed guest execution.
