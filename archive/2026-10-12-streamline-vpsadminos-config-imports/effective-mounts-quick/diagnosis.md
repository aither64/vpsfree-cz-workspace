# First effective-set check failure

The first normal check failed142s at the aggregate25.11 direct-filesystem
assertion before remaining batch operations. Original logs/status/source diff
and SHA inventory are preserved in attempt-1/.

The isolated read-only probe evaluated each direct assertion term on all three
actual inputs. Adapter ordering, direct/state/nonbind/recursive coverage and
source dispatch are true. Only the nonbind option-string assertion is false:
actual options are x-initrd.mount,defaults,mode=0755. Pinned filesystems.nix
adds x-initrd.mount for boot-needed filesystems. The full effective tuple is
correctly preserved in the raw callback. No production behavior fix is justified
by this assertion mismatch. Implementer applied the bounded three-test-file correction; all prepared
static checks passed and all seven other technical paths retain their initial
hashes. The corrected test derives the entire effective
option string and separately checks requested tokens; shell remount checks must
use the same effective entry rather than omit upstream-added options.

Probe original JSON/log/status and watcher wrapper receipts remain alongside
this record. No runtime or kernel compilation occurred. The next actual check
is necessary to validate this test correction, not a blind retry.

The corrected full check completes three-release assertion evaluation and
realizes all30generated snippet/mount pairs, then the shell builder fails at
its first case: line110 backing unbound. Bash dynamically scoped helper locals
shadow the harness's unprefixed state variables. This is a harness namespace
collision, not evidence of a production failure. Original second attempt is
preserved in attempt-2/. The derivation is retained in
evaluated-check-derivation.json; evaluated-shell-checks.sh extracts its exact
30invocations with only the harness path replaced by the corrected working
source. This permits focused shell verification without repeating evaluation.
Normal final-source flake verification remains required after rebase.

The first focused shell batch exits1 at declared/fresh source identity. A
retained Bash trace establishes the second harness mismatch: escapeShellArg
emits safe target operands unquoted, while fixture rewriting handles only
quoted paths. The upstream calls were relocated but dispatch operands remained
/var/lib/nixos and /var/log; the ordinary callback therefore ran. Correct only
the fixture's exact bare equality-operand rewriting, preserving component
boundaries. shell-debug.log and the retained root recorded in shell-debug-root
contain the decisive inner output. Third attempt is in attempt-3/. No product
source correction or assertion reduction is justified by this evidence.

The next focused run could not open its input: automatic store GC had removed
the unrooted generated outputs and derivations after the failed build. This
exit2 is infrastructure loss, not a code result. The normal check is being
regenerated with nix-instantiate --add-root and then realized with an output
root; this keeps the derivation available across failure and avoids losing the
same diagnostic inputs again. No global GC policy was changed.

As a bounded early diagnostic, the previously retained declared-case activation
and call text were restored to their original fixture locators by exact reverse
substitutions and run through the current harness. All20declared scenarios pass,
including source/target identity, metadata, mount/remount, backing and lookup
failures. This confirms the quote/scope corrections for that captured case;
it does not replace the rooted full30-pair normal check still running.
See retained-declared-diagnostic/harness.log and status0.

Rooted check: three-release assertions pass; generated shell runs reach the
unstable explicit-dependency matching-live scenario after the preceding release/
layout cases pass. Exact trace shows unstable's x-systemd.requires-mounts-for
value has been relocated in the actual command but not the expected option
string. The harness must apply its same fixture locator rewrite to expected
selected options per case and retain exact full comparison. This introduces no
hardcoded upstream token. 25.11 explicit control passes independently; its
options do not contain that dependency locator. Both diagnostic traces are
retained. Rooted attempt is in attempt-4-rooted/; all60generated source inputs
are now retained with original path/hash inventory to survive automatic GC.

After that batch terminal, the lead authorized the bounded suite trace-strength
refinement and expected-option relocation together. Production raw source remains
unchanged. Parent owns the complete retained30-call test and remaining checks.
