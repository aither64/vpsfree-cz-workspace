# C3 selected-input commit messages

Historical C3 execution receipt. Lead subsequently reported provider ff,
org69 and vpsFree07 integrated (17:55:19, 17:56:32 and 17:58:13 respectively,
as reported), with claims released and both fresh configuration master runs
passing. C4 supersedes the workflow-specific tool pins with sole flake.lock
authority; see [C4-org evidence](evidence-c4-implementer1.md). The provider's
selected-message behavior and exact accepted package proof remain applicable.
Lead later confirmed exact-ff automatic Tests43474592486 SUCCESS, closing the
historical pending CI snapshot below without any member rerun or duplicate
observation. C4's fresh hosted workflows also passed; see the successor receipt.

Owner: implementer1. Implementation is committed, quick-checked and published.
Lead accepted reviewer0's all-four-lane final review with no findings at exact
provider ff5e017 / org 69edee80 / separate B2 consumer 07a85cae, including
history, no migrations, consolidated pins and documentation. Post-review
full/packaged acceptance passed, and both prepared target windows were returned
to lead. Actual approved integration and hosted acceptance remain lead-owned.
Lead owns acceptance, integration and actual hosted dispatch. Implementer1
performed no default mutation, merge, claim or dispatch; target preparation is
recorded below.

## Exact review ranges and complete series

Both repositories use branch `2026-11-13-scheduled-workflow-fixes` and own
worktrees under `worktrees/2026-11-13-scheduled-workflow-fixes/`.

| Repository | Base at review/publication | Final feature head | Complete base-to-head series |
| --- | --- | --- | --- |
| confctl | `4c636b40b53b143fda6d9cad9332ce8b7b86bdb8` | `ff5e017780a35fb97b549db2a51b570193867c3b` | `ff5e017` inputs: scope guarded commit messages to selected inputs |
| vpsadminos-org-configuration | `8306d29d09f1939d1f92d44b5a5e241429b40c2e` | `69edee80f3ca49515f1ac562dfb3a0c5dbd960d5` | `69edee8` ci: use selected-input confctl commit messages |

Provider: five files, 172 insertions / 5 deletions. Org: one file, one insertion /
one deletion. Final diffs are directly available from these ranges and retained
as `/tmp/2026-11-13-scheduled-workflow-fixes-c3-provider.diff` and
`/tmp/2026-11-13-scheduled-workflow-fixes-c3-org.diff`. Comparison captures bind
these exact ranges. Fresh SSH remote proof matched both final feature heads and
unchanged defaults above. Worktrees and indexes are clean.

The provider is additive above already merged C2 `4c636b40`; merged C1 `8306d29`
and merged C2 history are preserved. The earlier selected-log/full-summary C3
proposal was never committed and its expectations were replaced. No obsolete
unmerged implementation remains in the final series. No migrations, persisted
formats, API/CLI flags or deployed-service changes exist.

Provider has no dependency/pin stream. Org has one consolidated CONFCTL_FLAKE
tool-pin stream: its old unmerged, unreleased, undispatched C2b range
`8306d29..6874f60516abbf7e96d8fc247036d0aa61d11cd1` is superseded by
`8306d29..69edee80`. The sole final pin selects
`github:vpsfreecz/confctl/ff5e017780a35fb97b549db2a51b570193867c3b#confctl`.
The prior intermediate 4c pin is not retained as another unmerged commit.
Old/new successor trees differ only in that provider hash: replacing ff with
4c reproduces the old workflow bytes exactly, and all other paths are identical.
`...-c3-org-successor.diff` retains this delta. This is pin-only equivalence
outside the intentional provider revision change, not equivalence of provider
behavior. Separate vpsFree consumption belongs to implementer0; no other
consumer was changed here.

## Contract, source and documentation

