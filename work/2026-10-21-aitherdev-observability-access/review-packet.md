# Final committed-deliverable review packet

Session: 2026-10-21-aitherdev-observability-access. Binding workspace
/home/aither/workspace/ai/vpsfree.cz. Project vpsfree-cz-configuration.
Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-21-aitherdev-observability-access/vpsfree-cz-configuration
Branch: 2026-10-21-aitherdev-observability-access. Target: origin/master.
Base: 38e7c837893695999e588a73f5d2a0088b8257b1
Head: 072f7e01f5000bfd43439c5ba27aee28cfe69b17
Complete history: final-series.txt. Complete final diff: final.diff.

## Outcome and accepted boundaries

User directed "Implement the plan" after selecting dedicated Random Basic secret.
Read design.md and plan.md/state.md. Add unprivileged SSH log-reader authenticated
by machine key WITHOUT IP restriction; readable remote/messages logs+archives,
rotation/new-host creation, no sudo/forwarding/PTY/tunnels/rc. Ordinary shell may
write home/tmp. User owns manual root authorized_keys removal; no source code
must remove it. Dedicated Basic codex-aitherdev/256bit secret covers selected
read/query/diagnostic endpoints on both mon1/mon2 /codex/api/v1. No IP bypass,
private DNS mapping, raw9090 access, generic auth service or custom client wrapper.
Use separate runtime verifier and user-home curl config; no live secret generated.
Normal human auth remains separate. Default deny paths/methods, strip credentials
upstream, scoped rate/concurrency/body/timeout limits. No production operations.

## History and migration inventory

Two independent logical commits: logger implementation+its fixture/docs, then
proxy+fixture/docs+shared flake/README/mkdocs registration. This ordering avoids
references to missing logger files in the intermediate tree. Initial unpublished
proxy64cabb9e and logger01450598 were reordered with exact tree proof f87278eee6804a494d6e67d476d287be3c756a06,
then narrowly corrected logger helper traversal/no-op and VM logrotate invocation;
those changes were folded into owning logger commit before this final review.
No published, merged, deployed, released or externally consumed branch version.
No obsolete approach or fixup commits intended to remain. Reviewer must inspect
complete history independently and explicitly conclude on this inventory.
No migrations (database/TSDB/log format); historical metadata reconciliation is
an operator-triggered helper, never automatic activation. No dependency/channel/
input update streams; no generated pin commits or retained transitional pins.
Explicit conclusions required on obsolete history, repeated update streams and
migration lineage (including "no migrations").

## Documentation and interfaces

Changed docs/operations/log-reader-access.md and prometheus-query-access.md with
entrypoint links in README/mkdocs. Lead contextual prose pass completed before
commits; technical completeness/security remain review concerns. Inventory,
maintenance/quiesce, metadata recovery, separate credential provisioning/rotation/
revocation and exact curl usage are reusable operations docs; no release artifacts
inside project repo. External interface: log-reader SSH + selected Prometheus API
prefixes, owned by site configuration; clients are aitherdev user's SSH/curl/Codex.
Native nginx/SSH/rsyslog/logrotate are the mechanisms; no provider/runtime changes.

## Quick checks and pending long verification

Pinned nix develop bootstrap passed in54s (environment-check.log/result.json).
Both packages Nixfmt/required Overcommit hooks and diff checks passed. Proxy:
production-generated two-vhost nginx config evaluated, pinned nginx1.30.6 -t via
fixture syntax mode passed, Python fixture and local+remote provisioning programs
AST parse passed. Logger: evaluated assertions/account policy, pinned rsyslog and
NixOS generated-logrotate syntax derivation, Python parse, effective sshd -T
Match policy including arbitrary source passed; bounded user-namespace helper
behavior/refusal checks passed. VM drvPath evaluation only; no long tests run.
Post-review planned: quick check derivations, prometheus-query-access.integration,
log-reader-access.vmTest, logger+proxy confctl builds. Production TLS, credential
files/permissions, actual old log ACL/readers and ingestion remain deployment
acceptance prerequisites, not validated by disposable tests.

## Review selection and lanes

HIGH risk: SSH/HTTP authorization, runtime secrets, root-operated historical file
permissions, service/deployment/recovery semantics. Reviewer0 retained independent
review-purpose ready member, gpt-6.1-sol / xhigh; no overrides, no fallback.
Read /home/aither/.codex/skills/mandatory-change-review/SKILL.md and ALL references:
general-review.md, architecture-review.md, scope-review.md, risk-review.md.
Perform review directly, no nested reviewer/subagents; read-only source. Inspect
repo AGENTS.md and workspace mandatory procedure routes. Include proportionality,
credential exposure/default-deny/auth inheritance/path normalization, new/rotated
log modes, helper races/refusals/partial failure/recovery and meaningful coverage.
Report severity/lanes/file+commit evidence, residual gaps and explicit whole-branch
history/migration/stream conclusion. Save report to this session review.md only.
No long tests, deploy, provisioning, merge or independent application changes.
