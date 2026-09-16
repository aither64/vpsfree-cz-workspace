# Mail grammar, campaign counts and member navigation review

All four required lanes reviewed vpsAdmin `bb1dc5068`, notification overlay
`f275bf35a` and KB contract `32b01694` using fresh gpt-6-astra reviewers at xhigh.
General and architecture used collaboration agents. Risk and scope used fresh
read-only ephemeral Codex processes after the collaboration thread limit was
reached. No reviewer delegated work.

General and scope reported no findings. Architecture reported one advisory:
count-query cost grows with campaign histories. A 501-row API probe passed;
loading its counts took 3.030 seconds / 2,025 SQL notifications in Index and
2.893 seconds / 2,022 in Show. Batching bounds memory; it does not make the
existing protection queries constant-cost. Retain the shared evaluator and
record this cost for the expected hundreds of allocations. Larger histories
need measurement before introducing an optimization. No new locks, persisted
counters or separate eligibility classifier were added.

Risk reported one Important issue: HaveAPI can serialize an expanded campaign
inside a request response without running Campaign.Show. Plain count readers
therefore returned null in that path despite declaring non-null integers.
Remediation adds lazy initialization in the three count readers while retaining
explicit refresh for direct Index/Show responses. A regression requests
`/ip_release_requests?_meta[includes]=ip_release_campaign`, checking all counts
and the model regression verifies exactly one evaluation for all three readers.
Focused API/model verification passed (two examples, seed31587); the final
spy-style model check passed (one example, seed49910). Ruby lint passed.
The initial test used a repository-forbidden any-instance expectation; it
was replaced with a concrete-instance spy before committing.

This directly fixes the reported serialization path without changing the
reviewed public contract or design, so the mandatory-review workflow requires
focused verification rather than a new review round.

The six prerequisite patches and the independent fixture correction are
unchanged. The matched KB input preserves the previous OS/nixpkgs revision.
Remediation is folded into vpsAdmin `58a9b71ea` (API `dc483b57a`); WebUI
`a8fa57999` and the ninth fixture patch are unchanged by range-diff. All commit
hooks passed. Exact KB pin `2e5cb3b0` passes the full local contract check.
Services rollout and live admin/member checks passed, with the pre-update
campaign records, quotas and PTR records preserved. The isolated full browser
flow passed all five tests in 8.6 minutes, and the full runner completed
successfully including teardown.
API Specs35107887309 completed successfully: all 26 topics and coverage passed.
KB managed runtime35108117644 passed. Every final-head workflow in all three
repositories is successful; no outstanding finding or validation failure remains. No screenshots were generated.

Final workflow evidence: [vpsAdmin API Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/35107887309),
[overlay Check](https://github.com/vpsfreecz/vpsfree-notification-templates/actions/runs/35105328791),
[KB Check](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/35108117525)
and [KB runtime](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/35108117644).
The live review cluster and session remain open.
