---
lifecycle: archived
---

# Current status

Merged and SSH-pushed to vpsfreecz/vpsadminos `staging`: exact final head
`05201326975fc19d20a545c52f651cce0420dbc9`, with remote feature at same head.
Fresh fetch/ancestry and ls-remote verify exact integrated head. Ordinary
fast-forward merge and pre-push hooks passed in prepared environment.
Repository claim `23ca3475-fa2b-4e58-a7ad-5e0aa057d878` acquired only after
preparation, verified held, then released immediately after push/proof; final
authoritative state released. No uncertain operation remains, no deployment.

Authentication correction: missing agent was an unsupported diagnosis. Existing
unchanged regular id_ed25519 file authenticated directly without agent in the
bounded debug check. Lead's ordinary fetch, feature lease-push and staging push
all then succeeded. Earlier publickey denials were real but cause remains
unknown/transient; no auth configuration/credentials/services changed, and
there is no evidence linking the failure to Ruby/Nix GC. No operator action
needed. Previous blocked-state paragraphs below are historical preparation.

Current verification: refreshed-head RSpec CI passed on both staging
(run 41072754356) and feature (41072532391). RuboCop CI on both branches
failed before lint at the already diagnosed inherited Ruby3.4.0/ubuntu26.04
archive mismatch. Local lint/hooks passed. Full CI run 41072532280 remains
in progress, currently Build toplevel closure (started 14:45:06Z); seven prior
checks passed. Fresh Luna/low watcher retains monitoring ownership. No failure
has been reported for that run, and no deployment has been performed.

User approval "merge it" covered vpsfreecz/vpsadminos staging. Equivalent
rebase preserved the reviewed patch; exact old/new ranges and independent
reconstruction evidence remain in review.md. No implementation or integration
work remains. Next action: account for the full CI result when available.

Read-only investigation complete. Root cause: queued miss
processing recreates a pruned container record without `last_hit`; pruning then
compares nil with a timestamp and crashes the entire daemon. Both observed
incidents were followed by supervisor restart within a second.

Evidence: [incident analysis](design.md) and [source proof](source-trace.md).
Accepted correction: only hits create tracking records; misses for missing
records are no-ops under the existing mutex. User approved integration into
`vpsadminos/staging`; deployment remains unauthorized and unstarted.

## Phase checklist

- [x] Verify exact session identity and inspect retained team/access.
- [x] Assign architect investigation with bounded read-only scope.
- [x] Locate exceptions and prove node23 attribution.
- [x] Trace implicated source and establish root cause/impact.
- [x] Reconcile findings and prepare operator explanation.
- [x] Implement focused correction and regression tests (implementer0).
- [x] Pass quick checks/hooks and commit all intended changes (implementer0).
- [x] Independent final review and whole-branch history inventory (reviewer0).
- [x] Publish feature branch and account for applicable CI (RSpec passed;
  inherited RuboCop runner setup failure documented).
- [x] User-approved vpsadminos/staging integration and exact remote proof.
- [ ] Account for automatically triggered refreshed-head CI (watcher assigned).

Deployment is not requested. Independent final change review now applies to
the implementation. Prior investigation findings alone did not require review.

## Evidence and constraints

- `dev-session current`: `2026-10-30-osctld-oomd-investigation`.
- Both environment markers match the bound session and workspace.
- Live retained roster: architect0, implementer0/1/2, observer0, reviewer0.
  Architect and implementers have saved workspace-write access and are ready.
- First assignment briefly refused because another dev-session command held the
  session mutation lock. A subsequent ordinary retry succeeded; no bypass used.
- Shared workspace contains unrelated dirty paths; preserve them.
- No project worktrees or feature branches created, no production mutations.

Next action: account for post-push CI results via fresh Luna/low watcher
`merged_ci_watch`; exact merged head is already proven remote. No deployment
requested. Session remains open and active while CI accounting is pending.

## Implementation branch

