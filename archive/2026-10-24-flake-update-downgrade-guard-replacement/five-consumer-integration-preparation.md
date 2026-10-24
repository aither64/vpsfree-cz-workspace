# Five consumer integration preparations

These are preparation handoffs, not integration results. The lead owns each
claim, fast-forward merge, non-force SSH default push, remote proof and release.
Actual integration outcomes belong in the root-owned integration receipts.
No claims, merges, default pushes, source edits, rebases, test reruns, CI waits,
authentication inspection, cleanup or lifecycle action were performed here.

Each detached target lives under the owned worktree group at
`<repository>-integration-target`, initially clean at its recorded base. Fresh
canonical SSH/fetch, exact reviewed complete series/full binary diff/lock, target
Nix environment and ordinary hooks were prepared one repository at a time.
All source remains bound to review6bb7af and inventory821181.

| Repository / target | Prepared base | Reviewed head | Per-repository plan/evidence |
| --- | --- | --- | --- |
| terraform-provider-vpsadmin / master | `2a2c10553` | `c3f20203a` | [ready/plan](verification/integration-preparation/terraform-provider-vpsadmin/plan.md) |
| vpsadminos / staging | `e2b2b9186` | `889f14e5f` | [ready/plan](verification/integration-preparation/vpsadminos/plan.md) |
| vpsf-status / master | `587cd65bb` | `018b700f0` | [ready/plan](verification/integration-preparation/vpsf-status/plan.md) |
| vpsfree-irc-bot / master | `94ac4eb5a` | `0a160463a` | [ready/plan](verification/integration-preparation/vpsfree-irc-bot/plan.md) |
| vpsadminos-org-configuration / master | `6b04b48e9` | `ca96c95a1` | [ready/plan](verification/integration-preparation/vpsadminos-org-configuration/plan.md) |

Terraform declares no hook framework and has no active Git hooks. vpsAdminOS,
IRC and org use ordinary installed/signed Overcommit; status uses its normal
`make hooks` Lefthook installation. Ruby repositories received distinct copies
of their already installed ignored gems, without copying caller Bundler
configuration. Org's exact generated `.bundle/config` path was already locally
ignored, so no exclusion change or source-ignore change was needed. No caller
environment sanitizer was introduced.

All five final comparisons are captured. Org's last capture succeeded after a
transient concurrent `dev-session` writer; refused attempts changed nothing.
Every per-repository ready receipt and plan is now handed to the lead for its
independent claim and critical section.

No uncertain package/kernel build occurred. Dependency dry-runs were inspected;
only ordinary small Nix shell helpers were realized where necessary. No duplicate
package/suite/live verification was run. The root must enter each declared
environment before claiming and inspect actual post-merge hook output even if
Git exits zero, then release before CI/records. All feature refs and roots remain.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
