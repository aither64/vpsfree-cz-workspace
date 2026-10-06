---
lifecycle: active
---
# 2026-06-14-vpsadmin-incident-filtering

## Repositories

- `vpsadmin`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-14-vpsadmin-incident-filtering/vpsadmin`
  - Branch: `2026-06-14-vpsadmin-incident-filtering`
  - Base for planning: `origin/master` at `82f39b5256d92240ca4f9da5112eaa7362063742`
  - Head after latest feedback follow-up:
    `9a8a3f435d7397e0531088924853343d0933c71d`
  - Remote: `git@github.com:vpsfreecz/vpsadmin.git`
- `vpsfree-cz-configuration`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-14-vpsadmin-incident-filtering/vpsfree-cz-configuration`
  - Branch: `2026-06-14-vpsadmin-incident-filtering`
  - Base for planning: `origin/master` at `46a0c48fd189f0d44c431bd1b4d8fb986c818df0`
  - Head after implementation: `9e9d6447c0b95c41edd9945de50b826f3dea97ad`
  - Remote: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
- `vpsfree-mail-templates`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-14-vpsadmin-incident-filtering/vpsfree-mail-templates`
  - Branch: `2026-06-14-vpsadmin-incident-filtering`
  - Base after fast-forward: `origin/master` at
    `7da522e060fc18d5426e1dd6cd305b6847faf5ed`
  - Head after implementation: `0a5602949a4915f34c0f932e83acb45eeb56d88e`
  - Remote: `git@github.com:vpsfreecz/vpsfree-mail-templates.git`

## Status

- Worktrees prepared for `vpsadmin` and `vpsfree-cz-configuration`.
- Implementation plan written in `plan.md`.
- vpsAdmin implementation is complete and locally verified.
- vpsAdmin feedback follow-up is implemented, locally verified, committed,
  reviewed, and deployed to the running dev cluster.
- vpsAdmin matcher-ordering follow-up is implemented, locally verified,
  committed, reviewed, and deployed to the running dev cluster.
- vpsAdmin final WebUI ordering polish is implemented, locally verified,
  committed, reviewed, and deployed to the running dev cluster.
- vpsAdmin incident rule form/list feedback follow-up is implemented, locally
  verified, committed, reviewed, and deployed to the running dev cluster.
- vpsAdmin matcher table layout follow-up is implemented, locally verified,
  committed, reviewed, and deployed to the running dev cluster.
- vpsfree-cz-configuration parser updates are complete and locally verified.
- vpsfree-mail-templates incident report mail update is implemented, locally
  verified, and committed.
- DokuWiki API access investigation is complete enough to request credentials:
  both public KB instances expose JSON-RPC and OpenAPI, anonymous reads work,
  and authenticated writes should use a DokuWiki bearer token for a normal wiki
  user with write permission.
- Draft DokuWiki documentation is in
  `work/2026-06-14-vpsadmin-incident-filtering/wiki-incident-report-filters.dokuwiki.txt`.
- Commits created:
  - vpsAdmin: `e3f31cbb701748b54a7a3b48bc4f5043fa4018b5`
    (`incidents: add report filtering rules`)
  - vpsAdmin: `53cf4fabdd76700e288505a7b016c17b95ea7afc`
    (`incidents: refine report rule management`)
  - vpsAdmin: `578976f54ded65b65f1764bf75a77533a0d171a4`
    (`incidents: bound report rule regex matching`)
  - vpsAdmin: `6cd5e60b7d44bc87f0d2ddee3b9f1fab4385dcac`
    (`incidents: cap report rule evaluation time`)
  - vpsAdmin: `5c8359b21c6921cf1e95eb5dd47be77c916bb3c1`
    (`incidents: fix rule editor inline forms`)
  - vpsAdmin: `37a9796eacdec1cbdcb521d50226c3768da55c85`
    (`incidents: polish report rule management`)
  - vpsAdmin: `891c8461c8063bcc16d0156e9c5ea77fd339fe64`
    (`incidents: remove matcher ordering from report rules`)
  - vpsAdmin: `504f31ee614daf4863b938930c38bd7c2b3cdf14`
    (`incidents: constrain report rule reordering`)
  - vpsAdmin: `c367fcd127e6b2bef627aeccc9711e67b0f4cf6d`
    (`incidents: refine report rule forms`)
  - vpsAdmin: `9a8a3f435d7397e0531088924853343d0933c71d`
    (`incidents: adjust matcher edit rows`)
  - vpsfree-cz-configuration:
    `9e9d6447c0b95c41edd9945de50b826f3dea97ad`
    (`vpsadmin-config: allow filtering automated incident reports`)
  - vpsfree-mail-templates:
    `0a5602949a4915f34c0f932e83acb45eeb56d88e`
    (`vps_incident_report: mention incident filters`)
- User clarified that every incident report should carry a parameter deciding
  whether filtering is allowed, and admins must be able to set it when
  creating reports. Plan uses `allow_filtering`, default `false`.
- Design summary:
  - User-owned ordered incident report rules.
  - Rules have action `report` or `ignore`; first matching rule wins, matching
    OOM report rule semantics.
  - Reporting rules may carry a separate recipient policy:
    `default`, `default_and_custom`, or `custom`.
  - Custom recipient addresses are modeled separately from the action, likely
    as nested rule recipient rows, so `report`/`ignore` remains the outcome.
  - Rules have multiple ANDed matchers with field/operator/value.
  - Explicit default/fallback behavior is to report.
  - Eligible ignored reports remain saved, are marked `ignored`, link to the
    deciding rule, and do not mail the user.
  - Existing and direct admin-created reports keep current behavior by default.
  - Dropped the initially proposed `continue` action because it would mainly
    add non-decisive counter semantics and make rule/result explanations less
    clear. It can be added later as an observe/count action if needed.
  - Existing mail delivery supports adding extra `to`/`cc`/`bcc` addresses.
    Replacing default user recipients will need a small `MailTemplate` delivery
    option while still rendering the standard incident template.
  - Human-friendly labels for rule actions, recipient policies, matcher
    fields/operators, and recipient kinds are provided through HaveAPI choice
    metadata (`choices: { values: ... }`), following the existing outage
    resource pattern.

## Implementation summary

### vpsadmin

- Added additive migration and schema entries for:
  - `incident_reports.allow_filtering`
  - `incident_reports.ignored`
  - `incident_reports.incident_report_rule_id`
  - `incident_report_rules`
  - `incident_report_rule_matchers`
  - `incident_report_rule_recipients`
- Added rule, matcher, and recipient models with validation, matching logic,
  hit counters, recipient policy support, and custom recipient safeguards.
- Added `VpsAdmin::API::IncidentReportFilters` evaluator. It evaluates only
  reports with `allow_filtering = true`, applies the first matching enabled
  user rule, stores the deciding rule, increments hit counters, and marks
  ignored reports as reported without mailing or applying side effects.
- Extended incident report delivery paths:
  - mailbox/parser handler filters before sending user mail or reply;
  - direct/admin `IncidentReport::New` filters before mail and side effects;
  - pending `IncidentReport::Process` filters before mail and side effects.
- Extended mail template delivery with `include_default_recipients: false` so
  report rules can replace normal user/template recipients with custom
  addresses.
- Added HaveAPI resources/actions for `incident_report_rule`, nested
  `matcher`, and nested `recipient`, with admin/all-user and user/self
  authorization.
- Extended `incident_report` API output/input/filtering with
  `allow_filtering`, `ignored`, and `incident_report_rule`.
- Extended the PHP incidents WebUI with rule list/create/edit/delete, matcher
  and recipient management, incident list filters and columns, incident detail
  fields, and the admin create checkbox.
- Updated endpoint coverage and CI selection metadata.
- Added focused API/model/transaction/mail/resource specs.
- Added explicit non-owner denial specs for nested matcher and recipient
  create/update/delete after mandatory review called out that test gap.
- After the mail-template/documentation follow-up review, fixed a blocking
  issue where the `allow_filtering` create default was also applied to index
  filtering. `allow_filtering` is now defaulted only in `incident_report#create`
  and index requests filter by it only when explicitly provided.
