# Live verification evidence

Run 1: checked/published head `7cb07fa77dd048fa46241a766dfacbbea946f04f`.
Fresh utility `/root/verify_python_client_batch_1`, retained gpt-6-luna/low,
full-access/never, verified policy/native config. Exact session runner
`run-verification.sh`, exit1 after342 seconds, no retry/diagnosis by watcher.
Owned processes completed and native harness cleanup ran; no session lifecycle.

| Check | Result |
| --- | --- |
| Current-source generic HaveAPI + actual Rack wire/parser | 59 passed |
| Wheel and standalone source-distribution rebuild/install | Passed |
| Shared release regression suite | 34 examples, no failures |
| Python release artifact validation | Six passed |
| Real vpsAdmin API / released HaveAPI 0.29.12 | Ten examples, eight pass, two token-mode failures |

vpsAdmin source `fb2f51222503a45f2e5a42af505f719e44279ed0`, native disposable
MariaDB, core API real Rack handlers/serializer/auth with only documented
external PTR/notification side effects suppressed. Native RSpec summary:
273.76seconds,10examples,2failures,0pending/outererrors.

Passing actual API scenarios in both sync/async modes: reads (ordinary/admin
authorization, VPS/network-interface, pagination/metadata), TOTP, forced password
reset and TOTP-then-reset. Failing scenarios: tokens/sync and tokens/async;
outer bridge child_status assertion is not root cause. impl2 owns full retained
traceback diagnosis and narrow fix. No blind rerun or compatibility-ready claim.

Complete local logs/status under `verification/`; private manifest contents are
not copied into this summary or portal artifacts. No production credentials/API
writes used. Registry OIDC/publication and node/VPS lifecycle remain unverified.
Exact-head CI run receipts tracked in state.md; feature branch published.

## Exact-head CI and diagnosed test limitation

All five push workflows for `7cb07fa77dd048fa46241a766dfacbbea946f04f`
completed successfully: Python39335159997 (3.11–3.15 checks, integration and
standalone package smoke), release39335159808 (validate/test/build, retained
artifacts verified, publish skipped), RubyRSpec39335160040, RuboCop39335159859
and i18n39335159821. No reruns or retries needed.

Released HaveAPI0.29.12 permits public OPTIONS when a token is invalid/expired;
protected actions require authentication. Token test expectations requiring
set_auth itself to raise are therefore invalid. impl2 owns fresh protected
user.current HTTP rejection assertions plus bounded redacted diagnostics. The
original Python failure line was not retained, so this remains a source-grounded
candidate root cause pending diagnostic-enabled targeted verification.

## Reviewed token follow-up

Protected-request assertions accepted by independent reviewer at9cdb038; two
Important diagnostic findings D1/D2 directly fixed/checked in054f718. Only test
bridge/docs changed; runtime unchanged. Canonical actual source-line bounds and
fixed process-exit summary prevent raw child digit/summary text retention.
Injection/permissions/bytebound proofs and normalhooks pass. Final owning fold
and fresh targeted2token watcher pending; original failure line still unavailable.

## Final targeted token result

Fresh Luna/low utility verify_python_tokens_2 tested final checked head
326c05b78cec149b81e2c516c5cdcb7d1810d678 using run-token-verification.sh.
PASS exit0,64seconds,2examples0failures, both sync/async token scenarios exit0.
Evidence: tokens-rerun/vpsadmin.log,rspec.json,driver.status,elapsed-seconds.
Native DB/listener/child cleanup completed, no owned operation remains. Together
with prior8passing scenarios, real core vpsAdmin/released0.29.12 compatibility
is verified for all10 scenarios. Runtime unchanged; no need repeat generic/
package/release stages for these test-only corrections. Original precise failed
assertion was not retained; source diagnosis and corrected protected proof pass.

## Final publication and CI

Published finalhead326c05b confirmed by ls-remote; fetched master remainsc58704a,
clean source/index, final62files+10535/-17. All5finalheadCI workflows SUCCESS:
Python39337780111,release39337779915,RubyRSpec39337779942,RuboCop39337779958,
i18n39337779914. Python3.11–3.15 each passes format/lint/type/unit+wheel/sdist
install; integration real server passes. Release validates/tests/builds and
verifies retained artifacts, publication skipped. Fresh Luna/low utility retained
complete final jobs/status JSON under final-ci,72.9s; no retry/cancel/run launch.
Ready, awaiting explicit HaveAPI/master merge approval. No registry publication,
deployment or session closure. Node/VPS lifecycle remains outside API proof.

## Master integration verified

Native FFmasterc58704a->c1823f3, normalSSH/nonforcepush/hooks/signatureson,
remoteequality+cleantree verified. Claimfa9aac60 releasedrev2. All5masterCIgreen
at exactc1823f3:Python39487820831,Ruby39487820870,RuboCop39487821041,
release39487821053,i18n39487820847; publishingjobskipped. Freshpolicyutility
verify_master_ci retained receipts verification/master-ci,7sobservation/noactive
operations. No release/tag/registry/deployment/sessionlifecycleclosure.
