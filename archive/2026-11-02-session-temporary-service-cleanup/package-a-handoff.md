# Registered temporary services: package A handoff

Package A is implemented in dev-workspace commit
`08a0df822b4a01cef25207ba663df861b2b4006d`, on branch
`2026-11-02-session-temporary-service-cleanup`. Its parent is B's independent
Resources/UI commit `fac02494b5b41d0d4a6f299f083e67f4ea3a799e`; the initiative
base remains `c2182254d29c4175c3e9fe4267e5a92dd1da6b79`.

The Git index and all nine A paths are clean. A hands the Git lane back to the
lead/B and will make no further Git mutations without another lane handoff.
No branch publication, rebase, integration, deployment or real-session lifecycle
action was performed by A.

## Delivered behavior and documentation

- Durable first-registration marker, private registry and same-operation cleanup
  prelude, with strict paired-state validation and exact session identity.
- `service run/list/stop`, UUID request replay and read-only allowlisted public
  status. Retired observations retain their saved stop time and never probe units.
- Native manager/cgroup placement recorded before launch; exact unit properties,
  Description, InvocationID, settled jobs and recursive cgroup proof precede
  retirement. Native client calls have a bounded process-group timeout.
- Complete registered candidate cleanup before archive tracking pruning or delete
  file removal, with original lifecycle journals and retry policies preserved.
- Deletion transfers retired registration evidence into existing private recovery;
  an interrupted transfer is retryable.
- Pure package requirements inventory handles registry/marker presence in both
  directions and reports unreadable/non-directory inventory roots as errors.
- Launch-only activity composes into the existing automatic-archive activity
  dimension. Untouched native values remain identical; unknown registered state
  preserves the prior digest and blocks eligibility. No Store schema/allowlist
  expansion or extra capability gate remains.
- Owning explanations are in `docs/dev-sessions.md` (Temporary services) and
  `docs/session-archive-recovery.md` (Registered temporary service cleanup).
  The lead's contextual wording pass and final launch-request precision are applied.

Unregistered services are neither discovered nor inspected. The supplied example
units and other sessions remain untouched. This introduces local schema-1 state;
there are no database migrations, published predecessor service schemas or
runtime rescue paths for the unconsumed branch draft.

## Verification and exact scope

Final source component command, using the repository Nix shell:

```sh
nix develop --command ruby -Itest test/dev_session/session_services_test.rb \
  --name /test_session_services_/
```

Result: **21 tests, 243 assertions, zero failures/errors/skips**, 12.56 seconds.
This covers final inventory-I/O and activity-digest corrections, durable-before-
launch state, lost replies/exact replay, initialization interruption, busy and
pure readers, size refusal, missing state, exact InvocationID and cgroup checks,
fast success/failure, unsettled jobs, pre-prune ordering, automatic retry and
partial deletion-evidence transfer.

The exact predecessor Store and Policy from `c2182254` are retained as a test-only
fixture. They load never-registered, registered and fully-retired current records;
their native-token recomputation starts fresh grace. Extracted predecessor code
was compared byte-for-byte with the Git source prefix before `module Runner`:
SHA256 `7bf2baefcfb6b47b098c8f43c73d7f33b47ff3476277724fdb4c10b3e573ce05`.

Broader regression evidence: [operation 02](a-ruby-components-02/manifest.json)
ran **130 tests / 3,108 assertions**, no failures/errors/skips, in 460.08 seconds
(452.87 seconds inside the test runner). Fresh pinned Luna/low watcher thread:
`01a19d57-bd14-7212-8f45-5ceb0e0daf56`, danger-full-access/never. It completed;
no process or utility slot remains held. Logs and exact result are
[output.log](a-ruby-components-02/output.log) and
[result.json](a-ruby-components-02/result.json).

That broader run tested immutable source snapshot
`/tmp/2026-11-02-session-services-components-ltudcu4x`, digest
`5a6c091dd944cfe80720adb6c9e6a34bcae644bd38986845a404ba02c75c304a`, before the
final inventory-I/O and activity-digest corrections. It is evidence for unchanged
portions, not a claim that final commit `08a0df82` ran the entire 130-test set.
The final focused run covers the changed portions. Final reviewed package
verification must use the complete committed A+B source.

[Operation 01](a-ruby-components-01/result.json) failed before tests because an
implicit Nix flake reference inferred `/tmp` as a Git repository. Explicit
`nix develop path:/tmp/SNAPSHOT` fixed the environment. Both attempts are retained;
the first watcher was not reused. No kernel build or live lifecycle experiment
occurred. No repository hook framework or active non-sample Git hooks were
declared/configured; commits ran through the repository Nix shell, with a temporary
message file and no bypass. Ruby syntax checks and staged whitespace checks passed.

## Remaining work

The lead/B owns the remaining shared functional commits and final history packet.
Independent mandatory review must cover the complete committed deliverable before
the long package/host/real-systemd VM checks. Fake-manager component tests do not
establish native systemd behavior; B's lifecycle VM fixture remains required.
A retains responsibility for review findings and follow-up lifecycle fixes.
Separate integration approval is still absent.

Disposable verification copies are owned by this session under
`/tmp/2026-11-02-session-services-components-d9zzrbll` and
`/tmp/2026-11-02-session-services-components-ltudcu4x`; neither contains a running
test command. Raw verification artifacts remain disposable under the session's
ordinary retention policy. The session stays open.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
