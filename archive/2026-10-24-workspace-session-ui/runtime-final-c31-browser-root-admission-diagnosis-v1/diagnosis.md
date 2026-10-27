# Exact root admission observation

The single authorized file-only observation completed (command exit0; this means observation completion, not admission success). In-process elapsed time was 0.001399100s. All three exact root paths were attempted once; no launcher/guard import or invocation, Nix, DB query, output inventory, source/tool/process scan, retry, repair or lifecycle action occurred.

| Exact root | Actual result | Frozen expectation |
| --- | --- | --- |
| za8 shell drv | FileNotFoundError, errno2, at lstat; no open/hash | mode0444,4680bytes, SHA25629f33a38d1297d3b58c3311d0c62b385f1f7462c1ff7f6c44e19816edf712824 |
| d0jj browser drv | FileNotFoundError, errno2, at lstat; no open/hash | mode0444,2184bytes, SHA25695cc590be7ab365980b493dda29a8219a1108b5073ce3b3a340a46e1854b0574 |
| 8q2 review-assets drv | Regular non-symlink, mode0444,3120bytes; bounded no-follow open/read, fstat before/after stable; SHA25617e5058c9d5b36cb41e590c538e5ab3a79de614aae13f8cdd85802ad72bd9927; exact match | Identical |

Full absolute paths, expected values, separate per-root observations, identity snapshots/errors and timings are in observations.json. The read cap was16MiB per root with a30s observation deadline. Only3120bytes were read from a store target; missing paths were never hashed. Exact command/cwd/actual exit/tool capture and timing are in observation-command.json.

These facts explain why the v3 Boolean raw-root admission could not pass at this observation time: two exact root paths are unavailable to lstat. They make no claim about NixDB validity, outputs, caches, or why the paths are unavailable. No absence/GC/deletion cause is attributed. The earlier materialization two command0 receipts, original failed aggregate, captured root hashes, delayed comparison and accepted reconciliation retain their original historical scope.

The new bindings.json preserves23 exact immutable local evidence hashes, including the complete frozen nine-file v3 packet, its failed owner guard/stdout/stderr, actual materialization receipts/raw metadata/identities/outcome, original root capture, delayed comparison and reconciliation/parent assessment. All originals remain unchanged. No successor or operational remedy is proposed; parent decides any further source-backed method.

Session remains open: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/>.
