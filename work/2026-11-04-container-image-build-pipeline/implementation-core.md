# P1/P2: repository service implementation evidence

Owner P1 implementer2; HTTP/dashboard/log/stats contribution P2 implementer1.
Authoritative implementation brief: [design.md](design.md). Initial service commit
`463704f2046b1a888ae18777ba4932e9d118872e`, base
`d2fe1489f0b0b213fb247aeee6e081d349adaf42`, vpsadminos feature branch
`2026-11-04-container-image-build-pipeline` in its registered feature worktree.
The initial owner delivery performed no push, deployment, default integration or
machine/session lifecycle action. Current lead state: feature head `fab23ed2` is
published and exact-remote verified; staging remains `d2fe1489`. Original review
and narrow-fix acceptance are retained under their actual ranges below.
Current consolidated whole-branch head:
`fab23ed26aefaed635c41cdb89ff30bf82632c61` (COMPAT then P3 remain distinct).
Service commit remains literally `463704f2046b1a888ae18777ba4932e9d118872e`;
latest COMPAT is `562f6bd5fe78456d7ce23be5982165659cd5931f`.

Fresh final package builds at `fab23ed26aefaed635c41cdb89ff30bf82632c61` passed
exit 0 in 211 s (2026-11-05 22:51:02–22:54:33 UTC): service
`/nix/store/xjb3rcq192kg3b5pyfy98j4629xgcp4m-osctl-repo-server-26.05.drv` →
`/nix/store/xqg8733plf4y28nvav4s4376y9xi006i-osctl-repo-server-26.05`, OSVM
`/nix/store/c3aaprivwjqaqp2br07aww92crxx775b-osvm-26.05.0.drv` →
`/nix/store/5rpgj050bvvq9k5njwm1ckkzsc6d2xi9-osvm-26.05.0`.
The service's `doCheck=true` build passed; installed binary SHA-256
`0412a98d8f5e00913112f71f432c1225739e549bbf5722c27c5bc7012f162a8c` equals
the prior actual runtime binary. [Accepted final receipt](artifacts/final-packages-acceptance.json)
supersedes earlier pending-build language; corrected UTC derives from raw epochs,
not the watcher's rejected hour labels. Runner `gf2m6b4...` is also actually
realized at `/nix/store/1a0gnrc2i2im69779823b6i030dr6l8c-test-runner`
([receipt](artifacts/consumer-runner-realize.json)). No whole-machine closure
equivalence is claimed; actual worker smoke remains scoped to `8d5093e3`.

The complete compilable service is one logical commit: shared initial SQLite
schema, model/store/control/socket/main/Go module, HTTP/dashboard/log/aggregate,
tests, Nix package/overlay/flake shell and README/protocol docs. Lead approved the
combined P1/P2 commit to avoid broken intermediate main/schema dependencies.
Compatibility fixtures/harness and pipeline files are excluded; their owners
retain separate packets and index windows. `git diff --cached --name-only` was
empty before staging and after commit, unrelated working changes remained.

## Delivered contracts

- Immutable ordinary files, durable upload hash/size verification and file/directory
  fsync before SQLite references; foreign keys, WAL, FULL synchronous commits.
- Sole process owner and per-role/repository local sockets, explicit run/item
  identity, attempt freezing, stable request receipts and conflicting-retry errors.
- Run-pinned baseline, exact candidate formats and verified build/test receipts,
  finish/seal separation, independent eligible subset publication, stale generation
  and source/admission checks; caller supplies trusted Git ancestry evidence.
- Logical native-compatible GC and retained run/export/rollback references;
  mark-before-unlink physical cleanup and open-inode reads. Slow upload streaming
  does not hold the catalog lock. Run expiry is separate from public policy.
- Coherent legacy in-place adoption, portable stable-ID public export/import and
  static `v1` materialization for reconciled recovery. No private runs/logs in export.
