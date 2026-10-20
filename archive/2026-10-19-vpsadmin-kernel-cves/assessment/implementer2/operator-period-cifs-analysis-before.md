# CVE-2026-64387 — CIFS SMB2 QUERY_DIRECTORY replay double-free

Assessment date:2026-10-19. Exact approved60 batch; factual bilingual candidates
await lead editorial review. No exploit was executed, no production conclusion
is inferred from source defaults, and no draft has been synchronized by this owner.

## Primary defect, score and correction

In the Linux kernel, the following vulnerability has been resolved:

smb: client: fix query directory replay double-free

A response-bearing attempt can return a replayable error and free its
response buffer. If SMB2_query_directory_init() fails before the next send,
cleanup retains the previous buffer type and frees that response again.

Reset response bookkeeping before each attempt to prevent the stale free.

Correction reviewed in full: Reset the response-buffer pointer and ownership type before each replay attempt.

- [Pinned Linux CNA record](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-64387.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) (PUBLISHED at snapshot56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9)
- [Mainline introduction](https://git.kernel.org/stable/c/4f1fffa2376922f3d1d506e49c0fd445b023a28e), first affected 6.8.0
- [Mainline correction](https://git.kernel.org/stable/c/9647492b5e41954be59d5157eddbcd4cdc1656f7), first fixed 7.2.0
- [6.12 stable correction](https://git.kernel.org/stable/c/1665f25b1dea30bf2d02e16245d203a944c9d994), official claimed official first-fix claim 6.12.96 (ineffective, see exception); ineffective backport, see exception

Formal metrics are Linux CNA CVSS source ratings, not a custom container score.
Their exploit-consequence discussion is attributed primary analysis, not proof
that the vpsAdminOS hardening/build was exploited:

```json
[
  {
    "cvssV3_1": {
      "version": "3.1",
      "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
      "baseScore": 9.8,
      "baseSeverity": "CRITICAL"
    },
    "scenarios": [
      {
        "lang": "en",
        "value": "AV:N - A malicious remote SMB server can trigger the flaw through crafted responses to SMB2 QUERY_DIRECTORY requests over the established network connection.\nAC:L - On a hard/retrans-enabled mount, the server controls the replayable error and can repeatedly induce disconnect/reconnect conditions before request reinitialization, without relying on an uncontrollable race.\nPR:N - The attacker needs no account or privilege on the client; the client authenticates to the attacker-controlled SMB server, and ordinary accessible-share enumeration reaches the code.\nUI:N - In a reasonable auto-mounted deployment, routine directory enumeration can be performed automatically by a daemon or application without human participation.\nS:U - The corruption occurs within the client kernel and compromises resources governed by that same kernel security authority.\nC:H - Double-freeing the attacker-influenced CIFS response object can poison the slab freelist or create overlapping allocations, providing UAF-style primitives capable of exposing arbitrary kernel memory.\nI:H - Allocator corruption and aliased CIFS buffers can enable attacker-influenced writes and potentially control-flow hijacking or kernel code execution.\nA:H - The double-free can immediately trigger allocator diagnostics, an oops, or a kernel panic, and corrupted freelists can cause subsequent fatal faults."
      }
    ]
  }
]
```

## Complete branch rules and backport lineage

| Branch | First affected | First fixed | Introduction commit | Correction commit |
| --- | --- | --- | --- | --- |
| 6.6 | 6.6.32 | No effective fix verified | 433042a91f9373241307725b52de573933ffedbf | 3409aedf3c81a810243da94164f6621c9d205c98 |
| 6.12 | 6.12.0 | No same-branch fix listed; open-ended | 4f1fffa2376922f3d1d506e49c0fd445b023a28e | — |
| 6.18 | 6.18.0 | No effective fix verified | 4f1fffa2376922f3d1d506e49c0fd445b023a28e | 00b0fa425941438b664950a8ee65dfba2def4336 |
| 7.1 | 7.1.0 | 7.1.4 | 4f1fffa2376922f3d1d506e49c0fd445b023a28e | 3317a5d015fca976475aa71df224056777316fde |

Global/CNA affected intervals were checked before adding older EOL branches.
A later branch inherits the mainline introduction unless CNA supplies a distinct
stable-backport interval/commit. Open-ended entries preserve affected EOL lines
without inventing a same-branch fix. The mainline global bounds also classify
unlisted releases; a stable backport before the mainline introduction is explicit.
CNA Git-fix references and first-unaffected versions are retained, and exact
Makefile branch checks are recorded in the session version-source manifest.

## Platform prerequisites, exact source and roles

CIFS and smb3 filesystem types lack FS_USERNS_MOUNT in both exact archived .95 and current pinned .113. fs/super denies a non-initial-userns superblock for these filesystems. CIFS module preload and namespace CAP_SYS_ADMIN therefore do not let an ordinary tenant mount an attacker-selected share. A host-prepared/delegated mount or actual host CIFS client workload is required. The source-described replay sequence needs a response-bearing replayable error and failure before the next response replaces buffer ownership; SMB1 additionally needs legacy dialect negotiation. No storage CIFS-client workload is established by backup/NFS-server source, so scope is node only, conditional on such a mount. This optional workload is not a claim that default VPS operation reaches CIFS. The evaluator cannot represent actual mount delegation; an affected-release result is conservative applicability, not measured exploitation.

- [Current pinned Linux `fs/smb/client/smb2pdu.c`](https://github.com/vpsfreecz/linux/blob/1dfea587406b7dd79973831d1677fb2418e5e9aa/fs/smb/client/smb2pdu.c)
- [Current pinned Linux `fs/smb/client/cifsfs.c`](https://github.com/vpsfreecz/linux/blob/1dfea587406b7dd79973831d1677fb2418e5e9aa/fs/smb/client/cifsfs.c)
- [Current pinned Linux `fs/super.c`](https://github.com/vpsfreecz/linux/blob/1dfea587406b7dd79973831d1677fb2418e5e9aa/fs/super.c)
- [vpsAdmin feature defaults](https://github.com/vpsfreecz/vpsadmin/blob/fb2f51222503a45f2e5a42af505f719e44279ed0/api/models/vps_feature.rb)
- [vpsAdmin device delegation](https://github.com/vpsfreecz/vpsadmin/blob/fb2f51222503a45f2e5a42af505f719e44279ed0/libnodectld/lib/nodectld/commands/vps/features.rb)
- [OS module loading policy](https://github.com/vpsfreecz/vpsadminos/blob/87fc13aac3fc8ce3d6c71c7ef3a8e72a5993a088/os/modules/config/kernel.nix)
- [OS LXC base config](https://github.com/vpsfreecz/vpsadminos/blob/87fc13aac3fc8ce3d6c71c7ef3a8e72a5993a088/osctld/configs/lxc/common.conf)
- [Storage workload source](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/a2ad6da408715de811cc6d8ea7b29ac55ea341ec/cluster/cz.vpsfree/nodes/common/storage.nix)
- [Kernel selection and operational overrides](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/a2ad6da408715de811cc6d8ea7b29ac55ea341ec/configs/node/kernels.nix)

Required interface declarations are {"CONFIG_CIFS": "enabled"}.
No host sysctl value is a sufficient generic predicate for this namespace/workload
path, so required_sysctls is empty. Loaded modules, actual mounts/protocol and
LSM state must be checked against the shared typed snapshot where relevant;
source preload and absent AppArmor in the archived build are not universal
runtime claims. Historical archived config is bound to Linuxa2384967b90f24d2470c9eb15f0e66d938df7e08 with digest
c10922b492fdf39ed3027b9c8f7ce2846a5d3799d57d417a161595fa81a64969.

## Separate impact and protections


The impact is conditional on the prerequisite namespace, mount or protocol
setup described above; no initial VPS-root gain is inferred solely from a score. The concrete shared-kernel corruption makes host kernel compromise
and cross-VPS access possible consequences, while reviewed primary reports and
patches do not establish a complete working exploit on this platform. Kernel
oops/panic is a plausible host availability outcome. This is source-scoped
negative evidence only; it says nothing about production exploitation.

Allocator freelist hardening/randomization, zeroing and stack protection in the
archived build may raise exploit difficulty or detect a failed corruption; they
do not repair object lifetime or bounds. Monitored kernel warnings are detection
and availability evidence, not trigger prevention. The corrective code above
remediates this defect; correct activation/history must be independently bound.

## Runtime, history and mitigation evidence

The assessment requests retained history from2026-01-01T00:00:00Z, a reviewed
operational scope rather than a claim about earlier years. No historical attestation or older dossier override was copied. The
independently reviewed Node126 lifecycle scope is recorded below. No accepted
custom build, livepatch or BPF tuple is asserted for this CVE; ordinary stable
source boundaries determine the result. Empty arrays imply no extra mitigation.

Evaluate against the one coordinated ignored snapshot; do not recollect per CVE.
Missing current relevant evidence remains unknown. Missing historical config on
affected releases is conservative affected, not retrospective safety. Stable
fixed/pre-introduction releases can classify without configuration. Actual
boot/release transitions and reviewed cumulative-patch tuples determine mitigation
timing; an old livepatch cannot cross a reboot by inference. Unmodeled mount,
peer and workload predicates remain explicit and do not become ignored YAML keys
or manually edited evaluation results. Drafts may retain honest unknowns and do
not imply publication readiness. No API/schema/deployment compatibility change.

## Effective-stable-fix exception

The CNA names1665f25b1dea30bf2d02e16245d203a944c9d994 /6.12.96. Full stable
patch hunk actually resets response state in send_set_info(), while the
SMB2_query_directory() replay loop still lacks reset in pinned6.12.113
1dfea587406b7dd79973831d1677fb2418e5e9aa. It frees resp_buftype/rsp and can
return to replay_again without clearing them. Thus6.12.fixed_in is explicitly
null, no effective fix verified through.113; the official claim is disputed
provenance rather than a safe-version rule. The mainline9647492b5e41954be59d5157eddbcd4cdc1656f7
patch was independently read from kernel.googlesource.com and correctly targets
SMB2_query_directory. Exact source, diff, URL and SHA-256 are retained in the
owned64387-source-correction.json and fixes directory. No empty patch is evidence.
Architect/lead accepted this bounded source correction. Other stable branch
fixes require their own hunk checks; no global inference from this one drift.

Other-branch verification completed: the6.6.145 correction (exact full SHA in primary/branch receipt) changes SMB311_posix_qfs_info,
not QUERY_DIRECTORY. The6.18.39 correction00b0fa425941438b664950a8ee65dfba2def4336
also changes send_set_info. Those branches therefore have fixed_in:null.
The7.1.4 patch correctly changes SMB2_query_directory and retains its safe bound.
The mainline patch correctly changes that function and retains global7.2.
The review does not assert that no later correction can exist; it records the
verified bounded source and rejects these three ineffective claimed fixes.

## Frozen snapshot evaluation checkpoint

Evaluated with the repository's existing CLI against schema8 snapshot collected
2026-10-19T21:48:39Z, byte SHA-256
61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274.
All13 active Nodes are included in the tracked schema4 evaluation. The storage
role is excluded by the tenant-only workload assessment, independently of its
missing current receipt/observation metadata. One applicable Node's retained
history and reconstruction start after the January review baseline; its initial
unknown is resolved by the independently reviewed lifecycle source below.
No override or historical attestation has been copied from an older dossier.

The other11 applicable Nodes receive vulnerable version classifications because
6.12.113 retains the described QUERY_DIRECTORY defect. These are conservative
conditional classifications: actual host-prepared/delegated CIFS mounts are
not established by the typed snapshot or generic evaluator. The public text
retains that prerequisite and does not claim a measured exploited mount.

## Reviewed production-entry history scope

Configuration commit [`e27882a9bc8f6900903e6ae84841b9935190548c`](https://github.com/vpsfreecz/vpsfree-cz-configuration/commit/e27882a9bc8f6900903e6ae84841b9935190548c)
first adds Node126 as a production hypervisor, including its module and cluster
registration. The reviewed parent has neither that node nor its module. The
frozen reconstruction begins with its same-day initial boot observation.
Together these facts support the Node126-only history start
`2026-03-31T20:11:46Z`. This is a retained baseline, not an exact deployment
timestamp. The global January review scope and ordinary affected-interval rules
remain unchanged. No storage-node override or historical attestation is added.

## Final frozen-snapshot evaluation

The regenerated result covers all 13 active nodes: 12 applicable nodes remain
vulnerable under the source-corrected open 6.12 interval; the storage role is
not affected by this tenant workload. No unknown remains after the independently
sourced Node126 lifecycle scope. The version-based vulnerable result is
conservative: an operator-prepared or delegated actual CIFS mount remains an
unmodeled prerequisite. It does not establish an observed exploitable mount,
VPS-root exploit, node takeover or cross-VPS access. No safe 6.12.96 boundary
is asserted.
The schema 4 evaluation is generated by the existing CLI using the unchanged
frozen snapshot and this final dossier digest. It is an assessment record,
not a deployment or publication action.
