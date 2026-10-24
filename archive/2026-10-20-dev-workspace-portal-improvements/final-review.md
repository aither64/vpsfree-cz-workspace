# Final independent review

Reviewer: retained `reviewer0`, thread
`01a15aeb-d483-7693-ac9b-95a9717f7347`, saved `gpt-6.1-sol`/`xhigh` as verified
by the lead before assignment. No model/effort override or nested agent was used.
Risk: **high**. Lanes: general, architecture/repetition, scope/proportionality,
and risk/compatibility. This is final review of the committed deliverable,
before long integration/browser/package tests.

**Disposition: changes required.** One Blocking history finding and one Important
recovery-display finding remain. The source review does not establish a new
authorization, sanitization, durable-ledger or citation-integrity vulnerability.
The two Advisory observations below do not prevent progress if explicitly
accepted by the lead. Long tests must wait for the Blocking finding and the
required disposition of the Important finding.

## Findings

### F1 — Blocking — Separate delivery recovery from transcript presentation/history

Lane: general; also scope/proportionality.

Affected commits:

- codex-web `2ea01d5fc5672da25cca8d5b45ce6aa7f7c52b70`.
- dev-workspace `3f0eae0071b918c742507bff9f1304d95d698bb7`.

Both commits combine independently revertible behaviors. In A,
`conversation/assets/conversation.js:101` introduces the delivery-failure helper,
and `:1464`/`:1524` replace Send/Queue failure presentation. The same commit adds
team classification/filtering, host-HTML rendering and quiet history controls.
In B, `portal/internal/web/static/app.js:5211` and `:5261` plus the Send/Queue
handlers introduce inline submission recovery, while `server.go:3695` and the
transcript render/filter changes introduce decorated user Markdown and team
presentation. History layout and the receipt-control changes are included too.
The delivery changes can be tested, explained and reverted independently of
Markdown/team/history rendering; neither behavior requires the other to exist.

The packet's shared files and combined browser fixture explain editing
convenience, not inseparability. In the review follow-up the lead confirmed that
no concrete state or contract boundary requires either bundle. The general
reference explicitly classifies unsupported bundling of independently reviewable
changes as Blocking.

Bounded correction:

1. Keep A's public post-attachment hook/type change as its own logical commit.
   Split the current second commit into transcript/team/HTML/history
   presentation and inline submission failure/recovery, with each behavior's
   tests, CSS and reference paragraphs in its owning commit. The citation-offset
   hook test may accompany the hook it validates. Preserve the final behavior.
2. Split B's final commit into transcript/team/Markdown/history presentation
   and delivery recovery/receipt presentation. Move the response-loss fixture
   and delivery assertions/docs with recovery. A combined acceptance fixture
   may grow across these commits; its existence does not require bundling them.
3. Keep one final A dependency update in B and one final B update in C. Amend
   those existing update groups to the final rewritten heads; do not add
   intermediate pin churn. Preserve integrated upstream citation/pin history
   and the recorded prior-head provenance.

No application redesign, migration, new framework or default-branch rewrite is
needed. A pure split should preserve the final tree, apart from the separately
required F2 fix. Verify the reconstructed final diff and source identities.

### F2 — Important — Confirmed delivery leaves an earlier uncertainty warning visible

Lanes: general and risk/compatibility.

Primary location: B `3f0eae0`,
`portal/internal/web/static/app.js:5196`, `:5221`, `:5261`.
Shared mounted counterpart: A `2ea01d5`,
`conversation/assets/conversation.js:1279`, `:1479`.

Reproduction: Send loses its response and displays the new inline failure
notice. Select **Retry original**, then receive a successful receipt.
`acceptMessageReceipt` changes the attempt to `accepted`, but it does not clear
the earlier notice. The notice still says delivery could not be confirmed and
instructs the user to retry. Later transcript confirmation also has no clearing
path for this notice. This presents contradictory delivery information after
recovery and keeps the new distracting warning visible until another composer
submission or page reload.

I executed the actual B `acceptMessageReceipt`/`retryMessageReceipt` source in a
controlled Node VM, starting with the displayed failure and the retained unknown
attempt. After the successful retry its output was:

```json
{"state":"accepted","bannerHidden":false,"banner":"Delivery could not be confirmed. Retry the original submission to check its status."}
```

This is separate from the correctly handled case where observation precedes the
HTTP failure. The current tests cover that order but miss failure followed by
successful reconciliation. In A, inspection shows the same stale notice after
failure followed by automatic transcript acknowledgement: `acknowledgeRetained`
clears the matching draft but never updates `submissionStatus`.

