---
lifecycle: active
---
# 2026-06-06-vpsadmin-user-timezone

## Repositories

- `vpsadmin`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-06-vpsadmin-user-timezone/vpsadmin`
  - Branch: `2026-06-06-vpsadmin-user-timezone`
  - Base: `origin/master` at `a5b59432d packages: update gem dependencies`
  - Remote: `git@github.com:vpsfreecz/vpsadmin.git`
- `web`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-06-vpsadmin-user-timezone/web`
  - Branch: `2026-06-06-vpsadmin-user-timezone`
  - Base: `origin/master` at
    `ea0f19c Use planned and unplanned outage wording in FAQ`
  - Remote: `git@github.com:vpsfreecz/web.git`
- `vpsfree-mail-templates`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-06-vpsadmin-user-timezone/vpsfree-mail-templates`
  - Branch: `2026-06-06-vpsadmin-user-timezone`
  - Base: `origin/master` at
    `22e73932 outage_report: include advisory CVEs in announcements`
  - Remote: `git@github.com:vpsfreecz/vpsfree-mail-templates.git`
- `vpsfree-cz-configuration`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-06-vpsadmin-user-timezone/vpsfree-cz-configuration`
  - Branch: `2026-06-06-vpsadmin-user-timezone`
  - Base: `origin/master` at
    `50726274 packages: update vpsfree-irc-bot`
  - Remote: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
- Workspace `dev-clusters/vpsadmin`
  - Changed in `/home/aither/workspace/ai/vpsfree.cz`.

## Status

- Worktrees prepared for `vpsadmin`, `web`, `vpsfree-mail-templates`, and
  `vpsfree-cz-configuration`.
- Exploration complete; implementation plan written in `plan.md`.
- Implementation complete across the affected worktrees and workspace
  devcluster helper.
- Changes committed in logical steps across the affected repositories and the
  workspace devcluster helper.
- `vpsfree-cz-configuration` branch pushed to origin so the DNS/config change
  can be deployed from
  `origin/2026-06-06-vpsadmin-user-timezone`.
- After internal DNS and aitherdev were deployed, the vpsAdmin devcluster was
  started successfully for this slug.
- Focused vpsAdmin API specs pass.
- External mail template ERB/Ruby syntax checks pass.
- Devcluster config Nix build passes with the active `web` and mail-template
  worktrees wired in.
- `vpsfree-cz-configuration` builds pass for `aitherdev` and all internal DNS
  consumers.
- PHP syntax checks and whitespace checks pass.
- Public `web` RSpec tests were not run because they drive Selenium against
  the live `vpsfree.cz`/`vpsfree.org` registration pages.
- Tracking files changed in workspace:
  - `work/2026-06-06-vpsadmin-user-timezone/plan.md`
  - `work/2026-06-06-vpsadmin-user-timezone/state.md`

## Commands run

- `bin/dev-session current`
  - Reused active slug `2026-06-06-vpsadmin-user-timezone`.
- `git --git-dir=repos/vpsadmin.git remote -v`
  - Verified SSH remote.
- `git --git-dir=repos/web.git remote -v`
  - Verified SSH remote.
- `bin/dev-session worktree add 2026-06-06-vpsadmin-user-timezone vpsadmin --as-is`
  - Created the vpsAdmin worktree, but Overcommit post-checkout reported that
    the `overcommit` gem is not installed in the ambient shell.
- `bin/dev-session worktree add 2026-06-06-vpsadmin-user-timezone web --as-is`
  - First attempt failed because the bare `web.git` had `HEAD` pointing to
    `refs/remotes/origin/master` and no local `refs/heads/master`.
- `git --git-dir=repos/web.git fetch origin master:refs/heads/master`
  - Created local bare `master` branch for `web.git`.
- `git --git-dir=repos/web.git symbolic-ref HEAD refs/heads/master`
  - Normalized bare `web.git` HEAD.
- `bin/dev-session worktree add 2026-06-06-vpsadmin-user-timezone web --as-is`
  - Created the web worktree.
- `bin/dev-session worktree add 2026-06-06-vpsadmin-user-timezone vpsfree-mail-templates --as-is`
  - Created the mail templates worktree.
- `bin/dev-session worktree add 2026-06-06-vpsadmin-user-timezone vpsfree-cz-configuration --as-is`
  - Created the configuration worktree; the command reported an ambient Ruby
    Overcommit/Gemfile load error, but the worktree was created successfully.
- Read local instructions:
  - `vpsadmin/AGENTS.md`
  - no `AGENTS.md` found in `web`.
  - `vpsfree-mail-templates/AGENTS.md`
  - `vpsfree-cz-configuration/AGENTS.md`
- Explored relevant code with `rg` and `sed`, including:
  - `api/models/user.rb`
  - `api/lib/vpsadmin/api/resources/user.rb`
  - `api/models/mail_template.rb`
  - `api/models/mail_template_translation.rb`
  - `api/lib/vpsadmin/api/mail_templates.rb`
  - `plugins/requests/api/models/registration_request.rb`
  - `plugins/requests/api/resources/registration.rb`
  - `plugins/requests/api/db/migrate/*`
  - `webui/lib/functions.lib.php`
  - `webui/public/index.php`
  - `webui/pages/page_adminm.php`
  - `web/lib/form.php`
  - `web/lib/register.php`
  - `web/js/form.js`
  - `web/en/registration/*`
  - `web/cs/prihlaska/*`
  - registration and API specs.
