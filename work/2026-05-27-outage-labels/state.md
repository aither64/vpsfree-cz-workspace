# Outage labels and wire rename state

## Branches and worktrees

Branch name: `2026-05-27-outage-labels`

| Repository | Worktree | Current head |
| --- | --- | --- |
| vpsadmin | `worktrees/2026-05-27-outage-labels/vpsadmin` | `c9d38cf5e9887d74955fdcbafe70a8093b8ad2e9` |
| vpsf-status | `worktrees/2026-05-27-outage-labels/vpsf-status` | `5f6db13103bf652e69b7b879a69e98794075e64e` |
| vpsfree-irc-bot | `worktrees/2026-05-27-outage-labels/vpsfree-irc-bot` | `184b9a4f2243fd48771f270402e8b5ed9ba65c92` |
| vpsfree-mail-templates | `worktrees/2026-05-27-outage-labels/vpsfree-mail-templates` | `d35ad25dab5de3f94fa25f485debde11413f5cd9` |
| web | `worktrees/2026-05-27-outage-labels/web` | `ea0f19ce13b06194faada5b1fd4eeed3dc46c4b8` |
| vpsfree-cz-configuration | `worktrees/2026-05-27-outage-labels/vpsfree-cz-configuration` | `1981c010428eaf12fad609bc6738f86e7c278b77` |

## Upstream refresh

- Fetched affected repositories before the follow-up push.
- Rebased `vpsfree-irc-bot` on origin/master `e570f08`.
- Rebuilt `vpsfree-cz-configuration` from origin/master `aec8b183` after
  scheduled dependency updates and after the final vpsadmin fix.
- Rebased `vpsadmin` on origin/master `c1fc04738` and added a webui fix for
  mapped HaveAPI choices.

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
  - Added local repository instructions documenting the confctl workflow and
    commit-message preferences.

## Validation

- `vpsadmin`
  - Ruby syntax checks for modified API, spec, nodectl, and metadata files
    passed.
  - ERB syntax checks for modified mail templates passed.
  - PHP syntax check for `webui/forms/outage.forms.php` passed.
  - PHP syntax checks for `webui/lib/functions.lib.php`,
    `webui/tests/Regression/ApiParamChoicesTest.php`, and
    `webui/tests/Regression/OutageDetailsReporterNameXssTest.php` passed.
  - `composer test -- --filter
    'ApiParamChoicesTest|OutageDetailsReporterNameXssTest'` passed.
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
  - `nix shell nixpkgs#ruby -c ruby -c
    lib/vpsfree-irc-bot/outage_reports.rb` passed.
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
    - `vpsadminServices` at `c9d38cf5`
    - `vpsfStatus` at `5f6db131`
    - `vpsfreeWeb` at `ea0f19ce`
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.vpsfbot`
    passed.
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.web` passed.
  - `nix develop -c confctl build -y cz.vpsfree/vpsadmin/int.api1` passed.
  - `nix develop -c confctl build -y cz.vpsfree/vpsadmin/int.api1` also
    passed after replacing the original vpsadmin input update with the
    `c9d38cf5` commit.
  - `git diff --check` passed.

## GitHub Actions

- `vpsadmin` current head `c9d38cf5`:
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

- Continue monitoring the long vpsadmin CI run for `c9d38cf5` and inspect
  failed logs if it does not pass.
