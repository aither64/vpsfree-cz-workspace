# Aitherdev rollout, 2026-11-12

User approval: "you can deploy aitherdev using vpsfree-cz-configuration. merge after verification".
Scope: aitherdev system and workspace user profile, then remote master integration
of dev-workspace, vpsfree-cz-configuration and workspace. No reboot or archival.

## Prepared source

- Runtime: 02881b401955ff0db71bb74f6fb84f6e475a7879 (base 6587c4c1).
- Configuration: 5dcde1ce5210a42e4499dbf1b6badbd1f0aa326c (base dda57166).
- Workspace: 42c76e8cb61e0d2063a3d25b4b448e66abee523f (base 05ad6ab3).
- Both deployment locks select exactly the runtime revision and NAR identity;
  extension, sibling inputs and native Codex inputs unchanged. Contract checker
  passes. Config hooks pass; generated confctl message width warning retained.
- Config worktree post-checkout initially failed because hook gems were absent.
  The checkout and registration had completed. Entered its declared Nix shell,
  installed and signed hooks, and completed the channel update without bypasses.

## Pre-deployment baseline

System and system profile both resolve to
/nix/store/jyyakgzy8bixrchqj5ycbgb4rgnsvn0n-nixos-system-aitherdev-26.05.20261026.718f670.
Selected workspace package: /nix/store/9hr3ppqzzwb12x51vwjasw8hq0ka7dab-dev-workspace-0.2.0.
Portal PID 3578672; native daemon PID 1309145, started 2026-11-08 15:42:32 CET.
Both active and profile Codex resolve to
/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/bin/codex.
Portal socket /run/user/1000/dev-workspaces/vpsfree-cz/portal.sock.
No maintenance or interrupt flag is planned. Native continuity must be verified.

## Initial execution and interruption

Composition/history review and both builds passed. Copy-only and dry activation
passed. Held machine claim ac205ec4-2d6d-4551-8adb-58e493865e89; exact machine
mapping verified against configuration 5dcde1ce. Generation 2026-11-12--16-28-33
produced /nix/store/1gcqjfy0r9f2b6l6cczn9m30vn54najm-nixos-system-aitherdev-26.05.20261026.718f670.
Composed package: /nix/store/a0nhkz2khja7qp17vw5fh1p8327i10iw-dev-workspace-0.2.0.

The no-reboot switch (parent tool session 82986) changed /run/current-system
before blocking on user-unit reconciliation. At that point system profile and
current-system differed. Foreign terminal-input assignment wrappers held the
transition lock. The original activation was retained until the following
user-directed recovery; no replacement activation was started.

## Recovery at 15:52 UTC

Public access was unavailable while activation waited: nginx had stopped.
Following the user's immediate restoration instruction, verified and terminated
only 32 stuck terminal-input assignment wrappers. Restarted nginx; original
activation completed successfully with auto-rollback still enabled. System and
profile identities match the built output; native daemon unchanged. Normal
workspace profile activation is now running. No manual lock/journal changes.

## Verified deployment

System and profile both match the built 1gcqjfy0r9f2b6l6cczn9m30vn54najm output.
Workspace profile switch exited 0 and selected a0nhkz2khja7qp17vw5fh1p8327i10iw;
new portal PID 3304698, unchanged ordinary native PID 1309145. Naming and ordinary
native model RPCs passed. Public HTTPS and backend health checks passed.

Live Linux review required refreshing the stale multi-pack index (3 indexed
packs versus 29,130 present). A single index-only write succeeded, preserving
all packs/objects/refs. Current 3,223-file comparison now loads in 334.3 ms;
selected NFS content/counts succeed. Evidence and exact range are in state.
Approved master integration and machine release are next.

## Integrated lineage and release

Remote masters now contain the exact deployed feature heads: runtime 02881b40,
configuration 5dcde1ce, workspace 42c76e8cb. Ordinary fast-forward merges and SSH
pushes succeeded with hooks enabled. Repository claims were released after each
remote proof. Machine claim ac205ec4-2d6d-4551-8adb-58e493865e89 was released
at 16:09:26 UTC after effect and lineage verification. Master CI is tracked in
state; existing feature CI and all deployment/live acceptance checks passed.

## Automatic counts follow-up preparation

The user requires automatic additions/deletions in overviews and diff headers.
Prepared runtime 4dd6c757, workspace bf0574e49, configuration f74dd69e.
Initial delivery's full master CI passed all four jobs. Follow-up remains
undeployed pending independent review/package checks. Effective extension and
Codex inputs are unchanged. Keep the built candidate rooted until selection.
Before activation check outstanding transition helpers, backend and public
HTTPS; the previous deployment showed that socket health alone is insufficient.
System/profile activation and release use fresh claims and normal recovery.

## Automatic counts deployment and final preview correction

Runtime 4dd6c757, workspace bf0574e49 and configuration f74dd69e passed review,
package/system verification and feature CI. System zlwdk1fy and user package
chlcbgg2 were activated. First profile activation refused a concurrently changed
repository proof; the same ordinary source switch resumed forward successfully.
Both backend/public health and native/naming RPC continuity were verified.
NFS totals are +349/-4 and +4311/-37; Linux is +61686/-31047 across 3,223 files.

Live acceptance exposed the pre-existing blob preview abbreviation cost. The
full-index correction is included in final runtime db4b0fa6, workspace 3bdad4b13
and configuration 55b83513. Each branch has one consolidated update; deployed
predecessors are retained by local -counts-deployed refs and this record.
Same reviewer approved the final series, with no findings or migrations.
Final build/redeployment/integration remain active as tracked in state.md.
Machine claim faad7680-b349-4d27-8876-e23e5ab55893 stays held through that proof.


## Final deployed lineage and release

The final batch passed in 556 seconds. Generation 2026-11-12--18-56-10 selects
system lgqf1fy2 and workspace package s0g8bym5. Copy/dry/no-reboot activation and
ordinary profile switch all passed. Public/backend health and ordinary/naming
RPCs passed; native PID 1309145 remained unchanged. The unchanged live script
now passes, including the previously failing client.c preview at 814.6 ms.
Linux totals are +61686/-31047; NFS vpsadminos advanced to a new frozen head
with 16 files +4905/-38. Exact pairs/results are in counts-live-verification.json.

Final runtime db4b0fa6, configuration 55b83513 and workspace 3bdad4b13 are proved
on remote master after ordinary fast-forward merges and SSH pushes. Hooks were
retained and shared index/files preserved. All short repository claims were
released. Machine faad7680-b349-4d27-8876-e23e5ab55893 was released at 18:05:38 UTC
following complete effect and integrated-lineage proof. No commands remain
activating the machine; no archival or branch deletion. Final CI is in state.md.


Final feature CI passed all applicable jobs on db4b0fa6. Master fast/package,
host and archive checks passed; its creation job exposed an unchanged fork
settings race. Preserve that failure and the diagnosis in
counts-ci-failure-analysis.md; no retry hid it. All watchers and command sessions
are joined. The repository-review delivery is complete, with the separate
baseline issue explicitly documented. Session remains open and refs retained.
