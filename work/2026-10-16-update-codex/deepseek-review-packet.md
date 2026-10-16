# Strict DeepSeek profile acceptance follow-up

Continue the independent review of this same Codex upgrade. Read the mandatory
review skill and applicable general, architecture, scope and risk references.
Inspect the new committed configuration behavior and supporting instructions,
and the complete configuration branch history. Unchanged repositories retain
their earlier review; do not duplicate those reviews.

Configuration worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-update-codex/vpsfree-cz-configuration`.
Read its AGENTS.md and the root workspace's applicable procedures before acting.
Base `ae98e9dbf05cd3f6b2d0c32255a4cb2d58c3865b`, previous reviewed/deployed head
`107255f8ab33c12ebdb4e484ea8b19d2fd792910`, new final head
`9721c331baa47edf3f0c4cbaaa5204889031047e`.

This adds one independently reviewable profile correction after the existing
skills, llm-agents and runtime pin commits. There is no repeated pin update,
obsolete branch approach or migration. The previous head was deployed to the
live system. Preserve its immutable rollout evidence; the new commit descends
from it. Other final heads and branch histories are unchanged.

The actual strict ephemeral DeepSeek canary failed before any model request:
preferred_auth_method is unknown. Exact 0.163.0 config schema also omits
model_supports_reasoning_summaries. The correction removes both. API login stays
forced and the existing model catalog declares reasoning summary support.
The guide and skill now validate using the actual strict ephemeral canary;
--help had exited before reading configuration. codex-ds is Home Manager-owned
under ~/.nix-profile/bin, selecting system assembly wz4w6709 (0.163.0).

Quick checks pass: git diff --check, Nixfmt, declared commit hooks, skill
validator, and strict native startup with rendered managed profile in a private
base config (no authentication copied, no model request):
deepseek-profile-source-check.json. The debug prompt-input approach was rejected
before commit because strict mode is unsupported there.

Overall risk remains high due to live deployment/authentication configuration.
Assess whether removal preserves intended ds behavior and whether documented
validation is sufficient. No new provider, model, credential storage, native
policy or persisted-state format is intended. User authorized aitherdev
deployment and this plan; no default-branch integration or reboot is authorized.
Existing coordinator reservation remains held and all prior jobs succeeded.
After accepted review, rebuild exact new configuration and deploy through a new
machine job under that reservation. Application profile/native identity stays
unchanged, so repeat only affected acceptance, not completed native/VM suites.

Write findings and explicit whole-branch history/no-migrations conclusions to
`work/2026-10-16-update-codex/deepseek-review-report.md`. Read-only review only;
this evidence report is permitted. Do not edit application files or spawn agents.
