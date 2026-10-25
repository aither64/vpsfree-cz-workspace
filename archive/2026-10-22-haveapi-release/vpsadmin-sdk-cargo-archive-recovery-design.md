# Native Cargo archive retention and 0.1.0 recovery

Architect0, 2026-10-24; assignment `fbd60a09-e5e3-423d-915f-2846a57be1d6`.
Proposed implementation brief for lead acceptance. Owner3 owns SDK source/Git;
reviewer0 independently reviews the committed fix. Architect actions were source,
documentation and retained-evidence reads only, plus official Cargo source GETs.
No Cargo/setup/compiler/upload/tag/registry operation was run.

## Proven failure and native contract

Failed run `40123807556`, attempt 1, source
`63b87e9a1b92727a3e5c5513898e183ab0be898a`, tree
`90dbaba680a47a70f5bd216082dfbc1fa6e201ca`; immutable annotated `v0.1.0` object
`c4f258b77dadf8057630c371152a607151b1c3e1`. The retained
[parent assessment](vpsadmin-sdk-publication-40123807556-attempt1/parent-assessment.json)
hash is `49569ba4a83cb9638de65c8120b583229e79a9b890d7c8b6c7fb8b1d2076979d`.
The [publisher log](vpsadmin-sdk-publication-40123807556-attempt1/publisher-job-120961659700.log)
hash is `19a452b3f8d1b586d3823d72c1a73b66d2dbad8b6b564db44605f8b2d14bb164`.
Its lines 841–845 show 697 files packaged; 1076–1078 show successful compilation
and the expected dry-run upload refusal. Line 1090 records Python's missing
`target/package/vpsadmin-client-0.1.0.crate`. Authentication/bootstrap and native
upload steps were skipped. Candidate and actual-publish artifacts are absent;
the separate CI package is not a substitute for either.

The selected binary reports `cargo 1.98.0 (797e8a9bc 2026-08-05)`; its Nix
package label is cargo-1.98.1. Official source resolves the reported revision to
`797e8a9bca276c1c9f9f738d2a20f484fa4eea9d`. Read-only source files, HTTP outcomes,
timestamps and SHA-256 hashes are retained in
[source evidence](sdk-cargo-archive-recovery-source/sources.json).

