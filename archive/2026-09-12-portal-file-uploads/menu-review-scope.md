# Scope and proportionality review

## Findings

No Blocking, Important, or Advisory findings.

## Assessment

Reviewed the final consolidated follow-up from the documented deployed bases:

- codex-web `7b79942eee2d7bcaf52252249d8599db76c033b2` to
  `4a4c77b4acc2bbaef44e2327c37d9c984e091867`
- dev-workspace `30bfb2a378138a7fdfe8f6aaa05fcbf8d98037b3` to
  `14871f50bb6f57542d3452de32924357ff629037`
- vpsfree-dev-workspace `9db07ad92eeb62490dbb14cdb5b9cd9a47b4412c`
  to `6063618bcf1fc3eefe57187a22ccc3b1bf0b22b6`
- workspace `a3b8e6b4945dfedcee48c6a732e933df4dc48f45` to
  `58bc7ea3734dca2763d3033c42f4de7d0fa6457d`
- vpsfree-cz-configuration
  `63652724f9ed0202d6f9c842d842da89ab33bbaa` to
  `c79a68ea6ef80dcaaef95cf17950fa87afbe976d`

The implementation is a proportionate fit for the accepted outcome. The
provider adds one optional `controlsRoot` placement point to its existing
upload component, while retaining the single-root default. The menu, focus,
viewport placement, lock handling, and cleanup stay in that component; the two
portal forms only supply action-row slots. Downstream repositories contain the
required dependency pins rather than additional browser implementations.

The direct review fixes remain within the same boundary. Restoring the root's
initial `hidden` value completes the existing destroy ownership contract. The
three cache-key changes and two host `:empty` selectors address the documented
five-minute mixed-cache deployment window using existing version-query
conventions; they do not introduce a compatibility framework. Removing stale
Go sums and consolidating pins are mechanical follow-through. The resulting
commit split keeps provider behavior, runtime integration, and downstream pins
separate and reviewable.

The focused provider contract test and the curated browser acceptance script
cover owned behavior without repeating transfer, quota, persistence, or Codex
lifecycle suites from the unchanged baseline. Omitting the 1 GiB transfer and
real Codex lifecycle reruns is consistent with the browser-only delta and its
explicit non-goals.

## Residual risks and test gaps

- The Node DOM double does not exercise native Popover API activation, top-layer
  layout, outside dismissal, or real focus behavior. The planned desktop and
  narrow Firefox acceptance, including warmed old/new asset combinations, is
  the appropriate remaining check.
- The planned browser check covers Firefox only. No broader browser support
  matrix was identified in the repository or initiative contract.
