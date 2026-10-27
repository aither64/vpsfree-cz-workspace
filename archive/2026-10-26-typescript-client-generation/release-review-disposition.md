# Release review disposition

The original report is preserved verbatim in [release-workflow-review.md](release-workflow-review.md). Reviewer0, using its retained gpt-6.1-sol/xhigh/read_only settings, reviewed HaveAPI `f02eca2e` and client `179a89c7` in all four lanes. The complete 5/2/1 histories contain no obsolete approaches, repeated pin streams or migrations.

Both Important findings are closed:

- R1: the checker removes exactly one terminal LF from each tar listing before splitting. It retains interior empty entries and the type, path and duplicate refusals. A real ordinary tar fixture reaches package-completeness validation; a real symlink archive is refused. The complete valid archive subsequently passed the extracted ESM, strict types and executor consumer.
- R2: the build job refuses tag attempts greater than one before checkout, dependency preparation, building or packing. Tests execute the actual workflow shell: first tag attempt passes, repeated tag attempts fail, and repeated branch builds pass. Publish-only retries retain the original `needs.build` artifact ID and fail if the artifact is missing. The recovery guide states this contract.

The lead inspected the four-path correction, applied the prose pass, accepted six focused regressions and reran actionlint successfully through the pinned Nix environment. These are the reviewer's requested narrow corrections under mandatory-change-review step 9; no new design or expanded contract requires another review.

Owner3 folded the fixes into the release commit. Final client head is `6fc0955fc078f3af3ef69adaaec30d5038eff70d`, tree `e817f5a05ac22c971e6c85f8b8e42e0952834036`. Its initial package commit `95eeff73` and producer `f02eca2e` are unchanged. Complete tree comparison proves exactly four changed paths relative to the reviewed release commit: 47 insertions, three deletions. Normal Git amendment preserved the informative message, with no hook bypass. Index and worktree were clean. Machine proof: `/tmp/2026-10-26-typescript-client-generation-release-remediation-proof.json`.

A fresh retained-policy Luna/low watcher ran both postreview commands once at these exact heads. Extracted TypeScript/shared Ruby gems passed generation, check mode, source ownership and a strict consumer using the published runtime in 4.2 seconds. The full retained npm archive passed ESM, strict types, executor and receipt checks in 10 seconds. No repack occurred after the receipt. Both worktrees remained clean.

Artifact SHA256 values:

- Shared Ruby gem: `d51775d35dc1d73159f52061e4cdf78160515069ecb77cf6f66aaf22badbb9d3`.
- TypeScript generator gem: `31f7b562cf75c36df3b0968e1c883bdc3746a17ad286a0c46f253df79afd6063`.
- npm archive: `b0825e0a86ff04fdbe461e3463826accf308d2d5d0111ddfe916fca09485a691`.

Status and native evidence use `/tmp/2026-10-26-typescript-client-generation-release-postreview*`. The watcher omitted the requested compact log, so the lead reconstructed it from its retained command output without rerunning either check. An earlier attempt to invoke actionlint through an old store path performed no check or mutation; the subsequent pinned Nix command passed. Original artifacts remain in `/tmp/haveapi-typescript-release-smoke-QoRLNF` and `/tmp/2026-10-26-typescript-client-generation-npm-retained.4EINxL`.

No version, tag, release, registry configuration/upload, default integration, deployment or lifecycle action was authorized or performed.

## Final CI version-preparation correction

HaveAPI release run40403389950 exposed an inherited Bundler4 `BUNDLE_LOCKFILE`: overriding only `BUNDLE_GEMFILE` still targeted the parent root lockfile. The existing test correctly required the TypeScript component lock to move to999.0.0; its expectation was not weakened.

Owner0 changed only the Makefile's TypeScript local-lock command and the existing version test. The command now clears the same inherited Ruby/Bundler state as the Rust command. The real disposable version-bump regression explicitly supplies a parent `BUNDLE_LOCKFILE`, retains exact version transitions/external graph checks and verifies original locks remain unchanged. Full `make release-test` passed213Ruby examples and6Python tests with offline prepared inputs; scoped lint/dryrun/whitespace passed.

The lead inspected these two paths as a narrow correction to the reviewed version-preparation contract. No new design, public contract, generator digest, shared source, VERSION, runtime or package content changed. Prior extracted artifact acceptance remains tied to unchanged actual inputs; no repeat is required. The fix was folded into the owning fifth release commit18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875, tree3615b0b415e5e245734d29b68c653ac0b158c8f4, parentexacte6d4f797. A mechanical exact producer revision refresh follows in the initial SDK commit. No obsolete fixup/pin stream will remain. Originalf02eca2review/failedCI and successful14caseperformance measurement remain provenance; final-head CI is separate.

The lead inspected the complete five-commit series after amendment. Compared with reviewedf02eca2, only Makefile and utils/release/spec/release_spec.rb differ. TypeScript subtree386017e27619a6e281f53647338b28e375050a72, Ruby subtree2f688d978db35546a19d6f5d0364ae9ca7dc74ac and VERSIONblobc25c8e5b74165cb091da0d733df57a19152ded93 are identical. No migrations or obsolete fixup/pin stream.

## Mechanical downstream refresh and final publication

The final client range is genuine empty root `6c67b3c6e10e4096f6717345026371a89691f62a..2dab582881c4af8d8b3f932d9f2308e133d8d925`. Its initial package is `34fefcec9ea382a58a019b4acc9e400df4b9abda`; the second commit retains the release patch. Relative to the accepted range ending `6fc0955`, only `tools/generator.json` changes, substituting the exact producer revision f02eca2e with18b45aed. Digest, shared identity, VERSION, manifest, tooling hashes, schema, provenance, locks and all674TypeScript modules are unchanged. Exact-source regeneration check passed without writes.

The lead independently reconstructed both expected Git trees entirely in memory from the old commits, replacing only the one pin blob and recomputing the affected tool/root trees. They match actual initial tree `686a5a270a99c41252224e165578c5ebb2b08ccf` and final tree `0cd0ced80ec32b74cf9797a680eb76a4d0e57abf`. Range-diff shows exactly the revision line in the initial commit and equality for the release commit. Messages and release patch bytes are unchanged. No migrations or intermediate pin/fixup stream remain. Owner proof: `/tmp/2026-10-26-typescript-client-generation-client-ci-repin-proof.json`.

Both corrected feature heads were published with exact leases and fresh SSH feature/default/clean-tracking proof. HaveAPI/master remains029f79b; client/main remains the genuine empty root. No other refs changed. Final CI observes HaveAPI18b45aed and client2dab582; IDs/results are in ci-results.md. No actual release, version/tag, registry setting/upload, merge, deployment or lifecycle action occurred.
