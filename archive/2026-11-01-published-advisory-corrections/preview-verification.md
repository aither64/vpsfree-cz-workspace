# Development preview verification

Current status: **development preview stopped and fully released at the user's explicit request**. The lead executed the supported public-wrapper stop and reset/full-release commands, both exit0. Redacted proof after stop: found=true/state=stopped/ready=false; after full release: found=false. Preview disks and configuration were removed by that authorized release. No production deployment, session archival/deletion/stop, private helper or implementer manual cleanup occurred. The access URLs, source/store paths and samples below are retained historical evidence, not an available running preview.

All five reviewed heads were integrated by the lead into their approved targets: API master `942c6eaed41331f823d8e0f670ed239e2b308440`, KB master `f97785c2c265172a4c78893e0673034fde56e4dd`, config master `c4107822060e9e34b24a83950d618c9f28a7722b`, modern main `1c8478bceb3943645ec06ccde895ee4b0985873f`, client target `2026-07-13-security-advisory-automation` at `0b771120bb2a878c012512b685208124c2b4263b`. Exact feature refs remain; all merge claims are released and driver/observer terminal0. Lead evidence: `/tmp/2026-11-01-published-advisory-corrections-merge-20261103T132728Z/`, especially `cluster-release.json`, per-repository results/remote proof and reviewed histories. No duplicate Git/cluster checks were run for this receipt.

Final local strictKBf977 passed509.55s and exactAPI942cadmin browser cases3/3 passed; original API, services34, user4, lifecycle3 and native/role evidence retain their recorded source/input reuse boundaries. Exact942c feature CI completed success. At the single post-merge snapshot, new master API CI was in progress/API Specs queued with quick workflows successful; master KB Managed was in progress/Check queued. Originalf977 Managed failure remains a user-accepted out-of-scope Ubuntu mirror package-setup failure, deeper cause unknown; UFW follow-up was withdrawn before launch. Original count/lock unknowns and duplicate local utility provenance limits remain explicit in [visibility-verification.md](visibility-verification.md). No pending pipeline is claimed green.

## Historical preview execution and access

Original preview start: cluster **running and ready**. Integrated start exited 0 in **968.78 seconds**. The user requested a running preview of both WebUIs; this is not production deployment or integration. Keep the cluster running and preserve its data for manual use. Both WebUIs passed normal CA-trusted login and advisory access checks. API and modern worktrees remain clean at the requested heads. No verification utility or browser command remains active; only the intended cluster runner and guests remain running.

## Historical access (preview released)

| Service | URL |
| --- | --- |
| Legacy PHP | https://webui.aitherdev.int.vpsfree.cz/ |
| Modern React | https://newadmin.aitherdev.int.vpsfree.cz/ |
| API 7.0 | https://api.aitherdev.int.vpsfree.cz/ |
| OAuth provider | https://auth.aitherdev.int.vpsfree.cz/ |
| Captured mail | https://mailpit.aitherdev.int.vpsfree.cz/ |

Login values are available in the **session portal → Cluster → service credential fields**. They are not copied into this receipt. All services use development accounts and this session's database.

The browser needs the internal/VPN route and DNS plus trust in the development CA. Download the public [preview CA certificate](preview-ca.crt) and trust it as a website CA in the browser/OS trust store. No private key is included. Its source is `.dev-clusters/vpsadmin/certs/default/vpsadmin-ca.crt`.

SHA-256 fingerprint: `1C:60:3B:7C:2C:95:48:ED:32:DC:3B:49:33:5A:AF:89:C9:54:F0:7D:EE:04:77:07:03:1B:C6:7C:AD:FB:57:14`.

Trusted `curl --cacert` requests pass chain and hostname checks. Chromium normal NSS trust passed modern login with no TLS bypass. Python 3.13's stricter default X.509 mode rejected the generated CA because it lacks a key-usage extension; this tool-specific limitation remains recorded rather than silently changing verification flags or replacing the CA.

## Inputs and launch

