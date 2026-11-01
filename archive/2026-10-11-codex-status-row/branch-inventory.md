# Final branch inventory

## dev-workspace

Base: `27ff7949944f79322b810fae7dd1a6e359d985c4`
Head: `17222c374bf48c65edc36895e07408c65f1e7b53`

```text
17222c374bf48c65edc36895e07408c65f1e7b53 portal: show team work in one compact status row
```

Final diff: dev-workspace-final.diff.

## workspace

Base: `12f3a91725b2a3565476c8184bd8a92fcf1c8f61`
Head: `7c54c132420ed367cfe0ed8445c8baf925b12d4d`

```text
7c54c132420ed367cfe0ed8445c8baf925b12d4d workspace: select compact Codex status row
```

Final diff: workspace-final.diff.

## vpsfree-cz-configuration

Base: `14cd296ad24cec0d62161f691c7d0374bda9e35c`
Head: `d1f0ce5a9a292039def259fef53c2f17bede4cac`

```text
d1f0ce5a9a292039def259fef53c2f17bede4cac inputs: set devWorkspace to 17222c37
```

Final diff: vpsfree-cz-configuration-final.diff.

## Disposition

One UI commit includes the narrow completed-plan visibility restoration and browser-fixture corrections. Each consumer has one consolidated runtime pin. No obsolete approaches, repeated update streams, follow-up commits, compatibility shims or migrations. The exact final source and consumer heads above were deployed and live-verified; execution and recovery evidence is in [rollout.md](rollout.md). APIs, native launch policy and persisted formats remain unchanged. Complete independent history conclusion and focused step-9 verification are in review.md. Fresh pre-integration refs, clean worktrees and matching saved diffs are recorded in [readiness-refs.json](readiness-refs.json) and [integration-preflight.json](integration-preflight.json). After the user's "merge it" approval, all three exact heads were fast-forward integrated into remote master without rebase or patch changes. Results and post-merge CI are in [integration.md](integration.md).
