# Portable KB review remediation

The two Important findings from the original K93/D51/Ed207 committed review are
implemented in K68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e. Root inspected the
13-path correction, accepted focused native evidence and consolidated it into
K's owning runtime commit. New physical lock plumbing still needs the committed
affected-lane reviewer rerun; package/VM readiness is not asserted here.

## Checked behavior

Capture retains the same open file description flocked by its fixed Ruby helper.
Only the helper inherits that descriptor. Both copies close without LOCK_UN;
the writer closes last after browser/SSH/cluster/helper cleanup. Combined lease
cancellation and staging/publication checks prevent later work after observed
loss; the retained flock excludes competitors during synchronous writes before
loss events can run. Already-issued operations/writes are not rolled back.
Validator's writing child retains its existing shared-description protection.

Update resolves replacement SSH endpoints and rejects changed hosts/ports before
candidate preparation, journal/phase changes, builds/import or predecessor stop.
Retained host-key trust is not rebound. Same-endpoint updates remain supported.
The owning contract paragraph was reconciled by root under the writing skill.

## Focused checks

Fresh watcher kb_runtime_review_fix_quick2 ran the immutable command once and
reported exit0, about20seconds, no remaining owned process or cancellation.
Root inspected all five aggregate/step exit receipts, native TAP/Minitest, actual
toolchain and the unchanged source freeze. 29 Node tests passed, with zero fail,
cancelled, skipped or todo; the existing proxy teardown also exited0. Runtime
has24runs/159assertions and zero failures/errors/skips. Syntax/ShellCheck passed.

Decisive cases pass: helper death during actual blocked synchronous PNG rename
cannot admit a competing capture, including controlled browser cleanup; normal
helper close and abnormal exit retain writer exclusion; writer death and
validator-wrapper death respect last-close release; unrelated children and actual
cluster/SSH fixtures do not inherit the lock; pending/readiness/known-loss windows
and CS/EN merging preserve their boundaries. Three changed endpoint preflights
preserve the old files/inodes/credentials/run/claims, and the real trust method
accepts the same endpoint/key while refusing changed prefixes or keys.

The owning K93 shell used Ruby3.4.9, Minitest5.26.1, timeout0.4.3 and Node24.18.0;
effective gem/module/executable paths are Nix store paths despite hostile ambient
Ruby settings. Native receipts are kb-runtime-review-fix-quick2-*.log/.exit.
The exact .sha256 manifest is24c56e5edaeb6ce697991d06b44ab4ceea5281ae8b80cb1789ad488bde67a2a0.
The watcher's report incorrectly sought manifest.json; that file is not the
packet format. Root independently checked the actual .sha256 before/after and
accepted its unchanged bytes. Provisional quick1 remains unlaunched preparation.

## Committed tree

Normal root commit ran in the owning Nix shell after empty-index/owned-path,
active-hook/framework, message, frozen mode/byte/diff and fresh default guards.
No hook framework or custom hook was declared; ordinary hooks were enabled.
A separate index reconstructed the exact expected tree before actual staging.
Final tree and original93-to-final correction equal the staged reviewed patch;
each committed blob equals its frozen SHA. Worktree is clean.

The whole K series remains exactly a50f8c1a11ea642edf823f04521f9eaa97132fd2
then68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e, no merges or leftover fixups.
The first pin commit is unchanged. No DB migration/state/connection schema,
lock/input, fixtures, VM scenarios, inventory or protected images changed.
Old source/history/tree/full diff, correction and range-diff are retained under
kb-runtime-review-fix-consolidated*. D51 and Ed207 are unchanged.

Canonical committed bin/check passed at the exact corrected head, exit 0. It
includes runtime 24/159, closure 12/51, pinned driver 4/20, export 4/18 and strict
60-concept/120-variant/120-PNG validation. The worktree and input hashes remain
unchanged. Exact K68 publication passed using the verified old93 feature lease;
remote head and clean local state were rechecked. Exact E K-pin refresh, affected
review and package/runtime/image proof remain. Synthetic guest/browser transport is not
live/rendered proof.
The canonical published source receipt is
`/nix/store/3l8p07gyra3xfmpqsdadmlc4m3maw90i-vpsfree-kb-runtime-source.json`.
Root verified its exact revision, unchanged lock/fixture/input identities and all
54 extant changed Git blobs against the immutable source. Bounded queued and
in-progress CI inventories had no superseded same-branch candidates; no
cancellation or CI wait occurred. The copied cancellation repository argument
was corrected before that helper's first launch.
No default integration, activation, actual cluster operation or production KB
write follows from these receipts.
