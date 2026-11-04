# HaveAPI prepared integration commands

Preparation is outside a claim. The parent must accept the affected review and
prepared equivalence first, then acquire and verify one exact session-owned
HaveAPI repository merge claim. These commands do not authorize that action by
the preparation owner.

Prepared target:
`worktrees/2026-11-01-typescript-client-migration/haveapi-integration-target`,
clean and detached at `eb91a4d031c2c1f1c6ec6dd1aaed62e1f320eea7`.
Prepared registered feature and separate candidate both identify
`f29c1e4675bc1f79641faa619b8c68ecec923c71`, tree
`63e1cfcee1ff75a9cc03e5f18ebbf7d44eec76e1`.

The exact already-realized Ruby/Git/Node and existing gem environment is in
`environment.sh` beside this file. Both configuration and all three custom hook
signatures verified, and native target post-merge/pre-push hook preflights
returned zero. No dependency install or trust bypass is needed.

After the parent verifies its held claim, the short critical section is:

```bash
set -euo pipefail
source /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/artifacts/package-s/haveapi-integration-preparation/environment.sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/haveapi-integration-target

test "$(git rev-parse HEAD)" = eb91a4d031c2c1f1c6ec6dd1aaed62e1f320eea7
test -z "$(git status --porcelain=v1)"
test "$(git rev-parse refs/heads/2026-11-01-typescript-client-migration)" = f29c1e4675bc1f79641faa619b8c68ecec923c71
test "$(git rev-parse 'refs/heads/2026-11-01-typescript-client-migration^{tree}')" = 63e1cfcee1ff75a9cc03e5f18ebbf7d44eec76e1
remote_master=$(git ls-remote origin refs/heads/master)
test "${remote_master%%[[:space:]]*}" = eb91a4d031c2c1f1c6ec6dd1aaed62e1f320eea7

git merge --ff-only f29c1e4675bc1f79641faa619b8c68ecec923c71
test "$(git rev-parse HEAD)" = f29c1e4675bc1f79641faa619b8c68ecec923c71
test -z "$(git status --porcelain=v1)"
git push origin HEAD:refs/heads/master
remote_master=$(git ls-remote origin refs/heads/master)
test "${remote_master%%[[:space:]]*}" = f29c1e4675bc1f79641faa619b8c68ecec923c71
git ls-remote origin refs/heads/master refs/heads/2026-11-01-typescript-client-migration
```

Inspect ordinary hook results before pushing: Git can report a successful merge
after a failing post-merge hook. If master moved or a hook needs intervention,
stop, reconcile effects and release the claim before repair. Reconcile any
uncertain push by authoritative remote ref inspection before release. Release
the repository claim immediately after exact remote proof, before CI, records,
handoff or cleanup. The parent owns these claim operations and resulting proof.

The existing remote feature must remain at exact old `52c37027` to retain
`eea3ae5e` reachability for the selected client provenance. Do not force-push or
delete it. The prepared equivalent successor can become literal master ancestry;
the nonancestor old `52c37027` must not be described as literally merged.

A master push runs build-only checks. `.github/workflows/release.yml` permits
its publication job only for a canonical-repository tag push, behind the
protected `release` environment. No tag, version change, registry upload,
environment approval or deployment is part of this integration. The user owns
release in another session.
