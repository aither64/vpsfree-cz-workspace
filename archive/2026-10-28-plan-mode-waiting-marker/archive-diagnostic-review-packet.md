# Archive hydration diagnostic review packet

Implementer0, 2026-10-29. Direct bounded lead brief after the exact isolated
archive acceptance repeated its initial hydration failure. No lifecycle action,
production source edit, timeout change or long test run by implementer.

## Committed and published delta

Repository dev-workspace; feature branch `2026-10-28-plan-mode-waiting-marker`.
Diagnostic range:
`5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3..08f3dbb92bc8585929edee85a824d44dfb3b0846`.
Commit `08f3dbb9 test: diagnose archive lifecycle hydration timeouts` changes
only `test/archive_lifecycle_browser.cjs`: 36 insertions, 10 deletions.
Fetched origin/master before commit; still cc0d452a, rebase was a no-op.
SSH publication and exact remote feature SHA verified; worktree clean and portal
comparison captured at 08f3dbb9. No default-branch integration.

New diagnostics track at most eight exact `/operation` GET requests. Request
initiation, response and failure receive monotonic elapsed timestamps; failure
reports Playwright's numeric request timing. This distinguishes no emitted
request from a request lacking a response without logging request/response
bodies, headers, authentication or query data. Other requests keep their existing
last-40 failure trace. The failure-only page snapshot records readyState,
visibility, focus, app script tag presence and the existing control selectors,
now capped at eight elements and 1200 characters per element. The existing
phase/errors facilities remain. A 1500ms failure-diagnostic bound reports
unavailable/timeout rather than masking the original failure indefinitely.
App-script tag presence alone does not claim execution or hydration completed.

The original 30000ms Playwright response deadline, action selection, archive
click/POST, receipt checks and acceptance assertions are unchanged. The 1500ms
bound applies only after a failure. No browser production JS or runtime pin changed.
No new API/protocol/state/migration; no production compatibility boundary.

## Existing failure evidence

[Isolated log](logs/archive-isolated-check.log) repeats phase `open page` with
no page errors and no archive click/POST. It explicitly reports KVM:
`Hypervisor detected: KVM` (line 62), paravirtualized KVM kernel (132), systemd
virtualization kvm (472/689). VM boot wait is 43.19s (870). Browser invocation
spans guest monotonic 130.225438–196.742399s. These observations do not prove
host load or explain the missing operation response; no missing-acceleration
claim is supported. Preserve the original [diagnosis](local-flake-failure-diagnosis.md)
and first/isolated failed artifacts. No blind rerun was launched.

## Quick checks and history

Using the flake's pinned interpreter, `nix shell
/nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source#nodejs -c node --check
test/archive_lifecycle_browser.cjs` passed exit 0. `git diff --check` passed.
The checked source was committed unchanged as 08f3dbb9; no successful unrelated
check was repeated. No hooks/framework are declared; only inactive samples,
no bypass. Focused diagnostic commit uses git commit -F temporary message file.
Affected-lane independent review is required before the next long VM check.

Complete dev-workspace branch range:
`cc0d452a0653a112c8a013492c1734d9554bb909..08f3dbb92bc8585929edee85a824d44dfb3b0846`:

```text
5f4f1c1c portal: use passive request identities for attention
08f3dbb9 test: diagnose archive lifecycle hydration timeouts
```

Two commits have distinct functional and diagnostic purposes. No obsolete
iteration history or intermediate dependency pins remain. The single codex-web
dependency stream remains pinned at 9d337b70987fdf1dd42a5d8efff31f755a122550;
no dependency update in the diagnostic successor. No migrations, release or
deployed migration lineage. Full branch diffstat is 11 files, 145 insertions,
45 deletions. codex-web remains the reviewed one-commit range
f6f4a187509b3bebfc81585c535be856eaab0d04..9d337b70987fdf1dd42a5d8efff31f755a122550.
The production target remains reviewed/built dev-workspace 5f4f1c1c. Workspace
and configuration pins were not changed. Diagnostic-only branch publication
does not itself certify production equivalence or deployment readiness.

## Minimal diagnostic fixture against exact reviewed runtime

Existing test parameterization supports the requested composition directly.
The Nix test definition is byte-identical in runtime and fixture commits
(SHA-256 `201d90814ff4b7099c626a3a83fa4e73b5ecb7d608c566bc9e9ba54ab3f387c2`).
Relative `../../test/archive_lifecycle_browser.cjs` is lexical to the fixture
import, while machine host module and `devWorkspace` come from runtime 5f4f1c1c.
No override framework, copied harness or production repin is involved.

Exact expression (also retained as [raw recipe](logs/archive-diagnostic-recipe.nix)):

```nix
let
  runtime = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/dev-workspace.git?rev=5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3&ref=2026-10-28-plan-mode-waiting-marker";
  fixture = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/dev-workspace.git?rev=08f3dbb92bc8585929edee85a824d44dfb3b0846&ref=2026-10-28-plan-mode-waiting-marker";
  pkgs = import runtime.inputs.nixpkgs { system = "x86_64-linux"; };
