# Reconcile watcher commands before fallback

Interrupting a verification agent does not prove its tool-owned build never ran
or stopped. Before launching fallback, inspect its operation/status and native
effects. Do not infer no execution from an unreadable or interrupted launch.

During mx2 staging, the watcher had started a native five-system build before
the lead interrupted it and mistakenly launched a duplicate fallback. Confctl
reused the earlier matching generation; a later successful invocation therefore
did not create a new timestamp. Match toplevel, role paths and actual native
generation metadata instead of assuming timestamp freshness proves execution.

Both invocations also wrote one captured log after truncation, leaving NUL gaps.
Preserve that raw artifact and report the capture limitation; do not fabricate a
clean replacement. Exact command status, registered output/deriver/NAR and
generation/source/input checks established the final result without another run.

Related session: work/2026-11-01-mx2-nixos-migration/staging-build-result.md.
