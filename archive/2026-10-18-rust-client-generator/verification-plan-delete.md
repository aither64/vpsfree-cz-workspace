# Corrected-runtime verification

Start only after the corrected HaveAPI and regenerated actual client are
committed, quick checks pass, and affected-lane independent review completes.
Freeze exact heads in watcher briefs. Current HaveAPI final source is
`e9173e20a38de4e4e71bd5f2d4d79967950ca900`; final client is `1a818c424259713147d9ac6970b7247c744422df`.
Use one fresh retained Luna/low watcher for each related batch. No source edits,
diagnosis, retries, publication or hidden timeout by watchers.

1. Corrected runtime default/blocking tests and strict all-feature Clippy. Run
   the small complete runtime matrix because its shared method classifier and
   tests changed. Reuse target caches, not old pass conclusions.
2. Generic generated fixture at root and mounted API paths, both transports.
   Assert exact DELETE null/falsy/omitted/Custom/input metadata and GET control;
   preserve existing auth/continuation/partial-output/error cases.
3. Actual regenerated client default/blocking all-target tests and docs; then
   disposable real vpsAdmin runner using short private DB state, source-only
   fixture checkout and captured API7 client. No production mutation. This
   acceptance remains incomplete until both client tests actually run.
4. Rust1.95 both all-target feature checks with the same committed lockfile,
   Cargo package verification and archive inventory. No lock refresh or floor
   increase to hide a failure.
5. Build/extract generator package and compare packaged generation/check against
   saved actual snapshot, all Rust files and full ownership manifest. Use a new
   artifact leaf, exact source/client guards, no actual client writes.

Independent operations may continue after another completed operation fails if
cleanup/ownership are confirmed. Stop dependent operations on failure. Owners
receive exact evidence and fix causes before reruns. Revised protocol behavior
requires review, but direct narrow test/fixture corrections can use the existing
review's focused-inspection policy when they do not widen accepted behavior.

The two publicGET smoke requests already passed both transports and need not
repeat solely for DELETEclassification. No API capture, credentials, release,
server deployment or database migration is part of these gates. Feature branch
publication and CI follow successful local verification; default integration
still requires the user's explicit repository/target direction.

Exact runtime commands, cwd HaveAPI pinned client-rust shell:

```sh
cargo test --locked --manifest-path clients/rust/runtime/Cargo.toml
cargo test --locked --manifest-path clients/rust/runtime/Cargo.toml --features blocking
cargo clippy --locked --manifest-path clients/rust/runtime/Cargo.toml --all-targets --all-features -- -D warnings
```

Generic and actual vpsAdmin exact runners are in verification-plan.md; use the
final source/client guards from this record. Artifact root paths may be deep
now that database state is explicitly short/private. Do not remove existing
receipts or reuse a nonempty generator package artifact leaf.

Completed corrected batch evidence so far (exact reviewed e9173e20/1a818c4):
runtime default/blocking/Clippy pass, actual client bothfeatures/docs/package pass.
Generic root realserver6cases pass; scripted exactpath expectation stillneeds
fixture correction, so mountedrun remains pending. ActualvpsAdmin DB/schema
bootstrap succeeds but invalid redundantDNSrecorduser prevents readiness;
clientassertions not yetrun. These two source-backed fixture-only corrections
will not justify repeating unchanged passingruntime/client checks; after scoped
commit, rerun actualvpsAdmin and genericsuite with fresh watcher, then reconcile
finalhistory/provenance and independenthistoryaddendum.

LatestactualvpsAdminprogress: bothtransportsreachandpassVPSshow/info/paging,
DNS TTL120->null andnestedCustom settingwrite/read. Fixture corrections use
canonicalvalidDNSownershipandWebUInamespaceui; no runtime/clientcontractchange.
Remainingtokenrequestfailurelocalizedstaticstage, source-backeddiagnosispending.
Do not call actualacceptance complete until request/existingtoken/renew/revoke
and expectedbadcredentialcases allfinish.
