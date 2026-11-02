# Monitor exporter metadata correction

## Proven cause and boundary

Batch 6 at `8d4e03d53699d80f46030b0ee6eb213151b8ae30` passed the VM check
(227.03s), actual mx2 (72.91s), brq/int.ns1 (65.09s) and prg/int.ns1 (60.15s).
mon1 then failed evaluation (27.82s) at the infra scrape target's unconditional
`metaConfig.services.node-exporter.port`; mon2 did not run. Full logs/status and
completed native generation metadata are preserved.

The monitor's exact monitored-infra/exporter selection against baseline
`c040c14cdbacc07998700b524996a89306188d7f` yields no machine missing that
service. The successful-runtime predecessor yields only
`cz.vpsfree/containers/mx2`. Both monitor configs use the default all-machine
selection. Shared monitor/system-monitor/service-definition source is unchanged.

The actual built predecessor system
`/nix/store/cpd6wpk8rmpn144hn3r49swgalrfz3f5-nixos-system-mx2-26.05.20261026.718f670`
contains `prometheus-node-exporter.service`, enabled for multi-user.target and
listening on `0.0.0.0:9100`. Shared `modules/system/monitoring.nix` enables it
independently of the metadata declaration. Neighbor containers declare
`node-exporter = { };`; the existing shared service definition supplies port
9100. This is a missing inventory declaration on the new host, not an unrelated
baseline problem or a disabled real exporter.

Lead accepted the bounded existing-contract correction:
`services.node-exporter = { };` in the mx2 machine module only. It restores
consumer target construction without a fallback, new listener, shared module,
dependency update or fixture/policy change. No new interface is designed.

## Final source and history

Head `1e3afc478fb72b54a25a0147910463f060fee88f`, tree
`77d73449040aba400215ca81843c3d6a2173593c`. Exact source delta from the verified
predecessor is one added line in
`cluster/cz.vpsfree/containers/mx2/module.nix`; [complete comparison](monitor-metadata-diff.md).

Final three logical commits:

1. `9c6e36135192f65baed975e3b127160f068e0b0d`: host/shared policy and complete exporter metadata.
2. `a5848319ae19d1bcd348ab3837683dec71c90e01`: DNS correction.
3. `1e3afc478fb72b54a25a0147910463f060fee88f`: isolated test and documentation.

Metadata follow-up is folded into the owning host commit. DNS patch ID remains
`87bf97c34572a6e79d3635773555be5e77ca9fd1`; test patch ID remains
`e99490962c8ec5c11f1b053bbf8d5b1015381fad`. Final tree equals the complete
pre-consolidation fix tree. Explicit
`2026-11-01-mx2-nixos-migration-verified-runtime` preserves exact predecessor
8d4e03d5; original 40411d67 and reviewed-import e4c1ac0c refs also remain intact.
Earlier reviewed/build ranges are preserved, not described as literally merged.
No migrations, state paths or dependency-pin streams change.

## Quick checks and exact evaluation

Normal formatting/hooks, Nix parsing and full whitespace checks pass.
Both complete monitor toplevels now evaluate successfully. The final monitored
infra inventory has no missing exporter, and mx2's service metadata resolves
address `37.205.11.114`, port 9100. Complete exact-head evaluation is retained in
disposable `monitor-metadata-evaluation.json`; durable system identities follow.

The actual Prometheus target is `mx2.vpsfree.cz:9100`: `monitoring.target = null`
makes the consumer use `host.fqdn`. The service metadata address
`37.205.11.114` is a separate field and expected DNS address, not the literal
endpoint string emitted by this scrape configuration.

| Machine | Direct absolute-path evaluation derivation (unbuilt) | Predicted output (unbuilt) |
| --- | --- | --- |
| `cz.vpsfree/containers/brq/int.ns1` | `/nix/store/dlas4bz5rfb5mkb36gkpm3n726mngqfd-nixos-system-ns1-26.05.20261026.718f670.drv` | `/nix/store/izaxf3r9y6app0sja5na4fdv561hm10j-nixos-system-ns1-26.05.20261026.718f670` |
| `cz.vpsfree/containers/mx2` | `/nix/store/nimkfibi5516wibm49ppyy7ypj85zpzq-nixos-system-mx2-26.05.20261026.718f670.drv` | `/nix/store/2mlbw90mqi5b2bw8znp2siaik2a2p8i8-nixos-system-mx2-26.05.20261026.718f670` |
| `cz.vpsfree/containers/prg/int.mon1` | `/nix/store/m8nnz66q5ma0j4nb43bdw32c36p6icpg-nixos-system-mon1-26.05.20261026.718f670.drv` | `/nix/store/z5935ji8ipdrclx15bwf0815xz3m5ala-nixos-system-mon1-26.05.20261026.718f670` |
| `cz.vpsfree/containers/prg/int.mon2` | `/nix/store/pigd46ccn2g3an7wrvvi5y3ihnjpvx9n-nixos-system-mon2-26.05.20261026.718f670.drv` | `/nix/store/yz5sqapwzmvd4gb6nmsnd0j7n4b7db6c-nixos-system-mon2-26.05.20261026.718f670` |
| `cz.vpsfree/containers/prg/int.ns1` | `/nix/store/jz98yajjk37zc5kbw5frkx8gidg26szz-nixos-system-ns1-26.05.20261026.718f670.drv` | `/nix/store/56v1nzpm54sfh80j6wwf53kgb49dykfm-nixos-system-ns1-26.05.20261026.718f670` |

