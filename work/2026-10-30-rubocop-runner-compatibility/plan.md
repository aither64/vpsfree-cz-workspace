# 2026-10-30-rubocop-runner-compatibility

## Goal

vpsadminos rubocop workflow has an issue since the runners were updated to ubuntu 26.04. see if other repositories that we manage have the same problem and suggest a solution.

## Affected repositories

Read-only audit of vpsadminos and all repositories in the workspace project map.
Narrow affected scope to repositories with Ruby/RuboCop workflows after inventory.
User follow-up authorizes implementation, verification and integration of the fixes in vpsadminos and security-advisories. No system deployment is needed.

## Approach

1. Architect establishes the exact vpsadminos failure from current workflow and failed Actions logs, checks upstream compatibility and recommends a solution.
2. Implementer0 independently inventories managed repository workflows and recent runs, distinguishing confirmed failures, latent exposure and unaffected repositories.
3. Lead reconciles findings and presents the smallest practical solution with evidence and remaining uncertainty.

## Decisions

- Initial request was investigation and suggestions only. Follow-up authorizes the proposed CI fixes and merge after verification.
- Use canonical bare Git objects and read-only GitHub APIs; avoid other session worktrees.
- Accepted recommendation: explicitly select CI Ruby '3.4' in vpsadminos RuboCop; use the same selector in security-advisories RuboCop and RSpec. Current 3.4.12 has Ubuntu 26.04 assets. Preserve project-wide version policy. Include vpsadminos workflow self-trigger paths.
- Merge approval: user follow-up in this conversation, "ok, implement the fixes. merge it after verification." Applies to vpsadminos → staging and security-advisories → 2026-07-13-security-advisory-automation, their freshly verified remote default branches.
- One implementer owns the narrow three-workflow package; architect owns brief updates; independent reviewer owns final review after commits and quick checks, before CI verification. Lead owns merge coordination.

## Compatibility and deployment

Assess runner OS, Ruby runtime and setup action compatibility, including differences between GitHub-hosted and self-hosted runners. Proposed fixes must preserve the intended lint environment; any recommendation to change Ruby must explain compatibility implications. No deployment is planned.

## Documentation

Readers: user and future implementer. Findings and evidence stay in this session: design.md (architect) and repository-audit.md (implementer0); state.md tracks acceptance and next actions.

## Testing plan

Completed investigation: current workflows, actual Actions logs and official upstream support/assets. Implementation: declared hooks plus focused YAML/action checks, independent final review, then real RuboCop and RSpec Actions runs on the final revision with actual Ubuntu 26.04 image evidence. Confirm successful Ruby 3.4 patch installation, Bundler and real commands. Use a fresh policy watcher for CI. Merge only verified reviewed final heads, under separate short repository claims, then verify remote refs and default-branch CI. No OS builds or fleet deployment.
