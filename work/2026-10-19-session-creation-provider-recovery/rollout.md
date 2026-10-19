# Creation provider handoff rollout

The user's provider-switch task remains defective after its earlier release:
accepted requests with explicit provider fail at Ruby initialization, and error
polling destroys selection. This follow-up keeps the standing deployment
instruction “deploy it to aitherdev” and conditional direction “when this is
fixed, deployed and verified, you can merge it into default branches and release
aitherdev”. Scope remains generic runtime plus workspace/configuration pins;
there is no new product scope, Codex patch, native update or team change.

Reviewed source:

| Repository | Base | Reviewed final feature head |
| --- | --- | --- |
| dev-workspace | 8385699aabcc2cfc74b585ca653a4658ff3eef75 | a85724214a4297ad62af4ec589d56a7ef3106724 |
| workspace | c31bd809eafc7805297f35b4d57b9d1e56804a7c | 60ff3068eff419047379c681c4e4dd608815b8ac |
| vpsfree-cz-configuration | 95a8b88d383c177fc65bf67d51c901a69c0b2847 | 98f6fe8e02d54eff7b694b064f0729d62e0eb04d |

Application review and separate final mechanical pin/history review accepted
with no findings, same Astra/xhigh reviewer. Both pin streams are singular;
extension/shared client/native selections are unchanged. Generated configuration
commit passed normal hooks. All feature branches are published over SSH.

Live baseline is in live-before.json: application a5dcgj4h, system lg6pjp0k,
Codex daemon PID 3387667, stock 0.163.0 binary SHA256 5e538cfe...c3d1a5. No active
reservation existed at the read-only baseline. This does not reserve the machine.

Real candidate Ruby validation accepts the exact two live failed receipts
without mutation (live-receipt-candidate-read.jsonl). Their saved requests remain
failed and user-owned; no retry, provider switch or new user session is performed.

Deployment remains prepared only. Finish local sandboxed package and browser
selection/clipboard verification, prepare exact configuration/system and composed
profile snapshots, then obtain ordinary approval/reservation and submit system
before profile. Preserve original request/job identities on uncertainty. Verify
actual serving assets, failed receipt acceptance, native/daemon continuity and
provider state before conditionally merging through the integration driver and
releasing this session's reservation. No reboot/archive/delete is authorized.

Rollback follows the supported forward-only profile/recovery procedure. Old
defective runtime cannot repair these requests. No schema migration is introduced;
retain exact deployed sources/artifacts and use reviewed compatible successors.

Final test-only CDP observation repair a857242 passed the real browser check
(23.115s). Final delta review accepted the three runtime commits and both
consolidated final pin streams, no findings or migrations. Original reviewer
follow-up interfaces refused its unloaded multi-agent child; fresh standalone
reviewer 01a1531d-c2b0-7cc3-8ab5-3f5eb70800b8 retained catalog Astra/xhigh
settings and accepted the affected general/history delta. Original reports
remain immutable. Exact final system/profile preparation is now being launched.
