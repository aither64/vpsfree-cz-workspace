# 2026-10-27-api-documentation-redesign

## Goal

i'm looking at haveapi-generated html documentation in vpsadmin api. first, since we have introduced new client examples, the languages don't fit on a single line, see image-1.png. maybe we could collapse language variants (sync, async, etc.) into a dropdown menu. or make a better suggestion. further, it might be useful to switch all examples to the selected language... however, I bet this would mess with page scroll position if the user would change the language in the middle of the page. maybe put the global example selection in the sidebar.

secondly, the client examples are extremely convoluted. only the ruby/php/cli examples seems to have kept their simplicity. I dunno, I realize that you're showing how to be thorough and handle errors... but it is making it hard to see the important bits.

all in all, looking at the documentation, I'd be open to a redesign, both visual and functional. API description doesn't have to be a single large page that takes long to load. we could have per-resource pages, for example. and the design could be updated as well... introduce dark/light/auto themes. my requirements are that it must be clear for users. the current version for example has a list of resources and actions on the right and scrolling the content keeps the sidebar in sync. so we need clear navigation.

the authentication as it is leaves a lot to be desired as well -- it allows only http basic. to be done properly, it should use the API's oauth server. although I guess that is a large change.

anyway, if you're going to be changing the design and functionality, I'll need a way to review it, so connect to some development server of yours.

Attached local files (inputs; keep these files outside version control):
[
  {
    "name": "image-1.png",
    "size": 631455,
    "path": "/home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/uploads/files/7b72f3b3-b3fd-434c-aa4b-6ff7ba27ac84/file.png"
  }
]

## Affected repositories

- HaveAPI owns generated HTML documentation, example templates, and browser behavior.
- vpsAdmin is the integration consumer and source of the realistic review API;
  application changes are conditional on the designer's authentication findings.
- No production deployment, release, or default-branch integration is authorized.

## Approach

Deliver a functional development preview of a clearer API reference. Prefer
resource-sized pages, persistent resource/action navigation, a global example
language selector with compact variants, short idiomatic examples, and
light/dark/system themes. Preserve useful deep links and the reader's position
when changing examples. Investigate the API's existing OAuth support before
choosing the authentication boundary. Keep the uploaded screenshot outside Git.

The retained architect owns investigation and `design.md`. Implementers own
complete packages identified in that design, including checks and commits.
The lead owns coordination, acceptance, user-facing wording, and preview access.

- Security-review communication approval: latest user message after the linked
  2026-10-29-haveapi-security-review session says “well you can coordinate with
  that session and report results to me”. This explicitly authorizes the pair
  with2026-10-27-api-documentation-redesign for audit progress/results. Grant
  b66bb06c5faaeb76ab486ef04209bdcf records the wording/conversation reference.
  Use session_communication leads-only, no peer file/team/transcript access.
  Main collects deliberately shared independent Daybreak findings and reports
  here; no source fix, integration or deployment approval is implied.
- User authorizes audit remediation and a second independent audit: “once the
  audit results are in, asses and implement fixes if appropriate. then rerun the
  audit. if it will report preexisting bugs, those should be addressed as well.”
  Assess all confirmed Daybreak findings, including pre-existing defects; do not
  discard a bug merely because it predates this branch. Architect0 owns design/
  compatibility assessment, implementer1 owns complete correction packages and
  regression checks, reviewer0 owns required final committed change review.
  Main reconciles findings/scope and then requests the independent Daybreak
  audit again on exact corrected source. No speculative source changes before
  findings, and no implicit default merge/release/production/lifecycle authority.
## Decisions

- User explicitly authorizes HaveAPI default-branch integration in the current
  conversation: “let's merge haveapi changes into master”. Scope is HaveAPI
  `master` only and the reviewed published successor
  `aee093cd3387c261570067e58b7f1e16029e3619`; it does not authorize vpsAdmin
  reconciliation, repinning, deployment, release, production, branch deletion,
  or session lifecycle action. Refresh the canonical target, preserve reviewed
  patch/history equivalence if a rebase is required, run the appropriate final
  checks, then use one short HaveAPI repository claim for fast-forward merge,
  normal SSH push and remote proof.
- Second independent audit ofddf confirms original01/02 fixed and identifies
  MEDIUM03CLIhelp shellquoting and04mixed response/copy shell injection. Address
  both under standing user authority;03pre-existing,04oldresponse sinks plus
  redesignwholeblockCopy exposure. Architect settles bounded serialization and
  request/response safety, owner1 completefixes/tests, HIGHall4review, published
  exactsource and another independentDaybreakrerun. Do not treat audit completion
  as a clean-security conclusion or repeat unchanged original work.
