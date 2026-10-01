# Default-branch rebase and React dev-cluster rollout

Status: all three rebases, generated pins, whole-branch reviews and feature
publications complete. The exact owned cluster was reset and built with React.
Initialization recovery completed, activated packages/providers were verified,
and the compact browser acceptance passed. The cluster remains running in
`read_write` at epoch 4; no shared host or default branch was changed.

Reviewer0 cleared Admin `90184b374..e65a5a6b0` across all four HIGH-risk lanes.
The series has nineteen coherent commits, one generated current-provider pin,
and the two consumed migration versions/blobs preserved. The foundation-guide
copied-owner wording advisory is explicitly accepted for this redeploy; actual
identity owners have restrictive FKs, while scope/target metadata is copied.
No runtime behavior or identity publication changed.

The stable reset/config helpers completed for this exact owned cluster.
The fresh private config preserves reviewed seed/network choices, enables the
distinct React hostname, and adds one dedicated level-99 disposable seed user
through the provider's existing seed interface. Credentials remain private.
The reviewed configuration `5eff558c4` is now published with an explicit lease
against its previous feature head. Its full two-commit review found no findings
and confirmed no migrations. The parent started the exact owned storage/bridge
rebuild after the occupancy check. Fresh Luna/low utilities observed each
long operation through private logs and independent completion markers.

## Final runtime acceptance, 2026-10-02

At exact Admin `e65a5a6b0`, OS `8d05dc3ae` and React `aa2f60b8`, the diagnostic
browser trial passed with exit 0 in about 46 seconds, completing 242 checks.
It proved real React login, member API read, logout and anonymous API 401;
PHP login/status and both review/confirmation mode changes; stale and
same-mode CAS 409; anonymous 401 and member 403; and a valid Pool Create
refusal 423 with unchanged relevant rows. PHP unfreeze returned its normal 302
redirect. Epoch advanced from 2 to 4 with exactly two new transition audits.
No fallback recovery was attempted. Independent root-socket SQL afterward
confirmed `read_write` epoch 4, four total audits, one control row and both
consumed migration versions.

The preceding token-route-corrected attempt failed at PHP unfreeze. It passed
all earlier checks and its nonce-bound API recovery returned `read_write`
epoch 2, but its summary included recovery counters and lacked a UI substep.
The implementer preserved that failed summary before adding fixed numeric
step and failure diagnostics. The final run preserved the actual forms,
submission timing, assertions and TLS checks. It did not reproduce or explain
the earlier failure; no application fix or claim of corrected runtime behavior
is made. Keep this uncertainty if the same UI failure recurs.

Private evidence: `/tmp/storage-redesign-redeploy-20261001/` contains the
separate original, token-route-corrected and PHP-diagnostic logs/results.
The retained pre-diagnostic summary and private helper are under
`/tmp/storage-runtime-acceptance-20261001/`. Only validated numeric outcomes
were forwarded. No credentials, browser state, DOM dumps or raw responses
belong in these records. Source/package provenance is recorded separately in
[devcluster-provenance-20261001.json](devcluster-provenance-20261001.json).

Exact-head Admin API CI `36925295017` passed all 27 jobs; other focused
migration/Node/PHP/lint/client/i18n/contract workflows passed. Broad Admin/OS
CI was still queued at this checkpoint. The upstream React nightly failures
below remain unresolved. The deployment gate is this bounded real-service
trial, not full React nightly acceptance or physical maintenance exclusion.
Historical terminal coverage and child coverage remain unknown; production
strict, identity publication, node quiet, repair readiness and APPLY stay off.

## Fresh initialization failure and supported recovery

The first start returned 1 after waiting for the hypervisor Pool seed. The
actual services guest was reachable with MariaDB running. Database setup had
loaded the current schema, explicitly bootstrapped singleton row 1 and applied
both storage migrations, then failed in the generated ordinary development
seed: the lead-added administrator lacked `namespace.blockStart/blockCount`.
Every configured seed user requires these fields, including level 99. The
account was partially upserted before the error; the API, Supervisor and React
container correctly remained behind the failed prerequisites.