- Existing v1 HTTP/aliases and sealed run URLs, public dashboard and bounded daily
  aggregate, private finite JSONL log. P2 retains ownership of its eight paths.

New persistence: **schema version 1, new/unreleased/undeployed**. There is no
supported predecessor database schema or guard/migration compatibility path.
No vpsAdmin schema, running-node protocol migration or coordinated fleet update.
One final functional commit; no obsolete intermediary history, deployed/released
lineage or published branch rewrites in the initial owner delivery. The lead
completed original full-branch review and accepted the narrow finding fixes under
their recorded ranges; later consolidation does not relabel the original review.

## Checks and outcomes

Declared targeted environment: `nix develop .#osctl-repo-server`; Go 1.26.10 plus
C compiler from pinned nixpkgs. Conventional `github.com/mattn/go-sqlite3` v1.14.32.
`go.sum` initially contained only its go.mod checksum; explicit module download
fixed the first watcher setup failure. First executing tests found a nil map after
empty file maps were omitted in persisted JSON; initialized it before upload commit
and added transaction rollback protection. Original failure is retained below.

Final command:

```sh
nix develop .#osctl-repo-server --command bash -c 'nixfmt flake.nix os/overlays/packages.nix os/packages/osctl-repo-server/default.nix && cd osctl-repo-server && go test ./... && go vet ./... && go build -o /tmp/osctl-repo-server-p1 ./cmd/osctl-repo-server'
```

Passed, exit 0; unit package 0.979 s after cached toolchain compilation. Covers
pinned same-tuple bytes, independent mixed-success publication, request replay,
integrity/roles, finite admission, restart receipts/pending cleanup, stale public
generation/admission, corruption rejection, portable/static round trips, symlink
rejection, logical expiry/ref-safe reclaim/open reads, slow producer isolation,
and the durable-file/pre-DB orphan recovery boundary. P2 HTTP/cache/privacy/log
and SQLite aggregate tests are included. Actual binary `/tmp/osctl-repo-server-p1`.

Native GC comparison against all four independent peer fixtures also passed in a
prior full test batch (0.921 s). That temporary Go test was removed before commit
to avoid a core-only commit depending on excluded peer testdata. The permanent
COMPAT packet owns native parity; its actual registered-server/old-client smoke
remains a next dependency, not an asserted result here.

Exact generated vendor tree hash:
`sha256-Swi56SaPh4AN7LZ2a+j3p/jNf/InnbmE6AEErjqLg0g=`. Lead watcher confirmed
the Nix package proof against initial `41e5c83e769115cefddb193237b4b05823d3d80f`
source: pass, exit 0, 153 s, output
`/nix/store/krkxhb10xgyjnx5hisa4hcr4sd6yisfh-osctl-repo-server-26.05`;
[log](artifacts/p1-nix-build.log). This proves dependency/package wiring for that
source, not the later authority/caller changes; exact final build follows review.

Normal active Overcommit hooks ran under the declared shell: Nixfmt passed;
commit-message checks passed with advisory >72-column warnings, all lines <=80.
No hook bypass. Logs retained:

- [Final checks](artifacts/p1-go-final.log)
- [Native fixture comparison batch](artifacts/p1-go-native-parity.log)
- [First executing failure](artifacts/p1-go-first-failure.log)
- [Binary build](artifacts/p1-go-build.log)
- [Commit and hooks](artifacts/p1-commit.log)
- [Final authority-boundary tests/vet](artifacts/p1-auth-boundary-check.log)
- [Amended logical commit and hooks](artifacts/p1-amend.log)

Before handoff, narrowed publisher authority to status/publication only (filesystem
export is admin-only) and scoped bulk expiry to the socket's repository. Added
a role/repository regression; all tests passed in 1.087 s and vet passed. Folded
these two-file corrections into the logical owner during a lead-granted short
amend window: old reviewed local checkpoint `41e5c83e769115cefddb193237b4b05823d3d80f`
became final `66338b0e811eeffb7400882008f7ed86e7515d9f`. Neither was pushed,
reviewed as a completed branch, deployed or externally consumed; no obsolete
authority-fix commit remains. Index verified empty and ownership released promptly.

