# Final review R1 reconciliation

The final independent whole-branch review found one Important issue: attachment
prevalidation could persist a pending claim when its transaction also saved
unrelated compaction. Lead accepts and fixes R1; no finding is waived.

Retained implementer0 (saved GPT-6.1 Sol/xhigh/workspace_write) changed only the
upload store and its two owning preparation test files. Validation runs the same
helper on an isolated catalog value with copied Files and Submissions maps.
The helper reads Scopes and existing slices without mutation. Actual claims
continue to run on the live catalog under its lock after the durable intent.
Compaction, claim replay, confirmation and pending retention remain intact.

The lead inspected the full diff, helper mutations and the existing pre-intent
directory-sync failure seam. Both new tests executed against the original
production store through a Go overlay and failed at the intended assertions:
premature ownership persisted, and failed intent left orphan ownership. Original
wrapper exit1; both leaves failed in under0.1s. The corrected focused race check
ran 29 top-level groups/46 total pass events, no failure/skip, exit0. Upload
package2.984s; web5.416s. It covered upload claims, all session preparations and
catalog compaction. Private evidence is retained in
`/tmp/automatic-session-slugs-prevalidation-{original,corrected}.{jsonl,exit}`.

Gofmt and diff whitespace passed. The source correction/upload regression are
folded into owning uploads89fb1b07; the portal regression is folded into owning
preparationea5b2e98. Final runtime45d4f13ab14a2dd7d19ea564dc1d364c5ac155c6 has
exactly those three changed paths versus reviewed660; tree equality was checked
through autosquash. Remaining runtime units are patch-equivalent and consumed
runtime4ef298b3 remains an exact ancestor. Backups retain reviewed660/628/32ca.
No fixup commits, new migration, API, catalog field or design boundary is added.

This is direct remediation verification under mandatory-change-review step9;
it needs no redundant reviewer turn. The completed complete-history and
migration conclusions remain valid, with refreshed actual comparisons.
Provider32775fa is unchanged, so its full native protocol proof carries forward
for the same native helper. This does not imply package or managed-service proof.

Runtime45 is published by SSH exact lease against660. Extension67c9a60b802537bbb7154959405b67f168f85397
and workspace8876efbffbb1312c782687226deeac3e7f053749 are each amended owning pin
units and published against628/32ca. Generated locks change only the new runtime
and extension revisions; provider, vendor hash and all other inputs are retained.
Consumed extension399c3302 and shared master5c ancestry are exact. The refreshed
inventory contains all final heads/series/diffs and migration disposition.

Final provider CI37182636158 passed. New exact runtime CI37184684052 and extension
CI37184744414 were in progress when handed to the package watcher. All older
same-branch runs were completed; no superseded active run required cancellation.
Package/resource/managed VM/deployment/live gates remain separate and pending.
