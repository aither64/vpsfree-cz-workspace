# Portal performance rollout

Current phase: complete. Deployment accepted and reservation released.

The user authorized integration into master for codex-web, dev-workspace,
vpsfree-cz-configuration and workspace, deployment of aitherdev, and release
of the machine reservation. The exact integrated heads and complete branch
series are recorded in [final-heads.json](final-heads.json).

The provider merged through integration e26cca5e-a674-4e0f-b212-476ae0f030cb.
The remaining merges and ordered system/profile activations completed through
integration 074406d2-822a-4079-9ef4-931a802da234. Its result and summary are
retained under integration/. No merge or deployment remains queued.

## Deployed identities

- Application: /nix/store/a6brrl4a354sn4q25crqw3q54wwg0qag-dev-workspace-0.2.0
- System: /nix/store/nsyavczcck0bmhid5h0bfrbfmkivinxf-nixos-system-aitherdev-26.05.20261013.a033e66
- Portal PID: 456486
- Original native Codex PID: 2615996
- Original tmux PID: 435397
- Native binary SHA256: 420f2b593ddd27a5c1edbe1a9791ef069de88de92b85201496112b7965c1bd28

The native binary and both session processes survived activation unchanged.
Native Codex remains 0.160.0. There are no migrations or persistent format
changes; the new caches rebuild in memory. pre-activation-identities.json and
post-activation-identities.json retain the before/after evidence.

## Verification

[final-verification.json](final-verification.json) is the sealed pre-integration
receipt. Its original workspace revision f73b89d9 was mechanically refreshed by
the installed native recipe to final 366517f2; the generated_pin certificate is
workspace-certified-refresh.json. No deployed source uses the original revision.
The independent report is composition-review.md, with review.md and
review-remediation.md retaining the original final review and resolved findings.

The provider full CI, runtime feature CI, focused Go/race checks, composed
package build and real Chromium/Firefox tests passed. The later runtime master
CI 38818112064 passed too, including its master-only host checks; evidence is
master-runtime-ci.json. The real native long-history probe completed 14,198
tool calls and 2,349 sent / 1,244 received messages with complete counts, 162
bounded observations and 0.467 s p95 (native-history-probe-result.json).

The first live instrument sandbox denied Unix socket access (EPERM); the
second could access the socket but could not query the user service bus.
Both stopped without acceptance measurements. Their original logs/reports
remain local. The fresh native Luna/low utility proved service-manager access
and ran one unchanged verify-live.sh invocation to completion. No deployment was repeated.

## Acceptance and release

Live acceptance passed in 600.17 seconds: 480 sampled activity/index requests
and six nonempty history pages, with no HTTP failure, stale snapshot or history
overflow error. The five-minute warmed portal average was 0.15086 core, versus
4.51664 cores in the fresh predeployment baseline (96.66% lower). Cached request
p95 was 0.07994 seconds. Activity counts were complete; historical timing
coverage remains explicitly partial where it was not observed. All live
profile, system, native binary and process identities stayed unchanged.

The first native finish request used a structured evidence object. The installed
command requires a nonempty string; it rejected the request before mutation.
The corrected new request retains the acceptance path and SHA256 in its evidence
string. This changed no proof or release criterion.

Native coordination finish succeeded: reservation
9a7c34b6-c406-4a28-901f-f24b26ccf7f9 is released at revision 5. The receipt is
finish-result.json. post-finish-coordination.json retains the full four-owned-head
integration proof plus deployed unowned extension revision
767dfd587e346168e1443e65ccdb67ce748f3fe3, settled six jobs and 14 delivered
notifications. The coordinator also confirmed unchanged deployed identities.
One artifact registration met transient lifecycle-lock contention and succeeded
on retry. No product or deployment work remains.

The release request was fb895c74-42b0-469c-8088-ce59217b91e8. Acceptance evidence
was bound in its evidence string to live-acceptance.json and its SHA256.
Feature branches, worktrees, rollback generations and the session remain retained;
no archive, deletion or session stop was performed.
