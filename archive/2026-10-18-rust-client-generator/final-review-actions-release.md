# Final review: client GitHub Actions publication

No findings. No Blocking, Important or Advisory issue was established in the
committed workflow package. End-to-end environment approval, OIDC and registry
upload remain unverified external operations.

Reviewed on 2026-10-19 by retained independent `reviewer0`, thread
`01a1508b-81fd-7ab2-b787-a7adb733a710`, model `gpt-6.1-sol`, effort `xhigh`,
saved access `read_only`. Live roster/settings and trusted session binding
match. `dev-session current` prints `2026-10-18-rust-client-generator` from the
bound tracking directory; both identity environment variables are absent.
No overrides, fallback, source authorship or subreviewers.

Applied mandatory-change-review and all four lane references: general,
architecture/repetition, scope/proportionality, risk/compatibility. Risk is High
because workflow authentication and permissions control irreversible registry
publication. Read the complete [packet](review-packet-actions-release.md), design
Clarification 6, workspace/repository guidance, actual committed diff/source,
operator docs and quick-check evidence. Existing
[source](final-review.md), [DELETE](final-review-delete.md),
[history](final-review-history.md) and [README](final-review-readme-release.md)
reports are preserved; unchanged application code was not audited again.

## Reviewed change and lane conclusions

Exact client range:
`c4a0f597cd3602e28ae11846962e2d1e07a0c1ff..091bd70954d270f3e575a71a8a5a1884eed2eccd`.
The actual delta is three files, 194 additions and one deletion:
`.github/workflows/release.yml`, `.github/workflows/ci.yml` and
`docs/development.md`. Final tree:
`1ebeda04321c99705fb98d6529ff0c39e9d72a7e`. Worktree/index are clean.
No source, runtime, generated model/action, schema, lockfile, manifest, example
or test change is included.

General: the manual release validates the canonical repository and package,
requires a tag exactly matching the manifest version, checks out the dispatch
SHA and confirms the current remote tag resolves to that commit. The revision
is retained as a job output. Publish checks out that immutable revision and
rechecks HEAD and the remote tag after toolchain preparation. Missing/moved tags
or Git failures stop the workflow. Input expressions pass through environment
variables rather than interpolation into executable shell/Python code.

The local `workflow_call` reference uses CI from the same workflow commit.
Explicit `github.sha` checkouts in all three CI jobs bind tests, docs/package,
MSRV and regeneration to the dispatch source. Verification must succeed before
publish, and no publishing secret is passed to the reusable workflow. Ordinary
branch/PR/manual CI remains; tag pushes alone do not publish or duplicate the
standalone push matrix.

Architecture/repetition: CI remains the single owner of the client test matrix.
The release workflow adds validation, protected publication and authentication
selection around that owner rather than copying its jobs or consulting an
unrelated successful run. Existing HaveAPI generator/shared release workflows
are unchanged. Operator instructions remain in the client maintenance guide.
No duplicated protocol or release framework is introduced.

Scope/proportionality: two explicit auth paths cover the demonstrated initial
crate limitation and later trusted publishing. Both call ordinary
`cargo publish --locked` through the committed Nix environment. There is no
automatic registry fallback, version/tag management, retry mechanism, release
bot, additional registry, or HaveAPI publication change. The implementation is
bounded to the approved client workflow package.

Risk/compatibility: global permissions are `contents: read`; `id-token: write`
is granted only to the protected publish job. CI has no publish environment or
secret inheritance. Release checkouts disable credential persistence.
Publication is serialized with cancellation disabled. Mode selection defaults
to OIDC; an OIDC error cannot take the bootstrap path.

Bootstrap verifies that the environment token exists without placing its value
in the prerequisite step. Only an HTTP 404 for the fixed crate endpoint allows
that mode to proceed; existing crates, auth/server errors, network errors and
timeouts fail. The token value appears only in the publish step environment.
Trusted token acquisition occurs after verification/tool setup/tag recheck,
and its output is supplied only to the OIDC publish step. No raw credentials
are printed or forwarded to tests.

