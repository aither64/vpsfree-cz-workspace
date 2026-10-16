# Final rebased local verification

Clean committed product HEAD bf74af0b76accdf844ad6ffbea75db6c409f386e,
tree 822fe1de775fb57c592d8cef884ff016695a6ac2, base 7fd09b9b1f87f0563d3ba0be47081bfe4342b9b8.
Batch 18188 completed with wrapper.status=0 and status=0 in 2092 seconds.
Fresh Luna/low final_quick_observer observed the existing process and terminal
receipts without restarting it. The parent reaped terminal0 and inspected
all individual statuses plus evaluator/hooks/discovery evidence. Source stays clean.

The exact command is ../effective-mounts-quick/final-checks.sh, run through the
repository's rooted nix develop profile. It instantiated and realized the
normal persistence check with derivation/output GC roots, ran standard
bash tests/nixos-container-eval.sh, exported the actual twelve registered
scripts and checked every one with Ruby-c, ran declared overcommit--run, then
normal test-runner ls-tci discovery. All individual stage statuses are0.
Original logs and statuses in this directory are authoritative.

Persistence assertions and all 483 generated shell scenarios pass on actual 25.11,
26.05 and unstable. The standard evaluator reports every selector/export/real
release/legacy/unknown-release assertion true; template output is all FOUR true,
standalone outputs force successfully and unsupported-release checks finish0.
Actual generated JSON has exactly 12 expected keys; all 12 syntax logs say Syntax OK.
Hooks report RuboCop/Nixfmt OK. Discovery lists exactly 12 expected registered
variants. No unexpected local Linux kernel compilation was observed.

Prepared static checks, source equality and prior documentation verification
remain in ../persistence-effective-mounts-static/receipt.md and
../effective-mounts-quick/receipt.md. Original development failures and their
bounded test-only fixes remain in ../effective-mounts-quick/diagnosis.md.
No duplicate check or source correction was needed for this final batch.

These are local syntax/evaluation/command-double/discovery results. They do not
prove guest boot, source-only adoption, restart preservation or real mount
failure refusal. Independent committed final review and revised runtime follow.
