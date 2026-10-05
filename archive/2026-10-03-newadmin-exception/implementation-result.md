# API implementation result

Status: original OAuth fix remains committed and independently reviewed. The
bounded API Specs timeout follow-up is separately committed and quick-verified,
with all applicable hooks passing in the lead's socket-capable execution.
The lead reports independent review passed all affected lanes and the complete
series without findings, and published exact head `f9beb46e` over SSH. API Specs
run `37151153953` at that exact head remains under lead verification.

## Ownership and revisions

- Session verified from its tracking directory with `dev-session current`:
  `2026-10-03-newadmin-exception`.
- Both `DEV_SESSION_SLUG` and `DEV_SESSION_WORKSPACE` were absent; the trusted
  developer binding supplies the matching session and workspace identity.
- Assigned API worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-newadmin-exception/vpsadmin`.
- Branch: `2026-10-03-newadmin-exception`.
- Base: `148ef0eaed0459c825f1ba94b8dad2b9f3311b2f`.
- Original auth-fix head: `af8a97670293f4aa9a57e3196ac263c9c9530644`.
- Current final head: `f9beb46e5206864bca9d37672e1419cf03661467`.
- Current subject: `ci: allow 60 minutes for API spec topics`.
- The initial auth fix finished with a clean worktree/index. At the workflow
  review checkpoint, tracked worktree/index were clean and preexisting
  untracked watcher `work/` logs were preserved and unstaged. The lead later
  verified the same-session capture and relocated it intact into canonical
  tracking `api-ci-completion-original-capture`, preserving all evidence and
  source/ref content. The lead reports current entire API Git status clean.
  The original review's untracked-log observation remains historical and valid;
  see [observer evidence placement](state.md#observer-evidence-placement).
- Worktree started clean. API source/spec directories and this report directory
  are writable. Lead plan/state/portal and architect design remain lead/architect
  owned.

## Changes

`api/lib/vpsadmin/api/operations/user_session/resume_oauth2.rb` captures
`oauth&.single_sign_on&.token` once and extends only a present token with expiry
earlier than the renewed access token. The source comment records the retained
authorization link and deliberately absent token after SSO closure. Existing
denials, access renewal, refresh and present-token expiry policy are preserved.
No schema, protocol, public API, client or deployment interface changes occur.
The concise source comment is the smallest useful project documentation update:
it keeps the retained tokenless-SSO invariant beside the code that must honor it.
No separate guide is needed for this bounded correction of an existing state.

Regressions are confined to existing files:

- `api/spec/models/operations/user_session/resume_oauth2_spec.rb`: persisted SSO
  closure, closure of a shared SSO, later expiry preservation, extension of an
  expired but present token, missing authorization/SSO, fixed access expiry,
  expired access denial and closed access-session denial.
- `api/spec/lib/vpsadmin/api/authentication/oauth2_config_spec.rb`: actual expiry
  cleanup with valid refresh authority, refresh, then access authentication;
  checks persisted session/current context, access renewal, retained SSO link,
  deleted expired tokens, and no recreated SSO token.

New examples use deterministic timestamps and synthetic credentials, without
sleeps. The lifecycle example captures cleanup stdout with RSpec's output
matcher so generated fixture tokens are not emitted in successful test logs.
Existing denial and account examples remain unchanged. No new spec files or CI
selection changes are needed.

## Verification and environment

- `git diff --check`: passed.
- Lead reported successful API/root/configuration Nix shell initialization.
- This member's `nix develop -c ...` fails immediately because the sandbox
  refuses the Nix daemon socket: `Operation not permitted`. The lead supplied
  cached output from the exact repository `nix print-dev-env --offline` shells;
  sourcing it in `bash --noprofile --norc` executes the declared environment and
  its shell hook. These prepared scripts already evaluate `shellHook`; an extra
  evaluation is unnecessary. No member HOME/BASH changes or hook bypass used.
- Touched-file `bundle exec rubocop`: 3 files, no offenses, exit 0, in the
  prepared API shell. The sandbox prevents the default home cache write;
  RuboCop continues successfully without that cache.
- Reviewed Overcommit configuration signed; standard hooks installed and
  reviewed PreCommit plugin signatures updated through the prepared root shell.
  Listed required RuboCop, API/WebUI i18n and MigrationSpecs checks are enabled.
  The root shell's unconditional Bundler installation attempts a network lookup
  refused by the sandbox, then cached bundle checking and Overcommit succeed.
- The lead's red watcher completed against the unchanged original source:
  3 examples, 3 failures, each `NoMethodError: undefined method 'valid_to' for nil`
  at `resume_oauth2.rb:40`. The cleanup/refresh case reached the intended resume
  call. Evidence: `red-regression-result.json` and `red-regression.log`.
- The lead's green watcher passed all three assigned suites: 72 examples,
  0 failures, exit 0, 77 seconds. Evidence: `green-regression-result.json` and
  `green-regression.log`. Original account/session denial coverage passed.
- Hook-managed commit attempted after lead release through the prepared root
  shell, with only the three assigned files staged and a wrapped temporary
  message file. Nixfmt, MigrationSpecs, WebUI i18n and RuboCop passed. API i18n
  failed with `Errno::EPERM: Operation not permitted - socket(2)` when its
  runtime catalog invoked the isolated database setup (`tools/test_db.rb:414`).
  Commit-message checks were not reached and that attempt created no commit.
- The lead then executed the prepared, unchanged staged content and temporary
  message through the same declared root shell with local socket access.
  Mandatory PreCommit checks all passed: Nixfmt, MigrationSpecs,
  VpsadminWebuiI18n, VpsadminApiI18n and RuboCop. Commit-message hooks also passed;
  TextWidth gave an advisory about a line over 72 characters that meets the
  workspace's 80-character limit. No hooks were bypassed. This resolved an
  execution-permission limitation only; application source/tests remained
  implementer-owned and unchanged from the green run.
- Final `git diff --check <base>..<head>` passes. Final diff is exactly the three
  assigned paths: 198 insertions, 4 deletions.

## Complete branch inventory

The complete base-to-head series now contains two coherent commits in order:

1. `af8a97670293f4aa9a57e3196ac263c9c9530644`:
   `api: preserve OAuth access after SSO closure`, containing the presence
   guard, invariant comment and two existing spec-file updates above.
2. `f9beb46e5206864bca9d37672e1419cf03661467`:
   `ci: allow 60 minutes for API spec topics`, containing only the two job
   timeout fields. Its exact parent is the preserved original auth-fix hash.

The complete final diff contains those three API source/spec paths and
`.github/workflows/api-specs.yml`. Final base-to-head diff-check passes, and the
index/ tracked worktree are clean. There are no
superseded approaches, follow-up fix commits, compatibility paths, schema
changes or migrations. No migration lineage or deployment conversion is needed.
Mixed API versions can read the same state; old workers can still raise the
original exception until replaced. Software rollback requires no data change
and restores the original defect.

Red command from the API repository root (the shell enters `api/`):

```sh
nix develop .#api -c bundle exec rspec \
  spec/models/operations/user_session/resume_oauth2_spec.rb \
  spec/lib/vpsadmin/api/authentication/oauth2_config_spec.rb \
  --example 'resumes after SSO closure' \
  --example 'resumes another valid authorization' \
  --example 'authenticates refreshed access after expired access and SSO cleanup' \
  --format documentation
