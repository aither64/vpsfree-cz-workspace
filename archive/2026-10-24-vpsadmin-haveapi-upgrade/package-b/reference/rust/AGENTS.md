# vpsAdmin Rust client

Read [README.md](README.md) and [docs/development.md](docs/development.md)
before changing this crate. The crate targets the saved API 7.0 description;
its package version is independent of that API version.

`src/generated/**` belongs to the HaveAPI Rust generator, including the copied
runtime. Never patch those files manually. Fix HaveAPI's maintained generator
or runtime, then run `tools/regenerate` using the saved snapshot and pinned
formatter. Keep generated refreshes separate from handwritten changes.

Use the pinned Nix shell. Known quick checks are formatting, shell syntax,
snapshot/provenance inspection and deterministic regeneration. Compilation,
package checks and real-server acceptance are separate verification gates.
Fixture tests mutate only an explicitly selected disposable loopback server.

There is no commit hook framework in this repository. Use informative commit
messages and preserve the generated-source ownership boundary.
