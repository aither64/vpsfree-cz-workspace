---
lifecycle: active
---
# 2026-07-08-webui-server-errors

## Repositories

- `vpsfree-cz-configuration`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-08-webui-server-errors/vpsfree-cz-configuration`
  - Branch: `2026-07-08-webui-server-errors`
  - Base: `origin/master` at `39cbe315 inputs: update vpsadminServices to ff74228b`
- `vpsadmin`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-08-webui-server-errors/vpsadmin`
  - Branch: `2026-07-08-webui-server-errors`
  - Base: `origin/master` at `ff74228b4 webui: format load and traffic numbers`
- `syslog-exporter`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-08-webui-server-errors/syslog-exporter`
  - Branch: `2026-07-08-webui-server-errors`
  - Base: `origin/master` at `69b0269 Version 0.13.2`
- `ssh-exporter`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-08-webui-server-errors/ssh-exporter`
  - Branch: `2026-07-08-webui-server-errors`
  - Base: `origin/master` at `e47d586 Version 0.3.1`

## Status

- 2026-07-09: User requested follow-up cleanup of PHP warnings/notices from
  `/home/aither/workspace/ai/vpsfree.cz/webui1-nginx-journal.txt`.
- 2026-07-09: Recreated the `vpsadmin` worktree at
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-08-webui-server-errors/vpsadmin`.
  The existing local branch `2026-07-08-webui-server-errors` had no unique
  commits and was fast-forwarded to `origin/master` at
  `9c1dd3e79 webui: update dependencies` before checkout.
- 2026-07-09: Read repository-local `vpsadmin/AGENTS.md` before WebUI edits.
- 2026-07-09: Updated `plan.md` with the WebUI warning cleanup scope,
  compatibility notes, and testing plan.
- 2026-07-09: Implemented the WebUI warning cleanup in `vpsadmin`:
  optional request values now use existing helper/default handling, missing
  `AJAX_SCRIPT` template fragments default to an empty string before appending,
  `Lang::detect()` tolerates an unset `$_SESSION`, `api_param_choices()`
  tolerates missing metadata, `colorize()` reindexes sparse input arrays, and
  the mount-on-start-fail label callback falls back to API-provided labels.
- 2026-07-09: Added focused WebUI regression coverage for missing choice
  metadata, sparse color arrays, API-provided mount labels, and language
  detection with no session superglobal.
- 2026-07-09: Before the 2026-07-10 rebase, Overcommit's repository-wide
  `PhpCsFixer` hook also reformatted four pre-existing non-compliant files
  outside the warning cleanup:
  `webui/forms/userdata.forms.php`,
  `webui/tests/Regression/CsrfContextSwitchTest.php`,
  `webui/tests/Regression/CsrfStateFormsTest.php`, and
  `webui/tests/Regression/WebauthnRegistrationCredentialsTest.php`.
  These hook-required formatting edits were kept in commit `d4bedab1b` so the
  mandatory hook suite passed without bypassing hooks. The 2026-07-10 rebase
  dropped them from the feature commit because current `origin/master` already
  contains those formatting fixes.
- 2026-07-09: Committed the WebUI cleanup in `vpsadmin`:
  `d4bedab1b43abac30ba296c8d1d2fda5264bc629`
  (`webui: avoid warnings for missing request values`).
- 2026-07-09: Ran mandatory change review for the WebUI warning cleanup with
  standalone reviewer `019f4785-c736-74d1-9a75-2ae8e963ad5e`. Reviewer found
  no blocking, important, or advisory issues. Residual risks noted by reviewer:
  no browser/Playwright flow was run, and direct `$_GET`/`$_POST` reads remain
  elsewhere outside the observed warning sample.
- 2026-07-09: Pushed `vpsadmin` branch
  `2026-07-08-webui-server-errors` to origin.
- 2026-07-10: Rebased the `vpsadmin` branch on current `origin/master` at
  `b7b47ecfaf102b2e0370eb450a9ead5d4a3a42ce`
  (`deps: update HaveAPI to 0.29.3`). The rebased WebUI cleanup commit is
  `a92b6669946b4261c014fbe8acc6f9d40368c289`. Pushed with
  `--force-with-lease`; no superseded queued or in-progress old-head workflow
  runs were present to cancel.
- 2026-07-10: Fast-forward merged `vpsadmin` feature commit
  `a92b6669946b4261c014fbe8acc6f9d40368c289` to `origin/master` using
  temporary worktree `vpsadmin-merge-master-20260710`.
- 2026-07-10: Updated the `vpsadmin` channel in
  `vpsfree-cz-configuration` with
  `confctl inputs channel update --commit vpsadmin` and pushed master commit
  `1c85e9b62bd855db1ab5e057bd98c4dd1d360815`
  (`inputs: update vpsadminServices to a92b6669`).
- 2026-07-08: Verified active session slug
  `2026-07-08-webui-server-errors` with matching
  `VPSFREE_DEV_SESSION_SLUG`.
- 2026-07-08: Prepared worktrees for `vpsfree-cz-configuration`,
  `vpsadmin`, and `syslog-exporter`.
- 2026-07-08: Read repository-local `AGENTS.md` in `vpsadmin` and
  `vpsfree-cz-configuration`. `syslog-exporter` has no local `AGENTS.md`.
- 2026-07-08: Investigated current WebUI logging, central syslog forwarding,
  syslog-exporter metrics, and existing Prometheus rules.
- 2026-07-08: Wrote solution options and compatibility notes in `plan.md`.
- 2026-07-09: User selected solution 1: parse existing nginx journal/syslog
  messages in `syslog-exporter`.
- 2026-07-09: Analyzed uploaded sample
  `/home/aither/workspace/ai/vpsfree.cz/webui1-nginx-journal.txt` and revised
  `plan.md` for fatal-only matching.
- 2026-07-09: User requested a prerequisite phase before WebUI fatal-error
  monitoring: add RSpec support, baseline coverage, and GitHub Actions RSpec
  workflows to both `syslog-exporter` and `ssh-exporter`, then commit those
  generic test-support changes first.
- 2026-07-09: Prepared `ssh-exporter` worktree and revised `plan.md` with
  suggested specs for both exporters.
- 2026-07-09: Added and committed generic RSpec support, baseline specs, and
  RSpec GitHub Actions workflows in both exporter repositories:
  - `syslog-exporter` commit
    `3f13f889ed2b186cb653600a776f7b0643defdc2`
    (`Add RSpec coverage and CI`);
  - `ssh-exporter` commit
    `b7577a544e52d967f064309cb2198c2784d5c6fd`
    (`Add RSpec coverage and CI`).
- 2026-07-09: Ran mandatory change review for the prerequisite commits. The
  reviewer reported no blocking or important findings. Advisory follow-up:
  the `syslog-exporter` commit also contains two behavior-equivalent
  RuboCop-required cleanups in `parser.rb` and `processor.rb`; the commit was
  left unchanged and the rationale is recorded here. The advisory to update
  this state file is resolved by this entry.
- 2026-07-09: Implemented WebUI fatal-error monitoring:
  - `syslog-exporter` commit
    `f3f7a7aeb31f2ee8c850ebe5f8cda42c3587f052`
    (`collectors: monitor vpsAdmin WebUI fatal errors`);
  - `vpsfree-cz-configuration` commit
    `0d6b4e36487f4a6a21c1174ec323041f2e1113c6`
    (`syslog-exporter: monitor vpsAdmin WebUI fatal errors`).
- 2026-07-09: Pushed `syslog-exporter` branch
  `2026-07-08-webui-server-errors` so the configuration package can fetch the
  pinned exporter commit. Also pushed `ssh-exporter` branch to run its new RSpec
  workflow.
- 2026-07-09: Pushed `vpsfree-cz-configuration` branch
  `2026-07-08-webui-server-errors`. The first push attempt from the ambient
  shell failed because git hooks could not load their Ruby gems; retrying inside
  `nix develop` succeeded.
- 2026-07-09: Revised the WebUI collector after review discussion: removed
  hardcoded production FQDNs from `syslog-exporter`, added optional per-host
  `collectors` configuration, and opted only production `webui1`/`webui2` into
  `vpsadmin_webui` from `vpsfree-cz-configuration`.
- 2026-07-09: Ran mandatory change review for the functional monitoring
  commits. The reviewer reported no blocking or important findings. Advisory
  follow-up was to record the review result in this state file, resolved by
  this entry. Reviewer noted one residual deployment observation: first
  deployment should confirm the metric appears from a real WebUI fatal line,
  because the specs bypass end-to-end rsyslog pipe processing.
- 2026-07-09: Ran mandatory change review again after the collector opt-in
  amendment. Reviewer reported no blocking, important, or advisory findings.
- 2026-07-09: Merged and pushed default branches:
  - `ssh-exporter` `master` fast-forwarded to
    `b7577a544e52d967f064309cb2198c2784d5c6fd`;
  - `syslog-exporter` `master` fast-forwarded to
    `f3f7a7aeb31f2ee8c850ebe5f8cda42c3587f052`;
  - `vpsfree-cz-configuration` `master` fast-forwarded to
    `0d6b4e36487f4a6a21c1174ec323041f2e1113c6`.

## Commands run

- `git --git-dir=repos/vpsadmin.git fetch origin --prune`
- `git --git-dir=repos/vpsadmin.git update-ref
  refs/heads/2026-07-08-webui-server-errors refs/remotes/origin/master`
- `bin/dev-session worktree add 2026-07-08-webui-server-errors vpsadmin
  --as-is`
- `perl -ne 'while (/PHP message: PHP .../) ...'
  webui1-nginx-journal.txt`
- Various `rg`/`sed`/`nl` inspections in the `vpsadmin` worktree.
- `vpsadmin`: `nix develop .#webui -c composer install
  --working-dir=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-08-webui-server-errors/vpsadmin/webui`
- `vpsadmin`: `git diff --name-only -- '*.php' | xargs -r -n1 php -l`
- `vpsadmin`: `nix develop .#webui -c bash -lc 'cd .../webui &&
  vendor/bin/phpunit tests/Regression/ApiParamChoicesTest.php
  tests/Regression/DatasetScriptLocalizationTest.php
  tests/Regression/LanguageSelectionTest.php'`
