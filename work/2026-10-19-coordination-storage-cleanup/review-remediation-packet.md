# Affected-lane review: interrupted integration removal

Reuse independent reviewer /root/retention_review, Astra/xhigh with its verified
native settings. Read the original review.md and review-packet.md; all prior
scope, trust and user-authorization boundaries still apply. Review directly,
read-only, without nested agents. Recheck risk/compatibility and general lanes
only; the original architecture/scope conclusions remain applicable.

One Important finding concerned partially removed integration scratch. The
remediation adopts the review's proposed admitted-intent boundary. Normal dirty
checkouts must still pass clean first admission. A saved payloadGcPending intent
resumes only its exact path/common-directory/HEAD and unchanged detached Git
registration; holds, process references, liveness and busy resources still
protect it. A changed branch/HEAD or absent registration preserves a surviving
path. Pending checkouts must not be reused, as now explicitly documented.

Git's native remove and targeted repair both refuse an existing directory whose
.git file has disappeared. The fallback therefore finishes that already-admitted
directory deletion through FileUtils.remove_entry, then uses Git to remove its
retained registration. This new deletion primitive warrants affected-lane review,
rather than merely asking you to confirm a requested narrow edit.

Final committed/published ranges (same bases as the original packet):

- Runtime base 8385699aabcc2cfc74b585ca653a4658ff3eef75;
  cleanup 6ff8560785a33c83310bacba9f50919a855b66cf;
  profile/final 926c669f148e05b881bc41bd432389d14998e411.
  Compare original reviewed head 957dc29 against final for the remediation.
  The requested fix is folded into its owning cleanup commit; no fixup remains.
- Workspace base 92a9a8d3c88e91b81d7a752fc29d1b807ed9d02f;
  final 1fb8372c939777f5541a00de6ce0804ab6d41e3f, one final runtime pin.
- Configuration base 95a8b88d383c177fc65bf67d51c901a69c0b2847;
  final 67616867156d4c541e13b67dddb26c885a0dc4a3, one final confctl-generated pin.
  Regenerated directly from base to preserve the final generated changelog.

Both locks change exactly one intended runtime node. No migrations, changed
public interface or repeated dependency-update streams. No activation or master
integration. Focused suite passes: 33 tests, 169 assertions. Tests exercise
partial deletion with/without .git, branch/HEAD changes, explicit pending holds,
and replacement operator data after registration removal. Existing dirty/foreign
first-admission tests remain. Long packaged verification has not started.

Save the affected-lane findings/conclusions as review-remediation.md. Preserve
the original review report and exact original ranges.
