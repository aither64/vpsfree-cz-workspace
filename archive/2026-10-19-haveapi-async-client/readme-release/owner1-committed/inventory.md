# Committed README/release handoff

Head `349aacd53790c6c820fe2dacc8cb6d151c92d0fc`, tree `c80eaddb6e42633d154c15b020e4e74b9faa8d76`, clean tree/empty index. Documentation commit changes
only README.md, clients/js/README.md and doc/agent-instructions/releases.md. Both
author and committer are Jakub Skokan <jakub.skokan@havefun.cz>, command scoped in
the normal top-level Nix context. Installed Overcommit precommit and commit-msg
hooks passed, with nonblocking body-width and ambient extension warnings; no bypass.

Complete eight-commit range `c58704a08451a231fdf6c6123437133422af46dc..349aacd53790c6c820fe2dacc8cb6d151c92d0fc`:

```
991101f212eb7da24b5ba71e679eb4b59baef56d clients/js: capture callback bundle compatibility
0d2111e5a93490abbad2f5167d45dea026f663f3 clients/js: author callback client in TypeScript
8f8e5766b8be9c99d2bf39a9e1fe7f80220fade5 clients/js: add an independent typed Promise client
f3fcd33fdbc1d00461535d95f0337c44aa0d12d4 clients/js: document TypeScript source workflow
19c20c90cc957d4225ece50a92e190855f252710 clients/js: expose the callback client as CallbackClient
f94e65e35166a0bf8048a27c9d57c7d36957d65b clients/js: preserve nested API rejection errors
3a79c8ec0863de22823ab5f2031a6e845f612afb release: validate packaged JavaScript client interfaces
349aacd53790c6c820fe2dacc8cb6d151c92d0fc docs: explain JavaScript and TypeScript client usage
```

The five earlier client implementation/compatibility/naming commits remain; f94
adds the reviewed nested-wire-error correction, 3a79 adds bounded release gates,
and349 adds only current documentation. No migrations or runtime/deployment/state
conversion. No new dependency/pin update stream; VERSION, package/lock, client
source/generated outputs, workflow, publisher and build scripts equal f94.
No history rewrite, rebase, push, version/tag, registry publication or WebUI repin.

The complete final diff and latest f94->head delta are retained beside this
inventory. Final independent review and real isolated retained-tar runtime/type
smoke remain pending. The guide describes those implemented checks without
claiming their actual tarball operation has run. Git/index slot is released.