- `vpsadmin`: `nix develop .#webui -c bash -lc 'cd .../webui &&
  composer test'`
- `vpsadmin`: `nix develop -c bash -lc 'cd ... && php-cs-fixer fix
  --dry-run --diff --config=.php-cs-fixer.dist.php
  --path-mode=intersection $(git diff --name-only -- "*.php")'`
- `vpsadmin`: `nix develop -c bash -lc 'cd ... && overcommit --install'`
- `vpsadmin`: `nix develop -c bash -lc 'cd .../api &&
  env -u BUNDLE_BIN_PATH -u BUNDLE_GEMFILE -u BUNDLER_VERSION
  BUNDLE_GEMFILE=Gemfile BUNDLE_PATH=.gems bundle install'`
- `vpsadmin`: `nix develop -c bash -lc 'cd ... && overcommit --run'`
- `vpsadmin`: `git diff --check`
- Mandatory change review by standalone agent
  `019f4785-c736-74d1-9a75-2ae8e963ad5e`.
- `vpsadmin`: `git push -u origin 2026-07-08-webui-server-errors`
- `vpsadmin`: `gh run list --branch 2026-07-08-webui-server-errors ...`
- `vpsadmin`: `gh run watch 29030495183 --interval 15 --exit-status`
- `vpsadmin`: `gh run watch 29030495201 --interval 15 --exit-status`
  (stopped local watcher after more than one hour because the CI workflow has
  a 720-minute test-step timeout and no live logs are available before
  completion)
