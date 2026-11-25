# Loader evidence review reconciliation: LC1

LC1 is **resolved** on unpublished diagnostic head
`9805ea20e336aa6e2559f5f7af73de36fce3ecc8`. The original independent report,
[loader-csd-review.md](loader-csd-review.md), remains intact and records one
Blocking finding, no Important or Advisory findings, and all four review lanes
at HIGH risk. This record binds the direct correction to the final committed
source; it is not a new independent review or a runtime result.

## Exact reviewed and corrected ranges

- Reviewed: `2951a632c4254a44747a8da326e3dde897eaa0e2..12df7c05ac72a48fac748b09f6f9c7660f3a1e0e`.
- Corrected: `2951a632c4254a44747a8da326e3dde897eaa0e2..9805ea20e336aa6e2559f5f7af73de36fce3ecc8`.
- Both loader owners have parent `b361b8c600bc1d50c237a68ca5413d38be9a0e99`.
- The reviewed old owner is retained at local
  `refs/heads/2026-11-03-livepatch-fixture-failures-reviewed-loader-12df7c05`.
  It is not an ancestor of the corrected owner. Neither loader owner has been
  published by this package; the last remote diagnostic proof remains b361.

A preserved the prior nine provenance refs, detached5235 and the source GC roots;
there are now ten local provenance refs. The six prefix commit objects, their
messages and patches remain unchanged. The corrected series still has seven
purposes, 27 paths, +4548/-274. The loader purpose is four coupled paths,+645/-2;
its helper remains mode100644 and is invoked through Bash. New loader patch ID:
`b6b39fbdbd31def7e7a5ebf6c88fa048e701f4cb`.

## Direct correction and representative checks

The only old12df-to-new source difference is the marker redirection in
qualification_loader_command: `>` becomes `>|` for trace_marker. The per-attempt
PID file retains plain `>` under set-C. Locale, module, PID/marker content,
attempt behavior, shared deadline, health and recovery are unchanged. This is
the reviewer's requested correction inside the accepted contract, with no new
design or interface.

C first corrected the fixture to precreate a regular, non-symlink marker that
already contained the begin clock marker. The old committed command then failed
at that redirection with status1 and zero exec calls. After the source fix:

- Attempts1 and2 each reached the actual executable fixture with matching PID,
  localeC and module; attempt1's file was unchanged after attempt2.
- Repeating attempt1 failed at its exclusive PID file, without another exec or
  modification of its file or the marker.
- All35 affected actual-loader controls, Ruby parse, declared RuboCop and
  one-file whitespace checks passed. Fixture children were reaped.

Evidence: [C remediation](package-c-loader-lc1.md),
[RED log](package-c-loader-lc1-red.log),
[RED command results](package-c-loader-lc1-red-commands.log),
[GREEN log](package-c-loader-lc1-green.log),
[GREEN command results](package-c-loader-lc1-green-commands.log),
[style check](package-c-loader-lc1-rubocop.log).
The other82 earlier controls retain only their unchanged component/input scope;
they were not rerun or relabelled as a fresh117-control batch.

## Coordinator verification and history disposition

Root read the full independent report, C's receipt, actual check output and
strengthened control code. Root inspected the committed diff and independently
verified that it is byte-for-byte C's saved one-file patch, SHA256
`b1dedf7496d0efdb6b52f8e6af338704e59852719bb2d2ef8f6827031821a818`.
The committed qualification SHA is
`5c4db809f464110d1eea2a29008fc23f9359d9d944a8cd48ee00c818422caf72`.
Workflow/common/helper hashes remain exactly
ffce88c8ad7a5e5654ff967c98f5e8218cbfa546bead738102c08c5f9cdf2ed7,
8acb93d5d59568b65e35e0a7fb436ce1354da149a5b882b7e66f9e94518c0509,
and6b85cedda7222e0b37019d7040767204b4a306a5b9eb9c006d32822b1db8045c.
All other tree modes/blobs are identical to the reviewed owner.

A's normal Bundler-enabled amend preserved the raw owner message, SHA256
`09e4322a686e84dd95955c3e9152be6923876d9d61a49c68ca5036c2cacb97c1`.
Nixfmt, RuboCop and all three message hooks passed; root read the hook receipt.
The amend exited0 at05:05:03.726759Z and Git ownership was explicitly released
at05:05:03.960158Z before history or record work. Both checkouts are clean;
A's complete history/receipt package is accepted, with all clients terminal.
See package-a-diagnostic-300s-history.log, -hooks.log,
[package A result](package-a-result.md) and [launch record](verification-launch.md).

Under mandatory-change-review step9, these focused checks and inspection close
LC1. The change is precisely the requested narrow correction; it introduces no
new design, scope or contract that triggers step10. No reviewer rerun is needed
solely to confirm it. This intentionally changed source is not labelled a
mechanically equivalent rebase. The original independent whole-history
conclusions remain applicable through the unchanged prefix and folded remedy:
no obsolete/fixup/WIP repair history, repeated update streams or migrations.
No migration merge/release/deployment/external-use provenance is introduced.

## Remaining gates

The code-review gate is cleared for a separately released, fresh-ref-guarded
publication and ONE exact-head diagnostic run. This closure does not prove Nix
module evaluation, actual naming/APIC-to-owned-TID mapping, runner permissions
or schedstats, trace formats, clock brackets, first-fault freeze/loss bounds,
final host coverage, healthy transition or normal late cleanup. A complete RED
capture is not qualification. No retry, warning waiver, kernel correction or
four-hour escalation follows automatically.

Primary645927/original14400/full workflow and production skip-message remain
unchanged. All four temporary diagnostic purposes stay outside shipping ancestry.
Final delivery still needs marker removal, final history/review preparation and
full exact-final-head native plus nine rows with semantic, identity, health and
recovery proof and applicable integration approval. No deployment or session
lifecycle action is authorized. Session remains open.