- Implemented vpsAdmin changes:
  - added nullable `users.time_zone`;
  - added nullable `user_requests.time_zone` for registration requests;
  - added API-visible nullable `time_zone` fields for users and registration;
  - validated IANA timezone identifiers with TZInfo;
  - allowed users to update their own `time_zone`;
  - copied registration request `time_zone` to the approved user;
  - added mail-template `local_time`/`local_date` helpers and converted
    date-time template formatting away from `.localtime.strftime`;
  - set PHP webui request timezone from the authenticated user's setting, with
    nullable fallback to the captured server default;
  - added a visible profile select for timezone configuration.
- Implemented public `web` changes:
  - added a visible registration timezone select;
  - defaulted the select from `Intl.DateTimeFormat().resolvedOptions().timeZone`;
  - included `time_zone` in validation, preview restoration, and API submit
    payloads.
- Implemented `vpsfree-mail-templates` changes:
  - converted timestamp formatting from `.localtime.strftime(...)` to
    `local_time(...)`;
  - used `local_date(...)` for timestamp-backed date-only displays;
  - left pure membership/payment validity dates as business dates.
- Implemented devcluster changes:
  - added `web-cs.aitherdev.int.vpsfree.cz` and
    `web-en.aitherdev.int.vpsfree.cz` to default domains and URL output;
  - passed `worktrees/<slug>/web` into Nix as
    `VPSADMIN_DEVCLUSTER_WEB_SOURCE`;
  - live-mounted the web worktree in the services VM and generated a dev
    `config.php` pointing to `https://api.aitherdev.int.vpsfree.cz`;
  - added nginx/PHP-FPM vhosts for the Czech and English web roots.
- Implemented `vpsfree-cz-configuration` changes:
  - removed the old `containers.vpsfree-web` setup from `aitherdev`;
  - removed the now-unused TCP 80 firewall exception on `aitherdev`;
  - repointed internal DNS aliases `web-cs.aitherdev.int` and
    `web-en.aitherdev.int` to `frontend.aitherdev.int.vpsfree.cz.`;
  - incremented the internal zone serial to `2026060701`.
- `nix develop .#api -c bundle exec rspec spec/api/plugins/requests/registration_spec.rb`
  - Passed: 29 examples, 0 failures.
- `nix develop .#api -c bundle exec rspec spec/api/resources/user_write_spec.rb spec/api/plugins/requests/registration_spec.rb spec/models/mail_templates_spec.rb`
  - Passed: 84 examples, 0 failures, 1 pending.
  - Pending example is the existing soft-delete authentication pending case.
  - Re-run after the external-template/devcluster/config changes with the same
    result.
- `ruby -c` on changed Ruby API files, specs, and migrations
  - Passed.
- `php -l` on changed vpsAdmin webui PHP files
  - Passed.
- `php -l` on changed public `web` PHP files
  - Passed.
- `git diff --check` in `vpsadmin` and `web`
  - Passed.
- `ruby -rerb -e 'ARGV.each { |path| RubyVM::InstructionSequence.compile(ERB.new(File.read(path), trim_mode: "-").src) }' ...`
  - Passed for all `vpsfree-mail-templates` ERB files.
- `nix develop -c ruby -c $(rg -l "" -g 'meta.rb')`
  - Passed for `vpsfree-mail-templates` metadata files.
- `nix develop -c ruby -rerb -e 'ARGV.each { |path| RubyVM::InstructionSequence.compile(ERB.new(File.read(path), trim_mode: "-").src) }' ...`
  - Passed for all `vpsfree-mail-templates` ERB files inside the repo Nix
    shell.
- Searched mail template directories for remaining date-time
  `.localtime.strftime` usage
  - No matches.
- Searched `vpsfree-mail-templates` for remaining `.localtime`
  - No matches.
- Checked ActiveSupport timezone lookup against all TZInfo identifiers in the
  vpsAdmin API bundle
  - All identifiers resolved.
- `jq empty dev-clusters/vpsadmin/default-config.json`
  - Passed.
- `bash -n dev-clusters/vpsadmin/bin/devcluster`
  - Passed.
- `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt ...`
  - Formatted changed Nix files.
- `dev-clusters/vpsadmin/bin/devcluster status 2026-06-06-vpsadmin-user-timezone`
  - Cluster is stopped.
- `dev-clusters/vpsadmin/bin/devcluster config 2026-06-06-vpsadmin-user-timezone`
  - Merged config includes `domains.webCs`, `domains.webEn`, and `web`.
- `dev-clusters/vpsadmin/bin/devcluster urls 2026-06-06-vpsadmin-user-timezone`
  - URL output includes Web CS and Web EN.
- `nix build --impure ... path:/home/aither/workspace/ai/vpsfree.cz/dev-clusters/vpsadmin#cluster-config`
  - Passed; built cluster config with active `vpsadmin`, `web`,
    `vpsfree-mail-templates`, and `vpsfree-cz-configuration` worktrees.
