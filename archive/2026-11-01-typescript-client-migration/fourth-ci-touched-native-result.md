# Fourth CI touched native browser result

- Result: failed; observer exit code 1.
- Tested WebUI HEAD: `b1b37ccf5dc5d000baed3d77d49fab6f5b84b663`.
- Exact launch: `PATH=/nix/store/b1wn5clix1mz4vpfih7x9cnj9qfh7c6h-git-2.54.0/bin:/nix/store/frlyjd2wya3rk8xmdc98yq3x0rhpkh9n-nodejs-24.21.0/bin:/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15/bin:$PATH WEBUI_EXPECTED_HEAD=b1b37ccf5dc5d000baed3d77d49fab6f5b84b663 /nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15/bin/python3.13 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/fourth-ci-touched-observed.py`
- Selection: frozen 136 selected IDs (68 Cr + 68 mC); selection preflight SHA-256 `b8a12c6e65b9c72e79b24dd3e53349d7bd9f1be0dc97a96ef82763dbceb264cc`.
- Native observer identity: PID/PGID/SID `1011773`, start ticks `25518296`; started `2026-11-02T20:59:46.749456+00:00`; finished `2026-11-02T21:00:21.840147+00:00`; elapsed `35.091s`.
- Browser summary: 6 passed, 1 failed, 1 interrupted, 128 did not run; stopped after the configured maximum of one failure.
- First failure: `e2e/specs/app/vps_power_stop_confirm.spec.ts:85:3`, “starts a stopped VPS and tracks the returned action state”; assertion at line 97 expected `request.postDataJSON()` to equal `{}`. Trace: `browser-fourth-ci-touched/results/app-vps_power_stop_confirm-7f907-s-the-returned-action-state-chromium/trace.zip`.
- Interrupted case: `e2e/specs/app/vps_lifecycle_tab_actions.spec.ts:215:3`, “resets configuration review and lifetime editor when the VPS route changes”; trace: `browser-fourth-ci-touched/results/app-vps_lifecycle_tab_acti-67ce8--when-the-VPS-route-changes-chromium/trace.zip`.
- Durable observer log: `fourth-ci-touched-observed.log`; state: `fourth-ci-touched-observed-state.json`; exit record: `fourth-ci-touched-observed-exit.json`.
- No retry, diagnosis, cancellation, or cleanup performed. Parent owns remaining process/listener effects proof.
