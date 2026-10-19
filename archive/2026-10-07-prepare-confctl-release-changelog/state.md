---
lifecycle: complete
---

# confctl v3.0.0 release preparation

## Current phase

confctl v3.0.0 released and publication verified. Remote master and annotated
v3.0.0 tag resolve to 1b56616. RubyGems reports version 3.0.0, Ruby >=3.3.0 and
the verified SHA-256; downloading the public gem confirms identical bytes.
Independent review, both local Ruby suites, lint/format, Nix package and isolated
gem CLI passed. Exact-head GitHub RSpec/RuboCop passed. Self-hosted Tests remains
queued under watch_revised_ci; this is remaining CI work. Session stays open and
active for that result, with no lifecycle cleanup authorized.

## Phase checklist

- [x] Verify bound identity/retained roster and inventory changes since v2.2.3.
- [x] Refresh locked dependencies on Ruby 3.3; regenerate gemset with Bundix.
- [x] Add reusable release skill and mandatory AGENTS.md route.
- [x] Finish changelog and all four release identifiers; final version commit last.
- [x] Independent final review of the revised complete branch.
- [x] Verify Ruby 3.3/3.4, Nix package, gem build, isolated CLI and checksum.
- [x] Replace development branch and cancel superseded CI.
- [ ] Complete CI monitoring (RSpec/RuboCop passed; self-hosted Tests queued).
- [x] Receive user approval for confctl master integration/tag/RubyGems publication.
- [x] Execute and verify the approved release.

## Scope and user decisions

User requests prepare v3.0.0 changelog/commit, then wait for approval. Subsequent
instructions: swpins will be removed in v4; update all Gemfile.lock dependencies;
gemset.nix is managed by Bundix; release commit must be latest; preserve future
release instructions as a skill. Preparation initially withheld integration/tag/upload; the user subsequently
approved the release explicitly (recorded below). Refresh keeps existing gem constraints and Ruby >=3.3.0.

Lead owns all investigation, design and edits. Retained reviewer0 remains
read-only, saved gpt-6-astra/xhigh. Utility watcher policy is gpt-6-luna/low,
separate from the roster; no new or reconfigured team member.

## Repositories and complete history

confctl remote: git@github.com:vpsfreecz/confctl.git; default master.
Branch: 2026-10-07-prepare-confctl-release-changelog.
Worktree: worktrees/2026-10-07-prepare-confctl-release-changelog/confctl.
Base / unchanged origin/master: 6ed1715c27ed1aa6264e9e90213afedb3df7a25f.
Current local head: 1b56616eff41e760327f3a0dbed8875e4aa9dbec.
Complete unmerged series:
1. 358ed3f6bd91495df80fcd68d75bb2309b9af602 Refresh Ruby dependencies for the next release
2. c6eaab032c90a4108ed82b2453c598282f9975de Document confctl version releases as a skill
3. 1b56616eff41e760327f3a0dbed8875e4aa9dbec Version 3.0.0

[Final diff](confctl-final.diff): 7 files, 282 insertions/115 deletions.
No obsolete approaches, fixups, unused compatibility paths or migrations.
The swpins-to-flakes helper is merged baseline functionality, only documented
here. [Upstream inventory](upstream-commits.txt) covers 123 already merged commits.

Original remote feature candidate a2f27fcab72e0376a6e5acedf69eb19aeab4d453 was
unmerged/untagged/unreleased and was replaced using that exact old-head lease.
Remote feature and master now both point to 1b56616, with release-last ordering. Original patch/packet/checksum retained in
original-release.patch, original-review-packet.md and original-gem.sha256.
No published default history was rewritten.

## Documentation

[Plan](plan.md), [design](design.md), [revised review packet](review-packet.md).
Public changelog links existing docs/flake-inputs.md and docs/swpins-to-flakes.md.
README and CLI/man docs checked. New owning procedure:
skills/confctl-release/SKILL.md, with UI metadata and AGENTS.md routing.
It explains Bundix generation, all four identifiers, release-last history,
actual Nix and packaged CLI checks, authorization and partial-release recovery.
Exact release evidence belongs here, not in reusable project docs.

## Current quick verification

- bundle update completed on Ruby 3.3.10; no Gemfile/gemspec constraint changes.
- Bundix regenerated gemset.nix, then nixfmt formatted it; generation repeated
  after source/lock version bump. No manual gemset metadata maintenance.
