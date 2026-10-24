# Final Git/cache and eight-repository history review

No Blocking, Important or Advisory findings. The affected Git/cache deliverable
and complete eight final branch histories pass this independent final review.
No remediation or additional source review rerun is requested. The remaining
publication and runtime gates below still apply; this is not integration,
deployment or completed-runtime acceptance.

**Identity and method.** `dev-session current` returned
`2026-10-24-flake-update-downgrade-guard-replacement` in the bound directory.
Both DEV_SESSION identity variables are absent; the trusted binding names that
slug and `/home/aither/workspace/ai/vpsfree.cz`. Native `CODEX_THREAD_ID` is
`01a16da6-4cc0-7fd1-8b85-0933235d3dd0`, exactly matching live same-session roster
member reviewer0: purpose review, ready, saved gpt-6.1-sol / xhigh, read_only.
No model/effort override, fallback, nested agent or implementation authorship.

Read mandatory-change-review in full and all four lane references: general,
architecture/repetition, scope/proportionality and risk/compatibility. Applied
all four to the changed Git/cache boundary at HIGH risk. Read workspace AGENTS,
applicable routed procedures, all present repository-root AGENTS, the current
Git design, verification brief, packet, owner source inventories/reports and
quick evidence. IRC and org configuration have no repository-root AGENTS.
Inspected actual source, tests, owning docs, consumers and local Git, rather
than accepting packet assertions. Previous reports remain intact.

Only this new evidence report was written. No source/ref mutation, test/build
launch, network/authentication operation, claim, publication, default merge,
deployment or lifecycle action occurred. Lead-owned state, plan and active
verification utilities were left untouched.

**Exact complete ranges.** Independently verified all eight actual HEADs and
trees, clean index/worktree/untracked status, base ancestry, complete ordered
commit messages/series, final changed paths and byte-identical full-index binary
diffs against git-rework-final-source-inventory.json. Its reviewed SHA256 is
821181a5dad2340b149f1013846cf1430c8373bec8258c881da49caf6bc833ab.

| Repository / target | Base | Reviewed final head | Commits |
| --- | --- | --- | --- |
| confctl / master | cc40679d267165aecfa569128438bb55fe910268 | 822c0e35dbe2549111912f539116b4225dfd3035 | 2 |
| haveapi / master | 7ac977a26080d45d44b6608aafad2cadd2ec7f81 | c7bfc1aa5af956b6057be8e623f9035c00ccb268 | 1 |
| terraform-provider-vpsadmin / master | 2a2c1055302f86f8e250f1d7e4c331d62012efe8 | c3f20203a5ba6200d0ff6b77f500bff6473f2c11 | 1 |
| vpsadminos / staging | e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854 | 889f14e5f964c85eac0dbffdff96909a46ab35c6 | 1 |
| vpsf-status / master | 587cd65bb02e6dddea7f6b6409e42a15f36ab4fb | 018b700f06cf216a125a70ac9bfedddaabf07b92 | 3 |
| vpsfree-irc-bot / master | 94ac4eb5a7caf0456fff7df86a44cae198463276 | 0a160463a4ee12ec5f6c45e38eaba11592787d9f | 1 |
| vpsfree-cz-configuration / master | 50d263d4127c05163d660fae1c4b9b887584032d | 5f0f4466adb175ed4fcac9b6d5c8909e87a1fec1 | 1 |
| vpsadminos-org-configuration / master | 6b04b48e9c076e5525ccb7c38ce174232414f0b5 | ca96c95a1fee04793468785d8323a759615b2b4e | 1 |

Reconstructed the complete final deliverables from previously reviewed R trees
and independently inspected every changed R-to-new path. Actual Git confirms
the provider's 28-path final scope and 16-path R delta, and the consumers' 14
delta paths. Unchanged guard/graph/transaction/manual/metadata/Ruby source blobs
were checked directly, including LockGraph, GuardedUpdate, Updater, FlakeLock,
FlakeLockDiff, input CLI surfaces and the package wrapper/environment spec.
This supports retaining unchanged conclusions from review-report.md,
review-followup-report.md, review-r-report.md, review-status-metrics-report.md
and review-haveapi-refresh-report.md; those historical reviews alone are not
proof of this new backend or package.