- `nix develop -c confctl build --yes cz.vpsfree/machines/aitherdev`
  - Passed; built generation `2026-06-07--09-24-56`.
- `nix develop -c confctl build --yes --tag all-internal-dns`
  - Passed; built generation `2026-06-07--09-26-54` for:
    `brq/int.ns1`, `prg/int.mon1`, `prg/int.mon2`, and `prg/int.ns1`.
- `nix develop -c overcommit --sign`
  - Signed the vpsAdmin Overcommit configuration before the first commit.
- `nix develop -c overcommit --sign pre-commit`
  - Signed vpsAdmin pre-commit hooks before committing.
- `nix develop -c git commit -F <tmpfile>`
  - Ran vpsAdmin hooks for both commits. RuboCop found style issues before
    the final commits; they were fixed and the hooks passed on retry.
- `git commit -F <tmpfile>` in `web`
  - No hook framework was declared in the repository.
- `git commit -F <tmpfile>` in `vpsfree-mail-templates`
  - No hook framework was declared in the repository.
- `git commit -F <tmpfile>` in the workspace root
  - No hook framework was declared in the coordination workspace.
- `nix develop -c git commit -F <tmpfile>` in `vpsfree-cz-configuration`
  - Ran Overcommit Nixfmt and commit-message hooks; all passed.
- Removed transient untracked `.bin/` and `.bundle/` directories generated by
  the `vpsfree-cz-configuration` Nix/Overcommit commit path.
- `git push -u origin HEAD:2026-06-06-vpsadmin-user-timezone`
  - First ambient-shell attempt failed because Overcommit could not load the
    repository bundle.
- `nix develop -c git push -u origin HEAD:2026-06-06-vpsadmin-user-timezone`
  - Passed; created remote branch
    `origin/2026-06-06-vpsadmin-user-timezone`.
- `dev-clusters/vpsadmin/bin/devcluster start 2026-06-06-vpsadmin-user-timezone`
  - First run reissued the local server certificate for `web-cs` and `web-en`,
    then exposed two startup bugs:
    - services VM shared source mounts were configured under
      `virtualisation.fileSystems`, leaving `/mnt/vpsadmin` and `/mnt/web`
      absent;
    - `api/db/schema.rb` contained `users.time_zone` but still used schema
      version `2026_06_01_120000`, so fresh database setup loaded the column
      and then tried to run `20260606223000_add_users_time_zone` again.
- `dev-clusters/vpsadmin/bin/devcluster stop 2026-06-06-vpsadmin-user-timezone`
  - Stopped/killed the half-started VM run.
- `dev-clusters/vpsadmin/bin/devcluster reset 2026-06-06-vpsadmin-user-timezone`
  - Removed the partial devcluster VM/database state before the clean restart.
- `dev-clusters/vpsadmin/bin/devcluster start 2026-06-06-vpsadmin-user-timezone`
  - Passed after fixing the mount wiring and schema version. The wrapper
    reached ready state but its automatic node refresh initially missed
    `node1` SSH while the node network was still settling.
- `dev-clusters/vpsadmin/bin/devcluster refresh 2026-06-06-vpsadmin-user-timezone`
  - Passed after `node1` became reachable.
- `curl -k` checks against:
  - `https://webui.aitherdev.int.vpsfree.cz/`
  - `https://web-cs.aitherdev.int.vpsfree.cz/`
  - `https://web-en.aitherdev.int.vpsfree.cz/`
  - `https://api.aitherdev.int.vpsfree.cz/`
  - All returned HTTP 200.

## Commits

- `vpsadmin`
  - `3ca9b305b users: add configurable time zones`
  - `7f68c7314 mail_templates: render times in user time zone`
- `web`
  - `b6a55b7 registration: collect applicant time zone`
- `vpsfree-mail-templates`
  - `7da522e templates: render timestamps in user time zone`
- Workspace `dev-clusters/vpsadmin`
  - `d9e993f devcluster: serve vpsFree web`
  - `d5a0154 devcluster: mount shared sources in services VM`
- `vpsfree-cz-configuration`
  - `4159e6cd cluster: move aitherdev web to devcluster`
- Follow-up after devcluster startup:
  - `vpsadmin`
    - schema version fix squashed into
      `3ca9b305b users: add configurable time zones`
- Follow-up webui sidebar tip:
  - `vpsadmin`
    - `95067364c webui: add per-user settings store`
    - `b699749b0 webui: suggest browser time zone in sidebar`
- Follow-up flake input update:
  - `vpsadmin`
    - `913cc7709 flake: vpsadminos 0ac745ae3 -> a791e6b37`

## Results

- `vpsadmin` user setting path:
  - User model is `api/models/user.rb`.
  - API user resource is `api/lib/vpsadmin/api/resources/user.rb`.
  - Normal users can currently self-update a whitelist of profile/auth fields
    in `User::Update`; `time_zone` should be added there.
  - Profile form is `webui/pages/page_adminm.php`.
  - Account settings form action `edit_member` already updates language and
    mail preferences immediately for normal users.
  - Personal information form action `edit_personal` creates a change request
    for non-admin users; time zone should not be put there.

