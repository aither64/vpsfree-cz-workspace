# Final follow-up review, 2026-11-10

No findings. The focused proxy-guide addition and refreshed feature preparation
are acceptable within the plan-only request. This is not a deployability result
or authorization to provision credentials, change permissions, activate or merge.

- Base: `0f3897b5b7dc53edee33f1289cbda25ec28910f5`.
- Reviewed head: `959e1d54cabc7ac5530dac6179acacb077a57754`.
- Tree: `d12a1746a0d11506559b5dc98c1b3105e1bd7fec`.
- Reviewer: retained independent `reviewer0`, `gpt-6.1-sol` / `xhigh`, saved
  `read_only`; live same-session roster/thread verified, no overrides/fallback.
- Lanes: General, Scope and proportionality, Risk and compatibility. High risk
  because the runbook governs live proxy activation and access setup.

`dev-session current` from the bound tracking CWD matched the session; both
optional environment identity variables were absent. Rechecked before writing.
Project HEAD/tree matched and worktree/index were clean. Read the current review
skill and assigned references, including all seven documentation questions,
applicable current workspace/repository guidance, design/state and both Nov10
receipts. Reviewed the complete series/diff inventory, replay range-diff and
new guide delta directly. No nested agent, test, live command, credential access,
Git mutation, claim or lifecycle action was used. Only this report was written.

## Scope, correctness and compatibility

Scope was assessed first. The only substantive addition after mechanical replay
is the paragraph at `docs/operations/prometheus-query-access.md:77` and the split
dry-activate/switch code fence. It gives a reusable, proportionate safety checkpoint
for this shared proxy; it introduces no script, application mechanism or redesign.
Routine session planning/evidence did not itself trigger this review.

The paragraph requires comparing nginx configuration, packages, activation scripts
and affected services against the running system, retaining rollback, and validating
the candidate configuration before switching. It prefers reload, forbids a deliberate
nginx stop, and requires aborting for unexpected disruption or more than a brief
reload/restart. It correctly warns that a reload-capable unit may still be restarted
by system activation. It does not promise that `enableReload` alone satisfies the
outage constraint. The dated plan records concrete gates and fallback separately.

The reported live preflight explains why that checkpoint matters: live blog.org
routing/upload behavior is absent from the old Nov2 artifact, which would also
remove three ACME units. The guide does not certify that old artifact or the fresh
candidate. The current metadata scan is also correctly treated as an observation,
not a final quiesced inventory or outage estimate. Required world-readable-message
consumers remain unresolved before permission changes. These are execution gates,
not defects in this completed preparation deliverable.

Prior implementation/architecture conclusions in [review-followup.md](review-followup.md)
and [operator-simplicity-review.md](operator-simplicity-review.md) remain applicable
to the equivalent replayed work. No authentication, helper, API, credential format,
log format or persisted-metadata contract is changed. Human access, runtime-file
independence, conditional rollback revocation, recovery and user-owned root-key
removal are preserved.

## Documentation placement and preservation

All seven current general-lane questions pass for the affected material:

1. **Discovery:** README's grouped Operations section links both access guides;
   MkDocs preserves their entries beside upstream navigation. Existing README
   anchors, including `aitherdev-operations`, are retained.
2. **Audience/owner/home:** operator-facing permission and SSH guidance belongs in
   `docs/operations/log-reader-access.md`; credential/query and low-outage proxy
   operations belong in `docs/operations/prometheus-query-access.md`. Concise
   configuration facts in these runbooks support their tasks. Dated refs, profiles,
   steps and results belong in session `design.md` and the two Nov10 receipts.
3. **Durability:** the new proxy paragraph remains useful after this rollout and
   requires no private branch/session context. Exact Nov10 store paths and candidate
   assessment remain in session records, not reusable configuration documentation.
4. **Fidelity/evidence:** the guide describes requirements, not executed results.
   Source, receipt and plan distinguish observed live facts, equivalent source,
   historical successful tests, unavailable outputs and pending candidate checks.
5. **Preservation:** no content relocation occurred in this delta. Existing setup,
   initial-only `-c`, private modes, maintenance restart guard, partial-failure,
   stale-inventory, rollback and revocation guidance is retained; the switch step
   is separated from dry activation to expose its new precondition.
6. **Applicability/retirement:** no supported upgrade/recovery path is retired.
   Earlier user rollout remains historically unknown; reported current absence
   of the features does not justify discarding persisted-state recovery. Actual
   required logger readers remain an explicit unresolved operator prerequisite.
7. **Authority/links/meaning:** each contract retains its existing configuration-owned
   guide. README/MkDocs lead to those homes, existing page headings/anchors remain,
   and the new prose strengthens the operational checkpoint without changing the
   access contract. Individual execution evidence is separately linked in session
   records, respecting the repository's prohibition on tracked rollout receipts.

Explicit conclusion: placement, discovery and preservation are sound; no relocation
exception, lost recovery instruction or unsupported-path retirement was found.
Unresolved execution applicability is disclosed rather than silently assumed.

## Complete history and verification conclusion

The complete three-commit series is:

1. `6f65dd5383643c27bcc7d33fe1b882c8b8981675`: logger.
2. `27868feec96aafa6cd458a6e919e5081fead4e4c`: proxy/shared registration.
3. `959e1d54cabc7ac5530dac6179acacb077a57754`: operator guides.

Independently checked the old-to-mechanical range-diff: logger and docs replay
equal; proxy differences are limited to README/flake/MkDocs registration placement
and context, preserving upstream and feature entries. The mechanical tree at
`54b4f273` is `8bdfa6b5b7ada0201caed2dcd9cbdb7faaca7814`, matching the recorded
pre-rebase reconstruction. The final delta is only the accepted proxy paragraph
and fence split. Helper, policy, logger guide and fixture blobs checked against
the prior reviewed head are identical. Full final inventory remains 15 feature
paths, +1577/-6. The focused change is folded into its owning docs commit.

No obsolete application approach, transitional shim or redundant fixup remains.
There are no repeated dependency/channel/input/generated update streams in this
feature series. The final lock equals new master exactly; independently compared
the old/new lock blobs and confirmed only the seven inherited nodes listed in
the receipt changed. They are baseline updates, not feature pin-selection commits.
**No migrations** or transitional migration lineage are introduced or rewritten;
there are no migration versions needing deployment/release provenance.

Quick checks/hooks are recorded as passed. The four evaluated check derivations
match the Nov2 successes, but their output paths are currently unavailable locally.
This report claims neither a fresh runtime pass nor an available built deployment
artifact. Repeating unchanged long checks merely to prepare this plan is unnecessary.

Before any separately authorized execution: build fresh exact logger/proxy closures,
preserve actual live rollback closures/generation mappings, compare full candidate
packages/units/activation/nginx effects, validate the explicit candidate configuration
with required runtime files, and apply the no-prolonged-proxy-outage gate. Do not
deploy the regressive old Nov2 proxy artifact. Resolve required logger readers,
then use a fresh quiesced inventory and preserve restart/recovery handling. Runtime
credential provisioning and live SSH/HTTPS/ingestion/exporter/rotation acceptance
remain pending. Source publication supplies no deployment or merge approval.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-21-aitherdev-observability-access/>.
