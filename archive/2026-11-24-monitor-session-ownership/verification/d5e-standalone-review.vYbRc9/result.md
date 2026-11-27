**D5e: no Blocking or Important findings. One Advisory finding:**

- [pi_creation_discard.go:593](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-24-monitor-session-ownership/dev-workspace-discard-bridge/portal/internal/web/pi_creation_discard.go:593) still says a “confirmed POST” may unlink the marker. Describe the revalidated startup grant instead. The implementation correctly exposes no HTTP discard action.

Reviewed General, Architecture, Scope and Risk across the complete committed ranges:

| Range | Final head |
|---|---|
| H: `e3102d0b…` → | `9044ec0d0eaa558d207bca632702dc82f342a670` |
| K: `6bb0b605…` → | `5ba7a17176f81835f49da014b33fedcc4effabb3` |

Session identity and both binding variables matched exactly.

The fixed root-only publisher and reader agree on the bounded grant, ownership and permissions. The selected portal rechecks its generation, managed parent/service and native typed claim before entering the transaction. Startup precedes ordinary creation loading and workers. Completion requires the audit and terminal mapping before marker cleanup; completed replay avoids retiring a later owner’s selectors. The implementation remains bounded to the requested repair.

Both ranges contain one coherent commit. No obsolete implementation history or repeated update streams remain. **No migrations**: pending/audit/grant records are additive bridge state; completion uses the existing terminal mapping format.

Documentation placement and fidelity are sound apart from the comment: preparation behavior belongs in [session-preparations.md:520](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-24-monitor-session-ownership/dev-workspace-discard-bridge/docs/session-preparations.md:520), transition/recovery guidance in [workspace-updates.md:317](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-24-monitor-session-ownership/dev-workspace-discard-bridge/docs/workspace-updates.md:317), and individual execution records in the session.

I independently confirmed that K’s patch equals the complete O→H diff and its dependency graph preserves W0. Reported Go/Ruby, publisher and source-projection checks remain supplied evidence; I did not rerun compilation. Final source/package outputs were unavailable locally.

**Actual guest evidence remains required:** completed O→B selection and old-process join; real root publication and native managed-service verification; refusal/recovery and later-owner isolation; confirmed cleanup and privileged retirement; then unchanged T consuming B’s actual result with zero Pi Start/Create/Send.

**F5 separately completed:** `2f470c0f…→ed66ec29f58fd177fd9ba441cdd36e46bd0a494c` contains one generated pin commit, with no findings, repeated streams or migrations. D→F5 feature equivalence is supported by matching runtime dependency graphs, codex-web identity and unchanged machine/site configuration. This conclusion covers feature lineage only.

- Review complete; Advisory correction and guest verification remain.
- No merge or deployment clearance.
- [Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-24-monitor-session-ownership/)