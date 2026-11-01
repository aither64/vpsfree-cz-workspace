# E5 / 0.31.2 actual runtime acceptance

**Accepted by lead for qualified current manual development use.** Native0, all four guest proofs, real PHP/React access, the primary Go token-documentation remedy and the status locale smoke passed. C1 independent exact-source/native-chain proof was directly inspected and accepted by lead/architect. Cluster, scope, roots, session and owned KB staging remain running/open. No default integration or production publication is implied.

## Current access and completed flows

- PHP: https://webui.aitherdev.int.vpsfree.cz/
- React: https://newadmin.aitherdev.int.vpsfree.cz/
- API documentation: https://api.aitherdev.int.vpsfree.cz/v7.0/
- Status: https://status.aitherdev.int.vpsfree.cz/?lang=en and normal `?lang=cs`.

Requires development VPN/routing/DNS and trust in the workspace CA. Public CA file `/home/aither/workspace/ai/vpsfree.cz/.dev-clusters/vpsadmin/certs/default/vpsadmin-ca.crt`, SHA256 fingerprint `1C:60:3B:7C:2C:95:48:ED:32:DC:3B:49:33:5A:AF:89:C9:54:F0:7D:EE:04:77:07:03:1B:C6:7C:AD:FB:57:14`. curl used --cacert; Chromium used isolated NSS trust with no ignored HTTPS errors or host trust change. Seeded `test-user1` credentials are privately available in the owned config `.dev-clusters/vpsadmin/clusters/2026-10-24-vpsadmin-haveapi-upgrade/config.json`, under seed.users; retrieve locally, never publish config/passwords or native urls output.

Actual member OAuth login **2/2**, logout **2/2**, both return to their correct interfaces; observed API7 GETs all200. PHP EN/CS selections passed. React authenticated users/current and session endpoint200, accessToken/sessionExpiresAt/sessionKey shapes only, no values retained. React authenticated locale switching is not claimed. [Member results](member-login.json). No VPS/member-data mutation, screenshots/traces, credential/token/cookie logging or Go token acquisition.

ONE anonymous English public HTML GET was saved **before** assertions in [anonymous-en-go-token.html](anonymous-en-go-token.html),2812232bytes/SHA256 `62116eea79ec2a20e349d826b2b9c6a1beae35624dc3ccd060d81aa24f5ce60e`. Actual auth-token-go contains `api.SetExistingTokenAuth(os.Getenv("HAVEAPI_TOKEN"))` and the intended Go import, former mismatch limitation absent, advertised X-HaveAPI-Auth-Token/_auth_token unchanged; Basic/OAuth2/init and TS/Rust panels remain. Framework0312 present. This proves rendered existing-token documentation, not a new authenticated Go request. [Assertions](go-token-html.json). One ordinary status-render smoke on its existing EN/CS locale pair returned200 with normal HTML/title and matching html lang, no panic; [results](status-render.json). No extra GET, SDK/auth/browser campaign or retry.

## Native completion, containment and actual systems

Parent65129 fully consumed exit0; nativePID/PGID1216515 exit0 at1793185097.42711 (**2026-10-28 10:58:17UTC**), elapsed1328.65s. Exact attempt [20261028T103607Z](../activation/20261028T103607Z/result.json), scope `vpsadmin-haveapi-upgrade-e-20261028T103607Z.scope`. Parent completion observation proves publicrunning/ready/single/bridge/WebUI2e32dirtyfalseworktree; runner1531763 exactnative4tuple and QEMU1542926/1546495/1547152/1547235 all resident in that active scope after parent exit.32GiB max/12CPU/zeroOOM; peak20511846400bytes. Separate globaldaemon snapshot494772224bytes/MemAvailable54581724KiB is not E-attributed.313 store events were buffered at completion; no per-store timing claim. Parent kernel-alert receipt is empty: no observed HALT alert. No stop/retry/signal/teardown.

Selected built config `/nix/store/lwmf26d62k9w45ky98iy4g95ng4rq6zf-os-test-vpsadmin-devcluster-2026-10-24-vpsadmin-haveapi-upgrade.json`, SHA256 `cd2e27dc75548fdfd2f81f09025b85dbc7a9f12be40cbc05c5557d1f7ba660f6`. Four independent publicSSH-n reads passed current==booted==selected, entire closure validity and existing roots:

| Guest | Selected current/booted system | Standard system-1-link | Additional provider root |
| --- | --- | --- | --- |
| dns-primary | `/nix/store/bvvibi0l6fiz446czzhx6jz9cwv0sc9w-nixos-system-dev-dns-primary-26.05pre-git` | present | present |
| dns-secondary | `/nix/store/pn0mnpnzj4cvsvxmaadxh4is9qrsn67p-nixos-system-dev-dns-secondary-26.05pre-git` | present | absent |
| node1 | `/nix/store/8kqp2iipvxxaxa20v37ha4cyfx509cs4-vpsadminos-system-dev-node1-26.05pre-git` | present | absent |
| services | `/nix/store/4cjjwh6kikppbnqs8r9h0r2mz9jjym2j-nixos-system-vpsadmin-services-26.05pre-git` | present | absent |

