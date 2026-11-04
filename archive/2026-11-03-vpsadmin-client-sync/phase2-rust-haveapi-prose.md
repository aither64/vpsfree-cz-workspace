# Phase 2 Rust and HaveAPI guidance draft

For lead's main writing pass before applying/committing. Canonical candidate
section is owned by implementer3. No runtime, generator, version or test change.

## Rust docs/development.md

Replace the plain `docs/api-schema-export.md` reference under Saved schema with
the full canonical [schema export and generated-client synchronization](https://github.com/vpsfreecz/vpsadmin/blob/master/docs/api-schema-export.md#generated-client-synchronization)
link, retaining the existing review/copy/regenerate instructions.

Add after the existing canonical-format paragraph:

Follow that procedure when API, shared-schema, generator or copied-runtime
changes affect this client. Record the API source revision and either refresh
the client default branch or retain source-tied evidence that no generated
change is needed. A successful `tools/regenerate --check` proves consistency
with the saved inputs; it does not prove they match current API source.

Add under Compatibility and release checks, before the existing release checklist:

Ordinary source synchronization does not itself require a crate release.
Assess Rust interface compatibility under this crate's versioning policy when
preparing a release, and follow the linked synchronization procedure for task
completion and any dependent release requirements.

## HaveAPI AGENTS.md route

Add Required procedures row:

| Changing shared-schema code, Go/Rust/TypeScript generators or copied runtimes that affect generated vpsAdmin clients | [Downstream generated-client synchronization](doc/agent-instructions/development.md#downstream-generated-client-synchronization) |

## HaveAPI development guidance

Add `## Downstream generated-client synchronization` before the Rust generator
and runtime section:

When shared-schema code, a Go/Rust/TypeScript generator or its copied runtime
changes the generated vpsAdmin clients, assess all three downstream clients.
Follow vpsAdmin's [generated-client synchronization procedure](https://github.com/vpsfreecz/vpsadmin/blob/master/docs/api-schema-export.md#generated-client-synchronization)
to refresh affected client defaults or record source-tied evidence that no
generated change is needed before completing the task.

Retain the exact API schema/profile, HaveAPI revision and dependency/toolchain
identities used for each assessment. Existing saved-input regeneration checks
establish reproducibility; assess current API source separately. Ordinary
source synchronization does not require publishing client packages. Required
releases and integration order follow the linked procedure and each client's
own compatibility policy.

This rule applies to generated vpsAdmin clients. APIs built with HaveAPI retain
their own downstream maintenance and release policies.
