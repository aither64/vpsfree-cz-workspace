# Follow-up copy for simplified legacy settings

Root applied vpsfree-user-facing-writing and both language Humanizers. This
supersedes the legacy form mode/pending/reset copy in the earlier root-copy.md;
React form controls are outside this specific simplification. Preserve existing
threshold warnings, placeholders, permissions and saved-history meanings.

| Context | English | Czech |
| --- | --- | --- |
| Form-wide inheritance help | Leave a limit empty to use the default. | Pro použití výchozí hodnoty ponech limit prázdný. |
| Invalid nonempty value | Enter a positive whole number, or leave the limit empty. | Zadej kladné celé číslo, nebo nech limit prázdný. |
| Current status, singular | Last %d day | Za poslední %d den |
| Current status, plural | Last %d days | Za poslední %d dny / Za posledních %d dní |

Use the existing gettext/ngettext conventions and Czech plural selection. The
actual current windows render Last 7 days / Last 30 days and Za posledních 7 dní /
Za posledních 30 dní. Saved report periods retain their existing event-time
labels. A known inherited value may appear as a numeric placeholder; do not show
an existing custom value as the unknown default after clearing it. Preserve native
number constraints and server rejection; blank alone means null/inheritance.
Remove the requested redundant section and filter without replacement prose.

The two sibling candidate files change only the policy-settings instructions and
explanation. They preserve the earlier accepted files unchanged in nov18-kb-source,
all semantic tags, the original prefix and Accessible-MySQL-and-later tail. The
source owner and independent reviewer must compare this wording with the final
implementation before acceptance. Report22 wording remains pending actual saved
membership/visibility evidence; no no-match claim is introduced here.
