# Post-collection mechanical receipt interface

Preparation only. No snapshot read, API call, extraction, collection or restricted
project file write has been executed under this interface. Execution requires
lead notification after the one shared collection. The watcher owns collection;
this package reads its frozen result only.

Inputs: frozen ignored `.state/evidence.json`, its collection receipt,
`assessment/livepatch-seeds.json`, and `assessment/prerelease-boundary.json`.
Compute the exact snapshot byte SHA256 and retain it in every output. Check the
actual schema against the repository collector before extraction; missing or
unexpected shapes are reported rather than silently omitted.

## Release flags

Inspect both current `nodes[].kernel` and every retained
`nodes[].kernel.history[]`, including each event's `security_evidence.kernel`.
Read both `booted_release` and `reported_release`, including event-level release
fields even when an event lacks security_evidence. Flag prerelease/rc identifiers
and custom/ambiguous release forms, preserving the original string verbatim.
Do not normalize them into final releases or infer source membership.

Restricted `.state` receipt retains Node/event linkage, exact field path,
original release and available source/build identity for architect inspection.
A sanitized session receipt may contain snapshot hash, checked current/event/
release-field counts, flagged counts and unique release strings only. Missing
release/source fields are completeness limits, never evidence of safety.
Flag relevance to 7.2 prerelease/custom ambiguity separately for architect
attention. If actual evidence needs the distinction recorded for
CVE-2026-74753, report that its evaluation/sync must stop until architect
reconciliation or a scoped evaluator fix; do not edit evaluations, source
boundaries or code. This flag is not an impact classification for other CVEs.
If no relevant ambiguity occurs, no tooling change follows from this unit.

## Livepatch observations

Enumerate every current `runtime_mitigations.livepatches` entry and each
retained event's `security_evidence.livepatches`, with no enabled/transition
filter. Retain empty arrays and missing containers as separate completeness
counts. Preserve both possible atomic-replacement counterparts, inactive
patches and transitioning patches. Do not fill sparse identities or carry a
patch across events/boots; the evaluator owns timeline semantics.

Restricted `.state/livepatch-observations.json` (mode 0600) preserves raw
components, Node IDs/names, boot IDs, event IDs/kinds, timings, enabled/transition
states, booted/reported/module kernel releases and available Linux/software
identities. Boot and event linkage never enters session artifacts.

Sanitized `assessment/implementer3/livepatch-observed-tuples.json` contains
opaque SHA256 tuple keys bound to snapshot hash, distinct source tuples and
completeness/observation counts. A source tuple preserves module ID,
patch_version, module-reported kernel_version, booted release, reported Linux
revision if present, and relevant booted/current vpsAdminOS revision/cleanliness.
Record enabled/transition state combinations without Node/event association.
Do not invent exact recipe, variant or source identity; technical owners bind
those later. Missing fields remain explicitly missing. Never claim coverage,
accepted tuples, activation safety, mitigation intervals or first fix dates.

All raw linkage stays in ignored restricted project `.state`; only sanitized
counts/release strings/source tuple identities reach this owned session path.
No shared snapshot replacement, extra API calls or Node recollection is part
of this interface. Architect accepts substantive source/coverage conclusions.
