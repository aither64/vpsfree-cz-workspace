# Nov19 PHP usability — KB follow-up scope

Source is the eight-path owner4 delta b2e6cf8c..ea978fe3d4ab5b3b3a0e9b112174a474940fd1aa (tree bee1770ec176c91cad888eda473403a1d0a3885c). Canonical workflow read in full: vpsfree-kb-contracts/docs/webui-change-workflow.md.
No KB source, contract, pin, capture, fixture or production mutation is part of this package.

| Controls/pages | Actual impact |
| --- | --- |
| vps.incidents.menu, vps.incident-reports.menu; navigation paths vps.incidents.open and vps.incident-reports.open | IDs, labels, destinations, report-return behavior and separate intents retained. |
| vps.incidents.page / .policy / .settings / .permission | Remove counting paragraph and System config/category row; show Details content and history directly. Effective numeric prefill uses explicit per-field Inherited/Custom controls, per-field and whole-form inheritance draft resets, pending custom→inherit until authoritative Save/readback. Existing four-column current facts remain. False shared permission remains meaningful. |
| vps.incidents.warning and overview threshold perex | Root warning/stop messages identify incident reports and reached action. Per-policy status includes the already available localized policy label; threshold-only triggers and stop precedence unchanged, no list column or query added. |
| Report list policy_key control | Actual authorized active-registry select with All policies, preserving an exact retired deep-link key as a historical option. Changes clear pagination cursor; VPS/user scope retained. One registry lookup per filter, no per-row fetch. Unavailable stays distinct from a successful registry result. |
| incident-report.policies / .policy / .policy-diagnostics | Heading becomes Matched policies. Keep saved tables/active anchors/retired history. Member-empty remains neutral unavailable because private error outcomes can be hidden. Exhaustive admin false/empty evidence alone permits No matching policies; diagnostics stay separate and private. |
| Notice status/detail/list | Sent/Odesláno replaces SMTP/inbox caveat; no delivery-state or origin/permission change. |

Review both CS navody:vps:incidenty and EN manuals:vps:incidents for the expanded
settings, explicit modes/reset behavior, filter choices and saved membership states.
Preserve original IDs and authorized association-only links; none retired/reused.

Reassess both languages of getting-started/vps-details, getting-started/vps-list
and restore-backups/playground-vps-list. Policy/filter/detail geometry and longer
threshold text affect any associated screenshots; actual final source capture
selection belongs to owner3. Existing zero-count/no-alert and reached states stay.
Six concepts are the existing three bilingual obligations, not six new concepts.

Final canonical five pins, fingerprints, bilingual article/annotation checks and
media/runtime/publication stay separately allocated. This package's actual PHP
render previews use synthetic HaveAPI responses and local assets, not a live API,
VM acceptance or canonical KB screenshot certificate. The inherited 1150px legacy
layout remains; this package does not redesign responsive behavior.
