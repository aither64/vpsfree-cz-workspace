Add administrator Incidents Overview and History alongside the existing Reports page (REQ-051). The readers use the generated SDK and server-provided counts and outcomes. Existing Reports routes and shared pagination remain unchanged.

Overview shows VPS and policy, incident counts, status and the latest outcome in four columns, with secondary facts in Details. History separates the decision and counts recorded at evaluation from the current action and email outcome. More filters retains active values. The long explanatory banners are removed.

The presentation follow-up builds on deployed `ef6c72f4`. It preserves the API readers, authorization gates, cutoff and URL behavior, and distinguishes missing values, explicit restrictions, mail acceptance and confirmed shutdowns. It does not infer an unrecorded reason for no action.

Validation: 37 focused tests, strict typing of the changed code and its real imports, i18n and documentation audits, lint, formatting and diff checks pass. Independent review found no React issues. All four English/Czech desktop/mobile flows passed across two batches; two final desktop capture cases verified the added spacing. The [gallery](docs/work-log/screenshots/2026-11-24-admin-incidents-compact/README.md) shows synthetic data and records the capture revisions. Earlier authorization checks and full-application evidence retain their original scope.

The immutable development SDK remains selected; a compatible published registry artifact is required before merge. This compact presentation has not yet been deployed. The local browser checks do not certify the live API.
