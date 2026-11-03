# Modern live session preview

## Historical preview — stopped and released by explicit user request

After source integration, the lead executed the user's requested development
cluster stop/release through public stop then reset, both exit0: after-stop state
stopped, after-reset found=false. The source/runtime/OAuth evidence below remains
historical evidence for its exact revisions. No production deployment occurred.
The session remains open; no session archive/deletion/stop or cleanup was performed
by implementer1. Do not infer that the URLs below currently have a running cluster.


## Current server-only visibility acceptance — 2026-11-02

The server-only correction is live at API
`a38c9f871f89312f16d18e158efbbbb340ec53e4`. Implementer0 performed the standard
services update and proved applied pending=null, all relevant services active,
API source bytes and retained DB/config/node1. The actual API directory is
`/nix/store/rv84rni10460lppzkyznyfx82vjhxw6h-vpsadmin-api-a38c9f871f89312f16d18e158efbbbb340ec53e4/api`;
current services system is
`mygq0r3nbd1hyb3ddy1r0sbvmsb7n7l2` (the hash supplied in the immediate READY
handoff; the full path belongs to implementer0's authoritative runtime receipt).
Modern source is unchanged at exact reviewed/running
`1c8478bceb3943645ec06ccde895ee4b0985873f`, tree
`7d3169bc4f80af199631e73cc4442b7985d8cf6d`, clean worktree/index. The same frontend
`qhq8ykqd3lqmbjq48crbxff0v14j3vhz` and BFF `mgi5vi58sjgjxjc32bfrxv4mxfm6lrc4`
package paths below remain in the services closure; no modern rebuild or source
activation was done. Preserve the original path-input metadata limitation below.

User correction is authoritative: visibility belongs to the server. The withdrawn
modern filtering/cache-defense candidate f7c4 remains evidence only; the branch
and draft PR122 are exact1c847. See [withdrawal](modern-visibility.md).

A corrected bounded read-only browser operation passed from
2026-11-02T17:03:57.433Z to17:04:36.937Z (39.5 seconds). The fresh Luna/low watcher
returned exit0 and terminated; Chromium and all role contexts were closed and
the utility slot was released to implementer0 for the legacy check.

| Fresh browser identity | Public list | Direct draft1 / published2 / retracted3 | Admin management |
| --- | --- | --- | --- |
| Anonymous | ID2 only | API404 / 200 / 404; ordinary unavailable for1/3, published2 renders | List and all three direct routes show normal login-required gate |
| Normal OAuth member | ID2 only | API404 / 200 / 404; ordinary unavailable for1/3, published2 renders | List and all three direct routes show normal admin-required gate |
| Normal OAuth admin | IDs2+3 | API200 for all; unchanged public UI shows2+3 and ordinary unavailable for draft1 | List IDs1+2+3; each direct read200, original marker and Edit available |

Actual browser API evidence includes the public list's existing separate
published/retracted requests: anonymous/member retracted filters return empty,
published filters return ID2. Admin retracted filter returns ID3 and the all-state
management list returns3,2,1. These are real API responses, not a mocked/client
hide assertion. Admin CVE rows1/2/3 and node-assessment rows1/2 were observed;
update/outage-link responses were empty in this sample DB. No populated update
history or node3 response is inferred from this short run. All three admin
originals remain accessible; implementer0's broader live API matrix owns the
complete relation/state proof.

Each role used a new Chromium context, with full-document navigation for every
list/direct destination (24 UI destinations, plus normal OAuth redirects).
Anonymous identity was confirmed through same-origin browser `/session.json`
without exposing its fields; member/admin identities were checked against actual
`/users/current`, expected role levels and normal OAuth callbacks. Secure,
HttpOnly, SameSiteLax cookies were confirmed without saving values. No injected
token, mocked response, client filtering code, advisory write or fixture change.
No screenshot/capture/build campaign or source/Git mutation occurred.

The actual devcluster public CA remained normally trusted in Chromium's NSS
profile, no ignoreHTTPSErrors or certificate bypass. The first setup attempt
stopped before advisory traffic because Playwright's separate Node-side request
context did not use Chromium's CA trust. Its failure/log is retained. The parent
changed only the temporary script to read the same-origin session through
Chromium's normal fetch and corrected route-gate assertions from AppShell source.
The corrected operation passed; this setup issue was not an application failure.

The operation blocked external font/CDN and legacy-origin asset attempts:
cdn.jsdelivr.net, use.fontawesome.com and webui.aitherdev.int.vpsfree.cz. Functional
OAuth/API traffic stayed within modern/auth/API origins. Those blocked assets'
appearance is not certified; no production requests were allowed. No physical
mobile/other-browser matrix, older open-tab revocation or production claim.

Sanitized [role result](modern-server-visibility-result.json) is retained here.
Private mode0600 script/log/full sanitized wire-result and original setup failure:
`/tmp/2026-11-02-modern-server-visibility/`. Actual result is `browser-result.json`;
the watcher incorrectly looked for an unrequested `result.json`, so its missing-file
remark does not describe the existing browser-result artifact. Private OAuth
credentials remain only in the own portal file and browser memory; raw auth
responses were not copied here. No advisory email was requested; backend owner
checks captured mail separately. Leave the cluster and samples running/intact.


Session2026-11-01-published-advisory-corrections; accepted [preview plan](preview-plan.md).
Integrated single/bridge cluster was started by implementer0, source API
`49f5a29e5a7d85559d06d31496acb5c08895bcda`, modern
`1c8478bceb3943645ec06ccde895ee4b0985873f`. No separate frontend/server, source,
Git, reset/stop or default integration/deployment action by implementer1.

## Actual runtime provenance

Services running system supplied and residency-verified by implementer0:
`/nix/store/wzid0563rxs78bbn1dg0yfzhg4ianynj-nixos-system-vpsadmin-services-26.05pre-git`.
Actual newadmin nginx ExecStart reads
`/nix/store/picn8ammvkq358mwnb5xf4gpmyyffmxn-nginx.conf`; its static root is
`/nix/store/qhq8ykqd3lqmbjq48crbxff0v14j3vhz-vpsadmin-webui-frontend-1.0.0`.
Actual BFF ExecStart is
`/nix/store/mgi5vi58sjgjxjc32bfrxv4mxfm6lrc4-vpsadmin-webui-bff-0.1.0/bin/vpsadmin-webui-bff`.
Derivations: `/nix/store/4sar4ijblhk5kpnrzyik7sf9mc705z2d-vpsadmin-webui-frontend-1.0.0.drv`
and `/nix/store/k10mgn84hv397iwz81159ym0nkds3d53-vpsadmin-webui-bff-0.1.0.drv`.

Both use cleaned source `/nix/store/rf9zg89hf0ksirxgaqfcpli1qbkqg7zq-source`
(BFF its bff/ subtree). Actual comparison found2541tracked files byte-equal to
clean modern1c847,0missing/0different; all7installed BFF runtime modules also
byte-equal. Provider result-config labels webuiSourceRevision1c847,
webuiSourceKindworktree and webuiSourceDirtyfalse are independently retained at
`/nix/store/3w6s6bbka0qm95219dah3x7dn4dnfdhy-os-test-vpsadmin-devcluster-2026-11-01-published-advisory-corrections.json`.
Applied config pending=null and successful start/residency proof belong to backend
owner. This is worktree byte/selection proof. Served frontend and installed BFF
build metadata say unknown/dirtytrue/sourceunavailable due to path input: do not
call these packages a clean Git-metadata release. Historical clean package receipt
is separate and was not substituted for these running paths.

## Strict TLS and normal OAuth acceptance

Strict curl with the actual devcluster CA passed /healthz(ok), /config.json and
/build-info.json at modern origin. API config is
https://api.aitherdev.int.vpsfree.cz/version7.0, X-HaveAPI-OAuth2-Token and _meta.
Normal user NSS trust imported only the actual public CA, fingerprint
1C:60:3B:7C:2C:95:48:ED:32:DC:3B:49:33:5A:AF:89:C9:54:F0:7D:EE:04:77:07:03:1B:C6:7C:AD:FB:57:14.
Browser used ordinary certificate validation; no ignoreHTTPSErrors, certificate
bypass, token injection, mocked responses, standalone authentication or secret
URL was used. Credentials were read only in browser-script memory from the own
private portal status; none were copied into this receipt or screenshots.

Fresh standalone Luna/low with explicit danger-full-access/never ran one bounded
operation, about70seconds, exit0. Normal /oauth/login redirected to owned auth,
accepted the configured synthetic test-admin, observed /oauth/callback and actual
/users/current response with matching identity and admin level. A Secure,
HttpOnly, SameSiteLax session cookie was verified without recording its value.
Logout and a second normal login passed: two normal login/callback cycles, one
logout/re-login sequence, two advisory original editors opened/cancelled, two
delete confirmations opened/cancelled, and one published retraction confirmation
and announcement composer each opened/cancelled. No advisory write was sent.
The SPA reached live API across origins;
no CORS block occurred for those flows. This is actual dev backend evidence,
separate from the earlier synthetic browser suite.

At /admin/security-advisories/2 (published) and /3 (retracted), original Edit opens
and cancels, Delete confirmation opens and cancels with backup/history-loss text,
and draft-only Publish is absent. Published2 also opens/cancels direct Retract and
the separate announcement composer with its mail choice. No original correction,
announcement, lifecycle confirmation or advisory mutation was submitted. Shared
examples1draft,2published,3retracted remain intact for the user's trial.

The operation blocked unexpected third-party font/CDN and legacy-origin resource
attempts instead of permitting production requests. Successful normal auth/data
requests used only the three configured newadmin/auth/API origins. Third-party
appearance is not certified by this bounded run. No broad browser matrix or
physical-device acceptance is claimed. No auth trace/screenshots were created.
The requested separate browser-command.log was not created by the watcher; actual
private watcher log, result and sanitized browser-result.json exist mode0600 under
own cluster modern-acceptance/. No missing-log content is claimed. Browser closed
and operation exited; utility slot explicitly released to implementer0.

## User entry and remaining limits

Modern admin list: https://newadmin.aitherdev.int.vpsfree.cz/admin/security-advisories
Normal login: https://newadmin.aitherdev.int.vpsfree.cz/oauth/login
Shared examples: append /1, /2 or /3 to the admin list route. Both UIs use the same
development API/DB. Legacy browser verification and captured Mailpit/SMTP proof
are implementer0's package; it reported active local Mailpit capture and total0.

The user needs internal/VPN DNS/routes and trust in the public development CA.
Normal session portal supplies seeded test-admin/other dev credentials privately;
do not copy OAuth secrets, tokens, session responses or passwords into notes.
Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
Keep the cluster running for the trial. Start supplied no cleanup/reset/stop,
archive, production or default-branch authority. Main owns the member-facing
explanation of the UI differences and controls.
