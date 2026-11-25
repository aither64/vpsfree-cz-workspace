# vpsAdminOS staging integration receipt

On2026-10-22, user explicitly accepted the observed six product-test failures
and AMD-scale-aged-v6 scheduler warning as nonblocking for this change. Lead
accepted the final freshness packet and released the critical section. This is
an accepted-exception integration, not a successful broad-CI claim.

Target advanced by ordinary fast-forward from
`55c5046514d06fe9398a022c1622bdaae5228841` to
`846bb469505789ba0b2a405fa5905ba6d8253006`, tree
`df9bd828d843225df749b7a05ed9529bf17425c9`. Exact reviewed two-owner series
852826+846bb remains unchanged: sixfiles+399/-1, no merges/migrations/pins or
repeated streams. Feature and disposable target remain clean.

Single repository claim `8c19bca8-754b-4b6c-9400-78ab645943f0` was acquired and
verified held17:18:38Z. Fresh SSH refs/cleanliness matched expected target and
feature. In the prepared disposable target's normal Nix environment,
`git merge --ff-only 846bb469505789ba0b2a405fa5905ba6d8253006` exited0 with normal hooks
and no hook failure, then non-force SSH `git push origin HEAD:refs/heads/staging`
exited0. No hook bypass or new commit/rebase occurred.

Independent direct SSH ref proof at17:19:40Z:

```text
846bb469505789ba0b2a405fa5905ba6d8253006 refs/heads/2026-10-20-kernel-check
846bb469505789ba0b2a405fa5905ba6d8253006 refs/heads/staging
```

The claim was immediately released17:19:57Z, then independently read back as
released (revision2), before these records or CI follow-up. Evidence:
[merge output](generic-sysctl-merge-command.log),
[normal SSH push](generic-sysctl-merge-push.log),
[final readiness](generic-sysctl-premerge-accepted-exceptions.md).

Original run39767770407 completed with failure at 2026-10-23T01:14:16Z: all
11 jobs terminal, eight successful and three failed. The product suite and
aged-v6 failures were the accepted merge exceptions; the later aged-v5 RCU
stall was separately reported after integration. Complete metadata, first
evidence and limits stay in [the failure note](generic-sysctl-ci-failure.md).
The same600s observer returned; its exact watch exit1, CLI exit0 and
[no-active receipt](generic-sysctl-ci-39767770407-no-active-observer.json)
complete this original run's accounting. No duplicate observer, workflow, retry or cancellation was launched
for integration. Automatic target-push CI, if created, is not claimed as watched
or green by this receipt.

Feature branch, backup refs, worktrees and session remain retained/open. No
configuration pin update, deployment, production runtime write, machine claim,
archive, delete or cleanup occurred.
