# Final affected rootless-stop review

## Findings and disposition

No Blocking, Important or Advisory findings in the completed rootless-stop
correction at `35b64f5a09e5fa0e0822c7507fe6605a759b788a`. Accept this affected
source-content review under the assigned general and risk/compatibility lanes.
The two nil/empty guards follow trusted-session validation and preserve the
ordinary closure path. Known-root loss still refuses before recovery or kill.

This clears the affected source review gate; it does not establish corrected
native archive completion, a successful creation check, final package/composition
acceptance or deployed usability. Publication, native verification, deployment,
integration and lifecycle actions retain their separate authorization and checks.

## Identity, settings and reviewed scope

Retained independent `reviewer0`, purpose `review`, thread
`01a19ca7-8da1-7e63-852f-72d8332c553a`, saved
`gpt-6.1-sol` / `xhigh` / `read_only`. Fresh live roster revision 27 confirms
ready state, identity and settings. No override, fallback, substantive authorship
or nested agents. `dev-session current` returned the exact bound slug
`2026-11-02-session-temporary-service-cleanup` before record access; both environment
markers matched that slug and `/home/aither/workspace/ai/vpsfree.cz`, consistent
with the trusted developer binding.

Read mandatory-change-review in full and the general/risk references, applicable
workspace procedures, immutable runtime AGENTS, current plan/state, released
packet/receipt/diff and architect's rootless-stop brief. Reuse unaffected previous
service, capacity, machine, deletion, cancellation and diagnostic conclusions;
this is the requested narrow affected review. Risk remains High because stop
changes native recovery admission around terminal retirement and persistent
restoration authority.

