# Narrow final-review remediation verification

Reviewed base bf74af0b76accdf844ad6ffbea75db6c409f386e plus the six frozen paths in
source.sha256. Independent Astra report is ../effective-mounts-review/astra-final-report.md;
lead disposition is ../effective-mounts-review/i1-disposition.md. No new mount
or metadata policy is introduced; this enforces the existing root:root/0755 choice.

Prepared format/parsers/Bash/Ruby/inverse checks pass in
../persistence-effective-mounts-i1/receipt.md. Parent inspected exact raw delta:
only checked numeric chown0:0 and chmod00755 follow each successful missing-path
mkdir. Existing path early-return and all mount/account logic are byte-unchanged.
GNU coreutils documentation confirms explicit five-digit mode clears special bits.

Normal I1 three-release persistence evaluation passed0. Its initial native shell
build failed at the new real-SGID test setup: chmod2775 EPERM. Nix filter-syscalls
is enabled and its installed manual explicitly forbids setuid/setgid creation.
Original wrapper/build/status/derivation/input evidence is retained under
attempt-1-sandbox/. Do not claim that native aggregate build passed.

Implementer removed only this prohibited pure fixture setup, leaving checked
fresh-path-only numeric ownership/full-mode arguments, created/chown/chmod list
equality, actual ordinary chmod, both injected failure negatives and all original
scenarios. No filter disablement, conditional skip or simulated SGID claim.
Four raw modules and registered suite are byte-identical to successful evaluation.
The real fresh-ancestor guest SGID control remains unchanged.

Parent reran the complete failed shell stage using all30actual evaluated tuples,
with only the harness path replaced by the corrected working source. All543
scenarios passed0 in81seconds. Exact30invocations and all60input files are retained.
No duplicate broad Nix evaluation was needed for this shell-only correction.
This is the focused requested remediation check under mandatory-review step9.

Remaining actual-script/hooks operation89111 passed0 in486seconds. Exported JSON
has exactly12registered keys; all12Ruby syntax logs say Syntax OK. Only the actual
fresh-ancestor-26.05 string contains the SGID-parent setup. Declared RuboCop and
Nixfmt hooks pass. Final source.sha256 recheck passes. The initial diagnostic
wrong-CWD launch was interrupted before tests; see diagnostic-cwd-correction.md.

Real setgid inheritance, root ownership and parent metadata preservation remain
VM acceptance work. The new control uses an actual parent0:1234:2775, an absent
child required to become0:0:755, and repeated parent metadata/inode snapshots.
No source/data repair, account/map ID seeding or readiness relaxation exists.
Exact final commit/tree and runtime clearance follow hook-enabled folding.

Exact-final-head normal CI validation is now confirmed independently of the
local failed fixture attempt. Job116424410403, workflow38735726547, head
edb90d2fe2190d88d8b9d2d21bd0def79eedc898 is completed success. Its step6
Check NixOS persistent activation runs the normal flake nix-build command and
passes12:40:33Z–12:48:35Z, building
/nix/store/6218pz068gff57gp72fjhw2b0ylh5msd-nixos-container-persistence.drv.
Actual job/step JSON and raw log are retained under ../effective-mounts-ci/.
Compatibility/template, both disk-reuse checks and host build/cache also pass.
Initial log download refused terminal escapes; --allow-escape-sequences was used
only to retain the raw file, without outputting it to the terminal or rerunning
a check. This new success does not erase the original local sandbox failure.
Broader runtime/CI workflow acceptance remains pending.
