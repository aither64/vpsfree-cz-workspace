# Wait through upload card repaints in Selenium

`mountUploads` replaces card elements as status changes. A Selenium acceptance
assertion that finds a card and then reads its text can encounter
`StaleElementReferenceException` between those operations. Add that exception
to `WebDriverWait` ignored exceptions so each poll finds a fresh card; keep the
state assertion intact. Both actual portal forms passed 16 acceptance checks
after this harness correction.

Initiative: `work/2026-09-16-portal-upload-recovery/`; fixture and browser script
there preserve the reproduction.
