# Final R provider and configuration publication

After [focused final review](review-r-report.md) passed, the provider was
published first, followed by both configuration adoptions. Fresh SSH probes
before each push matched the reviewed default base and exact prior published
P feature head. All pushes ran in their ordinary declared Nix development
shells with installed hooks and explicit exact `--force-with-lease` values.
No source, default ref or rebase changed.

| Repository | Published reviewed R head | Exact prior P lease |
| --- | --- | --- |
| confctl | `5436d3d7c36d3d5174eab3c44e3578830749d3db` | `bdaed19e901237e05bd0a779f368e76cb311143f` |
| vpsfree-cz-configuration | `28ce92517be0151c0bd52f7ae6e64632474888e9` | `7b0609cf41fc9fe54b6d09129246ff100fb4197a` |
| vpsadminos-org-configuration | `949220c108d3c87341457aa96649dd92bad333b6` | `4352f16fb967e3b9da829972c9799157badd0494` |

Post-push SSH observations confirmed each exact feature head and unchanged
default branch. All three worktrees remain clean at the reviewed heads.
The provider proof was delivered to lead/C before consumer publication.
Full refs, times, review hash, trees, order and log hashes are in
[package-r-publication.json](package-r-publication.json). Logs:
[provider](package-r-push-confctl.log), [vpsFree](package-r-push-vpsfree.log),
[org](package-r-push-org.log). Earlier P/Q source reports, scripts, attempts and
publication receipts remain unchanged.

## Bounded CI snapshot

The post-publication snapshot found these exact-R confctl runs:

- [RSpec 40102634368](https://github.com/vpsfreecz/confctl/actions/runs/40102634368): success.
- [RuboCop 40102634418](https://github.com/vpsfreecz/confctl/actions/runs/40102634418): success.
- [Tests 40102634372](https://github.com/vpsfreecz/confctl/actions/runs/40102634372): in progress at observation.

Neither configuration feature push had a listed exact-head run. There were no
superseded queued/in-progress same-branch runs in these three repositories;
zero cancellations were requested. Current/completed/other-branch runs were
untouched. No CI wait, rerun or dispatch occurred. Exact snapshots:
[summary](package-r-ci-summary.json), [provider](package-r-ci-confctl.json),
[vpsFree](package-r-ci-vpsfree-cz-configuration.json),
[org](package-r-ci-vpsadminos-org-configuration.json).

Actual prior-P inspection found all three P workflows successful, including
Tests 40099730892. It did not reveal a failed P CI log to diagnose; the empty
failed-only log and exact-source observations are retained in
[package-b-p-ci-observation.md](package-b-p-ci-observation.md). No cause was
inferred from a new green run or the separate local sandbox failure.

## Remaining root-owned verification

The exact local immutable R exported check passed all 197 examples with zero
failures or pending cases. Before reuse, compare published GitHub R with
[verification/local-R-identities.json](verification/local-R-identities.json):
source NAR/path, complete archived input graph, package output/derivation and
exported-check output/recursive derivations. This comparison has not been run by
the implementer. Root owns the serialized startup/identity operation; mismatch
requires diagnosis before reuse or downstream runs.

For reference, these are identity-only Nix commands for that assigned watcher,
with output captured under its owned root and the existing token-safe logging:

```sh
R_SOURCE=github:vpsfreecz/confctl/5436d3d7c36d3d5174eab3c44e3578830749d3db
nix flake metadata --json --no-write-lock-file "$R_SOURCE"
nix flake archive --json --no-write-lock-file "$R_SOURCE"
nix derivation show --recursive "$R_SOURCE#confctl"
nix derivation show --recursive "$R_SOURCE#checks.x86_64-linux.rspec"
nix eval --raw "$R_SOURCE#confctl.outPath"
nix eval --raw "$R_SOURCE#checks.x86_64-linux.rspec.outPath"
```

No duplicate suite/build/probe was launched here. Final D runtime/project
operations remain prepared in [package-d-live-checks-r.md](package-d-live-checks-r.md),
using the C R startup receipt and independent owned D root. Actual old config/IRC
environments/hooks, all seven real nonpublishing patterns, Git race, Terraform VM
and final CI completion remain separate gates. No integration, deployment,
claim or lifecycle action occurred or is authorized.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