- Web UI date/time path:
  - `tolocaltz()` is in `webui/lib/functions.lib.php`.
  - It formats using `date_default_timezone_get()`.
  - No `date_default_timezone_set()` was found in webui, so the implementation
    should set PHP's default timezone for each authenticated request from the
    current user's `time_zone`.

- Mail template path:
  - Mail rendering is `MailTemplate.send_mail!` in
    `api/models/mail_template.rb`.
  - ERB rendering is `MailTemplateTranslation::TemplateBuilder` in
    `api/models/mail_template_translation.rb`.
  - Templates frequently use `.localtime.strftime(...)`, which uses server
    local time. Add builder helpers and migrate templates to those helpers.
  - Mails sent with `opts[:user]` can use that user's time zone. Mails without
    a user should keep existing server-local behavior unless a time zone is
    explicitly supplied.

- Registration path:
  - Registration requests are implemented by the `requests` plugin.
  - `RegistrationRequest` persists registration fields in the `user_requests`
    table.
  - `plugins/requests/api/resources/registration.rb` controls public
    create/preview/update API params.
  - `RegistrationRequest#approve` creates the real `User`; it should copy
    `time_zone`.
  - Website registration submits through `web/lib/register.php`.
  - Website dynamic form reload is in `web/js/form.js`; it already saves and
    restores input/select state across entity type changes.

- Validation and storage:
  - Recommended storage is a nullable string IANA identifier.
  - Validate with `TZInfo::Timezone.get` or equivalent.
  - PHP side can render options with `DateTimeZone::listIdentifiers()`.
  - API side can expose choices for the webui profile select.

- Hooks/tooling:
  - `vpsadmin` declares `.overcommit.yml` with Nixfmt, RuboCop and
    PhpCsFixer pre-commit hooks.
  - Hooks are installed in `repos/vpsadmin.git/hooks`.
  - Ambient shell lacks the `overcommit` gem. Use `nix develop` or otherwise
    provide the repo's hook tooling before committing.
  - `web` did not declare a hook framework in the checked files.

## Implementation Notes

- The database columns are nullable. `NULL` and blank strings mean "server
  default" and preserve current behavior for existing users.
- The API declares `time_zone` as nullable; JSON clients may omit it, send
  `null`, or send an empty string to clear the setting.
- The webui captures `VPSADMIN_SERVER_TIME_ZONE` before applying any per-user
  timezone, so the "Server default" label and fallback reset are stable within
  the request.
- Mail templates without an associated user still use server-local behavior
  unless a caller explicitly passes `time_zone:`.
- Public registration defaults from the browser only when the select has no
  restored user selection.

## Decisions

- Existing users:
  - Leave `users.time_zone` nullable and use current server-local behavior as
    fallback until the user configures a value.
- Registration UI shape:
  - Show a visible select populated from PHP `DateTimeZone` identifiers and
    auto-select the browser-detected value with JavaScript.

## Follow-up: public registration form 500

- Symptom:
  - `https://web-en.aitherdev.int.vpsfree.cz/registration/pravnicka-osoba/form.php`
    returned HTTP 500 and the browser displayed the generic form load error.
- Cause:
  - The devcluster live web root symlinked top-level directories from
    `/run/vpsfree-web-live` to `/mnt/web`.
  - PHP resolved the registration script path through the symlinked source
    tree, so `lib/init.php` looked for `vendor/autoload.php` and `config.php`
    under `/mnt/web`, not only under `/run/vpsfree-web-live`.
  - The initial devcluster web setup generated those files only in the live
    root.
- Fix:
  - Workspace commit `cc3e1e8 devcluster: expose web composer dependencies`.
  - The devcluster now builds the web Composer package from the matching web
    worktree and exposes Composer vendor entries under `/mnt/web/vendor`.
  - `/mnt/web/vendor` remains a directory, preserving the tracked
    `vendor/.keep`; Composer entries inside it are ignored symlinks.
  - `/mnt/web/config.php` is pointed at the generated devcluster config when
    absent or already a symlink.
- Commands/results:
  - `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt dev-clusters/vpsadmin/nix/test.nix`
  - `git diff --check -- dev-clusters/vpsadmin/nix/test.nix`
  - `dev-clusters/vpsadmin/bin/devcluster update 2026-06-06-vpsadmin-user-timezone services`
  - `curl -k` checks returned HTTP 200 for:
    - `https://web-en.aitherdev.int.vpsfree.cz/registration/pravnicka-osoba/form.php`
    - `https://web-en.aitherdev.int.vpsfree.cz/registration/fyzicka-osoba/form.php`
    - `https://web-cs.aitherdev.int.vpsfree.cz/prihlaska/pravnicka-osoba/form.php`
    - `https://web-cs.aitherdev.int.vpsfree.cz/prihlaska/fyzicka-osoba/form.php`
  - `systemctl --failed` on the services VM reported zero failed units.

## Follow-up: webui time-zone sidebar tip and generic settings

- Request:
  - Replace the originally discussed pop-up with a less intrusive sidebar tip.
  - Back the "do not show again" state with a generic webui per-user key-value
    store that has server-side protections against unbounded keys/data.
