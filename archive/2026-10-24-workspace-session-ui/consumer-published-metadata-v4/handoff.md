Prepared only: consumer published metadata v4

Assignment 2e8a63a1-b4bb-467a-9811-4139382834e1. Identity/current/environment pair verified; live implementer0 is ready Sol/xhigh/workspace_write. The frozen v3 release is preserved at SHA bb06cf8004aee16fd59b8518beb8a68ba13c460c24e4b965be34287a67584f1a. No project or peer source/index/ref was inspected or changed in this preparation.

capture.py is a self-contained 303-line script, using the existing exclusive-receipt and owned-process-group capture pattern. The only spec changes are releaseId and the two result destinations, recorded in spec-from-v3.diff and static-assessment.json. Full new source is also in capture-new-file.diff. The two command arrays, cwd values, manifests, indices, eight bindings, 1550-entry evidence manifest, selected/resolved Nix identities, bounds and forbidden keys retain the v3 expectations. There is no expectation refresh. dev-session/Python identities are carried from the retained own continuation inputs; they were not rediscovered with a tool scan.

Guard-only has an explicit branch before execute/release/result creation; it imports no local driver and launches no Nix. It checks own/script/spec/upstream bytes, pinned Python/dev-session and current identity, incoming forbidden keys/session pair, selected Nix alias vs resolved binary and selected bytes, all 472+620 source modes/bytes/blob identities, both raw indices, eight fileBindings and all 1550 exact absolute evidence paths. Successful stdout is only JSON actual counts. This mode was NOT run by implementer0.

The complete literal argv/cwd for guard-only and execution are in ready.json. Both use the pinned Python -I -B. No shell/launcher code is needed. The parent must inspect, run guard-only, then write parent-release-v4.json with the exact template bindings and a real nonempty releaseId before releasing execution to a fresh utility. parent-release-template.json is not a release. Copy its fields to the specified new parent-release path only as part of parent authorization; results-v1 must remain absent before execution.

Environment policy is unchanged literal inheritance, with no filtering or normalization. Exact forbidden keys from the spec refuse before any Nix, without logging values. Only the explicit public name list is logged; all other values, including secrets, inherit without logging. No equality between selected alias and resolved Nix strings is required: argv[0] equals nixSelected, resolve(nixSelected) equals nixResolved, SHA(selected) equals nixSHA256.

Execution guards first, then exclusively creates results-v1 and immediate batch/command started receipts. Commands run sequentially once; configuration 120s then workspace 180s; batch 420s; stdout/stderr cap 16 MiB each. Timeout/overflow/interruption sends only the owned group INT/5s, TERM/5s, KILL/2s as needed. Receipts retain exact argv/cwd/public environment/tool, PID/group/startticks/procExe when available, exit/end/elapsed/raw stdout/stderr and signal actions. First failure stops the sequence; finally always attempts postflight guards after an admitted operation. Partial/failing results remain; no retry, cleanup, or daemon-settlement claim. A pre-admission refusal creates no results.

AST parsing, compile-object construction without execution/import, JSON parsing, local packet hashing, and exact v3/v4 spec equivalence passed. No script/guard/Nix/metadata/root/eval/build/test/network/source/Git operation was run. Prior three refusal packets remain untouched. No metadata/source binding acceptance is claimed.

Parent owns inspection, guard-only, fresh Luna/max1 execution, interpretation and later source/eval/build releases. Session remains open.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
