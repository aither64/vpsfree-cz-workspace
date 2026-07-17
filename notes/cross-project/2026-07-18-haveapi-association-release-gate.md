# HaveAPI output association release gate

Initiative: `work/2026-07-13-security-advisory-automation`

Symptom: a least-privilege security-advisories collector can read
`node_cgroup_state#index`, but the live response contains
`node: {_meta: {resolved: false, authorized: false}}`. The collector then fails
with `vpsAdmin returned node without a typed resource ID`.

Cause: vpsAdmin packages HaveAPI 0.29.3. Its ActiveRecord output-association
authorization retains the parent resource path, so token scope filtering does
not apply the related resource's `node#show` scope. The reviewed HaveAPI branch
commits `f9064b6` and `3bd0f94` preserve the related resource path for input and
output association authorization.

Avoid: do not grant the parent's Show action merely to compensate for the
framework context, and do not add scalar relationship IDs. Both hide the
authorization bug and expand or duplicate the API contract.

Resolution: release the HaveAPI fixes, update vpsAdmin's packaged gem, verify a
token carrying `node_cgroup_state#index` plus `node#show` receives a typed Node
ID, then rerun the scoped collector. A package release is an external action
and needs explicit approval.

Verification: on the clean bridge cluster at vpsAdmin `b1551d3da`, the same
token resolved `node_kernel_evidence.node` with ID 101 but did not resolve
`node_cgroup_state.node`. The token was revoked after the failed read-only
collection.
