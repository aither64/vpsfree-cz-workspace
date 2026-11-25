# Final API schema export receipt

- Source: `git@github.com:vpsfreecz/vpsadmin.git` at `da7724abdc080e59820cc4f0812ce1a41b3fc5df`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-exception-root-cause/vpsadmin`; clean before/after. Exporter itself requires clean committed source.
- Command: `bash /tmp/exception-root-cause-export.sh`; exact command recipe follows `docs/api-schema-export.md` using `nix develop .#vpsadmin`.
- Result: exit 0, approximately 2m25s. Database-free safety/snapshot checks: 14 examples, 0 failures. Two independent fresh-database exports: 529 actions / 156 resources each.
- `cmp` succeeded for schema, provenance and tooling lock between `/tmp/exception-root-cause-schema-1` and `/tmp/exception-root-cause-schema-2`.
- Complete log: `/tmp/exception-root-cause-export.log`. Source session 10160 and enclosing watcher invocation 3790 completed; no owned work remains running.

## Raw artifacts

Primary directory: `/tmp/exception-root-cause-schema-1`. The repeat directory has byte-identical artifacts. Preserve these raw files unchanged for the three client assessments.

| File | SHA-256 |
| --- | --- |
| `schema.json` | `7e2a529787c06944f1ad0cdf3369edd8b4650d79826f3bbda9101af2dfb67628` |
| `provenance.json` | `59194958ead214f70ff7835a0fec5e6d3280cfca6d31ddd2a97e3276e96186e8` |
| `tooling.Gemfile.lock` | `64c1663d2fd040dd5bf0e92aa7a5b2a1b187c5d464ba9b2cc5154aaf16729b69` |

## Profile and tools

- API `7.0`, protocol `2.0`, profile `vpsadmin-full-fixture`, locale `en`, acquisition `mounted-source`.
- Plugins: `monitoring`, `newslog`, `outage_reports`, `payments`, `requests`, `webui`. Their exact source hashes and migration inventories are in raw provenance.
- Ruby `3.4.12`, Bundler `4.1.1`, HaveAPI `0.32.2`, ActiveRecord `8.1.4.1`, mysql2 `0.5.7`.
- Database: `11.4.13-MariaDB`. Each export uses the normal isolated temporary database runner; no shared or deployed database is used.
- Tooling Gemfile SHA-256: `87df3509b79a68dcf55f4f344017c619a8fcf0dbb9e70e576a2d2d39891a8ef2`; tooling dependency-lock SHA-256 is recorded above. Full exact installed gem/version/archive inventory and input-file hashes are retained in provenance.
- Repository `flake.lock` SHA-256: `217f28c000b42194924caf06dea8348ea52b18a2cca512ffd39b814c116d2858`.
- Fresh watcher: GPT-6 Luna/low, installed package `/nix/store/1zn1a51qrsin83fszrprdjp45208vsj4-dev-workspace-0.2.0`, catalog `1184a2cf511b6e77ff7afe12433027abe06e8bb0b897f39cffc26efd443d1a7c`; explicit danger-full-access / approval never. No saved team settings changed.

Implementer1 owns Go/Rust/TypeScript comparisons against these exact raw artifacts; no generated client files are edited by package B. Client freshness is pending until that report arrives. This receipt is evidence, not integration or deployment approval.
