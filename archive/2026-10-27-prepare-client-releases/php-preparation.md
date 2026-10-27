# PHP mirror 0.31.0 candidate

Integrated and published after independent history review and explicit user
approval of PHP master, tag and PHP-first order. Lead verified the atomic SSH
push and released repository ownership before protected HaveAPI publication.
Packagist now indexes the exact candidate. No repository claim is held.

## Exact source and original artifact

- HaveAPI source: `c9124da141adc258fbbaf67d4ec19ee3f8580849`.
- Corrected annotated HaveAPI tag object:
  `d300dfa8715cca35c29bce312333ece886b5e74e`.
- Tag build: https://github.com/vpsfreecz/haveapi/actions/runs/40554625752 .
  Build job `122367248732` succeeded. All other 19 current-head native
  workflows succeeded; the protected `release` environment is waiting.
- Original artifact ID `12756023295`, `release-40554625752`, size 1,099,112
  bytes; GitHub artifact digest
  `sha256:8f32e6db10c1fe93a538411b05df6076072201a1500d29f6039555f5bf044d76`.
- Local original download: `haveapi-tag-40554625752/` in this session.
- `release-manifest.json` SHA256:
  `6e31e4c59e4629adeff0fd8f00e86935b644b6018c3d53361450b07a1b102a49`.
  Schema 1, version 0.31.0, source above, run ID 40554625752. It retains all
  five gems, npm/browser/PHP/Python outputs and notes (11 payload files), with
  hashes and all ten actual resolved dependency-lock texts.
- Retained `haveapi-client-php-0.31.0.tar` SHA256:
  `41cad3619e9a26f6e8ecb2bae1afb008ba0e1325df0f94b6c27e04a3f685aea8`.
- Tools-only verification at the exact HaveAPI source passed:
  `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c ruby utils/release/cli.rb verify`
  with the absolute artifact directory. No rebuilding or manifest editing.

## Repository, worktrees and candidate refs

- Canonical repository: `git@github.com:vpsfreecz/haveapi-client-php.git`.
- Default target: `master`, freshly checked at
  `a02dd2506209f54ea782fbd949243207bf9f93bc`, the published 0.30.2 commit.
- Feature branch: `2026-10-27-prepare-client-releases`.
- Registered feature worktree:
  `worktrees/2026-10-27-prepare-client-releases/haveapi-client-php`.
- Prepared clean detached target:
  `worktrees/2026-10-27-prepare-client-releases/haveapi-client-php-target`,
  at the exact saved base above. No merge has run.
- Candidate head: `eafc2a9b77990dd5c927f0d412d14801261223cc`.
- Local annotated `v0.31.0` object:
  `fe2e2355933f334244e8bb80a31ce4bd6c02af4f`, peeling to candidate HEAD.
- Only the preparation feature branch is published. Fresh SSH readback proves
  that exact feature head and unchanged remote master; remote v0.31.0 is absent.

## Complete history and quick verification

The complete base-to-head series is one commit:

```text
eafc2a9b77990dd5c927f0d412d14801261223cc
Release 0.31.0

HaveAPI-Source: c9124da141adc258fbbaf67d4ec19ee3f8580849
```

Final diff: `composer.json` and `src/Client.php`, two insertions and two
deletions, changing only 0.30.2 to 0.31.0. No migrations, runtime changes,
obsolete approaches, follow-up fixes, repeated dependency/pin streams or
transitional compatibility paths exist in this range. No candidate release
tag/master has been deployed, published or externally consumed. The feature
branch publication is preparation only.

Fresh complete tree inspection found no AGENTS.md, repository Nix shell,
release/development procedure or hook-framework configuration. README and
composer metadata were read; core.hooksPath is unset, and only sample hooks
exist. Normal Git commit/tag/push ran through the HaveAPI top-level tools-only
Nix shell; no hooks were disabled and no new framework was installed.

Read-only `Publisher#preflight_php` against the original retained artifact
returned false at the clean 0.30.2 base, permitting a new candidate. Extracted
only the verified PHP tar into `php-tag-snapshot-40554625752/`, then copied with
`rsync -a --delete`, preserving `.git`, `AGENTS.md` and `.github`. Inspected the
two-line version diff, passed `git diff --check`, and committed through the
required message file. Created the local annotated tag through that same file.

After commit/tag, the exact-source tools-only `Publisher` constructor verified
the whole original artifact; `preflight_php(candidate)` returned true. This
proves byte/mode snapshot equality and the exact HaveAPI-Source provenance
required by the future workflow. The peeled tag equals candidate HEAD, which
descends from the saved remote base. No publish/sync_php/credential helper was
called, and no GITHUB_* environment was spoofed. Comparison captured with
`dev-session worktree capture-comparison ... haveapi-client-php --as-is`.

No additional application tests were needed: the tagged coordinated build
already tested PHP, and the candidate is the verified original tar. Existing
release procedures remain sufficient; this document records only this rollout.

## Next operator boundary

The named review, approval and integration boundary completed. Lead's claim
`18deacb8-41f8-41c8-915f-d03ef92c8645` was authoritatively released at
2026-10-27T18:07:40Z before protected approval. Independent final readback proves
remote master and peeled v0.31.0 equal candidate `eafc2a9b77990dd5c927f0d412d14801261223cc`,
with annotated tag object `fe2e2355933f334244e8bb80a31ce4bd6c02af4f`.
Packagist p2 and cache-distinct package metadata now list 0.31.0 with source and
distribution references equal to that same commit. The HaveAPI publish workflow
confirmed the existing PHP tag and completed successfully; see the final
[publication receipt](haveapi-preparation.md#final-publication-receipt).
No PHP action remains. Keep original artifacts and refs under the existing
recovery contract; no session lifecycle action is authorized.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-prepare-client-releases/

## Approved integration receipt

User explicitly answered "Approve PHP sync and finish release" to the question
covering this exact PHP master/tag update, PHP-first ordering and subsequent
protected HaveAPI publication. Lead acquired PHP-only claim
`18deacb8-41f8-41c8-915f-d03ef92c8645`, confirmed held ownership, exact feature/tag,
clean target at the saved base and fresh remote master/tag absence. Normal
`git merge --ff-only` fast-forwarded the detached target, then
`git push --atomic origin HEAD:refs/heads/master refs/tags/v0.31.0` succeeded.

SSH readback proved remote master and peeled tag exactly
`eafc2a9b77990dd5c927f0d412d14801261223cc`, annotated tag object exactly
`fe2e2355933f334244e8bb80a31ce4bd6c02af4f`. No hooks were bypassed. Claim release
and authoritative released-state readback completed at 2026-10-27T18:07:40Z,
before records, CI waits or protected publication approval. No machine was
reserved or deployed. These receipts supersede the pending-operation status
above without changing its reviewed preparation evidence.
