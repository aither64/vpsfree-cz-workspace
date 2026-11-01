# C0312 own branch and separate protected PR74 gate

Own0312 branch is published at `2e32c814d3af70ac39257f2542075bd580ee38d4`;
accepted base `9113caa0915b2908373ecd616f8f752e779ed4c9`, tree
`ae4e282a33886faff151818255a99bd5710de832`. Lead accepted final review and released
the complete check/conditional publication package; all checks passed, one
explicit no-force own-ref push and independent remote proof completed.
[Final evidence](postreview-results.md). This grants no protected PR74 rewrite,
default integration or deployment approval.

Preserve published/live e468 on `dev/vpsadmin-haveapi-0311`, baf on
`dev/vpsadmin-haveapi-031`, f10 on `dev/vpsadmin-haveapi-upgrade`, all old source
refs/checkouts/private config and PR74 alias `dev/haveapi-async-client` at
`5dd2333b9af230d4a81c8f772cbbb08d39b14913`.

Old published PR74 range:
`7860521f30826c3886c89c35e8ab6f4e082e0a4b..5dd2333b9af230d4a81c8f772cbbb08d39b14913`
(pilot/docs0d05a2584bf30ee4acfa1d64bf00325cdda62934 and5dd2333b).
Concrete proposed successor range, **not approved for protected rewrite**:
`9113caa0915b2908373ecd616f8f752e779ed4c9..2e32c814d3af70ac39257f2542075bd580ee38d4`,
exactly dependency73070a17e07cfffdf972d85690ffa5011172c53e then production2e32c814.
[Mapping](content-mapping.json), [full series](commit-series.txt),
[final diff](final.diff), [0311/0312 range-diff](old-new-range-diff.txt).

Original authorship/dates retained; no migrations/obsolete intermediate pins.
Observed default40653 is intentionally excluded under the accepted explicit
branch dependency; later integration needs separate baseline reconciliation and
approval. No new PR, PR74/PR63 update, force/default/native action occurred.
