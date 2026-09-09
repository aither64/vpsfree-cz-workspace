# Preserve the KB runtime when updating the vpsAdmin input

`nix flake update vpsadmin` resets its nested inputs to the provider's embedded
lock. In the IP release initiative, both old and new vpsAdmin commits embedded
vpsAdminOS 8e44a512, while the KB lock and page/runtime contract intentionally
used 6bdf458f. Updating the API pin silently selected the older runtime and
`bin/check` rejected the page-contract revision mismatch.

Declare the existing exact runtime under
`inputs.vpsadmin.inputs.vpsadminos.url`, then update the vpsAdmin input again.
This makes the consumer's existing runtime choice durable and leaves its
nixpkgs/runtime action pins unchanged. Do not blindly change page/runtime
revisions to match an incidental nested dependency reset. Verify both providers'
embedded locks and run the full contract check.

Related initiative: work/2026-09-09-ip-release-mechanism.
