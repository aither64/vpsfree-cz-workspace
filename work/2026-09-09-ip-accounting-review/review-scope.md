# Scope and proportionality review

Reviewed `vpsfree-maintenance-tasks` commit
`9ec505df9b67bc19f7983c1bb5c34ad160eddd05` against
`6eea682ede8d8e2634b2d41e5b11cf0f02231bc6`, using the initiative plan,
state, review packet, repository instructions, and the unchanged vpsAdmin
models at `19971f039` as context.

## Findings

No Blocking, Important, or Advisory scope/proportionality findings.

## Assessment

The commit is confined to one dated maintenance-task directory and contains
one report implementation, its operator documentation, and focused tests. It
does not introduce shared abstractions, compatibility shims, generalized
integrity checking, or changes to vpsAdmin itself.

The implementation's substantial mechanisms are supported by the requested
contract:

- The three-way comparison of inventory, recorded use, and package/stored
  limits in `check_ip_accounting.rb:39-188` implements the explicitly accepted
  overage and accounting-drift report. Evidence arrays and unresolved charging
  environments directly support later administrator reconciliation.
- The repeatable-read, database-enforced read-only transaction in
  `check_ip_accounting.rb:196-203` is proportionate to an operational audit
  whose defining constraint is that it must not repair or otherwise mutate
  state.
- Decimal strings and schema versioning in `check_ip_accounting.rb:24-34` and
  `check_ip_accounting.rb:159-187` preserve the actual `decimal(40,0)` model
  contract and make the new report usable by later tooling without adding a
  parser or framework that has no current consumer.
- Private, complete, no-overwrite publication in
  `check_ip_accounting.rb:205-213` is a small self-contained safeguard for an
  administrator-facing evidence file. It does not expand into report
  lifecycle, retention, upload, or reconciliation machinery.
- The 16 examples in `check_ip_accounting_spec.rb:63-213` exercise the task's
  owned behavior and the explicit accounting decisions. They do not attempt
  to duplicate broad ActiveRecord, MariaDB, JSON, or filesystem conformance
  suites.

The README documents the current script contract and one example query; it
does not add deployment, repair, or downstream-consumer commitments beyond the
requested read-only report.

## Residual risks and test gaps

- Production-sized runtime and report size have not been measured. The code
  batches users, while retained mismatch evidence necessarily grows with the
  number of findings. This is a bounded operational observation rather than a
  reason to add batching/export infrastructure before a real need is shown.
- A snapshot can capture a transaction chain between its logical steps. The
  README explicitly requires review and rerun before reconciliation, which is
  the proportionate boundary for this read-only task.