Bounded acceptance for the fix:

- Associate the displayed failure with its original attempt and conversation/
  thread (and action where needed). Clear or replace it when that exact attempt
  is accepted or observed, including successful **Retry original** and later
  transcript reconciliation in both portal and mounted shared UI.
- Confirmation of another attempt/thread must not clear an unrelated warning.
  Keep the failure visible while its outcome is unresolved.
- Preserve the original ID/text/uploads, durable receipt retention, explicit
  same-ID retry, accepted/observed precedence, and current draft/attachment
  safeguards. Clearing a visual notice must not acknowledge a message or remove
  an unresolved retry record.
- Add focused order-sensitive coverage: failure then successful same-ID retry;
  failure then observation/acknowledgement; observation then failure; unrelated
  confirmation; changed draft/attachments. No live turns or transport redesign
  are needed.

The lead acknowledged that B requires a fix after this report. The shared
mounted counterpart should be included in the same bounded recovery correction.

### A1 — Advisory — Final failed enrichment drops a valid last-known count

Lane: general. B `f94b7ce2b77ffac7fdf2d50d211a37a5a6da77fe`,
`portal/internal/web/server.go:1022`, `:1118`, `:1152`.

Early membership preserves a measured same-observation count, but the completed
enrichment result initializes a fresh count map and inserts a count only when
inspection succeeds. On a provider error it replaces that valid cached count
with `runningClustersKnown:false`/zero, even if the same session observation had
a confirmed count immediately before the refresh. Thus the count disappears
when the warning arrives. This is conservative and grants no unsafe controls,
but differs from the design's last-known-count plus independent-error behavior.

Prefer retaining the previous measured value only for the same
`ObservationIdentity`, while keeping the actual failure notice and never
marking the underlying observation fresh. Alternatively record the intentionally
more conservative display choice. The current new tests inspect the minimal
publication, not the final known-to-error result; add that bounded transition
case if preserving the design's behavior. Never reuse another incarnation's
count or the provider cache's slug alone as identity proof.

### A2 — Advisory — Dependency commit body names the superseded source

Lane: general. B `ca56a207044d3f47e6b162284eca525d00bd3757` says
“Select codex-web 441ebee”, while its actual files select `2ea01d5`.
Correct the description during the required history rewrite so it describes the
final citation-preserving dependency selection. The effective pin itself is
correct; this is a misleading commit explanation, not a dependency mismatch.

## Reviewed identity and scope

`dev-session current` from the assigned tracking directory printed exactly
`2026-10-20-dev-workspace-portal-improvements`. Both `DEV_SESSION_SLUG` and
`DEV_SESSION_WORKSPACE` were absent, so the trusted thread-bound developer
binding supplied ownership. An initial invocation from the shared workspace
root found no current session; using the prescribed intended directory resolved
that before any session-file inspection. No conflicting environment identity
was present.

Read the full review packet, final inventory, plan and design, the mandatory
skill and all four references, affected repository AGENTS files and applicable
workspace procedures. The workspace feature's routed procedure files are
unchanged. Checked project documentation entry points, shared reference and
portal/team guides, representative source/tests and integration wiring.
The lead owns roster/settings verification; I made no live roster operation.

Exact reviewed ranges, independently checked against worktree HEADs and
merge-base ancestry:

| Repository | Base | Head | Feature commits |
| --- | --- | --- | --- |
| codex-web | `57972192e30fe52ab33b867c8fe4d171f59a7fd5` | `2ea01d5fc5672da25cca8d5b45ce6aa7f7c52b70` | 2 |
| dev-workspace | `52dcd471186ef874c5c93f4133744195d4815454` | `3f0eae0071b918c742507bff9f1304d95d698bb7` | 7 |
| workspace | `0ea5682410a38fe19627bc731e13894c1e51db57` | `d16483d8cb7041fa786312f05af7e118c66f6649` | 3 |

All three worktrees were clean at those heads. I inspected the complete ordered
commit series, commit bodies/path ownership and complete final changes, rather
than only the tips. The captured final diffs/inventory identify the same files.
The report is the only authored file; no application or tracking-state edits,
commit/ref changes, merges, deployments, lifecycle or live roster actions occurred.

## Whole-history, dependency-stream and migration conclusions

**A:** `bf47be9` adds the optional presentation hook/types;
`2ea01d5` adds browser integration. No removed design iteration, fixup chain,
obsolete compatibility path or repeated dependency-update stream remains in the
complete `5797219..2ea01d5` series. The independently revertible bundle is F1.
**No migrations:** neither commit changes a database, manifest, roster, queue,
submission-ledger, native protocol or lifecycle-journal format. Optional
transcript presentation metadata does not rewrite durable conversations.

