# I1 verification and retained review-runtime evidence

## Configuration vpsAdmin channel — generated, checked and published

The resumed package now pins root's SSH-verified merged vpsAdmin source
`99207a8dcd92f5907c52dbc99af52b30aa7ecac1` (API tree
`3f3cd9a11eec7d8694bc6c1777adf708239a56c3`). Configuration's fresh remote master
remained the clean prepared base `2f470c0fe7745d7dcebfba382df28e9ad367a884`, so
no rebase was required. Final feature head is
`2f264616638f4baa464692c02bea9ea76d7ffdde`, tree
`8880e91d90729afb6137557d4f5b7a32c7ff4b0d`. Its complete one-commit series is
`inputs: update vpsadminServices to 99207a8d`.

The first normal pinned-shell `confctl inputs channel update --commit vpsadmin
vpsadmin` completed exit0/39.410s, handle38499. `GIT_EDITOR=true`/`EDITOR=true`
preserved the generated message noninteractively. Precommit/Nixfmt and commit-msg
hooks passed; generated72-column advisories were retained. The useful changelog
contains the four integrated API/PHP/test/menu commits. No message rewrite,
manual lock edit, hook bypass or unrelated dependency update occurred.

The complete delta is only `flake.lock`,3 insertions/3 deletions. Only the existing
`vpsadminServices` node's `locked.rev`, `lastModified` and `narHash` change;
no nodes were added/deleted. All sibling/transitive nodes, originals and follows
remain equal. Final hash is `sha256-DD4ivXsh7taeFo18M3lgXJuNUqrWfl5lyOM/oFo/krE=`.
Existing WebUI/vpsAdmin and notification-template/vpsAdmin follows resolve the
new service input as expected; their channels were not independently updated.

Bounded validation13261 passed exit0/29.922s: normal `confctl inputs check-update`
against retained baseline, exact `vpsadmin` channel list, direct Nix mapping/revision/
NAR evaluation and whitespace check. The evaluated mapping remains
`vpsadmin/vpsadmin` → `vpsadminServices`, exact revision99207. No package/system
build, deployment/dry-activation, broad tests or full CI wait was run.

Normal pinned-shell SSH publication89657 exited0. Fresh `ls-remote` proves
`refs/heads/2026-11-25-backup-disable-design` equals exact2f264616 and remote
`master` remains exact2f470c0f. Feature and prepared detached target are clean.
The target is
`worktrees/2026-11-25-backup-disable-design/vpsfree-cz-configuration-integration-target-20261126`
at2f470c0f. Its existing normal checkout hook and own Bundler setup passed; no
refresh was needed. Enter `nix develop --no-write-lock-file --command bash`
before root's claim, then use normal root-owned fresh checks/FF/push/proof.
Overcommit0.76.0/signature verification1 and all normal hooks remain active;
Gemfile.lock/hook/config bytes are unchanged. Public session CLI stays outside
project GEM_PATH, as established by the accepted registration recovery.

Exact base/head/tree, full generated message/series/diff, lock comparison, hook
identities/trust, resolved source, command logs, prepared target and remote proof
are in `i1-configuration-final-receipt.json`, `i1-configuration-final.diff`,
`i1-configuration-{update,validation}.log` and retained baseline/final locks.
The prior `i1-configuration-prep-receipt.json` preserves the diagnosed startup
refusal and successful normal existing-registration recovery without recreation.

This is one mechanical generated pin stream with no migrations, fixups, repeated
updates, host/module changes or new logic; standalone content review is exempt,
subject to root's final complete history/diff assessment. No new project docs are
needed for this ordinary channel update. Current source defines only scheduled/
manual Daily update workflow166934900; no applicable push/spec workflow wait was
introduced. Root retains comparison capture, claim, default integration and CI
observation. All I1 update/check/publish/read handles are terminal/joined, with no
active utility or unknown effect. Source/fix ownership remains I1; no deployment,
workspace-package, cluster, service, lifecycle or cleanup action occurred.

## Infra integration preparation — published, root merge handoff

The lead released these two independent infra branches for integration preparation
under the user's explicit all-initiative merge instruction. Root retains comparison
capture, independent mechanical-equivalence acceptance/certificate, short claims,
final default comparison/merge/push and CI observation. This packet performs no
merge, deployment, selected-package switch or cluster operation.

| Repository / SSH origin | Fresh target → published final head / tree |
| --- | --- |
| `dev-workspace` / `git@github.com:aither64/dev-workspace.git` | `master` `2a1d58df7c3bb845da4d286ef38989bae01da4a0` → `009e90de32cb926b97f5994c6a46fbeab68c4743`; tree `4a9e89eae30086137fe3ee48e284164cbd199e54` |
| `vpsfree-dev-workspace` / `git@github.com:vpsfreecz/dev-workspace.git` | `master` `bf12ac71a8a00b1581eed5352f99c1b2daaeff5b` → unchanged `39e7a09eb6afbf14fc5a6b6bea74fd1c0a568b55`; tree `24bdf603f7b7d4951e28198715c7c59a959d2920` |

Both feature refs are `refs/heads/2026-11-25-backup-disable-design`.
Ordinary SSH pushes succeeded; fresh `ls-remote` verified both exact feature heads
and targets above. Feature and prepared target worktrees are clean. Generic master
advanced nine commits; the ordinary conflict-free rebase preserves its one reviewed
commit. `range-diff` reports `15511ef8 = 009e90de`; stable patch IDs both equal
`f57c36a02806488c84dbc0b8e0d3ab294d0df5dd`. `git merge-tree --write-tree
15511ef8 2a1d58df` reconstructs the exact final tree above. The reviewed head is
retained at `refs/heads/2026-11-25-backup-disable-design-reviewed-15511ef8`.
The provider needed no rebase; its A1-reviewed predecessor ref is retained.

Complete final series: generic `009e90de host: preserve standard streams for
cluster SSH`; provider `39e7a09e devcluster: prepare React sources before first
boot`. Generic remains three paths,117+/4-; provider only its README,28+.
No obsolete/fixup commits, migrations, repeated dependency/generated-input streams,
pin changes or deployed infra lineage exist. The relevant SSH dispatch, guard,
interactive, streaming and capture helper methods are byte-equal to reviewed
15511ef8. Upstream's host changes concern separate Pi transition compatibility;
its other documentation/monitor/UI changes do not alter this patch. `flake.nix`,
`flake.lock` and the affected test fragment/helper inputs are unchanged upstream.

Both Ruby syntax checks and the exact32-method fragment selection through the
normal aggregate entrypoint PASS on the rebased head:420 assertions, zero
failures/errors/skips,12.588083s test time; full inline batch52.999s. Both whitespace
checks PASS. Exact argv, outputs and SHA are retained in
`i1-integration-prep-quick.log` and `i1-integration-prep-packet.json`.
Provider unchanged review/organization-source evidence retains its exact scope;
no unchanged provider test was rerun. The prior four-lane reviewer0/Sol/xhigh
acceptance and direct narrow A1 acceptance remain the review basis; root owns the
independent reconstruction/certificate for the mechanical generic refresh.

The historical736.836s package PASS applies to exact15511ef8 only. A changed full
package derivation is not claimed equal or passed on009e90de. No new package build
or full CI wait was run, as directed for this specs-only integration release.
Historical raw JSON/log receipts linked below are unavailable in the present
tracking directory; the accepted Markdown record remains. They have not been
silently replaced with fresh or reconstructed execution evidence.

Prepared detached targets under `worktrees/2026-11-25-backup-disable-design/`:
`dev-workspace-integration-target-20261126` at2a1d58df and
`vpsfree-dev-workspace-integration-target-20261126` atbf12ac71. Their normal pinned
Git/Ruby environments were entered successfully; neither repository declares a
hook framework, installs executable hooks or overrides `core.hooksPath`. No hook
was disabled. Root should enter the cached environment before taking each claim:

```sh
# Generic target, then root's normal claim/freshness/ff-only merge/push/proof.
nix develop --no-write-lock-file --command bash
# Provider target has no declared devShell; use its pinned nixpkgs tools.
nix shell --no-write-lock-file --inputs-from . nixpkgs#git nixpkgs#ruby --command bash
```

Actual workflow identities: generic `Check` ID354263807, feature run45886262132
(head009e90de); automatic jobs `Essential application contracts` and `Session
creation smoke`, other three jobs manual-only. Provider `Check` ID355130097,
feature run45886260143 (head39e7a09e), job `flake`; `Host migration` ID355898750
has a path filter excluding this README-only patch. One metadata read supplied
these IDs; no polling, waiting, dispatch or cancellation was performed. Root owns
which relevant spec job to observe and the user-directed wait boundary.

Complete series, full binary diffs, range-diff, workflow blobs/IDs, exact remotes,
cleanliness, relevant-method equality, environment paths and effects are in
`i1-integration-prep-packet.json` and its linked `i1-integration-prep-*.diff` files.
Project docs remain the accepted provider how-to and generic provider-contract
reference; no new project-doc change is needed for this unchanged patch refresh.
All fetch/rebase/quick/environment/push/read handles are terminal/joined; no active
utility or unknown effect remains. Retained source/fix ownership remains I1.
Next dependency is root acceptance and normal integration drivers; no I1 default
branch or runtime action is authorized by this packet. The cluster stays released;
the session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-backup-disable-design/ .

