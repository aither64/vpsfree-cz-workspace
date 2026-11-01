# HaveAPI 0.32.1 site final-review packet

Completed candidate `c040c14cdbacc07998700b524996a89306188d7f`, tree
`ff284f9838fd9369a1f8610f1ec9efc67787c178`, on fetched configuration master
`bd76e7b3c7eef6e4a36ad0a679b6764ffc50fff2`. Source is clean and unpublished.
Parent owns the retained independent final reviewer assignment: all four lanes,
HIGH risk because this changes authentication configuration and operator recovery.
Review the complete branch, including history and explicit NO MIGRATIONS.

| Commit | Purpose |
| --- | --- |
| `f93d6f9a2159ff36036ee1c18c6c242d3cb4ef43` | API1/API2 setup instructions, including accepted DOC-OAUTH-R1 restart correction |
| `1490ff7c7da4a7899f849ee7b40b7ba19f5aaa3e` | Literal switch-user revoke map and existing DB-free forwarding assertions |
| `c040c14cdbacc07998700b524996a89306188d7f` | One normal generated services pin, 0f450b89 to published097226b2 |

[Full history/messages](full-series.txt), [whole binary diff](full.diff),
[475-entry mode/OID inventory](tracked-inventory.txt), [final proof](final-proof.json).
Only the operator doc, hook, existing spec and lock differ from fresh base; all471
other entries are preserved. No fixup, merge, obsolete or repeated pin stream.
NO MIGRATIONS: no schema, private-state, credential or format conversion; no
coordinated node upgrade. Previously merged history is preserved.

The lead approved replay after upstream master advanced only the WebUI locked
rev/NAR/time to70bd11d9. That input is inherited intact; no previousf276 verification
is claimed for it. Named local recovery preserves835 and its doc849 parent.
[Replay equivalence](rebase-equivalence.json) and [range-diff](rebase-range-diff.txt)
prove exact old/new binary patches, full messages, authors/dates and all474
non-lock entries. The original doc review stays scoped to82aacc, with lead's
[accepted narrow correction](../../documentation-oauth-setup/doc-oauth-r1/lead-acceptance.json).

The hook passes static `switch_user_revoke_params: { 'close_sso' => '1' }` while
retaining `settings.fetch('switch_user', false)`. No private JSON field, fallback,
logout change, sanitization or ExceptionMailer change. Instructions retain common
client/key, both-host ownership/modes, paired service restarts and rollback.
The matching API bundle and authored hook must ship or roll back together; an
older HaveAPI rejects the new option. Producer HaveAPI owns the switch-only
behavior; this site only forwards the accepted option.

The [whole final lock](whole-final-lock.json) changes only services lockedrev,
NAR and timestamp. All other nodes/originals/follows remain exact freshbase,
including upstreamWebUI70bd, devWorkspace, nixpkgs/node channels and notification
follows. [158 resolved paths](semantic-input-delta.json) differ only for services
and its existing WebUI/notification follows. Selected097 source is
`/nix/store/zqx1dw5amlsjqjdyp8q5wk5cvwzl3yg1-source`, NAR
`sha256-NPeSoec5VuDuz/Gi6CR6LzkKmbKhRGIJwaW2zk0vxrg=`. Native lockedsource fetch,
Git timestamp and relevant exact source-file bindings are in final-proof.json.
The native [pin message](final-pin-message.txt) retains upstream610's already
merged gem update plus E2's097 adoption; [selected product range](product-pin-range.txt).

Verification is QUICK ONLY by explicit user direction. Existing hook spy8/0,
Ruby syntax and scoped lint apply through exact unchanged source/tool inputs:
[original hook evidence](../site-hook/committed.json). The spy does not prove
actual library/SSO behavior. E2's [actual bundle constructor/artifact proof](../../haveapi-0321-product/consumer-load.json),
[product review/remedy](../../haveapi-0321-product/R1-final-proof.json), and
[publication](../../haveapi-0321-product/publication/final-proof.json) retain their
separate scopes. Producer behavior proof is supplied by lead's accepted
[release handoff](../published-release.json); no duplicate campaign is requested.

Normal confctl pin exited0/31.7425s, native77155, with precommit/commit-msg PASS;
its native generated-message TextWidth advisory is retained per repository rule.
Final JSON/native Nix parse/diff batch exited0/12.0850s, native53934. No system
or host evaluation/build, closure reconstruction, runtime/services/API/PHP/cache/
foundation/browser/real-provider check or production snippet was executed.
No new CI observation or CI-pass claim. All handles consumed/PIDs gone.
No publication, default integration, claim, deployment, PR, lifecycle or cleanup.
Private/live/frozen249f, old refs and roots are retained. Source writer idle.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/)
