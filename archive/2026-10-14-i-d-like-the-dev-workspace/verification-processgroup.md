# Final exact-source verification

Runtime6e1d9a191724d376cad2a71f234f0e4d1c01f36f passed the one authorized fresh
full flake command and CI Check38706253498. The fresh Luna/low utility watcher
retained execution and results; no operation remains active.

run-processgroup-flake.sh ran nix flake check --no-write-lock-file
--print-build-logs against the exact committed git+file revision in the declared
cached runtime environment. Start2026-10-15T10:32:22+02:00, finish10:45:43+02:00,
13m21s, exit0; processgroup-runtime-flake.log ends all checks passed.
processgroup-runtime-flake.status binds the full revision and status.
ci-processgroup-result.json independently binds successful Check38706253498 to
the same exact head. No unexpected local kernel build or cancellation occurred.

The recovery VM completed all five subtests and both disposable reboots. Its
expected injected startup/compensation failures produced bounded diagnostic
records; nonterminal checkpoint probe tracebacks were retried by the existing
waiter. They did not fail the completed scenario assertions or aggregate.
verification-processgroup.json records the exact completed subtests, reboot
count and frozen log/status/CI/final-head/review-chain hashes.

Source quick evidence remains accurately scoped: the reviewed b4b90aca full
uncached focused package passed both real cancellation cases, deterministic
contracts and the live-owned negative control; only the changed terminal-sample
wait contract was rerun uncached at amended6e1. Source review and direct narrow
Advisory remedy verification passed; final composition/history review found no
additional findings. See processgroup-review.md, its dispositions and
processgroup-composition-review.md. Final lock/checker/hooks evidence is linked
from processgroup-composition-inventory.md and processgroup-final-heads.json.

The original bb9 local flake failure remains causally unexplained. Its process
state was not captured; failed-source store inspection was unavailable. The
test observer had demonstrated ambiguity and was corrected, without changing
production cancellation. This passing final run validates this candidate/run;
it does not prove a Z-to-X cause or repair of a production defect. The earlier
provider recovery failure also remains unexplained, with all evidence preserved.

No own version is deployed yet. Historical native Chromium/Firefox provider and
worker evidence belongs to its exact earlier run; all three shipped browser
assets remain identical. Final live-native-6e1d9a19 is prepared and unrun. It
requires genuine final profile preparation and successful activation. Physical/
macOS display and actual notification click remain unproved. No deployment/use
readiness or merge approval is supplied by verification alone.