- Added index regression specs proving unfiltered incident lists include both
  filterable and unfilterable reports, while explicit `allow_filtering` filters
  still work.
- Adjusted incident rule add forms so blank `position` is omitted, allowing
  API append behavior instead of forcing WebUI-created rules to position `0`.
- Adjusted the WebUI add-rule form to offer only recipient policies that can
  validate before recipients exist. `custom` remains available in rule edit
  after adding recipients.
- Feedback follow-up implemented on 2026-06-15:
  - Rule lists are always scoped to a specific user and are reachable from
    user profile, incident report list, and incident report detail sidebars.
  - Admins reach a user's rules through that user's profile; the rule list no
    longer exposes user ID filtering or user ID fields in the add form.
  - Rule positions are no longer exposed in WebUI forms. New rules append to
    the end, drag-and-drop table ordering posts reorder actions, and up/down
    arrows provide a no-JavaScript fallback.
  - Rule enablement uses `boolean_icon()`; enabled can be toggled from the
    list, disabled rules use the existing gray row background, and the
    implicit rule shows a non-toggle true icon with label `Implicit rule`.
  - Rule deletion now requires confirmation.
  - Matchers and custom recipients are editable inline; their add forms are
    the final table rows.
  - Matcher summaries in the rule list render one matcher per line and
    truncate long values to avoid wide table overflow.
  - User-facing option labels are taken from API descriptions when available,
    with PHP fallback maps only as a guard.
  - Removed matcher fields `ip_address_assignment_id` and `mailbox_id`.
  - Added matcher field `vps_hostname`.
  - Added regular-expression matcher operators `matches` and `not_matches`
    with regex validation.
  - Rule creation can create the first custom recipient and then switch the
    rule to `custom`, so all recipient policies are available from the start.
  - Rule creation also consumes the first custom recipient field for
    `default_and_custom` when an address is provided.
  - Playwright support-page coverage now exercises user-scoped incident rule
    CRUD, inline matcher and recipient edits, custom recipient policy, matcher
    summary truncation, sidebar links, and delete confirmation.
- Matcher-ordering follow-up implemented on 2026-06-15:
  - Removed matcher `position` from the HaveAPI resource, create/update input,
    model validation, original incident-rule migration, and schema.
  - Matchers are listed in stable `id` order for display only; all matcher
    semantics remain ANDed.
  - Removed matcher drag handles, move arrows, reorder actions, and WebUI
    reorder helpers.
  - Kept rule ordering intact.
  - Fixed the deployed TableDnD asset issue by restoring
    `webui/public/js/jquery.tablednd.js` permissions to `0644`.
  - Added handle-only cursor styling and made the rule reorder script skip
    cleanly when the plugin is unavailable.
  - Shortened rule-detail matcher value inputs to size `30` and recipient
    address inputs to size `38`.
  - Scoped the add-rule custom recipient show/hide script to the add form.

### vpsfree-cz-configuration

- Set `allow_filtering: true` on automated abuse notice parser-created
  incident reports for BitNinja, Fail2Ban, LeakIX, MasterDC, PROKI, SpamCop,
  USGO, and X-ARF.
- Extended parser specs to assert the flag.
- Added explicit top-level `csv` Gem dependency because `master_dc.rb` requires
  it at runtime and Ruby 3.4 no longer provides it as a default gem.

### vpsfree-mail-templates

- Added a conditional note to `vps_incident_report` English and Czech plain
  text templates.
- The note is shown only for filterable incident reports and links to
  `?page=incidents&action=rule_list`.
- The note is placed after the report/action guidance and before the sign-off,
  so the incident report itself remains first.
- The ERB guard uses `respond_to?(:allow_filtering)` so the template can be
  deployed before every vpsAdmin renderer has the new model attribute.

### DokuWiki documentation/API

- Existing user documentation pages:
  - English: `manuals:vps:incidents`,
    `https://kb.vpsfree.org/manuals/vps/incidents`
  - Czech: `navody:vps:incidenty`,
    `https://kb.vpsfree.cz/navody/vps/incidenty`
- `vpsfree-cz-configuration` configures both DokuWiki sites in
  `cluster/cz.vpsfree/containers/int.kb/config.nix`.
- Current DokuWiki settings include `remote = true`, `useacl = true`,
  `authtype = "oauth"`, `superuser = "@admin"`, and `remoteuser = ""`.
  The blank `remoteuser` means the API is not additionally restricted by
  username/group, but ACL checks still apply to page operations.
- Both sites expose:
  - JSON-RPC endpoint: `/lib/exe/jsonrpc.php`
  - OpenAPI explorer: `/lib/exe/openapi.php`
  - OpenAPI spec: `/lib/exe/openapi.php?spec=1`
- The deployed API exposes `core.getPage`, `core.getPageInfo`,
  `core.savePage`, `core.whoAmI`, and legacy `wiki.putPage` among other
  methods. `core.savePage` is the preferred page update method.
- Anonymous `core.getPageInfo`/`core.getPage` works for the public incident
  pages and reports permission `1` (read).
- Anonymous `core.whoAmI` returns `No user available`, so editing requires an
  authenticated user.
- Official DokuWiki documentation says API authentication should use Token
  Auth where users create a login token in their profile and clients send it
  as `Authorization: Bearer <token>`. If the webserver does not forward that
  header, `X-DokuWiki-Token` can be used instead.
- Recommended access for Codex/Aither:
  - create or select a normal wiki/OAuth user with write rights to the two
    incident pages;
  - generate a DokuWiki login token from that user's profile;
  - provide the token out-of-band as an environment variable, never in files or
    commits;
  - optionally restrict `remoteuser` in configuration to a small group for API
    users instead of leaving it blank.

## Commands run

- `bin/dev-session current`
  - Returned active slug `2026-06-14-vpsadmin-incident-filtering`.
- `find work/2026-06-14-vpsadmin-incident-filtering -maxdepth 2 -type f -print`
  - Confirmed empty `plan.md` and `state.md` existed.
- `find worktrees/2026-06-14-vpsadmin-incident-filtering -maxdepth 2 -type d -print`
  - Confirmed the initiative worktree directory existed but no repositories
    were checked out yet.
