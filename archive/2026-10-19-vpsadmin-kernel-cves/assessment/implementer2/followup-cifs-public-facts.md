# CVE-2026-64387 factual delta for the lead's English/Czech writing

Status: technical preparation only. The lead owns final public wording. The
operator's whole-period answer is pending; no exclusion has been applied.

The operator confirmed that VPSes at vpsFree.cz do not get CIFS mounts that
could be abused through this path. Source already prevents a VPS administrator
from creating such a mount independently: CIFS/smb3 lacks FS_USERNS_MOUNT and
the generic superblock gate requires initial-user-namespace authority. These
two facts close both tenant mount routes within the policy's confirmed scope.
The statement does not establish the policy's January start, host-only CIFS
absence, a missing CONFIG_CIFS option, or a corrected kernel source.

The lead is asking whether the policy covers the full reviewed period from
2026-01-01 through the frozen snapshot at 2026-10-19T21:48:39Z, including
operator-prepared/delegated mounts. If confirmed, the supported empty affected
role array can produce not-affected results for this tenant workload. If the
answer covers only current operation, it cannot support whole-history role
exclusion. Until the answer, role declarations, public fields and the existing
version-conservative evaluation remain unchanged.

The user permits explicitly stating the flawed LTS backports. Exact reviewed
source supports that the official 6.6.145 patch targets SMB311_posix_qfs_info,
and the 6.12.96 and 6.18.39 patches target send_set_info, whereas this defect is
in SMB2_query_directory. The primary official claims remain disputed provenance,
not safe-version rules. Keep fixed_in:null for these three branches. The
mainline 7.2 fix and 7.1.4 fix target the correct function and remain effective.
Only the 6.12 branch was additionally inspected through downstream 6.12.113;
do not claim a full later-branch audit or that no future fix can exist.

Public reachability should reflect the confirmed actual workload scope, rather
than leave operator-prepared mounts as an unexplained hypothetical on vpsFree.cz.
Keep generic shared-kernel consequences conditional on reaching the defect;
the absent tenant mount is a trigger exclusion, not memory-corruption mitigation
or a claim about historical exploitation. Do not imply that allocator hardening,
monitored faults or the ineffective stable patches repair it.

This delta is exclusively CVE-2026-64387. It supplies no authorization to revise
other CIFS dossiers or to modify publication, submission or remote state.
Technical evidence remains in the existing source-correction receipts. Final
normal validation/evaluation and digest regeneration follow accepted temporal
scope and the lead's editorial pass.
