# Creation refusal diagnostic handoff

The clean local diagnostic commit is `c63fffa67e4678d22d09dbbf56b10f421b51d97e`
(tree `cf519028086aa8ffbe018fca85df7a065ce42445`), directly after reviewed B37.
It is not published. Remote feature remains B37; a fresh canonical SSH fetch and
ls-remote proved default exactly the newly selected `10bb0475`. The next series
must preserve that baseline and select the one final refreshed A before publication.

Nine controlled tests pass in 0.909 seconds in the repository Nix environment,
including standard strace attachment to a disposable process and its original
exit 37. Node, Nix, VM Python and emitter Python syntax pass. Structural checks
prove original browser assertions/timeouts/pauses and VM scenario/browser-call
sequence unchanged. The first controlled run found and corrected unfinished
strace-result parsing; the final nine-test run covers it. No hooks were bypassed.
See [structured receipt](package-b-creation-diagnostics-20261025.json).

Only the creation browser helper, creation Nix VM, one test/support helper and
its quick tests changed. The observer attaches to the existing service MainPID;
there is no product hook, launcher replacement, syscall injection, lock acquisition,
operation retry or timeout adjustment. It traces flock only. New serialization
omits argv/environment, bodies/headers/cookies, raw error text and URL credentials.
The helper caps events, input scanning, matching owners and bundles; diagnostic
failure is recorded separately from the unchanged first operation failure.

The syscall event has exact actor/FD/path/mode/errno and strace timing. Descriptor
identity is explicitly unproved. A later path stat may identify kernel FLOCK rows
at that later instant, with its own delay and missing/truncation markers. It does
not prove the refused FD identity or original holder. Browser monotonic chronology
is temporal context only. Controlled green tests establish observer behavior;
they identify neither original VM holder and claim no naming or archive fix.

Original local and CI failures remain distinct: local plan source EX refusal after
POST 202; CI candidate reservation refusal after successful naming in 681 ms.
Raw originals and separate successful-input receipts remain in the existing
`package-b-creation-37a87a8a-*` artifacts. The local batch did not run archive/full
flake; completed CI archive success is a separate observed receipt.

Preservation is in `package-b-creation-diagnostics-before-37/manifest.json`, the
local `...-before-refresh-20261025` ref, `package-b-before-refresh-20261025.bundle`
and the exact c63 patch. These retain the old four commits/reviews/pins and the
new fifth diagnostic owner before reconstruction. No migrations were added.

The retirement owner is retained unchanged: A872c joins causes on failed Request,
while list/metadata method validation may fail after Request success. B37's two
failed read-only observation boundaries therefore have a distinct responsibility.
Architect0 confirmed this source-backed partial overlap; final real protocol
refusal/attempt/no-archive checks still need the exact refreshed A.

Next: finish the dependency-first forward reconstruction after final A publication,
run the released quick regressions on that exact tree, publish with the explicit
old-B37 lease, and give main the full inventory for independent review. Main owns
all later long/native/VM checks; C stays frozen. No deployment or lifecycle action.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/)
