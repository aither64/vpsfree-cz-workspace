# Frozen runtime frontier refresh

Owner: implementer0. Accepted authority: the architect's complete "Frontier
refresh implementation brief, 2026-10-15" and the lead's explicit go-ahead.
Exact current session, both absent environment identity markers and ready saved
workspace-write member identity were verified. No product edits beyond the
clean rebase were needed; no wording change or new copy pass is involved.

## Exact ranges and preservation

Old reviewed base: `ba8669b14536f72b559abc912bba8eac430111e4`.
Old final head: `0b403305e085aa01884cf56acea7c717f78f7e86`.
New integrated base: `832d9f1a6a21337dd44063ddf39f7a88cfc95450`.
New frozen clean head: `bb9e6291bec10227c961c36559fba406938f1eaa`.

The original head and both ancestors remain reachable through
`refs/session/2026-10-14-i-d-like-the-dev-workspace/frontier-original-0b403305`.
New `frontier-runtime-original.json`, `frontier-runtime-original.patch` and
`frontier-runtime-original-series.txt` preserve the exact original range;
`frontier-runtime-upstream.patch` records the three incoming upstream commits.
All prior evidence, reviews, pins, probes and live harnesses remain untouched.

Executed source command:

```sh
git rebase --onto 832d9f1a6a21337dd44063ddf39f7a88cfc95450 ba8669b14536f72b559abc912bba8eac430111e4
```

It replayed exactly two commits with no conflicts, manual edits, dropped commits
or merges. No new dependency, generated pin or format update was introduced.

| Original commit | New owning commit | Scope |
| --- | --- | --- |
| `b8a6be26a75347dcc9ec0fd1330dff886e47c93f` | `96717cdeb5f733391846a95d78c117068ce77de8` | Complete attention/Web Push feature, including its inseparable dependency/import/vendor closure |
| `0b403305e085aa01884cf56acea7c717f78f7e86` | `bb9e6291bec10227c961c36559fba406938f1eaa` | Bounded provider failure diagnostics, safe VM failure evidence and 10-second collection timeout |

Final new-base-to-head inventory: 40 files, +3893/-82. Complete messages/parents,
file inventory, exact patch and freeze metadata are in
`frontier-runtime-series.txt`, `frontier-runtime-stat.txt`,
`frontier-runtime-final.patch` and `frontier-runtime-freeze.json`.

## Overlap and equivalence evidence

`frontier-runtime-range-diff.txt` reports `=` for both commits. Stable patch IDs
also match in `frontier-runtime-patch-ids.json`:

- Feature: `30bc996313be67952785ae0dc1446bbe90a3f8cc`.
- Diagnostics: `a1f32e31625524d66e2ab45b7f69b5c0cafe3af4`.

`frontier-runtime-blob-comparison.json` checks all 37 nonoverlapping feature
files byte-for-byte against the old head and all 30 upstream-only changed files
against the integrated base. Every comparison is identical. This includes the
attention/notification/title/browser/worker/transport source and provider
implementation/test/VM/docs. The three overlaps were inspected explicitly:

- `libexec/dev-session`: upstream artifact expected-owner/incarnation logic and
  CLI option remain; our optional strict creation-preference reader remains.
- `libexec/workspace-host`: upstream notification-worker dispatch remains;
  our second optional strict receipt reader remains.
- `nix/workspace-portal.nix`: upstream integration configuration/catalog/metadata,
  helper installation and Ruby source-filter/shards/aggregate/passthru remain;
  our vendor hash and five attention/browser verification commands remain.
  The removed old inline Ruby suite block was not restored.

`frontier-runtime-overlap.patch` shows only our expected effects against the new
base. Upstream `flake.nix`, development shell and check exports, strict optional
integration capability decoding, digit-bearing role handling, admission locks,
notification worker and integration/certification implementation remain exact.
The Ruby source filter includes `nix/`, so our extracted VM-driver contract still
receives its fixture. Python/Ruby/Node are available to those shards.

`flake.lock`, `portal/go.mod` and `portal/go.sum` are identical to the old head.
Vendor hash remains
`sha256-iyydGWryLmh8P+YxQcQ2SqGIj1Lds+WBDgsKQV4uFqA=`.
No dependency acquisition, closure update or new vendoring declaration occurred.
Cached declared tools remain Go 1.26.6, Ruby 3.4.9, Node 24.19.0 and Python
3.13.15. No hook framework/core.hooksPath or active nonsample hooks are declared;
none was bypassed.

These source comparisons support affected review. They do not certify the
substantive integrated baseline or authorize the certified-equivalence exception.
The lead's retained affected independent review remains required before long
checks; old unaffected review conclusions need their explicit source boundaries.

## Bounded quick checks

