# Final R pin and history review

No Blocking, Important or Advisory findings in the affected R changes or final
history. This focused final gate passes for the eight exact ranges below.
The unchanged guard, scope and risk conclusions in `review-report.md` and
`review-followup-report.md` are retained. Final publication/artifact identity,
real workflow/runtime verification and CI evidence remain outstanding; this
report supplies no default-branch integration or deployment approval.

## Identity and review scope

`dev-session current` in the bound session directory returned
`2026-10-24-flake-update-downgrade-guard-replacement`. Both session environment
variables are absent; the trusted binding matches that slug and
`/home/aither/workspace/ai/vpsfree.cz`. The live same-session roster again
verified `reviewer0`, thread `01a16da6-4cc0-7fd1-8b85-0933235d3dd0`, purpose
`review`, state `ready`, saved `gpt-6.1-sol` / `xhigh`, access `read_only`.
No model/effort override, fallback, nested agent or loss of independence.

Applied the mandatory review skill's general and architecture/repetition lanes
to the fixture/native-test dependency corrections, seven mechanical pin streams
and complete final histories. Reused unchanged skill, lane and repository
guidance already read in this context. The narrow corrections introduce no new
public contract, production behavior, abstraction or compatibility boundary;
the prior scope/risk conclusions remain applicable. No serious outside-lane
issue was encountered. No source/ref mutation, build, test launch, publication,
claim, lifecycle action, merge or deployment occurred; only this new report was
written. Prior reports and failed attempts remain preserved.

## Exact reviewed ranges

Independently checked HEAD, clean Git status, base ancestry, complete ordered
series/messages, final changed-path lists and P-to-R delta paths against
`review-r/inventory.json`. Reconstructed the final diffs from the previously
reviewed final trees and independently inspected all new deltas.

| Repository / target | Base | Final head | Commits |
| --- | --- | --- | --- |
| confctl / master | `cc40679d267165aecfa569128438bb55fe910268` | `5436d3d7c36d3d5174eab3c44e3578830749d3db` | 2 |
| haveapi / master | `67fcd34ba506264a5c7ee2e8e18a88d221c6f469` | `baec8e58e11a4868a6c713e70d406709bb94c152` | 1 |
| terraform-provider-vpsadmin / master | `2a2c1055302f86f8e250f1d7e4c331d62012efe8` | `f835d63b14931712129771792039f645cf6a3305` | 1 |
| vpsadminos / staging | `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854` | `d86ea84e653e09bb1d47e21f6b219406c5462906` | 1 |
| vpsf-status / master | `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb` | `6b5e8a6089926112bfbb63a45413b886ee56e549` | 2 |
| vpsfree-irc-bot / master | `94ac4eb5a7caf0456fff7df86a44cae198463276` | `5b68640fdf0d52bbf5786c886d37d62db595e1a9` | 1 |
| vpsfree-cz-configuration / master | `50d263d4127c05163d660fae1c4b9b887584032d` | `28ce92517be0151c0bd52f7ae6e64632474888e9` | 1 |
| vpsadminos-org-configuration / master | `6b04b48e9c076e5525ccb7c38ce174232414f0b5` | `949220c108d3c87341457aa96649dd92bad333b6` | 1 |

The provider's first commit remains the exact original reviewed guard
`7ba361d22a4aac044cb02abf8397800bcf5726bf`. The second, R, retains the independent
baseline package-startup defect fix with its supporting fixture correction
folded in. Its P-to-R delta is only
`spec/confctl/cli/package_environment_spec.rb`; wrapper, guard, CLI, inputs and
docs are unchanged from P.

Status retains adoption `ebb7e6a2252f5a7f61d06a5935bb4c88a6c1964e` followed by
the independent baseline vendor-hash fix `6b5e8a6089926112bfbb63a45413b886ee56e549`.
Its native check dependency belongs with that fix's Perl-driven tests. Actual
`git range-diff` reports `589f233 = 6b5e8a6` for the sandbox-tested fix versus
the final fix. Both provider/status two-commit splits remain independently
justified: the package startup and vendor-hash bugs already existed in their
bases and are separately useful from guard/adoption. All six other repositories
retain one coherent adoption commit. Messages describe final behavior and
motivation, including status's declared check dependency.