- New user milestone2026-10-29: update instructions to prevent future client-
  example formatting regressions. Keep this a bounded developer-guidance change
  owned by HaveAPI, linked from its existing instructions and using its existing
  example guide/checks. Architect0 settles minimal location/content; implementer1
  owns docs/checks/commit/publication after that brief; reviewer0 independently
  reviews the committed final instructions. Preserve applied/deploying style1b
  and keep this follow-up separate from current installed/served acceptance.
  No new formatter dependency, broad client audit, release or default merge.
  Delivered as ae46cf27: exact two files/+55, links/sync/two existing guide
  routes/hooks green, independent general/history review no findings, ordinary
  separate feature publication/readback complete. No cluster repin required.
- Latest user direction2026-10-29: “I tested oauth in the dev cluster and it works
  just fine. Continue deploying formatting fixes.” Adopt published/reviewed
  HaveAPI1b264e25 through the approved vpsAdmin peer's ordinary consumer/update
  workflow. Preserve applied90e2/2f6 recovery, OAuth client/key/config and private
  state. Validate applied identity and representative served example formatting;
  retain accepted OAuth results. This overrides the earlier no-style-adoption
  direction for the dev cluster, without authorizing release or default merging.
  Delivered: applied consumeraae07e62/HaveAPI1b264e25, full installed lineage
  and20 served-format assertions passed; original update/effects reconciled.
- User style follow-up2026-10-29: check every registered client example and
  variant for its own language's quoting, indentation and blank-line conventions.
  Correct PHP's mixed literal quotes and excessive constructor/auth/error-wrapper
  spacing while preserving exact values/escaping and existing useful handlers.
  Keep language-specific choices; do not force PHP quoting onto Python/JS.
  This is a separate milestone in an isolated same-session HaveAPI worktree based
  on accepted2f6. The user explicitly said it must not delay vpsAdmin dev-cluster
  deployment or testing OAuth. Keep active consumer90e2/HaveAPI2f6 rollout stable;
  no automatic consumer repin, rebuild or restart for the style successor.
  Delivered separately as published1b264e25: all15 variants audited, language
  owners corrected, independent review accepted,150 focused examples and63 TS
  units pass, and all11 final CI workflows succeed. The OAuth dev-cluster trial
  completed independently on90e2/HaveAPI2f6. Style adoption is now requested by
  the later user direction above.
- User milestone8 follows the M7 preview: smaller non-displacing copy overlay,
  literal example credentials, less duplicate single-variant selection with
  disabled singleton controls, useful error-handling variants across all clients
  (not just Ruby/PHP), and unquoted string inclusion/exclusion values in code
  markup. The architect audits actual runtime semantics and records the brief
  before source edits. Preserve direct rendering/custom/legacy contracts and
  actual authentication/request proof while adapting the existing acceptance
  fixture to literal examples. Stop old copy-UI reruns; later validation targets
  final M8 and retains existing passing/failed evidence at its actual scope.
- M7 meaningful-detail presentation also requires the existing installed HTML
  acceptance harness to select declared panels, with thorough-to-Simple fallback.
  Preserve its36-panel/six-challenge matrix. Callback Simple setup/auth completion
  is proven by per-run fixture discovery/provider receipts rather than injected
  stdout. This four-path verification follow-through stays with C's HTML metadata;
  no new harness, dependency or product capability is introduced.
- User milestone7 adds generated TypeScript idiomatic typed property examples,
  precise Go response mismatch diagnostics, truthful supported-runtime wording,
  "API client" instead of SDK, resource subresources/current-action
  subsection navigation, authentication-type section links, reference heading
  permalinks and copy icon inside the visual code block. Architect owns exact
  renderer/nav/DOM boundaries before source edits. Existing profile config keys
  and fixed published-runtime gates are not renamed by visible wording. Finish
  the already launched immutable milestone6 installed batch; unstarted remaining
  wire/performance gates target completed/reviewed milestone7 to avoid duplication.
- Runtime versions in examples must not be copied from a hardcoded compatibility
  test pin. Remove the precise version comment rather than inventing configuration
  solely to display it; show a version only if supported by actual client metadata.
  Existing fixed compatibility-test/package inputs retain their real scope.
- Replace the filter-like top-level sliders icon with a conventional settings
  gear; keep one menu trigger and its accessible name/geometry unchanged.
