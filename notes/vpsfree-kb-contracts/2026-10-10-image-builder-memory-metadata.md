# Inspect effective VM builder memory in structured derivations

Related initiative: `work/2026-10-05-network-ipv4-left-counter`.

A hosted projection test for a reduced KB runtime failed twice while inspecting
`nix derivation show` from Nix 2.34.8. Format 4 wraps records in `derivations`,
with the requested derivation basename as its key. After fixing that lookup,
`env.memSize` still failed: the pinned nixpkgs VM builder uses
`__structuredAttrs = true`, and effective memory is encoded in
`structuredAttrs.env.QEMU_OPTS`.

Read the selected record through the pinned tool's explicit format. Parse its
QEMU arguments with Shellwords and check both `-m` and the memfd memory object
and machine binding. Avoid a fallback to an unrelated record or a source-text
constant. Keep failure output to key names and extracted memory fields: the
whole structured record can contain build scripts and seed configuration.

Runtime machine RAM and image-finalization RAM have different owners. The OSVM
machine consumes the cluster machine's memory; the image builder consumes
`nixos.config.virtualisation.memorySize`. Align both through the owning services
module when reducing the profile.

At K `1f84c999172056cbf5f8b537abbc123f18a99e82`, both exact hosted source checks
passed the projection with two 2048 MiB runtime machines and an effective
2048 MiB image builder (verifier 29 tests / 320 assertions). This is declaration
proof, not payload fit, guest boot or a measured minimum. The two failed native
batches are retained separately in the session evidence.
