# HaveAPI A+D implementation evidence

Current checkpoint: independent final review accepted with no findings, and
reviewed head `439beea801df3139b7154283a171f53c68295939` is published on the
SSH feature branch with fresh remote equality. Full CI Ruby RSpec passed across
3.2/3.3/3.4; documentation-assets and PHP-formatting jobs failed before execution
on the unchanged pinned PHP formatter. The missing documentation checks passed
locally in the accepted derived shell; performance and Rust CI also succeeded.
The parent accepted all six original paired native documentation cases in two
separate phases (first case, then remaining five), against the final composed
provider/UI/site fixture. Source/check/native package acceptance is complete;
the reviewed/published source is unchanged. No integration or lifecycle action.
No release, default integration or deployment.

Owner: implementer1. Worktree:
`worktrees/2026-11-26-oauth-dark-theme/haveapi`. Branch:
`2026-11-26-oauth-dark-theme`. Fetched base:
`4c126e3b0ed259b2be18a241a0c4c716046eb816` (origin/master).
The source version and Ruby gem version are `0.32.0`; no release or version
change is authorized. The supported `v0.32.2` release is a separate backport
line, not a literal ancestor. Source server differences from that tag before
this feature are the version/gemspec metadata and a documentation language
label stylesheet change. Other server backports are patch-equivalent by
`git log --left-right --cherry-pick origin/master...v0.32.2 -- servers/ruby`.
The API consumer owns its exact source-gem packaging and behavior proof.

## Environment

The initial default Nix shell failed before its shell hook: pinned
`php83Packages.php-cs-fixer` 3.95.30 contains Symfony 8.1 packages requiring
PHP >=8.4.1, but the declared PHP is 8.3.37. See
[haveapi-root-setup.log](haveapi-root-setup.log). No bundle/setup command ran.
The unrelated PHP package was not upgraded and no source/flake input changed.

The lead accepted this bounded derived shell, with the same locked default
shell and only its unused PHP formatter removed:

```sh
nix develop --impure --expr 'let f = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-26-oauth-dark-theme/haveapi"; in f.devShells.x86_64-linux.default.overrideAttrs (old: { nativeBuildInputs = builtins.filter (p: (p.pname or "") != "php-cs-fixer") old.nativeBuildInputs; })'
```

Fresh lead-owned watcher setup passed, exit 0, in 76 seconds, installing the
root and server bundles, running `make doc`, and installing/signing Overcommit.
See [haveapi-setup-corrected.log](haveapi-setup-corrected.log). No operation
remained running. Subsequent checks and Git operations use that exact shell
with `HAVEAPI_RELEASE_TOOLS_ONLY=1`, which skips repeated dependency setup.
The PHP hook has no applicable PHP files in this package; Ruby hooks remain
enabled. The locked Node is 24.22.2 and Ruby is 3.4.12.

## Checks and corrections

- Initial focused RSpec: 128 examples, 1 failure (9.71 seconds). The failure
  was the new test's asset URL expectation: static assets follow the Rack
  prefix, separately from the API mount. Corrected that assertion and supplied
  the API-mount cookie path explicitly to the head script, so cookie clearing
  does not infer it from static asset URLs.
- One follow-up invocation incorrectly ran server specs from the root and
  failed to load `spec_helper`, with zero examples executed. Corrected the
  working directory to `servers/ruby`, as declared by repository guidance.
- Focused RSpec after correction: 128 examples, 0 failures (10.32 seconds),
  seed 18176. From `servers/ruby` with its own Gemfile:
  `bundle exec rspec spec/authentication/oauth2_spec.rb spec/documentation/oauth_spec.rb spec/documentation/oauth_fixture_spec.rb`.
- The JavaScript documentation controls test passed with the locked Node:
  `node servers/ruby/spec/client_examples/assets/documentation_test.cjs`.
  It covers returned auto mode, preserved example preferences, cookie path and
  clearing, ignored invalid enum, denied storage, existing media-change behavior,
  and login target validation.
- Touched Ruby syntax and `git diff --check` pass. RuboCop's initial style
  findings were corrected; five files passed with no offenses.
- A follow-up added independent return-capability handling when the optional
  initial theme is absent, plus actual click/auxclick/switch-form JavaScript
  tests. A test run overlapped a local Ruby/template localization refactor and
  observed mixed old/new source (one failure); it is not accepted evidence.
  With source held unchanged, the final D batch passed 105 examples, no failures
  (9.92 seconds), seed 17694, and the JavaScript controls test passed.
- Provider A committed as
  `1046a14f2f0485f460b3918098e5bc078a3da758`. Required Overcommit i18n and
  RuboCop checks passed; commit-message hooks passed with one advisory 72-column
  warning. The message stays within the required 80 columns.

Long integration/package/browser checks have not run and remain after final
independent review. No services, production access, deployments or integration
were performed. No database migrations, API action/schema declarations,
generated SDKs or token response fields change.

## Documentation and history

The main-agent writing pass is complete on `doc/en/oauth-theme.md`, the README
link, and additions to `doc/en/{documentation-oauth,documentation-ui}.md`.
The provider contract has one authoritative source in `oauth-theme.md`;
client docs explain persistence, error/retry and rollback behavior. Existing
translated UI messages are reused without locale/catalog changes.