- Slash focuses the existing search field, opening the mobile navigation when
  needed; normal typing/editable controls and modified shortcuts keep their behavior.
- Audit simple/thorough output by renderer and example kind. Offer a detail
  choice only where current examples meaningfully differ; initialization may be
  single-level while actions support both. Preserve saved preferences and direct
  renderer contracts, without adding boilerplate solely to force a difference.
  The selector stays visible and enabled even when only one meaningful option
  remains, as the user explicitly reconfirmed.
- Remove the duplicate content search form from Resources; the sidebar owns
  search, retaining native query/results behavior.
- User review milestone6 supersedes the literal ellipsis and hidden-selector
  choices: search placeholder `Resource...`; Client and Examples selects stay
  visible with only available values. Normalize slashless version roots; make
  documentation account authentication OAuth-only when configured while
  preserving ordinary API/OPTIONS auth and reference examples. `/doc` displays
  the existing README; sidebar resource identity uses dotted paths consistent
  with search, while breadcrumbs may use slashes. Remove the exact Overview
  sentence "The sidebar follows the action in view; breadcrumbs link to parent
  resources." Main approves deletion with no replacement. Architect records
  precise auth/routing/DOM boundaries before implementation. Broad remaining
  milestone5 gates are deferred until the next completed/reviewed source.
- Latest milestone6 title/menu constraint: keep sidebar width unchanged and
  icons beside the title. Use one icon opening one menu containing expanded
  theme choices directly, then available OAuth/account controls. No nested
  theme dropdown, icons below the title or truncation of the required preview
  host/production api.vpsfree.cz label. Arbitrary long configured names may wrap.
- Cross-session authorization source: the user message in this conversation
  beginning "we also have session intercommunication deployed" explicitly says
  "you can coordinate with session 2026-10-24-vpsadmin-haveapi-upgrade" and
  "You'll work on haveapi and the other session will update vpsAdmin API to it
  and deploy it on its dev cluster." It also says "We make no haveapi releases
  yet" and requests development source and resulting HaveAPI bug fixes.
  The later user message "fyi you should use the session_communication tool
  instead of CLI" governs the channel. This is the user's approval for grant
  437ea7ad85f78fbcfeb42f5807633371, not authority from a peer lead.
- Visual review milestone 5 (image-3 outside Git): simplify current-resource
  sidebar context and remove duplicate Vps/vps; placeholder exactly `...`;
  show full parent-qualified resource names in search results; replace the
  sign-in arrow with an Account/person icon. Streamline the entire index/internal
  overview/sidebar hierarchy, remove "API description" and duplicated navigation.
  Identify the concrete API name/label/domain rather than generic documentation.
  Index may use default-version sign-in where auth is compatible (single-version
  vpsAdmin); signed-in Account dropdown shows username, Sign out and Switch user.
  Architect owns the full amendment and supported switch/identity semantics.
- Additional milestone5 requirements: corner copy icons for client examples,
  copying exact currently displayed code with accessible success/failure;
  detail selector only for selected clients that support error-handling detail,
  preserving the saved preference when temporarily viewing single-detail clients.
  No guide-code buttons, clipboard storage/network or client-ID capability list.
- User explicitly authorized official coordination with
  `2026-10-24-vpsadmin-haveapi-upgrade`: this session supplies a development
  HaveAPI revision and fixes HaveAPI bugs; peer updates vpsAdmin and deploys its
  HTTPS development cluster for OAuth testing. No HaveAPI releases. The prior
  OAuth hold is superseded for this scope, including the known narrow R1 fix.
  This does not authorize activating our local TLS/private fixture, inspecting
  peer records/team/cluster, production deployment or default-branch integration.
  Peer owns its cluster/config/input selection and claims. User also authorized
  asking `2026-10-28-cross-session-messaging` for coordination improvements.
- Visual review milestone 4: place account controls beside a compact theme
  dropdown, add a search placeholder, show the current resource in the sidebar,
  and try a readable validator subtable. Search should prioritize resources,
  then actions, then parameters. The user rejected refetching the whole API
  description on each normal page navigation; architect designs compact,
  reusable permission-scoped search data with explicit invalidation and a
  non-blocking load, preserving the normal GET fallback. That design is now
  recorded and accepted in design.md's milestone4 amendment;0/1/3 implement it.
