# Post-review verification batch

Run only after parent accepts the final independent review. Installed utility:
gpt-6-luna/low, full_access/never, catalog
495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7;
native identity dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96.
Read dev-session-monitor skill and relevant repo AGENTS/procedures. No edits,
diagnosis, retries, deployment, acceptance or nested agents. Stop the batch at
first failure, unexpected local kernel build or changed source. Silence is not
failure. Expected 15-25 minutes total; report overrun at 25 minutes but retain run
ownership. Parent decides continuation. Capture each command stdout JSON separately
from stderr log, exact status, elapsed time, and derivations/output identities.

Workspace group: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-archive-native-watchers.
Tracking directory: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-28-archive-native-watchers.

1. In dev-workspace at db9578e2e195d2a86873e49bcdcfb1cf28bf62d8:
   nix build --json --print-build-logs --out-link TRACKING/roots/runtime-checks
   .#checks.x86_64-linux.package .#checks.x86_64-linux.session-archive-lifecycle
2. In workspace at afc2c144c7cea241b71ff425b5a455a1db060c15:
   nix build --json --print-build-logs --out-link TRACKING/roots/workspace-checks
   .#packages.x86_64-linux.default .#checks.x86_64-linux.deployment-contract
3. In vpsfree-cz-configuration at 2c738ac851f43545272579a96cf836f99876eefb:
   nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev
4. Observe exact GitHub run40713491647 for runtime db9578e2 with gh run watch
   --repo aither64/dev-workspace 40713491647 --exit-status, retaining final JSON
   and failure log if needed. Do not rerun or cancel unrelated workflows.

Use logs under TRACKING/verification/ (disposable untracked artifacts) and return
one compact Markdown report. Build roots protect candidate packages until rollout.
Do not build Linux locally unexpectedly; this is not kernel work. If observed,
stop only this owned build and escalate. Other concurrent sessions remain untouched.
