# Targeted architecture and risk review rerun

Initiative 2026-09-13-portal-reliability, workspace /home/aither/workspace/ai/vpsfree.cz.
All worktrees are worktrees/2026-09-13-portal-reliability/<project>. Read current
plan.md and state.md in this tracking directory. Original packet and four lane
reports remain in review/. This packet supersedes their old indexed-recovery design.

| Project | Base | Head |
| --- | --- | --- |
| codex-web | aec4ea2ff13a053e340a2a47616d6fbc89aeeac1 | 6335da93acdcc82cc26200d2fbc7f479655aa7c3 |
| dev-workspace | f41d4220dd1d5ade08ba3bb28f964e9570a11ed9 | 3a1cd051826cf0dd16127f660ced9ef63aa6a51a |
| vpsfree-dev-workspace | 9f3142248f6e40d602115aa0fad66701595ef232 | fcc63b20e194e200b56cf0d05b69244b8c4cc53a |
| workspace | 7b00c831a3b6d171185885ccecab554f040a8d57 | 037bf6873b0d013afa1bf90aa31093ff1584647c |
| vpsfree-cz-configuration | 3d9ffa45c7e0388c96434fd3a6127d0a54c0b9ea | 3de09ed5d43174712f41745ef7cc06b454f840e3 |

Rerun scope: the review remediations introduce provider contract/budget ownership
and complete cluster-section refresh. Review the changed design and its representative
consumers, and any important interactions. Narrow deletion of the rejected indexed
lookup and direct immutable-comparison/workflow/draft fixes have focused verification;
do not require wholesale repeated review merely because commit IDs changed.

Owning generic runtime embeds runtime-contract.json and publishes it through its
Nix lib. New additive clusterProvider fields declare busy exit 75 and portal release
timeout 180 seconds. Generic Go cluster reader and release handler consume them.
Organization shell loads the published contract and owns shutdown.json with 120-second
grace, 10-second kill, 20-second cleanup. Ruby and shell consume these budgets; shell
validates their sum below the portal ceiling, Ruby test checks actual contract. Nix
packages shutdown.json both beside shared runtime.sh and alongside each provider runner.
Consumers ship together through organization and workspace input pins. No persisted
cluster schema/transition policy, receipt schema or comparison schema changed. Old
generations ignore additive contract fields; new org requires the matching new runtime.
Old live runners keep their original implementation and ownership checks.

The complete server-rendered clusters template is shared by initial page and details
refresh. Browser replaces all cards, including absence, preserves selected service tab,
and delegates copy/reveal/tab/release controls. Supplementary comparison capture is
owned by ordinary repository status inspection, runs after primary status with a separate
one-second budget, and logs failure. Explicit CLI save waits for the per-head lock
within context, rejects conflicting exact pairs, never overwrites first exact base/head.

Initialization retains authoritative upstream thread/list; measured auth-email lookup
was 61.265 seconds with zero matches. Thread CLI timeout now 180 seconds for create/fork/
retire, outer creation command 210 and receipt 240. No private index/rollout format parsing,
Codex upgrade or alternate identity policy. Sync only codex-web diff remains.

Quick checks: codex-web current exact-head CI passed; dev-workspace current exact-head
CI passed. Focused Go tests cover first-exact immutability, writer contention/cancellation,
status reads on capture failure, complete running/busy/stopped/absent HTML response.
Organization runner 6/13 and status 47/526 passed; flake no-build evaluation passed.
Browser syntax passed; full browser/live/package integration follows review resolution.
Commit split remains dependency; deadline; creation; cluster; comparison in runtime,
shutdown/status/dependency in organization, workflow/pin in workspace, generated config pin.

High risk; required reviewer model gpt-5.6-sol and effort xhigh. Trusted local operator
per repository AGENTS; remote clients untrusted. Preserve auth/Origin, path/identity,
lifecycle, generation and process ownership checks.

User authorized aitherdev deployment using feature configuration, not merges/archive.
Auth-email unfinished creation blocks normal profile switch. Proposed one-time recovery
uses installed private dev-session CLI with its current profile/generation/token and
shared transition lock, same journal/goal SHA/receipt/evidence, changing only its portal
command to the reviewed candidate. The CLI reconciles the existing creation and submits
its retained original goal once, then normal profile switch proceeds. No shared Codex
restart, guard bypass, or journal editing. Prior risk reviewer accepted this bounded path.
Historical password-reset comparisons use the four exact recorded pairs validated
against current registered heads, never inferred from moving default branches.

Return findings ordered by severity or explicitly none, with residual tests/risks.
Write your report under review/architecture-r2.md or review/risk-r2.md in this tracking
directory. Read mandatory-change-review skill and lane reference; review directly, no
nested agents and no code mutations.
