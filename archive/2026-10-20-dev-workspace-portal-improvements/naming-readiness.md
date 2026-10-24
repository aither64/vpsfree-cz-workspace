# Prepared naming process readiness observation

Prepared only, for the parent or its fresh utility after profile activation.
No live probe, naming request, session operation, restart or process mutation has
been run. Codex/tmux/root/roster continuity remains the parent's separate check.

Exact argv, from this session tracking directory:

```json
["python3", "/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/naming-readiness.py", "--package", "/nix/store/hzf9qda2ckjsv72b689bclc6p3v8ap9l-dev-workspace-0.2.0", "--unit", "workspace-portal@vpsfree-cz.service"]
```

Save stdout and exit/elapsed privately under
`verification/deployment-smoke/naming-after.{json,result.txt}`. The helper prints
one bounded JSON result. Exit 0 means one candidate-owned naming process and its
fixed catalog were observed; exit 1 reports a generic readiness reason without
raw diagnostics. A startup race or changed portal identity yields failure rather
than creating/restarting anything. It makes no HTTP, provider or model request.

The supported source is final Bf8's
`portal/cmd/workspace-portal/naming_runtime.go`: `startNamingRuntime` resolves
`PACKAGE/libexec/codex/libexec/codex/bin/codex`, then directly starts that native
child with `-c model_catalog_json=<quoted resolved catalog>`. It owns the child
for the portal lifetime. The ordinary Codex daemon is a separate service and is
not an adopted naming process. The fixed catalog is
`PACKAGE/share/workspace-portal/codex-models.json`. Bf8's
`nix/workspace-portal.nix` postFixup verifies its exact SHA256:

```text
049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1
```

The helper requires exactly the specified candidate and service. It reads only
systemd's MainPID property, expected immutable executable/catalog paths, normal
`/proc/PID/task/TID/children` ownership lists, process executable links, and the
fixed catalog setting from matching native children. Go may fork from any OS
thread; collecting every bounded task children list avoids assuming the main
thread alone owns the child. No recursive scan of unrelated processes is needed:
the supported launcher directly starts the native naming child.

It verifies the portal executable belongs to the expected candidate, exactly one
direct native child has the candidate's catalog argument, and that the portal
MainPID and direct-child relation remain stable on recheck. Normal observation
bounds are 1024 tasks, 64 direct children, four matching native candidates,
128 KiB streamed argument bytes per candidate and a ten-second process scan.
Systemd MainPID reads each have a five-second bound. Catalog hashing is bounded
to 1 MiB.

It never reads environ or logs. It never captures a complete command line:
unknown argument bytes are discarded as streamed, without retaining whole
arguments; only a setting immediately following `-c` with the exact
`model_catalog_json=` prefix is retained. No provider/authentication arguments,
unexpected argument values, command lines or raw subprocess errors are printed.
Output contains only readiness scope, known package/unit/catalog paths, the
catalog hash, portal/naming PIDs and expected native executable path.

Python AST validation and three in-memory argument cases passed: quoted catalog
after `-c`, rejection of an unbound catalog setting, and omission of unrelated
settings. These fixtures did not read `/proc`, run systemctl or invoke the helper's
live observation entry. The helper SHA256 is
`c0d61f5693c0cdbd12d6907a3ce684a31b1a1d91fabb471ae6f9a6a30d1b1ebe`.

This proves serving-process/catalog readiness only, not a successful naming turn.
There is no read-only public naming health endpoint. A package switch may replace
the portal and its naming child; the retained session root/roster must remain
unchanged under the parent's existing continuity procedure. Keep that acceptance
limit explicit and do not create a session or naming turn to extend this check.
