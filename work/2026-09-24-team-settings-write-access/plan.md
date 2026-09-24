# Team settings drafts and member write access

## Goal and affected projects

Fix the portal Team tab so background refreshes do not overwrite unsaved member
model/reasoning choices. Make future design members able to write assigned
design artifacts, and let members run read-only session identity commands from
their Codex sandboxes. Keep implementation work with the implementation member
instead of shifting it to the lead after a misleading permission error.

- `dev-workspace`: Team browser controls, session-detail refresh, CLI transition
  lock handling, tests, and portal documentation.
- This coordination workspace: installed team catalog, lead/architect guidance,
  catalog tests, and site team documentation.
- `codex-web` and `vpsfree-dev-workspace` are not expected to change. The
  existing client already passes each member's retained sandbox policy.

## Design

1. Scope conversation settings refreshes away from Team forms. Track Team
   edits and focus so session-detail polling does not replace an in-progress
   form; leave other session refreshes running and apply pending Team HTML when
   editing ends or after the existing successful-save reload. Preserve choices
   and error text on a failed save. Show the saved access mode for each member.
2. For `current`, `list`, `url`, and `team list`, acquire an existing host
   transition lock with a read-only descriptor and a shared flock. Do not
   create the lock from these read-only commands; fail clearly if it is absent.
   Keep generation checks under the lock. Mutating commands retain their
   existing writable lock path.
3. Set the installed designer/architect role to `workspace_write` for new
   teams. Its instructions permit assigned design artifacts, not source
   implementation. The implementer remains `workspace_write`; the reviewer
   remains `read_only`. Guide the lead to check the recorded role access and
   exact error before taking over delegated implementation.

## Compatibility and rollout

The user chose **future teams only** for the architect permission change.
Existing rosters, including `2026-09-23-storage-redesign`, remain untouched;
their access and instructions stay frozen. The existing implementer benefits
from the read-only CLI fix without a roster migration. No persisted schema,
database, public API, or Codex protocol changes are planned. The new package
can read old rosters and a rollback can read new rosters; only catalog defaults
for newly created teams change. No vpsAdminOS/node update is involved.

After quick verification and mandatory review, run longer packaged checks and
a minimal live permission canary, then deploy the workspace application through
its user profile on aitherdev. Deployment does not authorize merging feature
content into default branches; await explicit repository/target approval.

## Verification and documentation

- Browser regression: edit model and effort, force conversation and details
  refreshes, confirm values and focus persist; test save payload, failed-save
  retry, and an idle Team refresh.
- Ruby lock tests: read-only commands can acquire the host lock when its
  containing state directory is not writable; they still block on an exclusive
  transition and reject a changed generation. Mutating commands remain gated.
- Catalog/runtime checks: new architect and implementer use workspace-write,
  reviewer stays read-only. Verify a minimal live member can run
  `dev-session current` and edit an owned worktree.
- Update the generic portal guide for member access/refresh behavior and site
  team documentation for the future-team policy. The likely readers are team
  operators and future portal maintainers; transient rollout evidence stays in
  this initiative state.
