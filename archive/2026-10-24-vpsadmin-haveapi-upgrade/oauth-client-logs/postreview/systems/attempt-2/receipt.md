# PHP-only final postreview: checks passed, publication held

Exact configuration `60af1a1f0930c731d6f0bbabd0a0cb3ed21b550a`, tree
`5ba2ab16c503be3e6e95a1d18006b49815782e29`, selected published P0
`75c691b17c48115f929b57ef55f78935be006ea6`. Source stayed clean/frozen through
all checks. Lead accepted reviewer0 native01a18e5c-de50 Sol/xhigh/read_only
ALL4/HIGH NO NEW FINDINGS, complete FCC four-commit history/one pin/NO MIGRATIONS.
Prior original findings/failures remain their original scopes, not relabeled.
[PHP-only source/review packet](../../../php-only/review-packet.md).

## Actual outputs and complete inputs

Four ordinary sequential declared-shell `confctl build --max-jobs1 --cores2
--yes EXACT_TARGET` calls, CPU60–63/nice5; original-owner monitoring because
retained840 utility unavailable. Original batch98859 consumed0, no unexpected
local kernel work. No canceled component build/check/fixture ran.

| Target | Actual system output | Actual derivation | Build |
| --- | --- | --- | --- |
| proxy | `/nix/store/3yjwzag7xz4aacnydmnkxmp33xwy4hfy-nixos-system-proxy-26.05.20261026.718f670` | `/nix/store/9nl8zmyf68zlb14qsinj4fiqw80kijyr-nixos-system-proxy-26.05.20261026.718f670.drv` | 105.719s |
| webui1 | `/nix/store/h5r10wz203mca9cmlzn9gqhx9bq1ank1-nixos-system-webui1-26.05.20261026.718f670` | `/nix/store/sl5466kfs0wi3n3r3v7qvn2dfs9jz0a4-nixos-system-webui1-26.05.20261026.718f670.drv` | 85.697s |
| webui2 | `/nix/store/yw2v2fnr3yngp8zj3v5zbmv1178c98nm-nixos-system-webui2-26.05.20261026.718f670` | `/nix/store/4y1paxl68xgp2isgm1l76qcby13j2qrz-nixos-system-webui2-26.05.20261026.718f670.drv` | 71.371s |
| webui-dev | `/nix/store/aab10yxryd7dfip17kshgyfz7scs3gja-nixos-system-webui-dev-26.05.20261026.718f670` | `/nix/store/vghrgf6m23cr070yd0qdi78hrm1ra79n-nixos-system-webui-dev-26.05.20261026.718f670.drv` | 59.612s |

[Exact commands/results](build-results.json), [preflight](preflight.json),
[full graph/NAR/root receipt](full-graph-root-proof.json). Each `ALIAS-identity.json`
links its complete recursive derivation graph and recursive output closure with
SHA256. Four graphs contain4167 unique derivations and1225 unique closure paths;
no missing dependency/reference edges. Every closure path has its NAR hash.
[Root/source/system NAR metadata](root-NAR-info.json).

Clean configuration source `/nix/store/1ghcr38azid75vnhxifnpg5vn5r5nxfn-source`
is persistently rooted and all477 files/modes/symlinks match committed60af,
without extras. [Full source proof](source-full-identity.json),
[locked flake graph](flake-metadata.json). All64 lock nodes preserved. Each actual
system embeds clean60af configuration metadata; each services generation input
binds75c and its exact locked NAR. Normal system/input roots and config source
root remain under `roots/`. Config source is an evaluation input; the full tree
is not falsely asserted a runtime derivation dependency. An initial receipt
assertion making that assumption was corrected using the existing source/command/
metadata chain, without recollecting graphs or inventing an edge.

## Generated configuration and syntax

