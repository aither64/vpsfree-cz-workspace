# Catalog compatibility correction

Base: published/deployed `075fe6f34e66710ee09ae04fcec49a13bc6bdfb7`.
Head: `558be8715063cb29f262aa4d26e8d6612350583c`.
Tree: `494626ff95a29f67d2c0649135ad195ec2ac11f5`.
Additive literal parent; no rewritten consumed history or migrations. Eleven owned
paths, 656 insertions/17 deletions. No receipt/state/launch or protocol format change.

`ReadInitialStart` uses the owning schema1/2 complete ancestor codec, requiring the
named root, starting phase, original revision1 and no predecessor. The shared web
helper joins the ready journal's immutable generation, validates the unchanged
intent against that original immutable package, and permits only additive model
inputs/model evidence metadata in the selected catalog. Provider/account/route/
model/default/fallback fields and installed model bytes remain constrained; current
policy support is checked without recomputing saved policy digests. Both retained
gates use the helper. Initial/incomplete validators are unchanged. Same-catalog
admission does not acquire the new original-package dependency.

The technical guide paragraph is the lead's supplied final prose. Production
worker/SDK, native image evidence, generic file upload behavior and user sessions
were untouched. The live request remains `4ee92850-29a7-468f-9473-1fb3d82b816f` with
expected predecessor `ec93a842c5cd8a59f32460cf3c5f1ffcf6d9876444fed876cd80952d4377d9af`;
only the lead owns later recovery.

## Verification

All Go commands used the retained declared shell
`nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command`.

- `quick.log`: focused `TestReadInitialStart*` and
  `TestPiReadyCatalogAllowsOnlyAdditiveInputsAndModelEvidence` passed (watcher25s).
- `run-focused3.sh`/`joined3.log`: existing actual
  `TestPiReadyUpgradeCLIHTTPKeepsOriginalReceiptAndGenericFileContinuation` passed,
  test16.62s/package16.688s. Real loaded fixture catalog A→B, ordinary CLI→UDS HTTP,
  preparing interruption/portal restart, same-request recovery/repeat, actual
  attachment ACK/Load/publication, zero new Create/Send/Configure during upgrade,
  unchanged original intent/journal/evidence/preparation/receipt/history/settings,
  schema2 root ancestry, both retained gates, full/page/reload and later generic
  continuation. A/B use the existing fake-host/provider worker boundary; this is
  not another production model/image qualification.
- The same original batch failed only provenance/endpoint: fixture https→http
  replacement was a no-op on the actual http input. Other provenance cases passed.
  Fixed the fixture to change parsed baseUrl and assert changed bytes; affected
  endpoint/sampling selectors passed, package0.200s (tool session80208).
- Added loaded-current account/route/settings shared-helper refusal cases passed,
  package0.343s (tool session34269). Actual HTTP refusal cases separately assert
  bad original generation/intent/incomplete journal cause zero reservation/host
  effects. Pure relation tests cover other provider/model/thinking/tools/default/
  fallback/removal differences. No claim that every pure case ran a full HTTP
  upgrade. No duplicate successful composed upgrade was run.
- Gofmt output empty; unstaged and staged `git diff --check` passed. No hook
  framework is declared/configured in this repository; normal Nix Git commit.

Original `joined.log` setup failure (missing B, no upgrade) and `joined2.log`
setup failures (112-byte Unix socket pathname and null fallback fixture) remain.
Store disappearance cause was not established; unchanged local bytes were re-added
to the same paths and retained with ordinary own per-user roots. No evaluation or
build occurred. Existing directory-FD socket convention and explicit empty
fallback before initial freeze corrected the fixtures without production changes.

Watcher3 initially claimed artifacts that it had not redirected. The same watcher
recovered its exact original tool-captured output from completed session31953 and
saved `joined3.log`/result without rerun. These are reconstructed captured output,
not original redirected files. Result JSON's elapsed16428ms reflects its reported
tool wait and is not asserted as total command time; Go's actual test timing is
reported above. All operation-owned handles are joined.

Source/index window was positively released to implementer1 after the commit;
its four browser/upload paths were not staged. Lead owns grouped affected review
with that independent fix and any later publication/pin/build/live recovery.