## Dev cluster stopped and released — accepted terminal outcome

The user explicitly requested stopping and releasing this session's dev cluster.
Root executed only the normal exact-resource drivers: current refresh3 edge then
BFF registered stops (driver51266, both0), registered Vite5187 stop99611 exit0,
normal provider stop74201 exit0, and normal public provider reset1123 exit0.
The selected runtime guide's release-cluster contract maps portal Release to
`reset <slug>`; root read that exact contract and the provider's removal extent
before release. Reset was the requested cluster Release, not session reset,
archive or deletion. No physical-machine claim was substituted.

Before cluster stop, the single remote read28093 proved exact edge Invocation
`97cd725e5dd643aa9d690a034d7aa3f2` and BFF Invocation
`a19c353cba1f407ebc1910af1bcb8a3c` terminal/MainPID0/inactive/dead, units and
recorded cgroups absent. Receipt: `i1-react-runtime-prep/cluster-stop-remote-proof.json`.
The registered Vite row was linked by its existing argv to own
`i4-logs/vite-c723f2fa.sh`, which ran the same-session legacy preview at127.0.0.1:5187.
No unregistered or foreign process was discovered or adopted.

The one final local verification batch49025 joined exit0 at
2026-11-26T11:10:42Z. Supported provider status returned schema2/kindvpsadmin/
`found:false`; the exact directory
`/home/aither/workspace/ai/vpsfree.cz/.dev-clusters/vpsadmin/clusters/2026-11-25-backup-disable-design`
and recorded socket directory `/tmp/vpsfree-devcluster-0d0960cb6876` are absent.
Runner1656251, all five previously bound guest PIDs and current refresh3 host/SSH
owners are absent; no local Unix sockets reference the recorded namespace.
Current edge `383bd08d-ec47-4e94-ac15-3eaa07837154`, BFF
`203cb011-868e-401f-a28b-3ec4ad386e40` and Vite
`7b8cc3d8-157b-4cf3-a945-7ad8bdb36909` are stopped/retired, with no running or
unknown registered preview. The historical failed-first row `2b7078f3` remains
untouched: its exact local unit has MainPID0/empty ControlGroup and the recorded
cgroup is absent. It is retained failure history, not a running resource.

Safe final receipt: `i1-react-runtime-prep/cluster-release-final-verification.json`.
All root drivers and I1 observation handles are terminal/joined; no active
operation, held utility or unknown effect remains. Lead accepted the complete
stop/release verification. The logical resource is provider vpsadmin + canonical
workspace + this exact slug/recorded socket; the selected contract has no separate
address-reservation row or additional release command. No further claim action
is pending.

Normal Release intrinsically removed this cluster's retained guest disks, current
backend data, configuration, applied/provenance roots inside the cluster directory
and socket namespace. Historical running/data/private-guest-state assertions below
describe their original checkpoints, not current resources. Source worktrees,
session tracking/evidence, SDK/UI artifacts, local app roots and Git refs outside
the released cluster were not targeted. Provider-common certificate/SSH state was
outside the removal scope. I1 made no guest call after stop, retry, manual cleanup,
source edit, credential operation, session archive/delete or other-resource change.

This package is PARKED with I1 recovery/fix ownership retained. Source/prevention
and original storage verification remain parked; no further status/check/runtime
action or cleanup is pending from I1. The session remains open.

## Historical React refresh3 — healthy before requested cluster release

Root executed the ordinary development refresh for corrected defaults: exact
refresh2 edge→BFF stop driver89674 returned both0; reconciliation57484 proves
edge Invocation `45586e7a6b00493fa73744195b238d3f` and BFF Invocation
`56075bd161e841218a0bb0922b69f061` terminal/MainPID0/inactive/cgroups absent.
Ordinary admission records fresh selected generation
`/nix/store/3y9ns5h3raj9zszrwcr5pgvf9gng8q4b-dev-workspace-0.2.0`, exact input
hash `e70dd59a6546c396fcb76a7954cc408f228769d9e4ee35addaf6b355a39d2bea` and
clean reviewed source `39a1f17ce859600d10276da0fe29bfb1593c8132`, tree
`2709241c82f0b0a314d3699ac9f8570c5b3a1233`. No peer-switch receipt was needed.

The exact active pair is frontend
`/nix/store/59ynv5gwz6b3s0ddnpzdggzg718d2vfb-vpsadmin-webui-frontend-1.0.0` and BFF
`/nix/store/jxscjby6p1dh2jyv6nr9b7yvrmprbcdg-vpsadmin-webui-bff-0.1.0`.
Root stage42819/supervisor4162821 exited0, final phase
`apps-rooted-staged-no-service-or-firewall-activation`. The60-path full closure
was exported/imported through the accepted mounted-file/daemon route, with full
validity/equality/metadata/root checks and config staging. NAR271544136bytes,
SHA256 `d77ea0ff0e8aaaf9a242829e2476bd1975e272715be363ba3cf30c74c26dadfc`;
runtime manifest SHA256
`859f67859d4f4a70f4b116708612b8a1225672c6e4434ac7bbacf032f0586fe3`.
Host roots/receipts use `app-stage-refresh3`; guest roots use
`/nix/var/nix/gcroots/vpsadmin-review-ac1f7e2d-refresh3-{frontend,bff}`. All old
roots/payloads/failed and stopped-attempt evidence remain retained.

| Live component | Registration; host owner / SSH PID=PGID | Guest unit; InvocationID | Main PID / actual UID |
| --- | --- | --- | --- |
| BFF refresh3 | `203cb011-868e-401f-a28b-3ec4ad386e40`;4166830 /4166885 | `vpsadmin-review-bff-ac1f7e2d-refresh3.service`; `a19c353cba1f407ebc1910af1bcb8a3c` | 181297 /65292 |
| Edge refresh3 | `383bd08d-ec47-4e94-ac15-3eaa07837154`;4176447 /4176506 | `vpsadmin-review-edge-ac1f7e2d-refresh3.service`; `97cd725e5dd643aa9d690a034d7aa3f2` | 181707 /62523 |

Both exact registrations are running; identity-bound guest units are
active/running with populated owned system.slice cgroups and DynamicUser=yes.
Actual pinned Node24.21.0 executes exact jxsc BFF `server.js`; nginx1.30.7 uses
the exact refresh3 prefix/config/daemon-off argv. Typed credential counts are
3BFF/2edge and recorded edge ExecStartPre `nginx -t` exited0. Host/SSH owners are
present with start receipts and no exit receipts, as expected while retained.

BFF canonical-Host/forwarded-HTTPS loopback health returned200. Strict existing
CA/hostname TLS returned200 for health, exact full clean39a1 metadata, bound API
URL/7.0/HaveAPI auth header/`_meta` config and prescribed same-origin session with
exactly three null anonymous fields. Config/session no-store, single nosniff and
single same-origin CORP passed. Safe receipts are
`i1-react-runtime-prep/refresh3-{bff,edge}-health.json`; bodies/secrets were
suppressed. No retry, OAuth/login or business-data read/mutation was performed
by I1. Root owns I4's real-defaults application-proof release.

Root registration drivers96281/51294 and I1 read handles95462/6996 joined0;
all assigned effects are settled, with no active read/utility or unknown effect.
Immediate readiness reports are `892078bb-c8e3-4840-ad13-089723d7cc3c` and
`556c58c3-97a6-4cf2-b0e7-bc7721e61ec1`. I1 changed only existing evidence after
health; frozen ownership/stage/admission/input controls remain unchanged.
Private credentials/signing/TLS inputs, BFF sessions/StateDirectory, existing
origin/ports/firewall, old files/refs/roots and Vite are retained. All five guests
and current user data are preserved; no fixture rows were assumed, queried or
recreated after the user's PHP submission. Historical fixture counts below retain
their original scope. Source/prevention/storage remain parked; I1 retains
technical recovery/fix ownership, with no further health call pending.

## Historical refresh3 preparation and final actual binding

Lead accepted/froze the controls and preserved-file hashes, then accepted I4's
reviewed matching actual corrected-default outputs. Final local binding passed
once, exit0; the source/artifact dependency is satisfied. Existing refresh2 previews
remain running until root's actual drivers. Root owns ordinary edge→BFF stops, exact remote reconciliation,
fresh selected-generation admission, full staging and BFF→edge registration.
There is no peer-switch receipt or extra user gate for this authorized ordinary
development refresh. I1 has performed only local preparation under the existing
`i1-react-runtime-prep`; no live probe, source worktree/index, build, export/import,
service, port, credential, account, fixture or lifecycle action has run.

Fresh BFF is `203cb011-868e-401f-a28b-3ec4ad386e40`; fresh edge is
`383bd08d-ec47-4e94-ac15-3eaa07837154`. New unit/prefix/host and remote attempt
identities use `refresh3`. The only old targets are refresh2 BFF
`be2b20b5-4704-42a6-ba03-fc69fc2f263c`/Invocation
`56075bd161e841218a0bb0922b69f061` and edge
`d9e230fb-a0c2-429e-9798-5ec83134709f`/Invocation
`45586e7a6b00493fa73744195b238d3f`.

