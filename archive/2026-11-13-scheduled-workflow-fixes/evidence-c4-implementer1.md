# C4-org: repository lock is the only confctl revision authority

Owner implementer1; sufficient lead-released C4 brief in design.md. Prior C3
receipts describe historical delivered behavior, not the final workflow design.
Implementation, quick checks, independent final review and focused acceptance
are complete; both intended commits are published with remote proof. The
prepared target window was returned to lead, which has completed approved
integration. The fresh hosted workflow is observed solely by root's managed
watcher and has now passed. Lead fully accepted C4 delivery; no package work
remains.
Source boundary: only `flake.lock` and `.github/workflows/daily-update.yml`.
No provider source, normal flake declaration, channel, registry or extra wrapper.
Implementer1 performed no default mutation, claim, dispatch or CI observation;
released target preparation is recorded below.

## Lead-reported integration and fresh run

Lead reported exact reviewed `15352aeb13c4011b5dd1a1f78d1fdcb08f7c2420`
fast-forwarded from `04b85313c0fe30be13e73c19acaa2760283e7874`, using the
prepared scoped compatible bundle/profile and normal bundled Git/hooks. Target
was clean and SSH remote proof matched the exact final head. Claim
`2be8f01a-8b5f-49ea-86aa-c507098ed641` held 18:34:14–18:34:54 UTC, then released
and verified; lead's owned PTY61065 exited 0 with no unresolved effects.

After release, lead dispatched fresh master
[run43484020423](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/43484020423),
attempt1, event head15352aeb. Root managed watcher
`23d4b2f4-840e-4622-a4e2-2b32c47c849a` is the sole observer under its frozen
Luna/low/full-access policy. These are lead-reported receipts, not a duplicate
member observation. Implementer1 retains actual-failure diagnosis ownership if
root reports one. Target window remains returned; no further source/target/check,
dispatch or lifecycle operation was taken for this reconciliation.

Lead subsequently reported final hosted SUCCESS for run43484020423 attempt1 at
exact integrated15352aeb, workflow_dispatch 18:34:57–18:39:14 UTC (4m17s).
All steps, hooks, updates, final guard and push succeeded. Final output was
`No changes.` and `Everything up-to-date`; no generated update is claimed.
Managed monitor23d4 reported terminal passed/exit0 with all owned cells/sessions
ended. Root's fresh fetch confirmed source/master exact153, clean feature,
ancestry and absence of the YAML override.

Root-hosted artifacts:
`/tmp/scheduled-workflow-fixes-c4-org-hosted/final.json` and `final.log`;
reported log SHA256
`b293501db3bd04045b7f6047e36063364addfc28e48d523e1727b08e40e71344`.
Counterpart vpsFree run43484770367 also succeeded. Lead confirmed provider auto
Tests43474592486 SUCCESS at ff, closing the historical CI gap without a local
rerun. This is receipt-only reconciliation of the sole root observer's report,
with no duplicate check, source/target/default mutation or lifecycle action.

## Current range and implementation

Fresh SSH fetch and ordinary hooked fast-forward moved the own feature branch
from merged `69edee80` to current generated master
`04b85313c0fe30be13e73c19acaa2760283e7874`, retaining generated
`f8c8aa3` (nixpkgs) and `04b8531` (vpsadminos) history.

The normal current declared-shell command
`nix develop ... -c confctl inputs update --commit confctl` generated separate
commit `cde440b16d65d597caf5e223dd25ba760d584645`, subject
`inputs: update confctl to ff5e0177`. Only flake.lock changed (+51/-16).
Actual updating executable was
`/nix/store/9r7w7d05wjn9y8kh4l78gk6nigk2cbw6-confctl/bin/confctl`, caller Ruby
3.3.10 and declared Bundler 4.0.7. Normal hooks passed (TextWidth advisory on
generated changelog header); generated message remains as produced by confctl.

Final base `04b85313c0fe30be13e73c19acaa2760283e7874` → head
`15352aeb13c4011b5dd1a1f78d1fdcb08f7c2420`. Complete chronological series:

1. `cde440b16d65d597caf5e223dd25ba760d584645` — generated confctl input update.
2. `15352aeb13c4011b5dd1a1f78d1fdcb08f7c2420` — `ci: use the locked confctl input`.

