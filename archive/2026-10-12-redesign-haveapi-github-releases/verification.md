# Verification and integration

Current outcome, 2026-10-19: HaveAPI `master` and the retained feature ref both
resolve to `c14e7d3158b91c134c2817b489cd29772fc09f82`, independently verified over
SSH after the approved coordinator merge. Integration
`f06835bb-e0ed-4269-91b0-4c9f44f29914` is complete; its merge job succeeded.

The exact merged head passed refreshed quick checks, independent review and full
local component/package checks, followed by all five successful pre-merge Actions.
See [refreshed verification and CI links](merge-verification-summary.md),
[pre-merge review](merge-review.md) and
[integration receipts](integration/f06835bb-e0ed-4269-91b0-4c9f44f29914/summary.md).
No version tag, package publication, PHP mirror write or supported release-line
integration occurred. Real publishing credentials remain first-release checks.

## Earlier verification before rebasing

Previously tested feature head: cb256a87539c4503b70594df6fe04678e1814dfb.
Base: 06865bb847a564fe20e59ea6d72856c2f01a82e3.

Independent final review preceded long verification. The reviewer assessed all
four lanes and the complete two-commit history. Both findings were fixed through
narrow remediations and folded into the owning commits. See [review.md](review.md)
and [the remediation range-diff](review-remediation.range-diff).

## Local checks

A fresh Luna/low utility watcher ran the parent-authored verify-all.sh command
for the exact final SHA. Exit status 0, about 85 seconds including CI monitoring.

- Release metadata and full Ruby lint passed.
- Release-helper specs: 21 examples, zero failures, including run-ID rejection and
  refusal to publish registries when PHP preflight finds a conflict. The focused
  remediation suite also passed under GITHUB_RUN_ID=123.
- Ruby server: 355 examples, zero failures, including extracted-gem documentation.
- Ruby client: 47 examples, zero failures.
- Go client generator: 9 examples, zero failures.
- JavaScript: 43 passing.
- PHP: 51 tests, 144 assertions, passed.
- Clean maintained-package build succeeded. Manifest/source/checksum verification
  passed, the actual npm tarball loaded, and all three extracted Ruby libraries
  loaded with the expected version.
- Workflow lint, shell syntax, local documentation links and Git whitespace passed.
- All intended project commits passed the installed and signed Overcommit hooks.

Evidence: [verification.log](verification.log), verification.status,
verification-wrapper.status and [focused remediation checks](review-fixed-quick.log).
The fixture Ruby exception stack trace exercises the expected error path; the
suite's final result has zero failures.

## GitHub Actions

All five push workflows succeeded on the exact final SHA:

| Workflow | Run |
| --- | --- |
| release | [38277751550](https://github.com/vpsfreecz/haveapi/actions/runs/38277751550) |
| servers/ruby RSpec | [38277752118](https://github.com/vpsfreecz/haveapi/actions/runs/38277752118) |
| clients/js tests | [38277751611](https://github.com/vpsfreecz/haveapi/actions/runs/38277751611) |
| RuboCop | [38277751479](https://github.com/vpsfreecz/haveapi/actions/runs/38277751479) |
| i18n health | [38277751497](https://github.com/vpsfreecz/haveapi/actions/runs/38277751497) |

The release workflow's build/test job succeeded and its publishing job was
skipped, as required for a feature-branch run. No package, version tag or PHP
mirror update was published. See [CI results](ci-results.json) and ci-watch.status.

## Limits and operator setup

On 2026-10-19 the user reported publisher/deploy-key setup configured. The initial
read-only API check found the new `release` environment without required reviewers
or a deployment policy. After the user completed those settings, a follow-up
check verified required reviewer `aither64`, `prevent_self_review: false`, custom
deployment policies enabled and the sole deployment rule `type: tag`, `name: v*`.
The user confirms setup is complete.

Environment-secret names, the `HAVEAPI_RELEASE_ENABLED` repository variable and
PHP deploy-key metadata each returned HTTP 403 with this session's API token.
The activation-variable read was repeated after the final setup confirmation and
still returned HTTP 403. These settings rely on operator confirmation. Registry
trusted-publisher settings, PHP deploy-key push rights and the Packagist webhook
remain first-release checks, described in the repository's release procedure.
The real publishing path needs approval for a specific new version; no dummy
version was published for verification. No remote settings were changed by these
checks, and no project documentation change was needed.

The original pair of patches was rebased unchanged over upstream's Nix pin update
and verified again before the now-completed master merge. No migration or runtime
change is introduced. Previous build artifacts are retained in
`artifacts-cb256a87539c/`; current artifacts and dependency caches remain in the
owned worktree. The disposable PHP test cache was removed after verification.
No development cluster or KB staging was created. The session remains active.
