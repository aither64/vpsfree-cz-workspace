# Invoke the skill validator with PyYAML

## Symptom

Executing
`/home/aither/.codex/skills/.system/skill-creator/scripts/quick_validate.py`
directly fails with `Permission denied`.

Invoking it with ambient `python3` then fails with
`ModuleNotFoundError: No module named 'yaml'`. Adding
`nixpkgs#python3Packages.pyyaml` as a separate `nix shell` package does not add
the module to the ambient interpreter's import path.

## Cause

The validator script is readable but does not have its executable bit set in
the installed system skill. It also imports PyYAML, which is absent from the
ambient Python environment.

## Workaround

Construct a Python environment containing PyYAML and invoke the script with
that interpreter:

```sh
nix shell --impure \
  --expr '(builtins.getFlake "nixpkgs").legacyPackages.${builtins.currentSystem}.python3.withPackages (ps: [ ps.pyyaml ])' \
  -c python3 /home/aither/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  PATH_TO_SKILL
```

## Verification

The command validated `skills/mandatory-change-review` successfully.

## Related initiative

`work/2026-07-17-mandatory-review-updates/`
