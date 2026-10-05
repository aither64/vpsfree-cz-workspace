---
lifecycle: active
---
# 2026-07-20-webui-requests-error

## Repositories

- `vpsadmin`
  - branch: `2026-07-20-webui-requests-error`
  - base: `origin/master` at `08ef57462`
  - merged/pushed default: `master` at `9773ac2bd`
- `vpsfree-cz-configuration`
  - branch: `2026-07-20-webui-requests-error`
  - base: `origin/master` at `d42caeed`
  - feature/default commit: `1931c5d4`
  - merged/pushed default: `master` at `1931c5d4`
- `haveapi-client-php`: read-only inspection at `a8b1b403a75a29287659ea983957c42d9a071214`
- `haveapi`: read-only inspection at `origin/master` (`e374966`)
- `vpsadmin-kb-captures`
  - branch: `2026-07-20-webui-requests-error`
  - base: `origin/master` at `8d0ff0913`
  - merged/pushed default: `master` at `b9eb59ebc`

## Status

The implementation and its exact documentation pin are merged into and pushed
on their default branches. The `vpsadmin` channel in
`vpsfree-cz-configuration` is updated to `9773ac2bd`; all 11 vpsAdmin service
machines built successfully, and configuration `master` is pushed at
`1931c5d4`. All initiative worktrees and their generated build/dev-shell
artifacts are removed; feature branches are retained locally and remotely.

## Commands run

- Verified the active development-session slug and inspected workspace status.
- Fetched `vpsadmin`, `haveapi-client-php`, and `haveapi` origins.
- Created the vpsAdmin initiative branch and worktree from current
  `origin/master`.
- Inspected the failing WebUI line, request API resource/model, user lifecycle
  model and chains, PHP client lazy association resolution, and HaveAPI Ruby
  association serialization.
- Attempted a read-only production probe with `confctl ssh` and direct SSH.
  The available identity was not authorized, so no production database query
  was run.
- Ran a temporary focused API example in the vpsAdmin API development shell;
  removed the example and generated gem cache after the run.
- Re-entered the API development shell for implementation verification. Its
  shell hook already changes into `api/`; the initial command's extra `cd api`
  therefore failed before running specs. Recorded the reusable invocation in
  `notes/vpsadmin/2026-07-20-api-devshell-working-directory.md`.
- Ran `bundle exec rake vpsadmin:i18n:update`; the generated locale catalogs
  were already normalized and did not change.
- Installed/confirmed Overcommit hooks with `nix develop -c overcommit
  --install` and ran `nix develop -c overcommit --run` on the staged change.
- The first `git commit` attempt was made from the ambient shell and was
  rejected because commit-time hooks could not find their Nix-provided tools.
  No commit was created. Recorded the required invocation in
  `notes/vpsadmin/2026-07-20-overcommit-requires-root-devshell.md`; the commit
  was rerun successfully with `nix develop -c git commit -F ...`.
- Pushed vpsAdmin head `9773ac2bd` to
  `origin/2026-07-20-webui-requests-error` over SSH.
- Created the `vpsadmin-kb-captures` worktree and pinned `flake.nix`,
  `flake.lock`, `captures.json`, and `contract/navigation.yml` to the exact
  vpsAdmin feature revision.
- Ran `nix develop -c bin/check` in `vpsadmin-kb-captures`; the complete
  documentation contract and screenshot inventory passed without drift.
- Committed the mechanical documentation pin as `b9eb59ebc` and pushed it to
  `origin/2026-07-20-webui-requests-error` over SSH.
- Inspected GitHub Actions for vpsAdmin head `9773ac2bd`. WebUI PHPUnit, i18n
  health, and RuboCop completed successfully. The parallel API workflow had 24
  of 26 successful jobs with only its core/full platform shards still running.
- Confirmed the integration selector intentionally chose the full `tag=ci`
  suite because a requests-plugin model changed. That long workflow remained
  in progress without a failure at handoff; its focused `webui#users-admin`
  regression had already passed locally.
- Rechecked the pushed vpsAdmin Actions before integration. The complete API
  matrix, WebUI PHPUnit, i18n health, and RuboCop workflows succeeded; the
  intentionally broad `tag=ci` integration workflow was still active without
  a reported failure.
- Fetched all affected repositories, created fresh temporary default-branch
  worktrees, and integrated vpsAdmin `9773ac2bd` and the capture pin
  `b9eb59ebc` with fast-forward-only merges before pushing both `master`
  branches over SSH.
- An initial merge command remained in the coordination checkout after
  `git worktree add`; its merge failed and its push was a no-op. No repository
  changed. Retried with explicit `git -C` paths and recorded the reusable
  lesson in
  `notes/cross-project/2026-07-20-worktree-add-does-not-change-directory.md`.
- Recreated the configuration feature worktree, installed its declared
  Overcommit hooks in `nix develop`, and ran `confctl inputs channel update
  --commit vpsadmin` with changelog generation enabled.