Repository/target: `git@github.com:aither64/dev-workspace.git`, `master`.
Affected exact range:
`9acfcf4d3138a94b40f11f9670fb14a549e29740..35b64f5a09e5fa0e0822c7507fe6605a759b788a`.
Head tree: `c682b0ab59b043e223ce87d86497a4ebd077777c`.
Whole branch range:
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79..35b64f5a09e5fa0e0822c7507fe6605a759b788a`.
Only `libexec/dev-session` and `test/dev_session/tmux_runtime_test.rb` change from
9ac: 127 insertions/4 deletions, including production 3 insertions/2 deletions.
The complete branch is 93 files, 7753 insertions/410 deletions. Separate mutable
creation fixture work is excluded; review binds the immutable submitted source.

## General correctness and scope

The observed 9ac archive failure reaches an explicitly confirmed stop of a
session started with `--no-codex`, then passes `--thread-id ''` to cancel-retries.
The native tmux parser preserves empty fields (`libexec/dev-session:704-718`),
whereas the common ManagedTmux default is nil. Ruby's former truthiness guards
therefore admitted an empty string. The Go recovery bridge correctly rejects it
before constructing its native client (`portal/cmd/workspace-portal/recovery.go:26`).
The saved native log and the controlled red regression support this exact cause.

`libexec/dev-session:1807-1818` now retains the validated session's thread ID and
admits each existing recovery call only when it is neither nil nor empty. Every
nonempty ID is preserved exactly; no stripping, coercion, inferred root, rescue
or validator relaxation is added. Order remains cancel-retries, close_session!,
then stop. A failure still propagates at its original boundary.

This is the smallest conventional correction for the evidenced baseline bug.
It adds no classifier, collector, native probe, registry, service discovery or
new policy. Existing unregistered services remain excluded. Stop itself does not
stop or unregister previews; later authorized archive cleanup owns that work.
The existing documented exact-terminal/files-preserved stop contract remains
accurate (`docs/dev-sessions.md:641`). An additional application prose update is
unnecessary for restoring that contract; the design and causal receipt retain
the incident-specific rationale.

## Ownership, closure and compatibility

The guards execute inside the existing creation/slug locks, after selection of
retained authority, conflicting-journal refusal and ensure_managed_session!.
`select_tmux_for_slug!` loads and validates authority; an incomplete or empty
retained Codex tuple is rejected (`libexec/dev-session:3209,3278-3305`).
`validate_authority_session!` compares an existing recorded Codex tuple with the
live exact root/socket/version (`:8752-8788`). A live nil/empty root cannot bypass
that comparison when authority names a conversation. The new guards do not
establish ownership or classify a missing known conversation as a shell.

For a genuine shell, authority deliberately omits that tuple (`:3322-3329`).
Only the two native recovery calls are skipped. close_session! still validates
tracking/location, retirement identity, idle/team conditions, creation token,
conditional tmux kill, post-kill absence and authority retirement (`:9279-9308`,
`:9649`). Missing required authority and replacement-session mismatches retain
their refusals. Native quiescence already applies the same nil/empty predicate
(`:9464`). No closure, native validator or package-capability path is bypassed.
The trusted local operator boundary remains intact; ordinary identity mistakes,
concurrency and interruption remain relevant.

The affected change introduces no state, schema, CLI/API, recovery-format,
service-format, package-capability or dependency change. Existing conversation
recovery cancellation and stop semantics remain intact for every nonempty root.
No new mixed-version or rollback conversion is needed for this correction.

## Regressions and evidence limits

Read the actual added tests and their existing ManagedTmux implementation.
`tmux_runtime_test.rb:94` checks nil and empty shell roots independently, fake
closure only, authority retirement, preserved tracking bytes and absent socket.
`:115` checks the exact nonempty identity and cancel-retries / require-idle /
close / stop order. `:131` seeds valid conversation authority, removes the live
root as nil or empty, and verifies refusal before any portal call or kill with
unchanged authority/tracking bytes.

The helper at `:533` uses disposable workspace/state/XDG/SHELL, existing fake tmux,
an absolute local Ruby portal and an absent temporary socket. The portal stub
validates exact argv, workspace, cwd, state root, socket and call order; it never
delegates to an installed helper or connects natively. The two selected existing
active-root runner environments change only to disposable XDG state. Existing
active-turn, replacement/kill-boundary, legacy-authority, confirmation and archived
tracking controls remain in the aggregate selection.

Matched retained logs to the receipt hashes. Causal red is three cases/42
assertions with one error: only the empty-string case reaches the controlled
rootless recovery tripwire. Green is the full eleven stop cases/105 assertions,
zero failures/errors/skips, in 2.051526 seconds, plus two Ruby syntax checks.
The receipt binds those quick checks to the final tree; immutable source bytes
and the committed final diff were independently compared. I ran no tests.

The 9ac native archive log confirms the original empty-ID failure and earlier
held-turn progress; it is a failed archive check, not a full native pass. The
corrected rootless stop and subsequent automatic registered-service cleanup
still need the existing native acceptance. Older fast/package success belongs
to 9ac and cannot certify this final package. Creation's separate held-response
ordering investigation/correction is outside this review; neither its native
proofs nor any future fixture source are accepted here.

## Whole history, migration and input conclusion

Independently inventoried all six commits and the complete base-to-head diff:

1. `19dd03b79a2997098934afafbe70c63b978c1ca7` — Resources/Team UI.
2. `f7add7cea8a836810d32688ef2d1cf4cc011af19` — registered-service owner/lifecycle.
3. `5b4b711748343f4ffe88b96c50d88a9f98eeb04d` — dependent portal/package integration.
4. `08f51074618efc0c72c2ae1e4b85c4390998c72b` — capacity proof and retained fixture diagnostics.
5. `9acfcf4d3138a94b40f11f9670fb14a549e29740` — machine claims/prior corrections.
6. `35b64f5a09e5fa0e0822c7507fe6605a759b788a` — this baseline rootless-stop fix.

The first five are exact unchanged ancestors. Independently compared the entire
old stop method: c218 and 9ac are byte-identical (SHA256
`e78f999bec333a0571727c982b85bc0cc20a3dfdca37afea3a18f948c9717e0a`).
Blame locates the original recovery guards in aafaf4195 and 97ea4c56f, before the
feature base. The separate sixth is therefore a coherent independently reviewable
baseline correction, not an unrelated fixup of new machine behavior. Its tests
support that single behavior. Commit message describes the result and rationale.

No obsolete fixup, abandoned approach or transitional implementation remains in
this final six-commit history. Prior superseded refs/source roots/reports and CI
failures remain retained separately; the exact reviewed 9ac parent also remains
at `retained/rootless-stop-reviewed-9ac`. Earlier accepted consolidation and direct
remediation conclusions are unchanged.

**No database migrations.** The sixth adds no migration. Previously reviewed
supported retry/claim schema-1 predecessors and direct schema-2 introductions,
local service schema 1, saved lifecycle journals and receipt contracts keep their
accepted provenance and forward-reader/recovery boundaries. There is no new
intermediate schema or conversion for an abandoned branch iteration. Migration
lineage remains sound under those retained conclusions.

**No repeated dependency/generated input stream exists in the runtime series.**
The runtime lock is unchanged from c218; no sixth-commit generated pin is added.
Extension f8da/workspace48b and the stored downstream selections are unchanged.
Their single final runtime selection stream still requires the actual final
pin consolidation, source/NAR and complete graph proof after runtime acceptance.
No hypothetical future pin or default-branch readiness is certified.

## Immutable source and review boundaries

Independently recomputed NAR hash for
`/nix/store/1hwld3skcaz9f922l9nlwcc19wcw4kvp-source`:
`sha256-zm9mnrSKCG2q2vX71/879gZWIhwuUmgzeyQj68IOn+I=`.
All 679 Git entries match source bytes, symlink targets and executable modes,
with zero missing/extra entries. Metadata names exact 35b64f5a. Its full nine-node
lock graph, actual follows and recursive child input paths/edges equal the prior
9ac evidence. Lock SHA256:
`fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955`.
The ordinary `rootless-stop-review-source` link resolves to that exact source and
was left intact. Saved final diff equals the committed two-path delta, SHA256
`49ccde35ac0e40c4bc772dbb8fde36621d90570a491c9e2a55eb56145e5ce1cd`.

The historical first ambient confirmation fixture invocation still has unknown
exact branch/effects because its argv/stderr were discarded. Later isolated
controls and this unrelated correction do not certify that incident. No live
investigation or cleanup was performed. Remaining native/package/composition,
Playwright where still required, deployment and usability gaps remain with the
lead's existing check/disposition process.

No reviewer tests, builds, VM/CI/GH requests, native/live probes, lifecycle or
cleanup actions, source/Git/store mutations or nested agents were performed.
Only read-only source/history/hash/log inspection and this permitted report write.
All prior reports and review roots remain unchanged. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