- `bin/dev-session worktree add 2026-06-14-vpsadmin-incident-filtering vpsadmin --as-is --branch 2026-06-14-vpsadmin-incident-filtering --base master`
  - Created the `vpsadmin` worktree, but checkout hook reported missing
    Overcommit gem in the ambient shell.
- `bin/dev-session worktree add 2026-06-14-vpsadmin-incident-filtering vpsfree-cz-configuration --as-is --branch 2026-06-14-vpsadmin-incident-filtering --base master`
  - Created the `vpsfree-cz-configuration` worktree, but checkout hook reported
    missing bundled gems in the ambient shell.
- `git status --short --branch`
  - Confirmed both worktrees are on
    `2026-06-14-vpsadmin-incident-filtering` with clean working trees.
- Read repository-local `AGENTS.md` in both worktrees.
- Searched and read existing vpsAdmin incident/OOM implementation:
  - `api/models/incident_report.rb`
  - `api/lib/vpsadmin/api/resources/incident_report.rb`
  - `api/lib/vpsadmin/api/incident_reports.rb`
  - `api/lib/vpsadmin/api/tasks/incident_report.rb`
  - `api/models/transaction_chains/incident_report/*.rb`
  - `api/models/oom_report_rule.rb`
  - `api/lib/vpsadmin/api/resources/oom_report_rule.rb`
  - `api/lib/vpsadmin/supervisor/node/oom_reports.rb`
  - `webui/pages/page_incidents.php`
  - `webui/forms/incidents.forms.php`
  - `webui/pages/page_oom_reports.php`
  - `webui/forms/oom_reports.forms.php`
- Searched and read vpsFree.cz parser configuration:
  - `configs/vpsadmin/api/incident_reports.rb`
  - `configs/vpsadmin/api/abuse_notice_parser/proki.rb`
  - `configs/vpsadmin/api/abuse_notice_parser/utils.rb`
- Checked branch bases with `git rev-parse HEAD`, `master`, and
  `origin/master`.
- `git merge --ff-only origin/master` in the `vpsadmin` worktree
  - Fast-forwarded the feature branch from stale local `master`
    `aba00ba4312a6f6760f6988b0888cf3bc1b62713` to current
    `origin/master` `82f39b5256d92240ca4f9da5112eaa7362063742`.
  - Hook again reported missing Overcommit gem in the ambient shell.
- Re-read updated `vpsadmin/AGENTS.md` after the fast-forward.
- `nix develop .#api -c bundle exec rspec ...`
  - Focused vpsAdmin suite covering incident report rules, report API, parser
    handler, transaction chains, send chain, and mail templates.
  - First run found a fixture-shape bug in
    `spec/models/incident_report_rule_spec.rb`; fixed by unwrapping the helper
    result when it returns a standalone VPS fixture hash.
  - Final result: 68 examples, 0 failures.
- `nix develop .#api -c bundle exec rspec spec/api/resources/incident_report_rule_spec.rb`
  - Added after mandatory review to cover non-owner nested matcher/recipient
    create/update/delete denial.
  - Result: 8 examples, 0 failures.
- `nix develop .#api -c bundle exec rspec spec/api/resources/incident_report_spec.rb`
  - Rerun after review finding around `allow_filtering` index filtering.
  - Result: 25 examples, 0 failures.
- `nix develop .#api -c bundle exec rspec spec/api/resources/incident_report_rule_spec.rb`
  - Rerun after WebUI/order follow-up.
  - Result: 8 examples, 0 failures.
- `nix develop -c bundle exec rspec spec/configs/vpsadmin/api/abuse_notice_parsers_spec.rb spec/configs/vpsadmin/api/generic_abuse_parser_spec.rb spec/configs/vpsadmin/api/master_dc_parser_spec.rb`
  - First run failed before examples because `csv` was not available under the
    Ruby 3.4 dev shell.
  - Added explicit top-level `gem 'csv'` and refreshed `Gemfile.lock`.
  - Final result: 12 examples, 0 failures.
- `nix develop .#api -c bundle exec rspec spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb`
  - Result: 2 examples, 0 failures.
- `nix develop .#api -c bundle exec ruby /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-14-vpsadmin-incident-filtering/vpsadmin/tests/ci-selection-test.rb`
  - Result: 15 runs, 54 assertions, 0 failures.
- Syntax checks:
  - `ruby -c` for new vpsAdmin migration, filter service, rule resource, and
    rule models: OK.
  - `php -l webui/forms/incidents.forms.php`: OK.
  - `php -l webui/pages/page_incidents.php`: OK.
  - Rerun after review follow-up:
    - `ruby -c api/lib/vpsadmin/api/resources/incident_report.rb`: OK.
    - `php -l webui/forms/incidents.forms.php`: OK, rerun after the final
      add-rule recipient-policy UX follow-up.
    - `php -l webui/pages/page_incidents.php`: OK.
  - `ruby -c` for changed abuse notice parser files in
    `vpsfree-cz-configuration`: OK.
- Hook checks:
  - vpsAdmin Overcommit pre-commit hooks passed under `nix develop`.
    `PhpCsFixer` rewrote unrelated PHP files when run manually across the
    worktree; those formatter-only hunks were manually reverted before
    staging.
  - vpsfree-cz-configuration Overcommit pre-commit hooks passed under
    `nix develop`.
  - Removed local generated `.bin/`, `.bundle/`, and `.rubocop_cache/`
    artifacts from `vpsfree-cz-configuration` after test/hook runs.
- Commit checks:
  - vpsAdmin commit and amend both ran Overcommit hooks through
    `nix develop`; hooks passed. Commit-msg hook warned about lines over 72
    characters, but the workspace rule is 80 characters and all message lines
    are within that limit.
  - vpsAdmin follow-up amend to
    `f4fc5f1ae75485ff57835deb3f683fa1675ae029` ran Overcommit hooks through
    root `nix develop`; hooks passed with the same non-blocking 72-character
    commit-message warnings.
  - vpsAdmin final amend to
    `e3f31cbb701748b54a7a3b48bc4f5043fa4018b5` ran Overcommit hooks through
    root `nix develop`; hooks passed with the same non-blocking 72-character
    commit-message warnings.
  - vpsfree-cz-configuration commit ran Overcommit hooks through
    `nix develop`; hooks passed. Commit-msg hook gave the same non-blocking
    72-character warning.
- Mandatory change review:
  - Fresh standalone reviewer found no significant findings in the committed
    diffs.
  - Residual risks reported:
    - deployment must apply the vpsAdmin migration before new incident
      processing code runs;
    - add explicit nested matcher/recipient non-owner denial tests.
  - Deployment-order note was updated in `plan.md`.
  - Nested non-owner denial specs were added and the vpsAdmin commit was
    amended.
  - Follow-up review of amended vpsAdmin head
    `5b6ceb0b98ae026b8922457b39537da4c8db6d00` found no significant new
    findings and removed the prior residual test-coverage caveat.
