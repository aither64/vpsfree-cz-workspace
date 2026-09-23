# Session identity and catalog-owned team prompts

## Goal

Make portal-launched development conversations reliably identify their own
session, and move persistent team-member instructions from portal code into the
installed team catalog. Support configured custom roles with explicit purposes
while keeping the existing CLI and portal on the same creation path. No prompt
may cause a model turn before the first real user message or assignment.

## Scope and design

- Generic `dev-workspace`: validate catalog role purpose and instructions,
  project them into direct-creation snapshots and durable member rosters, and
  bind each thread to a technical session identity. The portal may prepend its
  own identity text. Existing members retain their current instructions.
- vpsFree extension: permit ownership verification by a thread-bound session
  identity plus a matching `dev-session current` result when an external shell
  omits the environment markers. Explicit mismatches still fail closed. Select
  reviewers by role purpose, not only a hardcoded role name.
- Coordination workspace: configure concise defaults and update workspace
  agent rules to use the verified binding and purpose-based team delegation.
  Configuration-defined roles are not edited in the portal in this phase.

The prompt is attached as developer instructions during thread start/resume;
starting an idle thread must not submit a prompt-only turn. The creation receipt
and roster freeze the resolved role instructions and purpose. A member added
later uses the catalog current at that time. Forked sessions preserve the
source's member policy but use the destination session identity.

## Compatibility and deployment

The catalog and direct-creation snapshot gain a new schema version. Readers
continue to accept existing receipts and rosters and apply the exact legacy
instructions when prompt fields are absent. The installed package on aitherdev
is upgraded forward only; rolling back to an older package after creating a
custom-role session is unsupported. This affects one development host only.
No vpsAdmin, database, service protocol, generated client, cluster format or
NixOS node configuration changes. The dependency order is generic runtime,
extension, then site package pin and aitherdev user-profile switch. The user
authorized integration of those three repositories into `master` in the plan
discussion preceding implementation.

## Verification

Run focused parser, snapshot, runtime, CLI and portal tests, including old
receipt compatibility, custom roles, prompt-free bootstrap, wrong-session
rejection and missing environment markers. Commit and perform mandatory
Sol/xhigh change review before long packaged checks. Use a fresh Luna/low
watcher for long Nix build, tests, CI and deployment monitoring. Exercise a
new portal-created session and verify its first external tool shell sees the
correct binding; inspect the installed catalog and UI. Capture final feature
heads, fast-forward approved master branches, and retain the session open.
