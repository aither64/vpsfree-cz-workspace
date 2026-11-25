# Package B: bda1 diagnostic AMD runtime audit

The main AMD row supplies the required FUSE/TCP runtime witnesses, and its
selected fragment case supplies the native/current timer-state comparison.
This acceptance is limited to run **41921632759**, attempt **1**, job
**126907163480**, committed source
`bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf`. Local job metadata records success
from **2026-11-04 22:48:22Z to 23:26:29Z (38m07s)**. It is not acceptance of
the complete diagnostic matrix, a successor/final head, or four-hour/aged
qualification. The main row has its own ten-case selection.

Session/env and retained implementer1 Sol/xhigh/workspace-write identity were
verified. Only supplied local artifacts and immutable Git objects were read.
No API, polling, download, test, VM, build, evaluation, compilation, application
edit, Git mutation or owned background process was used. The sole CI watcher
was left unchanged. Prior [C main](package-c-main-runtime-acceptance.md) and
[C Intel](package-c-e175-intel-runtime-acceptance.md) receipts supplied contract
boundaries, not values reused as current observations.

## Evidence and identity

Artifact **13372996844**, `os-test-logs-41921632759-1-livepatch-amd.zip`,
independently measures **220745 bytes**, SHA256
`2ad73ef1130aa6950dd1239d291d9adab50bba52f44fecac157156110c5a2e22`.
All **68** member names are unique safe relative paths without traversal,
backslashes or symlinks. Total uncompressed size is 2555322 bytes. Selected
identity, summary, launch/console and numbered shell/source excerpts are in
[the bounded evidence directory](package-b-diagnostic-300s-amd-evidence/audit-receipt.json);
[files.json](package-b-diagnostic-300s-amd-evidence/files.json) records their
sizes/digests. Full all-case extraction and the full 1046347-byte main shell
log were avoided. Excerpt labels retain **original file line numbers**.

Build-job log `job-126895318703.log:319–324`, main-job log
`job-126907163480.log:225–238`, and extracted `livepatch-identity.txt` agree:

| Captured input | Identity |
| --- | --- |
| Source | `bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf` |
| `flake.lock` SHA256 | `604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa` |
| Normal producer | `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95` |
| Module | producer + `/lib/modules/6.12.95/extra/livepatch_7.ko` |
| Module SHA256 | `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f` |
| Sites output | `/nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites` |
| Extracted sites SHA256 | `093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1` |

The immutable bda1 lock bytes independently hash to the captured lock digest.
Main-job lines 152–169 guard source/lock, normal producer, resolved module
path/digest and sites' module digest. This is the ordinary current producer;
the transferred fixture path is the separate
`/nix/store/lm2k2sxi01wyimay11amp7dfpxwmqa4f-livepatch_7-current-candidate.ko`.
The ZIP does not contain module bytes: guest checks and the retained B measured
module/ELF receipts establish that byte scope; no new module parse was run.

Here **main shell/runner** name original files under
`os-test-kernel__livepatch-6.12.95-9f465251/`; **fragment shell/runner** use
`os-test-kernel__livepatch-inet-frag-144ad4d5/`.
Main shell **45–84** returns status 0 for release `.95`, module/sites hashes,
released-v5 SHA `b31f64403d9d55f62e3d59e4bbefcbddcbda4fa66a2dc0689f9bb7cd7e927984`
and v6 SHA `960b13f1b461b95e29cccff58ddf0d3f3badf151046eb46eba36a9c8c7e5efe3`.
Fragment shell **54–66** independently checks the same module/sites bytes.
The sites record is schema 1, ELF64/EM_X86_64, build ID
`fd8cbfe4c314ddac8f35d87bee4bb8b909e479d5`, exactly nine witnesses and ABI
node/timer/lock/connect-worker offsets **0/56/96/1600**. It matches retained B
actual-artifact output byte-for-byte. Source excerpts come from bda1 objects;
the main/fragment consumers, probe helper and resolver/Nix blobs also match
`645927`, as recorded in the evidence receipt. Current local HEAD was not an
audit input.

The actual replacement lookup is exact-module, U/u-filtered and four-field:

```awk
$2 !~ /^[Uu]$/ && $3 == "tcp_write_xmit" && NF == 4 && $4 == "[livepatch_7]" { print "0x" $1 }
```

