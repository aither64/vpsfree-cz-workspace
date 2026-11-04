# Final candidate export receipt

All four retained exports passed at source `742eb30cb1a8b6766c85e915d26b0400e38244b1`. Each host-only primary JSON guard matched the successful native image configuration before any VM action. Each fixed export input emitted its marker; every native PTY exited0 normally and no VM/process remains from export.

| Image | Actual archive version | Archive SHA256 | Repository tar SHA256 | Transcript |
| --- | --- | --- | --- | --- |
| opensuse-leap-15.6 | leap-15.6 | `6471ec52c13a0fde252cf93f7374d991b1cca46e92961bbed9fd3fc8a34fb21b` | `0dccfae831fea4a8ab7a2d2238b558d74d66b7515bdbd0b7e3ea14cd80b1e1cc` | [session/export-15.6-742.log](session/export-15.6-742.log) |
| opensuse-leap-16.0 | leap-16.0 | `a95c9ef8a89169d6e82687831a468ce12e9be379a002be313a17d7f77bdd2940` | `0546672d9698b4417689d09710cc9b1251cc630428884730d2c82ca1b43bdfa0` | [session/export-16.0-742.log](session/export-16.0-742.log) |
| opensuse-leap-16.1 | leap-16.1 | `5fd3f8fac6c56910aa25842f532c2db7573545ca4e52f0f5a32a5b17b21b40d0` | `f18a77ea2731d3bc9f1a5eb4b6d8de734e9054308d832b6c454a5535492d9d4f` | [session/export-16.1-742.log](session/export-16.1-742.log) |
| opensuse-tumbleweed | tumbleweed-20261103 | `05c4bbe5e73f568ad63498bf96a48543094779229cd66f3e0607d6eba22cb39f` | `a0158658b8dc163f6bc7c16ac3262729f703018452a8b7dc91c3fa00d6eaa8ac` | [session/export-tumbleweed-742.log](session/export-tumbleweed-742.log) |

All Leap builders reported `/etc/os-release` VERSION_ID16.0 and RPM4.20.1; the Tumbleweed builder reported VERSION_ID20261028 and RPM4.20.1. Builder stopped states were restored. The actual Tumbleweed target OS release is20261102, while its archive version is the normal build-date identity tumbleweed-20261103. The isolated repositories live under `/tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-candidates/<image>` with local latest aliases only. No production repository/tag changed.

Normal build identities and JSON hashes are in [the batch receipt](session/final-images-native-742-result.md). All four frozen bootstrap audits are accepted in [the audit](final-completed-case-audit-742eb30cb.md), including explained/preexisting warnings and their limits. Native candidate runtime checks remain separate; these exports prove artifact identity and transfer, not device-unit success.
