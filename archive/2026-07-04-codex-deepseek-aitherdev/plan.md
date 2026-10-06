# 2026-07-04-codex-deepseek-aitherdev

## Goal

Add a Codex DeepSeek launcher/profile on `aitherdev` through
`vpsfree-cz-configuration`. The default `codex` command must keep using the
existing OpenAI/codex-lb setup; DeepSeek should be opt-in through `codex-ds` or
`codex -p ds`.

## Affected repositories

- `vpsfree-cz-configuration`

## Approach

- Add a NixOS systemd service `codex-deepseek-responses-proxy` on
  `cz.vpsfree/machines/aitherdev`.
- Package the proxy from `~/codex-deepseek-proxy-share.tar.gz` as a Nix store
  script, with support for `DEEPSEEK_API_KEY_FILE` so the API key remains in
  `/home/aither/.codex/deepseek-key`.
- Run the proxy as user `aither`, listen only on `127.0.0.1:4141`, and store
  non-secret call-continuity state under
  `/var/lib/codex-deepseek-responses-proxy`.
- Use Home Manager to install a `codex-ds` launcher that executes
  `codex -p ds`.
- Bootstrap `~/.codex/ds.config.toml` as a normal mutable user-owned file
  during system activation, replacing only a missing file or a stale
  Home Manager/Nix store symlink.
- Do not install the shared bundle's model catalog in v1. Codex 0.142.5 uses
  profile files directly, and the shared catalog vendors an older Codex prompt
  metadata snapshot.

## Compatibility and deployment

- No database, persistent service protocol, DNS, firewall, or public endpoint
  changes.
- Existing Codex configuration stays compatible because the base
  `~/.codex/config.toml` is not managed or replaced.
- Rollback removes the service/profile/launcher. State under
  `/var/lib/codex-deepseek-responses-proxy` is non-secret and can be left or
  removed manually.
- Mixed-version operation is not relevant beyond the deployed Codex CLI version
  on `aitherdev`. The pinned `llm-agents` Codex package is 0.142.5, which
  supports `~/.codex/<profile>.config.toml`.

## Testing plan

- Run Nix formatting checks for touched Nix files.
- Run repository hooks before commit.
- Build/evaluate `cz.vpsfree/machines/aitherdev` with `confctl build`.
- Run mandatory change review after commit and quick local verification.
- Optionally dry-activate `cz.vpsfree/machines/aitherdev` before deployment.
