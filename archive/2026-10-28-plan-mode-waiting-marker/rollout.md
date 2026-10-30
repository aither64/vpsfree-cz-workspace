# Aitherdev rollout

## Scope and authority

User steering in this conversation: "aitherdev can be deployed using
vpsfree-cz-configuration". Prepare matching configuration/workspace composition,
then deploy the waiting-title fix after completed review and checks. Integration
approval remains separate and absent. No session closure authorized.

Machine catalog: `vpsfree:aitherdev`, alias `aitherdev`,
`aitherdev.int.vpsfree.cz`, selector `cz.vpsfree/machines/aitherdev`;
configuration repo `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`,
target `refs/heads/master`. Profile machine is the same physical machine.
Selected runtime guide read from
`/nix/store/d0wikyzpr7qk1w2c2zbqgj97qz1m58qn-dev-workspace-0.2.0`.

## Prepared source heads

- codex-web `9d337b70987fdf1dd42a5d8efff31f755a122550`, target master,
  `git@github.com:aither64/codex-web.git`.
- dev-workspace `5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3`, target master,
  `git@github.com:aither64/dev-workspace.git`.
- Workspace/config feature heads, complete input graphs, exact system/profile
  paths: pending deployment design and pin preparation.

## Gates and order

- Source independent final review pending; quick checks pass.
- Architect0 preparing bounded composition and rollout addendum.
- Implementer1 will prepare required exact pins and checks after design.
- Build/copy before acquiring machine where supported; no current claim.
- Acquire only the physical machine near activation, recheck exact held claim.
- System activation only if required by actual change; verify current-system and
  system profile after confctl dry-activate/no-reboot switch, keeping rollback.
- Application from workspace user profile; matching direct nested runtime input,
  preserved extension/native/unrelated inputs and deployment checker required.
- workspace-host switch requires DEV_WORKSPACE_CLAIM_ID and both exact session
  environment values. Preserve active threads/guests and transition journals.
- Verify portal health, naming/conversation continuity and real background Plan
  question marker, focus acknowledgement, answer/resolution.

## Recovery and release

Application recovery is a corrected compatible forward package; do not select an
older profile or manipulate private journals to bypass a refusal. Inspect all
unfinished or uncertain command effects before any further action.

Release the exact owned machine claim only after deployment/effects verified
and complete deployed feature lineage integrated into approved remote defaults,
including dependencies. Fresh remote ancestry/equivalence evidence belongs here.
No integration approval yet. Verify authoritative claim status before release,
release and verify resulting state. Do not await separate UI acceptance once
conditions hold. A later deployment needs a fresh claim. Machine release never
closes this session.

## Design checkpoint before preparation

Architect deployment addendum accepted in [design.md](design.md). At its read-only
checkpoint, live and persisted system links both resolve to
`/nix/store/fczhh0f76j8sy2awv7skrv2rp59vr7lg-nixos-system-aitherdev-26.05.20261026.718f670`.
Recheck at activation. Config baseline `584691d9b96ce1555a5787a0a1d999eeb528811f`;
workspace baseline `1085b570dc27d7250faa94ae893f9f8ffd04c45c` includes initial
tracking. Extension `767dfd587e346168e1443e65ccdb67ce748f3fe3` must remain.
Implementer1 owns only exact runtime selections and preparation evidence.
Source final independent review has no findings; required source suites running.
No claims or activations have run.

Prepared machine-only request file (not submitted/acquired):
`logs/deployment-machine-request.json`, request ID
`9f7c56fb-7e03-40cf-9fb7-a5d567c1db0d`, machine alias aitherdev.
Submit near activation after builds/copies; authoritative status must report
held before dry activation/profile selection. No repository resource bundled.

Published deployment heads for independent review:
workspace `398dc7bab89ee51bcc77d23a5acc52c7e02878c1` (functional base 1085b570d,
remote master 5fc7000f plus initial tracking) and config
`b3b933bf6f9fc9f7f533b3f4e06775defd8879da` (base 584691d9). Both select
runtime 5f4f1c1c / codex-web 9d337b7; semantic graph/checker passes, extension,
native and sibling edges/follows unchanged. Candidate system output reportedly
differs current; exact metadata reconciliation pending before build/activation.

## Exact read-only candidate identities

Implementer1 verified explicit committed workspace git+file revision 398dc7bab
and sparse worktree evaluate the same application drv/output (warning is not
an actual source difference):

