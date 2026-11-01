# E1: production channel and documentation OAuth preparation

Requested outcome: prepare the approved vpsAdmin consumer channel update and
reusable deployment instructions. The user will create the dedicated docs
OAuth client before activation. No production action is authorized by this
source package. Lead/architect accepted design.md's2026-10-30 E1 section and
HTTP redirect appendix; lead completed the context-owner operator-writing pass.
Existing [plan](../plan.md), [state](../state.md), [design](../design.md) remain
lead/architect-owned. Session `2026-10-24-vpsadmin-haveapi-upgrade`.

## Exact deliverable and complete history

Repository `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
Owned registered worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-cz-configuration`.
Branch `2026-10-24-vpsadmin-haveapi-upgrade-docs-deployment`.
Fresh canonical default/base `fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627`; no upstream delta at final fetch.
Final head `d0024528e93da895deeb4b7efc2b68c1461c94ec`, tree `18448041543e983a6c5932277bcc0e5cc829dddf`.
Own worktree clean, all command handles reconciled, no source writer active.

Complete TWO-commit range:
1. `f4366508b50508c4e0a6185e8d82cfff3c07b77d` — `vpsadmin-config: prepare OAuth sign-in for API documentation`.
   Optional hook, focused tests, four scoped API/auth frontdoors, required
   operator guide and discoverability pointers are one functional change.
2. `d0024528e93da895deeb4b7efc2b68c1461c94ec` — generated `inputs: set vpsadminServices to 33d6c772`.
   One normal exact channel update, separated from functional configuration.
   Generated full changelog and native hook behavior preserved verbatim.

[Complete commit series](commit-series.txt), [complete final diff](final.diff),
[generated pin message](generated-pin-message.txt). Exactly seven changed paths:
- `cluster/cz.vpsfree/vpsadmin/common/frontend.nix`
- `configs/vpsadmin/api/README.md`
- `configs/vpsadmin/api/api.rb`
- `docs/operations/vpsadmin-documentation-oauth.md`
- `flake.lock`
- `mkdocs.yml`
- `spec/configs/vpsadmin/api/documentation_oauth_spec.rb`
No obsolete approaches, follow-up/fixup commits, repeated pin streams, pending
migration iterations, compatibility shims or generated-tool framework. The one
services-input stream moves directly from4a21 to final33d6; no interim A0 head
was pinned. Previously merged upstream dependency commits in the generated
consumer changelog are external lineage, not redundant E1 commits to rewrite.

## Input and source boundaries

Actual command in the declared config `nix develop` tools shell:
`confctl inputs channel set --commit vpsadmin vpsadmin 33d6c7723b392c828de2165854d106d9528f9305`.
[Command identity](channel-pin-command.json), [full log](channel-pin.log),
[result](channel-pin-result.json): exit0,38.890s, parent78492 consumed.
No manual flake edit or disabled changelog. [Semantic lock proof](semantic-input-proof.json)
compares the complete before/after JSON: ONLY node `vpsadminServices` changes,
ONLY locked `rev`, `narHash`, `lastModified`. Input original/follows unchanged;
all other nodes exactly equal, including nixpkgs/confctl/devWorkspace,
vpsadminProduction/Staging, vpsadminWebui and notification-template revisions.
Their existing follows composition now sees the intended new service source.
New source33d6 tree `ffab19170fee23226eced451ba18776c01273e84`,
NAR `sha256-YbtMmXT2QSGt/TI2laas2KyNDkgEi4uZayliuUkwzeY=`;
old service source `4a21dd25b23de9832166def98526f410416b651e`.
Full lock SHA256 `2dbacb72ec8ee369571ea922d69dabd518712045e849b70ee1461c78d9b0a8aa`.

A0 lead accepted final published consumer baseac10..33d6, package/product checks
and independent SSH publication proof. Preserve the actual reviewer history:
reviewer0 Blocking R1 at76ba (obsolete Git-installer args passed to strict common)
was resolved by exact six-line removal, bounded eval and normal hooks under
step9 narrow-fix inspection. This is not relabeled as an original no-findings
review. A0 source/evidence: sibling `package-032/vpsadmin` and `postreview/resume-3`.
This receipt does not claim deployed production source or database state.