Final preparation handoff: implementer0 stopped all repository mutations and
handed exclusive Git writer to lead. Receipt: `integration-preparation.md`.
Both feature and detached target clean; normal target hooks/environment ready.
Refreshed focused14/14 and component41/41 pass with exact restored patchedRuby;
scoped lint/Overcommit pass. No running check or preparation operation remains.
No usable current-user SSH agent/socket/systemd/tmux environment was found.
No credential substitution, peer access, service change or further SSH retries.
Remote feature last proven at original4642beb9c; failed fetch preceded any push.
No repository claim acquired; request JSON is prepared but unsubmitted. No
default branch mutation. User merge approval persists for resumed integration.

Refreshed checks confirmed 14/14 and 41/41 with restored exact patchedRuby.
Publication currently blocked by SSH authentication change: member and lead
shells have no SSH_AUTH_SOCK; GitHub SSH returns Permission denied(publickey).
Member's first final fetch failed before any effect. Feature local is clean
052013269; remote last known 4642beb9c; target local clean a5ad. Implementer
investigates only existing current-user agent environment/socket, no credential
substitution or peer access. No claim, merge/default push or production change.

Refreshed verification complete (implementer report): exact original patchedRuby
output `z30vypx0r6mgbfs0a86m6vd3s7pk07sb-ruby-3.4.11` restored with local root;
focused/component test operation exited 0. Source head remains equivalent
`05201326975fc19d20a545c52f651cce0420dbc9`; independent refreshed history and
equivalence review passed with no findings, preserved in `review.md`. Lead also
verified complete diff bytes match original reviewed range. Target detached at
a5ad, clean, actual post-merge/pre-push hook setup exits 0; feature lease-push
in progress before repository claim. No further checks/setup selected.

Feature refreshed without conflicts onto a5ad: new head
`05201326975fc19d20a545c52f651cce0420dbc9`. Implementer range-diff shows
`4642beb9c = 052013269`; old head retained in backup ref. Component shell setup
completed; two missing root hook gems restored normally. Plain component Ruby
cannot load libosctl native extension (known missing timer-symbol export), so
implementer is restoring exact patchedRuby only, without broad root rebuild.
New quick-check result and final hook environment recipe pending. No claim or
default mutation. Original reviewed range/evidence remains preserved.

Merge preparation found target movement before any claim: fresh staging
`a5ad64f818a7a208e5f2308295c14c6a776eea6d` differs from reviewed base
`8ce6234db194ccb934db724c7262aeab7fd26915`; feature local/remote remains
`4642beb9c37c558e1d0b74e285fecdda16d62eca`. Implementer is inspecting target
delta before proposing an equivalent refresh. No rebase/merge/push attempted,
no repository claim held.

Preparation intervention, unlocked: ambient rebase/hook trust refused before
feature ref change; detached integration target exists at a5ad but hook trust
needs normal preparation. Prior Ruby store path was garbage-collected, so old
Nix environment could not execute hooks. Implementer stopped exact owned Nix
client before rebase launched and is preparing smaller declared component shell
with existing gems via fresh watcher. No claim/default mutation; feature still
original reviewed head. Root rebuild expansion stopped where possible.

- Repository: vpsfreecz/vpsadminos, default/integration target `staging`.
- Branch: `2026-10-30-osctld-oomd-investigation`.
- Worktree: `worktrees/2026-10-30-osctld-oomd-investigation/vpsadminos`.
- Initial base: `8ce6234db194ccb934db724c7262aeab7fd26915`.
- Sole source/Git writer: implementer0; no independent second package is needed
  for this small fix. Architect retains design ownership, reviewer independent.
- Review risk classified high because daemon policy affects host/node behavior;
  general, architecture, scope and risk/compatibility lanes apply. Selected
  retained reviewer0 uses saved `gpt-6.1-sol` / xhigh, no override or fallback.
- User implementation direction does not authorize integration into `staging`
  or any production rollout.
- Regression specs drafted in existing `killer_spec.rb` before source edit.
  implementer0 uses a fresh retained-policy Luna/low watcher to prepare the
  repository Nix environment. Next checks: demonstrate old source fails, apply
  narrow guard, then green component suite and hooks.