Main shell **15046–15051** returns exactly `0xffffffffc1a6f4c0`; the analogous
FUSE query (**10086–10091**) returns exactly `0xffffffffc1a38760`.
Committed main consumer **939–965** requires one nonzero valid address and
rejects missing/ambiguous results; no first-match/dedup fallback is used.

## FUSE hold, transition and recovery

The manifest selects inline `fuse_ref_page`'s caller instruction
`fuse_copy_page+0x369` (five bytes), return offset **0x36e**, and original
`fuse:fuse_copy_finish`, sympos **1**, size 176, safe preprologue **+5**.
The actual original callee base is `0xffffffffc0dca2a0` in both phases.
Probe installation is disabled, the return predicate configured, then
`0xffffffffc0dca2a5` installed; kprobe-list output confirms
`fuse_copy_finish+0x5 fuse` (main shell **9780–9839**, **10086–10145**).

| Phase | Configured return PC | Actual `/proc/<pid>/stack` caller |
| --- | --- | --- |
| Native caller across activation | `0xffffffffc0dca88e` | `fuse_copy_page+0x36e/0x610 [fuse]` |
| Current caller during abort | `0xffffffffc1a38ace` | `fuse_copy_page+0x36e/0x630 [livepatch_7]` |

Both phases reach held Y / exactly one hit, nonzero captured arg0 and zero
misses (**9879–9927**, **10158–10188**). The native reference-entry probe also
has exactly one hit and zero misses. Helper source **310–337** checks the
return PC at entry-equivalent SP before hit counting, capture or holding.

The actual recovery sequence is complete: resend signal/resent markers pass;
forced activation returns **EBUSY**, candidate module is absent, and the
resend helper remains alive without fatal completion (**9582–9729**). Clean
activation reports enabled 1 / transition 1 while the native caller is held;
release reaches unheld/completed and then transition 0 (**9942–9999**).
Fatal/consume/abort resend markers complete and the resend process exits
(**10014–10062**). Current-caller connection abort releases to `aborted`
(**10194–10215**); close completes and exits (**10230–10260**). Patch disable,
removal and helper cleanup follow (**10275–10368**). Example **14/39** passes
in **22.67s** (runner **29–30**).

Limits: `FR_LOCKED` clear is the retained static proof of the selected call
after successful unlock, bound here by exact module/sites digest and return
PC; no live raw-flag read is logged. Caller frames are observed, but no
standalone reliable-unwinder return status or dedicated unrelated-caller
runtime negative is supplied.

## TCP completed wide value and receiver integrity

