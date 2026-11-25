# Current-build probe-site feasibility

Owner: implementer1. Planning evidence only, measured 2026-11-03 from the
session-owned worktree at `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
Architect owns the proposal; implementer3 owns source semantics and handler
contracts. No application implementation, source/pin/Git edits, Nix evaluation,
build, runtime test or CRC check was performed for this package.

## Artifact identity and scope

Both previously copied outputs had disappeared from the store. The lead then
explicitly authorized one fresh catalog-resolved Luna/low watcher to restore
these two exact signed-cache targets, with a 90-second deadline and no retry:

```sh
timeout --signal=INT --kill-after=5s 90s nix copy --from https://cache.vpsadminos.org /nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95 /nix/store/6hiwxy4nmpnb18xmsn9a5mh5g8mb246p-livepatch_7-6.12.95
```

The copy exited 0 in 6.405 seconds; exact-process reconciliation found no
remaining owned copy or timeout. [Restore receipt](probe-module-restore-result.md)
and [log](probe-module-restore.log) retain that operation. Parent
`nix store verify --sigs-needed 1` checked contents and trust for both outputs
and exited 0. Measured module digests match their earlier independent receipts:

| Artifact | Module SHA-256 | Module bytes | GNU build ID |
| --- | --- | --- | --- |
| Current `qi47yi2g9kp89dv0h8jxwndm89vbq6az` | `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f` | 82,769,056 | `fd8cbfe4c314ddac8f35d87bee4bb8b909e479d5` |
| Historical `6hiwxy4nmpnb18xmsn9a5mh5g8mb246p` | `573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d` | 82,766,368 | `8e6cb0d33933cce7640901a683745592d68c1240` |

Both modules are at `OUTPUT/lib/modules/6.12.95/extra/livepatch_7.ko`.
They report GCC 15.2.0 in `.comment`. Analysis used already-local GNU Binutils
2.46 at `/nix/store/63wdfxcylc7rzym8iwhv84yppg8gj3vv-binutils-2.46/bin/`.

All executable sections and their code/livepatch relocation sections are
byte-identical between these two artifacts. In particular, `.text` is section
13, file offset `0x8c40`, size `0x74ca2`, SHA-256
`d5ae5fadc4b620e5ee25662af2babb8864040f4d3c0e8ac0cf8fef6321fe81d5`.
Thus there is **no observed instruction-layout drift in the examined pair**.
Future current builds still need explicit predicates; a whole-file digest
difference alone does not establish instruction changes or justify dropping
these witnesses.

## Symbols and relocation encoding

Each selected function has exactly one defined function symbol of its exact
name, local `t`, in coalesced `.text`; these addresses and sizes match in both
artifacts. The 16-byte `__pfx_*` symbols are separate symbols, not function
entries. Imported `.klp.sym.OBJECT.NAME,ORDINAL` symbols occupy a separate
namespace and must retain object/ordinal identity during matching.

| Function | `.text` value | Size |
| --- | --- | --- |
| `svm_vcpu_run` | `0x3280` | `0x8a2` |
| `fuse_copy_page` | `0x11660` | `0x624` |
| `inet_frag_find` | `0x44e50` | `0x788` |
| `tcp_write_xmit` | `0x483c0` | `0x1703` |
| `nft_pipapo_insert` | `0x61890` | `0xa15` |
| `vpsadminos_sunrpc_cb_release` | `0x70560` | `0x3f` |
| `xs_connect` | `0x70b10` | `0x2e5` |
| `vpsadminos_sunrpc_tls_drain` | `0x70e70` | `0x7e` |
| `xs_tcp_tls_setup_socket` | `0x70f00` | `0x84a` |

The measured named calls are x86-64 five-byte `E8 rel32` instructions. Their
ELF64 RELA offset points to the four-byte displacement, one byte after the call
opcode; the addend is `-4`. Resolve the target section via relocation metadata,
bound it to the caller's symbol range, then validate the instruction boundary
and opcode. Subtracting a function start from a relocation offset alone would
select the displacement, not the probe instruction.

## FUSE: a real two-call ambiguity, resolved by inline identity

`fuse_copy_page` has two calls to the exact imported callee
`.klp.sym.fuse.fuse_copy_finish,1`. They are `R_X86_64_PC32` entries in
`.klp.rela.fuse..text`, at `.text` displacement offsets `0x11853` and
`0x119ca`. Thus the calls are function-relative `+0x1f2` and `+0x369`.
Ordinary `objdump -dr` did not label these special relocations; `readelf -rW`
does expose them. A resolver must include special livepatch relocations.

Both sites also have a preceding call to
`.klp.sym.fuse.unlock_request.part.0,1`. Callee uniqueness or simply checking
for a preceding unlock is therefore insufficient. Existing inline DWARF
distinguishes them in both artifacts:

| Call | `addr2line -j .text -f -i` inline attribution |
| --- | --- |
| `+0x1f2`, `.text:0x11852` | `fuse_try_move_page`, `fs/fuse/dev.c:864`, in `fuse_copy_page:1008` |
| Intended `+0x369`, `.text:0x119c9` | `fuse_ref_page`, `fs/fuse/dev.c:965`, in `fuse_copy_page:1003` |

The intended current and historical instruction neighborhood is identical:

```asm
+0x350  mov  0x8(%r14),%rdi
        test %rdi,%rdi
        je   +0x366