**General correctness and coverage.** At provider head 822c0e35,
lib/confctl/inputs/git_compare.rb:11 validates source components and immutable
SHAs and delegates to the owning mirror. Raw locked URL spelling matches
existing changelog cache keys while normalized source identity remains policy.
lib/confctl/git_repo_mirror.rb:71 requires exact commit objects, fetches missing
SHAs, and accepts forward ancestry only through Git's actual ancestor operation.
A negative result requires the complete parent walk before behind/diverged
classification. Nonstandard statuses, missing history and invalid caches remain
typed evidence errors, not policy rejections or acceptance. Equality retains
the intended no-work path. No API backend, fallback, token lookup, cherry-pick
equivalence or partial graph splice remains in the final implementation.

Read the real local-Git fixture specs and provider/guard/caller wiring tests.
They cover DAG/merge/revert/cherry-pick outcomes, exact object types, unavailable
SHAs, missing deep history, replacement refs, invalid cache forms, cold failure
and retry, warm/offline reuse, inherited Git redirection, ordinary fabricated
transport configuration, exception release and concurrent/reentrant locking.
Tests delegate Git semantics to actual Git rather than creating another graph
implementation. Existing transaction/error precedence tests remain applicable
through the unchanged source and narrowly updated provider doubles.

**Architecture and repetition.** Strict repository/evidence ownership stays in
GitRepoMirror, policy in ForwardGuard, and full graph/transaction ownership in
the existing components. No downstream resolver or ancestry implementation was
copied into consumers. The shared helper's sibling flock covers cold creation,
fetch, validation and reads (git_repo_mirror.rb:34); its Monitor supports the
same-instance setup/read nesting used by both actual callers. The two discovered
changelog callers, lib/confctl/inputs/commit_message.rb:48 and
lib/confctl/cli/cluster.rb:1529, hold the same lock across setup and log.
Changelog's existing soft failure cannot catch the earlier strict guard failure.
Locks end before commit hooks. Small per-workflow cache declarations are
appropriate repository glue, not duplicate security policy needing extraction.

**Scope and proportionality.** Reusing the existing exact-URL SHA256 full-mirror
cache is a bounded implementation of the requested rework. Git owns ancestry;
there is no generic provider framework, API fallback, partial-clone subsystem,
new source-fetcher contract or dependency-selection change. Cache validation,
atomic installation and the two caller locks address actual shared storage and
proof requirements. The owning input guide and manual explain cold-cache cost,
strict failures, recovery and limits; rollout identities stay in session records.
No unrelated application, module, deployment-tool or runtime pin update appears.

**Risk and compatibility.** git_repo_mirror.rb:113 installs a validated cold
clone by rename, leaving failed attempts nonauthoritative. At :130 it rejects
wrong origins, nonbare/invalid caches, shallow/graft/alternate/common storage,
partial/promisor configuration and symlinked object storage. At :191 it confines
repository/object redirection isolation to Git children and disables replacement,
lazy-fetch and commit-graph shortcuts. Ordinary Git URL rewriting/authentication
and caller Ruby/BUNDLE state remain available. Errors omit transport stderr and
identify the cache only by safe digest. This is not a hostile-same-user cache or
arbitrary-hostile-Git-configuration security boundary, as documented.

Inspected all seven final workflow bodies and their helper/docs deltas. Each
selects exactly one external CI tool at 822c0e35; all runtime flake locks remain
unchanged. Five workflows gain restore/save pairs, the two configurations reuse
their existing pairs, and all seven save under !cancelled(). That condition is
confined to save: no cache-hit bypass, continue-on-error, failed-validation push
or failure masking was introduced. Each ordinary push remains after validation
of committed HEAD:flake.lock against the original baseline. Selections, subjects,
hooks, tests and configuration shell boundaries remain those previously reviewed.
Existing workflow GITHUB_TOKEN declarations remain; the ancestry provider does
not read them. The owner's official action compatibility receipt supports cache
v6 on these hosted runners; I made no network/version recheck.

**Complete history and repeated pins.** Provider guard commit
550717765d58e9f28d960ea5bca3459ace86eb9e introduces the final Git design directly;
the obsolete API provider is absent even from this first final feature commit.
Separate commit 822c0e35 fixes the independent pre-existing packaged Ruby startup
defect. Its actual stable patch ID remains
28c777b2e44b88a2757213ac112b4bcfacdd0504, equal to R. The final provider tree is
e004bb150090777e53d9796011f191a7ba80fd4a, independently equal to the owner's tested
preconsolidation tree. The two logical commits are justified.