Two files, +54/-20; full diff retained as `final.diff` in the artifact root and
available directly from the exact range. Separate commits preserve the generated
input history and make the workflow correction independently clear, as required
by the brief. No superseded unmerged approach or migration remains. One final
confctl input-lock stream, no workflow-pin stream. Earlier workflow pins are in
already integrated C2/C3 history and are preserved as historical boundaries.
Normal branch publication is a fast-forward from the previously published head;
fresh default remained 04b85313, feature remote matched 15352aeb, and the final
comparison capture binds this exact range. Source/index are clean.

Semantic old/new comparison uses the existing provider LockGraph, independent
of generated node IDs. Seven changed paths, all confctl-owned:

```text
confctl
confctl/nixpkgs
confctl/vpsadminos
confctl/vpsadminos/netlinkrb
confctl/vpsadminos/nixpkgs
confctl/vpsadminos/nixpkgsUnstable
confctl/vpsadminos/ruby-lxc
```

Expected resolved graph matches provider ff5e017780a35fb97b549db2a51b570193867c3b,
its OS 67fcc17372d175b036706a1459a8b471bfc225e0, Nixpkgs
8b8c811c7c2541c30382c5de7ed26be055569c60 and unstable Nixpkgs
f13ff45afd1bb73e640eaa08a7066dbed07e3238. Root nixpkgs
ac588ef1c914865dad517b337ea0eb9694a4021c and root OS
c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62 remain unchanged, along with all
unrelated semantic paths and root follows relationships. Normal
`confctl.url = "github:vpsfreecz/confctl"` and all flake.nix bytes are unchanged.

The committed workflow removes CONFCTL_FLAKE and replaces all three nested package
invocations with plain confctl inside the same declared-shell blocks. Channel
arguments, flags, hooks, baseline/final guard, permissions/authentication,
cron/manual trigger and ordinary push stay byte-identical after inverting only
those removals. There is no scheduled confctl self-update.

## Quick preparation and checks

- Lock JSON and semantic graph scope passed; expected provider graph asserted.
- Workflow YAML, exact inverse byte comparison, three confctl calls inside
  existing declared-shell heredocs, and all five extracted `bash -n` bodies
  passed. No workflow provider pin or override remains.
- Declared bundle/tool preparation, channel/machine inventory and actionlint
  passed under fresh native utility `/root/c4_org_environment`, exit 0 in
  50.4 seconds. Source cell and exec session 8762 ended with no running effects.
  Command: `bash /tmp/2026-11-13-scheduled-workflow-fixes-c4-org.bflRyY/prepare-environment.sh`.
  Tested source was committed input cde440b plus the exact owned workflow bytes
  subsequently committed as 15352aeb. No source edit or commit occurred in the
  utility command.
- A fresh copied Gemfile/lock in the artifact directory's `bundle-env` lets the
  real declared shell bootstrap its compatible bundle. This preserves the old
  source cache and existing detached target's symlink inputs; no ABI-based reuse
  or target operation. Actual new Ruby is 3.4.9, ABI 3.4.0, with declared Bundler
  4.0.7. Original cache remains untouched at Ruby 3.3.10. Copied Gemfile and lock
  were byte-compared to the repository after setup; all five project gems are
  pure Ruby, with no `.so`/`.bundle` extensions in the isolated cache.
- Installed watcher policy was reread: package
  `0s5dljmmfngj7ia2r9lfkxwydnfiz6b6-dev-workspace-0.2.0`, schema6 catalog
  `f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`,
  Luna/low, full-access native utility. Parent stayed active; no duplicate polling.

New environment identities:

- Declared package `/nix/store/v4b3r3r8102kyf92lidwvk62plpjs13j-confctl`, source
  `/nix/store/1qw3c7q3r67drrv0z4vmac9g70pvxyf5-source`: exact accepted C3
  provider package/source/input identities, with derivation
  `/nix/store/6nq336f5rfs8jgd38bsmdgpdhy5rw0rd-confctl.drv`. Reuse the full
  package/source/NAR/graph and 225-spec/110-file/actual packaged guard+hook proof
  in [evidence-c3.md](evidence-c3.md); no provider suite repeated. Same receipt
  supplied directly to implementer0 for its matching provider derivation.
- Actual caller Ruby executable
  `/nix/store/pnyd647xzsszp5r6vicpsl7q9fsz5xyk-ruby-3.4.9/bin/ruby`.
