# Affected final review: SDK npm archive path

No Blocking, Important or Advisory findings at `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`. The affected source-review gate passes; full CI and explicit recovery/integration approvals remain.

## Correctness, scope and risk

The complete incremental diff against integrated main `4689d00ca4acf0cc26a3507fc3c238b687b53475` is one workflow file, +2/-1: publish `./release/*.tgz` and explain npm's GitHub-shorthand parsing. This is the smallest conventional correction to the observed failure. It adds no helper, framework, test asserting a command literal, credential fallback or account-setting change.

The failed canonical log shows successful preflight/receipt verification followed by Git lookup of `ssh://git@github.com/release/vpsadmin-typescript-client-0.1.1.tgz.git`. Static inspection of the installed pinned npm 11.19.0 confirms:
- npm-package-arg recognizes explicit relative file paths before hosted-Git shorthand.
- publish resolves the manifest before its OIDC call and registry upload.
- the dry-run branch suppresses upload.

The leading `./` therefore directs npm to the local retained tarball. The preceding receipt verifier accepts the same expanded pathname through filesystem/tar APIs; the verification/publication identity boundary remains intact. The workflow still uses the protected publish job, immutable artifact ID, preflight, original receipt, scripts disabled, public access and explicit npm registry. Imported actions, runtime/schema/generator pins, metadata, version and authorization settings are unchanged.

Saved meaningful verification ran the actual corrected command with --dry-run/--json under pinned npm/Node and isolated empty authentication/config state. I inspected its successful package-keyed output: 0.1.1, 1,358 files and exact original SHA512 integrity. The retained original tarball's SHA256 still equals its receipt: `9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8`. Six existing release tests and invariance checks are recorded passing. I ran no checks/builds.

This evidence establishes local archive preparation, not npm OIDC acceptance. The canonical failure occurred before authentication/upload; the saved duplicate-job record has an empty publish-step list after rejection and no pending deployment. These support the recorded no-upload reconciliation without treating a registry 404 alone as proof.

## Complete history, boundaries and migration conclusion

Canonical repository/target: vpsfreecz/vpsadmin-typescript-client / main. Historical base `149c72f11acef67224a47ed77711a3abb805fbd4`. Inspected complete ordered series and cumulative diff (8 files, +83/-19):

1. `38a25ad88d0bf3018670184620cf69cdb71e92e7`: actual published 0.1.0 source.
2. `4689d00ca4acf0cc26a3507fc3c238b687b53475`: integrated 0.1.1 metadata and accepted failed-tag artifact source, not a public npm version.
3. `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`: narrow workflow path correction.

The retained origin/main equals 4689d00 and is the incremental merge base; the feature tree is clean and one commit ahead. Local v0.1.1 remains annotated object `cb914823d2e74e9565e56a1af770b0d129fd0876`, peeling to 4689d00.

Explicit whole-history conclusion: **no obsolete unmerged approaches or unnecessary fix chains remain**. Keep exact published 38a and already integrated 4689; the new correction properly follows protected main history rather than rewriting it. The two package/lock/digest updates retain the actual 0.1.0 publication boundary and later integrated 0.1.1 candidate. **No redundant repeated dependency/channel/input/generated streams** require consolidation. **No migrations** or transitional migration lineage exist.

Reuse the unchanged source/configuration reviews. This workflow-only repair introduces no package API, protocol, persisted-state, schema or mixed-version change. Its comment is sufficient durable rationale; recovery details appropriately remain in session records.

## Remaining gates and reviewer identity

Proceed with ordinary feature push/full CI. The new main fix needs explicit integration approval; the exact failed SDK tag replacement needs its own user authorization or a new-version recovery decision. Prior HaveAPI recovery direction does not authorize this SDK tag rewrite. An unchanged old-tag job cannot pick up the new workflow from main. Preserve the original tag, run, receipt and artifact; the original receipt remains bound to 4689d00 and must not be relabeled as a 60a receipt. Recovery must honor the retained-artifact contract and verify actual registry identity/integrity/provenance.

Session binding/current/environment and live retained reviewer0 identity matched: thread 01a17e59-3823-76f0-9764-5525072525a2, gpt-6.1-sol/xhigh/read_only, unchanged settings and no fallback. Read mandatory-change-review plus general/architecture/scope/risk references, packet, appended design, failure/recovery records, actual workflow and relevant pinned npm source; reused unchanged applicable guidance. Remained read-only: no tests, builds, writes, nested agents, claims, source/ref mutation or publication. Report returned for the lead to save as sdk-path-review.md.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-prepare-client-releases/