+0x359  call unlock_request.part.0     # special livepatch relocation
        test %eax,%eax
        jne  +0x554
+0x366  mov  %r14,%rdi
+0x369  call fuse_copy_finish           # selected instruction
+0x36e  mov  0x18(%r14),%rax
        mov  %r12,(%rax)               # subsequent pipe-buffer publication
```

Finite selection by caller + qualified callee + inline `fuse_ref_page` scope
+ call boundary + copy-state register/frame predicate is credible here. Source
line numbers are diagnostic evidence, not the selector's semantic identity.
Zero or multiple matches, missing usable inline DWARF, or an unsupported frame
must produce an explicit diagnostic.

There is a separate hold ABI constraint: `fuse_copy_page` pushes
`rbp,r15,r14,r13,r12,rbx`, then subtracts `0x38` from RSP. At the selected call
the established RBP frame remains live and RSP is entry RSP minus `0x68`;
RDI is the copy-state pointer in R14. This is not the entry-equivalent stack
state of the post-fentry sites below. The existing FUSE example uses the
schedulable hold trampoline, rather than enabling `probe_spin_hold`.
Old/current frame layouts match exactly, but a future selector needs the
source owner's accepted interior-frame/unwind contract. Static call selection
alone does not prove that an altered interior frame is safe to hold. This
package makes no new alignment or unwinder safety claim.

## SUNRPC: unique named calls and actual arguments

All three intended callee matches are unique **within their exact caller
symbol**, with ordinary `.rela.text` `R_X86_64_PLT32` relocation/addend `-4`:

| Caller / callee | Call offset | Displacement offset | Actual pre-call state |
| --- | --- | --- | --- |
| `xs_connect` / `klp_shadow_alloc` | `+0x1ec` | `+0x1ed` | `mov %rbx,%rdi` supplies transport; RSI shadow ID `0x2c5d466e3067e6a`; EDX `0x30` allocation size. Existing site is count-only; no ABI-argument reinterpretation needed. |
| `vpsadminos_sunrpc_cb_release` / `klp_shadow_free` | `+0x27` | `+0x28` | Callback `0x18(%rdi)` loaded into RAX, then `mov %rax,%rdi`; same shadow ID in RSI; `xor %edx,%edx` supplies NULL destructor. RDI is the transport. |
| `vpsadminos_sunrpc_tls_drain` / `cancel_delayed_work_sync` | `+0x56` | `+0x57` | After `vpsadminos_sunrpc_tls_take_work` returns, RAX is saved in RBX and checked non-NULL; load `0x18(%rbx)` into RAX, then `lea 0x640(%rax),%rdi` supplies the owned transport's embedded work. |

These are real instruction/argument predicates supporting the source owner's
existing count/matched-argument contract. The ownership and exactly-once
release expectations remain independent source/runtime assertions; the ELF
does not establish that they occur in a live run.

## Post-fentry holds: validate the prefix, not an unconditional `+5`

`svm_vcpu_run`, `nft_pipapo_insert` and `xs_tcp_tls_setup_socket` all begin with:

```asm
+0x0  e8 00 00 00 00   call __fentry__    # PLT32 relocation at +1, addend -4
+0x5  55               push %rbp
+0x6  48 89 e5         mov %rsp,%rbp
```

At `+5`, no function prologue push/allocation has executed and RDI retains
arg0. That matches the relayed vCPU/NFT/work_struct argument contract and
entry-equivalent stack requirement in both measured artifacts. The finite
predicate should validate this prefix and first post-fentry boundary for the
selected function, and reject changed unsupported prefixes rather than assume
five bytes. Runtime ftrace/kprobe registration and ORC behavior remain untested.
Frozen-boot `+6` gate repair is a different, already-prologued contract and is
not recertified here.

## Fragment timer-order witness

Within `inet_frag_find`, exactly one call targets `mod_timer`:
`R_X86_64_PLT32` at displacement `+0x3b7`, call `+0x3b6` (`.text:0x45206`).
DWARF identifies inline `inet_frag_create`, `inet_fragment.c:409`, within
`inet_frag_find:428`. Representative instructions are:

```asm
+0x393  call rhashtable_insert_slow
        mov  %rax,%rbx
        test %rbx,%rbx
        jne  insertion_error
        movslq 0x10(%r15),%rsi
        mov  jiffies(%rip),%rax
