# Exact proposed project prose for lead English pass

The source design is accepted at design.md:2002. Focused helper/rendered/snapshot tests pass31/31 in10.39s on the current working inputs. Combined compiler/audit checks are pending; no browser or broad pass is claimed. Only the following current-contract fragments and one append are proposed. Existing history stays intact.

## docs/design/REQUIREMENTS.md, REQ-055 row

| REQ-055 | Preserve advisory management and audit evidence. | Privileged management gated independently of navigation; history readable and filtering supported; advisory table cells have consistent edge spacing and headers align with their content; original text, CVEs, precise/null publication time and node assessments remain editable in draft/published/retracted states with captured revision/state guards; bulk node notes change only for explicitly selected languages, including explicit clearing; explicit silent retraction and permanent deletion require confirmation; partial or uncertain saves preserve input and stop before another write; no exposure of sensitive secrets. | C; [advisory routes](../../src/routes/securityAdvisoryAdminRoutes.tsx), [audit](../../src/lib/api/audit.ts) | Baseline; [expanded corrections prepared](../work-log/2026-11-01-advisory-corrections.md), not deployed |

## docs/design/WORKFLOWS.md, replace existing localized-note paragraph

Publication and mitigation inputs retain seconds and preserve null. Editing can
leave zero CVEs or missing node assessments; only explicit add/bulk operations
create rows. Existing retired-node assessments remain removable. Node notes use
localized fields. A bulk note field stays disabled until its language's update
checkbox is selected. Unchecked languages retain their existing notes; selected
text replaces the note after trimming, and a selected empty field clears it.
Unchecking retains the draft but omits that language from the write. Cancelling
and reopening bulk resets its note choices; cancelling only the confirmation
retains them. The single-node editor preserves languages it does not edit.
Published and retracted node writes offer resolved states and require both
mitigation times when mitigated. A correction refreshes affected-user/VPS and
public caches.

## docs/work-log/2026-11-01-typescript-client-migration.md, append

## Broad-smoke fixture repairs and explicit bulk notes (2026-11-03)

The broad workflow on merged WebUI `670cf286` failed 24 Chromium and nine mobile
Chrome cases across 12 specs. Diagnosis inspected all 99 retained attempts,
including retries, before correcting source. The six successful required core
and PR-smoke jobs and final Nix packages had narrower verification scopes; no
passing broad result existed before merge.

The affected fixtures now use generated response namespaces, nullable resource
references, serialized transaction payloads and complete lookup identities.
Request approval fixtures provide authenticated eligible resources, and the
list-return case explicitly opts out of the existing review queue. Tests cover
the supported OS-family filter and existing manual rollback reconciliation.
Busy gates, payload omissions, focus restoration, receipts and no-replay
assertions remain. Whole-leaf strict adoption now selects 152 files and retains
131 deferrals, with the original baseline, sourceRevision, compiler options and
surviving deferral records unchanged.

The advisory trace also exposed a product defect: a state-only bulk update sent
null notes and cleared existing text. Each bulk language now has an explicit
update checkbox. Unchecked fields are omitted; selected text is trimmed, and a
selected empty field clears only that language. Existing single-node editing,
public-note privacy help, captured guards, sequential revisions and partial-save
recovery remain. The browser case retains its stored-note assertions and now
expects the required captured state in every exact mutation body.

Focused helper, rendered-panel and snapshot tests passed: 3 files, 31 tests in
10.39 seconds. They cover note preservation and explicit clearing, independent
languages, cancellation, missing-row creation, an in-flight payload and blocked
replay after failed read-back. These are working-source and synthetic-fixture
results. Independent final review, implemented EN/CS desktop/mobile captures,
final broad smoke and integration acceptance remain pending.

The approved bilingual copy follows the repository's own locked terminology at
API `a65a4dfe`; the site's effective API `942c6eae` is a distinct revision with
identical inspected guide bytes. The canonical KB contract at `f97785c2` maps
PHP/API942c and has no registered React advisory control, managed page or
screenshot concept for this change. No mapped KB update was identified;
unregistered live wiki prose and existing image currency remain unverified.
No backend, SDK, dependency, persisted-format, configuration or running-preview
change is part of this repair.

## WORK_LOG.md, prepend index entry

## Broad-smoke fixture repairs and explicit bulk notes (2026-11-03)

Correct the observed generated-wire fixtures and preserve untouched notes during
bulk advisory updates. [Scope and verification](docs/work-log/2026-11-01-typescript-client-migration.md#broad-smoke-fixture-repairs-and-explicit-bulk-notes-2026-11-03).
