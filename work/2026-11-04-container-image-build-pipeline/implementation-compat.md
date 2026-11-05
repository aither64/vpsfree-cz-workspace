# P1-COMPAT completion and acceptance evidence

**Current lineage (2026-11-06):** accepted, published whole head
`fab23ed26aefaed635c41cdb89ff30bf82632c61`, COMPAT
`562f6bd5fe78456d7ce23be5982165659cd5931f`, includes the caused generator-only
lint correction: [sequential/duplicate/invalid-value semantics and CI-compatible
RuboCop 1.75.8 proof](artifacts/compat-rubocop-42120921304-ready.md),
[fold receipt](artifacts/p1-compat-fold.json); final-head GitHub RuboCop
`42124511723` passed. Everything below describing whole head `2120ec2d`, tree
`ec81e391` and COMPAT range ending `39f7e737` is the **historical actual four-case
runtime scope**, not a run at `8d5093e3` or `fab23ed2`. The
[fresh final package receipt](artifacts/final-packages-acceptance.json) records the
final service binary's identical SHA-256
`0412a98d8f5e00913112f71f432c1225739e549bbf5722c27c5bc7012f162a8c` versus the
exercised Nix binary; [scoped source/input evidence](final-source-identity.md)
and the generator semantics proof support retaining that runtime evidence.
No runtime rerun or whole-machine closure equivalence is claimed.

Owner: implementer3. **Complete, submitted to lead for acceptance, 2026-11-05.**
The committed fixture/harness subdeliverable was already accepted; its parked
runtime dependency is now satisfied. No remaining COMPAT findings or tests.
Capacity is available after this completion report. Initiative readiness,
publication, integration and deployment remain lead-owned and separate.

## Exact source and deliverable

- Repository: `git@github.com:vpsfreecz/vpsadminos.git`; default target `staging`.
- Tested whole head: `2120ec2de70b9daa38588a8ad79a8296ec3e6167`.
- Whole tree: `ec81e39192b08402eea967a1bdb1978761e36e2a`.
- Final COMPAT range:
  `463704f2046b1a888ae18777ba4932e9d118872e..39f7e73746d0157bdd8b734a76d13f9b974b7890`.
- Eight owned paths: `osctl-repo-server/compat/{README.md,generate_native.rb,check_fixtures.py,service_check.py}`
  and `osctl-repo-server/testdata/native/{catalog,gc,subset,mixed_failure}.json`.
  No production service implementation or shared types were added by COMPAT.

