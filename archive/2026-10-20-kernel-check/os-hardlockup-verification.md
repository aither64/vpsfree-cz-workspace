# Current panic-policy package: normal sysctl declarations

User-directed v3 is complete and quick-checked at
`8528262315b0794a8f50917cf33c53a07fd14030`, on fresh staging base
`55c5046514d06fe9398a022c1622bdaae5228841`. Reviewer0 accepted the focused final revision across all four affected lanes,
with no findings; SSH publication has succeeded. The targeted activation package below is superseded and historical.

The full branch contains one coherent commit: `os: panic on lockups when crash
dumps are enabled (v3)`. Tree `ed8f0498c77a1fb673700065baabaf697cfefaab`;
source blob `2e6a906118374ba5a42b74e465ed1e0cd2b4b5ed`. The clean feature
worktree changes only `os/modules/misc/crashdump.nix`, seven insertions and one
deletion versus base. Native comparison binds this exact range. The former
14cdf head is unmerged, contained only by this session's feature refs, with no
known deployed pin consumer; its CI/cache records remain historical. Exact
backup `refs/backup/2026-10-22-kernel-check-targeted-activation` preserves it.
No migrations, state/API/protocol changes, pins, repeated update streams or
obsolete implementation commits remain in the proposed branch.

Under the existing crashdump-enable gate, normal sysctl declarations set both
`kernel.hardlockup_panic` and `kernel.softlockup_panic` to integer one. Both boot
arguments and the NMI hard-panic comment remain. The custom activation snippet,
helper and activation-specific option description are completely removed. No
generic sysctl service, activation mechanism or framework is implemented.

[Actual full-module evaluations](os-hardlockup-v3-eval.json) and
[assertion results](os-hardlockup-v3-check.log) passed enabled, disabled, paired
zero overrides and paired null omission. Generated sysctl text matches the
values; boot lists exactly match the prior accepted arguments. No custom hook
or target panic sysctl write exists in generated activation. No mock activation
or host write was run for v3. [Evaluation stderr](os-hardlockup-v3-eval.log),
[format/parse/whitespace/bundle checks](os-hardlockup-v3-quick.log), and
[commit/hooks](os-hardlockup-v3-commit.log) retain evidence. Normal `--amend -F`
hooks passed; message includes factual validation and v1/v2/v3 development
history. Only advisory 72-column warnings were emitted; all lines are <=80.

**Application limit:** NixOS's systemd-sysctl consumes the generated file and
its restart trigger. Current vpsAdminOS runit applies sysctls at boot stage 1;
ordinary live switches do not automatically replay these declarations. The
independent [lifecycle trace](hardlockup-sysctl-lifecycle.md) anchors that
comparison. Generic live application is a separate design proposal, not part
of this commit. No current configuration pin, runtime setting, deployment or
merge changed. Removing declarations does not reset already applied values;
future authorized rollout/rollback requires direct value verification.

Reviewer0's focused final review accepts this exact v3 branch, including the
paired soft declaration, hook removal, whole history, no migrations and no
repeated streams. This is separate from the older 14cdf acceptance. The old-head CI/RSpec batch remains owned while its exact 14cdf runs are
reconciled and, if still queued/running, cancelled under the lead's explicit
direction after replacement publication. No blind rerun or new test is selected.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/>

[SSH publication](os-hardlockup-v3-push.log) succeeded with an exact lease
against 14cdf; readback returned feature `8528262315b0794a8f50917cf33c53a07fd14030`
and staging `55c5046514d06fe9398a022c1622bdaae5228841`. The source worktree
is clean. Automatic CI status and stale-run accounting follow separately;
no CI success is claimed.

The superseded 14cdf batch is terminal and its utility has ended. Existing
RSpec `39744127815` succeeded (watch exit zero); CI `39744127896` was still
in progress on verified exact 14cdf and was cancelled only after v3 publication
under the lead's explicit stale-run authorization (watch exit one). Its OS build
had reached persistent-activation checks; no failed test result was reported
before cancellation. Pre-cancel/final metadata, full available logs, artifact
listings and watch exits are retained under `os-hardlockup-runtime-ci-<run>-`.
No old observer remains active.

