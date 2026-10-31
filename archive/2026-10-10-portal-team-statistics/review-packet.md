# Final review request

Read mandatory-change-review/SKILL.md and all four lane references. Review directly,
read-only, without nested agents. Assess full committed history and final diff of
all four branches, including dependency-update consolidation and "no migrations".

User requests Team activity, conversation sent/received and tool counts, session
lifetime working/waiting/idle, model changes during active/interrupted states,
and accurate automatic-wait labels. Accepted choices: lead plus retained members;
no utility roster entries; historical missing timing remains explicit; stopped
model choices do not activate threads. Deployment to aitherdev authorized;
default-branch integration is not authorized.

Scope/design: plan.md and design.md. Inventory: branch-inventory.md and four final
diffs. Runtime and library code plus docs are complete and committed. Quick checks:
codex-web focused activity/history Go suite; portal focused activity/recovery/model
Go suite, pure Node browser contracts, syntax and diff checks; composed deployment
contract; configuration Nixfmt/commit hooks. All pass. Full Go/Nix/native/browser
integration checks remain after review. TMPDIR=/tmp avoids Unix socket path length
in Nix shell test fixtures. Use repository Nix environments for any quick checks.

Risk high: private persistence, capability changes, native protocol and deployment.
Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
No retained roster exists (tracking-only initiative without Codex root); installed
catalog default lead_reviewed role reviewer requires gpt-6-astra/xhigh/read_only.
Catalog digest 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.

Owner of additive ActivitySnapshot and wait recorder: codex-web. Consumers found:
its conversation handler/browser/example and dev-workspace activity observer;
portal pins the provider in Go and Nix. Workspace direct nested runtime input and
configuration dev-workspace channel select the same runtime; extension unchanged.
Native Codex stays 0.160.0; exact local schema was inspected. Current PATH Codex is
0.162.0 and must not be used for native integration verification.

Checkpoint JSON fields and private portal records are additive. Roster/recovery
schemas are unchanged. Older packages ignore separate records and cannot apply
pending cold choices; forward recovery retains them. No database, CLI or cluster
contract changes. User profile is the application deployment authority; configuration
selects matching host module. Keep all branches unmerged. Local operator trusted;
remote clients untrusted. Preserve exact origin, cwd/thread binding, lifecycle and
package locks. Do not demand hostile operator filesystem containment.

Docs: codex-web README.md and dev-workspace docs/workspace-portal.md (statistics,
model semantics, state coverage and compatibility). Rollout-specific details will
remain in this initiative's rollout.md. Report concrete Blocking/Important/Advisory
findings and residual verification gaps, with explicit history/pin/migration
conclusions. Return report to parent; do not edit source or tracking records.

## Affected-lane rerun

Final inventory and diffs have been refreshed after the requested fixes and hash
repair. Focused library and portal Go regressions pass; 21 pure browser contracts,
syntax, diff, hook and composition checks pass. Vendor hash is now computed from
the final module revision. No long integration checks have been started locally.

Review new behavior in general and risk lanes: native active team-wait history
restores observation; sleep history lacking lifecycle status leaves a missed-start
turn unclassified until it ends; UI calls this Activity unknown. The Team configure
form now calls the capability-checked member settings endpoint in stopped and
active sessions. Initial rendering and polling retain recovery-ready selectors.
Other direct Team actions retain their existing interactive gates. Direct fixes
also recheck activation inside settings, verify member cwd for statistics, and
apply holds independently per observer thread. README timing semantics corrected.

Assess the refreshed complete series for the folded remediations and repeated
input updates; explicitly conclude pin consolidation and no migrations. Initial
full review remains applicable outside these affected lanes. Do not rerun long
checks or edit files. Return any concrete findings and residual test gaps.

## Workspace instruction-size repair

The packaged runtime, full browser tests, 0.160.0 protocol contract and isolated
live model/effort update proof passed. Both final provider/runtime CI passed.
The composed flake check then failed its existing 16 KiB core instruction check:
16797 bytes, identical at the workspace base. Deployment has not started.
The workspace adds a separate instruction-only commit: AGENTS.md explicitly
routes declaring an unmerged branch ready to the already mandatory Git procedure.
Its summary remains in the core; detailed rules stay in that procedure with an
explicit whole-branch history and migration conclusion. No policy gate is removed.

Review this committed change in the general lane and refresh the complete
workspace base-to-head history conclusion. Other heads and contracts are unchanged;
all original lane conclusions remain applicable outside this bounded repair.
Quick check: workspace's own Nix check environment, ruby
test/agent_instructions_test.rb: 8 tests, 144 assertions, all pass. Core is 16278
bytes; git diff --check passes. Confirm every original rule is still mandatory
and reachable before the relevant activity. No migrations or additional pin stream.
