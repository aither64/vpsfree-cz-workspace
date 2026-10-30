**Result: failed, incomplete.** The frozen guard refused admission. Its latched first failure was `scope.inspect / present-invocation`: the named scope query returned an empty `InvocationID`, so the expected identity was unavailable. No build or CLI checks ran.

- Helper native exit: **1**; elapsed: **1.382311 s**.
- Admission: **no**; samples: **2**.
- Host memory recorded: initially 101,227,433,984 bytes total / 59,535,081,472 available; last 101,227,433,984 / 59,344,162,816.
- Reconciliation found the watch directory present; build path, expected output, and output root absent. The named scope was `not-found` on the bounded follow-up query; both known process births were absent at reconciliation. Protected daemon effects were not inspected, so this does not establish that all protected activity ended.

Retained evidence:

- [Operation log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/recorder-fixed-build-3-utility-operation.log)
- [Effects reconciliation](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/recorder-fixed-build-3-effects-reconciliation.json)