Only [CI 39745935323](https://github.com/vpsfreecz/vpsadminos/actions/runs/39745935323)
was discovered for exact v3 head; a second bounded discovery found no separate
RSpec workflow for v3. One fresh retained Luna/low utility,
`/root/os_panic_v3_ci`, now owns observation of that existing run. It must verify
exact head, retain full output/status, report first failures and remain responsible
through completion without retry, cancellation, source edits or deployment.
The fresh utility confirmed session/env identity, native Luna/low selection
and inherited danger-full-access/approval-never execution. It verified run
39745935323 at exact head 8528262315b0794a8f50917cf33c53a07fd14030 and reported
in progress. No manual workflow or new test was launched. CI is pending, not
certified by older versions. A generic sysctl-on-switch proposal is separate and unimplemented.
The session remains open, with no merge, pin, deploy or runtime write.

## Historical v2 targeted activation package

The following prior package and its review/check/CI claims are retained history,
not current v3 behavior.

# Current OS hard-lockup policy package

Final source head `14cdf1caec606bb6bc88fcb32ac48f707f5dabb0` is complete,
quick-checked, accepted by reviewer0 and published over SSH. The [runtime final
review](os-hardlockup-runtime-final-review.md) covers all four lanes and the
complete refreshed branch; no unresolved findings remain. A pin-label advisory
was closed directly. Automatic CI is pending; the earlier review and CI below
apply only to historical boot-only `b81c43ff`. No manual long verification or
old failed-job rerun was selected.

Base is fresh-fetched `origin/staging` at
`55c5046514d06fe9398a022c1622bdaae5228841`; parent is unchanged. Complete
base-to-head series: one commit, `os: panic on hard lockups when crash dumps are
enabled (v2)`. Tree `70b0e11688686a490d5d81c96bba03250ec9f333`; module blob
`80566cb122af59df22540c195ea11de203b584ee`; clean worktree. Native comparison
binds this base/head. One file changes, 19 insertions/1 deletion. No migrations,
state formats, APIs, protocols, inputs, pin updates or repeated update streams.
Earlier f3e/b81c iterations are folded into this owner; exact backup ref
`refs/backup/2026-10-22-kernel-check-boot-policy` retains b81c and all earlier
receipts remain historical. No known downstream deployed pin consumes that
revision; its published automatic CI/cache output is retained, not erased.

The accepted [runtime supplement](design.md#runtime-hard-lockup-policy-supplement)
adds the hard-only sysctl declaration and targeted activation snippet under the
same crashdump-enable gate. Both original boot arguments remain unchanged. The
comment explains the NMI hard-lockup argument; the option description covers
activation. The command uses the final merged value, shell-escapes its complete
assignment, honors an override to zero, omits null and encodes false as zero.
It runs after `specialfs`, calls explicit procps sysctl for only this one key,
and is excluded from dry activation. Soft runtime policy, detector settings and
thresholds are unchanged. No general sysctl replay, new service or framework.

A failed write emits stderr and flows through the existing activation ERR trap
to a nonzero aggregate status. The current Ruby switcher ignores that child
status: a future rollout requires direct sysctl readback. The hook precedes
changed-service restarts and cannot certify crash-image availability. Disabling
crashdump/removing the declaration does not undo an already applied one; a later
authorized rollback must explicitly restore/verify zero or boot the old policy.
Mixed versions remain compatible; no coordinated fleet update or pin bump.
Nothing was deployed and no host sysctl was written.

Quick verification passed in `nix develop`: Nix formatting, parsing,
`git diff --check`, `bundle check`, active Nixfmt and commit-message hooks.
The commit used `--amend -F` with normal hooks and includes factual validation
prose plus v1/v2 history. The width hook emitted advisory 72-column warnings;
all lines satisfy the repository's 80-column limit.

[Quick output](os-hardlockup-runtime-quick.log),
[commit/hooks](os-hardlockup-runtime-commit.log),
[real-module evaluation](os-hardlockup-runtime-eval.json),
[evaluation stderr](os-hardlockup-runtime-eval.log), and
[isolated mock checks](os-hardlockup-runtime-mock.log) retain the evidence.
Full OS graphs covered enabled, disabled, explicit zero override, null omission
and false. Enabled produces integer one and generated text/command one;
override and false produce zero; disabled/null have no activation write.
Every boot-argument list exactly matches its prior b81c counterpart. No soft
runtime key is added. Complete generated dry scripts omit the target command,
and the full activation order places `specialfs` before the new snippet.

The inline isolated check extracted the real generated snippet and its generated
error wrapper/trap, replacing only the procps executable path with a temporary
mock. Exact `-w kernel.hardlockup_panic=<effective value>` arguments and both
success-zero/failure-seven results were checked for one, zero and false. Failure
sets aggregate status one and emits both the explicit error and generated
snippet diagnostic. No full host activation or sysctl invocation was executed;
there is no new repository test harness. Two local inspection assertions were
corrected for source-backed sysctl entries with null text and shell-quoted
assignments; these were receipt inspection errors, not product failures.

The independent [lifecycle trace](hardlockup-sysctl-lifecycle.md) explains why a
declaration alone was insufficient and anchors boot/switch/error semantics.
Configuration withdrawal remains zero-range at `37a338b25192d9271ee211110800c2dc6a094a57`.
The appropriate final review is reviewer0 at its retained Sol/xhigh settings,
covering general, architecture, scope and risk lanes for host-policy/rollback
behavior. No merge, pin, deploy, forced-fault or lifecycle action is authorized.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/>

The pre-publication remote check found staging advanced from 252b80df to
55c50465 solely by a Nixpkgs lock refresh (cd4ea8d5 to da6dc0e7). Rebase moved
unpublished 10f31e04c to current 14cdf1cae. [Range comparison](os-hardlockup-runtime-range-diff.txt)
proves an identical policy patch; source blob and commit message are unchanged.
The [normal rebase/signing log](os-hardlockup-runtime-rebase.log) records the
declared environment retry after the ambient hook signature refusal. No hook
was bypassed. The final real-graph evaluation on the refreshed input reproduced
all declaration, generated sysctl, snippet and boot-list values exactly; dry
exclusion/ordering and isolated success/failure mocks were checked again.
[Pre-rebase module output](os-hardlockup-runtime-eval-pre-rebase.json) is retained.
No new broad check or unrelated source change was needed.

SSH publication used the exact lease against remote b81c43ff, with normal
hooks in the declared environment. Independent remote-ref readback returned
feature `14cdf1caec606bb6bc88fcb32ac48f707f5dabb0` and staging
`55c5046514d06fe9398a022c1622bdaae5228841`. [Push log](os-hardlockup-runtime-push.log).

The push automatically started existing exact-head runs
[CI 39744127896](https://github.com/vpsfreecz/vpsadminos/actions/runs/39744127896)
and [RSpec 39744127815](https://github.com/vpsfreecz/vpsadminos/actions/runs/39744127815).
Both were in progress when handed to one fresh retained-policy utility,
`/root/os_runtime_ci_14cdf`, explicitly selected as `gpt-6-luna`/`low` with
fresh context. Its startup confirms session/env identity and exact heads.
The retained catalog at `profile-159-link/share/dev-workspace/agent-teams.json`
(digest `ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376`)
supplies the watcher settings; current installed access is full-access and the
native utility configuration declares danger-full-access/approvals-never.
The native spawn request records model/effort; the utility cannot independently
inspect its launch argv from its own process list.

The utility owns both redirected `gh run watch --interval 60 --exit-status`
processes as one related batch (combined shell handle 20989) through terminal
results. [CI output](os-hardlockup-runtime-ci-39744127896-watch.log) and
[RSpec output](os-hardlockup-runtime-ci-39744127815-watch.log) retain full
logs, with adjacent exit receipts to be written at completion. It has no
permission to retry, edit, diagnose, cancel or deploy; implementer2 owns any
failure diagnosis and will preserve first evidence before considering a retry.
No duplicate workflow or parent CI observer exists. Source handoff is complete;
CI is explicitly pending. The session stays open.

## Historical boot-only package and automatic CI

The following retained evidence applies to f3e/b81c, not the current runtime
package. In particular, old assertions of no sysctl assignment and boot-only
applicability are superseded above.

# vpsAdminOS hard-lockup panic policy: final review packet

Source delivery and the direct review remediation are complete; automatic
CI remains pending under implementer2's watcher ownership. The single commit
`b81c43ff6865a033268072f55cd94ad763d0630b` on base
`252b80dfdb4bced0713e8423ef7ba3d5600d05dd` in
`worktrees/2026-10-20-kernel-check/vpsadminos`, branch
`2026-10-20-kernel-check`, upstream target `staging`.

The complete feature series is one commit:
`os: panic on hard lockups when crash dumps are enabled`.
Only `os/modules/misc/crashdump.nix` changes: add `nmi_watchdog=panic`
immediately after `softlockup_panic=1` under the same `mkIf cfg.enable`,
and correct the enable-option description to describe soft/hard panic.
There are no other changes, migrations, repeated dependency/channel/input
streams, generated updates, superseded approaches or fixup commits in this OS
range. No migration was merged, released, deployed or externally consumed.
The worktree is clean and the native comparison was captured.

The owner is the generic vpsAdminOS crashdump module: every configuration with
`boot.crashDump.enable = true` gains this argument, including consumers outside
vpsFree.cz. Disabled configurations gain neither panic argument from this
module. Linux `1dfea587` `kernel/watchdog.c:80-101` recognizes the `panic` token
of `nmi_watchdog=` and sets `hardlockup_panic`; detector enablement uses separate
`0`/`1` tokens. No detector bit, threshold, global sysctl, kernel build
configuration, package/input pin or crash-kernel forwarding logic changed.
The policy applies at boot, not a live switch. Existing later boot/runtime
overrides remain available; panic/capture is not guaranteed. Mixed versions
are compatible with no persistent-state or API change. No merge, deployment,
runtime write, reboot or fault was performed.

## Quick checks

All completed checks exited 0. The repository's declared `nix develop`
environment installed dependencies and active Overcommit hooks normally.
The initial post-checkout hook refused an unsigned configuration; the created
checkout was preserved and registered with native `--no-fetch`, then hooks
were installed/signed after reading `.overcommit.yml`. No hook was bypassed.

Format/parse/whitespace and gems:

```sh
nix develop --command bash -c 'set -e; nixfmt --check os/modules/misc/crashdump.nix; nix-instantiate --parse os/modules/misc/crashdump.nix >/dev/null; git diff --check; bundle check'
```

[Quick-check log](os-hardlockup-quick-checks.log).
The commit used `git commit -F`; active Nixfmt and all commit-message hooks
passed: [commit log](os-hardlockup-commit.log).

Actual full OS-module evaluation (no reduced module or new test harness):

```sh
nix eval --impure --json --expr 'let f = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-kernel-check/vpsadminos"; eval = enabled: after: (f.lib.vpsadminosSystem { system = "x86_64-linux"; modules = [ ({ lib, ... }: { boot.crashDump.enable = enabled; boot.kernelParams = lib.mkAfter after; }) ]; }).config; pick = c: { inherit (c.boot) kernelParams; hardlockupSysctl = c.boot.kernel.sysctl."kernel.hardlockup_panic" or null; }; in { enabled = pick (eval true []); disabled = pick (eval false []); override = pick (eval true ["nmi_watchdog=nopanic"]); }'
```

[Final evaluated values](os-hardlockup-eval.json) and
[stderr](os-hardlockup-eval.log). Enabled contains each panic token exactly
once, adjacent; removing the new token reproduces the
[base enabled list](os-hardlockup-baseline-eval.json) exactly. Disabled equals
the base disabled list exactly and contains neither panic argument. The
`mkAfter` case places `nmi_watchdog=nopanic` later. All three configurations
have no hardlockup sysctl assignment. Inline receipt assertions passed.
The evaluation occurred before commit against the identical committed source;
only the Nix option description changed after the first two-case check, then
the final three-case evaluation and formatting were repeated before commit.

## Review boundary

High risk because this changes host failure policy. Lead assigns retained
`reviewer0` with saved Sol/xhigh settings and general, architecture, scope,
risk/compatibility lanes under mandatory-change-review. This packet requests
actual independent whole-branch/history and no-migrations/no-repeated-streams
conclusions. Prior review of the withdrawn site sysctl is historical.

The related site configuration withdrawal has a zero feature range:
[withdrawal evidence](hardlockup-configuration-withdrawal.md), base/head
`37a338b25192d9271ee211110800c2dc6a094a57`. No site or OS pin bump.
The architect's [accepted brief](design.md#move-panic-policy-to-vpsadminos)
records scope, overrides, compatibility and recovery. The module's option
description is the proportional reusable documentation update.
No further long build/test is selected absent a concrete check failure or
review finding. No induced VM/crash/lockup test is needed for this argument
addition. Source setup built only development tools; no kernel build occurred.
Publication is independent of the review gate; its verified result is below.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/>

## Publication and automatic CI

SSH feature publication succeeded with hooks enabled in `nix develop` after
normal Overcommit signing. An initial ambient-shell push was rejected by the
signature gate before publication; no hook was bypassed.
SSH `git ls-remote` independently returned feature
`f3e91f6213934bf5d1a2ca52a7fdc6e63941a647` and staging
`252b80dfdb4bced0713e8423ef7ba3d5600d05dd`. Source blob:
`13e9b1f7371b2c98c19429e44f5173c6b1af134a`; worktree clean.
[Publication log](os-hardlockup-push.log).

The push automatically started [CI run 39598560664](https://github.com/vpsfreecz/vpsadminos/actions/runs/39598560664)
for this exact head. It was in progress at the metadata check; no CI completion
is claimed. This is automatic remote CI, not an extra locally launched test.
Implementer2 owns the automatic CI follow-up; the lead coordinates final acceptance.

## Direct review remediation

Reviewer0 accepted the source/semantics and requested the repository-required
validation summary in the commit body. The same coherent commit was amended
with factual validation prose; active hooks passed. Current head is
`b81c43ff6865a033268072f55cd94ad763d0630b`. The source tree, file blob and
parent are identical to reviewed `f3e91f621`: see
[identity proof](os-hardlockup-amend-identity.txt) and
[amendment hooks](os-hardlockup-amend.log). No behavioral re-evaluation or full
review rerun is required for this direct message-only remediation. The earlier
publication/CI references above are retained history, superseded below.

The amended feature was published with an exact lease against old `f3e91f621`.
[Lease publication log](os-hardlockup-amend-push.log). The still-running old CI
run 39598560664 was checked to match that old head and cancellation requested
under the lead's explicit authorization; final old-run conclusion and new-head
CI follow-up are being reconciled.

SSH confirmation after amendment returned feature
`b81c43ff6865a033268072f55cd94ad763d0630b` and staging
`252b80dfdb4bced0713e8423ef7ba3d5600d05dd`. The old run completed
`cancelled` after the authorized request; its local observer exited 1 and is
no longer running. [Old final job status](os-hardlockup-ci-old-status.json)
and [retained observer log](os-hardlockup-ci-watch.log).

A fresh retained-policy Luna/low standalone watcher observes only existing
[new CI run 39600028637](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637)
at exact amended head. It uses danger-full-access/approvals-never and has no
permission to retry, cancel, edit source or deploy. No duplicate workflow was
started; the parent does not poll CI alongside it.

Native worktree comparison was refreshed after the message amendment and binds
base `252b80dfdb4bced0713e8423ef7ba3d5600d05dd` to current head
`b81c43ff6865a033268072f55cd94ad763d0630b`.


The exact amended-head automatic CI has a completed failed native job
`119228578900` (3h36m46s): 124 tests passed and five upgrade guest cases failed
the same retained impermanence boot-dataset assertion. The [failure diagnosis](os-hardlockup-ci-failure-analysis.md)
retains the complete failed-job log and native artifact. All five cases kept
their predecessor kernel/boot identity through userspace activation, so the new
boot argument was not parsed in these failures. The underlying run-state loader
cause remains unresolved; the run is not green. Five successful jobs and five
unfinished livepatch jobs are recorded in the existing watcher output. The
watcher continues; no rerun, new test, source edit or cancellation was performed.


## Final automatic CI result

Run [39600028637](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637)
finished with **failure** at exact head
`b81c43ff6865a033268072f55cd94ad763d0630b`; final metadata update is
2026-10-22 01:11:10 UTC (03:11:10 CEST). All 11 jobs completed: the OS build
and all nine livepatch lifecycle jobs passed, while the native suite failed.
The last job, AMD fresh, passed in 1h32m17s. The span from first job start to
last job completion was 12h41m28s, including runner queue waits.

The native result is 124 passing tests and five failures, all at the same
impermanence boot-dataset preservation assertion. The [bounded diagnosis](os-hardlockup-ci-failure-analysis.md)
records direct evidence that these cases kept predecessor kernels and boot
identities, so they did not execute the added boot argument. The underlying
run-state cause and actual retained mount source remain unresolved. No baseline
rerun, source repair, further diagnostic execution, merge or deployment was
selected. CI is not green.

Final [metadata and all job/step conclusions](os-hardlockup-ci-new-result.json),
[all-job logs](os-hardlockup-ci-new-jobs.log) (10,909 lines; 2,019,185 bytes),
[failed-job logs](os-hardlockup-ci-new-failed.log),
[watch output](os-hardlockup-ci-new-watch.log) and
[actual watch exit](os-hardlockup-ci-new-watch.exit) are retained. All 11 job
names occur in the full log. The native artifact ZIP and uploader-matching
SHA256 are recorded in the diagnosis. The watch command exited 1 for failed CI;
the utility CLI then exited 0 after collecting the result, which is not a
success claim. No observer or CI job remains running.

The [raw watcher summary](os-hardlockup-ci-new-watcher-result.md) names only
three failed examples from an intermediate log excerpt; the authoritative final
native summary at all-job log lines 7155–7162 includes all five, including both
v1 variants. The parent reconciled this before the final report. Watcher-downloaded
artifact copies remain at `/tmp/os-hardlockup-ci-new-artifacts/`; the complete
native ZIP is additionally retained under this session.