The preceding table is an unbuilt direct-evaluation prediction, not the native
batch-7 output graph. The authoritative native outputs all passed in generation
`2026-11-02--18-26-56`; captured generation-file SHA-256 values and registered
NARs are in `verification-final-systems.json`.

| Machine | Actual native deriver | Actual built output | Verified NAR |
| --- | --- | --- | --- |
| `cz.vpsfree/containers/mx2` | `/nix/store/4wz0nkyqx44hiilgv4q6a1fm8c6mrrx1-nixos-system-mx2-26.05.20261026.718f670.drv` | `/nix/store/r3y0rddwn8mkpvbdd7wyymsfzgdn3vz8-nixos-system-mx2-26.05.20261026.718f670` | `sha256-Sb7O6rudD0FtfKvrCkWECVkiOueB3EnxltrESe+IJ4s=` |
| `cz.vpsfree/containers/brq/int.ns1` | `/nix/store/1qqsyshbla0bbplmq3n4js9ngqmcdwk6-nixos-system-ns1-26.05.20261026.718f670.drv` | `/nix/store/ff6c4raplcz51h867vlap3j3dlx0qkvg-nixos-system-ns1-26.05.20261026.718f670` | `sha256-c5cTcHWfnelMHBn+w7ra9fjl6zzhK6560ba1/QywneE=` |
| `cz.vpsfree/containers/prg/int.ns1` | `/nix/store/y70la10nsgcqgiynfk09c8c07y02q0xy-nixos-system-ns1-26.05.20261026.718f670.drv` | `/nix/store/44sgccyp9sc8h2dh3glpnivh8cj2bcr4-nixos-system-ns1-26.05.20261026.718f670` | `sha256-JoAtSNXjXfzLR4+0Wvd/ERKNZgLwbh7bPHke/ATg9E8=` |
| `cz.vpsfree/containers/prg/int.mon1` | `/nix/store/6q29p6sl3gwgfl5ngp8rh6pg6v8z3lsh-nixos-system-mon1-26.05.20261026.718f670.drv` | `/nix/store/9dz8gzhvz03kva8647d2ph928i5w1v8b-nixos-system-mon1-26.05.20261026.718f670` | `sha256-t8WXDIQJToCoWkcjJwdHdNzAVTu1Ny23W1LYqtK+rVI=` |
| `cz.vpsfree/containers/prg/int.mon2` | `/nix/store/mwrnp6ci89q0n1xzw1wnpgvk65qjbc71-nixos-system-mon2-26.05.20261026.718f670.drv` | `/nix/store/vfy97r42hjmdc9wpp5qkq9pnmbq6nvl6-nixos-system-mon2-26.05.20261026.718f670` | `sha256-7qAjKVrOikr78nLQxtb3ypZKYvyH1vDjCIGCS9oxZSo=` |

The identity difference is explained by source context. The earlier expression
used `builtins.getFlake (toString ./.)`, an absolute-path flake with `rev = null`
and `dirtyRev = null`. Pinned `mk-confctl-outputs.nix` therefore sets
`configurationInfo = null`. Native confctl selects `.#confctl.build.<key>` from
the Git worktree; its self revision is final
`1e3afc478fb72b54a25a0147910463f060fee88f`, clean. The pinned configuration-info
module writes that revision/clean flag into `/etc/confctl/configuration-info.json`.
This different source/metadata construction changes the system identities.
Metadata-only replay reproduced the earlier mx2 `nimkfibi... -> 2mlbw90...`
from the absolute-path context and the actual `4wz0nky... -> r3y0rdd...` from
native `.#` with the pinned flags; no build was repeated.