- `vpsadmin`: `gh run view 29030495201 --json status,conclusion,jobs,url,createdAt,updatedAt`
- `bin/dev-session current`
- `printenv VPSFREE_DEV_SESSION_SLUG`
- `bin/dev-session worktree add 2026-07-08-webui-server-errors vpsfree-cz-configuration --as-is`
- `bin/dev-session worktree add 2026-07-08-webui-server-errors vpsadmin --as-is`
- `bin/dev-session worktree add 2026-07-08-webui-server-errors syslog-exporter --as-is`
- `git --git-dir=repos/syslog-exporter.git update-ref refs/heads/master refs/remotes/origin/master`
- `git --git-dir=repos/syslog-exporter.git symbolic-ref HEAD refs/heads/master`
- `git --git-dir=repos/ssh-exporter.git update-ref refs/heads/master refs/remotes/origin/master`
- `git --git-dir=repos/ssh-exporter.git symbolic-ref HEAD refs/heads/master`
- `bin/dev-session worktree add 2026-07-08-webui-server-errors ssh-exporter --as-is`
- Various `rg`/`sed` inspections in the three worktrees.
- `wc -l webui1-nginx-journal.txt`
- `rg -n "PHP (Fatal error|Parse error|Recoverable fatal error)|Uncaught|Stack trace|thrown in|Allowed memory size|Maximum execution time|upstream prematurely closed|connect\\(\\) to unix|recv\\(\\) failed|readv\\(\\) failed|No such file or directory\\).*vpsadmin-webui.*\\.php" webui1-nginx-journal.txt`
- `rg -c "PHP Fatal error" webui1-nginx-journal.txt`
- `rg -c "PHP Warning" webui1-nginx-journal.txt`
- `syslog-exporter`: `nix-shell --run 'bundle exec rspec'`
- `syslog-exporter`: `nix-shell --run 'bundle exec rake'`
- `syslog-exporter`: `nix-shell --run 'overcommit --install && overcommit --run'`
- `syslog-exporter`: `git commit -F <tmpfile>`
- `ssh-exporter`: `nix-shell --run 'bundle exec rspec'`
- `ssh-exporter`: `nix-shell --run 'bundle exec rake'`
- `ssh-exporter`: `nix-shell --run 'overcommit --install && overcommit --run'`
- `ssh-exporter`: `git commit -F <tmpfile>`
- Mandatory change review by standalone agent
  `019f45fa-d725-7e03-8316-eb03bb04ff30`.
