# Package tests must expose runtime tools

## Symptom

The workspace portal passed tests in its development shell, but the clean Nix
package build failed three development-cluster certificate tests with
`missing required command: openssl`.

## Cause

OpenSSL was available in the interactive environment but absent from both the
package's check inputs and the installed development-cluster wrapper path.

## Fix

Add every externally invoked command to both `nativeCheckInputs` and the
relevant installed wrapper path. The clean package build is the check that
proves these two environments are complete.

Related initiative: `2026-09-06-portal-config-deployment-policy`.
