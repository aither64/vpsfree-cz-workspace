# Inspecting refs in a new bare clone

A bare clone may have no remote.origin.fetch mapping. In that case, plain
git fetch origin updates FETCH_HEAD without populating origin/master or a
published feature's remote-tracking ref. Inspecting origin/<feature> can then
fail with "unknown revision" even though the branch exists remotely.

Fetch the required refs explicitly before comparing them, for example:

```sh
git fetch origin '+refs/heads/master:refs/remotes/origin/master' '+refs/heads/<feature>:refs/remotes/origin/<feature>'
```

This resolved the PHP mirror inspection during
work/2026-10-11-diagnose-vpsadmin-api-exception. Both remote-tracking refs then
matched the server's published heads; no branch reset or force-fetch over
another session's local branch was needed.
