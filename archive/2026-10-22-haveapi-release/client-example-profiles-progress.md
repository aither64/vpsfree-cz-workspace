# Current release progress

HaveAPI master contains the reviewed fixes, dependency refresh and Go/Rust
profiles at67fcd34b. All six local acceptance phases, ten feature CI workflows
and ten master CI workflows passed. Integration hooks/ancestry/claim release are
verified. Five backports at8591394e reproduce the integrated preversion tree.

Version0.30.1 metadata and the changelog dated24October2026 are now prepared.
The maintained target succeeded after isolated native cache recovery. Only18
version paths and CHANGELOG changed; external Python/Rust graphs and JS
dependencies/declarations remain fixed. The old changelog content is preserved.

Required Python and Ruby environments are verified, with source unchanged.
Release quick checks now pass: the metadata check,170 Ruby examples and six
Python tests. The real npm compiler contract and disposable version fixture also
passed. The normal nineteen-file0.30.1 version commit succeeded at91d4293e and hooks
passed. Independent final review passed all four lanes with no findings, including
whole-history consolidation and no migrations. Actual0.30.1 Go/Rust checks also
passed with matching loaded versions and paths, real renderers, and mismatch
controls. The normal candidate feature push, one authoritative automatic build
and fresh artifact verification are authorized through the prepared package.
The feature branch is now published at91d4293e with normal hooks; exact-head
automatic CI passed all ten workflows. Fresh release packaging succeeded and
publishing was skipped. Exact artifact download and manifest/lock verification
are in progress; master/support/tags are unchanged.
Next: independent whole-range final
review, actual0.30.1 Go/Rust checks, one candidate build campaign and supported
branch integration. No tag or package publication is authorized.

[Current state](state.md) records exact owners and evidence. The session stays open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
