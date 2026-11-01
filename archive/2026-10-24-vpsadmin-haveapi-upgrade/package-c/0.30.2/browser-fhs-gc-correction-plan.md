# C FHS GC correction: concrete environment-only continuation

No retry launched. Previous FHS environment expression and all application/
browser/source identities remain unchanged.

Confirmed cause: host nix-store-gc-on-pressure.service began09:21:42UTC and
deleted exact wrapper drv/output/rootfs at09:22:07UTC during batch3-fhs.
See fhs-gc-journal.log and fhs-postrun-missing-paths.json. Standard --no-link
realization did not retain this runtime closure. Desktop browsers already
started and all31desktop cases passed; later31mobile cases failed to spawn
with ENOENT, before app assertions. All owned operations/Vite/listeners are
reconciled; no foreign process/service touched. This is runtime collection,
not mobile product behavior. Initial stub-ld62cases and FHS31/31case evidence
are both retained.

Proposed sole change: realize the exact SAME playwright-fhs.nix using
--out-link <records>/fhs-gc-root, retaining a normal indirect Nix GC root
through wrapper/probes/browser run and final evidence capture. Keep the
root afterward; no session/root cleanup needed to complete verification.
No disabling/altering host GC, host runtime changes, browser substitution,
app/fixture/Git edits, security flags or new route. Same pinned Node/PW/1228/
ffmpeg, standard64bit FHS and policy visibility.

Exact setup:
```sh
nix build --file <records>/playwright-fhs.nix --max-jobs 1 --cores 2 \
  --out-link <records>/fhs-gc-root --print-build-logs --json \
  > <records>/fhs-rooted-build-results.json
```
Require same expected wrapper drv/output and NAR; recapture recursive graph/
closure plus prove root symlink and corresponding auto-root registration.
Then repeat only the versions/hash probes under the retained root. Any failure
stops before tests; unexpected kernel build stops/escalates owned setup.

To avoid repeating accepted desktop cases, retain exact31desktop results
from browser-fhs-results.json and run ONLY same nine existing fixture files
with --project=mobile-chrome --workers=2 --retries=0. Other command options,
local Vite/52847/CI1/artifacts and cleared overrides remain as accepted.
Use separate browser-mobile-rooted JSON/artifacts/log/status paths.
If lead requires one combined62case receipt instead, same setup supports
that unchanged2project selection; no such repeat launched without direction.

Before execution recheck cleanf10, all source/lock/wrapper/binary hashes,
capacity/freeport and preserved previous receipts. Parent fallback/CPU60–63/
nice5/Nix1job2cores remain. Capture postrun source/binary/root/NAR existence
and reconcile owned processes/port. Unit/build/Nix/source proofs are unchanged
and need no repeat. An output collected after its completed successful check
does not erase its retained derivation/source/exit proof; no package deployment
or artifact-use claim is made.
