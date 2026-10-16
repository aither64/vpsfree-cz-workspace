# Exact test-host binding verification

Current test and guest source: clean published d3bf74bc92ea0ced100df12ba10e1dadd7fd1ec5.
Host source: original immutable /nix/store/hzblqf1z79akb3wrck2xqmfi791g0xk4-source,
with truthful edb90d2fe host build metadata and original locked inputs.
The public VPSADMINOS_CONFIG module replaces only the host overlay list with
its original four overlays, in their original order. No machine output is
substituted, no test root redirected and no product packaging changed.

The earlier host-inputs/ attempt evaluated0 but failed strict equality because
it imported the already-coerced gem source, producing a second copy. That
failure remains intact. A tiny derivation-only probe proves this actual flake
root coerces to the original gem src; both source NAR hashes match.

Fresh utility declared_host_eval_watch (gpt-6-luna/low) owns one public-helper
evaluation. compare.py requires full non-script equality to the original native
runtime config and exact equality of ALL twelve scripts to current quick inputs.
It records hashes on success; no host or package normalization is permitted.
Prior old-to-current comparison already proves only the accepted declared setup
and source stdout/adjacent-blank provenance differ. Normal check derivation6218pz
and the actual runner package are separately retained.

Evaluation/comparison terminal results and affected runtime acceptance remain
pending. The failed original guest remains untouched. This is evidence for an
explicitly pinned test host, not runtime acceptance of the ordinary unoverridden
local-source host build.

TERMINAL: fresh watcher evaluation0 in587seconds; parent comparison0. Complete
non-script JSON equals original-config.json, including original hd5…toplevel,
3j3…squashfs and every kernel/initrd/qemu/virtiofsd/resource/framework field.
All12current script entries equal quick/inputs.json byte-for-byte. comparison.json
binds exact input hashes and current test-source head to original host-source head.
Normal check6218pz and runner3317pn… remain separately identified. Gate is clear
for one NEW declared-backing runtime; no ordinary unoverridden host acceptance.