- Declared shell derivation
  `/nix/store/x5jharjl5nfiv16nqd3sx9h0w73ainqx-nix-shell.drv`;
  profile `/tmp/2026-11-13-scheduled-workflow-fixes-c4-org-shell` resolves to
  `/nix/store/1sxjac78h9bqzkycjlgpsbyqdbadqlir-nix-shell-env`.
- Isolated bundle: artifact-root `bundle-env/.gems/ruby/3.4.0`, Overcommit
  0.68.0, childprocess 5.1.0, iniparse 1.5.0, logger 1.7.0, rexml 3.4.4.
  The same declared shell and isolated bundle ran the ordinary workflow source
  commit; pre-commit and all commit-msg hooks passed cleanly.
- Actionlint 1.7.12, shellcheck 0.11.0 and pyflakes 3.4.0 came from the adopted
  provider's locked Nixpkgs tool set. No action versions were changed.
- Channels evaluated as nixos-stable→root nixpkgs ac588ef1 and os-staging→root
  vpsadminos c0ad0ad8. All eleven machines evaluated: builder, cache,
  docker-registry, gh-runner1–4, images, iso, www and proxy. No node/kernel build.

Artifacts: `/tmp/2026-11-13-scheduled-workflow-fixes-c4-org.bflRyY` contains
the pre-update lock/base, generated update log, canonical old/new graphs and
changed-path inventory, plus fresh-environment commands/log/exit/inventory and
declared-shell derivation receipts. Driver shell syntax was checked before
execution; one draft nested-quote typo was removed before any environment run.

## Review and remaining acceptance

Lead accepted reviewer0's all-four-lane final review at exact 04b85313..15352aeb
with no findings, including whole history, the two-commit split, no migrations,
single input stream, documentation and actual sole-lock authority. Focused
post-review acceptance and conditional target preparation passed below;
implementation owner retains follow-up findings. No CI observation or default
mutation. Library/tool adoption remains within C4's compatibility
brief; no production system or persisted schema change is deployed. New library
configuration-info metadata applies to future generated systems only. Recovery
uses additive source/input corrections while keeping the sole lock authority;
an older provider may not retain the guard/C3 behavior.

Architect clarified the post-review check baseline: save the adopted final lock
and compare it with exported HEAD:flake.lock through the declared plain confctl.
Record exact file hashes, executable/package identity and exit status, scoped
as a real no-change executable/guard wiring check. Pre-adoption 04.lock is not
the baseline for a daily channel transaction. This no-op does not independently
retest a changed update/rewind; exact accepted C3 proof supplies that coverage.
The exact no-change acceptance has now passed with no regeneration or source
change.

Product documentation needs no change in this two-file package: the normal
input declaration, declared-shell command contract and provider behavior are
already documented by their owner. This receipt holds individual execution,
exact identities and compatibility constraints; lead owns initiative state.

Receipt SHA256:

```text
6d55920928911f2b09a794522f5de44b1b50a4675cf9d088ba3dc7871a2c50eb declared-shell-derivation.json
ff41d0b4f453a46872411655cc94c3da7deeebb15d713954b43755727ac3e118 environment.log
77cf1df44f0da5af6c70a63338d33ef2c1bdcbaba421b38a44c408b458637fec semantic-before.json
ab116f88ffde3b7014c688f747d83714c5a34a21aa1102b8f3458f57804f1e97 semantic-after.json
```

## Focused final acceptance

Fresh native utility `/root/c4_org_focused_acceptance` ran
`bash /tmp/2026-11-13-scheduled-workflow-fixes-c4-org.bflRyY/focused-acceptance.sh`
once after review release, exit 0 in about 20 seconds. Installed package/catalog
and native full-access Luna/low policy were reread before launch. Session 92845
and all operation cells ended with no remaining effects; parent stayed active.
Terminal result was reported before target work or receipt expansion.

Actual final-source provenance resolved through the normal configuration input:

```json
{
  "revision": "ff5e017780a35fb97b549db2a51b570193867c3b",
  "source": "/nix/store/1qw3c7q3r67drrv0z4vmac9g70pvxyf5-source",
  "package": "/nix/store/v4b3r3r8102kyf92lidwvk62plpjs13j-confctl",
  "derivation": "/nix/store/6nq336f5rfs8jgd38bsmdgpdhy5rw0rd-confctl.drv",
  "shell": "/nix/store/x5jharjl5nfiv16nqd3sx9h0w73ainqx-nix-shell.drv"
}
```

