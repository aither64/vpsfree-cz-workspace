# Preserve a consumer's nested platform pin explicitly

`nix flake update vpsadmin` can replace a consumer's retained nested vpsAdminOS
lock with the platform revision recorded by the newly selected vpsAdmin input.
During the IP release refinement, updating the API commit changed the KB
consumer's tested 6bdf458 platform to the API repository's older 8e44a51 revision,
along with its nixpkgs inputs. No platform change was intended.

Declare `vpsadmin.inputs.vpsadminos.url` with the retained exact vpsAdminOS
revision in the consumer flake, then update vpsadmin again. Inspect all changed
lock nodes, not just the direct input. A lock-only or command-line override does
not express the intent for the next update. The explicit override restored the
previous platform and nixpkgs; full `bin/check` passed.

Related initiative: `work/2026-09-09-ip-release-mechanism`.
