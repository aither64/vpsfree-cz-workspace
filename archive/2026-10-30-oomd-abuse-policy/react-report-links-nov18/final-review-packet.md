# Nov18 React policy explanations and report links — final source packet

Package43a556cf is complete for independent review. Clean local head
`6b14ae5e1702ee8c137605d3512c123c9a24b582`, tree
`727af56aede9132a1e9a77c5726330f31ed61044`, on retained base
`88ac13b89d6421c914cd57e18153de1fee6fc7b7`. No push, PR update, CI operation,
browser, immutable package, demo, deployment or lifecycle action occurred.
Owner2 retains concrete fix ownership and the exclusive React Git/index window.
Live roster and verified session retain Sol/xhigh/workspace_write; no settings change.

## Scope and source

The lead/architect Nov18 addendum in `design.md` is the authority. The change
adds clear supplied Period / Incidents / Limit / Action rows for current policy
facts and saved report facts. It adds a report-list navigation tab beside the
existing policy destination, preserving app/admin and owner query context.
Authorized report detail renders explicit matched=true recorded/audit_only rows
in stable key order, active policy anchors, and filtered history for retired
keys. False/null and every error state remain separate admin diagnostics; missing
capability/data receives the approved neutral message. A notice uses only its
explicit saved origin. There is no codename inference, per-row list lookup, new
action or generic framework. Shared permission, guarded writes, uncertainty
locks and threshold-only overview/list warnings remain.

The reusable table and saved-section components are feature-local. The registry
lookup is shared/cached and detail-only. Navigation uses authorized included VPS
associations and opaque-key encoding. Tests cover two unequal policies, supplied
and absent facts, active/retired links, false/null/true error states, admin/member
privacy, notices, owner context, old capability and narrow rendering. The browser
fixture is extended and typechecked; it has not been executed in this package.

Compared with accepted b1fb:33 paths,967 insertions/158 deletions, including
173 lines of new history tests and the new dated worklog. The complete retained
base-to-head series has79 paths,3810 insertions/62 deletions, including eight
historical PNGs. See [Nov18 delta](nov18-final-delta.patch) and
[complete final diff](full-series-final.patch). Changes are scoped to React,
its fixture/tests, catalogs, dependency input and owning documentation. No backend,
BFF, runtime peer, flake lock, route declaration or migration change is introduced
by the Nov18 delta.

## Exact SDK dependency

Ordinary immutable development URL:
`https://raw.githubusercontent.com/vpsfreecz/vpsadmin-typescript-client/2d251bb0e10f5379a19df3a07eb7a0b0f19e3c88/development-artifacts/incident-escalation-sdk.tgz`

- Packed source `44c651b2a57e8de553dd51236c2dccbc09946fac`.
- Actual backend `de4df3d63f4d4afb0c27e8b9be2785c15d24811c`.
- Schema SHA256 `7cb28ebd8e0957d9a8ba2c359c8658040ed1cd195f0dd14327c03b595012fc85`.
- Raw generation provenance `a9e536e9984183866604a7b8d14c6f1ba02f26e7986b52f10131ee82f2cd6fd8`.
- Archive345048 bytes, SHA256 `983061ec981e24e45c25abeef81d8049d4253bad4d473ea37d5ce27ff0a1b718`.
- Integrity `sha512-Efx3yzdcq1Z1IvLFhn5AB4Go609guqaJuiLWgWTMhzw9z4Zs0MIXI+0kTeemCkjk6NuL8RxfgeeCJAjwXms6Pg==`.
- Exporter lock `2e9a124eff7b80d6fd57cd0f03cb2809847c67cc7f1af6364911c3622d7242a0`.
- HaveAPI generator1ef9b204 and runtime0.32.0 remain distinct and unchanged.

