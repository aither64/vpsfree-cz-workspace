# Prepared syslog exporter replacement

Prepared locally; **not deployed**. The user explicitly requires approval before
deployment. No dry-activation, candidate copy to production, machine claim,
default-branch integration or session lifecycle action has occurred.

## Exact candidate and recovery identity

| Item | Identity |
| --- | --- |
| Configuration repository / target | git@github.com:vpsfreecz/vpsfree-cz-configuration.git / master |
| Exporter repository / target | git@github.com:vpsfreecz/syslog-exporter.git / master |
| Configured machine / SSH alias | cz.vpsfree/containers/prg/int.log / log.int.prg.vpsfree.cz |
| Prepared exporter head | faf06c1185ad2f6d39286d2e33896a6455b7bea6 |
| Prepared configuration head | a839ccf7e7ff07ac616ad7994af33f07975bd1b5 |
| Observed clean production configuration | 959e1d54cabc7ac5530dac6179acacb077a57754 |
| Local confctl candidate build NAME | 2026-11-11--00-46-58 |
| New package | /nix/store/3hk34i2k760dirn1xrarxqsrwrcryaj5-syslog-exporter-0.14.0 |
| New system | /nix/store/nw3d0j9hb1mrwf7hd0daxm6gk1vcfabc-nixos-system-log-26.05.20261026.718f670 |
| Retained prior system | /nix/store/kgrfplplhrhhj4idvzx172lqh4hiyimq-nixos-system-log-26.05.20261026.718f670 |
| Observed prior profile | /nix/var/nix/profiles/system → system-143-link |
| Prior exporter package | /nix/store/w7g32wplgls6x79608h6nij02a4vvq9y-syslog-exporter |

The old numeric profile143 is **not** a confctl local build NAME. Recovery uses
the retained exact old system/package; do not invent a matching historical NAME.
The new system has not been made current on production.

Complete source/input/derivation/closure graphs, source retention reconstruction,
normal Git-versus-path evaluation proof, artifact NAR identities and local root
locations are in [C2 evidence](c2-evidence.md) and its linked raw receipts.
Keep durable identities in that Markdown when pruning disposable raw output.

- Package NAR: `sha256-Y+H0duMpY5PGDsNk9DYyO7YJXG3u8u4kwV9Y9X0md28=`.
- New system NAR: `sha256-KknCgMIpbg2EJqGIijH1rFdiAWjtdt33n+Saj2HLemU=`.
- Prior system NAR: `sha256-bWKb/DaGJe+JB1a1VYYtML3ejYssKpSyRRi1HudJxZU=`.
- Normal confctl system derivation:
  `/nix/store/nc86mbf1kmkwakxy1lcg87n60bxw8b1b-nixos-system-log-26.05.20261026.718f670.drv`.

The initial historical path evaluation omitted Git provenance and produced
another toplevel. Final preparation uses normal confctl Git-flake evaluation,
binding clean a839 source metadata. Original source/input and evaluation lineage
remain in C2 evidence. Exact final package/host receipts are
`c2-artifacts/i2-build-verification-summary.json`.

## Verification and compatibility

- [Review record](review-packet.md) binds the original full exporter and consumer
  reviews, direct I1/A1 fixes, current [affected I2 review](i2-final-review.md)
  with no findings, and independently reconstructed mechanical consumer refresh.
- Exact-head exporter CI42921690945 attempt1 passed; rustfmt, Clippy and19tests
  passed through the active hook. All19tests also passed in the Nix release
  package build159.576s; normal local confctl host build120.315s passed.
- Package runtime closure has7paths and contains neither Ruby nor Python.
  Final653path host closure excludes the old exporter package/gem and superseded
  Rust candidate, preserving unrelated Ruby/Python services. Exact old662path
  closure is fully retained locally and NAR/path-set verified.
- Generated67hostJSON is unchanged, as are FIFO0640 root:syslog-exporter,
  stateDir0750, port9102, alert/scrape contracts, rsyslog and logrotate paths.
  The observed prior state directory was empty. No persisted format or migration
  exists. Rollback restores software together; metrics reset in either direction.
- The repository's intervening DNS/status changes do not enter the logger's
  selected input graph. Realized closures and identical logging policy paths
  corroborate the narrow host change; source provenance metadata also changes.
- Final release paired/periodic scraping passed:42 responses200 while1,040,000
  records counted exactly over65s at about16k/s; max6.76ms, no scrape error.
  Ten final100k comparison cases had exact counts. Ordinary finite Rust rates
  about50–70k/s and OOM36k/s exceeded fresh Ruby controls16k/s and4.1k/s by more
  than2x. RSS was7.6–8.2MB versus38–39MB. These shared-host, producer-limited
  observations certify neither production peak nor isolated causal scrape cost.
