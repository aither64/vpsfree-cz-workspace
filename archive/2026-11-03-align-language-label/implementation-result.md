# Implementation result

The bounded alignment fix is committed and locally checked. It awaits the
lead's review-readiness acceptance and independent final review. Nothing was
published, merged or deployed. Lead retains plan/state ownership.

## Repository and complete history

- Repository: `git@github.com:vpsfreecz/haveapi.git`, target `master`.
- Branch: `2026-11-03-align-language-label`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-align-language-label/haveapi`.
- Original new-branch base and current fetched `origin/master`:
  `f29c1e4675bc1f79641faa619b8c68ecec923c71`.
- Final head: `b606b4b3c32bf05779c05babeaa1c31a33dee6fa`.
- Complete base-to-head inventory: one commit,
  `b606b4b3c32bf05779c05babeaa1c31a33dee6fa servers/ruby: align documentation language label`.
- Complete diffstat: `servers/ruby/lib/haveapi/public/css/documentation.css`,
  one insertion and one deletion. No superseded approaches or transitional
  commits remain; no dependency/pin streams changed.
- No migrations. No schema, persistence, API, protocol, client or configuration
  changes. No release, deployment or external consumption of this feature.
- Final worktree is clean. Registration records the exact original base.

## Cause and fix

The later `.docs-sidebar label { margin: .6rem .5rem; }` rule has the same
specificity as the former `[data-documentation-language] label` rule. It wins
by source order and adds the horizontal indentation visible in the supplied
screenshot.

The existing component rule now selects
`.docs-sidebar [data-documentation-language] label` and sets
`margin: 0 0 .4rem`. Its greater specificity keeps horizontal margins at zero
and restores the component's intended bottom spacing. Language consequently
shares the settings content's left edge with Theme and the select. No markup,
label association, translation, JavaScript or other control changed. The
external screenshot was inspected in place and never copied into Git.

## Quick checks and setup

All commands below exited 0 on the final CSS content:

- From repository root: `nix develop .#server-ruby -c make doc`.
- From `servers/ruby`: `nix develop .#server-ruby -c bundle exec rspec spec/documentation/language_settings_spec.rb`:
  9 examples, 0 failures, seed 7934. Existing coverage checks localized native
  forms, label/select association, ordering above Theme, and language submission.
- From root: `nix develop -c bundle exec rubocop servers/ruby`:
  206 files inspected, no offenses.
- `git diff --check` before commit and for the complete base-to-head range.
- Commit through `nix develop -c git commit -F /tmp/2026-11-03-align-language-label-commit-message`:
  required HaveapiI18n pre-commit hook passed; SingleLineSubject, TextWidth and
  TrailingPeriod commit-message hooks passed. No hooks were bypassed.

The first `dev-session worktree add` fetched over SSH and created the new
branch/worktree at the recorded base, then its post-checkout hook rejected a
stale Overcommit configuration signature. Retrying the public command with
`--no-fetch` registered the existing checkout and preserved its exact base.
After reading `.overcommit.yml` and custom hooks, ran
`nix develop -c bundle exec overcommit --install` and
`nix develop -c bundle exec overcommit --sign`, both successfully.

Only repository-declared root/server bundle preparation was needed. A fresh
Luna/low watcher ran that uncertain-duration batch under the installed and pinned
catalog policy; both Nix shell preparations passed in 106 seconds. See
[setup result](nix-prepare-result.md); the raw log is disposable.

## Documentation and remaining verification

Read repository `AGENTS.md`, `doc/agent-instructions/development.md`,
`doc/agent-instructions/documentation.md`, `README.md`, and
`doc/en/documentation-ui.md`, including the documentation-language and theme
behavior. Checked the shared brand template, stylesheet and existing settings
spec. No project documentation update is useful for a cosmetic margin fix;
diagnosis and temporary verification belong in this session record.

Independent final review remains with reviewer0 through the lead. No new test
harness was added. No rendered browser geometry check was performed: browser
tooling was unavailable in the ambient environment, and dependency expansion
was unnecessary for this bounded fix. CSS inspection establishes the margin
correction; the existing spec verifies preserved markup and native submission.
Publication and applicable CI remain after the lead accepts the review packet.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-align-language-label/)
