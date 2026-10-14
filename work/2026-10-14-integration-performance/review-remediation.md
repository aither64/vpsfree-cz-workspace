# Integration performance review remediation

The original independent final review is retained below. All Blocking and
Important findings are addressed in the reconstructed final branches.

- Bind expected reviewed/certified heads before checks; verify snapshots and
  deployment coverage, refusing concurrent edits. Focused regression passes.
- Deploy-first retains deployed receipts and prepares/approves fresh merge
  snapshots in the successor generation. Resume with stable command after switch.
- Approval and pending-refresh steps recover exact IDs and receipts after lost
  replies. Refresh intent remains durable even after job state changes.
- Ruby filtered source includes its two documentation contracts; scheduler
  escape matches dispatch_notifications. Both focused regressions pass.
- Runtime series reconstructed with integration hunks in their owning commit,
  cache packaging in cache commit. Intermediate load/filter checks pass. Original
  refs retained, no deployments/releases or migrations.
- Initial journal publication and completion outputs use admission plus exact
  tracking binding. Run-specific records prevent stale results across runs.
- A committed pin recipe resumes through its read-only verifier, preserving
  original parameters and candidate identity. Focused lost-reply test passes.
- Metadata verification remains synchronous in scheduler; residual performance
  limitation documented. No broader owner-verification redesign in this scope.
- Configuration pin regenerated from actual upstream predecessor with confctl;
  generated message/hook results preserved. No redundant pin streams remain.

Upstream sensitive-session feature landed during implementation. Rebase preserves
it; sensitive completion registers local artifacts but commits no tracking.
Focused sensitive-completion and existing sensitive owner tests pass.

Final inventory: review-inventory.json. Quick integration suite: 16 tests,
67 assertions; admission 4/13; certificates 4/8; extension recipe 3/8; affected
host regressions 2/16. Composition passed at 1ad548d4. No long tests/rollout yet.

Artifact registration now uses tracking-relative paths, as required by the
production API; the sensitive-completion regression asserts those exact paths.

Please review affected general/history, architecture and risk lanes: new durable
refresh intent, successor-generation preparation, lifecycle-protected outputs,
recipe recovery, run-specific artifact paths and upstream sensitivity adoption.
No unrelated full-scope rereview needed. Require final complete series/migration
conclusion and assess consumer pins. Original full branch review covered all lanes.

Further narrow remediations: validate a pending refresh snapshot before storing
it and again before approval on every resume; repeated rejection regression
passes (3 targeted tests/21 assertions). CI fixture package-layout failure was
missing newly required integration/admission libraries in the synthetic package;
fixture library inventory corrected with focused archive-load regression.

Final lifecycle remediation adds optional artifact add --expected-owner UUID.
The manifest writer validates retained owner workspace/slug/fence and exact
tracking identity under its existing creation/session locks before mutation.
The driver passes its original owner. Focused API tests cover unchanged manifest
bytes in a recreated inode, unknown owner rejection and CLI forwarding. This
small cross-command contract needs only affected architecture/risk assessment.
