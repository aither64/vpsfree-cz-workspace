# Final verification and readiness

Ready, awaiting merge approval. Implementation and required review corrections
are complete on the exact published, clean source composition below. Deployment
and configuration pins remain outside the authorized implementation scope.

| Repository | Base | Final head |
| --- | --- | --- |
| codex-web |57972192e30fe52ab33b867c8fe4d171f59a7fd5 |852e8c51091512bc79ca6c921ef1f5ccc46a9535 |
| dev-workspace |52dcd471186ef874c5c93f4133744195d4815454 |db25364999aa4bf12b67506662a08e9e464bee33 |
| workspace |0ea5682410a38fe19627bc731e13894c1e51db57 |3de65bbd0e90f0c3b19e0d64ed925158155647a6 |

Final SSH checks found these exact feature heads and unchanged master baselines.
Comparisons are captured in the portal. [Complete final inventory](final-remediated-inventory.md)
records all3/8/3 commits, final diffs, one final dependency stream per consumer,
no obsolete history and no migrations. [Independent review](final-review.md)
covered all four lanes with retained reviewer0 Sol/xhigh. [Requested corrections](review-remediation.md)
were directly inspected and checked under the narrow-fix policy, without a new
public contract or design expansion. Pure history splits reproduce reviewed trees.

## Acceptance evidence

- [Actual Chromium acceptance](verification/browser-scroll-watcher-result.md):
  exit0, elapsed15s, Go6.682s. Covers sanitized user Markdown/attachments/citations,
  team view, Send/receipt recovery and X, source middle-click/copy/original download,
  500-artifact races/download/independent scrolling/refresh/removal/narrow layout,
  rapid sequential Add exact displayed effort, no dialogs/pageerrors.
- [Supplemental native links](verification/native-links-watcher-result.md): exit0,
  approximately18s, Go3.934s. Standard click, Linux Ctrl-click, Enter and trusted
  uncanceled right-click passed. Correct viewer/line fragment, noopener and original
  page retention verified. Headless testing does not select OS menu items; macOS
  Cmd-click was not executed on Linux. No source/pin edits for this supplemental test.
- Workspace default package plus policy/instruction/deployment checks, A default/
  generic-source and B package/generic-source stages all passed. Exact derivation/
  output receipts: [workspace](verification/post-review-packages-3de65bbd/workspace.json),
  [A](verification/post-review-packages-3de65bbd/codex-web.json),
  [B](verification/post-review-packages-3de65bbd/dev-workspace.json).
- [Installed metadata assertions](verification/post-review-packages-3de65bbd/metadata-assertions.log)
  passed: schema6/full_access, two-implementer defaults and3–6 variants, unchanged
  role models/efforts, capacity8/digest, separate Luna/low utility1, native policy,
  exact shipped shared sources and Codex0.163.0.
- [Registration correction](verification/post-review-packages-3de65bbd/registration-contract-correction/diagnosis.md):
  original CLI call succeeded with nativechild0/states[] plus required reporting
  MCP args. Batch's final pure assertion incorrectly expected all argv empty.
  Corrected exact reporting-only whitelist passes original actual JSON, owner0.954s,
  lead independent rerun0.793s. Derivation/input/hash receipts bind unchanged A/B/C
  and original outputs. No build, metadata or CLI repeat was needed. Original batch
  exit1/915.254s remains preserved; it reflects that incorrect assertion, not a
  product failure. The pressure GC later collected the unrooted package output;
  evidence remains bound to the surviving derivation and exact source NAR. A future
  deployment must realize its approved candidate again if needed.
- [A CI39505066197](https://github.com/aither64/codex-web/actions/runs/39505066197)
  SUCCESS on852e8c5; [B CI39506876852](https://github.com/aither64/dev-workspace/actions/runs/39506876852)
  SUCCESS ondb25364 (fast/creation/archive, host intentionally skipped). Final
  [A receipt](verification/ci-852e8c5.json), [B receipt](verification/ci-db25364.json).
  Workspace has no branch workflow. Earlier stale514a82a/c9b02d0 runs also completed
  success; no active stale run remains. Cancellation attempts had returned403.

Earlier browser failures were diagnosed fixture issues: test certificate/download
interception, then directory-collapse scroll clamping. B folded narrow test fixes
into the owning presentation commit; source behavior stayed unchanged and all
original behavior assertions remain or are stronger. No blind retries.

## Remaining boundaries

No application profile selection, deployment, configuration integration, live roster
change or session lifecycle action occurred. All source claims are explicitly
released; all utility operations finished. Session stays open with lifecycle active.
Merge approval is still required for codex-web/master, dev-workspace/master and
workspace/master. Recheck targets and verification identities before approved
fast-forward integration; no approval is inferred from this readiness report.

The production POST502 cause remains unproved. Implemented recovery preserves
original input/uploads/identity and confirmed state; disposable tests establish
that contract, not a live App Server restart or elimination of all proxy errors.
A1 conservative unknown cluster count after failed enrichment is intentionally
accepted. No remaining implementation, review or verification task is identified.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
