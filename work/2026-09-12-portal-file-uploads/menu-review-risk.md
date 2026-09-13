# Risk and compatibility review: compact attachment menu

Lane: risk and compatibility. Risk: high. Reviewer: `gpt-5.6-sol`, `xhigh`.

Reviewed commits:

- codex-web `7b79942eee2d7bcaf52252249d8599db76c033b2..aa26ec23712e7bdcefd5545ca7715d9bff00f8b7`
- dev-workspace `30bfb2a378138a7fdfe8f6aaa05fcbf8d98037b3..4ddf911fc73e2c8d3c96e1b713cea404dacc7296`
- vpsfree-dev-workspace `9db07ad92eeb62490dbb14cdb5b9cd9a47b4412c..905f7a52b766d219d90940885d6cccb3de5a0360`
- workspace `a3b8e6b4945dfedcee48c6a732e933df4dc48f45..19dc77784383ae0063ed240a2210347cb74c3f46`
- vpsfree-cz-configuration `63652724f9ed0202d6f9c842d842da89ab33bbaa..3d3fa67dd306e1261237cb7df331b664b8b0e8e1`

## Important

### A warm browser can lose both attachment controls during forward deployment

The new templates render `#creation-uploads` and `#message-uploads` with the
`hidden` attribute (`portal/internal/web/templates/index.html:50` and
`portal/internal/web/templates/session.html:81`). The new application passes a
separate `controlsRoot` (`portal/internal/web/static/app.js:979-984` and
`:2561-2566`), but the baseline `uploads.js` ignores that option and appends its
Attach files control to the upload root. Consequently, a browser that receives
the new HTML/application while reusing the baseline provider module places the
only attachment control inside a permanently hidden element. This affects both
new-session and existing-session forms; selected draft cards and errors are
hidden as well.

That mixed asset combination is part of the normal deployment topology. Provider
assets are explicitly cached for five minutes (`codex-web` commit `aa26ec2`,
`conversation/handler.go:226-236`), while the application still imports
`/codex/assets/conversation.js?v=5` (`app.js:631`) and that module still imports
the unversioned `./uploads.js` (`conversation/assets/conversation.js:1-2`). The
follow-up changes both modules without changing either cache key. This is more
severe than the packet's accepted possibility of briefly displaying the old UI:
the advertised attachment action disappears until the cached module expires or
the user forces a refresh.

Resolve this before deployment or record an explicit acceptance. A compatible
approach is to leave the roots initially visible and let the new `mountUploads`
hide an empty split root, as it already does synchronously; the cached baseline
then continues to show its old control and limits sentence. Alternatively, use
new cache identities for the complete changed dependency chain, including the
nested `uploads.js` import and stylesheet, and verify forward deployment and
rollback with warmed caches. Add a mixed-version browser or DOM contract for the
baseline module with the new templates so this boundary remains deliberate.

## Other findings and residual gaps

No other Blocking, Important, or Advisory findings.

The upload HTTP API, authorization checks, quotas, prompt IDs, persisted state,
deletion behavior and Codex protocol are unchanged. The inspected pin chain
selects `aa26ec2` in runtime `4ddf911`, then that runtime consistently in the
organization, workspace and host-configuration consumers. Either package
generation can read the same upload state, so deployment and rollback do not
require migration or coordinated node updates.

The planned Firefox acceptance covers the current-head DOM and native Popover
behavior, but it starts with a fresh browser profile and therefore does not cover
the warm-cache transition above. It also leaves behavior in other browser engines
unverified; the shared component now requires the Popover API, and the repository
does not state a broader browser-version support contract.
