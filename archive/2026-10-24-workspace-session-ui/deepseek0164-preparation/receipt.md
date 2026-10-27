# DeepSeek 0.164 static preparation

Complete frozen managed profile: **PASS**, exit 0; 0.49 seconds inside the
one-off runner. Runtime/provider acceptance is pending final outputs and review.

Identity was verified with `dev-session current` and both environment values:
`2026-10-24-workspace-session-ui`, `/home/aither/workspace/ai/vpsfree.cz`.
Same-session roster confirms implementer3 and implementer1 have workspace-write
access. Implementer1 supplied the already-realized declared checker environment
and confirmed no duplicate DeepSeek validation was running.

## Frozen inputs and result

Configuration comes only from canonical bare Git objects at
`b167cd4388a5c94ff3f978df85b6800fafd1b8af` in
`repos/vpsfree-cz-configuration.git`. No configuration worktree was inspected or
changed. [static-result.json](static-result.json) records every source's Git blob,
mode, byte count and SHA256; exact public snapshots are under `source/`.

| Input | SHA256 |
| --- | --- |
| `cluster/cz.vpsfree/machines/aitherdev/config.nix` | `e728c6c268efd7bac76cac32649eab24683ff64e6a51ee16bca59f02f4fc76f5` |
| Extracted complete [ds.config.toml](ds.config.toml) | `2f56fd540dd93ccef16c7963dba59fb2e452af5a9ec4f78c2510e743d70374e3` |
| `packages/codex-deepseek-models/models.json` | `bce20f679495809f4fa6e48672b6dcbab84b6adff5251890b6e6a21eddb9c12f` |
| Exact raw 0.164 `core/config.schema.json` | `ea611ee3f12a6df314b3e49585015ec6e2ebc7c3f072ccbf63c21306a4cdb5dc` |

Schema path:
`/nix/store/10pdz4z8bfg35ysd7aqrhnzdkijpmmwb-source/codex-rs/core/config.schema.json`.
This is the retained raw 0.164 source for upstream
`6aaac694803004a63c6f393d153c96d22521a6b9`; its earlier source prerequisite
receipt remains authoritative for the source NAR and package patch provenance.

The literal `codexDsConfig` block has **nine string leaves**, not ten. The
runner extracts the complete block, rejects interpolation/escaped Nix strings,
parses it with `tomllib`, checks the exact schema, then calls the existing
`jsonschema.Draft7Validator(schema).iter_errors(profile)` on the entire object.
It does not run the unrelated 55-restriction utility-policy test.

| Managed key | Exact string value |
| --- | --- |
| `model_provider` | `deepseek` |
| `model` | `deepseek-v4-pro` |
| `model_reasoning_effort` | `high` |
| `web_search` | `disabled` |
| `model_catalog_json` | `/etc/codex/deepseek-models.json` |
| `model_providers.deepseek.name` | `deepseek` |
| `model_providers.deepseek.base_url` | `https://api.deepseek.com/` |
| `model_providers.deepseek.wire_api` | `responses` |
| `model_providers.deepseek.env_key` | `DEEPSEEK_API_KEY` |

The selected catalog contains `deepseek-v4-pro` and supports `high` reasoning.
No `forced_login_method`, `preferred_auth_method` or
`model_supports_reasoning_summaries` was added. The catalog check here is JSON
parsing and selected model/effort membership, not native catalog decoding.

Executed command, from this session's tracking directory:

```sh
/nix/store/5a0h3d6488628sh6w1ccqk8dizvmp8ji-python3-3.13.15-env/bin/python3 \
  deepseek0164-preparation/check-frozen-profile.py
```

Python 3.13.15 / jsonschema 4.26.0 is the already-realized environment selected
by codex-web's declared `python3.withPackages (... jsonschema ...)`. Canonical
codex-web `8b60554bc10c2a6bcbf9732a8b77ad959c317036:flake.nix` declares it;
`test/codex_ephemeral_config_contract.py` establishes the existing Draft7
checking approach. The retained `codex-web-0164/run-go-quick-nix-v2.sh` records
this exact interpreter. No Nix setup, evaluation or realization was launched.
The one-off runner writes new receipts exclusively and refuses to overwrite
them; a repeat needs a separately owned evidence directory.

## Remaining gates and handoff

The source wrapper executes the assembled package with `-p ds`. Activation
installs the managed profile as `ds.config.toml` mode 0600 and installs the
catalog under `/etc/codex`. Source inspection confirms these declarations;
their final built/deployed identities remain unverified. Raw 0.164 source
`config/src/loader/mod.rs:131` and `cli/src/main.rs:2030` confirm that `-p ds`
selects the profile file under the selected `CODEX_HOME`.

[future-verification.md](future-verification.md) prepares the output-gated
assembled/system/Home Manager wrapper checks and one isolated strict-config
provider request. The wrapper always reads the production key file, so the
isolated request uses the same verified assembled launcher directly with
`-p ds` and a securely supplied provider environment key. Installed wrapper
resolution is checked separately without executing it.

No native executable, provider request, production home/config/key/auth read,
build, source edit, Git mutation, claim or activation occurred. Schema success
proves accepted keys/types/enums, not native startup, strict-config loading,
provider availability, final assembly equality, shared-state compatibility or
safe downgrade. System-level configuration layers may still apply at runtime.
Parent owns final outputs, review, watcher execution and runtime acceptance;
implementer1 owns any operations-guide changes and handoff for the lead's main
writing pass. No technical profile change is indicated by this check.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
