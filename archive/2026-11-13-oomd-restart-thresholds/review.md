# Independent final review

Reviewer0 returned this review through report_to_lead; lead saved the report
because the retained reviewer is read-only. Completed 2026-11-13 around 21:20 UTC.

**Findings: none** (no Blocking, Important or Advisory findings).
Review passed for the exact committed range. Required post-review node25 build
and actual generated JSON inspection remain gates before integration.

## Identity, method and range

Reviewer verified exact session identity and roster: reviewer0, thread
`01a1d6b6-f705-7bd3-b80c-5bf152be0663`, review purpose, read_only,
saved `gpt-6.1-sol`/xhigh, ready. No override, fallback or nested reviewer.
Directly used mandatory-change-review and all four complete lane references:
general, architecture/repetition, scope/proportionality, risk/compatibility.
High risk classification is solely due to host/node behavior.

Repository `vpsfree-cz-configuration`, target master:
`1a948a872f84bdb4643926b357cf15534de1d313` →
`08d68a85f24a95b70b2d806f995f04b236e4d89a`.
Verified merge base, entire one-commit range, exact clean HEAD/worktree, complete
commit/message and final diff, repository AGENTS/README and quick/hook logs.
Independently repeated full-range `git diff --check` successfully. All quick
checks pass; nonfatal 72-column message preference warning meets the 80-column
repository rule.

## Scope, correctness and risk conclusions

Five additions at node25/config.nix:110 implement exactly 4 restart hits and
1.5x median. This is the smallest conventional node-local settings block.
No shared/default, daemon, input/lock, API or other-node changes. One logical
commit is appropriate; no new subsystem or speculative hardening.

Reviewer traced production channel/flake/lock to vpsadminosProduction
`c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`, inspected module, source-gem
selection, CLI, watcher, host-load buffer, killer, CtTop and relevant specs.
Eight implementation/packaging contract files in
`/nix/store/yb3qniksa7pklfiy7fzqb3avxxldhh3d-source` were independently
compared byte-for-byte against the exact Git revision.

Existing freeform JSON supports both values and normal merging retains verbose.
Explicit restart_hits is independent of stop_hits. Host activation is one-minute
load >= median * 1.5; source defaults are 2.0 and 8 hits. Sampling, CPU/memory/rank
guards and 40 stop hits remain. The lower gate can advance stop-score accumulation;
successful restarts do not clear it. Scores accumulate/decay rather than requiring
consecutive rounds. These consequences are recorded in the design.

No security/compatibility defect found within scope. Conventional component
ownership, no duplicated policy or new cross-project contract. No fleet update,
migration, protocol or persisted-format transition. Restoring settings cannot
undo completed container actions.

## Whole-branch history and documentation

Complete history directly introduces final behavior in 08d68a85. No obsolete
approaches, fixups, compatibility shims or transitional migrations remain.
**No migrations**, so no migration merge/release/deployment/external-use boundary
to preserve. **No repeated dependency/channel/input/generated update streams**;
all pins/locks unchanged. Baseline pin advancement predates this feature range.
No consolidation needed.

README remains the environment/build entry point. Existing options need no new
repository reference/runbook or link. Node-specific rationale, individual
verification and future operator recovery context appropriately stay in session
tracking, consistent with the repository's execution-receipt prohibition.
Module/daemon remains the supported-semantics owner. No moves, removed anchors,
upgrade retirement, lost recovery contracts or weakened facts found. Design
distinguishes future operator checks from executed results, preserves rollback
limits and discloses the unverified running baseline. No additional repository
documentation useful for these two existing settings.

## Residual verification and disposition

Require the real node25 build and its generated config to be exactly
`{"load_multiplier":1.5,"restart_hits":4,"verbose":true}`; retain exact system,
config and input paths. Build/generated-config validation has not yet completed.
No live baseline, activation or runtime response verified; those are outside
configuration-only scope. Lead owns final fresh target/history checks and
approved integration. No source edits/builds/access/deployment/claims/lifecycle
actions were performed by reviewer. Session remains open.

## Coordinator's subsequent verification and integration

Required node25 full build was attempted and failed solely on the absent external
initrd SSH key; no system output was realized. Accepted bounded V then projected
the actual confctl activationScript context and traced unique etc → oomd-run →
JSON direct derivation inputs. Parsed canonical structured JSON equals exactly
4/1.5/true, including types and no extra keys; no evaluator copy, fake secret or
source change. See [implementation V](implementation.md#package-v-focused-canonical-json-verification)
and [state](state.md) for exact graph/outputs/input identities and unsuccessful
full-build evidence. This proves the merged settings, not a built or running
node. Lead accepted this limited environment coverage with the full-build gap
explicit. The reviewed source stayed unchanged; no review rerun was needed.

User-approved exact final head `08d68a85f24a95b70b2d806f995f04b236e4d89a` was
fast-forwarded and SSH-pushed into master with hooks. Fresh remote equality proved
both master and retained feature ref at that head. Repository claim released and
verified; no deployment or machine ownership. No history refresh/migration or
deployed-lineage substitution occurred.
