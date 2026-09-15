# Review packet v6: email sentence deletion and CI investigation

Initiative: 2026-09-09-ip-release-mechanism.
Tracking directory: /home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-ip-release-mechanism.
Read plan.md, the latest follow-up section of state.md and ci-investigation.md.

## Requested outcome

User explicitly requested removal of “Previously submitted reasons do not
prevent release under the current policy.” from emails, and investigation of
the failed vpsAdmin CI workflow. Remove its Czech equivalent too, for initial
notices and reminders, in text and HTML. Preserve the remaining assignment and
administrator-exemption instructions and all policy/release behavior.

## Exact delta to review

- /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsadmin
  Base: feccc00735c1d6323732ca39ef2aced8691d0432
  Head: 37e08d8be10c2f38138f5511403c94523126d033
- /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsfree-notification-templates
  Base: 0c80160f92a5ae81b33cc1dc2441b00e10c9eeb9
  Head: ff5cc7c474cab76dbdebabcd706b5d43c8d5319a

Both are clean, committed copies of the approved feature branch. One prose-only
follow-up commit per owning repository isolates the explicit post-review copy
request from the previously reviewed ownership/schema implementation. No
behavioral change or abandoned design is introduced. The existing render
assertion now checks the remaining exemption instruction instead of the removed
sentence; its logic is unchanged. The workspace overlay harness received the
matching literal update. Prior feature reviews v1-v5 are complete; review this
bounded delta, not the feature from scratch.

## Quick verification

- Campaign model spec: 38 examples, 0 failures.
- Actual notification overlay rendering/routing: 24 examples, 0 failures;
  EN/CS x requested/reminder x allow_keep true/false x IPv4/IPv6/mixed,
  with text and HTML checked and existing previews regenerated.
- Overlay nix flake check: passed.
- RuboCop for the changed spec: no offenses.
- Commit hooks and git diff --check: passed. TextWidth advisory is at 72
  columns; commit lines satisfy the repository's 80-column rule.
- Repository searches confirm no removed sentence remains in the 12 templates.

## CI evidence and limits

The old failed workflow is 34412825378 at 1e2d2d7c9. Full logs and artifacts
under /tmp/ip-release-old-ci-artifacts and /tmp/ip-release-old-integration-failed.log
show two separate failures, detailed in ci-investigation.md. A directly owned
browser IP fixture lacked charged_environment; that was fixed in 473b5c62a
and the full four-test VPS browser regression then passed locally. The shaper
scenario passed its assertions, then OsVm::Machine#stop timed out reading the
poweroff command. Guest logs do not establish the deeper cause of that hang.
Current completed CI 34474145934 at feccc0073 passed all 12 selected tests,
including the same shaper scenario and normal teardown. Completed log is
/tmp/ip-release-final-ci-complete.log. Do not treat its success as proof of the
unknown guest hang's cause. No speculative runner change or blind rerun is made.

## Scope, risk, compatibility

Low risk for this follow-up: literal deletion from existing email prose only;
no runtime logic, schema, API, security, retention policy, deployment or state
contract changes. No new abstraction, test control flow, dependency pin or
cross-project interface change. General lane only at gpt-5.6-sol/xhigh.
Existing API descriptor/overlay consumers and built-in EN fallback remain
unchanged. KB contract head 87bc0fbcb and API product pin 871fa3dae remain valid
for WebUI: no visible page/control/screenshot change. No merge, deployment,
wiki write, real email delivery or session lifecycle operation is authorized.

Check the two committed diffs and the investigation evidence directly. Perform
your review yourself, without nested reviewers or code edits. Report concrete
Blocking/Important/Advisory findings, or no findings plus residual gaps.
