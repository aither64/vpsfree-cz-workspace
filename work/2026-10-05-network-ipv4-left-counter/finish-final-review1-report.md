**Important — plaintext campaign credentials appear in exported tracking evidence.**  
Lane: risk/security; evidence handling.

[finish-runtime-reduction-real-start-proof1.json](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-runtime-reduction-real-start-proof1.json:624) contains account passwords at lines 624, 635 and 646, plus web-auth passwords at lines 540 and 562, under `failed_phase.inputs.configuration`. These belong to the retained G13 configuration. Copying them into tracking evidence violates the workspace credential boundary and exposes them to readers or publication paths with access to that artifact. I did not establish external publication.

Root should redact exported evidence and reconcile any tracked or published copies while preserving the private original and its provenance. Artifact SHA256: `286eb4a859f006541d59935b176a7d5c81afeac64c46a2c0cec370ba954ed36d`.

During inspection, I emitted part of that nested credential block once. I should have filtered the configuration before printing it. No credential values are repeated here, and I performed no redaction, rotation or cleanup.

**No new implementation findings in the exact K/E/C committed source. All four assigned lanes are complete.** The complete report was delivered through `report_to_lead`, message `e9ae256d-d882-464d-a514-5c75c79cc2b6`. Root owns the evidence finding’s disposition and any subsequent operation.

Identity was independently verified from the absolute tracking CWD with `login:false`: `dev-session current` matched the bound session; both environment markers were absent. Fresh roster17 retained reviewer0 as ready, review-purpose, read_only, `gpt-6.1-sol/xhigh`, thread `01a10c52-55c7-7490-8cd9-75efda7f00d9`. No override, fallback or delegation occurred. Required skill references, workspace routes and affected repository guidance/contracts were read or reused after confirming unchanged content.

The reviewed objects were:

| Project | Exact base | Exact head | Exact tree |
|---|---|---|---|
| K | `873758fd6aec0c03f50a94600e0ceab97946f255` | `49221a07e2fabbee4a3621979f814eac8c8bad9d` | `7af2e7c2b9564dc26a3cb456183334b196f20be7` |
| E | `3e5dc4681b0343ec236c3f3dfc0d6f725577c376` | `265bd7892b334c67cf760680d06e24fcd06d5cdf` | `1c78c79e0ea77375d450322dbd4e2affbbcec1f8` |
| C | `6e4947b52abe103c582bfab2d0b37a8f17a7c02d` | `b5c37e01957b9bde4c382a9fa0e47ae9c8db93ba` | `8e7fb494dcf12daa4c3fed25e31148dba08224c4` |

Both K worktrees matched. All inspected worktrees were clean. Independently generated complete binary/full-index diffs matched the six inventory artifacts; their hashes, heads, trees, merge bases and chronological commit lists matched. Unchanged Vebe4fab3, Wce856841, Db1ec1bf1 and isolated W30cce68142 were confirmed, preserving their completed conclusions within their existing limits.

The four lane conclusions are:

1. **General:** K’s [launcher](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime/cluster/launcher.rb:79) forwards non-TTY `$stdin` through `Engine#ssh(input:)` while holding the existing gate. TTY input selects `nil`, delivering EOF without reading the terminal. The unchanged Engine retains endpoint selection, quoting, private key and known-hosts handling, strict authentication, environment clearing and failure behavior.

   Actual Ruby Open3 source confirms that an IO supporting `readpartial` reaches `IO.copy_stream`; Open3 closes child stdin, reads stdout/stderr concurrently and joins its child waiter. This verifies the delegation without executing local tests.

   The three added CLI tests exercise the actual launcher, State gate, Engine and Open3 with an owned synthetic SSH executable. They cover empty EOF, exact bytes without a trailing newline, binary input, file-backed stdin, trust arguments, environment clearing, gate exclusion and fixture preservation. The terminal case proves the read-refusing branch; it does not establish physical PTY behavior.

   The current `resources sh -s` consumer at `tools/runtime-verify.rb:594` reaches this input seam. No source correctness finding.

2. **Architecture/repetition:** The correction uses the existing Engine input contract in the single public launcher. Open3 owns copying and child waiting. Checkout and packaged launchers share the implementation. No duplicate transport, stdin framework, PTY mechanism or lifecycle implementation was introduced.

   E continues to import read validators from its selected immutable K source and delegates live operations to the paired packaged CLI. No architecture finding.

3. **Scope/proportionality:** Direct comparison of accepted K9c551c6 with K492 changes exactly three paths: `cluster/launcher.rb`, the added block in `tools/test-runtime.rb`, and the short runtime-contract paragraph. Frozen source hashes match the final launcher and test file. Engine, verifier phases, package selection, credentials, guest configuration and workflows remain unchanged.

   E’s affected delta changes only K input identity. C contains generated lock updates without module or service changes. No scope finding.

4. **Risk/compatibility:** Input travels to the existing authenticated remote command under the existing gate; it is not interpreted as local shell text. Terminal input remains unsupported. Existing Open3 failure, interruption and waiting behavior is preserved. Synthetic tests do not establish arbitrary transport failures or real guest behavior.

   No schema, ownership, credential or guest-format change occurs. The exported credential finding above is the sole new Important finding.

