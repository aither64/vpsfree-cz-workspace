# Final recovery pins and operator handoff: general review

## Findings

No unresolved findings remain after the direct documentation remediation below.

### G1 — Important, resolved: runtime masks do not override the generated NixOS unit

`rollout.md:30-38`, repeated at lines 40-84 and 134-160, relies on
`systemctl mask --runtime` followed by `UnitFileState=masked-runtime` to keep
both supervisor writers stopped across application switches. The dated
maintenance task's `README.md:76-81` also recommends runtime service masks.

Both API hosts use NixOS-generated supervisor units in
`/etc/systemd/system/vpsadmin-supervisor.service`. That directory precedes
`/run/systemd/system` in systemd's unit load path. A runtime mask creates the
lower-priority `/run` symlink and does not mask the existing `/etc` unit.
The documented state check should halt safely, but the prepared rollout cannot
proceed as written. Omitting that check would permit activation to restart a
writer before the schema is ready.

Evidence:

- Exact C-built API1 closure
  `/nix/store/xcjmifj9d7vsic19cdwwx039hnbxxxr2-nixos-system-api1-26.05.20260911.21a67dc`
  contains the supervisor unit under `etc/systemd/system`.
- C's pinned nixpkgs source,
  `/nix/store/i2wrp0fbhvysy6bcanmwn6smd3jw938f-source/nixos/modules/system/boot/systemd.nix:641`,
  installs the generated unit directory there.
- An isolated `systemctl --root` fixture with a unit under `/etc/systemd/system`
  accepted `mask --runtime` and created the `/run` mask, while both
  `is-enabled` and `list-unit-files` still reported `static`.

Replace the mask procedure with a task-specific runtime drop-in containing
`[Unit]` and
`ConditionPathExists=!/run/vpsadmin-kernel-history-writers-paused`, plus the
named pause marker. Reload the manager, verify the effective negated,
non-trigger condition and expected drop-in, stop the supervisor, and probe a
start while the marker exists. Require `ActiveState=inactive` and
`ConditionResult=no` on both hosts before and after each switch. Retain both
files throughout the migration and any approved preview/apply window; remove
only those exact task-owned files and reload/start when restoring writers.
The production instructions and task README should describe the same method.

The replacement's mechanics were checked with a uniquely named harmless local
user-unit fixture. Existing true conditions composed with the runtime guard;
the guarded start skipped `ExecStart`; replacing the base unit and reloading
preserved the guard; removing the exact marker/drop-in restored execution.
Only fixture-owned files and its service were touched.

`systemctl show -p Conditions` prints `[unprintable]` with the installed systemd
260.2. The effective condition can instead be checked before probing a start
through:

```sh
busctl --json=short get-property org.freedesktop.systemd1 \
  /org/freedesktop/systemd1/unit/vpsadmin_2dsupervisor_2eservice \
  org.freedesktop.systemd1.Unit Conditions
```

Require a `.data` tuple whose first four values are
`["ConditionPathExists", false, true,
"/run/vpsadmin-kernel-history-writers-paused"]`.
Do not use the tuple's fifth integer as the observed pause check: an ephemeral
fixture returned an untested value after a skipped start. Use the service's
`ActiveState` and `ConditionResult` for that check.

The pinned API1 activation script updates `/etc`, and the pinned
`switch-to-configuration-ng/src/main.rs:2333-2378` reexecutes/reloads systemd
before normal start/restart jobs. Neither removes the proposed runtime guard
or marker. This is source inspection and a local service fixture, not a full
NixOS activation rehearsal.

Direct remediation verified: the concrete `rollout.md` now installs the unique
drop-in and marker on each API host, checks their presence and effective
condition before the blocked-start probe, repeats the checks around both
activations, and removes only the task files before reload/restart. Both deploy
commands select the completed generation `2026-09-14--19-51-56`. The instructions
also prohibit rebooting an API host while the runtime guard is needed and reuse
the same guard for repair and rollback. All fourteen revised shell blocks pass
`bash -n`.

