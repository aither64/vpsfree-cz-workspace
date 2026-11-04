# Affected final review: isolated API fixture readiness

Session: 2026-11-01-typescript-client-migration.
Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui
Requested outcome: finish the generated-client migration and verify the unpublished
SDK against the existing isolated mounted API. SDK publication/default merges,
deployment and session lifecycle actions remain outside authorization.

## Completed boundary

Review exactly `3e7f54e8176970cb0c04fc6cff7be85c09bd3ce0..d80c0c21b91bc8f7cb1b03fe4d7b2b5035ce3e5f`, three existing runner paths,
+77/-8. Source commit is complete; seven focused Node tests and Node/Ruby syntax
pass. Later one-line fixture typing and E2E-adoption metadata are separate
consumer test maintenance; no application/runtime/dependency/API inputs changed.

```
d80c0c21 test: release API fixture readiness before child shutdown
 scripts/integration/vpsadmin-sdk-contract.mjs      | 37 +++++++++++++++----
 scripts/integration/vpsadmin-sdk-contract.rb       |  7 +++-
 scripts/integration/vpsadmin-sdk-contract.test.mjs | 41 +++++++++++++++++++++-
 3 files changed, 77 insertions(+), 8 deletions(-)
```

The original whole migration was independently reviewed at aef727cf with all
four findings directly remediated under step9. History proof is retained in
webui-review-remedy-fold-receipt.json; packaging adapter separately cleared at
7cad7ffb. Retain those unaffected conclusions. This review concerns the new
readiness protocol implementation and owned fixture shutdown interaction,
not another full migration audit.

## Observed cause and intended behavior

Attempt2 exited1 after337.383s; its log reported the fixture Timeout::Error
before SDK step1. Ruby wrote its private JSON facts and waited300s on stdin;
Node awaited fd3 EOF. Implementer0 reproduced on pinned Ruby3.4.11 without
DB/server: an inherited unregistered fd3 survived Process.spawn in a descendant
(same socket inode). Data arrived at194ms, EOF at888ms when descendant exited.
Registering fd3 and close_on_exec before spawning prevented inheritance;
data+EOF at213ms while descendant stayed alive until898ms.

The producer now registers fd3, close_on_exec and sync before any Bootstrap
child. The consumer parses the existing puts newline frame on data without
waiting for EOF, and rejects incomplete, malformed and early-exit producers
with fixed errors. The existing Node owner, stdin shutdown, native timers,
Ruby ensure, Bootstrap/TestDb at_exit and single private channel remain.
No provider/API/schema/generator change or automatic replay/retry is introduced.

## Ownership and compatibility

WebUI owns these test-only runners. They consume clean API610a96f8 and SDK99ee0665
with HaveAPI0.32.0 through the retained archive receipt. Existing Safety,
Bootstrap, SpecSeed and TestDb own isolation and cleanup; mounted loopback Puma
owns HTTP serving. Private fd3 carries synthetic credentials and must not be
printed or written to ordinary evidence. No shared public protocol or persisted
format changes. No database migrations, no released/merged/deployed runner
version or supported transitional state to preserve. Final integration-fix
history consolidation remains planned once the campaign finishes, preserving
this reviewed range and reports.

## Quick evidence and documentation

- node --test scripts/integration/vpsadmin-sdk-contract.test.mjs:7/7 pass346ms.
- node --check and Ruby syntax:pass; owned diff-check:pass.
- New pure cases prove fragmented complete line resolves while stream stays
  open, early EOF/exit rejects and malformed frames use fixed messages.
- Nearby producer comments preserve the non-obvious inherited-fd rationale.
  Existing test-runner documentation still owns invocation/isolation/limits;
  no public application behavior or new operations procedure needs changing.
- No third DB/server/matrix run has started.

## Residual effects and planned check

Attempt1 exact TestDb state was natively stopped/pruned and proven absent.
Attempt2 had durable normal exit1 after its Ruby Timeout. Source shows Puma
stop, DB disconnect and registered TestDb stop/prune at_exit are entered.
Exact second Ruby/DB/directory identities were not retained; deletion cannot be
externally certified. Lead records cleanup expected by controlflow, externally
unconfirmed; no timestamp-based attribution/deletion or unrelated process
mutation. A third run uses a new uniquely owned TestDb only, and does not prove
historical deletion. Its fresh watcher retains durable root/exit capture; owner0
will capture exact descendant Ruby/DB and nonsecret directory/socket metadata
under that known root for post-exit effects proof. Native run budget and
shutdown must be observed before success. See sdk-real-api-2-result.md.

## Review assignment

Overall risk HIGH: private readiness/credentials and temporary DB lifecycle.
Use all four lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Same retained independent reviewer0, saved Astra/xhigh,
read_only, no override/nested reviewer. Read mandatory-change-review SKILL.md
and each selected reference, applicable workspace/repository guidance, actual
source/history/tests and relevant API fixture owners before conclusions.
Report findings with severity and exact source; assess proportionate minimal
fix, no source edits or tests/build/DB/browser execution. Source clearance is
not runtime matrix/cleanup acceptance. Earlier unrelated evidence is retained.
