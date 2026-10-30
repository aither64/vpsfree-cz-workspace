# Exact A integration-spec predecessors

Complete snapshots derive from original A4363d1114f31cbb5d61411a95f6501bda17b50c0.
Only ts_generated_client_spec.rb changes one label expectation from
TypeScript (generated) to TypeScript API client, matching final A's wrapper.
Go/Rust specs do not assert the changed display labels; their configured
limitation strings are fixture data and remain byte-identical. TypeScript
profile spec is byte-identical. All old constructor/delegation/identity/profile
coverage remains, with no modern query assertions or disabled tests.

Final B restores all four complete accepted6b source files. These snapshots are
tracking-only inputs; no source/index edits, Git mutations, hooks/tests or
scratch checkout were used to prepare them. Owner2 runs the four actual A quick
files once after applying exact snapshots. Full original blobs and hashes plus
projected SHA256 values are in manifest.json.
