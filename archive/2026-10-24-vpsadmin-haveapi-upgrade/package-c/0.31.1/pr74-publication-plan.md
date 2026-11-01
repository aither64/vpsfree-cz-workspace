# C0311 own publication and separate protected PR74 plan

New own branch `dev/vpsadmin-haveapi-0311` is published at
`e468ca48406bde1bd99cc42a05e1832fb42162f4`. Actual fresh target/base is
`9113caa0915b2908373ecd616f8f752e779ed4c9`, tree
`13db539707ae88c8635e194ca04f3e36c6e3d76a`. Lead accepted final affected review,
released checks and conditional own publication; all required checks passed.
One explicit no-force own-ref push and independent remote proof completed.
See [final postreview/publication evidence](postreview-results.md). This plan
does not grant protected rewrite, default integration or deployment approval.

Retain published C31 branch `dev/vpsadmin-haveapi-031` at
`baf00acc31d34ab37720643c5833b4476a341f3b`, and original LIVE branch
`dev/vpsadmin-haveapi-upgrade` at
`f10d3d48c4f21cc39187c3667ffffd9952404c11`. Their checkouts/configuration remain
untouched. Retain the old local source877 and all historical review/roots.

Protected PR74 alias `dev/haveapi-async-client` and PR head remain
`5dd2333b9af230d4a81c8f772cbbb08d39b14913`. Concrete old published range:
`7860521f30826c3886c89c35e8ab6f4e082e0a4b..5dd2333b9af230d4a81c8f772cbbb08d39b14913`
(pilot/docs0d05a2584bf30ee4acfa1d64bf00325cdda62934 and5dd2333b).

Concrete proposed replacement range, still requiring explicit published-history
authorization if PR74 is reused:
`9113caa0915b2908373ecd616f8f752e779ed4c9..e468ca48406bde1bd99cc42a05e1832fb42162f4`,
exactly dependency `ea842820d8696a726e3fc408c32e32827ff612b7` and production
`e468ca48406bde1bd99cc42a05e1832fb42162f4`. Source authorship/dates retained;
no migrations or obsolete intermediate pin commits. [Mapping](content-mapping.json),
[full history](commit-series.txt), [final diff](final.diff),
[old/new C31 range-diff](old-new-range-diff.txt).

No PR74/PR63 rewrite, new PR, protected force, default merge or live-source
change occurred. Any later exact-lease operation must recheck its expected old
head and exact new range after explicit authorization; a moved boundary returns
to lead. Publication alone never authorizes merge or deployment.
