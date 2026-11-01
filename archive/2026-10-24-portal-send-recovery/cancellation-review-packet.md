# Added cancellation evidence review

Retain your existing identity and gpt-6.1-sol/xhigh settings. Read mandatory
review and affected general/architecture/risk lane references. Do not edit source
or run long tests. Prior F1-F3 narrow corrections remain unchanged from final
57dd01b and were verified directly under step 9. Long source/native/browser
checks passed; do not repeat their unaffected review.

New provider head 872c7ad (read exact full HEAD from source), base 11ec57d.
Incremental change from 57dd01b only: public requestWithAdmission retains a
concurrently completed caller cancellation alongside an existing request error
with two wrapped causes. Successful requests remain successful; errors.As/Is
for transport/RPC cause remain intact. This must not invent non-delivery.
One deterministic test induces transport failure plus cancellation at admission,
with noncancelled control, and verifies both causes. Documentation states the
contract. Source remains one consolidated functional commit; no migrations.

Reason: runtime CI 40131027714 failed attempts 1 and 2 in existing
TestRetireThreadPersistedEmptyRootRefusesUnsafeEvidence/cancel. Expected
context.Canceled; received disconnection from request response select. Both
fixture and select are unchanged. Local focused 100 repetitions on old and
new passed; baseline 1000 single-scheduler repetitions passed. Full CI
reproduces the ordering race. Rather than accepting another rerun, preserve
both truthful error causes at the public request wrapper. Changes are committed,
quick send/shared-ledger/history/cancellation checks pass. No deployment yet.
No protocol, ledger schema, successful receipt or cancellation-lifetime change.

Assess this added error-chain boundary and deterministic coverage, including
that it does not weaken delivery classification. Check final history conclusion
for the provider; runtime/config/workspace only receive matching mechanical pins
once accepted. Write cancellation-review-report.md in this initiative directory.
