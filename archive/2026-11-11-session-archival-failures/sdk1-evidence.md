# SDK1 committed review packet

Ready for root-owned R25; no live action or default-branch integration performed.

| Repository/range | Committed head | Scope |
| --- | --- | --- |
| codex-web, dd90fb4308ba85617ee2a4267cc835aa9a4f11ce → head | 91a17d00a737d59a91b5e7bb420aa89e7ec52d93 | One project/read ObserverOnly allowance; existing passive fixture extended; 2 files,24+/2- |
| D runtime, 52c8ded89a2b4cab402ff4058658ba80e23094ab → head | e32d0bd497dbd69fd3a8cd07bfb477d7cb44d3f3 | SDK dependency inputs + existing real transition-client regression; 6 files,19+/9- |
| Final runtime, ee1dd065ce0aae78816d8fcab2ee25d90eb2535a → head | 3492365c3a3e12b18418919964844089d560dc1b | Same dependency/regression correction; 6 files,19+/9- |

All three features published over canonical SSH; fresh exact feature remote
heads match. All three worktrees clean. Provider default observed once, exact
dd90; runtime default observed once, exact734a85fea42c8f8276e6b037196c24cf8903cd12.
No default branch changed.

## Focused verification

- Provider Nix environment: `go test -mod=readonly ./codex -run '^TestObserverListQueueStaysReadOnly$' -count=1 -timeout=20s` PASS0.023s. Actual ObserverOnly ReadProject checks exact parameters, success and wrong response identity. Existing fixture rejects project/create and thread mutations and fences unsolicited supported/unsupported native requests with subsequent reads. Every client.go byte outside the allowlist addition is unchanged, including incoming handling.
- Both declared runtime Nix environments: `go -C portal test -mod=readonly ./cmd/workspace-portal ./internal/monitoroperation -run '^TestTransitionProof|^TestMaintenance(Monitor|InventoryRetains|Utility)|^TestMonitorLifecycle' -count=1 -timeout=45s` PASS. D package times1.016/1.002s; final1.015/1.035s. Regression uses actual newTransitionClient.ReadProject; existing dormant-ledger, uncertainty, maintenance and lifecycle cases remain.
- Both actual pin checker and existing `test/codex_web_pin_test.sh` PASS; `git diff --check` PASS. No hook framework declared/active hooks configured in either repository; ordinary commits used without bypass.
- Normal scoped flake update and Go tidy remove old SDK checksums. Complete runtime9-node locks change only codex-web; other7 dependency identities and all other Go module declarations/checksums unchanged. Native packaging/runtime contracts unchanged; native647 and model catalog inputs retained. SDK catalog SHA256049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1 unchanged.
- Fresh dependency-only `nix build --no-link --print-out-paths .#workspace-portal.goModules` PASS0: /nix/store/1w1dmf4gjwgd4jhgcapy3rpigxqzcfjd-dev-workspace-0.2.0-go-modules.drv → /nix/store/n3yxih9kaqq66pkr6c04axwsmnal7iqc-dev-workspace-0.2.0-go-modules. Vendor hash `sha256-GNrQHxh5yywQqLHJYokS1mE8YEt4DzKVZ/OblP8TDSc=`; actual vendored client byte-equals published SDK. Both consumers have identical Go/dependency inputs. SDK NAR `sha256-5egPR/a4ig5NpjhvLHAiekREjuutcMEr5BSxNoHPPz4=`.

## History, limits and next dependency

Whole review series: SDK dd90→91a17 (one commit); D b8329e32f1132fd947f4a9c803bf44e3ed9ce481→e32d0bd4 (R24 D1 + one SDK update); final734→3492365c (R24 D1 + one SDK update). No superseded pin update or migration in these streams. D52 is consumed; preserved checkpoint `refs/checkpoints/2026-11-11-session-archival-failures/sdk1-consumed-D52` retains exact52. Final oldee checkpoint `sdk1-final-ee1d` retains exactee. Consumed workspace E9 and all older D refs remain untouched. Final remains descendant of merged734. Unconsumed workspace f53/config d038 remain untouched, for owner0's later checkpoint/consolidation after root release.

Environment deviations retained in raw logs: first final Go-only shell failed before tests because gcc was absent. A full-package .drv shell shortcut was unsuitable and attempted unrelated bootstrap/dependency realization, then failed before tests; that was an avoidable verification-scope error. Both handles terminal/joined; corrected final verification used ordinary declared nix develop and passed. No claimed success from either attempt. No application build, full suite, native/provider/API, CI watch, profile/machine/claim/selection action performed by SDK1. No package acceptance or later maintenance gate is proved by these focused checks.

No product-documentation edit needed for this omitted existing read allowance; the existing passive contract and adjacent fixture/commit rationale cover behavior. Root owns review, any later acceptance/build/selection and separate codex-web/master integration approval. Owner0 owns matching compositions after release. Source fixes retained; all tools joined, capacity available after acceptance.

Raw command logs and compact pin proof: `/tmp/session-archival-sdk1/`.
Pin proof SHA256: 3ad079658c264f079fcbeca41eadc64cae9418382648ca04500dbb3864142741.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/
