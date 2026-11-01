# E1 targeted postreview: PASS, published source preparation

Exact configuration head `d0024528e93da895deeb4b7efc2b68c1461c94ec`,
tree `18448041543e983a6c5932277bcc0e5cc829dddf`; base
`fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627`. Complete two-commit history is
functional `f4366508b50508c4e0a6185e8d82cfff3c07b77d` and generated final pin
`d0024528e93da895deeb4b7efc2b68c1461c94ec`. Source stayed unchanged through
all postreview checks/publication. Original reviewer0 all4/HIGH report at aead
remains ONE Blocking E1-R1, resolved by accepted mandatory step9 literal option
move; no other findings. Original packet/recovery/evidence retained in E1-R1.
History/consolidation/NO MIGRATIONS accepted:315 implementations+33 specs exact.

## Actual builds and identities

Ordinary repository `nix develop -c confctl build --max-jobs1 --cores2 --yes`
was run sequentially on exact proxy/api1/api2 paths only. CPU60–63/nice5,
original-owner visible fallback (retained840 unavailable), no extra watcher.
All target exits0: proxy144.366s, api1204.804s, api259.328s. Parent87316 consumed,
all children complete; no unexpected kernel compilation. Full command/log/result
files are in this directory and native confctl logs remain in the own worktree.

| Target | Actual normal system output | Derivation |
| --- | --- | --- |
| proxy | `/nix/store/2ck1fdd8c17a46qjkxd4w96mjkf6c59k-nixos-system-proxy-26.05.20261026.718f670` | `/nix/store/k2md6x9a7wsv0m9kv3i5mvpwa19piyhr-nixos-system-proxy-26.05.20261026.718f670.drv` |
| api1 | `/nix/store/xa0r3csqlhkkbnmr01jm233wghnyicms-nixos-system-api1-26.05.20261026.718f670` | `/nix/store/4r8vqavqn9qgbgvm4h86mi6hnk8r91zw-nixos-system-api1-26.05.20261026.718f670.drv` |
| api2 | `/nix/store/lpwcj29a2sxfz9py857dv79j8z4i7idy-nixos-system-api2-26.05.20261026.718f670` | `/nix/store/j1r3f01cif6jdnvbjmqnzg60r3awmacf-nixos-system-api2-26.05.20261026.718f670.drv` |

[Target generations/inputs](target-identities.json), [actual package/source
binding](actual-source-package-binding.json), [full recursive graph](recursive-input-graph.json)
(4291derivations/no missing edges; SHA256
`1077e3e5a9eda933d12dc1f249b89743b7bee319cac23d6631de9efafd285db4`),
[full output closures](recursive-output-closures.json) (1320paths/no missing
reference edges), [roots/NARs](roots-closure-proof.json).
Normal persistent roots remain for all3systems, exact config Git source and
services source. Config source `/nix/store/y0gnailgrnfil0w8dik9p1f8f383qcdw-source`,
NAR `sha256-oXb9HhO1z/RCzyj64LIGBXn8HpcXdhVvP8p6o4voffA=` binds clean exactd002.
All3actual services-input files bind33d6; API package and transformed source
are linked through actual derivations, not package labels alone. Earlier
path-flake R1 eval3xq7 and actual clean-Git buildk2md have different metadata
contexts; actual built paths above are authoritative, no equivalence claim.

## Generated configuration and service proof

[Eight actual API/auth blocks](proxy-generated-config-proof.json) prove exactly
four HTTP+four TLS server/name/alias/listener sets, including both DDNS aliases,
301 `https://$host$request_uri` within location `/`, no unprotected duplicate
redirect, generated `^~` ACME challenge precedence, one query-free access log
and disabled sensitive error log per server, safe inherited ACME/maintenance
logging and retained503 maintenance. All relevant proxy locations have trusted
edge headers and all4upstreams point to the existing HAProxy Unix backend.
[ACME/HAProxy proof](proxy-acme-haproxy-proof.json) binds actual unit SANs/webroot,
existing Unix+*:5000 listeners and both9292backends, API frontend `no log`.

Normal actual nginx1.30.6 `-t` [PASS0/.102s](nginx-syntax/isolated-result.json)
in disposable user/network namespace, with existing PUBLIC nixpkgs test
certificates and log/pid runtime paths substituted only in a temporary config.
No production certificate/key created, host port bound or daemon started by
that successful isolated check. Original actual generated config was checked
separately and remains immutable/rooted. Original unprivileged host check
printed syntaxOK but failed bind80; its full result/log is retained. A guessed
system-path nginx executable was corrected using actual nginx.service ExecStart.
The unrelated `prasiatko.vpsfree.cz` duplicate-name warnings come from unchanged
baseline proxy definitions; eight scoped API/auth names are unique. Initial
inspection-order/packaging-path assumptions were diagnosed and corrected in
probe-only evidence, with no source repair or blind product rerun.

[API runtime proof](api-runtime-config-proof.json) covers both actual API units:
serviceowner/group, packagedconfig->/run->persistent API path,0750directories,
regular-file preservation, exact authoredhook, supervisor's separate owner/
state/config and no private docs files in authored store config. Actual clean
configuration metadata and package selections are bound.0600private files are
operator prerequisites, not files created or read by these checks.
[Followed composition](followed-composition-proof.json): WebUI config evaluation
PASS0/15.953s with builds/IFD disabled; its own pin unchanged and input follows
services33d6. Notification source is unchanged and consumed by actual API1 build.
No WebUI system build or new application/browser/SDK campaign occurred.

## Limits, recovery and effects

All graph/eval/build/syntax handles consumed; own worktree clean, no active
source/lock writer. Normal root query emitted native Nix housekeeping of3stale
indirect links whose targets were already absent; no explicit GC, store-data
cleanup, service or host-policy action was requested or run. Roots retained.
[Rollback predecessors](rollback-predecessor.json) retain exact configured
FCC/4a21/NAR/before-lock identities. Live production generations were not
queried and must be inventoried by the operator before a later approved rollout.
No claim of an already-prepared live rollback generation or production use.

Operator must register/check the dedicated client and provision the same stable
key/protectedJSON on both hosts BEFORE later authorized activation. Proxy-first
ordering, actual provider/CA/callback, sign-in/signout/revoke/expiry acceptance
and paired rollback remain in the reusable guide. No production request/access,
client/secret/provisioning/activation/dry-activate/default integration/lifecycle
or CI campaign occurred. No merged/default-ready or live-login claim.

Publication completed separately: see [publication receipt](../publication/receipt.md).
Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
