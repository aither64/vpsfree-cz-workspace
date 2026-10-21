# Dynamic omfile creation policy correction

The natural VM failure at `5d910028d32ce9305dc8161c51b3ed17ec4179bb`
failed the first `wait_for_ingested` predicate: SSH grep of the current remote
file returned permission denied. The exporter-marker predicate was not reached.
The UDP listener and expected pathname were present.

`runtime-verification-01.log` contains 2362 lines / 260483 bytes, SHA256
`263496ae8f2553c01056b6e87e0fcf654163bf5269391ffe861a2c65a50d7c47`.
Its emitted metadata shows reconciled `/var/log/remote` as root:log-readers0750,
but every new nested directory as root:root0700 and its log as root:root0640.
The recorded natural timeout is 31.39 seconds for the explicit 30-second
predicate. `runtime-verification-result.json` remains failed; host builds were
not run after command 1 failed.

## Cause and evidence

Legacy globals supply the local messages selector, but do not supply the
intended owner/group/directory modes to the RainerScript dynamic omfile action.
The previous protocol probe substituted the reader group with root and checked
only the regular-file mode, so it could not prove the new tree's group/traversal.

Two bounded native probes used the pinned rsyslog and frozen VM configuration
inside a disposable root user namespace with mapped nonzero groups. Both passed.
They compare original globals with the same six explicit action properties:

| Output | Globals only | Explicit omfile properties |
| --- | --- | --- |
| Every fresh remote directory | uid0/gid0/0700 | uid0/gid100/0750 |
| Current remote file | uid0/gid0/0640 | uid0/gid100/0640 |
| Local messages | uid0/gid100/0640 | uid0/gid100/0640 |
| Precreated exporter pipe, second probe | uid0/gid200/0640 | uid0/gid200/0640 |
| Local/remote/exporter markers | Present | Present |

The separate group 200 for the pipe proves the reader group's policy does not
replace the exporter's group. `logger-permission-probe-{01,02}.log` preserve the
complete outcomes. A final focused compatibility probe also passed: existing
remote files uid0/gid0/0600 and directories uid0/gid0/0700 retain their metadata
when the explicit action appends to the file. Its evidence is
`logger-existing-metadata-probe.log`.

The native probes use 3-second input-start bounds, 0.2-second local/remote spacing,
2-second observation bounds and a 1-second TERM grace followed by owned-child
kill/reap. They change only disposable paths/ports and namespace group names.
No host group, production file, service, deployment or credential changed.

## Approved correction

Architect0 confirmed and clarified the design: set fileOwner=root,
fileGroup=log-readers, fileCreateMode=0640, dirOwner=root, dirGroup=log-readers,
dirCreateMode=0750 directly on the remote omfile action. Retain the umask,
legacy local selector, template, inputs, pipe, rotation and HUP behavior.

The quick policy check asserts those action properties; its syntax rendering
substitutes root only because the build sandbox lacks the deployed reader group.
Actual-group semantics are established separately by the native probes and must
still pass the full VM. VM assertions now require the fresh subtree to be absent
before injection, inspect every new ancestor, and inspect initial messages mode.
The operations guide distinguishes explicit remote policy from legacy messages
defaults and creation from historical reconciliation; lead supplied final wording.

Final base: `38e7c837893695999e588a73f5d2a0088b8257b1`.
Consolidated logger: `bd54b28c63770b782a4af435ad8dfb9619b6032c`.
Final head: `d07b4251172020472b21e8830e92b023849d543f`.
The proxy patch is identical by range-diff. Delta from the failed head is limited
to logger config, quick policy fixture, VM assertions and operations explanation
(four files, +35/-7).

AST, pinned nixfmt, diff checks, final-head quick Nix policy/rsyslog/logrotate
syntax check and mandatory commit hooks passed. Scoped independent review of the
production correction precedes a fresh watcher-run VM. Neither full VM success
nor host-build success is claimed here.
