# Preview registered with session service tracking

Result: registration and migration succeeded on 2026-11-04. The preview remains
running at <http://aitherdev.int.vpsfree.cz:4567/v1.0/?doc_lang=en>, with the same
exact eb91 source, generated-client profiles and recovery inputs.

The installed selected package was
`/nix/store/9f239ylkq9ck9pmpnkny8nk0hy15lmwl-dev-workspace-0.2.0`.
Its public service API supports run/list/stop and deliberately has no adoption
operation. The user requested registration; the lead approved the necessary
brief replacement of this exact legacy preview. No session lifecycle action was
performed. The other three unregistered loopback services were left untouched.

- Resource UUID: `c70aa611-da3c-4f6b-b663-c1384e8ec0eb`.
- Registry UUID: `63421777-9201-4093-ae8a-c4bdd11e684c`.
- Managed unit: `workspace-session-c70aa611-da3c-4f6b-b663-c1384e8ec0eb.service`.
- Ruby PID: `2776403`; invocation: `c8dd786a487b4e19a798d12caf63eeda`.
- Started: `2026-11-04 09:55:41 CET`; application ready journal entry: `09:55:51 CET`.
- Public status: registered, count 1, phase/state running, error null.
- Exact source: `eb91a4d031c2c1f1c6ec6dd1aaed62e1f320eea7`, tree
  `d6b39fec8fe094471b47ac9054d890df6abf767c`; all 933 exported Git blobs matched.
- Working directory: this session's `preview-source-eb91a4d0` export.
- Runtime Ruby: `/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`.

The legacy unit `haveapi-doc-language-preview-20261101.service` was verified as
PID `1688000`, invocation `3ba77a243dc247feb7e4b1e1a13afb38`, with the exact
source/launcher/profile before stopping it. Its definition is retained in
[preview-legacy-before-registration.service](preview-legacy-before-registration.service).
The legacy process exited and port 4567 was free before the managed launch;
no duplicate server was launched. Source, launcher/profile hashes, dependency
paths and the no-socket profile build were checked before handoff.

Exact executed public launch command:

```sh
/nix/store/9f239ylkq9ck9pmpnkny8nk0hy15lmwl-dev-workspace-0.2.0/bin/dev-session service run 2026-11-01-api-doc-language-settings \
  --as-is --id c70aa611-da3c-4f6b-b663-c1384e8ec0eb \
  --name 'HaveAPI documentation preview' \
  --cwd /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview-source-eb91a4d0 \
  --json -- /run/current-system/sw/bin/env \
  HAVEAPI_PREVIEW_SOURCE_ROOT=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview-source-eb91a4d0 \
  HAVEAPI_PREVIEW_BIND=0.0.0.0 HAVEAPI_PREVIEW_PORT=4567 \
  HAVEAPI_PREVIEW_PRELOAD=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview_profiles.rb \
  /bin/sh /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview_launch.sh
```

The run returned exit 0 with one running registration. Independent health,
English/Czech overview/resource/authentication/protocol pages, all three profile
identities and exact versioned JS/CSS body hashes passed. First HTTP success was
observed within 22.1 seconds of stopping the old unit; that is an observation
upper bound, not a precisely measured outage. The other three loopback units'
PID/invocation/working-directory values matched their pre-migration records.

Inspection commands, already used during this trial:

```sh
dev-session service list 2026-11-01-api-doc-language-settings --as-is --json
journalctl --user -u workspace-session-c70aa611-da3c-4f6b-b663-c1384e8ec0eb.service --no-pager
systemctl --user show workspace-session-c70aa611-da3c-4f6b-b663-c1384e8ec0eb.service
```

Supported stop command for a future explicitly authorized stop; **not executed**:

```sh
dev-session service stop 2026-11-01-api-doc-language-settings --as-is \
  --id c70aa611-da3c-4f6b-b663-c1384e8ec0eb --json
```

The mechanism is appropriate for new temporary previews: durable ownership,
same-ID reconciliation and cgroup containment replace ad hoc PID tracking. The
existing-service migration is less convenient because it requires an explicit
manual handoff. An operator-facing migration example would help.

Actual usability findings:

- `dev-session service --help` returned generic usage instead of option help;
  `dev-session help` was also unsupported. The complete service documentation was
  available in the exact package's build source, not its installed documentation.
- Caller exports are not forwarded into the managed unit; explicit `env` arguments
  were necessary. No secrets were included in this request's arguments.
- Run reports native ownership/process state, not HTTP readiness. The process was
  reported running before the fixture's ready message; application checks remain
  necessary.
- Public list intentionally omits unit, PID, command and log location. Native unit
  inspection and the journal supply those operational details. Logging defaults
  to the journal; the old [preview.log](preview.log) remains historical.
- `Restart=no` and no revive relaunch are part of the contract. Stop, archive,
  delete, failure recovery and same-ID retry were not exercised in this trial.
  The three unregistered old loopbacks remain outside the new inventory.

No guard refused the registration. No manual registry edits, project-source or
dependency changes, host configuration changes, session lifecycle actions or
cleanup tests were needed. Leave the managed preview and all other services
running. Feedback remains in this conversation; no peer-session message was sent.

Evidence: [prepared exact request](preview-service-registration-plan.json),
[migration events](preview-service-migration-events.json),
[public run result](preview-service-registration-run.json),
[managed runtime and HTTP verification](preview-service-managed-runtime.json).
Lead-owned state was not edited.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-api-doc-language-settings/).
