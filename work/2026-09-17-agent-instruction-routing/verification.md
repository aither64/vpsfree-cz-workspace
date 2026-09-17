# Verification results

All 123 original nonblank paragraphs in the three changed instruction files
survive verbatim in their entry file or a mandatory procedure. The complete
inventory covers sixteen canonical project instruction files plus the workspace;
fourteen project files remain unchanged. Eleven canonical projects have no
instruction file. See coverage.md, coverage.json and inventory.json.

## Committed checks

- Final workspace revision: `c8889ea85682f5e673ac243e27f533ecc7ef3700`.
- `ruby test/agent_instructions_test.rb` and its `LC_ALL=C` variant: 2 tests,
  32 assertions, zero failures/errors in the local Ruby environment.
- `nix eval --json .#checks.x86_64-linux --apply builtins.attrNames` exposes
  agent-instructions and deployment-contract.
- `nix build --no-link --print-build-logs .#checks.x86_64-linux.agent-instructions
  .#checks.x86_64-linux.deployment-contract`: exit 0. Instruction check: 2 tests,
  31 assertions; deployment contract: 3 tests, 14 assertions; no failures/errors.
  Assertion-count differences reflect the packaged Minitest version.
- Whitespace/formatting and repository commit hooks passed. Exact already-tested
  HaveAPI/vpsAdmin heads passed whitespace checks in fresh temporary target
  worktrees before pushes. No application runtime code changed.
- Four fresh Astra/xhigh review lanes completed. Findings and final narrow
  remediations are in review-results.md. No unresolved Blocking/Important finding.

The initial packaged check found repeated dynamic Nix system attributes; grouping
both checks fixed evaluation. The next run exposed implicit US-ASCII Ruby reads
under the builder locale; explicit UTF-8 reads fixed it. The final run verifies
both the added check and existing deployment check. No unchanged behavioral case
was repeated, because these repairs did not change any instruction content.

## Live instruction-following scenarios

A Luna/low watcher ran the authorized driver; its test workload created twelve
isolated Astra/xhigh threads with delegation disabled. Thirteen turns completed
in about five minutes, including one later-turn scope expansion. Prompts described
ordinary work without naming the required procedure files. Fixtures had separate
Git roots outside the workspace, exercising standalone project discovery.

The parent checked successful command output against complete required file
contents, inspected all commands and final explanations, and confirmed only
read/list operations occurred. behavioral-results.json retains IDs, completion
records and read commands. All cases passed:

| Case | Observed result |
| --- | --- |
| Workspace commit/integration | Read Git and commit procedures; retained hooks, shared-index protection, comparison capture and fast-forward-only integration. |
| Failed CI / long build / kernel | Read verification; preserved failure investigation, kernel escalation, bridge default and fresh Luna/low versus Astra/xhigh responsibilities. |
| Later scope expansion | Same thread read the KB procedure in its second turn; production approval remained required. |
| Lifecycle/deployment | Read both procedures; unfinished journal blocked switching; cluster identity/schema checks and user-profile deployment remained required. |
| KB/WebUI | Read KB procedure; reported unavailable downstream workflow in the fixture and withheld production publication without direct approval. |
| HaveAPI standalone | Read localization, release and development procedures; retained source catalogs, release/backport branch selection and publish approval. |
| vpsAdmin standalone | Read testing/localization/development; retained exact-once API topics, runtime CI selection and external KB obligations. |
| vpsAdminOS standalone | Original inline guidance selected the local modified runner and data-integrity assertions. |
| Missing procedure | Failed to read commits.md, reported the missing guidance and stopped commit preparation. |
| Push-only | Read Git and verification; cancel only obsolete active runs on the same branch. |
| Downstream pin | Read Git/deployment; fetch/rebase prerequisite and exact confctl pin command preserved. |
| Workspace suspension | Read lifecycle; unfinished journal blocks suspension. |
| Existing vpsAdmin tests | Read development/testing despite no edit request; selected WebUI scripts and CI coverage requirements. |

The fixtures intentionally contain instruction sources, not full application
checkouts. Missing downstream KB/CI implementation files were reported rather
than invented or loaded from another checkout. These cases verify routing and
preserved obligations, not execution of the application workflows themselves.
They cannot guarantee perfect compliance for every future prompt.

## Context sizes

Workspace entry: 45,697 → 11,056 bytes (75.8% smaller). HaveAPI: 6,823 → 4,018
(41.1%); vpsAdmin: 10,052 → 4,907 (51.2%). The previous workspace automatic load
was truncated to 32,768 bytes, so restoring all applicable rules may increase
context for some tasks compared with that incomplete load.

The following are file-content bytes for the listed combinations, excluding
other skills, tool wrappers/output, rereads and conversation history. They are
not measured token charges or complete guarantees about a task's eventual scope.

| Repository | Example scope | Core plus selected procedures |
| --- | --- | ---: |
| workspace | commit and integration | 20,237 bytes |
| workspace | development with review and verification | 39,626 bytes |
| workspace | lifecycle and deployment | 19,828 bytes |
| workspace | KB work | 17,938 bytes |
| haveapi | development/test | 5,663 bytes |
| haveapi | localization | 5,032 bytes |
| haveapi | patch release | 7,853 bytes |
| vpsadmin | existing tests | 10,001 bytes |
| vpsadmin | visible UI change | 12,494 bytes |

Broad tasks can exceed their previous full-file size. Some live probes also read
additional applicable files or reread guidance. vpsAdminOS stayed inline because
its normal test-task context increased from 5,231 to 6,916 bytes after extraction.
This change reduces the initial load and avoids truncation; no weekly allowance
saving has been measured. No CI workflow was awaited, as requested.