`refresh3-preparation.json` records exact control hashes, preserved-old-file hashes
and passing AST/bash syntax/critical3BFF+2edge argv/state/TLS namespace checks.
The argv check used an explicit non-path BFF placeholder, not a guessed artifact.
`refresh3-controls.diff` contains the minimal identity/ordinary-admission changes
and reuse of the accepted full mounted-NAR/daemon staging route. Literal root
commands and first-UNKNOWN recovery are in the existing runbook's Refresh3 section.
The full export/import stage stays after exact stop/reconciliation/admission;
no new transport/cache or early-copy protocol was added.

Only the binder's expected-head literal changed to clean reviewed
`39a1f17ce859600d10276da0fe29bfb1593c8132`, tree
`2709241c82f0b0a314d3699ac9f8570c5b3a1233`. I4's accepted first matching five-target
build passed once/97.708s; its receipt is `i4-logs/defaults-nix-output-receipt.json`.
The actual pair is frontend
`/nix/store/59ynv5gwz6b3s0ddnpzdggzg718d2vfb-vpsadmin-webui-frontend-1.0.0` and BFF
`/nix/store/jxscjby6p1dh2jyv6nr9b7yvrmprbcdg-vpsadmin-webui-bff-0.1.0`.
The existing binder proved matching full clean metadata/output layout/inline CSP
and generated exclusive inputs/env/nginx. Admission remains absent; all other
frozen ownership/stage/admission controls are unchanged. Unbound binder/manifest
copies and binding log are retained in the same prep directory.

| Final file | SHA256 |
| --- | --- |
| `bind-refresh3.py` | `b2141f235d976402137089db56dedb6259aba384651f3cd9a4ad54ab9fba5aa1` |
| `inputs-refresh3.json` | `e70dd59a6546c396fcb76a7954cc408f228769d9e4ee35addaf6b355a39d2bea` |
| `outputs-refresh3.env` | `88ba2dc3c36ff3b48c934a940613fc08ababb20a7e74e64ed8a3b4438bb4996c` |
| `nginx-refresh3.conf` | `af7ca491b4d393ff93e7407b40f9eae558e8b965228dd8063c9ffb8d8bd8c62e` |
| `refresh3-preparation.json` | `2d66a9d444b8f2e98256782eb5ef1b1992c47771d8cff52c1310d4e6ed138b1e` |

Root retains final actual-binding acceptance and all drivers; no guest, stage,
import, service or backend action occurred during binding. There is no
preservation blocker or active utility. Private inputs/signing/TLS,
BFF sessions/StateDirectory, current user backend data and all old files/roots/
refs/receipts are preserved. Historical fixture rows are not assumed or re-probed.
Source/prevention and storage remain parked with fix ownership retained.

## Historical React refresh2 — accepted before refresh3

The user approved one preview interruption; fresh peer READY and root's own
execution release preceded normal refresh1 edge→BFF stops. Both stopped registry
commands exited0. Root's exact remote reconciliation (tool86616, exit0) proves
edge Invocation `5939ce88915749079709484121cc07a6` and BFF Invocation
`9a0195e943bc41b9baaabf5558bedd2d` terminal: MainPID0, inactive, cgroups absent.
The single original switch joined0/152s and explicit clearance followed. No local
exit/grace/lock inference substituted for those proofs. Old identities, failed
attempts and all receipts remain retained.

`refresh2-admission.json` records the fresh selected generation
`/nix/store/3y9ns5h3raj9zszrwcr5pgvf9gng8q4b-dev-workspace-0.2.0`, known succeeded
outcome, explicit clearance, reconciled old owners and reviewed-inline binding.
The app source is unchanged clean `1d895a5746561d15413f42afd83678b898de3b45`, tree
`1e52746fdf08f561e70efdbee6e7bbd22a57aebd`:

- Frontend `/nix/store/8zryvl94jahgq206bg2jf5wn6zymzrwp-vpsadmin-webui-frontend-1.0.0`.
- BFF `/nix/store/wdgyn07nr7mch8i5l3113h06injclnj3-vpsadmin-webui-bff-0.1.0`.

Root's resident stage tool10589/supervisor3703466 exited0, phase
`apps-rooted-staged-no-service-or-firewall-activation`. Ordinary validity, exact
closure/metadata and fresh roots/config staging passed for the same60 resident
paths. Closure-list SHA256 is
`c4fe4cb00bc8ee733ed13d1a871b57e06d779b5528f7eeb4643200eae1e55ce1`;
runtime manifest SHA256 is
`cbe7ebbdf978555754a51cca8ba30cc496c95b1f91dc0aa9c0e586fe75f1f26a`.
Host receipts/roots are `app-stage-refresh2/{exit.json,payload.json,frontend,bff}`;
guest roots are `vpsadmin-review-ac1f7e2d-refresh2-{frontend,bff}` under
`/nix/var/nix/gcroots`. No NAR export/import, rebuild or new firewall action ran.

| Live component | Registration; host owner / SSH PID=PGID | Guest unit; InvocationID | Main PID / actual UID |
| --- | --- | --- | --- |
| BFF refresh2 | `be2b20b5-4704-42a6-ba03-fc69fc2f263c`;3706624 /3706672 | `vpsadmin-review-bff-ac1f7e2d-refresh2.service`; `56075bd161e841218a0bb0922b69f061` | 166368 /65292 |
| Edge refresh2 | `d9e230fb-a0c2-429e-9798-5ec83134709f`;3714558 /3714612 | `vpsadmin-review-edge-ac1f7e2d-refresh2.service`; `45586e7a6b00493fa73744195b238d3f` | 166814 /62523 |

Both exact registrations are running; bound guest units are active/running with
populated owned system.slice cgroups and DynamicUser=yes. The actual pinned
Node24.21.0 executes the exact wdgyn `server.js`; nginx1.30.7 has the exact refresh2
prefix/config/daemon-off argv. Typed credentials are3BFF/2edge; recorded edge
ExecStartPre `nginx -t` succeeded. Both host/SSH owners are present with start
receipts and no exit receipt, as intended for persistent servers.

BFF canonical-Host/forwarded-HTTPS loopback health passed200. Strict existing-CA
and hostname TLS passed200 for `/healthz`, exact full clean1d895 `/build-info.json`,
bound API URL/7.0/HaveAPI header/`_meta` `/config.json`, and prescribed same-origin
`/session.json` with exactly three null anonymous fields. Config/session no-store,
single nosniff and single same-origin CORP passed. Bodies/credential values were
suppressed. No auth/OAuth, account or business mutation was attempted by I1.

Safe receipts are `refresh2-bff-health.json` and `refresh2-edge-health.json` in
`i1-react-runtime-prep`; I1 read handles52833/75670 joined0. Root BFF/edge
registration handles28565/96891 joined0. All assigned commands/read effects are
settled; no read handle, watcher or unknown effect remains. Readiness reports are
`ee4ceb27-3395-40de-b3d2-9971a5a7d8f2` and
`d0b14297-a146-40af-b0a0-43c0f923490b`.

The accepted frozen manifest/diff remain `refresh2-preparation.json` and
`refresh2-controls.diff`; inputs/output env are byte-identical to refresh1.
Private client2/signing/TLS inputs, BFF sessions/StateDirectory, existing8443
rule, old controls/roots/refs and Vite are retained. Five guests/runner and
VPS1/plan/three source snapshots/one backup were not targeted or re-probed.
Only root executed the authorized app stop/stage/start drivers; I1 performed the
released read-only health batches and this evidence consolidation. No source,
push/merge, selected-package or session lifecycle action was performed by I1.
Source/prevention and original storage remain parked; I1 retains recovery/fix
ownership. Root owns final acceptance and handoff; no further I1 action is pending.

## Historical React refresh1 — health/application proof accepted before refresh2

Lead accepted both refreshed components' readiness and I4's real inline
OAuth/visual proof:53.406s,89 reads, zero business/account writes, all handles
joined. Runtime remains PARKED with I1 technical recovery and review-fix
ownership. Prevention is the one resumed source package below; original storage
verification remains parked. No further runtime action is assigned to I1.

The selected source is clean `1d895a5746561d15413f42afd83678b898de3b45`, tree
`1e52746fdf08f561e70efdbee6e7bbd22a57aebd`. I4's accepted five-target build and
postproof are in `i4-logs/inline-nix-output-receipt.json`; the path-flake versus
Git-flake evaluation difference was reconciled without a rebuild. Actual pair:

- Frontend `/nix/store/8zryvl94jahgq206bg2jf5wn6zymzrwp-vpsadmin-webui-frontend-1.0.0`.
- BFF `/nix/store/wdgyn07nr7mch8i5l3113h06injclnj3-vpsadmin-webui-bff-0.1.0`.

The binder passed parsed clean metadata equality and the built inline CSP.
Frozen `inputs-refresh1.json`, `outputs-refresh1.env`, and `nginx-refresh1.conf`
SHA256 values are respectively
`cec1df5239f5c73c46566067b3079cd191fc21ee633d7cbedefb13d3c4358da1`,
`e0f989bdb854a5a53466ac981f099e1606281972fd8a18347c071ea11bde5156`, and
`22947c8908072b5b601e951f3af3e5b7f30708e1e704374389bb661979287c04`.
Historical ff2 inputs, fallback copies, scripts, roots and receipts are retained.

