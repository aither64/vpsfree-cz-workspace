# Native instruction-file overrides require nonempty contents

In the automatic session slug initiative, fake-transport utility tests accepted
empty private instruction files, but the actual Codex0.160.0 utility failed
during setup before inference. The ordinary native control passed.

The exact pinned source `core/src/config/mod.rs` reads
`model_instructions_file` and `experimental_compact_prompt_file` before applying
explicit prompt precedence. Its `try_read_non_empty_file` rejects trimmed empty
contents with `InvalidData`. Supplying explicit `baseInstructions` does not
avoid that read. Schema/type validation alone does not establish this contract.

The implementation uses one fixed provider-owned
`EphemeralInstructionFileContent`, validated by the helper and provisioned by
its consumer for both private file overrides through teardown. Explicit task
instructions retain precedence. Focused checks and independent source review
passed; actual native calls progressed beyond this loader prerequisite but the
complete native fixture failed separate tool/persistence gates. No package or
isolation pass follows from the loader correction alone.

Design and execution history: `work/2026-10-03-automatic-session-slugs/`.
