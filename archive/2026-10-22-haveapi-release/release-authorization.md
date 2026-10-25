# HaveAPI 0.30.0 integration and publication authorization

User direction in the current conversation:

> well then, merge the changes and you can make the release

Accepted scope: integrate the prepared HaveAPI feature into `vpsfreecz/haveapi`
`master`, prepare the required `haveapi-0.30` release branch and annotated
`v0.30.0` tag, and perform the repository's protected GitHub Actions release
workflow for HaveAPI 0.30.0. This includes the workflow's RubyGems/npm/PyPI
uploads, PHP mirror/tag synchronization and GitHub Release. The chosen Rust
generator gem name remains `haveapi-rust-client`.

The reviewed starting feature head is
`b64fb25bea8d8222fb3263b99956c0b61438a859`, tree
`05384a632290653cb4560c7451b3897acd5956c8`; base
`a32b15e379f44fc6dae4b15ef4ec17a142e5f465`. All ten final-head CI runs,
local acceptance and mandatory independent final review passed. Fresh target
checks, enabled hooks, short repository claim and exact remote proof remain
required for integration. A material source/patch change returns to preparation
and applicable review rather than silently extending this approval.

Not included: the separate `vpsfreecz/vpsadmin-rust-client` publication,
credential reads, unrelated registry/account changes, deployment or any session
archive/delete/stop/cleanup/lifecycle operation. Existing artifacts and historical
results remain preserved. The session stays open.

Owners: implementer0 prepares and executes serialized Git operations; implementer1
owns bounded read-only publication preflight; lead owns acceptance, publication
coordination and records. Long CI/publication observation uses a fresh policy
watcher. No claim is held during preparation, tests, review or CI waits.

The user subsequently answered the pending publisher setup question: **Both are
configured**, referring to RubyGems `haveapi-rust-client` and PyPI `haveapi-client`
with tuple `vpsfreecz / haveapi / release.yml / release`. npm is already
established per the user. This is account-owner confirmation, not an API inspection
of registry account entries. Proceed with authorized release after integration
and the workflow's own preflight; preserve any failure before deciding recovery.

## Follow-up development boundary

User subsequently requested fixes for PyPI/RubyGems confirmation behavior and
all relevant warnings in the original Test and build maintained packages output,
including deprecated npm dependencies and Rollup's rewritten top-level `this`.
These fixes are authorized on a new development branch only, after resolving
0.30.0. No further release is authorized without fresh user approval. The
existing 0.30.0 recovery remains authorized with its original tag/artifacts;
never fold follow-up source changes into that released version.

Architect0 owns full-output investigation/design; implementation packages will
be assigned after the bounded design and separate worktree are ready. No version
bump, default integration, release tag or publication is authorized for followups.
