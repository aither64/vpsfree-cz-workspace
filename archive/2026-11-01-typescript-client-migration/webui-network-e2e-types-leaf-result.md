# Strict network E2E adoption passes

Result: passed, exit0. Tested HEADf79cad52a5a36384f7da7dd71ee96c6430db2999
with held whole-file adoption metadata. Coverage103 checked/179 deferred;
TypeScript has no diagnostics. Exact command nix develop --command npm run
typecheck:e2e:core, known short affected repeat. Full output:
webui-network-e2e-types-leaf.log. Leaf IpReference with required id is identical
to the existing adapter type and avoids importing application configuration;
wire payloads and assertions remain unchanged. W now owns the exact2JSON commit.
