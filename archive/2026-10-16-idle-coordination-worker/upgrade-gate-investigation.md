# Read-only upgrade-gate investigation

The foreign manual integration 1ff62d7b-911b-4551-82ed-be4a0f6d2460 is still in prepare. No foreign files, jobs, reservations, refs or journal were changed.

Installed immutable recipe source: vpsfree-dev-workspace-tools/share/vpsfree-dev-workspace/lib/workspace_integration_recipe.rb, capture at line 13 and verify at line 49. A generic 262144-byte stdout cap also applies to Git filename output. The retained workspace scratch comparison from a158608e2baa41696cd2340c82b45460f56d77da to 5fb850f59fe26d67020fdf680744fe08a83a4c67 emits 1634249 bytes and 10840 paths. Both lock files are only 20172 bytes, and scratch Git status is clean. This reproduces the stated size refusal without executing a recipe refresh or mutation.

Excluding work/archive/notes yields just 88 bytes, but paths are AGENTS.md, flake.nix, skills/update-codex/SKILL.md and skills/update-codex/agents/openai.yaml. Therefore a size fix alone would expose the recipe's separate unrelated-file refusal. Do not treat filtering the large tracking list as proof that the semantic refresh is valid. Its owner must inspect the intended feature and baseline changes, preserve required behavior and obtain applicable review before settling that run.

Our own profile preparation is intentionally refused by the selected schema-1 predecessor while any manual run is pending. Our deployment remains queued behind the existing holder and earlier request. No native startup blocker remains. User was offered optional expansion to investigate/fix the foreign blocker; no reply or scope expansion is assumed.
