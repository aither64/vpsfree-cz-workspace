# Public CI evidence: advisory visibility

Package A, implementer0, 2026-11-04. Retrieval and comparison are complete.
Source, manifest and example IDs match; dependency graph, seed/order and runner
image differ. This evidence does not isolate a cause. No project edits/tests,
workflow reruns, production access or cross-session access were performed.

## Native identity and outcome

Both public `push` runs use attempt **1**, `.github/workflows/api-specs.yml`,
source `4ac49f49e63545200df8afa920c6eafda8722523`, tree
`98e2401bcbfb42a60eaf5d27a1399e798c86aa2b`, from
`git@github.com:vpsfreecz/vpsadmin.git`. The source commit changes only `AGENTS.md`
and `docs/api-schema-export.md`.

| Input/result | Failed | Passing comparison |
| --- | --- | --- |
| Run | [41822368583, #811](https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368583) | [41679570284, #810](https://github.com/vpsfreecz/vpsadmin/actions/runs/41679570284) |
| Branch at trigger | `master` | `2026-11-03-vpsadmin-client-sync` |
| Created, UTC | 2026-11-04 11:37:02 | 2026-11-03 16:58:21 |
| Full/platform-operations job | [126548402180](https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368583/job/126548402180) | [126069310937](https://github.com/vpsfreecz/vpsadmin/actions/runs/41679570284/job/126069310937) |
| Result artifact | `13318816860` | `13254476736` |
| Manifest artifact | `13316939449` | `13251763651` |
| Seed | `13353` | `56402` |
| Native summary | 239 examples, 1 failure, 0 pending | 239 examples, 0 failures, 0 pending |
| Target execution position | 237 of 239 | 205 of 239 |
| Target duration, seconds | 7.183617228 | 131.616067242 |

Target in both native results is
`./spec/api/resources/security_advisory_spec.rb[1:3:2]`, source line 487,
“VpsAdmin::API::Resources::SecurityAdvisory Read visibility scopes CVE, node and
update reads and included parents without changing retained history”. The failure
is `RSpec::Expectations::ExpectationNotMetError` at assertion line 522:

```text
{role: :anonymous, path: "/v7.0/security_advisory_cves", state: "draft", http_status: 200, response_status: false, error_class: "Hash", error_fields: ["security_advisory"], requested_meta: {count: true, includes: "security_advisory"}, returned_meta: nil}
```

The exact API validation message, rejecting method and record ID were not saved.
Neither target job has an `API_SPEC_REQUEST_EXCEPTION` marker. The saved Hash
field error supports rejection before a successful list response, without proving
which validation branch rejected it.

## Verified graph and other inputs

There is no tracked `api/Gemfile.lock` or standalone lock artifact among either
run's 52 artifacts. Complete `/usr/bin/cat Gemfile.lock` output is recoverable.
`log-reconstructed-api.Gemfile.lock` files are **log reconstructions**, not native
lock artifacts; both exactly match the native environment JSON's SHA256 after
removing only GitHub timestamps and retaining whitespace/final newline:

| Lock | Bytes | SHA256 | Combined job log lines |
| --- | ---: | --- | --- |
| Failed | 7874 | `aa49ff9efa5e9beaa4ea278eabfc17fd40ed032d99d0705ee9f18a880d60cd21` | 507–841 |
| Passing | 7862 | `cc8bafa0ce1ba177ee4eb86bf29b7b644a5ad90a14dcef36aad1022ad62a1b47` | 501–835 |

[Complete lock diff](evidence/ci/lock-diff.patch): only
`activemodel`/`activerecord`/`activesupport` change from **8.1.4** (passing) to
**8.1.4.1** (failed), and `mime-types-data` changes from **3.2026.1027** to
**3.2026.1103**. All other lock text agrees. Each lock preserves 122 resolved gem
specifications and edges, including excluded development dependencies; both
native setup logs report 34 direct dependencies and 104 installed gems.

Both native environments record Ruby
`3.4.12 (2026-10-23 revision 366f5fdc00) +PRISM [x86_64-linux]`, Bundler **2.6.9**,
RSpec **3.13.6**, HaveAPI/client/generators **0.32.2**, and MariaDB
`11.8.6-MariaDB-5ubuntu0.1 from Ubuntu`, `REPEATABLE-READ`,
`innodb_snapshot_isolation=0`. MariaDB server/client/header apt packages match
`1:11.8.6-5ubuntu0.1`. Workflow environment: `RACK_ENV=test`,
`VPSADMIN_PLUGINS=all`, `SPEC_MODE=full`, `TOPIC=platform-operations`,
`BUNDLE_WITHOUT=development`, `BUNDLE_JOBS=4`, `BUNDLE_RETRY=3`.

Both use Ubuntu 26.04.1 and runner 2.338.2, but image/provisioner/region differ:

| Input | Failed | Passing |
| --- | --- | --- |
| ubuntu-26.04 image | `20261025.179.1` | `20261101.186.1` |
| Provisioner | `20261021.618` | `20261028.624` |
| Azure region | westcentralus | centralus |

Resolved actions match: checkout `3d3c42e5aac5ba805825da76410c181273ba90b1`,
upload-artifact `cf430e030ddbb5b0abf93d22962f4752f3646cd9`, setup-ruby
`de492cf36cbab201753d720ce4f4e336cd688c94`. Native logs preserve their refs,
provisioner commits, cache keys, apt package lines and command environment.

The native manifests are byte-identical, eight files, SHA256
`331ca14d9fd819078fe7a325a17f21d6a4bf85b78cc16beb47d5417b6d277052`:
`incident_report`, `lifecycle_bypass`, `object_history`, `oom_report_rule`,
`oom_report`, `security_advisory`, `transaction_chain_read`, `transaction_read`,
each under `spec/api/resources/` with `_spec.rb` suffix. In `api/`, CI loads the
sorted manifest into `files`, then runs:

```sh
bundle exec rspec "${files[@]}" --format documentation --format json \
  --out "tmp/rspec-results-full-platform-operations.json"
```

Source `.rspec` requires `spec_helper`, which sets random order and Ruby's PRNG
seed from RSpec. Native results exclude generator examples. CI uses apt and
`ruby/setup-ruby`; **no Nix command/store receipt applies**. Complete source
`flake.nix`/`flake.lock` are retained as local-reproduction reference only.

## Saved evidence and acceptance checks

[Raw evidence](evidence/ci/) is Git-ignored. Each `<run>/attempt-1/` contains the
unchanged native results/environment JSON under `results/`, manifest under
`manifest/`, original artifact ZIPs, full original `logs.zip` and extracted logs,
run/attempt/job/artifact API JSON, timestamped command/hash retrieval receipts,
`input-receipt.json`, reconstructed lock and full `resolved-lock-graph.json`.

Failed combined log is `logs/9_API specs (full) - platform-operations.txt`;
passing is `logs/16_API specs (full) - platform-operations.txt`. Both full logs
ZIPs have 54 members and pass CRC checks. Public ZIP digests independently match
GitHub metadata:

| Artifact | SHA256 |
| --- | --- |
| Failed results `13318816860` | `93e5b78dfe64d8c2c8cc4d9df57cfdfe373b14cb8f48b5aeecbb2e662ceb1a6e` |
| Passing results `13254476736` | `21ab14f6f1479cb2a8175ad22886d9a9bdad53505e6ed90f3f7c344ba155c1c6` |
| Failed manifest `13316939449` | `31d724bb86578558a408ea0c20af8bd2acc517247ce24e40d50826dac5ebd950` |
| Passing manifest `13251763651` | `108226ea52ccd3eb216d3e8e8c7422abef971e08b49c732059c3d3271fd31ba2` |

[Comparison](evidence/ci/comparison.json) verifies complete JSON parsing,
run/attempt/source/artifact identity, all 27 jobs and 52 artifacts, 239 unique
example IDs, identical ID sets and only the target status difference, with no
pending-reason difference. `native-example-order.tsv` preserves all execution
IDs; `example-order-log-map.json` corroborates every JSON entry against successive
native documentation lines. Graph receipt reached Package B before its tests.

`source/` preserves the complete public source archive, Git tree inventory,
source/input blob and SHA256 receipt, workflow, Gemfile/plugin Gemfile, spec
helpers, database bootstrap and Nix reference inputs. Source archive SHA256:
`ad0dd1ec83aab2a9372c673774b11c3fbcae2f51bef9582f6085864c2d94c927`.
[SHA256SUMS](evidence/ci/SHA256SUMS) covers every raw file except itself.
Retrieval used explicit read-only `gh api` run/attempt/artifact/log endpoints on
2026-11-04; all requests succeeded. Exact commands/times remain in receipts.

## Exact remaining gaps

No retrieval blocker remains. Native evidence lacks the validation message and
rejecting branch, full process/system environment, complete apt/runner state,
installed gem/cache binary checksums and database state. Locks lack per-gem archive
checksums. The complete generated lock bytes are independently recovered by hash.
A local graph/seed/source-matched run still differs from the native CI machine;
record its actual Ruby/platform/MariaDB/bundle differences. Package B owns causal
experiments; Rails-only or order-only causality remains unproven by Package A.
No API/client/schema/deployment contract changed. Raw evidence remains disposable
under workspace retention; this Markdown retains the critical provenance.

[Stable session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-vpsadmin-advisory-visibility-ci/).