**B:** ordered series is `ca56a20`, `df3830a`, `a846b4f`, `b0ff062`, `f94b7ce`,
`df50d90`, `3f0eae0`: shared dependency, preset labels, authorized source actions,
artifact navigation, early index membership, Add-member retention, and the final
conversation bundle. No superseded approach or follow-up fixup remains. The
single logical shared-source update includes Go/Nix declarations and hashes;
there are no redundant intermediate feature pins to retain. F1 requires a split
of the final behavior bundle, not pin consolidation. **No migrations:** source
downloads, raw preview text and display-known/communication fields are additive;
durable session/roster/creation/delivery formats and schema bounds are unchanged.

**C:** `52178b3` compresses instructions; `66a90bf` adds the team family/default;
`d16483d` supplies the final composed pin. These are independently focused.
No obsolete history, fixups or transitional migrations remain. Its one nested
runtime selection also updates the transitive A node; these are one composition
stream, not two separate feature updates. **No migrations:** schema 6 and
retained snapshot semantics remain unchanged. New defaults affect new selections.

The integrated A citation commit `5797219`, B `af4c853`/`52dcd47`, and workspace
`0ea56824` remain intact ancestors. The refresh is semantic reconciliation, not
automatic patch equivalence. Original-text citation offsets, host HTML/citation
fallback and pending older-page repair remain present in the final composition.
No citation parser/history-recovery redesign or durable-state migration was
introduced by the refresh.

Earlier published A `441ebeea0eb3befa91006e2e3de9c73eab1ca32c` and B
`2dc2dc720deb7069f913a9c0381bf7ce5bc72edc` were consumed by initiative
preparation. Preserve those exact identities and preparation evidence. External
release/deployment of those feature heads is unestablished; this report neither
asserts their deployment nor infers that no external consumer exists. No
intermediate feature-pin commit is necessary to preserve a supported schema or
consumer boundary identified in the packet/current sources. Integrated baseline
pin commits are outside the feature consolidation and must remain untouched.

The migration inventory is empty in **every branch**, so there are no migration
versions requiring merge/release/deployment/external-use lineage retention, no
transitional migration to squash, and no schema-existence guards to justify.
Final history readiness still requires F1 and validation of the rewritten heads.

## Contracts, architecture, security and scope assessment

- **Ownership/consumers:** codex-web owns generic transcript metadata, the HTTP
  hook, classification/filter helpers and mounted UI. Its example remains a
  consumer with nil hooks. The portal imports the shared Go packages and browser
  helpers but owns its application-specific team envelope, Markdown, file mapping
  and custom UI. The workspace composes that runtime through the retained
  vpsFree extension and supplies team policy. Inspected the example resolver,
  portal imports/member wrapper, Nix/Go pins and extension composition at
  `767dfd5`; there is no reversed dependency or duplicated Markdown parser.
- **Transcript identity:** both handler read routes preserve validation and
  TransformTranscript timing, then attachment observation, then optional final
  presentation. The ordinary lead/member conversation resolver installs the
  hook with thread-scoped uploads; member wrappers retain roster/thread checks.
  Presentation uses decorated user text including empty text; canonical text,
  client IDs, digests and attachment identities are preserved. Team envelopes
  and report-tool labels are presentation hints, never authorization.
- **HTML/citations:** existing Goldmark/Bluemonday owns sanitization; the added
  anchor target is restricted to `_blank`, with existing no-referrer/link
  protections. Source-title support remains. Shared mounted precedence is typed
  activity, trusted sanitized host HTML, citation DOM, then ordinary text.
  Assistant/reasoning/plan render/copy use original UTF-8 citation offsets;
  user/artifact source does not resolve citation tokens. Pending-source repair
  and request-cursor tracking remain independent of the active filter. Labels
  use text insertion. No raw browser Markdown is injected as trusted HTML.
- **Source access:** downloads call the same resolver/eligibility path as
  previews, including registered repository ownership, recorded archived final
  objects, exact workspace root, literal Git paths, ignore checks and regular-file
  confinement. Browser input cannot choose an arbitrary Git ref/socket/root.
  Downloads preserve bytes under a finite 10 MiB limit, use attachment/octet-stream
  and sandbox policy, and do not inherit preview omissions. Shared session paths
  remain excluded from generic workspace reads. Source links remain native
  anchors with safe new-tab attributes and line fragments. No new access beyond
  the existing authenticated portal source contract was found.