**History conclusion:** no obsolete P/Q repair, fixup, transitional approach or
superseded pin commit remains in any complete final series. Fixture and native
test corrections are folded into their logical owners. Old published P and
failed local Q remain provenance and recovery/lease evidence, not retained
intermediate shipping commits or claimed integrated/deployed lineage.

**Repeated-update conclusion:** all seven adoption deltas are exact P-to-R SHA
substitutions in their workflow constant and applicable shared-doc URL. This
was checked mechanically against actual Git deltas, including status's adoption
commit independently of its second fix commit. Each workflow has exactly one
tool declaration selecting
`5436d3d7c36d3d5174eab3c44e3578830749d3db`; no old P/Q selection remains.
There is one consolidated final tool-selection stream per consumer, with no
redundant repin commits and no release, supported-consumer or deployed-state
boundary requiring one. Preserve the exact provider ref used by those consumers.

**Migration conclusion: no migrations.** All eight `flake.lock` files remain
unchanged from their bases. No migration/schema path or persisted-format
transition occurs in the per-commit/final inventories. The provider change is
test-only relative to P; status adds Perl to native checks, in addition to the
previously reviewed development-shell dependency. Both configurations retain
their deployment-tool declarations/locks. No migration release, deployment,
default integration or external runtime-state boundary requires preserving an
intermediate version.

## Affected code and verification conclusions

In confctl's package-environment spec, the generated real Git hook now uses an
absolute executable `env` path found on the declared PATH. `File.expand_path`
keeps the `env` dispatch name when the executable is a symlink to multicall
coreutils. Keeping the shebang's `ruby` argument preserves caller-PATH interpreter
selection. The real GitCommit/hook execution, preload/BUNDLE settings and
interpreter/gem/marker/commit assertions remain intact. This corrects the fixture
without changing the production wrapper, clearing caller variables, bypassing
the sandbox or weakening the test. No reusable abstraction or duplicate policy
was introduced.

Status's `nix/package.nix` explicitly accepts `perl` and declares
`nativeCheckInputs = [ perl ]`. Its existing `callPackage` supplies the
dependency, so the Go-driven helper tests receive Perl during buildGoModule's
checks rather than relying on a host executable. Checks stay enabled; the
application's vendor expression and runtime behavior are unchanged. The input
belongs to the package that owns the tests and does not duplicate a build rule
across consumers.

Inspected `provider-r-rspec.log`, `verification/local-R-identities.json`, the
fixture correction report and status sandbox verification/build log. The exact
immutable local R exported check passed 197 examples, zero failures and zero
pending, using the packaged CLI. Recorded identities are:

- Local source: `/nix/store/j9psyfalj0zzjj54pz18kks0saqfirvd-source`.
- Provider output: `/nix/store/jkviasl372dir0nzgp0lrrs3nwflvfbi-confctl`.
- Check derivation:
  `/nix/store/nwixlam94dpcf03wxksq358idlgdkpsy-confctl-rspec-5436d3d.drv`.
- Check output:
  `/nix/store/cxh30i73cs69sd08lxhycqzigqbwcshw-confctl-rspec-5436d3d`.

Status's retained sandbox build at `589f233a48d6da6315a6a0bbacabbc1e482c7002`
ran root/config/tools checks successfully. Its recorded eight-path realized
runtime closure contains no Perl. The final fix patch matches that tested fix;
this is not a claim that the rewritten final status source has the same output
identity. C/D report their final 40/20 mocks, lint and ordinary hooks passing.
No failed P/Q run is treated as successful proof. These narrow corrections
were directly inspected and tested under the skill's narrow-fix policy; no
further full four-lane rerun or redundant focused check is requested.

Remaining gates are the published GitHub R package/check/source/input identity
comparison before reuse of local R verification; all seven complete real
nonpublishing workflow patterns, including status and IRC/both old configuration
runtime/hooks; actual Git target-movement/fresh-baseline verification; Terraform
workflow VM coverage; fresh final publication proof and final-head CI evidence.
Original ancestry/source-policy and software-compatibility limits remain in
force. Publication and runtime preparation do not supply integration approval.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/>
