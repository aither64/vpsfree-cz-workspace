# Recovery delivery: exact pins and compatibility review

No unresolved Blocking, Important, or Advisory findings in the reviewed
downstream pin and operator-handoff scope.

The shared Important finding about runtime masks is resolved in the revised
rollout procedure: a mask under `/run/systemd/system` cannot override the NixOS
supervisor unit under `/etc/systemd/system`. The old preflight would stop safely,
but would not permit rollout. The replacement uses an explicit runtime drop-in
and marker, verifies the loaded effective condition, and proves that a start is
skipped on each API host. See the general lane's independent reproduction and
guard validation. This lane reviewed the concrete replacement procedure.

## Reviewed revisions and scope

Standalone GPT-6 Astra review at xhigh, following the user's explicit model
choice and the mandatory risk/compatibility lane. Overall risk is high because
the delivery adds persisted comparison state and prepares historical writes.
No nested agents or production operations were used.

- vpsadmin: `014fbc78422f3660b295add7a50f35cc7acdf0c8` through
  `42984def67d405c235e2a34d91820563858ddd89`, with two logical permanent
  commits. The completed implementation reviews and their direct fixes were
  inspected; this was not a blanket implementation rerun.
- vpsfree-cz-configuration: `3f213d5ebf922ab5522690ab28b3fdfa9b3bed1d`
  through `c8b7a4995b587b7e072b5f77be6006356fbb104d`.
- vpsfree-kb-contracts: `919577d0c770e47b623c591f8bf0cce4e8d30666`
  through `610cb7bf35953ea6c1a9110fc12102e0713fcfc5`.
- vpsfree-maintenance-tasks: `6eea682ede8d8e2634b2d41e5b11cf0f02231bc6`
  through final `2fdc9f2889ac419136cd0cde0e0955c015ae7107`. Its only tree
  difference from reviewed implementation `a80cc098` is the directly inspected
  README replacement of the runtime-mask instructions. Both maintenance hash
  occurrences in the rollout now select the final head.
- Read the applicable local AGENTS.md files, plan/state, review packet and
  reconciliation, commit series, migrations, service/package definitions,
  maintenance launcher/runner/repair, relevant regression coverage, consumer
  records and the revised `rollout.md`.
  All fourteen final rollout shell blocks independently passed `bash -n`;
  reviewed rollout SHA-256:
  `eec0ad942237a23c32d26e10ae8917e742b469cf5336b76ce6b6cce84eea4ef1`.

## Evidence and compatibility conclusions

- **Exact consumers:** a structural comparison of the committed lockfiles
  against their bases changes only C's `vpsadminServices` and K's `vpsadmin`
  nodes. Their complete locked vpsAdmin metadata is identical. K's five canonical
  revision files consistently select V42984def6; OS
  `6bdf458fd9105379860234ff33d352e55844f08f` and its existing nixpkgs locks are
  preserved. C's channel mapping and all eleven recorded buildPlan consumers
  select `vpsadminServices` at the exact final V head. The completed consumer
  build log lists all eleven machines at generation `2026-09-14--19-51-56`,
  which both prepared API deployment commands now select explicitly.
- **Two-writer rollout:** `rollout.md` installs the marker and unique drop-in
  on both API hosts, reloads systemd, stops the supervisors, verifies loaded
  paths/content and the effective non-trigger negated path condition, then
  requires `ActiveState=inactive` and `ConditionResult=no` after an explicit
  start probe. Those checks repeat around both activations. The procedure
  accounts for confctl's per-host SSH failures and the runtime files' loss on
  reboot. Cleanup is explicitly run as root on each API host, removes only the
  task's two files, reloads, restarts, and checks both service states. This
  prevents old and new supervisor writers from overlapping during migration.
- **Schema and rollback:** API1 supplies the new database package before the
  explicit migration; `autoSetup=false` is correctly accounted for. The
  migration command uses the database service's working directory and account,
  avoiding reliance on API DDL privileges. Both migrations are additive, with
  no default, backfill or historical rewrite. The unique checkpoint node key
  and cascading foreign key support older node deletion code. Application
  rollback retains both schema additions and evidence-supported repairs;
  older writers resume their known recording limitations. A newer retained
  event takes precedence over a stale private checkpoint after older writes.
  No node protocol, node package update or reboot is needed.
- **Separate repair:** the installed Ruby loader reaches the unconditional
  task executable; the task uses the new package's shared comparator. Default
  selection includes all eligible node/storage roles, including inactive hosts;
  repeated `--node` limits the selection and the documented default is 1,000.
  The preview/apply commands preserve that selection and batching. The operator
  procedure keeps all history writers paused, compares fresh previews, and
  explicitly states that apply does not consume a saved preview. Immutable
  proof, strict interval ordering, fixed candidates, locked revalidation,
  revision invalidation, skips and partial-apply reruns match the implementation.
  Checkpoints and mutable snapshots cannot justify a historical repair.

## Validation limits

- This lane independently inspected code, exact metadata, command semantics
  and recorded results; it did not rerun the completed database suites or launch
  long integration tests. General-lane guard testing used isolated fixtures,
  not a production API host or a full production activation.
- At review time the new local supervisor/WebUI integration runs and long
  final-head CI were still being monitored by the coordinator. Earlier green
  delivery results do not validate these final heads. The completed eleven
  consumer builds and focused/migration/schema/lint results do not replace
  those remaining runtime checks.
- The final README-only maintenance amendment changes no repair code, tests or
  C/K pin. Its exact committed diff and final rollout hash assertions were
  checked directly; no broad implementation review rerun was needed.
- Production rows were not inspected. Lost comparison reports cannot be
  reconstructed, and retained immutable evidence may be insufficient to tighten
  node1 or other historical intervals. No deployment, repair, merge or session
  lifecycle action is approved or performed by this review.
