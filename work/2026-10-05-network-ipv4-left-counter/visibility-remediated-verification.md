# Final visibility verification (2026-10-07)

Final heads: V `cc3337d0a2699a8b28a0327bbee5ef62f3fbe166`, W
`e4c49bcdc91b33b7f644a2f125231cb413cf4bf4`, C
`b217e0f0a74b45fe2a95fcc79c2eb646f21248ce`, K
`609fd8a0070235339a4ddb567d905e466776d6a8`.
[Inventory](visibility-remediated-inventory.json) records each complete series;
`visibility-remediated-{v,w,config,kb}.diff` and `.history.log` retain full
comparisons. The original independent report and packet keep their original
snapshots. Root's step-9 disposition is in
[review findings](visibility-review-findings.md).

## Completed local evidence

The five visibility resource files have 226 full-mode examples with no failures,
pending examples or outside errors. Core evidence comprises 223 unchanged passes
plus the exact three corrected examples; scoped ID parity is recorded in
[example parity](visibility-example-parity.json). Both modes of the entire
network_write_spec now pass all 29 examples; native IDs agree. Scoped syntax and
lint passed. No product change was made to satisfy those corrected assertions.

Normal hooks passed on the V amend. The only old-to-new V difference is the
network_write_spec name/list assertion correction. The sole feature migration
and schema remain unchanged from the original API commit. Generated C histories
and the full lock graph were inspected; only selected backend locked revision,
hash and time change from the reviewed C snapshot. W's identity/follows and all
unrelated fresh-base inputs remain exact. K's five records agree with V, and
fresh-shell static checks used `/nix/store/dx2z2iz71vrcw36k3zsic2h99ag5c5ki-source`.
The K suites passed 8/50, 10/22, 38/112 and 4/10 runs/assertions; inventory remains
60 concepts, 120 variants, 66 CS and 61 EN page references, 120 PNGs. Existing
PNG bytes and fingerprints are unchanged.

The K commit helper completed and saved exit 0. The outer login shell then
reported an unset variable in `/etc/bash_logout`; the saved operation status,
commit, final receipt and clean tree prove the commit succeeded. Subsequent
capture wrappers use `login:false`, as covered by the existing workspace note.
No commit or check was repeated to compensate for shell logout.

## Feature publication

V, C and K exact feature refs are published. C/K publication and bounded
superseded-CI steps each saved exit 0 in `visibility-remediated-{config,kb}-`
`{publish,ci}.{log,exit}`. Their published SHA receipts match the committed heads.
Cancellation of old K run 37539847534 was submitted; no current-head or other
branch run was canceled. The publication watcher reported overall exit 0 in
about 54 seconds but did not capture the requested outer aggregate log/exit;
this account uses the retained inner receipts and exact published-SHA proofs.
The first attempt stopped before mutation because the fresh watcher lacked
`dev-session` in PATH; the second wrapper declares the required tool paths.
No checks or commits were repeated.

## Current runtime phase

Fresh watcher `visibility_final_runtime` owns the immutable final-head batch;
its aggregate is `visibility-final-runtime-operation.log/.exit`.

Completed: `vps/migrate-with-data-check` at final V passed, selector exit 0.
The named data-preservation example passed in 366.82 seconds; the runner reports
one successful test and 1081.86 seconds for the test script. The exact scenario
retains the payload checksum/sentinel, destination-running/source-removal checks,
assigned IP identities and disabled-network flags. Runner cleanup completed
before the wrapper advanced. Logs/status: `visibility-vm-migration.log/.exit`;
detailed owned state is recorded in `visibility-vm-migration.state.path`.

Completed: `storage/restore-after-reinstall-with-descendants-remote` at final V
passed, selector exit 0. Its named root/descendant-preservation example passed in
633.83 seconds. The exact scenario retains root marker, child/grandchild data,
checksum/mount checks, assigned IP identities and disabled-network flags. Cleanup
completed before the wrapper advanced to legacy inventory. Logs/status:
`visibility-vm-restore.log/.exit`; detailed owned state is recorded in
`visibility-vm-restore.state.path`.

Failed: `webui#admin-cluster` at final V, selector exit 1 and aggregate exit 1.
The network-availability scenario could not find its expected confirmation form
within 20 seconds, before the first toggle. The browser-flow example failed in
144.54 seconds; the script failed in 513.74 seconds. The first-failure wrapper
stopped, so none of the 12 C builds ran. The watcher-owned PTY ended; no process
remains from this batch. Implementer0 is tracing the capability/rendering path
from source and retained logs before a bounded correction or retry. Root found
that the real HaveAPI ResourceInstance has __get but no __isset; checks using
isset on enabled therefore treat real response fields as missing. The existing
stdClass fixtures do not exercise that client behavior. Implementer0 is
preparing a narrow correction and real-client coverage for all introduced
network-state presence checks, without changing the client or backend policy.
The accepted correction includes state badges and detached-address assignment
hints affected by isset/null-coalescing on magic fields. A nullable helper will
read explicit client attributes, preserving enabled, disabled and missing
old-API states; advertised input parameter checks remain unchanged.
The first quick batch (quick3) stopped at four test-only arrow-function spacing
offenses, formatter/aggregate exit 8. No behavior test ran. Root inspected the
actual formatter diff and assigned only those four lines for correction. The
watcher also misread an abbreviated repository-guidance path; subsequent briefs
will name its full absolute path. This attempt supplies no PHP-suite pass.

Quick4 completed all four gates and aggregate exit 0. Native JUnit records
104 tests, 515 assertions, no errors, failures or skips; the real-client
network suite has seven tests and 116 assertions. PHP 8.4.24, HaveAPI client
0.29.6 and PHPUnit 13.4.1 were recorded. One deprecation was reported. A
known-short seven-test diagnostic run with --display-deprecations passed and
identified the existing implicit nullable constructor argument in
webui/lib/pagination.lib.php:151, unchanged from base c4d9b50f. No source change
or suppression was made for it. The four source paths remained frozen.

Logs/status: `visibility-vm-legacy.log/.exit`; runner state is recorded in
`visibility-vm-legacy.state.path`. Browser trace/screenshot/error-context paths
reported by the guest are not present on the host, so this record does not
claim those artifacts were exported.
The normal VM sizes and 8 GiB reserve remain unchanged; fresh capacity guards
require at least 32 GiB available memory/shared memory for each 24 GiB scenario.
No local kernel build or unrelated lifecycle operation has been reported.

## Limits

W's shared OPTIONS capability lookup can outlast its suggestion timeout; this
Advisory is accepted and recorded, with no admission bypass. W retains its older
baseline and proxy-addr 2.0.7; independently advanced main includes the separate
patch, so current-release/deployment reconciliation is still needed. Prior
React/browser/admission/configuration receipts remain tied to their recorded
heads and unchanged-byte proofs rather than being relabeled as new execution.

Two member-IP-list PNGs remain pending until a supported owned capture runtime
is available. No raw legacy cluster helper, state-copy adapter or forged
ownership record is used. Static checks do not certify the new Enabled column
in those bitmaps. No production revisions, writer inventory, migration
consumption, counter contribution or retirement list have been established.

Branches remain unmerged and undeployed as directed. Workspace instruction
integration was the sole authorized default integration. No PR management is
performed outside the W repository. No production or lifecycle operation ran.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