in
import (fixture.outPath + "/nix/tests/session-archive-lifecycle.nix") {
  inherit pkgs;
  self = runtime;
  devWorkspace = runtime.packages.x86_64-linux.default;
}
```

Evaluation only: `nix eval --impure --json --file
logs/archive-diagnostic-recipe.nix --apply
'check: { drv = check.drvPath; driver = check.driver.drvPath; }'`.
No build or acceptance VM was run. Exact resulting derivations:

- Diagnostic acceptance:
  `/nix/store/w3pwbnfc8afpc6d8rgl8ylplwjy24xn2-vm-test-run-dev-workspace-session-archive-lifecycle.drv`.
- Diagnostic driver:
  `/nix/store/gr2j8vakpy61jhbm2vk5cfc9vh1y74bb-nixos-test-driver-dev-workspace-session-archive-lifecycle.drv`.
- Shared reviewed application:
  `/nix/store/im2nqqi35ll7fdz9d6l66z64p5rb7hjs-dev-workspace-0.2.0.drv` ->
  `/nix/store/bipq4qapx80y2jb9q2y128dbj7ndnyb4-dev-workspace-0.2.0`.
- Shared runtime source:
  `/nix/store/wdh3nqarvakn0aqs3q4zw479v3lgjr2s-source`.
- New lexical CJS:
  `/nix/store/6bjlyncplwanwm42rc6z35681d791hcz-archive_lifecycle_browser.cjs`,
  SHA-256 `276eddfbce1c3eba3d9522dcaf22524e717b101e25a9c928fe8be8d18d86c38a`,
  equal to the committed file.

Pinned runtime nixpkgs is revision f20cd90e28fe0403873f473b29e42662cd86e8c4,
NAR `sha256-EjZqHKObBfIOeHZnMRVV87HB3pPq/WBkmRJWyFxmZu8=`.
The exact recursive old/new acceptance graphs each contain 6071 derivations,
with 6067 shared, including every machine, app and package/Ruby dependency.
Only four derivations per graph differ: test-script, driverConfiguration,
wrapper driver, and acceptance runner. Python test-script text is identical
after replacing only the exact CJS store path. Therefore neither machine nor
application/package dependency graph needs rebuilding for this composition.

Evidence: [identity](logs/diagnostic-recipe-identity.json),
[graph comparison summary](logs/diagnostic-recipe-graph-proof.json),
[old/new immediate driver metadata](logs/diagnostic-driver-comparison.json).
Exact differing derivation metadata retained as `logs/diagnostic-graph-*.json`.
This establishes test composition identities, not a runtime behavior result.

After independent affected-lane review, lead can assign a fresh watcher the
single exact diagnostic acceptance derivation with `--max-jobs 1` and the
unchanged deadline; no run authorized/performed by implementer before review:

```sh
nix build --no-link --print-out-paths --print-build-logs --max-jobs 1 \
  /nix/store/w3pwbnfc8afpc6d8rgl8ylplwjy24xn2-vm-test-run-dev-workspace-session-archive-lifecycle.drv^out
```