- [`cargo_package::create_package`](https://github.com/rust-lang/cargo/blob/797e8a9bca276c1c9f9f738d2a20f484fa4eea9d/src/cargo/ops/cargo_package/mod.rs#L166)
  creates **`<build_dir>/package/tmp-crate/<name>-<version>.crate`**, truncates
  it and writes the native archive under a file lock.
- [`package()`](https://github.com/rust-lang/cargo/blob/797e8a9bca276c1c9f9f738d2a20f484fa4eea9d/src/cargo/ops/cargo_package/mod.rs#L219)
  copies that archive to `<target_dir>/package/<name>-<version>.crate` after
  verification. This is the standalone `cargo package` path.
- [`publish()`](https://github.com/rust-lang/cargo/blob/797e8a9bca276c1c9f9f738d2a20f484fa4eea9d/src/cargo/ops/registry/publish.rs#L162)
  instead calls `package_with_dep_graph`, which returns the original scratch
  file without this copy. Publication hashes that same file and passes it to
  `registry.publish`. Dry run uses the same creation path and stops before upload.
- [`FileLock::drop`](https://github.com/rust-lang/cargo/blob/797e8a9bca276c1c9f9f738d2a20f484fa4eea9d/src/cargo/util/flock.rs#L134)
  unlocks/closes; it does not unlink the file. The inspected package/publish
  paths do not delete it on ordinary success or error. The failed hosted runner's
  actual directory cannot now be inspected; lifetime is established from exact
  implementation and still needs the targeted native check below.
- Cargo 1.98 documents `build.build-dir` / `CARGO_BUILD_BUILD_DIR` separately
  from the target directory. Set it explicitly through supported Cargo config;
  set `--target-dir` explicitly too. The **scratch subpath is an implementation
  detail**, not a promised CLI output. Confine that dependency to one helper
  guarded by the selected Cargo version/commit. No publish output/archive flag
  or machine-readable archive path is exposed by this revision's CLI.

The defect is our workflow's use of the standalone-package output contract
after publish. Neither compiler failure nor expired/deleted artifacts caused
the observed Python error. Do not describe native dry-run as an upload attempt.

## Small fix: owner3 boundaries

Edit only `.github/workflows/release.yml`, new `tools/publish-crate`, new
`tools/test-publish-crate.py`, and the relevant paragraph in
`docs/development.md`. Add the focused helper tests to the existing CI helper
check in `.github/workflows/ci.yml` if needed. Preserve all action/tool pins,
`Cargo.toml`, lock resolution/transfer, generator/schema/provenance and all 686
generated Rust files. No new publication protocol or generalized path discovery.

The small Python helper replaces the two inline archive-handling blocks and
wraps the native command synchronously. Expose `candidate` and `publish` modes
with explicit expected source, lock SHA, owned work directory and evidence
directory. Example interface, finalized by owner3 without changing the contract:

```sh
nix develop --command tools/publish-crate candidate \
  --source "$GITHUB_SHA" --lock-sha256 "$LOCK_SHA256" \
  --work-dir "$RUNNER_TEMP/native-crate" \
  --evidence-dir "$RUNNER_TEMP/crate-candidate"
# Later, only at the already protected native publication step:
nix develop --command tools/publish-crate publish \
  --source "$GITHUB_SHA" --lock-sha256 "$LOCK_SHA256" \
  --work-dir "$RUNNER_TEMP/native-crate" \
  --candidate-dir "$RUNNER_TEMP/crate-candidate" \
  --evidence-dir "$RUNNER_TEMP/crate-publish"
```

Contract:

1. Require clean exact source, package `vpsadmin-client` / declared version,
   exact restored lock, and selected Cargo identity before launching. Do not
   accept unknown Cargo versions with guessed paths. Candidate rejects a
   supplied publish token; no credentials are needed for that mode. Never log
   environment values, tokens or credential files. Use subprocess argument
   arrays, not shell interpolation.
2. Select absolute `build.build-dir` and `--target-dir` within the owned work
   directory. The scratch filename is derived only from validated package
   identity. Require it absent before **each** invocation; reject stale files
   and symlinks. Do not search/glob fallback directories, or adopt the CI package.
   Keep compile outputs for the subsequent native publish; the exact scratch
   archive is moved into evidence after candidate, freeing that pathname.
   Refuse existing evidence destinations instead of overwriting earlier attempts.
3. Run ordinary `cargo publish --dry-run --locked` for candidate and ordinary
   `cargo publish --locked` for publication, preserving native verification.
   Supply explicit Cargo config/target arguments on both. No `--no-verify`,
   repack, custom uploader or synthetic archive. Remain synchronous; no polling
   watcher races Cargo while it writes the scratch file.
4. In a `finally`-style post-child path, preserve the exact scratch archive if
   present **before** asserting validity. Record native exit status, presence,
   size/hash, command/tool/source/lock identity and validation result, even on
   error. Preserve malformed/partial bytes as failed evidence, not a candidate.
   If failure occurs before archive creation, record absence honestly and fail.
   Keep child failure visible even if archive retention or validation also fails.
   Hard runner loss/cancellation cannot guarantee artifact upload; record that
   limit instead of promising evidence that did not survive.
5. Successful candidate retains existing strict package checks: safe unique
   members, identity, normalized dependency restrictions, original/normalized
   manifest, clean exact VCS source, actual packaged lock and runtime hashes,
   and equality of packaged Rust sources to checkout. Extend only where needed
   to reject malformed/symlink members safely. Root and packaged lock hashes
   are separate facts; Cargo normalizes the package lock. Do not relax any
   accepted oracle or claim they must be byte-identical without evidence.
6. Before publish, bind the candidate to exact source/tool/root lock and ensure
   these remain unchanged afterward. Preserve the newly produced native archive
   separately on success or failure; compare its SHA-256 with the candidate.
   A retained archive from a failed child is only evidence of native-produced
   bytes, **not proof an upload occurred**. A mismatch or missing archive fails
   visibly without replacing candidate bytes. Candidate capture and actual
   capture use the same helper and scratch contract.
7. Upload candidate evidence after successful candidate validation, before
   authentication. An `always()` failure-evidence upload must also retain a
   failed candidate report if the helper started. Similarly upload actual
   publish evidence whenever a native publish mode was attempted, irrespective
   of its status. Do not manufacture an actual-publish archive when the step
   was skipped. Keep existing bootstrap/OIDC conditions, tag recheck and protected
   environment. The token exists only in the native publication step.

Public verifier1 compares registry version metadata and downloaded original
archive with the **actual native publish** SHA/content and retained candidate.
Cargo source demonstrates that this scratch file is the stream native upload
uses. The later public checksum proves acceptance of those bytes. Do not use
ordinary CI package equality as a replacement for that chain.

## Focused verification

Quick, credential-free helper tests cover success capture, absent/stale scratch,
wrong source/tool/lock, symlink or malformed archive, child failure with present
or missing archive, capture error, candidate/actual mismatch, and preservation
of original child failure. Synthetic fixtures/stubbed subprocesses test helper
logic only; label them as such. Add shell/Python/workflow syntax checks and
source/686-file/schema/pin equality proof. No regeneration or compiler campaign
is required for these unchanged files.

Commit the final intended helper/workflow/docs delta before reviewer0's affected
final review. Supply complete prior/new range, retained tag/run lineage, prior
review and no migrations. The tagged failing commit is a retained public source
boundary, not permission to rewrite it.

After affected review, owner3/fresh utility executes **one actual candidate-mode
dry run of this SDK**, at the committed fix head, using its selected pinned Nix
Cargo 1.98 and the exact failed run's retained local Cargo lock:
artifact `12571947738`, SHA-256
`e75582cba0ade6552f3dfacce0689d0ed2f0cb149591282503ca0da5dfdae323`.
Bind the actual source path/HEAD/tree, complete native/tool inputs and lock;
use a new owned work/evidence directory and no registry token or local login.
Use prepared qualified dependency caches without changing graph or constraints.
Native dry-run read-only registry metadata needed by Cargo is within that
explicit later check, not this investigation. Preserve actual archive/hash,
697-member inventory where unchanged, VCS/source/runtime/lock validation and
exit 0. This proves the selected scratch path survives the real command. It
does not prove credentials or publication. No toy crate stands in for the SDK.

Reuse previous async/blocking/MSRV/regeneration results only with explicit
unchanged application source, dependency graph and native/tool identity proofs.
No duplicate local full matrix. Retain ordinary feature CI if automatically
triggered; the eventual normal release workflow's required verification remains.
Any concrete input drift or new failure reopens only affected checks/review.

## Public-tag recovery decision (lead-owned, not yet authorized)

Current instructions in `docs/development.md`, **Publishing from GitHub Actions**,
require dispatch at `v<Cargo.toml package.version>`, source/tag equality and the
protected environment; the final recovery paragraph says **"Never move a release
tag or overwrite a published version."** The current workflow enforces exact
`refs/tags/v0.1.0`. That tag points to the faulty workflow. Rerunning it uses the
same workflow; pushing a feature fix or merging main cannot change its contents.
The tag-only environment also rules out an ordinary feature-branch dispatch.

| Route | Consequence / required decision |
| --- | --- |
| Rerun unchanged v0.1.0 | Repeats deterministic path error; not viable. |
| Corrected feature head, replace v0.1.0 | Smallest normal-workflow route to package 0.1.0, but needs **explicit user authorization for this exact tag movement and the quoted instruction exception**, after fix/review/native validation. Preserve old annotated object, commit, remote observations and failed run; never imply they were the new tag. This is the recommended proposal if 0.1.0 remains required. No tag operation is currently granted. |
| Keep tag; one-off native publication of original63b87e9 | Technically Cargo can publish that version using the reviewed helper outside its old source. However it needs an explicit repository publication-procedure exception and a concrete credential/protected execution route; the existing GitHub workflow cannot run corrected code for that tag. Do not invent a workflow/source split, bypass protection or expose a bootstrap token to make this look ordinary. Higher operational cost; not the default recommendation. |
| Preserve failed v0.1.0; prepare a new version/tag | Follows immutable-tag recovery, but changes the user-selected version and requires an explicit version decision. Not an automatic 0.1.1 bump. |

Source repair, quick checks, committed review and the credential-free actual
dry-run can proceed before that public-tag choice. Lead presents the concrete
reviewed result and exact necessary exception; architect does not ask the user
or treat silence as approval. No SDK main/default integration is needed for
normal feature-tag dispatch and none is authorized. Any future upload attempt
requires fresh exact tag/source proof and bounded public registry state check
by its assigned owner. No registry probe was duplicated in this investigation.

All generated/API/runtime/schema semantics, dependency constraints, MSRV and
tool pins remain unchanged. No server migration/deployment or rollback ordering
arises. Preserve original run ZIP/hash, absent-candidate fact and protected
approval receipt; do not relabel an earlier CI archive as native publication
evidence. An uncertain future upload must be diagnosed against its original
archive and registry checksum before retrying. Session remains open.