- `syslog-exporter`: `nix-shell --run 'bundle exec rspec'`
- `syslog-exporter`: `nix-shell --run 'bundle exec rake'`
- `syslog-exporter`: `nix-shell --run 'overcommit --run'`
- `syslog-exporter`: `nix-shell --run 'git commit -F <tmpfile>'`
- `syslog-exporter`: `git push -u origin 2026-07-08-webui-server-errors`
- `ssh-exporter`: `git push -u origin 2026-07-08-webui-server-errors`
- `vpsfree-cz-configuration/packages/syslog-exporter`:
  `nix-shell -p bundix --run 'bundix -l'`
- `vpsfree-cz-configuration/packages/syslog-exporter`:
  `nix-shell -p bundix --run 'bundle lock'`
- `vpsfree-cz-configuration/packages/syslog-exporter`:
  `nix-shell -p bundix --run 'bundix'`
- `vpsfree-cz-configuration`:
  `nix-shell -p nixfmt-rfc-style --run 'nixfmt packages/syslog-exporter/gemset.nix modules/clusterconf/monitor/rules/syslog.nix'`
- `vpsfree-cz-configuration`:
  `nix build --no-link --impure --expr 'let flake = builtins.getFlake (toString ./.); pkgs = import flake.inputs.nixpkgs { system = "x86_64-linux"; overlays = import ./overlays; }; in pkgs.syslog-exporter'`
- `vpsfree-cz-configuration`:
  `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.log`
- `vpsfree-cz-configuration`:
  `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.mon1`
- `vpsfree-cz-configuration`: `nix develop -c overcommit --run`
- `vpsfree-cz-configuration`: `nix develop -c git commit -F <tmpfile>`
- `syslog-exporter`: `gh run list --branch 2026-07-08-webui-server-errors ...`
- `ssh-exporter`: `gh run list --branch 2026-07-08-webui-server-errors ...`
- `vpsfree-cz-configuration`: `git push -u origin 2026-07-08-webui-server-errors`
- `vpsfree-cz-configuration`:
  `nix develop -c git push -u origin 2026-07-08-webui-server-errors`
