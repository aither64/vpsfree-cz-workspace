# U9: measured VM fixture probe budget

Owner implementer0, retained Sol/xhigh/workspace_write. Capacity accepted after
U8/R6; exact identity/environment and live roster verified. Bounded direct lead
brief. Final commit `9fb102e285a2847427ffc1d25919183298630f3b`, parent
`d6d972ade865849cee7324060f611aec649ad31e`. Exclusive commit window released;
worktree/index clean.

## Cause and bounded change

C11 completed its focused services timing probe (exit 0, 247.05s, session52174
joined; lead owns teardown proof). It is diagnostic evidence, not a full-suite
pass. Healthy steady WebUI HEAD requests exceeded the fixture's two-second
budget: two capped attempts returned curl28 at 2.002s; ten-second capped attempts
returned HTTP200 at 8.690s cold / 3.986s / 4.322s. HAProxy showed per-request
2MB API OPTIONS metadata plus PHP/API work. Actual Node.PublicStatus GET later
returned status:true in about 0.04–0.05s; console was about 0.009–0.09s.
Early Layer4/503 and WebUI JSON parse failures were startup observations;
aborted-request load remains unproven and is not the claimed root cause.

Change only the test status VM's `check_timeout` from 2 to 15 seconds, plus one
source rationale comment and six README lines. Two files, eight additions /
one deletion. Polling setting remains two seconds. Existing per-service/API
loops are independent; an in-flight 15s probe plus interval and next bounded
probe fits within the unchanged 90/120s detection/recovery windows. HTTP REJECT
normally fails faster. No assertion or deadline was weakened.

Production configuration/default60, application/backend, Go/dependencies/input
graph, all seven example bodies and U8 first-failure collector remain unchanged.
The two-second fixture budget predates this feature; this is a distinct logical
test-fixture correction, not another OS pin or an obsolete dependency fixup.

## Checks

- Nix parse and diff checks passed.
- No-build evaluation of the actual fixture module function verified timeout15
  and interval2. No local/remote builders or substitution were allowed.
- Generated Ruby SHA256
  `7bf635aa409aa771eb4aa9cf6adb2c438e71743f5eae5b98cbc49b41a826d59d`
  matches reviewed U8 byte-for-byte; actual test metadata matches U8 exactly
  (three VMs, 14 CPUs, 17,920MiB memory/shared memory, one script).
- Mechanical reversal of only the timeout/comment reproduces the complete
  original suite file, verifying all examples, assertions, ordering, setup,
  cleanup, networking, resources and diagnostic collector are preserved.
- Lead directly applied the writing skill to actual README prose and accepted it
  unchanged. No new UI strings or app prose.
- Required Nix/Lefthook2.1.5 i18n hook passed 0.38s (0.39s total), gofmt skipped
  without Go files. Commit used the required temporary message file; no bypass.
- All 99 compiled/logical source inputs match after hooks, receipt
  `u9-source-inputs.json`, digest
  `4660e527245cf70bfea47bb6cae3340874f6b7486e24fb3b4e6641db2a8e4d1f`,
  bound to final head. No unexpected hook effects; worktree/index clean.

No new generic tests, guest/process mutations, source builds, full test replay,
CI actions, push, rebase, services or integration by U9. Old C10/C11 diagnostic
source/run receipts remain separate from this new fixture head. No migrations,
schema/state conversion or production deployment. Earlier reviewed UI/preview,
CI visibility, OS baseline and failure-capture commits remain intact; independent
review assesses complete final history before readiness. Next dependency is
R7 committed final review, then lead-owned exact-head full consumer validation.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-status-theme-responsive-preview/)
