# Verification

Quick checks: JavaScript syntax and focused Go portal checks pass; after the
baseline refresh, Go completed in 0.197s. Final composition checker passes at
ad63a832bad1061b023b861fe3772bbe6b85c6de.

Previous exact final heads fdd44b3 / 38715961 / 838c6833 passed browser (166s),
application Nix build (921s) and aitherdev configuration build (145s). Browser
covered stale archive completion, missing/unknown details, real pending recovery,
Retry without mutation and cancellation in Chromium/Firefox, plus lifecycle,
presentation and team activity. Seven other browser scripts passed earlier.
Application output: /nix/store/w8dn36rxwknbn8b4xa5vjp8hb4jijga1-dev-workspace-0.2.0.
Configuration generation: 2026-10-14--18-52-16. These are build-only results;
no own activation occurred in those attempts. The tools install checks took most of
the application build; it completed without cancellation or a kernel build.

Runtime rebased onto newly merged 6f8773da; both own commits retain identical
patches. The browser batch remains applicable to that unchanged patch. Final
exact composed application/system builds are still required and recorded below.
Logs/status are retained locally; earlier failed attempts are described in state.

Final refreshed exact builds passed: workspace 00689c78, 892s, application
/nix/store/khdgb3zhwb7d0qmsnb2sx0mjps178lh3-dev-workspace-0.2.0; configuration
5cd53c69, 140s, generation 2026-10-14--19-13-02, system
/nix/store/ngzvkhy412m11hq45yi8fcj0lhf7jyfc-nixos-system-aitherdev-26.05.20261012.7993f34.
No kernel build. Profile preparation selected the exact built application and
passed Codex/semantic contracts at version 0.160.0. Another tracking-only archive
advanced workspace default; own pin rebased patch-equivalently to ab996e0f.
Nix evaluation confirms the same already-built application output. Refreshed
workspace/profile snapshots follow. All three original heads later merged through coordination. No own activation has occurred.


Current combined baseline: runtime 92b2576d, workspace 5a2119d4, configuration
ac001928. Each contains the previously merged own head. JS syntax and the final
composition checker pass. Focused Go details/embedded/recovery notice tests pass
in 1.371s with TMPDIR=/tmp and absent fixture provider catalog. The first invocation
failed only at 110-byte Unix socket paths below Nix shell TMPDIR (Linux limit
108 bytes); shortening the temporary prefix runs the same tests without source
changes. Exact combined build and browser results follow after affected review.


Exact combined checks passed under fresh utility `/root/stale_archive_combined_checks`:
Chromium/Firefox archive and lifecycle checks 76s at runtime 92b2576d (Go package
74.057s); application build 22s at workspace 5a2119d4, output
`/nix/store/13s6kwhliihnnby7rxym6wsbafv6cxh6-dev-workspace-0.2.0`; aitherdev
configuration build 103s at ac001928, generation `2026-10-14--20-46-22`.
All tool handles are closed. No source edits, retries or deployment in the utility.
Logs/status files use `*-combined` prefixes. Actual deployment and live acceptance
remain separate. Both preparations will use this reviewed combined composition.


Final live acceptance passed after both original deployment jobs succeeded.
Actual application 13s6kwh and system xf0i8ry match the exact builds. The original archived
session heals a simulated stale page in Chromium and Firefox with exactly one
reload and zero mutations; the authoritative index has no pending marker. Native
Codex/tmux PIDs and socket identities match the final baseline; actual native
service binary reports 0.160.0. The ambient terminal client is separately 0.162.1
and must not be used to infer this service's version. See acceptance.md for exact
identities and corrected check. Reservation released; final notifications settled.
