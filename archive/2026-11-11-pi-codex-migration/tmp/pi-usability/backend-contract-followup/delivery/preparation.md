# Ordinary portal-parity delivery preparation

Owner implementer0, 2026-11-20. Current session and retained roster68 settings
verified: Sol6.1/xhigh/workspace_write. This is preparation only; final independent
review bdc28478 / queuedSubmission01a1fab8-bef2-7e81-9fd8-f45f662118b8 has no main
accepted disposition in this package yet. R583ea68afddb23fbf1dde543a518bf6517b8092e /
tree9e4c08059a3cd0786ba5d02f3dfdc0c0d3295fc3 is the accepted source/quick candidate,
NOT a released publication/build target. Await main's exact reviewed head/tree.

## Retained exact baseline and recipe sources

- W root `worktrees/2026-11-11-pi-codex-migration/workspace-pi-cli-communication-stage-final`,
  e8ccae241373d13801dfd09c40df84d0034c669f /
  d4254382c9bd373cc772379d721067fe3958478c, read-only clean/index empty.
  Its Git common directory is the shared workspace `.git`; preserve its existing
  ordinary Git registration and known portal alias limitation. Do not create a
  replacement bare workspace repository or repair aliases.
- H root `worktrees/2026-11-11-pi-codex-migration/vpsfree-cz-configuration-pi-cli-communication-stage-final`,
  f7d69f9f23a6034ebb46ae150f72b027bcea953a /
  70057e0beba296b082d4676221f3e40fb27351b1, read-only clean/index empty.
  Canonical `repos/vpsfree-cz-configuration.git`; supported session registration.
- Retained selected app `/nix/store/gh680l33jv55f0pxnfi4sca1nmjcavl4-dev-workspace-0.2.0`;
  retained system `/nix/store/l4h78sa6ka86gijph33d29z67r538pqh-nixos-system-aitherdev-26.05.20261113.f1e5c35`,
  deriver `/nix/store/s4i92x06zx46d13rbrf8kbpf0qxnvba9-nixos-system-aitherdev-26.05.20261113.f1e5c35.drv`.
  These are accepted artifact references, not a fresh live observation.
- Existing source/lock/history: `tmp/pi-usability/team-ui-parity/pi-cli-communication/stage-delivery/source-freeze-handoff.json`
  and `frozen-inputs.json`. Existing reduced artifact shapes:
  `stage-delivery/deployment-prep/candidate.json` and `minimal-output-proof.json` /
  its corrected proof script/result. Reference them; do not execute an old immutable
  runner unchanged or export their full history again.
- Accepted route: `../delivery-compatibility.md`; H owning guide
  `docs/operations/pi-runtime-aitherdev.md`. Applicable workspace Git/commits,
  deployment/lifecycle/verification, R/W/H AGENTS, documentation/monitor guidance read
  or reused unchanged. H flake134-136 maps channel `dev-workspace`, role `devWorkspace`
  to flake input `devWorkspace`; no handwritten H lock edit.

## Execution only after main's single exact review release

1. Publish exact immutable reviewed R via canonical `repos/dev-workspace.git` /
   `git@github.com:aither64/dev-workspace.git` to a new unique dated feature ref.
   Fresh narrow default advertisement/fetch, fresh target absence, explicit absent
   lease, fetch and prove exact head/tree. Preserve prior/default refs; no blanket
   remote-ref inventory. Promptly report R publication; main owns CI disposition.
2. Fresh absence checks, then new isolated owned W
   `workspace-portal-backend-parity` and H
   `vpsfree-cz-configuration-portal-backend-parity` under the initiative worktree group,
   matching unique dated branches, from exact retained e8cc/f7d. W uses its established
   ordinary Git worktree route, with the portal alias limit explicit. H uses supported
   `dev-session worktree add` and declared hooks.
3. W changes only direct nested runtime URL to exact PUBLISHED R and runs
   `nix flake update vpsfree-dev-workspace/dev-workspace` in the new W root.
   Expected four runtime lock leaves: locked lastModified/narHash/rev and original.rev.
   Preserve extension/follows/siblings/Cb302/module/vendor/native/worker/catalog/policy.
   H command from new H root:
   `nix develop --no-write-lock-file --command confctl inputs channel set --commit dev-workspace devWorkspace REVIEWED_R`.
   Preserve generated messages/hooks and expected three runtime lock leaves; no sibling
   normalization. Stop on substantive unexpected delta.
