# Affected independent final review

No Blocking, Important or Advisory findings in the completed follow-up changes.
This affected final review gate passes for the exact eight ranges below. The
prior unchanged guard review remains valid; package/runtime, integration-test
and final CI gates remain outstanding. This report does not grant default-branch
integration or deployment approval.

## Identity and review boundary

Verified `dev-session current` in the bound session directory returned
`2026-10-24-flake-update-downgrade-guard-replacement`. Both session environment
variables are absent; the trusted thread binding identifies the same exact slug
and `/home/aither/workspace/ai/vpsfree.cz` workspace. The live same-session roster
still identifies `reviewer0`, thread `01a16da6-4cc0-7fd1-8b85-0933235d3dd0`,
purpose `review`, state `ready`, saved model `gpt-6.1-sol`, effort `xhigh`, access
`read_only`. No overrides, fallback or nested agents were used. I remain
independent of all implementation changes.

Reread mandatory-change-review and all four lane references. Applied general,
architecture/repetition, scope/proportionality and risk/compatibility to the
new package boundary, status correction and consumer repins. Risk remains
**High** because the packaged CLI environment and automated publication are
shared contracts. Reused unchanged workspace/local guidance and the frozen
[original review](review-report.md); repository AGENTS files are unchanged.
No source/ref mutation, build, long test, publication, lifecycle, integration or
deployment action was performed. Only this new report was written; the original
report is preserved.

## Exact ranges and complete history

Independently checked actual Git HEADs, clean status, base ancestry, complete
ordered commit lists/messages, full changed-path lists and old-reviewed-to-final
delta paths against `review-followup/inventory.json`. The final diffs consist
of the original reviewed changes plus the inspected deltas. Six consumer deltas
are exact SHA substitutions only. Status's adoption commit also changes only
that selected SHA relative to its reviewed adoption; its independent fix is the
only additional substantive delta. Provider guard code, tests and input locks
are unchanged from the original review.

| Repository / target | Base | Final head | Commits |
| --- | --- | --- | --- |
| confctl / master | `cc40679d267165aecfa569128438bb55fe910268` | `bdaed19e901237e05bd0a779f368e76cb311143f` | 2 |
| haveapi / master | `67fcd34ba506264a5c7ee2e8e18a88d221c6f469` | `aebbc9930c39a4df6fad01fefed8254921635b15` | 1 |
| terraform-provider-vpsadmin / master | `2a2c1055302f86f8e250f1d7e4c331d62012efe8` | `58a3d083381ccadf4075e8eeffe2c169741be691` | 1 |
| vpsadminos / staging | `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854` | `afc2eb385096e361b883ff66afe0bc7eb74eb698` | 1 |
| vpsf-status / master | `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb` | `c8869b8f274dd840539a94da30d19d355cd623c1` | 2 |
| vpsfree-irc-bot / master | `94ac4eb5a7caf0456fff7df86a44cae198463276` | `fb5d72fb44176ebee217370f761762afd275ab54` | 1 |
| vpsfree-cz-configuration / master | `50d263d4127c05163d660fae1c4b9b887584032d` | `7b0609cf41fc9fe54b6d09129246ff100fb4197a` | 1 |
| vpsadminos-org-configuration / master | `6b04b48e9c076e5525ccb7c38ce174232414f0b5` | `4352f16fb967e3b9da829972c9799157badd0494` | 1 |

The two-commit splits are justified independently of the packet's proposal:

- Confctl retains reviewed guard commit `7ba361d22a4aac044cb02abf8397800bcf5726bf`
  followed by package fix `bdaed19e901237e05bd0a779f368e76cb311143f`. The original
  base's package wrapper already inherited Ruby preloads. The startup correction
  is independently useful outside guarded updates, and its wrapper/spec/docs
  form one coherent fix. It is not a repair of guard logic or a superseded
  guard design.
- Status retains adoption `13830fc82bb2fe3ed7a212832d578e3a61c1d1cb` followed by
  `c8869b8f274dd840539a94da30d19d355cd623c1`. The original base already used the
  defective two Perl substitutions, and the actual conditional package
  expression is unchanged. Fixing that pre-existing updater works independently
  of ancestry enforcement. Its caller/helper/tests and declared Perl dependency
  belong together. I reconstructed the old/new fix ranges; `git range-diff`
  reports `521c5b6 = c8869b8`, supporting the owner's patch-preservation claim.

**Whole-branch conclusion:** no obsolete approaches, transitional compatibility
paths, fixup/WIP residue or redundant repair commits remain in the eight final
series. The two independent baseline fixes warrant separate commits. All
remaining repositories contain one coherent adoption commit. Commit messages
describe the resulting behavior and reasons.

**Repeated pins:** all seven workflow constants and applicable shared-doc URLs
select the one final provider source
`bdaed19e901237e05bd0a779f368e76cb311143f` (P). The previous `7ba361d` selections
were folded into their owning adoption commits rather than retained as repin
commits. There is no repeated update stream left to consolidate in any final
series. Prior source/adoption revisions are provenance only; no released,
deployed or supported consumer boundary requires an intermediate pin. Preserve
the exact final provider feature ref needed by these consumers.