- **Artifacts:** manifest normalization/deduplication retains ownership; the
  directory projection does not create another path-authority registry. Selection
  generations and aborts bind preview/copy actions to the selected path. Removed
  selections disable actions. Raw Markdown text comes from the bounded preview,
  images are not text-copyable, and invalid UTF-8 replacement is documented.
- **Index:** membership authority still follows complete successful membership
  reads. Enrichment does not grant lifecycle/cluster controls or fresh activity
  notifications. The integer plus additive known flag preserves old-browser
  behavior; unknown clears the new browser's count. Same-observation cache use
  protects reincarnated slugs. A1 records the conservative final-error display
  difference. No dangerous freshness/authorization change was found.
- **Delivery:** retained same-ID submission and server ledger remain authoritative;
  no blind POST retry, new-ID resend, global timeout enlargement or live restart
  was introduced. Accepted/observed state is not downgraded by response loss.
  F2 concerns the new visual notice rather than the ledger. The HTTP/fake-native
  fixture demonstrates its stated contract, not actual App Server restart.
- **Teams/Add:** one parameterized family produces counts 2–6, N+2 specialist
  slots and derived capacity 8; defaults both select `delegated`. Models, efforts,
  access, utility `gpt-6-luna`/low/max1 and existing presets remain intact except
  the accepted count-neutral lead wording. Direct registration continues to
  request zero native children. Friendly names derive actual counts; retained
  snapshots/rosters are not rewritten. Add captures displayed settings, prevents
  overlapping dispatch and preserves the actual form across roster refreshes;
  deliberate role changes still validate. No live member was created/reconfigured.
- **Documentation/proportionality:** lasting contracts are discoverable in shared
  reference, portal guide and workspace team guide; rollout evidence stays in
  session records. No speculative generalized framework is needed or introduced.
  Instruction compression preserves routes and precedence; measured size is
  16,313 bytes under the unchanged 16,384-byte bound. The accepted standalone
  reviewer-default consequence is documented. Scope is otherwise proportionate.

## Independent focused verification

Executed only bounded checks; no browser, full package or live/native integration
suite was started:

- A: `nix develop --command node test/conversation_browser_contract_test.cjs`
  passed. This exercises actual shared module behavior, including composition,
  filters, citation repair and response-loss ordering in the shipped contracts.
- B: focused `go -C portal test -mod=readonly ./internal/web` under `nix develop`
  passed for citation Markdown, source raw downloads, decorated user Markdown,
  same-observation membership cache and actual-handler response loss/retry
  (0.665 s package result).
- B: `TestAddMemberCapturesAndRetainsSelection` passed (0.160 s package result).
  `TestFullTeamFamilyNamesCountsAddressesAndCreationJournal` passed (0.058 s),
  covering the finite family and existing journal decoder/bound.
- B: the controlled Node VM reproduction above confirmed F2 using the actual
  acceptance/retry source; it made no HTTP/live-session request.
- C: direct Nix JSON evaluation confirmed both defaults, all five counts/slot
  values, capacity 8 and unchanged separate utility settings.
- Independently compared JSON lock nodes: B changes only `codex-web`; C changes
  only `dev-workspace` and `codex-web`. Extension and sibling/follows nodes are
  unchanged. Go module/Nix shared revision agree with the reported A head.
- `git diff --check` passed for each complete range; worktree HEAD/cleanliness,
  merge-base ancestry, ordered commit paths/bodies and migration-path inventory
  were inspected. These checks do not substitute for the pending composed build.

## Remaining verification and follow-up

After F1 and F2, inspect the complete revised series/final diffs and effective
pins. Apply the mandatory skill's narrow-fix rule: direct focused verification
can establish a requested bounded correction; a new design or cross-project
contract needs the affected lanes rerun with this retained reviewer. Do not
replace the reviewer or alter saved settings. Update the packet and provenance
to the actual final heads.

The prepared actual-browser run, full composed package/catalog metadata checks,
and exact-head CI remain post-review work through the required fresh utility.
Browser clipboard/download/native navigation, keyboard/context-menu interaction,
large-catalog geometry and narrow layout are not certified by this source review.
The synthetic largest-team journal check does not replace generated final
package/catalog validation. Production POST 502 root cause remains unproved;
the existing bounded GET/proxy observations cannot establish it.

No deployment or feature integration approval is supplied by this report.
Source pins do not prove installed-package correspondence. Preserve the selected
runtime and open session; perform no lifecycle cleanup as a consequence of review.
The lead owns report registration/state reconciliation and assigning corrections.

Session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
