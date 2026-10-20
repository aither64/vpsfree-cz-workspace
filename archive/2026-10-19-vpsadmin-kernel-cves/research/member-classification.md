# Broader member-relevance selection (policy version 2)

Final research proposal, 2026-10-19: **60 CVEs**, comprising the preserved **41** earlier
recommendations and **19** additions. The additions are five exact-build negative
assessments, three privileged-program cases and the eleven earlier conditional
cases. [member-selection.json](member-selection.json) is the machine-readable
set. The bounded 26-row evidence package has been reconciled: **19 proposed
additions, five review-only cases and two deferred controls**. No additional
enumeration or source-gate investigation remains in this research package.

The user requested high-threat assessments even when vpsAdminOS was not
vulnerable. Selection now answers whether an assessment would be useful to
members; exposure separately answers what the evidence establishes about a
specific build, profile, role and time. These are research recommendations,
not advisory drafts. User approval is still required before dossier or draft
preparation. [The original proposal](selection.json) remains unchanged.

## Proposed additions

- **Exact archived-build exclusions:** CVE-2026-80585, CVE-2026-80586 and
  CVE-2026-80587 require MPTCP, disabled in the exact archived 6.12.95 build.
  CVE-2026-53260 and CVE-2026-72069 require PREEMPT_RT, also absent from that
  build. This establishes no universal fleet or historical claim. MPTCP impact
  concerns connection-state/data integrity, possible disclosure and disruption;
  do not relabel it a proven host escape from the Critical rating.
- **Privileged programs:** CVE-2026-63830 (SK_MSG shared file-page writes),
  CVE-2026-74616 (XDP clone metadata corruption) and CVE-2026-98039 (percpu-kptr
  arbitrary kernel read/write or invalid free). Preserve the initial-userns,
  token-authority or preexisting host-program prerequisite. Enabling unprivileged
  BPF does not prove access to these program/map/kfunc paths.
- **Earlier conditional cases:** CVE-2026-89783, CVE-2026-74746,
  CVE-2026-74597 and CVE-2026-98222 remain conditional on host module/type
  availability. CVE-2026-64383, CVE-2026-64384, CVE-2026-64385,
  CVE-2026-64386, CVE-2026-64387, CVE-2026-64597 and CVE-2026-89633 require
  host-prepared/delegated CIFS mounts. CVE-2026-89633 additionally requires
  SMB1. CVE-2026-64597 is first fixed in **6.12.96**, correcting an early .97
  report. Promotion changes relevance only; it supplies no new exposure proof.

## Evidence and controls

Build exclusions bind to the archived .95 configuration and provenance in
[package A](platform-baseline.md), not to every newer release or running Node.
Formal scores retain their Linux CNA provenance. The exact stable fixes remain
inside the inclusive .95–.113 interval; a correction in .95 does not imply that
.95 itself is vulnerable. Current mitigation and historical exposure are not
assessed here. Private remote drafts remain unavailable to anonymous dedup.

CVE-2026-53341 is a review-only negative control: pinned default seccomp blocks
open_by_handle_at, but the primary fix explicitly limits the described effects
to a comparison-result leak, loop or crash. Its 7.8 score and UAF label alone do
not support a high-threat privilege-gain addition. The remaining review-only and deferred decisions are below. Original
borderline/deferred reasons remain in [classification.md](classification.md).

## Final bounded decisions outside the proposed 60

These are explicit research dispositions, not conclusions that the platform was
safe. Missing a demonstrated complete exploit is not alone an exclusion rule;
the unresolved point is the specific effect or relevant prerequisite below.

| CVE | Decision | Reason and exposure limit |
| --- | --- | --- |
| CVE-2026-53341 | Review-only; not selected as high-threat | The primary description expressly limits impact to an integer-comparison leak, loop or crash. The pinned common seccomp profile blocks the only described syscall, but that exclusion covers that profile only. No fleet-wide or host-caller conclusion. |
| CVE-2026-64355 | Review-only | Fragmented XDP clone retains invalid fragment metadata; reviewed description establishes out-of-bounds frame-return access. Its stronger corruption consequence remains less qualified than 74616. It is a distinct defect, not deduplicated by subsystem similarity. Host-program/authority conditions remain unknown. |
| CVE-2026-53092 | Review-only | Linked-register verifier/runtime mismatch is real; the permitted program path and resulting unsafe access need further qualification before a serious platform-impact assessment. No assumption that tenant BPF reaches privileged program types. |
| CVE-2026-93045 | Review-only | Below-base arena frees produce invalid allocator offsets and later allocation below the mapping. The resulting out-of-range effect and relevant arena authority need qualification; ordinary socket-filter BPF enablement is insufficient. |
| CVE-2026-74607 | Review-only | AMD SEV owner/mirror lifetime corruption is serious. The exact SEV hardware/firmware and context/device access are unestablished. Compiled support proves neither hardware absence nor availability to tenant VMMs. |
| CVE-2026-98041 | Deferred | Speculative alternate-path verification still matters unless bypass_spec_v1 applies. A working permitted ordinary-tenant unsafe path was not established by the reviewed sources; neither universal exposure nor non-exposure is justified. |
| CVE-2026-63823 | Deferred | The request-key helper/authentication context needed by this lifetime flaw has not been established as accessible to the scoped tenant. Keyctl availability alone is insufficient; no proof of absence is claimed. |

## Final acceptance and handoff

The accepted additions exactly match the 19 proposed rows in
[the bounded evidence package](member-relevance.md), with per-row source gates,
primary introductions/fixes, formal scores, revision reasons and required next
evidence in [its structured proposal](member-relevance-evidence/proposal.json).
All 14 reused source-manifest inputs match their recorded hashes. All 60 proposed
IDs are unique, PUBLISHED at the frozen primary snapshot, in the stable interval,
and absent from the public 57-CVE prior-report set. Stable fix SHA/release pairs
and CVSS values/vectors match the primary records. The prior selection file
remains byte-for-byte unchanged at SHA-256
`09c51860a0a250c2fd0ad3c08799fba3674474da4a47bf7768c99935a2ac00b2`.

Coverage remains **3,493** mechanically joined CVEs, **3,445** new to public
reports, **317** focused-screened new records and **3,128** mechanical-only
unresolved records. Reconsidering the 26 records adds no newly audited CVEs to
those counts. Public evidence cannot exclude private remote drafts; that check
remains a prerequisite to approved draft creation. Current and historical
per-node exposure and actual mitigation activation remain unassessed.

The final proposal contains the same 60 IDs as the provisional proposal. The
lead owns the approval document and user handoff. Any approved later assessment
must bind its conclusions to typed Node evidence and preserve conservative
historical evaluation. No dossier, draft, publication or notification has been
authorized by this research result.
