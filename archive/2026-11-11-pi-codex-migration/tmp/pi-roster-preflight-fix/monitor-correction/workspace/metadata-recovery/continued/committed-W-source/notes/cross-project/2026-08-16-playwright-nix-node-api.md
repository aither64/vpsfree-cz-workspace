# Playwright Node API needs the Nix browser path

Related initiative: `work/2026-08-14-kb-updates`

## Symptom

Running a standalone Node script with `require('playwright')` from the
`playwright-test` Nix package failed because Playwright searched
`~/.cache/ms-playwright` and could not find Chromium.

## Cause

The Nix package's `bin/playwright` wrapper exports
`PLAYWRIGHT_BROWSERS_PATH`, but a script launched directly with `node` does not
inherit that wrapper variable. `NODE_PATH` is also needed when the script lives
outside the package output.

## Workaround

Build `nixpkgs#playwright-test`, use its `lib/node_modules` directory as
`NODE_PATH`, and read the packaged browser directory exported by its
`bin/playwright` wrapper into `PLAYWRIGHT_BROWSERS_PATH` before invoking Node.
Do not download another browser with `npx playwright install`.

## Verification

With both variables set, the production KB browser check launched the packaged
Chromium and verified 29 rendered pages, 14 reciprocal language pairs, images,
lists, managed-source actions, and localized examples.
