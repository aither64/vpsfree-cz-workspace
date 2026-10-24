# Package C current source and verification handoff

HaveAPI target movement follow-up: the new master contains only a lockfile-policy
guidance addition. The exact patch-equivalent successor 74f1cef6 is based on 7ac977a2, passed
narrow independent review and focused checks/hooks, and is now published with
exact SSH proof and successful new-head Ruby CI40109905180. One fresh HaveAPI-
only real pattern remains for the lead after TF3. Prior baec8e58 and all original
source/proof receipts remain preserved.
[Current refresh report](package-c-haveapi-refresh-report.md) distinguishes the
local successor from the historical published-head snapshot below.

Latest accepted gate update: corrected real Git race passed (45 operations,
strict preservation true) and exact final status Integration 40105130350 passed.
[Retained receipt bindings](package-c-final-remaining-verification.json) preserve
those results without replacing the earlier bounded CI snapshot. Only Terraform
VM verification remains: its first attempt stopped before examples because an
evidence path exceeded the UNIX socket limit. The
[new fixed-argv short-state brief](package-c-r-terraform-smoke-2-brief.md) is
prepared for the lead's serialized watcher; no member retry ran.

All five final reviewed feature heads are published, clean and equal to fresh
SSH feature refs. Fresh target refs remain at the original bases. The single
bounded final source/CI observation is retained in
[package-c-final-source-ci-snapshot.json](package-c-final-source-ci-snapshot.json).
No source, default branch, pin, claim, deployment or lifecycle change occurred
while collecting it. Every project lock remains byte-identical to its base.

| Project | Target | Unchanged base | Current published head | Commits |
| --- | --- | --- | --- | --- |
| haveapi | master | `67fcd34ba506264a5c7ee2e8e18a88d221c6f469` | `baec8e58e11a4868a6c713e70d406709bb94c152` | 1 |
| terraform-provider-vpsadmin | master | `2a2c1055302f86f8e250f1d7e4c331d62012efe8` | `f835d63b14931712129771792039f645cf6a3305` | 1 |
| vpsadminos | staging | `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854` | `d86ea84e653e09bb1d47e21f6b219406c5462906` | 1 |
| vpsf-status | master | `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb` | `d4c816bbf7ad22b9b2dcb424c1f316b1d0b6c6aa` | 3 |
| vpsfree-irc-bot | master | `94ac4eb5a7caf0456fff7df86a44cae198463276` | `5b68640fdf0d52bbf5786c886d37d62db595e1a9` | 1 |

All workflows select the same provider R
`5436d3d7c36d3d5174eab3c44e3578830749d3db`; no runtime input was added.
The [final R review](review-r-report.md) and
[status test compatibility review](review-status-metrics-report.md) passed with
no findings, including complete history/pin/no-migrations conclusions. Status's
three independently useful commits are the adoption, pre-existing vendor-hash
bug correction and pre-existing metrics test compatibility correction. There
are no superseded pin, fixup or transitional migration commits. No migration,
persisted format change, release/deployment boundary or default integration
occurred. Full reviewed diffs/series/provenance remain in `review-r-c/`,
`review-status-metrics/` and the earlier frozen inventories.

Complete current series:

haveapi:

- `baec8e58e11a4868a6c713e70d406709bb94c152` ci: preserve flake input ancestry during automated updates

terraform-provider-vpsadmin:

- `f835d63b14931712129771792039f645cf6a3305` ci: require forward-only flake input updates

vpsadminos:

- `d86ea84e653e09bb1d47e21f6b219406c5462906` ci: guard automated flake updates with ancestry checks

vpsf-status:

- `ebb7e6a2252f5a7f61d06a5935bb4c88a6c1964e` Guard automated flake updates with commit ancestry checks
- `6b5e8a6089926112bfbb63a45413b886ee56e549` Fix dependency updater vendor hash replacement
- `d4c816bbf7ad22b9b2dcb424c1f316b1d0b6c6aa` Check metrics cache exclusion against exporter headers

