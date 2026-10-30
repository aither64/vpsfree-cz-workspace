# Final HaveAPI source rebind

This supplements the preserved [original review packet](typescript-review-packet.md).
It requests affected-range correspondence acceptance, not a default merge or
publication. Reviewer0 reported no findings for the original complete range,
including independent 674/674 formatter equivalence and npm archive baseline
proofs, no repeated streams and no migrations. Version remains 0.1.1; no release.

## Reviewed and refreshed ranges

| Identity | Exact revision |
| --- | --- |
| SDK common base | `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc` |
| SDK independently reviewed head | `55e03a0e0a57533f0572f6f4856af33035472408` |
| SDK final rebound head | `d14ee69953d0664b4b6d96d7b8f2a3ede4383d88` |
| HaveAPI original candidate | `f0465630595b4fd120561337b3d1d7fa96cbe221` |
| HaveAPI final candidate | `0e7166a0f8f15827bfac051666a53bf449e999ec` |

The refreshed SDK complete series remains one logical commit:
`d14ee69953d0664b4b6d96d7b8f2a3ede4383d88 Refresh offline generation for HaveAPI 0.32`.
It amends the prior unpushed logical commit; no obsolete intermediate pin commit
remains. No migrations, repeated update streams, release/deployment/consumer
boundary or incompatible behavior was added. Final diffstat remains 684 files,
+57548/-19317. Worktree/index clean; comparison captured for the final range.

## Independent correspondence checks

Read-only inspection confirmed final HaveAPI HEAD and clean worktree. Its full
old-to-new diff is exactly two added `ruby-version: '3.2'` lines, in existing
`i18n-health.yml` and `rubocop.yml` workflows. No generator/template/runtime,
VERSION, formatter configuration, source dependency or fixture change.

Parsed `haveapi-logs/candidate-identities.json` and
`haveapi-logs/candidate-identities-ci-fix.json`: all fields excluding `revision`
are equal. Independently hashed all ten actual lockfiles in the final source;
each matches the recorded unchanged digest. Original/final record file hashes:
`38744461292916f96f671544960ef88170594948acd361406c13f6179dad435f` and
`41463e0a99b756d8754bbf18e35f7d6029afc8068de1463277fa20117f7729bb`.

Recomputed the source helper identity with pinned SDK Ruby and exact final
HaveAPI load paths; unchanged values:

- Generator: `947a98d704dca737f8bef2e1042f710e77396a0a793cb7233e8093887a713d6e`.
- Shared 0.32.0 source:
  `e12f7989a028bb529f4a78a510af8e09411bbeb5eec9c782feb1fbf20862533c`.
- VERSION: `e0ccf7913110f807adecc59be43ce6fb334f82a8a7f70f70fbbba34bf1eeaaf2`.
- Formatter config:
  `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356`.

SDK old-to-new diff changes only `tools/generator.json`'s `haveapi_revision`.
Parsed pin objects excluding that field are equal. The following command passes
with empty output:

```sh
git diff --exit-code 55e03a0e0a57533f0572f6f4856af33035472408 \
  d14ee69953d0664b4b6d96d7b8f2a3ede4383d88 -- . \
  ':(exclude)tools/generator.json'
```

Thus every generated file/manifest and schema/provenance/lock byte remains
identical to the reviewed SDK head. Original exhaustive formatter-equivalence,
API/runtime unchanged and no-release evidence is preserved directly, without
reclassifying the two workflow lines as a generator change. No HaveAPI checkout,
bundle or ref was mutated by the SDK owner.

## Affected verification and gate

Fresh policy-selected Luna/low watcher ran the exact
[rebind batch](typescript-rebind-command.sh) against the final HaveAPI source:
generation, deterministic `--check`, and source/shared-input/local-formatter
refusal regression. **Passed, exit 0, about 41 seconds**, 1/1 regression test,
zero failures. No process remains. The watcher reported the requested raw log
file was absent; its completion report retains command/revisions/result and
TAP summary. No duplicate rerun was used solely to recreate that log.
`git diff --check` also passed before amendment. Original build/typecheck/strict
consumer/unit evidence remains applicable because all its inputs are unchanged.

Push and package/CI batch remain held pending the lead/reviewer's affected-range
acceptance. Updated exact-head proposed package batch:
[final package command](typescript-package-final-command.sh), not executed.
The old proposed command is retained as historical preparation only. No default
merge, tag, npm publication, publisher change or runtime/version bump occurred.
