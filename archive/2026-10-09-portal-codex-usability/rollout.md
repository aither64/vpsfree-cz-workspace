# Aitherdev rollout

Deployed and verified on 2026-10-09. The user authorized deployment via
vpsfree-cz-configuration. Default-branch integration remains unapproved.
All three actual resets remain available; checks used no live redemption POST.

## Initial delivery sources

- codex-web: `860d515d0aa5d2f7ad68893db41f0969c78e00a7`
- dev-workspace: `675504f638d21578e87a94f460cc9cbf9e0df395`
- workspace: `5448392af308b64cd28af4c0c665d68cf81e18a7`
- vpsfree-cz-configuration: `081ac7cc6098f79b004f7ff349e71c85257b518f`

Extension source remains 0ff827df13e82dfab4b536ff29979280f264e8f5.
Host/profile composition check passes at runtime 675504f6.

## Predecessor and transition

Previous profile: /nix/store/a6c63h1ik2y4ghgn7gz53wn418mlq9qc-dev-workspace-0.2.0.
Previous host: /nix/store/cd5wdjz1v9fji8c2hjlbd1wdgczhh05z-nixos-system-aitherdev-26.05.20261006.b253099.
Native Codex 0.160.0 is retained by the compatible live-switch policy. The
portal/router restart and browsers reconnect; persistent formats do not change.
Forward-only recovery retries the same switch or selects a newer fixed package.
Do not force an older package or clear unrelated lifecycle/cluster state.

## Executed sequence

1. Packaged/provider/browser/runtime/workspace checks and aitherdev build.
2. Exact aitherdev confctl dry-activate, inspect changes.
3. Exact aitherdev confctl switch; verify host services.
4. workspace-host switch --source the initiative workspace worktree.
5. Verify selected profile, native Codex identity, portal assets and read-only
   live limits/credit count. No live redemption POST.

All five steps passed. The host switch used the exact built generation with
`--dry-activate-first --enable-auto-rollback`; both host health checks passed.
The stable `/home/aither/bin/workspace-host switch --source` command selected
the initiative workspace worktree and passed protocol/semantic compatibility
checks. The package transition used its existing forward-only recovery policy.

Selected profile:
`/nix/store/0krn8v92j23j0xdkia8l43iphsh4iwkk-dev-workspace-0.2.0`.
Selected host:
`/nix/store/pzhs0yvpcpsmami7gvrvdv1hx3yb47gx-nixos-system-aitherdev-26.05.20261008.7c8764b`.
Selected native Codex remains
`/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0/bin/codex`.
Codex MainPID 1204139 did not change; the restarted portal is active at
MainPID 2002921.

Byte comparisons of the served app, reset controller, refresh, upload, sync
and conversation modules match the final source files. The session page serves
app.js?v=26. Read-only live limits report credits, `canReset: true`, three
available resets, three detail rows and three expiration dates. Reset IDs,
account scope and balances are omitted from this record. No reset POST was sent.
The public session URL verifies TLS with the configured public CA and returns
the expected HTTP401 without credentials. Private portal GETs return HTTP200.
The ordinary system CA bundle does not trust the private CA; see the existing
[local-CA note](../../notes/dev-workspace/2026-10-02-local-ca-portal-checks.md).

## Evidence

Read-only account check before deployment: selected App Server reports credits,
three banked resets and three detail rows. No redemption request was sent.
The installed old portal only reports windows, confirming the data was lost
in its earlier account presentation.

Initial independent review and focused lock rerun pass after four Important
findings were resolved. Provider CI run 37943560998 passed at 860d515d.
Provider packaged checks and all seven real-browser cases pass, including
native text paste and binary/mixed clipboard attachments.


Runtime exact-head CI 37945562244 passed at 675504f6. Superseded current-day
runs finished; cancellation attempts were denied by token permissions and
no unrelated run was targeted.

All runtime fast package checks and composed workspace checks/build passed in
1,757 seconds. Host generation 2026-10-09--17-06-31 built successfully; 509
derivations, kernel and modules fetched from cache. No local kernel build.
Parent launched portal-codex-usability-dry.service with exact source guards and
atomic exit evidence under /tmp/portal-usability-deploy-evidence/dry/.
Dry activation exited zero. Parent then launched
portal-codex-usability-activate.service; host-switch, profile-switch and overall
exit statuses are zero. Activation completed in about 82 seconds. Complete
local deployment evidence is under /tmp/portal-usability-deploy-evidence/;
each mode has its own log, stage and atomic exit.status. Fresh Luna/low watchers
observed the parent-launched operations without deploying or retrying.

## Approved visual follow-up (executed and verified)

The compact account/composer presentation was deployed on 2026-10-09 from:

