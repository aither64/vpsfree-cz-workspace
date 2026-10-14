# Aitherdev portal attention rollout

Status: prepared outline, not executed.

## Authorization and scope

User direction in this conversation: "ok, proceed until it is implemented &
verified. you can also deploy aitherdev using vpsfree-cz-configuration."

This authorizes feature implementation, checks and aitherdev system/profile
deployment. It does not authorize master merges, reboots or session closure.
Configuration target is `cz.vpsfree/machines/aitherdev`; coordinator machine
identity is `vpsfree:aitherdev`.

## Sources and dependencies

Use same-session `dev-workspace`, `workspace` and `vpsfree-cz-configuration`
worktrees and their published feature heads. Keep the workspace extension and
unrelated inputs unchanged. The nested workspace runtime and configuration
`devWorkspace` channel must match the exact final runtime feature revision.
codex-web changes are unnecessary based on current prompt/activity contracts.

## Preparation and checks

Baseline composition check passed after upstream refresh, before this feature's
runtime pin: workspace nested runtime and configuration `devWorkspace` both
selected `ba8669b14536f72b559abc912bba8eac430111e4`. Repeat against final feature
locks after generating the new pins.

1. Complete application changes and owning-project feature/operations docs.
2. Complete quick checks, committed whole-branch inventory and independent final
   review before long integration or browser proof. Reconcile findings.
3. Publish runtime. Generate workspace nested lock and configuration channel pin
   through their owning commands. Include final composition in history review.
4. Run `bin/check-dev-workspace-deployment` against both final locks, then
   package/CI/browser checks under fresh verification watchers.
5. Prepare exact machine/profile snapshots with checksummed session evidence.
   Record deployment approval using the user quote above. Request the machine
   reservation near completed preparation; declare every registered obligation.
6. Submit machine activation and profile activation jobs with explicit ordering.
   Build/copy outside claims. Wait interruptibly; no direct activation bypass.

## Live acceptance

- Check matching selected runtime/system composition, portal/router health and
  continued Codex/tmux access after activation.
- Check title markers, creation/settings controls and authenticated worker/API
  delivery on the deployed portal.
- Check no-tab server observation and sender/service-worker integration without
  conflating provider acceptance with OS notification display.
- Actual Firefox/macOS and Chrome/Chromium permission/subscription is a browser
  action. The Test notification control must permit validation while another
  tab is active and all portal tabs are closed, browser running minimized or
  unfocused. Record actual OS display only with corresponding evidence.

## Recovery and reservation

Retain original operation IDs, artifacts, GC roots and deployment logs. Unknown
effects require reconciliation of the original job; do not replay activation.
Profile recovery follows the selected package's forward-only policy. Retain
private notification keys/preferences across package updates; do not publish
subscriptions, keys, endpoints or credentials as artifacts.

The earlier foreign review hold cleared at coordinator revision 538. Prepare
independently and request ownership near deployment. Once granted, retain our reservation during
UI review/feedback. Normal release requires integrated final heads and explicit
deployment/review completion. No integration approval has been supplied.
