# Bounded observer startup-guard revision

The accepted original42-file packet remains at
`../client-example-profiles-publication-preparation-20261024T085327Z/` with
manifestSHA256 `b8e4bd53c993dc35a8a846903a13e4e8fa5e1486b7171ce091a3f0a9c255a35e`.
Its receipt, README, template and all42 manifest entries were independently
rehash-checked before copying and again after this revision. No original was
changed. Copied original manifest/receipt remain here as
`prior-preparation-manifest.json` and `prior-preparation-receipt.json`.

The earlier launcher verified declared CLI arguments/TOML and bound the actual
`thread.started` event, but did not verify the persisted first turn. Its consumer
also had an unnecessary10-second startup-context wait. No watcher had been
launched from that preparation, so this is a preparation correction without
Git/API/CI effects or a changed application source/review boundary.

Only `launch-observer.py`, `run-observer.py`, `observe.py` and README change from
their original contents, with a new parent-only `parent_startup_gate.py` helper.
The new launcher will verify the actual new thread's persisted session metadata,
first-turn model `gpt-6-luna`, effort `low`, `never`, `danger-full-access`, exact
native developer instructions, native/catalog identity and current installed
`full_access` policy before writing any observation gate. It derives a narrow
exact-UUID/date rollout lookup from its own CLI event; it never scans foreign
threads. This helper is called only by the parent, not the ordinary utility.

The explicit gate is the absolute future operation directory's
`launch-verified.json`. It binds absolute rollout path/threadID, persisted-event
hashes, catalog/native identities, exact operation entrypoint/argv/scriptSHA and
the complete payload-manifestSHA. The parent verifies all payload bytes before
atomic gate creation. Payload includes grant, discovery, executable/tool policy,
launch/readiness records, brief, common guard, observer and gate-consumer scripts.

The brief names that exact gate and tells the utility to run the assigned
self-waiting command once. Missing gate at startup is expected. Exclusive
`gate-consumer-started.json` creation prevents a second invocation. The consumer
checks the parent proof and exact payload hashes, records consumption and runs
the exact observer once. It does not call a private `turn_context` tool, inspect
its own rollout/context, scan homes/workspaces or infer model settings. Parent
startup rejection stops the consumer without API calls; no automatic retry or
replacement launch. No arbitrary quiet/startup deadline or process termination.

For schema confirmation, only whitelisted metadata keys and native-instruction
presence from the known completed root-recovery watcher identified in its
accepted `launch-verified.json` were inspected. No current Rust/review/long logs
or live utility contexts were read. No action entrypoint was imported/executed;
validation is syntax parsing and static guard inspection only. All execution
flags and future evidence/artifact identities remain false/unset. Existing user
merge/backport preparation authority persists, with actual feature/CI execution
still gated on complete accepted Rust results. No source, Git, SSH, API, setup,
test/build/install, utility/claim, publication or lifecycle action was performed.