- dev-workspace: `577d5b72b9bdcd68e37cd74f6304b2ca80b8bf97`
- workspace: `76bc6985207e44d1bee4d57c9454924dc2e4f88e`
- vpsfree-cz-configuration: `04ee1fe64e40e9b2c40f073556210196cc37cf88`

Provider `860d515d0aa5d2f7ad68893db41f0969c78e00a7` and extension
`0ff827df13e82dfab4b536ff29979280f264e8f5` remain unchanged. All sources are
committed/published; the workspace branch was rebased patch-equivalently onto
shared master c31fd962. The previous delivery commits are retained because they
were consumed by the initial deployment.

Independent final review passed all four lanes with no findings, including
the coherent full 11-commit history and explicit no-migrations conclusion.
The fresh Luna/low verification watcher ran the affected browser fixtures,
runtime package checks, composed workspace checks/build, aitherdev build and
exact CI run 37956710362; all passed. Browser cases completed in 63 seconds.
Evidence: /tmp/portal-visual-checks.log and /tmp/portal-visual-checks.exit (zero).
Screenshot-only temporary fixture copies preserve the committed test assertions
and application bytes; capture files use mocked data. The lead inspected the
limits, desktop composer and phone composer captures before deployment.

The parent launched guarded dry activation for exact host generation
2026-10-09--18-40-23, inspected its successful result, then launched guarded
host/profile activation. Host-switch, profile-switch and overall exit statuses
are zero. Both host health checks passed. The existing compatible live-switch
policy preserved native Codex 0.160.0 and MainPID 1204139; the restarted portal
is active at MainPID 3194295.

Selected profile:
`/nix/store/hkl8717mdlm57abxg56ykjh3v3jxi6ri-dev-workspace-0.2.0`.
Selected host:
`/nix/store/hjd6dqs0r2vvidihlkgpw7v99hqjyzqr-nixos-system-aitherdev-26.05.20261008.7c8764b`.
Native Codex still resolves to
`/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0/bin/codex`.

Served app.js, style.css and reset-credits.js byte-match the final source.
Session HTML selects app.js?v=27 and style.css?v=6. Private GETs return HTTP200;
the public stable session URL verifies TLS using the configured local CA and
returns the expected unauthenticated HTTP401. Read-only account data still
reports credits, three available resets, three reset detail rows and three
expiration dates. No live reset POST was sent; account IDs and balances are
omitted from this record.

Deployment evidence: /tmp/portal-visual-deploy-evidence/{dry,activate}/, with
independent logs, stage statuses and atomic exit.status files. Dry invocation
172d550f744f403182034c44d275a866; activation invocation
dfba0da0a79a4cbda55567fd527a24b6. Fresh Luna/low watchers only observed these
parent-launched operations. Their verified native identities are
01a1218d-e913-7690-b2b7-a27c7e487a8c and
01a1218e-a1a8-7c72-b54e-1bf9d1cb17b7, respectively.

A stable `dev-session url` call that waited across the profile switch was
correctly rejected as belonging to a superseded package generation. Rerunning
the stable command after activation succeeded. No transition bypass was used.

No default branch was integrated. The initiative remains active and ready,
awaiting explicit merge direction for the four repositories.

## New-session paste correction (executed and verified)

Deployed on 2026-10-09 from these clean, published feature heads:

- codex-web: `860d515d0aa5d2f7ad68893db41f0969c78e00a7` (unchanged)
- dev-workspace: `c650a4c7ee38ebd546ce91cbbe2f0713abe6bae4`
- workspace: `97ab907c6a1a57b5a7dccf5601459cfdf18650ac`
- vpsfree-cz-configuration: `557c97a730a0517de1b9db9bc9eafeecd5a79785`

Extension remains `0ff827df13e82dfab4b536ff29979280f264e8f5`. Matching runtime
composition passed. The new input paste option uses the existing shared handler,
with no API, persisted-format or migration change.

Final four-lane independent review passed without findings at the original
follow-up snapshot. The first browser run exposed the fixture's stale trusted
origin. Parent inspected its one-line test-only correction under review step9,
then consolidated only the unconsumed source/pins. The coherent final series has
14 commits; already deployed provenance remains. No obsolete unconsumed history
or migrations. Diagnosis and review evidence are in state.md and review.md.

The corrected usability/creation regression passed in 7.69 seconds; creation
settings/recovery passed in 3.95 seconds. Runtime evaluation/generic-source and
composed workspace checks and full package build passed. Full package Go and
Ruby suites passed, with expected skips and no failures/errors. Aitherdev build
produced exact generation 2026-10-09--19-22-15. Exact runtime CI 37963716009 passed.
Total authorized verification batch was about 14 minutes, exit 0. Full evidence:
/tmp/portal-creation-paste-retry.log and /tmp/portal-creation-paste-retry.exit.
Unchanged team/extension/namespace and host VM variants were not repeated for
this bounded browser-option correction. No local kernel build occurred.

