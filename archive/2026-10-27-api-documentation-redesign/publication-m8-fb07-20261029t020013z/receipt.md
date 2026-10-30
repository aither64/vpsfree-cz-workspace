# Final fb07 development-branch publication

Published `refs/heads/2026-10-27-api-documentation-redesign` to
`fb07c1378e4267bdfd54fa8fbfcfc57b6ec53413`, tree
`0e72671b95ef3d0893eb83271c4ef2b78993d57a`, over canonical SSH
`git@github.com:vpsfreecz/haveapi.git`.

Fresh SSH fetch and symbolic-default/heads read matched expected feature
`5114746f3a9f87e91c704147c0d99dd4f0d32f02` and master/base
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`, an ancestor of final HEAD.
The required external511 recovery was absent. Peer committed consumer `59d7623`
pins published511 for its package/services/HTTPS trial; rewritten fb07 does not
literally contain511. Lead explicitly authorized its durable upstream recovery.

One atomic push used `--atomic --no-follow-tags`, exact feature lease
`--force-with-lease=refs/heads/2026-10-27-api-documentation-redesign:5114746f3a9f87e91c704147c0d99dd4f0d32f02`,
and exact absent-ref lease
`--force-with-lease=refs/heads/recovery/2026-10-27-api-documentation-redesign-external-511-m8-final:`.
Explicit full-SHA refspecs updated only the feature to fb07 and created that
recovery at exact511. No existing recovery was overwritten or deleted.
The exact argv, output, exit and elapsed time are in push.execution.json/stdout/stderr.

Fresh SSH readback proves feature fb07, master f6 and these exact recoveries:

| Remote ref | SHA |
| --- | --- |
| `refs/heads/recovery/2026-10-27-api-documentation-redesign-published-a06b-20261028t184526z` | `a06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9` |
| `refs/heads/recovery/2026-10-27-api-documentation-redesign-published35c-20261028t180031z` | `35c1fb964735639c0873aacf078e18569f05f9bc` |
| `refs/heads/recovery/2026-10-27-api-documentation-redesign-published-cefe-20261028t191454z` | `cefe8c5d43277dbaba35632b5239d95a1959cf1e` |
| `refs/heads/recovery/2026-10-27-api-documentation-redesign-external-d67-20261028t204550z` | `d67bebcb37f2d4558a97caa208465147da19dbef` |
| `refs/heads/recovery/2026-10-27-api-documentation-redesign-external-511-m8-final` | `5114746f3a9f87e91c704147c0d99dd4f0d32f02` |

fetch/remote-before/push/remote-after all exited0, elapsed respectively
1.321/1.284/2.989/1.221 seconds. fresh-target-proof.json and remote-proof.json
bind the authoritative before/after refs. Intended remote effects are reconciled;
no retry, rebase, checkout, source edit or additional remote mutation occurred.

Ordinary executable pre-push remained enabled and unchanged, SHA256
`a81910ebf3fd7a535b81cc3497d14bbed38190d6e2a6473ee71f04634c516cc5`.
Normal push completed successfully. Frozen root bundle check passed exit0/0.332s.
Declared immutable Ruby/Git/Bash and normal OS utilities were used; exact PATH,
GEM_HOME, BUNDLE_GEMFILE, BUNDLE_FROZEN=true and unset GEM_PATH are in environment.json.
Root lock SHA256 remains
`d877e06242f07be3dd1f1abef41136901bef26d10b58126d4d37e4068449e96f`.
No hook bypass, tool setup, Nix realization, install, dependency/config/lock change.

completion.json and before/after manifests prove actual HEAD/tree, all908 source
hashes/modes, all2148 protected inputs, logical index entries/flags, empty index,
clean source and every local head/recovery unchanged. The existing23 roots and
root/server/component locks remain preserved under the retained fold/input proofs;
no root or tool mutation was performed. e368/24ec/b869/18b9/e5ea/511/da1/d67 and
older local recovery contracts remain intact.

SOURCE/Git/network slot explicitly RELEASED after readback/preservation and BEFORE
CI observation; prompt lead report fc871218-b966-462e-adf3-f22aa21c537e delivered.
No utility was used or blocked. All owned command handles returned; no active
owned process or uncertain remote effect remains.

One initial CI observation, with no wait, query loop, retry, rerun or dispatch:
`2026-10-29T02:01:18.246774+00:00`, query exit0.

Exact fb07 feature:11 runs,1 success,5 in_progress,5 queued.

| Run ID | Workflow | Observed status |
| --- | --- | --- |
| [40803800834](https://github.com/vpsfreecz/haveapi/actions/runs/40803800834) | clients/ruby RSpec | queued |
| [40803800827](https://github.com/vpsfreecz/haveapi/actions/runs/40803800827) | i18n health | in_progress |
| [40803800814](https://github.com/vpsfreecz/haveapi/actions/runs/40803800814) | servers/ruby RSpec | queued |
| [40803800783](https://github.com/vpsfreecz/haveapi/actions/runs/40803800783) | servers/ruby performance | queued |
| [40803800779](https://github.com/vpsfreecz/haveapi/actions/runs/40803800779) | clients/rust | in_progress |
| [40803800774](https://github.com/vpsfreecz/haveapi/actions/runs/40803800774) | clients/go RSpec | queued |
| [40803800768](https://github.com/vpsfreecz/haveapi/actions/runs/40803800768) | clients/js tests | queued |
| [40803800711](https://github.com/vpsfreecz/haveapi/actions/runs/40803800711) | release | in_progress |
| [40803800694](https://github.com/vpsfreecz/haveapi/actions/runs/40803800694) | clients/python | in_progress |
| [40803800687](https://github.com/vpsfreecz/haveapi/actions/runs/40803800687) | RuboCop | completed/success |
| [40803800666](https://github.com/vpsfreecz/haveapi/actions/runs/40803800666) | clients/php PHPUnit | in_progress |

The necessary new recovery branch triggered11 separate exact511 runs:3 success,
5 in_progress,3 queued. These are recovery CI, separate from fb07 acceptance.
They were left untouched, along with current feature, other-branch and completed runs.

| Recovery511 run ID | Workflow | Observed status |
| --- | --- | --- |
| [40803800727](https://github.com/vpsfreecz/haveapi/actions/runs/40803800727) | RuboCop | completed/success |
| [40803800701](https://github.com/vpsfreecz/haveapi/actions/runs/40803800701) | servers/ruby RSpec | queued |
| [40803800696](https://github.com/vpsfreecz/haveapi/actions/runs/40803800696) | clients/ruby RSpec | in_progress |
| [40803800676](https://github.com/vpsfreecz/haveapi/actions/runs/40803800676) | release | in_progress |
| [40803800672](https://github.com/vpsfreecz/haveapi/actions/runs/40803800672) | clients/js tests | in_progress |
| [40803800668](https://github.com/vpsfreecz/haveapi/actions/runs/40803800668) | clients/go RSpec | in_progress |
| [40803800665](https://github.com/vpsfreecz/haveapi/actions/runs/40803800665) | clients/python | queued |
| [40803800662](https://github.com/vpsfreecz/haveapi/actions/runs/40803800662) | clients/php PHPUnit | completed/success |
| [40803800655](https://github.com/vpsfreecz/haveapi/actions/runs/40803800655) | i18n health | completed/success |
| [40803800651](https://github.com/vpsfreecz/haveapi/actions/runs/40803800651) | servers/ruby performance | queued |
| [40803800648](https://github.com/vpsfreecz/haveapi/actions/runs/40803800648) | clients/rust | in_progress |

No superseded queued/in_progress SAME-feature runs were present in this snapshot;
0 cancellation requests. ci-summary.json and ci-once.* retain the single observation.
The existing workflow named release is included in the snapshot; no tag, registry,
default-branch or manual release action was performed by this package.

Final source/history/review proof remains
[the fold receipt](../history-m8-python-fold-20261029t014637z/receipt.md):
Core51073383f063abbc24bf19ca669b9b6e46bb9555,
Optional2462dfbac4921e15619ce17736bde9931f6d3fac,
Performancefb07c1378e4267bdfd54fa8fbfcfc57b6ec53413;
148 paths,+11467/-1282, accepted da1 tree/aggregate byte-equal, original messages
verbatim, no migrations or dependency/channel/input update streams. Aggregate
SHA256 `f468f0edc893f2899604aa88040f7a6e59bb09869a39c49528413f80eccd73c0`.
Original product/R3/511 reviews and final one-spec
[milestone8-python-review.md](../milestone8-python-review.md) remain accepted,
with no findings. Focused7/0, lint, normal hooks and final package/profile10/0
retain their actual executions; this publication reran none of them.

No additional project documentation change is useful for this publication-only
operation. Existing Go/TS/Rust native, installed, browser and all-client evidence
retains its actual source/input/execution scope, not a fresh fb07 execution claim.
Full fb07 CI/artifact assessment, exact direct-f6 performance and peer actual
final package/HTTPS/OAuth work remain separate. No readiness, deployment, default
integration or release claim. No test/compiler/performance/makeDoc/preview refresh,
provider/TLS/peer/service or session lifecycle operation was launched here.
Session remains open and active.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