The actual declared executable was the package's `bin/confctl`, with caller Ruby
3.4.9 at the pnyd647 store path above and Bundler 4.0.7 using the isolated fresh
bundle. Source/index remained clean at reviewed 15352aeb. Exact provider package,
source and inputs match accepted C3; its mixed/rewind/transport proof is reused,
with no repeated provider suite. Actual new-caller hooks were covered by the
normal 15352aeb source commit receipt from the same prepared shell/bundle.

Saved `adopted-baseline.lock` from the final reviewed working lock; exported
`HEAD:flake.lock` to `final-head.lock`. Both SHA256 values were identical:

```text
b32c83170638732275698f1bad77487362df61147c2afe87dfcbd21a90d5d143
```

Inside the real declared shell, from the repository root, ran plain:

```sh
confctl inputs check-update --old-lock "$artifacts/adopted-baseline.lock" \
  --new-lock "$artifacts/final-head.lock"
```

Result `No changes.`, exit 0; both supplied files and reviewed source stayed
unchanged. Scope is actual no-change executable/final-guard wiring, not another
new-update or rewind test. No channel regeneration, node/kernel build, provider
suite or CI observation occurred. Fresh final hosted workflow acceptance remains
lead-owned.

## Target preparation returned to lead

After focused PASS only, entered the released existing target:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/merge-targets/vpsadminos-org-configuration`.
Fresh-fetched origin; verified master04 and feature153. Installed/signed normal
hooks with the compatible C4 shell/bundle, then normally fast-forwarded the
detached baseline from previously integrated69 to generated current default
`04b85313c0fe30be13e73c19acaa2760283e7874`. No feature merge or default push.
Final target is clean/detached at04, with FF ancestry to exact feature
`15352aeb13c4011b5dd1a1f78d1fdcb08f7c2420`; fresh remote snapshots matched both.
Known quick preparation completed inline in 8 seconds, exit 0; session31295
ended with no remaining effects. Window explicitly returned to lead immediately
with raw readiness, before these prose updates; no subsequent target operation.

The target remains at the old default lock until lead integrates C4. Its prepared
invocation deliberately uses the reviewed feature's frozen C4 profile and fresh
Ruby3.4.9 bundle, compatible with the incoming adopted input. Existing target
`.gems/ruby` still aliases the old same-session source cache, and its private
`.bin` is preserved. Preparation made no ABI-based reuse or old-cache rewrite.
Exact child invocation for lead's approved Git operations:

```sh
cd /tmp/2026-11-13-scheduled-workflow-fixes-c4-org.bflRyY/bundle-env
BUNDLE_GEMFILE="$PWD/Gemfile" BUNDLE_APP_CONFIG="$PWD/.bundle" \
  nix develop /tmp/2026-11-13-scheduled-workflow-fixes-c4-org-shell \
  -c bash -c 'cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/merge-targets/vpsadminos-org-configuration; exec bundle exec "$@"' \
  bash <approved-git-arguments>
```

The environment is scoped to that child; workspace coordination CLI must run
outside it. Prepared GEM_HOME is artifact-root
`bundle-env/.gems/ruby/3.4.0`, BUNDLE_PATH `bundle-env/.gems`, Gemfile/config are
the matching copied files, package v4b3, Ruby pnyd647 3.4.9 and Bundler4.0.7.
No claim, feature merge, default push, dispatch or deployment by implementer1.

Raw new receipts in the existing artifact root: `focused-acceptance.log/.exit`,
`final-provenance.json`, `final-guard.log/.exit`, `guard-lock-hashes`, both exact
lock snapshots and `target-prep.log/.exit`. SHA256:

```text
b1bea5bd9bb461e74f644bb5d29d00886a78dd92b6a6278553441c5114c7b4e0 focused-acceptance.log
d62c6bbfb353e74ca0f2f46ec669fc9b1ce5bc794fa64622753dc7a2a8f99b11 final-provenance.json
0e9a49518efa6e750bf15426ce0beee97fd9e3339678a33707f6021510104fa5 target-prep.log
```

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/)
