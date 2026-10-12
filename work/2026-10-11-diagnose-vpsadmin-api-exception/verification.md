# HaveAPI verification and handoff

Final head: `ed88e2a814b3e1f8bbf85067f84cf64032c20f63`. Branch
`2026-10-11-diagnose-vpsadmin-api-exception` is published and clean. Comparison
base: `feda9518634a89b0ff5724fa32bea3c694deebdc`.

## Changes and acceptance

- Release requires shared-doc generation; the direct server Rake build rejects
  missing/empty required docs without blocking clean Bundler setup.
- Missing JSON schema returns 404 without exception mail; other errors retain
  normal reporting.
- Generated-doc routes and a real extracted gem are covered. Child dependency
  paths survive a Bundler path install; the framework location remains checked
  against the extracted artifact.
- CI prepares docs and selects changes to shared docs/build/workflow inputs.
- Developer guidance describes the build contract. No version bump/migration.

## Local evidence

- Quick checks: 20 focused examples passed, changed-file RuboCop and syntax
  passed; actionlint passed. Required Overcommit hooks passed.
- Review remediation: 3 packaging examples passed with an empty original gem
  home and Bundler-configured vendor/bundle path; changed-spec lint passed.
- Full Ruby server suite: **355 examples, 0 failures** (Ruby 3.3.10).
- Fresh tracked-source fixture: clean build correctly rejected absent generated
  docs; release dry-run's first command is the copy/generation script. After
  `make doc`, extracted-gem packaging specs: **3 examples, 0 failures**.
- Full verification command exit 0; watcher-owned operation took 25 seconds.

Logs remain local outside the tracking commit: quick-checks-final.log,
bundler-path-check-final.log, workflow-lint.log and full-verification.log.
Result/status files record commands, exact revisions and exit statuses.
[Independent review and narrow remediation](review.md) is complete.

## Exact-head CI

All seven triggered workflows passed on the final published head. Server
RSpec passed on Ruby 3.2, 3.3 and 3.4; generation and server specs ran successfully
in every matrix job. CI runs were already completed at the first read, so no
long parent CI wait or monitoring agent was needed.

| Workflow | Conclusion |
| --- | --- |
| [RuboCop](https://github.com/vpsfreecz/haveapi/actions/runs/38228219248) | success |
| [clients/go RSpec](https://github.com/vpsfreecz/haveapi/actions/runs/38228219689) | success |
| [clients/js tests](https://github.com/vpsfreecz/haveapi/actions/runs/38228219316) | success |
| [clients/php PHPUnit](https://github.com/vpsfreecz/haveapi/actions/runs/38228219241) | success |
| [clients/ruby RSpec](https://github.com/vpsfreecz/haveapi/actions/runs/38228219697) | success |
| [i18n health](https://github.com/vpsfreecz/haveapi/actions/runs/38228219441) | success |
| [servers/ruby RSpec](https://github.com/vpsfreecz/haveapi/actions/runs/38228219852) | success |

Structured evidence: [ci-result.json](ci-result.json).

## Delivery boundary

The first deliverable is ready for the user's review, awaiting explicit merge
approval. No default branch integration, HaveAPI 0.29 backport/release, vpsAdmin
dependency update, configuration update or deployment has happened. After user
review, carry out the agreed backport/release and downstream work with required
approvals. The user deploys. No technical blocker remains.

[Review diff](https://github.com/vpsfreecz/haveapi/compare/feda9518634a89b0ff5724fa32bea3c694deebdc...ed88e2a814b3e1f8bbf85067f84cf64032c20f63)

[Stable session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-11-diagnose-vpsadmin-api-exception/)