- Accepted [preview plan](preview-plan.md); exact session/environment identity verified.
- API/legacy clean own worktree: `49f5a29e5a7d85559d06d31496acb5c08895bcda`.
- Modern clean own worktree: `1c8478bceb3943645ec06ccde895ee4b0985873f`.
- OS standard provider input: canonical local `origin/staging` at `823d7b7a84277edfd77f474fc1640a1cf756e8f7`, without fetch/ref movement. Actual store source `/nix/store/bxj9slkz81b09wl8diaz6vyz7f062nyy-source` matches all **2367 tracked Git blobs** at that revision.
- Initial state: config and socket identity only; no retained disks, runner or applied selection. Only config change: `dns.enable: true → false`; every other semantic value and recorded socket identity retained. The services resolver, modern UI and Mailpit remain enabled.
- Host `br0`/KVM/bridge-helper prerequisites passed. Single/bridge starts exactly services and node1, each 8192 MiB/4 CPUs.
- Parent-owned command: `vpsadmin-devcluster start 2026-11-01-published-advisory-corrections --topology single --network bridge`.
- Fresh pinned Luna/low observer watched private status/logs and finished; it did not launch/retry the mutation. No timeout, reset, force, kernel escalation or source mutation was used. At 625 seconds the exact owned Nix client had 118.27 seconds CPU and waited on daemon IPC; no concrete blocker was established. Normal startup subsequently passed.

Selected configuration: `/nix/store/3w6s6bbka0qm95219dah3x7dn4dnfdhy-os-test-vpsadmin-devcluster-2026-11-01-published-advisory-corrections.json`, SHA-256 `cd631e7c78efb8a45cd42a5d7fdf019b5a537d3f6d53e1ef5b149efa2c2efa60`.

Applied selection is nonpending and contains full-boot proof for both guests. Running `/run/current-system` matches each selected descriptor. Provider labels attest `webuiSourceKind=worktree`, `webuiSourceRevision=1c8478bceb3943645ec06ccde895ee4b0985873f`, `webuiSourceDirty=false`. This is distinct from modern package build-info metadata, which reports unknown revision/dirty for the path input; source-byte proof establishes the actual selected content.

## Runtime evidence

- **node1** system: `/nix/store/bhkf4ar8pq4fbj9jwpvgk4zq3i8ynq2m-vpsadminos-system-dev-node1-26.05pre-git`; derivation `/nix/store/c8q8jjf2m5pdf8z5zfjxm348v4figkzd-vpsadminos-system-dev-node1-26.05pre-git.drv`. Complete closure: 721 items; list SHA-256 `a0b035bb9d02bff6c8843baf7f57db46d2f364d1f3ea63bd50c677e2224c701b`.
- **services** system: `/nix/store/wzid0563rxs78bbn1dg0yfzhg4ianynj-nixos-system-vpsadmin-services-26.05pre-git`; derivation `/nix/store/m0xk2mpzp8i4drcs106yjwgjixz7zjby-nixos-system-vpsadmin-services-26.05pre-git.drv`. Complete closure: 1482 items; list SHA-256 `2cca0b4b9e97a42e1e72864da0f8875309211ae48dccffbf063d7bd16c8621c5`.

API unit ExecStart and working directory use `/nix/store/c69zk5frfs6703mbw0arh2awp06r69rh-vpsadmin-api-49f5a29e5a7d85559d06d31496acb5c08895bcda`. API, supervisor, legacy container, modern container and mailer are active. HTTPS OPTIONS confirms successful 7.0 versions/default envelope; authenticated 7.0 node reads pass. Live PHP advisory page, forms and main stylesheet match the clean worktree's SHA-256 hashes. Modern actual frontend is `/nix/store/qhq8ykqd3lqmbjq48crbxff0v14j3vhz-vpsadmin-webui-frontend-1.0.0`; BFF is `/nix/store/mgi5vi58sjgjxjc32bfrxv4mxfm6lrc4-vpsadmin-webui-bff-0.1.0`. Both derive from `/nix/store/rf9zg89hf0ksirxgaqfcpli1qbkqg7zq-source`; 2541 tracked source files and seven installed BFF runtime modules match clean modern1c847 bytes. Exact derivations, normal OAuth and honest path-input build-metadata limits are in [modern-preview.md](modern-preview.md) and [modern-preview-source-proof.json](modern-preview-source-proof.json).

A concurrent plain status call returned nonblocking-lock failure while SSH checks held the cluster lock; sequential native status then passed running/ready. The packaged CLI's default `api.vpsadmin.test` URL reaches the wrong nginx virtual host after provider domain overrides, returning 401 before any writes. Using the configured trusted HTTPS API works normally; no configuration/source workaround was made.