+0x3af  mov  -0x58(%rbp),%rdi          # timer pointer
        add  %rax,%rsi
+0x3b6  call mod_timer
        mov  -0x50(%rbp),%rdi
+0x3bf  call _raw_spin_unlock_bh
```

This supports a unique call/argument site and preserves the observed
insert-success -> timer -> unlock neighborhood. The handler's `timer-56`
node and `timer+40` lock offsets remain separate fixed-ABI predicates: symbol
selection does not validate them or prove a linked/locked object at runtime.
No missed-hit, linked-state or held-lock runtime assertion was exercised.

## TCP: a credible finite semantic block and a live computed value

There is no named call to select the inlined arithmetic. DWARF maps the current
and historical `tcp_write_xmit+0x7e0` to inline `tcp_mtu_probe`,
`tcp_output.c:2479`; the queued-byte comparison at `+0x7f9` maps to line 2495
in that same inline scope. The block is identical in both modules:

```asm
+0x79f  mov    0x578(%rbx),%ebx       # reordering input (source-owner mapping)
+0x7a8  mov    0x5a0(%rax),%r15d      # mss input (source-owner mapping)
        ...                           # gates/probe-size preparation
+0x7d7  mov    %ebx,%eax              # 32-bit write zero-extends into RAX
+0x7d9  mov    -0x30(%rbp),%rdi
+0x7dd  movslq %r8d,%rdx              # probe_size
+0x7e0  add    $0x1,%rax              # 64-bit addition, after zero extension
+0x7e4  imul   %r15,%rax              # 64-bit multiplication
+0x7e8  mov    0x674(%rdi),%ecx
+0x7ee  add    %rdx,%rax              # RAX now holds size_needed
+0x7f1  mov    0x624(%rdi),%edx
+0x7f7  sub    %ecx,%edx
+0x7f9  cmp    %rax,%rdx              # queued bytes versus size_needed
+0x7fc  jb     +0x853
        ...
