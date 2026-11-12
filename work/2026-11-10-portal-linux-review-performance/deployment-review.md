# Independent deployment composition and branch history review

## Findings

1. **Important, general/readiness: rebase the workspace feature onto current
   master before the composed build and final delivery.** The reviewed workspace
   head `290a659de1993242ee259136f2c3478e96b42e1f` starts at
   `2ffa0b1cd8828ab610284a8e7062095f7932b13a`, while local and fetched
   `origin/master` are `05ad6ab3e430ac69ec20d94a481843a7e1f57124`. The latter adds
   the production-observability routing instruction and guide. The branch is
   therefore not a fast-forward of its current target. Workspace
   `docs/agent-instructions/git.md` requires rebasing onto current master before
   final review. Rebase the single pin commit, verify patch equivalence and the
   final deployment contract, then build/select that final source. This is a
   narrow baseline repair: unchanged pin behavior can retain this review after
   the lead verifies the resulting range and fresh target. Do not omit the
   current target guidance or integrate with a merge commit.

No deployment-composition, architecture, scope or compatibility defect was found
in the reviewed pin changes. No Blocking findings. The readiness finding needs
resolution or an explicit recorded decision before long verification.

## Scope and reviewed revisions

Reviewer: fresh standalone `/root/deployment_review`, assigned
`gpt-6.1-sol` / `xhigh`. The installed selected package's catalog independently
resolves its default development team to `delegated` and its first review-purpose
role to `reviewer` with those exact settings. The previous application reviewer
is no longer live, so the coordinator selected this fallback. No delegation or
source edits were performed. Overall risk is high because this delivery selects
a live host/profile composition; state and native contracts are unchanged.

Read the mandatory-change-review skill and all assigned general, architecture,
scope and risk references, the review packet, plan/design/state, prior application
review, applicable repository instructions and deployment/documentation guidance.

| Repository | Complete reviewed range | Series |
| --- | --- | --- |
| dev-workspace | `6587c4c1cedabee95bcc52f4667e7d33e3a82859..02881b401955ff0db71bb74f6fb84f6e475a7879` | One portal feature commit |
| workspace | `2ffa0b1cd8828ab610284a8e7062095f7932b13a..290a659de1993242ee259136f2c3478e96b42e1f` | One exact runtime-selection commit |
| vpsfree-cz-configuration | `dda57166bd8bb6d85a74decdd05a8810933bdecc..5dcde1ce5210a42e4499dbf1b6badbd1f0aa326c` | One generated channel update |

Each stated base is its branch's merge base with the inspected target. All three
worktrees were clean. The application review remains authoritative for unchanged
application behavior. I inspected the final file inventory and the entire delta
from the originally reviewed application head `06e48780` to `02881b40`: it consists
only of the two recorded narrow remediations and their regression coverage.
These preserve the accepted design and do not add another implementation stream.

## Composition, ownership and deployment compatibility

Workspace `flake.nix` retains the direct nested
`vpsfree-dev-workspace/dev-workspace` selection. Only that runtime node changes
in the workspace lock; extension revision
`0c7168f352f6d4f11c46368e702b9356d81012c6`, sibling inputs and follows paths are
unchanged. Configuration changes only its existing `devWorkspace` locked node
through the `dev-workspace` channel's `devWorkspace` role. Its flake declaration,
channel mapping and aitherdev imports remain unchanged. Both nodes select
`02881b401955ff0db71bb74f6fb84f6e475a7879` with content hash
`sha256-TLsZCYeW4bPgcA/QAEkyjZDizq7sko4KPyVyt3PRdRA=`.

An independent semantic lock traversal confirmed that both effective runtime
dependency graphs are identical despite their different node labels. Their
`codex-web`, `llm-agents` and `nixpkgs` subgraphs also match the reviewed runtime's
own source lock. The runtime's `flake.nix`, `flake.lock`, `nix/` and `libexec/`
are byte-for-byte unchanged against its base. There is no Codex, provider,
host-module, transition-helper or persisted-contract upgrade hidden in the pins.

The generic runtime owns the host module and package contract. Configuration
consumes its host module and Codex wrapper through `devWorkspace`; the workspace
consumes the same runtime through the retained site extension to build its user
profile. The application remains in that profile. The patch does not introduce
another system-installed application, duplicate selector or compatibility layer.
The pin-only scope is proportionate to the user's deployment direction.

The planned build/copy, exact schema-2 machine claim, mapping verification,
confctl dry-activation and no-reboot switch, system/profile identity checks, then
ordinary guarded profile selection preserve existing ownership and recovery
boundaries. Preserve confctl auto-rollback and its retained generations. Profile
recovery remains forward-only through the existing journals; do not use a forced
restart or bypass a refusal. No coordinated fleet update is required. Cached
browser pages still require refresh, and older portal code cannot resolve new
metadata-generation file IDs; those application limits remain documented.

## Complete history, streams and migrations

The three feature series each contain exactly one logical commit. The application
commit contains the final feature with supporting tests, asset versions and docs;
its remediations are folded into that commit. The workspace pin and independently
generated configuration pin are appropriately separate repository-owned changes.
The configuration message preserves confctl's generated history and is exempt
from generic message-width reformatting.

**No obsolete unmerged approaches or separate follow-up fix commits remain.**
The current-target rebase identified above is still required. There are no
superseded runtime revisions in these feature histories.

**No repeated update streams.** Workspace's nested runtime stream has one final
update, and configuration's matching channel stream has one final update. These
are distinct necessary consumer selections of the same revision, not redundant
iterations. No intermediate pin commits need consolidation or a retained-consumer
exception. The packet reports no intermediate deployed or externally consumed
feature version; no deployment exemption is used to retain history.

**No migrations.** The final file inventory contains no database, manifest,
saved-comparison, journal or other persisted-format migration. Existing application
review established unchanged descriptor/state formats, and the deployment pins
add no conversion step. There is no intermediate migration version with merge,
release, deployment or external-use provenance to preserve.

## Documentation placement and verification limits

README remains the application's entry point and links the portal reference.
`dev-workspace/docs/workspace-portal.md` owns the lasting metadata, no-fetch,
legacy-link, count and rollback limitations. The configuration operations guide
owns concrete host/profile deployment and recovery; workspace deployment and
coordination guidance own the matching-input and claim contracts. Individual
rollout revisions/results belong in this initiative's state and rollout record,
not tracked configuration release reports. Routine pin selection introduces no
new public behavior requiring another project-doc change. No docs, anchors,
prerequisites, supported upgrade paths or recovery restrictions were removed by
the pins. Prepared deployment remains distinct from executed verification.

I independently passed all three base-to-head `git diff --check` checks and the
workspace deployment checker against the final locks. Inspected semantic lock
diffs, effective dependency graphs, channel ownership, actual aitherdev imports,
commit messages and complete histories. Prior application tests, package build
and CI are recorded in state and were not repeated for this pin review.

Composed package/host builds, dry activation and live verification remain pending.
They must prove the actual final rebased source, exact system and profile paths,
portal health, real Linux metadata/content, naming and native daemon continuity.
This review does not establish those operational results or remote integration
proof. No heavy tests, deployment, merge, claim or lifecycle operation was run.