- Mandatory review after adding mail templates and DokuWiki draft:
  - Fresh standalone reviewer found one blocking issue: unfiltered incident
    report index requests would default to `allow_filtering=false` because the
    create-time parameter default lived in the shared parameter definition.
  - Also noted two advisory issues:
    - DokuWiki draft wording said admin-sent reports are never filterable,
      while admins can explicitly opt created reports into filtering.
    - WebUI rule creation forced default `position = 0`, bypassing API append
      behavior.
  - All three issues were fixed. The DokuWiki draft now says admin-created
    reports are not filterable by default unless explicitly marked filterable.
- Follow-up review of the amended vpsAdmin head
  `f4fc5f1ae75485ff57835deb3f683fa1675ae029` found no blocking or important
  findings. It noted one UX advisory: the WebUI add-rule form allowed
  `recipient_policy = custom`, but custom-only rules need a recipient and
  recipients are added after rule creation.
- The UX advisory was fixed by limiting the initial rule form to `default` and
  `default_and_custom`; the edit form still supports `custom`.
- Final follow-up review of vpsAdmin head
  `e3f31cbb701748b54a7a3b48bc4f5043fa4018b5` and the cross-repo diffs found
  no blocking, important, or advisory issues.
  - Residual risk: deployment ordering remains important.
  - Residual test gap: no browser/Playwright flow was run for creating a rule,
    adding a recipient, and switching to `custom`.
- `bin/dev-session worktree add 2026-06-14-vpsadmin-incident-filtering vpsfree-mail-templates --as-is --branch 2026-06-14-vpsadmin-incident-filtering --base master`
  - Created the `vpsfree-mail-templates` worktree.
- Read `vpsfree-mail-templates/AGENTS.md`.
- `git merge --ff-only origin/master` in `vpsfree-mail-templates`
  - Fast-forwarded the feature branch from local `master`
    `d35ad25dab5de3f94fa25f485debde11413f5cd9` to `origin/master`
    `7da522e060fc18d5426e1dd6cd305b6847faf5ed`.
  - Preserved the local incident template edits.
- `ruby -rerb -e "ARGV.each { |p| ERB.new(File.read(p), trim_mode: '-').src }" vps_incident_report/en.plain.erb vps_incident_report/cs.plain.erb`
  - ERB syntax compile check passed before and after adding the defensive
    `respond_to?` guard.
- `git diff --check` in `vpsfree-mail-templates`
  - Passed.
- Checked for declared hook frameworks in `vpsfree-mail-templates`
  - No `.overcommit.yml`, `.pre-commit-config.yaml`, `lefthook.yml`, or
    `.husky` was present.
- `nix develop -c ruby -rerb -e "ARGV.each { |p| ERB.new(File.read(p), trim_mode: '-').src }" vps_incident_report/en.plain.erb vps_incident_report/cs.plain.erb`
  - Passed inside the repository Nix/Ruby environment.
  - First run installed bundled gems into ignored `.gems/`.
- `git commit -F <tmpfile>` in `vpsfree-mail-templates`
  - Created commit `0a5602949a4915f34c0f932e83acb45eeb56d88e`
    (`vps_incident_report: mention incident filters`).
- DokuWiki API investigation commands:
  - Queried `cluster/cz.vpsfree/containers/int.kb/config.nix` in
    `vpsfree-cz-configuration` for DokuWiki site config.
  - Used `curl` against DokuWiki official raw docs for Remote API, JSON-RPC,
    `remote`, `remoteuser`, and authentication/token auth behavior.
  - Used `curl` against `https://kb.vpsfree.org/lib/exe/openapi.php?spec=1`
    and `https://kb.vpsfree.cz/lib/exe/openapi.php?spec=1` to enumerate
    deployed API methods.
  - Verified `core.getPageInfo` and `core.getPage` through standard JSON-RPC
    POSTs on the English and Czech KB sites.
  - Verified unauthenticated `core.whoAmI` returns `No user available`.
- `dev-clusters/vpsadmin/bin/devcluster start 2026-06-14-vpsadmin-incident-filtering --topology single --network bridge`
  - Built and started a single-node vpsAdmin dev cluster for the feature
    worktree.
  - Initial start reached `ready: yes`, but exited non-zero during the final
    pool refresh because `/run/osctl/osctld.sock` was not available yet on
    `node1`.
  - Shortly after, `node1` reported `osctld` running and the socket existed.
- `dev-clusters/vpsadmin/bin/devcluster refresh 2026-06-14-vpsadmin-incident-filtering`
  - Reran the final pool preparation after `osctld` came up.
  - Completed successfully.
- `dev-clusters/vpsadmin/bin/devcluster status 2026-06-14-vpsadmin-incident-filtering`
  - Final status: running, topology `single`, network `bridge`, `ready: yes`.
- `curl -k -I https://webui.aitherdev.int.vpsfree.cz/`
  - Returned HTTP 200 from nginx/PHP.
- `curl -k -I https://api.aitherdev.int.vpsfree.cz/`
  - Returned HTTP 200.
- Feedback follow-up commands on 2026-06-15:
  - `php -l webui/forms/incidents.forms.php && php -l webui/pages/page_incidents.php && php -l webui/pages/page_adminm.php`
    - Passed.
  - `ruby -c` on touched incident rule API/model/spec Ruby files
    - Passed.
  - `git diff --check`
    - Passed.
  - `nix develop .#vpsadmin -c git commit -F <tmpfile>`
    - Ran Overcommit pre-commit hooks successfully on staged files:
      Nixfmt OK, PhpCsFixer OK, and RuboCop OK.
    - Commit-msg hooks passed with a 72-column warning; all commit message
      lines are 80 characters or fewer.
    - Created commit `37a9796eacdec1cbdcb521d50226c3768da55c85`
      (`incidents: polish report rule management`).
- Mandatory change review of vpsAdmin follow-up range
  `5c8359b21c6921cf1e95eb5dd47be77c916bb3c1..37a9796eacdec1cbdcb521d50226c3768da55c85`
  found no blocking, important, or advisory findings.
  - Reviewer checked the API/WebUI label contract, authorization paths for
    batch matcher/recipient updates, deployment compatibility notes, commit
    shape, and local repository instructions.
  - Reviewer ran `nix develop .#api -c bundle exec rspec spec/models/incident_report_rule_spec.rb:170`
    and `git diff --check`; both passed.
  - Residual gaps: Playwright does not directly exercise drag gesture behavior
    or prove handle-only/background reorder in-browser; no explicit
    no-JavaScript browser coverage for new-rule recipient-field hiding.
  - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/lib/pages/support.cjs`
    and `... specs/support-pages.spec.cjs`
    - Passed.
  - `nix develop .#api -c bundle exec rubocop models/incident_report_rule.rb models/incident_report_rule_matcher.rb models/incident_report_rule_recipient.rb lib/vpsadmin/api/resources/incident_report_rule.rb spec/models/incident_report_rule_spec.rb spec/api/resources/incident_report_rule_spec.rb`
    - Passed, 6 files inspected, no offenses.
  - `nix develop .#vpsadmin -c php-cs-fixer fix --dry-run --diff --config=.php-cs-fixer.dist.php webui/forms/incidents.forms.php webui/pages/page_incidents.php webui/pages/page_adminm.php`
    - Passed with no files needing changes.
  - `nix develop .#api -c bundle exec rspec spec/models/incident_report_rule_spec.rb spec/api/resources/incident_report_rule_spec.rb`
    - Passed, 18 examples, 0 failures.
  - `./test-runner.sh ls 'webui#*'`
    - Confirmed `webui#support-pages` target exists.
  - `./test-runner.sh test 'webui#support-pages'`
    - Failed after 1 of 9 Playwright examples due to a test locator strictness
      issue in the new incident rule CRUD test:
      `#aside a[href*="page=adminm&action=edit"]` matched sidebar and table
      links.
    - Fixed by asserting the sidebar links by visible role/name
      (`User profile`, `Incident reports`). The heavy webui target still needs
      to be rerun after commit and mandatory change review.
  - `nix develop .#vpsadmin -c bundle exec overcommit --run`
    - Started the declared hook framework but invoked project-wide RuboCop and
      PHP CS Fixer rather than a staged-file check; it was stopped.
    - PHP CS Fixer had touched unrelated webui files. Those formatter-only
      spillover diffs were reversed immediately. Focused hook-equivalent
      checks above were used before committing.
  - `git commit -F <tmpfile>` in `vpsadmin`
    - Ran Overcommit pre-commit hooks successfully on staged files:
      Nixfmt OK, PhpCsFixer OK, RuboCop OK.
    - Commit-msg hooks passed with a 72-column warning; all commit message
      lines were checked afterward and are 80 characters or fewer.
    - Created commit `53cf4fabdd76700e288505a7b016c17b95ea7afc`
      (`incidents: refine report rule management`).
