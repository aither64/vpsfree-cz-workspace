# Final review packet

Requested outcome: diagnose and repair failing daily configuration updates; audit other scheduled workflows and repair demonstrated automation/test defects. User subsequently approved merging completed repairs and running affected workflows. Lead owns all integration/dispatch. No production deployment or KB publication.

All six intended deliverables are committed and quick checks pass. Retained reviewer0 is independent, Sol/xhigh/read_only; verify roster before assignment. Overall risk: high conservatively, because automated generated commits target remote default branches and hook/environment changes must retain source-integrity safeguards. Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility. No authority or token expansion intended.

Read workspace AGENTS and routed review procedures plus each repository AGENTS. Read mandatory-change-review skill and all four lane references; perform review directly, no nested reviewer. Compare actual request with scope/diffstats before detail. Plan/state/design/audit and scheduled-inventory in this same directory.

## Complete ranges and full series

### B1: vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/vpsfree-cz-configuration

Base: 6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494
Head: 355e269f034422bb042f6c39fdab1725855b47e0

Complete series:

~~~text
355e269f034422bb042f6c39fdab1725855b47e0 ci: reuse the initial daily update shell
~~~

~~~text
 .github/workflows/daily-update.yml | 14 ++++++++------
 1 file changed, 8 insertions(+), 6 deletions(-)
~~~

Evidence: [evidence-b1.md](evidence-b1.md).

### C1: vpsadminos-org-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/vpsadminos-org-configuration

Base: ca96c95a1fee04793468785d8323a759615b2b4e
Head: cdb886678ba30d10b5114cab279d5eb602209954

Complete series:

~~~text
cdb886678ba30d10b5114cab279d5eb602209954 ci: sign the custom pre-commit plugin before updating inputs
~~~

~~~text
 .github/workflows/daily-update.yml | 1 +
 1 file changed, 1 insertion(+)
~~~

Evidence: [evidence-c1.md](evidence-c1.md).

### E1: vpsfree-irc-bot

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/vpsfree-irc-bot

Base: 7d7a48b2b2dc45732cf5853deca196b1ae05571f
Head: 41fd2f146d1fe7aa548e68b859a5d60cf2c55ba4

Complete series:

~~~text
41fd2f146d1fe7aa548e68b859a5d60cf2c55ba4 ci: isolate dependency updates from Bundler preloads
~~~

~~~text
 .github/workflows/daily-update.yml | 33 ++++++++++++++++++++++-----------
 README.md                          | 29 +++++++++++++++++++----------
 2 files changed, 41 insertions(+), 21 deletions(-)
~~~

Evidence: [evidence-e1.md](evidence-e1.md).

### F1: vpsadmin

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/vpsadmin

Base: 6f71da9777edfc902f6483edcdd84a2ef7d464ab
Head: 81d754f47a58e92fddb2a84c67b1aec98b740ae3

Complete series:

~~~text
81d754f47a58e92fddb2a84c67b1aec98b740ae3 api: correct raw migration default expectations
~~~

~~~text
 api/spec/migrations/20260707140000_add_sysconfig_localized_spec.rb  | 2 +-
 api/spec/migrations/20260713120100_add_node_kernel_history_spec.rb  | 2 +-
 api/spec/migrations/20260713120200_add_node_kernel_evidence_spec.rb | 2 +-
 api/spec/migrations/20260716120000_add_node_system_states_spec.rb   | 2 +-
 .../migrations/20260716120100_make_node_capacity_reported_spec.rb   | 6 +++---
 .../migrations/20260818115900_add_authentication_generation_spec.rb | 2 +-
 api/spec/migrations/20260818120000_add_password_recovery_spec.rb    | 2 +-
 .../migrations/20260821120000_add_password_event_counters_spec.rb   | 2 +-
 api/spec/migrations/20260909170000_add_ip_release_campaigns_spec.rb | 2 +-
 9 files changed, 11 insertions(+), 11 deletions(-)
~~~

Evidence: [evidence-f1.md](evidence-f1.md).

### G1: haveapi

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/haveapi

Base: b606b4b3c32bf05779c05babeaa1c31a33dee6fa
Head: 3194488d1ab3403bbb83896bdac8089f1195e645

Complete series:

~~~text
3194488d1ab3403bbb83896bdac8089f1195e645 utils: synchronize Ruff with guarded nixpkgs updates
~~~

~~~text
 clients/python/CONTRIBUTING.md        |  11 +-
 doc/agent-instructions/development.md |  12 +-
 utils/sync-ruff.py                    |  60 ++++++++
 utils/test_update_nixpkgs.py          | 264 ++++++++++++++++++++++++++++++++++
 utils/update-nixpkgs.sh               |  31 +++-
 5 files changed, 369 insertions(+), 9 deletions(-)
~~~

Evidence: [evidence-g1.md](evidence-g1.md).

