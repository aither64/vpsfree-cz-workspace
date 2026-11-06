# Independent final private staging review

Reviewer0 delivered the final report on 2026-11-03 through report_to_lead.
Retained independent identity: thread01a19caf-15c8-74a2-baf1-6594cf30d117,
gpt-6.1-sol/xhigh/read_only, settings unchanged, no fallback or nested agents.
Reviewer independently verified session binding, saved purpose/access and source.

## Decision

No Blocking or Important findings. General, architecture/repetition,
scope/proportionality and risk/compatibility review clears the exact five-system
build batch. Prior unchanged mail/DNS reviews remain applicable. Activation still
requires exact configured-machine claim admission; no integration or public
cutover permission is supplied.

Reviewed base c4107822060e9e34b24a83950d618c9f28a7722b to
0844881779d62d9a6a86d2bacd61d21565b33932, tree
34dc1820c5feda2a0d875f60c964b8375de0af49. Independent checks confirmed clean
worktree, merge-base, whole-range whitespace and exact remote feature/base.
Full range:13 paths,740 additions/four deletions. New staging behavior changes
only config.nix and module.nix; no additional framework/runtime/catalog work.

## Source, generated configuration and consumers

The confirmed candidate ID/target/name/channels and stateVersion25.05 are retained.
Private address metadata is accurate; host-supplied networking is not replaced.
Monitoring/logging and auto-update/exporter metadata are disabled for staging.
Generated units have neither exporter nor rsyslog. No new queue conversion.

The enabled firewall accepts general TCP22 and IPv4 TCP25 only from observed
172.16.106.40/32 before terminal refusal. No general/IPv6 SMTP or exporter
exception remains; the source is not added to Postfix mynetworks. Generated
resolver has only1.1.1.1, justified by split DNS; actual guest DNS/connectivity
remains a postactivation check. All prior root keys are retained plus exactly the
approved existing workspace key. The initial shared-admin selection assumption
was caught and corrected before review, without global key/credential changes.
Main.cf, transport, Postgrey and Postfix derivations/text equal prior reviewed
policy. Temporary rollout details correctly stay in session records; reusable
project guide remains valid.

Reviewer independently confirmed monitor and alerter consumer selection.
Supplemental completed content comparisons show mon1/2 remove only the mx2
infra exporter and infra-ping entries (Prometheus unit only), and alerts1/2
remove only mx2/node5.brq inhibition (Alertmanager unit only). Other content is
equal. Build exactly mx2, prg/int.mon1, prg/int.mon2, prg/int.alerts1 and
prg/int.alerts2. Activate none of those consumers in this task.

Both ns1 roots differ only in revision configuration-info and its propagation.
System units/DNS and other etc dependencies are identical. Skipping DNS behavior
rebuilds is justified; the new revision-bearing DNS closures are not claimed built.
The reviewer inspected completed comparison receipts after the main report and
confirmed no new finding, source revision or review/build gate.

## Test reuse, inputs and history

Final test derivation independently equals the successful historical
/nix/store/8pan3ddqairw3js87iaysvjqwzalxgls-vm-test-run-mx2.drv.
Canonical root JSON SHA256d1e739bbeefe29f257dbb3a5e27558bb2183fe48314d324fa59a7ee661191255
and full4038-derivation graph SHA256e366b1480f8650a403de926389d537a45e9652f37ea962422ba2117ba0915c96
were independently reproduced. Historical pass reuse is bound to exact consumed
graph identity. Preserve the historical-pass/current-output-unavailability
qualification; no automatic VM rerun is required.

Whole root lock changed only through inherited upstream vpsadminServices, which
the VM does not consume; final lock equals current default. Independently checked
SHA256507e781c2fa52da5a389e6eab824efe68baa72b1727de0fc162ea0a5e6b4c098,
blobf6b87ab2ca27a72c3fe1bdd134129ff1e4a9f7e9.

Complete series:548514a9e573ccbc3f145d49d7d307c3e23b5aa5 host/shared/private
staging; e7cd91d881fce72fe15339a8df736a6481d7000d DNS;
0844881779d62d9a6a86d2bacd61d21565b33932 tests/docs.
Independent old/new range-diff shows only owning host changes; DNS/tests are
patch-equivalent. No obsolete public-host iteration, exporter follow-up, key
fixup, abandoned compatibility path or transitional migration remains.
Original40411/importe4/runtime8d/reviewed-mail1e refs remain preserved without
nonancestor literal-merge/deployment claims. No database/schema migrations or
feature-owned repeated dependency/channel/generated-update stream. Upstream's
already-merged updates are protected default history, not feature redundancy.

## Next gate and residual limits

Run the five native builds with the required watcher or documented fallback.
Expected candidate drv bpyiq4bfdmd9anf96zqyg8kqmyd3d9b0 -> unbuilt4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2.
Evaluation is not realization or activation. Preserve exact build/input/source
and native-generation evidence.

Do not activate until exact27627/172.19.9.22 machine ownership is admitted and
held. Preserve strict host/key trust, empty/accounted queue and rollback
/nix/store/98n9xjgm42pjmzi9vy430qilp2hqbzvb-nixos-system-mx2-25.05.git.7c43f080a.
After activation verify new current/profile/configuration-info, SSH/private
network/firewall/DNS/persistence/units before the at-most-two marked podpora
messages. No deliberate live DSNs or primary interruption. Preserve accepted
queues on rollback. Public IPv4/IPv6, inbound TLS, recipient/backscatter/milter
and final source identity remain later cutover gates.