**NO MIGRATIONS** in E1 or complete4a21..33d6 consumer interval:
[full migration inventory](consumer-migration-inventory.json) proves all348 inventory entries (315 actual core/plugin migrations plus33
migration specs), paths, file modes, types and Git objects exactly equal.
No new/modified migration version or merge/release/deployment/external-use
migration lineage exists. No coordinated Node upgrade is introduced.

## Intended behavior and review boundaries

The hook retains ExceptionMailer and derives the documentation label from
`core.api_url`. It reads optional JSON and the stable key through
`File.join(VpsAdmin::API.root, 'config', ...)` because authored config is a
store symlink. Missing JSON means anonymous docs; malformed/missing fields,
key read failures or consumer validation errors raise sanitized startup errors
without nested causes. Scopeall/session3600/switch defaultfalse follow the
consumer contract. The supervisor shares authored config but receives no private
files. Source contains no production secret or automatic provisioning helper.

Four API/auth production+maintenance backends use the existing HAProxy Unix
socket and disable only API request logging. Only those TLS/HTTP vhosts receive
trusted edge headers, query-free access logs and `/dev/null` error logging.
TLS uses forceSSL=false/onlySSL=true; four unique HTTP-only partners preserve
same names/DDNS aliases,301 wire target and certificate-backed ACME webroot.
Explicit redirect stays in location `/` so HTTP-01 wins. The old unsafe access
log fragment is replaced while `error_page503 @maintenance` remains. Shared
Varnish/PHP/React/console/download/global logging and binds are untouched.
The API metrics60-second Varnish cache is intentionally bypassed on these routes.
No provider/upstream module change or generic proxy framework was added.

The142-line operator guide (lead writing pass preserved byte-for-byte) explains
existing-interface client creation BEFORE deployment, dedicated confidential/
nondefault/fixed3600/no-refresh/SSOoff/exact callback; provider from
`core.auth_url||core.api_url`, scope in docs config; regular0600/API owner files
in0750directory on both API hosts, same>=64byte stable key, store/runtime symlink
boundary, no supervisor credential sharing, proxy-first activation, real TLS
acceptance later, paired rollback and preservation/revocation limits. No client,
JSON or key was created and no host accessed. README+MkDocs point to one guide.

## Quick checks and reuse

- Ruby syntax and8focused optional-hook RSpec cases PASS; scoped RuboCop PASS,
  parent76151/15.164s, [full log](quick-hook-corrected.log) and
  [source hashes](quick-hook-corrected-result.json). Earlier test-style lint
  failures remain retained, diagnosed and corrected before commit.
- Pinned Nixfmt+Nix parse+diff check PASS, parent25654/11.692s,
  [log](quick-proxy.log)/[result](quick-proxy-result.json).
- Operator/README local Markdown links and MkDocs target PASS before commit;
  final committed range whitespace, exact scope/history/clean checks PASS.
- Normal source commit hooks Nixfmt/RuboCop and commit-msg PASS; native72column
  TextWidth advisory only, all authored message lines meet documented80.
  Generated pin commit hooks/identity PASS with message/changelog preserved.
  No hooks bypassed. Declared environment Ruby3.4.9/Overcommit0.73.0.
- All hook/test/prose/link files match the prior quick-tested functional source.
  The only subsequent functional difference is E1-R1's literal nginx option
  move, checked again with Nixfmt/parse and normal hooks. Entire confctl/nixpkgs/shell/dependency/follows
  graph otherwise equal. Reuse checks only for their unchanged fixture/syntax/
  docs/tooling scope; this is NOT final generated native module or runtime proof.
  No duplicate focused suite or broad fleet/API/browser/SDK campaign performed.

Normal hook setup recovery documented in [setup note](setup-note.md). The first
worktree-add post-checkout lacked local pinned gems; declared Nixshell setup
recovered, then public same-existing-worktree registration validated path/branch
without duplicate Gitadd/checkout or bypass. Both effects/handles reconciled.

## Independent review and next gate

Overall risk HIGH: OAuth credentials/trusted forwarding/privacy logs and future
deployment/rollback. Request ALL FOUR retained final-review lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility; include full
history/consolidation and explicit NO MIGRATIONS. Lead verifies/assigns retained
reviewer0 saved settings. All intended source changes are committed and quick
checks pass; original independent E1 review at aead is complete with sole Blocking E1-R1.
The exact requested option move below is ready for lead step9 inspection.
No postreview build pass is claimed.

