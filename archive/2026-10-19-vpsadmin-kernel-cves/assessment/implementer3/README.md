# Mechanical requirements-union helper

`check-union.rb --partition-only` checks the package map against the exact 60
approved IDs without reading owner ledgers or partially written dossiers.

After lead notification that ledgers/declarations are ready, run through the
repository-pinned Nix Ruby environment:

```sh
nix shell --inputs-from /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories nixpkgs#ruby_3_4 -c ruby assessment/implementer3/check-union.rb
```

The helper reads `assessment/<owner>/requirements.json` with the Phase 3
`rows` interface, checks exact ID ownership and required fields, then loads all
worktree dossiers with the existing `SecurityAdvisories::Advisory.load`.
Invalid legacy or new dossiers are reported because the collector also loads
all dossiers. It compares owner option maps, reviewed sysctl value maps, history
start and roles with the actual declarations. It reports the collector's
all-dossier option-name union and earliest history start, plus sysctl names.
Array ordering has no meaning for accepted sysctl values or roles. Source and
unmodeled prerequisites are checked for field presence, not interpreted as
new evaluator predicates. Owner/architect review must settle their semantics.

Output is written only here as `partition-result.json` or `union-result.json`.
No credentials/API calls, source/index edits or raw evidence writes occur.
Incomplete owner ledgers/dossiers are pending dependencies, not a security
classification failure. Unknown runtime state is not evaluated by this helper.
The architect accepts the reconciled union; passing this helper does not
release collection. Wait for the lead's exact collection command before any
production Node read or shared snapshot write.

The provisional design, package map, repository loader and collector interfaces
were read before preparation. No declaration scan or production collection has
been launched while owner ledgers are being prepared. This helper does not
invent requirements or repeat CVE research.

## Early ledger-only checkpoint

`check-ledgers.rb` explicitly accepts only a root array or an object with a
`rows` array. The current owners 0/1 use object.rows; owner 2 uses an array.
It validates exact ownership and required field shapes without loading any
incomplete dossier. It preserves each CVE's option predicates and accepted
sysctl values separately; a union of names does not merge those semantics.
The full declaration helper accepts these same two explicit containers.

The initial ledger-only result is [ledger-union-result.json](ledger-union-result.json):
60 distinct approved CVEs, 20 per owner, no structural mismatches, 41 CONFIG
names and four sysctl names. All declared history starts are
2026-01-01T00:00:00Z. Exact input hashes are recorded. No dossier completeness
or source-citation semantics were assessed in this pass. The actual all-dossier
validation/declaration gate remains pending and collection is unreleased.

## Actual declaration gate

The released offline gate loaded and validated all 111 dossiers (60 approved
plus the 51 existing), with all three ledgers present and no ownership or
option/sysctl/history/role mismatches. The collector catalog has 67 CONFIG
names, seven sysctl names, and earliest history start 2026-01-01T00:00:00Z.
The updated 98039 declarations include BPF_JIT and DEBUG_INFO_BTF; 98368 includes
IO_URING and the reviewed io_uring sysctl declaration, matching latest ledgers.
Exact ledger/dossier hashes and declarations are in [union-result.json](union-result.json).
This establishes mechanical readiness for architect reconciliation only. No
collection or substantive union acceptance is implied, and no API was called.

## Prepared final acceptance helper (not executed)

`check-final-acceptance.rb` awaits lead notification of the final source and
evaluation freeze. It uses current repository Advisory.load and
Reconciler.load_evaluation, with a client that rejects network calls. It checks
exact approved60, supported dossier schema1/2 through the loader, evaluation
schema/dossier digest through Reconciler, frozen snapshot SHA and shared evidence/
node-set digests, 13 exact Node IDs (never emitted), required completeness.states and summary counts/flags/blocking-set consistency, bilingual text presence, saved primary 6.12 fix versions/SHAs, the
recorded 64387 effective-fix exception and 74753 canonical stable bounds.
Sanitized file/dossier digests and counts are written only under this path.
It does not evaluate again, reinterpret security outcomes, refresh duplicate
APIs, rewrite prose or certify independent review/publication readiness.
Supporting repository interfaces remain in progress; recheck their final
shape at freeze before execution rather than treating this preparation as a
passed final gate.

## Final frozen gate result

Executed through Nix Ruby at frozen head
34ad7d5785382215cbe00b5140174cad5661a132. All 111 dossiers load and validate:
110 schema1, one schema2 (CVE-2026-74753). Exact approved60 evaluations load
through Reconciler: 59 schema1 dossiers plus the one schema2 dossier, every
schema4 evaluation matching its dossier digest and the same frozen snapshot
SHA/evidence digest/node-set digest/collection time and exact 13-Node set.
Required completeness.states, summary counts/flags/blocking IDs match actual
rows. Primary stable fix fields, documented 64387 effective exception, canonical
74753 stable bounds, public dedup and localized text presence pass. Zero errors.
[Final result](final-acceptance-result.json) includes sanitized hashes/counts;
[Catalog helper](check-final-catalog.rb) extends the prepared approved60 helper
to verify all 111 with the same loader. No API, evaluation execution/edit,
source/index write or collection occurred. This is source/snapshot consistency,
not independent review, security correctness, writing review or publication
readiness. The earlier helper preparation section is historical.

## Review-remediation digest gate

Rechecked current head ef4b0604d8bfb9750a6a9a2a3487daac754234e5 through the
same offline helpers: all111 loader-valid, exact60 evaluation/dossier digests,
same frozen61904 snapshot and13Node set, mandatory summaries/fix exceptions/
dedup/localization presence pass, zero errors. Prior receipt retained as
final-acceptance-34ad7d5.json; current final-acceptance-result.json and
remediation-digest-delta.json record the new head and changed digest counts.
No API, evaluation execution, source/index write or security review was run.