4. Normal focused commits and mechanical pin-stream consolidation, retaining direct,
   consumed and deployed refs. Use existing proper W base
   fcbed7990960a914eae2241a39dce9ef989bccc0 (W5) and H base
   5c67e6a010462a850fb6258c486eeef4490c27d5 (H3), preserving inherited migration/consumer
   boundaries. Bind final/direct whole-tree and proper-base full-index equivalence;
   no source/default rewrite or unrelated history export.
5. Freeze exact clean final W/H heads/trees/four source-lock hashes. Run ONCE
   `bin/check-dev-workspace-deployment --workspace-root NEW_W --configuration-root NEW_H`.
   Both effective runtime identities must equal reviewed R. No intermediate mixed-
   revision exception. This is lock/site compatibility, not aggregate output proof.
6. Resolve CURRENT selected installed validated utilities.verification_watcher and
   matching native config at launch; verify actual catalog/model/effort/execution
   policy. ONE fresh Luna/low/full_access utility (if current installed policy agrees)
   owns this related pair; active parent retained and sole source-log observer.
   Rebind the small existing runner shape, no new framework, no pre-build full metadata
   evaluation, no stale utility reuse. Preserve original argv/logs/results/joins.
7. Concurrent independent ordinary builds, no disabled internal checks/substitutes:
   W: `nix build --json --print-build-logs --out-link NEW_EVIDENCE/W-app git+file://NEW_W?rev=FROZEN_W#packages.x86_64-linux.default`.
   H cwd NEW_H:
   `nix develop --no-write-lock-file --command confctl build --yes cz.vpsfree/machines/aitherdev`.
   Retain normal generated generation.json plus exact system output/deriver and input
   rev/source. No speculative source or output equivalence. Quiet build is not failure;
   no arbitrary timeout/retry. Unexpected local kernel build follows stop/escalation.
   Report launch, first artifact and terminal phases without withholding a completed
   artifact behind optional checks. Join every utility/source/cell/tool effect.
8. Minimal post-build physical proof only: actual app output/deriver and R source/NAR,
   physical new Go, exact Cb302/module/vendor binding, reporting4/live-switch2 contract,
   native package+wrapper and complete registration/startup/catalog/tool/worker inputs.
   Bind actual normal H generation's devWorkspace/source and system/deriver plus owning
   host module/helper/Pi/session-entry/unit/native inputs. Reuse accepted unchanged
   component evidence at scope; no whole-H equality or native-readiness assertion.
   Retain owned output link/GC root. No separate metadata/test/classification campaign.
9. After positive artifacts/proof and complete utility joins, parent-owned short W/H
   dedicated feature SSH publication with fresh narrow default/target absence leases
   and fetched exact head/tree proof. W remote
   `git@github.com:aither64/vpsfree-cz-workspace.git`; H remote
   `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`. Preserve all originals.
   Compact candidate/effect handoff links original receipts; main acceptance/activation
   follows. No default integration.

## Compatibility, ownership and present boundary

The accepted same-policy route retains reporting4/live-switch2, exact native binary,
full startup semantics, catalog/worker/host inputs, maintenance selection and retained
policy. Ordinary admission must prove the actual marker/input equivalence. It can
preserve native while restarting ordinary application services; Pi workers remain on
their retained packages. No updater bridge, forced selection, old journal replay,
maintenance-enablement change, native tool adoption or worker upgrade is prescribed.
Changed native/registration contract or actual gate refusal returns to main; no bypass.
Main owns claim/mapping, H dry/switch, W profile switch and immediate UI/continuity
acceptance. This member performs no activation/live target operation.

Owner4's NEW Waiting-to-send/manual-Retry investigation is independent. Do not include
or block on speculative fixes; only main can supply a proven reviewed successor.
User-directed native/recovery/composition-test/VM/browser/Ruby/separate-test campaigns
remain out of this ordinary artifact-preparation scope; ordinary package checks stay.
No publication, new worktree/pin/commit mutation, Nix metadata evaluation, build, native
utility or target action has started. All preparation reads/records are terminal.
The single current package is parked for main's review disposition and exact released
R head/tree; no automatic successor queue.