**Migration conclusion: no migrations.** Per-commit inventories and final diffs
contain no schema or persisted-format transition. Every final `flake.lock` is
byte-identical to its base. All `flake.nix` files are unchanged except status's
addition of Perl to its development shell; no runtime input or deployment-tool
pin changes. No intermediate migration was merged, released, deployed or
externally consumed. Local successor publication is correctly distinguished
from historical remote-head evidence; this review makes no remote-publication
or integration claim.

## Affected lane conclusions

**Package fix, P:** `nix/package.nix:31` passes `--disable=rubyopt` only to the
absolute packaged Ruby interpreter. It does not disable RubyGems or remove the
caller's Ruby/Bundler variables from the environment. Existing packaged gem,
source and runtime PATH selections remain intact. Child commands can still
select the caller Ruby and activate their own bundle; explicit Bundler loading
remains governed by that bundle. This narrow boundary matches the demonstrated
IRC caller-preload failure without introducing a general environment sanitizer
or consumer-specific startup branch. The
[Ruby 3.4 option reference](https://docs.ruby-lang.org/en/3.4/ruby/options_md.html#label---disable-3A+Disable+Features)
documents `rubyopt` separately from `gems`.

`spec/confctl/cli/package_environment_spec.rb` meaningfully exercises the actual
package through `CONFCTL_BIN`: valid JSON without caller-preload activation,
then a real Git pre-commit hook through confctl's GitCommit path, asserting the
caller interpreter, path gem, bundle settings and preload markers. Clearing
only the outer RSpec launcher's `BUNDLER_SETUP` in the simulated caller is
explained and does not change production. The actual IRC shell exports used in
the diagnosis do not contain that variable. These tests establish the chosen
RUBYOPT boundary; they do not claim isolation from explicit RubyGems/Bundler
activation. Guide/manual changes describe this boundary in their owning docs.

**Status fix, `c8869b8`:** the two workflow calls pass a quoted SRI value as an
argument to `tools/set-vendor-hash.pl`, so `/` and `+` cannot become Perl
program syntax. The helper validates the supplied shape, accepts the flat and
current conditional default assignment, retains the local-source override and
checks the match count before opening the file for writing. Its bounded
supported layouts fit this repository's actual package. It does not attempt a
general Nix parser or source-rewriting framework. Both callers share the same
setter, preventing the fake/default replacement rules from drifting.

`tools/vendor_hash_test.go` covers real/fake transitions, base64 punctuation,
the actual current package, unchanged override text and no-write failures for
invalid input, unsupported expressions and duplicate supported assignments.
The normal Go suite discovers these tests. Declaring Perl in the development
shell is necessary for that repository-owned test/helper dependency and does
not add an application runtime dependency. No API, metric, translation or
production service behavior changes.

**Consumer repins:** inspected actual Git deltas, not only manifests. The six
other consumers change only old-to-P SHA text; status's adoption delta does the
same. The original input selections, complete-graph guard, token passing,
committed-HEAD final check, hooks/check stages and ordinary non-force push
semantics are retained. No duplicated guard, new fallback or deployment-tool
upgrade was added. Ownership, proportionality and risk conclusions from the
original review remain applicable to unchanged implementation.

## Evidence assessed and outstanding verification

Inspected the current environment-fix report, both new specs/helpers, status
failure/fix evidence, final branch inventories, mock results and focused quick
logs. The actual candidate-package log reports two package regressions passing
with zero failures; source hashes are rechecked. The candidate artifact is
`/nix/store/5zxmilj7i4783didd7qb63i5g5wyb6ih-confctl` with bundled Nix 2.34.8,
as recorded in its receipt. This precommit candidate proof is deliberately
separate from the final P artifact. The invalid missing-old-output negative
control and earlier failed candidate test remain failures, not successful
verification or proof of old behavior.

Status's regression/full-Go checks passed on the preserved fix patch; the
final repins passed 40 C and 20 D mocked workflow scenarios, lints and ordinary
hooks according to their linked evidence. These are appropriate prerequisites
for this review. I launched no replacement suite/build and do not extrapolate
mock or precommit results into final package/runtime success.

Before readiness, the lead still needs to establish:

- The exact final published P artifact, its source/input/derivation identity,
  bundled Nix and complete 197-example provider suite, with package cases active.
- All seven real nonpublishing workflow patterns at these final heads/P,
  including status's actual vendor-hash update and the IRC/both old configuration
  shell and hook environments. Preserve supported caller settings; changing
  them merely to make the probe pass would test a different boundary.
- Actual Git target-movement/fresh-baseline behavior, the supported Terraform
  workflow VM check and exact-final-head CI evidence. A mock push failure is
  not the real Git race proof.
- Fresh publication/ref proof in the authorized provider-before-consumer order.
  Reuse verification only with exact source/input/derivation evidence; the
  unchanged guard or preserved status patch alone does not identify a new
  package or composed artifact.

The documented ancestry, strict source/path transition, upstream-revert and
software-compatibility limits are unchanged. No coordinated machine update is
required. No remediation or further affected-lane rerun is requested by this
report; newly demonstrated defects remain subject to the skill's narrow-fix
and affected-review rules.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/>