- App drv: `/nix/store/wxxdwf6ibjnhrfdvv3dx7gf2flhqp3x9-dev-workspace-0.2.0.drv`.
- App output: `/nix/store/g650vgjpzvyifjmb1j44pc5bby3522z4-dev-workspace-0.2.0`.
- System drv: `/nix/store/jzr4idz432cmmx95xixbqb1ppxl1yx1v-nixos-system-aitherdev-26.05.20261026.718f670.drv`.
- System output: `/nix/store/287h21qgjmfcnmbbclw20n2shw5y3mia-nixos-system-aitherdev-26.05.20261026.718f670`.
- Auto-rollback drv: `/nix/store/za41c9rsf8k0qv0ay8svf4kc4y2x0q51-auto-rollback.rb.drv`.
- Auto-rollback output: `/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb`.

Base configuration 584691d9 evaluates to the exact current fczhh0 system output;
therefore the runtime pin changes system derivation/output. Activation required
on that baseline after successful build/copy and difference inspection. These
are evaluation identities only, not successful builds or deployed results.

## Source-identity correction before any system build

Implementer1's final exact Git check found config path evaluation jzr/287 differs
from explicit committed Git revision evaluation ia5gh8wr/r4rd3qyn. Therefore
previous jzr/287 identity is **provisional and not authoritative for confctl**.
No build or activation used it. Implementer1 is reconciling the actual confctl
installable/source metadata; system build remains stopped until corrected.
Both candidates differ live, but only the ordinary confctl path can establish
its exact deployable generation. Application committed/sparse equivalence still
holds. Preserve this correction and the final resolved identities below.

## Resolved authoritative system identity

Implementer1 proved ordinary confctl's actual installable
`.#confctl.build.m_cz_vpsfree_machines_aitherdev_0b1e0938.toplevel` equals explicit
committed Git revision evaluation:

- **Authoritative system drv:** `/nix/store/ia5gh8wr85mp6crbgi16nwf7wn66zz80-nixos-system-aitherdev-26.05.20261026.718f670.drv`.
- **Authoritative system output:** `/nix/store/r4rd3qyn52z1bipbln8kdh43mjd2wb1k-nixos-system-aitherdev-26.05.20261026.718f670`.

Cause: path `builtins.getFlake(toString ./.)` omits Git revision metadata and
therefore `/etc/confctl/configuration-info.json`; ordinary committed Git input
includes it. Exact-vs-path etc inputs add only configuration-info derivation.
jzr/287 remains a superseded path-evaluation result, never deployed. Use actual
confctl build/generation metadata for later copies/activation. No source change
or build occurred during reconciliation; system-first activation still required.

## Bounded deployed acceptance

Implementer0 inspected existing support read-only. The notification browser
fixture replaces attention in disposable httptest TLS state and cannot target
the live portal. Native Plan controls are isolated ephemeral exact-binary tests,
not an application policy escape hatch. Current Default root has no blocking
request_user_input and no browser/computer-use tool. No new session/native thread,
retained settings mutation or live checkpoint injection is authorized/needed.

After activation verify selected profile/package, portal service ExecStart and
/proc/MainPID/exe against exact candidate; pinned `go version -m` proves runtime
codex-web pseudo-version. Check healthz and authenticated current session page,
attention and team-stats/activity for identity/freshness/absence of stale input.
Preserve actual composed regression evidence: passive native transport ->
ActivitySnapshot, portal attention reducer/API, 75-case browser title/focus/
resolution harness. Report deployed artifact/health and composed regression
separately. Live organic native Plan-question/focus/answer remains unverified
until a normal user Plan question occurs; no new test subsystem required.

## Application build passed

Fresh corrected build watcher2 reports exact immutable workspace398dc7bab build
passed exit0 in730s, output
`/nix/store/g650vgjpzvyifjmb1j44pc5bby3522z4-dev-workspace-0.2.0`, matching
expected wxxdwf6i derivation. Full log logs/composed-app-build-2.log and
logs/build-preparation-progress-2.json. Lead rooted the successful output at
logs/composed-application-root to retain it through remaining VM checks and
activation. This is a build, not profile selection; failed archive-check
reconciliation still gates deployment. System generation build now running.

## System build passed

