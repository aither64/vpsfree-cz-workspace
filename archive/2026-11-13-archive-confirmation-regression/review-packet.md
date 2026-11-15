# Final committed-deliverable review packet

2026-11-15; owner lead, independent reviewer reviewer0. User requested the provider-helper fix, aitherdev deployment via configuration as appropriate, and merge after verification. Existing Archive retry behavior is accepted and outside the implementation. Read plan/state and design.md G/H for scope, not as a substitute for independent source inspection.

## Readiness and selected lanes

All intended G/H changes are committed and published. Quick checks pass; feature worktrees are clean. No long local integration/package/build check or deployment has started. The automatically push-triggered GitHub Check run is being read-only observed separately.

Risk: high, because provider transition tooling validates persistent native identities before thread close/reopen and this delivery includes runtime selection/deployment. No schema/protocol/state format change is intended. Review all four lanes: general, architecture/repetition, scope/proportionality, risk/compatibility. Use mandatory-change-review/SKILL.md and each corresponding reference. Saved eligible independent member: reviewer0, gpt-6.1-sol/xhigh/read_only; no model/effort override or fallback. Perform review directly, no nested reviewers.

## Exact full ranges and final diff

All worktrees below are under `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-archive-confirmation-regression/`; branch in each is `2026-11-13-archive-confirmation-regression`.

| Repository / worktree | Full base | Full final head | Complete series / diff |
| --- | --- | --- | --- |
| dev-workspace / dev-workspace | 458c7857b942fb592607c83af7b5287a6c93ea96 | e96284d1a0484a01888a6d7166fcbd5f68855659 | One commit, provider: preserve native utility proof inputs; four files, +216/-12 |
| workspace / workspace | aa9333916fdc1062755a88e1b8298b845ec2ccc4 | da432f0a2928bf296c497ec66a282e4ee61af960 | One commit, inputs: select provider helper proof fix; flake.nix and flake.lock, +5/-5 |
| vpsfree-cz-configuration / vpsfree-cz-configuration | 11ef63c5e173019b5312d672570158a0b0fb6dad | 9f7679c90bb3c7dc2070a611685e631a25e06a51 | One generated commit, inputs: set devWorkspace to e96284d1; flake.lock, +3/-3 |

Inspect the entire series and final diff of all three, not only their latest files. One functional change plus one matching mechanical runtime pin per consumer is the intended split. Tests stay with their behavior. There are no obsolete approaches/fixup commits, repeated pin streams, transitional compatibility paths or migrations reported; verify and explicitly conclude on whole-branch history, repeated-update consolidation and no migrations. None of these feature commits has been merged, deployed, released or externally consumed except publication of branches for the pins. No earlier independent review is being reused.

## Functional contract and boundaries

The raw provider SDK client deliberately has no implicit resume, ordinary provider resolver, watches or automatic question answering. Its composition must include the workspace's vscode source policy so valid headless utility provenance can pass. The scoped Ruby helper must receive the existing registered-workspace Codex environment so archive proof has canonical home. Preserve all source/origin/CWD/ephemeral/history/bootstrap/archive checks; active lead/member threads remain eligible. Do not replace the raw client wholesale, weaken validation, add an idle restriction, change RetryStore/recovery, alter Archive confirmation, introduce diagnostics infrastructure or migrate state.

The small factory extraction permits tests to exercise the actual production composition. New Go regression covers real scoped inventory with a retained monitor and independent source/home/provenance negatives; Ruby regression invokes actual scoped subprocess boundary rather than overriding the method. Review their adequacy and scope independently. Native working-turn acceptance still needs the post-review disposable check; a metadata status alone does not prove a working turn.

## Inputs and consumers

Owning fix: reusable dev-workspace provider helper. Consumers: workspace composition through direct nested `vpsfree-dev-workspace/dev-workspace`, and configuration channel `dev-workspace` role/input `devWorkspace`. Both final locks select e96284d1 with narHash `sha256-7J2yBTO+gdq+B1bl9HWyPHOjaXXQKbjDbkKNviR8AT8=`.

Extension remains d76bd681c6db981907a52c187a3298549af87ab0. Full graph comparison reports identical node sets, edges/follows and every other locked identity; codex-web remains91a17d00a737d59a91b5e7bb420aa89e7ec52d93, llm-agents remains91ff550fe42d4dd51dcf8b6bad87a0134fe7f314, native Codex remains0.165.0. Verify exact graph/diff evidence in h-evidence.md. No public API or cross-project contract expansion.

## Quick checks and packet links

- [implementation.md](implementation.md): exact G files, commands, clean/published range, hook status, compatibility and history. Nix-shell focused Go TestProvider/TestScopedProvider PASS1.648s; Ruby provider_sessions PASS12runs/80assertions/0failures1.373s; formatting/diff checks clean. No declared hook framework/custom hooks; no bypass.
- [h-evidence.md](h-evidence.md): exact pin commands/ranges/graph proof. Parity checker against both exact roots PASS0.19s, semantic graphs, Nix parse/whitespace, configuration channel/selector inventory pass. Configuration Nixfmt/commit hooks pass; generated confctl message retained. Workspace has no root hook framework.
- [design.md](design.md): sufficient G/H briefs, supported active flow and deployment/recovery decisions.
- [provider-reproduction.md](provider-reproduction.md): generic earlier causal evidence, not a substitute for review or post-fix integration. Incident-specific sensitive operational metadata is deliberately omitted; do not access the affected session or private logs.

## Documentation routing and preservation

| Topic | Reader / class | Authoritative home | Evidence / disposition |
| --- | --- | --- | --- |
| Raw client no-resume/no-routing and required source policy | runtime maintainers / reference rationale | changed comment beside providerCodexClient | Owning code boundary; no new subsystem or duplicated documentation |
| Provider selection, native transition, state/recovery | operators/maintainers / reference and operations | dev-workspace docs/codex-providers.md, linked from README | Already describes restored contracts; implementer assessed no prose change needed |
| Matching runtime channel/user-profile versus host selection | site operators / reusable operations | configuration docs/operations/codex-providers-aitherdev.md and workspace deployment procedure | Existing contract; routine generated pins require no product-doc or configuration receipt commit |
| Individual review/build/deploy/lineage | this initiative / execution | shared tracking review-packet.md, state.md and forthcoming rollout.md | Keep exact receipts outside reusable docs/config repo |

Independently conclude on placement/preservation and any missing explanation; do not require cosmetic documentation expansion.

## Verification and deployment still pending

After review: isolated exact-native idle/working scoped-prepare with a valid retained monitor; required package/session-creation/session-archive-lifecycle checks; composed application and exact aitherdev configuration builds. User-profile application activation is required; system activation is only needed if the exact built generation differs for relevant reviewed reasons. Builds/copies precede machine reservation. Preserve accepted operations, sensitive state, runtime/cluster/claim package contracts and forward-only recovery. No live provider switch or session lifecycle operation is silently authorized.

User explicitly authorizes merge after verification. Lead owns separate short claims for approved dev-workspace/master, workspace/master and configuration/master integrations; shared workspace integration also takes the nonblocking tracking lock. Machine held only near activation, retained through verified deployment and full integrated lineage, then explicitly released. No claim is held during this review.

Report findings with severity/file/line and lane, explicit history/migration/repeated-pin and documentation conclusions, residual risks and tested gaps. Save review.md in this tracking directory and report_to_lead with stable ID. Remain read-only.
