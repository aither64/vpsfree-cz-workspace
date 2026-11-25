# Final review: boot and runtime hard-lockup panic

Lead-preserved summary of read-only reviewer0 final report and closed Advisory.
Reviewer identity: same-session retained reviewer0, native thread
01a15a63-a5c6-7eb0-b0f4-1e1ca77467f6, read_only, Sol/xhigh, no overrides or
fallback. All four mandatory lanes reviewed directly at high risk.

Accepted exact range: `55c5046514d06fe9398a022c1622bdaae5228841` to
`14cdf1caec606bb6bc88fcb32ac48f707f5dabb0`. One coherent v2 policy commit,
one module +19/-1, clean published feature. Tree70b0e11688686a490d5d81c96bba03250ec9f333,
moduleblob80566cb122af59df22540c195ea11de203b584ee. Reviewer verified refreshed
baseline was only upstream root-Nixpkgs lock and old/new patch range identical;
new graph checks bind the actual updated input. No baseline freshness gap.

No Blocking or Important findings. One Advisory historical pin-attribution
error in lifecycle evidence was corrected by implementer0 and directly verified
by reviewer0: b81c root Nixpkgs is cd4ea8d5; e4bae1bd is nested impermanence.
Advisory CLOSED. No remaining findings, no source change or retest needed.

General/architecture: same crashdump gate, retain boot arguments, explanatory
comment, ordinary hard-only sysctl. Targeted named activation uses final merged
value, honors0/null/false encoding and shell escaping, explicit procps path,
after specialfs, excluded from dry activation. Existing runit boot-only apply
explains need for hook; no unrelated replay/new service/framework/soft policy.

Real module outputs and isolated generated-wrapper mocks prove enabled/
disabled/override/null/false, generated text, order/dry exclusion and exact
arguments. Mock success0 gives wrapper0; write failure7 emits diagnostics and
aggregate activation1 through existing ERR trap. Hooks/format/parse pass,
commit validation prose and v1/v2 history meet repository rules.

Risk limits: switch/test activation can apply without reboot, but existing
switch wrapper does not enforce child's aggregate status, so future rollout
must read runtime value. Hook precedes service restarts/crash-image loading;
no image/detection/capture guarantee. Removing/nulling/disabling does not reset
live1; rollback explicitly applies/verifies0 or boots prior policy. Manual
runtime override can be overwritten by a later configured activation. Mixed
versions compatible without coordinated fleet update or stored-format change.

Whole history: one final owner, no obsolete/fixup/transitional history; old
f3e/b81c/pre-rebase10f31 folded with exact historical backups/check receipts.
No repeated dependency/input/channel/generated streams; upstream lock is not
feature work. NO MIGRATIONS: none introduced/merged/released/deployed/consumed,
empty lineage sound. Site configuration frozen withdrawal37a338b2..37a338b2
stays zero-feature range; newer default commits are unrelated baseline.

Reviewer directly confirms clean HEAD=origin feature14cdf and
origin staging55c504. Source/history and quick checks accepted; new exact-head
CI/RSpec remain pending, no full system/live-readback/crash claim. Old b81c CI
is historical, not new runtime-path proof. No merge/pin/deploy/host write or
lifecycle action authorized/performed by this review. No extra review required
absent substantive later changes.
