# API and KB integration preparation

Status: **prepared and handed to the lead; no integration performed by implementer0**. The lead reports the user's explicit “merge” authorization for the five prepared repositories. The lead owns every actual repository claim, fast-forward merge, default push, remote proof and release. This preparation grants no deployment or session lifecycle action. UFW verification was withdrawn before launch after the user accepted the original mirror dependency failure as out of scope; that original failure and unknown deeper cause remain retained.

Session identity and environment both match `2026-11-01-published-advisory-corrections` / `/home/aither/workspace/ai/vpsfree.cz`. Workspace Git/hooks procedures, both repository AGENTS files, API development commands, and the selected package's `workspace-host coordination guide` were read. Selected package: `/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`; full guide retained in the evidence directory below.

## Exact prepared targets

| Repository | Detached target | Target/default | Reviewed source |
| --- | --- | --- | --- |
| API/legacy | `/tmp/2026-11-01-published-advisory-corrections-integration-prep-20261103T132351Z/targets/vpsadmin` | `5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5` | `942c6eaed41331f823d8e0f670ed239e2b308440` |
| KB | `/tmp/2026-11-01-published-advisory-corrections-integration-prep-20261103T132351Z/targets/vpsfree-kb-contracts` | `ce2c8cd9358c3636e5d39343e595df813a0b197f` | `f97785c2c265172a4c78893e0673034fde56e4dd` |

Fresh explicit fetches and SSH `ls-remote --symref` confirm each master remains the expected default and each remote feature matches its local reviewed head. Both defaults are ancestors of the corresponding features. Features and new detached targets are clean after environment preparation. These target checkouts are separate from the preserved feature/live PHP worktrees. Feature refs remain intact. No rebase was needed.

API common Git: `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git`; origin `git@github.com:vpsfreecz/vpsadmin.git`. KB common Git: `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin-kb-captures.git`; origin `git@github.com:vpsfreecz/vpsfree-kb-contracts.git`. The KB historical bare-clone basename differs from the current upstream project name; its actual common-directory and canonical origin identity are proven, not inferred from a pathname. Exact per-target Git directories are in `integration-ready.json`.

## Declared environments and hooks

API target Nix profile `/tmp/2026-11-01-published-advisory-corrections-integration-prep-20261103T132351Z/vpsadmin-devshell` resolves to `/nix/store/5m7xf80v9h6wrscc0r6jiznhnb1b221d-vpsadmin-env`. Its ordinary default shell installs Bundler4.0.23 and the50-gem root development bundle, with Overcommit0.74.0, Ruby3.4.9 and Git2.54.0. The ignored root tool lock copied from the equal-Gemfile feature environment has SHA256 `025ff224c66e9dd1cd37c61024590ec6e179e147a230f6e5f47252e5e51adcf0` and matches the feature lock;48cached gem archives were copied into the disposable target before ordinary installation. No feature source was edited.

API common hooks were already installed and executable. Overcommit's normal configuration loader verified its existing signature with verification enabled; enabled hooks/plugins were enumerated. Four owned precommit plugins remain present/enabled: Nixfmt, MigrationSpecs, VpsadminApiI18n and VpsadminWebuiI18n. Hook/config/Gemfile/Nix source is unchanged across5586..942c. Ordinary `git hook run post-merge -- 0` and empty-input `git hook run pre-push -- origin git@github.com:vpsfreecz/vpsadmin.git` both returned0 without a ref mutation. Effective PostMerge and PrePush have no enabled tasks. Fast-forward integration creates no commit, so it does not invoke precommit/commit-message checks. Configuration and plugin signature checks stay enabled; no signing or bypass was used. Ambient Overcommit0.71.0 must not replace the declared0.74.0 environment.

KB target Nix profile `/tmp/2026-11-01-published-advisory-corrections-integration-prep-20261103T132351Z/vpsfree-kb-contracts-devshell` resolves to `/nix/store/h392k9zfx25rgza4cg9nx9j717px1chs-nix-shell-env`. Its ordinary default shell realizes Ruby3.4.9-with-packages and Git2.54.0. Neither baseline nor feature declares a hook framework; no active standard commit/merge/push hooks are installed there. No framework was invented or added. These are target-baseline integration tool environments, not new final-source acceptance runs.

Fresh preparation-only Luna/low utility `01a1a19a-6172-75d0-8bc1-1ada066a9256` and its command are terminal, exit0. Actual banner full-access/never/low and per-invocation `--disable multi_agent` were verified before release. Native driver clock:105.47s total, API46.63s, KB44.46s; the watcher's approximate94s is not authoritative. It ran no tests, merge, push or claim. Utility slot was released to implementer1 by message; no operation remains active.

## Lead-only execution handoff

Enter the ordinary prepared target Nix environment **before** acquiring its repository claim, for example from each exact target:

```sh
nix develop --profile /tmp/2026-11-01-published-advisory-corrections-integration-prep-20261103T132351Z/vpsadmin-devshell .#default --command <lead-owned API integration command>
nix develop --profile /tmp/2026-11-01-published-advisory-corrections-integration-prep-20261103T132351Z/vpsfree-kb-contracts-devshell .#default --command <lead-owned KB integration command>
```

The API shellHook performs Bundler/gem setup; environment entry belongs outside the claim. The lead's existing driver then owns one repository critical section at a time: verify held ownership, recheck exact remote target/feature plus clean target and unchanged reviewed history, perform the ordinary fast-forward merge and non-force SSH push, prove the resulting remote SHA, and explicitly release before CI, records or target cleanup. On baseline movement or hook intervention, stop/reconcile effects and return to preparation outside the claim.

API commands inside its claimed critical section:

```sh
git merge --ff-only 942c6eaed41331f823d8e0f670ed239e2b308440
git push origin HEAD:refs/heads/master
```

KB commands inside its separate claimed critical section:

```sh
git merge --ff-only f97785c2c265172a4c78893e0673034fde56e4dd
git push origin HEAD:refs/heads/master
```

Inspect normal hook output before pushing: Git may return0 even if a post-merge hook fails. No force option, hooksPath override, signature update or hook-disable environment variable is part of this package.

## Unlaunched integration observer

`/tmp/2026-11-01-published-advisory-corrections-integration-prep-20261103T132351Z/observer/` contains `launch-args.json`, the exact copied native utility TOML, catalog policy, `prompt-template.txt` and README. It was **not launched**. The lead must first set its original driver status/log and policy-gate paths, then start a fresh observer and verify the actual banner/restriction before opening the observer gate. No placeholder is executable authority.

Catalog495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7 selects gpt-6-luna/low, native `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, full-access/never. Supported CLI argv includes `--disable multi_agent` and the exact native developer instructions. Original native TOML: `/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml`. Parent-side `codex --disable multi_agent features list` must show false. The utility only observes original driver status/logs; it must never execute/import/relaunch that driver, acquire claims, merge/push, spawn agents or launch another CLI. Its files remain unique to the eventual lead batch.

Evidence root: `/tmp/2026-11-01-published-advisory-corrections-integration-prep-20261103T132351Z`. `fresh-source-remote.json`, `prepared-targets.json`, `integration-ready.json`, target-create/environment logs and `hook-prep-watcher/` preserve the exact preparation. No new acceptance tests, UFW follow-up, source/pin changes, preview/data mutation, merge/default push, claim or lifecycle operation occurred. The lead owns main state/handoff.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/).
