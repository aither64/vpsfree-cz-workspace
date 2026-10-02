# Expanded final whole-branch review

## Outcome and scope

Use plan.md and accepted design.md including its reliability amendment. User
requests original-author filtering only in #vpsfree, suppress all-ignored pushes,
retain human/unknown commits from mixed pushes, exact noreply fallback and
explicit username precedence, original event metadata/full comparison link,
channel isolation, absent/empty legacy compatibility. Exactly six #vpsadminos
routes: vpsadmin-webui, vpsfree-kb-contracts, ruby-lxc, vpsf-status, ssh-exporter,
syslog-exporter. Template rename already correct. No other repository additions,
no merge/deploy authorization. Owning bot README/sample contract unchanged.

The real two-channel VM exposed a pre-existing shared HTML asset startup race.
Lead authorized the minimal necessary reliability fix after the architect wrote
an amendment before app edits. Immutable assets copied concurrently can raise
EACCES before chmod, leaving ChannelLog without a logger. Constructor reproduction
observed9/10 failures; final controlled regression fails deterministically on
pre-fix source and passes on fixed source. VM causality remains inferred because
initial JOIN journal was outside old tail; current fixture captures full boot
unit journal on failure. Inspect evidence without assuming this fixes the VM.

## Exact ranges and complete chronological series

Worktrees: worktrees/2026-10-02-vpsfbot-github-notifications/{vpsfree-irc-bot,vpsfree-cz-configuration}.
All intended changes committed; both indexes/worktrees clean.

Bot base88906fd54b0fc8cf613fc2cec2fb930d8196d05a to e9c60b0b95d3cc0dad6f012d8127c2bc078cfa7d:

1. cf21b243d1e207f5aeca0077112d8467af851b7f: github: filter commit authors per channel.
2. e9c60b0b95d3cc0dad6f012d8127c2bc078cfa7d: html_logger: serialize shared asset installation.

Configuration base028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d to b164a3b786cb82878f00f8ebd2a7825ee5254c15:

1. cf2840c1894501f3c9c859dcf2600ed44647c415: functional routes/policy.
2. b164a3b786cb82878f00f8ebd2a7825ee5254c15: separate fixed source pin.

Current final full diffs: review-final-bot.diff and review-final-configuration.diff.
Additional already-upstream pin range565c4b4e99c7b6b6daf8b0a9768b9b3796611247
through bot base remains nine commits limited to workflow/flake.lock/advisory
fixture, saved review-pin-upstream.diff and previously inspected. No runtime
lib/bin/dist/Gemfile/Gemfile.lock/gemset changes in that upstream range.

No obsolete sender-only approach or unused transitional shim exists. Invalid
fixture hook iteration was folded into the owning unmerged feature; repeated
pin revisions folded into the separate pin commit. Logger fix is an independently
reviewable existing-bug correction, with its own regression and diagnostic line,
not a tidy/fixup for notification behavior. Legacy formatter is supported.
No migrations in either final branch or extra pin range: no schema/seed/
persisted-format conversion or version needing release/deploy/consumption
provenance. Require explicit whole-branch and migration conclusions again.

## New reliability behavior and constraints

HtmlLogger owns one eagerly initialized process-wide mutex across mkdir/cp_r/
complete chmod. Preserve every-install content refresh, destination0644/source
read-only, exception propagation and lock release. Normal log writes stay per
instance. No nil guards, cache, lock registry, filesystem transaction or source
permission change. One writing process per archive root remains an assumption;
no cross-process or crash-atomicity guarantee. New comment owns durable rationale.
The deterministic real-file spec checks copy/chmod ordering, both logger markers,
bytes/modes, refresh, absent assets and injected failure/recovery. Inspect cleanup,
worker exception propagation and bounded waits without assuming concurrency proof.
No interface/schema/module/dependency/formatter/bridge changes.

## Verification, compatibility and documentation

Final bot focused logger4/0; same final spec loading pre-fix committed method
fails4 examples/1failure, EACCES style.css in0.076s. Full RSpec112/0, RuboCop62
files clean; Nixfmt/fixture parse/extracted Ruby syntax/diff checks pass. Real
precommit/commitmsg hooks pass with signature verification and exact pinned
Ruby3.3.10/Bundler4.0.12. Config final pin formatting/parse/diff and actual hooks
pass in its pinned Ruby3.4.9 environment. Config functional JSON/exactsixroutes
already checked and unchanged. No hook bypass. Author/lead report quick evidence;
review remains independent read-only.

Pin rev e9c60b0b95d3cc0dad6f012d8127c2bc078cfa7d and local committed archive NAR
sha256-jONz5RyWIzH2/h9oALb31Ms1pQlbwP3MNRUe1vwzp5A=. Publish/archiveverify,
new signed-webhook VM, scoped build and exact-head CI follow this review gate.
Previous cf21 archive/build/RSpec passed; VM failed second-channel archive.
Old integration CI37025858914 queued and will be cancelled after superseding push.

New bot with old config remains legacy-compatible; old bot ignores ignored_users.
Later activate bot/policy together; paired rollback state-compatible, restoring
old bot also restores race. No migration or fleet update. Existing in-memory
queue can lose events on restart. Actual deployed revision/private overrides/
hook subscriptions/IRC-Matrix delivery unknown; API hook403. Private settings
load later and can override generated JSON; do not access/print secrets.

Bot README/sample/testREADME own durable policy and fixture use. Logger comment
owns narrow synchronization rationale; accepted design contains operational
assumptions. Session owns branch/review/rollout evidence; no production operation
executed. No new public option or separate upgrade guide is needed.

## Required independent review

Retained reviewer0, eligible read_only gpt-6.1-sol/xhigh, no override/fallback.
Risk remains HIGH for cross-project policy, pin activation/rollback, plus startup
logging data-loss implications. Perform all four affected lanes directly:
general; architecture/repetition; scope/proportionality; risk/compatibility.
Read mandatory skill and every lane reference. Inspect complete final ranges,
messages, current diff and consumers rather than only latest commit. Earlier
review.md covers initial scope; this expansion requires final gate again.
Return severity/path/line/commit findings or no findings with residuals, explicit
obsolete-history conclusion and explicit no-migrations/provenance conclusion.
No source/record edits, longchecks, hooks, pushes, nested reviewers, deploy/merge
or session lifecycle actions. Lead reconciles findings and records report.
