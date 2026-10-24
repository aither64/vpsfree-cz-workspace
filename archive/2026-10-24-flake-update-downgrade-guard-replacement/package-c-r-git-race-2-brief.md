# Prepared real Git race successor

The first fixture attempt is preserved at
`/tmp/flake-update-guard-downgrade-guard/git-race/`. Its ordinary stale push
rejected with status 1 and the fresh-baseline guard rejected the old tip with
status 3. Equality returned 0. HEAD, index, flake.lock and local remote remained
at the intended manual pin. Its final strict status check saw only the normal
rejection log under .confctl/logs and reported failure. No provider/application
defect was identified and no external remote was pushed.

[Exact failure/effect reconciliation](package-c-r-git-race-failure-reconciliation.json)
records manual/fresh/remote commit `47c2546beb7a29a8ccc4903b66411260724f4472`,
byte-identical original/final index, unchanged baseline lock, exact local-only
push URLs, the one untracked runtime log, and no remaining owned process group.
The original script hash is `5c5ff67aba1e412888f5d0db1a005e4bd3535356705fb5502a8d1eee2e585ff1`.

The successor changes only owned-clone setup: before snapshots or checker
commands, append the exact anchored rule `/.confctl/logs/` to that clone's own
.git/info/exclude, recording the path/rule/hash in its receipt. Strict final
porcelain/index/HEAD/lock/local-remote assertions are byte-identical. No broad
ignore, cleanup, environment sanitizer or relaxed final assertion is added.
[The exact diff](package-c-r-git-race-2.diff) and
[static preflight](package-c-r-git-race-2-preflight.json) preserve this boundary.

Both original and successor require --root and pass the parsed value directly
to the unchanged driver's Operation, which uses Path(args.root).absolute().
No source ignores or substitutes the requested root. The first launch's
complete argv is not retained in the local log, so the provenance of the
unexpected caller-selected root cannot be established from that log. The new
command below explicitly selects a separate exact root; no old root is reused.

Frozen successor source SHA-256: `a438361c71aff87c771dfc1f2c1d85066a40d1899789a797617da70018af4823`.
Unchanged driver SHA-256: `237b5b40646218726a33355ec0a35a706e96330390454621035558291b70f1bf`.
Unchanged manifest SHA-256: `bbeec793c0c6407023bd4f5eda8d942dbeaeded7cc7e435725d4352575023e8c`.
Provider remains R `5436d3d7c36d3d5174eab3c44e3578830749d3db`, with original
review-r-report.md SHA-256 `2b9ecce9d66a5994e664b99ba0c1f1454631c14a923a53f58b25ece48ded99a9`.
The local immutable ancestry fixtures remain initial9d63ab4f, stalecc40679d,
manual5436d3d7. Actual provider/API checking, real bare remote and ordinary
nonforce Git rejection remain enabled.

Prepared only; no successor command or watcher has run. After the lead's current
Terraform VM operation, a fresh serialized Luna watcher may run this exact
command from /home/aither/workspace/ai/vpsfree.cz with GITHUB_TOKEN supplied
privately:

```sh
python3 work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-r-git-race-2.py \
  --root /tmp/flake-update-guard-git-race-r-2 \
  --review-receipt /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/review-r-report.md
```

Require the receipt under the exact new root's git-race/ directory. On any
nonzero result or different root, stop and report; do not diagnose, retry, edit,
clean up, use an alternate root or push externally. Keep the original failed
attempt and retained R package out-link. No source commit, integration,
deployment, machine ownership or session lifecycle action is part of this check.
