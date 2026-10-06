# vpsAdmin KB documentation contract

## Goal

Make navigation text and screenshots in both vpsFree.cz knowledge bases
traceable to stable vpsAdmin WebUI concepts, so a WebUI change produces a
deterministic impact report naming the Czech/English pages, annotated
navigation instructions, and capture checkpoints that require review.

Detection is the first objective. The system must not rewrite or publish KB
prose automatically. All staging and production KB writes retain their normal
review and explicit approval gates.

## Affected projects

- `vpsadmin-kb-captures`: own the documentation contract snapshot, page and
  screenshot bindings, source fingerprints, and the operator-run consistency
  checker.
- `vpsadmin`: expose stable documentation landmarks in rendered WebUI elements
  and keep their IDs next to the label/route definitions used by the
  interface.
- `dokuwiki-plugin-vpsadmindoc` (new standalone repository): implement paired
  `<vpsadmin-nav>` annotation syntax that preserves human-authored visible text
  while exposing stable semantic IDs to renderers and inventory tools.
- `vpsfree-cz-configuration`: package the reviewed plugin revision for both
  production KBs and the on-demand staging container.
- Top-level workspace KB tooling: fetch, validate, stage, and report annotated
  page inventory without bypassing production approval.

## Design

### Stable semantic IDs

IDs describe user intent rather than display order or translated labels, for
example `member.public-keys.add`, `vps.details.set-root-password`, and
`networking.routed-addresses.list`. IDs survive label translation, page layout,
and route parameter changes. Retired IDs remain as explicit aliases or removals
so the checker reports an intentional migration instead of silently losing a
binding.

### DokuWiki annotation

The syntax plugin will accept paired annotations such as:

```text
<vpsadmin-nav id="member.public-keys.add">Edit profile → Public keys → Add public key</vpsadmin-nav>
```

The body remains localized, reviewable DokuWiki prose. The plugin does not
fetch labels from production vpsAdmin and does not rewrite the body. It renders
the body normally with a stable semantic marker and exposes annotation metadata
for inventory/checking. Unknown or malformed IDs produce a visible/editor
diagnostic rather than disappearing.

### WebUI contract

Documented controls and navigation entries receive stable semantic landmarks
next to the definitions that provide their gettext msgid and target route.
Rendered HTML exposes `data-vpsadmin-doc-id`. The capture repository's pinned
contract records the ID, gettext msgid, source fingerprint, affected pages,
and screenshot bindings, then verifies those facts against the exact vpsAdmin
source revision. Capture scenarios prefer the rendered landmarks over
translated-text selectors where available. Keeping the impact contract outside
the runtime WebUI avoids adding an otherwise unused production endpoint or
generated artifact.

### Consistency checker

The operator-run checker compares a pinned vpsAdmin contract, capture bindings,
and locally fetched KB sources. It reports at least:

- unknown, duplicate, retired, or unreferenced semantic IDs;
- label msgid/translation changes affecting annotated prose;
- route or landmark changes affecting navigation instructions;
- screenshots whose scenario/checkpoint is bound to a changed semantic ID;
- missing Czech/English counterparts and unannotated known navigation phrases;
- stale capture provenance relative to the vpsAdmin contract revision.

The report is deterministic and suitable for local use; no GitHub workflow is
required.

## Compatibility and deployment

- Annotation tags are additive page syntax. The plugin must render their body
  as readable text and fail visibly if an ID is invalid.
- vpsAdmin landmarks add HTML attributes and contract metadata without changing
  routes, API behavior, database state, or persisted formats. Old WebUI builds
  and annotated KB pages can coexist; the checker reports a missing contract
  rather than breaking page rendering.
- Capture schema changes must retain all current screenshot IDs and both
  language variants. Existing capture commands remain operator-run.
- Install the plugin on staging before any annotated page is staged. Production
  deployment order is plugin first, then separately approved page publication.
  Rolling back pages before the plugin is safe; rolling back the plugin while
  tags remain published is not allowed unless fallback rendering is proven.
- No production KB write, plugin deployment, or vpsAdmin deployment is
  authorized by this initiative without a later explicit user approval.

## Implementation sequence

1. Inventory current navigation phrases and screenshot/page bindings from the
   completed localization release.
2. Define and validate contract schema and stable ID naming in
   `vpsadmin-kb-captures`.
3. Add initial vpsAdmin landmarks/contract generation for the inventoried
   controls and migrate capture selectors to semantic IDs.
4. Implement and test `dokuwiki-plugin-vpsadmindoc` in its standalone
   repository.
5. Package the plugin for staging and production configurations, build the
   affected NixOS closures, and deploy only through the normal operator path.
6. Generate local Czech/English annotated candidates, run the checker, stage
   after explicit review authorization, and stop for user approval before any
   production page write.

## Verification

- Schema/unit tests for IDs, aliases, bilingual bindings, source fingerprints,
  and deterministic reports.
- vpsAdmin tests for contract generation and rendered semantic landmarks.
- Capture strict validation and selected cluster/Playwright scenarios using the
  landmarks.
- DokuWiki plugin PHP syntax/unit tests and rendered-page tests on the internal
  staging container.
- `confctl` build of the aitherdev staging container and production KB
  container configuration; deployment remains operator-only.
- Mandatory standalone change review after committed quick checks and before
  long cluster/staging integration.

## Durable handoff

- Add a canonical WebUI-change workflow to `vpsadmin-kb-captures` covering the
  cross-repository trigger, semantic-ID decisions, contract checks, screenshot
  regeneration, KB candidate validation, staging, and approval-gated release.
- Link the guide from the vpsAdmin and capture repository instructions and from
  the coordination workspace instructions so an agent entering through any of
  those repositories discovers it.
- Promote reusable all-page fetching, exact replacement-plan application, and
  guarded release-manifest generation from this dated initiative into stable
  top-level `bin/` commands. Keep publication outside the capture repository.