- Lead acceptance inspection of pending diff: only `killer.rb` and existing
  `killer_spec.rb`, 101 insertions/1 deletion. Creation moved into hit branch;
  absent-record miss skipped inside mutex with brief invariant comment. Four
  examples use existing component harness/Fiber boundaries, no infrastructure
  or public-contract expansion. Verification/commit still owned by implementer.
- Root Nix shell preparation began unrelated ordinary package builds, no kernel.
  Implementer is canceling that owned setup before switching to component shell;
  this is environment setup cost rather than a failed product check. Monitor
  uses pinned catalog digest `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
  `gpt-6-luna`/low, full-access/never, matching retained session policy. Lead
  independently read the installed catalog/native utility configuration.
- Setup reconciliation: root `nix develop` actually completed successfully
  (exit 0, about six minutes) before cancellation took effect. No setup operation
  remains; prepared environment will be reused rather than starting another.
  `oomd-environment-setup.log` retains final success but one middle output chunk
  is explicitly incomplete. This log is supporting disposable evidence.
- Metadata refresh produced no remaining diff. Quick batch: original-source
  regression expected two failures, including exact nil/< prune exception;
  corrected focused specs 14/14 and complete osctl-oomd suite 41/41 pass.
  Batch took 107 seconds; final exit 1 was a root lint-launch environment issue:
  inherited component BUNDLE_PATH pointed root Bundler at a nested gem tree,
  while root GEM_HOME already held installed gems. Implementer will unset that
  variable for lint/hooks, preserving successful test evidence. No check utility
  remains running. Evidence: `oomd-quick-checks.log` (disposable supporting log).

## Implementation verification and final review

Committed head `4642beb9c37c558e1d0b74e285fecdda16d62eca`, one commit from
base `8ce6234db194ccb934db724c7262aeab7fd26915`. Final diff: two files,
+101/-1. Clean worktree, no migrations/dependency streams/transitional history.
Focused specs 14/14 and full component suite 41/41 pass after final test-only
lint adjustment (Kernel.system spy instead of subject-method stub). Scoped
RuboCop passes. Full Overcommit --run and normal commit hooks pass; reviewed
unchanged hook configuration signed normally. TextWidth warning at >72 chars
is non-failing and all lines meet workspace <=80 rule.

Full hooks took about three minutes. Implementer's attempted cancellation found
the owned process had already exited naturally 0 and committed; no signal
delivered, no running operation left. No repeat of successful checks needed.

Independent reviewer0 assigned all four required lanes for exact committed
range above, retained Sol/xhigh settings unchanged. Packet:
[review-packet.md](review-packet.md). Publication/CI remain in progress;
review must complete before readiness. No production deployment or integration.

Review completed: [review.md](review.md), no findings in any lane, exact
base/head retained. Explicit conclusions: no obsolete branch history, no
migrations and no repeated update streams. Lead persisted review because
retained reviewer instructions require read-only work. No remediation or review
rerun necessary. Portal comparison captured for exact reviewed range; fresh
SSH ls-remote independently confirms feature head and unchanged staging base.

Publication confirmed by implementer SSH push + `git ls-remote` at exact head
`4642beb9c37c558e1d0b74e285fecdda16d62eca`; fresh origin/staging remains the
same base. First ambient push failed pre-push signature context before branch
creation; push from prepared Nix environment passed without bypass or re-sign.
No source utility/command remains running.

CI for exact head: [RSpec run 41059850721](https://github.com/vpsfreecz/vpsadminos/actions/runs/41059850721)
passed in 10m21s (exit 0), followed by fresh Luna/low utility `oomd_ci_watch`.
All setup and suites passed; no check or observer remains running. Evidence:
`oomd-ci-rspec.log`. No retries or CI cancellations. RuboCop run `41059850756` failed in
`ruby/setup-ruby` before lint: requested Ruby3.4.0 download for ubuntu26.04 is
404; action says only newest3.4 patch is built for this runner. Lead inspected
failed logs; implementer is verifying unchanged baseline inputs and recent
staging behavior, read-only. No speculative workflow expansion or blind rerun.

Implementer CI attribution: base/head `.ruby-version` and `rubocop.yml` are
byte-identical (blobs `18091983f59ddde8105e566545a0d9e4a12a4f1c` and
`44346d2c88ed0fd1c00963e4275e3d98a5da1c9b`). Feature RuboCop used ubuntu26.04;
last staging success [40296454481](https://github.com/vpsfreecz/vpsadminos/actions/runs/40296454481)
used ubuntu24.04 with the same source blobs and setup-ruby action SHA
`7f797815d8adceb1c412e7abefdd1ab4abc47a5f`. That staging run linted 1,494 files
without offenses. This is latent inherited config exposed by runner rollover,
not evidence of an already observed failing staging run. Record this limitation;
fixing unrelated CI/runtime selection is outside the narrow requested change.

Final branch and history readiness: one reviewed commit, no additional source
edits or follow-ups after review; exact head published and portal comparison
captured. No migrations, no obsolete history or dependency update streams.
No long VM test required for this in-memory-only change. Review receipt:
[review.md](review.md). Local reproduction proves this fix prevents the exact
incident failure; production deployment has not been tested or performed.

## Initial findings

- Central `/var/log/remote/localhost/log`, 2026-10-30 13:26:51 CET, embeds
  `node23.prg.vpsfree.cz` and `osctl-oomd` attribution.
- Logged gem is `osctl-oomd26.05.0`, store prefix
  `fmzf8z0lf0bzg5pv3s5a5q2dpz3kpxil`; `Killer#prune` line 166 evaluates
  `ct.last_hit < Time.now - 300` after both hit counters are zero.
