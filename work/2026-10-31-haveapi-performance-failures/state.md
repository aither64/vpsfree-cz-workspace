---
lifecycle: active
---

# 2026-10-31-haveapi-performance-failures

## Status

- Implementation preparation. Investigation complete; user approved implementing/verifying the narrow new-branch no-work solution and merging into HaveAPI `master`.

## Phase checklist

- [x] Verify exact session identity and retained roster.
- [x] Diagnose failed current-master workflow jobs and compare available controls.
- [x] Record evidence and minimal proposed solution.
- [x] Lead acceptance inspection and user handoff.
- [ ] Implementer0: resolver, regression specs and documentation committed; quick checks pass.
- [ ] Reviewer0: independent final branch review, history and migration conclusion.
- [ ] Longer verification/feature CI as appropriate.
- [ ] Lead: approved fast-forward merge into HaveAPI master, remote proof and claim release.
- Deployment/release: unnecessary for this CI-only fix.

## Next actions

- Commit initial session records, then assign the complete design.md package to implementer0 (retained Sol/xhigh, ready, workspace_write). One package suffices; other implementers have no independent work boundary.

## Integration approval

- User's current follow-up: "agreed. implement the fix, verify and merge" authorizes HaveAPI `master` integration of the accepted solution after verification. No other repository/default or deployment is approved.

## Documentation

- `plan.md`: authorized scope and owners.
- [design.md](design.md): accepted architect-owned findings and prospective fix/verification brief, including exact run/source links and verification limits.
- No project documentation changes planned for this investigation.

## Repositories

- HaveAPI: read-only upstream/canonical repository inspection; no feature branch/worktree registered.

## Commands run

- `dev-session current`: `2026-10-31-haveapi-performance-failures`; environment matches trusted thread binding.
- `dev-session team list 2026-10-31-haveapi-performance-failures --as-is`: retained Full team with architect0 ready, workspace_write, Astra/xhigh; four implementation-purpose members ready; reviewer0 retained Sol/xhigh.
- `dev-session team assign ... --to architect0 --message-stdin`: investigation assignment accepted.

## Results

- Current remote master reported as `0e7166a0f8f15827bfac051666a53bf449e999ec`.
- Lead verified run `41056402034` on that SHA passed both endpoint comparison and performance gate (2026-10-30).
- Architect found failed run `41056909892` on the same SHA through exact-SHA lookup; branch-only query omitted it. Do not infer current health from the passing master-branch run alone.
- Failed run was the creation of `refs/heads/haveapi-0.32`: `before` is forty zeroes, `after` is the current master SHA. Its artifact error is `HaveAPI::PerformanceCI::Error: Baseline and candidate must differ`. Resolver selected merge-base(candidate, captured default), which equals candidate, then rejected equality before relevance/no-work handling. No benchmark assertions ran.
- Proposed fix: allow only validated quick zero-before branch pushes with merge-base equal to candidate to produce `relevant: false` and explicit no-work evidence. Preserve lineage/source checks, ordinary equal-pair rejection and campaign distinct-SHA requirement. Existing workflow already records `outcome=no-work` and accepts it in the gate.
- Lead acceptance reads: `utils/performance_ci.rb`, `.github/workflows/servers-ruby-performance.yml`, `servers/ruby/spec/performance/event_baseline_spec.rb`, all at exact SHA `0e7166a0f8f15827bfac051666a53bf449e999ec`. Existing spec explicitly expects rejection of this new-branch case, so regression coverage must change with the proposed fix.
- Architect verified passing run's actual report: `status=pass`, all 14 workloads pass wall/CPU/allocations; all-client contract: 214 examples, 0 failures. No other failed workflow found in exact-SHA inventory. This is quick-profile evidence, not weekly or production verification.
- Historical master run `40529570313` failed with response-identity ContractError, already addressed by master ancestor `4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`; following run `40547615707` passed. Separate from the current new-branch resolver error.
- Review exemption: deliverables are routine investigation/findings/session evidence only; no substantive project change. No local checks, reruns or deployment performed.

## Open questions

- No unresolved design blocker. Implementation/review/check results pending.

## Cleanup

- Session remains open. No lifecycle actions, feature checkouts or machine reservations requested.
- Raw downloaded artifact locations are listed in `design.md`; durable evidence is summarized there. No tracking commit required before project-code commit/external mutation because neither occurred.