Maintenance amendment `2fdc9f2889ac419136cd0cde0e0955c015ae7107` changes only
the README's runtime-mask advice to the tested drop-in/condition procedure;
the executable, runner, repair code and tests are unchanged from a80cc098.
Both maintenance revision occurrences in the rollout now select this final
amended head. The root agent reports its SSH push completed. The inspected
post-remediation rollout SHA-256 is
`eec0ad942237a23c32d26e10ae8917e742b469cf5336b76ce6b6cce84eea4ef1`.
G1 is closed; this bounded correction requires no blanket implementation rerun.

No other Blocking, Important or Advisory findings in the assigned final-pin
and operator-handoff scope.

## Reviewed revisions and consistency

Review performed directly with GPT-6 Astra at xhigh, per the user's explicit
override. Read the mandatory review skill, general lane, all four project
`AGENTS.md` files, initiative plan/state, implementation reconciliation,
committed pin diffs, operator documentation and relevant package/module code.

| Project | Base | Reviewed head |
| --- | --- | --- |
| vpsadmin | `014fbc78422f3660b295add7a50f35cc7acdf0c8` | `42984def67d405c235e2a34d91820563858ddd89` |
| vpsfree-maintenance-tasks | `6eea682ede8d8e2634b2d41e5b11cf0f02231bc6` | `2fdc9f2889ac419136cd0cde0e0955c015ae7107` |
| vpsfree-cz-configuration | `3f213d5ebf922ab5522690ab28b3fdfa9b3bed1d` | `c8b7a4995b587b7e072b5f77be6006356fbb104d` |
| vpsfree-kb-contracts | `919577d0c770e47b623c591f8bf0cce4e8d30666` | `610cb7bf35953ea6c1a9110fc12102e0713fcfc5` |

- C has one generated input-pin commit and changes only the
  `vpsadminServices` lock node to exact V42984def67d405c235e2a34d91820563858ddd89.
  Channel `vpsadmin` selects that input; staging, production, OS and other lock
  nodes are unchanged. The generated message accurately lists the two permanent
  vpsAdmin commits.
- K has one pin commit affecting exactly the five canonical revision files.
  Every field selects the same V revision and narHash as C. Only the `vpsadmin`
  lock node changes; existing vpsAdminOS 6bdf458 and nixpkgs nodes, page prose,
  navigation structure, screenshots and runtime fixtures are preserved.
- Independently compared parsed base/head lockfiles and asserted every recorded
  consumer input: all eleven select `vpsadminServices` at the exact V head.
  `recovery-consumer-build.log` ends with the completed eleven-host generation
  `2026-09-14--19-51-56`.
- V's final history contains the two permanent logical fixes; M contains one
  dated maintenance-task commit. The obsolete one-time repair is no longer an
  application commit. C/K pin updates are consolidated.
- The migration invocation matches the database package's actual
  `WorkingDirectory`, bundled Ruby path, account and schema-cache path. Both
  additive migrations exist at the documented IDs. The API1/migration/API2
  ordering is otherwise consistent with `autoSetup=false`.
- M's executable unconditionally invokes its importable runner under the
  installed `load` interpreter. Its implemented default covers all node/storage
  roles, including inactive hosts; repeated positive node IDs select a subset,
  batch size defaults to 1000, and writes require `--apply`. The documentation
  correctly distinguishes separately computed previews from reserved plans,
  requires paused writers for exact approval, and describes partial-apply and
  immutable-evidence limitations.
- All fourteen current rollout shell blocks passed `bash -n`. The reviewed
  pre-remediation rollout SHA-256 is
  `1c595e9f9bdc702ee8dc3f291c3b52466a755df9c694d8c0be8594050d02efde`.

## Validation limits

The root agent owns final VM integration and GitHub Actions monitoring. Earlier
delivery results do not validate the current follow-up; pending current-head
results must be recorded before the final handoff. This review did not repeat
the already completed implementation lanes or their database suites.

No production host, database row, deployment or historical repair was accessed
or changed. The number of repairable production events, including node 400,
remains unknown. The replacement pause method is validated by the local
systemd fixture and pinned activation-source inspection, not a complete
production-like NixOS switch rehearsal; its per-host runtime checks remain
necessary during an approved rollout. No persistent instruction or session
lifecycle action was taken.
