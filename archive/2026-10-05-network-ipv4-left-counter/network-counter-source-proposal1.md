# Network counter and inventory source proposal

The source follows the accepted network inventory/counter refinement in
`design.md` and root-owned `network-counter-final-copy.json`. The lead owns
normal hooks, commits/history consolidation, the W rebase, publication and pins.
This proposal authorizes no command execution.

## Intended splits

- V API: seven exact paths in `network-counter-v-api.paths`, proposed message
  `network-counter-v-api.message`.
- V PHP: seven exact paths in `network-counter-v-php.paths`, proposed message
  `network-counter-v-php.message`.
- W: seventeen current paths in `network-counter-w-ui.paths`, proposed message
  `network-counter-w-ui.message`. Include inventory output only if the canonical
  source generator produces a reviewed diff.

The V snapshot is `network-counter-v-source1.*`, from exact
`5d5527a67315c18b595345aa6996d7724c1ed071`. The W snapshot is `network-counter-w-source1.*`, after parent-owned
inventory generation from `e4c49bcdc91b33b7f644a2f125231cb413cf4bf4`; the lead will
preserve the complete draft before rebasing onto current main, which already
contains the separate proxy-addr patch. Historical evidence is not new-head
proof. The snapshot records a dirty source draft with an empty index, not a
commit or publication.

## Source regression coverage

V `network_read_spec.rb` adds four examples: admin Index/Show counts; disabled
availability with retained reserved owned rows; user absence; support absence.
The fixture contains six IPv4 rows spanning owner/interface/reservation cases,
a real export interface, and one registered IPv6 prefix. Existing statistics,
per-network isolation and reservation rows are asserted. Two existing
`ip_address_spec.rb` examples assert included-network admin counters are absent
for user/support without changing visibility expectations.

PHP `NetworkAvailabilityTest.php` has ten real-client/template test methods,
including three new count/escaping/large-capacity regressions. Its existing
inventory/capability test now asserts four groups and the enabled-specific
properties element. Routed-row coverage checks false-only grey treatment,
missing/true state, removed column, retained service/action links and unchanged
detail handling. Large capacity checks actual superscript/unit markup instead
of escaped numeric HTML. The directly affected existing admin-cluster browser
case checks four cells, disabled zero availability and the Enabled icon rather
than the Managed icon.

W source has 24 focused cases across `networks.test.ts` (4),
`NetworksPage.test.tsx` (12) and `IpAddressesPage.correctness.test.tsx` (8).
The six newly added cases cover optional fields, zero/missing data, bilingual
counter descriptions, the distinct editor owned total and false-only badges in
both row/card renderers with retained links/actions and no extra IP fetch.
The existing availability E2E file has six tagged cases (two bilingual network
editor cases, older API, member detached inventory, two bilingual admin flag
cases). Both desktop/mobile projects select them, for twelve prepared browser
executions. Added output images show counts and flags from synthetic fixtures.
These source counts are prepared coverage, not executed results.

## Hosted selection

No local CI, suite, build, VM or capture is requested or performed. After final
exact source publication, use the existing hosted workflows and their native
results/artifacts:

- V `.github/workflows/api-specs.yml`: full/core `network` selects the changed
  `network_read_spec.rb`; `ip-ownership` selects `ip_address_spec.rb`. Require
  the ordinary topic-coverage aggregate. No new file/pattern or model spec is
  introduced, so topic membership remains unchanged.
- V `.github/workflows/webui-phpunit.yml`: ordinary `composer test` includes the
  ten actual-client test methods. V hosted integration selectors already map
  cluster forms/admin-cluster scenario to `webui-admin-cluster`; network model,
  resource and networking forms to `network`/`webui-networking-dns`. Generated
  gettext paths retain their existing broader `webui` selection.
- W `.github/workflows/ci.yml`: normal quick quality/types, unit/script/BFF
  suites, production build and Chromium script lane at the final rebased head.
  Existing adopted E2E type coverage includes the changed availability file.
- W `.github/workflows/e2e-smoke.yml`: `e2e:pr:desktop`/`e2e:pr:mobile` select the
  six `@pr-smoke`/`@pr-smoke-mobile` cases. Preserve report/test-results artifacts
  and inspect bilingual implemented screenshots, descriptions/focus, wrapping,
  themes and retained actions. Synthetic responses do not certify a real API.

No test framework, selector, workflow or debt-ledger edits were needed. Browser
geometry, visual contrast and live API/UI integration remain unverified.

## Source preparation and hooks

Root completed API all-plugin locale and PHP gettext generation with exit zero;
only the intended locale outputs changed. The W canonical inventory command completed with byte-identical output:
`nix develop --command npm run docs:inventory` from its root. It writes only
`docs/design/IMPLEMENTATION_INVENTORY.md`; its SHA-256 remains
`537ebeae238449aab23c4d5cdc41d6d780efc25e8a1d4d06d993bc3f10b87f89`. No local audit/suite accompanies that source generator.

V declares Overcommit, with executable installed pre-commit/commit-msg hooks.
Declared checks are Nixfmt, RuboCop, API i18n health, PHP locale health, migration
spec inventory and PHP CS Fixer; custom health hooks and configuration were read.
Use the declared root Nix environment and ordinary hooks, without bypass.
W declares no hook framework in the inspected source; use normal Git, preserving
its own PR workflow. The lead owns any normal-hook formatting corrections.

Schema/migration, allocator/chain/operations, VM source and V flakes are unchanged
in the V snapshot. W package/flake/lock, BFF, structural ledger and Host IP-table
source are unchanged by the refinement. Existing published feature histories and
all configuration/KB runtime sources remain held.

The KB impact remains exactly the pending CS/EN `networking/ip-address-list`
images, showing the grey disabled row without an Enabled column. No capture,
staging or production write is part of this packet.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
