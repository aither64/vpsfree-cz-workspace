# Verification

Validated on aitherdev with Codex 0.154.0 at the revisions recorded in
[the review packet](review-packet.md). All four mandatory Astra/xhigh review
lanes passed before the longer package and deployment checks.

## Local and packaged checks

Skill creator `quick_validate.py` passed with PyYAML from Nix. `nixfmt --check`
passed for both changed Nix files; `git diff --check` passed. Core and extended
catalog installation/metadata assertions and rejection of extension replacement
of the built-in skill passed. Consumer deployment contract alignment and all 47
portal manifests passed validation. Configuration commits/pushes passed
Overcommit in the repository Nix shell.

Fresh Luna/low watchers ran these commands and returned evidence to the parent:

| Worktree | Command | Result |
| --- | --- | --- |
| dev-workspace | `nix build --no-link --print-build-logs .#checks.x86_64-linux.extension-catalog .#checks.x86_64-linux.generic-source .#checks.x86_64-linux.host-package-contract` | Exit 0, 236s |
| vpsfree-dev-workspace | `nix build --no-link --print-build-logs .#checks.x86_64-linux.package-metadata .#checks.x86_64-linux.organization-source` | Exit 0, 231s |
| workspace | `nix build --no-link --print-build-logs --print-out-paths .` | Exit 0, 216s |
| vpsfree-cz-configuration | `nix develop -c confctl build --yes cz.vpsfree/machines/aitherdev` | Exit 0, 131s, 78/78 steps |

Generic, extension and application logs each include 77 Ruby test runs,
475 assertions, 0 failures, 0 errors and 3 skips, alongside other package checks.
Local logs: generic-build.log, extension-build.log, application-build.log and
host-build-noninteractive.log. No unexpected kernel compilation occurred.
The original host invocation failed at its confirmation prompt before building;
parent diagnosis and command correction are recorded in state.md.

## Live automatic delegation

The owned managed thread received an ordinary verification request with no model
or skill named in the prompt. It was asked to read current workspace policy,
run one known quick fixture and one related long batch, and independently inspect
the fixture source while waiting. No code or tracking edits were authorized.

- Parent: `01a0ae94-9308-79a0-96da-5d8d0db3cea0`.
- Parent turn: `01a0aea8-d0a8-7d53-a42a-cd95537d76c2`, completed, 142s.
- Automatic watcher: `01a0aea9-6667-7ee3-8427-5c5b5506ca6a`.
- Parent raw turn context: model `gpt-6-astra`, effort `xhigh`.
- Native spawn arguments: model `gpt-5.6-luna`, reasoning_effort `low`,
  fork_turns `none`. Child thread/read and raw turn context independently confirm
  Luna/low; child session metadata has forked_from_id null and the correct parent.
- The parent ran the quick fixture inline (exit 0), inspected source, then used
  native waits (50s and 30s) rather than polling the watcher's logs.
- The watcher ran the 65-second passing fixture (exit 0), then the deliberate
  failure fixture (exit 7), each once. Its report preserved both outcomes and log
  paths, and stated that no operation remained running.
- The parent continued automatically with a correct final result. No retries,
  fixes, nested watcher or user approval intervened. Both threads are idle.

Evidence was inspected through completed thread history and the retained local
rollouts. Logs live-quick.log, live-long.log and live-failed.log each contain one
start and one result. Raw transcripts are deliberately not committed.

## Fallback and escalation

An isolated ephemeral thread had `agents.enabled=false` and Astra/xhigh set.
It used the installed skill and visibly reported that native delegation tools
were unavailable. It ran its 65-second fixture exactly once with blocking waits,
returned exit 0 and its log, and completed. Thread
`01a0aea8-d591-7213-8ebe-b6953509de87`, turn
`01a0aea8-d79e-7721-adfa-b733edc75dee`, elapsed 105.3s including model work.
The socket also broadcasts unrelated child notifications; evidence was filtered
by thread identity rather than mistaking those for fallback delegation.

A separate fresh Luna/low watcher received an explicit cancellation rule for an
owned synthetic `MONITOR_ESCALATION` marker. It observed that marker, sent Ctrl-C
only to its own PTY 80977, and returned incomplete with actual exit 1 after about
1.3s. The parent verified live-escalation.log. No unrelated process was touched.
This exercises caller-directed escalation, not a real stalled build or kernel
compilation.

## Deployment and limits

Host dry-activation/switch and user-profile activation passed; see
[the rollout record](rollout.md). Installed skills/list with forceReload returned
exactly one enabled monitoring skill and no errors. Both workspace router and
vpsfree-cz portal services were active. Model/list advertised Astra/xhigh and
Luna/low, consistent with the observed live model selections.

CI was not awaited or used for a live monitoring test, per the user's instruction.
CI run-identity/failure-evidence behavior was covered by skill review. Missing
model/capacity and inaccessible existing handles share the documented fallback,
but only delegation-tools-unavailable was exercised live. No standalone timeout
policy was added. Automation follows agent instructions, not a deterministic
scheduler. Weekly-limit savings were not measured; elapsed waiting alone does
not consume model tokens, and watcher setup also has overhead.