- check-metadata.rb compares every lock/gemset version and dependency edge for
  76 gems; all activated gem requirements accept Ruby 3.3.0. Versions all 3.0.0.
- Skill structural validation passed with Nix Python/PyYAML. Ambient Python
  lacked yaml; validation was rerun with the proper Nix dependency environment.
- Syntax, focused RuboCop, whitespace and Nix checks passed. Installed/signed
  updated Overcommit 0.73.0; all three commits passed required hooks.
- Worktree clean and latest subject is Version 3.0.0.

Key updates: vpsadmin-client 4.1.0 -> 4.2.1, haveapi-client 0.26.5 -> 0.29.8,
curses 1.5.3 -> 1.7.0, overcommit 0.68.0 -> 0.73.0, rubocop 1.85.0 -> 1.85.1,
and transitive updates. No flake inputs changed. Client consumer is
lib/confctl/cli/gen_data.rb: raw numeric VPS IDs, fixed resource names, token
login/network listing/association traversal. Checked HaveAPI release notes for
validation, encoding and localization changes. No authenticated production
API probe performed.

Nix package and flake RSpec both use bundlerEnv/gemdir; pinned nixpkgs imports
gemdir/gemset.nix. Dev shell uses Bundler directly and did not check Nix metadata
in the original preparation. Actual Nix package build is now required.

## Review

Original a2f27fc final review passed (general/low, [report](original-review-report.md)).
Advisory package smoke-test isolation was fixed: unbundled child environment,
retained dependency paths, extracted library/root and version assertions.
Original artifact passed direct verification. Expanded final review passed; original review/CI/artifact do not validate
changed dependencies or instructions.

Revised review assigned to the same retained reviewer0 with no model/effort
change; read-only gpt-6-astra/xhigh. Risk high to cover publication instructions
and dependency/runtime compatibility. General, architecture/repetition,
scope/proportionality and risk/compatibility lanes. Full series/diff/provenance
supplied. [Final report](review-report.md): no findings in any lane.
Native assignment turn 01a11815-2909-7581-9bcb-87b8aaab432d; actual saved model,
effort and read-only access verified. Longer verification now authorized.

## Original candidate evidence (superseded)

Original 64s check batch passed: 35 RSpec examples, no failures; 120 Ruby files,
no RuboCop offenses; Nix formatting; generated docs; clean-export gem; isolated
package checks. Artifact had 237 files and SHA-256
bbc13a984443d47f1692151b46981b498134c295b04706a956f14b42322de0c9.
That artifact has been replaced by the verified expanded-scope candidate.
Original RubyGems inventory showed 3.0.0 unpublished.

Original CI: RSpec 37680258825 and RuboCop 37680259410 succeeded. Tests
37680258650 remains queued/active by last snapshot. Utility watch_release_ci
stopped only its local observation at parent direction (exit 130); remote run
was not cancelled. No monitoring process remains. Parent will cancel superseded
queued/active runs after publishing the new exact head under workspace rules.
Evidence: ci-results.json and exact-ID logs/status files.

## Next actions and ownership

Release publication is complete. Fresh watcher watch_revised_ci retains
ownership of self-hosted Tests 37686200620, queued; record its final result and
investigate any failure. RSpec 37686200570 and RuboCop 37686200584 succeeded.
Master/tag pushes may also schedule same-source workflows; source remains exact
reviewed head. No additional publication, integration or approval work remains.

Keep worktree/branch and session open. Preserve unrelated shared checkout/index
changes. Tracking initial commit is 4d068514; subsequent records remain local
under normal consolidated checkpoint cadence. No session lifecycle operation is
authorized.

Stable session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-07-prepare-confctl-release-changelog/

## Revised verification fixture diagnosis

First batch at 1b56616 exited 1: 35 examples, one EEXIST in generation modes.
ConfDir memoizes its initial working directory, so the generation spec's later
Dir.chdir does not isolate its fixtures once another spec initialized ConfDir.
Inspection found only exact example.test legacy/swpins/flakes generation JSON
and dummy /nix/store symlinks left by the original successful test run in the
ignored worktree .confctl. This is repeat-run fixture contamination, not an
updated dependency failure. Preserve that cache and run each Ruby process from
its own fresh directory, with explicit source Gemfile and spec_helper/spec paths.
No release source edit; reviewed head remains unchanged. First utility also
mis-targeted tee; retained failure excerpt/exit are revised-verification-first.log
and .exit. The next utility uses exact absolute capture paths.

