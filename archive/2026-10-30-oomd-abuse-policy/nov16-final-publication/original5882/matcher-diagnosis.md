# Physical incident scenario — supported membership matcher

Exact original attempt963aee55 on ordinaryf9/4gj1/qljw ran once and remains
FAILED1/unexpected_failure. Native67907 and all operation work are terminal;
root accepted exact effects from two single-start/reapedQEMU0/destroy sequences,
both virtiofs disconnects and no new disk/socket/shared-dir/helper entries.
Original receipt98ac578980c29762e13d222bb7d39e906d58b27afbee450ed1b0167b0603e7b9
and all eight native-log lengths/hashes were independently verified and copied
unchanged into this directory. No manual cleanup or old-state action followed.

## Cause and bounded change

The exact compiled default script fails at8394 (scenario source152):

```ruby
expect(notices.map { |report| report.fetch('trigger_incident_report_id') }).to all(be_in(ordinary.map { |report| report.fetch('id') }))
```

The actual IDs are notice triggers[3,1], ordinary reports[5,3,1]. RSpec interprets
be_in as a dynamic predicate matcher calling in? on each Integer. The packaged
runner does not load that ActiveSupport extension. Reproduction uses the same
sv2 wrapper's explicit Ruby3.4.9, gem rootn2fk and RSpec expectations3.13.5/support
3.13.7, with the same rspec/expectations import and instance matcher context;
it reproduces the native message exactly, exit0. No API DB, guest, runner launch,
build, projection or dependency installation is involved.

The successor changes only that assertion:

```ruby
expect(notices.map { |report| report.fetch('trigger_incident_report_id') } - ordinary.map { |report| report.fetch('id') }).to be_empty
```

The set difference must contain no trigger outside the ordinary report IDs.
This retains the original subset direction, repeated-trigger and order semantics,
including the vacuous empty case; separate three-ordinary/two-notice checks remain.
No notice filtering, count/privacy/data weakening, dependency addition, threshold,
timeout, attempt or fixture change. A search finds only this one be_in/in? use in
the same scenario, so no additional defect or broader rewrite is included.

## Reached and unreached physical coverage

The exact retained compiled script executes sequentially and the native report
identifies this matcher as its sole failure. Thus the prior assertions completed:
first warning, deliberate SMTP stop and expected terminal mail failures, one
confirmed stop/autostart change despite duplicate input, restored SMTP and
independent stop-mail retry, one stop count, manual restart and first data sentinel,
third source count/cooldown, transfer completion/epoch/reset facts, new-owner empty
history, and admin three ordinary rows plus warning/stop_completed notices.
See failure-coverage.json for compiled line identities. These are partial results;
the whole example remains failed.

The membership assertion itself failed from its dependency, despite the actual
IDs being members. The corrected assertion has not run physically. The following
final post-transfer running-state wait and data command/assertion were not reached.
The earlier pre-transfer data check passed; post-transfer data preservation is
not yet established by this run. No whole-product success is inferred.

Native total1243.228367045s, runner1242.926364215s, default script969.78s and single
example493.37s are nested clocks, not summed. Original quota diagnostic success
remains only a non-reproduction; no quota investigation/retry or attribution is
part of this matcher correction.

## Focused controls and retained setup evidence

Ten exact-successor-source assertion cases pass with real packaged dependencies:
actual IDs, reordered IDs, shared trigger and empty subset positives; foreign,
nil, empty-source and reversed-subset negatives. No private matcher replacement
or ActiveSupport import is used. reproduction.json and membership-controls.json
record exact gem/interpreter identities. Ruby scenario-body syntax, Nix parse and
whitespace pass; normal commit hooks supply required Nix formatting and owning
repository checks. The source delta is exactly one line; all later assertions
and every helper/ordinary strict call are byte-identical.

An initial private reproduction check invoked the RSpec include matcher at Ruby
top-level, colliding with Module#include after the native failure had reproduced.
Its original script/exit are retained as reproduce-top-level-before.*. Moving
that private check into the runner-like instance matcher context fixed setup;
reproduction and all ten controls then passed. This did not change product source
or weaken checks. Normal hook-signature refusals are retained separately; unchanged
trusted configuration and four plugins were inspected and signed through ordinary
Overcommit commands. No hook bypass is authorized or used.

## Smallest faithful follow-up, not executed

From the final clean committed ordinary source:

```sh
./test-runner.sh test alerts/incident-escalation
```

Run the same one-default/one-attempt scenario with original600/900bounds. It must
retain setup/SMTP-negative phases and all retry/history/transfer/data assertions;
an isolated tail would omit its preconditions. Root owns fresh exact-final-source
input/selected-config/capacity and sole long-run admission. The only successor
runtime input delta is this test assertion; API product source, migrations,
schema, flake/package inputs, machine profiles and runner dependency declarations
are unchanged. Reuse retained runner/kernel/construction facts only after the
relevant input/derivation equality is established. Do not treat old4gj1/qljw as
successor-source proof, and do not launch a broad suite or automatic retry.

No physical/build/projection/push/CI/export/client/pin action is taken in this
package. Preserve f9 failure, original CI failure and b876/82c9 diagnostic refs;
root controls final history/publication sequencing. No product documentation
update is useful for this test-only dependency correction; this technical record
and owning A packet hold its evidence and remaining acceptance boundary.
