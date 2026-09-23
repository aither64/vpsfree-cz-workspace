# Team lead delegation rollout — 2026-09-23

The approved change was deployed to aitherdev's user-profile workspace package;
no feature branch was integrated into a default branch.

The first switch used the generic `dev-workspace` worktree and selected
`/nix/store/24khk7g30m929ig8kdkn2rgyrrxwcqk6-dev-workspace-0.2.0`.
Its runtime passed local packaged checks, but it lacked this workspace's
direct-team catalog and cluster providers. The portal service rejected the
site's `.dev-workspace.json` and restarted until the corrected switch; this
is visible in its journal. A full-team canary was refused before
session creation with `this workspace package has no direct team catalog`.

The corrected package was composed through `deployment-wrapper/flake.nix`,
which pins workspace `8fe84327`, site extension `ad13e7fc`, generic runtime
`1b836baf`, and Codex client `01e75798`. Its Nix build passed, including the
generic runtime checks (93 runs, 514 assertions, no failures or errors, three
skips). The package output was inspected for the `delegated` preset, Luna/low
verification utility, and `vpsadmin`/`vpsadminos` cluster providers before
switching. `workspace-host switch --source deployment-wrapper` completed and
selected `/nix/store/n4x37zawjxgh6q5ld6qpp0pmnffrksz3-dev-workspace-0.2.0`.
The profile status reports this package. Since 21:29 local time the portal
service has been active without startup errors; an unauthenticated request
returns HTTP 401, as expected.

The live canary `2026-09-23-lead-policy-canary` started with a full team. Its
roster records ready `architect0`, `implementer0`, and `reviewer0`, each on a
separate `gpt-6-sol`/`xhigh` thread. The root lead queried its live roster,
assigned the read-only design task to `architect0`, received its
`report_to_lead` message, and incorporated the finding in its final answer.
The canary is retained, not archived or deleted. It identified a separate
possible full-team startup issue: specialist model settings are not preflighted
as strictly as the lead setting. This is a read-only follow-up recommendation,
not part of this rollout.

The first dev-workspace GitHub CI attempt failed in an unchanged, tight
transition-lock timing test under parallel package builds. Focused local
repetition passed 20 times. The available GitHub token cannot request a rerun
or dispatch (HTTP 403), so CI is not recorded as green. This does not change
the successful local packaged and site-composed builds.
