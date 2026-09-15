# Review v8: neutral closing and deterministic notification assertions

Requested outcome: remove the implication that a member will relinquish their
IP addresses, investigate the failed API Specs workflow, and explain the
existing locking prerequisite. The implementation delta is limited to literal
mail copy and regression specs. No locking implementation is changed.

Tracking directory:
`/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-ip-release-mechanism`
Read plan.md, the September 15 section of state.md, and ci-investigation.md.

Worktrees are under:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism`

## Immutable review ranges

- vpsadmin: base `7483c4d2535b994a10ea3a82856052bd78c4913c`,
  head `395bf80b76b2e715fbad25f7c637c5763dc35ad5`.
  Commit `36a6869fe93b2699eafa2f75a8ae1ecf7be38d15` fixes initial/reminder
  substring assertions and supplies deterministic overlapping fixtures.
  Commit `395bf80b76b2e715fbad25f7c637c5763dc35ad5` changes four built-in EN
  text/HTML notice/reminder closing sentences.
- vpsfree-notification-templates: base
  `00519f79fa9a5073eb83f41bae3857bc66229e17`, head
  `51c8f2c3f94b094ca93e1bddb719e0b23a9e04ab`. One matching literal-copy
  commit for eight EN/CS text/HTML initial/reminder variants.

Both worktrees are clean. Commits have separate purposes. The deterministic
CI reproducer is deliberately separate from the earlier large implementation
commit: it documents the observed hosted failure and does not rewrite the
locking commit the user is currently examining.

## Acceptance and boundaries

- New closing is “Děkujeme za tvůj čas.” / “Thank you for your time.”
  The main agent applied the user-facing writing skill directly.
- Keep assignment guidance, opt-out gating, IPv4-only scarcity wording,
  locations, URLs/buttons and automated-mail footers intact.
- No new support-reply/exemption or past-policy explanation in forced mode.
- The API failure must be reproduced and explained, not dismissed after a
  rerun. Bare `.20` substring checks collide with eligible `.200`/`.204`.
  CIDR comparisons and explicit fixtures cover both initial and reminder tests.
- No policy, release, authorization, schema, accounting or locking rewrite.
  User asked for an explanation of existing locking, not a new design.
- No merge, production email delivery, deployment, KB publication or session
  lifecycle action.

Supplementary explanation: `locking-notes.md` describes the existing commit
`664e1e184f5d0d823d38ad6674d462206793df6e`. Check factual claims against
referenced code if needed, especially lock types/lifetimes and the difference
between parent/host reservation and bundled accounting/validation behavior.
This is a read-only explanation, not a fresh authorization to redesign or
re-audit the entire already reviewed v1-v7 feature. Report a concrete serious
problem if encountered, but keep the required change review on these deltas.

## Verification

- Before the assertion fix, explicit overlapping fixtures produced two
  examples and two failures (initial and reminder). Log:
  `/tmp/ip-release-prefix-repro.log`.
- `VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec spec/models
  --seed 24922`: 912 examples, zero failures, 50 existing pending; original
  failing CI seed. Log: `/tmp/ip-release-core-engine-fixed.log`.
- Existing overlay render harness: 24 examples, zero failures. All EN/CS,
  initial/reminder, opt-out policies, IPv4/IPv6/mixed combinations; HTML escaping
  and absolute URLs. Safe HTML previews regenerated. Run from vpsadmin:
  `IP_RELEASE_OVERLAY=<overlay-worktree> IP_RELEASE_PREVIEWS=<tracking>/email-previews
  nix develop .#api -c bundle exec rspec -I spec <tracking>/overlay-check.rb`.
  Log: `/tmp/ip-release-neutral-closing-render.log`.
- Overlay `nix flake check` passed.
- Touched API spec RuboCop, whitespace checks, and all commit hooks passed.
- Full integration CI 34491288911 passed on the previous head 7483c4d25.
  API Specs 34491288836 failed only core-engine; downloaded failed log examined,
  all other jobs passed. No new long integration run is needed for literal
  copy and spec fixes before review.

## Risk, components and compatibility

Low risk for this follow-up: literal reversible copy and test-only changes.
No new abstraction or persisted/public contract. General and architecture lanes
apply (hand-written test fixture/assertion logic changed), both
`gpt-6-astra` with `xhigh` effort and fresh context, per the current skill.
Prior full-feature reviews remain recorded in v1-v7 and state.md; this small
delta does not reopen their unchanged runtime scope.

Notification rendering is owned by vpsAdmin; the overlay supplies localized
variants through the existing template interface. Variables and metadata are
unchanged. KB contracts remain at `87bc0fbcb267292a30867d7a5f90eee92552fc10`,
pinning vpsAdmin `871fa3dae787678ceea7f36ba5cbec139c93e5ee`; WebUI documentation
behavior is unchanged, so no repin is needed. No other consumer/pin changes.

Upstream was fetched: vpsAdmin master f7a17d6e5 and overlay master 6ebfb6f have
advanced with separate authentication, recovery, reporting and dependency work.
Retain the established base for this bounded fix. Refresh and reconcile before
future integration; this review does not claim compatibility validation against
all newly merged upstream changes.

Read applicable AGENTS.md and the current mandatory-change-review skill/lane
reference. Review directly without code edits or nested agents. Report concrete
findings with severity or explicitly state no findings and residual test gaps.
