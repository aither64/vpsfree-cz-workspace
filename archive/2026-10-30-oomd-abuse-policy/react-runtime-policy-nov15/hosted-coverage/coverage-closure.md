# Exact final React hosted coverage

One finite post-terminal collection confirmed all four exact attempt1 workflows
succeeded at feature head `8ce6baac538061d5b51b84c09044947a22004435`: CI43766229151,
PRsmoke43766229474, broadPR43766229483 and broadpush43766224260. All10jobs and
every recorded step completed successfully. Raw exact-attempt run/jobs JSON and
ZIP logs remain beside [the detailed gate/source receipt](coverage-closure.json).
No observer, polling, dispatch, rerun or cancellation occurred.

All8PRjobs actually checked out synthetic merge
`5b467b755f2bcdfdc44b3ee1f6616788e2ef385f`. Its Git API parents are exactly
main `88ac13b89d6421c914cd57e18153de1fee6fc7b7` and reviewed feature8ce; its
full tree `8bfb33d90fa05363ef38ebe06994fc38b7849508` equals the reviewed tree.
Each checkout log independently records that SHA. The2pushjobs checked out8ce
directly. This certifies equal complete source contents, while retaining the
different Git checkout identities; hosted assets are not relabelled as the
separately built exact8ce Nix output. No substantive input difference was found.

| Documented gate | Actual successful job/step and result |
| --- | --- |
| Quick checks, types, locales, lint, format, docs and audits | CI Required nonbrowser checks step7 `npm run ci:quick`; docs286/76, E2E206checked/108deferred |
| Root/BFF production audits | CI same job steps5/6; declared critical/high thresholds; both report0vulnerabilities |
| Full root units, scripts and BFF | CI same job step8 `npm run ci:tests`;244scripts,58BFF,365unitfiles/2452tests passed |
| Production assets | CI Production build step6 `npm run build` succeeded |
| Chromium script regression | CI Chromium script regression step8:1passed |
| PR desktop/mobileChrome/mobileWebKit | PRsmoke step7:966passed,909passed,651passed+2skipped respectively |
| Broad desktop/mobileChrome | Both existing automatic runs step7:239passed+1skipped desktop,96passed mobile each |
| Nix installed packages/provenance/contents/source | Reuse accepted exact8ce [package receipt](../postreview-package-acceptance.json) and exact successful source-content drv; no repeat |
| New dynamic views and current captures | Reuse accepted [two synthetic flows/four actual PNGs](../postreview-browser-acceptance.json); no repeat |

The SDK remains a temporary immutable HTTPS development archive. A published
registry artifact must replace it in manifest/lock/provenance/hash before merge.
Deferred type files and skipped browser examples are not counted as executed
coverage. Synthetic views do not certify real backend enforcement, tenant
authorization or mail delivery. No additional E implementation or verification
gap was identified within the assigned development scope. No merge/deployment,
registry or lifecycle action occurred; the session remains open. Original failed
checks, history and old capture provenance remain intact.
