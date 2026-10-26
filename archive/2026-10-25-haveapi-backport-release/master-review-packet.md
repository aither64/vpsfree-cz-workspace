# Master-first final review packet

User explicitly directed fixes to master first, then backport. Scope is HaveAPI
master feature `2026-10-25-haveapi-backport-release-master`, worktree
`worktrees/2026-10-25-haveapi-backport-release/haveapi-master`, base
`38ecca75edaf797d048fb36c6a50ea7e05eb50a9`. No .2 metadata on master.

This is the coherent B tooling adaptation already reviewed within superseded C,
plus narrow corrections of original hosted CI failures. [Original final review](final-review.md)
remains historical exact-range evidence; [CI diagnosis](ci-failure-diagnosis.md)
retains failure logs/artifact and concrete causes. [Current design amendment](design.md#current-amendment-master-fixes-first-then-backport)
is authoritative. Final committed head, complete series/diff, quick results and
input evidence will be appended before assignment.

Review the complete master branch/history, reusing prior accepted runtime/B
conclusions where unchanged. Same independent reviewer0 saved Sol/xhigh;
High risk, general/architecture/scope/risk lanes apply, no nested review.
Focus changed correctness boundaries: deterministic complete binary tree delta
with full index IDs under short-abbreviation Git config; ordinary master/literal
ancestry without maintenance objects; portable owned shallow/component tests
without root lock/history assumptions; all previous raw/replay/negative gates.

Canonical unchanged-tree proof serialization is9374 bytes, SHA256
`0a008acbb46434a0914421064149ce154ea41a6e82a29022c53e666eb2066fd5`.
Original reference and four tree IDs/mapped ancestry/budgets remain unchanged.
No runtime/fixture/public API/schema changes. No migrations. No repeated external
input/pin updates; local source fixups should be folded into final coherent
master commit(s). Source origin B and old C retained in evidence; this is now
its upstream owning implementation, then exact integrated master commit will
be backported -x to A before one separate .2 metadata commit.

Master integration is explicitly user-authorized after review/checks/CI. No
release/default rewrite or tag/publication until final maintenance checks.

## Exact final master inventory

One commit `1741a25e1df45f06f9966942d5c34a97967ebb3e`: `performance: support portable release lineage checks`.
Base `38ecca75edaf797d048fb36c6a50ea7e05eb50a9`;7 files,+701/-19. Complete binary diff
`master-final-review.diff`, SHA256 `569d781ada30c537834683e298831d9195d18810f1989bb0ebec8bbe221b81bc`.
Source origin old B `d32aa0f35e2af0ff5053de54c3e1eae2ca385a62`; all local
fixes folded into final owning commit; no discarded iterations/repeated streams,
no metadata/dependency pin updates, no migrations. Master VERSION stays0.30.0.

Quick gates:98 performance examples/0 failures,52.16s seed58397 using component
lock only/root tooling lock absent; six changed Ruby files pass RuboCop. Complete
actual production proof passes abbrev4/7/12 canonical9374/hash0a008...; ordinary
master literal ancestry succeeds without maintenance probing. Normal hooks pass
after correcting reused GEM_HOME/bin PATH (first refused attempt made no commit).
Exact head clean; final shallow committed-source control result follows.

Committed-source shallow control passed exact1741: depth1, mapped object absent,
root lock absent;15 lineage plus1 strict missing-root-lock test pass. No install.
Actual full-history proof rerun exact1741 passes abbrev4/7/12; all handles stopped.
Logs/receipts: master-shallow-control.log, master-full-history-proof.json,
master-performance-quick.log, master-component-inputs.json.