Final caller fit committed and consolidated: a stored newer same-source admission now returns
`superseded` distinctly from transient generation `conflict`, permitting P3 to
record a superseded-only outcome without retrying old policy/defaults/GC. Only
control.go, its existing regression and README changed; all tests/vet passed
(1.049 s, [log](artifacts/p1-superseded-check.log)). No API/schema change. Lead
accepted this exact scope. After COMPAT commit
`178864cca147b6e518cf514adbba636756306948`, committed only these three paths as
`e7d0f28b2cc47e1dbcda8aeecdb30e3276500302` with normal hooks; [log](artifacts/p1-superseded-commit.log).
Index was empty before/after and immediately released. No rebase/autostash of dirty
peer work was attempted.

After P3 committed and released a clean tree, ordinary interactive rebase folded
only that caused fix into the service owner under a lead-granted exclusive window.
Complete old range: `d2fe1489..121d349f5a96a1bc3c92463ebe0e6bd76143ab7a`;
new range: `d2fe1489..932937390c876e4afcc5df6e0da653a39177af58`.
Exact tree before and after: `3844d6372319f75f2c3ff92094a8a83ab0ad978e`;
old/new diff empty, four commits became three, worktree/index clean. Retained
backup ref:
`refs/heads/2026-11-04-container-image-build-pipeline-before-core-fold-20261105T201409Z`.
No refs deleted, no reset/clean/stash/autostash. Preserved commit proofs:

| Owner | Old head | New head | Stable patch ID |
| --- | --- | --- | --- |
| Service | `66338b0e811eeffb7400882008f7ed86e7515d9f` plus caused `e7d0f28b2cc47e1dbcda8aeecdb30e3276500302` | `a9ce2d4f79775873b35a34cb596792515f761a98` | Exact intended fold, shown in range-diff |
| COMPAT | `178864cca147b6e518cf514adbba636756306948` | `9f78583b57d03bcda7e7a42d2acd196c4ee04d7a` | `8206b17821cae6c34c1ba2a62a53e67c76ff7dae` unchanged |
| P3 | `121d349f5a96a1bc3c92463ebe0e6bd76143ab7a` | `932937390c876e4afcc5df6e0da653a39177af58` | `428c99b5bbe405a6cd929388755c6961df0e5649` unchanged |

Proofs: [receipt](artifacts/p1-consolidation.json),
[range-diff](artifacts/p1-consolidation-range-diff.txt),
[normal rebase](artifacts/p1-consolidation.log). Ownership released before records
or final checks. Schema remains one new v1, unreleased/undeployed/unconsumed; no
migration predecessor or caused-fix residue remains in the final series.

Post-consolidation cached `go test ./...`, `go vet ./...` and binary rebuild under
the declared Nix shell passed, exit 0, against whole-branch
`932937390c876e4afcc5df6e0da653a39177af58`; [log](artifacts/p1-post-consolidation.log).
The actual `/tmp/osctl-repo-server-p1` now includes the final caller/authority
behavior. No listener was started. Worktree/index stayed clean.

## Next dependency and limits

### Later COMPAT lint-fix consolidation

After owner3's generator lint correction and clean release, the lead authorized
one narrow fold. Fresh old range:
`d2fe1489f0b0b213fb247aeee6e081d349adaf42..3fe6972958d56e2d9f819f36ffcff3d2c7ab1619`;
final range:
`d2fe1489f0b0b213fb247aeee6e081d349adaf42..fab23ed26aefaed635c41cdb89ff30bf82632c61`.
Both exact final trees: `475aff53b0a094cf863ecf74889e57012b044b99`.
Full old/new diff empty; four commits became three, index/worktree clean.
Retained backup:
`refs/heads/2026-11-04-container-image-build-pipeline-before-compat-fold-20261105T224440Z`.

