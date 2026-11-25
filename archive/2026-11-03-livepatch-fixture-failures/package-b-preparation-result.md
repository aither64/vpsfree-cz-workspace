# Package B preparation/check result

Tested source revision: `dd188397abe37d0bc33f4c5dfb3605206ce5e326`, with the assigned current uncommitted fixture edits in `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-livepatch-fixture-failures/vpsadminos`.

1. Command: `nix-build tests/fixtures/livepatch -A resolver --out-link /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-livepatch-fixture-failures/package-b-resolver`
   - Exit 0; elapsed 11 seconds.
   - Produced `/nix/store/22lpmzxk9g9vb5vi1f55q9x0phl73vhk-livepatch-probe-sites`.
   - Log: `package-b-tool-build.log`.
2. Since step 1 exited 0, command: `nix-build tests/fixtures/livepatch -A siteChecks --out-link /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-livepatch-fixture-failures/package-b-site-checks`
   - Exit 1; elapsed 18 seconds.
   - Failure excerpt: `ERROR: test_special_livepatch_relocation_section_is_resolved`; at `test_probe_sites.py:75`, `elf.structs.Elf_Shdr.build(header)` raised `AttributeError: 'dict' object has no attribute 'sh_name'`. Test summary: `Ran 20 tests`; `FAILED (errors=1)`.
   - Log: `package-b-controls.log`; derivation `/nix/store/mwk2cc19h0hxvca279van7q3jy6rv5br-livepatch-probe-site-checks.drv`.

No operation remains running. No retries or cancellations were performed. The two assigned outlinks were retained.