Two logical commits are intended: A provider interface and contract, then D
documentation consumer and tests. No obsolete alternate implementation or
migration history is retained. No release or merge has occurred.

## Final committed review packet

Base `4c126e3b0ed259b2be18a241a0c4c716046eb816`; final local head
`439beea801df3139b7154283a171f53c68295939`.
The worktree and index are clean. Full series:

1. `1046a14f2f0485f460b3918098e5bc078a3da758` — bounded provider hook and
   authoritative theme contract, including GET/SSO and POST specs.
2. `439beea801df3139b7154283a171f53c68295939` — documentation consumer,
   first-paint handoff, errors/retries/switching, tests and client explanation.

Both commits passed required Overcommit i18n/RuboCop precommit checks and
commit-message checks. Commit-message width produced advisory warnings only;
all lines meet the required 80 columns. D's last lint-only alignment correction
was verified by its passing hook. No behavior changed after the passing final
D batch. No superseded commits, repeated dependency/pin/generated update
streams or compatibility paths for abandoned branch iterations remain.
No migrations exist, and nothing was released, deployed or externally consumed.

The complete diff is available locally with
`git diff 4c126e3b0ed259b2be18a241a0c4c716046eb816..439beea801df3139b7154283a171f53c68295939`.
It changes 14 files, 444 insertions and 22 deletions:

- README link and `doc/en/{oauth-theme,documentation-oauth,documentation-ui}.md`.
- `servers/ruby/lib/haveapi/authentication/oauth2/{config,provider}.rb`.
- `servers/ruby/lib/haveapi/documentation_oauth.rb` and
  `public/js/documentation.js`.
- `views/main_layout.erb`, `views/documentation_oauth_error.erb` and
  `views/version_sidebar/authentication_control.erb` (under the same library).
- `servers/ruby/spec/authentication/oauth2_spec.rb`,
  `spec/documentation/oauth_spec.rb` and
  `spec/client_examples/assets/documentation_test.cjs`.

Documentation routing/fidelity:

| Topic / reader | Class / authoritative source | Evidence |
| --- | --- | --- |
| Provider/client theme contract; maintainers | Reference: `doc/en/oauth-theme.md`, linked by README and client article | Config hook/provider specs; no duplicate downstream authoritative contract |
| Docs sign-in, cosmetic handoff, rollback; operators | Existing how-to/reference: `doc/en/documentation-oauth.md` | Pending compatibility, state/error/exchange and cookie specs |
| Theme choice and retained examples; readers | Existing how-to: `doc/en/documentation-ui.md` | JS controls/preferences test; no new translated UI labels |
| This execution and environment failure | Individual evidence here; reusable shell lesson in workspace `notes/haveapi/2026-11-26-root-shell-php-formatter.md` | Watcher receipts/logs; not product behavior claims |

Risk is high because this touches OAuth success responses and pending
transactions. Applicable final-review lanes: general, architecture/repetition,
scope/proportionality and risk/compatibility. The lead owns reviewer selection
and invocation; no independent review has been claimed by the implementer.

Owning public interface is HaveAPI Config's optional
`authorization_response_params(sinatra_params:, oauth2_request:, auth_result:)`.
The vpsAdmin override is package B (implementer0); React/BFF is package C
(implementer2), following `doc/en/oauth-theme.md`. The documentation client is
the same-source HaveAPI consumer. Existing Config subclasses inherit the empty
default. Only the exact theme enum can extend success protocol parameters;
Rack::OAuth2 retains code/state/session_state/response mode/verified redirect.

The docs callback keeps strict unknown/duplicate input rejection except for
the one scalar theme field, applies it only after valid opted-in state and token
exchange, and preserves old pending-cookie records. Error/cancel applies the
initiating mode only. Authenticated cookies, API credential isolation, PKCE,
origin/CSRF/replay checks and clean validated destinations remain unchanged.
The 120-second cosmetic cookie is host-only, API-mount scoped and explicitly
cleared by the head script using its server-supplied cookie path; this path is
independent of the Rack/static asset prefix. LocalStorage denial retains state
in memory. Native screenshot/first-paint and end-to-end provider checks remain
post-review gaps; no production behavior was certified.

Publication is intentionally pending final independent review. The SSH remote
is `git@github.com:vpsfreecz/haveapi.git`; pushing this branch starts full server
RSpec and all-branch endpoint-performance workflows, so it must follow that
review under the lead's sequencing instruction. No remote-head equality exists
yet. The source metadata stays 0.32.0; the API owner must pin this exact source
honestly rather than claim a new package release or v0.32.2 ancestry.

## Prepared post-review checks (not run)

Source remains frozen at `439beea801df3139b7154283a171f53c68295939` during
independent review. Exact current input hashes:

| Input | SHA256 |
| --- | --- |
| `flake.lock` | `92ea97bc7d2089b09f408738f3b0b13dc25c1f450d2d03a75706214c97a714bd` |
| ignored root `Gemfile.lock` | `acd4023331a0f379ddf512c41b0d23539ec57a0e7daa515cb17eef68237a9f69` |
| ignored server `Gemfile.lock` | `7af4b1371d402eeb4d699983014192cc355c79dd53e9bea7b5a368b36189ea49` |
| `clients/js/package.json` | `1eb69570e525cd70cd8a9142efeac4c43216c21714592689ec485290867ebfce` |

