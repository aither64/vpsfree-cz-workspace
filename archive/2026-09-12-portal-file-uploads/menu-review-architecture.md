# Architecture and repetition review

Reviewed the committed follow-up ranges from `menu-review-packet.md`:

- codex-web `7b79942eee2d7bcaf52252249d8599db76c033b2..aa26ec23712e7bdcefd5545ca7715d9bff00f8b7`
- dev-workspace `30bfb2a378138a7fdfe8f6aaa05fcbf8d98037b3..4ddf911fc73e2c8d3c96e1b713cea404dacc7296`
- vpsfree-dev-workspace `9db07ad92eeb62490dbb14cdb5b9cd9a47b4412c..905f7a52b766d219d90940885d6cccb3de5a0360`
- workspace `a3b8e6b4945dfedcee48c6a732e933df4dc48f45..19dc77784383ae0063ed240a2210347cb74c3f46`
- vpsfree-cz-configuration `63652724f9ed0202d6f9c842d842da89ab33bbaa..3d3fa67dd306e1261237cb7df331b664b8b0e8e1`

## Findings

No Blocking, Important, or Advisory architecture/repetition findings.

The component boundary is coherent. `codex-web` remains the owner of menu
creation, visibility, placement, keyboard/focus behavior, lock handling, and
listener/control cleanup in `conversation/assets/uploads.js:165-361`. The
optional `controlsRoot` is an explicit, documented mount point; the component
adds and removes its own wrapper, so it does not claim or remove neighboring
host actions. The legacy single-root behavior remains within the same owner.

Actual browser consumers were derived from imports and call sites. The shared
`mountConversation` path delegates to `mountUploads` at
`conversation/assets/conversation.js:621-631`. The portal is the only external
browser consumer found and supplies the new mount point for both creation and
existing-session composers at `portal/internal/web/static/app.js:979-984` and
`:2561-2566`; its templates only declare the corresponding host slots. There
is no second menu implementation or repeated placement, focus, limits, upload,
or cleanup policy downstream. The small duplication between the two portal
mount calls is form-specific glue with different storage scopes and callbacks,
so extracting it would obscure rather than consolidate a rule that must stay
identical.

The dependency chain is aligned at the reviewed heads: dev-workspace pins
codex-web `aa26ec2` in its flake source and Go module; vpsfree-dev-workspace pins
dev-workspace `4ddf911`; workspace pins vpsfree-dev-workspace `905f7a5`; and the
configuration pin selects dev-workspace `4ddf911`. The downstream repositories
contain packaging changes only and introduce no parallel UI abstraction.

## Residual risks and test gaps

The provider DOM-double contract at
`test/uploads_browser_contract_test.cjs:60-118` covers split-root ownership,
lock/close behavior, legacy fallback, initialization errors, and cleanup, but it
does not exercise the browser's native Popover API, top-layer placement, light
dismissal, or real focus transitions. Nor do committed portal unit tests bind
both template slots to their browser call sites. The packet's planned Firefox
acceptance for both forms at desktop and narrow widths is therefore still
needed before deployment; this is a validation gap, not an architecture
finding.
