# vpsAdmin Rust SDK regeneration and 0.1.0 release

Architect0; assignment `6a328369-d4bd-4d6d-8890-314020adb64a`; 2026-10-24.
User authorized regeneration and publication, provisionally 0.1.0. This brief
does not grant default-branch integration. No deployment, API capture, credential
inspection, cleanup or session lifecycle action is included.

## Observed source and availability

- Owned root: `worktrees/2026-10-22-haveapi-release/vpsadmin-rust-client`, branch
  `2026-10-22-haveapi-release-regenerate-vpsadmin-client`, clean at
  `ff876abe17e3301da62c1b6afbda055ec89db9d2`, tree
  `322fa86ba290b5936a327c21371c94f96f86b249`. Official GitHub main GET at
  17:32 UTC identifies this same commit. Canonical bare local `main` and
  `origin/main` are stale; owner3 must reconcile through an ordinary fresh fetch.
  Preserve all previously merged commits/feature refs. Prefer a new registered
  `vpsadmin-rust-client-0-1-0` worktree and
  `2026-10-24-vpsadmin-rust-client-0.1.0` branch from that verified remote baseline.
- Crates API returned 404 / `crate vpsadmin-client does not exist`; exact
  `v0.1.0` Git tag and GitHub Release also returned 404. These support using
  0.1.0, already present in `Cargo.toml` and `generator.toml`; they prove neither
  name ownership nor permission to publish. Recheck before the actual upload.
- The release-environment endpoint returned 404. Existence/protections are
  **not established**; credential availability was not inspected. Preserve this
  uncertainty rather than claiming configuration is absent or usable.
- Full responses, UTC times and hashes are in
  [official observations](vpsadmin-client-0.1.0-release-investigation/observations.json).
  Source instructions, README, development guide, both workflows, regeneration
  and provenance helpers were read. No hook framework is declared.

## Fixed generator and schema inputs

Use HaveAPI release `v0.30.1`, exact source
`1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`. Original tagged manifest is
`release-0-30-1-successor-tagged-artifact-download/retained/release-manifest.json`,
SHA-256 `54816d85c307930d83d900b3329aa5a4ff5a55aafa06549839d95b47628a7c98`.
The retained `haveapi-rust-client-0.30.1.gem` hashes to
`226b1831bbcf8ed5bfc5ef58e12d3764b63df51304e610cbc95b6d6fb1fa18ca`, matching that
manifest. Its embedded `Gemfile.lock` equals the manifest's exact
`dependency_locks["clients/rust/Gemfile.lock"]` text and hashes to
`f35d5ad277861f14917651d564eb782a8c39764c48106c52d8e48b360bd58e43`.
Bundler is 4.0.23; Fiddle 1.1.8 and Tomlrb 2.0.5 remain in this actual graph.
Do not fabricate, commit or freshly resolve a different generator lock.

The released generator source digest, computed using its path/NUL/bytes/NUL
algorithm over `lib/**/*.rb` and `template/**/*`, is
`9b60df3bd861d20d8154888e76dd2679885c0eaf0dedd940c235e07075bbefdc`.
Templates and all eight runtime sources are unchanged from 090a. Model extraction
and documentation-profile changes alter generator source identity; actual
regeneration must establish output equality rather than infer it from this fact.

Preserve `schema/api-7.0.json` SHA-256
`70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d`, the complete
inventory and capture metadata: public unauthenticated API 7.0, 152 resources,
524 actions and 8,720 parameters. Preserve generator options, crate identity,
edition 2024, MSRV 1.95, rustfmt 1.9.0 and pinned SDK nixpkgs
`fe13242281a67641c0102cdb1087f0ebe586c7df`. Use its Ruby 3.3/libffi environment;
HaveAPI's Ruby 3.4 native bundle is not interchangeable.

## Owner3 implementation boundaries

One owner handles SDK source, dependency setup, Git and execution; lead routes
independent review and long watchers. Architect edits only this brief/evidence.