- `confctl` generated `1931c5d4` (`inputs: update vpsadminServices to
  9773ac2b`), changing only `flake.lock`. Nixfmt and commit-message hooks
  passed, with only the generated changelog's advisory 72-column warning.
- Pushed the configuration feature branch, fast-forwarded it into a fresh
  `master` worktree, and pushed `master` from `nix develop` so the mandatory
  pre-push hook could run. The first ambient-shell push was blocked by the hook
  because its gems were unavailable and did not update the remote.
- Verified with local refs and `ls-remote` that each repository's local/remote
  feature and `master` refs are identical: vpsAdmin `9773ac2bd`, captures
  `b9eb59ebc`, and configuration `1931c5d4`.
- After the vpsAdmin `master` push, WebUI PHPUnit, RuboCop, and i18n health were
  green. The repeated API matrix was active and full integration was queued;
  the same-head feature API matrix was already green and its full integration
  run remained active, so no mismatched-head workflow qualified for
  cancellation.

## Implementation progress

- Added `UserRequest#raw_user_id` and admin-only Index/Show API output.
- Added an early model guard preventing resolution when a stored user ID no
  longer has a visible user association.
- Made approval-request list and detail rendering null-safe, with the raw ID as
  the historical fallback and no resolution controls for a missing user.
- Added API coverage for active, soft-deleted, and hard-deleted owners,
  non-admin field redaction, and the resolution guard.
- Extended the existing `webui#users-admin` fixture and Playwright scenario
  with a denied hard-deleted-user request.
- Initially committed the six-file vpsAdmin change as `272c5d5b` (`webui:
  handle requests from hard-deleted users`) on
  `2026-07-20-webui-requests-error`.
- Commit-time hooks passed. The commit-message TextWidth hook warned about
  lines over its advisory 72-column limit; all lines satisfy the workspace's
  mandatory 80-column limit.

## Quick verification

- `nix develop .#api -c bash -lc 'bundle exec rspec
  spec/api/plugins/requests/change_spec.rb'`: 25 examples, 0 failures.
- Targeted RuboCop: 3 files inspected, no offenses.
- `php -l webui/forms/users.forms.php`: no syntax errors.
- `node --check tests/playwright/webui/specs/users-admin.spec.cjs`: passed via
  `nix shell nixpkgs#nodejs` because Node is not in the ambient/WebUI shell.
- `nix-instantiate --parse tests/suite/webui.nix`: passed.
- `git diff --check`: passed.
- Required Overcommit pre-commit hooks: all passed (`MigrationSpecs`,
  `VpsadminWebuiI18n`, `Nixfmt`, `VpsadminApiI18n`, `PhpCsFixer`, `RuboCop`).
- `./test-runner.sh test 'webui#users-admin'`: passed. The Playwright example
  completed in 370.4 seconds; the test script completed in 846.96 seconds and
  the full test completed in 1128.48 seconds (`1 test successful`).
- `vpsadmin-kb-captures`: `nix develop -c bin/check` passed its syntax checks,
  38-control/29-path/32-concept contract validation, 65-binding annotation
  validation, 15 test runs with 67 assertions, and the 118-PNG inventory.
- `nix develop -c confctl build 'cz.vpsfree/vpsadmin/*'`: built all 11
  vpsAdmin service machines successfully and recorded generation
  `2026-07-20--21-02-51`.

## Mandatory change review

- Reviewer: standalone fresh-context agent `/root/mandatory_change_review`.
- Reviewed base/head: `08ef57462..272c5d5b9`.
- Result: one Blocking, one Important, and one Advisory finding.
- Blocking: the browser URL filtered through typed `User` input using the
  hard-deleted ID, which would fail resource resolution before rendering; its
  numeric assertion was also ambiguous because the ID appeared in the filter.
- Important: the guard checked only `user_id && !user`, allowing an invalid or
  legacy null-owner `ChangeRequest` to reach resolution, especially `ignore`.
- Advisory: the browser detail scenario did not assert the stored requested
  full name, e-mail, and address.
- Decision: address all findings before the long browser test. Remove the user
  filter and scope the raw-ID assertion to the rendered definition-list row;
  make the resolution requirement subtype-aware so change requests always
  require a user while initial registration requests remain valid; add a
  null-owner ignore API regression; export and assert all stored requested
  values. Amend the unpublished functional commit after quick verification.
- Reviewer otherwise found the additive API, non-admin redaction,
  mixed-version attribute fallback, soft-delete behavior, and deployment/
  rollback compatibility sound. Residual risk: a concurrent hard-delete after
  the pre-resolution association check remains a low-probability race.
- Follow-up verification passed: two ChangeRequest missing-user resolution
  examples (hard-deleted ID and null owner), three RegistrationRequest examples
  (deny, deny with unavailable template, and approve/create user), targeted
  RuboCop, Node syntax, Nix parsing, `git diff --check`, and the full required
  Overcommit pre-commit suite.
