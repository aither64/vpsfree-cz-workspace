# Component shells and explicit lint paths

In initiative `work/2026-09-13-auth-email/`, `nix develop .#api -c` entered
`api/` automatically. Commands retaining an `api/` prefix failed with missing
files. Use component-relative paths inside the shell; the same applies to
`.#webui`. Corrected syntax and RSpec commands ran successfully.

When passing changed Ruby paths explicitly to RuboCop, include
`--force-exclusion`. Without it the generated `db/schema.rb` bypasses its
normal exclusion and reports thousands of irrelevant formatting offenses.
The corrected command inspected only hand-written files.

Use `bundle exec ruby` for metadata scripts that load YAML in the API shell.
Loading YAML/date before Bundler can activate Ruby's default date 3.4.1 while
the API bundle selects 3.5.1. Running through Bundler avoids this conflict.
The API topic coverage workflow explicitly excludes migration specs because
those run through a separate workflow; local coverage checks must do the same.

The default WebUI browser-test auth origin uses HTTP. Chromium drops the
production Secure device/challenge cookies there, including when launched with
`--unsafely-treat-insecure-origin-as-secure`. A local browser probe confirmed
empty cookie storage in both cases. Cookie-dependent scenarios need HTTPS:
add a test-only certificate to the existing auth virtual host and allow that
certificate in the scenario's browser contexts. Keep production cookies Secure.
The adjusted Nix configuration evaluates and the JavaScript syntax check passes;
full browser validation is recorded in the initiative state.

Run Git operations that invoke Overcommit hooks (including rebase and push)
inside the repository's root `nix develop` shell as well. The ambient shell
reported a changed configuration signature even though the tracked hook
configuration was unchanged. Repeating the rebase in the Nix shell passed
without re-signing or bypassing any hook.
