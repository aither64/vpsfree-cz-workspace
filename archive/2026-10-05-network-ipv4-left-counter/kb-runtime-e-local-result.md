# Managed KB provider local checks

The optional provider draft passes six integrated Ruby suites, 34 tests and
215 assertions. Public dispatch adds five tests and 58 assertions, with no
failures, errors or skips. Toolchain, syntax, source and immutable-receipt guards
pass. The tests use actual K93 snapshot readers and immutable D51 source;
lease processes and guest transport remain synthetic.

Canonical `nix flake update dev-workspace kb-runtime` selects published
D51aba080 and K93a16d6. Graph inspection matches D's 17 and K's 45 semantic
paths to their owning locks, including follows, and preserves the five existing
unrelated root graphs. K retains its own V/OS selection.

Receipts are retained under `kb-runtime-e-integrated-quick1`,
`kb-runtime-e-public-quick1` and `kb-runtime-e-inputs1`. Root reconciled README
and the new managed-provider guide. Source commits, clean-tree package
evaluation, independent review and real package/VM proof remain ahead. No
workspace package was activated, no real cluster ran, and no default branch
was changed.

Final committed tree: d2079f605ae87871037ae73c5e5daf20a3e0d03d, above
input-selection ce97027 and base0ff827df. Both normal commits preserve the
checked final bytes; the input commit contains only declarations and generated
lock. Clean-tree six-derivation evaluation passed, source/lock unchanged.
A Nix system-rename deprecation was reported. This is derivation proof, not
package execution or activation. Review and long verification remain ahead.
