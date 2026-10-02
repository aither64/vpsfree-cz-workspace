# Whole-branch review packet and final inventory

## Requested outcome and decisions

User requested implementation of the accepted plan: #vpsfree filters original
push AUTHORS, not push sender/committer; all ignored -> silence; mixed -> retained
commits/counts/order. Unknown authors remain. Explicit username wins; only absent
username permits exact GitHub noreply account recovery. Non-push/eligible empty
push events filter sender. Per-channel option ignored_users defaults empty;
legacy arrays/absent/empty preserve exact existing output. Keep original event
classification, SHAs and full compare URL, no shared-event mutation. Active
filtered output is capped at ten retained lines; force/fast-forward add retained
details. Core source owns parsing/rendering; announcer owns destination policy.

User selected AUTHOR ONLY and exactly six additions under vpsfreecz:
vpsadmin-webui, vpsfree-kb-contracts, ruby-lxc, vpsf-status, ssh-exporter,
syslog-exporter. No other repos. Template name already fixed. No generalized
bot matching, author display-name matching, commit-message/path heuristics,
server-wide suppression, global state/protocol/schema changes, workflow changes,
new Nix module option or lock update. No default-branch merge/production rollout.

## Initiative and owning components

Session 2026-10-02-vpsfbot-github-notifications, workspace /home/aither/workspace/ai/vpsfree.cz.
Plan/state/design/verification/repository-inventory in work/<slug>/.
Source worktrees in worktrees/<slug>/{vpsfree-irc-bot,vpsfree-cz-configuration}.

The bot owns ignored_users policy interface and author parsing/message rendering.
Its configuration consumer is the site Libera instance and fixed source package
pin. CLI normalizes GitHub channel settings at startup; Nix module settings are
free-form serialized JSON with later private overrides. Read existing
lib/vpsfree-irc-bot.rb, CLI merge behavior, helpers/channel logs and representative
consumer source. Actual helpers send PRIVMSG for Matrix bridge compatibility
while using notice log type. Preserve this. One Libera instance bridges both
channels to Matrix, but production effective overrides/subscriptions unverified.

## History, diff and migration inventory

Exact final heads and commit lists are appended by lead below before assignment.
Bot intended split: one coherent feature commit including source, unit coverage,
README/sample and isolated VM fixture. Tests/docs validate only this policy and
are inseparable from its supported behavior; no independent refactor/workflow or
dependency update is bundled. Configuration uses separate functional route/filter
and fixed source-pin commits per its repository guidance.

No superseded sender-only implementation was committed. No fixup or abandoned
branch iteration is retained. No migrations in either branch; no schema/seed or
persistent-state changes, and no migration version was merged, released,
deployed or externally consumed. Existing legacy formatting behavior is
supported upstream, rather than an unapplied compatibility path.

Source pin initially 565c4b4e99c7b6b6daf8b0a9768b9b3796611247; feature base
88906fd54b0fc8cf613fc2cec2fb930d8196d05a. Nine intervening upstream commits
change only .github/workflows/integration-tests.yml, flake.lock and
 tests/suite/vpsadmin-events.nix. They affect test infrastructure/flake inputs and
advisory fixture, not runtime lib/dist/Gemfile/gemset. Inventory/review this whole
pin-to-feature range as well as the base-to-head feature diff. Do not rewrite
already-upstream history. Local normalized archive NAR hash for d919902:
sha256-ablV9Fh3HLoAO/xqA6eiisrnY6huxZ/amqIXjtiVitM= . Actual GitHub fetch/hash
will be checked after review/publication before the scoped configuration build.

## Verification and documentation

Final bot quick checks at d919902dc18f774878c1aaa2bc8927cb24a16efa:
full RSpec108 examples/0 failures; full RuboCop61 files/no offenses; Nixfmt
fixture+registry; Nix fixture parse; extracted Ruby syntax; diff checks passed.
Actual pre-commit/commit-msg/post-checkout hook execution passed without bypass.
Configuration generated non-secret settings JSON, exact six additions and
preserved routes/gates inspected; Nixfmt and real commit hooks passed. Source
pin-only commit results appended below. Full long VM/build checks have not run;
they follow this review gate using a fresh catalog Luna/low watcher.

