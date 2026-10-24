# Accepted-fork attempt 2: environment preparation

Prepared only. Lead selects a fresh operation watcher; implementer0 has not run
this wrapper, Nix command, compiler or integration. Source and test assertions
stay frozen. Owner1 remains sole B Git owner.

Completed attempt1 failed before tests: runtime/cgo could not find gcc in PATH.
Raw Go build-output is in I-B1/accepted-fork-attempt-1/stdout.jsonl, not stderr.
Exit1/wall1.104s, zero passes and all21 required leaves missing. The explicit
Nix shell declared Go, Ruby and Git only. Add nixpkgs#gcc from the same locked
nixpkgs input; no CGO-disable or source/test changes. This prepares the missing
tool and does not establish that compilation or the fixture passes.

Original packet, wrapper, watcher logs and attempt1 streams/result are hashed
in accepted-fork-2-preservation.json and remain immutable. The new wrapper
refuses session/env mismatch, disabled cgo, changed original manifest/fixture
bytes or any head/tree/dirty-source mismatch. Runtime read-only Git guards
require B45e14be3d34a9ca2d3b418c310da927351b7f330 and tree
edb3f41dec072a44e03a4f4a7a4c4e8894b440f4. No Git commands ran in preparation.
Exact fixture hashes were rechecked directly against the original packet.

After lead release, the fresh watcher runs ONCE from canonical session tracking:

```sh
python3 accepted-fork-source-lock/accepted-fork-2-command.py
```

Verify script/brief hashes from accepted-fork-2-preparation.json first. Do not
precreate backend-successor/I-B1/accepted-fork-attempt-2. The unique output is
still absent. The wrapper records raw streams/exit before checking all21 exact
leaves, all3 topnames, package pass, zero skips/fails/missing cases and unchanged
source/evidence. First environment-corrected fixture runtime remains unmeasured;
expected<10s excluding compile, rendezvous<=5s, Go45s unchanged. Nix/compile
is uncertain. Monitor under the installed fresh Luna/low policy; no duplicate
run, diagnosis, retries, source edits or other verification. Escalate failures,
source/output conflicts or unexpected kernel builds to lead. No native/VM/full/
CI/browser/live/deploy/claims/lifecycle operations. No CI-holder inference or
waiver of historical9f/207/e7 failures.

Exact child CWD: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace/portal`

```sh
nix shell --inputs-from .. 'nixpkgs#go' 'nixpkgs#ruby' 'nixpkgs#git' 'nixpkgs#gcc' -c go test -mod=readonly ./internal/web -run '^(TestAcceptedForkSourceSharedLockRefusalAndReceiptRecovery|TestCreationFastSourceLockDoesNotWaitForLifecycleMutation|TestCreationReceiptRubyInitializerContract)$' -count=1 -timeout=45s -json
```

Only GCC was inserted into the original argv. ast.parse passed without
executing/importing the wrapper; all21 original manifest entries and both
fixture hashes remain exact. See accepted-fork-2-preparation.json for all hashes
and limits.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/)
