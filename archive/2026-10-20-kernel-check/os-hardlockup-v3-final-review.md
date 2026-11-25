# Focused final review: paired panic declarations

Lead-preserved read-only reviewer0 final report summary. Retained reviewer0
Sol/xhigh/read_only identity/session verified; no override/fallback/nested agent.
All four affected lanes reviewed at high host-policy risk. No findings.

Accepted range: base55c5046514d06fe9398a022c1622bdaae5228841 to
8528262315b0794a8f50917cf33c53a07fd14030. Reviewer verifies clean HEAD=SSH
feature, staging/merge-base55c504. One coherent v3 commit, sole crashdump.nix
+7/-1, treeed8f0498c77a1fb673700065baabaf697cfefaab,
blob2e6a906118374ba5a42b74e465ed1e0cd2b4b5ed. Message validation and chronological
v1/v2/v3 history, normal -F hooks and <=80 columns pass.

Final source meets explicit narrowed request: ordinary hard+soft sysctl integer1
under crashdump-enable; retained boot arguments and hard-lockup NMI comment.
Custom activation helper/hook/description entirely removed, no replacement
mechanism. Full module receipts enabled1/disabled omission/paired override0/
null omission and generated text independently checked; no panic-target write
or custom activation exists, boot lists unchanged. Format/parse/dependencies/
whitespace/hooks pass. Existing crashdump module is correct generic owner;
no site duplicate, unrelated framework, detector or threshold change.

Important scope distinction: a GENERIC sysctl-on-switch solution was requested
as a separate design proposal. Implementing it is not required for accepting
this source cleanup. Current OS runit applies declarations at boot stage1;
ordinary live switching does not itself apply them. NixOS's systemd trigger
behavior is different. Publication/evaluation is not proof of running values.
Null/removal does not reset live values or cancel retained boot arguments.
Overrides, rollback/readback and detector/crash-capture limits remain explicit.
No coordinated rollout, persisted format, API/protocol change or host mutation.

Whole final history: one owner, older b81c/14cdf folded with exact historical
backups/evidence; no obsolete commits, fixups, add/revert residue or transitional
compatibility. No repeated dependency/input/channel/generated streams or feature
input changes. NO MIGRATIONS in either package, none introduced/merged/released/
deployed/consumed; lineage empty and sound. Config withdrawal frozen37a..37a
remains zero diff/history, newer upstream commits unrelated.

Source review accepted. New exact-head CI/full system build/actual runtime/crash
behavior not certified; old14cdf checks are historical. No new test/observer,
merge/pin/deploy/runtime/fault/lifecycle operation performed by review. Generic
proposal remains suggestion only, outside this source deliverable.