1. **Generator provenance/preparation:** update `schema/provenance.json` to
   released version/source/digests. Add only the release-manifest URL and exact
   SHA needed to replay its Ruby lock, keeping existing capture/options intact.
   Add a narrow `tools/prepare-generator-lock` helper, used by regeneration CI
   and documented setup. It accepts an explicitly downloaded local release
   manifest, verifies its recorded hash, source/version/tag and the Rust lock
   digest, verifies `HAVEAPI_SOURCE` is the clean exact recorded source, and
   restores only its ignored `clients/rust/Gemfile.lock`. Existing identical
   bytes are idempotent; conflicting files, symlinks, source or hashes fail.
   It does not resolve dependencies or fetch implicitly. Obtain the manifest
   from the fixed official `v0.30.1` release asset; an owned dependency checkout
   under `target/` avoids changing original HaveAPI worktrees. Then use native
   Bundler 4.0.23 with `BUNDLE_FROZEN=true`, the recorded lock and SDK Ruby 3.3
   in an isolated owned bundle. Normal dependency installation may fetch exact
   locked official gems; preserve checksums and the full graph. Update
   `tools/check-provenance` only for the new recorded release fields and version
   consistency; do not weaken current checks. `tools/regenerate` stays on its
   supported source/lock seam unless a concrete change is required.
2. **Library lock and CI/release input preparation:** untrack `Cargo.lock` and
   ignore `/Cargo.lock`, preserving an actual local copy for verification.
   Retain `flake.lock`; change no Cargo dependency constraints or MSRV.
   Native `cargo generate-lockfile` is the clean-checkout preparation step;
   subsequent fetch/test/doc/package/publish commands use `--locked`.
   Existing local locks may be reused explicitly, with hashes recorded.
   In `.github/workflows/ci.yml`, resolve once in a preparation job and retain
   the actual lock as a run-bound artifact; all compile/MSRV/package jobs consume
   that exact lock. Expose its artifact ID and SHA through `workflow_call` so
   `.github/workflows/release.yml` restores the verified graph before publishing.
   Do not independently re-resolve in the publish job. Regeneration CI checks out
   exact 1c3 and restores the released Ruby lock before frozen installation and
   `tools/regenerate --check`. Verify current official action refs before choosing
   newly imported/updated action pins. Add only focused input-integrity tests
   for the helper, including wrong manifest/source/lock and existing-file conflict.
3. **Generated output:** run the actual released generator with saved schema
   and pinned formatter. Only it writes `src/generated/**`. Expected difference
   from ff876abe is ownership-manifest provenance: all 686 recorded generated
   file bytes, including runtime/public names/routes, should remain identical.
   Any Rust byte change is a finding to explain before acceptance, not permission
   to normalize or hand-edit it. Keep this generated refresh in its own commit.
4. **Documentation/release metadata:** update `docs/development.md`, the narrow
   lock rule in `AGENTS.md`, and `CHANGELOG.md` for released-generator provenance
   and local locks. README source links currently name an old development branch;
   make relevant release documentation/example/license links stable at the
   intended `v0.1.0` tag. Lead owns final user-facing wording. `Cargo.toml` may
   keep its package `Cargo.lock` include: Git tracking and shipping a resolved
   build input differ. Cargo normally includes a lock in `.crate` archives;
   consumers resolve library dependencies using their own application lock.
   Inspect actual package contents; do not introduce `--exclude-lockfile` or
   change package identity/version merely to remove tracking.

Suggested logical commits: generator provenance/helper/docs; library lock
policy and coherent CI/publication preparation; generated manifest/output;
release prose where a distinct final edit is needed. Consolidate superseded
unpublished attempts, without rewriting ff876abe or earlier merged history.

## Acceptance and release sequence

Before commits: source/schema/inventory and 686-file equality checks, shell
syntax, helper negative cases, provenance inspection, `cargo fmt --all -- --check`,
and actual `tools/regenerate` followed by `tools/regenerate --check` under the
qualified frozen generator bundle. Record real lock and tool identities.
Then complete the committed whole-branch independent final review, including
workflow input transfer, secret boundaries, history and no migrations.

