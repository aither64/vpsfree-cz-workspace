# Reusable creation-time policies — Owner1

Current implementation is uncommitted on backend0117035 and site1efe. Owner1
owns the first backend index window and site declaration; Owner4 PHP/browser
and Owner0 templates/renderer source remain disjoint. No final history fold while
those writers are active. Contract: [design](../design.md#nov18-feedback--reusable-creation-time-policies-and-clear-presentation).

Common model creation now visits an explicit, otherwise-empty registry; node
validation/dedup stays producer-owned. New node RPC uses existing write transport,
bound-node authority and stable token/fact dedup. Read/scheduler paths consume
saved membership only. API adds nullable matched, fixed periods and saved notice
origin; removes active source_type. Migration/schema remain unchanged.

Focused checks retain original failures in this directory. First common rollback
case needed an actual savepoint in its RSpec outer transaction. Same-object retry
then exposed ActiveRecord's cached association scope: reset plus reset_scope is
required after rollback. retry-scope-smoke has five passes and one RPC normal-chain
failure. RPC/API outer source+chain preparation now requests its own savepoint;
rpc-atomic-runtime is its finite recheck plus previously unexecuted runtime cases.
The first new watcher launcher was rejected before execution because its global
approval flag followed exec; launch2 uses the supported global position. No test
was repeated for that launcher error.

Remaining: adapt legacy duplicate-evaluation fixture helpers to creation ownership;
actual parser save/dry-run and real source notification, resource projection,
concurrency, RPC/CLI checks; generic integration fixtures; root prose/locale review;
scoped lint and normal hooks/commits. No long integration, VM, publication or demo
mutation is authorized. Old011 CI, demo and literal5aa1 export evidence keep their
original identities.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/

## Model/API milestone

model-api-regressions ran once:50examples/47passes/3fixture-only failures,
235.4148s, CLI50071/source32283 joined. Actual API one non-OOM report / two
independent policy memberships / one real source MailLog passes. Nullable saved
matched and fixed periods, member/error privacy, retired historical notice origin,
RPC node authority/dedup/CPU-action forwarding/atomic failure, summary and engine
cases pass. Narrow fixes retain failed evidence: freeze the runtime test clock;
seed before deliberately corrupting mode; capture time before Mail.new's
instance_eval. source-concurrency-remainder (fresh CLI11300) checks those plus
actual parser persistence, saved-only task discovery, node authority/report privacy
and concurrent ordinary insertion. No production source changed for these failures.

Owner4 has returned all PHP/gettext/browser source stable with no active handle;
its second Git window remains held. Owner0's static checks passed; its initial
utility marker failure and parent-owned interruption remain literal, and a fresh
finite real renderer/mail batch now shares the production model/helper freeze.
Owner0 owns only four-column assertion changes in the two granted mail spec paths;
Owner1 retains their mechanical common-creation setup. No Git isolation or production
formatting/locale generation until that loaded-source batch returns terminal.

Root approved new API labels and bounded RPC/CLI wording. Its exact corrections
for first-save wording, present-tense navigation, evaluated vs unevaluated manual
history and paired activation/RPC-before-CLI ordering are pending application at
the source-freeze return. There is no technical discrepancy with those statements.

## Current locking correction and affected checks

The first concurrency source batch retained48passes and two failures. Ordinary
concurrent creation produced2Stop decisions (node producer passed): the initial
VPS lookup and ordinary membership/action/settings reads could reuse a caller's
older repeatable-read snapshot. Architect's clarification approved settings-first
lookup plus joined current locking membership reads, current settings/override and
action/reconciliation reads. No isolation/schema/protocol change was introduced;
public batched summary source stayed unchanged.

current-read-concurrency then passed4/4 (native90016/CLI28771): both producers,
deterministic older outer snapshot/current override/warning exclusion/oneStop,
and actual site parser dry-run/save/historical ownership. Parser fixture needed
an explicit plain MIME header; no parser production code changed.

After safe formatting and root's finalCS9labels, affected-core-final passed40/40
(native result79.198s, CLI92189 terminal0), localehealth0 and actual nodectl
stable-token/timeout control0. libnodectld RPC specs passed7/7 separately. Scoped
Ruby30files lint0 and Nixfmt/parse0. The tracked nodectl development Gemfile references
a missing helper tools/vpsadminos; actual control loads the real CLI source
through the already-working declared libnodectld dependency bundle instead. This
is an offline source control, not packaged/runtime proof.

Owner0's first real mail batch passed22/23. The remaining old-payload example now
seeds an unevaluated pre-declaration report with an empty registry, restores rules,
retains original source-only plain/HTML guards and also verifies a newly created
manual report keeps false/skipped outcomes. Actual Send of both proves no backfill
and unchanged new outcome. Source returned for failed+exact unexecuted continuation;
no22-pass repeat. Backend staging remains held through that terminal return.

Site normal commit initially failed in environment loading. Correct repository
Gemfile selection exposed cached JSON native code for Ruby3.4.11 under the current
Ruby3.4.12 shell; no app dependency changed. An own ignored isolated bundle with
BUNDLE_FROZEN=true is preparing normal hooks/commit. Both original failed attempts
and their observer limitations remain in raw logs. No bypass, publication,
source rewrite, runtime or lifecycle action occurred.


Final Owner1 first-purpose completion and history: [owning packet](packet.md).
