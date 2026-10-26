# Integration preparation ready; Git window relinquished

D prepared a new clean detached target checkout at exact remote master
`39909094649b1d14a23f00615775ca7136acf4fd`:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-context-copy-performance-tests/haveapi-approved-master-integration`.
The original feature remains clean at
`38ecca75edaf797d048fb36c6a50ea7e05eb50a9`, tree
`c6cf3c6809ab52b3b2fba57c117139c7bcff6a37`. Canonical SSH fetch and remote
observations match this pair. All eight commits and combined diff SHA256
`4fe1fae97def3dcbb7363b4a00e4fd3bff4e30fd775af17c2792dedb1daeb08d`
match the reviewed inventory; b85 remains an ancestor.

[Final readiness and hashes](ready.json) supersedes the incomplete status in
[initial preparation receipt](preparation.json). Initial capture-comparison
refused the busy session-command mutex after target preparation succeeded; the
single bounded [capture retry](capture-comparison-retry-receipt.json) succeeded
ambiently, preserving exact base399/head38. Target creation and other preparation
commands were not repeated. No operation remains running.

## Concrete runtime launcher

The lead can run normal Git commands through this launcher after acquiring and
freshly checking the approved HaveAPI claim. These commands are prepared only;
D did not execute a merge or push:

```bash
prep=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-context-copy-performance-tests/package-d-integration-preparation
target=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-context-copy-performance-tests/haveapi-approved-master-integration
bash "$prep/prepared-runtime.sh" "$target" git merge --ff-only 38ecca75edaf797d048fb36c6a50ea7e05eb50a9
bash "$prep/prepared-runtime.sh" "$target" git push origin HEAD:refs/heads/master
```

[Launcher](prepared-runtime.sh) SHA256:
`e86e9ff419397bf54b1c93ebd1d4c2a3e0c1296e3b8395ed58a7258fff829c20`.
It uses only declarations from the already-realized repository mkShell output
`/nix/store/0k9907vhyha3rdfznk7159dn226gyyz6-haveapi`, bound to retained
derivation `/nix/store/ms7sialdgqsap5c6fbrm4hnlmgdf1dg9-haveapi.drv`.
Exports SHA256 is
`998368e5cd1a44e9a25ea05359670cbf0e0057541e6c2b89b03d490f9ef4f305`;
original mkShell output SHA256 is
`891d399f938704f4ae321ac2cd35c965c0f1f41db8a3cb5353b64f746456779f`.
The ordinary shellHook runs with `HAVEAPI_RELEASE_TOOLS_ONLY=1`, which skips
installation only. Runtime temporary paths replace derivation-only `/build`
paths; inherited Bundler state is cleared and the existing lock is frozen.
No Nix evaluator, realization, substituter, build or installer is invoked.

Actual Git is
`/nix/store/2k05jnr38sryn0fnvlrmjrshxbphj3jp-git-2.56.0/bin/git`;
Ruby is
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`.
Overcommit0.73.0 and the existing prepared root lock are reused. Target `.gems`
and ignored `Gemfile.lock` link to the session's prepared feature inputs; no
dependency resolution or new lock occurred. Both bundle readiness checks pass.
Invoke `/home/aither/bin/dev-session` ambiently, outside this Ruby environment.

## Normal hooks and boundaries

The common Overcommit hook launchers are present/executable and signatures stay
enabled. All five inspected launchers have SHA256
`a81910ebf3fd7a535b81cc3497d14bbed38190d6e2a6473ee71f04634c516cc5`.
Configuration, plugins, Gemfile and Nix inputs are identical on base and candidate;
existing trusted signatures already match. No hook installation/signing or shared
Git configuration change was necessary. Target checkout creation and explicit
normal post-checkout framework invocation both exited0. Hook inventory is retained
in [target readiness output](target-runtime-and-hooks.stdout).

Normal merge/push invokes post-merge/pre-push Overcommit. Their individual checks
are disabled by the existing repository/default configuration; preparation did
not disable them. Enabled pre-commit checks remain unchanged. No hook bypass or
signature override was used. Git may return0 after a failed post-merge hook: the
lead must inspect actual hook results before pushing. Git trace2 event logs can
retain the framework child exits during the actual merge and push.

The selected installed coordination guide matches the retained guide exactly;
identity, saved roster and implementer3 workspace-write access are verified.
D relinquishes the exclusive Git preparation window. The lead owns fresh claim,
target check, merge, ordinary master push, remote proof and immediate release.
No claim, merge, default ref push, rebase, source edit, test/CI, installation,
cleanup or lifecycle action was performed. Feature branches and target checkout
are retained.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/
