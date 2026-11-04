# Read-only WebUI prepublication snapshot

Session identity/environment matched the bound initiative. This bounded snapshot
used the already-realized Git 2.54.0 for canonical SSH `ls-remote`, and read-only
PR metadata. No checkout, index, ref or source mutation was performed.

Remote `git@github.com:vpsfreecz/vpsadmin-webui.git` advertised:

- `refs/heads/dev/typescript-client-migration`:
  `d3d5efbef53af8eb1caec025737dc47ecbc67e96`.
- `refs/heads/main`: `63d484fc070dbee633d32624de545e834d483701`.

[PR #126](https://github.com/vpsfreecz/vpsadmin-webui/pull/126) is open and not
a draft, with canonical same-repository head branch
`dev/typescript-client-migration` at the exact advertised feature SHA and base
`main` at the exact advertised default SHA. Metadata reports `UNSTABLE` merge
state and update time `2026-11-02T13:05:55Z`; no CI acceptance is inferred from
this registration/metadata snapshot.

Both refs match the lead's expected baseline. The planned feature publication
using an exact lease on `d3d5efbef53af8eb1caec025737dc47ecbc67e96` remains
feasible for the authorized message-only reconstruction and separately reviewed
unpublished source commits, subject to the publication owner's fresh final
remote/head checks. No upstream baseline refresh is indicated by this snapshot.
The snapshot supplies no new publication, merge or deployment authority.

No fetch, rebase, push, PR update/comment, test, build, CI wait, source write,
default/registry/deployment or lifecycle action ran. The frozen local `96d9`
browser batch was not accessed or disturbed. No Git/index turn was acquired;
read-only snapshot assignment complete.
