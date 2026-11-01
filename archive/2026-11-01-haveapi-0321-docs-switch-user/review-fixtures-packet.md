# Affected final review: release test fixture correction

Same reviewer0 Astra/xhigh, read_only; retain previous report review.md.
Affected lanes: general/history, architecture/repetition, scope/proportionality.
Production OAuth, master patch-zero guard, public contract/version metadata stay
unchanged, so original risk conclusion remains. Report any concrete risk found.

Failure: original feature CI20/21passed. Stable release41329778485 failed243
examples/2; evidence/feature-ci/failed-41329778485.log lines689-703.
Cold-source fixture copied patch VERSION then implicitly git master. Explicit
--master fixture also copied patch metadata. Correct guard rejected both.
One test file now explicitly uses release-fixture for generic cold source and
normalizes copied tracked text consistently to999.0.0 before detached-master
check. Nonzero0.31.2 rejection remains. Inspect independently.

Old reviewed master209a7ac0..cc06cb8c; new final
391b0190241cf195a69b06f7297d3e4eebec5a83. Full series ff0c2f07,cc06cb8c,391b0190.
Old reviewed stable0e7166a0..c54404c0; new final
9efeadf91d894e01d1d4f4a3e3fc64c6309785c7. Full series9d404273,0116bbe1,c54404c0,
9efeadf9(-x391b0190). Each new delta only release_spec.rb+6/-1. Both worktrees
clean, no target integrations. Old published feature heads retained under
<slug>-recovery-master-ci and -recovery-stable-ci. No history rewrite needed:
no obsolete approaches/repeated updates. Final master/stable only17version files
different. No migrations/dependencies/schemas/persisted formats or provenance.
Comparisons recaptured original bases/new heads. Explicit independent final
history/repeated-update/no-migration conclusions required.

Quick green on both lines: cold-source1/0, master-version-policy4/0 (positive CLI
and nonzero rejection), changed Ruby lint. Master commit hooks/stable diff hooks
pass; stable make release-check validates0.32.1 inputs. Logs
/tmp/2026-11-01-haveapi-0321-docs-switch-user-master-fixtures-quick.log,
-master-cold-fixture.log,-stable-fixtures-quick.log. No long checks/push/rerun after
fix yet. Original OAuth/baseline success remains valid for unchanged code.
No nested review/fixes/long tests; return exact heads/settings and findings.
