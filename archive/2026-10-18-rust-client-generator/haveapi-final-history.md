# Final HaveAPI feature history and verification inputs

Final HEAD: `9e4c29a0412a25256ce944641f60ba13e9f03c2b`. Comparison base: `526648131af45df68c25ac0042a52f22c7a81df5`.
Original registered initial base remains `c14e7d3158b91c134c2817b489cd29772fc09f82`.
No session registration was changed. Upstream was refetched and confirmed
exactly at the comparison base before rewriting.

| Final logical commit | Purpose | Stable patch ID |
| --- | --- | --- |
| `930a5f3f9ceca9586a4d89d72514d72f00f04d21` | clients/rust: add embedded protocol runtime | `9e95bfe266bc0d720ee7c9435827738273db2be4` |
| `8701baa51effcc90900a4c146d0fb27c31ec7db9` | clients/rust: generate clients from saved API schemas | `b77b459dd0c0fe4fcb92a628e69b53f5d53c1a08` |
| `9e4c29a0412a25256ce944641f60ba13e9f03c2b` | clients/rust: add protocol acceptance fixtures | `1f40718e4469c6d53d991c398b3659d47b163448` |

Acceptance head `41bbb37e40fe87851d327c4e986800071afd6277` and folded old-base head
`5f532ee8d5d3066b1264c276c1606ea3fca52105` have the identical tree
`dc8825b99a3394cbd401d92331409e0c8a4befd7`. Runtime and generator logical patches
are retained; integration folds `3aaf7cf85fca93433ca64c710fa326d31c0c6ec6`,
`a86d21ffe4ca557d315bf7240f2986206f0119b0` and `41bbb37e40fe87851d327c4e986800071afd6277` into its owner.
No source edits or conflict resolutions were needed.

After rebase onto `526648131af45df68c25ac0042a52f22c7a81df5`, all three individual patches and the
aggregate patch are equivalent. The [rebase range-diff](haveapi-final-rebase.range-diff.txt)
shows three `=` mappings. Final tree: `3ed0da056fbaa0d68c55e5fab635e3ea2105dc61`. Its entire difference from
the accepted tree is byte-for-byte the upstream patch touching only
`utils/release/publish.rb` and `utils/release/spec/release_spec.rb` (53 additions,
3 deletions). Their final blobs match upstream. No Rust, generator, Ruby-client,
server, schema, lock or flake input changed in the upstream update.

All three final logical commits explicitly ran `git commit --amend -F`
with prepared message files and mandatory root Nix hooks. Applicable
HaveapiI18n, RuboCop, SingleLineSubject, TrailingPeriod and TextWidth passed
without hook bypass/config changes. The integration fold also ran these
hooks. The final index and worktree are clean. No application build/test,
push, default-branch integration, publication or lifecycle action occurred.
An optional read-only Nix evaluation was slow and a stop was attempted; it
had already progressed and completed successfully. Its exit-zero receipt
is retained; no build or test was launched by it.

Verification reuse is bound to [actual component/lock hashes and completed
receipts](haveapi-final-input-receipt.json), plus exact tested
[flake-derived shell and compiler identities](haveapi-final-nix-inputs.json).
Runtime/client/MSRV/package results remain at their original tested heads;
all relevant production source, dependency locks and toolchain inputs match.
Generic root/mounted acceptance is bound to its passing `3aaf` inputs; actual
vpsAdmin/token-cycle acceptance is bound to passing `41bbb`/client `7279`.
The final package's 26 source-file hashes match its passed package inventory.
No old archive byte hash is claimed for a later provenance-only change.

Full base-to-head commit/path inventory and proofs are in
[the history receipt](haveapi-final-history-proof.json). The final feature
range contains exactly three logical commits. **No migrations** and no
obsolete follow-up/fixup commits or repeated update streams remain. No
intermediate published/released/deployed/consumed feature state requires
retaining corrective commits. Existing baseline history is not rewritten.

- [Reviewed e917 series versus final](haveapi-final-reviewed.range-diff.txt)
- [Accepted corrected series versus final](haveapi-final-accepted.range-diff.txt)
- [Folded old-base series versus rebased final](haveapi-final-rebase.range-diff.txt)

The lead should freeze this source for one client provenance revision-only
refresh and client test-fixup folding, then request the retained reviewer's
final history/patch-equivalence addendum. Feature publication is still
pending; default master integration remains unapproved.