| Owner | Old commit(s) | Final commit | Stable patch proof |
| --- | --- | --- | --- |
| Service | `463704f2046b1a888ae18777ba4932e9d118872e` | literally unchanged | `fd0d40fe7a0afadafab1c8690392ff1afe93a639` |
| COMPAT | `39f7e73746d0157bdd8b734a76d13f9b974b7890` + `3fe6972958d56e2d9f819f36ffcff3d2c7ab1619` | `562f6bd5fe78456d7ce23be5982165659cd5931f` | aggregate `138bc1c0fb8e1b195114b2b7cbbcd8d213be4292` |
| Pipeline | `8d5093e3d65f561dd305898074dd8add5e49323e` | `fab23ed26aefaed635c41cdb89ff30bf82632c61` | unchanged `7a5e3368e1ff0cc8e59658485c5fc19af2bc2529` |

Every final owner's path boundary is unchanged. COMPAT paths are disjoint from
service/pipeline; those two legitimately share `flake.nix` for the later existing
osvm package export. Initial preflight refused an overly strict all-owner-disjoint
proof before any mutation, released, and resumed only under a renewed exact window
with direct unchanged service/pipeline patch checks. No source edits, stash/reset/
clean/autostash, ref deletion, product build/test, VM or service action. The ordinary
rebase command's declared Nix shell unexpectedly substituted toolchain paths and
realized its small shell environment before Git; this incidental setup is visible
in the retained log, not claimed as product verification.

Proofs: [receipt](artifacts/p1-compat-fold.json),
[range-diff](artifacts/p1-compat-fold-range-diff.txt),
[normal rebase log](artifacts/p1-compat-fold.log). Window released before records.
Schema/protocol migrations unchanged: sole new unreleased/undeployed/unconsumed v1.
Actual `8d5093e3` runtime smoke evidence retains its original tested revision;
no Go/Nix proof reuse is inferred merely from this history-only final-tree equality.
Capacity released for a later explicitly allocated identity/check packet; no next
work assumed queued and no additional checks launched here.

### Final review-fix consolidation

After every owner committed findings and released a clean worktree/index, lead
authorized a final ordinary interactive rebase. Complete old range:
`d2fe1489f0b0b213fb247aeee6e081d349adaf42..fcf49d91c618abf6ab2a766d3a7c4fdc8ede91c3`;
new range:
`d2fe1489f0b0b213fb247aeee6e081d349adaf42..2120ec2de70b9daa38588a8ad79a8296ec3e6167`.
Exact final tree before and after: `ec81e39192b08402eea967a1bdb1978761e36e2a`.
Seven commits became three; old/new diff empty, index/worktree clean. Retained
backup:
`refs/heads/2026-11-04-container-image-build-pipeline-before-final-fold-20261105T203953Z`.

| Owner | Old logical owner and caused fixes | Final commit | Identical aggregate patch ID |
| --- | --- | --- | --- |
| Service P1/P2 | `a9ce2d4f79775873b35a34cb596792515f761a98` + HTTP `0870311705f8c10920a57c32307a5e199fb879f3` + core `df143b4608b4780867c4da5b49493855859612c2` + log `fcf49d91c618abf6ab2a766d3a7c4fdc8ede91c3` | `463704f2046b1a888ae18777ba4932e9d118872e` | `fd0d40fe7a0afadafab1c8690392ff1afe93a639` |
| COMPAT | `9f78583b57d03bcda7e7a42d2acd196c4ee04d7a` | `39f7e73746d0157bdd8b734a76d13f9b974b7890` | `8206b17821cae6c34c1ba2a62a53e67c76ff7dae` |
| Pipeline P3 | `932937390c876e4afcc5df6e0da653a39177af58` + `c2231c9df9b1f20378b1b3c72a03f55e0bf260fd` | `2120ec2de70b9daa38588a8ad79a8296ec3e6167` | `26cb365f4ab2fff91585564fecf156c77b15314f` |

