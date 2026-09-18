# 2026-09-18-aitherdev-codex-deepseek

## Goal

Restore the `codex-ds` wrapper on `aitherdev` by replacing the obsolete
localhost DeepSeek proxy with DeepSeek's native Responses API integration.

## Affected repositories

- `vpsfree-cz-configuration` only
- Target: `cz.vpsfree/machines/aitherdev`

## Approach

- Remove the custom proxy package and systemd service.
- Configure Codex profile `ds` for `deepseek-v4-pro` and native Responses API.
- Have `codex-ds` read `/home/aither/.codex/deepseek-key` and export
  `DEEPSEEK_API_KEY` for Codex's `env_key` provider authentication.
- Install the official DeepSeek model catalog under `/etc/codex/`.
- Replace the old `ds.config.toml` directly during activation; do not preserve
  or back up the proxy profile or proxy state.
- Add concise aitherdev operator documentation.

## Decisions

- Preserve the current default model and high reasoning effort.
- Use `env_key`, keeping the API key out of Git, Nix derivations, TOML, and
  process arguments.
- Follow DeepSeek's current Codex catalog rather than maintaining a reduced
  hand-written model definition.
- Direct deployment to aitherdev is in scope; merging into `master` is not.

## Compatibility and deployment

- This is a host-local configuration change with no public API or database
  migration.
- The new profile bypasses the removed localhost service and calls
  `https://api.deepseek.com/` directly over HTTPS.
- Build and dry-activate first, then deploy the feature branch to
  `cz.vpsfree/machines/aitherdev`.
- A single minimal live Codex request is sufficient for acceptance; avoid
  repeated requests because usage quota is limited.

## Documentation

- Add `docs/operations/codex-deepseek-aitherdev.md` and link it from the
  repository documentation navigation.

## Testing plan

- Check Nix formatting and model-catalog JSON syntax.
- Build the qualified aitherdev machine with `confctl`.
- Run `dry-activate`, then deploy with `switch`.
- Verify the proxy service/listener is absent and run one minimal
  `codex-ds exec --ephemeral` request.
- Run the required fast concurrent change review before long verification;
  review agents remain `gpt-6-astra`/`xhigh` under workspace policy, while
  long-running build/deploy monitoring uses the fresh Luna/low watcher.
