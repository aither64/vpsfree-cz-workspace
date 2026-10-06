# Deployment pin branch inventory

Workspace final base 09da5e10eff9d0ead7d5647691256944049524f4, final 88a75655ce6f4151f932df1d5204845edd8ea968.
Original reviewed/deployed selector commit 88c0b957 on base e5ba1912 was cleanly
rebased after a coordination-only checkpoint; range-diff is identical and the
package output remains the exact deployed candidate.
One dependency-only commit; flake input selector and two generated lock nodes.
Extension cd81e83 stays unchanged; all remaining inputs unchanged.
Existing shared-master coordination commits b234ec3e/e5ba1912 are preserved.

Configuration base9c5fafb9df6bb33d635e7eb8f1f2638dfb1cbfe4, finale179a58ee3f7ceb4cf0b253d368c8ad94967b2d5.
One confctl-generated pin commit; only runtime and expected transitive provider.
No handwritten configuration behavior changes, superseded approaches, obsolete
compatibility paths or migrations. The configuration pin has been deployed and
its host health checks passed. User-profile selection also passed after natural completion of the busy thread.
All four affected defaults are integrated; master CI verification passed.

Mandatory-change-review mechanical dependency-only exemption applies to these
two pin commits. Existing substantive runtime/provider final review remains valid
at unchanged exact heads. Architect0 independently inspected rollout contracts;
see deployment-design.md. No added review or application code is being skipped.
