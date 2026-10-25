# HaveAPI 0.30 release preparation and API examples

Current feature head27b4f8f895a4e5401357a402187c2a4590699aec,18 consolidated commits,
exact last message Version0.30.0. Implemented and quick-checked; final independent review completed with3 Important+1 Advisory findings.
All review corrections passed focused checks and direct lead inspection; final
assembled74 documentation+assets and5 Python protocol examples pass. Final
history was published27b4f8f8; all10CI/core suite/package checks passed, installed
dynamic token acceptance exposed a real mounted-URL bug. Architect recorded
contract, JS/Python owners implementing fixes; new affected-lane review and
remaining executable acceptance pending.
compiled/package acceptance and final feature publication pending.
Not ready for release publication yet. No default integration, official branch,
release tag, registry upload, secret configuration or deployment performed.

Implemented example matrix: JS callback/async, TS callback/async, Python sync/async,
Go generated SDK and Rust async/blocking generated SDK. Missing Go/Rust profile
hides that language from overview and every example section. Configured-invalid
profiles fail startup; unsupported samples show bounded limitations. File system
renderer/examples/overview link removed, separate project untouched. Other legacy
formats preserved. New profile config and typed callback helper described in
project docs, with explicit package/auth/input capability limits.

Pending publisher reminder: new RubyGems haveapi-rust-client and PyPI
haveapi-client pending entries, both owner vpsfreecz/repository haveapi/workflow
release.yml/environment release. Existing HaveAPI gems and npm package need
regular matching publishers. npm direct publish permitted; new entry expires
if no successful publication within two days. Account-side entries unverified.
HaveAPI Rust generator is a gem; no crates.io publisher/token applies to it.

Separate repository vpsfreecz/vpsadmin-rust-client publishes crate vpsadmin-client,
currently0.1.0. First publication needs protected release environment and secret
CARGO_PUBLISH_BOOTSTRAP_TOKEN. After crate ownership exists, configure crates.io
publisher vpsfreecz/vpsadmin-rust-client/release.yml/release; existing workflow
explicitly selects bootstrap or oidc with no fallback. Supplied token unread.
No downstream publication or tag authorized/executed.

Evidence: api-doc-review-packet.md, api-doc-final-* inventory, package0-api-doc-
receipt.md and package1/2/3 receipts; original final-review/full-green baseline
retained separately. Baseline artifacts08345b2 moved with checksum proof to
baseline-artifacts-08345b2; final source build must produce new candidate files.

Session remains active/open; integration/publication require explicit direction.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