The descriptor identifies `tcp_write_xmit+0x7f9`, three-byte
`cmp %rax,%rdx`, inside inline `tcp_mtu_probe`, after the completed wide
calculation. Its live roles are **RAX/64 needed, RBX/32 reordering, R15/32 MSS**.
Instruction semantics are retained in [B's measured ELF block](probe-elf-feasibility.md#tcp-a-credible-finite-semantic-block-and-a-live-computed-value);
the same module/manifest digests bind this runtime installation. Main shell
**15082–15132** renders those widths, installs `0xffffffffc1a6fcb9`
(base + 0x7f9), and confirms the replacement kprobe location.

PID **18923** owns one expected socket, fd 3,
**198.51.100.1:59964 → 198.51.100.2:9002** (runner **46**, shell
**15027–15042**). The event filter is that PID plus UINT_MAX reordering
(**15091**). Independent parsing of all **203** accepted rows (shell
**15243–15445**, runner **60–262**) finds only
`needed=2199023256532 reordering=4294967295 mss=512`.
Every row satisfies needed > UINT_MAX, reordering = UINT_MAX and MSS > 0.
The current consumer **2032–2049** checks those properties directly; neither
an old-value allowlist nor repetition of the arithmetic formula is accepted.
All four CPUs report **overrun 0, commit overrun 0, dropped events 0**
(**15449–15484**); probe profile is **295 hits / 0 missed** (**15489–15494**).
The profile counts before the event filter and exceeds accepted rows.

The receiver is started without a timeout/kill on its success path and writes
status only after `socat` returns (**14955–14968**). Sender completion/result
8388608, natural receiver termination with published **status 0**, exact
**8388608 received bytes** and full-file **`cmp`** against the prepared 8 MiB
payload all return status 0 (**15154–15202**). This is receiver EOF/content
evidence, beyond a sender count. Example **22/39** passes in **10.77s**
(runner **263**); trace cleanup returns 0 (**15498–15501**).

## Fragment native/current witness

The manifest's `inet_frag_timer` selects replacement `inet_frag_find+0x3b6`,
five-byte `mod_timer` call, inline `inet_frag_create`, RDI/64. ABI 0/56/96
produces actual fetches `next=-56(%di)` and `lock=+40(%di)`. Fragment shell
**1088–1097** performs the U/u-filtered exact-one NF4 replacement query,
returning `ffffffffc1d5bf50`, and installs `ffffffffc1d5c306` (base + 0x3b6).

| Actual phase | Timer-call observation | Profile |
| --- | --- | --- |
| Native | `inet_frag_find+0x22f/0x730`, timer `ffff9e2d3f9ec820`, next 0, lock 0 (shell **663**) | **1 hit / 0 missed**, **667–672** |
| Current | `inet_frag_find+0x3b6/0x790 [livepatch_7]`, timer `ffff9e2d3fc22bb8`, next `ffff9e2cc20057d1`, lock 1 (**1186**) | **1 hit / 0 missed**, **1190–1195** |

Both traces contain 1/1 entries. The consumer requires nonzero target linkage,
held lock, native unhashed/unlocked state, profile hits equal parsed rows and
zero misses. Both events are removed, patch disable completes, module removal,
namespace deletion and trace-instance removal return 0 (**1199–1310**).
The example passes in **10.04s**, result `expected_success`. This is the
selected stimulus/call-state property, not a general race-freedom claim.

## Launch identity, selected successes and acceptance limits

Both actual launch records (**machine-log:11–21**) name direct boot using:

- QEMU `/nix/store/kanckc6ljipqzjsrvj4aqaf87a4rhswr-qemu-host-cpu-only-for-vm-tests-10.2.4/bin/qemu-kvm` (version tag from path).
- Kernel `/nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot/bzImage`.
- Initrd `/nix/store/h3v4nwmsn39wph7apj7q6bg8hn58rv3x-initrd/initrd`.
- Main system `/nix/store/ijxaazn8qysnibd0q3y2p1gbprhnk3wf-vpsadminos-system-vpsadminos-26.05.git.bda1f5d`, squashfs `/nix/store/23765m3ba19addir8byn818fi0674z86-squashfs.img`, 8192 MiB / four CPUs.
- Fragment system `/nix/store/xihidcj5h6i0ii0wzc2c9j1h8n6jzg1d-vpsadminos-system-vpsadminos-26.05.git.bda1f5d`, squashfs `/nix/store/c4wvmci5qmhfnfzb59xipshrr21sc20k-squashfs.img`, 2048 MiB / two CPUs.

Main release `.95` is asserted in the guest. Fragment `uname -a` actually logs
`6.12.95 #1-vpsAdminOS SMP PREEMPT_DYNAMIC Sun Jul 5 16:42:06 UTC 2026`
(shell **113/726/1348**). The system version tag is `26.05.git.bda1f5d`.
Both QEMU exits are 0 (**machine-log:33–35**). These are launch-path/version
and guest-release observations; this artifact supplies no independent
in-guest boot-image SHA or notes comparison.

Main has **39/39** successful examples and `expected_success`. Other recorded
successes include exact v5/v6 failure/transition anchors (runner **3–6**), SVM
(**7–8**), occupied/unshadowed SUNRPC refusals (**25–28**), pipapo/NFtables
holds (**37–40**), SUNRPC worker/drain/callback/shadow allocation (**270–277**),
replacement exercise/removal and final kernel health (**290–297**). Detailed
semantic inspection here is limited to FUSE, TCP and fragment.
`test.log:2–11` selects main, fragment, three AMD lifecycle profiles, NFS
transition, v7 performance, SCTP baseline/hostile and NFS cancellation baseline;
**112–113** record ten scripts / ten tests successful in **2058.83s**.

No native kernel-identity case belongs to this ZIP. Its historical separate
receipt and pre-existing wrong-image `readlink` PATH negative-control limit
remain unchanged; no additional artifact or repair was requested. This audit
finds no missing required field within the assigned main/fragment contract.
It gives no historical failure cause, runtime CRC/ABI safety assertion,
whole-matrix acceptance, four-hour qualification or merge permission. Original
resolver/ELF/control/review evidence remains intact; no rerun was performed.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
