# Copy Nix template sources before overlaying them

Related initiative: `work/2026-08-31-vpsadmin-notifications/`.

The effective notification-template package initially tried to overlay custom
files onto a direct copy of Nix store inputs. Their read-only modes survived the
copy, so later layers could not replace bundled files.

Assemble layers in a build-directory copy and add owner write permission before
applying later sources. Validate the final tree after all layers are present.
For plugin collisions, copy a whole template only when the name does not exist;
file-by-file merging changes core-before-plugin precedence.
