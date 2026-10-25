# Final review: library lockfile removal

User directs actual library-lock removal, integration/backport and release0.30.1.
The earlier instruction-only change left actual locks tracked; this deliverable
implements the chosen library/application distinction and required build seams.

Repository vpsfreecz/haveapi. Worktree
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-library-lockfiles
branch2026-10-24-haveapi-library-lockfiles. Complete base/head:
7ac977a26080d45d44b6608aafad2cadd2ec7f81..1103a3a14b1dc6dec17fc4859df80220a54f111d
tree32a09190e05a89f6312e07f20a9e4585335e468c. One coherent commit;24paths,
346insertions/3989deletions. No migrations, obsolete iterations/fixups or
repeated dependency/input refresh streams; existing application locks retained.
Inspect actual full message/parent/diff/clean source independently.

Accepted design: library-lockfile-policy.md (authority addendum1405e27b;
technical brief originally95d290d6); design.md, plan.md, state.md.
Untrack JS package-lock/Python uv.lock/Rust generator Gemfile.lock; local native
inputs remain ignored. Preserve private Cargo harness/highlighter/flake locks.
Clean source metadata checks work before dependency preparation; explicit
prepared-input checks run for maintained releasecheck/build/manifest/version.
All nine real resolved lock texts remain in manifests. Rust gem requires actual
prepared Ruby lock as existing generator provenance; tools-only restore compares
packaged bytes with original retained manifest, resolving no new dependencies.
No registry retry/upload policy, generator/runtime/template/constraints or
downstream repin/regeneration change intended. Consumers still resolve manifests.
Fresh independent builds may resolve different compatible graphs; no commit-only
reproducibility claim. Previous090a downstream source boundary remains preserved.

Check commands/raw results under library-lockfile-removal/: release-check0/.862s
(retained), release-test-retry1.result.json0/16.915s (187Ruby/0+6Python/0), normal
commit-retry1.result.json0/7.475s with PythonChecks/I18n/RuboCop and messagehooks.
Initial test fixture variable-shadow failure corrected; original logs retained.
Normal signing after inspected .overcommit filter-only change, no hook bypass;
original signature refusal retained. Message TextWidth >72 warning qualified;
all lines comply80. Native setup actual ready77d7fe9a/54files27208ed1 inspected
and rehashed by lead; new own environments, no installed-native copies.
Rust focused4dependency/package examples0fail, style2files0offenses, syntax2PASS
in library-lockfiles-rust/; original one indentation finding fixed/retained.
Python YAML/AST/nativeRuff quicks in library-lockfiles-python-support/; changed
JS spec nativeNode syntaxPASS in library-lockfiles-native-setup/. Main prose
pass accepted JS/Python/Rust and operationaldocs; release notes deferred to
actual patch versioning. No full dev/test/build campaign repeated.

Risk HIGH for prepared input and retained-artifact release verification boundary;
assign all four lanes (general, architecture/repetition, scope/proportionality,
risk/compatibility). Mandatory final review after completed commit/quicks before
long affected release build. Review request does not approve publishing old91.
Original91/ref/artifacts and source reviews stay historical; next patch will
use genuine-x instruction/removal and final Version0.30.1 after master proof.
User authorizes actual newcandidate release; no lifecycle/deployment/cleanup.

Reviewer0 retained independent Sol/xhigh/read_only, roster34, no overrides or
fallback. Read full mandatory-change-review Shared Reviewer Instructions and
all four references, applicable workspace/owning guidance, then actual source
and full series. Return concrete findings/severity, history/consolidation and
explicit no-migrations conclusion; no source edits/tests/setup/network/CI or
moving logs. Lead accepts/persists report and coordinates required narrow fixes.
