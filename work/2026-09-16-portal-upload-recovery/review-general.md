# General review

Reviewer: gpt-6-astra, xhigh. Reviewed personally; no delegation or project-code
edits. Findings refer to the packet's committed revisions, before remediation.

## Findings

### G1 — Important: temporary resolver failures are treated as successful deletion

- Changed consumer: `codex-web/conversation/assets/uploads.js:314`, commit
  `20680804ac5301b27b2726b99f1ec4d9281a8305` (present at reviewed head
  `5c2c77b4649ec9aa6833ad0b7214f7702733e87e`).
- Provider contract: `dev-workspace/portal/internal/web/uploads.go:60–62` at
  `7bb347ccda2eba302d84fc0529ca6bbd6f4d1bc1`; resolver failures include
  `portal/internal/web/server.go:2410–2412`, `2432–2433`, and `2442–2443`.

The new browser code clears the selection on every DELETE 404. The runtime
already converts every session resolver error into 404, including a superseded
package generation, pending lifecycle operation, and a temporarily noninteractive
session. These failures do not prove that the uploaded file disappeared. A stale
page can therefore discard its only draft reference while the server retains
the file, contrary to the intended retryable handling of temporary failures.

Confirmed with a focused Go overlay test against the actual HTTP handler:
create and complete a session upload, switch the fixture's host-profile symlink,
then DELETE the file. The response is `404 {"error":"Upload scope is unavailable"}`;
opening the file directly through its backend still succeeds. The new browser
contract consequently treats this response as successful removal.

Preserve a retryable non-404 status for transient resolver failures. Retain
404 for proven missing scopes/files, and test the real runtime-to-browser
contract during a package switch or temporary session restriction.

### G2 — Important: a deleted file becomes ready again after a transient storage failure

- `codex-web/conversation/assets/uploads.js:313–320`, together with
  `245–257`, commit `20680804ac5301b27b2726b99f1ec4d9281a8305`.

After DELETE succeeds, `save(next)` can fail while the card remains in `entries`
with `state: "ready"`. The catch calls `failed()`, which saves the old selection.
If that second write succeeds, it clears `persistenceError`; `ready()` then
returns true and `ids()` includes the deleted file. The form enables submission
of an attachment the backend will reject as unavailable.

Confirmed using the shipped module and its DOM fixture, with only the first
post-deletion storage write made to throw. Server file count becomes zero,
draft count remains one, and `ready()` returns true. The committed test covers
permanent write failure, which does not expose this case.

Mark a successfully deleted/missing entry unavailable before attempting the local
removal save, so retaining its card after a storage failure cannot restore
submission readiness. Add a one-time failure regression.

### G3 — Important: a pre-request storage failure loses the known local-only outcome

- `codex-web/conversation/assets/uploads.js:262–265`, together with
  `309–311`, commit `20680804ac5301b27b2726b99f1ec4d9281a8305`.

`create()` changes `creation` to `unknown` before saving that transition. If
this save throws, no POST runs, but `failed()` can subsequently persist the
incorrect `unknown` state. Remove then creates an upload to reconcile an
operation that was never attempted. If the service is unavailable at that
point, the known local-only selection remains stuck behind an unnecessary
network operation.

Confirmed using the shipped module and fixture: let the initial selection save
succeed, fail the pre-request save once, then allow storage writes. There are
zero create calls before Remove and one afterward. Expected: zero throughout.

Restore the prior creation outcome when saving the pre-request uncertainty
fails; retain uncertainty only once the request can actually have started.
Cover this failure separately from lost HTTP acknowledgements.

## Scope and commit series

Reviewed local `AGENTS.md`, plan/state, README changes, implementation, tests,
consumer integration and commit history across all five packet ranges:

| Repository | Base | Head |
| --- | --- | --- |
| codex-web | 882c88ccfbebfb646fb2cafbe9bc6790141b2d13 | 5c2c77b4649ec9aa6833ad0b7214f7702733e87e |
| dev-workspace | 5d853b6b0c2608549a1f0e940c680ccb40a14bec | 7bb347ccda2eba302d84fc0529ca6bbd6f4d1bc1 |
| vpsfree-dev-workspace | b75cc8a6270219ca2fc25c1e292ce030fc33e45d | 471b412a17e5a508aa18f56e0495ff07cda3248f |
| workspace | 94f8add7ca745ae9b35e2ee700e923663a2c5a02 | 54e330b05c9274c242a659cc287454415e812c3f |
| vpsfree-cz-configuration | b6e650ad902482b4c4e66b5a89a4275bed92419e | d7936f735c4850d447cea3a8e43dc50a0d80abd7 |

No commit-split finding. Browser recovery, encoding validation, runtime filename
policy and downstream dependency updates have distinct, coherent commits.
Cache identities, Go module and Nix pins consistently select the reviewed
provider. Existing UUID storage paths, JSON prompt serialization, text rendering,
MIME download formatting and catalog format remain intact.

## Verification and residual gaps

- Two focused Node reproductions failed on the assertions described in G2/G3,
  using Nix-provided Node and a temporary copy of the existing test fixture
  importing the actual committed browser module.
- One focused Go overlay reproduction failed on the false 404 in G1, using
  Nix-provided Go/GCC and the actual runtime handler. No repository test files
  were changed.
- The packet's quick test results were inspected; this review did not repeat
  the entire suite or start long integration tests.
- Real Firefox acceptance of both forms, warmed-cache upgrade/rollback,
  package checks/builds, current-head CI, and live deployment verification
  remain pending as stated in the packet.
- The store's new catalog reopen test checks the new implementation reading
  unchanged records. Actual old-package readability and browser rollback still
  need the planned acceptance evidence.

No additional Blocking or Advisory findings.
