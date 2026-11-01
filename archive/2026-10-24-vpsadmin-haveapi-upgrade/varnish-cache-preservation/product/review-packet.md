# Preserve Varnish caching: committed and quick-pass

Final head `7219ab22a49f666077056fc2f093424547294aeb`, tree
`e18de031b98db415ecdc851d63765f1abadf1431`, clean existing worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-oauth-client-logs`,
branch `2026-10-24-vpsadmin-haveapi-upgrade-oauth-client-logs`.
**STOPPED for retained final review before long checks/publication.**
[Exact source/history proof](final-proof.json).

## Requested correction and boundary

The user explicitly requires preserving Varnish in its original position and
excludes shared-memory-only records from this persistent-log task. This replaces
the earlier bypass design; it is a substantive topology correction. Follow
design.md:6824 “Preserve Varnish caching: corrected requirement (2026-10-31)”.
Lead owns accepted prose and reviewer assignment; E1 owns site topology/pin work.
No default integration or deployment is authorized.

Relative to published45cb, exactly five paths change, +120/-20:

- `tests/configs/nixos/vpsadmin-services.nix`: restore only api.test's original
  Varnish socket and remove the bypass comment; auth.test remains its original
  direct HAProxy route. The final file equals its original pre-bypass base.
- `docs/api-client-examples.md` and `docs/http-log-protection.md`: exact lead
  prepared replacements, checked against original45cb and replacement hashes
  in prose/manifest.json. No independent prose rewrite was performed.
- Existing `tests/oauth-client-log-protection/module.nix`: export actual
  product-generated VCL and locked varnishtest from the ordinary Varnish module.
  Prior nginx/FPM/HAProxy fixture values remain exactly equal to45cb.
- One ordinary `varnish.vtc` native case in that existing fixture directory.

All3174 mode/type/OID entries outside those five paths equal45cb. Product
varnish.nix, cache semantics, persistent nginx/HAProxy/PHP controls, application,
P0 containment, authentication, dependencies and locks remain unchanged.
VSL is permitted for synthetic test records and is not suppressed. The module
still passes nonmetrics traffic, sets eligible metrics TTL60, and leaves builtin
cache eligibility and full-URL/token keying intact. No forced caching, VCL policy,
daemon logging policy, regex redactor or new runner/framework was introduced.

## Focused quick evidence

[Quick result and final source hashes](quick-result.json).

Actual generated service evaluation proves api.test/backend and nginx api_test
upstream select `unix:/run/varnish/vpsadmin-varnish.sock`; auth.test remains
`unix:/run/haproxy/vpsadmin-api.sock`. Its VCL policy equals the native fixture
except the synthetic domain/backend definition, and both select locked native
Varnish8.0.2 at4spn44qx. [Actual service values](services-route-2.json).
The fixture's actual generated VCL was adapted only for a private backend port;
no policy statement was added or changed. [VCL](actual-generated-2.vcl).

Native varnishtest passed0 in2.846s: two identical eligible tokenA metrics
requests give MISS→HIT with one backend fetch, tokenB gets a distinct fetch,
native insertion VSL records TTL60, and counters are2miss/1hit/6backend fetches
for7requests. The upstream advertises max-age5, so TTL60 comes from the actual
product VCL. Two identical uncached callback POSTs preserve encoded query/body,
Authorization/Cookie, status302, Location/Set-Cookie and distinct response bodies.
Two metrics requests with auth/cookie still fetch distinct private responses;
the fixture does not force-cache ineligible traffic.
[Native command/result](varnishtest-2.json), [complete native log](varnishtest-2.log).

The original attempt's wire assertions all matched, but its TTL pattern expected
60.000 while native VSL prints60, so logexpect waited to varnishtest's standard
60s timeout. Narrowing that assertion fixed the test without product changes.
Original log/result/effects remain retained; recorded owned Varnish PIDs are
absent, and the successful native parent waited its manager exit0. No fixture
daemon remains. [Original effects](varnishtest-1-effects.json).

The first scratch service evaluator omitted the VM options module required by
the existing services fixture. The corrected evaluator imports the normal
qemu-vm module; it only evaluates routing/VCL and builds no VM. Original failure
is retained in services-route.log. No blind runtime retry or broad campaign ran.

Normal declared-shell Nix formatting, final whitespace and doc references pass.
Original45cb/replacement prose hashes match; VTC bytes equal the actual passing
test. Final formatted fixture values equal the tested values, and every old
nginx/FPM/HAProxy value equals45cb. Unchanged24-case nginx/PHP5 proofs were not
rerun or relabeled as new-topology installed proof.

Normal consumer amendment and final protection amendment hooks pass, including
Nixfmt, migration, i18n and relevant Ruby checks. Commit-message hooks pass with
the recorded advisory72-column warnings; all message lines meet the required80
maximum. No bypass. Overcommit initially refused restore/pre-rebase signatures;
all five hook/config files were verified byte-equal45cb before ordinary
`overcommit --sign` plus direct post-checkout continuation. No rebase had started
at refusal. [Hook reconciliation](pre-rebase-hook-reconciliation.json),
[consumer hooks](consumer-amend.log), [final hooks](protection-amend.log).

## Cleaned whole history and migration provenance

Fresh canonical SSH fetch/readback established unchanged defaultac10 and own
published45cb. Named local45cb recovery was created before edits; remote own
feature remains45cb,75c recovery and live33d6 refs/checkout remain untouched.
No feature/default ref was pushed during consolidation.

Complete range `ac10a62f1cb0fc890378ae83cdf18dd0e29f049a..7219ab22a49f666077056fc2f093424547294aeb`
retains five logical commits,46paths/+9145/-5335:

| Prior | Final | Disposition |
| --- | --- | --- |
| `11b26c0a` | `11b26c0a5f6fa51fc6eb63b8f28dd5e8ccbaf721` | Released0.32 dependency stream unchanged |
| `33d6c772` | `ccb08e3cebb06f46b4dddea3a86baec31f1ff5b3` | Originating consumer route/prose corrected; message accurately describes persistent logging with cache |
| `a089b530` | `967da811892062ffc82d4cd98a43ed6a7e7a5a28` | Identical selector-test stable patch ID/message |
| `75c691b1` | `9cff7f2a14f8316468623d57a81482598beef98e` | Identical P0 stable patch ID/message |
| `45cb49e2` | `7219ab22a49f666077056fc2f093424547294aeb` | Functional protection retained; exact final prose/cache regression folded into its owner |

Every author's identity and author date is preserved. Consumer tree changes
against33d6 are only its route/prose, all other consumer source identical. The
expected later docs conflict was resolved using exact lead-prepared bytes.
No bypass-add/remove pair, repeated pin stream, fixup or superseded topology
remains. The single released HaveAPI update stays unchanged.
[Complete series](complete-series.txt), [old/new range comparison](range-diff.txt),
[five-path correction](final-correction.diff), [full final diff](complete-final.diff).

**NO MIGRATIONS** across the complete series; no changed schema/database paths
or migration version has merge/release/deploy/external-use disposition to alter.
[Migration history](migration-history.txt). Old published/deployed33d6/45cb and
their recovery refs/receipts remain valid historical identities. The successor
is not literally ancestral to those heads and is not whole-patch-equivalent:
cache topology is materially corrected. Do not relabel prior deployed proof.

## Review, reuse and remaining work

Request retained reviewer0 saved Sol/xhigh/read_only for all4 HIGH lanes, cache/
persistent-log boundary, actual routing/fixture and explicit complete-history/
one-stream/NO MIGRATIONS conclusions. Prior all4 review of45cb is evidence for
unchanged implementation, not approval of this substantive topology correction.
The lead's context-owning writing/Humanizer pass supplied the exact final prose.

After accepted review and lead release, run the existing affected services-up
once through restored nginx→Varnish→HAProxy and required normal package checks.
Reuse only exact unaffected derivation/input proof. Do not repeat broad clients,
PHP/browser or generic workspace checks. New publication and E1 exact source
handoff wait that released package; app merge/deployment remain separate.

Original CI observer20145/PID51188/startticks7336282 remains active separately
for old45cb run41229546687/attempt1. No new CI query/watch/cancel/dispatch/rerun
occurred for this correction. Its eventual result remains scoped to45cb. Other
owned source/quick/hook operations ended; source writer is idle pending review.
No source retrieval campaign, native/registered-cluster change, credential or
live request, claim, lifecycle or cleanup action occurred. KB/Discourse stay
canceled; React/workspace releases are untouched.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