- One-Hz stress-vs-none ordinary median difference12.8% is noisy and is a separate
  profile from normal60s activity. The isolated<=10%capacity-impact subclaim
  remains unestablished; preparation is accepted only for the measured envelope.
  No threshold was retroactively changed and no full-design performance
  certification is claimed. Historical8ef measurements keep their own scope.
- Four useful TCP/UDP/private-local/OOM-burst transport cases preserved counts.
  Explicit overloads lost records/markers as expected; pinned ompipe reproduced
  a positive short write and concatenated records. Restart/partial-EOF/backlog
  termination observations completed; post-exit backlog drain remains unobservable.
  [V evidence](verification.md) preserves exact recipes, counts and stage limits.
  All measured processes/cgroups and watcher effects ended.
- Stable retention and owned scratch cleanup are complete; all command effects
  ended. Candidate653 and rollback662 closure sets are locally valid and match
  retained receipts. No store path or peer data was removed.

## Stable local retention

All10 ordinary indirect roots live under this session's `retained/` directory.
Each target was checked before redundant owned temporary roots were unlinked,
and again after cleanup. Keep these roots through the later approval/operation.
Final confctl NAME and generation links remain unchanged. Exact registration,
closure validity and owned cleanup proof is in C2 evidence and
`c2-artifacts/stable-retention-cleanup.json`.

| Root basename | Exact target |
| --- | --- |
| candidate-system | /nix/store/nw3d0j9hb1mrwf7hd0daxm6gk1vcfabc-nixos-system-log-26.05.20261026.718f670 |
| candidate-package | /nix/store/3hk34i2k760dirn1xrarxqsrwrcryaj5-syslog-exporter-0.14.0 |
| rollback-system | /nix/store/kgrfplplhrhhj4idvzx172lqh4hiyimq-nixos-system-log-26.05.20261026.718f670 |
| exporter-source | /nix/store/1ifcmrq7w2d86cjhqf7lsk6fcs226nqq-source |
| configuration-source | /nix/store/xvr7fkwhwkljagh8wx5mdcrvq5a5lz4v-source |
| production-configuration-source | /nix/store/jm67q6awjzqcyn9pr23i5hncxq4jj94v-source |
| nixpkgs-stable-source | /nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source |
| vpsadminos-source | /nix/store/cgk63vdx1wjl4ybd53abkd5aqyzc7sfa-source |
| confctl-source | /nix/store/8mjng71gica53p9jr4085f22xq1zslzg-source |
| normal-confctl-host-drv | /nix/store/nc86mbf1kmkwakxy1lcg87n60bxw8b1b-nixos-system-log-26.05.20261026.718f670.drv |

Both owned temporary Cargo targets were removed after their checks/reviews ended.
C2 additionally removed20 redundant root symlinks and12 explicit unused scratch
files (12,496,896allocated bytes), without GC or store deletion. Compact useful
measurements and failure evidence remain. This is retention for the open session,
not authorization to archive or otherwise close it.

## Approval boundary and later operation

The current authorization ends at preparation. No deployment command should run
until the user approves the target/candidate. Integration into each named remote
master needs its own explicit direction; deployment approval does not supply it.

At a future approved operation, reread the then-selected runtime coordination
guide and applicable configuration procedure. Recheck actual production
generation, candidate/rollback availability and complete activation difference;
the read-only snapshots above are time-bound. Prepare copies/builds before the
machine reservation as supported, acquire the exact configured machine only near
activation and verify its mapping. Keep one FIFO reader; replace package and
launcher together, preserve FIFO/state/log ownership, and avoid an unnecessary
rsyslog restart. Record any actual restart or service gap.

Verify both services, continuing file logging, real ingestion, legacy metrics/
labels/alerts and multiple60s scrapes/full240s flare window. HTTP availability
alone is insufficient. On regression restore the retained prior system through
the approved recovery procedure. Counters/gauges reset; rollback cannot recover
already lost FIFO events. No synthetic fatal/OOM messages belong in production.

Approved integration uses independently prepared fresh targets and short
repository claims, required hooks, fast-forward pushes and fresh remote ancestry
proof. Preserve exact reviewed/final ranges if history changes; a nonancestor
deployed head is not literally merged. Release a deployed machine only after
effects are verified and its complete deployed lineage is integrated into the
approved defaults. No release, approval, handoff or completion authorizes closing
this session.