- `syslog-exporter`: `gh run view 29005319750 --json ...`
- `ssh-exporter`: `gh run watch 29005903721 --interval 15 --exit-status`
- `ssh-exporter`: `gh run view 29005903721 --json ...`
- Mandatory change review by standalone agent
  `019f460e-7e83-7a82-83bd-283f07e4c87e`.
- `syslog-exporter`: `git commit --amend --no-edit`
- `syslog-exporter`: `git push --force-with-lease origin 2026-07-08-webui-server-errors`
- `vpsfree-cz-configuration/packages/syslog-exporter`:
  `nix-shell -p bundix --run 'bundle lock'`
- `vpsfree-cz-configuration/packages/syslog-exporter`:
  `nix-shell -p bundix --run 'bundix'`
- `vpsfree-cz-configuration`:
  `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.log`
- `vpsfree-cz-configuration`:
  `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.mon1`
- Mandatory change review by standalone agent
  `019f4641-43aa-7673-ab31-60569a0af387`.
- `vpsfree-cz-configuration`: `nix develop -c git rebase origin/master`
- `vpsfree-cz-configuration`: `nix develop -c overcommit --run`
- `vpsfree-cz-configuration`:
  `nix build --no-link --impure --expr 'let flake = builtins.getFlake (toString ./.); pkgs = import flake.inputs.nixpkgs { system = "x86_64-linux"; overlays = import ./overlays; }; in pkgs.syslog-exporter'`
- `vpsfree-cz-configuration`:
  `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.log`
- `vpsfree-cz-configuration`:
  `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.mon1`
- Merge worktrees:
  `git merge --ff-only origin/2026-07-08-webui-server-errors`
- Merge worktrees:
  `git push origin HEAD:master`
- `syslog-exporter`: `gh run watch 29009780220 --interval 15 --exit-status`
- `ssh-exporter`: `gh run watch 29009780285 --interval 15 --exit-status`

## Results

- Warning extraction from `webui1-nginx-journal.txt` found 830 nginx lines with
  PHP warning/notice/deprecated signatures. The largest clusters are optional
  missing request values:
  - `forms/outage.forms.php`: missing `type`, `state`, `impact`, and `order`
    in outage filters, plus affected VPS/export filter values;
  - `forms/monitoring.forms.php`: missing `monitor`, `object_name`,
    `object_id`, `state`, and `order`;
  - `forms/dataset.forms.php`, `forms/vps.forms.php`, and
    `forms/users.forms.php`: first-render form defaults;
  - `pages/page_console.php`, `forms/dataset.forms.php`, and
    `pages/page_networking.php`: missing `AJAX_SCRIPT` template variable before
    appending JavaScript;
  - `lib/functions.lib.php`: missing parameter metadata guard in
    `api_param_choices()` and short color palettes in `colorize()`;
  - lower-count page routing/default warnings in `page_outage.php`,
    `page_userns.php`, `page_adminvps.php`, `page_adminm.php`,
    `oom_reports.forms.php`, and `networking.forms.php`.
- `vpsadmin` verification passed:
  - syntax checks on all modified PHP files;
  - focused WebUI regression tests, 14 tests and 21 assertions;
  - full WebUI PHPUnit suite, 56 tests and 198 assertions;
  - PHP CS Fixer dry-run on modified PHP files;
  - Overcommit pre-commit hook suite after installing root and API bundles;
  - `git diff --check`.
- Mandatory change review for the WebUI cleanup passed with no findings.
- GitHub Actions on pushed `vpsadmin` branch:
  - `i18n health` run `29030495183` passed on
    `d4bedab1b43abac30ba296c8d1d2fda5264bc629`;
  - `Webui PHPUnit` run `29030495270` passed on
    `d4bedab1b43abac30ba296c8d1d2fda5264bc629`;
  - `CI` run `29030495201` was still in progress in the `Run tests` step after
    more than one hour. GitHub did not expose logs while the job was still
    running. The workflow has `timeout-minutes: 780` for the job and
    `timeout-minutes: 720` for the `Run tests` step.
