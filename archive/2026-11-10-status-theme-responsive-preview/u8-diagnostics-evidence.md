# U8: bounded first-failure diagnostics

Owner implementer0, retained Sol/xhigh/workspace_write; capacity accepted after
U7. Exact session/environment and live roster verified. Bounded direct lead
brief; source base `b589972c57a22fb806a643a1de9a683beca3a363`. Final separate
commit `d6d972ade865849cee7324060f611aec649ad31e`, parent b589972. Exclusive
index/commit window released; worktree/index clean.

## Source

Two files, 64 additions: `tests/suite/status-page.nix` (58) and `tests/README.md`
(6). One shared first-failure collector, called by rescue-and-reraise in the
seven existing example bodies. No assertions, timeout values, example order,
setup, cleanup, machines, networking, resources, app code or inputs changed.
Mechanically removing only the diagnostic additions exactly restores the old
suite bytes, confirming preservation of the original test program.

Six native `machine.execute` calls each have an eight-second deadline (48-second
command budget): status journal; API GET, WebUI HEAD and console HEAD; failed
services/API+WebUI-container journal; container nginx/PHP-FPM journal. HTTP
connect/max timeouts are two/four seconds, output only code/remote IP/timing and
curl errors. Three journal tails are 60 lines at 300 characters per line;
failed-unit lists are 20 lines. No response body, config or credential dump.
Capture errors log only exception class, do not replace the original failure,
and do not stop remaining commands or test cleanup. Capture occurs once.

Verified unit/command provenance at pinned vpsAdmin3f9: API module declares
`vpsadmin-api.service`; cluster config declares `containers.webui`; WebUI module
declares PHP-FPM pool `vpsadmin-webui`. Existing upstream failure extension uses
the same `nixos-container run webui` / `nginx.service` /
`phpfpm-vpsadmin-webui.service` commands. Status module owns vpsf-status.service.
All collection uses the existing test `status` and `services` machine objects.

## Checks

- `nix-instantiate --parse tests/suite/status-page.nix`: passed.
- Extracted actual generated script through selected650 test framework's
  `makeTests`/`test.config.testScripts.default.script` with local/remote builds
  and substitution disabled; `ruby -c u8-status-page.rb`: Syntax OK.
- `u8-error-preservation.rb` loads actual selected runner `TestRunner::Example`
  and generated helpers/original first example. Focused proof passed: original
  RSpec failure object preserved, first diagnostic command error tolerated,
  remaining capture continues, repeat failure does not duplicate collection,
  exactly six command deadlines of eight seconds. No VM or new framework.
- Ordinary no-build test metadata evaluation: status-page, three VMs, 14 CPUs,
  17,920 MiB memory/shared memory, one script unchanged (`u8-metadata.json`).
- Diff checks passed. Lead directly approved the actual README wording unchanged.
- Required Nix/Lefthook 2.1.5 i18n hook passed 0.37s (0.39s total); gofmt skipped
  without Go files. Required temporary message file; no bypass.
- All 99 compiled/logical source inputs match after hooks; receipt
  `u8-source-inputs.json`, digest
  `292d4bb87a02d32890d1e9558cadd88e430995601d0982d60d2156186ad84db8`,
  bound to final head above. No unexpected hook effects.

## Original failure and next dependency

The old run used exactly b589972, not U8. Lead/watcher reported baseline JSON
and metrics failures at 240.61s / 120.19s, then authorized interruption of the
remaining dependent run. Later interruption/BrokenPipe cleanup is not a separate
product finding or root cause. Original watcher owned PGID2720984/session58463
and confirmed joined/VM teardown; U8 never attached, signalled or reused guests.
Old store-frozen source, logs and input receipt remain distinct evidence.

Pinned650 runner has no individual-example selector. `-f` means `--fresh`;
`--stop-on-failure` stops scheduling test scripts, not example execution. Its
RSpec-like after hook receives no result, so U8 does not invent an RSpec
`example.exception` API. Rescue/reraise is the accepted smallest local insertion.

No disposable six-example-omission suite snapshot was constructed. Architect C10
and lead instead own an independent session-only services-machine diagnostic
through the existing realized `test-json-runner`, reusing old reviewed b589 JSON.
That investigation is neither a U8 full suite nor evidence of runtime success.
Root cause/product fix remain pending actual HTTP/journal evidence. Independent
committed review precedes any future U8 full suite. No input refresh or assertion
relaxation is justified by the current failure.

Separate test-diagnostics commit retained initially; possible later consolidation
with CI visibility remains lead-owned before final branch readiness. No migration,
schema/data conversion or deployed state boundary. No rebase, push, master
integration, services or lifecycle changes by U8.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-status-theme-responsive-preview/)
