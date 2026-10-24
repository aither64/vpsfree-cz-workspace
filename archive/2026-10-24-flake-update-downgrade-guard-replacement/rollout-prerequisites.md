# Rollout prerequisites, 2026-10-24

Historical API-provider and packaging-rollout investigation. The current Git
provider contract and work order are in [design.md](design.md#current-revision-git-evidence-through-shared-mirrors)
and [the Git verification brief](git-mirror-verification.md). In particular,
the API-token prerequisite and intermediate P/Q sequence below are superseded;
their original evidence is retained here.

Architect investigation for packages C/D. The lead approved using an externally
pinned guarded confctl CI package in **all seven workflows**. Leave both
configuration repositories' deployment-tool input pins unchanged. Commands
below describe the rollout interface. The guard and initial adoptions were
reviewed/published using provider `7ba361d22a4aac044cb02abf8397800bcf5726bf`;
the final packaging successor **P** and seven consolidated pins are now being
prepared locally. The post-fix sequence below is the current verification gate.

## Inventory refresh

[inventory-refresh.json](inventory-refresh.json) contains SSH `ls-remote
--symref origin HEAD` observations from 11:46:39–11:46:46 UTC and the confctl
fetch result supplied by implementer0. All 32 canonical repositories plus the
coordination workspace were inspected at those exact remote-default commits.
Only missing objects in clankerdev, haveapi-client-php and vpsadmin-webui needed
targeted fetches; existing objects sufficed for the other changed refs. No
feature branches, worktrees or remote refs were changed by the architect.

All seven updater repository commits and workflow paths in [design.md](design.md)
remain unchanged. The refreshed clankerdev, PHP client, Linux default branch,
Rust client and WebUI trees add no publishing flake updater. Refreshed vpsadmin
still has its manual non-published environment override, not an eighth updater.
Actions enablement and external bots remain outside the static inventory.

## One CI package, including configurations

Set a repository-reviewed constant to the final published guard commit, using
the same exact revision in every consumer:

```sh
# Example placeholder; replace with the reviewed final 40-character SHA.
CONFCTL_FLAKE=github:vpsfreecz/confctl/REVIEWED_FULL_SHA#confctl
nix shell "$CONFCTL_FLAKE" -c confctl inputs update --forward-only nixpkgs
```

Do not use a mutable branch as the tool selector. A published feature SHA can
be tested before its separately approved default-branch integration. If history
is consolidated, update consumers to the final reviewed SHA; do not retain a
superseded implementation pin. No new gem release is required by this plan.

Keep this as a CI tool reference, not a new runtime input in consumer
`flake.nix`. Confctl already depends on vpsAdminOS; making vpsAdminOS depend on
confctl as a normal flake input would create the unwanted reverse dependency.
The externally invoked package has its own immutable input closure. It does
not become part of the target lock graph merely because it updates that lock.

The current provider API accepts `GITHUB_TOKEN`, falling back to `GH_TOKEN`.
The workflow should pass its token through the selected variable's environment;
Nix access-tokens and the Ruby provider are separate consumers. Keep the
existing publication permission and do not embed credentials in the tool URL.

`nix/package.nix` prepends its packaged `pkgs.nix` to PATH. Consequently the Nix
used by confctl may differ from the ambient install-nix action's binary. Record
and verify the packaged Nix version when testing the final tool artifact.

### Packaged Ruby startup boundary

Implementer1 diagnosed the IRC shell exporting `RUBYOPT=-rbundler/setup` and
repository `BUNDLE_GEMFILE`/`BUNDLE_PATH`: packaged Ruby 3.4.9 attempted to activate
the IRC Ruby 3.3 bundle before the first read-only input listing. The accepted
bounded correction is `ruby --disable=rubyopt` in the packaged entrypoint only.
Ruby documents [disabling rubyopt independently of gems](https://docs.ruby-lang.org/en/3.4/ruby/options_md.html#label--disable-3A+Disable+Features).
Confctl's entrypoint requires its own libraries directly, and its wrapper already
selects the package's gem/source paths; it does not need inherited Bundler setup.

Keep `RUBYOPT` and `BUNDLE_*` environment values for ordinary child interpreters
and repository hooks. Do not disable RubyGems or unset these variables globally.
The acceptance check must demonstrate actual read-only startup in the IRC
environment and a representative child Ruby/bundle/hook loading the caller's
bundle. Environment-string retention alone does not prove hook compatibility:
the existing wrapper also changes GEM_HOME/GEM_PATH/RUBYLIB and PATH. This is
startup-only isolation, not a guarantee about user scripts that explicitly load
Bundler. Implementer1 owns the reproduction, implementation and verification.

The architect inspected [the prototype receipt](package-b-ruby-env-diagnosis.json)
and accepted this boundary on 2026-10-24. Exact published provider
`7ba361d22a4aac044cb02abf8397800bcf5726bf` fails before listing with the observed
IRC exports; its in-memory single-flag variant returns full-SHA JSON. The
hook-style child chooses Ruby 3.3.10, loads the IRC bundle's Overcommit 0.69.0,
and confirms Bundler preload activation. Parent caller variables are preserved.
The receipt retains a preliminary failed assertion: Bundler normalizes RUBYOPT
inside the child, so post-activation string equality was the wrong assertion.
The corrected check verifies preservation before spawn and functional bundle
activation afterward. The lead subsequently authorized this bounded source
change. The first actual candidate-package regression then failed loading
`require_all` before either behavior assertion; it does not establish startup
or hook acceptance. Implementer1 traced this to `BUNDLER_SETUP` inherited from
the outer `bundle exec rspec`, which RubyGems loads independently of RUBYOPT
and which the real IRC shell did not set. The lead accepted clearing only that
key in the miniature caller fixture, preserving both real behavior cases.
Production remains the sole `--disable=rubyopt` change, without broader Bundler
sanitization or support claims. Actual candidate listing with the known IRC
exports passed; the corrected two-case artifact gate is in progress under the
lead's watcher. The prototype remains evidence for its recorded environment,
not a substitute for the final built-package regression and review.

## Post-fix verification sequence

The lead selected the following sequence on 2026-10-24. No commands in this
section were executed by the architect, and this plan does not launch work.

1. Resolve the focused built-package startup and real-hook regression. Preserve
   the failed attempt and its owned output link under
   `/tmp/flake-update-guard-b-env-2026-10-24-1`. Commit P locally only after its
   two behavior cases, affected quick checks and ordinary hooks pass.
2. Implementer0 consolidates the five ordinary consumer pins to P;
   implementer1 does the two configs. Preserve status's separate setter fix
   (currently local `521c5b627a845e2f2e7378b309b1ea8f86f3d13d`). Commit and
   quick-check all seven final sources before affected independent review.
   No follow-up feature push may trigger long CI before this gate.
3. After review, publish provider P before consumers that reference it. Bind
   new manifests to the final provider/consumer commits, review receipt and
   source/input/driver hashes. A candidate built from dirty or precommit source
   is quick evidence, not automatically the exact final P artifact.
4. Establish and retain the exact P package, wrapper, Ruby and bundled Nix paths
   and source/input/derivation/runtime-closure receipts. Run the two package
   regressions against that artifact (or explicitly prove the earlier passing
   artifact has the identical derivation, inputs and output). Probe the real
   IRC shell and both old config shells with their ordinary caller variables.
   Require full-revision JSON, config settings/channel compatibility and real
   hooks; do not clear Ruby/Bundler variables to obtain a pass.
5. Rerun all seven complete real nonpublishing patterns below. Complete the
   actual local Git race and the selected Terraform VM test after their exact
   source/package prerequisites. Collect newly triggered exact-head CI results.
   Do not dispatch unrelated tests or repeat a successful identical check.

The lead owns one fresh watcher operation at a time. The focused package gate
precedes P and consumer commits; final review precedes publication-triggered CI
and new long local checks. After review, the final package receipt precedes any
C/D command that consumes it. IRC/config environment probes precede their real
update patterns. Git race depends on P and its updated fixture, not on a real
remote write; the VM depends on the final Terraform source/baseline, not on a
new live candidate. Both run as separate serialized operations, with native
guest/process ownership and the existing unexpected-kernel-build stop rule.
No repository merge claim, deployment or lifecycle action follows from testing.

### Evidence retained and final seven-pattern acceptance

Original [review](review-report.md), [C manifest](package-c-verification-manifest.json),
[D manifest](package-d-verification-manifest.json), [CI snapshot](ci-post-review.json)
and attempts remain unchanged. The original C root is
`/tmp/flake-update-guard-2026-10-24-C-postreview-1`; each `project-<repository>/receipt.json`
binds commands and full source/input evidence to provider `7ba361d`.

| Pattern | Original result | Required final-P disposition |
| --- | --- | --- |
| HaveAPI `nixpkgs` | Pass, `d4dc3c7c6b15d3bdad51ce18f6959136dc68b23e` | Complete helper, existing flake check, hook/commit and committed-lock validation. |
| Terraform `vpsadmin` | Pass, `171e32d8bf6706748651ba33df6abb05849244fa` | Complete helper/commit/final check; separate supported `workflows` VM check. |
| vpsAdminOS `--all` | Pass, `0552cfeecf127671e21dcb72db78b7188d342107` | Complete exact workflow blocks, preserved message and final check. |
| Status nested `nixpkgs` | Incomplete, exit 255 at vendor setter | Complete fixed pattern, Go/vendor refresh, tests, package build and final check; preserve parent revisions. |
| IRC nested `nixpkgs` | Incomplete, exit 4 after packaged startup failure | Final package in real caller bundle, complete helper/hooks/subject/final check; preserve parent revisions. |
| vpsFree config channels/llm-agents | Deferred; no execution receipt | Old settings/channels runtime, complete channel/version/dependency/hook sequence and final check. |
| vpsadminos.org config channels | Deferred; no execution receipt | Old settings/channels runtime, complete channel/hook sequence and final check. |

First-three original durations were 77–116 seconds. The lead chose complete
final-P execution instead of new equivalence machinery. Keep their historical
passes; do not relabel them as final-P results. Run exact reviewed shell bodies
with only the existing explicitly recorded nonpublishing/environment omissions.
Live policy rejection 3 is a safe stopped outcome when its preservation and
no-publication assertions hold; mark later steps unexecuted. Unknown evidence,
startup failure and workflow failure are incomplete/failed verification, never
successful skips. A conditional llm-agents no-op does not prove its update arm
executed; retain the deterministic arm/rejection fixtures alongside that limit.

The full 195-example source suite and original CI remain historical/component
proof. They do not prove P's changed wrapper. Implementer1 confirmed the existing
`checks.<system>.rspec` uses `src = self` and selects the actual package through
`CONFCTL_BIN`. Run that exported check once for final P with its exact source,
input and derivation receipts; it covers the suite and the two package cases
(197 examples expected if the original 195 remain unchanged). This replaces a
duplicate source-only suite invocation, not the old result's identity. A
source-binstub run that skips the two package cases cannot satisfy this gate.
No new test framework or reuse tooling is needed, and neither commit/tree
equality nor an old green CI badge transfers an exact-artifact result to P.

The real Git fixture must reject an ordinary stale push to its **local fixture
remote**, restart from the new manual pin, reject a non-containing candidate,
accept equality and retain lock/index/HEAD as specified. Forty mocked workflow
cases do not establish this. Terraform's supported minimum VM selection remains
`./test-runner.sh test -f --jobs 1 --stop-on-failure --state-dir <owned-dir> workflows`:
all eight ordered examples, native networking, no unsupported `--network` flag
or fabricated example filter. Both checks are still unexecuted at this note.

Implementer0 will prepare `package-c-final-verification-manifest.json`,
`package-c-final-post-review.py`, `package-c-final-git-race.py` and
`package-c-final-verification-brief.md`, with new attempt root
`/tmp/flake-update-guard-2026-10-24-final-provider-1`, after final heads exist.
Implementer1 confirmed successor names `package-d-post-review-final.py`,
`package-d-verification-manifest-final.json`, `provider-runtime-probe-final.sh`
and `package-d-live-checks-final.md`, under new attempt roots matching
`/tmp/flake-update-guard-d-final-*`. These are intended paths, not already
completed artifacts. P and final consumer identities remain pending. Do not
overwrite original manifests or reuse an old attempt directory.

### Retaining artifacts between stages

The old provider output disappeared after its successful execution; its cause
is unknown. Later ENOENT is not a package negative control. Preserve that failed
attempt and avoid attributing removal to GC without evidence.

The verification owner should retain the final build through a Nix-managed,
session-owned output link, record its target and verify it before handing the
artifact to another stage. Keep the link in a retained session verification
location for the entire review/verification handoff, rather than relying solely
on a temporary directory or `--no-link` output. Preserve source/derivation roots
separately where later verification requires them: a runtime output root need
not retain every build-time source/input. Log/JSON store paths are receipts,
not GC roots. This is a precaution, not a new host GC policy or cleanup task.

If a required artifact is absent, stop its dependent stage. The owning operation
may re-realize only the recorded exact derivation/source inputs, then compare
output identities/NAR hashes before resuming; changed identities require fresh
affected verification. Keep roots and failed-attempt evidence until the lead's
retention decision. No root removal or session cleanup is authorized here.

## Exact configuration selections

Read from `vpsfree-cz-configuration` commit
`50d263d4127c05163d660fae1c4b9b887584032d` and
`vpsadminos-org-configuration` commit
`6b04b48e9c076e5525ccb7c38ce174232414f0b5`.

In vpsFree configuration, replace each flake-update invocation with the pinned
external package while retaining its channel selection and commit policy:

```sh
nix shell "$CONFCTL_FLAKE" -c confctl inputs channel update \
  --forward-only --commit --no-changelog \
  '{nixos-stable,production,staging}' nixpkgs
nix shell "$CONFCTL_FLAKE" -c confctl inputs channel update \
  --forward-only --commit --no-changelog nixos-unstable
nix shell "$CONFCTL_FLAKE" -c confctl inputs channel update \
  --forward-only --commit '{staging,os-staging}' vpsadminos
nix shell "$CONFCTL_FLAKE" -c confctl inputs channel update \
  --forward-only --commit --no-changelog llm-agents
```

The last invocation remains within the existing Codex-version-change condition.
Keep its post-update version check. A rejected/error update must stop before
the common push; a version difference cannot override ancestry policy.
The first selector resolves to `nixpkgsStable`, `nixpkgsProduction`,
`nixpkgsStaging`; the next selectors resolve respectively to `nixpkgsUnstable`,
`vpsadminosStaging` plus `vpsadminosOsStaging`, and `llm-agents`.

In vpsadminos.org configuration:

```sh
nix shell "$CONFCTL_FLAKE" -c confctl inputs channel update \
  --forward-only --commit --no-changelog nixos-stable
nix shell "$CONFCTL_FLAKE" -c confctl inputs channel update \
  --forward-only --commit os-staging
```

These resolve to `nixpkgs` and `vpsadminos`. Existing `nix develop` steps for
hooks, Ruby dependencies and other tools can keep their current behavior.
Do not accidentally run the old `confctl` binary during the update step by
wrapping it in a later `nix develop -c confctl` call.

Both old pinned tools export `confctl.settings` and `confctl.channels`:

- `af164b442100b92b8d93c0d67b315eff982e0180`,
  `nix/flake/mk-confctl-outputs.nix:481–482`.
- `7bee58a52372b95c2198ce3f2a719807a3c2c66b`,
  `nix/flake/mk-confctl-outputs.nix:508–509`.

At current master `cc40679d267165aecfa569128438bb55fe910268`, channel updates
still read this same mapping via `ConfCtl::Nix#eval_json('.#confctl.channels')`.
The Nix helper constructor reads `.#confctl.settings` before the channel query.
Implementer1's minimal fixture exposed this dependency: channels alone are
insufficient. Preserve the constructor/settings behavior and use a legacy-style
fixture with `settings = {};` and channels; changing to a stateless helper is
unnecessary for real consumers and could alter settings-derived evaluation
flags. The old-to-new channel class diff only replaces its flake-configuration
check. `moduleOptions` is used by other commands, not channel updates. This is
source-level compatibility evidence; implementer1 owns the focused fixture.
No live configuration evaluation or machine build was started by the architect.

## Ordinary projects and nested follows

HaveAPI updates `nixpkgs`; vpsAdminOS uses the guarded `--all` selection;
Terraform provider updates the real root `vpsadmin`. Preserve their commit
format/tests in their existing wrappers, with no copied ancestry algorithm.

Status and IRC bot both resolve `nixpkgs` through
`vpsadminos/nixpkgs` and then `vpsadmin/vpsadminos/nixpkgs`. The guard's resolver
must normalize that request to the fully terminal path. Keep the requested
semantic input label for their commit messages; do not advance parent
`vpsadmin` or `vpsadminos` just to update the leaf.

For revision reads, use the lead-approved additive interface
`confctl inputs ls --json nixpkgs` through the same pinned tool. It returns an
array of `{input,type,ref,rev,url}` rows, with the full resolved SHA in `rev`
(or null for revisionless sources). Require one matching row and a non-null
revision, then shorten it to the existing 11-character status or 9-character IRC
subject. Default table formatting is unchanged. Package B implements/tests this
interface; C must not copy the alias resolver into shell/Python helpers.

[selector-prototype.json](selector-prototype.json) records a local fixture with
three small Git-backed dependency flakes and this chained follows shape:

| Nix update selector | Exit | Leaf advances | Parent revisions preserved | Original lock unchanged |
| --- | --- | --- | --- | --- |
| `nixpkgs` | 0, no-match warning | No | Yes | Yes |
| `vpsadminos/nixpkgs` | 0, no-match warning | No | Yes | Yes |
| `vpsadmin/vpsadminos/nixpkgs` | 0 | Yes | Yes | Yes |

Each invocation used `--reference-lock-file` with the original snapshot and
`--output-lock-file` with a distinct candidate, from the original directory.
The fixture ran in seconds on Nix 2.34.9 without builds or network input fetches.
Its temporary Git directories were removed after preserving the evidence.

The [Nix 2.18 manual](https://nix.dev/manual/nix/2.18/command-ref/new-cli/nix3-flake-update)
already documents both lock-file flags, but its update positional argument is
a flake URL. [Nix 2.19](https://nix.dev/manual/nix/2.19/command-ref/new-cli/nix3-flake-update)
documents the positional input syntax used by confctl along with both flags.
Therefore 2.19 is a documentation-backed minimum for this command shape, while
2.34.9 is the version actually exercised here. This does not claim a complete
cross-version runtime test matrix. Unsupported versions must fail without an
in-place fallback.

## Rejected alternative: upgrading configuration tool pins

The original proposal advanced the two configuration confctl inputs as bootstrap.
The lead rejected that broader rollout in favor of the external CI tool.
Investigation found no static consumer source blocker, but the upgrade crosses
confctl's unreleased removal of software-pin commands/options, legacy APIs and
generation-format support. This is unnecessary for automated flake-update safety.

Both repositories already use flakes and `mode = "tools"` development shells;
their Gemfiles do not pin the confctl gem. The vpsFree user scripts use retained
MachineList/MachineControl/hook APIs. Searches found no removed confctl swpins,
NixFlake/NixLegacy/ConfCache references or removed confctl nixPath settings.
The one `nixPath` match is the ordinary NixOS option on aitherdev, not removed
confctl metadata. New moduleOptions exports and configuration source metadata
would nonetheless change the configuration tool/module behavior. Old local
generation records may be excluded; current/numeric generation selection and
rotation can refuse until the documented recovery procedure is followed.

Local complete Git histories prove both confctl pins are ancestors of current
master and their vpsAdminOS pins (`a169291a51b9a5d1cab3e084d3b6a1c0280a10b3`,
`6f9b2c755143197bd9c3452e1c0121b22e978c4d`) are ancestors of the tool's current
`67fcc17372d175b036706a1459a8b471bfc225e0`. Nixpkgs transitive ancestry was not
queried; a future complete pin upgrade must validate the resulting full graph.

Neither configuration has a channel mapping for `confctl`. If a separately
authorized future deployment-tool upgrade pins an exact feature SHA, its root
command is `confctl inputs set --commit --no-editor confctl <exact-sha>`, run
through the new external tool, followed by `check-update` against the saved old
lock before publication. This is a deliberate manual bootstrap, not a scheduled
unguarded update, and it would require the separate compatibility checks and
rollback preparation in confctl's `docs/swpins-to-flakes.md`. Do not execute it
as part of package D.

## Remaining dependencies

- Corrected focused package gate, local P and seven consolidated local pins,
  affected final review, then provider-first publication.
- Exact P package/exported RSpec check, real IRC and both config environments,
  seven final workflow patterns, actual Git race and supported Terraform VM
  check as specified above. Original 7ba evidence remains separate.
- Final committed-lock validation before ordinary non-force publication;
  a moved target requires regenerating from its new snapshot.
- Application verification and artifact retention remain owner/lead work;
  this architect update ran no application test, package build or live pattern.
