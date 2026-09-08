# Focused review rerun: stable alert identity

Read `review-packet.md` for the user request, repository paths and topology.
This packet supersedes its head and label-compatibility details.

- Configuration base remains `e26f0a3360e1a20e76c3c0ef4193448584a8c1bb`.
- Initially reviewed head: `0297b0c3bfcec0a4cc0e32fa294c996bfe978afa`.
- Current amended head: `08dae58b16abdde30cff1572478b29343ed32fc4`.
- `git diff 0297b0c3 08dae58b` isolates the review remediation; inspect it in
  the worktree named by the original packet. The feature is still one commit.

The risk lane found that the two query branches produce different target label
sets. With the new two-minute confirmation, an ongoing failure temporarily
resolved when stale metrics disappeared from the lookback or returned while
still stale. This was reproduced with promtool.

The remediation gives the rule static `alias = "status.vpsf.cz"`,
`instance = "status.vpsf.cz:443"` and `type = "vpsf-status"` labels. These are
the existing singleton scrape job's identity in
`modules/clusterconf/monitor/default.nix`. Normal stale-render labels remain
the same; missing-metric alerts acquire that same identity so the pending/firing
state carries across both conditions. Query semantics, annotation `$labels`,
thresholds, confirmation, evaluation and scrape intervals remain unchanged.

The supported target remains this one public status service. No multi-target
configuration API or generic monitoring abstraction is introduced. The plan
explicitly records that changing the target or its scrape labels must also
update this dedicated alert identity. Old missing-metric notifications may
group separately during a mixed rollout because the old rule lacked these
service labels; the rule-group move already resets state at upgrade.

A seventh production-rule fixture asserts uninterrupted firing at minute 18
when metrics disappear and at minute 21 when a still-stale sample returns;
a fresh sample at minute 22 clears it. The existing absence expectation now
checks the same service labels. All seven scenarios pass through
`nix build .#checks.x86_64-linux.vpsf-status-prometheus-rules --no-link -L`.
Commit hooks passed without warnings. No integration build has started.

Rerun only risk/compatibility and architecture/repetition, at `gpt-5.6-sol`
`xhigh`. General and scope findings remain recorded for the original change;
the remediation is bounded to the previously accepted single-service policy.
Review the new handling directly and report any concrete remaining issue or
accepted residual limit. Do not edit files, spawn agents or start builds.