The amended sufficient C3 brief is in
[design.md](design.md#c3-keep-guarded-commit-messages-scoped-to-selected-inputs-sufficient-provider-brief).
The user explicitly required transitive inputs to be absent from the entire
message. The first C3 draft retaining their summaries is superseded.

- `lib/confctl/inputs/updater.rb`: the guarded callback supplies requested
  logical paths through optional internal `selected_inputs`; full original
  changes still flow through guard, callback and result. Manual flow keeps nil.
- `lib/confctl/inputs/commit_message.rb`: select a new message-only changes
  array before existing title, body and group construction. Original changes
  are not mutated. Only selected paths can contribute names, hashes, summaries
  or logs; no repository-name heuristics or selection widening.
- Original nil/empty changes still raise `no changes`. Default/nil selection
  retains existing manual/Setter behavior. For a nonempty guarded request with
  only descendant changes, emit exactly `inputs: update <sorted requested names>`
  with no body, revision claim, arrow or Git-log query. It still commits the
  accepted full-graph lock. No empty-request mode or CLI option was added.
- Selected aliases use their requested logical names; unselected aliases and
  terminal paths are excluded. Existing selected-source/range deduplication and
  downgrade direction remain. `--no-changelog` suppresses all message log queries.
- Existing `commit_message_spec.rb` and `guarded_update_spec.rb` contain the
  bounded regressions. Guard, graph, Setter, CLI and C2 tempfile transport are
  untouched; Git diff against 4c confirms those implementation files unchanged.
- `docs/flake-inputs.md`: eight-line reference/how-to clarification for operators
  in the existing authoritative input guide. Lead directly applied the writing
  pass after revised facts settled; owner inspected the factual diff against
  source and tests before commit. README already links this guide, so no new
  entry point, documentation subsystem or individual rollout report was added.
- Org `.github/workflows/daily-update.yml`: only the immutable tool pin changes.
  All command flags, actions, guards, cron/dispatch, permissions, push/auth and
  configuration lock remain unchanged. This chooses the CLI tool, not a channel.

Full graph ancestry, snapshot/race checks, callback timing, installation,
returned change records and final check-update remain unchanged. Excluding a
message entry never excludes an ancestry comparison or rejection. Provider must
be integrated before consumers and actual dispatch; lead owns that ordering.
Reverting C3 restores verbose messages while merged C2 still transports large
messages safely. No coordinated service rollout or state migration is required.
Individual review/acceptance receipts belong here and in lead-owned state.

## Quick checks and normal hooks

The declared confctl Nix shell was entered with
`nix develop /tmp/2026-11-13-scheduled-workflow-fixes-c2-shell -c ...`, reusing
profile `/nix/store/vha0zqm64yp7pijfx4jf7b82dzk3lkpi-nix-shell-env`, Ruby 3.4.9,
locked Bundler 2.5.7. Baseline RubyGems constant warnings remain non-failing.

| Check | Result / evidence |
| --- | --- |
| Revised `bundle exec rspec spec/inputs/commit_message_spec.rb spec/inputs/guarded_update_spec.rb` | 41 examples, 0 failures, 3.84 seconds |
| Targeted RuboCop on both source and both spec files | Four files, no offenses |
| `ruby -c` on all four changed Ruby files | All syntax OK |
| Existing guard/lock-graph and CLI manual/forward-only/Setter scope | Passing pre-amendment 107-example batch retained for unchanged scope; message-selection assertions replaced and rerun above |
| All 50 tracked Nix files, `nixfmt --check` | Passed; no Nix file changed afterward |
| Actual provider commit hooks | Nixfmt, RuboCop and commit-msg hooks passed |
| Org YAML / inverse pin byte and structural comparison | Passed against merged8306; no other delta |
| Org action refs and all five extracted Bash bodies | Unchanged official refs; all `bash -n` passed |
| Actual org amend hooks | Nixfmt and commit-msg hooks passed |
| Org old/new successor comparison | Only immutable provider hash changed; remainder byte-identical |
| Final diff whitespace and worktree/index state | Clean |

No action ref or shell logic changed; unchanged action references were verified
structurally without bootstrapping an undeclared actionlint environment for a
pin-only delta. The existing official action validation remains unchanged.

Final revised batch exit 0 is retained at
`/tmp/2026-11-13-scheduled-workflow-fixes-c3-revised-quick-final.{log,exit}`;
org checks at `...-c3-org-quick.{log,exit}`. Commit/publish logs use corresponding
`...-c3-commit.log`, `...-c3-publish.log`, `...-c3-org-commit.log` and
`...-c3-org-publish.log` names.

One initial revised alias test expected the pre-filter group's URL spelling;
filtering correctly made the selected alias (with trailing slash) the reference.
Corrected only that fixture expectation and reran the four-second affected batch.
The superseded draft had one regex style correction; it is no longer part of
final behavior. Commit-msg TextWidth produced advisories for body lines over 72;
all messages remain within the required 80 columns, and hooks passed normally.

First provider push from the ambient shell stopped at Overcommit's configuration
signature check. Fresh remote proof showed both refs still at 4c, with no partial
publication. Re-read the unchanged declared configuration, refreshed its normal
signature in the repository Nix shell, and published the same exact commit using
bundled Git. No bypass or source/hash change. Org published with the exact old
feature-head lease at 687 after fresh fetch; no stale-default rebase was needed.
No superseded org feature runs existed to cancel (branch run list empty).

## Review and acceptance boundary

Final review accepted by lead as recorded above. Implementation owner retained
for findings and post-review full checks/packaged proof; no long local acceptance
was launched before review. Prior C2 package proof remains
bound to its exact source/inputs and is not represented as C3 acceptance.

Pre-acceptance read-only automatic CI snapshot at exact ff (no dispatch/wait):
[RSpec43474592588](https://github.com/vpsfreecz/confctl/actions/runs/43474592588)
and [RuboCop43474592622](https://github.com/vpsfreecz/confctl/actions/runs/43474592622)
passed; [Tests43474592486](https://github.com/vpsfreecz/confctl/actions/runs/43474592486)
was in progress. Required full local RSpec/RuboCop and immutable packaged mixed
selection/full-graph rejection proof subsequently passed below.
Actual named-workflow message inspection remains lead-owned after integration.
One final delivery-time read of exact Tests run 43474592486 still showed job
132054976570 in its Run tests step with no terminal conclusion. No CI wait,
duplicate run, cancellation or rerun was started; this remains an explicit CI
gap separate from the passing scoped full/package acceptance.

Post-review operation: fresh native utility `/root/c3_postreview_acceptance`,
Luna/low, ran the exact `nix develop` C2 profile followed by
`bash /tmp/2026-11-13-scheduled-workflow-fixes-c3-postreview.70mim6so/acceptance.sh`.
Logs, exit marker, immutable package/input receipts and the disposable adaptation
of existing `package_environment_spec.rb` are in that artifact root. The fixture
invokes actual packaged CLI update/check-update, real tiny Git ancestry/mirrors,
selected-only messages and live private tempfile/caller Bundler hook, then
rejects an excluded descendant rewind while preserving lock/index/HEAD. Only
candidate generation is controlled; no fake ancestry or message result.
Installed utility package `0s5dljmmfngj7ia2r9lfkxwydnfiz6b6-dev-workspace-0.2.0`,
catalog `f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`,
schema 6 and full-access native utility TOML were reread before launch. Native
delegation was used for this member-owned operation; parent stayed active.
Utility shell session 45726 ended with exit 0 in about 126 seconds; native final
confirmed no surviving operation cells/sessions or effects. No retries, source
changes, dependency regeneration or local kernel build. Terminal PASS was sent
to lead before target work and extended receipt updates.

| Post-review check | Result |
| --- | --- |
| Full RSpec with immutable `CONFCTL_BIN` | 225 examples, 0 failures |
| Full RuboCop | 110 files, no offenses |
| One adapted packaged caller example | 1 example, 0 failures |
| Real Git ancestry in mixed candidate | OS and Nixpkgs both ahead |
| Generated message and log query | Only selected OS title/summary/log; no descendant names/hashes/log |
| Actual caller hook | Caller Ruby/Bundler/preload preserved; live private message bytes match generated message; only flake.lock committed; tempfile removed |
| Exact final committed check-update | Both full-graph change records preserved and accepted |
| Excluded Nixpkgs rewind | Actual ancestry behind, CLI exit 3; lock/index/HEAD byte-exact and no commit hook/log query |
| Final reviewed source | Clean, immutable ff unchanged |

The disposable fixture uses the existing caller environment scaffold and tiny
real local Git histories. Ordinary Git URL configuration maps fixture GitHub
URLs to those local histories in an isolated cache/config. Candidate generation
alone is controlled; real guard, mirrors, messages, Git commit and caller hooks
execute. There is no live Nix dependency regeneration in this proof. Temporary
fixture repositories are removed by the existing scaffold; assertions, exact
fixture source and logs remain in the artifact root. Real hosted component
messages still require the lead's fresh integrated-master run inspection.

## Immutable package and full flake input receipt

- Source: `ff5e017780a35fb97b549db2a51b570193867c3b`,
  `/nix/store/1qw3c7q3r67drrv0z4vmac9g70pvxyf5-source`,
  NAR `sha256-Y7vwZfDEpElVUxEyDdpwHC8/1IapvkMz3/0AFr7U+yw=`.
- Package: `/nix/store/v4b3r3r8102kyf92lidwvk62plpjs13j-confctl`,
  derivation `/nix/store/6nq336f5rfs8jgd38bsmdgpdhy5rw0rd-confctl.drv`,
  NAR `sha256-SEm2XycyQviAqJXW79ovMIrUM6wwp3LfBCTTpPWEXQ0=` (1248 bytes).
  Indirect GC root `accepted-package` in the artifact directory retains its
  existing closure without another build.
- Package direct references: the source above;
  `/nix/store/v9yi65x2qnizjm9mnq0xk3f3cm4d1y4d-confctl-deps`;
  `/nix/store/pnyd647xzsszp5r6vicpsl7q9fsz5xyk-ruby-3.4.9`;
  `/nix/store/j7fnzcrbbxc1r2b3b9fhqkha6hqb0jh1-git-2.54.0`;
  `/nix/store/azi9n31ia037jml4ibi4nfwz1v4hmrj6-nix-2.34.8`;
  `/nix/store/1sr8rmx4v0v994lkbzhwc1f0qr1gxxs9-bash-5.3p9`;
  `/nix/store/4lh63ihbvf9jl83pgykm70avydcrxw58-openssh-10.4p1`.
- Actual caller shell: Ruby 3.4.9, Bundler 2.5.7, Git 2.54.0,
  invocation Nix 2.34.9; packaged Nix remains 2.34.8. The live hook assertion
  matched caller `RbConfig.ruby`, fixture gem and inherited preload/bundle.
  Source bytes for Updater, CommitMessage and C2 GitCommit were compared directly
  between reviewed Git ff and the immutable source store path.

Complete lock graph: root plus eight locked nodes. Provider lockfiles were not
edited. Each row records the exact source revision and NAR hash:

| Node | GitHub source | Revision | NAR hash |
| --- | --- | --- | --- |
| home-manager | nix-community/home-manager | `c47b2cc64a629f8e075de52e4742de688f930dc6` | `sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=` |
| impermanence | nix-community/impermanence | `7b1d382faf603b6d264f58627330f9faa5cba149` | `sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=` |
| netlinkrb | vpsfreecz/netlinkrb | `d9de53d843d2586ffa5b7b404887fa801c697ddf` | `sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=` |
| nixpkgs | nixos/nixpkgs | `e4bae1bd10c9c57b2cf517953ab70060a828ee6f` | `sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=` |
| nixpkgsUnstable | NixOS/nixpkgs | `f13ff45afd1bb73e640eaa08a7066dbed07e3238` | `sha256-zDSUbpoeo/9ZmD2+wXnzxoo1+uhL8vxc0b8yuYMKYq0=` |
| nixpkgs_2 | NixOS/nixpkgs | `8b8c811c7c2541c30382c5de7ed26be055569c60` | `sha256-CiOTEjmwAmG2AWnaIno9YaCJJmpca2FXPhMAsnrolCg=` |
| ruby-lxc | vpsfreecz/ruby-lxc | `004bf35eb90d41ba60b347b5b1e73d868a4f95d9` | `sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=` |
| vpsadminos | vpsfreecz/vpsadminos | `67fcc17372d175b036706a1459a8b471bfc225e0` | `sha256-HOL3ACMUyRFhA4Cd2zk5qhnUf0zaEifHsQv86hwHgSc=` |

Complete edges (arrays are root-relative follows paths):

```json
{
  "root": {"nixpkgs": ["vpsadminos", "nixpkgs"], "vpsadminos": "vpsadminos"},
  "vpsadminos": {"impermanence": "impermanence", "netlinkrb": "netlinkrb", "nixpkgs": "nixpkgs_2", "nixpkgsUnstable": "nixpkgsUnstable", "ruby-lxc": "ruby-lxc"},
  "impermanence": {"home-manager": "home-manager", "nixpkgs": "nixpkgs"},
  "home-manager": {"nixpkgs": ["vpsadminos", "impermanence", "nixpkgs"]}
}
```

Raw receipts in artifact root: `flake-metadata.json`,
`package-derivation.json`, `package-info.json`, `package-references`,
`source-flake.lock`, `acceptance.log/.exit`, full RSpec/RuboCop logs and
`packaged-proof.log`. SHA256:

```text
36474d7bbf7c32bfdbec54c4b273b625bbe933d31cdeb259cb00b1ed4fc03c34 flake-metadata.json
a2a7d4f4c960d2f1f1410c35a9b5bca340d1086d373b35f869493588877dc2f2 package-derivation.json
3e812debafa444d6815390c41cc0234fc999601ec0622fbf3502911380bf541c package-info.json
17af06ae76afeba640d695a8e974d76be742e795977d026771c178c523a4eaba source-flake.lock
d3c27339ca613de6b2000af88e934b540587184bd26f8ff8a9e0cd071339047c acceptance.sh
4277bbe9315a040bdd4914eaf3a68c837ae33ea91bff94678f2f078d241b43af packaged_selection_spec.rb
fe3f930d4b9f7967a927e6d3798eeecb8956f574116bf115a3129a4031af825e acceptance.log
```

## Sequential target preparation and handoff

After acceptance PASS only, prepared existing detached targets sequentially;
no source edits, merge, default push, claim or workflow dispatch. The cached
bundle/hook preparation was a known quick operation, completed inline in 16
seconds with exit 0. `target-prep.log/.exit` and `prepare-{one-target,targets}.sh`
are in the same artifact root. No command or session remains active.

| Target under own merge-targets directory | Detached clean HEAD / fresh remote master | Fresh feature / ancestry | Normal environment |
| --- | --- | --- | --- |
| confctl | `4c636b40b53b143fda6d9cad9332ce8b7b86bdb8` | `ff5e017780a35fb97b549db2a51b570193867c3b`, FF ancestor passes | C2 profile, Ruby 3.4.9 |
| vpsadminos-org-configuration | `8306d29d09f1939d1f92d44b5a5e241429b40c2e` | `69edee80f3ca49515f1ac562dfb3a0c5dbd960d5`, FF ancestor passes | C1 profile, Ruby 3.3.10 |

Exact root:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/merge-targets/`.
Both bundle checks passed; normal Overcommit install/config signing/plugin
signing succeeded and pre-commit/commit-msg hooks are executable under their
canonical bare repo hook paths. Existing `.gems/ruby` aliases still resolve to
the same-session feature caches; private `.bin` directories were preserved.
No broad reset/clean/stash or target-head change. Fresh remote/default and feature
snapshots were rechecked after hook preparation and matched the table. Both
exclusive windows were explicitly returned to lead in the raw readiness report;
implementer1 performs no further target operations without a new window.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/)
