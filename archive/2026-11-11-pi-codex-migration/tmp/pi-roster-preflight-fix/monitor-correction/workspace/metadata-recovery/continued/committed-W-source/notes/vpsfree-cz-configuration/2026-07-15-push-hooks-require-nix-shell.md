# Push hooks require the configuration Nix shell

Initiative: `work/2026-07-13-security-advisory-automation`

The `vpsfree-cz-configuration` Git hooks load the repository bundle. A push
from the ambient shell can fail before contacting the remote with missing
Overcommit and RuboCop gems, especially after cleaning generated `.bundle/`
and `.bin/` directories.

Run pushes from the repository development shell:

```sh
nix develop --command bash -lc 'git push ...'
```

The same lease-protected push succeeded there. The failed ambient invocation
did not update the remote. Clean any regenerated `.bundle/` and `.bin/`
directories after the Nix-shell operation.