Root normally stopped the exact old edge then BFF registrations. Both saved old
InvocationIDs were reconciled terminal with cgroups gone. The original waiting
workspace switch exited0; explicit clearance and fresh selected package
`/nix/store/yg3mcl33znja8q4kaqfsjbz7ds7p5cib-dev-workspace-0.2.0` were recorded
before new readers. Root's `stage-apps-refresh1.sh` exited0, supervisor191096
(`app-stage-refresh1/exit.json`): complete closure export/import, validity,
metadata, persistent roots and public config staging passed. Host roots are
`i1-react-runtime-prep/app-stage-refresh1/{frontend,bff}`; guest roots are
`/nix/var/nix/gcroots/vpsadmin-review-ac1f7e2d-refresh1-{frontend,bff}`.
No guest build, remount or layout change occurred.

| Live component | Registration; host owner / SSH PID=PGID | Guest unit; InvocationID | Main PID / actual UID |
| --- | --- | --- | --- |
| BFF refresh1 | `01f924c6-7e76-4c06-9833-15993e028f8e`;196617 /196743 | `vpsadmin-review-bff-ac1f7e2d-refresh1.service`; `9a0195e943bc41b9baaabf5558bedd2d` | 57973 /65292 |
| Edge refresh1 | `8636db4f-65a6-4e1f-b95b-afc45e842350`;211069 /211211 | `vpsadmin-review-edge-ac1f7e2d-refresh1.service`; `5939ce88915749079709484121cc07a6` | 58724 /62523 |

Both registrations are running; exact identity-bound guest units are
active/running with populated owned `/system.slice/UNIT` cgroups and
DynamicUser=yes. The BFF's actual pinned Node24.21.0 executes the exact wdgyn
`lib/vpsadmin-webui-bff/server.js`; nginx1.30.7 uses the refresh1 prefix/config
and daemon-off arguments. Typed D-Bus credential arrays contain three BFF and
two edge entries. Recorded edge ExecStartPre `nginx -t` exited0. Each host start
receipt exists without an exit receipt, as expected for the retained servers.

Canonical-Host BFF loopback health returned200. Strict existing-CA/hostname TLS
returned200 for health, exact full clean1d895 build metadata, API7.0 runtime
config, and same-origin anonymous session. API URL, HaveAPI auth header and
`_meta` match; config/session no-store, single nosniff and single same-origin
CORP passed. Session has exactly three null fields. An initial request without
same-origin context returned403; the prescribed Origin/Sec-Fetch context passed.
The initial BFF credential text-parser mismatch was resolved through the typed
property. Neither check artifact was an application failure. Bodies and
credential values were suppressed; no login/auth action was performed by I1.

Root confirms all stop/reconcile/admission/stage/register control handles joined
(BFF79914 and edge92643 exited0) and the admission gap closed. I1 read handles
71506/26492/8456 and7683/95708 are joined. No uncertain effect or held utility
remains. Safe readiness reports are `f983c9d5-f1fd-4949-aaca-82de3b825fe7` and
`087d0d80-b842-4ddc-8eea-24ad0e084378`.

Private OAuth client2/signing inputs, the shared BFF session StateDirectory,
existing TLS/CA/origin/ports and owned guest8443 rule are unchanged. New BFF/edge
owners remain intentionally live; failed-first and stopped-old attempt evidence
remains intact. Five guests/runner, VPS1/plan/three source snapshots/one backup
and Vite5187 are preserved; the prior catalog observation below was not repeated.
I1 performed no service, guest, credential, fixture or lifecycle mutation.

## Prevention source packet — reviewed, A1 accepted, package check passed

I1's current package follows design.md's
`future-session-react-preparation-and-ssh-prevention-brief`. Both new worktrees
are under `worktrees/2026-11-25-backup-disable-design/`, on branch
`2026-11-25-backup-disable-design`, with separate clean indexes. No backend index
or live runtime input was changed. Upstream was fetched before setup; the generic
base still routed SSH through `Open3.capture3`, so no existing fix was duplicated.

| Repository | Exact base → final head | Complete package series / tree |
| --- | --- | --- |
| `dev-workspace` | `f6d60bf87002fb1896599f35f0284743c16d7e6f` → `15511ef8db238b1035c46c4034d1b199fe794880` | One commit, `host: preserve standard streams for cluster SSH`; tree `5bf85e8654615a66afae6e9f7d08563fe1b01d94` |
| `vpsfree-dev-workspace` | `bf12ac71a8a00b1581eed5352f99c1b2daaeff5b` → `39e7a09eb6afbf14fc5a6b6bea74fd1c0a568b55` | One commit, `devcluster: prepare React sources before first boot`; tree `24bdf603f7b7d4951e28198715c7c59a959d2920` |

The generic diff is exactly `libexec/workspace-host` (two-line SSH-only selection
of existing `system_env_interactive!` inside the same guard),
`test/workspace_host/commands_and_locks_test.rb` (three real-dispatch subprocess
regressions using the existing fake provider), and the existing provider-contract
paragraph in `docs/workspace-portal.md`:117+/4-. Provider diff is only
`dev-clusters/vpsadmin/README.md`:28+. Tests prove binary bytes/EOF, separate
streaming stdout/stderr before child exit, inherited terminal stdin/out/err,
nonzero failure mapping and generation-lock retention through provider cleanup
then release. Existing capture-lease/non-SSH behavior and environment coverage
remain included. No new launcher, fixture framework or safety abstraction.

Quick evidence, all in each repository's pinned Nix environment:

- Ruby syntax and the three new cases:3 runs/28 assertions, exit0.
- Exact32 affected methods through existing `test/workspace_host_test.rb`:
  32 runs/403 assertions, zero failures/errors/skips, exit0 in12.460395s.
  `i1-prevention-affected-entrypoint.log` retains the exact name filter and seed.
  Initial direct fragment loading had13 missing-helper NameErrors because the
  established aggregator loads shared classes from other fragments. That failed
  command/log is retained; no production code/assertion was weakened to fix it.
- Final generic-source policy check exit0, derivation
  `/nix/store/g4fzkjr2carfsx33911jdv45nhcbs66a-dev-workspace-generic-source.drv`;
  final provider organization-source check exit0, derivation
  `/nix/store/ilzqcr4j3nn4rzcpk0kmv895cbm799rn-vpsfree-dev-workspace-source.drv`.
  Logs are `i1-prevention-{generic-source-committed,organization-source-final}.log`.
- Both `git diff --check` checks clean. Normal commits succeeded; neither repo
  declares a hook framework, and no hook was disabled or bypassed. Commit
  messages were supplied through files. All check/commit handles are terminal.

The final generic amendment only makes the requested switch-lock consequence
explicit in docs. Runtime/test blobs equal the quick-checked initial commit
`ccd30848963aedacbda4798a86bc5a453b142264`: respectively
`682016d4a56e3086409c1ca7366028dde0b68e8b` and
`4381791a10afccc269eef86083f36ad261bd6032`. The final documentation input passed
the refreshed source-policy check. No repeated pin/dependency/generated update
stream, migrations, schema/version/fixture/default changes or obsolete fixup
commits remain in either complete package range. Nothing was merged, published,
released, deployed or externally consumed from these two branches; no push was
made under the retained publication hold. Earlier runtime receipts are separate.

Documentation routing: provider operators' initial React setup/recovery limits
(how-to) → existing provider README basic/optional-React sections; SDK/archive
details point to `docs/design/PACKAGING.md` in the exact selected WebUI
checkout/revision. Generic
extension authors' SSH stdio/generation-lock contract (reference) → existing
`docs/workspace-portal.md` provider paragraph. It explicitly says a long-lived SSH
command delays package switches; provider docs direct persistent React through
ordinary provider/module preparation before first boot. Writing skill/factual
fidelity checks preserved commands, domains/placeholders and the layout limit.

Compatibility: no persistent format, provider protocol, catalog, credential,
auth or migration change. Old wrappers retain their stdin limitation; mounted
file/argv workarounds remain usable. Package rollback restores that limitation
without conversion. Existing React-disabled guests keep their layout restriction.
The trusted-local-operator model remains unchanged; remote clients/providers
retain their existing validation/authority boundaries. Generic catalog dispatch
owns the public interface; organization providers consume it without pin changes.

Independent final review found no Blocking/Important findings. Reviewer A1 was
the provider README's misleading `blob/main` local-archive recipe link. The
normal amend replaces only that passage with the approved exact-checkout/revision
sentence; lead directly inspected and accepted it. Reviewed `aa848df` is retained
at `refs/heads/2026-11-25-backup-disable-design-reviewed-aa848df`; the exact old-to-new
diff is `i1-prevention-a1-old-to-new.diff`. The generic head/runtime/test blobs
remain byte-identical. No reviewer or separate32-method rerun was required.
The amended organization-source check passed once, exit0/2.870s, log
`i1-prevention-a1-organization-source.log`; whitespace checks passed.

Complete final series/diffs, exact bases/heads/trees and no-migration/dependency-
stream conclusions are in `i1-prevention-final-source-packet.json` and the two
`i1-prevention-*-final.diff` files. Both streams remain one logical unpublished
commit. No push, merge, package selection or activation is authorized.

