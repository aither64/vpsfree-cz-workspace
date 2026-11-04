# Integrated synchronization rules

All six documentation changes have been integrated by fast-forward and normal SSH push. Fresh remote heads match the reviewed final candidates. Every repository claim was explicitly released and checked; the workspace tracking lock was released after preserving unrelated records. No deployment or lifecycle action was performed.

| Repository | Target | Integrated head |
| --- | --- | --- |
| vpsadmin | master | `4ac49f49e63545200df8afa920c6eafda8722523` |
| vpsadmin-go-client | master | `af9a819ca35f6de5556092679b4df7cb72e7aa89` |
| vpsadmin-rust-client | main | `823a4f8450fce4947310fc81bcdebdca91d9ffae` |
| vpsadmin-typescript-client | main | `2da950a98fa13468b36d03b13fb5e81cca206e0e` |
| workspace | master | `08ec23ca587067ea7653610a200277b750aa4a52` |
| vpsadmin-webui | main | `47b6992e28c16585aa6247bd75413637a7ca6388` |

WebUI [PR127](https://github.com/vpsfreecz/vpsadmin-webui/pull/127) is merged at its exact reviewed head. Its four pre-merge workflows passed all ten jobs, with expected browser skips and no flaky annotation visible in retained logs. Original and all refreshed review ranges remain preserved, with independent history/migration conclusions and separate tree reconstructions. No migrations or repeated update streams remain in any final documentation range.

The canonical procedure is public in [vpsAdmin](https://github.com/vpsfreecz/vpsadmin/blob/master/docs/api-schema-export.md#generated-client-synchronization). Its public bytes match the reviewed SHA256 `109f3830f889d61785c17831b795ee3a611f624c3a4a25c0707eada31b3c53c2`. It requires source-specific client assessment and remote-default completion, preserves release-free ordinary synchronization, and gates dependent WebUI merges on a published SDK. TypeScript releases default to the next minor unless the user overrides it.

The rejected HaveAPI change was removed entirely before integration: its feature and public baseline remain `f29c1e4675bc1f79641faa619b8c68ecec923c71`, with zero owned delta. Prior acceptance, the rejected commit/ref/patch, immutable generator source and old receipts remain historical evidence. Site-specific routing stays in the workspace verification guide; no additional site-extension feature was needed.

Published Phase1 client releases remain Go0.2.0, Rust0.2.0 and TypeScript0.4.0. This documentation integration introduces no runtime/dependency/schema/version changes and authorizes no deployment.

## Final automatic checks

The exact eight default-push runs are terminal and recorded in [the final CI receipt](phase2-integration/default-ci-result.md). Seven workflows succeeded; API Specs41822368583 failed the existing security-advisory assertion, with topic coverage failing consequently. Job totals are41success/2failure/1intentionallyskipped (TS publication). All WebUI default CI/broad/smoke jobs passed; expected browser skips are retained, with no flaky summary visible. Lead independently checked every terminal JSON against the exact run/head manifest. The single fresh Luna/low observer finished and released capacity; no operation remains. Earlier feature checks retain their own scope and are not relabeled default results. No manual workflow, retry or rerun was started.

## Evidence

- [Integration commands, approvals and released claim identities](phase2-integration/results.json)
- [Fresh SSH remote proof](phase2-integration/final-remote-proof.json)
- [Independent reviews and all lineage addenda](phase2-review-result.md)
- [WebUI pre-merge CI terminal results](phase2-webui-final-ci-result.md)
- [HaveAPI removal](haveapi-guidance-removal.md)

The attempted final peer handoff was not confirmed. Runtime list/history shows the pair grant revoked because the peer session was archived/deleted. No retry, new grant or peer-file access was attempted; the peer completion notice remains retained. This does not affect the approved source integrations.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/)

## Unresolved default API check

API Specs41822368583 failed one existing visibility example in
`api/spec/api/resources/security_advisory_spec.rb:487` (assertion522, ID[1:3:2],
seed13353;239examples/1failure). Anonymous draft-advisory CVE filtering with
count/includes returned HTTP200 with statusfalse and a security_advisory input
error instead of the expected successful empty response. Coverage correctly failed
because the full matrix failed; both modes cover all417eligible files in13topics.

The same-source feature run passed that example, but its effective dependency
lock selected Rails8.1.4/mime-types-data3.2026.1027, versus Rails8.1.4.1/
3.2026.1103 in the failing default run; random order also changed. Prior success
is not equivalent-input evidence. The specific validation rejection and cause
remain unproven. The example predates our base and the integrated commit changes
only Markdown. Documentation delivery is accepted with this explicit baseline
residual; no unrelated runtime/test/dependency change or blind rerun was added.
Detailed raw failure/result/environment artifacts and both effective locks are
retained through [the API receipt](vpsadmin-local-ready.md). Further diagnosis is
separate product/dependency work, not an uncompleted documentation patch.

## Final disposition

Documentation/release task delivered. Six final feature heads are integrated,
all repository claims released, all automatic workflows terminal, and the one
baseline API failure explicitly accepted as an unresolved residual with retained
raw evidence. No outstanding in-scope change, test, integration or deployment.
This session stays open; no cleanup or lifecycle action is authorized/performed.
