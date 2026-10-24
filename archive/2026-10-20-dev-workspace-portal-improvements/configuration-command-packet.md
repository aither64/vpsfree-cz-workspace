# Exact confctl deployment command packet (prepared only)

Lead accepted final C `530038a8ee2bf6772144b07ca0cb02426fc1e6d6`, runtime B
`f8f2938b4e2cfd6e5b82657d08f014357817808f`, shared A
`852e8c51091512bc79ca6c921ef1f5ccc46a9535`, configuration
`450e1ff538c1e94c1ec74f57b50fbe2efb31502b` and the affected-lane review gate.
This packet has only been syntax-checked. Implementer0 has not launched any build,
copy, dry activation, switch, machine claim or profile selection.

## Exact argv and execution ownership

Fresh Luna/low verification utility may launch the first two commands after lead's
explicit execution go-ahead. Both prepare outside machine ownership:

```sh
bash /tmp/portal-improvements-configuration-build.sh
python3 /tmp/portal-improvements-confctl.py copy
```

The first shell script only execs `python3 /tmp/portal-improvements-confctl.py build`.
The Python driver invokes the pinned confctl in the configuration Nix shell:

```sh
nix develop --no-update-lock-file -c /nix/store/j5wxvlxdnsh2gyc6wbjx8xxfllqp4zmv-confctl/bin/confctl build --yes cz.vpsfree/machines/aitherdev
nix develop --no-update-lock-file -c /nix/store/j5wxvlxdnsh2gyc6wbjx8xxfllqp4zmv-confctl/bin/confctl generation ls --local cz.vpsfree/machines/aitherdev
nix develop --no-update-lock-file -c /nix/store/j5wxvlxdnsh2gyc6wbjx8xxfllqp4zmv-confctl/bin/confctl deploy --generation EXACT_RECEIPTED_NAME --copy-only --yes --no-interactive --no-reboot cz.vpsfree/machines/aitherdev
```

After build/copy acceptance, parent acquires **only** physical machine
`vpsfree:aitherdev` with `repositories:[]`, reads authoritative held status and
launches these two independent commands. A fresh utility observes their independent
logs/status; it does not launch or resume activation:

```sh
env DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz DEV_WORKSPACE_CLAIM_ID=EXACT_HELD_UUID python3 /tmp/portal-improvements-confctl.py dry
env DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz DEV_WORKSPACE_CLAIM_ID=EXACT_HELD_UUID python3 /tmp/portal-improvements-confctl.py switch
```

Underlying activation argv (the exact generation is read from the immutable build
receipt, never supplied as current/latest/an offset):

```sh
nix develop --no-update-lock-file -c /nix/store/j5wxvlxdnsh2gyc6wbjx8xxfllqp4zmv-confctl/bin/confctl deploy --generation EXACT_RECEIPTED_NAME --no-reboot --yes --no-interactive cz.vpsfree/machines/aitherdev dry-activate
nix develop --no-update-lock-file -c /nix/store/j5wxvlxdnsh2gyc6wbjx8xxfllqp4zmv-confctl/bin/confctl deploy --generation EXACT_RECEIPTED_NAME --dry-activate-first --no-reboot --yes --no-interactive cz.vpsfree/machines/aitherdev switch
```

No reboot, health-check suppression, keep-going or rollback override is present.
Pinned confctl defaults health checks on and auto-rollback to the configured policy
(default enabled, timeout60s). Switch runs through the existing rollback helper,
then publishes the system profile. Dry activation is repeated immediately before
switch by the ordinary CLI. `--yes` skips ordinary confirmation; `--no-interactive`
prevents activation/health-check menus. The driver runs confctl with `setsid --wait`,
EOF stdin and `SSH_ASKPASS_REQUIRE=never`, so a broken authentication route fails
without prompting. No SSH config/key/known-host/auth/sudo changes are made.

## Source, artifact and live guards

Every phase checks exact current session/trusted-bound literals, clean config450,
Bf8 and C530 checkouts; both semantic lock paths must select Bf8/A852, retaining
extension767. The selected user profile must still be installed6bb. Unexpected
partial/conflicting identity markers or CONFCTL_SSH_CONFIG overrides refuse.
No command uses another session or changes refs/default branches.

The build runs only `cz.vpsfree/machines/aitherdev`. After successful build it reads
the generation selected by that command exactly once, records its literal timestamp
name and immutable `generation.json` hash, and validates embedded clean config450
and runtimeBf8. A prior exact output can be reused by confctl; the receipt records
whether that named generation existed before this build. Later phases load the
literal receipted name, rehash generation metadata and revalidate its store metadata.
They do not use the mutable current pointer to select a deployment.

