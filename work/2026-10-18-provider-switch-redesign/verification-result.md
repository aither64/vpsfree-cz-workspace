# Provider redesign verification

Current candidate uses stock Codex: dev-workspace
2b96a3f44569fd9f5e5bba01e1c2c94a3f2a8fe8 on upstream 7053012;
codex-web c064ce09cfcea8d8af6bf676635a53cd823f772c on upstream 56ec377.
No downstream native patch or build override remains. Temporary subagents may
stop during native tree teardown, as explicitly accepted by the user.

## Current evidence

- Focused stock worker recovery tests: pass (~1.44s), including native shutdown
  failing before the archive marker moves and a goal finishing before a new
  ordinary turn is interrupted. Nine fault/goal combinations; repeated
  continuation keeps its durable identity.
- Exact stock-native integration passed: switch phase 2.6135s, full test 4.042s.
  It proves saved retained roster, idle member, stopped old v2 child/readable
  history, identity-bound new-child target inference, per-retained-thread HTTP
  routing, queues/goals, idle/unrelated continuity and stable policies.
- Eleven provider browser contracts: pass (~0.31s).
- Rebased shared client routing/settings tests: pass (0.08s / 0.02s).
- Dependency pin consistency and whitespace: pass.
- Rebased shared-client exact-head CI: success:
  https://github.com/aither64/codex-web/actions/runs/39142745669
- Native assembly code/tests/docs are identical to upstream. Exact existing
  binary SHA256 5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5:
  /nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/libexec/codex/bin/codex
- Final same-identity review completed all four lanes with no Blocking or
  Important findings. Its Advisory child-ID assertion and the subsequent saved
  fixture-policy correction were applied and directly verified without changing
  production code. Final application CI passed (fast/package 9m15s; archive/recovery/revival VM 10m06s; host job skipped under feature-branch policy):
  https://github.com/aither64/dev-workspace/actions/runs/39143904845
  No deployment or integration claim.

## Earlier stock prototype

These results covered 2bfc504 (dev-workspace) and 9e53d02 (codex-web), not the
final current candidate. Native four-root test passed in ~1.62s/full 2.73s;
actual Playwright creation settings/draft/recovery passed in 9.47s; focused host
provider/creation checks passed 23 runs/230 assertions. Native goal/queue/idle/
unrelated continuity was proved without real model inference or subscriptions.
It did not include the final retained roster or accepted child-interruption
policy. Earlier final application CI succeeded:
https://github.com/aither64/dev-workspace/actions/runs/39133675250
Fast/package 8m34s, packaged archive/recovery/revival VM 8m41s; host job skipped
under its declared feature-branch policy. Old shared CI:
https://github.com/aither64/codex-web/actions/runs/39123540992

Native timing excludes provider authentication/health and terminal quiescing.
Normal native interruption may cancel tools/dialogs and unsampled buffers.
Saved histories and durable native queues retain their persistence guarantees;
interrupted temporary tasks may need reassignment. No lossless hot-migration
claim is made. No custom native build completed or was activated.

No live provider switch, package activation, deployment, shared service restart
or default-branch integration occurred. Keep the initiative active. Detailed
failures, review decisions and old revisions: implementation-history.md and
per-run logs/statuses. Current phase and next action: state.md.
