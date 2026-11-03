# Committed branch refresh review packet

Scope: user-authorized Red Hat-family release refresh and approved source-identity /
nullable-channel correction. Existing design.md remains the accepted brief.
No new feature behavior is proposed. Initial request authorized merge when verified;
subsequent approval explicitly directed the proposed root-cause fix.

Repository vpsfreecz/vpsadminos; target staging; feature worktree
worktrees/2026-11-03-redhat-image-releases/vpsadminos. Session records are here.

Original reviewed range dd188397abe37d0bc33f4c5dfb3605206ce5e326..
58aae8d54887a14f59fada178a833b33a6ebfa81. Two narrow reviewer findings were fixed
and folded into original tested head 1a637e9eac4311adba2b08d60dfa7a17d07bcb52;
lead inspected exact two-file changes and real-module regressions under narrow-fix
rule. See metadata-result.md, review-result-expanded.md and retained patch receipt.

Refreshed base: 742eb30cb1a8b6766c85e915d26b0400e38244b1.
Refreshed head: 54b4313404cea35b58ebb9df951ae75e27c44971.
Implementer reports conflict-free replay with six equal range-diff entries and
byte-identical per-commit binary patches. Verify rather than assume that report.

Complete refreshed feature series:
1. 3aac965d5d6bdaa2fa8a139dd10159201c26b54f — CentOS9 release.
2. b436a06ba9c27bb3195f0d8ba32eed633d0e1fb8 — CentOS10 release.
3. 31bfa71efd3ec4d223b61076b2376bebb784db56 — Rocky9 release.
4. ea432db774500954351387fb8a10a112e98f13bf — Rocky10 release.
5. b19dbec8bf90554569b1f0e6a9083443d17238e5 — nullable channel consumer/test.
6. 54b4313404cea35b58ebb9df951ae75e27c44971 — captured source identity/docs/tests.
Final feature diff: 18 files, 665 insertions / 48 deletions, unchanged in size.
No migrations, persisted formats, released/deployed intermediate feature state,
new pins or coordinated node update. No repeated dependency/release streams or
obsolete approaches; each of four image directories advances once. Preserve the
required split. Old tested head retained in a separate local ref, not claimed merged.

Baseline delta consists only of three openSUSE commits: builder Leap16.0,
new Leap16.1 recipe/distribution, udev install plus device-units expectations.
No overlapping feature paths. The distribution list and source identity change
actual test inputs, so no old-head Nix verification reuse is assumed.
Review the affected baseline interactions and complete refreshed history/diff;
reuse your prior analysis where unchanged. No full external-consumer resurvey is
needed absent a concrete changed boundary. Existing optional framework signatures,
matching provider isolation and native/legacy/explicit identity semantics must hold.

Reviewer: retained reviewer0, saved gpt-6.1-sol/xhigh/read_only. Overall high risk
remains for generated OS/security provenance/framework compatibility. Applicable
lanes: General, Architecture/repetition, Scope/proportionality, Risk/compatibility.
Read mandatory-change-review skill and all four references, plus local guidance.
Independent whole-branch conclusions must include history/streams and no migrations.
No edits, long tests, CI actions or nested delegation by reviewer.

Documentation: docs/os/test-framework-integration.md owns the lasting interface;
plan/design/evidence own temporary verification. The generic source identity fix
preserves existing source selection and GC lifetime; pinned external vpsAdminOS
provider must retain its own identity. External vpsAdmin consumer inspection and
pins are recorded in prior review; no downstream pin update/deployment needed.

Quick checks and exact old/new mapping: refresh-result.md (implementer0).
Assign review only once that receipt says committed changes and quick checks pass.
Long checks at original head: 42 focused Ruby examples, both Nix matrices,
all4 local8GiB images, all4 native24GiB CI images, 317 scripts /109 core tests,
RSpec/RuboCop pass. CI-managed-result.md retains exact old-head evidence.
Nine livepatch jobs failed same immutable pre-existing fixture derivation as
baseline; accepted as unrelated failures, never as passes. Precise checksum/read
failure unobserved. No fixture/kernel project is authorized.

Remaining after review: publish refreshed branch and exact-head checks, then
fresh-target/clean-head/history/hooks/short claim/ff-only SSH staging integration.
No repository claim held, no production deployment or session lifecycle action.