All member commands sourced the existing `runtime-dev-env.sh`; Go used cached
modules/build outputs with `GOFLAGS=-mod=readonly`, `GOPROXY=off`, `GOSUMDB=off`,
and an absent provider catalog. `PORTAL_BROWSER_TEST` was unset. Exact commands,
exit statuses and wall times are retained in new `frontier-runtime-*.status.json`
beside their logs. No full/unbounded suite, browser, network, native provider,
live host, queue or lifecycle operation ran.

| Check | Result |
| --- | --- |
| Node actual-module attention/browser contracts | 15 passed, about 0.47s command time |
| Five app/attention/store/notification/worker JavaScript syntax checks | PASS |
| Focused Go `web -run Attention\|Notifications -count=1` | PASS, 0.427s test / 8.563s command; real browser test gated off |
| Go `internal/agentteams -count=1` | PASS, 0.144s test / 1.374s command |
| Member provider Ruby, unchanged real-socket case excluded | 19 cases / 183 assertions, PASS, 1.075s test |
| Lead exact-head full provider Ruby including real Unix socket | 20 cases / 185 assertions, PASS, 0.993705s; no failures/errors/skips |
| Two optional strict creation-preference receipt readers | 1 case / 5 assertions and 1 case / 10 assertions, PASS |
| Selected artifact expected-owner/CLI contracts via aggregate bootstrap | 2 cases / 8 assertions, PASS |
| Bounded admission tests | 4 cases / 13 assertions, PASS |
| Selected integration batch/idempotency/reply-loss/worker/capability contracts | 4 cases / 16 assertions, PASS, 3.482s test |
| Selected certification migration/check-input contracts | 2 cases / 4 assertions, PASS |
| Four source/test Ruby syntax checks | PASS |
| Flake, package, Ruby-check and recovery-VM Nix syntax parse | PASS, no daemon/evaluation/build |
| Committed final upstream-to-feature diff whitespace | PASS |

Evidence groups: `frontier-runtime-go.log/status.json`,
`frontier-runtime-static-node.log/status.json`,
`frontier-runtime-ruby.log/status.json` and
`frontier-runtime-ruby-additional.log/status.json`. The first direct standalone
artifact test load failed with upstream `NullTmux` bootstrap absent. The same
two selected cases passed through `test/dev_session_test.rb`; no source change
or full suite run was needed. Preserve both attempts. Lead full provider evidence
is `frontier-provider-lead-ruby.log/status`, bound to exact bb9e629 head.

Core commands were:

```sh
node --test portal/internal/web/attention_browser_test.cjs
go -C portal test -mod=readonly ./internal/web -run 'Attention|Notifications' -count=1
go -C portal test -mod=readonly ./internal/agentteams -count=1
ruby test/workspace_host/codex_provider_test.rb --exclude '/test_shared_readiness_waits_for_native_protocol_and_refuses_early_exit/'
git diff --check 832d9f1a6a21337dd44063ddf39f7a88cfc95450 HEAD
```

Package/check-graph Nix evaluation and all long verification remain lead-owned.
The member did not invoke the daemon or realize checks. Exact optional lead
evaluation command (no build), in the declared environment:

```sh
nix eval --json 'git+file:///home/aither/workspace/ai/vpsfree.cz/repos/dev-workspace.git?rev=bb9e6291bec10227c961c36559fba406938f1eaa#checks.x86_64-linux' --apply 'builtins.mapAttrs (_: value: value.drvPath)'
```

## Compatibility and provenance

Our two commits add no migration files/conversion. Retained feature private
notification schema 1, optional strict preference receipt and fixed browser
cleanup obligations remain exact, with the same capable bundled-reader and
forward recovery contract. Provider diagnostics are additive stderr and no new
state format. No new feature state was deployed, released or externally consumed
through this refresh; old disposable probes remain evidence, not predecessors.

The integrated upstream baseline **does** introduce supported versioned
integration journals/certification capability metadata and pending-operation
fencing. Those are protected upstream capabilities, not obsolete feature-local
migrations to remove or squash. They remain byte-identical with their checks and
source-filter packaging. A predecessor without integration capability cannot
replace a package with a pending run. Do not downgrade composition to reuse an
old output. Ordinary forward-only recovery preserves notification subscriptions,
VAPID keys, outbox, receipts and upstream coordination/integration state.

Upstream coordinator thread notifications and our browser Web Push are distinct
channels. Nothing in this refresh combines their observers, persistence or
delivery workers. Original provider failure/root cause remains unresolved.

No source push, downstream pin, default integration, profile/host mutation,
reservation/queue action or lifecycle action was performed. Lead owns new final
workspace/config pins, publication, affected review, exact long checks and
deployment preparation. Hold push and long checks. A new exact-head live harness
will be prepared separately; old proof and harness inputs remain historical.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
