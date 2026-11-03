# Private candidate implementation checkpoint

Source package complete at084488. Independent final review accepted the
two-file staging change, five-system build set, exact VM evidence reuse and
DNS build omission. The five native systems are built and locally validated in
[staging-build-result.md](staging-build-result.md). Lead owns machine-admission
resolution and deployment. Source stays frozen; session stays active/open.

Committed head `0844881779d62d9a6a86d2bacd61d21565b33932` on fresh canonical
base `c4107822060e9e34b24a83950d618c9f28a7722b`. Clean three-commit series:
`548514a9` host, `e7cd91d8` DNS, `08448817` isolated tests/docs.
Staging changes touch only the two approved mx2 files. Normal Nixfmt and
commit-message hooks passed for the key correction and it was folded into host.
No system was realized, deployed or contacted during these checks.

## Generated quick assertions: PASS

Native Git-flake installable `.#confctl.build.m_cz_vpsfree_containers_mx2_d27c8511.toplevel`
was instantiated with `nix derivation show`, without realization. Generated
configuration-info names this exact clean final head (`revisionDirty=false`).
Root derivation `/nix/store/bpyiq4bfdmd9anf96zqyg8kqmyd3d9b0-nixos-system-mx2-26.05.20261026.718f670.drv`,
expected unbuilt output `/nix/store/4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2-nixos-system-mx2-26.05.20261026.718f670`.

Compared directly to reviewed1e native root `4wz0nkyqx44hiilgv4q6a1fm8c6mrrx1`:
main.cf, transport, Postgrey unit and Postfix unit have identical derivations
and text. All prior authorized-key lines remain, with the approved existing
aitherdev key added. Shared `aither.all` excludes that key; the initial d792
assumption that it survived via the shared administrator selection was disproved
by generated output and corrected before review/deployment. No global key change.

Generated firewall is enabled and accepts TCP22 generally. The only other TCP
exception is `iptables -A nixos-fw -p tcp -s 172.16.106.40/32 --dport 25 -j nixos-fw-accept`,
before terminal `ip46tables -A nixos-fw -j nixos-fw-log-refuse`. No general/IPv6
SMTP or exporter exception. Resolver static data contains only1.1.1.1.
Generated unit list has neither node-exporter nor rsyslog. Private metadata
is VPS27627, target172.19.9.22, v4 172.19.9.22/32, empty v6, monitoring/logging
false, no auto-update tag. Source stateVersion remains25.05.

Raw bounded evidence: `staging-generated-assertions.json`, `staging-mx2-root.json`.
Mail derivations: `3qphk9vpw8wwv88xlzccp1dg6rvbx76q-postfix-main.cf.drv`,
`pb9d1shyj2r7xsj5fkmsvj6dgkr8jzz3-postfix-transport.drv`,
`6zpa7r4wpixn4h3qr92f478mcahak3ic-unit-postgrey.service.drv`.

Monitoring selection changes affect mon1/mon2 scrapes and alerts1/alerts2
node-down inhibition. These four and mx2 form the behavioral build set.
Final-head consumer derivation identities/comparison are being reconciled;
earlier d792 predictions in staging-evaluation.json are superseded.
VM test remains the previously passed8pan derivation at d792; final-head
identity/input proof follows. No VM/source/fixture policy edits were made.

Full lock differs from reviewed1e only by the inherited upstream vpsadminServices
updates in fresh master (097226b2 to942c6eae); no own input update was made.
Selected mx2/test nixpkgsStable and vpsadminosOsStaging roles remain unchanged.

Lead owns independent review, long checks, claim admission and actual deployment.
No remote mutation, message delivery, default integration or lifecycle action.

## Final input and consumer identities

Final native roots for084488 are in `staging-final-roots.json`; all seven
instantiated successfully, without realization. The earlier d792 table is
historical and superseded. Selected config comparison to actual reviewed1e
is in `staging-consumer-comparison.json`. Both DNS servers have exactly the
same etc dependency set except the configuration-info revision file. Their
system-unit derivations, including DNS, are identical. DNS behavior is unchanged;
changed system roots reflect source revision metadata. No DNS rebuild is needed
for this staging-only delta. Both monitors change units as well as revision.