- Final pre-handoff check on 2026-07-09 found the `vpsadmin` worktree clean and
  tracking `origin/2026-07-08-webui-server-errors`. `CI` run `29030495201`
  remained in progress in the same `Run tests` step.
- Follow-up CI check on 2026-07-10: the pre-rebase `vpsadmin` runs on
  `d4bedab1b43abac30ba296c8d1d2fda5264bc629` all completed successfully,
  including `CI` run `29030495201`, `Webui PHPUnit` run `29030495270`, and
  `i18n health` run `29030495183`.
- Post-rebase verification on
  `a92b6669946b4261c014fbe8acc6f9d40368c289` passed PHP syntax checks on
  modified PHP files, focused WebUI PHPUnit regression tests
  (14 tests, 21 assertions), and `git diff --check`.
- GitHub Actions on the post-rebase `vpsadmin` commit:
  - passed: `Console Router Specs` run `29078682603`;
  - passed: `Download Mounter Specs` run `29078682619`;
  - passed: `Webui PHPUnit` run `29078682590`;
  - passed: `RuboCop` run `29078682625`;
  - passed: `Client Specs` run `29078682567`;
  - passed: `i18n health` run `29078682586`;
  - still in progress as of the first post-rebase check: `API Specs (topic parallel)` run
    `29078682607` and `CI` run `29078682622`.
- Final post-rebase feature-branch check before merge: `API Specs (topic
  parallel)` run `29078682607` passed; feature-branch `CI` run `29078682622`
  was still in progress in the `Run tests` step when the user asked to merge.
- `vpsadmin` master push for
  `a92b6669946b4261c014fbe8acc6f9d40368c289` started GitHub Actions:
  `Webui PHPUnit` run `29092818933` passed, `i18n health` run `29092819015`
  passed, and `CI` run `29092818757` was still in progress at the last check.
- `vpsfree-cz-configuration` validation for commit
  `1c85e9b62bd855db1ab5e057bd98c4dd1d360815`:
  - `confctl` commit hooks passed (`Nixfmt` OK; commit-msg text-width warning
    only, allowed for generated confctl messages);
  - `confctl build -y cz.vpsfree/vpsadmin/int.webui1` passed, generation
    `2026-07-10--14-34-13`.
- `nix develop .#webui -c composer install --working-dir=webui` failed
  because the WebUI shell changes Composer's current directory to
  `/home/aither/.config/composer`; using an absolute `--working-dir` succeeded.
- The first `overcommit --run` failed in `VpsadminApiI18n` because the API
  bundle was not installed under `api/.gems`. Running `bundle install` in
  `api/` with the same environment used by the hook fixed it. A partially
  completed hook run was interrupted after PHP CS Fixer because the earlier
  failed run left the process waiting; the subsequent full hook run passed.
- `vpsfree-cz-configuration` worktree was created, but the helper command exited
  non-zero because an Overcommit hook tried to load gems that are not installed
  in the ambient shell. The worktree itself is present and clean.
- `syslog-exporter` worktree creation initially failed because the canonical
  bare clone had `HEAD` pointing at `refs/remotes/origin/master` with no local
  `refs/heads/master`. Added a local `master` ref from `origin/master` and set
  bare `HEAD` to `refs/heads/master`; the worktree was then created normally.
- Current configuration already forwards NixOS syslog to `int.log`
  (`modules/system/logging/nixos.nix`) and mirrors central syslog into
  `syslog-exporter` (`cluster/cz.vpsfree/containers/prg/int.log/config.nix`).
- Prometheus already scrapes syslog-exporter as job `log` every 60 seconds
  (`modules/clusterconf/monitor/default.nix`).
- `syslog-exporter` already exposes `syslog_message_count` labelled by
  `program`, `alias`, and `fqdn`, plus custom flare-style metrics for selected
  log events.