- Mandatory change review of vpsAdmin feedback commit
  `53cf4fabdd76700e288505a7b016c17b95ea7afc` found one important issue and
  one advisory:
  - Important: user-controlled regex matchers had no runtime timeout guard,
    so a costly expression could burn CPU during incident processing.
  - Advisory: ordering/toggle WebUI paths are not directly covered by tests.
  - The important issue was fixed in commit
    `578976f54ded65b65f1764bf75a77533a0d171a4`.
  - The ordering/toggle coverage gap remains advisory; the main CRUD,
    inline-edit, sidebar, truncation, and delete-confirmation browser flow is
    covered, and the heavy target is rerun below.
- Regex guard follow-up commands on 2026-06-15:
  - `ruby -c api/models/incident_report_rule_matcher.rb && ruby -c api/spec/models/incident_report_rule_spec.rb`
    - Passed.
  - `nix develop .#api -c bundle exec rubocop models/incident_report_rule_matcher.rb spec/models/incident_report_rule_spec.rb`
    - Passed, 2 files inspected, no offenses.
  - `nix develop .#api -c bundle exec rspec spec/models/incident_report_rule_spec.rb spec/api/resources/incident_report_rule_spec.rb`
    - Passed, 19 examples, 0 failures.
  - `git diff --check`
    - Passed.
  - `git commit -F <tmpfile>` in `vpsadmin`
    - Ran Overcommit pre-commit hooks successfully on staged files:
      Nixfmt OK, RuboCop OK.
    - Commit-msg hooks passed with 72-column warnings; all commit message
      lines were checked afterward and are 80 characters or fewer.
    - Created commit `578976f54ded65b65f1764bf75a77533a0d171a4`
      (`incidents: bound report rule regex matching`).
- Mandatory change review of vpsAdmin head
  `578976f54ded65b65f1764bf75a77533a0d171a4` found one important issue:
  - Important: per-regexp timeouts still allowed a user to stack many
    near-timeout regex matchers across a full rule set, creating a practical
    worker-level DoS risk.
  - The issue was fixed in commit
    `6cd5e60b7d44bc87f0d2ddee3b9f1fab4385dcac`.
- Aggregate evaluation budget follow-up commands on 2026-06-15:
  - `ruby -c api/lib/vpsadmin/api/incident_report_filters.rb && ruby -c api/models/incident_report_rule.rb && ruby -c api/spec/models/incident_report_rule_spec.rb`
    - Passed.
  - `nix develop .#api -c bundle exec rubocop lib/vpsadmin/api/incident_report_filters.rb models/incident_report_rule.rb models/incident_report_rule_matcher.rb spec/models/incident_report_rule_spec.rb`
    - Passed, 4 files inspected, no offenses.
  - `nix develop .#api -c bundle exec rspec spec/models/incident_report_rule_spec.rb spec/api/resources/incident_report_rule_spec.rb`
    - Passed, 20 examples, 0 failures.
  - `git diff --check`
    - Passed.
  - `git commit -F <tmpfile>` in `vpsadmin`
    - Ran Overcommit pre-commit hooks successfully on staged files:
      Nixfmt OK, RuboCop OK.
    - Commit-msg hooks passed with 72-column warnings; all commit message
      lines were checked afterward and are 80 characters or fewer.
    - Created commit `6cd5e60b7d44bc87f0d2ddee3b9f1fab4385dcac`
      (`incidents: cap report rule evaluation time`).
- Final mandatory change review of vpsAdmin head
  `6cd5e60b7d44bc87f0d2ddee3b9f1fab4385dcac` found no blocking,
  important, or advisory code findings.
  - Residual gaps: heavy `webui#support-pages` still needed rerun at the time
    of review; browser coverage still does not directly exercise enabled
    toggle, up/down move links, or drag-and-drop reorder; regex timeout spec
    uses mocking rather than a real catastrophic regexp.
- Browser follow-up commands on 2026-06-15:
  - `php -l webui/forms/incidents.forms.php`
    - Passed.
  - `php -l webui/pages/page_incidents.php`
    - Passed.
  - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/lib/pages/support.cjs`
    - Passed.
  - `git diff --check`
    - Passed.
  - `./test-runner.sh test 'webui#support-pages'`
    - Passed. Playwright reported `9 passed (3.5m)` and the runner reported
      `Script support-pages finished in 521.79s` in
      `/tmp/os-test-runner/os-test-webui-fd1a3b33/test-runner.log`.
  - `git commit -F /tmp/vpsadmin-incident-inline-forms.commitmsg`
    - In the ambient shell, Git stopped before committing because the shared
      Overcommit hook was installed but the `overcommit` gem was not present
      in that shell.
  - `nix develop .#vpsadmin -c git commit -F /tmp/vpsadmin-incident-inline-forms.commitmsg`
    - Ran Overcommit pre-commit hooks successfully on staged files:
      Nixfmt OK and PhpCsFixer OK.
    - Commit-msg hooks passed with a 72-column warning; all commit message
      lines are 80 characters or fewer.
    - Created commit `5c8359b` (`incidents: fix rule editor inline forms`).
  - Fixes made after the failed browser attempts:
    - matcher and recipient success paths now redirect back to the rule editor
      so session notifications are visible after POST;
    - matcher and recipient rows render complete inline forms in one table
      cell, and the previous rule update form state is cleared before the
      nested tables, avoiding invalid nested forms;
    - the Playwright support page helper now locates edited matcher and
      recipient rows by input values, because input `value` attributes are not
      visible table text.
  - API label note: incident rule actions, recipient policies, matcher fields,
    matcher operators, and recipient kinds are exposed as HaveAPI associative
    choice values. The WebUI reads those `validators.include.values` labels
    from API metadata and does not keep incident-rule label tables locally.
