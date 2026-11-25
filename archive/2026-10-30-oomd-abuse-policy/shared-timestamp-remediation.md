# R1: confirmed timestamps at API serialization

Original reviewed range: ac10a62f1cb0fc890378ae83cdf18dd0e29f049a..
e9a6530b0e18f2f58b013b3a470f3d6991d79876. Preserved unchanged at
refs/review/2026-10-30-oomd-abuse-policy/vpsadmin-shared-final-review.

The rework omitted the previous summary-aware timestamp accessors. The batched
summary could compute confirmed Stop/Chown times while actual Index/Show
serialization read nil/old persisted columns. The two new actual-route cases
failed on the reviewed runtime: missing stop timestamp, and stored old ownership
epoch instead of confirmed Chown time. Native negative result: 2 examples,
2 failures, exit 1, 16.960 seconds, seed 53700.

The fix restores the two loaded-summary/raw-fallback getters on Vps. The summary
calculator and evaluator explicitly read persisted last-stop/accounting attributes,
so an existing display cache cannot change reconciliation or decision persistence.
No schema, API field, source qualification, mail or transaction behavior is added.
The project contract already describes the intended confirmed timestamps; no
additional feature documentation is needed.

Exact source paths:

- api/models/vps.rb
- api/models/vps_incident_summary.rb
- api/models/incident_escalation.rb
- api/spec/api/resources/incident_escalation_spec.rb

Positive command:

```sh
VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec \
  spec/api/resources/incident_escalation_spec.rb \
  spec/models/vps_incident_summary_spec.rb \
  --example 'confirmed timestamps before scheduler persistence' \
  --example 'VpsIncidentSummary' \
  --format documentation --format json --out <explicit evidence path>
```

Positive native result: 9 examples, 0 failures/pending, exit 0, 28.254 seconds.
The two API cases exercise both Index and Show, check unchanged stored columns
before reconciliation, compare summary-backed model getters, then verify raw
persistence. Chown retains the previous physical-stop cooldown; a cached virtual
epoch does not alter evaluator counts before explicit reconciliation. The seven
existing summary query/parity/transfer-state cases also pass. Scoped lint reports
4 files/no offenses, and diff whitespace passes.

Evidence: shared-timestamp-{negative,positive}.{log,json,exit},
shared-timestamp-lint.log and shared-timestamp-hooks.log. Lead accepted direct
inspection under mandatory review step 9; the original independent review
continues on its preserved e9 range. The normal hook-backed fix is retained
separately until the lead releases consolidation. No broad rerun, publication,
image/guest/browser build or lifecycle action accompanies this correction.

Terminal receipt: the normal commit command exited 0. All pre-commit hooks
passed; commit-msg hooks passed with nonfatal 72-column text-width warnings.
Retained fix commit: 3cde6709ba57ea7e5809bcccbf10938494d2bc31.
Tree: f6656bd2c1d49f308c6cc1697ad3fb1c44d2be5c.
The exact original-review-to-fix patch is saved as shared-timestamp-fix.diff.
Only the pre-existing excluded PHPUnit cache is untracked. All owned local
command handles were collected/exited; no local runner, builder, guest or
isolated database operation remains active. No tests were repeated after the
accepted focused positive. Source is held until the original review report is
released by the lead; no consolidation or publication has occurred.