vpsfree-irc-bot:

- `5b68640fdf0d52bbf5786c886d37d62db595e1a9` ci: preserve commit ancestry in automated flake updates

## Accepted real updater results

The lead accepted all seven complete real updater patterns on R. For C's five,
[exact hashed receipts](package-c-final-real-workflow-receipts.json) independently
bind the reviewed source head, manifest, driver, review, generated local heads,
final committed lock and all-zero command results:

- HaveAPI: 32 operations, exit 0; 87.3 seconds reported by the lead.
- Terraform: 32 operations, exit 0; 58.2 seconds reported by the lead.
- vpsAdminOS: 31 operations, exit 0; 110.5 seconds reported by the lead.
- IRC: 41 operations, exit 0, including its exact package/caller/hooks and
  unchanged auxiliary source consistency checks.
- Corrected status: 39 operations, exit 0; 214.3 seconds reported by the lead.
  Reviewed source d4c816b generated local head
  `27403b4b607046937a4cf10e17007f7a781fb928`; hooks, full Go tests, Nix build and
  final committed-HEAD lock validation passed. The earlier failed status attempt
  remains intact. Root supplied the watchers; implementer0 launched none.

Initial 40 mock scenarios, meaningful status helper/metrics compatibility
checks and ordinary hooks remain recorded in the previous reports. Real
provider source/package/check/input identity and all 197 exported examples are
retained by the lead. These are verification evidence, not merge approval.

## Bounded final CI observation

At the timestamp recorded in the snapshot:

- HaveAPI Ruby 40102844869: success.
- Terraform Go 40102865906: success.
- IRC RSpec 40102965672: success.
- Status i18n 40105130335: success; Integration 40105130350: in progress.
- vpsAdminOS: no matching push-triggered workflow.

No exact final-head failed run was present, so no new failure log investigation
was needed. The prior status P failure remains directly artifact-diagnosed in
[its evidence](package-c-status-prior-p-ci-diagnosis.json); its missing native
Perl prerequisite was corrected and sandbox-tested. The separate actual R
metrics-test failure was diagnosed from source/logs, fixed without production
changes and verified in the now-successful complete status pattern.
No CI wait, dispatch, rerun or cancellation was performed in this observation.
That snapshot remains unchanged. The lead subsequently retained exact-head
Integration success in verification/final-status-ci.json, now hash-bound by
package-c-final-remaining-verification.json. All triggered final-head CI is green.

## Remaining lead-owned gates

The actual Git race first attempt reached expected ordinary stale push rejection
1 and fresh-baseline guard rejection 3, but its final strict cleanliness
assertion failed on the expected .confctl/logs error log. Lock/index/HEAD/local
remote preservation and no owned process were reconciled read-only in
[the exact evidence](package-c-r-git-race-failure-reconciliation.json).
The [bounded successor](package-c-r-git-race-2-brief.md) passed in the exact new
root /tmp/flake-update-guard-git-race-r-2, with 45 operations and all strict
preservation assertions true. Root retained its receipt and complete command
logs under verification/git-race-r-success. Only the exact owned log-directory
exclusion was added; the failed first attempt remains intact. No application
or provider edit, external publication or member-launched retry occurred.

Only the Terraform workflows VM gate remains. Its first attempt stopped during
before-suite setup on a 125-byte UNIX socket path; none of the eight examples
ran. Native cleanup completed, source/index/lock stayed unchanged, and no owned
process or bound socket remains. The
[short-state fixed-launcher successor](package-c-r-terraform-smoke-2-brief.md)
uses 101-byte maximum native sockets and preserves the supported eight-example
selection, native networking and kernel escalation rule. Root alone launches
its serialized watcher; preparation does not claim a successful VM result. No additional C source work or runtime
command is pending with implementer0. The session remains active and open;
default integration requires separate explicit authorization.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
