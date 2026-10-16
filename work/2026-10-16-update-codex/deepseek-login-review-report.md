No Blocking, Important, or Advisory change requests. **The authentication correction passes the affected general and risk review.** Live provider acceptance and deployment verification remain outstanding.

I performed the review directly, without writes, provider calls, deployments, messages, or delegation. Earlier reports cover unchanged architecture/scope lanes and companion repositories. This report supersedes the earlier conclusion that `forced_login_method = "api"` was appropriate for DeepSeek.

The reviewer thread is `01a14598-96f1-7e92-9212-eb4912342792`. Its environment identity matches the launcher receipt, which records `gpt-6-astra` / `xhigh` / `read_only` and matches the installed catalog’s `lead_reviewed/reviewer` policy. Replacement is justified by the recorded “no rollout found” failure for the previous ephemeral reviewer.

| Reviewed item | Exact identity |
| --- | --- |
| Repository | `vpsfree-cz-configuration` |
| Worktree | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-update-codex/vpsfree-cz-configuration` |
| Branch | `2026-10-16-update-codex` |
| Base | `ae98e9dbf05cd3f6b2d0c32255a4cb2d58c3865b` |
| Previously reviewed/deployed head | `9721c331baa47edf3f0c4cbaaa5204889031047e` |
| Final reviewed head | `aed7d5071e24793d7bd811af11ccfa80e6f049d6` |
| Final tree | `c7194671fe0d2ac04eec823edac0d0cb495b711d` |

The worktree was clean at both inspections. The base equals the locally available `origin/master` merge base, and local/remote-tracking feature refs contain the final head. No fetch was performed.

**Authentication conclusion:** removing the restriction is correct. Native [login enforcement](/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source/codex-rs/login/src/auth/manager.rs:1326) checks shared OpenAI credentials and removes conflicting credentials before provider startup. That path performs local deletion without invoking token revocation.

DeepSeek authentication remains intact in the [managed profile](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-update-codex/vpsfree-cz-configuration/cluster/cz.vpsfree/machines/aitherdev/config.nix:85). The wrapper still requires and exports its key. Native provider resolution selects that environment key before shared authentication; a missing or whitespace-only value produces an error rather than falling back to ChatGPT credentials. Endpoint, model, Responses protocol, catalog, and reasoning effort are unchanged.

The synthetic receipt supports the intended regression boundary: the old profile deletes synthetic authentication; the corrected profile preserves its bytes and reaches empty-prompt rejection. I inspected that evidence and the exact native source, but did not rerun startup or provider requests. `git diff --check` passed independently.

The complete configuration branch series is:

| Commit | Purpose |
| --- | --- |
| `8f9b857dfd806d1b47d624d996e10ad0ce81c083` | Host upgrade skill and operations guidance |
| `81ab9fad6778ed1880607997f08cd47d2c06f328` | System llm-agents selection |
| `107255f8ab33c12ebdb4e484ea8b19d2fd792910` | Runtime selection and transitive pins |
| `9721c331baa47edf3f0c4cbaaa5204889031047e` | Invalid profile-key removal and validation guidance |
| `aed7d5071e24793d7bd811af11ccfa80e6f049d6` | Shared-login preservation and authentication guidance |

**Whole-branch history conclusion:** no obsolete approach, redundant update stream, abandoned compatibility path, or required consolidation remains. The schema cleanup removes invalid settings inherited from the base; the authentication correction removes a separate valid setting with harmful semantics. That distinction supports separate reviewable commits independently of deployment history. Each dependency stream changes once; system and runtime llm-agents nodes serve distinct consumers. Lock graph edges remain unchanged.

**Migration conclusion: no application migrations.** The complete series introduces no schema migration, state conversion, or migration guard. There are no migration versions requiring merged/released/deployed/externally-consumed classification. Earlier upstream Codex state-compatibility evidence remains applicable; this correction introduces no state-format change.

The unchanged, clean companion heads match the retained evidence:

- codex-web: `a0561fad8decb794117f8959fa2dd629547c5ba7`
- dev-workspace: `3c57e2eab56c94fec5f456d8067def8717a0d418`
- workspace: `a158608e2baa41696cd2340c82b45460f56d77da`

Residual risks and remaining gates:

- Run the planned isolated strict DeepSeek canary. Synthetic empty-prompt startup does not prove provider authentication or response compatibility.
- Build and activate the exact final configuration, then verify installed profile loading and shared-auth preservation. Earlier deployment receipts do not certify this head.
- A private working directory alone does not isolate `CODEX_HOME`; apply the skill’s explicit isolation requirement to source/provider probes.
- Restoring an earlier deployed profile can restore the destructive login restriction. Account for that before using `codex-ds` against shared ChatGPT credentials after rollback.

Review is complete. No merge or reboot approval is implied.