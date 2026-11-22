# Build review UI assets before the full editor test file

Running `node --test editor.test.mjs` in a fresh `portal/review-ui` copy passed
8 tests but failed the bundle contract with `ENOENT: dist/review-build.json`.
That test consumes generated esbuild metadata and assets.

Install the locked npm dependencies, run `npm run build`, then `npm test`, using
Node/npm from Nix. With build prerequisites present, all 9 tests passed. For a
projection-only investigation, a focused test name filter can avoid the bundle
contract, but the full test file requires a build.

Related initiative: `work/2026-09-15-portal-diff-highlighting/`.