Status retains adoption 99c64d1080818c9f3da0f75fed117909fc7dd214, independent
baseline vendor-hash/Perl fix 79321b0e0d8486beef85bf8ce78f2742726dbcf3, and
independent existing metrics-test compatibility fix 018b700f. The latter two
actual stable patch IDs equal their previously reviewed R-series counterparts:
a991b51e941de6b6d282c731596336655b17cdf8 and
5c26de3c554767187f74a069e8a564ead2781aed. These separately useful baseline fixes
justify three commits; they are not repairs of the adoption. Six other consumer
branches each contain one coherent adoption commit. Messages explain final
behavior and rationale within repository conventions.

No obsolete API approach, fixup, redundant repair, transitional shim or P/Q/R
repin history remains in any complete final range. Independently grouped the
seven CI-tool update streams: actual Git history changes CONFCTL_FLAKE in exactly
one adoption commit per repository, with one final 822c0e35 selection and matching
owning-doc links. Superseded updates are consolidated, not retained because they
were once reviewed, published or tested. No other repeated dependency stream is
introduced. All eight flake.lock blobs, and applicable Go module blobs, equal
their bases; both configuration deployment-tool pins remain intact.

**Source preservation and migrations.** No migrations: no database schema,
lock format or on-disk mirror format transition exists in these complete ranges.
New sibling locks do not migrate existing mirrors. New cooperating callers may
share them concurrently; old binaries/manual writers must reuse them sequentially.
No released, deployed or externally retained runtime-state boundary requires an
intermediate migration, repair or pin commit. R's CI/local source consumption is
real provenance, not a default merge or production deployment.

Independently verified local provider preservation ref
refs/heads/2026-10-24-flake-update-downgrade-guard-replacement-provider-r-evidence
equals exact R 5436d3d7c36d3d5174eab3c44e3578830749d3db. Each consumer's local
before-git-cache-rework backup ref matches its inventoried R head, whose actual
workflow selects R once. **Before replacing the published provider feature ref,
the lead must preserve and verify that exact R under the remote evidence ref.**
This preserves old published consumers' source reachability without redundant
shipping history. No fresh remote state or completed remote preservation is
claimed here. Publish the new provider before its newly pinned consumers.

HaveAPI's complete range intentionally retains accepted base 7ac977a2 and the
previously tested 74f source as historical evidence. Later unrelated default
1103 movement is deferred to separately approved integration preparation; this
review makes no current-target ancestry or future integration-readiness claim.

**Evidence limits and remaining gates.** Read the passing quick receipts:
147 distinct focused provider examples (86 + 36 + 25), final 32 mirror examples,
12-file lint, man generation and ordinary hooks; consumer C40/D20 fixtures,
98 cache scheduling scenarios and 14 negative controls at the final pin. The
cache scheduling fixture models GitHub Actions semantics; it is not an actual
cache service run. The provider's 203-example manifest is dry-run discovery,
including both package cases, not a successful actual package check. Failed
fixture/hook/preflight attempts are preserved and distinguished from final passes.

After lead acceptance of this report, retain the planned gates from
git-mirror-verification.md: actual immutable package/exported suite with zero
failures/pending and complete source/input/Git/Nix/Ruby identity; real IRC and
both configuration caller/hook environments; all seven selected guarded updater,
commit and final-lock paths; one shared genuinely cold cache followed by proven
warm reuse, with additional cold mirrors recorded honestly; and an actual local
target-movement/nonforce rejection followed by fresh-baseline retry. Preserve
rooted package outputs and exact publication receipts. Those seven runs are
selected paths, not complete workflow reruns. Historical R dependency/build/VM
passes remain limited to their recorded components and inputs; this rework does
not itself require unrelated refresh/build/TF8 repetitions. Relevant failures
may require further checks through the lead.

Accepted residuals are full-mirror cold disk/time cost, visible fail-closed
handling of invalid or unavailable history, no automatic invalid-cache repair,
and unsupported concurrent old/manual writers. Existing source/graph policy and
the distinction between ancestry and semantic preservation remain in force.
This gate permits the planned feature publication and longer verification after
lead acceptance; it never grants default integration, deployment or cleanup.

All eight exact heads and clean states were rechecked at completion. Prior
reports and unrelated tracking changes are preserved. Lead retains fix ownership
routing to provider/consumer owners if later evidence reveals a defect.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/>
