# Hosted verification after the diagnosed comparator fix

Preparation only, implementer3. C owns the source fix, composition regression
and Git/amend window. No D source edit, push, rerun, snapshot, dispatch,
cancellation, CI wait, test or installation is authorized in this continuation.
The utility slot being free does not authorize D to occupy it.

## Diagnosed failure and preserved evidence

Old published candidate: `ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43`.
Fixed accepted reference: `b85ec364057f536940d689b09e612512ffffaf82`.
Default/merge-base captured at publication:
`39909094649b1d14a23f00615775ca7136acf4fd`.

Manual quick `40186001987`, attempt1, completed failure with runner exit3:
`Invalid comparison input: key not found: "sha"`. The lead accepted C's
root-cause diagnosis: parent `run_samples` returned its original symbol-keyed
source proof to the direct Comparator instead of the existing normalized
`@sources`. JSON serialization of saved samples had hidden that in-process
composition mismatch. The authorized fix returns the existing normalized source
proof and adds a run-composition regression. No schema, gate, budget or workload
change is intended. C owns the final correction and its checks; D does not
modify C's files or interpret a source change as reviewed before lead acceptance.

**No numeric result or classification from this failed head is accepted.**
Raw worker measurements remain diagnostic artifacts. A first workflow attempt
at a reviewed corrected head will verify the diagnosed source correction;
it is not a blind rerun of the old attempt. Preserve the old failed report,
logs, samples, source archives, inputs, fingerprints, run IDs and receipts.

Original push inventory: eleven runs in
[old snapshot](api-performance-hosted/ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43/push/runs-initial.json).
Performance push ID `40185931208`; manual quick ID `40186001987`;
accepted manual weekly ID `40186402016`. Complete quick failure evidence:
[old checkpoint](api-performance-hosted/ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43/hosted-verification-status.md),
[authoritative run JSON](api-performance-hosted/ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43/manual-quick/bounded-status/run.json),
[raw attempt logs](api-performance-hosted/ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43/manual-quick/bounded-status/logs.zip),
[raw artifact](api-performance-hosted/ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43/manual-quick/bounded-status/artifact.zip).
Quick artifact SHA256:
`524b1bbbc274acf7146460f40851b4212c23aeff9d1efa14331f3bf24dad006d`.
Old weekly dispatch receipt remains preserved; its actual status has not been
read by D. Do not invent completion/failure or cancel it before a new final
head is published and verified.

## Future successor publication, not launched

Wait for the lead to supply the final corrected full SHA/tree, accepted affected
review/check evidence and a new exclusive Git publication window. Capture exact
old/new ranges and whether C amended published history. Never reuse ae60's old
publication script: its frozen head/tree checks are intentionally obsolete.

In the normal prepared top-level Nix environment, with ordinary hooks and no
installation, recheck exact candidate/tree/branch and clean tracked/index state,
canonical SSH origin, fixed b85 ancestry and preservation of the first-seven
commit lineage. Retain the final review/range receipt. Fetch over SSH only when
the new window authorizes it; stop if origin/master or the expected merge-base
moved from 39909094649b. Never auto-rebase or refresh the reference.

Use a new evidence directory `api-performance-hosted/<NEW_REVIEWED_FULL_SHA>/`;
retain exact commands, logs, exits, runtime/store paths, workflow/budget/flake
copies and hashes. Verify the remote branch still has the expected published
head before selecting publication mode:

- If the successor is a fast-forward from the published remote, ordinary
  feature-only non-force push is appropriate.
- If C's amend rewrites the already published tail, report that fact and the
  exact old/new ranges to the lead. Use only the publication mode approved in
  the new window; a lease must name the exact previously verified remote head
  `ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43`. Do not silently force-push or retry
  a failed push with a broader option.

After an authorized successful push, require SSH `ls-remote` equality with the
new full SHA and fresh clean local head/tree/index proof. Retain all receipts
and relinquish the Git window promptly. No default push, PR, merge or release.

## Superseded-run evidence and cancellation after publication

The lead explicitly authorized cancellation only **after** the new final head
exists and fresh remote-head verification succeeds. This is not permission to
cancel ae60 work now or any current-head run later.

After publication, take the lead-authorized bounded status inventory of old
same-branch ae60 runs. For every possible cancellation, retain complete original
run/attempt/head/event/branch/status JSON. Verify all of:

- Canonical feature branch now resolves to the new reviewed full SHA.
- The selected run belongs to `vpsfreecz/haveapi` and branch
  `2026-10-24-context-copy-performance-tests`.
- The run's authoritative `head_sha` is exactly old ae60, different from the
  new published head, and it is queued or running (not terminal).

Before cancelling obsolete weekly `40186402016`, capture all available evidence:
run/attempt/jobs/step JSON, available attempt logs and artifact metadata/files,
with commands/exits and SHA256 manifests. Verify any retained artifact's run/head,
expiry/digest and actual event inputs. A still-running run may not expose logs
or an artifact yet; preserve the precise API refusal/absence, do not pretend
missing evidence was captured and do not poll or wait outside a granted watcher.
Capture equivalent available evidence for an obsolete running performance push.

Only after those guards/evidence, use `gh run cancel OLD_RUN_ID --repo
vpsfreecz/haveapi` for the specific superseded queued/running run and preserve
command output/exit. Terminal ae60 runs, other branches and every current-head
run are excluded. Reconcile cancellation errors/races with authoritative state
rather than treating a successful CLI call as completed cancellation. Any
uncertain/long completion wait uses a separately granted fresh utility; do not
run a parent polling loop or leave an uncertain effect unreported.

## New exact-head workflow inventory and later dispatch

Once publication and a bounded snapshot are authorized, enumerate all eleven
expected workflows for the new exact full SHA/feature branch, retaining IDs,
events, status/conclusion and URLs. Keep new attempt evidence in the new-head
directory; do not overwrite ae60 records or reuse its run IDs as new evidence.
Run IDs for the successor do not exist yet and must not be invented.

The push automatically triggers hosted checks. A watcher starts only in the
lead's granted serialized utility window, with fresh pinned Luna/low policy,
exact new-head run IDs and no diagnosis/edits/reruns/dispatch/cancellation.
D independently checks artifacts, exact source/input/runtime graphs, operation
counts and every output identity before accepting classifications. Any
regression, inconclusive, schema/provenance/response error blocks; no automatic
reference/budget update or retry-until-green.

**No new manual workflow_dispatch is authorized yet.** Wait for corrected final
review acceptance, publication and the lead's explicit new dispatch batch.
When authorized, quick/weekly use the exact corrected candidate and unchanged
b85 reference, retain each first attempt/input receipt, and serialize same-group
manual runs to prevent one cancelling the other. Preserve actual dispatch
refusal if encountered; never merge or work around default-registration policy.
PR/default/Sunday event execution stays distinct from locally tested resolvers.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/