The lead verified eight unused namespace blocks and added that allocation only
to the private disposable configuration. Recovery uses the supported running
services update, preserving the initialized marker, schema and partial seed
upserts. Existing initialization skips schema reload and base `test.nix` seed;
the provider's separate repeatable development seed supplies the corrected
account. Do not delete the marker or replay the generic initial seed by hand.
The provider automatically refreshes node Pool directories and NodeCtld after
successful services activation. The failure did not demonstrate an application
or migration defect and required no source change.

A member accidentally inspected generated seed bytes beyond the helper into
the embedded private admin configuration. The exposed disposable password is
replaced privately and applied through another supported services update before
acceptance. No credential is retained in coordination evidence. Unit completion
checks use `Result` and `ExecMainStatus`: ordinary and React seed oneshots may
correctly be inactive after success.

Both supported updates finished with exit 0, without local kernel compilation.
Live database setup, ordinary/React seeds and credentials preparation have
successful results and exit status 0. API, Supervisor, MariaDB, RabbitMQ, nginx
and the new React container run normally. A fresh private logical DB backup was
taken before stateful acceptance. All three node generations match the selected
build, NodeCtld/osctld run, and actual root-socket responses expose version 1
`gc_trash_v1` with active workers and no provider-unknown result. This observation
does not prove child exclusion or node quiet.

Actual nginx uses the selected frontend output; the BFF's running executable
uses the selected BFF output. The served frontend build-info equals both
installed metadata files under strict CA validation. All three source heads and
trees remain unchanged and tracked-clean, with React fully clean. Detailed
source, derivation, NAR and activation paths are in
[the provenance artifact](devcluster-provenance-20261001.json).

The first browser attempt passed real React login, current-user API retrieval,
logout and anonymous API 401 under trusted TLS. It stopped before PHP login or
any freeze change because the helper's direct-token URL returned 404. The lead
confirmed the versionless `/_auth/token/tokens` route from actual OPTIONS and
the global HaveAPI authentication-chain source. The correct request returned
200, and authenticated current-user/freeze/Pool reads succeeded. Implementer0
corrected only the private helper before retry; the successful React checks
remain evidence. No deployed application fix was required.

The first diagnostic used Python 3.13's default strict X.509 policy, which
rejected the existing development CA's missing key-usage extension before an
HTTP request. The actual browser and Node acceptance clients validate the
provider's CA under their supported TLS policies; the Node diagnostic then
reproduced the route error. No certificate-validation bypass was introduced.

The publication command's captured result was 0 and SSH confirmed the remote
head. The outer login shell subsequently emitted an unrelated unbound-variable
error from `/etc/bash_logout`; this did not invalidate the verified push.
Use a non-login tool shell for subsequent strict scripts instead of changing
system logout code or retrying a successful publication.

The user requested rebasing the active storage work on current defaults and
redeploying the dev cluster with the new vpsadmin-webui component. They then
explicitly authorized resetting this disposable cluster because they had not
changed it. The selected rollout is a fresh storage/bridge cluster, using the
installed provider's optional React service. No shared-host switch or default
branch integration is authorized.

## Verified starting points

| Repository | Feature head | Fetched default |
| --- | --- | --- |
| vpsAdmin | fa7cec3a89e433e91516a369f10b1b17b6eddfef | master 90184b374ce0a139319b66326a29373b92d8ee93 |
| vpsAdminOS | dcad075a171244cc17d67d625ab89c402d11781e | staging 26f28c69149b5312305aceb7f5614bd1d3fe3bbc |
| Site configuration | fc203cb0ff260d741f14a6c446b3d543e9eb06d2 | master 029c616ed906de80b8813cc20391e294c3e9f4c2 |
| React WebUI | aa2f60b89df65d2f987be48784ed42bab7010833 | main aa2f60b89df65d2f987be48784ed42bab7010833 |

The maintenance repository's default remains 2fdc9f2; its feature already
descends from that revision. The superseded instruction-only workspace and
extension branches are excluded. They remain retained.

All three rewritten source branches have `backup/2026-09-23-storage-redesign-before-20261001`
refs. The earlier OS staging port 107cef01 also has its own backup ref. The
new React worktree is registered from main, with no application feature changes.

