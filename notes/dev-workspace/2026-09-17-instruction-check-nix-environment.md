# Validate instruction checks in the Nix builder

During `work/2026-09-17-agent-instruction-routing/`, the local Ruby guard and
Nix formatter passed, but the packaged check found two environment-specific
failures. Repeated `checks.${system}.name` declarations collided at evaluation;
put all names in a single `checks.${system} = { ... };` attribute set. Formatting
alone does not evaluate this expression.

The builder then used a C/US-ASCII Ruby default encoding. `File.read(...).strip`
failed on Czech procedure text. Read Markdown with explicit `encoding: 'UTF-8'`;
verify locally with `LC_ALL=C ruby test/agent_instructions_test.rb` and run the
packaged check. Both the new instruction check and existing deployment-contract
check passed after these fixes; no locale-dependent instruction content changed.
