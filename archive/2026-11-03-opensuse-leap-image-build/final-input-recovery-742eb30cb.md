# Final verification input recovery

The [v2 discovery](final-discovery-v2-result.md) validated syntax and priority:
`{ image = 8192; namespaces = 4096; }`. Its first native listing then stopped
because the previously recorded immutable source path was absent. The source
had been inspected without establishing a durable session GC root. The exact
time/mechanism of removal was not audited; no product defect is inferred from
its absence.

The exact clean source was materialized again with the existing runner helper
`nix/resolve-repository-source.nix`, using `--argstr repoRoot` with the explicit
Git URL/revision below. Passing the worktree as a Nix path was rejected by the
file audit because that copied ignored gems, `.git`, Gemfile.lock and result
files. That rejected import was never used for a listing or VM.

```text
git+file:///home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git?ref=refs/heads/2026-11-03-opensuse-leap-image-build&rev=742eb30cb1a8b6766c85e915d26b0400e38244b1
```

Accepted exact identity:

- Git head `742eb30cb1a8b6766c85e915d26b0400e38244b1`, tree
  `19f423e70ff439867d4bb27e8ed07b9c95fdb703`; product source/Git unchanged.
- Source `/nix/store/m1n49nc1qdf1f3j298zcmjjb5ni43iag-source`, NAR
  `sha256-MwArttbMI6mzt/YzUwvSbK1Pd4mizjKqO600EnK2fNE=`: exactly the original
  identity. All 2,371 tracked files/symlinks and executable flags compare equal
  to `git archive 742eb30cb...`, with zero differences, extras or missing files.
- Native helper output
  `/nix/store/wq78kzx0mmmdbl2xyq6dajxzlrc2ryd0-test-runner-repository-source`.
  Its `source` link resolves to the accepted source above.
- Durable indirect GC root
  `work/2026-11-03-opensuse-leap-image-build/.nix-gc-roots/source-742eb30cb-exact`.
  `nix-store --query --roots` on the actual source reports that root through
  the helper output, proving reachability rather than merely assuming it.
- Existing runner separately rooted at
  `work/2026-11-03-opensuse-leap-image-build/.nix-gc-roots/runner-742eb30cb-v3`,
  targeting `/nix/store/jwkyiqgfq607h40zasf5p0rkd3rzkkly-test-runner`.
  Native root inspection confirms it. All nine literal wrapper dependency
  paths exist, and a quick require-only preflight under the actual wrapper's
  environment prints `FINAL_RUNNER_REQUIRE_OK`.

The fixed [invocation file](final-runner-742eb30cb-v3.sh), SHA256
`c13929304f04033528bba1b5e98bd24bde862a35b2d6d6d9aa234631790c4e06`,
was generated from the real wrapper's interpreter/path and the exact source,
revision and v2 module paths. It exports only that metadata and executes the
unchanged native wrapper with its arguments. No Ruby/gem paths are transcribed.
Shell syntax passes. The underlying wrapper remains SHA256
`b587483082b031fb8606d150c4da39f5a7082ba8ce3aa2bb1572f436e424f0a2`.

The v2 module remains SHA256
`f6bebf53ebdb690c996fd325ced3db201403d97dc1e525731ea9178b849fd90d`.
All previous failed inputs and discovery logs/results remain unchanged. No
test listing, OS/VM/kernel build, server or long test was launched during this
recovery; only the native source-link derivation was realized. The rejected
path-style import remains unused; do not select it as a verification input.

Next action is the lead's fresh native listing operation through the fixed
invocation. Actual four-case selection and device selector discovery remain
pending. Independent product review can proceed at the unchanged Git head.
