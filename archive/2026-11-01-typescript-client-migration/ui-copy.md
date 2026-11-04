# Migration copy

Lead-authored after technical reconciliation and direct application of
vpsfree-user-facing-writing/humanizer guidance. Terminology resolved from the
WebUI locked vpsAdmin input `a65a4dfeb92a59df4a80a737a20bcbf8558793ff` at
`/nix/store/030czw9xwvihmw4l24p97d5r2xxd71vi-source`, not the newer API schema
capture input. Exact key placement follows existing catalog ownership; W owns
shared catalog changes, domain owners consume keys. These messages are approved
copy for the corresponding settled behavior, not permission for new behavior.

| Suggested key / use | English | Czech |
| --- | --- | --- |
| `errors.settings_path_unsupported` / local settings adapter error | Server settings sync is unavailable: the configured settings path must be /webui_user_settings. | Synchronizace nastavení se serverem není dostupná: cesta pro nastavení musí být /webui_user_settings. |
| `filters.unsupported_text_search_removed` / reset old traffic/user-data URL search | Text search is unavailable here. The search filter from this link has been removed. | Textové vyhledávání zde není dostupné. Filtr vyhledávání z odkazu byl odstraněn. |
| `admin.help_boxes.filter.unlocalized_removed` / reset unsupported unlocalized-only URL filter | Filtering for help boxes without a language is unavailable. The language filter from this link has been removed. | Filtrování nápověd bez jazyka není dostupné. Filtr jazyka z odkazu byl odstraněn. |
| `admin.help_boxes.validation.language_clear_unsupported` / localized edit clear | The language of this help box cannot be cleared. Choose a language or keep the current one. | Jazyk této nápovědy nelze odebrat. Vyber jazyk nebo ponech původní. |
| `admin.user.payments.paid_until_clear_unsupported` / populated date clear | The paid-until date cannot be cleared. Enter a date or keep the current value. | Datum „Zaplaceno do“ nelze smazat. Zadej datum nebo ponech původní hodnotu. |

Do not echo an arbitrary configured path, secret value or payload into an error.
Use the shared stale-search message only when that URL filter was actually
removed. Existing untouched dates/languages remain valid. Reuse accurate existing
conflict, required-field and unknown-value messages rather than adding duplicates.
Host-assignment confirmation copy will follow its final actual parent-interface
view and placeholders; no arbitrary target selection is implied.

## Additional settled controls

| Key / use | English | Czech |
| --- | --- | --- |
| replace `admin.host_ip_addresses.assign.help` and `admin.ip.hosts.assign_help` | The host address will be assigned to the network interface where its parent IP address is routed. | Host adresa se přiřadí k síťovému rozhraní, na které je routovaná její nadřazená IP adresa. |
| replace `admin.host_ip_addresses.assign.interface_required` | The parent IP address has no available routed network interface. | Není dostupné rozhraní, na které je nadřazená IP adresa routovaná. |
| `admin.host_ip_addresses.assign.route_changed` | The parent IP address route changed. Review the current interface before assigning the host address. | Routa nadřazené IP adresy se změnila. Před přiřazením host adresy zkontroluj aktuální rozhraní. |
| `admin.security_advisories.validation.revision_changed` | The advisory changed since it was reviewed. Unsaved edits remain in the form. Reload and review the current version before continuing. | Bezpečnostní upozornění se od kontroly změnilo. Neuložené úpravy zůstaly ve formuláři. Před pokračováním načti a zkontroluj aktuální verzi. |
| `admin.security_advisories.validation.revision_unavailable` | The advisory revision is unavailable. Changes cannot be submitted until the current advisory is loaded. | Revize bezpečnostního upozornění není dostupná. Změny nelze odeslat, dokud se nenačte aktuální upozornění. |
| `admin.security_advisories.validation.language_profile_unsupported` | The API requires a language this client does not support. Update the generated client before submitting changes. | API vyžaduje jazyk, který tento klient nepodporuje. Před odesláním změn je potřeba aktualizovat generovaného klienta. |
| replace `lifetimes.state_log.hint` (supply real `{limit}`) | Showing up to {limit} earliest records. The current API cannot reliably load further history. | Zobrazuje se nejvýše {limit} nejstarších záznamů. Další historii nelze se současným API spolehlivě načíst. |
| `admin.cluster.os_templates.unsupported_filters_removed` | The search, enabled and supported filters are unavailable. These filters have been removed from this link. | Filtry vyhledávání, povolení a podpory nejsou dostupné. Tyto filtry byly z odkazu odstraněny. |

Revision messages describe an existing advisory editing workflow, not atomicity
across several writes. Only use the retained-draft message where the form really
keeps the unsaved values. For a non-form confirmation use the same existing
conflict explanation without claiming a saved draft. Lifecycle hint describes an
initial chronological prefix, never the latest entries or a complete history.

| Key / use | English | Czech |
| --- | --- | --- |
| `requests.resolve.template_unavailable` | The selected OS template is unavailable for this request. Choose an available template before continuing. | Vybraná šablona OS není pro tento požadavek dostupná. Před pokračováním vyber dostupnou šablonu. |

Use this only when a required selected template is known to be unavailable.
A failed lookup keeps its existing load-error message. Do not block unchanged
request-correction, deny, ignore, or approval without VPS creation when no
template override is requested. A current unavailable reference may remain
visible as display context, but is not an eligible submitted choice.

## Final review corrections

Locked terminology re-resolved and both guides reread at
a65a4dfeb92a59df4a80a737a20bcbf8558793ff. Main applied both Humanizers after the
review facts settled. These labels distinguish accepted writes from readback
verification; work needing review may include an uncertain send. W inserts exact
consumed keys; i6 owns rendering and mutation guards.

| Key (prefix admin.security_advisories.) | English | Czech |
| --- | --- | --- |
| cve_changes.title | CVE changes need review | Změny CVE je potřeba zkontrolovat |
| cve_changes.body | Some changes may already have been applied. Review the current advisory before submitting more changes. | Některé změny už mohly být provedeny. Před odesláním dalších změn zkontroluj aktuální bezpečnostní upozornění. |
| cve_changes.requested | Requested CVEs | Požadovaný seznam CVE |
| cve_changes.accepted | Accepted changes | Přijaté změny |
| cve_changes.remaining | Changes to review | Změny ke kontrole |
| cve_changes.review | Review advisory | Zkontrolovat upozornění |
| nodes.action.review_required | Review required | Je nutná kontrola |
| nodes.bulk.partial_failure_body (replace) | {completed} node updates were accepted; {remaining} need review. Check the current advisory before trying again. | Přijaté aktualizace nodů: {completed}; ke kontrole: {remaining}. Před dalším pokusem zkontroluj aktuální upozornění. |
| toast.created_without_cves (replace) | Draft created; review the CVE changes. | Koncept byl vytvořen. Zkontroluj změny CVE. |
| toast.saved_without_cves (replace) | Draft saved; review the CVE changes. | Koncept byl uložen. Zkontroluj změny CVE. |

Use the review-required label only for the stopped/disabled state. Preserve any
active continuation label if an actual supported continuation state uses it.
Do not add continuation to make the old copy true.
