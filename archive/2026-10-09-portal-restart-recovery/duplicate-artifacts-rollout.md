# Duplicate artifact handling rollout

Status: deployed and verified without reboot. User approved implementation/deployment of the
reiterated plan; aitherdev must not reboot. Default branch merges are unapproved.

Selected runtime a756b2c6a3ec30efaf5fd25dccf1717c21a8efa8, composition
be09a8866026fe1464814a50dd693e96e3d8ca80, configuration
875420e068aafb6fed9f7067a1cd3e8100ef5ef7. Provider c9878454 and native Codex
0.160.0/extension0ff827df are unchanged. Previous deployment is in rollout.md.

The prepared sequence required independent review and packaged/browser/configuration/
CI checks, then configuration deployment from its feature checkout with
--dry-activate-first --no-reboot, followed by the stable workspace-host switch
--source on the composition checkout. Fresh Luna/low utilities observed long waits;
main owned invocation.

The verification plan required a fresh system/profile/boot/service baseline,
actual profile output, healthz, owned and affected pages, enabled services,
lingering, unchanged boot/native/tmux identity and manifest hash. The duplicate
needed one catalog link retaining its first label and a working download. Read-only
conversation access needed the exact retained root. Send/Continue and foreign
tracking edits were excluded. Recovery preparation used the same reviewed forward
switch with durable receipt/hold state retained.

## Captured baseline

Boot ID 0104034e-3a15-4772-aa62-aac7ee4ff6ef. Native Codex PID 1204139, tmux
435397, portal 1415774, router 1415614. Selected system
/nix/store/kxscawff631f111i9blaiwbjpvv9h9g6-nixos-system-aitherdev-26.05.20261008.7c8764b;
profile /nix/store/wgbyyyivgza0i1y4wpk8d0hn8c0pd8fj-dev-workspace-0.2.0.
Affected manifest SHA-256
ac058185886e7ea9ce5ba0bfdb7c512578927ed8c78abc3b962e81d170f8c50f.

The parent prepared exact-head-guarded configuration/profile commands and a
post-switch health script. Deployment invocation belongs to the parent; fresh
utility watchers observe accessible logs/status.

## Pre-deployment verification

Independent whole-branch review: no findings in all four lanes; exact final heads
and consolidated pin streams accepted, no migrations. Corrected check batch exit
0 after 1,048s. Both generic/composed outputs passed: Ruby session 405 runs/5463
assertions/12 skips; auto-archive 12/50/0 skips; host 127/994/3 skips, all with zero
failures/errors. Packaged Go checks passed. The unchanged original duplicate
manifest validated successfully. All seven browser checks passed in 160.20s;
localhost certificate diagnostics did not fail them. Aitherdev build generation
2026-10-10--09-13-27 passed. Runtime CI 38032042779 passed at a756b2c6; host job
skipped, with unchanged original VM/native evidence retained.

Fresh pre-deployment check confirmed the captured boot/profile/native/tmux and
manifest baseline still matches. Parent started configuration deployment using
`nix develop --command confctl deploy --yes --no-interactive --dry-activate-first
--no-reboot cz.vpsfree/machines/aitherdev switch` at configuration 875420e0.
Configuration deployment exited 0 and activated generation 2026-10-10--09-13-27.
SystemState=running and firewall.service ActiveState=active, 2 checks passed/0
failed. The parent then started the stable workspace-host switch --source at
composition be09a886. Application switch exited 0, selected user-profile generation
104, and reported protocol compatibility with unchanged Codex 0.160.0.

## Actual deployment and health result

Selected system:
/nix/store/dmzm997gh7smblm2c1dlrcfsqwbr1mjq-nixos-system-aitherdev-26.05.20261008.7c8764b.
Selected application:
/nix/store/s2zxa731kh87li7syxi3qzjzw3wcp9zd-dev-workspace-0.2.0.
Exact deployed source heads are the runtime/composition/configuration listed
above. No default branch integration occurred.

Post-switch health script exited 0. Recovery and live-switch policies remain 1;
all four user services are active/enabled and lingering is on. healthz returns
ok. Owned and affected session pages return HTTP 200. The affected thread API
returns HTTP 200 and the exact retained manifest thread identity. Its repeated
artifact appears once with the first label and downloads with HTTP 200. HTTPS
still requires authentication (unauthenticated HTTP 401).

Affected manifest SHA-256 remains
ac058185886e7ea9ce5ba0bfdb7c512578927ed8c78abc3b962e81d170f8c50f, with both original
declarations retained. Boot ID remains 0104034e-3a15-4772-aa62-aac7ee4ff6ef.
Codex PID 1204139 and tmux PID 435397 are unchanged; portal/router refreshed to
3094612/3094571. No Send/Continue, foreign tracking edit or host/native/tmux restart
was performed. Retain the forward package and feature refs; the initiative stays
active, ready for use and awaiting merge approval. Original VM/native fixture
limits remain documented in the independent reviews.
