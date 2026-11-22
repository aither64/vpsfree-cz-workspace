# Go tests in a Nix shell with vendor mode

## Symptom

Running a focused `go test` in the workspace portal's Nix development shell
failed because the shell supplied `GOFLAGS=-mod=vendor`, but the checkout has
no vendor tree.

## Workaround

For an ad hoc focused package test, override only that invocation with
`env GOFLAGS=-mod=mod go test ./path/to/package`. Keep the repository's normal
Nix package build as the full validation because it owns the production module
inputs and runs the complete packaged suite.

## Verification

The focused package passed with the override, and `nix build
.#workspace-portal --no-link -L` subsequently passed the full Go, Ruby, PKI,
password, wrapper, schema, and JavaScript checks.

Related initiative: `work/2026-09-03-dev-session-portal`.
