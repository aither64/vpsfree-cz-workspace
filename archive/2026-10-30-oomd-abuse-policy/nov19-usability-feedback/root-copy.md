# Nov19 UI copy decisions

Root applied vpsfree-user-facing-writing and the English/Czech Humanizers after
reading the current incidentEscalation locales and the user's requested wording.
These strings preserve current threshold/action distinctions. Reaching a limit
must not claim the VPS has already stopped. Preserve dynamic placeholders,
plural rules, policy names, and real pending/error/uncertain action states.

| Context | English | Czech |
| --- | --- | --- |
| VPS stop-threshold warning | Too many incident reports: VPS shutdown limit reached | Počet hlášení incidentů dosáhl limitu pro vypnutí VPS |
| VPS warning-threshold warning | Too many incident reports: warning limit reached | Počet hlášení incidentů dosáhl limitu pro upozornění |
| Sent escalation notice | Sent | Odesláno |
| Incident detail membership heading | Matched policies | Odpovídající pravidla |
| Empty membership list (only when known empty) | No matching policies | Žádná odpovídající pravidla |
| Any-policy filter | All policies | Všechna pravidla |

Where a policy name is already available, display the localized name with the
warning. Do not add a new policy-specific mechanism just for this text. Keep
information-unavailable distinct from a known empty membership list.

Threshold values must combine a count with its period. For example, the warning
value is `3 reports in 7 days` / `3 hlášení za 7 dní`. Preserve proper plural forms
for dynamic values. Do not print `Warning limit 7 days` as an ambiguous joined
label. The final table/form arrangement follows the architect's existing data
and UI-component assessment; the user does not need a counting explanation.

Delete the requested generic policy-counting paragraph and the SMTP/inbox
explanation rather than replace them with other explanatory prose. Remove the
legacy System config policy-settings row. Remove the Details disclosure label
and keep its content visible, without a replacement collapsed wrapper.

Use the user's Czech word order for relevant restart messages:
`VPS #<id> <name> byl restartován, protože přetěžoval sdílené systémové prostředky a omezoval tak dostupnost ostatních VPS na nodu.`
The existing template syntax, actual ID/name formatting and optional hostname
handling must survive. Do not rewrite stored historical reports or sent email.

The analogous confirmed-stop producer sentence is:
`VPS #%{vps_id} %{hostname} byl vypnut, protože přetěžoval sdílené systémové prostředky a omezoval tak dostupnost ostatních VPS na nodu.`
Retain the source locale's existing trailing paragraph/newline convention.

The user's removal of the delivery caveat also covers its duplicate in visible
warning/confirmed-stop notice bodies. Remove only the delivery-disclaimer clause;
keep the existing factual first sentence in each EN/CS notice, without claiming
inbox delivery. The `sent` status remains `Sent` / `Odesláno`; internal delivery
state, errors and operational diagnostics remain unchanged.

Form-local intent labels approved for both UIs: `Inherited` / `Výchozí`,
`Custom` / `Vlastní`, and `Inherited after saving` / `Výchozí po uložení` for the
pending custom-to-inherit state. A per-field action can use `Use inherited limit`
/ `Použít výchozí limit`. Use the existing member-facing unavailable string
`Policy information is unavailable for this report.` /
`Informace o pravidlech nejsou pro toto hlášení dostupné.`

An empty member policy-evaluation response can hide private error outcomes and
is not proof that nothing matched. Use the neutral unavailable presentation;
reserve No matching policies for genuinely exhaustive saved evidence. Never add
a hidden lookup or expose admin error/skipped rows to establish emptiness.

Final PHP count and validation additions:

- English gettext plural pair: `%d report` / `%d reports`. Czech: `%d hlášení`
  in all three plural forms. Preserve the numeric placeholder and existing
  Czech plural-selection rule.
- Threshold composition: `%s in %s` / `%s za %s`, with the report-count phrase
  first and the existing localized period second. For example, `3 reports in
  7 days` / `3 hlášení za 7 dní`.
- Invalid custom limit: `Limits must be positive integers.` /
  `Limity musí být kladná celá čísla.` Inheritance uses its explicit control;
  zero is not a valid custom limit.
- A failed registry query may reuse the existing `Incident settings unavailable`
  translation. Preserve a selected historical key and distinguish the failed
  query from a successful empty registry.
