# OSVM boot evidence: affected committed review packet

Final repository range: vpsfreecz/vpsadminos
54b4313404cea35b58ebb9df951ae75e27c44971..dc74bcdadef75f181934bad2178afb589c34644c.
Worktree: worktrees/2026-11-03-livepatch-fixture-failures/vpsadminos.
Affected new delta: reviewed ad8991fe6d48ec06fb7cf7d64f15af7578d37e7a..dc74bcdadef75f181934bad2178afb589c34644c.
All changes committed and quick checks pass; source/index/nonignored-untracked clean.

## Requested outcome and authorization

Preserve accepted current-normal-module qualification with nine meaningful semantic
witnesses and exact predecessors/boot/recovery safeguards, without Nixpkgs freeze,
blind checksum repin or historical-only lane. User authorized implementation and
conditional vpsadminos -> staging integration when required CI passes. No deployment
or session lifecycle authorization. The user kept latest-device-unit blocking; the
six temporary image-absence exceptions never waived a new cause. All seven image
cases now actually pass on old5235/new16.1 input; that is not final-head proof.

The new observation change is necessary failed-check handling, not a claimed fix
for the original boot stall. Native-only exact5235 run41811208607 produced three
before-hook timeouts on one cgv1 guest (kernel/vpsadminos): cpu-view-cgroups-v1,
memory-view-cgroups-v1,tmpfs-cgroups-v1. It remained at firmware/ROM, no Stage1/2 or
shell; no functional assertion ran. Same-head prior cgv1 passed. Old artifacts
omit actual config/argv/PID; underlying cause is unclassified, not proven flaky,
resource-related or a product regression. Existing failure hook skips guests
without a working shell, so a plain new-head rerun would retain the same blind spot.

The existing-debug route was considered first. One bounded cache-only preflight
of exact detached5235/unstable6.18.49 completed after command/metadata corrections:
55 planned builds include two material squashfs guest images and OS/Ruby systems.
No kernel/oldNix build was listed, but whole closure was cold under configured
caches. No realization/copy/build/VM was started; no cache outage/exhaustive
absence claim. Root selected the already-designed minimal observation fallback.
See native-lineage.md, design.md and implementation-plan.md native-boot sections.

## Owned source boundary and behavior

Only four new files change relative to ad899:
- osvm/lib/osvm/machine.rb (+167/-1)
- osvm/lib/osvm/machine_log.rb (+27)
- osvm/spec/osvm/machine_spec.rb (+430)
- osvm/spec/osvm/machine_log_spec.rb (+29)
Total +653/-1; 194 product/log lines and 459 spec lines. No new files/classes,
public runner API/options/mode, QMP/monitor/register engine, guest/kernel config,
Nix lock/producer/pin or package dependency change. No migration or fleet update.

Machine assembles spawn arguments once and passes them unchanged. A fixed
allowlisted launch event uses known Nix store input paths/numeric topology and
owned PID identity, omitting arbitrary arguments/config/environment/parameter and
exception text. Failure collection precedes the caller's unreachable-guest hook:
pinned proc-directory FD, PPID/starttime checks, safe process fields and at most32
owned task states. No signals, waits/reaping, guest or external host commands.
Missing/reused/exited PID, collection/log errors yield bounded unavailability.

Preserve existing spawn/reaper/pipe handoff, original readiness exception object,
rollback and cleanup. The lead's pre-commit acceptance inspection found initial
proc identity IO inside the masked handoff lacked a separate bound. D fixed it:
identity read and post-handoff launch log share min(now+10s,startup deadline),
expired budget skips IO, distinct local Timeout does not swallow queued OSVM
startup timeout. Four extra regressions cover blocked identity, consumed deadline
and original pending error/reaper/kill/join order. Review actual code and tests,
not just these assertions. No standalone guest boot or old-cause resolution claim.

Log methods have fixed qemu-launch/boot-wait-failure event keys, not new user
prose or a persisted production/public protocol. Assess privacy, boundedness,
PID lifecycle/races and actual consumers of existing Machine/MachineLog.

## History, equivalence, scope and documentation

