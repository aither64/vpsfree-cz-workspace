# Effective persistence acceptance

Final test/guest source: d3bf74bc92ea0ced100df12ba10e1dadd7fd1ec5.
The explicitly pinned test host is the exact original edb host (hd5…toplevel,3j3…squashfs).
Public module composition, full non-script JSON equality and all12current script
equality are proved in persistence-declared-payload-diagnosis/host-inputs-original-source/.
The old-to-current script comparison permits only the accepted declared setup
and stdout-source/adjacent-blank provenance; all generation/registration paths match.

The original12case run is terminal1:11PASS and1old-fixture payload metadata failure.
Its complete logs/config/disk remain preserved. Successful rows below are reused
by exact execution-input proof, not rerun or relabeled as a wholly green batch.

| Scenario | Evidence | Script seconds |
| --- | --- | --- |
| ancestor-var-26.05 | PASS, original edb run; exact-input reuse | 429.68 |
| ancestor-var-lib-26.05 | PASS, original edb run; exact-input reuse | 413.4 |
| declared-backing-26.05 | PASS, new corrected d3bf run | 831.04 |
| dependent-mount-26.05 | PASS, original edb run; exact-input reuse | 443.41 |
| direct-filesystem-bind-26.05 | PASS, original edb run; exact-input reuse | 410.19 |
| fresh-26.05 | PASS, original edb run; exact-input reuse | 379.84 |
| fresh-ancestor-26.05 | PASS, original edb run; exact-input reuse | 726.47 |
| root-backed-26.05 | PASS, original edb run; exact-input reuse | 432.86 |
| storage-failures-26.05 | PASS, original edb run; exact-input reuse | 1198.88 |
| upgrade-25.11 | PASS, original edb run; exact-input reuse | 535.73 |
| upgrade-26.05 | PASS, original edb run; exact-input reuse | 443.4 |
| upgrade-unstable | PASS, original edb run; exact-input reuse | 514.3 |

The corrected declared run runtime-declared.vv3bb97_ PASSED0 in a new disposable
old guest. Example563.78s/script831.04s; all old baseline/challenge/candidate/
repeat/restart and preservation assertions passed. Original setup guards executed0
before first payload. Actual native host/runner/executable inputs match; only the
printed source provenance differs, and all24changed files in that immutable
source match committed bytes. Full logs/hashes and receipt are in that attempt.

All12planned scenarios are now covered:11prior passes retained after the exact
input comparison, plus one new corrected declared pass. The original failed
attempt remains terminal1 and its guest/disk/logs remain untouched.

Independent Astra/xhigh whole-approach/four-lane/history review is complete.
Its Important fresh SGID/group finding is fixed and verified directly, including
the actual fresh-ancestor runtime. Quick source checks and hooks pass.
New-head CI has passed normal persistence, compatibility/templates, disk reuse,
host build/cache, RSpec and all6images. Broad native/livepatch remains pending.

No migration or coordinated host update. No merge, production deployment, KB
publication or lifecycle closure is represented by this record.