- Mandatory change review of vpsAdmin follow-up range
  `6cd5e60b7d44bc87f0d2ddee3b9f1fab4385dcac..5c8359b21c6921cf1e95eb5dd47be77c916bb3c1`
  found no findings.
  - Reviewer confirmed the inline matcher/recipient forms render as real POST
    forms inside table cells, keep CSRF tokens, and use post-redirect-get for
    notifications.
  - Residual gap: Playwright covers the normal user inline flows, but not a
    separate admin-through-user-profile inline edit flow. This path relies on
    the same API authorization and `user_id` redirect handling.
- API-label/WebUI feedback follow-up commands on 2026-06-15:
  - Removed the remaining WebUI incident-rule label maps. `incident_param_choices`
    now reads labels from API descriptions only.
  - Added `load_validators: false` to the incident rule action,
    recipient-policy, matcher field/operator, and recipient kind API
    parameters so imported ActiveRecord validators do not replace labeled
    HaveAPI choice hashes with raw arrays.
  - `nix develop .#api -c bundle exec rspec spec/api/resources/incident_report_rule_spec.rb`
    - First focused rerun reproduced the live issue: matcher field choices
      were emitted as raw arrays from model validators.
    - After the `load_validators: false` fix, passed, 10 examples,
      0 failures.
    - Final rerun after Playwright helper changes also passed, 10 examples,
      0 failures.
  - `curl -k -s -X OPTIONS https://api.aitherdev.int.vpsfree.cz/v7.0/`
    - Before redeploy, live dev API still returned old matcher fields
      `ip_address_assignment_id` and `mailbox_id`, and no regex operators.
    - A plain `vpsadmin-api.service` restart was insufficient because the
      service runs from a Nix-store `vpsadmin-api-dev` derivation.
  - `dev-clusters/vpsadmin/bin/devcluster update 2026-06-14-vpsadmin-incident-filtering services`
    - Rebuilt and switched the services VM from the current dirty worktree.
    - After the update, live API metadata returned labeled choice hashes with
      `vps_hostname`, regex operators, and `not_equals` labelled
      `does not equal`; removed matcher fields were absent.
  - `curl -k -s -o /dev/null -D - https://webui.aitherdev.int.vpsfree.cz/`
    and `curl -k -s -o /dev/null -D - https://api.aitherdev.int.vpsfree.cz/`
    - Both returned HTTP 200 after the devcluster services update.
  - `php -l webui/forms/incidents.forms.php && php -l webui/pages/page_incidents.php && php -l webui/forms/vps.forms.php`
    - Passed.
  - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/lib/pages/support.cjs`
    and `... tests/playwright/webui/specs/support-pages.spec.cjs`
    - Passed.
  - `nix develop .#api -c bundle exec rubocop lib/vpsadmin/api/resources/incident_report_rule.rb spec/api/resources/incident_report_rule_spec.rb`
    - Passed, 2 files inspected, no offenses.
  - `nix develop .#vpsadmin -c php-cs-fixer fix --dry-run --diff --config=.php-cs-fixer.dist.php webui/forms/incidents.forms.php webui/pages/page_incidents.php webui/forms/vps.forms.php`
    - Initially reported an existing touched-file style issue in
      `webui/forms/vps.forms.php`; fixed with php-cs-fixer and the rerun
      passed with no files needing changes.
  - `./test-runner.sh test 'webui#support-pages'`
    - First run failed in the incident rule deletion helper because Playwright
      waited for the click while the JavaScript confirm dialog was open.
    - Updated the helper to accept the dialog concurrently with the click.
    - Rerun passed: 1 test script successful in 767.31 seconds.
  - `git diff --check`
    - Passed.
- Matcher-ordering follow-up commands on 2026-06-15:
  - `php -l webui/forms/incidents.forms.php && php -l webui/pages/page_incidents.php`
    - Passed.
  - `ruby -c api/lib/vpsadmin/api/resources/incident_report_rule.rb && ruby -c api/models/incident_report_rule.rb && ruby -c api/models/incident_report_rule_matcher.rb && ruby -c api/db/migrate/20260614160000_add_incident_report_rules.rb && ruby -c api/spec/api/resources/incident_report_rule_spec.rb`
    - Passed.
  - `nix develop .#api -c bash -lc 'cd api && bundle exec rspec ...'`
    - Failed because the component shell already entered the API context and
      the extra `cd api` resolved to a nonexistent nested directory.
  - `nix develop ..#api -c bundle exec rspec spec/api/resources/incident_report_rule_spec.rb spec/models/incident_report_rule_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/lib/vpsadmin/api/incident_reports_spec.rb`
    - Passed, 40 examples, 0 failures.
  - `./test-runner.sh test 'webui#support-pages'`
    - Passed: 1 test script successful in 810.28 seconds.
  - `curl -k -s -o /dev/null -D - https://webui.aitherdev.int.vpsfree.cz/js/jquery.tablednd.js`
    - Returned HTTP 200 after restoring the JS file mode to `0644`.
  - `dev-clusters/vpsadmin/bin/devcluster update 2026-06-14-vpsadmin-incident-filtering services`
    - Rebuilt and switched the services VM from the current dirty worktree.
  - `curl -k -s -X OPTIONS https://api.aitherdev.int.vpsfree.cz/v7.0/`
    - After the services update, live matcher create/update input parameters
      were `field`, `operator`, and `value`; `position` was absent.
    - Live matcher operator labels included `does not equal`, `matches regular
      expression`, and `does not match regular expression`.
  - `curl -k -s -o /dev/null -D - https://webui.aitherdev.int.vpsfree.cz/`
    and `curl -k -s -o /dev/null -D - https://api.aitherdev.int.vpsfree.cz/`
    - Both returned HTTP 200.
  - `nix develop ..#api -c bundle exec rubocop lib/vpsadmin/api/resources/incident_report_rule.rb spec/api/resources/incident_report_rule_spec.rb models/incident_report_rule.rb models/incident_report_rule_matcher.rb db/migrate/20260614160000_add_incident_report_rules.rb`
    - Passed, 5 files inspected, no offenses.
  - `nix develop .#vpsadmin -c php-cs-fixer fix --dry-run --diff --config=.php-cs-fixer.dist.php webui/forms/incidents.forms.php webui/pages/page_incidents.php`
    - Passed, no files needing changes.
  - `nix develop .#vpsadmin -c bundle exec overcommit --run`
    - Passed, but the PHP fixer mutated unrelated files because the manual
      hook run was not limited to staged files. Those unintended formatter
      changes were manually reverted before commit.
  - `nix develop .#vpsadmin -c git commit -F <tmpfile>`
    - Overcommit pre-commit hooks passed during commit. Commit-msg hooks
      passed with line-width warnings only.
- Mandatory change review of vpsAdmin matcher-ordering follow-up range
  `37a9796eacdec1cbdcb521d50226c3768da55c85..891c8461c8063bcc16d0156e9c5ea77fd339fe64`
  found no Blocking, Important, or Advisory findings.
  - Residual risks/test gaps:
    - Browser coverage does not perform an actual TableDnD drag gesture; it
      covers WebUI CRUD/form behavior.
    - Existing dev DBs that already ran the draft migration may still retain
      the old matcher `position` column until reset or manually cleaned up.
