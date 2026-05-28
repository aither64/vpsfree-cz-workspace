# Outage labels and wire rename state

## Branches and worktrees

Branch name: `2026-05-27-outage-labels`

| Repository | Worktree | Current head |
| --- | --- | --- |
| vpsadmin | removed after merge | `f960f0e5d6f869e302a09f57cc27c181e87d13a1` |
| vpsf-status | removed after merge | `5f6db13103bf652e69b7b879a69e98794075e64e` |
| vpsfree-irc-bot | removed after merge | `73ef144e761acd5b44b64d4d27ef292ea1b1322e` |
| vpsfree-mail-templates | removed after merge | `d35ad25dab5de3f94fa25f485debde11413f5cd9` |
| web | removed after merge | `ea0f19ce13b06194faada5b1fd4eeed3dc46c4b8` |
| vpsfree-cz-configuration | removed after merge | `e16d8ad3f51ff4e93aa9ee21a74d96b77dfea25d` |

## Upstream refresh

- Fetched affected repositories before the follow-up push.
- Rebased `vpsfree-irc-bot` on origin/master `e570f08`.
- Rebuilt `vpsfree-cz-configuration` from origin/master `aec8b183` after
  scheduled dependency updates and after the final vpsadmin fix.
- Rebased `vpsadmin` on origin/master `c1fc04738` and added a webui fix for
  mapped HaveAPI choices.
- Rebuilt `vpsfree-cz-configuration` again from origin/master `aec8b183` after
  the webui wording follow-up and mailing-list removal.

## Implementation

- `vpsadmin`
  - Renamed outage type API wire values from `maintenance`/`outage` to
    `planned_outage`/`unplanned_outage`.
  - Kept the Czech wording unchanged.
  - Added display labels for impact values.
  - Updated nodectld halt-reason output to use the new outage wording and
    pretty impact labels.
  - Regenerated packaged `nodectl`, `nodectld`, and `libnodectld` gems in a
    separate generated package commit.
  - Fixed HaveAPI `choices:` usage to pass `values:` explicitly; a bare hash
    is treated as validator options, not as the allowed-choice map.
  - Fixed webui form rendering for mapped API choices, preserving the empty
    filter option while using HaveAPI labels.
  - Changed the overview sidebar link to `Outages`.
  - Changed outage list table headings from `Type` to `Outage` and list-row
    type labels to `Planned`/`Unplanned`.
  - Updated the outage API spec expectation for `unplanned_outage`.
- `vpsf-status`
  - Consumes and emits `planned_outage`/`unplanned_outage`.
  - Normalizes legacy local history values for rendering old stored data.
  - Labels outage impact values in status tables.
  - Renamed internal outage-report helpers away from maintenance/outage terms.
- `vpsfree-irc-bot`
  - Renders planned/unplanned outage labels and labeled impact values in IRC
    notices.
  - Accepts legacy local values for old cached data.
  - Removed the obsolete mailing-list plugin, POP3 polling code, sample
    configuration, and `mail` gem dependency in a standalone commit.
- `vpsfree-mail-templates`
  - Updated English templates to planned/unplanned outage wording.
  - Kept Czech wording as odstávka/výpadek.
  - Uses vpsAdmin-provided impact labels in mail text.
- `web`
  - Updated English FAQ wording only; Czech FAQ remains unchanged.
- `vpsfree-cz-configuration`
  - Updated vpsadmin, vpsf-status, and web inputs with `confctl inputs channel
    set --commit`.
  - Updated the packaged vpsfree-irc-bot source revision and hash.
  - Removed obsolete deployed `mailing_lists` settings for vpsfbot.
  - Added local repository instructions documenting the confctl workflow and
    commit-message preferences.

## Validation

- `vpsadmin`
  - Ruby syntax checks for modified API, spec, nodectl, and metadata files
    passed.
  - ERB syntax checks for modified mail templates passed.
  - PHP syntax check for `webui/forms/outage.forms.php` passed.
  - PHP syntax checks for `webui/pages/page_index.php`,
    `webui/forms/outage.forms.php`, and
    `webui/tests/Regression/OutageDetailsReporterNameXssTest.php` passed after
    the webui label follow-up.
  - PHP syntax checks for `webui/lib/functions.lib.php`,
    `webui/tests/Regression/ApiParamChoicesTest.php`, and
    `webui/tests/Regression/OutageDetailsReporterNameXssTest.php` passed.
  - `composer test -- --filter
    'ApiParamChoicesTest|OutageDetailsReporterNameXssTest'` passed.
  - `nix develop .#webui -c composer test -- --filter
    'OutageDetailsReporterNameXssTest|ApiParamChoicesTest'` passed after the
    webui label follow-up.
  - `git diff --check` passed.
  - `nix develop .#api -c bash -lc 'bundle exec ruby -c
    spec/api/plugins/outage_reports/outage_spec.rb'` passed.
  - `nix develop -c rake vpsadmin:gems` passed and regenerated gem package
    metadata.
  - `nix develop -c ./test-runner.sh test 'webui#support-pages'` was started
    after the mapped-choice fix, but the local VM run hung after Playwright
    evaluation and was killed; do not count it as a pass.