Corrected watcher2 completed both commands and exited; no owned build remains.
Config b3b933bf build passed exit0 in115s, expected ia5gh8wr drv / r4rd3qyn output.
Confctl generation `2026-10-29--19-25-31`, metadata under configuration worktree
`.confctl/generations/cz.vpsfree:machines:aitherdev/2026-10-29--19-25-31/generation.json`.
Auto rollback output `/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb`.
Complete logs/progress in logs/*build-2.log and build-preparation-progress-2.json.
No copies/activation yet. New fresh remaining-source watcher native
`01a188eb-9750-73d0-b88c-27c360e980ce` (session11046), verified Luna/low,
danger-full-access/never, isolates exact archive first unchanged30s deadline;
if pass, finishes only two interrupted outputs and final cached aggregate.

## Built system closure difference

`nix store diff-closures` reported no package-version changes. Exact recursive
path-set comparison (logs/system-closure-diff.json) is stronger: both closures
contain1340 paths; only four paths differ: system output, etc tree,
/etc/confctl inputs-info JSON and configuration-info JSON. Kernel, initrd,
executables and service packages remain exact same closure paths. This is not
store-path equality; normal explicit-generation dry-activate/switch remains.
Supported closure-copy preparation started via `confctl deploy --generation
2026-10-29--19-25-31 --copy-only --yes ...`; no machine claim/activation yet.

Closure-copy preparation completed exit0; resolved generation was exactly
`2026-10-29--19-25-31`, kernel6.18.57, devWorkspace5f4f1c1c,
home-managerc47b2cc6, llm-agents91ff550f, nixpkgs718f670e. No activation occurred.
Confctl's explicit --copy-only command succeeded; no unfinished copy command.

## Pre-activation service baseline

Portal unit is `workspace-portal@vpsfree-cz.service`, active, MainPID467329,
ExecStart via selected profile workspace-host run-portal vpsfree-cz. Raw HTTPS
using default curl trust fails because the development CA is not in that bundle;
using public CA `/var/lib/dev-workspaces/public/ca.pem` validates TLS and returns
expected401 without Basic Auth. Direct private password read was denied and
sudo required a password; no credential read/exposure occurred and no access
control was changed. Use the owned portal Unix socket for backend acceptance.

GETs on `/run/user/1000/dev-workspaces/vpsfree-cz/portal.sock` with configured
canonical Host returned200 for healthz `{ok:true}`, current session page,
attention and team-stats. Attention fresh=true, event=null, rootThread matches
`01a188ac-a505-7372-acc3-c4c59cada380`. Compact baseline in
logs/predeploy-backend-checks.json. This verifies private backend plus external
TLS/auth gate separately, not authenticated browser rendering. Recheck after
activation with exact running binary/selected package identity.

## Fresh baseline check during remaining verification

SSH ls-remote confirmed defaults still equal reviewed bases: codex-web f6f4a187,
dev-workspace cc0d452a, configuration584691d9, workspace5fc7000f. Live system
still fczhh0 and selected package d0wikyz; no baseline drift or rebase needed.
This is not final merge ancestry proof or machine ownership. Recheck immediately
before activation and any separately approved integration.

## Repeated local verification failure

Exact isolated archive failed again at initial open-page hydration before any
archive click/POST. Batch stopped; interrupted creation/recovery and aggregate
were not run. No machine claim/activation. Implementer0 now owns a narrow
existing-fixture diagnostic edit with unchanged30s acceptance and production
source. Planned production head/pins/built outputs remain5f/9d and398/b3.
Reviewer must assess diagnostic successor before long diagnostic run; existing
source/pin reviews retained. Existing Nix test function {pkgs,self} may permit
new committed fixture diagnostics against exact old5f runtime/package dependencies;
implementer is checking that natural parameterization, no new framework.

## Authenticated external baseline and deployment access

Read-only SSH root@172.16.106.40 returned uid0, confirming normal deployment
connectivity. Using the installed Nix Python path (root PATH lacks python3),
a remote Python process read Basic Auth only into memory, used the configured
public CA and requested canonical HTTPS health/session/attention. All returned200,
healthok=true, attentionfresh=true/eventnull/exact root thread. No credential
value/header was printed, saved or transferred in output. This verifies the
full TLS/auth/nginx/backend path, supplementing the owned-socket baseline.
No claim/activation occurred; recovery acceptance remains running.

## Executed activation and verified effects

Machine-only claim9f7c56fb-7e03-40cf-9fb7-a5d567c1db0d was held and rechecked
before mutation. Lead driver started19:44:25UTC, completed19:45:57UTC, both
subprocesses exit0. System activation33.61s used explicit generation,
--dry-activate-first, --no-reboot and configured auto rollback; confctl reported
systemd running/firewall active,2health checks passed. Both live and persisted
system links are exactly r4rd3qyn output above. Application activation57.29s
used ordinary workspace-host switch with exact session/claim env, selected g650
above and passed native/local semantic protocol contracts (Codex0.165.0).
Raw status and logs: logs/deployment-driver-status.json, system-activation.log,
application-activation.log. Observation-only watcher ended; no mutation remains.

Post-activation portal unit active, MainPID4041906; /proc/PID/exe resolves exactly
g650/bin/workspace-portal. Pinned Go build info reads codex-web
v0.0.0-20261029173332-9d337b70987f from the running binary. Authenticated canonical
HTTPS health/session/attention/team-stats return200; healthok, attentionfresh,
no stale input, rootThread01a188ac-a505-7372-acc3-c4c59cada380 unchanged. This
conversation continued through selection and dev-session current still matches.

Naming-only childPID4042171 is owned by portal, exact packaged Codex0.165.0,
with a live owned Unix socket. Authenticated ordinary /api/models returned200
and9models; /api/codex-providers returned200 with provider/active/default state.
This is process/socket/provider/catalog availability, not positive inference.
docs/session-preparations.md says a real positive naming canary is optional and
requires separate authorization; no canary or session-creation POST was made.
No managed session/settings/private creation record was created or changed for
verification. Live organic Plan question/focus/answer remains unexercised; the
composed native/attention/browser regressions cover the marker behavior.

## Integration and reservation at handoff

Fresh SSH refs confirm final published heads9d337b7/08f3dbb9/398dc7bab/b3b933bf
and unchanged configured master targets. Exact local ancestry checks against
those fresh remote targets prove deployed feature lineage is not yet integrated.
Production runtime5f4f1c1c is literally an ancestor of final source08f3dbb9;
no rewritten/nonancestor equivalence claim is needed. Source08 changes diagnostics
only and was independently reviewed; production pins intentionally remain5f.

Integration approval is absent. **Keep machine claim held** until separate
explicit approval and integration of all four reviewed final branches into their
master targets, then fresh remote ancestry plus claim status/effect reconciliation.
Release promptly once those conditions hold; no separate UI smoke acceptance is
required. No archive/delete/stop/session cleanup is authorized or performed.

## Explicit integration approval

User message "ok, merge and release aitherdev" approves the four previously proposed repositories (codex-web, dev-workspace, workspace/aither64-vpsfree-cz-workspace, vpsfree-cz-configuration) into master and subsequent aitherdev reservation release. Previous awaiting-approval statements above are historical. No rebase/source changes planned; exact reviewed final heads retained. Session remains open.

## Approved integration verified

All four final reviewed heads fast-forwarded into approved remote masters with normal SSH pushes, unchanged history and no migrations. Configuration merge/push used pinned nix develop and active hooks; workspace integration held the nonblocking tracking lock and preserved unrelated work/index. Each repository-only claim released immediately after remote proof. Fresh final remote/ancestry evidence: logs/final-remote-lineage.json.

- codex-web: git@github.com:aither64/codex-web.git target refs/heads/master equals 9d337b70987fdf1dd42a5d8efff31f755a122550; final head is ancestor.
- dev-workspace: git@github.com:aither64/dev-workspace.git target refs/heads/master equals 08f3dbb92bc8585929edee85a824d44dfb3b0846; final head is ancestor.
- workspace: git@github.com:aither64/vpsfree-cz-workspace.git target refs/heads/master equals 398dc7bab89ee51bcc77d23a5acc52c7e02878c1; final head is ancestor.
- vpsfree-cz-configuration: git@github.com:vpsfreecz/vpsfree-cz-configuration.git target refs/heads/master equals b3b933bf6f9fc9f7f533b3f4e06775defd8879da; final head is ancestor.

Deployed runtime5f4f1c1c is literally an ancestor of integrated08f3dbb9 (diagnostic-only successor); codex-web9d and workspace398/configb3 are exact integrated deployed selections. Existing complete lock/source graphs and system/profile receipts remain authoritative. Live and system profile rechecked equal r4rd3qyn, selected application g650. All activation commands exited successfully; no unfinished or uncertain effects remain. Exact machine claim is next rechecked and released before post-merge CI.

## Machine released

At20:30:15UTC normal owner-only release of exact claim9f7c56fb-7e03-40cf-9fb7-a5d567c1db0d returned released revision2; subsequent authoritative claim-status confirmed released. Resource machine:vpsfree:aitherdev / aliases aitherdev, aitherdev.int.vpsfree.cz, cz.vpsfree/machines/aitherdev. All four integrated heads and deployed lineage verified before release; no unfinished effects. Repository claims are also released. Post-merge CI is observed separately with no reservation; no session archive/delete/stop/cleanup performed.
