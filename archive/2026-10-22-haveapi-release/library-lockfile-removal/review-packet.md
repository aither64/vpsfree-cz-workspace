# Library lockfile removal: final review

HaveAPI `7ac977a26080d45d44b6608aafad2cadd2ec7f81..1103a3a14b1dc6dec17fc4859df80220a54f111d`, tree `32a09190e05a89f6312e07f20a9e4585335e468c`.
Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-library-lockfiles`, branch `2026-10-24-haveapi-library-lockfiles`, clean index/source.
ONE commit: `build: keep library dependency lockfiles local`. Complete history
in history.txt; full binary/full-index source.diff SHA256 ae326d5898c7303163462f9f7f531d43da282e2e9c9ae1d4c3b05f33f0f0e9eb.

User policy: untrack library locks, retain application locks. JS package-lock,
Python uv.lock and Rust generator Gemfile.lock are deleted from Git and ignored
locally. Runtime Cargo.lock, highlighter package-lock and flake.lock stay exact.
Instruction7ac is already merged separately. All24 changed paths form one logical
removal: without coordinated preparation/versioning/packaging/restoration changes,
fresh checkouts would break. Tests/docs support that behavior. No superseded
approaches/fixups/repeated update streams or migrations; no deployed-state change.
Design: ../library-lockfile-policy.md accepted95d290d6 and ../design.md.
Session ../plan.md and ../state.md are lead-owned; this receipt is their update.

Source-only check/check-clean no longer require local library locks. Mandatory
check-inputs retains existing JS/Rust identity/version checks and requires actual
prepared library inputs; release-check, version preflight, build and manifest
creation use it. Explicit native npm/uv/Bundler preparation precedes locked
consumers. Schema1 manifest retains all9 nonempty actual lock texts. Tools-only
verification checks packaged Rust Ruby lock against original retained manifest,
without resolving or requiring a local library lock. Missing/malformed/conflicting
evidence fails. Source file set/executable/dependency/hash checks remain.

Quick evidence (actual results/rawlogs beside this packet): release-check0/.862s;
release-test-retry1 0/16.915s:187Ruby examples and6Python tests. Covers real999
make-version using actual local3locks, allPython universal/top-level fields,
Rust external bytes, JS external records/bytes, source/root/tool locks unchanged;
cold clean source; missing prepared inputs; real Rust package cold restoration;
malformed/missing/conflicting retained locks. Original failure retained: a test
block-local path variable shadowed outer npm path; renamed, affected target
reranPASS, successful release-check not repeated. No oracle weakened.

../library-lockfiles-rust/receipt.md and final-inventory.json:4focused real
package/dependency specs, syntax and root-config RuboCopPASS. Python support
source-yield-receipt and JS support source-receipt hold YAML/AST/Ruff/Node syntax
results. ../library-lockfiles-native-setup/ready-receipt.json77d7fe9a proves fresh
ordinary ownRust/JS/Python setup (51.784s), Ruby3.4.11/Bundler4.0.23/nondefault
Fiddle1.1.8/Tomlrb2.0.5/TS6.0.3/Python3.11.17/Ruff0.17.1; no copied native bundle.
Local3 lockbytes unchanged7f51/47b4/6722; rootowning lock remains absent.

normal-commit-retry1 logs: PythonChecks/HaveapiI18n/RuboCopPASS; allcommit-msg
hooksPASS with advisory72column width warnings, everyline satisfies repo80.
Original normal hook trust refusal retained. Inspected .overcommit change only
removes ignored uv.lock trigger. Both plugin sources unchanged frommaster;
normal --sign plus --sign pre-commit refresh only config and PythonChecks
effective-config signatures, verifySignatures enabled. trust-refresh.diff retained.

Risk HIGH for retained-release input verification across build/restoration and
publication. Request retained reviewer0 Sol/xhigh/read_only ALL4lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. Read full
mandatory-change-review skill and applicable lane references; independently
inspect complete series/consolidation/no-migrations and actual Makefile/CLI/build/
workflow consumers and negative coverage. Main/support prose accepted bylead.

No dependency constraints, generator/templates/runtime/API, registry recovery or
publication policy changed. Fresh compatible resolutions can differ by checkout;
manifest records actual provenance, not commit-only reproducibility. Old91/source/
artifacts retained. No push/integration/backport/tag/publication/cleanup/lifecycle
here. Lead routes ONE final0.30.1 automatic build/package/smoke campaign after
review; standard tagged release follows accepted candidate. No duplicate full
local/development campaign. Source/Git/utility yielded, no active process.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
