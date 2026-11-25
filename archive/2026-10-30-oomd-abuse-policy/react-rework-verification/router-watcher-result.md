**Result: passed.** The single runner invocation exited `0` after 34 seconds. Both checks passed: overview filters (2 tests) and older API on mobile (1 test).

Tested head: `55a813b44edb915c7ed5ce68366d6d797a551606`; tested staged tree remained `4bee7d1455f35cd422fc385fafda18486f6ee3ea`, with no unstaged changes afterward.

Logs and receipt are in `react-rework-verification/`: [filter log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/react-rework-verification/browser-router-filter.log), [mobile old API log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/react-rework-verification/browser-router-old-api-mobile.log), [completion receipt](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/react-rework-verification/browser-router-followup-result.json).

No failure excerpt. The receipt reports port 5197 refused a connection after completion (`connect_ex=111`); no listener cleanup was needed.