# Codex 0.163.0 rollout — executed and accepted

The authorized system/application rollout and provider corrections succeeded.
Final acceptance is [postactivation-acceptance.json](postactivation-acceptance.json).
Feature branches remain published and unmerged; the session and aitherdev
reservation remain active pending explicit integration direction.

## Authorization and final selection

User requested “update codex in dev-workspace/codex-web and aitherdev to the
latest version” with repeatable skills, authorized aitherdev deployment using
vpsfree-cz-configuration, then directed “Implement the plan.” This covers the
system switch and workspace application rollout. No merge, reboot, reservation
release or session closure was authorized.

Frozen Codex 0.163.0 comes from llm-agents
e85b99217baf13a38fc887b31338b1833f1159c0. Final source identities and complete
series are in [final-heads-login-fixed.json](final-heads-login-fixed.json).
The final configuration is aed7d5071e24793d7bd811af11ccfa80e6f049d6.

- Running system and system profile:
  /nix/store/lr6b9x4023rf7404lpgw9n14gabbibcp-nixos-system-aitherdev-26.05.20261015.26f4107
- Workspace application:
  /nix/store/a335n75hnlpwfzf1bz8xkxgzvgynggd9-dev-workspace-0.2.0
- Workspace native assembly:
  /nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0
- System Codex assembly (also used by Home Manager's codex-ds):
  /nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0

## Executed coordinator sequence

All used reservation 0c72d37a-dcdd-44bc-bd4a-bc9f9a462505 and owner
c7fbd286-e060-419b-b538-6675336ab1ce. Builds/copies occurred before claims;
approved machine adapters performed dry activation and no-reboot switches.

| Job | Operation and source | Result |
| --- | --- | --- |
| c99ecbc3-7376-4b55-b7b8-3f1edb4abaaa | System 107255f8 -> i2908m46 | succeeded/applied |
| 587f4fa9-f4df-4bf2-ab4d-42d0664f8edf | Dependent workspace a158608e -> a335n75h | succeeded |
| ca886f70-c791-4d3b-a63d-8f3a059c3744 | Remove invalid profile keys, 9721c331 -> icx8yqs5 | succeeded/applied |
| 02558206-3690-414d-8e55-06b2362fb903 | Preserve shared login, aed7d507 -> lr6b9x40 | succeeded/applied |

Final attempt: 5c5c1563-76a9-4a27-a467-8eb1fc124a7e. All nine coordinator
notifications were delivered. Authoritative final records are in
[login-deployment-status.json](login-deployment-status.json). The reservation stays
in deployed_review; no finish/release was attempted.

Original release-evidence.json and intermediate deepseek-release-evidence.json
remain immutable. Final login-release-evidence.json binds the accepted review,
synthetic credential-preservation proof, isolated real provider success and exact
final build. No old receipt was relabeled as evidence for a later head.
Selected a335 catalog resolves adapter 39n6n34l in environment f7zlrnwa; prepared
artifacts were compared to that installed selection, not historical helper names.

## Verification and observed corrections

Exact native/package/catalog identities, original closure retention, full local
and CI checks, managed naming VM and both predecessor state-reader paths passed.
Independent full histories and affected-lane reviews accepted the final series
with no remaining findings or application migrations. Detailed review and test
receipts are linked from state.md and frozen release evidence.

Strict execution exposed two obsolete managed profile keys that --help had not
loaded. Removing those passed schema/startup validation. A later real-profile
check exposed forced OpenAI API-login enforcement against shared ChatGPT auth.
The guard removed the local credential before any provider request. Parent
restored the private credential from two identical retained operator backups;
local login status passes. That attempt should have used an isolated home.
No credential values were printed/committed, and the guard did not revoke tokens.
The final profile removes the unrelated login restriction while retaining the
required DeepSeek provider key. Both corrections were independently reviewed.

Synthetic empty-prompt before/after tests prove preservation. A real strict
private-home DeepSeek request then returned CODEX_UPDATE_OK in 2.47 s without
copied production login or shared-auth change. Final actual deployed-profile
loading preserved shared-auth bytes and stopped at empty prompt, without another
model request. Exact semantic profile and wrapper identities match that canary.

Final services, portal health/five browser assets, installed skill bytes,
provider selection and owned terminal panes passed. The retained thread has its
original ID/cwd and eight saved turns. Real final-package Luna naming passed in
3444 ms. HTTPS verifies against /var/lib/dev-workspaces/public/ca.pem and the
route requires authentication (401); ambient curl lacked that private CA.
The pending Codex marker cleared through ordinary scheduled reconciliation.

## Retained recovery and remaining ownership

[postactivation-retention.json](postactivation-retention.json) proves original
system 0.162.1, intermediate 0.163.0 systems, previous workspace 0.160.0 and native
roots remain retained. All owned verification runners ended and disposable state
probes were cleaned. No GC, branch deletion, archive or session stop was run.

Application recovery remains forward-only through the original supported
transition. Disposable compatibility probes passed old/new thread readers, but
do not authorize selecting an older workspace package. Preserve original jobs,
attempts, journals and roots; reconcile uncertain effects on their original job.

A system rollback to an older profile can restore forced_login_method=api and
its destructive shared-login conflict. Before using codex-ds on such a generation,
use an isolated Codex home without copied login credentials or deploy the corrected
profile. Do not test that old guard against the restored shared login. Remote
ChatGPT token refresh was not exercised by the local recovery check.

The next operator action is explicit integration direction for all four named
repositories to master. Refresh/check current target bases and applicable review
proofs before submitting merges. Reservation finish requires exact final
integration proofs, settled deliveries and explicit deployment/review completion.