- Implemented in `vpsadmin` worktree:
  - Added `plugins/webui/api/db/migrate/20260607190000_add_webui_user_settings.rb`.
  - Added `WebuiUserSetting` model with:
    - current-user-owned settings;
    - allowed namespaces: `forms`, `tips`, `ui`;
    - key format validation;
    - 64 keys per user;
    - 8 KiB per serialized JSON value;
    - 64 KiB total serialized JSON value data per user.
  - Added `VpsAdmin::API::Resources::WebuiUserSetting`:
    - `GET /webui_user_settings`;
    - `GET /webui_user_settings/{namespace}/{key}`;
    - `PUT /webui_user_settings/{namespace}/{key}`;
    - `DELETE /webui_user_settings/{namespace}/{key}`.
  - Left the `webui` plugin version unchanged; vpsAdmin is versioned as one
    project.
  - Added API specs in
    `api/spec/api/plugins/webui/webui_user_setting_spec.rb`.
  - Added `webui/lib/tips.lib.php` to render webui sidebar tips.
  - Added `webui/public/js/tips.js` to reveal the time-zone tip only when:
    - the account time zone is unset;
    - the browser reports a valid IANA time zone;
    - the browser time zone differs from `VPSADMIN_SERVER_TIME_ZONE`;
    - the tip has not already been remembered.
  - The time-zone tip can update the current user's `time_zone` using the
    existing user self-update API or dismiss while keeping server default.
  - Added sidebar tip styling to `webui/public/template/css/main.css`.
  - Exposed current user id/time zone and server default time zone in
    `webui/public/config.js.php`.
  - Added isolated Playwright fixture users for the tip flows and covered them
    in `users-self-service.spec.cjs`.
  - Added `webui/lib/tips.lib.php` to `tests/ci-selection.yml`.
- Commands/results:
  - `ruby -c` on the new Ruby model/resource/migration/spec files
    - Passed.
  - `php -l webui/lib/tips.lib.php webui/public/config.js.php webui/public/index.php`
    - Passed.
  - `nix shell nixpkgs#nodejs -c node --check webui/public/js/tips.js`
    - Passed.
  - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/specs/users-self-service.spec.cjs`
    - Passed.
  - `nix-instantiate --parse tests/suite/webui.nix`
    - Passed.
  - `ruby tests/ci-selection-test.rb`
    - Passed: 15 runs, 54 assertions, 0 failures.
  - `nix develop .#api -c bash -lc 'bundle exec rubocop ../plugins/webui/api/db/migrate/20260607190000_add_webui_user_settings.rb ../plugins/webui/api/models/webui_user_setting.rb ../plugins/webui/api/resources/webui_user_setting.rb spec/api/plugins/webui/webui_user_setting_spec.rb'`
    - Passed: 4 files inspected, no offenses.
  - `nix develop .#api -c bash -lc 'VPSADMIN_PLUGINS=webui bundle exec rspec spec/api/plugins/webui/webui_user_setting_spec.rb'`
    - Passed: 15 examples, 0 failures.
  - `./test-runner.sh test 'webui#users-self-service'`
    - Passed: 1 test successful; script `webui#users-self-service`
      succeeded in 708.4 seconds; total test run 1015.21 seconds.
- Notes:
  - An attempted parallel `nix develop` validation run collided while
    installing gems into the local `.gems` directory. Sequential reruns with
    `nix develop .#api` passed.
  - Ambient `node` was not available; JS syntax checks were run through
    `nix shell nixpkgs#nodejs`.

## Follow-up: vpsadminos flake input

- Request:
  - Update the `vpsadminos` flake input in the `vpsadmin` worktree.
- Commands/results:
  - `nix develop -c tools/update_vpsadminos_flake.sh`
    - Passed.
    - Updated `flake.lock` only.
    - Updated `vpsadminos` from
      `0ac745ae324072ec079620445ed4ea3531a7db96` to
      `a791e6b372bb0fb6c9ffd65383517c140f510f8b`.
    - Also updated nested `vpsadminos/nixpkgs` and
      `vpsadminos/nixpkgsUnstable` lock entries as part of the flake input.
    - Created commit
      `913cc7709 flake: vpsadminos 0ac745ae3 -> a791e6b37`.
  - `nix flake metadata --json . | jq -r '.locks.nodes.vpsadminos.locked.rev'`
    - Confirmed `a791e6b372bb0fb6c9ffd65383517c140f510f8b`.
  - `git status --short` in `vpsadmin`
    - Clean.

## Follow-up: commit stack cleanup

- Request:
  - Squash the schema-version fix into the original user timezone commit.
