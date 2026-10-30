# Managed-repository Ruby runner audit

Observed 2026-10-30; completed 17:14 UTC. Investigation only, owned by
implementer0. Session identity matched `dev-session current`, both environment
variables and the thread binding. No project edits, fetches, branches, commits,
tests, builds, reruns or external mutations were performed.

## Conclusions

- No additional **confirmed** instance of the Ubuntu 26.04 / exact Ruby 3.4.0
  download failure appeared in the inspected runs outside vpsadminos.
- **security-advisories is susceptible:** both RuboCop and RSpec pin `3.4.0`
  with `ruby/setup-ruby@v1` on `ubuntu-latest`. Their latest successful runs used
  Ubuntu 24.04, so those successes do not validate Ubuntu 26.04.
- **vpsadmin and HaveAPI RuboCop demonstrably pass on Ubuntu 26.04:** minor
  selectors resolved to Ruby 3.4.12 and 3.2.11 respectively. confctl also uses a
  minor selector and its latest run passed, but its runner log was unavailable.
- RuboCop also appears in HaveAPI's Rust-client workflow and the production
  configuration's daily updater; both obtain Ruby through Nix rather than
  `ruby/setup-ruby`, so the specific ruby-builder download failure does not apply.

The known-failure comparator is the architect's evidence for vpsadminos
[run 41072754123 / job 124120814797](https://github.com/vpsfreecz/vpsadminos/actions/runs/41072754123/job/124120814797):
head `05201326975fc19d20a545c52f651cce0420dbc9`, exact `3.4.0`, attempted
`ruby-3.4.0-ubuntu-26.04-x64.tar.gz`, HTTP 404; RuboCop skipped. The action explains
that newer images receive only the latest patch and identifies 3.4.12 / 3.4 as
available alternatives. This comparator was supplied by the lead, not
independently re-audited in this package.

## RuboCop and matching Ruby-setup exposure

Workflow links below are immutable current-default snapshots. All listed
workflow runner labels are `ubuntu-latest`; observed image versions come from
job logs, not from that moving label.

| Repository / workflow | Ruby selector and setup action | Latest run evidence | Classification for the reported failure |
| --- | --- | --- | --- |
| [vpsadmin / rubocop.yml](https://github.com/vpsfreecz/vpsadmin/blob/ac10a62f1cb0fc890378ae83cdf18dd0e29f049a/.github/workflows/rubocop.yml) | `.ruby-version` is `3.4.0`, but workflow uses `cut -d. -f1,2` → **3.4**; `ruby/setup-ruby@v1` | Latest overall [41081549557](https://github.com/vpsfreecz/vpsadmin/actions/runs/41081549557/job/124151697420), Oct 30, feature branch: **success**, Ubuntu **26.04.1**, image `20261025.179.1`, Ruby **3.4.12**, 2190 files inspected. Latest default [40531100501](https://github.com/vpsfreecz/vpsadmin/actions/runs/40531100501/job/122283799374), Oct 27: **success**, Ubuntu 24.04, Ruby 3.4.12. | **Unaffected in observed Ubuntu 26.04 run.** The exact file pin does not reach the action. |
| [HaveAPI / rubocop.yml](https://github.com/vpsfreecz/haveapi/blob/0e7166a0f8f15827bfac051666a53bf449e999ec/.github/workflows/rubocop.yml) | **3.2**; `ruby/setup-ruby@7f797815d8adceb1c412e7abefdd1ab4abc47a5f` (**v1.335.0**) | Latest default [41056402040](https://github.com/vpsfreecz/haveapi/actions/runs/41056402040/job/124064915203), Oct 30: **success**, Ubuntu **26.04.1**, image `20261025.179.1`, Ruby **3.2.11**, 427 files inspected. Latest overall [41056909576](https://github.com/vpsfreecz/haveapi/actions/runs/41056909576), same head/tag: success. | **Unaffected in observed Ubuntu 26.04 run.** v1.335.0 demonstrably handled this image; no evidence here of action-version incompatibility or the exact-patch 404. |
| [confctl / rubocop.yml](https://github.com/vpsfreecz/confctl/blob/822c0e35dbe2549111912f539116b4225dfd3035/.github/workflows/rubocop.yml) | **3.4**; `ruby/setup-ruby@v1` | Latest overall/default [40126408707](https://github.com/vpsfreecz/confctl/actions/runs/40126408707/job/120968685913), Oct 24: **success**. Runner image / resolved patch unknown: log endpoint returned HTTP 503 twice. | **No exact-patch exposure; latest successful.** Ubuntu 26.04 execution unverified. |
| [security-advisories / rubocop.yml](https://github.com/vpsfreecz/security-advisories/blob/e6ceb642878dd97546174217676d9861afc38d4e/.github/workflows/rubocop.yml) | **3.4.0 exact**; `ruby/setup-ruby@v1` | Latest overall/default [39434900122](https://github.com/vpsfreecz/security-advisories/actions/runs/39434900122/job/118669228677), Oct 20: **success**, Ubuntu **24.04.5**, image `20261018.339.1`; downloaded `ruby-3.4.0-ubuntu-24.04-x64.tar.gz`; runtime reports `ruby 3.4.0dev`. | **Susceptible**, not an observed Ubuntu 26.04 failure. Same exact-patch selector as comparator; latest execution predates image change. |
| [security-advisories / rspec.yml](https://github.com/vpsfreecz/security-advisories/blob/e6ceb642878dd97546174217676d9861afc38d4e/.github/workflows/rspec.yml) | **3.4.0 exact**; `ruby/setup-ruby@v1` | Latest overall/default [39434899895](https://github.com/vpsfreecz/security-advisories/actions/runs/39434899895/job/118669226042), Oct 20: **success**, Ubuntu **24.04.5**, same 3.4.0 asset/runtime as RuboCop. | **Susceptible**, despite workflow name being RSpec. No matching Ubuntu 26.04 failure observed. |
| [HaveAPI / clients-rust.yml](https://github.com/vpsfreecz/haveapi/blob/0e7166a0f8f15827bfac051666a53bf449e999ec/.github/workflows/clients-rust.yml) | Nix-selected Ruby (`nix develop .#client-rust`); **no setup-ruby**; `cachix/install-nix-action@v31.11.2` | Latest default [41056402068](https://github.com/vpsfreecz/haveapi/actions/runs/41056402068/job/124064915254), Oct 30: **success**, Ubuntu **26.04.1**, RuboCop 25 files / no offenses. Latest overall [41056909642](https://github.com/vpsfreecz/haveapi/actions/runs/41056909642), same head/tag: success. | **Unaffected by this setup-ruby asset failure**, observed pass on Ubuntu 26.04. |
| [vpsfree-cz-configuration / daily-update.yml](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627/.github/workflows/daily-update.yml) | Nix-selected Ruby; **no setup-ruby**; `cachix/install-nix-action@v31`; updater contains `bundle exec rubocop` | Latest overall/default [41044633201](https://github.com/vpsfreecz/vpsfree-cz-configuration/actions/runs/41044633201), Oct 30: **failure**; Oct 28 run [40674539688](https://github.com/vpsfreecz/vpsfree-cz-configuration/actions/runs/40674539688) succeeded. Failure not diagnosed further under the bounded scope. | **Outside this specific setup-ruby failure path.** Failed workflow is not evidence of the matching 404; actual runner image and RuboCop execution not established here. |

HaveAPI action-version evidence is separate from Ruby asset selection. The
successful RuboCop job logs the exact `7f797815...` action SHA, Ubuntu 26.04 and
Ruby 3.2.11. vpsadmin's successful Ubuntu 26.04 job resolves floating `@v1` to the
same SHA. This is direct compatibility evidence for those runs; action release
history and every older HaveAPI action pin were not audited.

## Other Ruby workflow selectors

These were inspected for exact patch exposure while reading every workflow.
Unrelated test runs were not expanded into separate failure investigations.

| Repository | Other Ruby workflow setup visible on current default |
| --- | --- |
| vpsadmin | `api-migration-specs.yml`, `api-specs.yml`, `console-router-specs.yml`, `download-mounter-specs.yml`, `daily-update.yml`: `ruby/setup-ruby@v1`, all derive **3.4** from `.ruby-version`. Other Ruby checks use Nix. |
| HaveAPI | `_ruby-rspec.yml` (called by server/client RSpec wrappers): **3.2 / 3.3 / 3.4**, pinned **v1.333.0** (`e1bd6146574da5e0795075b5319b300edb30c5b0`); JS and PHP integrations: **3.3**, pinned **v1.335.0**; Python integration: **3.3**, pinned **v1.330.0** (`a89e929fdc35d88f2b8f20f26452c4adbeb9e371`); i18n: **3.2**, floating **v1**. No exact old patch selector found. Older action pins have **unverified** Ubuntu 26.04 compatibility in this audit, distinct from the exact 3.4.0 asset failure. Release/performance/Rust jobs use Nix; performance runner is explicitly `ubuntu-24.04`. |
| confctl | `rspec.yml`: matrix **3.3 / 3.4 / 4.0**, `ruby/setup-ruby@v1`, `ubuntu-latest`. |
| ssh-exporter | `rspec.yml`: **3.4**, `ruby/setup-ruby@v1`, `ubuntu-latest`; latest [31189637404](https://github.com/vpsfreecz/ssh-exporter/actions/runs/31189637404), Aug 7, success; newer-image execution unverified. |
| syslog-exporter | `rspec.yml`: **3.4**, `ruby/setup-ruby@v1`, `ubuntu-latest`; latest [31189639318](https://github.com/vpsfreecz/syslog-exporter/actions/runs/31189639318), Aug 7, success; newer-image execution unverified. |
| vpsfree-irc-bot | RSpec and dependency update use Nix (`cachix/install-nix-action@v31`), not setup-ruby. Latest RSpec [40127636885](https://github.com/vpsfreecz/vpsfree-irc-bot/actions/runs/40127636885), Oct 24, success. |
| vpsadminos-org-configuration | Daily dependency updater invokes Bundler/Overcommit inside `nix develop`; no setup-ruby or direct RuboCop invocation in workflow. |

## Complete project-map coverage

All **23** managed projects other than explicitly excluded **vpsadminos** were
checked. Local canonical bare objects supplied the initial inventory/remotes;
no fetch was performed. The authoritative inventory used read-only GitHub API
repository metadata → current default branch ref → immutable SHA workflow
contents. This caught newer workflows absent from stale bare default heads,
including security-advisories' non-master default branch.

| Managed project | Default branch snapshot | Workflow files | Relevant coverage |
| --- | --- | ---: | --- |
| dev-workspace | [master @ 4155d0099d03](https://github.com/aither64/dev-workspace/tree/4155d0099d03028b43d5f08d225a88156cb4155a) | 1 | No setup-ruby or direct RuboCop invocation. |
| vpsfree-dev-workspace | [master @ 767dfd587e34](https://github.com/vpsfreecz/dev-workspace/tree/767dfd587e346168e1443e65ccdb67ce748f3fe3) | 2 | No setup-ruby or direct RuboCop invocation. |
| codex-web | [master @ 9d337b70987f](https://github.com/aither64/codex-web/tree/9d337b70987fdf1dd42a5d8efff31f755a122550) | 1 | No setup-ruby or direct RuboCop invocation. |
| vpsadmin | [master @ ac10a62f1cb0](https://github.com/vpsfreecz/vpsadmin/tree/ac10a62f1cb0fc890378ae83cdf18dd0e29f049a) | 12 | RuboCop + other Ruby setups covered above. |
| security-advisories | [2026-07-13-security-advisory-automation @ e6ceb642878d](https://github.com/vpsfreecz/security-advisories/tree/e6ceb642878dd97546174217676d9861afc38d4e) | 2 | RuboCop and RSpec exact 3.4.0 pins; covered above. |
| vpsfree-kb-contracts | [master @ ce2c8cd9358c](https://github.com/vpsfreecz/vpsfree-kb-contracts/tree/ce2c8cd9358c3636e5d39343e595df813a0b197f) | 2 | No setup-ruby or direct RuboCop invocation. |
| ruby-lxc | [vpsfree @ df19e1f287da](https://github.com/vpsfreecz/ruby-lxc/tree/df19e1f287da338324db4dee6a2bac8340fc1154) | 0 | No GitHub workflow directory. |
| haveapi | [master @ 0e7166a0f8f1](https://github.com/vpsfreecz/haveapi/tree/0e7166a0f8f15827bfac051666a53bf449e999ec) | 13 | RuboCop, Rust RuboCop and Ruby setup inventory covered above. |
| vpsf-status | [master @ 3e941289c7c9](https://github.com/vpsfreecz/vpsf-status/tree/3e941289c7c90536b70a0fb8c4a9888028355657) | 3 | No setup-ruby or direct RuboCop invocation. |
| vpsadmin-go-client | [master @ 134a9e69f9aa](https://github.com/vpsfreecz/vpsadmin-go-client/tree/134a9e69f9aa6ddec5c94b53744865c6f81ecdd0) | 0 | No GitHub workflow directory. |
| confctl | [master @ 822c0e35dbe2](https://github.com/vpsfreecz/confctl/tree/822c0e35dbe2549111912f539116b4225dfd3035) | 3 | RuboCop and RSpec minor selectors covered above. |
| vpsfree-cz-configuration | [master @ fcc7fc97be79](https://github.com/vpsfreecz/vpsfree-cz-configuration/tree/fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627) | 1 | Nix daily updater contains direct RuboCop; covered above. |
| vpsadminos-org-configuration | [master @ ca96c95a1fee](https://github.com/vpsfreecz/vpsadminos-org-configuration/tree/ca96c95a1fee04793468785d8323a759615b2b4e) | 1 | Nix/Bundler updater; no setup-ruby. |
| vpsfree-irc-bot | [master @ 9439adb63a35](https://github.com/vpsfreecz/vpsfree-irc-bot/tree/9439adb63a35e2426dde8814d25ee814c42a5e84) | 4 | Nix RSpec/updater; no setup-ruby. |
| vpsfree-mail-templates | [master @ 2cfd218d9152](https://github.com/vpsfreecz/vpsfree-notification-templates/tree/2cfd218d9152888feea4109f064459078ea9f76e) | 1 | Remote redirects to vpsfree-notification-templates; no setup-ruby/direct RuboCop. |
| terraform-provider-vpsadmin | [master @ 134aaa02f9ec](https://github.com/vpsfreecz/terraform-provider-vpsadmin/tree/134aaa02f9ec97ac6e756df6fa91a96055c48374) | 4 | No setup-ruby or direct RuboCop invocation. |
| web | [master @ 307635a96bc3](https://github.com/vpsfreecz/web/tree/307635a96bc3532af51ff5d08206d920704eee00) | 1 | No setup-ruby or direct RuboCop invocation. |
| ssh-exporter | [master @ c1b481a68e00](https://github.com/vpsfreecz/ssh-exporter/tree/c1b481a68e00d90802aeb36730c68a19f3c17711) | 1 | Ruby RSpec minor selector covered above. |
| syslog-exporter | [master @ 7c5a8e74e44a](https://github.com/vpsfreecz/syslog-exporter/tree/7c5a8e74e44a704cceb99cd05716af6800d78efd) | 1 | Ruby RSpec minor selector covered above. |
| vpsfree-client | [master @ 56357098b914](https://github.com/vpsfreecz/vpsfree-client/tree/56357098b914e19d3a0f2ed34896e5dbbd802e21) | 0 | No GitHub workflow directory. |
| vpsfree-maintenance-tasks | [master @ 2fdc9f2889ac](https://github.com/vpsfreecz/vpsfree-maintenance-tasks/tree/2fdc9f2889ac419136cd0cde0e0955c015ae7107) | 0 | No GitHub workflow directory. |
| linux | [vpsadminos-6.12 @ 9ccd5d6597a6](https://github.com/vpsfreecz/linux/tree/9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd) | 0 | Default branch workflow inventory only, no kernel work; no workflow directory. |
| zfs | [vpsadminos-release-next @ 481845fca6ae](https://github.com/vpsfreecz/zfs/tree/481845fca6ae3f61ca2262c1a5693a58ae364650) | 6 | Default branch workflow inventory only, no ZFS work; no setup-ruby/direct RuboCop. |

## Evidence boundary and reproducibility

GET endpoints used: `repos/<owner>/<repo>`, `git/ref/heads/<default>`,
`contents/.github/workflows?ref=<head>`, each workflow's contents at that SHA,
`actions/workflows/<file>/runs?per_page=10`, selected `actions/runs/<id>/jobs`,
and selected `actions/jobs/<id>/logs`. Recent detailed run inspection focused on
RuboCop workflows and the matching security-advisories RSpec setup; additional
Ruby-only workflow runs were sampled only where noted. This is not an exhaustive
historical-run audit. Absence of setup-ruby means absence of this binary download
path, not proof that every transitive Nix check or future runner update succeeds.
Repositories outside the workspace project map were not included, even if a bare
clone exists. RuboCop invoked transitively by generic Nix checks/hooks was not
expanded beyond visible workflow commands and inspected logs.

Compact conclusions are retained here. Disposable API responses and selected
logs were held in `/tmp/rubocop-audit-implementer0`. After the lead accepted this
report, implementer0 verified ownership and absence of running command, working
directory or open-file references, then removed that disposable directory.
The complete Markdown evidence and immutable source and run/job links above
remain available; this investigation package is complete. GitHub CLI refused ANSI-containing
job logs until its documented `gh api --allow-escape-sequences` flag was used;
retrieved logs were captured and ANSI-stripped before selective evidence output.
confctl's repeated HTTP 503 is the only unresolved log-access gap in the primary
RuboCop table.

Suggestions only: consider using the existing minor-series pattern for
security-advisories' two exact `3.4.0` workflow pins, alongside the vpsadminos
recommendation. No fix, workflow rerun or action upgrade was requested or made.

Session portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-rubocop-runner-compatibility/
