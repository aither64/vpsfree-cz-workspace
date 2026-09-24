# Team settings drafts and member write access

## Goal and affected projects

Fix the portal Team tab so background refreshes do not overwrite unsaved member
model/reasoning choices. Make future design members able to write assigned
design artifacts, and let members run read-only session identity commands from
their Codex sandboxes. Keep implementation work with the implementation member
instead of shifting it to the lead after a misleading permission error.

- `dev-workspace`: Team browser controls, session-detail refresh, CLI transition
  lock handling, tests, and portal documentation.
- `vpsfree-dev-workspace`: pin the reviewed generic runtime revision so the
  site package includes the fixes.
- This coordination workspace: installed team catalog, lead/architect guidance,
  catalog tests, site team documentation, and the extension pin.
- `codex-web` is not expected to change. The existing client already passes
  each member's retained sandbox policy.

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
4. Keep host package-switch validation aligned with the frozen direct-team
   snapshots accepted by session creation. Accept legacy read-only architect
   snapshots and expanded snapshots with saved read-only or workspace-write
   architect access; do not apply current catalog defaults to old journals.
5. When the installed host command cannot parse otherwise valid persisted
   state, permit an explicit switch from the exact package built from source.
   Require an unchanged installed profile and run the ordinary journal,
   cluster, runtime, Codex, activation, and recovery sequence under the same
   transition lock. Quiesce and pre-selection recovery use the installed
   session helper; post-selection restore uses the candidate. Other candidate
   commands remain refused.
6. At the user's later explicit request, add a role-neutral CLI `team
   update-access` operation for one ready member. It must hold the existing
   session/team operation locks, require that member's Codex thread to be
   idle, validate the requested access against retained purpose, and preserve
   its address, thread, instructions, model, effort, and history. Clear the
   member's catalog digest for a manual override. Apply it only to
   `architect0` in `2026-09-23-storage-redesign`, then verify a real worktree
   write. Do not implicitly update any other member or team.

## Compatibility and rollout

The user initially chose **future teams only** for the architect permission
change, then explicitly requested a one-member exception for `architect0` in
`2026-09-23-storage-redesign`. Other existing rosters and members stay frozen.
The selected member retains its thread identity, instructions, and model/effort;
its saved access changes and its catalog digest is cleared. The existing
implementer benefits from the read-only CLI fix without a roster migration.
No persisted schema,
database, public API, or Codex protocol changes are planned. The new package
can read old rosters; only catalog defaults for newly created teams change.
The user-profile package is forward-only, and an older package need not read
newly expanded creation snapshots. No vpsAdminOS/node update is involved.
An existing ready schema-3 creation journal already stores an expanded preset;
the host switch must validate that frozen shape without requiring a migration
or changing the other session. Expanded snapshots remain forward-only as
described in the generic portal guide.

The site package consumes the extension flake, which pins the generic runtime.
Update the extension's generic input and the site's extension input in that
order after their feature revisions are available remotely. The installed
package must select both exact heads. After quick verification and mandatory
review, run longer packaged checks, deploy the workspace application through
its user profile on aitherdev, and then run a minimal live permission canary
against the activated package.
For this rollout, the installed switch rejects a ready expanded creation
journal before it builds the fixed package. Use the candidate's explicit
`--from-candidate` switch entry from the final site worktree. Do not alter the
other session's saved journal.
Deployment does not authorize merging feature content into default branches;
await explicit repository/target approval.

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
- Verify extension and site dependency pins resolve to the exact reviewed
  generic and extension heads; retain feature refs until integration approval.