After review, a fresh watcher runs the bounded maintained matrix:
`cargo test --locked --all-targets` with default and blocking features;
the same two modes on Rust 1.95; `cargo doc --locked --all-features --no-deps`;
and native package/publish dry-run verification. Inspect package inventory and
extracted manifest/source/runtime, absence of HaveAPI path/Git dependencies,
exact package version, VCS commit and lock. Retain ordinary feature CI; use its
exact-head results rather than dispatch duplicate matrices. The release workflow
still calls its mandatory verification. No real-server fixture is required
when schema, Rust source and runtime equality hold. A substantive output change
reopens affected review/tests before release.

Publish from a new immutable annotated `v0.1.0` tag on the reviewed feature head.
The current remote default already contains `release.yml` with
`workflow_dispatch` and `ci.yml`; release validation checks repository, tag,
version and unchanged tag SHA, not main ancestry. GitHub dispatch accepts a tag
ref, so no default merge is needed or authorized. Owner3 retains ordinary SSH
feature/tag publication and fresh remote proofs. Do not move an existing tag.

Before actual upload, establish the existing procedure's `release` environment
reviewer and version-tag protections, and a usable first-publication bootstrap
credential. The maintained workflow's `authentication=bootstrap` requires an
absent crate and `CARGO_PUBLISH_BOOTSTRAP_TOKEN`; OIDC is its later-release path.
Credential values must be configured through the appropriate secret interface,
never notes or chat. This is an operational prerequisite, not another request
to authorize the already-requested release. Lead routes any owner-only action;
feature work proceeds meanwhile. Do not silently fall back between auth modes.

Keep native `cargo publish --locked` as the uploader. Before credentials enter
the job, run its dry run against the restored verified lock and retain the
candidate `.crate`, lock, source/tool identity and SHA-256 as run/attempt artifacts.
Retain the `.crate` produced by the actual publish command as well, even on
failure, and compare its hash with the candidate and public registry checksum.
Cargo may repack during publish; do not claim an unsupported prebuilt-archive
upload seam or bypass native verification. Fail visibly on byte divergence.
No compilation or resolution runs with the bootstrap credential except the
existing native publish step itself.

Once upload succeeds, independently GET exact crate/version metadata and the
registry's original archive, verify `vpsadmin-client`/0.1.0, checksum and content
against the retained actual publish archive, and observe docs.rs separately.
The existing workflow does not create a GitHub Release; a release page with
reviewed notes and retained checksum/artifact links can be prepared by owner3
as part of the authorized SDK release, after crate acceptance. Do not present
docs.rs indexing delay as an upload failure. Any later OIDC registration and
bootstrap-token retirement is an explicit owner operation, without secret reads.

## Recovery and compatibility

On uncertain upload, preserve tag, exact source, resolved inputs, original archive
and failed logs. Check public version/hash before any retry. A matching accepted
version needs verification completion, not reupload; a conflict or unavailable
original payload requires diagnosis. Do not overwrite/yank accepted content,
move tags, regenerate replacement bytes or select a new version silently.
Fresh absence is not proof that an earlier attempted upload was rejected.

Generated API/runtime and server schema are expected unchanged. No migration,
server deployment, mixed-worker ordering or new credential requirement for SDK
consumers is introduced. Rust 1.95 and existing async/blocking APIs remain.
Removing the tracked lock changes fresh developer resolution, not consumers'
dependency contracts; each verified release retains its actual local lock.
Older Git consumers can keep their previous revision. Main remains unchanged
until the user separately authorizes integration.

Official references: [Cargo packaging and lock behavior](https://doc.rust-lang.org/cargo/commands/cargo-package.html),
[manual workflow prerequisite](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow),
[dispatch accepts branch or tag](https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event).
The live crates.io trusted-publishing page did not expose readable text to this
read-only client; first-publication details above are the repository's actual
supported workflow contract, not a claim that an account binding was inspected.
