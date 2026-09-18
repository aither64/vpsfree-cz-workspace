# Architecture and repetition review

Reviewed vpsAdmin commits `791ab3aa89e2f613979da6090b89785c78245db5..6682da3bafc1212f30c395707319147a8c51fcc9`
(`22fa7adc3` and `6682da3ba`) for the architecture and repetition lane.

## Findings

### Important: the shared stable-state contract has no provider-level specification

`VpsAdmin::API::KernelEvidence::StableState` is a new shared policy boundary for
both live confirmation writes and historical repair
(`api/lib/vpsadmin/api/kernel_evidence/stable_state.rb:7-52`,
`api/lib/vpsadmin/api/operations/node/record_kernel_evidence.rb:294-340`, and
`api/lib/vpsadmin/api/operations/node/repair_kernel_history_bounds.rb:62-131`).
The reviewed tree has recorder and repair integration specs, but no spec owned
by `StableState`; the only file under
`api/spec/lib/vpsadmin/api/kernel_evidence/` remains
`configuration_writer_spec.rb`.

This makes the public contract of the new abstraction implicit in fixtures
spread across two consumers. A later change to boot fallback, completeness,
transition handling, or the effective-ID projection can satisfy the consumer
being edited while silently changing the other consumer's proof standard. In
this change that can either stop advancing `last_confirmed_at` or let the repair
operation tighten persisted history under a different rule from the recorder.

Add a focused `StableState` spec at the owning boundary. It should directly
cover known, missing, and mixed boot IDs with the `booted_at` fallback;
livepatch error and nil-state completeness; transitions; effective-ID
normalization; ignored volatile metadata; and mismatches in boot, reported
release, and effective IDs. Keep the existing recorder and repair specs as
representative consumer validation.

### Advisory: boot identity is still implemented in two places

The new helper says that `same_boot?` matches the recorder's rule, but
`RecordKernelEvidence#new_boot?` independently repeats the boot-ID/fallback
decision (`api/lib/vpsadmin/api/kernel_evidence/stable_state.rb:5-15` and
`api/lib/vpsadmin/api/operations/node/record_kernel_evidence.rb:72-81`, commit
`22fa7adc3`). The present known-identity behavior agrees, and the helper's
rejection of two unknown identities is intentionally stricter for positive
historical evidence. Even so, adding or changing an identity source now needs
coordinated edits. If only one side changes, the recorder can delimit boots one
way while confirmation and repair compare them another way.

Move the common identity comparison into one owner and let the recorder apply
its explicit policy for an `unknown` result. A three-state result (`same`,
`different`, `unknown`) would retain the intentional conservative difference
without duplicating precedence and fallback rules.

## Consumer and residual-risk notes

The helper is owned appropriately by the vpsAdmin API kernel-evidence layer.
Its actual consumers in the reviewed tree are the supervisor recorder and the
new repair operation/rake task. Existing HaveAPI resources and WebUI code
consume `observed_after`, `observed_before`, and revisions; they do not receive
`last_confirmed_at`. No node-report or vpsAdminOS interface changed. The later
configuration and KB pins are outside this review target as stated in the
packet.

Long integration testing had not run at this checkpoint. The historical repair
also remains intentionally dependent on retained immutable event snapshots, so
a safe no-op for intervals without such evidence is a residual operational
limitation rather than an architecture defect.