The JavaScript dependency directory/ignored lock is not prepared yet. Its
first existing-manifest install below must retain/hash the resulting lock in
the check receipt before claiming exact inputs. No source/flake change or
package publication is part of this preparation. Use a fresh lead-owned
verification watcher for this uncertain-duration batch, only after the review
result allows it. Hold the source unchanged while it runs.

### Full documentation check

Canonical cwd is the HaveAPI worktree. Prepared exact command:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --impure --expr 'let f = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-26-oauth-dark-theme/haveapi"; in f.devShells.x86_64-linux.default.overrideAttrs (old: { nativeBuildInputs = builtins.filter (p: (p.pname or "") != "php-cs-fixer") old.nativeBuildInputs; })' -c bash -euo pipefail -c 'unset BUNDLE_GEMFILE; npm --prefix clients/js install --no-audit --no-fund; sha256sum clients/js/package-lock.json; make test-documentation'
```

Expected duration: roughly 2–5 minutes with available caches; this is an
estimate, not an automatic timeout. Stop the batch at its first failed command,
report the exact stage/log and diagnose before retry. Reassess at five minutes
if still running, using the watcher's authoritative status; do not kill a quiet
build based on elapsed time alone. Resource waits remain interruptible.

This established target copies documentation, builds public JavaScript
declarations, runs all `spec/client_examples` and `spec/documentation` examples,
then runs the highlighter/tabs/documentation asset consumers. It covers more
than the already accepted focused quick checks. It does not include the
top-level `spec/packaging_spec.rb`, all authentication specs, native pixels,
real provider redirects, or the API consumer's Nix gem assembly. Do not repeat
the focused quick batch just to accompany this result.

### Package and full-server proof without duplicate local extraction

The real shared-documents gem-build/extraction/route spec is
`servers/ruby/spec/packaging_spec.rb`. The default server RSpec CI workflow
already runs it via `bundle exec rspec` from `servers/ruby`, after `make doc`
and JavaScript declaration preparation. Observe that exact published-head run
after review/publication instead of starting a second local generic extraction.
If CI is unavailable, the bounded fallback is the same prepared shell, with
`make doc`, then from `servers/ruby`:
`env BUNDLE_GEMFILE="$PWD/Gemfile" bundle exec rspec spec/packaging_spec.rb`.
That fallback is conditional and must not be run in addition to an accepted
equivalent CI result. Stop on its first failure; expected duration is under a
minute once dependencies are prepared, but use a watcher if unknown.

Package B owns the *actual consumed* source-gem build and installed runtime
proof, including the final HaveAPI source SHA/archive/filelist, source version
0.32.0, dependency graph and Nix output paths. Its one manifest/runtime check
must include `lib/haveapi/authentication/oauth2/config.rb`, the provider hook,
`lib/haveapi/views/documentation_oauth_error.erb`,
`lib/haveapi/public/js/documentation.js`, the matching main layout and
`doc/en/oauth-theme.md` plus existing shared documents. Reuse that exact
artifact's evidence for the downstream package; this HaveAPI package does not
build/extract the same consumer gem independently. The generic CI gem and the
consumer Nix artifact have distinct proof boundaries, not interchangeable
input identities. B's settled exact build command/paths are supplied by its
owner rather than guessed here.

The push-triggered server performance workflow is repository-owned required
CI; observe its existing exact-head run. No optional local timing benchmark or
benchmark harness change is planned for this cosmetic change.

### Shared native browser flow

Coordinate with B's existing API bootstrap, isolated temporary database,
synthetic user and dedicated confidential documentation OAuth client. C owns
Vite/BFF plus the standard local nginx TLS edge and locked Nix Chromium.
Current tentative origins are UI `https://localhost:5188` and auth/docs
`https://127.0.0.1:5189`, with API backend 5190. These are not launch evidence
or final command inputs. No new provider server/browser framework is needed.

Sent B the pre-mount `api.documentation_oauth` configuration interface: fixed
HTTPS callback `<actual API mount>_documentation/oauth/callback`, dedicated
synthetic client/secret, private uniform session-secret material of at least
64 bytes, scope `all`, and switch-user capability only after account selection
is demonstrated. The provider metadata must point to that TLS edge; Ruby's
standard TLS trust must use the owned fixture CA, and API request capacity must
allow callback and token requests concurrently. Origin, CSRF, state and TLS
verification stay enabled. The documentation cookie never authenticates API
actions. B owns the final mount/version/CA/client configuration; do not invent
those inputs.

Sent C the existing selectors and assertions for the shared harness:

- Open `[data-documentation-menu]`; choose
  `button[data-theme-choice="light"|"dark"|"auto"]`.
- Sign in through `a[data-documentation-login]`; preserve validated
  resource/page/fragment while sending preference and exact return capability.
- Start dark, select light on the real provider and verify successful return
  before first paint, local mode and removal of `haveapi_docs_theme`.
- Start/return auto; verify auto remains in saved preferences while effective
  `html[data-docs-theme]` follows later emulated OS changes.
- Preseed programming-language/client/detail fields and verify only theme is
  changed; deny localStorage acquisition/read/write separately and verify
  in-memory scheme plus the next outgoing sign-in/switch mode.
