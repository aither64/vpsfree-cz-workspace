# Affected legacy node-form layout review

The latest real browser attempt passed 11 cases and failed at the Add checkbox
because the sidebar intercepted its click. The lead accepted a scoped native
horizontal scroller. Implementer1 completed the three-path source/quick package;
implementer0 inspected it, amended B with normal hooks, and refreshed the single
KB pin. Both successors are committed, quick-checked and pushed. Affected review
gates strict final KB and real legacy retry; neither has run on these heads.

## Exact ranges and consolidated series

API target master, base
`097226b22edf8b59f80b5dfaa55265e9d0cac633`, final head
`49f5a29e5a7d85559d06d31496acb5c08895bcda`:

1. A `9415cf2855a3f9caef6ab68dc7df8405ed9f3ef8`, exact unchanged object.
2. B `49f5a29e5a7d85559d06d31496acb5c08895bcda`, advisory WebUI management
   with the scoped layout correction folded into its owner.

Affected comparison is
`006454821ee35b291def4bfafee19cd0553bc7b2..49f5a29e5a7d85559d06d31496acb5c08895bcda`.
Exactly three files differ, +12/-1: form creation name, five CSS lines, six
existing-case regression lines. Final tree
`0ac9a9144e394a8c963db71a49d059e48ebec23c` matches an independent alternate-index
reconstruction of `006454` plus this exact patch. No other implementation/fixup
commit remains; prior tested source stays under the own `-pre-layout` ref.

KB target master, range
`ce2c8cd9358c3636e5d39343e595df813a0b197f..5276b64b9cab0d29bc14968730eccf88c230059d`.
Complete series is one five-pin commit, +8/-8, selecting exact API `49f5a29e5`.
Only the selected vpsadmin lock node changes, with all unrelated nodes, root
follows, selected-node edges and explicit OS
`6bdf458fd9105379860234ff33d352e55844f08f` preserved. Capture/page provenance,
content and assets are unchanged. No obsolete repeated pin stream remains.

Both worktrees/indexes are clean. Fresh targets stayed `097226b` and `ce2c8cd`;
SSH lease-push plus independent remote head proof succeeded. Comparison snapshots
were refreshed. NO MIGRATIONS, schema, API, mail, authorization, deployed/default
history or session lifecycle change. Earlier reviewed/tested ranges remain
evidence, not new execution claims.

## Failure and bounded correction

Real `006454` legacy output: 11 passed, 1 failed, 6 did not run. The membership
case at spec line 478 found `node_101_add` visible/enabled/stable, but the sidebar
helpbox Edit link repeatedly intercepted its pointer. The lead assigned the B
owner the layout diagnosis and rejected forced clicks, hidden sidebar, changed
viewport/deadline, input-size reduction and general CSS changes.

The standalone form's auto-layout table has seven columns and exceeds its
805px available content width. The added rightmost Actions column can lie below
the 300px sidebar. Cell overflow does not contain the table. The correction:

- Gives only `security_advisory_node_form()` the existing form helper's name
  argument `security_advisory_nodes`.
- Adds only `form[name="security_advisory_nodes"] { max-width: 100%; overflow-x:
  auto; }` in the existing main stylesheet.
- In the existing membership case, checks the named form's bounds against the
  content and retains the ordinary checkbox check and normal form submission.

All columns, size-14 inputs, field names, hidden revision/state values, membership
semantics, sidebar, JS and request payloads remain. Embedded creation form layout
is outside the selector. The owner found no conflicting form-name selector or
generic-form JS dependency. No new visible text or localization change.

## Quick and visual evidence

PHP syntax, declared php83 PHP-CS-Fixer (zero offenses), JavaScript syntax,
three-path/whitespace checks passed. Implementer0 independently inspected the
complete diff and viewed the owner's screenshot. Normal root Nix amendment hooks
passed in 65.52s, including PHP formatting, RuboCop and both locale health checks.

The owner rendered the actual PHP form/XTemplate/main and scheme CSS using
synthetic API objects and existing packaged Playwright/Chromium. At 1280x720:
form/client width 805px, table/scroll width 970px, content/form right 885px,
uncontained table right 1049.921875px. Scoped overflow keeps the form at 805px;
normal checkbox check naturally scrolls it 165px, table right becomes
884.921875px and the checkbox is checked. Input size 14, published state and
revision 9 remain. This is synthetic layout evidence, not real API acceptance.
The screenshot shows the implemented layout after this normal interaction.

Owner receipt: `legacy-layout.md`; screenshot: `legacy-node-layout.png`.
Measurements: `/tmp/2026-11-01-advisory-layout-result.json`. The initial synthetic
launch lacked default headless-shell; selecting the already-used explicit full
Chromium binary corrected only temporary launch setup. That result and the
declared formatter selection are retained in the owner receipt. No dependency,
framework, collector or production request was added. Browser/utility exited.

## Inputs, retained evidence and remaining checks

Raw amendment/proof files live under
`/tmp/2026-11-01-published-advisory-corrections-acceptance/layout/`: exact patch,
final delta/range-diff, status and normal hook log, API metadata/actual shell
derivation, `reuse.json`, and KB old/final graph/quick metadata. API subtree and
test-runner subtree equal `006454`; A is the same object; actual API shell
derivation JSON equals the original verified derivation, and the full locked
graph is equal. Original full/core88/79, client298 and modern evidence is retained
for its actual source/environment/derivation scope. WebUI layout intentionally
changed and still needs real browser verification; no reuse claims that passed.

Prior first strict fixture, readiness and notification-selector failures plus
their limits remain in `api-acceptance.md`. Latest 11/1/6 native files were
snapshotted separately under `notification-diagnosed/native-failure/` before
the deterministic native directory could be reused. Guest screenshot/trace paths
did not survive destruction, so no guest visual inspection is claimed. Native
services/node1 each record QEMU exit 0 and destroy; node2 never started and was
destroyed. Exact owned runner-path process scan was empty. No local test is running.

The lead will assign retained affected review of this committed range, then
release strict exact-pin KB followed only on PASS by the real legacy advisory
script. No unchanged long API/client/modern repetition, integration, deployment
or lifecycle operation is authorized here.

Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/>