The actual generated nullable matched/period and notice-origin members are used;
obsolete discovery source_type is removed. No copied models, unchecked casts,
raw fallback or custom pipeline. All1382 installed archive files match; the lock
delta is only root+SDK records. Manifest, lock and development provenance agree.
The actual prefetch result is
`sha256-R22CY+X8p6ZSXIq9shb+Plz4JNOCFiaMa5H3pqTUtWE=` in frontend.nix.
The BFF graph is unchanged. See sdk-verified.json, sdk-installed.json and the
adoption logs. The former3cb7/API5aa/b00e archive evidence remains literal.
A published registry SDK artifact containing these fields is required before
any eventual default integration. This candidate is not a registry release.

## Quick evidence and original failures

All commands use the declared `nix develop` environment. Exact argv and input
hashes are in the frozen plans/results, not inferred from current HEAD.

| Evidence | Actual outcome |
| --- | --- |
| Full application typecheck against final SDK |0,72.242s; final-quick-01.log |
| Original nine focused files |86 pass/2 fail,8 files pass/1 fail,17.293s; final-quick-02.log |
| Minimal JSDOM diagnosis and stronger complete five-href assertion |Existing correct href reproduced; affected file9/9,0,11.804s; selector-diagnosis.md and retired-link-diagnostic* |
| Narrow affected TypeScript proof |Initial temporary config omitted existing ambient declaration; retained failure14.224s. Corrected config includes actual src/types/vpsadmin.d.ts;0, native68544 |
| E2E core typecheck |0,18.199s;207 checked/108 deferred; final-completion-01.stdout.log |
| Lint |Initial four arbitrary widths rejected1/2.500s; four classes changed to standard w-1/4, then0; width-token-control* |
| Remaining nine commands |All0,50.002s aggregate; final-unrun/results.json |
| Production assets within those nine |0,28.413s; chunk-size warning retained |
| Prefetch within those nine |0,3.024s; six optional WASI missing-resolved warnings retained |
| Final docs inventory |0;268 routes/75 API modules; regenerated content unchanged |
| Final design docs audit after returned prose/facts |0,2.067s;289 docs/76 requirements; final-docs-metadata-01.log |
| New files/worklog formatting |0; final-new-files-format* |
| Frontend hash metadata parse and diff whitespace |Both0; final-docs-metadata-result.json |

The nine-command batch includes scoped format82files, i18n8387keys in each locale,
i18n structure, structural budgets, component contracts, UI strings, mutation
audit, assets and prefetch. Original failure logs/results are immutable and are
not relabelled. The eight unchanged test-file passes plus affected9/9 establish
the focused88-test scope cumulatively; no full-unit rerun is claimed. Prior draft
checks are recorded separately and do not replace these actual-SDK checks.

The temporary narrow-config failure was check setup, resolved by including the
repository's existing declaration. The class correction affects layout widths
only: [width-token-equivalence.json](width-token-equivalence.json) reverses four
literal substitutions to the original checked input hash. No type/logic/text
change requires repeating full typing or units. The stronger href assertion has
its own real narrow type proof and affected tests. Production assets were built
after the class correction. This is npm asset evidence, not Nix installed-package
or final clean-commit provenance proof.

## Writing and documentation fidelity

Root applied the required main-agent writing pass and supplied the final EN/CS
product strings. All seven returned prose hashes matched before factual result
reconciliation. Six paths remain exact; reverse application of the saved factual
paragraph diff reproduces the seventh returned hash. See
[root-writing-final-equivalence.json](root-writing-final-equivalence.json),
root-final-writing-return.json and final-factual-prose.diff. Product strings and
protected technical identifiers remain unchanged. Locked terminology revision:
`a65a4dfeb92a59df4a80a737a20bcbf8558793ff`.

| Topic / readers / class | Owning location and evidence |
| --- | --- |
| Current/saved facts, privacy, absent data / developers / reference |API_CONTRACTS, WORKFLOWS, REQUIREMENTS REQ051 and EVIDENCE_MATRIX; implementation and focused actual-SDK tests |
| SDK identity and supported development input / maintainers / reference |HAVEAPI_CLIENT and PACKAGING; verified archive/installation/prefetch |
| This implementation and its actual limits / maintainers / dated execution |docs/work-log/2026-11-18-incident-policy-explanations.md, linked by WORK_LOG |
| Check failures, history and review handoff / session owners / execution |This packet and raw receipts; no temporary private work path in product inputs |

