# Three API article changesets

These are complete Czech/English page revisions in publication order, starting
from the captured production originals. Each directory contains both pages,
its localized revision summaries and a diff against the preceding revision.
The final pages equal the rewritten cumulative staging candidates.

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
   Include installation, usage guidance and links without treating generated
   clients as the only options. Preserve the separate TypeScript client/runtime
   pairing.
   [Czech diff](03-other-clients/cs.diff), [English diff](03-other-clients/en.diff).

`content-chain.json` binds each predecessor and result by content SHA256.
It does not claim production revisions for changes that have not been published.
The original production guards are CS revision1783860648 and EN1777543182,
with hashes retained in `../../kb-original` and the existing source index.

## Review and publication

The installed release tool supports one full-page write per page and one
pending review digest. It checks both the actual production baseline and
staging predecessor. It cannot stage these three different revisions in a row
against unchanged production. The ordinary cumulative staging preview therefore
shows the final page; the per-step diffs above show the intended publication
history. No production write is authorized yet.

After explicit approval of the exact changesets, use the normal guarded release
workflow for each step and language: prepare its schema-5 manifest, stage,
verify the source/rendered page and localized summary, then promote. Save the
actual new production revision/content with a consistent page-info read around
the content read. Preserve each source snapshot, and generate the next step's
guards from those observed facts. Do not use staging revisions, predicted
timestamps or private pending-state edits. Restore the exact pending manifest
through normal staging if required before promotion.

The user-facing writing was prepared by the lead. This package changes KB text
only. Existing authentication/CLI examples and supported package identities are
retained; it does not alter an API, schema, OAuth configuration or deployment.