- Cancel/fail a callback and verify initiating mode on the styled docs error
  and retry, with no imported response theme and no arbitrary return URL.
- Submit the native logout form containing `input[name="switch_user"]` and
  `[data-documentation-theme]`; preserve CSRF and verify the fresh fixed login.
  Ordinary logout keeps its established destination/revocation scope.
- Capture desktop and narrow/touch screenshots of real rendered provider and
  docs return/error screens in the same batch. The error wrapper intentionally
  has `main.docs-main` without a full `[data-docs]` navigation root.

The exact shared native command is pending B/C's settled harness; this is an
explicit owner dependency, not an executable command or a claimed pass. Append
their final command, fixture source/lock identities, CA and service registration
receipts, expected duration and stopping condition before launch. A watcher
runs the single bounded scenario batch after final review; server registrations
use `dev-session service run` and remain session-owned. No servers or browser
checks have been launched by implementer1.

## Accepted review and SSH publication

The lead reported reviewer0's retained Sol/xhigh final review of the complete
`4c126e3b..439beea8` A+D range: all four lanes, no findings, explicit clean
whole-history/no-migrations/no repeated-stream and documentation-placement
conclusions. The source was held frozen through review. The lead then directed
publication of that exact head only.

Fresh fetch left `origin/master` at
`4c126e3b0ed259b2be18a241a0c4c716046eb816`, an ancestor of the reviewed head.
The hook-bearing SSH push used the accepted derived Nix shell and exited 0.
It created `refs/heads/2026-11-26-oauth-dark-theme` on
`git@github.com:vpsfreecz/haveapi.git`. Fresh `git ls-remote --heads` returned:

```text
439beea801df3139b7154283a171f53c68295939 refs/heads/2026-11-26-oauth-dark-theme
```

Own HEAD matches and the index/worktree are clean. The reachable final exact
source was sent to package B. Source metadata stays 0.32.0. This is branch
publication, not a package release, default-branch integration or deployment.

One bounded initial GitHub API read identified these `push` runs at that exact
head, all attempt 1, created 2026-11-26 12:21:15–16 UTC:

