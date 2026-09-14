# API-guide documentation follow-up review

Initiative: `2026-09-13-auth-email`.
Workspace: `/home/aither/workspace/ai/vpsfree.cz`.
Tracking: `work/2026-09-13-auth-email/` (plan.md, state.md).

Review only the added bilingual API-guide edits and their updated guarded
release records. Existing account-page candidates already passed GENERAL review
in review-kb.md; their content is unchanged. This is documentation of the
implemented authentication contract, with no new runtime or API behavior.
Overall initiative risk remains high (authentication); this follow-up is
unmanaged-page prose only and selects the GENERAL lane, gpt-5.6-sol/xhigh.

Repositories under `worktrees/2026-09-13-auth-email/`:

- vpsadmin base `791ab3aa89e2f613979da6090b89785c78245db5`; pushed production
  implementation `ddd01f59ca533c030f29b9b8a75984699e5dc581`.
  Local head `1b82f44b88663b9a50e82012c1e77f561b294bc5` changes browser tests and
  their selection only. The production tree is identical. API/WebUI and
  production templates already completed four-lane implementation review.
- vpsfree-kb-contracts base `919577d0c770e47b623c591f8bf0cce4e8d30666`, committed
  and pushed head `4ccc913036b3e904b9a24d2a5808f0ca6170836a`, pinning `ddd01f59c`.
  No new contract-repository change is introduced by the API-page additions.
- vpsfree-notification-templates base
  `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11`, head
  `06f03bad4294b6f28ca9478e907f43967ebeb7d0`, unchanged in this follow-up.

Read these local tracking artifacts:

- `kb-sources/en/manuals/vps/api.txt` and `kb-sources/cs/navody/vps/api.txt`
- `kb-candidates/en/manuals/vps/api.txt` and `kb-candidates/cs/navody/vps/api.txt`
- `kb-annotation-plan.yml` (schema 3, four guarded content replacements)
- `kb-candidates/review.md`
- `kb-release-cs.yml`, `kb-release-en.yml`, `release-changes.yml`
- `kb-impact.md`, `review-kb.md` for prior scope and known annotation drift

These are unmanaged production pages; canonical candidate/release artifacts live
in the coordination initiative, not the contract source repository. The complete
private source/candidate inventories remain ignored. Do not output their bulk
content or credentials. Only the four changed public pages are eligible for the
tracking checkpoint. Guarded construction uses production revision/checksum data.

Acceptance criteria: the guides explain that fresh password-token requests need
an email code when account policy requires it; HTTP Basic rejects without sending
mail; existing tokens remain usable; vpsfreectl handles the continuation; the
unsupported get-token helper in terraform-provider-vpsadmin is explicit and has
a supported issuance replacement. Preserve all unrelated guide content and
machine syntax. Czech additions use informal singular forms. No new WebUI action
is introduced by these API/CLI instructions, so no new navigation path is added.

The main agent applied the installed vpsfree-user-facing-writing skill directly.
Its path overrides the KB repository's stale removed workspace-skills reference.
Do not redo the main rewrite without a concrete finding. No production writes,
new client implementation, broader guide refresh or infrastructure change is in
scope. Production publication still needs direct user approval. The existing
four unrelated all-page annotation mismatches remain recorded in kb-impact.md.

Quick verification: kb-contract-build succeeded for all 191 source pages,
changing exactly the two account pages and two API pages; both schema-5 release
manifests regenerated with informative per-page summaries. Both contract GitHub
workflows passed at 4ccc913 (Check 34834111563, runtime 34834111545). Existing
account-page replacements are unchanged from the previous review.

Write findings to `review-api-docs.md`, ordered Blocking / Important / Advisory,
with concrete source references. If none, say so. Review directly; do not spawn
nested agents. Follow mandatory-change-review/SKILL.md and GENERAL reference.
