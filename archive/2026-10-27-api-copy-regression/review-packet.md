# Final source review

User scope evolved from explanation to applying/reworking the supplied TypeScript fix, then explicitly requiring performance tests for all client examples. User authorizes after verification: HaveAPI master integration, all-new-commit backport to haveapi-0.31 and 0.31.1 publication. No deployment or session lifecycle action.

Session: 2026-10-27-api-copy-regression. See plan.md, design.md, findings.md and state.md here. Source worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-copy-regression/haveapi.

## Complete series and history inventory

Base: 4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c.
Head: 8ea2c365a430c931afcde3e161178bf71cee928d.

1. 2ff8931bf266037d2d0cbca8655491043c105e35 — clients/typescript: bound documentation normalization work.
2. 8ea2c365a430c931afcde3e161178bf71cee928d — servers/ruby: cover all example clients in performance tests.

Complete final diff: 13 files, 624 insertions/16 deletions. Separate production adapter fix/direct tests and all-client coverage commits; no superseded approaches or follow-up fix commits remain. No migrations, schemas, generated artifacts, dependency/pin updates, repeated update streams or deployed intermediate source versions. Source has not been published/deployed/integrated yet. Tree and index clean; diff check passes. Assess full history and explicit no-migrations/repeated-stream conclusion independently.

## Acceptance and boundaries

- Remove per-render full-description normalization; select action/provider/metadata before recursive normalization. Preserve aliases, mixed string/symbol collision semantics, chosen-provider equality, token checks, output/limitations, frozen inputs and authorization isolation. No request caching.
- Every one of 15 current registered renderer/mode IDs has direct init/basic/token/oauth2/public/protected/failed-action scenarios and output/work/allocation assertions. Unsupported authentication is explicit, not used to replace successful action coverage.
- Full Rack pages enable actual Go/Rust/TypeScript profiles and check all panels/code and admin/member/admin isolation. Allocation slope at 2/4/8 resources must catch original bug.
- Exact registry matrix and all-client CI relevance prevent silent omissions. Missing profiles/dependencies fail. Required new contract result precedes historical paired timing.
- Existing fixed-reference timing suite is preserved: old baseline predates generated TypeScript. New current-source deterministic contract is not represented as historical wall/CPU comparison. No new baseline/replay framework or calibration/budget changes.
- No wire/API/public SDK naming/state compatibility change; Ruby server invokes generator adapters for optional documentation profiles. No consumer pins or deployments in this scope; rollback code/packages only. Go production renderer unchanged, investigation found no analogous copying.

Owning component is HaveAPI's Ruby-based TypeScript documentation adapter; consumer is the Ruby server's generated TypeScript renderer via configured documentation profile. Live authorized request description is a separate authority from frozen private SDK model. Public interfaces remain unchanged. Existing Go/Rust and dynamic renderers are exercised by new coverage, not rewritten.

Docs changed: clients/typescript/docs/documentation.md, doc/performance.md, doc/client-examples.md, doc/agent-instructions/development.md. Main agent checked final prose and technical claims. Current-source shell/dependency setup and exact coverage are documented; existing release/recovery procedure unchanged. Individual release prep lives only in this session.

## Quick checks and sensitivity

- TypeScript original adapter: all 5 focused work tests fail meaningfully. Action/alias recursive calls 3,222→155,997 with unrelated subtree growth 1→64; Basic 616→31,171. Fixed 16 behavior/work examples pass; changed Ruby lint passes. /tmp/2026-10-27-api-copy-regression-typescript-{red,green,lint,commit}.log.
- All-client final contract: 108 examples pass in 26.86s. all-client-final-quick.log/.exit.
- Routing/gate specs: 54 pass in 1.49s. all-client-routing.log.
- Original adapter loaded in isolated subprocess, committed adapter untouched: 8 selected cases yield 7 actual assertion failures; init passes as expected. Protected allocations 10,177→389,057, Ruby calls 4,440→173,400 while selected output fixed. all-client-original-red.log/.exit.
- Original full-page allocations (2/4/8 resources) 319,335/704,201/1,815,492 fail increment bound (1,111,291 > 962,165). Fixed 219,487/395,601/748,550 pass ratio 2.004 < 2.5.
- Changed four-file coverage Ruby lint, diff check and mandatory pre-commit/commit-message hooks pass. No long integration/CI run started yet.
- Fixture adjustment: supported string token query parameter makes live and JSON saved Go metadata agree; no Go product change. Unsupported RSpec wrapper option removed before actual check. Neither was treated as a product regression proof.

## Review selection

Risk high conservatively: authorization-filtered description selection and authentication metadata behavior touched, despite compatible performance-only intent. Lanes: general; architecture/repetition; scope/proportionality; risk/compatibility. Read all corresponding references under mandatory-change-review.

Selected eligible independent retained reviewer0: gpt-6.1-sol/xhigh, read_only, ready; native thread 01a17f20-d25a-7471-955a-26b36a5c3e75. No model/effort override. This is final committed review after quick checks, before longer integration. Review yourself, no nested reviewer. Report findings by severity, explicit whole-branch history/migration conclusions, residual gaps and exact reviewed range. Do not edit.
