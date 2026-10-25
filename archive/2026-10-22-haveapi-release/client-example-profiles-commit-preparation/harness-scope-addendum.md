# Narrow acceptance fixture scope addition

The source-inspected Go acceptance runner used two explicit saved-description profiles with register/mount/for_version, but the new lifecycle publishes profiles only after finalization. Lead granted owner2 exactly two existing harness/test paths: documentation_acceptance.rb adds finalize(nil) after mount at each legacy-only site; documentation_build_check.rb invokes the actual environment/profile check as a regression. All entries at these sites are already prepared profiles, so finalization does not use a server. Automatic profiles still require a real completed Server.mount. No product fallback or partial publication is introduced.

Add both files to final server lifecycle commit, since their need follows that lifecycle. Original25 accepted source hashes and historical draft are preserved. Final27-path inventory and updated receipt are required after owner2's focused quick/source yield, before commit activation. Source count stays775 because these two files already existed at4dc0. No generation/compiler/listener or broad check is part of this correction.

Before the finding no staging/commit/driver command had started; HEAD4dc0/indexempty, effects evidence under client-example-profiles-commit-20261024T081850Z. Session writer lock rejected direct confirmations; lead accepted relay8c945383.