Read-only official upstream inspection confirmed the new action pins and
current release versions: checkout v7.0.1 at `3d3c42e5...`, install-nix-action
v31.11.2 at `448cde739...`, and crates-io-auth-action v1.0.5 at `c6f97d422...`.
The pinned official auth action exposes the documented token output and
revokes it in its post step. Existing CI action refs retain their current
versions; this change does not add publishing rights to those jobs.

The operator guide correctly separates first upload from later OIDC:
short-expiry minimum-available-scope token in the `release` environment, then
register `vpsfreecz` / `vpsadmin-rust-client` / `release.yml` / `release` as
the trusted publisher and remove the bootstrap credential. It explicitly
requires workflow installation on the default branch and tagged revision,
administrator-configured environment reviewers/tag restrictions, and registry
state inspection before retrying a failed upload. Those setup requirements are
not silently supplied by YAML or by this review. Registry versions remain
immutable; no tag movement or version replacement is proposed.

## Evidence and remaining limits

Inspected the retained Actionlint/ShellCheck/YAML evidence and
`artifacts/client-release-static/check_gates.py`, parsed workflow snapshot and
26-case result. The cases exercise the actual inline repository/package/tag/
mode/source gates, moved tag and fetch failures, missing bootstrap credential,
404/existing crate, non-404/network/timeout failures, final revision/tag checks,
and permissions/token boundaries. Static gate checks use mocks; they do not
prove GitHub environment or registry authentication behavior. No tests, builds,
CI run, server or registry operation was launched by this reviewer.

After review, exact-head Actions CI remains the next verification step. Before
publication, an administrator must install the workflow as documented and
configure the protected environment; a crate owner must supply bootstrap or
register the later trusted-publisher binding. Real approval/OIDC exchange,
token acceptance, upload and docs.rs processing are not established by the
earlier Cargo dry-run or these static results. Publication failure still
requires checking registry state before another attempt.

## Whole final history, migrations and repeated updates

Independently inspected the complete final series/messages and diff inventory
from neutral client root `b67a3ba5eef89b2bd6533050aa8769aaa0574114`:

1. `f88d86ae97d335e4c89464a004e882fc7032720e`: handwritten package/schema/tests.
2. `62753f006d7bd3e5befe1033c49a2c630ca3ff02`: generated source/runtime.
3. `c4a0f597cd3602e28ae11846962e2d1e07a0c1ff`: requested library-user README,
   including the narrow absolute-link correction to the earlier review.
4. `091bd70954d270f3e575a71a8a5a1884eed2eccd`: Actions release capability and
   its CI reuse/operator documentation.

The last two commits are separate user-requested deliverables after initial
feature publication; they are not superseded source iterations. No standalone
README fixup remains. HaveAPI is unchanged at
`9e4c29a0412a25256ce944641f60ba13e9f03c2b`, with the same three reviewed
runtime/generator/fixture commits above comparison base
`526648131af45df68c25ac0042a52f22c7a81df5`.

**History conclusion:** no obsolete approach, transitional shim, abandoned
release mechanism or separate fixup remains in either final series. Commit
purposes and ownership remain coherent. **Repeated-update conclusion:** no
repeated dependency/pin/lockfile/schema/generated/provenance stream is introduced
or retained. CI reuse is part of one new release capability, not a redundant
dependency refresh. **Migration conclusion: no migrations.** No database or
persisted-format migration was introduced, merged, released, deployed or
externally consumed. Registry setup/publication is a new external operation,
not a migration of application state; no intermediate schema boundary requires
retention.

All four review lanes and the complete final history gate are satisfied for
client `091bd70...`, with the external verification/setup limits above.
The lead owns reconciliation, state/portal updates, CI and any authorized
publication. This review grants no tag/default-branch integration, registry
settings or upload, deployment or lifecycle authority. Only this review evidence
was written; application, Git and session state remain unchanged.

Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-rust-client-generator/>