+0x802  mov    0x59c(%rdi),%esi
+0x808  mov    %rsi,%rdx
+0x80b  cmp    %rax,%rsi              # snd_wnd versus same size_needed
+0x80e  jb     +0x853
```

Within this function there is exactly one each of the measured
`add $1,%rax`, `imul %r15,%rax`, `cmp %rax,%rdx` and `cmp %rax,%rsi`
instructions. The meaningful finite predicate is their operand-width/data
relationship in the inline scope, with both unsigned comparisons branching to
the same failure target. It is not uniqueness of one arbitrary opcode or fixed
register spelling. Supporting offset/register allocation drift can bind local
register roles while requiring this narrow typed block; unsupported compiler
transformations must fail with a diagnostic. A generic whole-function dataflow
engine is unnecessary for this measured layout.

At `+0x7f9`, RAX is demonstrably live **after** computation and **before** the
queued-byte comparison. A later read-only register capture can therefore
observe the result, rather than merely count entry into `tcp_write_xmit`.
Qualify the observation by the intended socket/workload, `reordering=UINT_MAX`
and positive MSS; then `size_needed > UINT_MAX` is the proposed independent
property. The existing probe only counts at `+0x7e0`, so exposing this live
value requires later explicit implementation. The source owner's receiver
content-integrity addition and a disposable cast-revert negative control remain
future validation: the reverted widening should fail the typed selector and/or
independent value property. Neither was implemented or tested here.

## Optional whole-section comparison

Using `readelf -SW` physical section offsets/sizes and hashing those file
ranges found 2,322 named sections in each module, with exactly three differences:

| Section | Current bytes / SHA-256 | Historical bytes / SHA-256 |
| --- | --- | --- |
| `.debug_str` (compressed, not allocated) | 6,401,374 / `f2824d61870274721b96a76805ad52831584a9eac450e7daa3e840fb8dfce454` | 6,398,739 / `71f6c3485743d71db36dbf7c19b85ba77625da03b3919726de80004ae8872c80` |
| `.rela.debug_info` (not allocated) | 52,275,744 / `fb60cc4e0a2034fe87872dbf0c88975d97f9a7f64e41bc7437e33bf39d984f0b` | 52,275,744 / `2fd4d7434eb938bb10a82649b844a1c562f7044a700b1811fda1fba4df95cac1` |
| `.note.gnu.build-id` (allocated note) | 36 / `d495396974645311e64f662ec329d9e26103444403681473011913e962b5b4dc` | 36 / `58f0bc38a718600cf3340191077034ab1b866564319dbabcde56232be2469041` |

All executable sections, symbol tables, allocated data apart from the build-ID
note, and code/data/livepatch relocation sections match byte-for-byte. Of 115
RELA sections, only `.rela.debug_info` differs. Container file offsets/header
layout can change as debug section sizes change. GNU `objdump -h` reports
uncompressed sizes for compressed debug sections, so those sizes must not be
used as physical byte ranges. This scoped comparison narrows the digest drift
to debug strings/debug relocations/build ID for these artifacts; it makes no
claim about runtime, ABI, import CRCs or arbitrary later builds.

## Resolver feasibility and remaining decisions

Already-local `nm -S`, `readelf -SW/-rW`, `objdump -dr --disassemble=FUNCTION`
and `addr2line -j .text -f -i` expose every measured fact above. Extra Python
ELF/disassembly dependencies were unnecessary for this investigation. A durable
resolver may use pyelftools/Capstone to avoid parsing tool text, but their
availability or packaging cost was not evaluated here. No decoder/framework was
implemented.

The proposed digest-bound finite witness record is feasible for the measured
named-call and post-fentry contracts. FUSE needs qualified inline attribution
plus an explicit accepted interior-frame contract; TCP needs the measured
typed-block predicate and result-register capture. Record exact symbol/section,
resolved relative offset, callee or inline identity, and validated frame/arg
predicates. Missing or ambiguous semantics must remain a diagnostic, not a
skip, offset guess or substitution with weaker entry coverage. Runtime
acceptance and negative-control evidence are still required by the architect's
eventual implementation brief.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
