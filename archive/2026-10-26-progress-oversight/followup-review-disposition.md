# Follow-up review disposition

Important1 fixed directly: the runtime returns ErrProgressCheckDeferred only
when retry admission proves no submission was attempted. The scheduler clears
only that exact unsent pending reservation. Unknown outcomes are untouched.
Paused manual-check regression proves refusal leaves no pending request and
after the three-minute deadline a new explicit check can run. Real native-wire
regression still proves original manual retry ID/deadline/phase are unchanged.
Focused TestProgress* and native cold receipt tests pass. Advisory2 corrected
site prose to describe a default automatic cadence and explicit idle exception.

The Settings commit retains these narrow fixes; site docs retain their owning
commit. Final consumer pins are mechanically refreshed once each. No migrations,
new architecture or public behavior beyond the reviewed design. Per review
step9, parent inspection and targeted checks complete remediation; no extra
reviewer turn is needed.

## Final revised heads

dev-workspace f0457b44a5a1e557fbb4dae0f21d4bfea7fd14fe
54e968ae progress: schedule checks for cold observers
f0457b44 progress: configure session checks from settings

workspace 1e001534f59d5e1b3378af5e72874ce27eeac950
d5d29dd2a docs: locate progress controls in session settings
1e001534f runtime: select observer activation and session settings

vpsfree-cz-configuration 1710aafb765e80bd66b2757038d5dd2994a5022b
1710aafb inputs: set devWorkspace to f0457b44

Final locks match runtimef0457b44; only runtime nodes changed. Configuration
updates were consolidated to one commit; the generated changelog was corrected
to the real9baeea52..f0457b44 range. No intermediate pin/history remains.

Parent inspection tightened the requested fix: clear definite retry-admission
refusal only on a new request's first dispatch attempt. A later refusal cannot
prove an earlier uncertain attempt was never submitted. Added a regression that
retains the same unknown ID in that case. This preserves the reviewed stable-ID
contract and needs an updated application derivation; reuse other successful
checks only for unchanged inputs.