Original range
`66338b0e811eeffb7400882008f7ed86e7515d9f..178864cca147b6e518cf514adbba636756306948`,
intermediate range
`a9ce2d4f79775873b35a34cb596792515f761a98..9f78583b57d03bcda7e7a42d2acd196c4ee04d7a`,
and final COMPAT range have identical owned content and stable patch ID
`8206b17821cae6c34c1ba2a62a53e67c76ff7dae`, independently checked by implementer3.
The complete final-fold ranges, unchanged final tree, backup ref and per-owner
proofs are retained in [core history evidence](implementation-core.md#final-review-fix-consolidation).
The original independent review at whole head `93293739` remains scoped to that
head; this packet does not relabel it as a new final-head review. The lead owns
review findings reconciliation and final-series assessment.

COMPAT contains no migrations, persisted schema changes, deployed revisions or
externally consumed migration lineage. Worktree and index were clean at final
evidence inspection; no source changes accompanied the runtime batch.

## Independent native oracle and quick checks

All four fixtures were generated at native source
`d2fe1489f0b0b213fb247aeee6e081d349adaf42`. Each fixture records SHA-256 of the
native writer/index/image/CLI, configured GC policy and actual Ruby GC program.
The generator invokes the real source-first native CLI and executes `gc.rb`,
substituting only its normal Nix command-path placeholder. It does not implement
Go catalog or retention logic. Fixtures preserve native INDEX bytes/order, real
alias symlinks and identifying payload bytes/hash/size; total JSON is about 146 KB.

Previously completed quick checks: four integrity/provenance tests passed,
Ruby syntax passed, both Python files compiled, native `catalog --check` matched,
and scoped RuboCop passed. Normal commit hooks passed Nixfmt/RuboCop and commit
message checks, with only the advisory 72-column warning (all lines <=80).
An initial hook launch omitted bundled `rexml` from explicit `GEM_PATH`; restoring
the normal Ruby gem directory resolved it without hook bypass or source changes.

## Actual post-review runtime batch

Fresh managed watcher: GPT-6 Luna/low, native thread
`01a1ad7d-aaa2-7b62-bcf0-35c9670dd570`. The lead registered four separate empty
loopback services and confirmed all three role sockets plus expected empty INDEX
404 before dispatch. The watcher ran sequentially, with no failure, retry, build,
source change or service action. **All four cases passed in 29 seconds of command
elapsed time**, as recorded by the watcher:

| Case | Result | Elapsed | Evidence |
| --- | --- | ---: | --- |
| `catalog` | PASS, exit 0 | 5 s | [log](artifacts/p1-compat-postreview/catalog.log), [status](artifacts/p1-compat-postreview/catalog.status) |
| `gc` | PASS, exit 0 | 10 s | [log](artifacts/p1-compat-postreview/gc.log), [status](artifacts/p1-compat-postreview/gc.status) |
| `subset` | PASS, exit 0 | 7 s | [log](artifacts/p1-compat-postreview/subset.log), [status](artifacts/p1-compat-postreview/subset.status) |
| `mixed_failure` | PASS, exit 0 | 7 s | [log](artifacts/p1-compat-postreview/mixed_failure.log), [status](artifacts/p1-compat-postreview/mixed_failure.status) |

[Watcher result](artifacts/compat-watch-result.txt) and
[exact dispatch brief](artifacts/compat-watch-brief.txt) retain execution details.
Each log says `PASS CASE: native INDEX/GC/aliases/bytes, HTTP framing and old clients`.

Tested immutable binary:
`/nix/store/g4434b8c720bhdjgcxs2ygfh1z7qfqxl-osctl-repo-server-26.05/bin/osctl-repo-server`.
SHA-256, independently read after the batch:
`0412a98d8f5e00913112f71f432c1225739e549bbf5722c27c5bc7012f162a8c`.
Final-head Nix service build passed in 211 s, derivation
`/nix/store/pqw1r6h689y75phgsdbb490lqybxnvsn-osctl-repo-server-26.05.drv`;
[package/evaluation receipt](artifacts/final-package-eval-watch-result.txt),
[Nix build result](artifacts/final-service-build.json).
That receipt also records separate worker-evaluation outcomes; the successful
service build and this compatibility batch do not imply worker verification.

Each case used the same command below with `CASE/PORT` set to
`catalog/19471`, `gc/19472`, `subset/19473`, `mixed_failure/19474`, from the
vpsadminos feature worktree. The native wrapper supplies its matching packaged
Ruby/native dependencies; clean GEM/BUNDLE variables and source-first `RUBYLIB`
prevent inherited ABI/dependency selection from replacing that closure.

```sh
env -u GEM_HOME -u GEM_PATH -u RUBYOPT -u BUNDLE_GEMFILE -u BUNDLE_PATH \
  RUBYLIB=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-04-container-image-build-pipeline/vpsadminos/osctl-repo/lib:/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-04-container-image-build-pipeline/vpsadminos/libosctl/lib \
  python3 osctl-repo-server/compat/service_check.py \
  --url http://127.0.0.1:PORT \
  --cli /nix/store/g4434b8c720bhdjgcxs2ygfh1z7qfqxl-osctl-repo-server-26.05/bin/osctl-repo-server \
  --native-cli /nix/store/n23vgl74jcgylfx0nl5205vq5ixn7wvv-ruby3.4-osctl-repo-26.05.0/bin/osctl-repo \
  --producer /tmp/p1-compat-2120ec2de70b/CASE/producer.sock \
  --publisher /tmp/p1-compat-2120ec2de70b/CASE/publisher.sock \
  --repository vpsadminos --scenario CASE
```

## Acceptance coverage and limits

The real CLI/HTTP/native-client batch proved native lexical order and configured
tag precedence despite reverse completion, vendor/architecture/variant grouping,
defaults and combined aliases, stream-only format omission, first-match Ruby GC
policy and keep-four behavior, full-catalog GC during named-subset/mixed-failure
publication, and independent successful publication after unrelated failure.
It also checked exact payload bytes/hash, GET/HEAD length/framing and identity
encoding, sealed INDEX/payload IMS/304, native direct and force-check cached
downloads, same-tuple refresh without stale 304, pinned old bytes after public
replacement/pruning, complete unchanged/new run views, and rejection of a failed
selected rebuild even when its tuple already exists in public.

This is tiny-payload repository compatibility evidence. It does not establish VM
boot/image validity, privileged-runner admission/capacity, worker concurrency or
replacement, full-CI success, live proxy/SSH cutover, production import/recovery,
large-file performance or a pipeline speedup. Other package and P0/live acceptance
conditions remain with their owners. No new COMPAT test expansion is required.

The batch processes finished. The four registered services at
`/tmp/p1-compat-2120ec2de70b/{catalog,gc,subset,mixed_failure}` remain open;
no stop, cleanup, deployment or session lifecycle action was requested or taken.
Lead next action: accept this completed package, link it from state and continue
overall readiness/publication separately. No tracking commit was made by this
package; the lead retains the normal coordination-record cadence.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/)
