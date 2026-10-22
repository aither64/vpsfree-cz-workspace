# Dependency follow-up complete

HaveAPI master and retained feature branch are verified at
`a8ea3132e7efe601aaa8965afe648459b3dab5c5`, tree
`9a596258d912ca2075c36ded30d11b3984c656ae`.

certifi is 2026.10.19 and Ruff is 0.17.1, matched by native Nix Ruff. Nixpkgs
was refreshed; its removal of Ruby 3.3 required the existing development shells
to select Ruby 3.4. The final test-only compatibility correction pairs the server
Gemfile and lockfile in two nested Bundler fixtures. uv lock revision 5 and all
other 25 versions remain unchanged. No application API/auth/version change.

Independent final and affected reviews found no issues; complete four-commit
history has no obsolete/repeated update streams and no migrations. All local
Python/Ruby/Go, integration, standalone package and release-tool checks pass.
All six feature and master CI workflows pass; release publication was skipped.

The user explicitly approved merging after verification. Normal native FF and
SSH master-only push succeeded from c1823f3 to a8ea313, all hooks passed, owned
scratch target removed, claims released and feature/recovery refs/stash retained.
See state.md for current summary and linked detailed evidence. Original failed
setup/test/bookkeeping logs remain truthful and separate from later proofs.

No package release, tag, version bump, registry write or deployment was performed.
No operator action remains for this update. The session stays open.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/
