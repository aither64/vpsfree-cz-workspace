# Fetch explicit remote refs for integration proof

An organization bare clone had no origin feature tracking ref. Running
`git fetch origin master <feature>` fetched objects/FETCH_HEAD but did not create
that missing ref, so the cleanup preflight could not resolve origin/<feature>.
No worktree removal had occurred.

Use explicit mappings when verifying exact remote heads in such a clone:
`git fetch origin refs/heads/master:refs/remotes/origin/master refs/heads/<feature>:refs/remotes/origin/<feature>`.
Then compare local/remote feature hashes and prove ancestry in origin/master before
removing any worktree. Explicit fetching resolved the missing ref and all four
repositories passed exact-head merge proof. Avoid relying on origin/HEAD being a
symbolic ref in a bare clone; verify the default using ls-remote --symref if needed.

Related initiative: work/2026-09-12-portal-review-experience/compact-integration-results.json.
