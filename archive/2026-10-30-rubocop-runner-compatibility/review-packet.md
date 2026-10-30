# Final review packet

User requested diagnosis across managed repositories, then authorized: "ok,
implement the fixes. merge it after verification." Integration targets are
vpsfreecz/vpsadminos → staging and vpsfreecz/security-advisories →
2026-07-13-security-advisory-automation. No PRs or system deployment requested.

## Final deliverable and acceptance

Three existing workflow files only: use quoted Ruby series '3.4', pin the jobs
to ubuntu-26.04, and include vpsadminos RuboCop workflow's own path in both path
filters. Explicit runner selection deterministically verifies the failing OS
on the final workflow, avoiding temporary validation branches/matrices.
Preserve existing commands, caching, permissions and all other trigger behavior.
Project-wide .ruby-version, gem manifests/locks and runtime source unchanged.

All intended changes are committed and local quick checks passed. Real CI
verification is deliberately deferred until this independent final review.
Acceptance after review: final-head RuboCop in both repositories and RSpec in
security-advisories must pass on actual Ubuntu 26.04 with successful Ruby setup,
Bundler and real commands. Merge only those verified final heads.

## Complete ranges and history inventory

Both feature branches: 2026-10-30-rubocop-runner-compatibility.
Worktrees are under /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-rubocop-runner-compatibility/.

| Repository/worktree | Exact base | Exact final head | Complete series and final diff |
| --- | --- | --- | --- |
| vpsadminos | 05201326975fc19d20a545c52f651cce0420dbc9 | 4dfed86538fcfaf7f5b43fdf2afcb2cadd4aa58d | One commit: ci: select available Ruby patches on Ubuntu 26.04; .github/workflows/rubocop.yml +4/-1 |
| security-advisories | e6ceb642878dd97546174217676d9861afc38d4e | 7b6c71807e3c5a41f585fd1d9563e151ada71244 | One commit: same subject; .github/workflows/rubocop.yml and rspec.yml +4/-4 |

Use git log BASE..HEAD and git diff BASE..HEAD for the complete small patches.
One logical CI compatibility fix per repository. No superseded approaches,
fixups, temporary test commits, repeated dependency/channel/input update streams,
generated changes or obsolete compatibility paths. No migrations: none created,
merged, released, deployed or externally consumed by this package. No deployed
boundary or consumer requires intermediate history. Require independent explicit
whole-series, repeated-stream and migration conclusions.

## Quick checks and tooling

- Both final committed diffs pass git diff --check; both worktrees clean.
- Psych YAML parses all three files. Focused structural reversal checks prove
  equality to base after reversing only approved runner/version/trigger changes,
  including string selectors, caching and both self-trigger paths.
- Hooks installed/signed and active; actual pre-commit and commit-msg passed
  on both commits. Tempfile messages and git commit -F used inside Nix shells.
- vpsadminos existing .#osup shell supplies root Gemfile Overcommit bundle without
  incidental default-shell docs dependencies; security-advisories default shell
  used with frozen bundle. No source/tooling changes, kernel or OS builds.
- Official latest action refs/releases and Ruby assets checked. setup-ruby@v1
  is latest v1.335.0/7f797815d8adceb1c412e7abefdd1ab4abc47a5f, observed compatible
  with Ubuntu 26.04. security-advisories checkout@v7 is current major.
  vpsadminos checkout@v6 retained: it already succeeded on the diagnostic Ubuntu
  26.04 run, uses node24, and unrelated major upgrade is outside this fix.
- Exact comparisons captured; remote defaults remained at bases after commit;
  feature refs not published. No CI or claims started. Environment watcher ended.

## Review policy and context

Risk: medium, bounded compatible change in CI configuration across two repositories.
No security boundary, data format/schema, public contract or production runtime
change. Lanes: general, architecture/repetition (workflow logic), scope/proportionality
(medium risk). Reviewer: retained reviewer0, gpt-6.1-sol/xhigh, read_only, thread
01a18dc8-3d4f-7ec3-930d-096bbc70cbea; identity/settings/readiness reverified.

Read mandatory-change-review SKILL.md and all three selected references. Perform
review directly, read-only, without nested reviewers. Report findings and test
gaps without treating proposed CI as already passed.

No runtime deployment order or fleet coordination. A rollback to Ubuntu 24.04
would retain availability of old Ruby 3.4.0; reverting only the Ruby input while
remaining on 26.04 restores the known missing-binary failure. No persistent data
conversion involved. Separate repository commits can be integrated independently.

Documentation checked: both repository AGENTS.md, relevant flake/Gemfile/hook
configuration by implementer, official action documentation/source/assets.
No project prose needed for these self-contained parameters. Session plan.md,
state.md, architect-owned design.md, repository-audit.md and implementation.md
preserve diagnosis, rationale, setup receipts and limits. Reusable components
and public interfaces are unchanged; workflow consumers are the existing hosted
CI jobs only. Changing project-wide .ruby-version or unrelated actions rejected
as broader than necessary; no generalized runner abstraction introduced.
