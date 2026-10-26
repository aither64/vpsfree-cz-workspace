# Original C CI failures: bounded diagnosis

Owner: implementer1. Read-only diagnosis on 2026-10-25. All three original runs
tested `5832ccc64dcf725a625c88ad440ddb631ff404b4` (old C). Logs and the available
failure artifact were inspected before any retry. No jobs were rerun, no local
application tests/campaigns were launched, and no source/index/Git changes were
made. Existing local packaging was not interrupted. Old C is retained evidence
and must not be published under the user's subsequent master-first direction.

## Concrete causes

| Run | Original failure | Cause |
| --- | --- | --- |
| [Performance 40210112771](https://github.com/vpsfreecz/haveapi/actions/runs/40210112771) | Resolver exits 3; artifact stderr: `HaveAPI::PerformanceCI::Error: Invalid published release lineage proof` | B pins a raw Git diff digest containing repository-dependent abbreviated index object IDs. Proof rendering is not canonical. No timed comparison started. The aggregate failure correctly propagates resolver failure. |
| [Server RSpec 40210112783](https://github.com/vpsfreecz/haveapi/actions/runs/40210112783) | Ruby 3.2/3.3/3.4 each report 561 examples, 9 failures | B's new specs assume real maintenance history and root tooling dependencies. The shared workflow deliberately uses `fetch-depth: 1` and prepares only the component bundle. |
| [Release build-only 40210113193](https://github.com/vpsfreecz/haveapi/actions/runs/40210113193) | Server suite reports 561 examples, 6 failures, all B lineage cases: `Invalid published release lineage proof` | The independent full-history/full-input path exposes the same raw-diff digest portability bug. The publishing job was skipped. No Actions release artifact was uploaded. |

The server log directly confirms both unsupported new-spec assumptions:

```text
Cannot establish ancestry: fatal: Not a valid commit name
8b7abc097db49893da9cc8fa4395648901fec71d

Missing resolved lock /home/runner/work/haveapi/haveapi/Gemfile.lock
```

For Ruby 3.4 these appear at original failed-log lines 778 and 768; final count
is line 883. Ruby 3.2 and 3.3 have the same count and causes. The actual workflow
definition at C is `.github/workflows/_ruby-rspec.yml`: checkout depth 1,
Bundler setup working-directory `servers/ruby`, then `bundle exec rspec`.
Production input and ancestry checks should remain strict; tests must provide
their own appropriate history/input fixtures rather than inherit the developer
checkout's full objects and ignored root lock.

## Raw diff portability reproduction

Read-only Git rendering against the unchanged exact objects establishes the
fault without rerunning application tests. The ranges are original reference
`b85ec364057f536940d689b09e612512ffffaf82` → mapped counterpart
`8b7abc097db49893da9cc8fa4395648901fec71d`, and published metadata commit
`1c3c98f0d77e0b23c8da1a8937f25c5799864a3b^` → that metadata commit.
Both complete ranges remain byte-equal with each option below:

| Additional `git diff --binary` option | Bytes | SHA-256 |
| --- | --- | --- |
| `--abbrev=7` | 8,318 | `98dc114609a977d8032ed133ea79aa049228dfcf6a1a0fdcecda2b98d6d2ae7e` |
| `--abbrev=8` | 8,350 | `7fe745206de33755d0388284c6afeea6e557ed96d9644f9c81419a248b05f2d1` |
| `--full-index` | 9,374 | `0a008acbb46434a0914421064149ce154ea41a6e82a29022c53e666eb2066fd5` |

The default local text diff contains `index 5b671a9d..07d30b81 100644`.
`--binary` alone does not force full index IDs for these text changes. The
hardcoded DELTA equals the local eight-character rendering. Git's default
abbreviation varies with repository/object population, making that digest an
invalid portable acceptance condition. All four immutable trees remain fixed.
The hosted failure artifact retains only the generic proof rejection, not its
raw attempted diff; its precise diff bytes cannot be recovered from that artifact.

The minimal production repair is to generate both full binary diffs with explicit
full index IDs and stable rendering options, then verify/re-pin that exact
canonical delta. Preserve the complete-delta equality, exact tree IDs, mapped
ancestry, original reference and budget gates. Add a control using different
abbreviation defaults. Do not accept an arbitrary hash or ignore entire files.

## Narrow proposed remediation and acceptance

Follow the architect's updated master-first brief. Author the existing B
adaptation plus these remediations on the same-session master feature, review
and verify it there, integrate only under the user's master authorization, then
backport with `-x` and restore .2 metadata separately. This file authorizes no
source mutation or branch operation.

- Canonicalize the existing proof serialization and update its exact evidence.
- Make the new specs independent of live maintenance HEAD/history and root
  lock availability. Include a true shallow/component-only control; retain the
  existing negative test that production rejects missing locks.
- Exercise ordinary master/literal-ancestor behavior when maintenance objects
  are absent. The current helper unconditionally probes the mapped commit;
  master must not acquire an unnecessary maintenance-object requirement.
- Keep focused resolver/runner/comparator, raw/replay/output negatives and
  deterministic performance specs; pass changed-file syntax/RuboCop/hooks and
  the relevant Ruby CI matrix. Re-review the affected B lane and complete final
  history/new head before long campaigns. No blind rerun can repair these defects.

No public API/runtime, fixed budget, calibration reference, fixture expansion or
new provenance framework is needed. Final edits/check selection belong to the
architect/lead and assigned implementation owner after serialized transfer.

## Preserved original evidence

Raw logs are session-local, untracked supporting artifacts:

- `ci-40210112771-original-failed.log`, SHA-256
  `885812b62db58028877cc8107ed1a9b0cadff0faba4dd241a04be6a279679003`.
- `ci-40210112783-original-failed.log`, SHA-256
  `b8ebfa4cfe99724570c114ea45ea04f2b93d186123cdc7b649c8a40ac6d96cad`.
- `ci-40210113193-original-failed.log`, SHA-256
  `2478ba214c4625b87f9ba16d4ab703730c16ca3eaf3442cd24aac9bc03c9e050`.

Performance artifact ID `12605054633`, name `performance-40210112771-1`, is
downloaded in `ci-40210112771-original-artifacts/`. It contains original event,
workflow receipt and resolver stdout/stderr. The event is a new feature push,
before all zeroes, after exact C. Server and release runs list zero artifacts.
No credential values were printed or recorded in this diagnosis.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/>
