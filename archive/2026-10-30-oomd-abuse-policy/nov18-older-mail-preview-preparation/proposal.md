# Older restyled mail — inventory and finite preview proposal

Preparation is complete. Nothing was rendered or sent in this package. The proposed next execution has exactly26 messages, one per changed source/language variant:24 site messages and two explicitly labelled built-in password-recovery fallback samples. All use synthetic data and the existing local Mailpit. The incident-mail table/multiple-policy redesign remains architect0/root-owned and outside this inventory.

[Inventory](inventory.json) records every changed HTML path, language, available MIME parts, immutable source/blob/SHA256, ERB variables, existing H case/render path and proposed unique preview ID.

## Exact scope

The site styling-only commit is `125f132a4c45ea8e8dbf6c392c7ca5f96e15a508`, tree `092c3638f123f1c275f6c48132bd58d344f9a1a4`. Its exact parent-to-head delta is24 existing HTML files across16 older template names. Backend H is the separate two-file password-recovery styling commit `5aa1df7b51fc22c9d35a2d7f6aec889afa54b303`; those two HTML variants and the production builder remain unchanged at accepted backend `0117035f22a465c2b3d78f02df05bc828775afab`, tree `90b3f6101cf089124b77cfe3f0209870a2e986db`. All26 immutable final HTML hashes match the retained H source-parity receipt.

H changed only HTML layout. Subjects, plain parts, metadata, conditions, recipients and operational behavior are preserved. The six pre-existing IP-release reference cards (site CS/EN requested/reminder, built-in EN requested/reminder) were unchanged and are excluded. No HTML is added for plain-only templates. The five new incident families are excluded.

| Source | Template | Languages | Existing parts | Representative input |
| --- | --- | --- | --- | --- |
| site | `alert_admin_monthly_traffic_closed` | EN | subject + HTML | populated logs long duration |
| site | `alert_admin_monthly_traffic_confirmed` | EN | subject + HTML | populated logs long duration |
| site | `alert_admin_unpaid_cpu_closed` | EN | subject + HTML | populated logs long duration |
| site | `alert_admin_unpaid_cpu_confirmed` | EN | subject + HTML | populated logs long duration |
| site | `alert_admin_unpaid_data_flow_closed` | EN | subject + HTML | populated logs long duration |
| site | `alert_admin_unpaid_data_flow_confirmed` | EN | subject + HTML | populated logs long duration |
| site | `alert_user_outgoing_data_flow_closed` | CS, EN | subject + plain + HTML | populated logs long duration |
| site | `alert_user_outgoing_data_flow_confirmed` | CS, EN | subject + plain + HTML | populated logs long duration |
| site | `alert_user_paid_cpu_closed` | CS, EN | subject + plain + HTML | populated logs long duration |
| site | `alert_user_paid_cpu_confirmed` | CS, EN | subject + plain + HTML | populated logs long duration |
| site | `daily_report` | EN | subject + HTML | dense synthetic report |
| site | `expiration_user_active` | CS, EN | subject + plain + HTML | thirteen days overdue |
| site | `password_recovery` | CS, EN | subject + plain + HTML | all four account outcomes |
| site | `payments_overview` | EN | subject + HTML | dense synthetic report |
| site | `snapshot_download_ready` | CS, EN | subject + HTML | snapshot download with expiry |
| site | `vps_oom_report` | CS, EN | subject + plain + HTML | seven total two selected |
| builtin | `password_recovery` | CS, EN | subject + plain + HTML | all four account outcomes |

There are26 HTML variants:16 multipart messages with their existing plain alternatives and10 HTML-only messages. The HTML-only set is six admin alerts, daily report, payment overview and the two snapshot-download languages. Do not manufacture plain alternatives or extra translations.

## Existing rendering and fixture seams

The existing H harness [render.rb](../nov17-html-uniformity/render.rb) loads the unchanged real `MailTemplateTranslation::TemplateBuilder` class and `VpsAdmin::API::TimeZones` without booting ActiveRecord or a database. Its synthetic `Rows`/`OpenStruct` fixtures cover all26 variants and all required dynamic shapes. Earlier H evidence has84 baseline/final comparisons, affected OOM/footer corrections and narrow/desktop visual checks; reuse those for their recorded scope rather than repeating a broad visual/check campaign.

Retained `previews/.../*-after.html` files are useful examples. They are not all guaranteed to include the last footer correction: that correction rerendered only one case for affected variants. The proposed batch therefore renders exactly the selected26 messages from immutable final source instead of blindly sending historical HTML. It preserves the old harness, outputs, sources and all accepted demo artifacts.

`MailTemplate.send_mail!` is a production application sender that saves MailLog and resolves recipients. Invoking password recovery, monitor, expiration, payments or snapshot transaction producers would create real application effects. Neither is needed. The API MailTemplate resource provides management CRUD, not a nonmutating preview seam. The ordinary nodectld sender shows the MIME contract: UTF-8 text/html or multipart/alternative and SMTP. Reuse that MIME assembly with direct capture-only SMTP, without invoking a node command, product producer or transaction chain.

## Concrete next execution proposal

Owner: implementer0. Source inputs stay literal125f and011; no application/Git/config/template-DB change, build, reset, new fixture, service restart or source synchronization. Root assigns a short exclusive preview/Mailpit-write window if approving this proposed execution. This preparation itself authorizes no such effect.