Parent launched guarded exact-generation dry activation, inspected its passing
result, then launched host/profile activation with dry-activate-first and host
auto-rollback enabled. Dry, host-switch, profile-switch and overall statuses are
zero. Both host health checks passed. Existing compatible protocol and semantic
checks preserved native Codex 0.160.0 and its MainPID 1204139. Portal restarted and
is active at MainPID 3496724.

Selected profile:
`/nix/store/81y60n11hr869w4d73jld43r3x3y1l6p-dev-workspace-0.2.0`.
Selected host:
`/nix/store/lz94vc6b11c6n17bbd9rnafszswkmvya-nixos-system-aitherdev-26.05.20261008.7c8764b`.
Native Codex remains:
`/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0/bin/codex`.
The preceding visual-delivery profile/host are recorded above and remain the
predecessor evidence. Recovery follows the existing forward-only package policy;
no forced older package, cleared state or transition bypass was used.

Live served app.js, style.css and reset-credits.js byte-match final source.
Index and own-session HTML select app.js?v=28. Private GETs succeed; the public
stable session URL verifies TLS with the configured local CA and returns the
expected unauthenticated HTTP401. Read-only account data reports credits,
canReset:true, three available resets, three detail rows and three expirations.
No live reset redemption or test-session POST was sent. Account IDs and balances
are omitted from this record. Browser creation and reset mutations were mocked;
actual draft uploads reached only the disposable test server.

Deployment evidence: /tmp/portal-creation-paste-deploy-evidence/{dry,activate}/,
with logs, stage statuses and atomic exit.status files. Dry invocation
832afb4b4c7e46aca3129493b8626e67 passed in about 31 seconds; activation invocation
44107c500f154ca6bf862cdd9fde58db completed by observation after about 97 seconds.
Separate fresh Luna/low watchers observed the parent-launched operations without
retrying or deploying. No operation remains running.

All feature refs are retained and published. No default branch was integrated;
the initiative remains active and ready, awaiting explicit merge direction.

## Prepared numbered clipboard rollout

Provider7dab7630, runtime66262519, workspace07b39360 and configuration1f356990
are committed/published, with preserved extension0ff827df and unchanged native
Codex. Workspace prior pin patches were rebased unchanged onto shared21624498.
Generated confctl message retained. Composition passes. Review and post-review
checks remain pending; this rollout has not been activated. Build the exact
package/host heads, retain new generation, dry-activate it, then guarded
confctl switch and separate /home/aither/bin/workspace-host switch --source
feature workspace. Read-only smoke compares app29 and provider upload6 assets
and verifies account resets remain3. No actual reset/session creation calls.

## Executed numbered clipboard rollout

All reviewed heads were built, checked and deployed. Provider7dab76305dc0084735095d6dbdaef607585d9bca;
runtime66262519d497073d9bb0dccc2252cdec4528f389; workspace07b393609417e921d5b1c2cfec7b3d89abc473ab;
configuration1f3569902a4a6b02633019cd172eade5afe90005. Extension0ff827df remains fixed.

- Host generation: 2026-10-09--20-31-44.
- Host store: /nix/store/g7grfapc1lky4p94r37yhf8y2rj5vn20-nixos-system-aitherdev-26.05.20261008.7c8764b.
- Workspace profile: /nix/store/za0yzb4j1ahkdgnbciix3plfzsyhcwrr-dev-workspace-0.2.0.
- Native Codex: /nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0/bin/codex, MainPID1204139 preserved.
- Portal MainPID3762055; its running executable proves selected profile.

Dry unit portal-codex-numbered-paste-dry invocation117b83600e4043babf20735986229f75
completed exit0 in about77s. Activate unit portal-codex-numbered-paste-activate
invocation3a118da9ebf94075a51e199c9b3ca2af completed in53.940s: wrapper exit0,
host/profile stage0 and host health2/2. Parent launched each guarded operation;
separate fresh Luna/low utilities only observed its retained logs/status. Evidence
/tmp/portal-numbered-paste-deploy-evidence/{dry,activate}/. No remaining process.

Read-only smoke: deployed app/static/provider bytes match final source; app29
selected by index and session HTML, provider conversation14 imports uploads6.
Live account still reports credits and three reset credits with three detail/expiry
rows. Native0.160.0 and its PID retained. Public TLS with configured CA gives
expected unauthenticated401. No actual reset/session creation was used for tests.
Browser fixture passed9.28s; packaged Go/Ruby checks passed (401/5408,12/50,126/988,
expected skips), exact provider/runtime CI succeeded. Full batch about15minutes,
exit0; /tmp/portal-numbered-paste-checks.log and .exit retain evidence.

Refresh the portal to use numbered paste. Source branches remain unmerged and
active, ready awaiting explicit repository/target integration direction. Recovery
uses a newer compatible forward package under the existing lifecycle policy.
