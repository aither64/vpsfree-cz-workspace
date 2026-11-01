# C4 controlled desktop expiry comparison: both pass

Lead released this one paired comparison after the architect's C4 addendum in
`design.md`. Both executions passed the unchanged sole desktop fixture. The
earlier 3/6 and 5/6 browser failures remain preserved and are not relabeled.
Publication remains held pending lead disposition. No source or Git ref changed.

| Input/result | f10 predecessor | 0.31 successor |
| --- | --- | --- |
| Exact source | `f10d3d48c4f21cc39187c3667ffffd9952404c11` | `baf00acc31d34ab37720643c5833b4476a341f3b` |
| Tree | `e1084bb80dd07140719034ab908a6f62daff855b` | `2e7b4cb5eba6bc96f34f834c49fc097d5fdd987b` |
| Installed HaveAPI | 0.30.2 | 0.31.0 |
| Isolated npm ci | exit 0, 12.479s | exit 0, 12.577s |
| Chromium result | 1 passed, exit 0 | 1 passed, exit 0 |
| Test duration | 11.392s | 11.967s |
| Playwright duration / command wall | 15.281s / 21.440s | 15.733s / 17.948s |
| UTC start | 2026-10-27 20:30:49.577 | 2026-10-27 20:31:35.815 |

Each complete source was exported by `git archive` into its own initially empty
directory. Archive hashes and original lock/integrity identities are in
[source-identities.json](source-identities.json). All 2371/2372 original source
files were compared with the corresponding Git archive before setup and after
execution. Both archives retained their original fixtures and lockfiles; neither
borrowed live node_modules or private configuration. Ordinary isolated `npm ci
--no-audit --no-fund` used the exact baf Git flake's unchanged locked development
shell: Node 24.21.0/npm 11.19.0. Both had no Vite cache before their respective
run. Actual installed dependency graphs differ only in HaveAPI version/resolved
tarball, as recorded in [installed-graph-delta.json](installed-graph-delta.json).

Both runs used the same registered Package C 0.30.2 `fhs-gc-root`, targeting
`/nix/store/yrvkph1ivq0gf80p5b4rvjf9lfz4iakw-package-c-playwright-fhs`,
all 185 closure paths with identical NARs/references, PW 1.61.0, Chromium headless
shell 1228 (Chrome for Testing 149.0.7827.55) and ffmpeg 1011. Browser hashes are
in [runtime-before.json](runtime-before.json). The comparison used CPU 60–63,
nice 5, Nix one job/two cores, the same declared exclusions, loopback 52847,
fresh Playwright-owned Vite, normal legacy development mode, and a fresh browser
context for each side. A0 retained the sole watcher slot; the released visible
parent-monitor fallback owned and reconciled each command handle.

The exact test selection on each side was:

```text
node scripts/playwright.mjs test e2e/specs/app/session_expiry_redirect.spec.ts \
  --project=chromium --workers=2 --retries=0 --reporter=list,json \
  --output=<side-specific artifacts>
```

Native `--list` proved exactly one case before either run. Full launch arguments
and environment exclusions are in [f10-browser-command.json](f10-browser-command.json)
and [baf-browser-command.json](baf-browser-command.json). Test/expect timeouts,
assertions, fixture responses, policy and browser family/version were unchanged.
There was no prewarm, preview workaround, legacy production build or further run.

Both completed the original sequence: expired authenticated fixture, navigation
to `/app/vps`, root URL after expiry query cleanup, visible public overview, and
visible fresh-session notice. The fixture's current-user response remains 401.
Success is established by the unchanged assertions, not just by observing a
redirect. Passing traces/screenshots/videos are absent under the unchanged
retain-on-failure policy; no new per-request timing or exact cause is claimed.

[f10 log](f10-browser.log), [f10 JSON](f10-results.json),
[baf log](baf-browser.log), [baf JSON](baf-results.json) retain separate results.
[f10 afterchecks](f10-afterchecks.json) passed before the second launch;
[complete afterchecks](paired-afterchecks.json) prove original source/locks,
clean protected worktrees at exact f10/baf, unchanged runtime/binary identities,
registered persistent root, no owned server/browser process, no listener on
52847, and a successful reusable bind. No process signals or host changes were
needed. Roots and all earlier failed artifacts remain retained.

These paired passes show the unchanged expiry fixture completes at both exact
sources under the controlled current runtime. They do not establish the cause
of the earlier failures or prove those failures preexisting. The latest six-case
batch remains 5/6, with this separate one-case successor pass; no synthetic 6/6
batch or full-browser pass is claimed. The older f10 60/62 mobile expansion
residual remains separate. Mocked fixtures do not certify real OAuth/TLS/BFF
login. Lead owns disposition/publication release and later cluster actions.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
