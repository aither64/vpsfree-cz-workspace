# Product HTTP defaults: committed, quick-pass, awaiting final review

Exact final head `45cb49e2ef5e9f570d8cc7d7629d014345fea223`, tree
`138b50e7fb3b5dc4b6eb9ef88aa31c180e1e4053`, clean worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-oauth-client-logs`,
branch `2026-10-24-vpsadmin-haveapi-upgrade-oauth-client-logs`.
**STOPPED before long checks and publication.** [Exact proof](final-proof.json).

## Scope and implementation

The user approved the finish plan including secure vpsAdmin defaults. Follow
design.md's “Product nginx implementation boundary (2026-10-31)” and the
finish-plan security section. Workspace integration/release remains independent
and first priority. Lead owns final prose and review; E1 owns dependent site
configuration simplification and its later generated product pin.

One new coherent commit above published `75c691b17c48115f929b57ef55f78935be006ea6`
changes 12 paths, +758/-70. The private module is 62 lines; the three standalone
fixture files are 555 lines after normal Nix formatting, adapted from the
existing site nginx fixture. No generic proxy/logging framework, new public TLS
option or synthetic virtual-host scheme was introduced.

Product frontend API/auth/PHP access logs omit queries and headers while keeping
method/path/status/size/timings. Raw nginx request errors are suppressed only on
those hosts. API/auth locations derive forwarding headers from nginx. PHP edge
and backend emit strict-origin Referrer-Policy. FPM's overridable native error
destination defaults to syslog; log_errors/catch_workers_output stay enabled.
HAProxy's existing logRequests option defaults false for API/PHP and retains true
for console. Console/download/unrelated hosts retain their prior policy.

The private module's virtualHosts apply sees merged defaults/overrides without
reading back the value being changed. Selected forceSSL hosts retain their
records and literal listeners, render addSSL, and prepend set/return HTTP
redirects with the merged redirectCode and untouched $host$request_uri. Invalid
original SSL-mode combinations reject. HTTP ACME exemption follows the owning
nginx generator's actual certificate/dnsProvider predicate; no certificate,
location or listener is reconstructed. Tests remove the prior masking API
log/header/HAProxy overrides and keep direct HAProxy topology.

The product application, P0 callback code/tests, HaveAPI 0.32 artifacts, API
profiles/specs/default selectors and all dependency inputs remain unchanged.
All 3166 entries outside the 12 changed paths equal 75c in mode/type/OID.
API full effective/packaged lock remains ea0a24b1; Composer c8effa3a; flake
d455fbfe. CI already selects full integration coverage for nixos/** and the
changed service fixture; no selection narrowing or workflow change occurred.

## Quick verification and effects

[Quick proof](quick-result.json) binds every final source-file hash. Commands:

```sh
nix eval --impure --json --expr 'import ./tests/oauth-client-log-protection/module.nix { nixpkgs = (builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-oauth-client-logs").inputs.nixpkgs; }'
python3 tests/oauth-client-log-protection/module_test.py MODULE_VALUES.json
python3 tests/oauth-client-log-protection/nginx.py --module-values MODULE_VALUES.json --output-dir NEW_PRIVATE_DIR
```

Locked nixpkgs source5b2ic4sx generated all actual nginx configurations. Twelve
config cases PASS: plain/addSSL/onlySSL/rejectSSL, forceSSL/default listeners,
global override, custom addresses/nondefault ports, explicit IPv4+IPv6 lists,
one-sided HTTP/TLS lists, shared HTTP ACME and DNS ACME. All three invalid
forceSSL combinations reject; aliases/default identity, safe logging, API/auth
headers, syslog and HAProxy defaults are asserted. Runtime fixture also exercises
own HTTP ACME and static certificates across five protected hosts. Formatted
module output equals the exact native-tested JSON; final evaluation exited0 in
33.849 seconds. [Final evaluation/test](final-module-test.log).

Native locked nginx1.30.4 passed 24 actual HTTP/TLS cases: API and alias/auth/PHP
edge/backend/maintenance redirects308 with exact encoded query before auth;
HTTPS401; HTTP ACME200; proxy callback302/provider502 with unchanged request and
response auth values; authenticated maintenance503; allowed PHP entrypoint
FastCGI-unavailable502 and denied PHP404; exactly one strict-origin header;
benign unrelated204. Synthetic code/state/token/cookie/auth/Referer/provider/body/
response sentinels are absent from captured logs, which retain status/timings.
[Native result](nginx-5/result.json), [path/port/worker adaptations](nginx-5/adaptations.json).
This is actual generated nginx proof, **not installed PHP or application login**.

Normal declared root shell formatting passed, Python syntax and relative doc
links pass, and staged whitespace checks pass. Normal pre-commit Nixfmt,
migration and both i18n hooks plus all commit-message hooks passed; no bypass.
[Commit log](commit.log), handle7144 consumed exit0. Existing pinned840 watcher
unavailability used the documented visible parent fallback; no resource caps.
nginx exited0, upstream thread stopped, ports reconciled; no owned operation or
writer remains. [Native effects](nginx-5/reconciliation.json).

Original unsuccessful native attempts are retained: nginx-1's scratch Unix socket
path exceeded the socket limit; nginx-2 exposed nginx's compiled-in default
global log path, corrected through fixture-only private path configuration;
nginx-3's incorrect maintenance-without-auth expectation was corrected to its
actual401; nginx-4 passed behavior but its unrelated-host control received a
synthetic Referer that ordinary combined logging retained. Protected logs were
clean. The final control uses benign input and the unrelated host is unchanged.
All attempts stopped their owned daemons; these are not relabeled as passes.

## Full history, comparison and migrations

Fresh canonical SSH fetch and independent readback confirmed unchanged default
`ac10a62f1cb0fc890378ae83cdf18dd0e29f049a` and published75c before editing.
[Baseline](baseline.json). Complete ac10..45cb series is five commits:

| Commit | Purpose |
| --- | --- |
| `11b26c0a5f6fa51fc6eb63b8f28dd5e8ccbaf721` | Final released HaveAPI0.32 dependency stream |
| `33d6c7723b392c828de2165854d106d9528f9305` | API docs/OAuth consumer and release checks |
| `a089b530376ca645456597df6a3533f720d24670` | Default-derived documentation test selectors |
| `75c691b17c48115f929b57ef55f78935be006ea6` | PHP callback containment and regressions |
| `45cb49e2ef5e9f570d8cc7d7629d014345fea223` | Product-owned secure HTTP defaults and their tests/docs |

Full diff46 paths/+9046/-5336, dominated by unchanged released JavaScript bundles.
[Complete series](complete-series.txt), [new diff](final.diff),
[complete diff](inherited-final.diff), [old/new range comparison](range-diff.txt),
[paths](complete-paths.txt). Four inherited commits retain the same identities;
one owning behavior/test/doc commit follows them. No repeated dependency update
stream, superseded implementation or unused transition remains.
**NO MIGRATIONS**, no schema/database paths in the complete series and no new
merged/released/deployed/externally consumed migration to preserve.
[Migration history](migration-history.txt).

Published75c is preserved by the local named oauth-client-logs-75c-recovery ref,
its remote feature remains75c, and original review/publication receipts are
unchanged. [Original75c accepted review/history/quick/publication](../package-php-oauth-logs/publication-handoff.md).
Its retained reviewer0 native01a18e25-f990 all4HIGH NO FINDINGS is prior-scope
evidence only, not final review of this new behavior. Earlier inherited A032-R1
and root OPTIONS residual remain honestly recorded in the original packets.
Canonical live33d6, updater3922, all historical aliases/private/recovery inputs
and site configuration were untouched.

## Compatibility, documentation and remaining acceptance

Intentional limit: one-sided literal listener lists remain accepted/unchanged;
the old split-server empty-half implicit listener is not synthesized. Current
inspected consumers do not depend on it. Arbitrary raw server rewrites may affect
exempt ACME requests, and custom headers may apply to redirects; no raw-snippet
parser or equivalence claim is made. Explicit overrides restoring sensitive logs
are operator policy. Per-vhost guarantees exclude pre-vhost parser failures,
sensitive paths and uncontrolled intermediary logs. Varnish pass-through is not
privacy-safe; direct routing remains an explicit consumer topology requirement.
Existing live PHP privacy is not certified by this package.

Owning contract: docs/http-log-protection.md, linked from docs/README.md and
docs/api-client-examples.md. Lead applied the context-owning writing/Humanizer
pass and supplied three exact wording corrections, all applied. No translated
UI text/layout/navigation or KB screenshot change was introduced. Deployment is
edge protection first, matching backend next, callback traffic after both; keep
protective config/topology on rollback. No DB or wire migration/node coordination.

Request retained independent reviewer0 saved Sol/xhigh/read_only for all four
HIGH lanes plus complete history/repeated-stream/**NO MIGRATIONS** conclusions.
Risk is HIGH because logs, forwarding identity, TLS redirects and auth are
affected. After review acceptance/lead release, the existing bounded installed
PHP/P0 and affected services/package checks remain; old75c/config60af runtime
results do not establish new installed-output acceptance. E1's later site
simplification/four-target checks wait final reviewed/checked publication.
No long build/VM/PHP/browser/provider campaign, publication, default integration,
real login, production/live deployment, lifecycle or cleanup was performed here.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