- Search-cache freshness is tied to the page's authorized metadata snapshot.
  Navigation/reload identifies changes; destination pages reauthorize. Do not
  claim instant permission changes while a page remains open. A bounded metadata
  fingerprint pass may trade server work for cross-page cache reuse, subject to
  unchanged performance gates. Prefer ordinary private browser caching over a
  generalized server cache; queries/results stay out of saved preferences.
- The settled representation is a lazy compact HTML JSON data island at the
  existing resources route, keyed by SHA256 of whitelisted authorized metadata.
  Fresh versioned HTML computes that key once; matching keyed responses use
  private browser caching. Cold/conditional network requests authenticate and
  describe before checking the key, with409/no payload for mismatch. Neutral
  pages and BFCache restores bootstrap no-store on search intent. No server
  history cache, page-load bulk fetch, Cache API, service worker or JavaScript
  persistence. These deliberate snapshot semantics require affected final review.
- The user explicitly requires phone/tablet-friendly documentation. Verify
  phone, tablet and desktop widths, touch/keyboard menus and search, readable
  examples/validator subtables, local table/code scrolling and no page-wide
  horizontal overflow.

- Visual review milestone 3: explain validator meaning and format allowed values
  clearly; compact sign-in UI while showing signed-in identity; explicitly
  distinguish anonymous full-reference visibility from signed-in accessible
  resources/actions/parameters; add quick resource/action/parameter search
  available throughout documentation; group overview links by language and
  explain how to use the reference. Remove the technical Guides section from
  version-specific API navigation. Keep a clearly labelled HaveAPI-internals
  link only in the index sidebar, without the misleading main Documentation
  heading/link. Preserve technical URLs and fix fenced-code rendering.
- Version sidebar order is Overview, Authentication, Resources, with provider
  entries indented beneath Authentication.
- OAuth hold requested by the user: wait for official cross-session messaging
  before further OAuth work or activation. Future coordination is with the
  HaveAPI-upgrade session's development cluster; do not access its records,
  team or cluster before that channel. Keep existing OAuth source/prepared
  private inputs and the HTTP visual preview. This is not a session pause or
  cleanup instruction. Candidate HaveAPI deployment is possible only with
  explicit matching gem/Nix input selection; a source mount alone is insufficient.

- Visual review milestone 2, explicitly requested by the user: remove the
  full-width API-version bar and put version identity in the sidebar; fix
  unreadably narrow validator content; apply one design to the version index
  and protocol/shared guides; compact the theme control with icons; introduce
  hierarchy breadcrumbs and improve resource browsing instead of burying the
  complete list in a constrained sidebar section. Fix Create/Clone active-action
  mismatch at clicked anchor destinations. Architect refines the contracts;
  keep this milestone separate from the original checked implementation.
- The overview must list dynamic HaveAPI client libraries as well as configured
  generated SDKs. All 15 example variants in the selector do not replace the
  library overview/link inventory.

- User addition: examples have a straightforward default and an optional
  thorough version with error handling. This detail choice is separate from
  language and sync/async/client variants.
- Python examples omit the `__main__` guard and unnecessary entry-point ceremony.
- User explicitly asked to take time for a proper design after the observer's
  timing concern. Do not rush unresolved architectural choices to satisfy that
  concern; independent Python cleanup and preview preparation can continue.
- Accepted OAuth milestone: optional confidential HaveAPI documentation client,
  existing provider code+PKCE, fixed HTTPS issuer/callback, encrypted HttpOnly
  documentation-only session cookie, current-user reauthorization, CSRF logout
  and truthful revocation failures. No refresh flow or provider protocol change.
  Isolated HTTPS fixture uses a session CA whose public certificate the user
  may trust explicitly; do not modify browser/host trust automatically.

## Compatibility and deployment

Keep protocol descriptions, generated SDK contracts, database state, and CLI
behavior compatible. Assess old documentation links and browser state explicitly.
OAuth changes must preserve supported clients and avoid credentials in browser
storage or records. Preview deployment must be isolated from production and
have a documented stop/recovery path. Integration needs separate user approval.

## Documentation

Readers are API users, HaveAPI maintainers, and operators serving the reference.
Keep lasting behavior and setup in the owning project's existing documentation;
keep design choices, exact preview revisions, and verification here.

## Testing plan

Use repository Nix environments and mandatory hooks. Run focused generator,
example, and browser checks before committing the final deliverable. Review the
complete committed branch independently, including history and migration
provenance, before longer integration checks. Verify the actual served preview,
navigation, selectors, themes, mobile layout, and authentication behavior.
