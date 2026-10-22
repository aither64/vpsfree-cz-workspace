# Retained-source Overcommit trust recovery

2026-10-20; implementer1; session identity reverified as
`2026-10-19-dynamic-python-api-client` in
`/home/aither/workspace/ai/vpsfree.cz`.

Coordinator run `a9c23f6e-036d-4680-b06b-4b27701c0393` stopped in `prepare`
with exit 75: the ordinary checkout hook rejected a stale Overcommit
configuration signature. No jobs had been submitted and no merge had occurred.
The lead owns the acknowledged handoff and same-run resume.

## Inspected inputs

The failed retained source is:

```text
/home/aither/.local/state/dev-workspaces/coordination/sources/c1823f3d70365b0442d0e2171bdf83bd4c6dbe31/checkout
```

It is detached and clean at reviewed commit
`c1823f3d70365b0442d0e2171bdf83bd4c6dbe31`, tree
`aec5847f4c735ac68a7b6158c76a4f667f6a6a18`.
Each inspected file matched its exact committed contents:

| Path | SHA256 |
| --- | --- |
| `.overcommit.yml` | `37ed119c44c6425dd84c92e97d8a797d3656b8f60cc9b652accd1b768191dd22` |
| `.git-hooks/pre_commit/python_checks.rb` | `34393288512ed5c0fee7549187413db6b67dc8e1bdf8f039f57a04a8f5cb2f9e` |
| `.git-hooks/pre_commit/haveapi_i18n.rb` | `57280b9992d3914434456f3a5ed90060668d6d3369ec9d3313e43405318d7aeb` |

The existing prepared environment artifact was
`sha256:f1efd997ffdfb5bf4333cac0dea83c57581725164e65b111b400b13cec8f5306`,
kind `merge_hooks`, repository `haveapi`, featureHead matching the reviewed
commit. Its file is:

```text
/home/aither/.local/state/dev-workspaces/coordination/sources/f1efd997ffdfb5bf4333cac0dea83c57581725164e65b111b400b13cec8f5306/artifact.json
```

The retained artifact's environment was overlaid on the process environment
for the ordinary Bundler/Overcommit commands. Environment values were not
printed or changed in the artifact.

## Authorized correction and evidence

The lead explicitly authorized ordinary CLI signing of the inspected final
configuration and plugins, including its normal shared trust effect in
`/home/aither/workspace/ai/vpsfree.cz/repos/haveapi.git/config`.
No manual configuration edits were made.

From the exact retained checkout, under that prepared hook environment:

```sh
bundle exec overcommit --sign
bundle exec overcommit --sign pre_commit
```

Both commands succeeded. Overcommit reported that plugin signatures had not
changed. The stored configuration signature changed from
`689faa60978769404adfbfa8665fda4599f9813868d38b5fe170cb3d6273711a`
to
`b60e0548237424002fc3f5930a5c0bf3743f5e7fa671f82d380ae0cf7729a4cb`.
`overcommit.configuration.verifySignatures` remains `1`.

The existing ordinary post-checkout hook, resolved through
`git rev-parse --git-path hooks/post-checkout`, then passed when invoked with
Ruby under the same environment and arguments:

```text
c1823f3d70365b0442d0e2171bdf83bd4c6dbe31 c1823f3d70365b0442d0e2171bdf83bd4c6dbe31 1
```

The full signing/validation command exited 0. Its final assertions confirmed
the retained source still has exact reviewed HEAD and an empty status/index.
Bundler emitted local missing-extension warnings for unused gems; these did
not prevent signing or ordinary hook verification.

## Handoff boundary

The retained-source signature failure is corrected. The lead may resume the
same coordinator run through its ordinary interface. Recovery did not resume
the coordinator, submit jobs, merge, push, rebase, edit source or refs, disable
checks, or modify coordinator artifacts or ledgers. Recovery refs and the
retained stash are preserved. No release operation was performed.

A later old-master target checkout could present a different historical
configuration. That target has not been signed preemptively; an actual later
failure requires inspection of that exact accepted configuration first.

The integration request's original premerge/review/verification evidence is
unchanged. This separate file records only the new hook recovery.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/>
