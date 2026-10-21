# Final README review before initial Cargo release

One Advisory finding; no Blocking or Important findings. The library examples,
configuration and behavior claims match the committed implementation. Release
dry-run and publication remain separate operations.

## Finding

**D1: Advisory, general lane: relative links break in the crates.io README.**
Client commit `bfa960e31fddb49b371c2cf6d26b7886fdf8f57f`, `README.md:132`
and `README.md:147` link relatively to `examples/async_vps.rs`,
`examples/blocking_vps.rs` and `LICENSE`.

The official crates.io renderer resolves repository-relative links through
`blob/HEAD` rather than the published feature revision. See
[the renderer](https://github.com/rust-lang/crates.io/blob/main/crates/crates_io_markdown/src/lib.rs#L237)
and its `relative_links` examples. GitHub reports this repository's default
branch as `main`; it still points to the neutral empty root. Read-only checks
confirmed HTTP 404 for all three raw `HEAD` targets and HTTP 200 for the async
example on the retained feature branch. Local target existence and inclusion
in the crate do not make these rendered links resolve correctly.

Narrow remedy: use absolute links to the retained feature branch or an exact
release source revision for both examples and LICENSE, as the maintenance link
already does. Default-branch integration is not necessary. The lead received
this finding during review; direct inspection of this narrow link correction
is sufficient under the existing remediation policy.

## Scope, identity and assessment

Reviewed on 2026-10-19 by retained independent `reviewer0`, thread
`01a1508b-81fd-7ab2-b787-a7adb733a710`, model `gpt-6.1-sol`, effort `xhigh`,
saved access `read_only`. Live roster/settings match. `dev-session current`
prints `2026-10-18-rust-client-generator` from the bound directory; both
environment identity variables are absent, consistent with the trusted binding.
No overrides, fallback, subagents or source authorship.

Applied mandatory-change-review and the general lane to this Low-risk,
README-only change. Read the [packet](review-packet-readme-release.md), applicable
workspace/repository guidance, actual commit/diff, final complete series,
maintenance docs, the Go client's README and existing review reports. The
lead's context-dependent writing pass remains its responsibility; this review
does not rewrite application prose.

The README now leads with Cargo installation and unauthenticated public stats,
then describes explicit credentials, fluent inputs/null setters, optional
outputs, timeouts/errors and blocking use. Relevant signatures, output fields,
default timeouts, feature flags and example environment variables agree with
committed source. The Go README supplies the requested usage-first structure;
the Rust text uses the actual Rust interface instead of importing Go-specific
auth callbacks or transport configuration.

Maintenance details remain discoverable through the absolute development link;
omitting capture inventories and wire-encoding internals from the entry page
does not remove them from their owning maintenance documentation. The mutation
example clearly says it changes state. Blocking construction/use/drop and
uncertain mutation outcomes after timeouts retain the relevant limits.

The packet reports eight balanced fences, parsed TOML, existing local targets,
pinned-rustfmt parsing of complete examples and clean whitespace. This reviewer
did not run checks, compile examples or repeat prior application tests. The
new crates.io installation and docs.rs URL intentionally describe the upcoming
authorized 0.1.0 release; their availability is contingent on upload and docs.rs
processing, not established by this review. Packaged README rendering was
assessed against the current upstream renderer, exposing D1 above.

## Complete final history and migration conclusion

Client base remains neutral empty root
`b67a3ba5eef89b2bd6533050aa8769aaa0574114`. Actual complete feature series:

1. `f88d86ae97d335e4c89464a004e882fc7032720e`: handwritten package/schema/tests.
2. `62753f006d7bd3e5befe1033c49a2c630ca3ff02`: generated source/runtime.
3. `bfa960e31fddb49b371c2cf6d26b7886fdf8f57f`: requested library-user README.

The third commit has exactly README.md as its changed path and descends directly
from the previously reviewed client head. It is a distinct user-requested
documentation follow-up after feature publication, not a leftover source fixup.
The two implementation commits and their prior history assessment are unchanged.

HaveAPI remains `9e4c29a0412a25256ce944641f60ba13e9f03c2b` on comparison
base `526648131af45df68c25ac0042a52f22c7a81df5`, with the same three runtime,
generator and fixture commits assessed in [the history review](final-review-history.md).
Both application worktrees/indexes are clean. Prior
[source](final-review.md) and [DELETE](final-review-delete.md) reviews are preserved.

**History conclusion:** no obsolete approach, transitional shim or separate
fixup remains in either complete series. The documentation follow-up has one
clear independently reviewable purpose. **Repeated-update conclusion:** no
repeated pin, dependency, lockfile, schema, generated-output or provenance stream
is introduced or retained by this follow-up. **Migration conclusion: no
migrations.** Neither feature branch introduces a database/persisted-format
migration; no migration has been merged, released, deployed or externally
consumed. Existing generated API migration methods remain ordinary bindings.

The user has authorized the initial Cargo publication after completion, as
recorded by the lead. This review performs no release action and grants no
default-branch integration approval. The new README changes the package payload,
so the planned final `cargo publish --dry-run` remains necessary before upload;
the older package archive is not claimed identical. Registry credentials are
reported unavailable in the packet, and actual upload/docs.rs processing remain
unverified.

Only this review report was written. No application, Git, check/build/server,
registry or session-state mutation occurred. Read-only upstream renderer/link
inspection made no production API requests. Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-rust-client-generator/>