- Rsyslog routes parsed HOSTNAME to `/var/log/remote/%HOSTNAME%/log`.
- Architect is checking recurrence and restart impact; implementer traces how
  `last_hit` remains nil and will bound the proposed remedy.
- Initial plan/state committed as `5aa1e1c3e`; no declared workspace hook
  framework or active commit hooks. No unrelated index entries were staged.
- Same signature occurred at Oct 29 15:33:50.376 CET and Oct 30 13:26:51.279
  CET. Each traceback is rendered twice; there are two observed crashes in the
  bounded Oct 27–30 log sample. Both have replacement daemon PIDs within a second.
- Today's log shows `tank:27837` restart running from 13:15:21.950 to
  13:24:41.272, followed by bursts of zero-counter misses. This supports an event
  backlog triggering stale misses; exact interleaving awaits source reproduction.
- Source trace so far: CLI sets `Thread.abort_on_exception = true`; event
  processing constructs a container record even for a miss, while only a hit
  sets `last_hit`. Pruning assumes that timestamp exists.
- Full deployed Git revision is unverified: direct node SSH failed host-key
  verification, and no trusted alias was found. No verification bypass used.

## Investigation acceptance evidence

implementer0 loaded actual `killer.rb` and libosctl Queue from canonical bare
revision `49636f902704ce6019a7a8ae47ec0b3ca6902f68`. Deterministic Fiber boundaries
reproduced two queued misses against an aged hit: first miss drains counters,
prune deletes the record, later miss recreates nil `last_hit`, next prune raises
the exact exception at line 166. A Ruby 3.4.9 child with
`Thread.abort_on_exception = true` exited 1 and rendered the traceback twice.
No worker/container commands or production changes were needed. Architect
reconciled the independent proof into the incident analysis.

Observed today: nine-minute restart delay and queued zero-counter miss bursts
support this trigger. The precise production interleaving and nil-record
container ID are inferred, not directly logged. `tank:27837` is a candidate.
Separate restart command failures were not diagnosed as the same bug.

Impact is transient OOM policy interruption and reset of in-memory hit history;
normal watcher output resumes after supervision restart. No additional lasting
container outage is established. Project docs, independent final change review,
builds, CI and deployment are unnecessary for these incident findings alone.
Tracking remains in this directory under the normal checkpoint cadence; initial
commit is preserved, later findings are current working-tree records.
Lead inspected both completed evidence files and confirmed `git diff --check`
passes for the owned tracking directory. Saved proof includes exact local source
revision/blob, file/line chain, reproducer and limits; no pending specialist work.
