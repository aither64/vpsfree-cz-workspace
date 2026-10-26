# Affected final review: deployed baseline and source admission

Retained independent reviewer 01a172a0-e739-7563-85b4-f3c8fc7f0ef2, saved gpt-6.1-sol/xhigh, read-only. Same coherent delivery change; reuse original review.md and reboot-review.md for unchanged behavior. All intended changes are now committed, clean and quick checks pass. High risk; general, architecture, scope and risk lanes apply to source lock waiting and deployed-baseline composition. Read mandatory-change-review and all four lane references, repo AGENTS, root applicable procedures. Do not launch other reviewers or edit source.

Requested outcome: reliable message submission, preserve uncertain post-write outcomes, recover original proven pre-write stale receipt without duplicate submission, deploy aitherdev without interrupting active Codex. No merge authorization. Trust local operator; preserve concurrent sessions.

Latest bounded design is design.md section Accepted fork source admission refinement. Two CI failures at source EX lock were investigated: Ruby nonblocking acquisition races source readers using runtime SH; exact historical CI holder is unknown. Controlled real Go/Ruby external SH-holder tests prove both source admission stages. Accepted source-bound creation now waits within the existing four-minute cancellable worker, with no destination creation/runtime lock held; identity/lifecycle revalidation follows acquisition. Direct CLI remains nonblocking, existing journal recovery unchanged. Assess deadlock and cancellation, especially source/destination and provider/transition ordering. New test TestAcceptedForkWaitsForSourceReadersAndRevalidates passes (~4.7s): both stages, stable/replaced source, worker cancellation, journal recovery, no native effects while waiting and exactly one fork. Ruby syntax and complete diff whitespace checks pass. Documentation changed docs/dev-sessions.md.

No schema or API change from source waiting. Existing SQLite migration schema 1, predecessor fences schema 4 and backup orphan guard are unchanged from accepted reboot review and prescribed narrow guard. None of this initiative's migration revisions have been merged, released, deployed or externally consumed. Disposable tests only. Original-attempt repair has not run. Existing exact-row repair script remains operational evidence.

The selected runtime changed during preparation. Its immutable source matches ec53874b6eea73bf65099cf19aa1a4bc5a3336aa by Git blob identities. Rebase our three commits onto it was conflict-free; preserve archiveRecoveryPolicy 3. Its c33f5191, f29686a5, ec53874b changes are already deployed baseline from another initiative, not newly designed here. Configuration preserves f5d55557 deployed retention documentation, but consolidates the superseded ec53874b channel pin into one generated 10bb0475 -> final runtime update. Workspace preserves baseline 7f94bfa79 archive artifact removal and eda0d9944 compact tracking/storage behavior by exact cherry-picks onto current shared master; baseline pin564979a0 is replaced by one final own pin. No other session's working files or refs were modified. Confirm inherited tree equivalence and history; archive deletion diff is omitted only from stored text, available in Git.

Pin streams: library has three reviewed logical commits with orphan-backup guard folded into backend commit. Runtime has one library pin, storage integration, browser behavior and separate source-lock correction. Configuration has one final generated runtime pin after inherited docs. Workspace has one final runtime pin after inherited baseline commits. Superseded own pins discarded; deployed baseline refs remain retained. Inspect final complete series below and provide explicit history, repeated-stream and migration conclusions.

Consumers: codex-web owns delivery/storage/browser contracts; dev-workspace imports/pins it, adds runtime capabilities and plan endpoint; workspace composes extension and runtime; configuration selects matching host module. Native Codex 0.163.0, extension767dfd5 and siblings preserved. Composed-lock check passes. Final builds/native/VM acceptance await this review. Activation/SQLite migration is forward-only afterward; candidate must keep policy3 lifecycle formats and submission schema/policy1. See rollout.md and owning docs/submission-storage.md, runtime docs/dev-sessions.md and docs/workspace-portal.md for recovery.

Review changed behavior against original assessed boundaries; do not require a confirmation review for the earlier prescribed orphan guard. Report only concrete findings with severity/lane/file/line, and residual limitations. Write baseline-review.md in this tracking directory. No long checks or live mutations.

### codex-web

Base 872c7ad3962f9fa9b17358244e27f3e3fac59fc5; head 8b60554bc10c2a6bcbf9732a8b77ad959c317036
```
66ab8c0d7e86af214555f8a17cd7ecae68f51831 deps: add SQLite submission storage driver
a9086b0328ce3183c32e8fa93ae917c522fa2b1a codex: preserve delivery recovery across durable admission
8b60554bc10c2a6bcbf9732a8b77ad959c317036 conversation: retry transient non-delivery in the background
```

### dev-workspace

Base 10bb047513c82d1310e8fcaa797e8772f948dd8a; head 101a1850253e7cb17f89c8e01f7d11a1b0860948
```
c33f5191b59358234222a1ecc66fa3bf71c61a4f archive: retain committed heads without checkout backups
f29686a58920dc898b6c368756237385ca969596 workspace: omit tracking from additional source checkouts
ec53874b6eea73bf65099cf19aa1a4bc5a3336aa coordination: expire unused payloads after one day
902f7554f1d33722dfdd23402d2275c2bce07cd6 deps: select transactional message delivery support
9ed22854e6f20ad4f8fa0aaf663e91f71ee76d51 portal: use transactional shared submission receipts
76b5c0cf50ee2967b72523c1d6d5e5822ba7ae74 portal: finish admitted sends and retry transient failures
101a1850253e7cb17f89c8e01f7d11a1b0860948 session: wait for accepted creation source readers
```

### vpsfree-cz-configuration

Base d12a77374b18e15fe7600f95307114e2e1882828; head f20e1863f4562faeb8e0db017e6bff3df8b5fae8
```
f5d5555785b8d179657c4766b44bdba916727576 docs: describe workspace archive and coordinator retention
f20e1863f4562faeb8e0db017e6bff3df8b5fae8 inputs: set devWorkspace to 101a1850
```

### workspace

Base cb89659dfe30af6ce3d8f789c8f5eed60e8451be; head b08175448ae4a22937a7baee8e5888210b75538e
```
9368c8fe95eac840765d48e88eb3a9b2146e246e archive: remove disposable historical verification artifacts
9ab0a185cdf7c86050d9f053def68ca6a71c2c5f workspace: keep compact tracking and provide storage maintenance
b08175448ae4a22937a7baee8e5888210b75538e workspace: select reliable transactional message delivery
```
