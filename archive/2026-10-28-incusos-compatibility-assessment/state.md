---
lifecycle: archived
---

# 2026-10-28-incusos-compatibility-assessment

## Status

- Phase: assessment delivered; stock IncusOS is incompatible with the current osctld system-container model. A maintained container derivative is conceivable, with central boot/security/storage/update contracts replaced; feasibility is not demonstrated.
- Identity verified by `dev-session current`, complete environment markers and the trusted thread binding, all matching this session and workspace.
- Architect0 (retained Astra/xhigh, workspace_write) owns substantive investigation/design. Lead owns scope and acceptance.
- Architect delegated independent read-only packages: implementer0 image/distconfig, implementer1 nested runtime/kernel/devices/storage, implementer2 vpsAdmin metadata/control mapping. Each owns its findings file; implementer3 remains unassigned because no further independent package is needed.

## Phase checklist

- [x] Verify identity, inspect retained roster and define assessment scope.
- [x] Inspect upstream IncusOS requirements and current image/configuration/runtime contracts.
- [x] Reconcile evidence into a compatibility verdict and implementation boundaries.
- [x] Deliver findings, uncertainty and viable next action.
- Implementation, runtime checks, independent change review and deployment: not requested; no changed product deliverable.

## Next actions

- No remaining assessment work. A future IncusOS port would need a separate scope decision accepting replacement appliance guarantees; an independent VM preserves the relevant boot/disk model.
- Leave this session open for follow-up. Lifecycle remains active; no closure action is authorized or performed.

## Documentation

- [Assessment plan](plan.md).
- [Compatibility assessment and source citations](design.md): accepted synthesis by architect0, including exact upstream startup failures and derivative boundaries.
- [Current image/distconfig evidence](vpsadminos-image-distconfig-findings.md): accepted at current staging; immutable-store support is possible with deliberate container contracts, while IncusOS's appliance contracts remain incompatible.
- [vpsAdmin integration evidence](vpsadmin-integration-findings.md): accepted, current source refreshed; no intrinsic template schema/API change, appliance management remains unsupplied.
- [IncusOS container boot/device/storage boundaries](vpsadminos-nesting-findings.md): accepted at current staging; no claim of runtime testing or production inventory. A citation typo was delegated back to its owner and corrected.
- Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-incusos-compatibility-assessment/

## Repositories

- Read-only inspection planned for canonical `repos/vpsadminos.git` and `repos/vpsadmin.git`; no registered feature refs or owned project worktrees.

## Commands run

- `dev-session current`, environment identity check, `dev-session team list ... --as-is`.
- Read required project/session/lifecycle/documentation/verification/git/commit procedures and documentation/handoff skills.
- Assignment to architect0 accepted with stable UUID `6bd6f4bc-b87d-4235-9880-06b6bd03ad65`.
- Initial tracking commit `19d702e31`; later findings/state retained in the working tree under normal tracking cadence. No project feature commits or remote writes.
- Lead acceptance spot-check: immutable upstream raw source for normal `run()` requirement guard, `CheckSystemRequirements`, mandatory LUKS discovery/PCR call and swap-labelled partition lookup. Paths/lines matched architect citations.
- `git diff --check` for owned tracking paths passed; final local Markdown links and file whitespace checked.

## Results

- User steering: ordinary-distribution Incus works already; assess IncusOS specifically. Relayed to architect and stopped unrelated nesting/alternative work.
- Assignment initially refused a descriptive message ID; retry with UUID succeeded without changing member settings.
- Upstream milestone from architect0: IncusOS main `539f012e716a7434e8429faf3232568a7aafb1d4` (2026-10-28 16:34 UTC) expects UEFI/own kernel, TPM-measured encrypted disks and A/B updates. Official Incus installation guide creates a VM. Current upstream permits either disabled Secure Boot or a software TPM as degraded modes, but not both; these do not establish container support. Source/runtime comparison pending.
- Local image/distconfig inspection uses vpsAdminOS `origin/master` at `4658d40f8ca459194b578aa30b0f9bb344cd7ee2`; implementer0 found no AGENTS.md at that revision and uses repository README/source.
- Evidence correction: that bare-ref revision is historical (kernel 6.1.32/LXC 5.0.2). Architect asked to coordinate current remote source inspection at fixed SHAs before drawing current version conclusions, without Git mutation. No production node inventory exists. Current Incus requirements and IncusOS bundled Incus version must be distinguished.
- Architect refreshed actual defaults through GitHub API: vpsAdminOS `staging=f40afdf844223410767a04d2a96215b1d796b967`, vpsAdmin `master=4cb66436558d4c494d658042192f7b743eddb54d`. Implementers instructed to refresh relevant files now, not defer to a future POC.
- Architect traced normal `incus-osd` startup to `CheckSystemRequirements`, followed by mandatory labelled LUKS partition discovery/PCR checking. This strengthens the verdict beyond an inference from UEFI boot-image expectations.
- Implementer2 refreshed 36 relevant vpsAdmin files at current default; all matched its pinned local source. Template metadata is extensible, but registration does not supply IncusOS appliance provisioning/API trust/storage/update semantics. Detailed source citations pending in its findings file.

## Open questions

- No unresolved question prevents the stock-IncusOS incompatibility conclusion. Runtime feasibility, patch set and security/update equivalence of a derivative remain unproven and outside this request.

## Verification and review limits

- Source inspection only at current published revisions; no image built, container started, production inventory, deployment or runtime success claimed.
- All three implementer packages accepted by architect; lead inspected synthesis and evidence files. Independent final change review does not apply: mandatory-change-review explicitly exempts investigation/findings/tracking alone; no substantive product/configuration/instruction changes exist.
- No migration, API/schema change, branch readiness or integration claim. Existing product documentation unchanged because no supported behavior changed; findings stay in their assessment/session home.

## Cleanup

- No owned running checks, machines, project worktrees or deployments. Preserve unrelated shared workspace changes and leave the session open.