1. Create one new execution-only plan/harness outside every accepted evidence home. Read the exact source blobs and real builder/TimeZones identified in inventory.json. Reuse the H fixture shapes but redirect outputs to the new home; never execute the old output-writing loop against its H evidence directory. Pure rendering must not boot the API or load its guest-ruby wrapper, which loads the application. No test database or new Nix shell/build is needed: select an already installed compatible packaged Ruby and its existing gems in the released execution window.
2. Save26 unique preview IDs/Message-IDs and the complete source/fixture/recipient plan before sending. Pure-render exactly26 subjects/HTML bodies and16 existing plain bodies. Parse the resulting MIME offline and reject missing parts, unresolved ERB, duplicate IDs, source mismatch or nonsynthetic envelope addresses before any SMTP submission. This is the smallest control for the actual preview payload; no broad checker,84-case rerender or application request is needed.
3. Freshly bind only the exact running cluster and services guest's existing Mailpit SMTP127.0.0.1:1025/HTTP127.0.0.1:8025, with no pending operation. Snapshot existing Mailpit message identities privately. Do not assume the earlier41-message total still applies or rescan demo acceptance. Keep sender/recipients entirely synthetic (`previews@example.test` and per-message `older-html+<source>-<template>-<language>@example.test`), cc/bcc empty, and use deterministic Message-IDs under `devcluster.test`. Preserve actual rendered subject/body; source/case identification belongs in envelope and X-Preview headers and the index.
4. Submit one finite ordered26-message batch through the services guest's capture-only SMTP, stopping on first failure or uncertainty. Record an attempt marker before each send and its actual acceptance result. Reconcile an uncertain send by exact Message-ID in Mailpit; do not blindly resend. No password token/recovery, payment, alert, snapshot, owner or VPS record is created. Direct capture mail has no application MailLog/transaction-chain provenance; do not present it as a product-triggered delivery test.
5. Read back the26 exact Message-IDs and map them to Mailpit IDs/deep links. Verify UTF-8 subjects and expected HTML/plain parts against rendered bytes, one captured message per planned ID, and continued presence of every pre-existing message. Supply a compact source/template/language → actual Mailpit-link index so the user can open them. Reuse existing H layout evidence; no new automated screenshot campaign is proposed. Leave all messages and the cluster/session running/open.

Use a fresh current-policy Luna/low utility if the released native phase is long or uncertain; none was needed for these bounded reads. Parent retains authoritative command/effect ownership through terminal. No production SMTP address, forwarding, external recipient or real member data is an input.

## Representative synthetic data

Use fixed synthetic time `2026-11-17T12:00:00Z`, Europe/Prague formatting, `sample-member` user123 and VPS456 `sample.example.test`, node `node.example.test`, and inert `https://vpsadmin.example.test/` action URLs. These are preview fixtures, not current demo objects or working action links. Use reserved test email/IP names and no actual reset/download token.

- Alerts:12 samples at one-minute intervals ending at the fixed time and a2-day+1-second event duration. Choose unit-faithful synthetic values: monthly traffic12.5×1024^4 bytes; unpaid-CPU idle15 → shown usage85%; data flow40×1024^2 → shown40Mbps; paid-CPU usage125%. Use the correct user versus VPS object shape for monthly versus other alerts. This exercises logs/truncation/duration without raising a monitor event.
- Password recovery:one message per source/language contains all four outcomes (recoverable, administrator, no_mfa, unavailable), including escaped sample login text and a fake `.test` reset URL with a synthetic token. No recovery request or token is generated.
- Expiration:13 days overdue, monthly amount300CZK, consistent paid-until/expiration dates and a membership with synthetic ID123. Existing QR image URLs remain template output; previews need no external image requests to render or send.
- Snapshot:synthetic dataset/snapshot names and download ID12, expiry one hour after the fixed time, no archive/download creation.
- OOM:seven total reports/two shown, one missing killed-name field, five remaining; no actual OOM event or policy action.
- Daily/payment reports:dense H-shaped in-memory rows, both assigned/unassigned payments and optional security/session sections. Stub any fixture-only User lookup to return the synthetic object; no database/network call is allowed.

## Acceptance and stopping conditions

Accepted preparation:exact26-variant inventory, all26 H hashes equal immutable final sources, concrete render/data/transport seam and finite proposal. Current package has no runtime/render/send result.

The proposed next package would pass only with26 locally captured unique previews (24 site+2 built-in), the expected16 multipart/10 HTML-only structure, an exact source/payload/Mailpit-ID ledger and a clickable index, while preserving pre-existing mail and all frozen demo/H evidence. Any source/runtime/Mailpit mismatch, render failure or ambiguous SMTP effect stops affected mutations for reconciliation. No producer action, broad rerender, build/reset or production delivery is a recovery option within this proposal.

Main incident-template implementation/copy remains separately owned. No technical design decision about its new tables/multiple policies is made here. No application documentation or source change is useful for this evidence-only preparation. Root retains state.md, next allocation and acceptance.

The accepted demo completionf0be152c, manifestaa4f7524 and all482 bound files are untouched; they were referenced without another acceptance scan. Historical preview/H evidence is untouched. Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
