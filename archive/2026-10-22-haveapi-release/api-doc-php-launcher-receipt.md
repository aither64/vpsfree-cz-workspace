# PHP fixture launcher cleanup

Bounded lead assignment after the full27b4f8f8 local batch exposed an inherited
pipe-holding orphan. No runtime/client/protocol changes; dist27b4 artifacts and
all baseline receipts preserved. Original parent cleanup proof remains
api-doc-verification-owned-orphan.json (exact736630 orphan of batch718618).

## Cause and bounded fix

The launcher used a proc_open command String, so its tracked native process was
`sh -c`, not Ruby. proc_terminate/proc_close reaped the shell, returning PHPexit0,
while the Ruby child retained the TCP listener and inherited descriptors.
A standalone native probe reproduced this exactly: shell1254271, Ruby1254276,
listener alive after stop; cleanup verified exact cmdline/starttime before
SIGTERM of only that owned child, listener then closed. Full evidence:
api-doc-php-launcher-before.json. No unowned process was touched.

Exact source paths: clients/php/tests/bootstrap.php and new
clients/php/tests/ClientTestServerTest.php. Use argv proc_open (PHP8 manifest
supports it), preserve stderr/stdout merging via descriptor redirect, and remove
pipe2 nonblocking setup because redirected descriptors do not return a pipe2.
Existing environment, Bundler selection, ephemeral port, readiness and native
TERM/proc_close behavior remain. Source comment records the ownership invariant.

After-probe tracked the actual Ruby PID1262688 directly, children[], PHPexit0,
listener closed after stop, remaining_owned[], cleanup[]. Full evidence:
api-doc-php-launcher-after.json. No manual post-fix cleanup was necessary.

## Focused verification and commit

Prepared top-level tools-only Nix shell:
`cd clients/php && vendor/bin/phpunit tests/ClientTestServerTest.php` passed
1 test/2 assertions in2.401s. Real TCP connection succeeds before stop and fails
after; finally calls idempotent stop. Both files PHP syntax pass; exact-file
PHP-CS-Fixer3.95.1 reports no edits/offenses, diff whitespace clean.
Hooked commit0403c452 (clients/php: reap the native fixture process) passed
required I18n/PHP style and commit-msg hooks with no bypass.

Lead directly accepted exact source/comment/assertion prose and quick evidence.
This new test-lifecycle fix must join final affected-lane independent review;
it is not silently covered by the original four capability-finding reductions.
No long rerun, source rebuild, feature push or artifact mutation was performed.

Reusable lesson saved notes/haveapi/2026-10-22-php-fixture-native-process.md.
The separately owner-ready diagnostics package is committed through serialized
Git below; it does not alter fixture route or dynamic runtime behavior.

Current head after separate diagnostics commit: 164a15e4b8b41fee15522977c08fc483d07a6577.
Final history consolidation still pending architect-defined mounted URL package;
launcher/diagnostics source will precede exact last Version0.30.0.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
