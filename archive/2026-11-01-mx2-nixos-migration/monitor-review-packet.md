# Targeted final review: mx2 exporter metadata contract

Completed committed narrow production-metadata fix; quick checks pass. Before
long affected-system build, independently review affected general,
architecture/repetition and risk/compatibility lanes under mandatory-change-review
step10. Scope/proportionality conclusion from prior full review retained: no new
mechanism/scope expansion, exactly one existing-interface declaration. Review
coherent full current history/migration disposition; do not repeat unrelated
mail-test review or earlier narrow test-fix review without a changed concern.

## Source and exact ranges

Worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration.
Fresh base c040c14cdbacc07998700b524996a89306188d7f.
Prior mail-suite/runtime-passed head8d4e03d53699d80f46030b0ee6eb213151b8ae30,
retained ref2026-11-01-mx2-nixos-migration-verified-runtime.
New head1e3afc478fb72b54a25a0147910463f060fee88f,
tree77d73449040aba400215ca81843c3d6a2173593c.
Complete current series:

1. 9c6e36135192f65baed975e3b127160f068e0b0d — final host/shared mail policy.
2. a5848319ae19d1bcd348ab3837683dec71c90e01 — internal DNS source alignment.
3. 1e3afc478fb72b54a25a0147910463f060fee88f — tests/docs.

Full old8d-to-new source delta only:
cluster/cz.vpsfree/containers/mx2/module.nix adds services.node-exporter = { }.
Lead directly inspected full diff and clean status. Host fix folded into owning
host commit; DNS/test stable patch IDs preserved, final tree equals pre-fold
metadata-fix tree. No migrations/input/generated update streams; original40411,
reviewede4 and successful8d refs kept. Historical feature deployment unknown,
none deployed by this task, no old nonancestor literally merged/deployed claim.

## Trigger and evidence

Batch6 verification-run-6.md: full three-VM mail matrix PASS227.03s, actualmx2 and
both DNSns1 builds pass. mon1 evaluates Prometheus targets and fails missing
metaConfig.services.node-exporter.port at modules/clusterconf/monitor/default.nix157.
mon2 was unrun due stop-first-failure. No remaining command/VM or production effect.

Owner applied exact consumer selection to baseline c040: no missing metadata;
prior8d: only newmx2 missing. Shared monitor/system-monitor/service definitions
unchanged. Both mon1/mon2 use default all-machine selection. Actual built8d
mx2 contains enabled prometheus-node-exporter.service/WantedBymulti-user.target,
ExecStart listen0.0.0.0:9100. Existing neighbors declare node-exporter={}; schema
owns defaultport9100. New declaration therefore restores producer contract,
not a new exporter, firewall rule, registry or generic consumer fallback.

Quick checks: normal hooks/format/Nixparse/whitespace; complete newhead mon1/mon2
(and all5affected systems) toplevel derivation evaluation PASS; missing metadata
selection nowempty, mx2 exporter metadataaddress37.205.11.114/port9100; consumer targetmx2.vpsfree.cz:9100. Raw exact evaluations and supported
union inventory in monitor-metadata-evaluation.json, durable owner receipt coming.
No long builds yet for successor; no source changes intended after commit.

## Verification reuse and remaining commands

New VM check is EXACT previously successful drv
/nix/store/8pan3ddqairw3js87iaysvjqwzalxgls-vm-test-run-mx2.drv,
output /nix/store/jgq1lk68xjj40j2h4wnw403pc3nylni4-vm-test-run-mx2.
Root verified successful output+NAR hash immediately postrun; it is now absent/null (unknown removalcause), so only historicalrealization/currentexactderivation reuse is claimed. Complete lock/input graph unchanged;
test/sharedmail/fixture files unchanged. Thus reuse is bound to exact derivation/
input identity, not tree equality. Source metadata successor does require all5
new system builds. Literal native pattern has inventory exactly these5:

cz.vpsfree/containers/{mx2,brq/int.ns1,prg/int.ns1,prg/int.mon1,prg/int.mon2}

Native File.fnmatch? with FNM_EXTGLOB supports it; no wrapper/tool change. One
confctl --yes build after review can batch groups in one environment. Parent
monitoring fallback remains justified after fresh utility readiness failure.

## Context, limits and requested result

Read current design/plan/state, prior verification-review.md and implementation/
remediation/runtime receipts as relevant, plus exact local producer/consumer/
service definitions. Previous full review all4lanes atf378 and direct step9 test
fixes remain recorded; metadata behavior needs this independent review. User
wants autonomous verification and explicitly approved internal mail DNS source
fix; no production deployment/default integration/primary changes authorized.
No new TLS/recipient infrastructure/CI/dependency campaign. Existing real-host,
TLS/recipient/backscatter/container/cutover limits remain.

Retained reviewer0, savedgpt-6.1-sol/xhigh/read_only, same-session independence
verified. Keep settings, no nested reviewers. Report findings/severities and
specific metadata correctness/consumer/risk plus final full-history/no-migrations/
no-repeated-stream conclusions. Read-only means send report to lead for
monitor-review.md recording; no source/files/Git/builds/production access.