- Commands/results:
  - Created local backup branch
    `backup/2026-06-06-vpsadmin-user-timezone-before-schema-squash` at the
    pre-rewrite head.
  - Rebuilt the branch from `origin/master` by replaying commits
    non-interactively with `git commit -F <tmpfile>`.
  - Squashed `c23d755 users: update schema version for time zone migration`
    into `users: add configurable time zones`.
  - Removed the temporary rebuild branch after moving
    `2026-06-06-vpsadmin-user-timezone` to the rebuilt history.
  - `git diff --exit-code backup/2026-06-06-vpsadmin-user-timezone-before-schema-squash HEAD --stat`
    - Passed; final tree unchanged from the pre-rewrite branch.
  - `git diff origin/master..HEAD --check`
    - Passed.
  - Final vpsAdmin commit stack:
    - `3ca9b305b users: add configurable time zones`
    - `7f68c7314 mail_templates: render times in user time zone`
    - `95067364c webui: add per-user settings store`
    - `b699749b0 webui: suggest browser time zone in sidebar`
    - `913cc7709 flake: vpsadminos 0ac745ae3 -> a791e6b37`
  - `git status --short` in `vpsadmin`
    - Clean.

## Follow-up: push vpsadmin and watch CI

- Request:
  - Push the `vpsadmin` branch to GitHub and watch workflows, resolving
    possible issues.
- Commands/results:
  - `nix develop -c git push --set-upstream origin 2026-06-06-vpsadmin-user-timezone`
    - Pushed the initial cleaned branch to GitHub.
  - First GitHub Actions pass for head `913cc7709`:
    - RuboCop passed.
    - libnodectld Specs passed.
    - Client Specs passed.
    - Webui PHPUnit passed.
    - API Specs failed in the full endpoint coverage job.
  - Failure:
    - `spec/api/endpoint_coverage_spec.rb` reported missing scopes:
      - `webui_user_setting#delete`;
      - `webui_user_setting#index`;
      - `webui_user_setting#set`;
      - `webui_user_setting#show`.
  - Fix:
    - Added those scopes to `api/spec/api/covered_endpoints.yml`.
    - Committed the change as a temporary `fixup! webui: add per-user settings store`
      commit with Overcommit hooks active through `nix develop`.
    - Autosquashed the fixup into `webui: add per-user settings store`.
  - Local validation after the fix:
    - `nix develop .#api -c bash -lc 'VPSADMIN_PLUGINS=all bundle exec rspec spec/api/endpoint_coverage_spec.rb'`
      - Passed: 1 example, 0 failures.
  - Force-pushed the rewritten branch with lease:
    - `913cc7709...5eb5686ed`.
  - Current vpsAdmin commit stack:
    - `3ca9b305b users: add configurable time zones`
    - `7f68c7314 mail_templates: render times in user time zone`
    - `f985549d6 webui: add per-user settings store`
    - `e1eb25c1b webui: suggest browser time zone in sidebar`
    - `5eb5686ed flake: vpsadminos 0ac745ae3 -> a791e6b37`
  - GitHub Actions for head `5eb5686ed`:
    - Running at the time of this note.

## Follow-up: webui session time zone source

- Request:
  - Do not call `api->user->current()` on every webui page load to refresh the
    time zone.
  - Store the user's `time_zone` in the PHP session and use that as the runtime
    source of truth.
  - When the sidebar tip changes the time zone through webui, update the PHP
    session immediately. Changes through other means may require logging out
    and in again.
- Implementation:
  - Changed `webui/public/index.php` to call `set_request_time_zone()` from
    `$_SESSION['user']['time_zone']` only.
  - Added `webui/public/session-time-zone.php`, a same-origin POST endpoint
    protected by the existing CSRF helpers, to update the session time zone.
  - Added a `session_time_zone` CSRF token to `webui/public/config.js.php`.
  - Updated `webui/public/js/tips.js` so the "use browser time zone" action:
    1. updates the user through the API;
    2. updates the PHP session through `session-time-zone.php`;
    3. remembers the tip and reloads the page.
  - Added the endpoint to the webui nginx PHP entrypoint allowlist in
    `nixos/modules/vpsadmin/webui.nix`.
  - Added the endpoint to CI selection and extended the Playwright self-service
    test to verify `window.vpsAdmin.user.timeZone` after the tip reload.
