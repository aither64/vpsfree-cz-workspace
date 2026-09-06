# Literal dollar signs in `writeShellApplication`

## Symptom

A NixOS build failed while building a `pkgs.writeShellApplication` helper even
though its shell syntax was valid. ShellCheck reported SC2016 for a single-
quoted regular expression that intentionally matched literal dollar signs in a
bcrypt record.

## Cause and fix

`writeShellApplication` runs ShellCheck and treats informational findings as
build failures. Keep the expression single-quoted and add a narrowly scoped
`# shellcheck disable=SC2016` immediately before that command. Changing to
double quotes would make the shell expand the literal dollar signs.

## Verification

Rebuild `cz.vpsfree/machines/aitherdev` with `confctl build`.

Related initiative:
`work/2026-09-06-portal-config-deployment-policy/`.