Every final owner's exact path set matches its old group; source content was not
edited during consolidation. No stash/reset/clean/autostash, skipped hooks or ref
deletion. Window released before records/checks. Full proofs:
[receipt](artifacts/p1-final-fold.json),
[range-diff](artifacts/p1-final-fold-range-diff.txt),
[normal rebase log](artifacts/p1-final-fold.log).
Original reviewer range/head `93293739` and reports remain historical evidence;
findings/fix receipts remain linked rather than relabelled as final-head review.
Schema remains the sole new v1, unreleased/undeployed/unconsumed; no predecessor
or caused-fix residue remains. Org configuration `2ed95c94f5be096b2142d96c84eb0f00b5e040be`
was handled separately by its owner and was not touched by this operation.

Final-head cached Go tests (1.136 s), vet and binary rebuild passed, exit 0,
under the declared Nix shell after window release at
`2120ec2de70b9daa38588a8ad79a8296ec3e6167`;
[log](artifacts/p1-final-head-check.log). Binary `/tmp/osctl-repo-server-p1`
SHA-256: `dc9579d5c0aa7e63a1d8c9a923d7f5a6ccc960e65c24862107686800e4abb85a`.
Worktree/index remained clean. No listener or long test/build was launched.

### P1 review findings F2/F3/A1

Reviewer originally assessed whole head `932937390c876e4afcc5df6e0da653a39177af58`.
Core fixes committed as `df143b4608b4780867c4da5b49493855859612c2`, parent
`c2231c9df9b1f20378b1b3c72a03f55e0bf260fd`, subsequently consolidated as recorded above.
Only `store.go`, `control.go`, `upload.go`, `core_test.go`, and README changed.

- **F2 availability:** sealing/publication now validate catalog shape and each
  durable ready file identity using SQLite metadata only. They do not reopen/hash
  the entire baseline under the shared reader mutex. Upload/adoption/import/export
  still verify bytes at their existing integrity boundaries. FIFO byte-I/O probes
  prove both operations complete without reading an unchanged baseline; reference
  identity tampering is rejected, and both export modes still reject corrupt bytes.
- **F3 headroom:** admission now accounts conservatively for every complete
  outstanding stream, including unwritten bytes, when reserving filesystem space.
  Import admission also respects those pending reservations. Concurrent stalled
  pipe streams write one actual byte in the regression; the second cannot consume
  the first stream's promised space or reserved database/control headroom.
- **A1 schema atomicity:** initial CREATE statements and `user_version=1` now
  commit in one ordinary SQLite transaction. One late-DDL-collision regression
  verifies rollback leaves no partial new schema/version. Schema is still the
  sole new unreleased/undeployed v1; no predecessor guards or API changes.

Focused new core regressions and vet passed (0.402 s). The first shared batch
encountered P2's in-progress sticky JSON encoder recovery failure, diagnosed and
fixed by that owner. After P2 declared source-stable, full Go tests and vet passed
exit 0 (root 1.131 s). Logs: [focused](artifacts/p1-review-focused.log),
[shared final](artifacts/p1-review-core-final.log),
[scoped mixed-source failure](artifacts/p1-review-mixed-source-failure.log),
[commit/hooks](artifacts/p1-review-core-commit.log). Main approved factual README
copy. Normal hooks passed without bypass; only advisory 72-column warnings, all
message lines <=80. Index verified empty and released immediately after commit.

Core index window released. Initial pending review/build steps are historical;
current original-review/narrow-fix acceptance and fresh final package proof are
summarized at the top. Lead owns further consumer/runtime acceptance and rollout
decisions. P1/P2 retain follow-up finding ownership. Live capacity,
proxy/SSH identity/admission and sole-writer cutover remain unverified and block
dependent activation, as recorded by P0; source checks do not authorize deployment.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/>