Old anchors and previous dated accounts remain. All eight historical PNGs are
byte-equal to b1fb and retain their own source labels. They are not Nov18 visual
acceptance. No KB/runtime action or new media claim occurred. Repository visual
obligations require later implemented desktop/mobile captures under the
post-review scoped verification package.

## Complete history and equivalence

Three final purposes on88ac:

1. `429d84cbd1d764ead4cf9e3c9748c048d9613653` — one final SDK input/provenance/cache update.
2. `ff61f4b1ffda10c8d6b563f2ee0a219c3fc57780` — generic UI, explanation/navigation, adapters, catalogs, tests and owning contracts.
3. `6b14ae5e1702ee8c137605d3512c123c9a24b582` — dated verification and historical captures.

The six-commit working series is preserved at
`dev/incident-ui-report-links-before-fold-nov18` →
`a9bf9f7f787856f752151a92a5396af498a56e0e`. Accepted b1fb remains at
`dev/incident-ui-before-report-links-nov18-b1fb37b0`; earlier8ce/d26/original refs
are unchanged. SDK updates were folded into one final stream; app/test and
evidence fixups were folded into their existing purposes. No unsupported old
selected-policy/callback display path is reintroduced. No new migration exists
in either the Nov18 delta or complete React series; no React migration was merged,
released, deployed or externally consumed.

[final-history-equivalence.json](final-history-equivalence.json) proves:
pre/post-fold tree equality at727af56a, byte-identical full binary patch,
all33 precommit paths equal final committed blobs, all31 final-check inputs match
(30 committed paths and one ignored narrow config), all prior refs unchanged
except the owned branch, all115 existing PNGs unchanged (including the eight feature captures), clean index/worktree,
and empty migration inventory. Both b1fb→final and six→three range-diffs are saved.
Contributor identity was the configured Jakub Skokan identity. No hook framework
or expected precommit hook is declared here; normal git commits/rebase ran without
hook bypass. Commit messages used files and native commit14771 joined0.

Independent final review is lead-owned, not yet performed for this successor.
The highest risk is HIGH because the complete series includes capability and
owner-scoped policy/history display and cross-project generated contracts. The
retained reviewer should assess all four applicable lanes, complete base→head
history, the33-path accepted-b1fb delta, and explicitly conclude consolidation and
no-migration lineage. This is a review handoff, not merge readiness.

## Remaining boundaries and handles

After independent review: only the affected scoped synthetic browser flows and
exact clean-head five-target Nix frontend/BFF/provenance/source/package checks,
as separately allocated by root. Six WASI cache warnings are not dismissed
without that actual build. No closure/toolchain-absence or live API/enforcement,
mail delivery, owner-transfer runtime, deployment or demo claim is made.
Existing b1fb/d26 packages, CI failure/success, demo and media remain literal;
this substantive source/SDK successor requires its own later package and demo
input allocation. No source is pushed and PR115 remains untouched in this package.

Utilities were fresh installed-policy Luna/low/full_access at catalog SHA
780db421a46b2a3bb6128dcc60b706de0753bd2a564c2e5f3c310344f3fce0bb.
nov18_final_resume ended native78842; nov18_final_completion completed both
commands inline; nov18_unrun_checks ended native45924. Its first wrong-cwd
identity refusal happened before checks and was resolved with the exact
trackingCwd. Parent controls68544/31859, inventory16144, format48543,
docs6983 and commits14771 are all joined. Prior source/adoption commands11373/
12737/49550/38460 were already terminal. No owned service, browser, observer,
command or uncertain native effect remains. Session stays open.

[evidence-hashes.json](evidence-hashes.json) binds94 raw logs/plans/results and
history/writing receipts. The stable
[session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
retains this packet. Owner2 remains available for concrete review findings.