- Final WebUI ordering polish implemented on 2026-06-15:
  - Rule drag-and-drop now only allows drops over rows with the same `rule_`
    prefix, preventing dragged rules from being placed below the implicit rule
    or the instruction row.
  - The bundled TableDnD plugin now copies the `onAllowDrop` option into its
    runtime config; the first review found that the original guard was inert
    without this wiring.
  - The implicit-rule and instruction rows keep their `nodrag nodrop` classes
    during hover.
  - Matcher and custom-recipient Add/Save action buttons are wrapped in a
    no-wrap inline action span so `Add` and `Save changes` stay on one line.
  - The support-page Playwright test now asserts that rule footer rows remain
    non-droppable through hover, that the registered TableDnD drop guard
    accepts rule rows but rejects the implicit and instruction rows, and that
    matcher and recipient action buttons use no-wrap styling after rows exist.
- Final WebUI ordering polish commands on 2026-06-15:
  - `php -l webui/forms/incidents.forms.php`
    - Passed.
  - `node --check tests/playwright/webui/specs/support-pages.spec.cjs`
    - Not run in the ambient shell because `node` is not on `PATH`; the
      repository test runner supplied the JavaScript environment instead.
  - `nix develop .#vpsadmin -c node --check tests/playwright/webui/specs/support-pages.spec.cjs`
    - Not run because the `.#vpsadmin` shell also does not provide `node`.
  - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/specs/support-pages.spec.cjs`
    - Passed.
  - `git diff --check -- webui/forms/incidents.forms.php webui/public/template/css/main.css webui/public/js/jquery.tablednd.js tests/playwright/webui/specs/support-pages.spec.cjs`
    - Passed.
  - `./test-runner.sh test 'webui#support-pages'`
    - Passed before the review fix: 1 test script successful in 802.61
      seconds.
    - Passed after wiring `onAllowDrop` and extending the guard assertion: 1
      test script successful in 772.54 seconds.
  - `nix develop .#vpsadmin -c php-cs-fixer fix --dry-run --diff --config=.php-cs-fixer.dist.php webui/forms/incidents.forms.php`
    - Passed, no files needing changes.
  - `nix develop .#vpsadmin -c git commit -F <tmpfile>` and amend rerun
    - Overcommit pre-commit hooks passed during commit and amend. Commit-msg
      hooks passed with a line-width warning only.
  - `dev-clusters/vpsadmin/bin/devcluster update 2026-06-14-vpsadmin-incident-filtering services`
    - Rebuilt and switched the services VM first to the pre-review revision
      and then to amended vpsAdmin revision
      `504f31ee614daf4863b938930c38bd7c2b3cdf14`.
  - `curl -k -s -o /dev/null -D - https://webui.aitherdev.int.vpsfree.cz/`,
    `https://api.aitherdev.int.vpsfree.cz/`, and
    `https://webui.aitherdev.int.vpsfree.cz/template/css/main.css`
    - All returned HTTP 200.
    - The served CSS contains `incident-inline-actions`.
  - `curl -k -s https://webui.aitherdev.int.vpsfree.cz/js/jquery.tablednd.js | rg 'onAllowDrop'`
    - Confirmed the deployed TableDnD asset includes
      `onAllowDrop: options.onAllowDrop`.
  - Mandatory review of pre-amend range
    `891c8461c8063bcc16d0156e9c5ea77fd339fe64..f112468186365a1ac3b86aef0459d2ff2285f556`
    found one Important issue: the TableDnD plugin did not register
    `options.onAllowDrop`, making the new prefix guard inert. The commit was
    amended to fix this before final handoff.
  - Mandatory review of amended range
    `891c8461c8063bcc16d0156e9c5ea77fd339fe64..504f31ee614daf4863b938930c38bd7c2b3cdf14`
    found no Blocking, Important, or Advisory findings.
    - Residual risk: Playwright asserts the registered guard directly and
      checks row classes, but does not perform a real pointer drag with
      multiple rule rows and verify the persisted order. Risk is low because
      TableDnD calls the same guard and the server rejects invalid posted rule
      ID sets.
- Incident rule form/list feedback follow-up implemented on 2026-06-15:
  - Matcher value inputs in rule edit were shortened from size `30` to `27`.
  - `matcher_save` and `recipient_save` now catch HaveAPI validation errors
    locally, render the validation details, and re-render the rule edit form
    instead of leaving the user on an otherwise empty POST action page.
  - Incident report lists no longer render the `Ignored` result column; the
    ignored filter and incident detail field remain.
  - Ignored incident reports in the list use the same `#A6A6A6` row background
    as disabled incident report rules.
  - The WebUI support fixture now includes a deterministic ignored incident
    report for display coverage.
- Incident rule form/list feedback follow-up commands on 2026-06-15:
  - `php -l webui/forms/incidents.forms.php && php -l webui/pages/page_incidents.php`
    - Passed.
  - `git diff --check -- webui/forms/incidents.forms.php webui/pages/page_incidents.php tests/playwright/webui/specs/support-pages.spec.cjs tests/suite/webui.nix`
    - Passed.
  - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/specs/support-pages.spec.cjs`
    - Passed.
  - `nix-instantiate --parse tests/suite/webui.nix >/dev/null`
    - Passed.
  - `./test-runner.sh test 'webui#support-pages'`
    - Passed: 1 test script successful in 760.32 seconds.
  - `nix develop .#vpsadmin -c php-cs-fixer fix --dry-run --diff --config=.php-cs-fixer.dist.php webui/forms/incidents.forms.php webui/pages/page_incidents.php`
    - Passed, no files needing changes.
  - `nix develop .#vpsadmin -c nixfmt --check tests/suite/webui.nix`
    - Passed when run by itself.
    - The first attempt was run in parallel with another `nix develop` command
      and failed while the shell populated `.gems`; see
      `notes/vpsadmin/2026-06-15-parallel-nix-develop-bundler-race.md`.
  - `nix develop .#vpsadmin -c git commit -F <tmpfile>`
    - Overcommit pre-commit hooks passed during commit and amend. Commit-msg
      hooks passed with a line-width warning only.
  - Mandatory review of pre-amend range
    `504f31ee614daf4863b938930c38bd7c2b3cdf14..c54748e84192a08b615761ecbba56f22727d132c`
    found one Important issue: `rule_new` still let first custom recipient
    validation errors bypass local rendering and could leave behind the
    already-created rule. The commit was amended to catch HaveAPI base errors
    around first-recipient create, delete the temporary rule, and locally
    render validation errors for `rule_new`.
  - After the review fix:
    - `php -l webui/pages/page_incidents.php && php -l webui/forms/incidents.forms.php`
      passed.
    - `git diff --check -- webui/forms/incidents.forms.php webui/pages/page_incidents.php tests/playwright/webui/specs/support-pages.spec.cjs tests/suite/webui.nix`
      passed.
    - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/specs/support-pages.spec.cjs`
      passed.
    - `nix-instantiate --parse tests/suite/webui.nix >/dev/null` passed.
    - `./test-runner.sh test 'webui#support-pages'` passed: 1 test script
      successful in 929.88 seconds.
    - `nix develop .#vpsadmin -c php-cs-fixer fix --dry-run --diff --config=.php-cs-fixer.dist.php webui/forms/incidents.forms.php webui/pages/page_incidents.php`
      passed.
    - `nix develop .#vpsadmin -c nixfmt --check tests/suite/webui.nix`
      passed when rerun by itself.
  - A second mandatory review of the amended range
    `504f31ee614daf4863b938930c38bd7c2b3cdf14..b2c7b645e8250fbe85ecec9c58d100b2342c787d`
    found one advisory test weakness: the invalid Add rule regression test did
    not fill a unique label before checking that no temporary rule was leaked.
    The commit was amended to fill
    `webui-playwright-invalid-incident-rule` before submitting and to assert no
    row with that label exists after validation fails.
  - After the advisory test fix:
    - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/specs/support-pages.spec.cjs`
      passed.
    - `git diff --check -- tests/playwright/webui/specs/support-pages.spec.cjs`
      passed.
    - `./test-runner.sh test 'webui#support-pages'` passed: 1 test script
      successful in 761.86 seconds.
  - Final mandatory review of
    `504f31ee614daf4863b938930c38bd7c2b3cdf14..c367fcd127e6b2bef627aeccc9711e67b0f4cf6d`
    found no blocking, important, or advisory findings. The only noted
    residual risk is that invalid inline updates are not separately asserted;
    they use the same `matcher_save`/`recipient_save` validation catch blocks
    as the covered invalid inline add paths.
  - `dev-clusters/vpsadmin/bin/devcluster update 2026-06-14-vpsadmin-incident-filtering services`
    - Passed. Services host switched to the new vpsAdmin closure, restarted
      API/WebUI-related services, and refreshed node runtime state.
  - `dev-clusters/vpsadmin/bin/devcluster status 2026-06-14-vpsadmin-incident-filtering`
    - Reported `status: running` and `ready: yes`.
  - `curl -k -s -o /dev/null -D - https://webui.aitherdev.int.vpsfree.cz/`
    - Returned HTTP 200.
  - `curl -k -s -o /dev/null -D - https://api.aitherdev.int.vpsfree.cz/`
    - Returned HTTP 200.
