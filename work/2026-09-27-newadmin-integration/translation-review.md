# English/Czech localization assessment

Reviewed source: `49c6a51d0b32c4a6d5dd1df426e0bac1d8066115`, fetched from
Kerrycek/clankerdev for adoption as vpsfreecz/vpsadmin-webui.

Authority used for this assessment: vpsAdmin
`7045c81b3a5be312eac0d41e8a44f783340abb9f`,
[docs/i18n-cs.md](https://github.com/vpsfreecz/vpsadmin/blob/7045c81b3a5be312eac0d41e8a44f783340abb9f/docs/i18n-cs.md)
and its localization procedure, plus the workspace's English/Czech writing skill.
The planned instructions will resolve this authority from the WebUI's locked
`vpsadmin` flake input, with the site's effective override recorded when used.
This replaces a sibling-checkout lookup and avoids duplicating the glossary.

## Scope and mechanical evidence

This assessment scans all locale source files mechanically and examines
representative English/Czech member, administrator, storage, network and BFF
copy. It identifies fixes and defines the full editorial pass; it is not a claim
that all 8,164 messages have received individual linguistic certification.
Application files have not been edited.

- The repository's `audit:i18n` passes and reports 4,567 keys per language.
- Its regex only recognizes single-quoted keys. Double-quoted catalog keys are
  skipped, so that number is not the full catalog.
- A separate scan of both single- and double-quoted literal entries found 8,165
  definitions and 8,164 unique keys in each language, with matching key sets.
- No cross-language interpolation-variable set mismatch was found among those
  literal entries. This does not check arguments passed by UI call sites.
- One duplicate key has conflicting values in both languages. Object spreading
  hides this conflict in the effective dictionary.

These are source-level results. The implementation should use AST/runtime-aware
catalog checks and rendered regressions, not turn this investigative regex into
the sole production validator. Existing Vitest checks also compare effective
dictionary keys, but cannot detect an already-overwritten duplicate definition.

## Confirmed issues and required changes

All paths below are relative to the new UI repository at the reviewed revision.
Line numbers identify evidence, not the only occurrences needing correction.

| ID | Evidence | Change |
| --- | --- | --- |
| L1 | `scripts/audit-i18n.mjs:7` extracts only single-quoted keys | Check all catalog definitions independent of quote style, detect duplicate definitions, and validate placeholders/plurals |
| L2 | `common/cross_domain.ts:23` and `mailer/crud.ts:39`, both locales, define `mailer.recipients.fields.label` as Recipients/Příjemci and Label/Popisek | Keep the field-label meaning used by `MailRecipientsAdvancedFilters.tsx:27`; remove/rename the obsolete conflicting entry and enforce uniqueness |
| L3 | `src/pages/app/vps/VpsNetworkInterfacesCard.tsx:72` passes `{ n: ips.length }`, while both `vps/network.ts:73` entries require `{count}` | Pass the correct argument and add a rendered check for both locales; review plural handling rather than displaying a raw placeholder |
| L4 | `cs/admin/user.ts:57,58,64,70` calls the account login `Přezdívka`; `src/i18n/index.test.ts:14` encodes that obsolete instruction | Use `Login` for login and reserve `Přezdívka` for Nickname. Fix the test's terminology rule as well as the affected messages |
| L5 | `cs/common/base.ts:62` has `Název hostitele`; `:70` has `Lokalita`; `cs/vps/lifecycle.ts:23` repeats the latter | Use `Hostname` and `Lokace` in the relevant labels, consistently with vpsAdmin |
| L6 | `cs/ops/audit.ts:15,23,24,61`, `cs/admin/user.ts:78-108` and many `cs/vps/console.ts` entries use `sezení` | Use `relace` and natural inflections; use `ukončit relaci` for the end action when that matches its behavior |
| L7 | `cs/storage.ts:148-205` and `cs/vps/storage.ts:70` use `subdataset` | Use `vnořený dataset`/`vnořené datasety`; distinguish recursive descendants (`potomci`) from direct children |
| L8 | `cs/vps/core.ts:118` uses `Zastavené`, and `cs/vps/lifecycle.ts:90` uses `Zastaveno` for VPS power state | Use `Vypnuté`/`vypnuto` as appropriate to the rendered context; do not replace unrelated stopped task/process states |
| L9 | `en/vps/lifecycle.ts:76,80,81,93,96` and its Czech counterpart describe Stop/force generically | Inspect actual graceful/immediate action selection and use Shutdown/Vypnout versus Poweroff/Vynutit vypnutí. Preserve action identifiers and distinct consequences |
| L10 | `cs/common/base.ts:102` uses `Klepněte`; `bff/oauth-error-page.js:7` uses `Zkuste` | Use the established informal singular voice. BFF pages are part of the same user-facing language review |
| L11 | `cs/vps/network.ts:44` says `Nech prázdné pro bez omezení.` | Correct to natural Czech such as `Pro neomezenou hodnotu nech pole prázdné.` after verifying empty-field behavior |
| L12 | `en/vps/lifecycle.ts:75` mentions the detail-header task queue; `:150-152` explains payload fields; corresponding Czech strings mix guest/force/reboot/payload wording | Rewrite member help around the action and its effect. Retain implementation identifiers only where they help an administrator make a concrete decision |
| L13 | `cs/vps/network.ts:73` has one `{count} IP adres` form, and `:80` one `{count} adres` form | Audit count messages and use Czech plural categories; test 1/2/5 rather than relying on key parity |
| L14 | `bff/oauth-error-page.js:14` says `The sign-in response could not be completed.` | Explain the failed sign-in plainly, preserving uncertainty and the available retry action; review the paired Czech message independently |

The duplicate in L2 does not currently prove the wrong text renders: mailer
entries override common entries and the checked call site expects a field label.
The defect is ambiguous ownership and an undetected conflicting definition.

## Areas requiring contextual review

Preserve vocabulary that already follows the guide: many Node, Lokace, Funkce,
Odstávka/Výpadek, Týká se and security-advisory strings are correct. Do not perform
an indiscriminate search-and-replace. In particular:

- Financial bank transfers can be `převody`; network/DNS transfers are `přenosy`.
- A metrics prefix is not necessarily the network Prefix covered by that rule.
- ZFS properties remain `vlastnosti`; VPS features use `funkce`.
- English technical terms such as dataset, namespace, snapshot, mountpoint and
  token are often appropriate. Avoid awkward hybrids when a natural phrase
  already exists, while preserving identifiers and units.
- UI action labels use infinitives. Transaction labels come from API-provided
  labels and use the API's terminology; do not create a second conflicting
  JavaScript translation system for them.
- Plain `Status` and `State` are not automatically interchangeable. Inspect the
  resource/column contract before changing Czech `Status`/`Stav`.
- Preserve permission, destructive-operation, partial-data and uncertain-result
  warnings. Clearer prose must not weaken the operational meaning.

## Required implementation verification

Read the pinned input's i18n guide at the start of localization work; record the
revision and compare it on input updates. The new UI's AGENTS route must make this
mandatory. An unavailable guide is a concrete setup failure, not permission to
guess the vocabulary.

Review all catalog modules, BFF copy and visible literal strings with a coverage
record. Check key/placeholder integrity, uniqueness before spreading and plural
selection, then exercise the affected rendered paths. A dictionary-only test
cannot catch L3. Check fallback/lazy loading, language preference persistence and
accessible names in both languages. Use narrow fixture exclusions in the UI-string
audit, not a broad reduction in product coverage.

The lead owns the final language edit with the writing skill; the implementer
applies agreed technical/call-site changes and the reviewer checks fidelity and
coverage. Follow the independent KB impact workflow for changed member-visible
labels/navigation. No production KB write is authorized by this assessment.
