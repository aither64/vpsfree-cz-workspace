# Recovery review: general

## Findings

### Blocking G1: the integration recovery report is rejected before recovery runs

Commit `268f7d09b9e3ca59d2b8f286e6666f72f9f7a9ff`,
`vpsadmin/tests/suite/supervisor/runtime-ingestion.nix:261` sets the recovered
current vpsAdmin software revision to `synthetic-recovery` and its source to
`native`. `api/lib/vpsadmin/api/kernel_evidence/payload_parser.rb:184` requires
every non-null software revision to match a full 40-character lowercase Git
SHA. The parser therefore rejects this entire report.

The helper at lines 195–214 waits only for the current-status observation time
to advance, which also happens for rejected evidence. It will return, but the
five expected recovery events at lines 279–282 will not exist and the private
checkpoint will remain. The new long integration scenario deterministically
fails instead of exercising valid recovery.

Replace that value with a valid synthetic SHA. Validate the exact constructed
recovery payload through `PayloadParser` before starting the integration run;
the unit-test fixtures use different construction and do not catch this value.
This is a narrow fixture correction that can be checked directly.

Focused confirmation in the repository API Nix shell invoked the existing
`PayloadParser#validate_software_identity!` with the fixture's identity fields.
It returned:

```text
rejected: software_versions.revision must be a full Git commit hash
```

No additional Blocking or Important findings.

## Reviewed scope and commit series

- Reviewer: general lane, `gpt-6-astra`, `xhigh`, as explicitly selected by the
  user. Review performed directly without subagents.
- Read the mandatory-review skill and general lane reference, both repository
  `AGENTS.md` files, review packet, accepted plan follow-up, current state and
  prepared rollout.
- vpsAdmin: `014fbc78422f3660b295add7a50f35cc7acdf0c8` through
  `268f7d09b9e3ca59d2b8f286e6666f72f9f7a9ff`.
  `cccf59c060be4c85a7a0809203e6fe24447e16a4` owns stable confirmations and
  their nullable schema field; `268f7d09` owns checkpoint recovery and the
  related application fallback correction. Their supporting tests, additive
  migrations and CI selection edits belong with their respective behavior.
- Maintenance tasks: `6eea682ede8d8e2634b2d41e5b11cf0f02231bc6` through
  `c77ff3742f623afd23c0be26c0f6ddbc026f1ba4`. The single dated task contains
  the command, local repair helper, operator README and focused disposable
  database tests. The superseded application Rake repair is absent from the
  reviewed vpsAdmin series. Commit messages satisfy repository scope rules.

Inspected recorder/comparator, parser, snapshot reader/writer, checkpoint model
and associations, schema migrations, public revision implementation, supervisor
transaction and stale-report handling, maintenance selection/proposal/write
paths, and the changed regression and integration tests. The reviewed design
keeps internal confirmations separate from public revisions, preserves invalid
current evidence, and revalidates repair proposals under the node lock using
immutable snapshot proof. No mismatch with the accepted implementation scope
was found beyond G1.

## Validation limits and remaining checks

- This review ran the focused parser rejection check and `git diff --check`;
  it inspected, but did not independently rerun, the reported database-backed
  suites or long integration scenario. The vpsAdmin tracked tree was clean
  when checked.
- The new integration run must pass after G1 is corrected. The reviewer did
  not execute production operations or alter implementation/state files.
- The review packet explicitly defers downstream exact pins and builds.
  `rollout.md` still contains the previous configuration/vpsAdmin preflight
  revisions and build generation; replace them with the final reviewed pins
  and results before delivering executable rollout instructions. This is
  outstanding delivery work already identified in the packet.
- Historical evidence retention can leave intervals unchanged, and already
  discarded observations cannot be reconstructed. The maintenance README
  correctly documents these limits, per-event commits, concurrency skips and
  the need to keep writers paused when approval must cover identical previews.