The first isolated wrapper run stopped before examples: its explicit helper
require did not add source/spec to Ruby's load path for files that themselves
require spec_helper. Added RSpec -I source/spec; no project source changed.
Evidence: revised-verification-loadpath.log/.exit.

Revised full log confirms both Ruby suites passed (35 examples each), full
RuboCop passed (120 files), tracked Nix formatting passed, and clean-export gem
verification passed (239 files, source_commit 1b56616, isolated extracted CLI).
Actual Nix package and refreshed native dependencies built successfully. The
utility misread the last log excerpt as setup-before-tests; parent inspected the
complete log and artifacts to establish the stages actually reached. Batch exit
1 was the verification script's incorrect assumption that confctl has an
installed gemspec in the dependency environment. Pinned nixpkgs pathDerivation
represents path gems by source, and nix/package.nix runs source/bin/confctl with
source/lib directly. Focused metadata verification must load that installed Nix
source's gemspec, assert source root/loaded library/version and run the actual
launcher help. No project source change or review rerun is needed.

Focused Nix check exited 0: path-gem confctl-3.0.0, loaded source
/nix/store/487pkz0jdp1rrvqaywmh327w5y0piyv3-source, actual launcher --help passed.
Evidence: nix-focused-verification.log/.exit, nix-package-metadata.txt and help.
Parent first invoked the helper from tracking CWD; Nix rejected its absent
confctl output without any build. Correct project-CWD invocation passed.
Updated gem SHA-256 a91ac2d50a62edcb77d0b5575dd202bf5ea85c09647c823196c6a9061ee696c1
and sha256sum --check passed. Gem metadata records exact source commit 1b56616.

## Release authorization and exact-head CI

User explicitly approved: "looks good, you can release it" (current conversation,
2026-10-07). Scope is the prepared confctl v3.0.0 release: integrate confctl
master, tag v3.0.0, push branch/tag over SSH and upload exact verified gem to
RubyGems, as described in the release plan and lead's response. Head 1b56616
and artifact SHA-256 a91ac2d50a62edcb77d0b5575dd202bf5ea85c09647c823196c6a9061ee696c1.
No session lifecycle action requested or authorized.

Development ref replacement succeeded with exact a2f27fc lease; remote now
1b56616. Old queued Tests 37680258650 was cancelled under the superseded-run
policy; completed old RSpec/RuboCop retained. Fresh utility watch_revised_ci owns
new-head RSpec 37686200570, RuboCop 37686200584 and Tests 37686200620. Initially
RuboCop successful, RSpec in progress, Tests queued. No failed run known.

Release prerequisites: fetched remote master remains 6ed1715, feature 1b56616,
remote v3.0.0 absent; RubyGems inventory still tops at 2.2.3. Configured XDG
RubyGems credentials and default key are present (only booleans/names checked;
no credentials printed). Fresh detached integration worktree:
worktrees/2026-10-07-prepare-confctl-release-changelog/confctl-release-master,
created from origin/master and fast-forwarded to reviewed 1b56616. Preserve it
and the session; no lifecycle cleanup authorized. Exact-head RSpec/RuboCop
success plus local tests/Nix/package checks accepted for release; queued
self-hosted Tests remains owned and recorded.

## Verified publication

Fresh target worktree fast-forwarded from 6ed1715 to 1b56616, then atomic SSH
push placed that exact head on master and created annotated v3.0.0. Remote
master and peeled tag verified via ls-remote (remote-release-refs.txt). Source
and artifact unchanged since review/verification. gem push reported successful
registration of confctl 3.0.0. Public RubyGems v2 version API and downloaded
203264-byte gem match expected version, Ruby >=3.3.0 and SHA-256
 a91ac2d50a62edcb77d0b5575dd202bf5ea85c09647c823196c6a9061ee696c1.
Evidence: rubygems-release.json, published-gem-verification.json.
Public package: https://rubygems.org/gems/confctl/versions/3.0.0
Tag: https://github.com/vpsfreecz/confctl/tree/v3.0.0
Release procedure: skills/confctl-release/SKILL.md included in this tag.
No tag deletion, gem yanking, version/artifact substitution or session lifecycle
action. Feature ref and both owned worktrees retained. No further tracking
commit required under this short initiative's normal cadence while CI is open.
