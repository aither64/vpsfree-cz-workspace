# Native publication readiness

Read-only investigation by implementer3, accepted by lead 2026-11-03. No workflow
dispatches, tags, releases, credentials or registry/auth settings changed.

Both client repositories have active native release.yml workflows and enabled
Actions. GitHub release environments require reviewer User aither64, allow
self-review, and restrict deployment to tags v*. Human release-environment
approval is therefore required after jobs reach that gate.

## Rust

Workflow ID392586616; existing crate vpsadmin-client owner aither64. Prior native
run https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/40133192469
succeeded via bootstrap; OIDC steps were skipped. Bootstrap secret metadata
still exists, its value was never read. Current trusted publisher binding is
private and not established by that old bootstrap run.

Owning guide docs/development.md:207 requires crate owner setup of trusted
publisher owner=vpsfreecz, repo=vpsadmin-rust-client, workflow=release.yml,
environment=release; then revoke bootstrap token and delete its GitHub secret.
User replied in this conversation: "Configured; bootstrap token retired".
Treat required Rust owner setup/retirement as confirmed; no duplicate approval
needed for that prerequisite. Native environment publication approval remains.
Existing crate cannot use bootstrap again; OIDC has no token fallback.

After approved integration and matching tag, expected native command:

```sh
gh workflow run release.yml --repo vpsfreecz/vpsadmin-rust-client \
  --ref v0.2.0 -f authentication=oidc
```

Then user approves GitHub release environment. Workflow reruns native CI and
publishes with cargo publish --locked. Publication is unattempted.

## TypeScript

Workflow ID397566387. NPM_RELEASE_ENABLED=true. Existing package maintainer
aither64. Previous native run
https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41538988296
has successful build+publish, providing historical evidence of working OIDC.
Current private npm publisher binding is not directly visible; no observed
activation blocker in GitHub metadata. Do not add speculative new confirmation.

After approved main integration, matching v0.4.0 tag push triggers publication;
manual workflow dispatch is build-only. User approves release environment.
Workflow publishes immutable build tarball after checking receipt; no rebuild or
repack of accepted publication artifact. Preserve original run/artifact/receipt
and reconcile registry state before retrying any uncertain failure.

Expected npm binding: org=vpsfreecz, repo=vpsadmin-typescript-client,
workflow=release.yml, environment=release, direct-publish permission.

## Limits

Read-only GitHub workflows/permissions/environment/policy/activation metadata,
existing run-step results, crate owners and public npm maintainer information.
No secret values were queried or emitted. Exact candidate versions and reviewed
heads must be refreshed at execution. No publication or default integration
approval is implied by this readiness receipt.