vpsAdmin has nineteen feature commits and no path overlap with the six newer
default dependency commits. The provider has fifteen changed paths and only
an additive `tests/all-tests.nix` overlap with newer staging. The site branch
has one guide and one generated service pin. The deployed foundation migration
20260924210000 and query-index migration 20260926100000 must keep their
versions and contents even though the VM disks will be reset.

## Deployment boundaries and preparation

The retained slot reports stopped, stale ready, storage topology and bridge
network. Its config and pre-reset disk/result provenance are retained privately
at `/tmp/storage-redesign-redeploy-20261001` (0700; files 0600). Existing G0/G1a
trial records remain diagnostic history. The reset is limited to this session's
cluster through the supported helper.

The new UI is React plus OAuth BFF, alongside legacy PHP. PHP storage-freeze
controls and direct-admin API remain available; this request does not add React
freeze controls. The installed provider supplies the React module, runtime
credentials, separate OAuth client and seed ordering. The intended public name
is `newadmin.aitherdev.int.vpsfree.cz`, which resolves to the disposable frontend.
Use the same-session WebUI worktree to bind both frontend and BFF to aa2f60b.

Require quick checks and independent complete-series/migration review before
long integration. After reset, preserve storage/bridge selection, enable
`newWebui.enable`, and start using the reviewed source revisions. Verify the
fresh core schema, singleton bootstrap, plugins/ordinary seed and React OAuth
seed before accepting services. Verify selected and running revisions,
HTTPS/config/session routes, real login/API access, legacy PHP availability,
NodeCtld/osctld health and storage activity protocol. Any failed phase is
recorded before a deliberate retry; no reset or secret rotation substitutes
for diagnosis.

Production strict, node quiet, repair readiness and APPLY remain off. The
existing advisory capture and rollback limitations are unchanged. No fleet
rollout or repair authorization follows from this disposable deployment.

The React path-input form can truthfully emit unknown/dirty/unavailable package
metadata despite the selected clean Git checkout. Both packages must agree;
record source Git/tree plus derivation/source/output paths separately. This is
development evidence and does not claim clean-release package provenance.

## Source verification and review checkpoint

OS `8d05dc3ae` is published and independently cleared in all four HIGH-risk
lanes, with an explicit one-commit/no-migrations history conclusion. Focused
provider checks passed 36/0 and normal hooks passed. The initial Admin rebase
`eade85a5` preserved every feature blob; focused API 62/0, Node 42/0, PHP
5 tests/17 assertions and selector 18/77 passed.

The obsolete OS pin was dropped at `0bdd6caaa`; all eighteen retained patches
and messages remained equivalent. The required updater generated final Admin
`e65a5a6b0f227f78cdcd40afa6a8de1f5b497b36`, selecting published OS `8d05dc3ae`.
Its lock-only commit also updates the OS's existing two nixpkgs inputs to
exactly their declared provider revisions, with no input mapping changes. Both
consumed migrations and schema blobs are unchanged. Architect conformance
found no blocker; final-pin quick checks and independent whole-branch review
remain separate gates.

The occupied addresses were released by the explicitly requested stable stop
of `2026-09-30-portal-review-improvements` (exit 0). No records, disks or session
lifecycle were changed. Recheck address availability immediately before start.

## Selected React upstream checks

At selected default `aa2f60b`, CI and both Playwright smoke workflows passed.
Nightly run 36847325876 failed two Chromium admin networking examples out of
798 (796 passed); its mobile job passed. Reviewed failed logs show missing
expected rows in `ip_addresses_empty_clear_filters.spec.ts` and
`networking_surfaces_smoke.spec.ts`, including retries. The cause is unresolved;
no rerun or source correction is claimed. These upstream fixture failures do
not establish a storage-rebase regression. The disposable trial must still
prove real login/API/logout and coexistence; it is not full React nightly
acceptance. Private failure logs are retained with this rollout's diagnostics.

## Procedure lessons

Signing Overcommit in Nix and invoking Git in an ambient shell caused signature
refusals before mutation. Signing and running Git in the same declared Nix
context completed normally; no hooks were bypassed.

An operation-only watcher can lack inherited session markers. After parent
identity verification, give its brief the literal verified slug/workspace pair
and canonical directory, and require its own current check. A failed identity
check performs no session operation; a corrected fresh utility observes the
existing run without relaunching it.
