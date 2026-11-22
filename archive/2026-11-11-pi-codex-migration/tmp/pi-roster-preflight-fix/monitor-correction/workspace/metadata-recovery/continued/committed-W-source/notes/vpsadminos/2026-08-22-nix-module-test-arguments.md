# Injecting test-only arguments into Nix modules

## Symptom

An `evalModules` test failed before running examples with:

```text
error: attribute 'ebpfLivepatchPrograms' missing
```

The production module function declared the argument with `? null`, but the
module evaluator still attempted to resolve it through `_module.args`.

## Cause

NixOS module evaluation resolves named module-function arguments itself. An
ordinary Nix default on a named argument is not a reliable test-injection seam
when the evaluator does not provide that argument.

## Workaround

Keep the test-only value out of the module's named arguments. In the test,
wrap the module path in a function and call the module directly with the normal
module arguments plus the test-only value. The module can capture its complete
argument set with `args@{ ... }` and read the extra value with `or null`.

## Verification

`./test-runner.sh test ebpf-livepatch` passed all 37 examples after switching
to the wrapper import.

Related initiative:
`work/2026-08-22-multiple-kernel-scopes/`
