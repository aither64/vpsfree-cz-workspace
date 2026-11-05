# I6: slow-image scheduling and existing catalog GC

Investigation/proposal only, 2026-11-05, `implementer1`. Capacity confirmed after
accepted I1; session/env identity verified. Fixed source **V =
`2951a632c4254a44747a8da326e3dde897eaa0e2`**, canonical `repos/vpsadminos.git`.
All source references below use V. Reuses I0–I4 evidence, especially
[I1](investigation-builder.md), [I2](investigation-publication.md), and
[I4](investigation-batching-concurrency.md). No fetch, execution, live-host check,
application change or commit. Only this evidence file is written.

## Exact slow-image families and scheduling consequence

| Image config under `image-scripts/images/` | Builder (`config.sh:1`) | Dated version |
| --- | --- | --- |
| `guix/config.sh` | `guix` | `RELVER=$(date +%Y%m%d)`, line 2 |
| `gentoo-openrc/config.sh` | `fedora` | `openrc-YYYYMMDD`, line 3 |
| `gentoo-systemd/config.sh` | `fedora` | `systemd-YYYYMMDD`, line 3 |
| `gentoo-musl-openrc/config.sh` | `fedora` | `musl-openrc-YYYYMMDD`, line 3 |
| `gentoo-musl-systemd/config.sh` | `fedora` | `musl-systemd-YYYYMMDD`, line 3 |

Bootstrap builders are Guix `guix:latest` and Fedora `fedora:44`
(`image-scripts/builders/{guix,fedora}/config.sh:1`). Fedora also serves Alpine,
Arch, Chimera, Debian 11/12/13/testing/unstable, Fedora 43/44/45/rawhide,
Slackware 15/current, Ubuntu 18.04 and Void glibc/musl (their `config.sh:1`).
Strict one-shard-per-builder therefore serializes all four slow Gentoo jobs and
can queue other jobs behind them while other workers idle. Exact duration is
user-supplied context, not measured here; family mapping alone disproves balanced
shards. Guix has its own family, so it does not directly block Fedora work.

Proposal: initially use bounded isolated VM workers, each serial internally;
dispatch individual images dynamically, starting known slow Guix/Gentoo early
while other workers advance remaining images. Builder warmth is a preference,
not exclusive ownership across VMs: duplicating Fedora in separate guests allows
useful parallelism. Preserve I4's per-worker state/disk/output/host-port isolation;
do not introduce concurrent calls into one shared builder root. Emit each tested
image's candidate/result immediately; neither visibility nor independent success
depends on waiting for every slow job or on the whole run succeeding.

## Authoritative retention policy and ordering

`os/configs/image-repository.nix:252` is the catalog GC authority. Every listed
rule has **keep=4**; rules match these rolling version families:

- Arch/Chimera/Guix: `^\d+$`; CentOS: separate `^9-stream-\d+$` and
  `^10-stream-\d+$`; Debian: separate `^testing-\d+$` and `^unstable-\d+$`.
- Fedora: `^rawhide-\d+$`; Gentoo: separate `^openrc-\d+$`, `^systemd-\d+$`,
  legacy `^musl-\d+$`, `^musl-openrc-\d+$`, `^musl-systemd-\d+$`.
- NixOS: `^unstable-\d+$`, independently for variants `minimal` and
  `impermanence`; openSUSE: `^tumbleweed-\d+$`; Slackware: `^current-\d+$`;
  Void: separate `^glibc-\d+$` and `^musl-\d+$`.

Preserve exact configuration/regexes, including rule order and nullable selectors;
do not replace them with one global count or four images per distribution.
Unmatched fixed versions have no deletion rule here. This is repository image
retention, separate from CI artifacts, cache/logs and publication reader grace.

`os/modules/services/osctl/image-repository/gc.rb:32` groups catalog entries by
vendor/variant/architecture/distribution, then by first matching rule (`:93`).
For each list it removes its first `count-keep` entries (`:47`), keeping the last
four; it does not inspect latest build outcomes, attempts or tag protection.
Input order is `osctl-repo local ls` (`:80`), which emits index order
(`osctl-repo/lib/osctl/repo/cli/repo.rb:13`). Native index save sorts tuple strings
(`local/index.rb:70`, `base/image.rb:87`, same `osctl-repo/lib/osctl/repo/` prefix).
Date suffixes thus sort lexically; this is not filesystem age/mtime retention.

Coordinator `os/modules/services/osctl/image-repository/build.rb:71` attempts
selected images, sets defaults, runs GC, then postBuild. Individual image failures
warn/continue (`:176`); named subset selection (`:133`) does not restrict GC's
full-catalog scope. GC can prune an overfull old group even if its current rebuild
failed or was unattempted. Four existing versions plus one failed new build stay
four; five existing versions plus a failed new build still prune to four. A failed
Gentoo openrc build does not consume a slot in systemd or musl-openrc groups.
Old last-good images are not immortal: eligibility for unchanged policy still
applies. GC's ignored removal status (`gc.rb:51`) is existing weak diagnostics,
not permission for a new path to claim unchecked deletions succeeded.

## Minimal preservation in candidate-delta aggregation

Use one catalog writer for adds, defaults, GC and publication, as I2/I4 require.
Seed a private aggregate from last-good; merge only validated eligible successful
image deltas. Failure/missing/unattempted results produce no deletion delta and
do not suppress other successful updates. At run-final aggregation, reuse the
existing GC runner and exact rule configuration once against this complete tree,
then validate/select it. Workers must not run full-catalog GC on partial catalogs
or send `--delete` mirrors of their subsets. Distinguish explicit GC removals
from absent build outputs; no extra retention subsystem is needed.

Preserve tag/default dependencies: successful `local/repository.rb:24` moves tag
symlinks; `local/index.rb:34` removes those tags from previous same-tuple-family
entries. Apply final successful deltas in original configured coordinator order,
not completion order: Debian 11 and 12 both request `oldstable`
(`os/configs/image-repository.nix:69`). Missing deltas synthesize no tag change.
Default vendor/variant targets must exist (`local/repository.rb:122`); configuration
defaults are `vpsadminos`/`minimal` (`os/configs/image-repository.nix:11`).
GC `local rm` removes index entry, payloads and its tags (`local/repository.rb:70`);
tagged entries have no GC exemption. Validate final index/symlink/payload
consistency after policy application; do not manufacture dangling aliases.

Result: independent success survives failures; catalog deletions remain governed
by the existing matching/count policy. Early per-image evidence remains useful
while the bounded run continues. Runtime capacity/timings and failure-injection
verification remain future implementation checks, outside this investigation.