Reviewer performed local reads/evaluations only; no file/Git mutation, build,
production probe, deployment, mail, claim or lifecycle action.


# Nov5 final independent review: public profile and TLS bootstrap

Reviewer0 (thread01a19caf-15c8-74a2-baf1-6594cf30d117) independently verified same-session
identity and saved Sol/xhigh/read_only settings. It applied mandatory-change-review
and all four lanes: general, architecture/repetition, scope/proportionality, and
risk/compatibility. High risk is public SMTP/TLS/firewall and deployment ordering.
No overrides, fallback, nested agents, substantive authorship or remote mutation.

**Accepted: no Blocking or Important findings.** The complete committed package
and quick checks permit the required native builds and private copy while084488
remains active. Public handover, old-host actions, cutover switches and integration
retain their separate authority. Source remains frozen at the reviewed identities.

- Base c4107822060e9e34b24a83950d618c9f28a7722b.
- Final b120342c4517b6faa1a519913ab92acafbc506f3.
- Sibling bootstrap27fcf245fdfa3b1bff78815481d9bb954d915146.
- Both parent actual deployed0844881779d62d9a6a86d2bacd61d21565b33932.
- Full final range13 paths769 additions/4 deletions; new public delta3 files42/13.
- Fresh observed masterf4069909b55fbed907cb658f350ec6a59f97e05a, deliberately not
  rebased because current selected OS inputs are frozen. This is not a claim of
  fresh-default integration readiness.

Reviewer independently checked clean state, full diff/history/parents, whitespace,
published SSH refs and exact lock SHA507e781c2fa52da5a389e6eab824efe68baa72b1727de0fc162ea0a5e6b4c098.
Both source locks/semantics equal deployed084488; nixpkgsStable718f670e and
vpsadminosOsStagingb45b27b4 unchanged. Owner evidence is in
[public-profile-preparation.md](public-profile-preparation.md), generated assertion
exports, consumer comparisons and exact system table linked there.

Native ACME/Postfix design was independently inspected: local base certificate
unit only in Requires/After, no network-order dependency or cycle; provisional
and real certificate files preserve acme:postfix restricted ownership/permissions;
key precedes chain, inbound TLS is opportunistic, renewal reloads Postfix. Bootstrap
retains exact workspace-only SMTP and general22/80; final changes only the SMTP
gate to general22/25/80 on both families. Exporter9100 stays limited to172.16.4.10/18.
Keys/Postgrey/resolver/transport match deployed state; main.cf changes only
myhostname and the two intended inbound TLS settings. Public metadata does not
allocate addresses. No auto-update, recipient-sync/scanner or extra framework.

Ordinary switches are appropriate after the old2992-to27627 handover, with both
artifacts prepared in advance, trusted certificate verification before public SMTP,
and both queues/disks retained. No second reboot required. Domain-wide acceptance/
backscatter and absent fail-open milter are explicit baseline limitations, not
newly introduced behavior. The actual host ACME/TLS path remains a live cutover
check; no certificate issuance or public readiness is claimed by source review.

Required builds: bootstrap mx2 plus final mx2/mon1/mon2/alerts1/alerts2. Consumers
only add mx2 exporter/ping entries and inhibition. DNS only changes revision
metadata, so no behavioral rebuild; do not claim new DNS closures built. The
historically passed8pan VM root exactly equals both variants; reviewer reproduced
native envelope hashd1e739bbeefe29f257dbb3a5e27558bb2183fe48314d324fa59a7ee661191255
and prior4038-node graph bindinge366b1480f8650a403de926389d537a45e9652f37ea962422ba2117ba0915c96.
Retain historical-pass/current-output-unavailability qualification. No new VM
runtime run needed. A selected ACME derivative was absent in the reviewer's local
store; it inspected pinned source and exported generated text, not every realized
leaf. Planned builds supply actual realization evidence.

Complete final history548514a9(host/private),e7cd91d8(DNS),08448817(tests/docs),
b120342c(public profile) is coherent. No obsolete unconsumed fixup or abandoned
implementation. Deployed084488 is a supported state boundary. Bootstrap27fc is a
necessary separate cutover ref and is not a final ancestor; never call it literally
merged. Successful final deployment can establish its substantive successor only
after execution. **No schema/database migrations and no feature-owned repeated
input/channel update stream.** Prior Postgrey reset remains separately authorized
operational history, not a migration or state-equivalence claim.

Advisory: docs/operations/mx2.md fixture paragraph's "only differences" can be
clearer about comparing the shared mail module; the unchanged VM does not cover
host ACME/inbound TLS. Lead accepts this minor clarity issue without source change:
the paragraph explicitly names the imported production mail module and the following
section excludes actual-host verification and explicitly requires trusted-certificate
checks before public SMTP. This receipt and the live plan state that limitation;
no new VM case or review cycle is justified. All acceptance claims remain bounded
accordingly. This advisory is accepted, not an unresolved blocker.
