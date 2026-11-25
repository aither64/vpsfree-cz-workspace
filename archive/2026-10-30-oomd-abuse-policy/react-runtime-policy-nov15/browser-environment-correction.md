# Browser launch environment correction

Original root operation `dc689e70-6e9d-4c0c-832a-4a4f92f207ef` failed before UI:
0 passed, 1 failed, 1 not run; native1/4.565s. The generic Linux cached headless
shell hit NixOS's stub loader and exited127. The initial presence-only full-Chrome
probe did not verify that actual default headless-shell executable. No product
defect or UI assertion result is inferred.

Original logs, native exit, JSON, context and trace are copied byte-for-byte in
[failed-browser-dc689e70](failed-browser-dc689e70/preservation.json), with 8 files/
43177bytes and SHA256 inventory. A first receipt write used an incorrect relative
CWD and created nothing; preservation was then completed at the correct absolute
tracking path. Repository system-Chromium discovery found no ambient executable.
The exact Nix browser root retained from earlier owner2 verification still exists.

[Corrected literal invocation and unchanged inputs](browser-environment-correction.json)
select it through ordinary PLAYWRIGHT_BROWSERS_PATH and the repository-supported
E2E_CHROMIUM_EXECUTABLE_PATH. The resolved executable and deriver are recorded;
no broad browser install, product build, SDK install, source/config/assertion edit
or policy relaxation was needed.

Minimal native launch/version/close passed0 in2.388s using pinned Playwright and
this exact executable: Chromium149.0.7827.55 connected, then closed/joined. It
created no page or UI flow; logs/argv/exit are in browser-nix-launch-control.*.
This proves native launch compatibility, not either usability flow. All owner2
native effects are terminal. Both original flows remain unexecuted. Root owns
its healthy registered preview and the fresh finite flow watcher; no competing
service/CI reads or mutation occurred. Source8ce, static NAR and all three fixture
hashes are unchanged. Preserve retries0/maxfailures1 and diagnose first actual
failure before any affected retry.
