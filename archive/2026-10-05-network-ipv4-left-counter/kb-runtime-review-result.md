# Independent final portable-tooling review

Reviewer0 completed all four lanes at HIGH overall risk on the original exact
committed snapshots. Result: 0 Blocking, 2 Important, 0 additional Advisory.
The working K corrections were excluded and remaining reads used git show.
This report supplies no integration, activation, deployment or KB permission.

## Identity and reviewed objects

Current slug and trusted binding were independently verified; both shell markers
absent. Live roster confirmed reviewer0, ready review-purpose/read_only,
gpt-6.1-sol/xhigh, thread01a10c52-55c7-7490-8cd9-75efda7f00d9.
No overrides, nested reviewers, authorship, mutations or verification execution.
Assignment turn01a116ee-de11-7ab1-ab5b-959fc7bae9f5.
Mandatory skill, all four lane references, applicable workspace/repository and
routed guidance were read. All bases equal exact merge bases; fresh packet
binary diffs/checksums matched Git objects.

- K873758fd6aec0c03f50a94600e0ceab97946f255 to
  93a16d6cecb6bc847ec9335a3f170eb8b301ab56.
- D a2bbf2f1c588de7eec0d7d52580a89a9d4bef984 to
  51aba080b264c28f5584867b6cf006bf423ae2f3.
- E0ff827df13e82dfab4b536ff29979280f264e8f5 to
  d2079f605ae87871037ae73c5e5daf20a3e0d03d.

## Findings and dispositions

Both findings originate in GENERAL and risk/compatibility at K93a16d6.
Root confirmed and accepted both, assigning implementer0 narrow correction and
focused evidence. Neither is yet resolved. Details and current decisions are
in [kb-runtime-review-findings.md](kb-runtime-review-findings.md).

1. runner/capture.cjs30-31,59-76,81 and lib/artifacts.cjs124-136:
   independent artifactLease loss is ignored by orchestration. Its flock may
   release while the capture continues fixture work and publishes a retained
   snapshot, allowing a competing writer's artifacts/results to be overwritten.
   Closing the helper reports failure after publication. Bind liveness to
   cancellation/publication or retain writer-owned serialization, and cover
   actual controller loss plus competing writer. Reviewer source-only evidence,
   no reproduction. Original message b1490f73-7c03-47c3-88bd-9e73f6f9bf8e.
2. cluster/lib/kb_runtime.rb199-209,510-522 and await_ready326-330:
   update admits changed SSH endpoints while retained trust compares complete
   keyscan lines, including host/port prefix. It therefore predictably fails
   after predecessor stop, even with the same actual key. Reject changed resolved
   endpoints in preflight or deliberately support verified rebinding. Existing
   runtime fixture overrides trust, so real-boundary coverage is needed.
   Root selected early rejection, retaining same-endpoint source updates and
   documenting the restriction. Message03b832bc-6de5-4782-9699-2a6f4c7fcb52.

Architect0 has a bounded design clarification to assess physical artifact-lock
ownership during synchronous publication; this is not another independent
review. If correction adds a new authority/contract boundary, affected-lane
review is required under step10. Narrow fixes otherwise follow direct inspection
and focused checks under step9. No long verification is cleared yet.

## Complete history, migrations and lanes

K: a50f8c1a inherited exact V pin, then93a16d6 coupled launcher/capture. The
old implicit consumer cannot operate with the new state/descriptor/source
contract, so the coupled commit is justified; pin stays independently reviewable.
D: c582ee75 lease, then51aba080 deadline/test supplement. Upstream8f0f40a's
functional CAS fix is in base; preserved local draft is outside history, and
only helper/post-proof deadline plus deterministic tests supplement it.
E: ce970275e7209616a5ebc1a6d3f49c35e49a55c6 declarations/generated lock,
then d2079f6 provider logic/docs/tests. First commit preserves baseline flake body.
No repeated input stream, fixup, obsolete committed approach, transitional
migration or unused compatibility path remains in these reviewed histories.

No database migrations in K, D or E. K directly introduces final root-bound
state2/artifact-connection-lease1; E binding1. Legacy/draft formats are refused
and left untouched, recreate-only. D inherits its generic lifecycle schema.
Reviewer concludes sound direct lineage for this supported predecessor boundary.
Local refs establish K/D feature publication and local E, not default integration,
release, activation or production consumption. Absence of external consumption
is not independently certified.

Architecture: one K engine, fixed E CLI for mutations/live operations, pinned
noncreating snapshot validators for reads. Creation provenance differs from
capture readiness. Managed descriptor changes only control.argv and verified
readiness digest C to M; canonical C remains intact. D/E pipe layers protect
distinct lifetimes, maintain outer guards and reap their own children, with
critical stdout loss versus harmless stderr EOF. Early positive cleanup inventory
avoids recursive session locking; reset remains guarded. Actual generic
cleanup/transition/executor consumers were inspected. Synchronous lost-CAS proof
rereads under one guard/deadline; background may discard stale proposals.

Composition: E K45/D17 graphs independently equal owning locks; five unrelated
roots preserved. K keeps exact V5d5527a6 and effective OS6bdf458f. Actual pinned
OSVM confirms retained-root subclass and integer multicast behavior. No OS
change/coordinated production-node upgrade. Scope mechanisms serve accepted
requirements; no concrete speculative abstraction or rule duplication found.
Trusted local D/E operator boundary retains remote/guest and ordinary integrity,
concurrency, recovery and publication requirements. Accepted resource race after
owned stop can fail an update stopped and is not an additional finding.

## Evidence and remaining gates

Reviewer inspected receipts, not executions: K canonical runtime20/112,
closure12/51, driver4/20, export4/18, Nodeconnection12/artifacts4, profile11,
four rendered scripts and strict60/120/120 existing PNG inventory; all53 extant
changed files match K93 metadata. D focused10/15 events, full276 passes plus two
opt-in browser skips/510 pass events; Ruby13/95 and immutable source match.
E34/215 plus5/58 equals39/273, no failures/errors/skips; all23 final bytes and
public source guards match. Final declaration/graph pure evaluation passed;
older integrated body stays equivalent. One system-rename warning retained.
These do not certify build/install, live guests or bitmap freshness.

After findings: actual package installation, guest SSH/closure import,
interruption recovery, disk/credential sentinels and live managed lease remain.
Four separate standalone selectors require genuine capacity/nested KVM; latest
269.6Gi free is below272Gi disk floor plus uncached working space. Update outage
and application-data downgrade limits remain documented. Two CS/EN IP-list PNGs
require real generation, allowlisted export, strict validation and visual/artifact
review. Existing V/W/C/K network/production/W-timeout limits remain separate.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/
