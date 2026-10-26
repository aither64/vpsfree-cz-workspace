# Archive permission repair deployment

Deploy the reviewed archive permission repair to aitherdev using
vpsfree-cz-configuration and the workspace user profile; verify effects, then
merge the runtime and both selection pins into their remote master branches and
release resource ownership. User authorization: “deploy aitherdev using
vpsfree-cz-configuration. when verified, merge and release.” The later response
“you can track this session” authorizes tracking from this deployment onward.
Earlier implementation intentionally had no tracking.

The runtime adds temporary owner-write permission to owned readable/searchable
directories during verified archive cleanup, never following symlinks or
changing files, shared parents, or canonical repositories. Surviving directories
regain their original modes; legacy recovery retains its integrity checks.
No public API, state schema, protocol, dependency or migration changes.

Affected repositories are dev-workspace (runtime), workspace (composed profile
selection), and vpsfree-cz-configuration (matching host-module selection).
Keep extension, Codex and all sibling pins unchanged. Activate the exact confctl
generation, then switch the workspace user profile under the machine claim.
Use ordinary package compatibility/journal guards and forward recovery; never
edit receipts or bypass lifecycle refusals. System recovery uses confctl's
retained generation. The original failed session archive is outside this rollout.

Acceptance: existing quick checks, independent review and GitHub CI pass; both
candidate builds and lock contract pass; live system/profile identities, portal
health and conversation service continuity are verified; cleanup smoke checks
use disposable data. Merge all three exact final heads fast-forward-only, with
short separate repository claims, before releasing aitherdev. Retain branches.

Documentation: runtime docs/session-archive-recovery.md describes behavior;
workspace docs/agent-instructions/deployment.md and docs/coordination.md own
rollout procedure. Configuration routine pin updates need no new feature docs.