For dry/switch the driver requires authoritative same-session claim status `held`,
resources exactly `["machine:vpsfree:aitherdev"]`, no repositories, and the exact
claim UUID. Both live and system-profile paths must still select predecessor75w4,
with clean config37a338b2/runtime968 metadata. Copy checks that those selections
remain unchanged. Switch success requires **both** paths to equal the receipted
toplevel with clean config450/runtimeBf8; zero exit alone is insufficient.

The fixed proven read-only SSH argv is:

```sh
ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o IdentitiesOnly=yes -o ConnectTimeout=10 -i /home/aither/.ssh/id_ed25519 root@172.16.106.40 COMMAND
```

Nix copy receives those proven options via NIX_SSHOPTS. Pinned confctl's ordinary
MachineControl uses its already proven configured `ssh -l root 172.16.106.40`
route. Copy checks the actual candidate activation executable/rollback artifact;
all remote metadata probes are read-only and access no password file.

## Receipts, logs and roots

All phase evidence is private under
`work/2026-10-20-dev-workspace-portal-improvements/verification/configuration-450e1ff5/deployment/`:

- `build.log`, `copy.log`, `dry.log`, `switch.log` contain exact confctl argv/output.
- Matching `PHASE-status.json` records running/passed/failed, PID, source heads,
  elapsed time and result; it is written independently of confctl logs.
- `generation-receipt.json` binds config/C/B/A, exact generation name/directory,
  SHA256 of `generation.json`, toplevel, autoRollback, derivation and embedded metadata.
- `generation.json` is the preserved original confctl record;
  `generation-names-before.json` records build reuse context.
- `PHASE-claim.json` records authoritative activation ownership. Before/after
  `*-system-paths.json` and `*-system-proof.json` preserve both path identities and
  nonsecret source metadata. Even a mismatch preserves observed system paths.
- `roots/` retains indirect local Nix roots for pinned confctl/Ruby, predecessor
  system, candidate system and derivation, rollback helper and every generation
  input source. They are retained through deployment/recovery; this driver removes
  no roots or generations.

Actual local confctl generation directory:
`CONFIG_WORKTREE/.confctl/generations/cz.vpsfree:machines:aitherdev/TIMESTAMP/`.
It contains `generation.json`, `toplevel`, `auto_rollback` and `ROLE.input` links.
Confctl also installs generation roots in
`/nix/var/nix/gcroots/per-user/aither/confctl-CONFIG_PATH_SHA256_FIRST8/`, named
`cz.vpsfree:machines:aitherdev-generation-TIMESTAMP-{toplevel,auto_rollback,input.ROLE}`.
Its ordinary command logs live under `CONFIG_WORKTREE/.confctl/logs/`; the phase
logs above remain independent of confctl's own successful-log retention decision.
Do not rotate/prune the prepared named generation or its roots during rollout.

Expected remote metadata paths are:

| Live | System profile |
| --- | --- |
| `/run/current-system/etc/confctl/configuration-info.json` | `/nix/var/nix/profiles/system/etc/confctl/configuration-info.json` |
| `/run/current-system/etc/confctl/inputs-info.json` | `/nix/var/nix/profiles/system/etc/confctl/inputs-info.json` |

Configuration fields are `schemaVersion:1`, `revision:450e1ff5...`,
`revisionDirty:false`; inputs field `devWorkspace.rev` must equal full Bf8.

A phase status already existing refuses automatic retry. Inspect logs/status,
local/remote processes, both system paths and retained rollback evidence first.
An exception/SSH disconnect does not release machine ownership or prove rollback.
No phase acquires/releases claims, selects the workspace profile, restarts Codex or
tmux, calls lifecycle helpers or cleans recovery evidence. Parent follows the
architect's system-before-profile order using the same held machine claim and
ordinary workspace-host switch. Preserve machine ownership through live review.

The utility brief must stop/escalate an unexpected local kernel build and report
failure promptly, without diagnosis/retry/deployment. No broader verification is
added here. Existing baseline smoke passed; final authenticated read-only smoke
and composition checks remain the parent's separate accepted commands.

## Read-only preparation validation

Pinned confctl source `8mjng71gica53p9jr4085f22xq1zslzg-source`, lock revision
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`, was inspected for CLI flags,
BuildList/Build generation persistence, NixFlake reuse, metadata field shape,
MachineControl/copy transport and rollback-before-profile activation order.
Actual `confctl build --help` and `deploy --help` confirm the options above.
Python compile and bash `-n` passed; no phase was executed.

Session-owned exact driver copy: [configuration-confctl.py](configuration-confctl.py).
Runtime argv uses the identical prepared `/tmp/portal-improvements-confctl.py`.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
