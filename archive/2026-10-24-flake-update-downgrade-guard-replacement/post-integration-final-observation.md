# Final post-integration source and CI observation

All eight exact final heads are proven integrated: fresh canonical SSH defaults
and features match, ordinary tracking fetches resolve the same exact defaults,
and actual `git merge-base --is-ancestor` returned **0 for all eight**. Each
fetched default equals its exact final head. All feature worktrees are clean;
complete series, full-index binary diffs, trees and locks match the applicable
reviewed mapping. This is a post-integration observation, not another merge or
claim operation.

Observed through 2026-10-24T20:10:43.591989+00:00. Full [final inventory](verification/post-integration-final-observation/final-inventory.json)
and [source inventory](verification/post-integration-final-observation/source-inventory.json)
bind root integration-result hashes, source reviews, SSH/fetch command receipts,
actual ancestry exit codes and all artifact hashes. Per-repository subdirectories
retain raw stdout/stderr, exact command identities, full series/diff and proof.

| Repository / default | Exact integrated final head | Equality / ancestry exit | One default/head CI snapshot |
| --- | --- | --- | --- |
| confctl / master | `822c0e35dbe2549111912f539116b4225dfd3035` | yes / 0 | [RuboCop 40126408707](https://github.com/vpsfreecz/confctl/actions/runs/40126408707): success; [RSpec 40126408695](https://github.com/vpsfreecz/confctl/actions/runs/40126408695): success; [Tests 40126408616](https://github.com/vpsfreecz/confctl/actions/runs/40126408616): success |
| haveapi / master | `39909094649b1d14a23f00615775ca7136acf4fd` | yes / 0 | [servers/ruby RSpec 40127981557](https://github.com/vpsfreecz/haveapi/actions/runs/40127981557): success |
| terraform-provider-vpsadmin / master | `c3f20203a5ba6200d0ff6b77f500bff6473f2c11` | yes / 0 | [Go Tests 40127138641](https://github.com/vpsfreecz/terraform-provider-vpsadmin/actions/runs/40127138641): success |
| vpsadminos / staging | `889f14e5f964c85eac0dbffdff96909a46ab35c6` | yes / 0 | No matching default/head run observed |
| vpsf-status / master | `018b700f06cf216a125a70ac9bfedddaabf07b92` | yes / 0 | [i18n health 40127557048](https://github.com/vpsfreecz/vpsf-status/actions/runs/40127557048): success; [Integration Tests 40127557047](https://github.com/vpsfreecz/vpsf-status/actions/runs/40127557047): success |
| vpsfree-irc-bot / master | `0a160463a4ee12ec5f6c45e38eaba11592787d9f` | yes / 0 | [RSpec 40127636885](https://github.com/vpsfreecz/vpsfree-irc-bot/actions/runs/40127636885): success |
| vpsfree-cz-configuration / master | `25258cd3f483f0116dbab35c7acf89b16eff4bbc` | yes / 0 | No matching default/head run observed |
| vpsadminos-org-configuration / master | `ca96c95a1fee04793468785d8323a759615b2b4e` | yes / 0 | No matching default/head run observed |

Exactly one default-branch/exact-final-head CI query was made per repository
(limit 50 each). The snapshots contain **8 successful completed runs, no
pending runs and no failed runs**. vpsAdminOS and both configuration repositories
returned no matching run. That is an evidence limit, not a passing CI claim or
a claim about why no run appears. No second poll, CI wait, dispatch, rerun or
cancellation occurred. C's separately owned feature queries were not duplicated.
No failed run required log/artifact diagnosis in this observation.

HaveAPI and vpsFree configuration retain their independently reviewed successor
ranges under [focused refresh review](review-integration-refresh-report.md),
SHA256 `f55e7a94a6bbb5778e6958f2379d9e1ecba395d92c538a7d6f773cd618bd7a2a`.
Actual checks of their old heads against the fetched defaults returned 1. The
old heads remain preserved provenance; they are not claimed as literal ancestors
or runtime executions of the new successors. The other six retain the exact
original [Git-cache review](review-git-cache-report.md) mapping. No migration or
obsolete shipping history has appeared. The refreshed vpsFree lock equals its
reviewed new upstream baseline; no input update was performed here.

The provider R evidence ref remains exactly
`5436d3d7c36d3d5174eab3c44e3578830749d3db`. All feature refs, detached targets and
Nix roots were preserved. The accepted exact provider package 203/0/0 and
selected-path/cache/race evidence remain their original component/source-bound
receipts; no package, suite, live test or consumer fixture was rerun.

Prior integration/claim execution remains recorded by the root-owned
`verification/integration/*/result.json` receipts. In particular, Terraform's
existing local-merge/admission timing exception is preserved there; this
source/remote ancestry proof does not recertify that earlier timing.

All B observation commands finished and no B operation remains running. Only
ordinary remote-tracking fetch refs changed. No source/app/default/feature or
evidence ref mutation, authentication/configuration/environment read, claim,
deployment, cleanup or lifecycle action occurred. The lead alone owns session
state; this report does not mark the session complete or authorize archival.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