- Incident matcher table layout follow-up implemented on 2026-06-15:
  - The matcher table now keeps `Save changes` in its own `New matcher:`
    separator row when existing matchers are present.
  - The add-new-matcher row now contains only `Add` in the action column.
  - Rules with no matchers continue to show the existing no-matchers message
    and do not show `Save changes`.
  - Playwright coverage now checks that `Save changes` is absent before any
    matcher exists, appears in the `New matcher:` row after a matcher exists,
    and is absent from the final add row.
- Incident matcher table layout follow-up commands on 2026-06-15:
  - `php -l webui/forms/incidents.forms.php`
    - Passed.
  - `git diff --check -- webui/forms/incidents.forms.php tests/playwright/webui/specs/support-pages.spec.cjs`
    - Passed.
  - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/specs/support-pages.spec.cjs`
    - Passed.
  - `./test-runner.sh test 'webui#support-pages'`
    - Passed: 1 test successful in 878.59 seconds; script completed in
      650.08 seconds.
  - `nix develop .#vpsadmin -c php-cs-fixer fix --dry-run --diff --config=.php-cs-fixer.dist.php webui/forms/incidents.forms.php`
    - Passed, no files needing changes.
  - `nix develop .#vpsadmin -c git commit -F <tmpfile>`
    - Overcommit pre-commit and commit-msg hooks passed.
  - Mandatory review of
    `c367fcd127e6b2bef627aeccc9711e67b0f4cf6d..9a8a3f435d7397e0531088924853343d0933c71d`
    found no blocking, important, or advisory findings. The only noted
    residual risk is that the empty action cell is not explicitly asserted and
    multiple matcher rows/admin rendering are not separately covered; they use
    the same server-side form renderer.
  - `dev-clusters/vpsadmin/bin/devcluster update 2026-06-14-vpsadmin-incident-filtering services`
    - Passed. Services host switched to the new vpsAdmin closure and
      restarted API/WebUI-related services.
  - `dev-clusters/vpsadmin/bin/devcluster status 2026-06-14-vpsadmin-incident-filtering`
    - Reported `status: running` and `ready: yes`.
  - `curl -k -s -o /dev/null -D - https://webui.aitherdev.int.vpsfree.cz/`
    - Returned HTTP 200.
  - `curl -k -s -o /dev/null -D - https://api.aitherdev.int.vpsfree.cz/`
    - Returned HTTP 200.

## Results

- Existing OOM report rule implementation provides a useful local pattern:
  per-resource rules, ignored saved reports, deciding rule link, and hit
  counter.
- Incident reports currently have two relevant delivery paths:
  - mailbox/parser path through `VpsAdmin::API::IncidentReports::Handler`,
    which sends immediately through `IncidentReport::Send`;
  - direct/admin and pending task path through `IncidentReport::New` and
    `IncidentReport::Process`.
- PROKI handling lives in `vpsfree-cz-configuration`, not in the vpsAdmin repo.
  The parser creates `IncidentReport` rows from zipped CSV attachments.
- The per-report `allow_filtering` flag is the clean compatibility boundary.
  It avoids relying on mailbox identity and lets admins explicitly control
  behavior for created reports.
- vpsAdmin focused specs, endpoint coverage, CI selection tests, syntax checks,
  and Overcommit hooks pass locally.
- vpsfree-cz-configuration parser specs, syntax checks, and Overcommit hooks
  pass locally.
- vpsAdmin dev cluster for the initiative was stopped on 2026-06-15:
  - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`
  - API: `https://api.aitherdev.int.vpsfree.cz/`
  - Mailpit: `https://mailpit.aitherdev.int.vpsfree.cz/`
  - Admin login: `test-admin` / `testAdminPassword`
  - User login: `test-user1` / `testUser1Password`
  - `dev-clusters/vpsadmin/bin/devcluster stop 2026-06-14-vpsadmin-incident-filtering`
    completed by killing the cluster after its shutdown timeout.
  - `dev-clusters/vpsadmin/bin/devcluster status 2026-06-14-vpsadmin-incident-filtering`
    reported `status: stopped` and `ready: stale`.

## Open questions

- None currently blocking.
- The implementation sets `allow_filtering: true` for all automated abuse
  notice parsers in the configuration repo, not just PROKI.
- Ignored reports remain visible in incident history and are not excluded from
  daily summaries or metrics by this change.
- Final API names used:
  - `allow_filtering`
  - `ignored`
  - `incident_report_rule`
  - nested `incident_report_rule.matcher`
  - nested `incident_report_rule.recipient`

## Cleanup

- Worktrees should be removed after the feature is merged or abandoned.
- Dev cluster has been stopped; start it again only when more manual testing is
  needed.
- Preserve `plan.md` and `state.md`; archive if useful.
- Before any commits, enter the appropriate Nix shell and install/activate the
  declared hook framework. Do not commit while Overcommit is unavailable.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
