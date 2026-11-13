# Scheduled workflow audit

Scope: project-map repositories, current remote-default workflow definitions;
named configuration repositories get latest three scheduled runs, last success
and first relevant failure. No other session worktrees are evidence sources.
Detailed run evidence is owned by implementers; this file records synthesis.
Current named-repository architecture and acceptance are recorded in the final
C4 section below. Earlier acceptance checkpoints remain historical evidence.

## Confirmed named failures

| Repository | Evidence | Cause and disposition |
| --- | --- | --- |
| vpsadminos-org-configuration | Initial latest run 43426233198; first failure 40180341616 on Oct25 after last success 40080535061 on Oct24 | Workflow ca96c95 signs configuration but omits the custom Nixfmt plugin. C1's real unsigned/signed/invalid-format fixture passed. Later commit-message and dependency-authority repairs are retained below. Final C4 head 15352aeb is integrated and actual run 43484020423 passed. [C1 evidence](evidence-c1.md), [final C4 evidence](evidence-c4-implementer1.md). |
| vpsfree-cz-configuration | Initial latest three 43425681836, 43224121534, 43016930206; first continuous failure 40862091609 on Oct29; last success 40674539688 on Oct28 | Input updates change Ruby between shell entries while native gems share the ABI directory; date_core.so explicitly linked the old Ruby. B1's frozen-shell native-gem and real-hook fixture passed. Final C4 head 7d9807e0 preserves that shell, is integrated and passed focused acceptance; actual final run 43484770367 also passed. [B1 evidence](evidence-b1.md), [final C4 evidence](evidence-c4-implementer0.md). |

The vpsadminos.org failure is **not** evidence of Ruby drift: upstream CLI and
initial install logs establish missing plugin signing directly. The latest
vpsFree missing-gem text is not evidence that its Gemfile omits Overcommit.

## Official action contract checks (2026-11-13)

Official repository REST release/ref/action metadata was inspected. Existing
major refs already resolve to the current releases, so no action bump is needed:

