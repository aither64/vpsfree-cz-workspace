# Overcommit pre-push must use the declared Nix environment

During the published-advisory-corrections session, an amended C commit passed
normal commit hooks in the repository Nix shell. A subsequent ambient `git push`
stopped with “Signature of configuration file has changed”. The tracked
`.overcommit.yml` and custom hooks were unchanged.

The ambient Ruby loaded Overcommit0.71.0, while the declared root Nix environment
loaded0.74.0. Running the same push in that declared environment passed normally:

```sh
env VPSADMIN_PLUGINS=all nix develop -c git push ...
```

Keep the repository environment around pre-push as well as commit hooks. When a
signature warning appears, inspect the configuration and compare the loaded tool
versions. In this case no signing, hook bypass, recommit or source change was
needed. The original failed log and the successful remote acknowledgement remain
in the session's verification receipt.

Related session: [published advisory corrections](../../work/2026-11-01-published-advisory-corrections/visibility-verification.md).
