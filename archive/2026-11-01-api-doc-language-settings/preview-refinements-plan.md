# Nov 2 browser acceptance preparation

Status: exact reviewed ef4c0cdc candidate acceptance passed; see
[candidate receipt](preview-nov2-candidate.md). After the lead's final release,
the exact ef4c0cdc preview is now live; see [live receipt](preview-nov2-live.md).

Scope follows `design.md` section “Three UI/example refinements after 51047”.
Implementer0 owns all project source/tests/commits. Implementer2 changed only
session-local acceptance helpers and notes. A separate authorized loopback
candidate was launched after review release; no project source, index, dependency,
host, live-service, lifecycle or cleanup operations were performed.

[preview_refinements_check.cjs](preview_refinements_check.cjs) reuses the existing
Playwright/Chromium installation and adds only these bounded cases:

- Native resource/authentication Go singleton: whole detail label/select hidden,
  disabled select retained, hidden scalar `example_detail=simple` occurs exactly
  once in FormData and the submitted URL, page/resource/query/locale retained.
  Switching language to Ruby and applying restores the two-choice detail control.
- JavaScript Ruby Thorough → Go singleton → Ruby Thorough: immediate wrapper
  visibility changes with saved Thorough retained and no page navigation.
- Actual Ruby Basic/token authentication Thorough, initialization and public
  action output: one top-level `require 'haveapi/client'`, a blank line then
  `begin`, constructor/setup inside, and localized token comments in English/Czech.
- Signed-in Settings forms from real application HTML: capability true displays
  Switch user before Sign out in DOM order; capability
  false displays only Sign out. Both states retain POST target and CSRF fields,
  and switch-user form retains `switch_user=1`. No logout form is submitted.

The ordinary preview has no documentation OAuth capability. The accepted
capability evidence is separate:
[preview_account_render.rb](preview_account_render.rb) uses the repository's
existing `DocumentationOAuthFixture` in-process against the supplied exact
successor export. It renders English/Czech real application HTML with the switch
capability true and false. Fixture credentials and cookies remain local/in-process;
only rendered HTML and its local manifest are saved. Chromium opens those files
with JavaScript disabled and inspects DOM/form order. No proxy,
listener, host configuration, invented controls or OAuth service is added.

Prepared commands after release, using the existing unbundled benchmark shell:

```sh
HAVEAPI_PREVIEW_SOURCE_ROOT=/absolute/exact-successor-export \
HAVEAPI_BENCHMARK_GEM_HOME=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-api-doc-language-settings/haveapi/servers/ruby/benchmarks/.gems \
RACK_ENV=production nix-shell /absolute/exact-successor-export/servers/ruby/benchmarks/shell.nix \
  --run 'ruby /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview_account_render.rb /absolute/session-local-account-renders'

/nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview_refinements_check.cjs \
  http://127.0.0.1:14567 /absolute/session-local-results.json \
  /absolute/session-local-account-renders/account-renders.json
```

Node `--check` and Ruby `-c` passed on these helpers. After review release, all
new and retained checks passed on the exact ef4c0cdc candidate. Existing
native/UI/comment/generated-profile harnesses are unchanged and reusable.
The same-service final refresh was executed after the lead's exact-head local/
hosted release and all five bounded live suites passed. Prior source, profile
preload and service recovery are retained; all services remain running.

The optional Playwright style injection into no-JavaScript local account HTML
did not settle. The owned harness was stopped, that optional injection removed,
and an explicit 55-second harness bound added. The accepted DOM/form checks then
passed. The separate exporter initially needed the explicit source Ruby-client
load path, which was added without installing dependencies. These were harness
environment corrections; no product source or product tests were retried.
