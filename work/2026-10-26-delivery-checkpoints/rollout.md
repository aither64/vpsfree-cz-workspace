# Aitherdev delivery-checkpoint rollout

User authorization: “so deploy aitherdev”. Application-only activation through
workspace-host switch using the reviewed workspace feature checkout. No system
rebuild, reboot, provider switch or native Codex change.

Runtime: `f8b94441a6b5066973a72284955b793b301c60ac`.
Workspace: `a192857356598e18b26075095cf59d2650bed925`.
Configuration: `45334601b2da0a5aec7f2310fe112f54d29a4059`; one generated confctl pin commit, hooks passed, published.
Composed lock matcher passed. Build/review evidence remains in build-report.md
and review-disposition.md; no repetition of those completed checks.
Candidate: `/nix/store/jgj93dxy9g8clzyxfx0gihlbvvz1pyd4-dev-workspace-0.2.0`.

Baseline is recorded in deployment-before.json. Verify selected package, portal
health, accessible session conversations and unchanged native PID/executable/argv
and system identity. Do not wake idle sessions for testing. Package recovery is
forward-only through the ordinary guarded switch with a compatible corrected
package; keep roots and journals. Retain the machine claim until verified effects
and complete deployed lineage integration under the installed retention policy.

Machine claim `aa2de87b-2f1f-46f0-8626-31d4f0828adb` is held.
The ordinary switch started on 2026-10-26 at 16:44 UTC. Its Nix preparation
found the earlier package output absent from the store and is rebuilding
prerequisites; the original command remains the sole activation owner.
No extra verification campaign or duplicate build was launched. Parent monitors
the original shell handle because it owns the switch completion status.
Configuration comparison captured at `45334601b2da0a5aec7f2310fe112f54d29a4059`.

## Result

Activation completed with exit 0. Verified at 2026-10-26T16:55:31.846703+00:00.
Selected package exactly matches the reviewed candidate. Portal and router
Unix-socket health returned `{"ok":true}`. The retained session UI conversation
returned HTTP 200 with its original thread ID (227 entries at observation).
Native Codex PID 3387667, executable and argv hash, native selection, live
system and system profile match the baseline. Portal and Codex units are active.
The current portal-owned naming child accepts socket connections. No inference
or manual progress check was requested. A direct HTTPS curl lacked the internal
CA in its trust bundle; the router was verified through its configured socket.

The package prerequisite Ruby shard passed: 129 runs, 2438 assertions, zero
failures/errors, two skips. Build and compatibility checks completed as part of
the original successful switch; no additional verification campaign was added.
Deployment output: deployment.log. Compact baseline/result: deployment-before.json
and deployment-after.json. Source heads above remain the deployed lineage.

Claim aa2de87b-2f1f-46f0-8626-31d4f0828adb was rechecked as held. Keep it held
until all deployed lineage is integrated into approved remote default branches.
No merge was authorized by this deployment request. All commands have ended;
there are no uncertain activation effects.

## Integration and release

User subsequently directed “ok, merge and release”. Remote master proofs:

- dev-workspace: `f8b94441a6b5066973a72284955b793b301c60ac`.
- vpsfree-cz-configuration: `45334601b2da0a5aec7f2310fe112f54d29a4059`.
- workspace: `60515c5340eb1488203bd630c671a3e51595e4ff`.

Workspace is the independently proved equivalent successor of deployed a192857;
see integration-review.md for exact ranges and complete tree reconstruction.
All source pins remain the deployed identities. This is equivalent deployed
lineage, not a claim that a192857 itself is an ancestor of master.
All merges were fast-forward-only with ordinary hooks and SSH pushes.
Repository claims were released immediately after remote proof. The selected
package remained unchanged. Aitherdev claim aa2de87b-2f1f-46f0-8626-31d4f0828adb
was released and rechecked as released at 2026-10-26T17:05:12Z. No uncertainty
or unfinished mutation remains.
