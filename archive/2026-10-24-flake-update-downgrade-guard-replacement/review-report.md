# Independent final review

No Blocking, Important or Advisory code findings identified in the eight exact
ranges below. The completed committed deliverable passes this independent final
review gate and may proceed to the planned longer verification. This conclusion
does not claim completed package/runtime verification, live workflow coverage,
integration readiness, integration approval or deployment.

## Identity and scope

- Session: `2026-10-24-flake-update-downgrade-guard-replacement` in
  `/home/aither/workspace/ai/vpsfree.cz`.
- Reviewer: retained `reviewer0`, thread
  `01a16da6-4cc0-7fd1-8b85-0933235d3dd0`, saved and assigned
  `gpt-6.1-sol` / `xhigh`, purpose `review`, access `read_only`. The live
  same-session roster matched the trusted thread binding; no overrides or
  fallback reviewer were used. I did not author the deliverable.
- `dev-session current` from the bound session directory printed the exact
  bound slug. Both `DEV_SESSION_SLUG` and `DEV_SESSION_WORKSPACE` were absent,
  which is permitted with the matching trusted binding. An initial invocation
  from the workspace root found no current session; the intended-directory
  invocation resolved that before accessing session files.
- Risk: **High**, because this changes a public CLI, cross-project dependency
  acceptance and automated branch publication. No live-system behavior is
  changed by these ranges.
- Lanes performed directly: general; architecture and repetition; scope and
  proportionality; risk and compatibility. Read the mandatory skill and all
  four assigned references, workspace AGENTS and routed procedures, each
  available repository AGENTS, relevant project documentation and source.
  IRC and the org configuration have no root AGENTS.
- No nested agents, source edits, long test launches, workflow dispatches,
  integration, deployment, claims or lifecycle operations. The only evidence
  write is this report; lead retains state/handoff ownership.

## Exact reviewed history

I independently checked each worktree's HEAD, clean tracked/untracked status,
base ancestry, complete base-to-head commit list, commit message and final
changed-path list against `review/inventory.json`. Each range has exactly one
commit and the inventoried paths match Git. I inspected the final diffs and
implementation/consumer context, rather than relying on packet assertions.

| Repository / target | Base | Final head |
| --- | --- | --- |
| confctl / master | `cc40679d267165aecfa569128438bb55fe910268` | `7ba361d22a4aac044cb02abf8397800bcf5726bf` |
| haveapi / master | `67fcd34ba506264a5c7ee2e8e18a88d221c6f469` | `d4dc3c7c6b15d3bdad51ce18f6959136dc68b23e` |
| terraform-provider-vpsadmin / master | `2a2c1055302f86f8e250f1d7e4c331d62012efe8` | `171e32d8bf6706748651ba33df6abb05849244fa` |
| vpsadminos / staging | `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854` | `0552cfeecf127671e21dcb72db78b7188d342107` |
| vpsf-status / master | `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb` | `7641e48787281d29cdd0df95f7ee06555c73fac6` |
| vpsfree-irc-bot / master | `94ac4eb5a7caf0456fff7df86a44cae198463276` | `a2ab57b8169ad978f6f8542dd19cf5199517b0cb` |
| vpsfree-cz-configuration / master | `50d263d4127c05163d660fae1c4b9b887584032d` | `f5bf3f026210d30c0b9b219aac47ff6490e4cddc` |
| vpsadminos-org-configuration / master | `6b04b48e9c076e5525ccb7c38ce174232414f0b5` | `30ea016491f78d88037508e3a7e9c9a20d50511b` |

The provider's policy, transaction, CLI and supporting tests/docs form one
coherent guarded-update feature. Consumer commits independently adopt that
feature in their owning repositories. The limited action-ref and commit-file
adjustments support those workflow changes; no unrelated application change
is bundled. Messages explain the final behavior and motivation.

**Obsolete history:** none remains in these complete final ranges. I compared
the original five C heads in `package-c-branches-initial.json` with the final
heads using `git range-diff`. The committed-blob correction and provider refresh
were folded into each adoption commit. These corrections are substantive;
they are not represented as patch-equivalent history. The provider's old
`d58181a4d8b0de716fdb93c56f524175dd36cce4` to final `7ba361d` comparison
changes only its guide/manual publishing examples. No abandoned policy,
automatic equivalence exception, partial-graph splice or bootstrap tool-pin
upgrade remains in the shipped diff.

**Repeated-update streams:** one external confctl CI-tool adoption per
consumer, all selecting exactly `7ba361d22a4aac044cb02abf8397800bcf5726bf`.
The former `d58181a` development selections were superseded and consolidated;
no repeated pin-update commits remain in any reviewed series. There is no
evidenced release, deployed-state or supported-consumer boundary requiring an
intermediate update commit. Publication receipts remain provenance, not a reason
to retain obsolete commits. Preserve the exact final provider ref while
consumers refer to it.

**Migration conclusion: no migrations.** The final path inventories and actual
diffs contain no database, runtime-state or persisted-format transition. All
eight repositories' `flake.nix`, `flake.lock` and relevant dependency manifests
are unchanged from their bases. The additive lock-reader contract retains
version 7; the process-lock file is coordination for cooperating updates, not
a state migration. There is no intermediate migration version whose merge,
release, deployment or external consumption needs preserving. The receipts
report no release, deployment or default integration of these feature ranges;
I performed none.

## Lane conclusions

**General and risk:** `ForwardGuard` compares every reachable semantic path,
including aliases and descendants, rather than generated node IDs. It rejects
removed paths and source/extraction transitions, accepts new supported immutable
sources, and leaves unchanged unsupported sources alone. Equality avoids HTTP;
changed revisions require the same supported source and positive ancestry
evidence. Errors take precedence over known rejections. Source attribute
allowlisting and full-SHA validation prevent an unknown attribute or mutable ref
from becoming a bypass (`forward_guard.rb:24`, `:65`, `:106`).

