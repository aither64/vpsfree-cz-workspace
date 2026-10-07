# Aitherdev rollout

Independent review, current-head CI, packaged checks and host build passed.
Deployment and live verification completed.

## Sources and contract

Generic runtime a2bbf2f1c588de7eec0d7d52580a89a9d4bef984.
Workspace fe6ef13c324500648b2e42b2910dee55c9a2a813.
Configuration cfa61475e57e12d3cc980844dfe00384cca14271.
Extension remains 0ff827df13e82dfab4b536ff29979280f264e8f5.
Host module and application runtime match; deployment contract checker passes.
All feature branches remain unmerged.

Current system before rollout:
/nix/store/gknwlgf8v3lhva6yr1ky8c367fi3sqn2-nixos-system-aitherdev-26.05.20261006.b253099.
Current workspace profile:
/nix/store/y0j44svpcdpqzvjj43n5kg06iqfnxvzv-dev-workspace-0.2.0.

## Prepared operations

1. Observe generic exact-head CI and build all composed workspace checks.
2. Hold composed default package with an initiative-specific Nix out-link.
3. In configuration's Nix environment:
   confctl build --yes cz.vpsfree/machines/aitherdev.
4. Deploy exact host target with dry-activate, then switch using --yes,
   --dry-activate-first and --enable-auto-rollback.
5. Parent launches supported workspace-host switch --source using the exact
   workspace feature worktree, in a named transient user service with complete
   logs and atomic exit status. Fresh watcher observes; it never deploys.
6. Verify installed schema-4 catalog defaults, exact role settings and user
   services. Read authenticated live form and model discovery, including team
   reset, without submitting a session or exposing credentials.

Respect global session/team idle proofs, unfinished lifecycle journals, cluster
ownership and forward-only package transitions. A refusal leaves its evidence
and must be resolved through the existing supported path. Do not interrupt other
sessions or repair their state. Keep previous system generation and all Codex
roots. Workspace recovery repeats the same supported switch or uses a corrected
newer package; no backward profile selection.

## Execution results

Generic CI 37612463997 passed. Composed nix flake check passed in 579 seconds;
package build passed and holds /tmp/lead-review-defaults-package pointing to
/nix/store/yc881ddhy7sr4k2f59jfqwjq6b1wr4p3-dev-workspace-0.2.0.
Host configuration built generation 2026-10-07--13-34-43.

Parent launched lead-review-defaults-deploy.service, guarded by exact source
heads, clean feature worktrees and verified session environment. Atomic stage
status files and complete logs are under this initiative. Fresh Luna/low watcher
verification_deployment observes the existing operation. Host dry-activation and activation passed (both status 0). Workspace profile
switch is running under normal protocol and session quiescence checks.
Profile switch passed; all stage and deployment statuses are 0. Systemd invocation
fa359b9433a343059a03783da8de8ecd finished with JOB_RESULT=done at 13:44:37.601+02:00
(422s), no operation remains. Launch client lost D-Bus connection and returned
nonzero; the independent unit completed and no retry was performed.

Installed profile matches candidate yc881ddhy7sr4k2f59jfqwjq6b1wr4p3. System is
/nix/store/794pz5dv69bkn0vcgr5l52xj9j93dkkz-nixos-system-aitherdev-26.05.20261006.b253099.
Portal/router/Codex/tmux and auto-archive timer active. Schema 4 catalog defaults to
lead_reviewed with Sol/xhigh lead and Astra/xhigh reviewer. TLS-verified authenticated
GET and Chromium checks pass: exact selections survive discovery and reset with
teams, zero empty options/page errors/server mutations. Screenshot captures only
lead settings. Details: installed-package-result.json and live-settings-result.json.
All feature branches remain unmerged; configuration master separately advanced to
b8e92252 with unrelated vpsAdminOS staging input changes.