The first required postreview `checks.x86_64-linux.package` command passed once,
exit0 in736.836s, from22:49:00Z to23:01:17Z on2026-11-25. Driver267963/Nix
PID=PGID267970 and tool93572 joined; both PIDs and the owned process group are
absent. `checkPhase` ran, followed by install/fixup; no unexpected kernel build
occurred. Exact argv,
revision/source/input graph, derivation and expected output are recorded in
`i1-prevention-package-plan.json`, `i1-prevention-package-flake-metadata.json`,
`i1-prevention-package-derivation.json`, and the exclusive
`i1-prevention-package-check/{start.json,private.log,exit.json}`. It uses
jobs2/cores2 and its own `i1-prevention-package-check-result` retention root;
this was distinct from the default build. The root resolves to actual output
`/nix/store/gra3q3bib3l8m4zsxnbpzv79k3j2j1yh-dev-workspace-0.2.0`, with exact
deriver `/nix/store/0wmhnqd2nznjz4jkzi9pbgq15ifxw733-dev-workspace-0.2.0.drv`.
Output NAR is34874800bytes, SHA256
`sha256-+Q9x1ilPkTALOMOBmGgGUSrfVJIGuQKNlOgQqz2ZkbI=`. The final receipt is
`i1-prevention-package-final-receipt.json`; the6465710-byte log SHA256 is
`c9cccd914a2c5184683b0aebe115696240bea876da218a63ffec373556b3660b`.
Fresh admission found30.44GB available RAM,131.66GB store/workspace free and
27.19GB shm free. The planned5–15min run had no quiet timeout and required stopping
on first failure/unknown/unexpected local kernel; none occurred.
The fresh installed-catalog Luna/low utility refused its identity check before
plan access/dispatch and reported zero check effects. No watcher repair/relaunch
occurred; the active parent is the sole command observer. Preflight corrected
Nix JSON coercion from a special `outPath` projection key before the package
command launched. Both final worktrees are clean at the heads above; all known
check/preflight/postproof handles are terminal, with no held utility or uncertain
command effect. No package switch/VM/current-service/fixture probe or mutation
occurred. The source package is delivered for lead acceptance, with fix ownership
retained and publication/integration still held. Runtime and original storage
verification stay PARKED, ownerI1.

## Historical ff2 React review runtime — accepted before refresh1

Lead accepted activation and I4's real admin/member OAuth/UI smoke. I4 reports
zero business mutation and joined browser effects. The human-review origin is
https://newadmin.aitherdev.int.vpsfree.cz:8443 . Provider `newWebui.enable=false`
and the five-guest layout remain unchanged; this is the separate registered
edge/BFF route. Older sections below retain their historical scope.

Final reviewed React source is `ff2cf8ae4b44781f90941611294a94fd6953763a`, tree
`2c1c9ff8928011b29d23ab96ab22ea2a14edfead`. The exact immutable pair is:

- Frontend: `/nix/store/yd27wqhv0pwqkdd6f94w6nvmj3rs82b7-vpsadmin-webui-frontend-1.0.0`
- BFF: `/nix/store/4f9ch790kw1i3hh8ypj1x6lsxpd9d5h8-vpsadmin-webui-bff-0.1.0`

I4's accepted final five-target/package/SDK proof is
`i4-logs/acknowledgement-nix-output-receipt.json` (SHA256
`75638305e4254164437c9c25fbc0f8a3b4cbf0def6136cf23e3fa0e4bf1fb2f3`).
I1 bound the realized pair, parsed clean metadata equality and built inline CSP
without repeating I4's checks. Separate frontend/BFF metadata hashes are retained
in `i1-react-runtime-prep/inputs.json` and `outputs.env`; formatting differs.

### Import, retention and active ownership

Root stage tool61734/supervisor3738667 joined exit0, final phase
`apps-rooted-staged-no-service-or-firewall-activation`. Its complete60-path
public closure export is271546512bytes, SHA256
`3a9a2a381fe2b382c53a36afcc243c3359f9ada2b202eb13a46176e5b7837ef1`.
The host payload is in the ignored/untracked backend
`.rubocop_cache/vpsadmin-react-review-ac1f7e2d/`, mapped at the same suffix below
guest `/mnt/vpsadmin`. Guest-side file redirection and `NIX_REMOTE=daemon`
preserved ordinary import/trust checks; complete validity, closure equality,
individual metadata hashes and root registration passed. No guest build,
alternate store, remount, provider update or layout change occurred.

Host roots `i1-react-runtime-prep/app-stage/{frontend,bff}` resolve to the exact
pair above. Guest roots are
`/nix/var/nix/gcroots/vpsadmin-review-ac1f7e2d-{frontend,bff}`. Import inventory,
digest and terminal receipt remain in `app-stage/{payload.json,exit.json}`;
`guest-stage-private.log` retains the successful root/validity checks.

| Component | Registration; host supervisor / SSH PID=PGID | Guest unit; InvocationID | Actual main process |
| --- | --- | --- | --- |
| BFF r2 | `fe58b25f-b98f-4f9a-b491-c211fc513c7e`;3807137 /3807148 | `vpsadmin-review-bff-ac1f7e2d-r2.service`; `88ea9d591b3d4fefa8b8b0a3a2633ddd` | PID44717, UID65292; pinned `/nix/store/503mh0fj8j1cfvrxcavr76szbn4dk2r7-nodejs-slim-24.21.0/bin/node` running the exact4f9 BFF `server.js` |
| HTTPS edge | `c346723f-3467-4ed3-910c-24033cd45bd9`;3816553 /3816587 | `vpsadmin-review-edge-ac1f7e2d.service`; `46b2480714a843a7a7df9e7c60c52998` | PID45156, UID62523; `/nix/store/v5yfyvpd7z7lbzh86bpbh5cjp10qad4m-nginx-1.30.7/bin/nginx`, own prefix/config and daemon off |

Both exact registrations were running; guest units active/running, matching
saved identities, own system.slice cgroups populated1/frozen0. BFF has three
individual credential entries, edge two; both use DynamicUser. BFF prestart
PID44710 exited0; edge `nginx -t` PID45149 exited0. Foreground local supervisors
and public SSH remain intentionally attached. Their `host-bff-r2/` and
`host-edge/` start receipts exist with no terminal receipt, as expected while
running. Stable private OAuth client2/signing files and the one BFF session store
are retained; no credential values are recorded here.

Guest-local strict CA/hostname TLS checks passed HTTP200 for health, final clean
build info, API7.0 runtime config and anonymous session. Exact API/OAuth routes,
HaveAPI header/namespace, no-store, single nosniff/CORP and three null anonymous
session fields passed; response bodies were suppressed. Root port tool77613
joined0, checking the exact guest `nixos-fw` ACCEPT rule for destination
`172.16.106.53/32`, TCP8443, comment
`dev-session:2026-11-25-backup-disable-design:react:ac1f7e2d`.
Host iptables was untouched. Root's outside-host `curl --cacert` without `-k`
returned200 and full cleanff2 build info. Python3.13's X509_STRICT rejection of
the existing dev CA's missing keyUsage is retained as a validator-specific result;
no certificate or TLS-verification bypass was introduced.

### Terminal attempts and preserved fixture

Root OAuth tool17748 ended1 at staging, before scripts/credentials/POST existed.
Corrected tool39632 ran the unchanged create once: stage3551973 and create3552398
PID=PGID both joined0. Root first BFF registration tool34841 joined0, but its
host supervisor3745525/SSH3745543 subsequently joined with SSH exit1. Its failed
unit/InvocationID `45c15fae092a4513b6998d6d2979287f` remain retained: malformed
space-joined LoadCredential source caused executor deserialization failure,
before Node started. MainPID0, no cgroup/listener/state directory; no uncertain
process effect remained. R2 supplies separate properties and a new attempt
identity without resetting/stopping/deleting the old one. Root corrected-owner
copy tool11865 joined0; r2 registration launch handle65251 and the separate edge
registration produced the intentionally persistent ownership above. Root owns
the registration control-handle records; this receipt does not infer unreported
control exit codes. All I1 observation commands, including catalog tool16853,
are terminal. No I1 utility or mutation command remains running.

The one allowed continuity observation found runner1656251 with this exact
session argument and all five live guests: services (1664169), dns-primary
(1670690), dns-secondary (1672101), node1 (1672195) and node2 (1672465).
The one catalog-only read at
2026-11-25T21:31:51Z returned running VPS1/member2/dataset1, sourceDIP1,
backupDIP2/pool3, real daily_backup membership1/environmentPlan1; source snapshot
IDs1/2/3 and backup snapshotID1 all confirmed/unlocked. VPS/source/backup locks
are free and both pools online. No payload was reread. Earlier physical marker
and backup-copy proof remains scoped to its original receipt below.

Both app services, five guests/runner, VPS/plan/history and existing Vite5187 are
intentionally retained. No disable/plan-removal POST, reset, cleanup, stop,
credential rotation, publication, integration or session lifecycle action was
performed by I1. Original two-fixture storage verification remains PARKED with
I1 ownership. I1 retains this package through review fixes; root owns final
acceptance/user handoff. Operational commands/recovery are in
`i1-react-runtime-prep/runbook.md`; failed and intermediate receipts remain intact.

## Persistent PHP review cluster — ready for read-only UI review