- Validation:
  - First focused run failed because nginx returned 404 for
    `/session-time-zone.php`; fixed by adding the explicit FPM route.
  - `php -l webui/public/session-time-zone.php`
  - `php -l webui/public/config.js.php`
  - `php -l webui/public/index.php`
  - `php -l webui/lib/tips.lib.php`
  - `nix shell nixpkgs#nodejs -c node --check webui/public/js/tips.js`
  - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/specs/users-self-service.spec.cjs`
  - `ruby tests/ci-selection-test.rb`
  - `nix-instantiate --parse nixos/modules/vpsadmin/webui.nix >/dev/null`
  - `./test-runner.sh test 'webui#users-self-service'`
    - Passed: 1 test script successful in 708.89 seconds.
- Commit/push:
  - Committed the change as a temporary `fixup! webui: suggest browser time
    zone in sidebar` commit with Overcommit hooks active through `nix develop`.
  - Autosquashed the fixup into `webui: suggest browser time zone in sidebar`.
  - Force-pushed the rewritten branch with lease:
    - `5eb5686ed...fe9fbd38f`.
  - Current vpsAdmin commit stack:
    - `3ca9b305b users: add configurable time zones`
    - `7f68c7314 mail_templates: render times in user time zone`
    - `f985549d6 webui: add per-user settings store`
    - `0f27787d1 webui: suggest browser time zone in sidebar`
    - `fe9fbd38f flake: vpsadminos 0ac745ae3 -> a791e6b37`
- GitHub Actions for head `fe9fbd38f`:
  - Canceled old replaced CI run `27127735782`; GitHub reports it as
    completed/canceled.
  - `27142922496` Webui PHPUnit: completed/success.
  - `27142922948` Client Specs: completed/success.
  - `27142922425` libnodectld Specs: completed/success.
  - `27142922559` CI: still in progress at last check.
    - The push diff touched `nixos/modules/vpsadmin/webui.nix`, which matches
      the current full-CI selection rule `nixos/**`.
    - Local reproduction of the selector for `5eb5686ed..fe9fbd38f` selected
      `mode=full`, `filter=tag=ci`.
    - `./test-runner.sh ls --filter tag=ci` listed 131 scripts, so the long
      runtime is expected for the selected workflow.
  - Follow-up check on 2026-06-09:
    - `27142922559` CI completed with conclusion `failure`.
    - The `Run tests` step timed out after 480 minutes.
    - Logs show no unexpected test failure marker before timeout; the runner was
      still executing the full `tag=ci` suite.
    - In GitHub's run, selector output was `mode=full`, `filter=tag=ci`,
      `reason=full rule matched api/db/migrate/20260606223000_add_users_time_zone.rb`.
      This happened after the force-push because the old pushed base was no
      longer available to the runner, so selection fell back to the branch diff
      from master.
    - Artifact uploaded: `vpsadmin-test-logs-27142922559`, artifact ID
      `7493531467`.
  - Follow-up local workflow change on 2026-06-09:
    - Increased `.github/workflows/ci.yml` `Run tests` step timeout from
      480 minutes to 720 minutes.
    - Increased the outer CI job timeout from 540 minutes to 780 minutes so it
      remains longer than the step timeout and leaves time for result
      evaluation and artifact upload.
    - Validated with
      `ruby -e 'require "yaml"; YAML.load_file(".github/workflows/ci.yml"); puts "ok"'`.
    - Local commit: `e267eabed ci: extend integration test timeout`.
    - Branch is one commit ahead of origin; not pushed.
  - Rebased initiative branches on default branches on 2026-06-09:
    - Fetched `origin` with pruning in `vpsadmin`, `web`,
      `vpsfree-mail-templates`, and `vpsfree-cz-configuration`.
    - Created local backup branches named
      `backup/2026-06-09-default-rebase` before replaying each branch.
    - `vpsadmin` rebased onto `origin/master` at `c8fbfe38f913`.
      The old `flake: vpsadminos 0ac745ae3 -> a791e6b37` branch commit was
      skipped because `origin/master` already updates `vpsadminos` further to
      `715b58e95`. The timeout commit was recreated as
      `b9b3dcc8ec8c ci: extend integration test timeout`; not pushed.
    - `web` was already up to date with `origin/master` at `ea0f19ce13b0`;
      head remains `b6a55b769e75 registration: collect applicant time zone`.
    - `vpsfree-mail-templates` was already up to date with `origin/master` at
      `22e739328a47`; head remains
      `7da522e060fc templates: render timestamps in user time zone`.
    - `vpsfree-cz-configuration` rebased onto `origin/master` at
      `64ec34367b60`; head is
      `2c33acf5d126 cluster: move aitherdev web to devcluster`. Removed
      generated untracked `.bin/` and `.bundle/` hook artifacts afterward.
    - Final worktree statuses were clean. `vpsadmin` and
      `vpsfree-cz-configuration` now diverge from their pushed feature branches
      because the local histories were rebased; no push was performed.
  - Merged and pushed default branches on 2026-06-10:
    - Used temporary merge worktrees under
      `worktrees/2026-06-06-vpsadmin-user-timezone/_merge/`.
    - Pushed `web` master to
      `b6a55b769e75 registration: collect applicant time zone`.
    - Updated `vpsfree-cz-configuration` `vpsfree-web` channel with
      `confctl inputs channel set --commit vpsfree-web vpsfreeWeb b6a55b769e75d2bf73aa6ea6d7bb6bf83cfcfd75`.
      Generated commit:
      `d5ab0df0 inputs: set vpsfreeWeb to b6a55b76`.
    - Pushed `vpsfree-mail-templates` master to
      `7da522e060fc templates: render timestamps in user time zone`.
    - Pushed `vpsadmin` master to `b5f9f0facb57`.
    - Pushed `vpsfree-cz-configuration` master to `d5ab0df0c386`.
    - Validation before pushes:
      - Web PHP syntax checks for changed files and
        `nix shell nixpkgs#nodejs -c node --check js/form.js`.
      - vpsAdmin
        `ruby -e 'require "yaml"; YAML.load_file(".github/workflows/ci.yml")'`
        and `ruby tests/ci-selection-test.rb`.
      - vpsfree-mail-templates ERB compilation across all templates.
      - `confctl build cz.vpsfree/containers/int.web`, built generation
        `2026-06-10--09-52-44`.
    - GitHub Actions for vpsAdmin master `b5f9f0facb57`:
      - RuboCop: success.
      - Webui PHPUnit: success.
      - API Specs (topic parallel): success.
      - libnodectld Specs: success.
      - CI: still in progress at last check.
  - Follow-up deploy pin on 2026-06-10:
    - Updated the `vpsadmin` channel in `vpsfree-cz-configuration` using
      `confctl inputs channel update --commit vpsadmin vpsadmin`.
    - Generated commit:
      `a78b816f inputs: update vpsadminServices to b5f9f0fa`.
    - Pushed `vpsfree-cz-configuration` master to `a78b816f162f`.
    - Verified with `confctl inputs channel ls vpsadmin`:
      `vpsadminServices` now resolves to `b5f9f0fa`.
    - Updated the `production` and `staging` channels in one command using
      `confctl inputs channel update --commit production,staging vpsadmin`.
    - Generated commit:
      `626d343a inputs: update vpsadminProduction, vpsadminStaging to b5f9f0fa`.
    - Pushed `vpsfree-cz-configuration` master to `626d343a6b13`.
    - Verified with
      `confctl inputs channel ls '{production,staging,vpsadmin}'`:
      `vpsadminProduction`, `vpsadminStaging`, and `vpsadminServices` all
      resolve to `b5f9f0fa`.
  - Local follow-up for equivalent time-zone names on 2026-06-10:
    - Implemented three-sample offset equivalence for the webui sidebar time
      zone tip. The webui now hides the tip when the browser time zone matches
      the server default offset at `now - 120 days`, `now`, and
      `now + 120 days`.
    - Added `serverEquivalentTimeZones` to the tip settings and updated
      `webui/public/js/tips.js` to use it before showing the tip.
    - Added PHPUnit coverage for Prague/Amsterdam equivalence and invalid
      zones.
    - Added Playwright coverage using `Africa/Abidjan` as a distinct
      UTC-equivalent browser zone in the current UTC test environment.
    - Local vpsAdmin commit, not pushed:
      `f2d992cf9 webui: hide time zone tip for equivalent zones`.
    - Validation:
      - `php -l webui/lib/functions.lib.php`
      - `php -l webui/lib/tips.lib.php`
      - `php -l webui/tests/Regression/TimeZoneEquivalenceTest.php`
      - `nix shell nixpkgs#nodejs -c node --check webui/public/js/tips.js`
      - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/specs/users-self-service.spec.cjs`
      - `nix develop .#webui --command bash -lc 'composer install && composer test'`
        - Passed with exit code 0: 23 tests, 115 assertions, 2 warnings.
      - `nix develop .#webui --command bash -lc 'vendor/bin/phpunit tests/Regression/TimeZoneEquivalenceTest.php'`
        - Passed: 3 tests, 6 assertions.
      - `./test-runner.sh test 'webui#users-self-service'`
        - Passed: 1 test successful in 732.02 seconds.
    - No push was performed. `vpsfree-cz-configuration` still points vpsAdmin
      channels at pushed revision `b5f9f0fa`; update them only after this
      local vpsAdmin commit is reviewed and pushed.
  - Merged and pushed equivalent-zone follow-up on 2026-06-10:
    - Fast-forwarded the vpsAdmin merge worktree and pushed master to
      `f2d992cf9a85 webui: hide time zone tip for equivalent zones`.
    - Fast-forwarded the `vpsfree-cz-configuration` merge worktree to current
      `origin/master` at
      `9ca9eb9a inputs: update vpsadminosOsStaging, vpsadminosStaging to 715b58e9`.
    - Updated vpsAdmin pins in one command:
      `confctl inputs channel update --commit 'vpsadmin,production,staging' vpsadmin`.
    - Generated commit:
      `070c32c0 inputs: update vpsadminProduction, vpsadminServices, vpsadminStaging to f2d992cf`.
    - Pushed `vpsfree-cz-configuration` master to `070c32c02174`.
    - Verified with
      `confctl inputs channel ls '{vpsadmin,production,staging}'`:
      `vpsadminServices`, `vpsadminProduction`, and `vpsadminStaging` all
      resolve to `f2d992cf`.
    - GitHub Actions for vpsAdmin master `f2d992cf9a85`:
      - Webui PHPUnit: success.
      - CI: in progress at last check.
- Devcluster:
  - `dev-clusters/vpsadmin/bin/devcluster update 2026-06-06-vpsadmin-user-timezone services`
    - Completed successfully after switching the services VM to the new system.
    - Restarted webui/API services and refreshed node1 pool runtime.
  - `curl -ksS https://webui.aitherdev.int.vpsfree.cz/session-time-zone.php`
    - Returned HTTP `405` with `{"message":"Method not allowed"}`, confirming
      that the live devcluster nginx routes the new PHP endpoint.
  - `dev-clusters/vpsadmin/bin/devcluster status 2026-06-06-vpsadmin-user-timezone`
    - `status: running`, `ready: yes`.

## Cleanup

- Cleanup performed on 2026-06-10:
  - All initiative and merge worktrees were checked for uncommitted changes
    before removal.
  - No branch refs were deleted.
  - Feature branches are intentionally kept after merge.
  - Removed the initiative and merge worktrees under
    `worktrees/2026-06-06-vpsadmin-user-timezone/`.
  - Stopped the dev cluster `2026-06-06-vpsadmin-user-timezone`; status is
    `stopped`.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