[Actual proxy proof](proxy-generated-proof.json) confirms three HTTP+three TLS
PHP server sets. Dev now has one protected pair and retains its Basic-auth file.
All carry one safe access log, scoped suppressed error output and strict-origin
policy with upstream copies hidden. HTTP301 retains full wire target; ACME
challenge precedence/webroot, names/aliases/listeners/cert references, maintenance
and backend selection are preserved. Three ACME service units are byte-identical
to prior inputs. Existing API/auth and React server blocks are byte-identical
to prior7fdb. No production cert/key/private Basic-auth file was read.

[All WebUI pools/backend proof](all-WebUI-generated-proof.json) covers three
actual FPM pools selecting `error_log=syslog`, normal log_errors and worker
capture still enabled. Backend nginx safe logging/header/entrypoint routing is
preserved. [HAProxy proof](HAProxy-generated-proof.json) binds unchanged actual
HAProxy config bytes, request logging off for PHP prod/dev and existing API,
and unchanged binds/backends/metrics.

Actual selected nginx `-t` passes for proxy, production and distinct dev configs:
[proxy](syntax/proxy/result.json), [production](syntax/webui1/result.json),
[dev](syntax/webui-dev/result.json). Private user/network namespaces, copied
config only; public nixpkgs test certs and synthetic auth file, pid/log/user
runtime paths substituted as recorded. No daemon/host listener or production
credentials. Unrelated unchanged prasiatko duplicate-name warnings remain visible.
Actual HAProxy `-c` [passes](syntax/haproxy/shortpath-result.json). Its first
scratch-only path exceeded Unix socket length; [original failure](syntax/haproxy/result.json)
retained. Only a short private runtime path prefix corrected it; no product,
settings, source or build retry. Syntax copies do not claim production credential
validation. The earlier optional pre-review IFD failure remains incomplete old
proof; normal builds here are new actual evidence, not a relabeled eval retry.

## Installed P0 and runtime result

[Actual installed source/package binding](installed-P0-source-package-proof.json)
links package deriver in final recursive graph, installed page_login bytes equal
released75c, vendor path and matching Composer lock/source revision.
[First actual runtime paths](webui1-runtime-paths.json),
[both production runtime inputs equal](production-PHP-equality.json).
Direct same-session handoffs e2479807 and8e626043 delivered to E2 as soon as
realized; no wait for all targets and no duplicate runtime sequence.

Lead accepted E2 [installed P0 receipt](../../php/attempt-3/receipt.md),
[five-case result](../../php/attempt-3/p0/result.json) and
[effect reconciliation](../../php/attempt-3/p0/reconciliation.json).
One actual HTTP/FastCGI/private-syslog sequence on selected installed FPM/nginx/
ini/pool/P0, preserving default scan behavior and logging settings. Effective
syslog/log_errors1; exactly three fixed callback diagnostics plus benign ordinary
native error present. All callback sentinels absent from final captured native/
FastCGI/nginx/FPM sinks. Setup/provider TypeError/provider Exception return generic
HTTP200, success preserves auth/order/HTTP302, ordinary initiation error remains
HTTP500 with native diagnostic. Production runtime inputs match exactly, so one
sequence covers both. Known namespace initgroups warning retained. E2 FPM/nginx/
collector/namespace effects ended0; no active operation. Prior failed missing-sink
attempt remains failed for old inputs, superseded only by these corrected inputs.

Dev's application root is mutable and not asserted equal to75c. Its generated
pool/proxy policy passes; real source binding/login acceptance remains a later
separate scope. No production/live login or historical log-absence claim.

## Final handoff

[Effects](effects.json): all four build PIDs gone, capture handles consumed,
source/index clean, no active source/Git/build writer, no uncertain E1 effects.
No source changes since review; full history/pin/removal/migration evidence stays
in the PHP-only packet. All old recovery refs, checkouts, private ignored files,
roots and actual7fdb evidence retained. No session/lifecycle/cluster/parent3922,
deploy/dry-activate/preStart, production/default action or CI campaign.

**STOP for lead acceptance and later feature-publication release.** No feature
push or default integration was performed. This receipt establishes build,
generated configuration and bounded installed synthetic P0 behavior; it does
not claim production deployment or mutable-dev real acceptance. Session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
