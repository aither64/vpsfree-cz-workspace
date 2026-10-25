# Narrow restore-policy extraction — source HOLD

Lead assignment9eec3256 accepts reviewer0's Important architecture finding.
Original review ff876..e370 is active. No SDK source/index/HEAD change is allowed
until the lead relays its explicit terminal read-only yield. This session note
is the only remediation preparation; no project/test/Git command has run.

After that yield, add one executable SDK `tools/restore-cargo-lock` using Python
stdlib. CLI: `tools/restore-cargo-lock INPUT_DIRECTORY --sha256 EXPECTED_SHA256`.
Use GITHUB_SHA/GITHUB_RUN_ID/GITHUB_RUN_ATTEMPT from the actual caller. Preserve
the existing policy exactly: the two-name regular/nonsymlink input inventory,
actual SHA check, exact four-field identity, and exclusive Cargo.lock creation
in the current working directory. No alternative graph, destination overwrite,
extra resolution or generalized transfer framework.

Replace all three inline workflow policies with that same helper invocation.
Add committed focused helper tests for a valid transfer, changed payload/SHA,
wrong source/run/attempt, extra entry/symlink and preexisting destination. Tests
invoke the real helper and assert effects without implementing another validator.
Run only these focused integrity checks plus affected YAML/shell/Python syntax
in the existing SDK Nix shell. Preserve all four accepted prose files and all686
Rust bytes; no generation/helper replay/compiler/package/MSRV campaign.

Normal commits after terminal yield; consolidate the unpushed owning build
commit using ordinary autosquash rebase if no other findings require a different
split. Preserve first generator-input commit and separate generated-refresh
commit. Record original/new complete series, commit mapping and precise diff;
no published/base history rewrite. Rebind a new disabled feature-CI preparation
to the final head after all coherent review fixes. Original review/e370 prep
and failed/successful earlier evidence remain immutable.
