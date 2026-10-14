# Legacy network availability: real PHP client correction

Prepared only; no check, commit, publication, pin, VM or lifecycle action has run.
This packet supersedes the unlaunched quick1 proposal; its artifacts remain intact.
The lead owns execution and interpretation.

Exact checked source parent: `cc3337d0a2699a8b28a0327bbee5ef62f3fbe166`.
Branch: `2026-10-05-network-ipv4-left-counter`.

## Diagnosis and scope

HaveAPI PHP client 0.29.6 is locked by the existing Composer files. Its real
ResourceInstance stores response attributes, exposes attributes() and __get(),
and has no __isset(). Therefore isset(resource->enabled) fails even when the
stored value is true or false; ?? on that magic property also takes its default.
Action::getParameters() returns stdClass, so metadata presence checks are valid.
The retained services log confirms that the Network availability heading was
rendered before the form guard returned. No page snapshot or token is copied here.

The draft is exactly four paths in the adjacent .paths and .diff. A nullable
network_enabled_state helper accepts ResourceInstance explicitly and reads its
attributes(). True, false and missing remain distinct. Network list/editor,
IP inventory/detail labels, detached assignment links and the stale assignment
form reuse it. Metadata guards, approved gettext strings, assigned removal,
VPS/host links and missing-field old-API behavior are retained. No client or
backend changes are included.

## Regression source

The existing NetworkAvailabilityTest now has seven methods. Its retained
selector case still checks advertised-only filtering. The stale form case now
uses the real client. Five new methods cover the real network editor's PUT
capability metadata and both target states; its absence when capability or
output is missing; the specific enabled inventory cell; IP inventory/detail
state and detached-action behavior; assigned service/VPS/host links; and enabled
or missing-field assignment forms. Only HTTP transport is replaced. Actual
HaveAPI action, response, resource and list interpretation and XTemplate rendering
run. The class disables parent global-state preservation in its existing isolated
PHPUnit processes so other specs' CSRF doubles do not replace the real helpers.

## Exact proposed execution

From the verified session context:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/legacy-network-client-quick2.sh
```

The immutable wrapper verifies identity, exact parent/branch, clean index,
exact four changed paths and frozen SHA256 before and after each sequential step.
It self-captures aggregate output/status and stops on first failure. The root
Nix shell supplies scoped dry-run PHP formatting; the WebUI Nix shell supplies
four PHP syntax checks, the full existing PHPUnit suite and locale health. No
locale generator or dependency installation runs. PHPUnit uses native JUnit
XML plus logs/exit and keeps its cache beneath tracking; it does not write a
result cache into the source worktree. Actual executed counts remain pending.

The protected tree inventory and HEAD diff guards preserve all migrations/schema,
VM/browser scenarios, Composer locks/manifests and catalogs. There is no new
runtime/test file or CI-selection change. The existing PHP directory discovery
covers these regression additions.

After passing checks, root will own normal-hook consolidation into the original
legacy commit, exact feature publication/pins and affected-lane final review.
Only the failed legacy selector and twelve configuration builds may be selected
again after review and corrected exact pins. Previously successful migration/
restore selectors are outside this correction. External KB pin/static impact
and existing selected bilingual captures remain under root coordination; this
correction adds no semantic ID, approved wording or capture concept.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/

The lead-requested explicit ResourceInstance contract removes the plain-object
fallback. Existing NetworkAvailabilityTest callers already use real client
instances; the selector metadata stub never invokes the helper.
CsrfStateFormsTest reaches its deliberate exception before metadata/form access,
so no fixture changes or product compatibility shim are required.