The previous Important capture-budget finding remains resolved in the preserved G9c/current source. `tools/runtime-verify.rb:315` uses zero existing-guest base only for live capture after resumed-guest attestation and continuity. Start and resume retain full guest admission. The focused regression exercises actual capacity methods, insufficient start/resume capacity and one-byte capture-margin failures. Assessment bindings, reserve/growth checks and private receipts remain intact; the final hosted verifier suite includes this regression.

I independently checked the final consumer and lock composition. E’s embedded owning graphs match all **45 K paths and 17 D paths**. It selects K492 with NAR:

`sha256-cFmsVhyYoM1JvR8t8CO+SZy8EjBr/KPNKO6EBL4C57g=`

Runtime and runtime-source come from the same input. Compared with accepted Ecbb8, only `kb-runtime` changes; unrelated roots and follows remain identical. Actual range-diff preserves the provider patch and message.

C selects Vebe through `vpsadminServices` and W30cce through `vpsadminWebui`. Base-to-retained-V changes only the services node; retained-V-to-final changes only the WebUI node. The WebUI API follows still resolves to `vpsadminServices`, with intended nixpkgs/OS follows preserved. Wce is an actual ancestor of W30. Fresh-base changes contain upstream lock selections, without feature module/service changes. No configuration build or deployment was inferred.

The complete history conclusions are:

- **K:** two logical commits—`680e0b1d937fac7df3f6f99f002ed01c09a96fdc` for the canonical V pin, then K492 for the owning runtime/capture/reduced verifier. Stdin and memory corrections are folded into their owner. Superseded two-root/historical/drain approaches are absent from the final series. Consumed G13/G9c and earlier G4/G6/K68 provenance remain preserved outside that series.
- **E:** two commits—`9aa41d21ea709af6a4845d3b9360971120470c83` for canonical K/D inputs, then E265 for the unchanged provider. No repeated input tail, fixup, merge or alternative remains.
- **C:** two generated commits—`ed54e93b16d8a055e28d1111848aaccd1881c5e4` for V, then Cb5 for W30. Range-diff confirms the retained V patch, removal of the superseded Wce pin and the final W30 selection. Generated messages are preserved. Native hook evidence records Nixfmt/pre-commit success with commit-message warnings.
- Complete V/W/C/K/D/E counts are **4/1/2/2/3/2**; isolated W30 has one owning commit. No obsolete intermediate approach remains in these final streams.

**No database migrations exist in K/E/C/W/W30/D.** V retains the sole `20261006120000 AddNetworkEnabled`, following `20260914190000`: directly reversible, `NOT NULL`, default true, without transitional guards. The cached V `origin/master` at `8a50010f46ad134e132394f2159d031601c17778` lacks that path. No fetch occurred. Disposable/preview consumption is known; production, release, deployment and other external consumption remain unverified.

Engine state2/artifact1/connection1/lease1 and E binding1 remain unchanged. `single-runtime-v1` refuses superseded campaign roots and arguments without adoption or conversion. Future corrected source does not repair incomplete state or prove historical rollback/update compatibility. Prior SSH ownership/trust/readiness/task-discovery/socket-handoff and lost-ack/waiter-barrier conclusions remain applicable to unchanged implementations. V’s expected disabled-denial feedback was resolved at Vebe; it is not an unresolved HTTP500 Advisory. Completed W30 conclusions remain bounded to that isolated source review.

I independently matched **all 27 hosted evidence hashes** against the collector map and acceptance map, then inspected exact checkout/fetch identities, native job/step metadata and raw results:

- K `38071236937` and runtime-K `38071232693`: exact K492, success.
- E `38071327643`: exact E265, both declared checks successful; native fetch confirms K492 and its NAR.
- K: runtime **99/1242**, closure **12/51**, machine **19/667**, verifier **30/348**, export **4/21**; Node **25/14/9/7**, with zero failures, errors or skips.
- Selected E SDK **8/68** and public composition **5/58**: zero failures, errors or skips.
- Broader D summaries retain 12 and 3 skips; E’s broader suite retains the environment-dependent supplementary-group skip. Nonverbose summaries do not identify every skipped case.

Source `--allow-missing` succeeded. **Strict media was skipped.** These results establish the hosted source/package/synthetic boundaries.

Full native log SHA256 values:

```text
K         48d6ed7bca050ed33647997ee1c193f322624ecd3b71dc23bbb33ee05b15e556
runtime-K f6bdb81acdeb701ade32c320905e0893ecc57ba1897bb08b5694982917af44e8
E         deb40bf0be51337013221f54256cf18dcf6840455e28cd6b1bf965197a1d9eaa
```

G13 remains a distinct failed real qualification using G9c551. Stored proof records fixed 8GiB image construction, successful public start of two 2048MiB guests, and matching identity/current-system reads. The next public `sh -s` received empty input; runtime-smoke exited 1 at resource observation. The omitted launcher input explains that route. Neither resource insufficiency nor a blank current-system defect is established.

There is no corrected real replay or completed runtime receipt. TLS/API/member PHP, live lease, ordinary stop/resume, fixture continuity and canonical PNGs were not reached. K492’s synthetic transport success does not relabel G13 as a pass.

G13, G4/G6/isolation3 and preview resources remain untouched and incomplete. The finite qualification ended. No further guest, replay, upscale, signal, stop/reset or cleanup was selected or performed. Future operations require a separate decision. Media freshness, installed activation, configuration builds, merge/default integration, deployment and production KB readiness are **not certified**.

No tracking/source writes, local verification, CI polling, publication or lifecycle operations occurred.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