[Guest proof](guest-residency.json) is independent of host roots/applied claims. F remains uninstalled: only dns-primary has the extra provider root. **No complete provider retained-boot certificate, future cold recovery or pruning-survival claim.** Standard current roots support qualified current testing; no root/envelope repair.

## Actual package/source/input chain

Canonical reviewed API8102179cf7f7e9bb534965c8acb3e02ef723045f / WebUI2e32c814d3af70ac39257f2542075bd580ee38d4. Accepted canonical20-node graph [e5-start-ready/canonical-metadata.json](../e5-start-ready/canonical-metadata.json), SHA2564e90223c7345528a2e25b40579371e3d19ce98fc5450ce3fa80221cdfb5e8a01; OSf4e55a13/nixpkgs718f670/status5723 and native follows retained. API rawNARsha256-tgQXSKpg5eViCf7nJhLQ/sQ1DT9wNSt/yjKOogiQRv0=, WebUIrawNARsha256-Wz8/aQCPE4qOuhojcDTF6807XjFv+SLnqJAuJPsU2YQ=; API full ignored lock45d4a2b6ecd4aab556869432dab1b7937064f6d4929aa586fff0a0949e25d469. Native outputs differ from standalone A/C inputs; no artifact-equivalence/reuse claim.

[Actual native path/deriver handoff](selected-native-paths.json), [full6749 input graph](recursive-input-graph.json) SHA256 `d96e905e8cdce0651431002302b8413ce8421fdb50d7aebac9a06cfa74aaf433`, [output closures](host-output-closures.json)738/738/721/1482paths, [host roots](host-roots.json) and [normal selected-config roots](selected-config-host-roots.txt) retained. Ordinary nix-store --query --roots reported removal of three stale auto-links to notification-root targets; this incidental native read behavior was disclosed, not an explicit cleanup/GC/repair command. No repeated root query or guest root action.

[Actual package bytes](packaged-identities.json) prove five distinct Ruby HaveAPI0312 packages (client occurs twice), Go Documentation532b38627deec0c2c884506e514875ce696d12522276768815ac104eee7ed1e9, TS Documentation57a9d866a548c86c06c7351bff70b8b8afa18b8c281407053586639ed0b6fd53, Fiddle1.1.8/libffi3.8.0 and nine packaged documentation assets. Actual API `/nix/store/h3i0g2y1p53bgdyms8khj6jwc2i8i85z-vpsadmin-api-8102179cf7f7e9bb534965c8acb3e02ef723045f`; actual PHP `/nix/store/avd5mj4cyj07hn384nzmg5dm6rjagrg8-vpsadmin-webui` contains haveapi/client0312/Guzzle7.16.1. Both native PHP and console-router JS bundles match released ecda280ff53be99964423191e55065e4e3ce9310468203458135ee72aa6e9259. Package/closure proof is not per-process gem introspection or a separate console flow.

C1 [complete independent native proof](../../package-c/0.31.2/native-provenance-e5/receipt.md) establishes exact2e32 filtered2439files/90,124,104bytes/modes/noextras, sourcec054 NARsha256-ZaLAoXcf21glVgdjvUQ47TqCxsMli1ZSXbS30DKF9eU=, and actual frontend117zwv/BFFx1wic derivers/outputs/FODs/locks/Node/services4cjj/nginx26cc/BFFunit chain, reusing this graph/residency without duplicate build/SSH/GET. Both embedded metadata records remain unknown/dirty/unavailable because provider path inputs carry no self.rev. **Normal embedded clean-release provenance gate is not passed.** Independent full source proof supports accepted qualified development use; no metadata fix, standalone output equality, fresh absent npm-cache byte inspection or reproducible-build attestation.

## Operations, evidence and retained state

One fresh retained840 Luna/low/fullaccessnever postboot utility67485/PID1847521/thread01a1822c-efde-7dd0-9cf6-fd6224499374 executed the prescribed related batch once, ~85s/exactbatch0; actual policy saved in [postboot-watcher-actual-policy.json](postboot-watcher-actual-policy.json). [Command log](postboot-check.log), [result](postboot-check-result.json), [utility final](postboot-watcher-final.txt). No postboot harness failure, missing probe or retry. Launcher67485/capture53709/directC1handoff8486 and inner operation all complete; no active E3 handle/watcher/writer. Utility slot released for independent work, no new utility launched. Historical failed helper outputs from earlier phases remain preserved separately.

Only this compact evidence receipt completed after lead acceptance. No further probes/queries/tests/source/dependency/provider/KB/default/index/lifecycle action. Old030/0311 refs/checkouts/private bytes and original receipts retained. KB0312 remains owned/up at its separately accepted [staging receipt](../../package-0.31.2/staging/receipt.md); no stop/release/promotion. Leave native cluster, containment scope, roots, KB staging and session running/open. Main state/handoff/checkpoint remains lead-owned.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
