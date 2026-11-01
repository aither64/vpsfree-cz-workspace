# Nginx format ordering: committed affected-review packet

Lead-authorized bounded correction complete; STOPPED before services retry or publication.

- Full range `08c3bd7e3cb4dc324a0381df6a1eec190daab1a7..3ae74281e0eed42edd351ffbe9c6fdb51fbf6834`, four commits,39 final paths.
- Old reviewed head `94ccabc5471a1b8f0ecbca66f3fe0eec4749a338`, tree `65381306e6c32a55f8238ee3a8ec05a7316b1c2b`, preserved by
  `2026-10-24-vpsadmin-haveapi-upgrade-devdocs-reviewed-94cc`.
- New head `3ae74281e0eed42edd351ffbe9c6fdb51fbf6834`, tree `3c047743c524d5764dec7793c29ffffbcb224137`.
- Package `a15e0882f87e557ac3f66c0efc2893ae98a2ec3d` and published/deployed8102179 remain unchanged.
- Exactly one changed path from94cc: tests/configs/nixos/vpsadmin-services.nix.
  Every other tracked entry is equal. **No migrations or schema changes.**

[Final proof](final-proof.json), [one-file diff](old-new.diff),
[complete series](complete-series.txt), [complete final diff](complete-feature.diff),
[range comparison](range-diff.txt), [quick result](result.json),
[normal hooks/amend log](finish-corrected.log).

## Defect and correction

The actual reviewed94cc services VM booted degraded because nginx could not
resolve vpsadmin_api_no_query when parsing API/auth server access_log directives.
The exact selected nginx1.30.4 binary/config reproduced unknown-log-format exit1
at generated line86. The declaration was emitted later by appendHttpConfig.
The source now selects commonHttpConfig for the same exact format, plus one
ordering comment. Safe logs, authoritative headers, direct API/auth HAProxy route,
PHP/console routes, immutable d67 source and all dependency/package policy remain.
No interface/prose change needs new project documentation; the nearby comment
records the parser ordering requirement.

## Focused actual-config proof

The normal declared services derivation graph supplies the actual old/new nginx
configuration. Raw derivation text and the old formatted native file contain
identical tokens. After removing the one relocated format line, old/new config
tokens match; the declaration precedes both API/auth uses. Whole HAProxy text
derivations match. Actual selected nginx syntax validation in a disposable
fixture returns0 with both syntax-is-ok and test-is-successful. Only writable
PID/log destinations and unprivileged loopback listener change in the fixture;
no missing TLS/include failure was ignored. Application listeners are unchanged.

[Native syntax log](nginx-syntax.log), [generated configs](generated-routes.json),
[fresh exact test graph](quick-test-recursive-derivations.json),
[original negative](../postreview-corrected-remainder/nginx-diagnosis.json).
Nix format/whitespace and normal pre-commit/commit-message hooks passed, including
RuboCop; the consumer commit was amended normally. Advisory message-width warning
only. No API build/probe, core/full, sample, compiler, SDK or native services rerun.

Temporary evaluator failures remain separate: missing VM option, unrealized
regex-extracted path, then raw-versus-formatted whitespace assertion. The final
check uses the exact declared services graph. The first syntax fixture's
privileged-port bind failure was retained and corrected, not counted as pass.
A wrong-CWD commit shell correctly refused missing Overcommit; ordinary repo
shell/hooks then passed without bypass. Postcommit receipt initially expected an
unchanged API drv and stopped; the exact input delta below is the corrected proof.
No application check assertion was weakened.

## Exact package evidence reuse boundary

The actual94cc API/buildEnv/five-new-gem outputs/12docs/Fiddle/frozen Bundler
proof remains [recorded](../postreview-corrected-remainder/api-package-milestone.json).
All five d67 gem outputs, Ruby environment/wrapper, frozen4ded lock and1,650 other
old API recursive dependency derivations are EXACT unchanged. The filtered
source inputs are byte/mode/link identical across3,510 paths, manifest
`ee2c323e2684cb7d355899f364663b775ec2aa7bb5a9199c3a50c0b0851214c1`.

The actual new API derivation/output are `/nix/store/b0prrr07pwzdbcldihlligmqazry74jb-vpsadmin-api-unknown.drv` /
`/nix/store/dm232ywpnjqrsq7fw2i0rdczg12xm10c-vpsadmin-api-unknown` and are **not yet realized/tested**. Only source-copy/API
identities changed because filterSource includes the unfiltered source basename;
API env differs only by source/output, and source version/install phase match.
Do not relabel the old API artifact as the new one. After affected review, normal
services preparation can realize the new source-copy/API while reusing exact
unchanged gems/runtime proof; no successful gem/probe campaign is required.
[Reuse detail](package-reuse-proof.json), [input graph](quick-test-recursive-derivations.json).

Fresh source `/nix/store/ikq5ydkhk4g436jhzxjbra9xqdkvpvdx-source`; prepared new test drv `/nix/store/ln0wf2vjddi5sri6pc41dim9qz2yqn76-os-test-vpsadmin-services-up.json.drv`,
config `/nix/store/4plp7f1528cpi2znj2mr0dpzyv3hi0fh-os-test-vpsadmin-services-up.json`. Native test script is unchanged. Ignored/packaged
API locks remain SHA2564ded33e27ae206ce6f7ea9352a591f4a373634c767c0d58bc1865717bfa1c0a6.

## Native failure and effects preserved

The original services test's readiness failed after900.08s; five other service
checks passed. Lead then specifically authorized interruption of the exact owned
native evaluator to avoid repeated waits on the same confirmed nginx failure.
The nginx example was interrupted; later examples were unperformed, not failed.
Native parent/wrapper exit1 and original logs/results remain, along with
[cancellation](../postreview-corrected-remainder/cancellation.json) and
[reconciliation](../postreview-corrected-remainder/reconciliation.json).
Runner/evaluator/owned VM/virtiofs are gone. No registered cluster or unrelated
session was modified. Native roots /tmp/hdrr.6fo4oifq/roots, original94cc build
roots /tmp/hdcr.xgjad6n2/roots and oldcba failed roots /tmp/hddc.2945ivos/roots remain.

Current source is clean, no writer or active operation remains. Utility slot
free. New quick root `/tmp/hdnf.yH3ntP/roots` retained. All old review/failure refs,
8102/React0312 rollback/config and prior evidence remain. Lead assigns affected
reviewer0 before any services retry/publication. No live source binding,
activation, client/private/provider/KB/default integration or lifecycle action.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