After accepted review, target ONLY ordinary proxy.prg/api1/api2 builds/evaluation
and followed WebUI/notification service composition: effective4HTTP+4TLS names/
aliases/listeners, no automatic unprotected redirect, unchanged301+ACME SANs/
webroot, no unsafe duplicate logs, inherited maintenance/ACME safe logging,
edge headers, direct HAProxy/request loggingoff; nginx syntax; API service
user/group/state path/private regular-file preservation and selected package.
No production dry-activate/fleet build. Actual unexpected kernel build stops
under the workspace procedure; ownership/logs/effects stay with executor.

Publication is pending review/check release; no push/default integration or
production client/key creation/activation authority is implied. Configuration
sourcepackage does not install A0 or repair a running system. Retain preceding
channel/config/system identities for later authorized rollback; private files
and client/key survive software rollback, and removal of JSON does not revoke
issued tokens. Live provider/TLS/credentials require later separate acceptance.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/

## E1-R1 narrow remediation, final source identity

Original retained reviewer0 all4/HIGH report at fcc7..aead remains ONE Blocking
E1-R1 with no additional source findings; original history/consolidation/
NO MIGRATIONS accepted. It is not relabeled as no-findings. Original reviewed
packet/tree/diff/evidence are preserved unchanged in [E1-R1](E1-R1/review-packet.md)
and recovery ref
`refs/heads/2026-10-24-vpsadmin-haveapi-upgrade-docs-deployment-E1-R1-reviewed`
at `aeadca545be5df868be8d6c7b8a9839cb8ec8952`.

Exact replacement `services.nginx.appendHttpConfig` -> `commonHttpConfig`
was folded into owning functional `f4366508b50508c4e0a6185e8d82cfff3c07b77d`; identical generated pin
replayed as `d0024528e93da895deeb4b7efc2b68c1461c94ec`. No fixup/redundant pin commit.
[Old/new narrow diff](E1-R1/old-new-narrow.diff),
[range diff](E1-R1/old-new-range-diff.txt),
[all-outside equality/pin-message proof](E1-R1/narrow-fix-proof.json).
The log_format payload and every other path/mode/object are exactly equal;
lock bytes, generated pin patch and full message unchanged.

Focused Nixfmt/parse/diff PASS; normal amend precommit Nixfmt/RuboCop and
commit-msg hooks PASS without bypass (same72column advisory only).
Rebase edit handle98233 and amend/replay92397 reconciled exit0; normal saved
identity and original authored messages used. Unchanged hook8/prose not rerun.

[Selected proxy evaluation](E1-R1/selected-proxy-eval-result.json): PASS0/25.286s
at exact final head, --max-jobs0 and allow-import-from-derivation=false, no build.
Source role exact33d6, selected systemdrv
`/nix/store/3xq7g6srriimhz6nd0hlf78nkwf039fr-nixos-system-proxy-26.05.20261026.718f670.drv`.
[Actual selected nginx text ordering](E1-R1/selected-nginx-ordering-proof.json)
binds system->etc->nginx derivations; named log_format offset4608 precedes all8
scoped access_log references (first8311). Actual text SHA256
`ca862e12fc6e57c2c93d4300eb2309ad7a0b564603cca24460746682830709bc`.
Pinned nginx module emits commonHttpConfig at303 before vhosts307/append309.
Full generated syntax/runtime/targeted package checks remain postreview gates.
No broad campaign/build/production action/source expansion. All owned handles
consumed, final own worktree clean, no active operation or writer. Lead step9
inspection applies without reviewer rerun only while this exact boundary holds.

## Final postreview/publication handoff

Lead accepted E1-R1 under step9; no reviewer rerun required. Targeted3builds,
generatedconfig/service/NAR/root/fullgraph/composition checks PASS at unchanged
d002; no broad campaign. [Postreview receipt](postreview/receipt.md) preserves
actual artifact identities, failed-environment originals and scope limits.
[Publication receipt](publication/receipt.md) proves exact ownfeature remote,
unchanged default and clean/no-writer effects. No merge/deployment/liveproduction
acceptance is claimed. Source ownership released after this completed handoff.
