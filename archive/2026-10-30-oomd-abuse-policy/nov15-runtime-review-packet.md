# Runtime incident policy: combined final review packet

All intended source is committed, quick checks pass and owners confirm their
commands terminal. The exact ranges below are frozen for combined independent
review. Earlier static-policy and diagnostic reviews remain historical evidence;
they do not certify the new runtime policy.

Assigned to retained reviewer0 under `9b490a34-030c-4b40-a1ad-3274e0ea6176`.
Native turn `01a1e117-91ff-7ba2-adf6-000a7ee3212c` started at 21:23 UTC;
actual Sol/xhigh settings verified. The completed [review](nov15-runtime-review.md)
identified only RUNTIME-R1 and RUNTIME-R2. This packet retains its frozen reviewed
ranges; successor corrections are tracked in the review record and state.

## Request and accepted boundary

The user requested configurable incident escalation, clarified that trusted
site Ruby should make decisions for each qualifying event, then authorized the
final plan with “proceed with implementation.” See the current sections of
[plan.md](plan.md) and [design.md](design.md), which supersede their historical
static-catalog proposals. The intended result includes truthful incident and
mail history, bounded contributor links, readable PHP/React summaries, required
generated clients, site configuration, localized templates and affected KB work.

The runtime callback receives a captured value context once per eligible new
incident. Ruby supplies base limits, requested mode, suppression and reason.
Audited nullable global overrides and explicit VPS overrides apply in that
order; the global mode and stop exemption remain ceilings. The engine owns
qualification, count windows, owner epoch, locking, deduplication, cooldown and
effects. Initial site behavior remains warning5/7days and stop10/30days, with a
new event and 24-hour cooldown required for repeat stops. No burst rule or
quiet-period latch, callback on reads/retries, arbitrary force-stop interface,
parallel policy store, new dashboard or public action/MailLog API is intended.

Any Ruby file makes current limits/status unknown, even with a constant observe
callback. Counts remain live. Historical evaluation fields describe the latest
attempt for the current owner/epoch; they cannot supply current thresholds.
Notice kind, safe historical trigger ID and six-state mail progress are nullable
read-only report fields. Queued does not establish SMTP success; sent does not
prove inbox delivery. Generated notices never contribute counts or re-enter
the ordinary report sender. Source reports retain the first-event explanation.

Contributor mail retains at most five immutable selected slots with no
reselection, same-owner privacy and optional centrally constructed URLs. Action
JSON also preserves the immutable normalized decision/count facts so deleting
a trigger cannot invent legacy limits during queued-stop recovery. Missing
pending sources suppress; queued/uncertain effects reconcile. The documented
legacy incomplete-audit boundary must remain truthful.

Reader updates must precede activating any Ruby file. Go's retained and newly
generated scalar decoder loses null as zero/empty; dynamic-summary interpretation
is explicitly unsupported. This accepted limitation does not authorize emitter
or provider redesign or certify arbitrary installed clients. React merge also
requires a published registry SDK containing the fields. The current immutable
HTTPS development archive is not that release.

## Scope and exact sources

All worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/`.
Owners retain source and review-fix responsibility. Inspect full `git log BASE..HEAD`
and `git diff BASE HEAD`, including the final tree and all commits, not only the
latest change. Package packets below supply full series, diffs, retained refs,
equivalence receipts, quick checks and migration provenance.

| Repository / owner | Base | Final head | Packet |
| --- | --- | --- | --- |
| vpsadmin / implementer0 | 537b0b7c4ce1d8a930c5fd24b8f4317271ae4f02 | 1a0935b2f0ed0c31d00d645922b88396dbdb2c7c | [A](nov15-runtime-policy-package.md) |
| vpsfree-cz-configuration / implementer3 | 5c67e6a010462a850fb6258c486eeef4490c27d5 | 0be59e51d8473ca0b26b4a9cfe49ca3fe6818fcb | [B](owner3-site-policy.md) |
| vpsadmin-go-client / implementer1 | af9a819ca35f6de5556092679b4df7cb72e7aa89 | 87745f1f54b8928620893c6b64cc1ef3a4f2b90a | [C](nov15-clients/review-packet.md) |
| vpsadmin-rust-client / implementer1 | 823a4f8450fce4947310fc81bcdebdca91d9ffae | 3f1b352785e5ccce3fd73f2a19102dbf72bb495c | [C](nov15-clients/review-packet.md) |
| vpsadmin-typescript-client / implementer1 | 2da950a98fa13468b36d03b13fb5e81cca206e0e | 3b98b045684528d0c38cc2abfef012ebf75e3e5a | [C](nov15-clients/review-packet.md) |
| vpsfree-notification-templates / implementer3 | 2cfd218d9152888feea4109f064459078ea9f76e | 6f95fc255d87d850b157935ac5d2f085a4390ac8 | [Templates](owner3-runtime-policy.md) |
| vpsfree-kb-contracts / implementer3 | cb7825245ea786fb0f51c469d1a7dc5c6a1ececc | 5cfb702685810c45eca3bc7d44c579baaff1c83e | [D](owner3-final-kb-source.md), [final source receipt](owner3-final-kb-evidence/final-packet.json) |
| vpsadmin-webui / implementer2 | 88ac13b89d6421c914cd57e18153de1fee6fc7b7 | 8ce6baac538061d5b51b84c09044947a22004435 | [E](react-runtime-policy-nov15/final-review-packet.md), [history](react-runtime-policy-nov15/final-history.json) |

The unchanged HaveAPI generator is `1ef9b204ba45bb261d3334be5c555cc1856b713b`.
The separately registered `vpsadmin-api-advisory-diagnostic` ref is retained
experimental evidence, never a merge candidate or new product source. Its prior
review is linked in [the original-topic packet](nov14-original-topics-packet.md).
Do not reopen or rewrite that experiment as part of this review.

Lead acceptance inspection confirmed clean A/B/template heads and full series:
A is 70 files, +5443/-170 across four commits; B is two files, +59 in one
commit; templates are 21 files, +675 in one commit. Client packet diffstats
separate generated/schema volume from handwritten tests/docs. These counts
describe scope, not a correctness conclusion or automatic line-count limit.

## History, migrations and dependency streams

A's four final purposes are API/runtime/schema/mail (`84b7e07d`), ordinary oomd
localization (`8a907832`), PHP (`38cb2f2c`) and MariaDB documentation (`1a0935b2`).
The final tree equals complete tested `1999086c`; original and rebased ranges
remain preserved. Assess the split and consolidation independently.

The original `20261030180000_add_incident_escalation.rb` bytes remain unchanged
(SHA256 `f1e6bc75aeffb14d2d14676a908fc4332d7f42f79ee29fe54f48def8e2756c7a`).
Additive `20261115120000_add_incident_policy_evaluations.rb` has SHA256
`b9d894772f61c65dd40952db0eacc04783cbc940144377f1a783d34b2a4a441c`.
Known disposable and exported-schema consumption does not establish production
schema use; durable external use remains unestablished, so the original is
preserved conservatively. No schema-existence guards or guessed override reset.
Full lineage and previous source are in `nov15-runtime-final-history.json`.

B and templates each have one logical feature commit and no migrations. Each
client has one final generated stream and one handwritten test/docs commit,
with no client migrations. TS's third commit contains only the final archive
and provenance: packed source `05c443c4` differs intentionally from delivery
`3b98b045`. The archive is 341951 bytes, SHA256
`24cf8549246e5beb14652639b911768041e3bd38197fa2a7ac7dbaee8604cb43`.
Old consumed archive refs and preconsolidation source remain available; their
obsolete archive contents are absent from the final source series.

All three clients use the same final raw schema `efff42fb…`, provenance
`619ebab3…` and tooling lock `2e9a124e…`; exact hashes, unchanged generator/runtime
inputs and whole-file inventories are in C's packet. Go's bounded OAuth
projection is documented separately. KB consolidates its five backend pin files
to A1a0935, with all other lock nodes/edges unchanged. The screenshot fixture
copies only the accepted B policy (SHA256 `f80804159bebf631501dceebfcd9db87842aed6cac7cabb2b38b7ec8a4bffd8f`)
into the existing public test configuration. Other topologies retain the
missing-file fallback.

KB's complete series is runtime repair `91d349c8`, final five-pin update
`9e0dcff9`, and screenshot fixture/docs/source-check registration `5cfb7026`.
The existing runtime repair is unchanged from its earlier reviewed source;
preserve the prior tracker/ack-loss review conclusions, runtime ownership and
recovery contracts while independently judging the full final branch. The new
fixture commit changes four files, +44/-1, including adding its Ruby file to
ordinary syntax checking in `bin/check`. The complete KB range is 21 files,
+1067/-213. No migrations. Existing media are retained historical evidence.

React's complete three-commit series is final SDK selection `ee9f1036`,
application/tests/docs `628476b3`, and retained historical media evidence
`8ce6baac`. Source tree `8bfb33d90fa05363ef38ebe06994fc38b7849508` equals the
preconsolidation and final staged tree. Original `bbd820a6` and obsolete SDK
references remain preserved; one final SDK stream replaces the earlier pins.
No React migrations. Historical PNGs do not certify the current implementation.
The whole React feature is 51 files, +1759/-47 plus four PNG assets; the packet
also separates the new runtime-policy delta from retained reviewed behavior.

## Evidence and documentation routing

Use each packet's exact check scopes. A's 136 related application examples and
14 DB-free exporter examples passed; runtime/mail coverage is 19 unchanged
passes plus two repaired/remaining cases, with two separate deletion controls.
It is not one invented aggregate suite. B's real loader/finalizer equivalence
passed in three modes without DB/bootstrap/deployment. C's generation, TS18
tests/strict packed consumers and Go/Python/Rust6 focused plus provenance,
refusal and deterministic checks passed. Template render/checker controls and
actual producer checks are distinct. D's scoped projections do not prove a
running policy or new captures. E's corrected batch `1b3754b4` passed full
typechecking, eight focused test files/107 tests, E2E core types (206 checked,
108 deferred), docs audit and dependency prefetch in 97.175 seconds. The prior
batch failed at test-file typing; only erased type declarations changed, with
identical emitted JavaScript. Its failure remains separate evidence. E's final
source-input proof retains all 31 frozen hashes; only the actual Nix dependency
hash and dated verification log changed afterward. The affected source-content
check and docs audit passed, and final Nix evaluation retains the exact checked
source-content derivation. See `react-runtime-policy-nov15/final-input-equivalence.json`.

| Topic / reader and class | Authoritative home | Evidence and limits |
| --- | --- | --- |
| Policy/ownership/effects/history, API developers and operators; reference | vpsadmin `docs/incident-escalation.md`, linked from docs index | A source/specs; preserve source-only explanation, queue recovery, reader-first activation and legacy limitations |
| Site configuration, operators; configuration and reusable operations | configuration `configs/vpsadmin/api/README.md` | B real loader and shared config transport; no activation claim |
| Nullable wire fields and selectors, SDK contributors; reference/how-to | Go README and TS/Rust `docs/development.md`, linking owning API/export docs | C real generated inputs, consumer tests and explicit Go limitation |
| UI behavior and SDK dependency, WebUI maintainers; reference/how-to | E's existing design handbook, requirements, API/client/packaging guides | E's final packet links exact checks; dated work log owns individual execution |
| Template interface, template maintainers; reference | template README pointer to owning backend reference | Protected selection/fallback/retry facts preserved in A; D render controls |
| Capture setup, KB contributors; reusable operations | KB `cluster/README.md` and runtime contract | Screenshot-only fixture source proof; actual runtime and image acceptance pending |
| Member incident guidance; KB reference | Existing EN/CS incident-page local candidates linked from D packet | Main-agent wording complete; production revision not established by body-only fetch; full inventory/release preparation pending |
| Exact revisions, operations and review evidence | This session's packets/state and receipts | Individual execution, not reusable product guidance |

## Review and later gates

Risk is HIGH: automatic stop effects, persisted audit/schema, ownership privacy,
public nullable contracts and mixed-version activation. Select retained
`reviewer0`, Sol/xhigh/read_only, for all four lanes: general, architecture and
repetition, scope and proportionality, risk and compatibility. Read the current
mandatory-change-review skill and all lane references. No nested reviewers.
Require explicit whole-branch history, repeated-stream consolidation, migration
lineage and documentation placement/preservation conclusions. Start with the
user request and proportionate scope; the internal design does not expand it.

Blocking and Important findings follow the skill's reconciliation policy.
Owners make fixes. Direct narrow corrections receive focused verification;
new design/contract behavior returns only affected lanes to the same reviewer.

Long integration, React browser/usability evidence and affected bilingual KB
captures follow review. Historical backend CI failures and the primary scenario's
unknown outcome are not waived by isolated controls or current quick checks.
The November14 diagnostics remain scoped nonreproduction, with original receipts
retained. Review must identify remaining gaps without claiming execution.

React and KB pushes are held at this source gate because they trigger long
workflows. Feature publication remains authorized after review. Default-branch
integration, registry release, deployment, production KB writes and session
lifecycle actions are not authorized. Keep the session active.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