C2/C3 completed at18:08:59Z. Backend remains
`140f0769e222dd2aa51e64d08f11cd5e8dae397b`, tree
`a872181147d22917e37f2a5023af7c30557fd7ea`; no application/Git changes.
Root's sole public dual/bridge start fd2e819c ended0 at17:47:44.774991Z
in2186.676s. All5 guests proved exact selected systems; appliedpending=null,
configuration exactly `/nix/store/mbriq0a91p71qppkqy6314ygal2s950d-os-test-vpsadmin-devcluster-2026-11-25-backup-disable-design.json`,
SHA256 `994c8eb3c570c0eb3cdb26a0ae4e77d171dbfefa954b65a2b19df81d55379058`.
API/supervisor/scheduler and both nodectld workers are healthy. Actual deployed
operation SHA256 `92f489343bbc186db5ce40224abc02b35915c608d9c4caed0efa3bcddf7fcff8`
and resource SHA256 `a473cf82d1002d31e2f155d93568ce9c6a6536dd32e51c7c6fe8bce5ffc9462a`
match reviewed source. Actual HTTPS OPTIONS exposes expected2Boolean defaults,
blocking POST and empty declared output; exact deployed source contains the
admin-only guard. No DisableBackups POST was sent.

- Running VPS1, memberID2, dataset1, sourceDIP1, backupDIP2 in backupPool3.
- Exactly3 confirmed/unlocked primary snapshots IDs1/2/3, labels review-1/2/3;
  exactly1 confirmed/unlocked backup snapshotID1 (SIP2). Source historical
  markers S1/S2/S3 and liveS3 match expected hashes; backup branch S1 also matches.
- Real daily_backup plan membership1/EnvironmentPlan1 retained. Group action1 /
  task1 cron `00 01 * * *`; backup action2 / task2 cron `22 02 * * *`, source1→2.
  Both DIPs retain10/10/86400. Pools online; VPS/source/backup locks released.
- Chains5(pool),6(VPS and its automatic backup placement),7(snapshot1),8(normal
  Backup),9(snapshot2),10(snapshot3) all done. All command handles joined;
  intentional persistent runner1656251 and5guests stay running.

Safe PHP URL: https://webui.aitherdev.int.vpsfree.cz/?page=dataset&action=edit&role=hypervisor&id=1 .
Backup listing `?page=backup&action=vps`; receipt `?page=transactions&chain=8`.
I2 received direct read-only handoff ca68220b-9b86-4ee1-a058-8d27bf95c62c; its
admin/member checkbox/explanation check is separate and must never submit cleanup.
Credentials stay in private cluster config/account view; no values are recorded.
React is disabled in this PHP-first cluster. Original two-fixture storage and PHP
VM packages remain parked. No cleanup, delete, reset, stop, push or lifecycle action.

Evidence: `i1-review-cluster-health.json`, `live-capability-public-route.json`
(with full i1-review-cluster prefix), `final-data.json`, `final-payload.json`,
`backup1-payload.json`; actual raw startup/fixture logs stay private beneath
`/tmp/backup-disable-ui-cluster-fd2e819c`. The original config10819... is preserved
privately0600; only approved newWebui.enable=false yielded config65ed....
Cache134.77984s exit0:821local/347fetches, exact2kernels substituted,9assemblies
separate. Initial native observers ended before start, joined; active-parent
fallback observed the one root driver and fixtures. Original receipts remain.
Owner-command mismatches (Pool lacks Confirmable; redundant duplicate-placement
guard contradicted ensure helper) were corrected without repeated object creation
or production changes. VPS.New's existing owned placement was reused as the
original helper requires. Obsolete api.vpsadmin.test returned401HTML; configured
HTTPS API worked with unchanged private auth/config. This is a real review fixture,
not full storage acceptance or live-backup certification.

## Reviewed acquisition to current input identity

Each object below is identical at reviewed50aa37a and currente303d336. In
addition, a whole-repository diff excluding only the two named PHP paths is empty,
so other tracked inputs omitted from the compact table are unchanged too.

| Input | Identical Git object |
| --- | --- |
| `api` | `bed58750a34e8d78532b9eb1c62a1fe8c1f58f9f` |
| `plugins` | `449edce0cab21fb2a3c355f551c4a865655adb27` |
| `libnodectld` | `67d14139e0ae58a02e31c781bf8a9ed6449cd8e2` |
| `nodectld` | `47209ddace522580cdb915907a3d9996459199a2` |
| `nodectl` | `cc5cc649b811be0cb63e450d4ae12ef0e0185a58` |
| `nixos` | `e95010a5167858c134014f16ba746e926ea278b0` |
| `packages` | `81ac016a997a5d0f22c20617a413574da4e24664` |
| `tools` | `87cd674523792d96b0a84ac31339743cce805e73` |
| `tools/api-schema-export` | `5d291b4cc5c6c3c59bcef42fa0399a15bfe88b62` |
| `tools/test-db` | `23b81b5dc0514d27a88ad7fafcf8d12ed8b7498a` |
| `tools/test_db.rb` | `1178f0fc31410cc9f50f934087ed2c4936735df6` |
| `Gemfile` | `21818ef377d101fe681366146653f3cab420854b` |
| `Rakefile` | `1e57e472855cb94b99724196df65a7c2be14cae3` |
| `.overcommit.yml` | `bca50b39f752cdf62329c612a58ff92fdfa64ebd` |
| `.git-hooks` | `09b6844b2eddd8fc622041cf2cd41eaa8e7480fd` |
| `.gitmodules` | `32c528fd76152eb96bddde4c0c93174459a898cb` |
| `.ruby-version` | `18091983f59ddde8105e566545a0d9e4a12a4f1c` |
| `VERSION` | `fae6e3d04b2cab9db74fb2bfb40e32f047084561` |
| `flake.nix` | `677b35e1995e5114e046fee23001a4d75514141e` |
| `flake.lock` | `e53d2b042cbe8b874e593b49ac6e09cfc315e3ce` |

The original actual raw client export/provenance naming50aa37a remains immutable
and accurate. This is a current-source equivalence mapping to the new head, not
an assertion that the old nonancestor was literally merged. The explicit
ancestry check returns1 for50aa37a→current, as expected after history rewriting.
No API tests, client regeneration/export or new schema capture was run solely
for this PHP-only correction/history fold.

## Follow-up commands, hooks and effects

Normal declared shell: `nix develop .#vpsadmin -c bash
/tmp/backup-disable-r1-history.sh`. Sequence uses ordinary autosquash, then
`git commit --amend -F /tmp/backup-disable-r1-php-message` on the corrected PHP
tree to run declared hooks before fixture replay. No hook bypass.
Nixfmt, MigrationSpecs, WebUIi18n, PHP CS Fixer and APIi18n passed; all commit-msg
hooks passed with existing72-column advisories only (lines<=80).

Log:`/tmp/backup-disable-r1-history.log`; full identity record:
`/tmp/backup-disable-r1-identity.json`; complete old/new range comparison:
`/tmp/backup-disable-r1-range-diff.txt`. Invariants require clean pre-state,
exact7cdec07 head, exact pre/post tree equality and only the two accepted paths
changed since the reviewed acquisition. Post-fold `git diff --check` and clean
index/worktree checks passed. Owner session47311 exited0; all follow-up tool
calls are complete and no operation-owned process remains. Exclusive I1
source/index/history window relinquished after this proof. Long VM/browser
checks, push, integration and deployment remain held for lead reconciliation.

The following original reviewed checkpoint and implementation evidence is
retained without rewriting its historical head or raw acquisition claims.

---

# Final source checkpoint