- Amended the unpublished functional commit with all review fixes. Final
  reviewed/fixed head is `9773ac2bd` with seven changed files. Commit-time hooks
  passed; only the advisory 72-column commit-message warning remained, while
  every line is within the mandatory 80-column limit.
- The subsequent capture-repository change is only an exact dependency and
  generated lock pin. It has no code or design change, so the workspace's
  explicit mechanical-update exception applies and no second mandatory review
  was run.
- The configuration change is likewise a generated one-input lock update made
  through `confctl`, so the mechanical-update review exception applies.

## Results

- The WebUI fails at `$r->user->login` in
  `webui/forms/users.forms.php`.
- HaveAPI serializes a missing ActiveRecord association as `null`.
- The PHP client treats a typed resource value of `null` as an unresolved
  association, has no path parameters to apply to `user#show`, and raises the
  observed `UnresolvedArguments` exception.
- `User`'s default scope excludes `hard_delete` only. It still includes
  `soft_delete`, so a soft-deleted owner remains resolvable through
  `ChangeRequest#user`; a hard-deleted owner does not.
- Hard deletion retains the user database row in `hard_delete` state and
  retains its user-request rows, so historical change requests can expose a
  `null` association even though `user_requests.user_id` remains populated.
- Focused local API reproduction passed: the same denied change request
  serialized its `user` as a resource reference while its owner was
  `soft_delete`, and serialized `user: null` after the owner was changed to
  `hard_delete` (`1 example, 0 failures`).
- A request with a genuinely null/orphaned `user_id` would produce the same
  client failure, but normal `ChangeRequest` validation requires a user. The
  hard-delete/default-scope path is therefore the expected production cause.

## Recommended solution

- Fix the vpsAdmin WebUI first. Check the association through the PHP client's
  null-safe `$r->user_id` accessor before ever accessing `$r->user`, resolve it
  at most once, and render a deleted/unavailable-user marker when it is absent.
- Apply the same handling to both the approval-request list and details form.
  When the user is absent, show the values stored on the request without
  comparing them to a current user record, and do not offer actions which could
  apply changes to that user.
- Add an API-side guard so a `ChangeRequest` whose user association is missing
  cannot be approved or otherwise re-resolved accidentally. Return a normal
  action error instead of allowing a model `NoMethodError`.
- Follow the established IP address assignment pattern: add
  `UserRequest#raw_user_id`, expose additive integer `raw_user_id` in the
  requests API, and blacklist it for non-admin Index/Show output as appropriate.
  The WebUI can then use the resolvable typed `user` association when
  `$r->user_id` is present and fall back to `$r->raw_user_id` otherwise. This
  preserves the historical database foreign key without making hard-deleted
  `User` resources globally visible. Consider the same `raw_admin_id` treatment
  for historical resolver attribution.
- Separately harden `haveapi-client-php` so a typed resource attribute whose
  value is JSON `null` is returned as PHP `null` instead of triggering a lazy
  Show action with no path arguments. This is a framework correctness fix, but
  it does not replace explicit null handling in the WebUI.
- Do not remove `User`'s hard-delete default scope or make `User#show` globally
  unscoped as part of this fix. That would expand the visibility and behavior
  of hard-deleted users across unrelated API and WebUI paths.

## Implementation decision

- Implement only the established vpsAdmin raw-ID pattern in this initiative;
  do not expand scope to the independent HaveAPI PHP client.
- Add `raw_user_id` to the common request output and blacklist it for
  non-admin Index/Show responses.
- Use the PHP client's raw attribute map for the additive field so a new WebUI
  does not depend on the API and WebUI being deployed atomically.
- Preserve historical request display, but do not show resolution controls and
  reject direct API resolution when a change request's user association is
  missing.
- Add API and existing `webui#users-admin` regression coverage.
- Follow the WebUI documentation contract after the exact vpsAdmin commit is
  available to pin.

## Open questions

- None blocking implementation or deployment. The exact production row remains
  unconfirmed because production SSH access was unavailable, but the focused
  reproduction verifies the complete hard-delete/default-scope failure path.

## Cleanup

- Removed the initial diagnostic vpsAdmin worktree after confirming it was
  clean, then recreated it when implementation was approved.
- Removed temporary gem caches and diagnostic SSH known-host files.
- Removed the vpsAdmin, capture-contract, and configuration feature worktrees
  plus all three temporary default-branch merge worktrees.
- The forced configuration worktree removal also removed only its known
  generated `.bin`, `.bundle`, and `.confctl` build/dev-shell artifacts.
- Pruned worktree metadata and removed the now-empty
  `worktrees/2026-07-20-webui-requests-error/` directory.
- Kept all local and remote initiative branches according to workspace policy.
