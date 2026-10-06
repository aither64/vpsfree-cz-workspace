## Summary

- require `vpsadmin-client ~> 4.2.1`
- release vpsfree-client 0.20.1

## Context

vpsadmin-client 4.2.1 consumes HaveAPI 0.29.6, which fixes traversal of API
resources when a resource name collides with an association name. The
collision previously caused `vpsfreectl snapshot download` to fail while
constructing snapshot resource instances.

Requiring 4.2.1 prevents new vpsfree-client installations from resolving to
vpsadmin-client 4.2.0, which still contains the affected HaveAPI client.

## Compatibility

The CLI and API contracts are unchanged. The dependency remains within the
vpsadmin-client 4.2 series, but raises its minimum compatible patch release.
No persistent state, schema, deployment ordering, or rollback concerns apply.

## Verification

- built `vpsfree-client-0.20.1.gem`
- installed the candidate against the public RubyGems dependency graph
- loaded vpsfree-client 0.20.1, vpsadmin-client 4.2.1, and
  haveapi-client 0.29.6 together
- verified the built gem requires `vpsadmin-client ~> 4.2.1`
- candidate SHA-256:
  `ef0dfadd1a5b7ba6183045fa8950a168d0913747f61ab9599c85642536026fcd`
