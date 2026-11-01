# Complete React transport-fixture follow-up — final review

Lead released design7340 plus7424. Request affected final review of the complete
new test-only correction, preserving dispatch-order strength and all original
UI/flow assertions. No application, dependency, workflow, timeout/retry or live
behavior change; original failed runs remain failed evidence.

Repository vpsfreecz/vpsadmin-webui; owned alias `vpsadmin-webui-031`, branch
`dev/vpsadmin-haveapi-031`. Base/main:
`163ad4e09a1b77f788e65a8345d69c74c8475723`.
Final head: `f2765d3fd778927f4cda3563f66615bfcf72b7cf`.
Final tree: `0f4949dc1c346bb4205940655f29965daeb16039`.
[One-commit full history](series.txt), [complete diff](final.diff),
[a44-to-final comparison](range-diff.txt), [committed binding](committed-source.json).
Exactly one coherent unmerged test-adaptation commit above immutable merged163,
9 files/+92−36. Prior a44 is retained exactly in named local recovery
`dev/recovery-haveapi-e2e-a44b3ac`; its original static results are preserved.
No repeated pin/dependency stream or obsolete intermediate commit remains in
163..final. **NO MIGRATIONS**; no schema/persisted-state or runtime change.

Four affected specs:
- list-row and lifecycle member deletion require exact `{ vps: {} }`, preserving
  confirmation/navigation and absence of admin-only mutation fields;
- profile keys/sessions matches GET, exact collection path and decoded auth_type
  category, preserving all filter/exact-ID/rename/close assertions;
- profile transaction filter replaces only its fetch-only local recorder with
  native XHR open/send observation. Metadata is stored after successful native
  open; matching GET/exact-path/limit51/absent-filter send snapshots location
  synchronously immediately before native forwarding. This/arguments/results/
  exceptions are forwarded with Reflect.apply; no shared or application hook,
  synthetic request, interception or asynchronous substitute. Positive actual
  request/recorder counts and every-location-no-invalid-param assertions remain.

Both complete profile specs are adopted into existing strict coverage; VPS
specs were already adopted. Compiler flags and all remaining deferred entries
stay exact. Only the prior profile fixture's known first-key index and nullable
close timestamp need local typing annotations; no fixture values change.
[Product/lock/runner/flag/assertion preservation](unchanged-inputs.json).
Owning docs: existing VERIFICATION.md, WORK_LOG.md and dated
2026-11-01-browser-wire-expectations.md; no route/adapter inventory change.

Original evidence: main/push163 broad41291251937/attempt1: desktop237PASS,
2FAIL/1SKIP; smoke41291251986/attempt1: desktop605PASS/2FAIL, mobileChrome548PASS/
1FAIL, mobileWebKit249PASS/2SKIP. CI41291251993SUCCESS remains separate. Observer
17843 consumedexit1/allterminal. [Broad facts](../../default-ci/broad-failure-facts.json),
[smoke facts](../../default-ci/smoke-failure-facts.json) and original metadata
bind retained private0600 logZIPs/traceZIPs under0700; original configured retry
traces are preserved. A0 read only necessary cases; no new retrieval belongs
here. Passing mock HTTP responses did not establish send-time normalization;
that invariant still needs the prescribed browser run.

Full declared `ci:quick` PASS, exit0/106.680s, Node24.21.0/npm11.19.0, E2E90checked/
187deferred, docs161/requirements76 and six BFF-type cases. [Result](static.result.json),
[stdout](static.stdout.log), [stderr](static.stderr.log). Quick staged tree equals
final commit tree exactly; [2489-entry exact Gitless source](static-identity.json).
Existing exact dependency installation reused; no install/build/browser/CI run.
Normal identity/hooks checked, no declared framework/active hook and no bypass.

All19972 private descriptors, inodes/path/terminal952323, canonical live clean2e32,
a44/02e/baf/live recovery refs and roots are preserved; no cleanup/root action.
[Final effects](effects.json). Source/Git writer RELEASED; no active owned command,
publication/default/PR/site/deploy/lifecycle mutation. E2 product CI untouched.

Risk MEDIUM: localized test observer and assertion adaptation; runtime/inputs
unchanged. Request retained reviewer0 saved Sol/xhigh/read_only, affected general,
architecture/repetition, scope/proportionality and risk/compatibility concerns,
including whole history/NO MIGRATIONS and exact native dispatch observation.
Lead assigns review; no model/effort change or self-approval.

STOP before browser/publication. After accepted review, one focused batch only:
1. Both full original affected files on Chromium: vps_list_row_click and
   profile_keys_sessions.
2. All three profile_session_transaction_filter cases on Chromium/mobile Chrome.
3. Only the lifecycle member-delete case on Chromium.
Use the ordinary pinned wrapper, existing isolated exact-source environment,
two workers and retries0. No broad/nightly/full local matrix, unit/Nix rebuild,
manual CI dispatch/rerun or production action. Preserve any ordering/later-assertion
failure and report before product changes.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/).