| Required native build | Derivation basename (all under /nix/store) | Expected unbuilt output basename |
| --- | --- | --- |
| mx2 | `bpyiq4bfdmd9anf96zqyg8kqmyd3d9b0-nixos-system-mx2-26.05.20261026.718f670.drv` | `4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2-nixos-system-mx2-26.05.20261026.718f670` |
| mon1 | `fajhrzprzxmdv43ssa247kmpf3397ifp-nixos-system-mon1-26.05.20261026.718f670.drv` | `8wyx524fsyyxpqid9ynrxrhrvn0kga65-nixos-system-mon1-26.05.20261026.718f670` |
| mon2 | `9agqnmwsyph2gzjikraxihyhxgallw0b-nixos-system-mon2-26.05.20261026.718f670.drv` | `085v7hqkq1nc2vc8inrynmyvxa8xk9md-nixos-system-mon2-26.05.20261026.718f670` |
| alerts1 | `r7a50vfxz53lfql0dx8wyi62fzmxbrc1-nixos-system-alerts1-26.05.20261026.718f670.drv` | `6qn8kzpgmrs3syxpqiqyvxhn8gvki9wj-nixos-system-alerts1-26.05.20261026.718f670` |
| alerts2 | `qhkmfxqgv6ag0wzfbgmgpky766v51qzg-nixos-system-alerts2-26.05.20261026.718f670.drv` | `id1cj8xkg84wscfi30jb4ajdsp18bhxy-nixos-system-alerts2-26.05.20261026.718f670` |

Exact supported five-target command (lead runs after review):

```sh
nix develop --no-write-lock-file -c confctl build 'cz.vpsfree/containers/{mx2,prg/int.mon1,prg/int.mon2,prg/int.alerts1,prg/int.alerts2}'
```

The same quoted union passed native `confctl ls`, listing exactly those five
managed NixOS targets. Pinned confctl7bee58a5 `lib/confctl/pattern.rb` uses
`File.fnmatch?(pattern, name, File::FNM_EXTGLOB)`; CLI selection uses that matcher.
No wildcard catches other systems. Builds/deployment have not run here.

The final VM check instantiates exact passed8pan3ddqairw3js87iaysvjqwzalxgls
with expectedjgq1lk68xjj40j2h4wnw403pc3nylni4. Canonical compact sorted root
derivation dictionary SHA256 remains
`d1e739bbeefe29f257dbb3a5e27558bb2183fe48314d324fa59a7ee661191255`,
identical to the historical successful receipt. This binds the same immutable
input-derivation graph. Full recursive consumed graph is4038 derivations in
`staging-vm-full-derivations.json`, canonical compact sorted JSON SHA256
`e366b1480f8650a403de926389d537a45e9652f37ea962422ba2117ba0915c96`.
Complete final flake source/input graph is in `staging-input-graph.json` and
recoverable from084488:flake.lock. Only inheritedvpsadminServices differs
from reviewed1e; that node is not consumed by this VM derivation. VM output
availability qualification in prior receipts remains: historical pass/NAR
was proven, later output absent, no cause established, no deletion or rerun here.

Selected mx2/test roles remain nixpkgsStable718f670e and
vpsadminosOsStagingb45b27b4; lockSHA256
`507e781c2fa52da5a389e6eab824efe68baa72b1727de0fc162ea0a5e6b4c098`,
blob`f6b87ab2ca27a72c3fe1bdd134129ff1e4a9f7e9`, equal freshbasec410.

## Publication

Fresh fetch still finds masterc410. Exact-lease push replaced reviewed1e
with084488; fresh SSH ls-remote confirms both refs. Comparison captured
explicitly c410..084488. GitHub branch run list is empty; no superseded
queued/running workflow exists to cancel. DNS/test stable patch IDs are
unchanged (`87bf97c34572a6e79d3635773555be5e77ca9fd1` and
`e99490962c8ec5c11f1b053bbf8d5b1015381fad`). Reviewed/source/import/runtime
refs are retained. Whole branch has no migrations and no own input update
stream. New staging edits are onlyconfig.nix+module.nix.

## Completed consumer comparison

Bounded native prior1e alert-root instantiation completed exit0 (handle53912);
no operation remains. `staging-selected-policy-comparison.json` now proves
exact generated-content equality after removing only the intended mx2 entries:

- Both monitor configs remove only `infra` target`mx2.vpsfree.cz:9100` and
  `infra-ping` target`mx2.vpsfree.cz`; their only changed unit isPrometheus.
- Both alerters share the changed config; only the mx2 container-inhibit rule
  for node5.brq.vpsfree.cz is removed. Their only changed unit isAlertmanager.
- Both DNS configurations change only the source revision receipt, with
  identical system-units and all otheretc dependencies. Their final unbuilt
  roots are hxz5f7… (prg) and r1v31w… (brq), retained in rawfinalroots.

This direct generated comparison isolates staging behavior despite the inherited
upstream vpsadminServices lock update. No refreshed extra checkout or synthetic
comparison commit was needed. No template, DNS, fixture or shared mail edits.
The earlier failed overly strict comparison added empty static_configs to jobs
that did not have that key; correcting the read-only comparison preserved absent
keys and proved exact equality. This was an evidence-script issue, no source defect.
