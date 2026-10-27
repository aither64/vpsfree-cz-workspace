# Final recovery VM passed; unchanged host evidence reused

The changed recovery-boot check passed at exact clean runtime
`3e29a94da2276e69eb4b386ec71701d63a329c45`, tree
`c956efc2f4fd0f53ab29aae3b0062e9e01cc5008`. The original command exited **0**
after **994s**, with actual UTC start `2026-10-27T14:59:42Z` and end
`15:16:16Z`. Fresh retained Luna/low watcher `/root/recovery_vm_3e29` returned
FINAL after the original handle30518 settled. No running or uncertain command
remains; the utility slot is free. Owners1/2 and lead received actual settlement
directly, releasing their conditional source refresh and serialized builds.

Source is `/nix/store/2b0938h319lnxz7fv07jds7andsdv4b6-source`, NAR
`sha256-dfyy2cyG8v0OUnYhy/Ju2d9Ynr3Z8uEDaSKijBNd+80=`.
[Full flake/input identity](flake-metadata.json) binds client255 and unchanged
llm-agents/nixpkgs revisions. The complete lock graph matches retained352a.

Recovery derivation
`/nix/store/nc6q6idxflgwl0f82xrkcarn7p6ia7ga-vm-test-run-dev-workspace-session-recovery-boot.drv`
produced valid output
`/nix/store/ra83aa6rb81js4zly0w0hjwzaa5z2y0d-vm-test-run-dev-workspace-session-recovery-boot`.
[Actual output receipt](outputs.json) records the matching deriver and NAR hash.
The original VM script finished in318.21s and completed cleanup.

The original command includes an execution deviation, retained verbatim:

```sh
nix build --no-link --print-build-logs .#checks.x86_64-linux.session-recovery-boot .
```

The trailing `.` additionally selects the default runtime package. That package
is already a dependency of this VM through `devWorkspace`; no second VM was
selected. The deviation was reported to lead without rewriting the metadata or
repeating the successful check. No CI observation, native/vendor replay, source
change or live operation was part of this batch.

The complete host-module derivation JSON exactly equals its retained352a
counterpart:
`/nix/store/m9q5gqjfn8yqcvyw05l78hg775l64w8d-vm-test-run-dev-workspace-host-module-idempotency.drv`.
Lead accepted reuse of the [historical successful host result](../host-vm-352a/result.md)
and [successful output receipt](../host-vm-352a/outputs.json) with the exact
derivation and full input equality. Output
`/nix/store/apfrvraxc5szzskp68bigip5i0i3vypr-vm-test-run-dev-workspace-host-module-idempotency`
is **unavailable locally now**, with no inferred cause.
[Current lookup](retained-host-output.json) records null, not fresh validity.
The earlier premature validity wording was corrected directly to lead before
the VM result. No host VM was rebuilt to recreate disposable output.

Evidence: [both derivations](check-derivations.json), [full original stdout/stderr](build.log),
[original command/source/real timestamps](build.meta), [true exit](build.exit).
Earlier35d6 and mounted-browser failure records remain under their original
heads; this result does not relabel those attempts. The focused mounted-browser
test separately passed3e29 in Chromium and Firefox.

Later exact3e29 automatic CI40526204419 observation remains held until owner2's
final profile success, bounded assessment and actual command/watcher settlement.
Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-codex-upgrade-naming/
