# Aitherdev rollout

Authorization in this conversation: "aitherdev can be deployed using
vpsfree-cz-configuration. once deployed and verified, you can merge it".
Deploy first, verify, then integrate dev-workspace and the required workspace
and configuration pins into their master branches. No reboot or lifecycle
cleanup requested.

## Current prepared rollout (November 8)

Exact published source heads are runtime d23a0e302246c2e3929d0856cf62f92eaf7ccea8,
workspace 437f437befffaa790ea44b6bdd496dd06f6a1483 and configuration
830df3f5bfd3816fb754ea2b9b9ebedc8fb8fcf6. These supersede the historical
November 6 preparation below. Fresh fetch confirms no further baseline movement.
Final independent review and narrow R3 remediation are complete. Batch
verify-nov8.sh owns final checks, including CI 42532231977 attempt 1;
configuration build has passed. Native watcher 01a1bd5d-3540-7272-901c-f331c88e689d
is still monitoring, with no deployment authority.

Fresh machine request 8a1702ee-4408-4667-8f09-0f52b90f7f93 is prepared in
machine-claim-nov8.json but has not been acquired. The old waiting claim was
canceled normally. Select the new generation produced by this batch, never the
November 6 build. Preserve Codex and tmux process identity, use ordinary
confctl dry-activate/switch with auto rollback and no reboot, then ordinary
workspace-host profile switch with exact held claim and session environment.

## Historical sources and review (November 6)

- dev-workspace: 59d2fe184742694e23378a57de63ae8241f6b8ef, independently reviewed
  implementation plus verified narrow remediations; CI successful.
- workspace: f5e060e4a2bf0b7f3c7204b2861f4609c3d028c0, based on
  0b25061aafbd328cacc6b7bea5dc558bc8c7f3b4.
- vpsfree-cz-configuration: 50988c8b8bd5f2fd4e13e9892b999ed65ff21da4, based on
  85b38f1cd07d6b3a0fde3eefd32258f747e757e5.

The two deployment commits only replace the generic runtime identity
3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7 with the reviewed final head.
Extension f8da821e3c76e26e73aa9d89a712eab0e0faa319, follows links, Codex and
all sibling inputs are unchanged. Configuration uses the dev-workspace channel's
devWorkspace role. These are mechanical dependency selections, exempt from
standalone content review under mandatory-change-review; each stream has one
commit, with no intermediate pins or new migrations. Existing runtime review and
schema-3 migration lineage remain authoritative.

Configuration Overcommit hooks are installed and passed; generated changelog
retained, including its nonblocking width warning. Workspace declares no hook
framework. Nixfmt reports pre-existing baseline formatting in the workspace
flake; the same check fails on its untouched predecessor, so do not reformat
unrelated content. Whitespace diff checks pass. The deployment-contract checker
passed against both final locks and the canonical portal identity.

## Before deployment

Selected profile: /nix/store/zmyllqw6x1cxk8vhwliy7r11ykd19cz9-dev-workspace-0.2.0.
Both live system and system profile:
/nix/store/pywczl26kl33lacqinr72y6s63k3qfyw-nixos-system-aitherdev-26.05.20261026.718f670.
Portal PID 3387608; Codex PID 1906; tmux PID 1917. All active.

Build exact package and configuration before claiming aitherdev. Compare system
paths, preserving no-reboot switch and confctl auto-rollback if activation is
needed. Select the application through ordinary workspace-host switch with the
exact session identity and held machine claim. Codex is unchanged; preserve its
daemon and running conversations. Verify selected package, runtime capability,
portal health, service identities, and read-only delivery/retry behavior. Use
disposable fixture checks rather than sending to the original livepatch session.

## Recovery and release

After first locked access, new retry records require SQLite-capable software.
Preserve JSON markers, SQLite files, legacy backups and native receipts. Follow
ordinary forward package recovery after an uncertain switch. Never restore stale
legacy state or select an incompatible package. Retain the machine claim through
verified effects and integration of the complete deployed lineage; repository
claims remain separate short merge locks.

## Prepared artifacts and current wait

Configuration generation 2026-11-06--19-32-52 built successfully to
/nix/store/xlbjz1jbyhdk5mxd9pfl6yvq2rxs18ra-nixos-system-aitherdev-26.05.20261026.718f670.
Application f5e060e4 composed output is
/nix/store/rvfzq44dbw4d14adpn9q7ggbdzgrnr93-dev-workspace-0.2.0.
Application build and all workspace flake checks passed; exact runtime CI and
review evidence are unchanged.

No activation has run. Machine request 51c9bb18-85d5-4150-8e88-5176510372a7
is queued behind 2026-11-03-lead-wakeup-delivery's held reservation
5ed5527b-c5b0-42fe-8d2d-53aacf27fd81. Resume only after our claim is held;
use `dev-session coordination claim-status` and `verify-machine` with the exact
session environment. This initiative is threadless and has no native grant
notification destination. Keep the existing queue rather than creating another
request or releasing the other owner's reservation.

Run dry activation and a no-reboot switch of the saved configuration generation
with auto rollback retained, then ordinary workspace-host switch of the workspace
feature worktree under DEV_WORKSPACE_CLAIM_ID. The selected package is still the
old baseline. Live HTTP baseline passed; prepared naming-smoke has not run.
Master integration remains conditional on successful live deployment verification.