```

## Next steps and limits

The original implementation passed independent review and was published by the
lead. The committed timeout follow-up passed independent review and is
published; an updated exact-head API Specs workflow result remains required.
The subsequent exact API configuration repin is lead-coordinated.
No push, configuration edits, integration, deployment or session lifecycle action
has occurred within this assignment. No design deviation has been made. The
only execution deviation was the lead's hook-managed Git commit after the
member-local socket refusal, described above.

## Bounded workflow timeout follow-up

The user requested increasing the timeout to 60 minutes after the full-platform
API Specs job hit the existing 45-minute cap. The lead assigned a direct small
implementation brief, preserving the original authentication fix commit.
Identity/current and retained ready `workspace_write` access were reverified
before acting. Unchanged workspace guidance and documentation/session procedures
were reused; API AGENTS, development/testing procedures and active hook content
were reread.

Only `.github/workflows/api-specs.yml` changes: `api-specs-full` and
`api-specs-core` each have `timeout-minutes: 60` instead of `45` (2 additions,
2 removals). Topic coverage retains `10`. Matrices, patterns, aliases, imported
actions, steps, application source and runtime specs are unchanged. No separate
design or project guide is necessary for this two-field CI policy adjustment;
the workflow values define the policy and this report records the reason.

Known quick checks in the declared cached root environment passed:

- Ruby/Psych safe YAML parse with aliases enabled.
- Parsed structural comparison against HEAD, allowing exactly the two timeout
  changes and proving every other workflow field unchanged; explicit topic
  coverage and shared matrix-alias checks.
- `git diff --check` and staged diff checks; temporary commit message lines
  satisfy the 80-character limit.
- Active executable precommit hooks; reviewed standard Overcommit config
  signature and custom plugin signature checks pass, with no plugin changes.

The lead separately verified official imported action refs as current and
compatible: checkout `v7` (latest `v7.0.1`), upload-artifact `v7` (latest
`v7.0.1`), download-artifact `v8` (latest `v8.0.1`), and setup-ruby rolling
branch `v1` (current version tag `v1.327.0`). No action ref was changed.
The lead also fetched upstream and confirmed API master remains the recorded
base and configuration master remains `7e32833aca1cb65902b50f61eb76dd1022691591`.

One mandatory hook-managed commit attempt stopped with exit 1: Nixfmt,
MigrationSpecs and WebUI i18n passed; API i18n failed with `Errno::EPERM` while
opening the isolated database socket at `tools/test_db.rb:414`. RuboCop was
normally nonapplicable to the YAML-only path. Commit-message checks were not
reached. No hook was bypassed, no retry made, and no commit was created by the
member. The staged single path and wrapped temporary message are delivered for
the lead's socket-capable dependent execution:

```sh
source /tmp/newadmin-exception-root-dev-env.sh
git commit -F /tmp/newadmin-exception-timeout-commit-message.txt
```

The lead subsequently executed that unchanged prepared content/message with
socket-capable access and all hooks active. Commit
`f9beb46e5206864bca9d37672e1419cf03661467` succeeded: Nixfmt, MigrationSpecs,
VpsadminWebuiI18n and VpsadminApiI18n all passed; all applicable precommit
checks passed. Commit-message TextWidth, SingleLineSubject and TrailingPeriod
passed; all applicable commit-message hooks passed and execution exited 0.
The command sourced the cached root environment once and used
`git commit -F /tmp/newadmin-exception-timeout-commit-message.txt`. No
application edit was taken over and no hook was bypassed.

Current complete committed series is base
`148ef0eaed0459c825f1ba94b8dad2b9f3311b2f` through
`f9beb46e5206864bca9d37672e1419cf03661467`: the preserved original auth fix
followed by the separate workflow policy commit, as inventoried above.
There are no migrations, schema/state changes, obsolete implementation
approaches or transitional compatibility paths in this follow-up.

No runtime specs were rerun for the unchanged source; no runtime change follows
the prior 72-example/zero-failure evidence. Actual timeout behavior will be
verified by API Specs at the new exact head. Per the lead's current
user-direction account, default-branch integration of both repositories is
conditional on that updated exact-head workflow succeeding; integration CI is
explicitly unawaited, and deployment remains user-owned. This implementer has
not pushed, changed configuration, integrated branches, deployed or performed
any session lifecycle operation.

Stable session URL:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-newadmin-exception/>
