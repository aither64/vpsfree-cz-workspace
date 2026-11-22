# GitHub organization runner API requires broader token scope

## Symptom

Read-only calls to `orgs/vpsfreecz/actions/runners` and
`orgs/vpsfreecz/actions/runner-groups` returned HTTP 403 with
`Resource not accessible by personal access token`.

## Cause and workaround

The active `gh` token can inspect repository workflow jobs, including their
assigned runner name, runner group, and requested labels, but it cannot list
organization-wide runner or runner-group configuration. Use individual job
metadata for routing verification, or use an organization token with the
required Actions administration scope when organization inventory is needed.

## Verification

For the `2026-08-09-test-vm-kernel-oops` initiative, repository job metadata
showed the Intel lifecycle job on `gh-runner2.int.vpsadminos.org` with
`intel-kvm`, the generic suite on `gh-runner1.int.vpsadminos.org` with
`self-hosted`, and the unassigned AMD job requesting only `amd-livepatch`.

