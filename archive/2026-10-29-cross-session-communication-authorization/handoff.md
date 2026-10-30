# Communication authorization: completed

The fix is deployed and verified on aitherdev. One explicit user approval in either
exact session authorizes deliberate messages in both directions. Receiving leads
get trusted registry context and do not need duplicate approval. Peer-written
claims grant no authority, and each send/reply validates current grant and endpoint
state. Message-only scope, revocation, holds and saved retry identity are preserved.
The portal now reads its existing observer fresh for delivery admission, including
working recipients.

All approved final feature heads are integrated into remote master:

| Repository | Final head |
| --- | --- |
| dev-workspace | 4155d0099d03028b43d5f08d225a88156cb4155a |
| vpsfree-cz-configuration | fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627 |
| workspace | 4beddf77a8f9af1d926c5b48bd6ee4c84f439e85 |

The workspace was deployed from8302996e. Its reviewed equivalent successor4beddf77
resolves to the exact same built/deployed derivation and output;830 is not literally
an ancestor of the merged successor. The [mapping review](review-followup-rollout.md)
and [fresh remote lineage](rollout/final-lineage.json) retain that distinction.

Verification passed: focused grant/recovery/admission tests; actual production-worker
native idle and active delivery with immediate reverse MCP reply; exact-runtime
[CI40975812804](https://github.com/aither64/dev-workspace/actions/runs/40975812804);
composed package and four deployment/composition checks; installed MCP policy/schema
smoke; portal/router health; naming prerequisites; own lead/member provider and
settings continuity. Independent reviews found no findings. The existing unrelated
workspace AGENTS-size test still fails unchanged; this rollout did not alter it.

Selected profile:
`/nix/store/d97nazmvhm2a2m3jn8ichid4ksannliq-dev-workspace-0.2.0`.
The guarded switch took66.061s and preserved native Codex and tmux processes.
The system generation and native executable stayed unchanged. Own session remains
on codex-lb with the saved team settings. The installed helper smoke made no host
call or real-session grant. Source-native worker tests and installed-helper checks
have separate evidence boundaries; naming checks did not request a generated name.

Aitherdev claim7bb60f85-6258-478f-b436-0af467b4144a is released, with authoritative
state verified at 2026-10-30T09:55:35Z. [Rollout](rollout.md) contains the source/input graph,
store paths, reviews, check receipts, deployment and release evidence.

No operator action remains. The session stays open; feature refs and registered
worktrees are retained. No archive, delete or stop was performed.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-cross-session-communication-authorization/