| Action | Latest release | Existing major resolves to | Relevant contract |
| --- | --- | --- | --- |
| actions/checkout | [v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1) | 3d3c42e5aac5ba805825da76410c181273ba90b1 | Node 24; existing fetch-depth/ref/token inputs retained |
| actions/cache restore/save | [v6.1.0](https://github.com/actions/cache/releases/tag/v6.1.0) | 55cc8345863c7cc4c66a329aec7e433d2d1c52a9 | Node 24; restore/save path/key contract retained |
| cachix/install-nix-action | [v31.11.5](https://github.com/cachix/install-nix-action/releases/tag/v31.11.5) | 3dc140bfc76c49fbd4dd958429132e3746bcb086 | Composite installer, Nix 2.35.6; v31 annotated tag peels to latest exact commit |

Locked Overcommit 0.68.0
[CLI source](https://github.com/sds/overcommit/blob/v0.68.0/lib/overcommit/cli.rb#L190-L202)
has separate `--sign` configuration and `--sign pre-commit` plugin paths, checked
through official API. Preserve both signatures; disabling signature checks is
outside the repair contract.

## Additional inventory: complete, targeted triage ongoing

Implementer2 inspected 24 other project-map repositories and found 14 scheduled
workflow triggers. Generic dev-workspace, its vpsFree extension and codex-web have
no scheduled workflows. [Complete inventory](scheduled-inventory.md) records
immutable sources, latest runs and explicit no-history/older-failure limits.

| Repository/workflow | Failure evidence | Current disposition |
| --- | --- | --- |
| haveapi/update-nixpkgs | 42627419157 | python-ruff-parity: Python pin 0.17.2 versus Nix Ruff 0.17.4. G1 sufficient: synchronize exact dev formatter pin with newly selected Nixpkgs, retain checks. |
| haveapi/servers-ruby-performance | 42469966615 | Actual Rust authentication-renderer timing/allocation regression against fixed accepted reference; residual product issue, not a broken scheduled runner. Keep reference, budgets and gate intact. |
| vpsfree-irc-bot/daily-update | 43425361187 | Source-platform bundle resolution inherits RUBYOPT=-rbundler/setup; fails before commit, then missing Overcommit is a second preload failure. [E0 evidence](evidence-irc-bot.md); E1 sufficient. |
| vpsadmin/api-migration-specs | 42610017068; latest three failed | Eleven assertions in nine files expect typed false/true/0, but raw MySQL Column#default preserves database strings. [F0 evidence](evidence-vpsadmin-migrations.md); F1 sufficient without migration/helper behavior changes. |
| vpsfree-kb-contracts/page-runtime | 42472276689 | NixOS GitHub 504 is external-network failure. Firewalld pre-restart checks pass; after restart the fixture waits for any one of 22/80/443, then port 22 fails. H1 sufficient to fix readiness/diagnostics; actual focused runtime must establish the observed failure is resolved. |

### HaveAPI performance disposition

Artifact `performance-42469966615-1` report binds baseline
`b85ec364057f536940d689b09e612512ffffaf82` and candidate
`b606b4b3c32bf05779c05babeaa1c31a33dee6fa`, harness SHA256
`7d3371df362eba2d8a5df956a8ee33b3f987cecdaa96b8c34f072fc36146bc39` and budget
SHA256 `57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050`.
Only `rust.async_auth` and `rust.blocking_auth` classify as regression: adequate
timing signal and 7/7 agreement in both wall/CPU, allocations 105→148 and 104→173.
Correctness is pass; responses shrink by 151 bytes in both cases. The workflow
completed the comparator and correctly returned regression. The fixed reference
and budgets must not be moved automatically under the repository performance
contract. Source comparison shows expanded localization/detail-aware Rust
authentication rendering since the reference, but no profile proves which part
causes the slowdown. This remains a separate bounded product-performance task;
no broad optimization or threshold change belongs in these automation repairs.

### KB failure limits

In the retained machine-shell log, firewalld's first IPv4 SSH check passed at
11:56:41+0100; after container restart, the readiness regex accepted any matching
listener at 11:56:58. Firewalld was active and eth0 public. At 11:57:05 SSH failed
immediately (0.02 seconds, status 1). Before the restart, initial listener setup itself
returned success with only 22/443 displayed, demonstrating its any-port test
does not ensure all required listeners are ready. The artifact has no exact
post-restart `ss` listing or sshd status. A narrow fixture readiness/diagnostic
repair can establish all required listeners before unchanged firewall assertions;
it cannot yet be described as a verified cure for the observed SSH failure.

## Retained acceptance findings and bounded amendments

Status statements in these chronological checkpoints apply at their recorded
stage; the final C4 section gives current named-workflow acceptance.

The lead subsequently obtained user approval to merge the six repairs and run
their workflows. B1 passed every hosted stage and F1 passed 84 migration examples
according to the lead's exact-run receipts. C1's merged head
`8306d29d09f1939d1f92d44b5a5e241429b40c2e` passed Nixfmt and commit-message hooks
and created its first generated commit in run 43448052982 attempt 1. A later
channel-update commit failed before producing Git/hook output. C2 diagnosis is
owned by implementer1; the initial signing repair is confirmed, but complete
org updater acceptance remains open.

C2 owner then reproduced a process-argument limit in exact pinned confctl
`822c0e35dbe2549111912f539116b4225dfd3035`: guarded updates include descendant
changes, and CommitMessage includes each complete changelog. Descendant Nixpkgs
range `02c087f3fe673c9e317f206a627cb6b910336dbe` to
`d4f25a3e562008648d45bcf2d70bcc7422cad84e` produces 1,200,140 bytes with the exact
mirror Git-log flags. GitCommit passes that message as one `-m` argument. Its
local 200,000-byte reproduction returns the same generic failure before Git or
hooks execute; direct spawn reports `Errno::E2BIG`. The candidate was not
exported by the hosted run: its identity is inferred from the staging commit
predating the run, while the source/size/exec mechanism is directly reproduced.
Root staging's own log is small; the oversized descendant log is the causal
path, and an old May transitive confctl OS pin must not be mistaken for the root
pin. Lead accepted a narrow seventh-repository repair: confctl temporary message
file/`-F`, followed by only the org workflow's immutable tool pin. The full
message transport and normal hooks remain required. At this checkpoint preserving
all descendant Git logs was assumed; C3 below supersedes that assumption. The
user subsequently explicitly approved confctl/master and lead integrated
`4c636b40` on 2026-11-13 at 17:14:35 UTC.

C2a is now implemented and published at
`4c636b40b53b143fda6d9cad9332ce8b7b86bdb8` over confctl
`822c0e35dbe2549111912f539116b4225dfd3035`; C2b is the additive org pin commit
`6874f60516abbf7e96d8fc247036d0aa61d11cd1` over merged C1 `8306d29`.
[Implementation evidence](evidence-c2implementation.md) records one source
change plus its focused spec and one immutable workflow pin, with no design
deviation. Real Git retained a complete 1,260,024-byte message, executed its hook,
preserved unrelated staged content and rejected a failing hook without moving
HEAD. Editor/TTY and temporary-file lifetime/cleanup cases passed; the related
spec batch passed 37 examples. Normal hooks and org one-pin/syntax checks passed.
Final review and full-suite/packaged acceptance were pending at that implementation
checkpoint. Lead subsequently completed C2 integration as recorded above. The org
pin remains unmerged and will consume the final C3 provider instead.

E1's actual acceptance at reviewed head
`9629a74c154a36f0a209a49cca8e71b25424003f` completed generation, native bundle
installation and hook installation/signing, then plain Git could not load
Overcommit. The exact exception was `LoadError: cannot load such file --
overcommit`. Bundler had installed Overcommit 0.76.0 beneath
`.gems/ruby/3.3.0`, while plain RubyGems searched `.gems`. Clearing RUBYOPT was
necessary for maintenance but left the final Git hook without bundle activation.
Reusing the prepared bundle, `bundle exec git commit -F` passed real PreCommit
and CommitMsg hooks and created fixture commit
`d77adcb6ec602584ae53840468a9ae416f759f08`. This used the same Ruby
`/nix/store/ncvfbigndbnclcfvdg0zbnfbd6v3mpds-ruby-3.3.13/bin/ruby`, Bundler 4.0.24
and source-platform Nokogiri 1.19.7. The sufficient amendment changes only that
workflow caller; no hook configuration or README change is needed. Owner evidence
retains the successful generation identities and hook probe, avoiding redundant
generation to diagnose the same final-stage failure.

E1's final reviewed/published head
`7f6fb0e5f58c5f76b573dc4df7124a4cae744dfd` subsequently passed the remaining
local acceptance in 42 seconds under a fresh watcher. The unchanged generation
prefix was reused with exact source/input/output receipts; all 71 application
lock/gemset entries agree, native Nokogiri loads, and the exact current updater
body reports `committed=false` on its immediate no-change pass with unchanged
fixture HEAD and output hashes. The fixture's historical parent is explicitly
distinguished from the new reviewed head. Exact-head RSpec also passed. See
[E1 delivery evidence](evidence-e1.md) for review ranges, package identities and
clean detached-target preparation. Lead acceptance, integration and fresh hosted
integrated-master execution remain separate from this successful local result.

The subsequent integrated IRC run
[43454018549 attempt 1](https://github.com/vpsfreecz/vpsfree-irc-bot/actions/runs/43454018549/attempts/1)
at `7f6fb0e5f58c5f76b573dc4df7124a4cae744dfd` passed generation and its bundled
commit, then failed the separate ambient-shell push because its pre-push hook
could not load Overcommit. The earlier local acceptance omitted this boundary.
E2's sufficient additive repair runs the same `git push origin HEAD:master`
through `nix develop -c bundle exec`, preserving its condition/auth/refspec.
The declared shell uses unchanged flake inputs, so it selects the same Ruby and
activates the refreshed installed bundle. Required focused acceptance extends
the retained bundle with a disposable bare remote: real pre-push success and
deliberate fixture-hook rejection with no remote-ref movement. Generation is
already proven and will not be repeated for this diagnosis. Lead owns release,
review, integration and a fresh hosted run; complete IRC acceptance remains open.

E2's reviewed additive head `f15bf5577924da84be217dcd925ab337e1c5c3c5` then passed
the actual local-bare push acceptance in 28 seconds. The exact reviewed command
advanced the seeded receiver master from `9629a74` to generated commit `d77adcb`.
For the negative candidate `5a986397`, the unmodified real Overcommit pre-push
framework passed, then its fixture-only instrumentation wrapper deliberately
returned 65; Git returned 1 and remote master stayed at `d77adcb`. Both calls
preserved and recorded real hook arguments/stdin and the same Ruby 3.3.13,
Bundler 4.0.24 and refreshed Overcommit 0.76.0. This proves Git honors pre-push
rejection without claiming that a repository hook rule itself rejected the
candidate. No dependency generation was repeated. The initial empty-receiver
pre-hook setup failure is retained separately. [E2 evidence](evidence-e2.md)
binds exact source, hook and bundle identities; lead inspected the traces,
accepted the proof and closed `irc-hook-validation-coverage`. Integration and
fresh hosted final acceptance remain lead-owned.

H1's reviewed head `2cfbde649769509e2628600535e3023d872f1735` correctly rejected
the incomplete post-restart fixture in its first focused acceptance (exit 1,
531 seconds): ports 80/81/443 appeared, but 22 did not. SSH initially started and
later stopped cleanly; after restart no standalone SSH start attempt appeared.
The runtime used Fedora 45 and OpenSSH 10.5p1-1.fc45. Wildcard status diagnostics
did not retain unloaded sshd.service state, so the exact failed boot transaction
is unknown.

Read-only inspection of the published
[Fedora 45 image archive](https://images.vpsadminos.org/v1/vpsadminos/minimal/x86_64/fedora/45/image-archive.tar)
under ETag `6aeed93c-fa8bc00` found both `multi-user.target.wants/sshd.service`
and `sockets.target.wants/sshd.socket`. The socket explicitly conflicts with the
service and listens on TCP 22. Archive SHA256 is
`b63c150090d0c594d2348a272bb493e9e7fb644bb81a19b4142210742cce46c4`; last modified
2026-11-07. It predates the run, but that run did not retain its image hash, so
this association is an inference. Independent extraction of the
[official exact OpenSSH RPM](https://kojipkgs.fedoraproject.org/packages/openssh/10.5p1/1.fc45/x86_64/openssh-server-10.5p1-1.fc45.x86_64.rpm)
(SHA256 `9ce49b6039741648c0fda93da8d24856ec01168b7d261871bfd7242159a4e9b0`)
confirmed the service's `WantedBy=multi-user.target`. The
[systemd SSH generator](https://www.freedesktop.org/software/systemd/man/261/systemd-ssh-generator.html)
local Unix socket does not replace TCP activation.

The H1 amendment selects one persistent activation mode in the Fedora fixture:
disable/stop sshd.socket before enabling/starting sshd.service, then assert that
mode initially and after restart. Keep the complete listener wait and all
firewall assertions. Explicit named unit diagnostics replace reliance on
wildcard matching. Quick checks and affected final review precede one further
focused run on changed source. No timeout increase, forced post-restart start,
image/pin changes or broad KB rework is authorized by this brief.

The amended, independently reviewed H1 head
`cb7825245ea786fb0f51c469d1a7dc5c6a1ececc` passed its one fresh changed-source
firewalld scenario: exit 0 with `expected_success`. Before and after restart,
sshd.service was enabled and active, sshd.socket disabled and inactive, all four
listeners were present, and every original firewall policy assertion passed.
No forced post-restart start, timeout growth or retry was used. The exact source
and native-script identities, failed predecessor and image-association limits
remain in [H1 evidence](evidence-h1.md). The exact final head is published and a
clean detached integration target is prepared; lead owns integration and the
full master workflow. This establishes focused local acceptance of the fixture
repair without retroactively claiming an exact image identity for the old run.

These amendments are in [design.md](design.md). No application source,
configuration inputs or production state was changed by this architecture
package. Lead and implementer evidence owns execution, integration and remaining
acceptance results.

## C3 user policy correction and selected-input message boundary

The user explicitly rejected Nixpkgs Git logs as large and useless, then approved
the independent confctl transport fix while stating Nixpkgs updates should use
`--no-changelog`. Exact wording and approval source are in state.md and the
[C3 brief](design.md#c3-keep-guarded-commit-messages-scoped-to-selected-inputs-sufficient-provider-brief).
The user subsequently clarified that transitive inputs should not appear in
commit messages at all. Both the original all-descendant-log assumption and
the first C3 design retaining transitive revision summaries are superseded.
That first C3 design used summaries for descendant-only updates; the current
title-only selected-input fallback below replaces that rationale.

Bounded source inspection identified the behavioral change at
[5507177](https://github.com/vpsfreecz/confctl/commit/550717765d58e9f28d960ea5bca3459ace86eb9e):
committed October 24, 2026 at 19:24:07 +0200, titled "Guard automated input
updates with cached Git ancestry" (Git author/committer metadata Jakub Skokan).
Its guarded callback sends all logical descendant changes from
`FlakeLockDiff.from_guard` to CommitMessage. The immediate parent
`cc40679d267165aecfa569128438bb55fe910268` and current manual updater construct
message changes using `diff(..., inputs: inputs)`. The broader messages were a
consequence of that guard implementation; the commit is not evidence that the
user requested that presentation change.
Current Setter has no guarded callback and already preserves selected-input
messages; it requires no change. No earlier history was needed.

Both named daily workflows already pass `--no-changelog` for genuine committing
Nixpkgs calls. Org's os-staging channel maps only vpsadminos; vpsFree's OS call
selects the vpsadminos role. Their Nixpkgs log expansion therefore comes from
the guarded descendant callback, not a missing CLI flag. HaveAPI and IRC
Nixpkgs scripts call confctl without `--commit` and write compact revision-only
messages. The audited vpsAdminOS flake updater similarly writes lock-derived
revision summaries. The brief records exact inspected heads and caller paths;
those custom-message consumers need no policy patch.

The current sufficient amendment filters only message changes by exact selected
logical paths before title/body/group construction. Full guard/callback/result
changes remain intact. Nil selection preserves manual/Setter behavior; true
original no-changes errors remain. `--no-changelog` still suppresses every log,
while selected-only revision summaries remain. For a valid descendant-only
update with no selected revision delta, emit only `inputs: update <sorted
requested names>`: no fabricated hash/arrow, descendant name/summary or log.
Nested/follows aliases retain the requested names without leaking other aliases.

Owner1 held implementation before commit on the user correction; the revised
sufficient brief then required lead release, with passing prior evidence retained but
superseded full-summary assertions no longer acceptance criteria. Org's unmerged
pin will consolidate to the final provider. Implementer0 still owns the directly
affected vpsFree B2 consumer; its pin edit waits for the final committed provider
hash and lead release. No repository-name filter, new CLI flag or guard change
is needed. No application edits were made by architect.

## C4 single authority for the confctl dependency

The user rejected the separate workflow provider pin and clarified: "there's
not supposed to be any pin in the workflow. we have flake.lock for that".
The normal `github:vpsfreecz/confctl` input declaration remains in flake.nix;
its immutable revision belongs only in flake.lock. Earlier C2/C3 workflow-pin
adoption was the wrong ownership model and is superseded by C4, without undoing
the accepted provider fixes or rewriting integrated history.

Both configurations already use the provider's tools-mode development shell.
`nix/flake/mk-config-devshell.nix` puts the input's packaged confctl first in
PATH. Therefore all updater and final guard calls can use plain `confctl`
inside their existing declared-shell blocks. At inspected sources org `69edee80`
and vpsFree `07a85cae`, the YAML selected `ff5e0177` while their real locks still
selected `af164b44` and `7bee58a5` respectively. Removing the YAML override alone
would lose accepted guard/message behavior. No channel owns the confctl root;
normal `confctl inputs update --commit confctl` adoption must accompany removal.

The [C4 brief](design.md#c4-use-the-repository-locked-confctl-input-sufficient)
records exact old/new confctl dependency graphs. Org's tools use the provider's
default Nixpkgs, so its initial Ruby environment may change; vpsFree supplies
its own root-stable tooling with the existing Ruby 3.4 overlay. B1's saved shell
must remain intact. A bounded 30-second read-only version evaluation timed out;
no actual Ruby version was inferred from that probe. Owner preparation later
verified org Ruby 3.4.9/Bundler 4.0.7 (old org tools were Ruby 3.3.10) and vpsFree
Ruby 3.4.11 with its saved profile. No architecture build/test ran.

Lead reports C3 provider `ff5e017780a35fb97b549db2a51b570193867c3b` integrated and
both prior master workflows passed (org 43477762211, vpsFree 43478026385), with
generated changes published and no remaining monitor effects. Owners must fetch
and fast-forward to those current defaults before normal lock adoption. C4-org
belongs to implementer1 and C4-vpsFree to implementer0 after lead release.
Each package changes only flake.lock plus its daily workflow; no flake.nix hash,
new output/channel/registry, unrelated consumer, provider-suite repeat or
production deployment. The earlier successful runs validate C3 functionality;
fresh final C4 workflow acceptance remained a separate requirement. Architect
did not inspect or duplicate observation of those runs.

### Final C4 architecture and acceptance

Both named configurations now declare the normal confctl URL in unchanged
flake.nix and lock `ff5e017780a35fb97b549db2a51b570193867c3b` only in flake.lock.
Their daily workflows contain no `CONFCTL_FLAKE` or separate provider revision.
Plain confctl from the declared tools shell handles every update and final
check. Full forward guards, selected-only C3 messages, `--no-changelog`, normal
hooks/auth/push and vpsFree's B1 saved shell remain in place. Prior C3 YAML pin
receipts are superseded architecture, retained only as integrated history.

Lead accepted all four final-review lanes without findings and integrated exact
repair heads org `15352aeb13c4011b5dd1a1f78d1fdcb08f7c2420` and vpsFree
`7d9807e021e6106d628c021da45f5f55077b2e9c`. Both preserve their generated
input-update commits separately from workflow corrections. Focused actual
acceptance passed: org plain final check/native proof in 20 seconds with Ruby
3.4.9; vpsFree saved-profile/native/final-check proof in 23 seconds with Ruby
3.4.11. Both use package
`/nix/store/v4b3r3r8102kyf92lidwvk62plpjs13j-confctl`, source
`/nix/store/1qw3c7q3r67drrv0z4vmac9g70pvxyf5-source`, derivation
`/nix/store/6nq336f5rfs8jgd38bsmdgpdhy5rw0rd-confctl.drv`, matching the accepted
C3 source/input receipts. Provider tests were not duplicated. Full evidence:
[org](evidence-c4-implementer1.md), [vpsFree](evidence-c4-implementer0.md).

Lead reports both final actual master workflows succeeded:

| Repository | Exact event source | Final run | UTC interval |
| --- | --- | --- | --- |
| vpsadminos-org-configuration | 15352aeb13c4011b5dd1a1f78d1fdcb08f7c2420 | [43484020423 attempt 1](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/43484020423/attempts/1) | 18:34:57–18:39:14 |
| vpsfree-cz-configuration | 7d9807e021e6106d628c021da45f5f55077b2e9c | [43484770367 attempt 1](https://github.com/vpsfreecz/vpsfree-cz-configuration/actions/runs/43484770367/attempts/1) | 18:39:36–18:44:03 |

Both completed updates, the final plain-confctl guard and ordinary push, with
no new generated updates (`Everything up-to-date`). These hosted runs establish
the final sole-lock architecture and no-change execution; changed-input,
selected-only message and rejection semantics remain established by the exact
accepted C3 package proofs. A no-change run is not presented as independent
changed-input or rejection coverage.

Lead's fresh fetch verified all seven final repair heads are ancestors of their
remote masters; both configuration defaults matched the exact source heads
above. Both managed watchers passed terminally and all owned effects ended.
Repository merge claims are released and verified; no physical deployment or
session lifecycle action occurred. No peer duplicated CI observation. Confctl's
exact-ff5e0177 automatic [Tests run 43474592486](https://github.com/vpsfreecz/confctl/actions/runs/43474592486)
was confirmed successful by lead. Auxiliary vpsAdmin CI 43447714261 was still
in progress at the last lead report; no additional observation or remote
mutation was started for it. Lead owns final state, ancestry receipts and handoff.

Residual dispositions remain explicit:

- HaveAPI's retained performance comparison reports a real product regression;
  its baseline, thresholds and gate were not changed to force a pass. This stays
  a separate product-performance issue, as detailed above.
- Syslog-exporter had no retained scheduled execution history. Active schedule
  metadata does not prove runtime success, and this audit makes no such claim.
- KB's retained NixOS failure was an external GitHub HTTP 504. No speculative
  retry or infrastructure change was added; that original failure remains in
  the evidence independently of the repaired firewalld fixture.
