# DEV-R1 narrow review remediation

Frozen independent review: retained reviewer0, Sol/xhigh/read_only, all four
lanes and complete08c3..c413 history. One Important DEV-R1, no other findings;
history stream split and no migrations accepted by lead. Read design.md:3203
and mandatory review steps9–10. This correction removes the rejected Varnish
transport within the reviewed proxy boundary; lead directly inspects it after
focused checks. No full review or unaffected test rerun is requested.

Starting consumer head: `c413b07cf8120eb6159b4249b150a6aff99ecaed`, tree
`61ea05a80724ac0f714b06e011ea15515f56041e`. Preserved review ref:
`2026-10-24-vpsadmin-haveapi-upgrade-devdocs-reviewed-c413`.
Package commit `3a92d6458cf76c9338afd6106c48b069575e196d` and published8102
remain unchanged. Immutable HaveAPId67 is unchanged; no M7 adoption.

Exactly two paths: test/development services API frontend uses its existing
HAProxy socket directly, matching auth; comment explains VSL retention even
for pass-through. The existing owning docs paragraph records the whole-route
boundary, metrics60-second-cache loss and rollback constraint. Shared Varnish,
nginx/HAProxy modules, service enablement, auth/PHP/React inputs and private
configuration/locks are unchanged. Do not restore Varnish transport while
documentation OAuth remains enabled.

One bounded actual NixOS services-module evaluation compares oldc413 and the
candidate using the same pinned inputs. It selects generated nginx upstreams
and locations plus full HAProxy config; assertion logic does not reproduce the
module renderers. Required: api_test upstream contains only HAProxy; API /
selects api_test; API/auth paths omit Varnish; safe logging/authoritative headers
remain; HAProxy API no-log/backend and complete config unchanged; auth/PHP/
console route equality. This consumer configuration declares no React route in
either snapshot; native provider React override equality remains E3's later
actual-config/closure gate, not a local-runtime claim.

Normal owning-consumer commit amendment/hooks follows this focused check.
No passed core/full/sample/archive/installer tests repeated. No API build,
services-up, publication, canonical rebinding or runtime activation permitted
until lead accepts this milestone. Packaged lock Bundler4.0.23 versus actual
smoke installer2.7.2 remains an honest postreview real-package gate.

## Completed narrow correction

New head: `cba626581a698256e873319983ac51312f40398c`; tree `40375b83d5077e0fe16c0c47b8307ff467a82b4f`.
Only the two authorized paths differ from reviewedc413; all other tracked
entries equal. Package3a92 and published8102 remain unchanged. Source clean,
full ignored/packaged lock remains4ded33e2. Actual imported services/frontend/
HAProxy/QEMU configuration evaluation passed, then normal amend/hooks passed
(wrapper0/~98s). Hook message line-width warning was advisory; no bypass.

[Generated config](../dev-r1-eval/generated-routes.json),
[assertion result](../dev-r1-eval/result.json),
[exact narrow diff](../dev-r1-eval/narrow.diff),
[range comparison](../dev-r1-eval/range-diff.txt),
[final source/lock/effects proof](../dev-r1-eval/final-proof.json).
The initial evaluator omitted the existing QEMU option module and stopped before
assertions/commit; original logs retained. The corrected evaluator imports that
ordinary pinned module, rather than mocking missing VM options. No VM started.
No owned process remains; watcher/slot released. All prior successful checks
retained; no suite/sample/archive/installer rerun. Lead direct inspection of
this requested narrowing is next, before API build/services/publication/runtime.