- vpsAdmin WebUI PHP-FPM is configured with `php_admin_value[error_log] =
  stderr`, `php_admin_flag[log_errors] = true`, and `catch_workers_output =
  true` in `nixos/modules/vpsadmin/webui.nix`.
- Production WebUI hosts are `webui1.int.vpsfree.cz` and
  `webui2.int.vpsfree.cz` in `vpsfree-cz-configuration`.
- Existing vpsAdmin monitoring covers service liveness and blackbox HTTP
  probes, but not intermittent server-side errors observed in logs.
- The uploaded nginx journal sample has 1539 lines. It confirms PHP errors are
  visible in `nginx.service` journal and not in the php-fpm service journal.
- The sample is dominated by non-alert-worthy nginx error-level logs:
  830 lines contain `PHP Warning`; there are also missing-file/probe entries.
- The sample contains 12 `PHP Fatal error` first lines. Examples include
  `Uncaught Error` and `Uncaught TypeError`, both reported through nginx
  `FastCGI sent in stderr`.
- A handled `HaveAPI\Client\Exception\ValidationError` produced a stack trace in
  nginx output without being a PHP fatal error. Matching `Stack trace` alone
  would false-positive.
- The selected collector should therefore match nginx `FastCGI sent in stderr`
  messages containing PHP fatal signatures and ignore warnings, handled
  validation traces, scanner/static-file errors, and stack-trace continuation
  lines.
- Before the prerequisite changes, `syslog-exporter` and `ssh-exporter` had no
  existing `.github/workflows/` directory and no RSpec setup.
- `ssh-exporter` has no local `AGENTS.md`.
- `ssh-exporter` had the same bare-clone `HEAD` issue as `syslog-exporter`;
  a local `master` ref was added from `origin/master` before creating the
  worktree.
- `syslog-exporter` now has RSpec/rake/CI support and baseline specs covering
  config loading, parser behavior, message counting, nodectld/osctld/lxc/kernel
  collectors, and ZFS flare reset behavior.
- `ssh-exporter` now has RSpec/rake/CI support and baseline specs covering
  config loading, required host fields, collector metric registration, SSH
  command construction, successful checks, and failed checks.
- Latest upstream GitHub Action versions were checked before adding workflows:
  `actions/checkout@v7` from the official `actions/checkout` releases and
  `ruby/setup-ruby@v1` from the official `ruby/setup-ruby` documentation.
- Verification passed:
  - `syslog-exporter`: `bundle exec rspec`, 12 examples, 0 failures;
  - `syslog-exporter`: `bundle exec rake`, 12 examples, 0 failures;
  - `syslog-exporter`: Overcommit/RuboCop passed before commit and through
    commit hooks;
  - `ssh-exporter`: `bundle exec rspec`, 7 examples, 0 failures;
  - `ssh-exporter`: `bundle exec rake`, 7 examples, 0 failures;
  - `ssh-exporter`: Overcommit/RuboCop passed before commit and through commit
    hooks.
- Reviewer-side verification also passed `bundle exec rspec` in both exporter
  worktrees and `git diff --check` for both diffs. Reviewer noted residual
  syslog coverage gaps for processor host/FQDN routing, LXC netns failure,
  flare renewal, and negative collector cases; these are acceptable for the
  prerequisite and should be targeted when adding the WebUI fatal-error
  collector.
- `syslog-exporter` now has `SyslogExporter::Collectors::VpsadminWebui`.
  It is enabled only for hosts whose config includes collector
  `vpsadmin_webui`, requires `program == "nginx"` and
  `FastCGI sent in stderr`, and matches only fixed PHP fatal signatures:
  `fatal`, `parse`, and `recoverable_fatal`.
- `syslog-exporter` host config has optional `collectors`, defaulting to an
  empty array for existing configs.
- The collector exposes
  `syslog_vpsadmin_webui_fatal_error_count{error_type,alias,fqdn}` and
  `syslog_vpsadmin_webui_fatal_error{error_type,alias,fqdn}`. `error_type` is
  a bounded label.
