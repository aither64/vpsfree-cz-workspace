---
lifecycle: complete
---

# Ubuntu 26.10 container image

## Current phase

Image build and tests passed at exact final head. Coordinated integration
into staging is being submitted under the user's conditional approval.
General CI remains running; its watcher retains ownership.

## Phase checklist

- [x] Verify session selection and retained Full-team ownership.
- [x] Architect design and upstream suite evidence.
- [x] Implement three files; quick checks and mandatory hooks pass.
- [x] Independent whole-branch review; advisory A1 resolved.
- [x] Publish feature branch 0081fc01f over SSH.
- [x] Image build/tests passed (981.97 seconds, one test, no failures).
- [ ] General CI complete (broader suites still running).
- [ ] Coordinated fast-forward integration into remote staging.
- [ ] Verify exact final head integration, finalize state and clean owned temp files.

## Repository and exact revisions

Workspace: /home/aither/workspace/ai/vpsfree.cz, shared master coordination only.
Session: 2026-10-14-ubuntu-container-build (user explicitly selected existing
session; no DEV_SESSION identity variables present in the tool shell).
Project: vpsadminos, remote git@github.com:vpsfreecz/vpsadminos.git.
Worktree: worktrees/2026-10-14-ubuntu-container-build/vpsadminos.
Feature branch: 2026-10-14-ubuntu-container-build; default target: staging.
Base: 0ffcc1da559c6d76e593e691e113d1e9349eebf1.
Reviewed head: 863e8e0d9f8a3e84814af236e437706d1ae27115.
Final published head: 0081fc01f13236a098380094ddbd00539a9c8dae.
Both heads have identical tree ae5fb27c9af0a037d7302391e4701da1c3396f01.
One logical commit, three files, 28 insertions; clean worktree.
Portal comparison captured for exact final base/head.
Initial substantive plan/state committed on workspace master as f620274a.

## Implementation and documentation

Design: [design.md](design.md). Full final source diff:
[vpsadminos-final.diff](vpsadminos-final.diff).
Added ubuntu-26.10 config/build from 26.04, changing only resolute -> stonking;
kept shared Ubuntu builder and systemd console helper. Added untagged repository
entry; 26.04 retains latest/stable/lts. Test discovery is automatic.
No migrations, API/protocol/module/persistent-format changes, dependency pins,
repeated update streams, obsolete approaches or superseded branch fixes.
No coordinated node update, production deployment or image publication performed.
No project prose update is useful because documented interfaces and alias policy
are unchanged. Read image-scripts README, image creation/repository docs/specs.
Upstream suite/mirror evidence: [metadata](upstream/ubuntu-stonking-metadata.txt).

## Team and review

Retained Full-team: architect0 Astra/xhigh/workspace_write designed;
implementer0 Sol/xhigh/workspace_write authored application changes;
reviewer0 Sol/xhigh/read_only independently reviewed all four lanes.
Live identities/access/settings verified before substantive assignments.
Reviewer thread: 01a1462f-623e-79d3-821e-c44dae4818cd, no override/fallback.
High risk conservatively for new userspace/host compatibility; general,
architecture/repetition, scope/proportionality, risk/compatibility lanes.
Report: [review.md](review.md); original packet: [review-packet.md](review-packet.md).
No Blocking/Important findings. Advisory A1 required validation prose in the
commit body under local patch policy. Lead made a message-only amendment with
all hooks passing and directly proved identical tree; no rerun needed under
narrow-fix policy. Explicit history conclusion: no obsolete history, no
migrations/provenance, no repeated dependency/channel/generated update streams.
Original exact review receipt: [integration-review.json](integration-review.json).

## Verification evidence and active watcher

Passed: bash -n both new scripts; config cmp; exact template diff (only suite
name); git whitespace checks; Nix parse; focused nix eval --impure confirms
new 26.10 entry and unchanged aliases. All required hooks passed for final head.
Default vpsadminos dev shell does not expose public osctl-image command; an
attempt resolved the local source directory. The corrected brief uses the
existing targeted image CI invoking public osctl-image inside its VM.
Bootstrap, package/signature, boot/systemd/console, network/SSH and shutdown
remain unverified until that image test passes. No claim for all older hosts
or legacy cgroups. Avoid a duplicate successful local image build.

Runs at exact final head:
- [Image build/test 38964791624](https://github.com/vpsfreecz/vpsadminos/actions/runs/38964791624)
- [CI 38964791583](https://github.com/vpsfreecz/vpsadminos/actions/runs/38964791583)

Fresh Luna/low utility 01a14678-cd40-7291-ada0-50ae403b8c67 (Erdos) owns
both watches. No inherited context; pinned catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd and matching
native utility policy verified. Logs/results under verification/. Parent does
not poll the same CI logs. No retries/cancellations authorized or performed.

## Integration approval and next action

User explicitly instructed on 2026-10-16: "when the image build is verified
and the built image passes tests, you can merge it". Repository/target in
this conversation: vpsadminos -> refs/heads/staging. Approval is conditional
on image build/test success. No integration before that evidence. A clean
patch-equivalent rebase may preserve approval under the Git procedure; a
material patch/scope change requires renewed direction.

Read workspace Git/lifecycle/verification/coordination procedures and the
selected runtime coordination contract/operations guide, plus integration
guide from canonical dev-workspace. After CI success recheck final series,
base/head, clean tree, complete review and target baseline, then submit the
coordinated merge-only integration driver. No machine reservation needed.
Do not bypass a refused coordinator or another session's ownership.

## Setup recovery and cleanup

Worktree creation initially stopped at Overcommit checkout signature; reviewed
.overcommit.yml and signed through repository Nix shell, then normal registration
retry succeeded. Hooks remained enabled. Implementer source access worked but
its sandbox denied Nix daemon; lead performed short dependent Nix-only checks
and commits, without taking over application edits or changing access.
Initial Nix setup and a later message amendment unexpectedly provisioned mkdocs
dependencies. Lead monitored existing non-transferable handles visibly; neither
built a kernel. Later uncertain verification uses fresh watchers.
Temporary pinned dev environment: /tmp/ubuntu-2610-container-build-dev-env
(and its generation link); remove after verification/integration. Message file:
/tmp/ubuntu-26.10-container-build-commit-message.txt. Retain source branches,
registered worktree, session and compact review/test evidence at handoff.
No archive/delete/stop action is authorized by task completion.

## Merge gate satisfied and final pre-merge inventory

Image run 38964791624 completed success; watch exit 0. Raw job log confirms
"Detected images: ubuntu-26.10", the exact targeted test, and "1 tests
successful" (981.97 seconds). Build, result evaluation and cleanup all passed.
Lead inspected final JSON and relevant completed-job log evidence directly.
Verified tested/published head 0081fc01f13236a098380094ddbd00539a9c8dae,
freshly fetched staging still 0ffcc1da559c6d76e593e691e113d1e9349eebf1,
clean worktree, complete single-commit series/final diff unchanged from review,
identical reviewed tree, no migrations/history/update streams to consolidate.
User condition satisfied; general CI is still observed by original watcher.

Merge-only driver request: integration-request.json, preserving original exact
review receipt and allowing certification of the message-only amended head.
No machine reservation or deployment requested. Do not modify checksummed input
evidence after submission. Driver will preserve refs and own its tracking writes.

## Integration 51def684-e3f2-4624-aecc-3b2a272af1da

Requested exact feature heads are integrated. See integration/51def684-e3f2-4624-aecc-3b2a272af1da/summary.md
and integration/51def684-e3f2-4624-aecc-3b2a272af1da/result.json for operation receipts. Feature refs and session retained.