| Workflow | Workflow ID | Run ID | Observed state |
| --- | --- | --- | --- |
| servers/ruby RSpec | 232133445 | [45818857050](https://github.com/vpsfreecz/haveapi/actions/runs/45818857050) | queued |
| clients/go RSpec | 232133443 | [45818856987](https://github.com/vpsfreecz/haveapi/actions/runs/45818856987) | in_progress |
| servers/ruby performance | 395874998 | [45818856879](https://github.com/vpsfreecz/haveapi/actions/runs/45818856879) | in_progress |
| clients/js tests | 232133447 | [45818856634](https://github.com/vpsfreecz/haveapi/actions/runs/45818856634) | in_progress |
| clients/ruby RSpec | 232133446 | [45818856748](https://github.com/vpsfreecz/haveapi/actions/runs/45818856748) | in_progress |
| RuboCop | 230808350 | [45818856623](https://github.com/vpsfreecz/haveapi/actions/runs/45818856623) | in_progress |
| clients/php | 232133442 | [45818856642](https://github.com/vpsfreecz/haveapi/actions/runs/45818856642) | in_progress |
| i18n health | 306702381 | [45818856712](https://github.com/vpsfreecz/haveapi/actions/runs/45818856712) | in_progress |
| clients/rust | 389778279 | [45818856597](https://github.com/vpsfreecz/haveapi/actions/runs/45818856597) | in_progress |
| clients/python | 389932879 | [45818856646](https://github.com/vpsfreecz/haveapi/actions/runs/45818856646) | in_progress |

All observed conclusions were null. These are initial receipts, not terminal
test results. No tests were rerun and no watcher was started by implementer1;
the lead received the exact identities for coordinated observation. The push,
fetch, remote verification and bounded API-read tool sessions all finished.

B additionally confirmed the shared native fixture is prepared and
syntax-checked but not launched: `browser-fixture/server.rb` under this session,
actual API root `/`, pre-mount docs configuration, fixed
`https://127.0.0.1:5189/_documentation/oauth/callback`, real temporary database,
synthetic manifest-owned clients, Puma 8 threads/backend 5190 and standard
fixture-CA TLS trust. C still owns private manifest, proxy and browser runner.
The same one provider/fixture will cover docs; no duplicate server was created.

## Bounded terminal CI snapshot and failure diagnosis

At the lead's explicit request, one new snapshot of exact head
`439beea801df3139b7154283a171f53c68295939`, all attempt 1, established:

| Run | Observed conclusion |
| --- | --- |
| servers/ruby RSpec 45818857050 | failure, solely `documentation-assets` |
| clients/php 45818856642 | failure, solely `PHP CS Fixer` |
| clients/js 45818856634 | success |
| clients/go 45818856987 | success |
| clients/ruby 45818856748 | success |
| clients/python 45818856646 | success |
| RuboCop 45818856623 | success |
| i18n health 45818856712 | success |
| servers/ruby performance 45818856879 | in_progress, no conclusion |
| clients/rust 45818856597 | in_progress, no conclusion |

No later status read was made in this turn. The server run's actual full RSpec
jobs all succeeded: Ruby 3.2 job `139905548858`, Ruby 3.3 job `139905549049`,
Ruby 3.4 job `139905548979`. The retained Ruby 3.4 log shows the full
`bundle exec rspec` command, the real `haveapi-0.32.0.gem` build and
**1054 examples, 0 failures**. This covers the complete documentation,
authentication and generic packaged-gem specs rather than only the earlier
focused checks. Package B's actual Nix-consumed artifact proof remains separate.
The server run has no uploaded artifacts (`[]`).

The failed server job `139905548445` stopped while realizing the default Nix
shell, before its highlighter/npm/asset checks. The failed PHP-format job
`139905547497` stopped at the same point. Both logs identify exactly
`/nix/store/8il7dhapszjv3gx9gml937c8brq6lm6z-php-cs-fixer-3.95.30.drv`, builder
exit 2: pinned Symfony 8.1 packages require PHP >=8.4.1, but PHP is 8.3.37.
This is the same source-independent shell failure observed before implementation.
`git diff 4c126e3b..439beea8 -- flake.nix flake.lock .github/workflows` is empty;
the feature did not modify those inputs. No PHP/Nix upgrade or blind workflow
rerun was made.

Actual PHP behavior jobs succeeded: PHPUnit PHP 8.4 `139905547857`, PHPUnit
PHP 8.3 `139905547976` and shipped-source syntax PHP 8.0 `139905547860`.
Do not describe the PHP unit tests as failed based on the aggregate run color.

Retained complete logs and SHA256:

- [Server failed job log](haveapi-ci-server-45818857050-attempt1.log):
  `29ed3fe0aad97a6776cbea09c31e2c9e5bd601976af363bab3693a59c0ccaab8`.
- [Ruby 3.4 full-success log](haveapi-ci-ruby34-139905548979.log):
  `d6496a8f46b253a425ec8e0d891a9eda31b7948e34e7a730d36a5ab4be028dc7`.
- [PHP failed formatter log](haveapi-ci-php-45818856642-attempt1.log):
  `a1a0e1b39ebdfff7789b44e954c1759fd6b7d616cc5fd62184b792abdaa63fce`.

The lead accepted this diagnosis and the full RSpec/generic package proof.
The lead had already launched the planned local `make test-documentation`
batch (outer utility session 7640) when this terminal snapshot arrived. Its
output remains watcher-owned; implementer1 did not inspect it, duplicate it or
request interruption. If that batch passes, it also covers the skipped asset
consumer tests. The only separate CI substep not part of that target is:

```sh
cd utils/highlight
npm ci --ignore-scripts --no-audit --no-fund
npm run check
```

Use the accepted derived shell if the lead schedules that remaining locked
highlighter integrity check, and do not repeat the already-proven full RSpec,
package extraction or asset tests with it. Its exact package-lock SHA256 is
`38ad557892bd08558fb350b3a22f78eed581badb651cb6db20ac449cec146fd7`.
No new local checks or observer were launched by implementer1 in this turn;
all completed-log/API-read tool sessions quiesced. Passing full server CI proves
the source/generic gem suite at this head and CI-resolved inputs, not B's
distinct final Nix-consumed package, native browser paint or a deployed service.

## Documentation acceptance complete and final CI milestone

The lead supplied the completed fresh utility receipt for the exact planned
`make test-documentation` command at
`439beea801df3139b7154283a171f53c68295939`: **exit 0 in 77 seconds**, including
public JavaScript declaration build, **498 Ruby examples, no failures**, and
highlighter/tabs/documentation asset consumer tests. Full log:
[docs-long.log](docs-long.log); result/native receipt:
[docs-long-result.md](docs-long-result.md). Utility outer session 7640 and all
underlying effects were reported quiescent. Its ignored JavaScript dependency
lock SHA256 is
`e0f9b0c6c51b87296076ec6e5052b3cd6d786229d12d9514964497bf5a0f34bf`.
This receipt was accepted without repeating the target or reading its output
alongside the utility.

The declaration build rewrote only tracked generated files beneath
`clients/js/dist/`. Those owned build outputs were restored to the reviewed
head with scoped `git restore --worktree -- clients/js/dist`; no authored source
or index entry was changed. An initial ambient restore's post-checkout hook
reported a signature mismatch after file restoration; the same scoped operation
then passed in the accepted prepared Nix hook environment. The resulting
worktree is clean. No hook was bypassed or source/generator update committed.

Read-only npm cache inspection proved all three necessary highlighter tarballs
present (esbuild 0.28.2, its linux-x64 binary and highlight.js 11.12.0). The one
remaining known-quick substep therefore ran inline in the accepted derived
shell, with no root/server dependency setup and no repeated make/spec/assets:

```sh
cd utils/highlight
npm ci --ignore-scripts --no-audit --no-fund
npm run check
```

It exited 0; npm added three cached packages in two seconds and
`node build.mjs --check` passed. No tracked file changed. Full log:
[highlighter-integrity.log](highlighter-integrity.log), SHA256
`526b733987bf52e069f286931dfc3c658bfa9c5bac7bd606205a694243f75ce3`.
The highlighter package lock remains
`38ad557892bd08558fb350b3a22f78eed581badb651cb6db20ac449cec146fd7`.
The command and all read-only inspection tool sessions finished.

At this completed milestone the lead permitted one new terminal snapshot:

| Workflow / run / attempt | Exact head | Terminal result |
| --- | --- | --- |
| servers/ruby performance / 45818856879 / 1 (workflow 395874998) | `439beea801df3139b7154283a171f53c68295939` | success; updated 2026-11-26 12:27:55 UTC |
| clients/rust / 45818856597 / 1 (workflow 389778279) | `439beea801df3139b7154283a171f53c68295939` | success; updated 2026-11-26 12:25:43 UTC |

These are workflow conclusions; no additional local benchmark or CI retry ran.
All exact-head CI workflows now have terminal receipts. The two aggregate reds
remain failed environmental jobs, with the applicable skipped documentation
steps independently completed against the same reviewed source. This is a
replacement of those test steps in the accepted Ruby/Node shell, not a claim
that the unchanged broken PHP formatter or its entire default shell now builds.
The feature touches no PHP source; its formatter is nonapplicable locally.
The full successful source/generic-gem checks still do not substitute for
package B's actual consumed Nix artifact, the combined native B/C/D browser
flow, screenshot/first-paint evidence or deployment. Those are the remaining
cross-package verification boundaries; no second provider fixture was created.

## Paired native documentation script prepared (not launched)

Own ignored/untracked artifact:
`browser-fixture/docs-acceptance.mjs`, SHA256
`b0fbac804800d57e329bbeb1f6500167c7060c431f786bb413709260843e2ed9`.

### D negative-route fidelity correction before native launch

The lead supplied changed evidence from C's actual browser: Playwright routes
only the first URL of a redirect chain, so a route on the redirected callback
can silently miss the intended fault. Narrow inspection found that same gap in
D's negative `contextRoute` helper. Cancel uses ordinary native form navigation
and its genuine callback/error/retry checks, without interception; it is unchanged.

Only the ignored runner was corrected. It forwards the real original provider
POST with `route.fetch({maxRedirects: 0})`, requires a genuine 302/303 and the
actual code/state/theme fields, changes only state to a different nonce of the
same valid shape, and fulfills the original response with its body/status and
all other headers/cookies preserved. Assertions require exactly one injection,
the actual docs callback's 400 response, unchanged other fields, consumed
pending/no authenticated docs cookie, and initiating dark appearance/retry.
No token response is mocked, and all existing six cases remain.

Final replacement script SHA256:
`4208eb83eba142936a739391013eeea4486d0744ef29ab2aa3e4aecdc7cddec6`.
This supersedes the earlier `b0fb...` launch hash; argv/cwd/env/bound are unchanged.
Syntax passed using the already-existing C Node 24.21.0 executable, and the
installed Playwright interface declarations support the selected options.
The earlier unrooted HaveAPI Node path was absent; no package setup/realization
was performed. No native action, service/data/source modification, suite check
or log polling occurred. Parent launch still waits for Csite terminal handoff;
the first two normal users, clients and SSO remain held unchanged.

### First paired D native result and bounded selector diagnosis

Parent D operation 10315 finished exit 1 in 37 seconds,
2026-11-26 15:26:38–15:27:14 UTC, using exact runner `4208eb83...` and the
accepted final graph. The complete sanitized log is `docs-paired-final.log`.
`captures-docs/results.json` contains only first case
`desktop-choice-return-and-switch`, failed at `provider-theme` with
`TimeoutError`; no screenshot was reached and no D case completed. Later five
cases did not run. The parent reports contexts/browser closed, product sources
unchanged and site branding intact. This is not a native acceptance pass.

Only the relevant existing artifacts, D stage/selector and actual normal
provider control structure were inspected. `startLogin` had already required a
visible real provider username input and exact TLS origin/authorize pathname,
initial theme and return capability before entering `provider-theme`. The page
was therefore reached; the failure is not evidence of client/redirect mismatch.

The runner's outer `.appearance-controls label` used
`filter({has: page.locator('.appearance-controls input[value=...]')})`.
Playwright resolves the inner locator relative to each outer label; that
requires an impossible nested `.appearance-controls` inside the label. The
actual B template has fieldset → label → input/span. Installed Playwright
declarations explicitly describe this relative-scoping rule, and C's passing
site case uses `label:has(input[name="appearance-selection"][value=...])` on
the same widget. This is a deterministic runner-only selector defect.

The cause and smallest strict correction boundary were returned to the lead:
use the exact label/input selector with unique/visible count assertions, retain
all existing theme/return/state/cookie assertions and corrected negative
injection proof. Proposed next parent scope is first failed case only, then
remaining five once, with distinct receipts and no general resume framework.
At this diagnosis checkpoint no runner edit, new authentication, retry, source,
fixture/service/DB/client/user/SSO/branding action or upstream test rerun was
performed. B helper/setup and first two normal users remain held.

### Accepted runner selector correction and explicit parent phases

The lead accepted the unique relative-`has` diagnosis and released only this
ignored-runner correction. The normal selector is now
`.appearance-controls label:has(input[name="appearance-selection"][value="..."])`,
requiring exactly one radio and one visible label before normal native click.
Checked state, HTML appearance, hidden enum and independent return capability
assertions remain. The real B template and C's passing selector establish the
same control mapping; existing C Node 24.21.0 syntax checking passes.

Frozen replacement script SHA256:
`b5f240faf2caa0913a27582e19aa965d1b5363eba3bae3b03edd9622d9c94fc4`.
It supersedes runner `4208eb83...`, without changing product source or any
service/data/client/user/SSO/branding setting. All six original case calls and
the corrected original-POST state-injection proof are retained.

The runner now requires one of two explicit phase values, with no generic
resume/persisted state or framework. `DOCS_ACCEPTANCE_PHASE=first` executes only
the original failed `desktop-choice-return-and-switch` case and requires one
result. `DOCS_ACCEPTANCE_PHASE=remaining` skips only that first case, executes
the remaining five and requires five results. A failed case still stops the
phase. Native JSON includes the phase and expected case count. Distinct
ignored/untracked output directories retain independent receipts and screenshots;
the original 37-second failed receipt remains untouched and means zero passes.

Exact first command, cwd the C worktree:

```sh
env DOCS_ACCEPTANCE_PHASE=first FIXTURE_MANIFEST=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-26-oauth-dark-theme/browser-fixture/private-manifest.json FIXTURE_OUTPUT_DIR=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-26-oauth-dark-theme/browser-fixture/captures-docs-first E2E_CHROMIUM_EXECUTABLE_PATH=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-26-oauth-dark-theme/browser-fixture/nix-chromium/bin/chromium nix develop -c node /home/aither/workspace/ai/vpsfree.cz/work/2026-11-26-oauth-dark-theme/browser-fixture/docs-acceptance.mjs
```

Expected first-phase duration is under 90 seconds once healthy, with the same
15-second action / 25-second navigation limits and first-failure stop. Only
after the parent accepts that first pass, use the identical argv with
`DOCS_ACCEPTANCE_PHASE=remaining` and
`FIXTURE_OUTPUT_DIR=.../browser-fixture/captures-docs-remaining`; expect under
three minutes, stopping on failure. Results are each directory's `results.json`.
These are prepared commands, not execution or pass claims. No owner native
action, source/test-suite rerun or independent service change occurred.

### All original paired documentation cases accepted

The lead supplied and accepted both terminal parent receipts at the frozen
runner SHA256 `b5f240faf2caa0913a27582e19aa965d1b5363eba3bae3b03edd9622d9c94fc4`:

| Phase / parent operation | Actual result | Time / retained evidence |
| --- | --- | --- |
| First only / 53033 | exit 0; `desktop-choice-return-and-switch` passed | 17 seconds, 2026-11-26 15:34:51–15:35:07 UTC; `docs-paired-first.log`, parent result receipt and `browser-fixture/captures-docs-first/results.json` |
| Remaining five / 6674 | exit 0; all five remaining original cases passed | 40 seconds, 2026-11-26 15:36:28–15:37:08 UTC; `docs-paired-remaining.log`, parent result receipt and `browser-fixture/captures-docs-remaining/results.json` |

The remaining phase passed `automatic-mode-follows-system`,
`mobile-cancel-and-retry`, `storage-getter-denied-return`,
`storage-methods-denied-return` and
`mismatched-state-rejects-response-theme`. First-case success was retained
separately and was not repeated in the remaining phase. The original operation
10315 / 37-second selector failure is still a zero-pass failure; it was neither
promoted nor replaced by these receipts.

These were actual composed-runtime checks with reviewed/published HaveAPI
`439beea801df3139b7154283a171f53c68295939`, the parent's accepted final vpsAdmin
provider `913...`, current matched C/E fixture and site branding. B's own exact
source/Nix artifact and full/core consumer receipts remain authoritative for
that component graph; no package was rebuilt or extracted for this record.
The parent accepted the corrected strict widget selector and all unchanged
theme/return/state/cookie assertions. In particular, the final negative case
requires one genuine original-POST state injection, callback HTTP 400, no docs
authenticated or pending cookie, and retained initiating dark appearance. The
successful result therefore includes those strict checks rather than only
navigation or a printed case label.

Accepted first-phase captures are
`captures-docs-first/provider-light-desktop.png` and
`captures-docs-first/docs-light-desktop.png`; remaining-phase captures are
`captures-docs-remaining/docs-auto-dark-desktop.png`,
`captures-docs-remaining/provider-light-mobile.png`,
`captures-docs-remaining/docs-error-dark-mobile.png` and
`captures-docs-remaining/docs-invalid-state-dark-desktop.png`, all beneath the
ignored `browser-fixture/` directory. They come from the actual rendered fixture,
with provider captures before credential fill and documentation captures after
clean return/error. This record reuses the supplied terminal proof without
rereading logs, rerunning cases or claiming an additional image inspection.

Together with the already accepted full server/generic-gem CI, focused/local
documentation and locked highlighter results, these receipts close the prior
paired native boundary for A+D. Existing baseline aggregate CI reds remain
limited to the unchanged PHP formatter dependency failure; applicable skipped
documentation checks passed in the accepted derived shell. This does not claim
that the formatter/default shell itself builds, or that any production service
was deployed. Source commits/history, independent review, published exact head
and no-migration conclusion remain unchanged.

No owner source/runtime/service/user/client/SSO/branding/cleanup or lifecycle
action followed the receipt. Normal users remain protected in their post-D
state. Any later B-only fixture phase needs its own parent binding/fidelity
preflight; D acceptance is not permission for independent fixture mutation.
Implementer1 retains A+D ownership for actual findings/final handoff; no next
package is assigned. Session records and portal remain open.
`node --check` passes. Both the script and output destination
`browser-fixture/captures-docs/` are Git-ignored and untracked. No manifest,
credential, CA, B server, C runner or nginx file was modified by implementer1.
The script reads the existing private manifest at runtime, never prints values
or OAuth URLs, and reports only bounded case/stage/type/pathname metadata.
Malformed manifest input also produces a generic failure without JSON excerpts.

C confirmed minimal direct use of its installed `@playwright/test` through
`createRequire` from the C worktree's package manifest. The script starts and
closes only its own browser/contexts; it never starts or stops shared services.
It uses the standard isolated-fixture HTTPS browser option; actual Ruby/Node
token-exchange TLS validation remains the B/C standard CA setup.

Six sequential cases are prepared:

1. Desktop dark entry → actual provider light choice → validated clean return,
   first visible frame, preserved example preferences, one-shot theme cookie,
   HttpOnly docs-session cookie, and anonymous API `/v7.0/users/current` refusal;
   then native protected Switch user and second fixture identity.
2. Automatic mode remains auto and follows a later OS color-scheme change.
3. Mobile cancellation → styled initiating-dark docs error → validated retry.
4. Denied localStorage acquisition still completes a light return in memory.
5. Denied localStorage methods still complete the same in-memory behavior.
6. Browser-side callback state corruption rejects the returned light theme and
   retains initiating dark appearance. The actual server state check is used;
   no replacement callback response is fabricated.

Screenshots cover actual provider desktop/mobile and docs return/auto/error
views, before credential fill or after clean return. Token-exchange failure is
already covered by the accepted full Ruby suite; no extra server failure hook
or new auth framework was added for that path.

The launch interface, to be frozen with final B/C input/service receipts, is:

```sh
env FIXTURE_MANIFEST=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-26-oauth-dark-theme/browser-fixture/private-manifest.json FIXTURE_OUTPUT_DIR=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-26-oauth-dark-theme/browser-fixture/captures-docs E2E_CHROMIUM_EXECUTABLE_PATH=<C-owned-verified-executable> nix develop -c node /home/aither/workspace/ai/vpsfree.cz/work/2026-11-26-oauth-dark-theme/browser-fixture/docs-acceptance.mjs
```

Canonical cwd is the C worktree. The placeholder is intentionally unresolved:
C's initial eight-test browser launch failed because the earlier reported
Chromium executable path was missing. C owns exact-output/availability/retention
diagnosis; implementer1 will neither launch D nor independently repair/realize
browser tools. B must also finish final review and the single shared
provider/nginx/BFF services must be registered and ready. API root/version are
settled as `/` and 7.0; the auth/docs origin is the existing loopback TLS edge
`https://127.0.0.1:5189`.

Expected scenario duration is under three minutes once the shared fixture is
healthy. A failure stops subsequent cases and writes sanitized results to the
private output directory; the owner diagnoses the exact failed stage before
retry. C and D scripts must run sequentially because they share synthetic
users/SSO/database state. The lead owns service/utility execution sequencing.
This is preparation only, not native browser acceptance evidence. HaveAPI
product source remains reviewed/published `439beea8`, unchanged.

### C-owned rooted browser prerequisite resolved

C reported its corrected setup and same eight C-only cases passed: exit 0,
24.3 seconds of browser execution / 75 seconds total, parent log
`c-browser-rooted.log`. Actual executable, `--version`, executable-bit and
`nix-store --query --roots` proof passed for the stable outlinks:

- `browser-fixture/nix-chromium/bin/chromium` →
  `/nix/store/7d79gfynv59x9lv4dd3n6haqw5kl4jcq-chromium-154.0.8037.57/bin/chromium`.
- `browser-fixture/nix-nginx/bin/nginx` →
  `/nix/store/mff9w3rn0czmiw7k8ff91nvngslxsbmp-nginx-1.30.5/bin/nginx`.

Reuse the owner receipt without duplicate realization/version checks. Roots stay
retained throughout the C/B/D acceptance. The prepared D command now resolves
the earlier executable placeholder as:

```sh
env FIXTURE_MANIFEST=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-26-oauth-dark-theme/browser-fixture/private-manifest.json FIXTURE_OUTPUT_DIR=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-26-oauth-dark-theme/browser-fixture/captures-docs E2E_CHROMIUM_EXECUTABLE_PATH=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-26-oauth-dark-theme/browser-fixture/nix-chromium/bin/chromium nix develop -c node /home/aither/workspace/ai/vpsfree.cz/work/2026-11-26-oauth-dark-theme/browser-fixture/docs-acceptance.mjs
```

Run from the C worktree only after B acceptance, shared registered provider/TLS
readiness and the lead's sequential C→D utility window. C reports auth-edge
aliases are prepared and nginx syntax validation passed, but no combined
provider/proxy/BFF service has launched. Implementer1 has not launched a browser,
repeated setup, or modified source. The D script hash remains
`b0fbac804800d57e329bbeb1f6500167c7060c431f786bb413709260843e2ed9`.