`GitHubCompare` uses a fixed HTTPS API host, encoded-safe repository/SHA
components, explicit token support, no redirects or retries, bounded connection
and read waits, sanitized errors and consistent summary fields. It does not use
the potentially truncated commit list as ancestry authority
(`github_compare.rb:20`, `:51`). No speculative clone fallback is present.

The transaction uses the original flake directory and separate same-filesystem
reference/output locks, then validates before rename or commit. It snapshots
lock/declaration bytes, HEAD and index entries and rechecks tracked state before
install. Pre-install rejection/error leaves the original data untouched by
confctl; post-install hook failure propagates while retaining the validated lock
for diagnosis (`guarded_update.rb:22`, `:75`, `:92`). The documented single-writer
precondition and per-invocation atomicity accurately limit the guarantee.
Unguarded/manual updater and setter branches remain available, with a focused
existing update/set regression in the quick evidence.

All seven real workflows use the exact external package, explicitly provide
the provider token, save the original baseline before update work and validate
an exported **committed `HEAD:flake.lock`** after hooks/checks, immediately before
an ordinary non-force push. No stale pull/rebase retry or force-push path was
added. Input/channel selections, llm-agents condition/postcondition, repository
commit formats and existing verification stages remain intact. The config
steps preserve their tools-shell context while explicitly selecting the new
tool; deployment-tool pins and running machines are unaffected.

**Architecture and repetition:** confctl owns the graph, policy, evidence and
transaction. Actual consumers were traced from workflow tool pins, helpers and
flake/channel declarations. Status/IRC metadata uses the bounded shared JSON
listing instead of another graph parser. Their jq selection and package-launch
glue are small consumer adaptations, not duplicated ancestry policy. The
external tool avoids adding a confctl/vpsAdminOS input cycle. Existing config
scripts use retained interfaces; no broader deployment-tool upgrade is hidden
in the adoption.

**Scope and proportionality:** strict GitHub-only changed-source support,
complete-candidate rejection and no automatic cherry-pick equivalence fit the
accepted boundary. The implementation delegates lock generation to Nix and
ancestry to the provider; it does not introduce another workflow framework,
repository catalog, generalized Git mirror fallback or live-system migration.
The JSON listing has concrete status/IRC consumers and preserves default table
formatting. No material speculative mechanism or obsolete compatibility path
was found.

The guide/manual explain the lasting interface, recovery limits, supported
sources and final committed-lock check. Consumer docs link that contract at
their selected immutable source; rollout provenance stays in session receipts.
The two config workflow-only changes need no additional deployment guide.
The minimum command syntax is supported by the
[Nix 2.19 reference](https://nix.dev/manual/nix/2.19/command-ref/new-cli/nix3-flake-update);
the [GitHub compare reference](https://docs.github.com/en/rest/commits/commits#compare-two-commits)
also documents SHA comparisons and pagination limits. These documentation
checks do not substitute for runtime proof at the packaged versions.

## Verification assessed and residual gates

Inspected the added graph/provider/transaction/CLI specs and relevant existing
code, the C/D fixture drivers, quick logs and current package reports. Provider
evidence reports 143 focused examples, one existing unguarded update/set
regression, 25-file RuboCop, man generation and ordinary hooks passing. C reports
40 workflow scenarios and lint/hooks passing; D's current receipt and log report
20 scenarios plus syntax/hooks passing. Fixture orchestration is appropriate
quick evidence, with its mock boundary stated; it is not package/live-updater
proof.

I additionally ran a read-only in-memory check using the actual new Ruby
resolver/validator on all eight real locks: all parsed and returned `unchanged`
with a provider that raises if called. Semantic path counts were 10, 1, 21, 8,
21, 21, 157 and 19 in the table's order. Status/IRC (and Terraform's nixpkgs
alias) resolved to `vpsadmin/vpsadminos/nixpkgs`; all-root vpsAdminOS resolved
the intended five input names. No lockfile or source was modified.

The following are deliberately post-review verification gates, not confirmed
code defects or completed checks:

- Build/run the exact pinned provider and record its complete source/input
  graph, executable/store paths and actual bundled Nix version. Validate the
  candidate/reference-lock behavior with that Nix, not merely the ambient
  installer or documentation-backed minimum.
- Exercise the actual package in both old configuration tools shells and with
  real commits/hooks. IRC's declared shell exports `RUBYOPT=-rbundler/setup`
  and `BUNDLE_GEMFILE`; preserve that environment when probing this boundary.
  The wrapper overwrites GEM_HOME/GEM_PATH/RUBYLIB but does not itself prove
  compatibility with every inherited Bundler setting. Harness-only stdlib
  environment isolation is not evidence for the supported package invocation.
- Run the complete provider suite and all seven prepared nonpublishing updater
  patterns, including actual Git history/target movement and representative
  old settings/channel outputs. Retain existing repository tests, and collect
  exact-final-head CI evidence. Mocked push failure alone is not an actual Git
  race test. Live known rejections are valid outcomes; evidence errors need
  diagnosis and must not be relabeled successful skips.
- GitHub API availability/rate limits, strict path removal/source-transition
  rejection, later upstream revert commits and semantic software compatibility
  remain the documented operational limits. No complete oldest-Nix-version
  matrix, live enabled-schedule inventory or external-bot audit is claimed.

The prepared commands in `package-c-live-checks.md` and
`package-d-live-checks.md` address these gates without source publication or
deployment. Their execution/results remain lead-owned. A newly demonstrated
defect should be routed to its implementation owner under the mandatory
review skill's narrow-fix/affected-lane policy. No remediation or review rerun
is requested by this report.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/>
