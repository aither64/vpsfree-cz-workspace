# Independent final review

Reviewed on 2026-10-19 by retained `reviewer0`, thread
`01a1508b-81fd-7ab2-b787-a7adb733a710`, model `gpt-6.1-sol`, effort `xhigh`,
access `read_only`. The live same-session roster matches those settings and the
thread binding. No fallback, setting override, source authorship or subreviewer.
Application files remained read-only; this file is review evidence.

`dev-session current` from the bound tracking directory printed
`2026-10-18-rust-client-generator`. Both identity environment variables were
absent; the trusted thread binding identifies workspace
`/home/aither/workspace/ai/vpsfree.cz`. A preliminary invocation from the shared
workspace root found no session; the required invocation from the intended
tracking directory resolved it before session records were read.

Risk: **High**, because authentication, credentials and a public cross-project
generator/runtime contract are involved. Applied mandatory-change-review and all
four lane references: general, architecture/repetition, scope/proportionality,
and risk/compatibility. Read workspace/repository instructions, applicable
procedures, packet, plan/design/state and owning project documentation.

Review is complete for the original committed ranges below. There are **two
Important findings and no Blocking findings**. The lead accepted both and assigned
narrow fixes. Their implementation, final history consolidation and longer
verification are separate pending gates; this report does not certify those
later revisions or claim readiness for release.

## Findings

### R1: Important: collision validation omits runtime methods and generated locals

Lanes: general and architecture/repetition. Owning commit:
`615293a1c313511723062283afab815c3e863a7d`.

Locations in HaveAPI:

- `clients/rust/lib/haveapi/rust_client/ir.rb:12`, `:83`, `:116`.
- `clients/rust/template/resource.rs.erb:22`.
- Related runtime methods: `runtime/src/runtime/client.rs:29`, `:194`, `:230`;
  the generated `builder` lives in `template/mod.rs.erb`.

An ordinary input named `new` or `prepared` passes the input naming scope and
produces a setter that duplicates an inherent runtime `Request` method. A
resource named `config` or `builder` likewise duplicates a `Client` method.
A remaining action placeholder named `path_params` is accepted, but the action
template shadows it with its local `BTreeMap` before calling `.to_string()`.
These cases produce uncompilable Rust instead of the promised collision error
with the original schema path. Rustfmt only parses/formats these definitions;
the passing formatting gate does not detect duplicate inherent methods.

A quick read-only probe under the client's pinned Nix Ruby, using a reduced copy
of the actual saved schema, confirmed that the IR accepts input `new`, resource
`config` and `{path_params}`. The actual captured vpsAdmin surface has none of
these conflicting names, so this finding concerns the supported generic
generator rather than an observed collision in the current client.

Remediation boundary: reserve the complete existing runtime/generated method and
local names, or make template locals hygienic. Add focused regressions that fail
with useful original-path diagnostics. Keep deterministic names and the existing
reject-on-collision contract; no naming fallback or new abstraction is needed.
The lead assigned this narrow fix to implementer1.

### R2: Important: documented integration entry point does not activate its bundle

Lane: general/verification. Owning commit:
`c50c07111baa68e4e321952511acc6da2a9ddce7`.

Locations in HaveAPI:

- `clients/rust/spec/integration/run.rb:10`, `:26`, `:82`.
- `.github/workflows/clients-rust.yml:51`, `Makefile:23` and the integration
  README invoke plain `ruby`.
- `flake.nix:153` sets `BUNDLE_GEMFILE` but does not activate Bundler.

The runner loads generator source without `bundler/setup`. The generator's
`haveapi-client` dependency is a local path dependency, not an installed gem.
Consequently the documented/CI invocation cannot load `haveapi/client` when
`Snapshot.fetch` starts acquisition. A quick read-only probe under the pinned
Ruby with the Rust component's `GEM_HOME` and `BUNDLE_GEMFILE` loaded the runner,
then reproduced `LoadError: cannot load such file -- haveapi/client`.

The child also overrides `GEM_PATH` with only the server gem home. A separate
activation-only probe with that exact gem selection reproduced
`Bundler::GemNotFound: Could not find net-pop-0.1.2 in locally installed gems`.
It excludes the pinned Ruby's bundled gems. Neither probe started a server or
invoked Cargo.

Remediation boundary: activate the locked generator bundle at the entry point,
or make all documented/CI invocations consistently use `bundle exec`. Start the
server with its own bundle while retaining the pinned interpreter's default
gems; account for inherited Bundler environment if activation occurs in the
parent. Add a focused dependency-activation regression. This needs no protocol
or server behavior change. The lead assigned it to implementer2.

