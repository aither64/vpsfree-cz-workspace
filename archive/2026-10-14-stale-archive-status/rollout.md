# Stale archive display rollout

Both original coordinated deployment jobs succeeded. Live acceptance passed;
reservation finish is the only remaining operation. Detailed verification is in
[acceptance.md](acceptance.md) and [verification.md](verification.md).

The user explicitly approved “Merge all three to master and continue deployment”
for dev-workspace, workspace and vpsfree-cz-configuration, each master, followed by
aitherdev deployment without CI waiting. Actual scope/wording are retained in
`coordination/user-authorization.json`. Runtime ad63a832, workspace cf5fac85 and
configuration 5cd53c69 first merged through coordinated jobs. Feature refs remain.

While the recovery-banner session held aitherdev for review, it integrated its
notice dismissal on top of our fix. All three own clean branches were then
fast-forwarded and published normally to already integrated defaults: runtime
92b2576d82a850fa4e24f889a8ff592a1e7f3e42, workspace
5a2119d4774719f78c1b72059cf0f8f10068374a and configuration
ac00192849f682eed847a152a91978a399f0105e. No new commit or merged-history rewrite
was needed. Both consumers select 92b2576d, preserving all other inputs/follows.
The same independent reviewer checked affected General/Risk concerns and found
no issues. Exact browser/application/system checks passed in 76s/22s/103s.

Built and deployed application:
`/nix/store/13s6kwhliihnnby7rxym6wsbafv6cxh6-dev-workspace-0.2.0`.
Built and deployed current system/system profile:
`/nix/store/xf0i8ryhpx575282m5hlq2vavq56vms8-nixos-system-aitherdev-26.05.20261012.7993f34`.
Our initial exact configuration generation was `2026-10-14--20-46-22`.
The other session had already selected these combined artifacts before it
released its reservation. We verified the original archive display then, with
zero mutation requests, and retained the original queued jobs for completion.

Own reservation `fb55bbd2-b9ac-487b-816d-7726a6ae7135` was granted afterward.
The original system attempt `46436aa9-3c14-4d22-9bc7-e02ed1e87580` returned
baseline_changed because its prepared catalog was superseded. It made no changes
and had no uncertain effect. Fresh preparations under current package 13s6kwh
passed in 95.7s/10.7s. System snapshot:
`sha256:1adb7619ad0e9895e9e1033a73a92e09588f6b5ee7d0e7055cbaabad140b3db2`;
profile snapshot:
`sha256:a8f9c5898cd5e46ff7171652c0de45d02b9ef934af0cea9154037117d6ad36ef`.
Both were approved under the existing actual user instruction. Temporary
admission conflicts were retried with the exact same request UUID/payload.
The original profile job was refreshed first, then the original system job;
dependencies and ownership were preserved, without new deployment jobs.

System job `6fb947c6-991b-4bcb-842b-4529292ac83f` succeeded/applied on attempt
`016c3f05-1df4-489e-a895-038780e16e42`. Profile job
`5d30cd46-bb35-4a49-b40a-2e777d99b968` succeeded/applied on attempt
`36f43c21-a51a-426d-922f-8319e13e74eb`. The reservation remains deployed_review
at revision 4 pending finish. All 13 notifications were delivered at acceptance.
System and application identities match the exact combined builds. Native Codex
and tmux processes/sockets remained; the portal restarted. No reboot, direct
deployment, forced release, foreign session mutation or CI wait occurred.

The original archive and recovery contents remain untouched. The final live
GET-only probe shows exactly one stale-page reload, no pending marker, hidden
Retry/Archive controls and zero mutation requests in Chromium and Firefox. The
authoritative list independently shows the session archived with no pending
lifecycle. Finish the owned reservation after fresh exact final-head proofs and
settled deliveries. Existing old tabs need one refresh to load the new client.


Finish completed successfully under request 969f44e4-d026-43bc-aa64-1c92df992267.
The owned reservation is released at revision 5 after exact integration and live
identity proofs. Final status revision 448 shows all five original jobs succeeded
and all 14 notifications delivered. No remaining work or blockers. Sources,
branches, private recovery and the current session remain available.
