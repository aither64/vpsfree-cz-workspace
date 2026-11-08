# W-prep: codex-web compatibility evidence

Investigation only. No source edits, project commits, tests, builds, integration
or deployment were performed. The lead owns acceptance and the next package.

## Checkout and authority

- Verified `dev-session current` and both session environment values match
  `2026-11-08-codex-version-update` in
  `/home/aither/workspace/ai/vpsfree.cz`.
- Retained self: `implementer0`, implementation, workspace_write, Sol/xhigh;
  architect and assigned peers resolved from the live same-session roster.
- `dev-session worktree add 2026-11-08-codex-version-update codex-web --as-is`
  fetched the SSH origin and created/registered the feature checkout at
  `worktrees/2026-11-08-codex-version-update/codex-web`.
- Branch: `2026-11-08-codex-version-update`; exact base and unchanged head:
  `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`. Checkout is clean.
- Read root applicable procedures, team guidance, documentation/handoff skills,
  current repository AGENTS, full update skill, README, and reference development
  and ephemeral utility sections. Current fetched instructions supersede the
  stale local master instructions inspected before checkout creation.

## Exact official sources

| Release | Official tag commit | Published |
| --- | --- | --- |
| 0.165.0 | `360319d8dee62d87e2d59fc0c21805d79519cfed` | 2026-10-27T20:09:38Z |
| 0.167.0 | `086ccc833bc9cf01024ad2dd6af7dbd421b6bf9a` | 2026-11-06T01:40:00Z |

Sources: [0.165 release](https://github.com/openai/codex/releases/tag/rust-v0.165.0),
[0.167 release](https://github.com/openai/codex/releases/tag/rust-v0.167.0),
[full comparison](https://github.com/openai/codex/compare/rust-v0.165.0...rust-v0.167.0).
Official release API, commit API, untruncated recursive trees, raw schemas and
selected source files were inspected. Raw supporting artifacts are disposable
under `codex-web-prep/`. The compare API reports 387 commits and caps its file
list at 300; complete tree identities were used for the migration inventory.

## Catalog and API boundary

Both exact source versions' `codex-rs/models-manager/models.json` are identical:
539696 bytes, SHA-256
`1384625c0b6b3e67d3c60da29becea2b017f2c283fc1e2d05b8edafb4698eb10`.
The existing 0.165 helper already proves that this catalog adds only Terra to
the retained 0.163/0.164 catalog and leaves Luna metadata unchanged. Candidate
source validation must confirm that before reusing canonical Luna SHA-256
`049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
No copied full catalog or manufactured version-specific Luna bytes are needed.

Preserve the existing strict `RunEphemeralTurn` contract on 0.163 with both
model profiles at low effort. Extend only the prompted naming compatibility
record for the selected 0.167 candidate; prompted support currently covers raw
0.164/0.165 Luna at low/high. Prompted native checks do not establish native
tool-effect isolation. Catalog content does not identify the native executable.

## Upstream schema delta

The official ClientRequest schema changes add optional additional-context names,
hook thread selection and an initialize capability for required human approval.
Detached review delivery is removed; the client does not request that mode.
Audio input becomes a placeholder with explicit runtime rejection; current
client requests use text/image inputs. Server changes include optional per-item
timestamps, image-generation identity and process drain status, a thread-section
notification, and the `policyCapacityUnavailable` error enum. Existing retry
classification must not acquire new eligibility merely because that enum exists.

`humanCommand` approvals require the new `requiredHumanApproval` initialize
capability; this client does not advertise it. Do not add the capability or new
approval UX as incidental upgrade work.

No consumed-field break or required core client edit was demonstrated from
official schemas. This is a source inspection result, not a passing protocol
check: official exports omit locally supplied queue/project/settings and other
extensions at both releases. Generate schemas from the exact packaged binary
and run the complete existing request-corpus and consumed-shape validator.

The config schema retains the fixed restriction keys inspected here and adds
feature/provider/network configuration. Its official 0.167 SHA-256 is
`66ed795352d32f2464778acd2e332b7fafe644246d540cdceec4663c56cfbc16`;
0.165 is `bc14a890a74c7f9a4eb83d772550fe8813c7f389f44c1f18499f0ce24a8e4a60`.
The required policy check must use exact patched candidate source.

## Native and persistent state

All 78 SQL migration files in the complete official trees are unchanged.
This does not establish downgrade or mixed-version write safety. Rollout
handling gains `DynamicToolsUpdated`; rollout canonicalization/rollback replay,
NFS migration and thread listener code change. Retain forward-only recovery and
test 0.165 to 0.167 with the existing disposable native state fixture.

Relevant native defaults: `deferred_tool_world_state` becomes stable and enabled;
`plugin_discovery_prefetch` is new and enabled. New `interrupt_on_cancel`,
`incremental_exec_tools`, `mcp_connection_sharing` and host-output truncation
flags default false. Preserve current fixed policy unless exact candidate checks
show a supported-contract defect. Models-manager now tracks catalog origins;
the existing native fixture must still prove CLI startup catalog selection and
sessionFlags origin. No isolation conclusion follows from unchanged JSON bytes.

## Smallest implementation and verification proposal

Subject to the architect's sufficient brief and lead acceptance:

1. Extend catalog refresh validation and add separate 0.167 prompted provenance;
   retain strict fixture, canonical Luna bytes and existing supported APIs.
2. Add the 0.167 prompted native selector and catalog source identity; add a
   0.165-to-0.167 state fixture selector after exact candidate identity is known.
   Make the existing conditional-steer native fixture select the reviewed 0.167
   candidate without discarding retained 0.165 coverage.
3. Update the repository-owned update skill/reference/API comments for supported
   versions and exact fixture invocation. Change client/protocol fixtures only
   for demonstrated compatibility needs, preserving corpus coverage.

Before final review: catalog reproducibility/hash checks, request-corpus coverage,
exact-binary generated-schema validation, patched-source fixed-policy validation,
focused Go tests and tagged compile-only coverage, browser checks, and packaged
flake checks. Known quick checks stay inline; uncertain-duration checks use a
fresh monitoring utility. Complete all intended source changes and commits before
the lead invokes independent final review.

After review: fresh watched namespace ownership control, 0.167 prompted native
fixture, 0.165-to-0.167 state fixture and exact conditional-steer fixture as
selected in the final brief. Preserve full source/input, binary/hash/catalog,
model/effort, cancellation, retry and process teardown evidence. Real-provider
naming canary and system/profile/native activation evidence belong to the runtime
and rollout packages. Do not rerun retained strict 0.163 tests without a relevant
source change or an explicit requirement in the accepted brief.

## Candidate handoff dependency

Implementer1 reports llm-agents revision
`d960982d3b05c294f3cf98cab3e23798548a0ced` evaluates Codex 0.167 to:

- output `/nix/store/22139ip2k5dfc272a1nv0br2ms0nymbv-codex-0.167.0`;
- derivation `/nix/store/9rxjqb3nzbf4b9s0bj3h4yl8igm105is-codex-0.167.0.drv`;
- unpatched source `/nix/store/j9bhifsiqjhxknbzmx46884jnr1lffrc-source`.

The derivation applies daemon-nix-store.patch, a chatgpt recursion limit of 256
and Cargo optimization settings. Neither source nor output was realized when
reported. The executable will be `output/libexec/codex/bin/codex`; exact binary
SHA-256 and patched-source schema/source graph remain pending. No build was
requested or launched by W-prep. The implementation release depends on the
accepted brief; exact-schema/native acceptance additionally depends on candidate
realization and source/binary evidence from the runtime package.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-codex-version-update/
