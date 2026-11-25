# Accepted-exception merge freshness

Observed 2026-10-22T17:15:38.587140+00:00.

User waived the observed product six failures and AMD-scale-aged-v6 warning as blockers for this change. This is not CI success. Exact current CI39767770407 remains owned by the same600s watcher; distinct new failures remain reportable. Lead critical-section release is still required.

Fresh SSH refs:

```text
846bb469505789ba0b2a405fa5905ba6d8253006	refs/heads/2026-10-20-kernel-check
55c5046514d06fe9398a022c1622bdaae5228841	refs/heads/staging
```

Complete unchanged reviewed series:

```text
8528262315b0794a8f50917cf33c53a07fd14030 os: panic on lockups when crash dumps are enabled (v3)
846bb469505789ba0b2a405fa5905ba6d8253006 os: apply sysctl configuration through runit (v3)
```

Feature and disposable target are clean; target detached55c504. Exact tree df9bd828d843225df749b7a05ed9529bf17425c9 . Patch SHA256 unchanged ee6a55c44aada17410cb6ea8edba274bad3294a47bfcb13be3a13bfd93295d56. Sixfiles+399/-1,no migrations/merges/pins/repeatedstreams. Existing exactv3 backup retained. Declared target Nix environment/ordinary hooks already prepared and postmerge hook passed; no source/input change since. No rebase,newtest,claim or merge performed.

Disposable target: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-kernel-check/vpsadminos-staging-integration`.