The actual mailer daemon configuration sends SMTP to `127.0.0.1:1025`; the active Mailpit unit listens at the same loopback address. Captured messages were **0 before** and **0 after** guarded fixture publication/retraction. Both publications explicitly used `send_mail=false`. Final count after normal browser login checks is **3**, all ordinary new-sign-in notices for the synthetic administrator; there are no advisory messages. A guarded same-name original PUT on published advisory2 preserved visible content/state/publication identity and advanced revision1→2. The final messages remained sign-in notices only. The initial final-zero assertion therefore failed on legitimate login mail; the retained actual message classification corrects that expectation without clearing mail, retrying publications or claiming zero total. No external SMTP route was used by these advisory operations.

## Ready-to-try synthetic advisories

All summaries/descriptions and node notes clearly identify development test data. `CVE-2099-0001` is a test identifier, not a security assessment. The eligible node is `101` (`dev-node1`). No VPSes are seeded, so affected VPS/user projections are empty. Keep these examples intact for the user; browser checks only open/cancel forms and confirmations.

| ID | Name | State / revision | Node assessment | Links |
| --- | --- | --- | --- | --- |
| 1 | Preview: editable draft | draft / 1 | row 1: unknown | [PHP](https://webui.aitherdev.int.vpsfree.cz/?page=security_advisory&action=show&id=1) · [React](https://newadmin.aitherdev.int.vpsfree.cz/admin/security-advisories/1) |
| 2 | Preview: published correction | published / 2 | row 2: mitigated | [PHP](https://webui.aitherdev.int.vpsfree.cz/?page=security_advisory&action=show&id=2) · [React](https://newadmin.aitherdev.int.vpsfree.cz/admin/security-advisories/2) |
| 3 | Preview: retracted original | retracted / 2 | row 3: mitigated | [PHP](https://webui.aitherdev.int.vpsfree.cz/?page=security_advisory&action=show&id=3) · [React](https://newadmin.aitherdev.int.vpsfree.cz/admin/security-advisories/3) |

Created through ordinary HTTPS API requests. Every original/node correction and retraction supplied the current revision and state; publications supplied the current draft revision. No production import, broad test-suite setup, database reset, or application source edit occurred. The published and retracted examples use synthetic mitigation timestamps `2099-01-01T10:00:00Z`.

## Browser results, limits and ownership

Modern acceptance passed two normal login/callback cycles, administrator identity, Secure/HttpOnly/SameSite-Lax cookie and logout/re-login. Published2 and retracted3 original editors and delete confirmations were opened/cancelled; published2 direct retract and separate announcement composer were opened/cancelled. No advisory browser write occurred.

Legacy normal administrator login, all three advisory detail pages, published/retracted edit forms with exact state/revision guards, and the bounded named node form passed. Its first observation-only run reached all these functional checks, then failed an overbroad zero-blocked-origins assertion. One corrected read-only observation retained the actual blocked asset inventory and passed with all functional/TLS/host-block guards unchanged. `https://cdn.jsdelivr.net` and `https://use.fontawesome.com` asset requests were aborted; successful auth/data requests used the configured PHP/auth/API origins. Third-party appearance was not verified. Legacy retract/delete confirmation dialogs were not exercised in this bounded preview check; modern confirmation controls were verified as described above, and full legacy acceptance remains separately retained in [api-acceptance.md](api-acceptance.md).

Final ordinary API reads confirm ID1 draft/rev1, ID2 published/rev2 and ID3 retracted/rev2; their visible sample content remains intact. Final native status is running/ready, single/bridge, runner PID1475262. Both source worktrees are clean at API49f5 and modern1c847. Start and modern observation utilities completed, both bounded legacy browser commands exited and closed their browsers, and no fixture/check process remains active. The cluster runner and two guests remain intentionally running for the user. No production/default-branch integration, physical deployment, reset, release, stop, or session lifecycle action is authorized.

Private operation evidence: `/tmp/2026-11-01-published-advisory-corrections-preview/` (start/config snapshots, applied state, graph/closure lists, API responses and bounded browser result). Raw logs and private credentials are not portal artifacts.

Session portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/

## Visibility correction: actual services update

Authorized parent command: `vpsadmin-devcluster update 2026-11-01-published-advisory-corrections services`; exit0,319.3s. No reset, force, stop, fixture/data edit, source rewrite or fetch. The fresh observer returned incomplete early; the parent kept the exact mutating process handle through its successful exit and verified effects. No update remains running. A first combined SSH observation lost its nested `sh -c` quoting and `readlink` had no operand; the corrected direct public SSH observation verified the actual running system below. That was an observation correction, not another update.

- Actual services `/run/current-system`: `/nix/store/mygq0r3nbd1hyb3ddy1r0sbvmsb7n7l2-nixos-system-vpsadmin-services-26.05pre-git`; derivation `/nix/store/jvcdmx7lznl121f825c8y98p2ddf6l5i-nixos-system-vpsadmin-services-26.05pre-git.drv`.
- Running API WorkingDirectory: `/nix/store/rv84rni10460lppzkyznyfx82vjhxw6h-vpsadmin-api-a38c9f871f89312f16d18e158efbbbb340ec53e4/api`.1852 packaged tracked files match clean source;7 executable rewrites differ only in shebang. Both changed runtime query owners match exactly. The derivation-referenced input source path is absent locally; do not substitute a zero-file comparison for source proof.
- API/supervisor/PHP/modern/mailer units active. Provider status running/ready/single/bridge, applied pending=null. Node1 entire descriptor and actual retained system `bhkf4ar8...` unchanged. Config bytes unchanged at SHA256784e5d3b45d343068435cb931c464dff82d61a84b8a19c9cf692fa39d8cf21ef; OS canonical local823d7b7 input retained without fetch.
- Modern original paired frontend `qhq8ykqd...` and BFF `mgi5vi58...` remain in the actual services closure, provider labels exact1c847/clean/worktree. Existing2541+7 source attestation remains applicable; no UI visibility source/build change.
- Normal CA-trusted API matrix:66 read-only requests across anonymous/member/admin,0failures. Wrapped state/parent filters and requested counts, original/CVE direct reads, node/update/outage-link lists all respect published-only non-admin reads. Admin history retained. Live support identity absent; real full/core support-role tests cover it. No new account or advisory write.
- Current samples remain1draft/rev1,2published/rev2,3retracted/rev2. Current Mailpit has0messages. Historical3 sign-in notices were observed earlier, without an immediate pre-update baseline; capture-ID preservation or a removal cause is not claimed. No sink clearing command or advisory mail was sent.

Private applied selections, actual closure/derivation/source/data/mail proofs and update status/logs are in `acceptance/preview-update/` under the visibility evidence directory. The cluster intentionally stays running with its data; no integration, production deployment or session lifecycle action.

### Final normal UI/server policy acceptance

- API:66read-only anonymous/member/admin requests passed with successful HTTP200 envelopes, wrapped state/parent filters and counts; hidden originals/CVE direct reads denied, hidden node/update/outage-link collections empty. Published and admin reads positive.
- Modern owner:24actual-server role cases passed on unchanged1c with normal CA-trusted OAuth. Guest/member list2 and direct1/3 server404/ordinary unavailable UI; admin list1/2/3, direct200 and edit access. Browser closed, fresh utility terminal,0advisory writes. Initial Node CA helper failure was retained; corrected Chromium same-origin fetch used normal trust.
- Legacy:21existing pages passed with normal CA trust and member/admin login. Anonymous/member list2; admin list1/2/3. State-filter and direct original pages reflect server visibility. Browser closed in finally;0advisory writes. External font/CDN appearance coverage is not claimed.
- Samples remain1draft/rev1,2published/rev2,3retracted/rev2. Final Mailpit4messages classify as4sign-in notices,0advisory messages. The immediate post-update snapshot had0; earlier historical3captures have no fresh pre-update continuity proof.

All owned commands are terminal; cluster and shared data intentionally remain running/intact. No further check, CI wait/retry, source/pin change, cleanup/lifecycle, default merge or production action. Receipts frozen for the lead's consolidated handoff.

## Approved live PHP source effect during merge preparation

Before the bounded redirect correction, the accepted preview contract (preview-plan.md46–61) records legacy PHP live-mounted from this session's API worktree. Editing `webui/lib/vps.lib.php` therefore changes the PHP source available to the running preview without a services activation. The approved correction restores VPS list/detail return navigation for origin-only referrers; it does not update the applied APIa38c system or modern1c, restart a service, or change stored fixtures/data. No new live-browser check is claimed here. Earlier “clean/unchanged PHP” statements describe their historical checkpoints; this source effect is explicit during the C correction.
