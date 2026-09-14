# Python libraries in an ad hoc Nix shell

`nix shell nixpkgs#python3Packages.pyyaml -c python3 …` did not make `yaml`
importable: adding a library package to PATH does not compose it into the
selected Python interpreter's module path.

Use a composed interpreter instead:

```sh
nix-shell -p 'python3.withPackages (ps: [ ps.pyyaml ])' --run 'python3 script.py'
```

Verified by parsing the email-login KB replacement plan and proving a blank-line
indentation cleanup preserved its parsed values. Related initiative:
`work/2026-09-13-auth-email/`.