- WebUI collector specs cover a fatal line preceded by PHP warnings,
  parse/recoverable fatal classification, warning-only logs, stack-trace
  continuation lines, handled validation errors, other programs, and host
  scoping. `syslog-exporter` RSpec now has 17 examples.
- `vpsfree-cz-configuration` now pins `packages/syslog-exporter` to
  `f3f7a7aeb31f2ee8c850ebe5f8cda42c3587f052` from GitHub because the new
  `0.13.3` exporter version is not published as an internal gem yet.
- Generated `int.log` syslog-exporter JSON was checked: `webui1` and `webui2`
  have `collectors = [ "vpsadmin_webui" ]`, while `webui-dev` has
  `collectors = []`.
- `vpsfree-cz-configuration` now adds warning alert
  `VpsAdminWebuiFatalError` on `syslog_vpsadmin_webui_fatal_error == 1`.
  Repeated-error critical escalation was intentionally deferred until real
  post-deployment event volume is known.
- `nix-shell -p bundix --run 'bundix -l'` failed for the git-pinned exporter
  because Bundler tried to write its git cache under `/nix/store`. Workaround:
  run `bundle lock` first and then `bundix` without `-l`; this generated the
  same lock/gemset intent and was accepted by package build verification.
- Verification passed:
  - `syslog-exporter`: `bundle exec rspec`, 17 examples, 0 failures;
  - `syslog-exporter`: `bundle exec rake`, 16 examples, 0 failures before the
    final config-field spec amendment; the final RSpec check covered
    17 examples;
  - `syslog-exporter`: Overcommit/RuboCop passed before commit and through
    commit hooks;
  - `vpsfree-cz-configuration`: `nixfmt` passed on touched Nix files;
  - `vpsfree-cz-configuration`: `pkgs.syslog-exporter` Nix package built;
  - `vpsfree-cz-configuration`: `confctl build -y
    cz.vpsfree/containers/prg/int.log` passed after rebase, generation
    `2026-07-09--11-51-13`;
  - `vpsfree-cz-configuration`: `confctl build -y
    cz.vpsfree/containers/prg/int.mon1` passed after rebase, generation
    `2026-07-09--11-52-21`;
  - `vpsfree-cz-configuration`: Overcommit Nixfmt/RuboCop passed before commit
    and through commit hooks.
- Functional change review passed with no blocking or important findings.
  Reviewer confirmed the collector scope, bounded labels, warning-only alert,
  mixed-version empty-expression behavior, and pushed package pin. Residual
  risk: specs do not exercise an end-to-end rsyslog pipe path, so first
  deployment should confirm the metric appears from a real WebUI fatal line.
- Amended design review after removing hardcoded WebUI FQDNs passed with no
  blocking, important, or advisory findings.
- GitHub Actions:
  - `syslog-exporter` feature RSpec run `29008751371` on
    `f3f7a7aeb31f2ee8c850ebe5f8cda42c3587f052` passed;
  - `ssh-exporter` feature RSpec run `29005903721` on
    `b7577a544e52d967f064309cb2198c2784d5c6fd` passed after rerun;
  - `syslog-exporter` master RSpec run `29009780220` passed;
  - `ssh-exporter` master RSpec run `29009780285` passed;
  - `vpsfree-cz-configuration` has no push workflow run for this branch.

## Open questions

- None for the current implementation.
- Post-deployment follow-up: confirm the metric appears from a real WebUI fatal
  line and decide later whether repeated events should get a separate critical
  alert.

## Cleanup

- All initiative feature and merge worktrees under
  `worktrees/2026-07-08-webui-server-errors/` were removed after merge.
- After the 2026-07-10 follow-up merge and channel update, removed the
  recreated `vpsadmin` feature worktree, the temporary `vpsadmin` master merge
  worktree, and the temporary `vpsfree-cz-configuration` channel-update
  worktree.
- Final cleanup on 2026-07-10 pruned worktree metadata and removed the empty
  `worktrees/2026-07-08-webui-server-errors/` directory. The durable
  `plan.md` and `state.md` notes remain under `work/2026-07-08-webui-server-errors/`.
- Feature branches were kept locally/remotely as required by workspace policy.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
