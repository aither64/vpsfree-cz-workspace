# H older HTML card layout: committed verification

H implementation and scoped commits are complete; see [final packet](packet.md).
Backend `4f391f06d42f27e5c48ee1bd0a25680be9fd51b0`; site
`dea33d0941efeb8ffc2cd3730631bcecfb342d5a`. Windows returned; no push or runtime
action. The following draft record preserves design and verification history.

Package owner: implementer4. Architect H brief: [design](../design.md#h--existing-html-uniformity-independent-sufficient-to-start).

Source baseline: site `d42ad451db702a4bf7982c3d94369c3e3d31d76a`, backend
`4842e75b17df5453b0c5883dd5d54524bf69b8a2`. The five M incident families,
all subject/plain/meta files, source locales, specs, AGENTS and the live demo
remain outside H. Root owns final visual acceptance and both Git windows;
implementer0 has the first M-only commit windows. Final H commits are listed above; no push.

## Result and protected content

The 32 existing older HTML variants comprise 28 site files and four built-ins.
H changes 24 site files and the two built-in password-recovery variants. Site
IP-release requested/reminder CS/EN and both matching EN built-ins already
conform and remain byte-identical. The complete paths and SHA256 values are in
`source-parity.json`; `site-owned.patch` and `backend-owned.patch` contain only
H changes.

The outer gray body, white bordered 640px card, Arial text, 24px cell padding,
charset and viewport follow IP release. Existing inner styles are scoped to
`.mail-content`, preserving blue data tables and local password action styles.
Fixed presentation-table layout keeps dense content from widening the card.
An inner overflow container preserves long-link wrapping; daily/payment tables
scroll individually where supported. CSS-ignoring clients retain ordinary
visible table content rather than hidden cells. No `overflow:hidden` is used.
The small four-column OOM table uses natural column sizing and 14px text to retain all
actions at narrow width. No renderer, shared CSS framework or new HTML variant
is introduced.

Source checks prove every ERB block and body interior is byte-identical, except
for whitespace immediately before the added closing frame. This preserves
wording, conditionals, interpolation, escaping, footer, links, image URLs,
recipient semantics and template-local helpers. Existing legacy unescaped
interpolations are unchanged; H introduces no escaping or wording correction.

## Verification

- Existing production `MailTemplateTranslation::TemplateBuilder` and TimeZones
  rendered 84 synthetic baseline/final pairs across all 26 changed variants.
  The builder is loaded from its unchanged production class without booting a
  database. Inputs cover empty/populated alert logs and truncation, short/long
  durations, membership reminders at 0/13/14 days and missing paid date,
  password single/multiple accounts and all four outcomes, OOM plural and
  selected/remaining counts, empty/populated payment and daily reports.
- Chromium DOM comparison: all 84 pairs preserve visible text, link labels and
  targets, image alt/source attributes, anchors and data-cell content. Inputs
  are synthetic; external requests are blocked.
- Final normal site `nix flake check` and `nix run .#check` pass: 77 templates,
  393 files. Final builtin checker passes: 60 templates, 197 files. Both Git
  whitespace checks pass.
- Twelve final visuals cover six representative messages at 390px/1280px,
  with matching baseline screenshots. Cards measure 366px/640px and document
  width remains within each viewport. Dense-table horizontal overflow is
  contained; unsupported-client fallback remains a visual-review limitation.

Raw logs, builder harness, DOM results, source hashes and previews are ignored
local evidence in this directory. The checker batch used fresh installed
Luna/low watcher `/root/h_quick_checks` from package
`/nix/store/3shank2g0lxy3xnlh282djq0kjsbzanr-dev-workspace-0.2.0`, catalog
`7659519e2fbe326ba88f3f4e4b07169f291b61a907be06e5b9e374d27fced37e`.
The changed-layout reruns were known quick cached checks. All command sessions
are terminal. One failed browser inspection was stopped with its exact owned
browser descendants; its replacement finished successfully. No server,
production sending, DB/fixture event, runtime or deployment operation occurred.

## Visual review links

[Full before/after HTML index](index.html) links all 84 pairs. Representative
screenshots in `visual/`:

- `daily_report-en-{390,1280}-{before,after}.png`: populated dense report.
- `vps_oom_report-cs-{390,1280}-{before,after}.png`: four-column table and links.
- `alert_user_paid_cpu_confirmed-en-{390,1280}-{before,after}.png`: alert/log.
- `expiration_user_active-cs-{390,1280}-{before,after}.png`: payment and QR data.
- `password_recovery-cs-{390,1280}-{before,after}.png`: all account outcomes.
- `snapshot_download_ready-en-{390,1280}-{before,after}.png`: simple long URL.

No project documentation update is useful for this styling-only change: existing
template structure/check instructions remain correct. No schema, API/client,
persisted-state or migration change; deployment is ordinary template-source
replacement/reconciliation, separately owned by root. Old saved MailLogs remain
unchanged. Rollback uses the previous template source.

Next: lead final acceptance and independent affected-lane review when the combined
deliverable is complete; feature publication remains separately directed.
No default integration is authorized. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/

## Root visual follow-up

Root accepted the overall outer card and content, requesting short OOM action
and link words remain whole at 390px plus a proof of dense-table scrolling.
Only site OOM CS/EN CSS changed: natural table sizing, normal word wrapping and
4px cell padding keep `Podrobnosti` and `neukončeno` whole. The affected twelve
paired renders and DOM parity checks pass; corrected CS/EN 390px samples retain
a 366px card and no document overflow. Unaffected render evidence is retained.
`daily-scroll-proof.json` proves all 43 overflowing daily-report tables across
390px/1280px reach their rightmost cells after scrolling to the exact maximum.
`visual/daily-first-table-{390,1280}-scrolled-right.png` supplies visual proof.
The original full-site receipt predates this two-file CSS adjustment; M's 35
files and every other source input remain unchanged. Owner0 was notified.