- `vpsf-status`
  - `nix develop -c go test ./...` passed without setting `CGO_ENABLED`.
  - `git diff --check` passed.
- `vpsfree-irc-bot`
  - `ruby -c lib/vpsfree-irc-bot.rb && ruby -c
    lib/vpsfree-irc-bot/outage_reports.rb` passed after mailing-list removal.
  - `nix shell nixpkgs#ruby -c ruby -c
    lib/vpsfree-irc-bot/outage_reports.rb` passed.
  - `nix-shell --run "bundle install ..."` was attempted after removing the
    `mail` gem, but failed in local native `prism` extension compilation; the
    deployment package path was validated through the `int.vpsfbot` confctl
    build instead.
  - `git diff --check` passed.
- `vpsfree-mail-templates`
  - ERB and Ruby metadata syntax checks passed in the Nix development shell.
  - `git diff --check` passed.
- `web`
  - `nix-shell --run 'ruby -c Rakefile && ruby -c
    spec/registration_en_spec.rb'` passed.
  - `git diff --check` passed.
- `vpsfree-cz-configuration`
  - `nix develop -c confctl inputs channel ls` shows:
    - `vpsadminServices` at `f960f0e5`
    - `vpsfStatus` at `5f6db131`
    - `vpsfreeWeb` at `ea0f19ce`
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.vpsfbot`
    passed.
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.web` passed.
  - `nix develop -c confctl build -y cz.vpsfree/vpsadmin/int.api1` passed.
  - `nix develop -c confctl build -y cz.vpsfree/vpsadmin/int.api1` also
    passed after replacing the original vpsadmin input update.
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.vpsfbot`
    passed again after the bot package update to `73ef144`, generation
    `2026-05-28--17-30-54`.
  - `nix develop -c confctl build -y cz.vpsfree/vpsadmin/int.api1` passed
    again after the config rewrite to `f960f0e5`. An initial parallel run built
    a generation but exited with a log-file collision, so it was rerun alone.
  - `git diff --check` passed.

## Merge and cleanup

- Fast-forwarded `master` for all affected repositories on 2026-05-28:
  - `vpsadmin` to `f960f0e5d`
  - `vpsf-status` to `5f6db13`
  - `vpsfree-irc-bot` to `73ef144`
  - `vpsfree-mail-templates` to `d35ad25`
  - `web` to `ea0f19c`
  - `vpsfree-cz-configuration` to `e16d8ad3`
- Removed feature and temporary merge worktrees, plus the empty initiative
  worktree directories.
- Kept local and remote feature branch refs as requested. No feature branches
  were deleted.

## GitHub Actions

- `vpsadmin` current head `f960f0e5`:
  - Webui PHPUnit run `26584462382`: success.
  - CI run `26584463139`: queued as of the last check.
- `vpsadmin` previous head `c9d38cf5`:
  - Webui PHPUnit run `26579189977`: success.
  - CI run `26579189978`: queued as of the last check.
- `vpsadmin` previous head `0db043da`:
  - API Specs (topic parallel) run `26577667251`: success.
  - RuboCop run `26577666852`: success.
  - Webui PHPUnit run `26577667088`: success.
  - CI run `26577666848`: still running as of the last check.
- `vpsadmin` old head `907b6380`:
  - CI run `26566551282`: failed in webui support-pages outage filter tests;
    this prompted the mapped-choice webui fix in `c9d38cf5`.
- `vpsf-status`, `vpsfree-irc-bot`, `vpsfree-mail-templates`, `web`, and
  `vpsfree-cz-configuration` have no branch workflow runs for the feature
  branch.

## Open items

- Continue monitoring the long vpsadmin CI run for `f960f0e5` and inspect
  failed logs if it does not pass.
