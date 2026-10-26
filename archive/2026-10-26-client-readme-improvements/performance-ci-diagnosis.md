# Old-head performance CI diagnosis

Run [40311552933](https://github.com/vpsfreecz/haveapi/actions/runs/40311552933)
failed with runner exit 3 and `HaveAPI::Performance::ContractError`:
`Calibration environment mismatch`. The aggregate gate consequently failed.
The retained report has status `error`, not a measured pass, regression or
inconclusive timing result.

The exact compared source pair was baseline
`39e98020070fabcceca32f8fabcf0440f0d8763e` and candidate
`b8c726274dc7ac449b17f72701c1ad423604d2d6`, quick profile. The workflow selected
the whole feature branch against captured default and considered it relevant.
Only nine Markdown files differ. Ruby server/benchmark sources, neutral fixtures,
Rust generator/runtime/template sources, dependency declarations, flake inputs,
performance workflow and comparison entry point are unchanged.

The sole delta between retained `samples.json.environment` and the budget's
required `environment.weekly` is `gems.faraday.version`: actual `2.15.1`,
calibrated `2.15.0`. The classifier checks exact environment equality at
`servers/ruby/benchmarks/performance_compare.rb:331`. This is dependency
resolution drift against the retained calibration, rather than evidence of a
documentation-induced runtime regression or ordinary timing noise. Both sources
used the workflow's common prepared dependency environment; that common graph
still fails the fixed calibration identity requirement.

Retained identities:

- harness SHA256: `5c4b2cf6976150bff9204dc468b2b54e1ed1a44d6cd4f299b90324954f97dcb3`
- classifier SHA256: `1d75af472fac704ea978c8f8884ef81cd6f95574efe7472742add2f88b7c38ac`
- budget SHA256: `57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050`
- baseline archive SHA256: `959600073c8af25bfe29ffab212e7e59d2ed2e5722fe76412991541049a0b487`
- candidate archive SHA256: `1e74c7149f1646d50e47564a04d5f5752bf8df623bebf0130ab29b6419bc42ff`

Quick timing policy remains 1 second baseline work, 750 ms minimum observed
batch, three baseline/self pairs, five baseline/candidate pairs, four-of-five
agreement, 20% relative wall/CPU budget and 50 ms minimum detectable batch
increase. The environment contract rejects this campaign; those timing gates
do not establish an accepted result.

Evidence remains under
`artifacts/ci-final-head/40311552933/performance-40311552933-1/`, especially
`results/report.json`, `results/samples.json`, `runner.stderr`, `selection.json`,
prepared locks and source manifests. The failed workflow log is
`artifacts/ci-final-head/40311552933-failed.log`; all eight old-head run
conclusions are in `artifacts/ci-final-head/final-status.json`.

No job was retried and no budget, reference, dependency or runtime source was
changed. The narrow documentation correction can be consolidated and published
independently. Its new-head workflows provide evidence for that new revision;
a later green result would not erase or resolve this original mismatch. A
performance-environment repair or reference migration needs its own scoped
design and verification under `doc/performance.md`.

## Refreshed final-head observation

Run40314732573 compared exact refreshed base
`ec84ec874eb209ab59848873998456293ddf3c52` and final candidate
`cb43ae2367b12e22e602d69312bfd1f7331b4995`, quick profile. It also rejected
before measurement classification with runner exit3 / report statuserror /
`Calibration environment mismatch`.

The retained environment has exactly two deltas against calibration: Faraday
actual2.15.1 vs required2.15.0, and Ruby executable
`/nix/store/jnjll1yxfq02bdcw5pjf9gl86wh8gfhq-ruby-3.4.11/bin/ruby` vs calibrated
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`.
Both Ruby versions are3.4.11; the upstream Nix update changed the store closure.
This remains an unvalidated environment gate, not a measured pass/regression.
Evidence: artifacts/ci-refreshed-head/ retained performance bundle and final.jsonl.
No retry, reference/budget change or runtime repair was performed.