### H1: vpsfree-kb-contracts

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/vpsfree-kb-contracts

Base: f97785c2c265172a4c78893e0673034fde56e4dd
Head: 2cfbde649769509e2628600535e3023d872f1735

Complete series:

~~~text
2cfbde649769509e2628600535e3023d872f1735 tests: wait for all firewall fixture listeners
~~~

~~~text
 tests/suite/kb/firewall.nix | 44 ++++++++++++++++++++++++++++++++++++--------
 1 file changed, 36 insertions(+), 8 deletions(-)
~~~

Evidence: [evidence-h1.md](evidence-h1.md).

## History, provenance and intended split
Each repository has one final logical repair commit; no superseded approaches or intermediate update streams remain. No migration was created/changed/removed; vpsAdmin migration definitions are byte-identical, expectations only. No schema deployed/released/externally consumed by these branches. No generated dependency or configuration input updates are included. IRC checkout v6 to current verified v7 is one action stream consolidated in E1. HaveAPI unpublished intermediate gate design was amended; published message-only previous head has equal tree and superseded CI was canceled. No deployed source lineage or recovery boundary requires intermediate history. Require independent explicit whole-branch history/no-migration/update-stream conclusion for all six.

## Acceptance and verification already established
- B1 real pinned-shell/native date/Overcommit and actual-hook commit survives deliberately failing fresh flake; YAML/Bash/actionlint and final hooks pass. C1 actual locked-hook fixture reproduces unsigned failure, accepts formatted commit after fix and rejects malformed Nix, no hook bypass; YAML/Bash/final hooks pass.
- E1 eight focused control-flow scenarios/YAML/Bash/actionlint/real hooks pass, exact-head RSpec success. F1 actual isolated core MariaDB 18 examples/0failures, syntax/RuboCop and full-plugin commit hooks pass. Hosted changed-file migration specs also pass under MariaDB11.8; full84 still required.
- G1 thirteen focused real-Git/stub-Nix/uv tests plus new Python lint/format, shell syntax and actual hooks pass. Future runtime uv/shared-Ruff format+lint gating is included. H1 generated Ruby/actual helper cases, pinned Nix formatting and full bin/check --allow-missing pass; source assertions/units preserved.
- After review: E1 real disposable generation/native bundle/hook commit + one no-change pass; G1 actual coherent Nixpkgs/Ruff parity and exact runtime gate; F1 full84 locally in prepared env; H1 one actual kb/firewall#firewalld scenario. These are not claimed passed yet. Owners retain follow-up fixes; fresh utility watchers own uncertain/long checks.

## Documentation routing/fidelity inventory
- B/C failure evidence, exact CLI semantics and execution limitations -> maintainers, individual investigation -> evidence-b1/c1 and diagnosis files; B workflow comment retains lasting toolchain invariant. C one-line signing change is self-explanatory; no separate project prose useful.
- IRC dependency generation instructions -> contributors, how-to -> existing README Bundix section plus workflow rationale comment; lead supplied final prose directly with writing skill. Source commands/preload/source-platform/purity requirements preserved.
- HaveAPI coupled pin/check/failure contract -> contributors, how-to and maintainer procedure -> clients/python/CONTRIBUTING.md and doc/agent-instructions/development.md. Lead directly applied writing skill twice as runtime gate settled. No docs moves, article generation, public protocol/version contract or library lock changes.
- F1 raw metadata explanation -> maintainers, diagnosis -> evidence-vpsadmin-migrations.md; assertion values reflect adapter contract, no helper behavior/doc subsystem needed.
- H1 all-port readiness/diagnostics -> test maintainers, source contract -> actual shared helper and evidence-h1. No KB article/example/hash/publication changes. Existing external firewall/data/rollback assertions protected.

## Boundaries and residuals
Preserve schedules, token scope, guard confctl pins, forward-only ancestry checks, nonforce pushes, mandatory hooks. No auto Python reformat, dropped parity/performance checks, one-off dependency bumps, product optimization or retries to chase green. All production schemas/APIs/protocols/configuration inputs/deployed state unchanged. Each repair revert restores source behavior; future generated HaveAPI lock+pin must revert together.
Audit covers26 repos/16 schedules. HaveAPI weekly performance is a separately evidenced product regression; reference/budgets unchanged. KB NixOS failure includes upstream GitHub504, no speculative retry fix; underlying firewalld SSH failure still requires runtime result. Older general vpsAdmin weekly failure superseded by success. Syslog schedule lacks retained run history. Retain these limits in review.

Please produce final-review.md, findings ordered by severity/lanes with file/commit refs, explicit scope/history/migrations/update-stream/docs conclusions, residuals and exact reviewed ranges. Read-only; do not implement fixes. Report via report_to_lead; no rubber stamp. If a narrow requested fix is later made, lead verifies directly unless new behavior/design requires affected-lane rerun.