## Whole-branch history, migrations and repeated updates

Inspected actual commit messages, per-commit file ownership, complete series and
final diffs, rather than only the last commit or the packet's conclusions.

| Repository | Reviewed range and full feature series | Disposition |
| --- | --- | --- |
| HaveAPI | Base `c14e7d3158b91c134c2817b489cd29772fc09f82`; `0717da05eb2a6dec60e2fce2a57d97b5bb556653` runtime, `615293a1c313511723062283afab815c3e863a7d` generator/tooling, `c50c07111baa68e4e321952511acc6da2a9ddce7` integration | Three coherent commits. Runtime harness/tests/docs belong with runtime; generator packaging/environment/specs belong with generation; integration is independently reviewable. |
| vpsadmin-rust-client | Neutral root `b67a3ba5eef89b2bd6533050aa8769aaa0574114`; `50f57a09328b5044f1da12b149c143fa38c94a66` handwritten package/snapshot/provenance; `fe7f7a7191895b7be33690102b0e4b952f5f9415` generated source | Root has Git's empty tree `4b825dc642cb6eb9a060e54bf8d69288fbee4904`; handwritten and generated changes are separated. No predecessor client compatibility shim. |
| vpsAdmin fixture source | Unchanged `fb2f51222503a45f2e5a42af505f719e44279ed0` | Dependency/fixture source only, no deliverable diff. |

**History conclusion:** no obsolete unmerged approaches, abandoned compatibility
paths or fixup history remain in these original reviewed series. Numbered design
clarifications describe pre-commit development; the commits introduce the final
chosen names and empty-output rule directly. Both branches were clean at the
original gate. Owner remediation edits began after findings were reported and
are outside these reviewed ranges. Fold narrow follow-ups into their owning
unmerged commits and preserve this report's original revision references.

**Migration conclusion: no migrations.** Neither final diff introduces a database
or persisted-format migration. Generated bindings for existing API migration
actions are ordinary client methods. The packet records no merged, released,
deployed or externally consumed feature/migration state, and the inspected
changes introduce no transitional migration lineage or supported predecessor
schema to retain. No server deployment or fleet coordination is required.

**Repeated-update conclusion:** no repeated dependency, channel/input pin,
lockfile, schema-capture or generated-artifact update stream exists in the
original committed series. HaveAPI's nixpkgs pin is unchanged. Its Ruby and
runtime Cargo locks are introduced once; the new client's flake/Cargo locks and
schema snapshot are introduced once, followed by one generated-source commit.
Separate repository lockfiles serve separate packages, not superseded updates.
No released consumer/state boundary requires retaining redundant updates.
Later remediation provenance/regeneration must be consolidated before readiness,
as the lead has already planned.

## Lane conclusions and evidence

General: R1 and R2 above. Documentation is linked from the relevant entry points
and separates durable generation/runtime contracts from session evidence. It
states the snapshot's visibility limits, async/blocking lifecycle restrictions,
omission/null behavior, release gates and recovery limits. No additional
supported-surface correctness finding was established through static inspection.

Architecture/repetition: HaveAPI owns generation and common runtime source;
the real client and fixture crates are its actual consumers. Copied runtime is
an intentional single-source boundary rather than a second handwritten
implementation. Async/blocking share validation, URL/body preparation, envelope
decoding and errors; their small transport-specific portions use their respective
reqwest APIs. R1 exposes the incomplete contract between those runtime methods
and naming validation. No additional maintenance blocker was found.

Scope/proportionality: the implementation follows the accepted embedded-runtime,
Ruby/ERB, async/default and optional-blocking scope. It does not add automatic
retries, paging, polling, browser auth or a public runtime package. Linux
`renameat2` exchange is a small, documented implementation of atomic owned-tree
replacement and fails before replacement on unsupported hosts. No additional
scope finding.

Risk/compatibility: static inspection found explicit auth selection, metadata
header names, credential suppression on token login/challenges, sensitive token
headers, redacted request/response/error diagnostics, verified TLS, disabled
redirects/retries, deadlines and response caps. URL data uses individual encoded
segments and mount preservation. Success/error envelopes distinguish HTTP,
protocol and typed failures. Outputs tolerate omitted/null fields and preserve
extra fields/partial associations. No credential leak or server compatibility
regression was established. Client rollback still cannot undo an executed API
action, as documented.