All five actual systems' configuration-info files report that exact final revision,
`revisionDirty = false`, schema 1. Their generation metadata hashes match the
captured hashes, and their embedded inputs-info agrees with generation roles:
`nixpkgsStable` revision `718f670e845328e9c2cecdd832835712b2cbd065` at
`/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source`; `vpsadminosOsStaging`
revision `b45b27b4330a08d85f413999e4bf66ba4503eee1` at
`/nix/store/c24mbj25ajwn8zixx4hagr85i5kmqlmy-source`. Native Git source is
`/nix/store/3yymp5i01lf3r8ivl6jvavn4i0yircyd-source`, NAR
`sha256-8g6W7qaQFC/jUbR7/UmH23c1aCBHMBzo/7YgjzjOhZc=`. Tracked source content
matches final HEAD; full transitive lock identity below is unchanged. There is
no stale-source or role-input mismatch.

Pinned `NixFlake#build_attributes` supplies each selected machine's `toplevel`
and `autoRollback`; `NixBuildFlake` invokes `nix build --json --no-link` with
`--impure --no-write-lock-file --no-update-lock-file`. Repository settings are
`impureEval = true`, `legacyNixPath = false`, no maxJobs/cores override; no legacy
`-I` or input override is added. All five systems were built together with the
native union documented below. The actual generation/NAR table supersedes the
unbuilt direct predictions for final readiness; no additional build or check is
needed for this reconciliation.

### Reused VM evidence

The new head resolves the exact same VM derivation as the actual passed batch-6
log, independently confirmed with ordinary pure flake evaluation and the full
head evaluation:

- Derivation: `/nix/store/8pan3ddqairw3js87iaysvjqwzalxgls-vm-test-run-mx2.drv`.
- Expected output: `/nix/store/jgq1lk68xjj40j2h4wnw403pc3nylni4-vm-test-run-mx2`.
- Canonical complete derivation JSON SHA-256:
  `d1e739bbeefe29f257dbb3a5e27558bb2183fe48314d324fa59a7ee661191255`.

That immutable derivation binds the same complete input graph. Full flake graph
is unchanged: lock blob `ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86`, SHA-256
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`, recoverable
from the exact final head's `flake.lock`. The same test patch/input identities
and the preserved actual success log support reuse; source-tree equality alone
is not the basis. No VM runtime rerun is needed for this metadata successor.

Artifact retention is distinct. Lead's immediate post-batch-6 `nix path-info`
verified a registered VM output with deriver `8pan3ddqairw3js87iaysvjqwzalxgls`
and NAR hash `sha256-pQpattmS9VmO3ZIQUFn66az8GSmB4IvYhTTCFn6SUmo=`. That earlier
realized-output proof is preserved. Later read-only checks by implementer and
reviewer find the expected path absent and unregistered. The full passing
log/status, original NAR evidence and exact derivation remain; no store output
was explicitly deleted by this session and the cause of its current absence is
unknown. This is current artifact unavailability, not a new test failure or a
claim that the output still exists. No broader storage investigation or automatic
VM rerun is requested.

## Supported exact build batch

Pinned `ConfCtl::Pattern` uses `File.fnmatch?` with `File::FNM_EXTGLOB`.
Native inventory with the quoted pattern below returned exactly:

```text
cz.vpsfree/containers/brq/int.ns1
cz.vpsfree/containers/mx2
cz.vpsfree/containers/prg/int.mon1
cz.vpsfree/containers/prg/int.mon2
cz.vpsfree/containers/prg/int.ns1
```

After targeted affected-lane review, lead can run the existing native batch:

```sh
nix develop --no-write-lock-file -c confctl build --yes \
  'cz.vpsfree/containers/{mx2,brq/int.ns1,prg/int.ns1,prg/int.mon1,prg/int.mon2}'
```

Inventory proof used `confctl ls -H -o name` with that exact literal quoted
pattern. No wrapper, tool or workflow is added. This avoids five repeated dev
shell/build setup cycles while selecting only the required targets.

Targeted independent review is complete with no source findings; see
[monitor review](monitor-review.md). It accepts producer/consumer/history and
exact VM reuse with the output-availability qualification. Lead started native
batch 7 at the current exact head using the five-machine union, without rerunning
the VM. Source remains frozen; lead owns actual run/status logs and completion.

Publication used the exact verified-predecessor `8d4e03d5` lease. Fresh remote
proof reports feature `1e3afc478fb72b54a25a0147910463f060fee88f` and unchanged
master `c040c14cdbacc07998700b524996a89306188d7f`; native comparison binds this pair.
The worktree is clean and only the declared mx2 metadata file differs from the
verified predecessor. CI has no feature runs, so none needed cancellation. The
original source, reviewed-import and verified-runtime refs all remain exact.
No implementer-owned command remains running. No long check, production
operation, deployment, default integration or lifecycle action was launched by
implementer0. The standalone scratch file stays retained/accounted; no additional
project/session cleanup is performed.
