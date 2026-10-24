# Final browser and declared-check supplement — PREPARED ONLY

No test, browser, Nix evaluation/realization, build, CI or live operation was
launched while preparing this packet. Only bound-session/source inspection,
file/executable metadata, syntax and hashes were checked. Existing composition,
notification and raw Firefox50 commands are preserved.

Exact source guards, all clean at preparation:

- A `6e32a9043ee6367d92bfaf8d3ebdf48036e275f9`.
- B `d617ef3968280e9955da85e2d7464a47030e7087`.
- C `48215f8c24f29358af338ac153d4ece88e1f4da2`.
- Configuration `9ab2909175b7248b5800237edd016b523d10d011`.

Parent launches under a fresh retained Luna/low utility after inspection:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-browser-final/run-supplement.sh
```

The one-time driver refuses to overwrite `run/`. A failed session/source guard
stops the batch before workloads. Otherwise five sequential independent stages
continue after a failed stage, retaining every exit/log/elapsed result without
retry. Each workload repeats exact source guards. There is no background runner,
mutation driver, activation, claim, secret reader or lifecycle action.

## Coverage

1. B `TestQuestionBrowser` runs its entire checked-in list of **13** scripts,
   together with `TestNewSessionSettingsBrowser`,
   `TestIndexRefreshPreservesSelection` and `TestArchiveFailurePage`.
   `manifest.json` records the exact 13 scripts. This supplements the prior
   one-subtest command; it does not create another standalone one-subtest receipt.
   The Go invocation uses the exact requested20-minute test timeout:

   ```sh
   nix develop --no-update-lock-file -c go -C portal test -mod=readonly \
     -overlay /tmp/portal-followup-browser-assets-overlay.json ./internal/web \
     -run '^(TestQuestionBrowser|TestNewSessionSettingsBrowser|TestIndexRefreshPreservesSelection|TestArchiveFailurePage)$' \
     -count=1 -timeout=20m -v
   ```

   `PORTAL_BROWSER_TEST=1`; absent provider sentinel
   `/tmp/portal-followup-absent-providers.json`; repo-matched Playwright1.59.1
   modules and browser set. Both actual executable prerequisites were present:
   Chromium1217 `chrome-linux64/chrome` and Firefox1511 `firefox/firefox` under
   `/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers`.
   Node comes from the repository dev shell. The pinned hllcf review assets
   overlay is generated only under `/tmp`, with no application source writes.
   Asset/module/browser absence fails rather than selecting another version.

2. A checked-in Node paging/history contract from A's own Nix environment:

   ```sh
   nix develop --no-update-lock-file -c node test/paging_browser_contract_test.cjs
   ```

   This is the declared Node fixture, not evidence of actual Firefox visibility.

3. C `checks.x86_64-linux.agent-instructions`.
4. C `checks.x86_64-linux.deployment-contract`.
5. C `checks.x86_64-linux.cluster-provider-composition`.

Each C stage instantiates the exact rev482 flake attribute, roots its derivation,
records the full derivation and expected output, realizes and roots that output,
then retains path-info and source/drv/output identity JSON. Runtime identities
are derived at execution, not guessed during preparation. There is no unrooted
`--no-link` acceptance. Roots stay under this packet's `run/roots/`; no automatic
removal is scheduled. Parent retains operation roots through acceptance.

Existing final notifications and raw ordinary Firefox50 stages remain separate
in the composition packet. This batch does not replace either or claim native
Codex/production performance. Actual browser assertions remain unchanged.

## Results and bounded expectations

Absolute operation directory:
`/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-browser-final/run/`.
It does not exist at preparation.

- `status`: RUNNING, then PASS or FAIL.
- `result.json`: aggregate exit outcome, wall duration and all stage receipts.
- `<stage>.result.json`: exact argv, UTC start, elapsed seconds, exit code/log path.
- `<stage>.log`: full combined stdout/stderr. B's verbose log must show all four
  named wrappers and all13 Question subtests; an entry/skip is not a pass.
- C additionally retains instantiate/realise logs and stdout, derivation JSON,
  expected output, path-info JSON, identity JSON and roots.

No retries, silent alternate inputs, assertion weakening or pass inference from
mere command startup. Parent diagnoses concrete failures from their full logs.
No external generic timeout wraps C or A; parent utility monitors uncertain time.

Parent already retains exact candidate package499s and A/B CI coverage receipts.
This supplement does not rerun creation/archive VMs or package batches.
The lead's accepted host-only VM exclusion (`host-module-idempotency` and
`session-recovery-boot`) remains separate: byte-identical host substrate and a
user-profile-only rollout. This is not a literal all-attributes validation claim.

All shell files pass `bash -n`; run.py is parsed without executing; manifest JSON
parses. `SHA256SUMS` binds the final preparation files. Browser dependencies are
being rooted by the parent's separate display/dependency utility; rechecked
filesystem presence here is not a GC-retention receipt or execution compatibility
proof. B source/Git remain frozen; no refs or existing packets were changed.
