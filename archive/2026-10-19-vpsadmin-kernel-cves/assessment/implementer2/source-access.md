# Exact-source read fallback

2026-10-19: Linux canonical bare repository is a partial/promisor clone.
A historical `git cat-file --batch` Makefile read automatically spawned
`git fetch origin --filter=blob:none --stdin` and a multi-million-object
`index-pack`, despite the intended read-only source task. The two owned
reader Python process trees were stopped (PIDs2299733 and2278273; both tool
sessions confirmed exit143). Other owners' readers were left untouched.
No refs, index, commits or branches were intentionally changed. A partial
object download may remain in Git object storage; no shared cleanup attempted.

All subsequent local Linux reads set `GIT_NO_LAZY_FETCH=1`. Missing objects
use the lead-authorized exact upstream public HTTP source/Makefile fallback,
retaining immutable revision, URL and SHA-256. No broad clone/fetch, build,
exploit or authenticated Node call is needed. `collect-source.py` records
source and version provenance under this owned directory.

The corrected exact HTTP fallback retained141 introduction/fix Makefile
snapshots, zero unavailable revisions, and branch checks without relying on
pre-release SUBLEVEL for a released first-fix number. Twenty stable patches
were reviewed;64387's ineffective backports were escalated and independently
accepted by architect/lead. Exact URLs/hashes are in source manifests.

An initial validation invocation selected the correct flake from the session
CWD and emitted a missing-Gemfile shell-hook warning before the direct CLI
validated five dossiers. It also created a session-local .gems directory.
That run is superseded by successful normal `nix develop --command
bin/security-advisory validate ...` runs from the owned repository worktree,
including final20. No shared index/commit was touched. Do not use the first
run as environment proof or remove potentially shared temporary files blindly.
