# Portal deployment blockers observed on aitherdev

During `2026-11-10-portal-linux-review-performance`, system activation stopped
nginx before blocking while reloading user units. Backend `/healthz` stayed OK,
but the public HTTPS endpoint was unavailable. Check the public ingress as well
as the Unix socket during and after a deployment.

The blocked reconcile helper needed the exclusive workspace transition lock.
Thirty-two `dev-session team assign --message-stdin` wrappers from another
session held shared locks while waiting on terminal input for hours. They had
no child processes. The CLI reads the complete stdin message before dispatch,
but takes its transition lock before that read. For noninteractive assignment,
supply stdin with a closed pipe or file; do not leave a PTY waiting for EOF.
Recovery was explicitly directed by the user. Each wrapper's exact command,
PID/start identity, terminal input, wait state and lack of children were checked
before a PID-specific SIGTERM. No daemon or process group was killed. The
original system switch then completed, and the Codex daemon kept its PID.
Never infer permission to stop another session's helpers from this example.

The host's pressure-triggered Nix GC also removed a prepared package that had
been built with `--no-link`. Its store path alone was not a retention root.
The ordinary profile switch rebuilt it. Retain a GC root for a prepared package
until selection or explicit retirement; preserve the helper's existing package
and journal retention. Do not disable host GC to retain a candidate.

Exact revisions, process and deployment evidence are in
[the rollout record](../../work/2026-11-10-portal-linux-review-performance/rollout.md).

## Linux object index

The live Linux clone contained 29,130 packs, while its multi-pack index covered
only three. Full commit lookup took 4–5 seconds and exceeded the portal's
four-second command budget. A single foreground `git multi-pack-index write`,
with lazy fetch and automatic maintenance disabled, indexed the existing packs
without repacking or deleting them. It finished in under a minute; observed
RSS was about 1.9 GiB. Lookup then took 166 ms and live portal checks passed.
Do not increase API deadlines before checking whether the shared object index
matches the clone's pack inventory. Keep any future maintenance bounded and
separate from request handling; this repair did not enable automatic maintenance.


## Exact diff header abbreviation

Even with a complete multi-pack index, Git's default patch index header can
spend seconds proving short object IDs unique. A Linux blob-to-blob diff took
3.61 seconds across 29,130 packs, versus 0.161 seconds with --full-index and
identical hunks. The portal's hunk parser ignores the index header. Requesting
full hashes avoids that scan without increasing deadlines or changing line
counts. Keep this distinction when diagnosing fast numstat but slow previews.
