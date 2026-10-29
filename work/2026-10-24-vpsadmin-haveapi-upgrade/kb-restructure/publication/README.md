# API article changesets

These are complete Czech/English page revisions in publication order, starting
from the captured production originals. Each directory contains both pages,
its localized revision summaries and a diff against the preceding revision.
The final pages equal the canonical candidates: Czech step04 and English step03.
The previous three-step chain and cumulative manifests are preserved under
`../install-policy/prior/`; its staging receipts remain historical evidence.

1. **Remove haveapi-fs.** Delete the obsolete client listing and FUSE guide;
   preserve the following Ruby backup examples.
   [Czech diff](01-remove-fs/cs.diff), [English diff](01-remove-fs/en.diff).
2. **Put authentication and the main Ruby client first.** Keep authentication
   and scopes before CLI installation/use, identify Ruby as the main client,
   add a short Ruby read example, and keep the existing Ruby backup examples
   together. Move the other-client catalogue after this material.
   [Czech diff](02-main-ruby/cs.diff), [English diff](02-main-ruby/en.diff).
3. **Describe the other supported clients.** Replace the old catalogue with
   PHP, Python, JavaScript/TypeScript, Go, vpsAdmin TypeScript and Rust sections.
   Include version-independent installation, usage guidance and links without
   treating generated clients as the only options. Let npm install the runtime
   required by the TypeScript SDK's declared dependency; link maintained Python
   and Rust requirements. Do not first stage the superseded pinned wording.
   [Czech diff](03-other-clients/cs.diff), [English diff](03-other-clients/en.diff).
4. **Remove the obsolete header warning.** Remove the Czech-only HTTP500 and
   required-header speculation, preserving the protocol link. There is no
   corresponding English edit or no-op revision.
   [Czech diff](04-obsolete-header-note/cs.diff).

`content-chain.json` binds each predecessor and result by content SHA256.
It does not claim production revisions for changes that have not been published.
The original production guards are CS revision1783860648 and EN1777543182,
with hashes retained in `../../kb-original` and the existing source index.

## Review and publication

The selected g650 runtime's public wrappers bind provider
`/nix/store/d50zvmwmvdj0j35pwcmaarcwyq3fqpqj-vpsfree-dev-workspace-tools-0.1.0`.
Its `kb-release` supports stage/verify/promote, schemas1–5 and one write per
page ID in a manifest. There is no sequence command or changesets field.
`lib/kb_release.rb:127–151,438–459,526–565,616–646,881–890` binds both production
and staging to the same source/candidate and retains one latest pending digest.
That digest is not a queue. The earlier cumulative manifests each requested one
full-page write, so the three local editorial commits produced one combined
staging revision per language.

The ordinary public `kb-page save --wiki cz-staging|org-staging PAGE FILE
--summary TEXT --update` supports successive revisions of the same staging
page. It checks session ownership, authentication and edit ACL under the native
staging lock. Every staging mutation invalidates the pending release digest
(`bin/kb-page:252–287,616–636`; `lib/kb_stage.rb:116–125`). No reset, history
deletion, private-state edit or tooling change is needed.

After committed checks and independent review, compare fresh production
revision/content guards with `kb-original`, and preserve the current staged
source/revisions. Restore the captured baseline through ordinary staging saves,
using the explicit staging-only summaries below, then save steps01,02,03 in both
languages and step04 in Czech only. Before each write verify ownership/auth/ACL
and the exact staged predecessor. Read back exact source, stable revision,
localized summary/history and bounded rendered output after every write; stop
on a mismatch. Preserve earlier history and leave the final candidates displayed.

- CS baseline: `Obnovení výchozího stavu pro kontrolu jednotlivých změn`
- EN baseline: `Restore the review baseline for separate changesets`

Use each step's `release-changes.yml` for the exact revision summaries.
`content-chain.json` binds the seven actual content changes; the baseline
restoration is review setup, not a production changeset. Final pending state is
honestly null after public page saves. The root aggregate schema5 manifests
remain canonical preview/check inputs, not an ordered production release.
No production write is authorized by this staging plan.

After explicit approval of the exact changesets, use the normal guarded release
workflow for each step and language: prepare its schema-5 manifest, stage,
verify the source/rendered page and localized summary, then promote. Save the
actual new production revision/content with a consistent page-info read around
the content read. Preserve each source snapshot, and generate the next step's
guards from those observed facts. Do not use staging revisions, predicted
timestamps or private pending-state edits. If staging displays a later candidate,
restore the selected reviewed snapshot with its exact summary through public
`kb-page save`, then register it with normal `kb-release stage` and verify it
before promotion. Serialize each language's pending manifest and promotion;
staging another manifest replaces the global pending digest. There is no English
step04. Production approval must cover the exact ordered changesets.

The user-facing writing was prepared by the lead. This package changes KB text
only. Existing authentication/CLI examples and API7 values are retained;
avoidable install pins are removed under the accepted `design.md` installation
and header brief. It does not alter an API, schema, OAuth configuration or
deployment.
