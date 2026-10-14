# Public SSH stdin: source-only freeze

The launcher now forwards its non-terminal standard-input IO through the existing Engine#ssh input seam while retaining the same gate. It reads no buffer in the launcher. Terminal input selects nil and keeps the prior EOF behavior. No interactive/PTY feature, flag, supervisor or Engine change was introduced. Root prose matches these facts and is preserved.

Three regressions are declared in the existing runtime owner. Piped and file-backed cases execute the actual public launcher and real synthetic SSH child; terminal branch coverage injects a read-refusing tty? object before the actual CLI runs. Strict argv/trust/environment/gate and private fixture bytes are checked. No test mocks Engine#ssh. Every original test is preserved.

All tests remain UNRUN. No passing source, SSH guest or real operation claim is made. The lead-reported failed campaign and all previous receipts remain historical evidence; this repair does not authorize replay or cleanup. Root owns normal consolidation/publication, exact hosted K/E gates and review.

No material scope blocker or deviation was found. The active tool catalog does not expose report_to_lead; a report and fresh message_id are saved here without claiming delivery or using an undocumented messaging route.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/