## November 8 refreshed rollout

Stale waiting claim canceled through ordinary API; root cause was the 256 KiB
packed-ref aggregate bound, with 933490 bytes/4346 refs in configuration.
Current source includes the streamed reader and a queued-grant regression.
No retained refs or private authority state were removed or edited.

Runtime 849bfdda6e1598b1e169e22bd741079941bb2d60 on master 32a5e31b;
workspace bcee53dd6b0058b1c2f18ce402a40dd42309dfdf on shared master 8aae9bd4;
configuration 2d050cfc26b23dce824e88ee61e83e2e929e7d0d on master 1072f89f.
Final review is refreshed for rebase conflict integration and packed refs.
The old pins were superseded and consolidated; all final feature refs published.
Current installed runtime c8edcb90 differs from master 32a5e31b only in a
creation-browser fixture; no deployed runtime behavior is dropped.

Baseline: selected /nix/store/9yibngx0gbiq17waqffcgszk067ngmhb-dev-workspace-0.2.0;
both system paths /nix/store/kycb055vxzjn9jzz4yyfwbgf673z6q8s-nixos-system-aitherdev-26.05.20261026.718f670.
Portal PID 1475620, Codex 1309145, tmux 1917; maintenance status none.
Native Codex/extension unchanged. Keep newer monitor/maintenance capability.

Verification batch after review: build composed application and configuration,
run workspace flake checks, and local host-idempotency/recovery VM checks omitted
by feature CI. CI 42531660276 covers fast/package, archive and creation on exact
runtime head. Do not duplicate those VM suites locally if exact CI passes.
Expected batch 10-25 minutes; stop on authoritative results, inspect any failure
before rerun. Build reuse requires exact derivation/input evidence.

Final prepared outputs: configuration generation 2026-11-08--23-53-37 selects
/nix/store/wbk0yqmpin2fyhark6pyxymiy4d2m4mm-nixos-system-aitherdev-26.05.20261026.718f670;
application candidate is /nix/store/45f7abhr9kx1adkd6idiz415rhdr9275-dev-workspace-0.2.0.
Application build and workspace checks exited 0. Ruby aggregate has complete
coverage (1,091 tests). CI fast and archive jobs passed; creation and local
host/recovery checks still pending. No activation yet. System closure comparison
shows no package-version changes. Both HTTP baseline paths returned 200; native
Codex/tmux PIDs are unchanged. Naming helper rebuilt against final pinned client.

November 9 fixture follow-up supersedes the preceding prepared source heads:
runtime d2cb9975a88079d79f361c5b4c65836ba0835821,
workspace 69c8165796300a389957979dda2f44fe9b89f959,
configuration 612b3459ec9b81bf24ae078a06da487648675001.
Same reviewer accepted the ten-line test cleanup; product behavior unchanged.
Pins are single consolidated commits and checker passes. New verification is
verify-nov9.sh / CI 42536185097 attempt 1. Use its resulting profile-candidate-nov9
and new configuration generation. No previous prepared artifacts were deployed.

Final batch passed (36m26s; 23:41:33–00:17:59 UTC), including CI creation and
both local host/recovery checks. New system generation 2026-11-09--00-41-59:
/nix/store/xwldgxzayy9113ljd57ib70vwrbksgp0-nixos-system-aitherdev-26.05.20261026.718f670.
Final profile /nix/store/8p7fs26ja6flmlgc886ddfgpprdkhfjy-dev-workspace-0.2.0.
Claim 8a1702ee-4408-4667-8f09-0f52b90f7f93 acquired held at 00:18:35 UTC and mapping
verified. Codex PID 1309145, tmux 1917, portal 1475620 before activation;
maintenance status none. Dry activation exit 0. System switch started with
explicit auto rollback and no reboot; deployment watcher observes logs only.

Live verification succeeded: both system paths xwldgxz, profile 8p7fs26;
confctl systemd/firewall checks passed. HTTP /healthz and own session page 200;
naming helper passed via portal-owned ephemeral socket and cleanup. Codex PID
1309145 and tmux PID 1917 preserved; portal restarted to 4101945. Maintenance
status none, switch exit 0. Final workspace rebase over tracking-only 2d45c4df2
is 6e7d45148, patch-equivalent to deployed 69c816579 and produces the exact same
ks9kg3a1lrs97sk4q6afl4hwlpgn5v1h derivation / 8p7fs26 output. Deployed feature
lineage is equivalent; do not describe 69c816579 as literally merged.

## Final integration and release

Verified remote master heads: dev-workspace d2cb9975, configuration 612b3459,
workspace 6e7d45148. All merges were fast-forward with ordinary SSH pushes.
Shared master/index preserved other work; workspace pin was patch-equivalent and
retained the exact deployed derivation. Separate repository claims released after
remote proof. Machine claim 8a1702ee-4408-4667-8f09-0f52b90f7f93 released normally
at 2026-11-09 00:24:57 UTC (revision 2). No pending or uncertain deployment effects.
Clean temporary merge worktrees removed, feature refs/worktrees retained. Session
complete but not archived, deleted or stopped.
