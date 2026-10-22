# Final committed-deliverable review

Session: 2026-10-12-redesign-haveapi-github-releases
Workspace: /home/aither/workspace/ai/vpsfree.cz
Repository/worktree: worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi
Branch: 2026-10-12-redesign-haveapi-github-releases
Base: 06865bb847a564fe20e59ea6d72856c2f01a82e3 (origin/master)
Head: 1bc5178c378bfb66230d15c8dd9d9c47a0051434

Read workspace AGENTS.md and applicable routes, repository AGENTS.md and
its development/releases procedures. Read the entire mandatory-change-review
skill and all four references in /home/aither/.codex/skills/mandatory-change-review/.
Review directly, read-only, without nested agents. This is final review of the
completed committed deliverable, not a request for advisory design review.

Goal: move releases of the maintained Ruby server, Ruby/JS/PHP clients and Ruby
Go-client generator into GitHub Actions. Exclude Elixir. Keep package identities,
shared VERSION, release branches and existing PHP Composer repository. Update
release docs. The user accepted required-reviewer environment approval and
explicitly directed implementation. No real publication, account changes,
master/release-line integration or version bump has been authorized.

Acceptance: validate source/version/changelog, test/build from clean source in
Nix, preserve exact tested artifacts across reruns, gate publication with required
reviewers, use OIDC for registries and scoped SSH for PHP, verify existing versions
before skipping, finish the GitHub Release only after all destinations succeed,
keep safe build-only validation, and document setup/recovery.

Context: work/<slug>/{plan,state,design}.md. Final diff:
work/<slug>/haveapi-reviewed.diff (the original assignment diff, preserved after
remediation). The current final diff is haveapi-final.diff; narrow fixes and final
heads are recorded in review.md/state.md. Inspect code, commits and docs independently.

Complete base-to-head series:
- aa23f97d8703ade9eb754988aa7b012917465c39
  release: automate maintained packages with GitHub Actions
- 1bc5178c378bfb66230d15c8dd9d9c47a0051434
  docs: describe approved releases and publication recovery

Intended split: first commit is one release implementation with its meaningful
helper specs, Nix tools and required npm repository metadata; second is the
maintainer procedure and entry-point links. No obsolete branch iterations,
fixup commits or repeated update streams exist. No flake.lock or application
library versions changed. No migrations: none merged, released, deployed or
externally consumed in this branch. Require explicit whole-history, repeated-
update and migration conclusions rather than only reviewing the final tree.

Risk classification: high (OIDC/SSH secrets, irreversible registry publication,
and PHP default-branch synchronization). Lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility. Selected retained reviewer0 is ready,
read_only, gpt-6-astra, saved reasoningEffort xhigh; no settings overrides.

Public interfaces/consumers: Makefile commands for maintainers; release.yml for
GitHub Actions; existing RubyGems gems, npm package and Composer PHP mirror for
package consumers. Runtime APIs/protocols, DB state, CLI behavior and downstream
configuration pins are unchanged. The mirror remains the root-layout Composer
publication destination; no independent PHP library work is performed there.

Documentation: doc/agent-instructions/releases.md is the authoritative procedure,
linked from README and AGENTS; development.md lists helper checks. It explains
activation and reviewer configuration, immutable versions, untagged PHP mirror
refusal, asynchronous Packagist indexing, no rebuild after accepted artifact upload,
expired-artifact/manual recovery limits, and the top-level publishing shell's
HAVEAPI_RELEASE_TOOLS_ONLY flag. Code owns the repeatable release behavior;
session records own temporary status and eventual integration evidence.

Notable choices/limits:
- One protected publish job gives one approval for all destinations.
- Tag publication requires HAVEAPI_RELEASE_ENABLED and an actual required-reviewer
  environment. No environment settings or registry trust are changed by this work.
- Only tag pushes publish. Branch/PR and workflow_dispatch runs are build-only.
- Successful original-run artifacts are immutable; reruns reuse them. Early failed
  builds may retry; missing/expired accepted artifacts refuse automatic rebuild.
- All registry conflicts are checked before writes. A missing PHP key fails before
  registry writes. A remaining network/authentication failure may leave partial
  publication; verified receipts permit retry with exactly the original files.
- PHP preserves .github and AGENTS, requires a tagged current master, refuses
  backward versions, creates source-provenance commits/tags, and pushes atomically.
- Dependency versions are resolved per build (existing repo did not commit locks),
  with resolved locks recorded inside the manifest. No reproducible-build claim.
- GitHub action SHAs were verified against latest official upstream releases.
  Added Nix tools: gh, Go, Node24 and OpenSSH. Existing nixpkgs pin retained.
- Local make publish now exits and points to the approved Actions release process.

Quick verification passed before review:
- nix develop: full bundle exec rubocop --parallel --force-exclusion,
  243 files, no offenses; make release-check; make release-test, 19 examples,
  0 failures; bash -n utils/release/build.sh.
- actionlint .github/workflows/release.yml: passed (actionlint 1.7.12).
- Local doc link checks, git diff --check: passed.
- Both commits passed installed/signed Overcommit hooks (i18n and applicable lint).
- PHP specs use disposable local Git repositories and check actual library bytes,
  deletion, preserved metadata, atomic push and replay/conflict refusal.
Evidence: work/<slug>/quick-final.log and actionlint.log.

Long verification has not started. After review, a fresh Luna/low utility will
run full suites, actual package build/smoke checks and branch CI. Live trusted
publishing and Packagist account settings require operator setup and a real
version's separate approval; no dummy registry version will be published.

Return findings by severity with file/line references, lane and concrete impact.
If none, state residual risks/test gaps. Include explicit conclusions for complete
branch history, repeated update streams and migration lineage. Send the report
back to the lead in this same session (lead address), retaining read-only access;
do not edit source, tracking or a review file.