- Base: `81e930b25fa3252d7e849aff4819e663cec37b07` (current local origin/master).
- Final head: `50aa37aede8926965598f4f8fb0782dce377afb6`.
- Final tree: `961f50965e926a77c5fb965d27e4fc6ff8fd878f`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-backup-disable-design/vpsadmin`.
- Branch: `2026-11-25-backup-disable-design`.
- SSH remote: `git@github.com:vpsfreecz/vpsadmin.git`.
- Final complete diff: 31 files, +2138/-85; I1 owns 21 source/doc/test paths,
  I2 owns the other 10. Final index and worktree clean.
- I1 Git/source window relinquished after all mutations exited. Lead owns
  acceptance, final independent review, state updates and publication timing.

## Complete final series

```text
cbb8def6056301558ed17c8b4818a9653ae5d35e api: preserve snapshots before disabling scheduled backups
bd36c4f241ed34da4ce726b702988e3e151d2549 webui: add admin backup cleanup confirmation
50aa37aede8926965598f4f8fb0782dce377afb6 tests: cover single-task backup disablement on remote storage
```

The old5commit series was consolidated into API/UI/fixture3commits; a final
one-line obsolete CI selector deletion was committed with required hooks and
folded into API. No D2 compatibility/history remains in this series. No migration,
release, deployment or externally consumed original state boundary exists.
Final API has ordinary `dataset:{}` alongside `_meta`; exact assertions passed.

# I1 API/storage correction evidence

Session: `2026-11-25-backup-disable-design`, implementer0.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-backup-disable-design/

## Contract and scope

Accepted D3: one admin-only `Dataset.DisableBackups` task, only `recursive=false`
and `backup_first=true`; ordinary `ok!` and `_meta.action_state_id`, with an empty
ordinary `dataset` namespace. No declared action-specific output. Ordinary
Transfer and existing RecvCheck commands precede every metadata/delete step across
the recursive scope. Older gaps outside normal transfer selection reject atomic
construction. No forced full mode. All metadata and cleanup helpers are
`not_reversible`; successful preserved copies survive later cleanup failure.
Existing confirmed non-head coverage and exact copies planned by this chain count.

Scoped unregister retains shared group action/task rows; selected memberships,
plans and head edits use ordinary confirmations. Minimal source locks and
post-lock scheduled identity/membership guards remain. Ordinary plan assignment,
restore and retention semantics remain unchanged. No notifier, Nix socket repair,
NoOp payload, manifest, PreserveForDisable, continuation or phase compatibility.

API/storage source, tests and documentation belong to I1. PHP source belongs to
I2, committed separately. SDK/export and React source belong to I3/I4. There is no
new node command, node wire parameter, storage format, schema or migration.

## Quick verification

- Fresh watcher actual API batch: 56 examples, 53 passing / 3 fixture/envelope
  expectation failures, no pending/outside errors. Log
  `/tmp/backup-disable-d3-api-runtime.log`, native JSON `.json` with same stem.
  Runtime source was HEAD `1fad9eee08f971d2417c0e26f0f96f731452ff55` plus
  working API/node patch SHA256
  `56cfa374d8164388c71afbaa9f27963b0b530938c151a489cbd069f91d9f2f25`.
- Diagnosed: local-send fixture moved destination to source node without seeding
  its port reservation; unchanged Transfer reserves a port before local-send
  selection. Added only that fixture row. Two ordinary-wire expectations wrongly
  omitted HaveAPI's resource namespace; changed to assert `dataset == {}` and
  ordinary metadata. Production source unchanged after the first batch.
- Fresh exact three-case follow-up: 3/0/0/0, exit0. Selectors API resource lines
  43/51, operation line97; exact example IDs `[1:5]`, `[1:6]`, `[1:4]`.
  Log/JSON `/tmp/backup-disable-d3-followup-runtime.{log,json}`. RSpec40.171s,
  native elapsed62.263s. Final patch SHA256
  `06a37b40b459c7cc2a18e101ecc95abf2f5deaec617394e39d3a63cb2b802ef1`
  exactly matches committed API correction5526c99f7f675977f7b0e4da5b060791bbd09c06.
- API command: `nix develop .#api -c bash -c 'bundle exec rspec
  spec/api/resources/dataset_disable_backups_spec.rb
  spec/models/operations/dataset/disable_backups_spec.rb
  spec/models/dataset_backup_concurrency_spec.rb
  spec/lib/vpsadmin/api/dataset_plans_spec.rb
  spec/models/transaction_chains/dataset/group_snapshot_spec.rb
  --format progress --format json --out /tmp/backup-disable-d3-api-runtime.json'`.
  Preflight dry-run selected56 nonzero examples. Follow-up uses the three line
  selectors above, same options and its separate output path.
- Node command+daemon batch:46/0/0/0 exit0,20.61s. Logs
  `/tmp/backup-disable-d3-node-runtime.{log,json}`. Includes new irreversible
  suffix regression proving successful create/deletion/metadata confirmations,
  retention of failed/future rows, no preservation rollback and failed followers.
  Command: `nix develop .#libnodectld -c bash
  /tmp/backup-disable-d3-node-runtime.sh`; script SHA256
  `24e77e97e9d5c0a672ddefd9cb374fb8be6b6a4e1d9c06fbc6404a6ae32cbd48`.
  Uses ignored isolated `.gems` under declared shell, preserving Nix RUBYLIB;
  real require base64/Bundler proof and46-example dry-run passed. No dependency
  product or lock changes. Node input unchanged in final API follow-up.
- API RuboCop8files0offenses; node spec root-bundle RuboCop1file0offenses.
  API catalogs normalized with `rake vpsadmin:i18n:update`; D2 keys removed.
- Fixture3paths: actual Nix-evaluated scripts for both existing remote fixtures
  passed `ruby -c`. Nixfmt3files passed. Selectors16runs55assertions0fail;
  both registered suites carry derived `storage-backup` tags. No new harness. Retained dataset_plans CI mapping selects storage/WebUI;
  removed the obsolete NoOp selector together with its removed D2 payload. Raw evaluated JSON/scripts and logs under
  `/tmp/backup-disable-d3-*`.
- Mandatory precommit and commit-msg hooks passed for API, I2 UI and fixture
  commits. No bypass. Advisory width warnings only; message lines<=80.

## Storage execution pending

The remote two-target source now checks normal lagging preservation, held-snapshot
partial deletion, retained per-snapshot markers/live checksum, deliberate remaining
cleanup, reenable higher tree/full then incremental send inputs and older-gap
construction rejection with unchanged source/plans/history. The interrupted-send
fixture checks no source deletion on preservation failure, source snapshot/live
checksums and plans, failed dependency followers, deliberate fresh retry and
retained backup payloads. Both reuse existing remote-common helpers.

No VM/browser integration execution, deployment, push or merge occurred. Actual
ZFS/data-integrity execution remains after independent final review. API and
scheduler guards must be deployed together before exposing the action. Software
rollback cannot restore destroyed snapshots; fatal/unknown chains need normal
reconciliation. SDK final-source reconciliation remains I3-owned.

## Documentation routing

| Topic and reader | Class and authoritative home | Fidelity evidence |
| --- | --- | --- |
| Disable behavior, API/CLI administration, failure and reenable | Reference/how-to: vpsAdmin `docs/storage/disable-backups.md`, linked by storage README/index | Source and focused specs; lead final prose/CLI review; exact ordinary namespace assertions |
| Transaction confirmations and locks | Reference: existing `docs/transactions.md` | Read for implementation; node command/daemon tests |
| PHP confirmation and receipts | Developer explanation: `docs/webui-backup-cleanup.md`, I2 | I2-owned source/tests/final wording |
| Temporary revisions, checks and publication limits | Individual execution: session design/plan/state and this evidence | Owner logs, exact ranges, no production claims |

Main-agent wording pass approved all new errors unchanged and applied bounded
storage-guide/CLI corrections. No session-only rollout state moved into product
docs. API export remains documented by existing `docs/api-schema-export.md`.

## History and migration provenance

Initial baseline: `81e930b25fa3252d7e849aff4819e663cec37b07`.

Old, unpublished/unmerged/undeployed series:

1. `46a4a1c0bd33c9f2c318086d475b1e289a50c678` — original D2 API.
2. `1fad9eee08f971d2417c0e26f0f96f731452ff55` — original D2 PHP.
3. `5526c99f7f675977f7b0e4da5b060791bbd09c06` — D3 API correction.
4. `f634d35d6e7d63c62f0b987bc497cb82116bc591` — D3 PHP correction.
5. `68fb14949dfb58afb7e94f7ba37dd2338e3d23e0` — D3 fixture source.

The first autosquash candidate `d692e428d7054ff42201f71c6abb851df47277c8`
had exactly the same full tree as old68fb149:
`93f2e632dc0418a703ce7be2cd3ec5c027bc1f97`. Final inventory then removed
one obsolete NoOp selector line and folded it into the API commit. No other
source difference is permitted by the final equivalence check.

Both old and final ranges contain **no migrations**, schema changes, dependency
or channel updates. No original migration version was released, deployed,
merged or externally consumed because none exists. D2 API wire additions were
unpublished implementation only; removed rather than supported. The final series
contains no transition/fixup commits. Product code/config restored to baseline
includes NoOp, DetachBackupHeads and API Nix service; unused legacy
DatasetPlans.confirm is unrepaired. No repeated pin/generated-input streams.
SDK generated candidates are separate I3 work and require exact final input
provenance reconciliation.

API subtree at export release5526c99 and final:
`bed58750a34e8d78532b9eb1c62a1fe8c1f58f9f`.
Export-tool subtree at both:
`5d291b4cc5c6c3c59bcef42fa0399a15bfe88b62`.
These establish source identity, not a replacement for I3's final provenance and
schema/client checks. The API/node runtime assertions and fixture quick checks
are reusable for their identical source inputs; no whole-suite retry was run
merely for rewritten SHAs.

## Review boundary

This is a high-risk destructive storage/API change. General, architecture,
scope/proportionality and risk/compatibility lanes apply; the lead owns invoking
independent review after all cross-package final inputs are reconciled. No review
or deployment acceptance is implied by this owner report. I1 retains diagnosis,
source, test, documentation and review-fix ownership. No merge, feature push,
release, deployment or session lifecycle action was performed.

The only extra final cleanup was an obsolete CI selector for unchanged NoOp.
Its first attempted command used `bundle exec ruby` and correctly failed because
the root bundle does not include minitest; no Git mutation happened. Reused the
repository's established `nix develop .#vpsadmin -c ruby` form and16/55 passed.
No dependency edit or product workaround was made. The required hooks passed,
then this selector deletion was folded into the API commit.

## I1 owned changed paths

```text
api/lib/vpsadmin/api/dataset_plans.rb
api/lib/vpsadmin/api/locales/cs.yml
api/lib/vpsadmin/api/locales/en.yml
api/lib/vpsadmin/api/operations/dataset/disable_backups.rb
api/lib/vpsadmin/api/resources/dataset.rb
api/models/dataset_action.rb
api/models/transaction_chains/dataset/backup.rb
api/models/transaction_chains/dataset/disable_backups.rb
api/models/transaction_chains/dataset/group_snapshot.rb
api/models/transaction_chains/dataset/snapshot.rb
api/models/transaction_chains/dataset/transfer.rb
api/spec/api/resources/dataset_disable_backups_spec.rb
api/spec/models/dataset_backup_concurrency_spec.rb
api/spec/models/operations/dataset/disable_backups_spec.rb
docs/storage/README.md
docs/storage/disable-backups.md
libnodectld/spec/nodectld/command_spec.rb
tests/ci-selection.yml
tests/suite/storage/backup-multiple-destinations-remote.nix
tests/suite/storage/backup-remote-interrupted-send.nix
tests/suite/storage/remote-common.nix
```

