# Client GitHub Actions release review packet

User requested a library-user README and publication with Cargo, then preferred
GitHub Actions trusted publishing and asked about initial upload for the crate
and Ruby generator. The README is complete/published/reviewed at c4a0f59, and its
exact-head CI and fresh Cargo dry-run passed. This separate change prepares the
client publication workflow; no registry state, tag or default branch is changed.

Scope: client .github/workflows/release.yml, small workflow_call reuse in ci.yml,
and docs/development.md. Architect contract: design.md Clarification 6. HaveAPI
9e4c29a and its shared release pipeline are unchanged. Generator mechanism is
information only; do not publish the shared HaveAPI release or modify its lists.
Client package remains 0.1.0/API7.0/MSRV1.95. No source/schema/locks/generated/
provenance/runtime/example/test changes are intended.

Risk: high because workflow auth/permissions control irreversible registry
publication. Select all four lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility. Retained reviewer0 settings remain
Sol/xhigh/read_only. Same independent reviewer; no overrides/subreviewers.

Required behavior: explicit dispatch against v<manifest-version>, strict
canonical repo/name/version/tag and exact commit binding; verify existing CI
workflow at same revision through workflow_call, no duplicate test matrix;
protected release environment; contents read globally, job-only id-token write;
serialize without cancel; auth choice oidc default or explicit bootstrap, no
fallback after OIDC failure. Bootstrap only if crate absent/404 and short-lived
environment token present; network/non-404 must fail. OIDC uses current official
crates-io-auth-action pinned by SHA and token supplied only to cargo publish.
Never log token or hand credentials to tests. Operator setup must match actual
owner/repo/workflow/environment. Default workflow installation prerequisite is
explicit and does not grant merge approval. New crate first publication needs
API token, but may run on Actions; later trusted publisher is registered after
initial upload. No actual upload in local validation.

No migrations or deployed persisted formats. Existing client runtime/consumer
contract unchanged. Registry versions immutable; recovery checks state before
retry, never moves tag or replaces a version, can disable workflow/trust binding.
Current prior source review/history report retained; full final series will be
provided after scoped workflow commit. README is a separately requested user
follow-up after first publication; workflow is a distinct new execution package,
not a repeated source/provenance update. No redundant update stream intended.

Implementation complete and committed: 091bd70954d270f3e575a71a8a5a1884eed2eccd,
parent c4a0f597cd3602e28ae11846962e2d1e07a0c1ff,
tree 1ebeda04321c99705fb98d6529ff0c39e9d72a7e. Clean worktree/index.
Exactly three scoped files, 194 insertions/1 deletion. Full client series above
neutral b67a3ba5eef89b2bd6533050aa8769aaa0574114 is f88d86a package,
62753f0 generated, c4a0f59 separately requested user README, 091bd70 Actions release.
HaveAPI full reviewed series 5266481..9e4 unchanged. Retain all prior review
conclusions; explicitly assess whole final series and no migrations/repeated
streams for client readiness. These follow-ups are separate user-requested
README and release capability after initial implementation publication.

Quick evidence: Actionlint 1.7.12 (official checksum verified) and ShellCheck
0.11.0 passed; YAML parse and every inline shell syntax passed. 26 extracted
actual gate/static cases passed: repository/package/tag/version/mode/source,
moved tag/fetch failure, missing secret, bootstrap 404 vs existing crate,
non-404/auth/network/timeout failures, final tag recheck, permissions/token
boundaries. Tests use mocked Git/registry, no uploads or external mutations.
Evidence artifacts/client-release-static/{check_gates.py,gates-result.json,workflows.json}.
Lead writing pass on release docs accepted before commit. No Cargo/source
matrix repeat needed for unchanged source; after review fresh watcher owns
exact-head Actions CI. No registry upload until owner prerequisites met.
Official latest action refs verified from official GitHub repos: checkout
v7.0.1, install-nix-action v31.11.2, crates-io-auth-action v1.0.5; new release
workflow pins exact SHAs. End-to-end OIDC/approval/upload cannot be tested
before environment/default installation/registry bootstrap setup.