Independent read-only checks reconstructed the committed HaveAPI generator and
runtime digests from `git archive c50c071...` in memory, compared the Ruby lock
digest and copied runtime bytes, and verified every owned generated file hash.
They matched the client's provenance/ownership manifest. A separate traversal of
the saved schema confirmed 152 resources, 524 action methods/routes matching
generated `SPEC`s, and 8720 parameter descriptions. No application build,
server, live request or long test ran during review.

The packet's pre-review quick checks cover Ruby specs/style, formatting,
deterministic production generation/check, provenance and hooks. They are not
compilation or acceptance evidence. Remaining gates after finding resolution:
runtime async/blocking tests and Clippy; generated-client scripted/real HaveAPI
acceptance at both mounts; actual crate/examples/docs/package compilation in
both modes; Rust 1.95 with the lockfile; packaged-generator generation; disposable
real vpsAdmin VPS/paging/null/Custom/auth acceptance. The optional public smoke
artifact is supplemental and was reported as unexecuted.

The lead owns finding reconciliation, focused remediation checks, final
consolidated history/provenance and state/portal updates. No default integration,
publication, deployment or session lifecycle action is authorized by this review.
The session remains open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-rust-client-generator/>

## Final consolidated history addendum

2026-10-19, same independent reviewer and retained settings. This addendum
completes the final history gate after the lead accepted and directly checked
the narrow R1/R2 fixes. It preserves the original source review above and does
not rerun source review or tests merely to confirm those fixes.

Independently inspected actual final commit series, messages, final diffs and
range-diffs, including the recorded
[HaveAPI consolidation](haveapi-history-consolidation.md) and both linked
range-diffs. Session identity was reverified; both environment markers remain
absent. Both final application worktrees/indexes were clean.

| Repository | Final complete series |
| --- | --- |
| HaveAPI, base `c14e7d3158b91c134c2817b489cd29772fc09f82` | `0717da05eb2a6dec60e2fce2a57d97b5bb556653` runtime, `e93e51ac9edaef7e7cf5ff57e42ee6a292d6c10c` generator, `874e8f2fd8c94a4bc34008936e13b856b82cdd2b` integration |
| vpsadmin-rust-client | Unchanged empty root `b67a3ba5eef89b2bd6533050aa8769aaa0574114`, `b8235d129ce2dad34e466f3a3d8754eacef49f53` handwritten package/snapshot/provenance, `58acdd6f95c6e03f57edeb3a533a9563649590a4` generated source |

HaveAPI has exactly three feature commits. R1 and R2 are folded into their
owning generator and integration commits; neither corrective commit remains
in the final series. Runtime is unchanged. An independent `git diff --exit-code`
confirmed equality with corrected pre-consolidation `54e233e...`; both trees are
`2590b086ebbdb2c8b6ebb2283059051b1e5bfb01`. The range-diff from the original
reviewed series contains only the bounded remediations, their regressions/docs
and the integration subject shortening.

The client retains exactly two feature commits after its neutral root. Its
range-diff from the original reviewed pair changes only generator provenance
and the generated ownership marker, plus the generator revision in the commit
message. The actual final tree delta is two JSON files with three lines
replaced: HaveAPI revision and source digest in `schema/provenance.json`, and
that digest in `src/generated/.haveapi-generated.json`. All 686 Rust files,
runtime, saved schema and dependency locks are unchanged. Final client tree:
`1c185458f56f701571aa1effb5f6c0dc58a405d6`. Provenance now selects HaveAPI
`874e8f2...` and generator source digest
`b2f1408d9a53eda4bdf33054f4293e5e1ae712d69c66863e6c0ee71902bcfc13`.

**Final history conclusion:** both complete final series introduce their chosen
implementation directly. No obsolete unmerged approach, transitional shim,
separate fixup or redundant generated refresh remains. The logical commit split
remains sound.

**Final migration conclusion: no migrations.** No new migration or persisted
format transition appeared during remediation/consolidation. There is no
merged, released, deployed or externally consumed intermediate feature/schema
boundary requiring preservation; ordinary generated API migration actions do
not change this conclusion.

**Final repeated-update conclusion:** no repeated pin, dependency, lockfile,
capture or generated-artifact update stream remains in either final series.
The client refresh is folded into the original handwritten/generated pair;
the intermediate generator revision/digest is not retained as an update commit.
No release or supported-consumer exception is needed.

The required final history/migration/repeated-update gate is satisfied for
HaveAPI `874e8f2...` and client `58acdd6...`. R1/R2 closure relies on the lead's
accepted direct remediation checks under the narrow-fix policy. Longer
verification remains a separate readiness gate and was not run by this
reviewer. This addendum authorizes no integration, publication or lifecycle
action; the session remains open.