## Full final diffstat

```text
api/lib/vpsadmin/api/dataset_plans.rb              |  47 ++-
 api/lib/vpsadmin/api/locales/cs.yml                |   5 +
 api/lib/vpsadmin/api/locales/en.yml                |   5 +
 .../api/operations/dataset/disable_backups.rb      | 193 +++++++++++++
 api/lib/vpsadmin/api/resources/dataset.rb          |  69 +++--
 api/models/dataset_action.rb                       |  21 +-
 api/models/transaction_chains/dataset/backup.rb    |   7 +-
 .../transaction_chains/dataset/disable_backups.rb  |  96 +++++++
 .../transaction_chains/dataset/group_snapshot.rb   |   7 +
 api/models/transaction_chains/dataset/snapshot.rb  |   5 +
 api/models/transaction_chains/dataset/transfer.rb  |   7 +-
 .../api/resources/dataset_disable_backups_spec.rb  | 116 ++++++++
 api/spec/models/dataset_backup_concurrency_spec.rb | 109 +++++++
 .../operations/dataset/disable_backups_spec.rb     | 314 +++++++++++++++++++++
 docs/README.md                                     |   3 +
 docs/storage/README.md                             |   5 +
 docs/storage/disable-backups.md                    | 133 +++++++++
 docs/webui-backup-cleanup.md                       |  38 +++
 libnodectld/spec/nodectld/command_spec.rb          |  33 +++
 tests/ci-selection.yml                             |   1 +
 .../webui/specs/storage-backup-export.spec.cjs     |  41 +++
 .../backup-multiple-destinations-remote.nix        | 189 ++++++++++++-
 .../storage/backup-remote-interrupted-send.nix     |  60 ++--
 tests/suite/storage/remote-common.nix              |  68 +++++
 webui/forms/backup.forms.php                       |   7 +
 webui/forms/dataset.forms.php                      | 167 ++++++++++-
 .../lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.mo | Bin 161605 -> 164903 bytes
 .../lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.po |  90 +++++-
 webui/lang/locale/vpsAdmin.pot                     | 107 ++++++-
 webui/pages/page_dataset.php                       |   4 +
 .../tests/Regression/DatasetDisableBackupsTest.php | 276 ++++++++++++++++++
 31 files changed, 2138 insertions(+), 85 deletions(-)
```

## Final quick identity checks

- `git diff 5526c99f7f675977f7b0e4da5b060791bbd09c06 HEAD -- api libnodectld nixos` is empty.
- `git diff d692e428d7054ff42201f71c6abb851df47277c8 HEAD` is exactly one removed
  `api/models/transactions/utils/no_op.rb` selector line in `tests/ci-selection.yml`.
- Final autosquash tree equals its checked pre-rebase tree. Logs:
  `/tmp/backup-disable-d3-{api-commit,fixture-commit,consolidation,selector-fix,final-consolidation}.log`.
- Final API topic expansion after deletion: full/core432eligible specs, exactly
  once in13nonempty identical topics, `/tmp/backup-disable-d3-topics.log`.
- `git diff --check 81e930b..HEAD` clean; no schema/migration paths changed.
- No `backup_disable_manifest`, `preservation_chain`, `PreserveForDisable` or
  `full_new_tree` source remains in API, node library or storage guide.
- Original and final range diffs in `/tmp/backup-disable-d3-final-range-diff.txt`;
  exact revisions and source-equivalence conclusion retained here.

No operation-owned process remains. Completed mutation sessions:30149(API),
68786(fixtures),12210(initial consolidation),47095(selector correction),28181(final
consolidation).58985failed before Git mutation on the Bundler/minitest command
noted above; all exited. Fresh runtime watcher operations were owned/accounted by
lead, with terminal receipts. No outstanding I1 tool cell/session effects.

## Post-review storage verification operation

Lead cleared the final review/history gate and accepted the exact two-fixture
packet `i1-storage-verification-packet.json`, SHA256
`1cdc4065472fd97bc3efad20c25561d24eec0c2996f14ece86b0aa64056e1ca0`.
Source remains `e303d336c538a75938eba08e646fbd9501afe124` with tree
`eaa2b1a7bf030b91815e90ff0159a1c5cfc045b9`. Only the two existing storage
fixtures are authorized, with cache preflight, exact selection and resource
checks before conditional VM execution. I1 owns the shared runner window first;
I2 browser execution and I4 browser overlap remain held.

Watcher policy was resolved from the selected `dev-session` wrapper to
`/nix/store/qgza552gsjwlbyqxrzrv50mz69z1bd9l-dev-workspace-0.2.0`, schema6,
catalog `1184a2cf511b6e77ff7afe12433027abe06e8bb0b897f39cffc26efd443d1a7c`.
Native utility `dw_c699c3bf36ffc569cca1d7f83580bf68e6fffbb536cfad0d` is
`gpt-6-luna`/low, max1, full_access. Actual CLI uses explicit approval never and
danger-full-access; member settings are unchanged. I1 is active parent through
terminal command/effect accounting and does not poll the utility's command logs.

The first fresh watcher `01a212e7-7de8-74a2-acfa-28cac72b488f`, CLI2701225/
parent tool45341, stopped incomplete before any verification phase. The brief
embedded the packet but omitted its explicit existing pathname. All5read-only
command starts completed, CLI exited0, and verification roots remained uncreated.
Its launch/events/result receipts are retained unchanged as
`i1-storage-watcher-*`. No test/cache command was retried or duplicated.

The corrected fresh watcher is `01a212e9-a6ca-71c2-9159-7bc731b79536`,
CLI2716207/parent tool30713; artifacts are `i1-storage-watcher-2-*`. It verified
packet digest, exact head/tree/clean status and all6declared file hashes. Actual
cache command launch is proven by native item4 and owned NixPID2719931,
parent2719920, with exact packet `preflightArgv` and canonical cwd. This is cache
preflight execution, not proof of selection, VM launch or test success. Final
outcome/effect receipt will be reconciled below when available. I1 remains
responsible for diagnosis; utility owns observation only.

### Cache-phase outcome and remaining-phase utility

Watcher2 completed its cache command with actual exit0, UTC
2026-11-25T13:34:24.675686+00:00–13:37:24.682503+00:00,
monotonic180.007s. It stopped incomplete before selection/VM on a conservative
name-based classification. Its4native command starts all completed; CLI and
NixPID2719931 exited; no test state, runner, guest or socket was created. The
utility omitted the requested exit JSON, so I1 reconciled a clearly owner-authored
receipt at `/tmp/backup-disable-storage-e303d336-run1-exit.json` while preserving
all original native output. Cache plan:714local derivations and331substitutions,
369.3MiB download/1.6GiB unpacked.

Bounded actual-derivation inspection established that this was image assembly,
not Linux compilation:

- Compile derivations `3slqrmfmm3jqz8x99rcvi2qr10y3w1dq-linux-6.12.118.drv`
  and `fk3a7aby05xaf0j14zc0hfa14p4bh985-linux-6.12.118.drv` are absent from
  the local-build plan. Their kernel outputs `alkl9mci…`/`hmjinny…` and modules
  output `j632l5z…` are explicitly in the substitution plan.
- `896cwhip…`/`zk88gh4…` linux-modules derivations use buildEnv to merge existing
  precompiled outputs and regenerate depmod maps. They explicitly prefer local
  assembly and disable substitution; there is no compiler invocation.
- `whx4sv24…`/`i98qabmn…` modules-shrunk use modules-closure.sh to copy selected
  precompiled dependency files; `nblinbcx…` initrd uses make-initrd-ng/cpio and
  compression. No kernel compilation is scheduled by these derivations.

Raw inspection records are
`/tmp/backup-disable-storage-{kernel-assembly,base-kernel}-derivations.json`;
compact proof is `i1-storage-cache-proof.json`. No source, flake, build
configuration or kernel-policy exception was introduced. The initial JSON
inspection was adapted to this Nix's versioned `derivations`/`structuredAttrs`
format after a read-only parser assumption failed; no build command was run.

Fresh remaining-phase packet `i1-storage-continuation-packet.json`, SHA256
`81fc2abab5ddcd24bb1f2f60937339d386fe4acfa1bcccc72f1c2fe08cea9c6d`,
binds the accepted packet and exact successful cache receipt/log/proof. It reuses
this passing cache evidence instead of repeating the unchanged180second check.
Only selection→resources/source→the same two-fixture runner remains; new terminal
receipt is `/tmp/backup-disable-storage-e303d336-run1-test-exit.json`, preserving
the original phase receipt. The guard names actual compiler derivations and the
five inspected assembly derivations, avoiding another substring false positive.

Fresh watcher3 `01a212f1-253a-7053-ba58-905b14ff3682`, CLI2777634/parent
11397, was launched under the same re-resolved policy. Its input/cache-proof
verification passed and exact selection is running. `i1-storage-watcher-3-*`
retains native launch/events/result. No actual VM/test launch is claimed until
its authoritative start receipt. ParentI1 stays active; no command-log polling
beside the utility, no retries, source edits or overlapping browser launch.
