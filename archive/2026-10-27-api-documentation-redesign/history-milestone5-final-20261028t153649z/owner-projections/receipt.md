# Milestone 5 original-owner optional documentation integration projection

Temporary provenance only. The final accepted working-tree server/helper and
five partials were read and snapshotted; no application file was written.
This operation did not run app checks, hooks, Git mutations, dependencies,
preview, private fixtures, OAuth/TLS or lifecycle work.

## Authoritative staging boundary

Use `basic-pre-e/` for actual C and `restored-pre-e/` for actual D, with each
file at its repository-relative path. `optional-documentation-oauth-pre-e.patch`
restores all optional integration. `basic-final/` and `restored-final/` are
separate final-E snapshots, **not C/D staging bytes**. Their restoration patch
proves exact current final reconstruction.

Both pre-E and final patches actually replayed with `patch --batch --fuzz=0 -p1`,
without offsets. Each replay matched every restored file byte-for-byte. The
current application bytes were rechecked unchanged after replay. `proof.json`
contains strict unique replacement counts, per-file hashes and reconstruction
results; `*.sha256` are exact tree manifests.

## Complete optional seam inventory

- Server's existing require, complete configuration/accessor method, helper
  registration and mount call move with D.
- Single-version root uses ordinary `authenticated?` in C, documentation-cookie
  wrapper in D; the same actual-user map, one aggregate describe and root
  account seed remain in both.
- Documentation helper's version HTML authentication is ordinary in C and
  wrapped in D. Its memoized account presentation merges `controls: nil` in C,
  versus the once-read optional controls in D. Identity/name/title, neutral
  links, filtered metadata, search and client capability forwarding stay in C.
- Account partial preserves person/native Account disclosure, actual escaped
  username and Basic login/logout in C. D adds cookie POST Sign out, optional
  Switch user form, CSRF, optional login URL/hook and optional status message.
- Brand, version sidebar and shared sidebar snapshots are identical across the
  optional split. Their context locals, theme, version and current-resource
  presentation are preserved. Status retains the visibility note in both.

No optional module/helper/control/switch references remain in the projected
Basic runtime files. No authentication behavior was invented. The ordinary
Cookies helper/provider/settings semantics remain. Only the exact existing
request-local resource-context cache block was replaced by its known pre-E
single derivation for staging; no whole-parent-blob reversal was used.

Existing milestone4 partial and server artifact directories were left untouched
and remain authoritative for their historical source. These new snapshots are
required for the new milestone5 shared helper/root/account seams. Prior receipts
were not rewritten.

Owner2 must prove actual committed C/D blobs and source-bound Basic mounted root,
version and account smoke without borrowing any final-feature module, then final
full-tree equality and unchanged E patch. This artifact operation does not claim
those runtime/history checks. Cookie/root backend tests live in owner4's D
module spec; owner0 identity_and_guides_spec contains synthetic optional-control
presentation examples that must remain mapped with optional behavior when
splitting tests. Do not infer test disposition from whole-file reverse blobs.

pre-e restoration patch SHA-256: `b0f4b5174be5755336c1f7c21d560e9361b6a8a2f3cdab8a2e8b58c24d6808f0`.

final restoration patch SHA-256: `10e859ba46b5f658059670d961b86e4746f22620aefbf0291f15427d63aca98a`.