README.md and dist/config.yml.sample own the durable ignored_users behavior
contract. tests/README.md documents the isolated signed webhook fixture. Main
lead applied user-facing writing pass after technical facts settled. Session
records own temporary branch/setup/recovery evidence. No reusable production
rollout doc needed because service topology unchanged and rollout not executed;
design/state record later target/order/rollback and live access limits.

Temporary execution setup: implementer lacked Nix socket access. Lead/watcher
prepared exact Nix environments and exported task-private scripts with retained
profiles. Locked Bundler copied from existing cache into correct .gems directory.
No source/dependency/hook bypass. Optional cross-project setup lesson at
notes/cross-project/2026-10-02-nix-dev-env-restricted-member.md is lead-owned
coordination documentation; inspect for accuracy if useful.

## Review selection, risk and required conclusions

Risk HIGH because new cross-project configuration policy, bot pin activation
ordering and old/new/rollback behavior need assessment. New bot+old config is
unchanged; old bot+new key runs but ignores filtering. Activate new package and
policy together in any later approved rollout. No database/API/auth boundary
change; signatures and event gates unchanged. Queue is in-memory and can lose
pending events on restart. Private overrides/subscriptions/actual deployed head
unknown; no production delivery readiness claimed.

Retained reviewer0 is independent, ready, review-purpose, read_only; saved
model gpt-6.1-sol, effort xhigh. No override/fallback. Required lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. Read mandatory
skill plus EVERY lane reference. Review directly; no nested reviewers.

Start with severity-ordered concrete findings, file/line/commit evidence;
otherwise explicitly say no findings with residual verification limits. Require
explicit complete-branch history conclusion on obsolete approaches/follow-up
fixes and explicit migration-lineage conclusion (no migrations). Early incremental
review cannot substitute. Do not edit source or records; return report content
to lead for saved review artifact. Do not run long tests or invoke merges/deploy.

## Original independently reviewed branch inventory

| Repository | Base | Head |
| --- | --- | --- |
| vpsfree-irc-bot | 88906fd54b0fc8cf613fc2cec2fb930d8196d05a | d919902dc18f774878c1aaa2bc8927cb24a16efa |
| vpsfree-cz-configuration | 028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d | 1a17649638a9f462945fee1e0d778a2e0405639f |

Complete chronological feature series:

- Bot d919902dc18f774878c1aaa2bc8927cb24a16efa: github: filter commit authors per channel.
- Config cf2840c1894501f3c9c859dcf2600ed44647c415: vpsfbot: filter automation commits and expand GitHub routes.
- Config 1a17649638a9f462945fee1e0d778a2e0405639f: vpsfbot: pin bot with per-channel author filtering.

Final exact diffs saved alongside this packet: review-bot.diff,
review-configuration.diff, and review-pin-upstream.diff. Both worktrees clean.
No obsolete/fixup commits or migration paths. Pin commit was amended only to
wrap its unpublished commit message; no follow-up source iteration remains.
Pin Nixfmt/diff checks and real commit hooks passed. Upstream heads refetched
before packet and still match bases. No feature refs published/deployed/merged.

## Final inventory after direct verification repair

The first VM execution found unsupported fixture after(:each) use before
examples. Implementer moved bounded diagnostics into the existing example's
rescue and preserved original errors/suite cleanup. Lead inspected the exact
fixture-only patch and quick checks/hooks. This direct narrow repair changes no
reviewed public contract; mandatory skill step9 permits focused verification
without rerunning unaffected lanes. See review.md and verification.md.

Current complete base-to-head feature series:

- Bot base88906fd54b0fc8cf613fc2cec2fb930d8196d05a -> sole feature commit
  cf21b243d1e207f5aeca0077112d8467af851b7f.
- Configuration base028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d -> functional
  cf2840c1894501f3c9c859dcf2600ed44647c415 -> separate pin
  2b84893e885944701e659fab69f03eec9c565e23.

Original reviewed bot->current tree diff is only the accepted fixture repair;
configuration diff is only source revision/hash. Pin hash is
sha256-nn3/hf1iAtCyltEAF9BLiY3i1WuwGhLVRn+tEZ478QM=. Both current heads
clean/published; comparisons recaptured. No obsolete intermediate iteration,
fixup or migration introduced. Independent whole-history/migration conclusions
and supported legacy path remain applicable; original review diffs are retained
as the evidence assessed, while portal comparisons show current exact diffs.
Corrected runtime/build/archive/CI checks are running. No merge/deployment.
