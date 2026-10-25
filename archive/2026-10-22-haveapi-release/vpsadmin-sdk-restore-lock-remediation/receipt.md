# Lock restore review remediation yield

Final `ff876abe..63b87e9a1b92727a3e5c5513898e183ab0be898a`, tree
`90dbaba680a47a70f5bd216082dfbc1fa6e201ca`, clean and command-free.
Shared `tools/restore-cargo-lock INPUT_DIRECTORY --sha256 EXPECTED` replaces
all three inline validators. Artifact inventory, regular/nonsymlink files,
raw SHA, exact source/run/attempt identity and exclusive destination creation
are unchanged. Credentials, artifacts and verification/publication timing are
unchanged. Focused committed tests invoke that real helper; they do not copy
its validator. Existing technical docs and four accepted prose files remain
accurate and unchanged.

Actual ten helper tests passed (2.284s; declared Nix wrapper25.29s including
ordinary substitutes). Corrected absolute session syntax driver passed in
0.86s: two YAML workflows,19 shell/embedded-Python run steps and two helper
Python sources. The original failed relative path invocation loaded no test;
its evidence remains in syntax-path-failure.json. No generation, compiler,
package/MSRV, push, API/CI, settings, tag or publication was run.

[Exact four-path delta](narrow-fix.diff), [result/mapping](result.json),
[range-diff](range-diff.txt), [final three-commit history](final-series.txt),
[focused tests](focused-tests.json) and [syntax result](syntax-result.json).

Mapping: generator commit926982 unchanged; owning build6adb22b2→d50a4b88;
generated refreshe370b39e→63b87e9a remains separate. The transient fixup was
folded into its owning unpushed build commit; base/published history untouched.
Final tree equals the staged narrow candidate. All686 generated Rust files,
eight runtime files, schema/options/Cargo/flake/local lock inputs and main
prose are unchanged. No migrations or obsolete intermediate streams remain.

Lead step9 inspection/acceptance precedes separately granted exact-head
feature CI. The new [disabled preparation](../vpsadmin-sdk-feature-ci-preparation-63b87e9a/README.md)
binds this corrected head without overwriting e370 records. Owner3 retains
review fixes/Git; no utility or local operation remains active.