Complete final series is TWO independently meaningful commits:
1. ad8991fe6d48ec06fb7cf7d64f15af7578d37e7a — tests/livepatch: qualify current module probe sites
2. dc74bcdadef75f181934bad2178afb589c34644c — osvm: record bounded host evidence for boot failures
Full base-to-head20paths+2923/-184. The original16-file feature blobs/modes/message
are byte-identical to reviewed ad899. Diagnostic support is separate because it
is independently reviewable host-test observation, required by concrete CI evidence.
No fixup/tidy residue, superseded approaches, repeated dependency/channel/pin or
generated streams. Six local provenance refs and detached5235 checkout retained,
none pushed/deleted. No migrations, deployed/external intermediate or schema lineage.

Fresh canonical SSH fetch verified staging54b and remote feature5235; unpublished
local final head is dc74. No default-branch mutation or repository claim. Preserve
conditional integration scope; no publication/long final-head CI has started yet.

Reuse source-identity-refresh-review.md for54b..ad899, and earlier final-review,
review-reconciliation, retention-review, defined-symbol-review/reconciliation for
unaffected work. Do not repeat the unrelated nine-site implementation audit.
Do independently inventory the complete final series/history/migrations and
assess this four-file behavior plus its intersection with the incoming runner.

Existing docs/os/testing.md and source-identity docs explain their unchanged
contracts; new bounded/privacy/recovery rationale is beside the owning helpers.
No new user workflow or product mode needs another document. Individual failed
attempts and actual rollout facts remain in session records.

## Verification and exact reuse

D current focused2files81examples/0failures/seed50896/1.32s; fullOSVM207/0,
seed39087/7.38s; declared RuboCop4files/whitespace pass. Includes real owned-child
proc-FD check without signals and negative privacy/PID/budget/error controls.
Earlier77/203 prototype logs are superseded and retained separately.

A post-commit integration99examples/0failures,seed27981/35.56s across existing
RepositorySource,CLIcommand,prebuild_nix,livepatch-runtime specs, using exact cached
declared Ruby3.4.11/native/test-runner bundle. No broad environment installation,
product/kernel/old-Nix build or VM. Only expected tiny source-symlink fixtures.
Normal commit hooks ALL passed with root Bundler activation/pinned RuboCop1.75.8.
An initial plain-Git invocation used unbundled1.87 and failed parsing its obsolete
cop warning; no commit/source/config change occurred. Correct bundle-exec Git
invocation fixed command context with no suppression/bypass. Receipts preserved.

ONE correct10-field IFD-disabled tuple on dc74 structurally equals ad899's full
receipt: package-a-osvm-identity.json. Producer161r03->qi47, sitesasfl9->aiqijl,
resolver3n2->5nps, siteChecksmci->94hk and frozen boot/SDK/config/compiler unchanged.
Realized module SHA7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f;
sites SHA093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1,
schema1/module binding valid; lock SHA604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa.
These support only exact corresponding prior24selector/ELF/SDK/helper49+19CRC reuse.
No whole guest/test closure or old-runtime transfer to dc74. Prior standalone
metadata evals reused only their unchanged source/locked-input boundary.

Full logs/provenance: package-d-result.md, package-a-result.md,
package-d-osvm-{spec,suite,rubocop}.log, package-a-osvm-{specs,checks,history}.log,
package-a-osvm-identity.json; final native comparison captured after Git release.

## Review assignment and readiness

Risk high overall (host process observation/startup ownership, privacy and kernel
verification). All four lanes, restricted to new four-file behavior/integration,
proportionality and complete final history. Retained independent reviewer0,
gpt-6.1-sol/xhigh/read_only; no override/nested reviewer. Read mandatory skill and
all selected references/applicable guidance; verify identity/roster/current source.
No source/session writes, Nix builds/evals, VMs, CI polling/retry/cancel, fetch/push,
merge/deploy/lifecycle. Known quick read-only checks permitted. Return full report
via report_to_lead for root to save osvm-boot-evidence-review.md.

Old original5235 run41773470432 is still owned by sole Luna/low observer:7/9 rows
passed, aged-v5 active/fresh pending at last snapshot; no new cause from it.
Review success will permit publication and full EXACT-FINAL-HEAD native+ALL9
lifecycle CI with source/guest metadata and semantic/identity/recovery evidence.
A future green run qualifies its own inputs; it does not retrospectively explain
old418 stall. Any actual new failure requires evidence/handling, not blind retries.
The user's conditional merge approval is still unsatisfied. Session stays open.
