# Portal upload acceptance fixtures

Real dev-session lifecycle acceptance needs a PTY for the existing yes/no
confirmation and a committed active lifecycle before committing the completed
state. A piped answer is refused; committing only the completed state is also
refused. The fixture must establish a local bare origin for archive/revive fetches.
These refusals were fixture setup errors, not upload failures.

Use the shipped browser client against its actual configured conversationPath.
Checking only the canonical provider endpoint missed the portal compatibility
route and adapter forwarding for queue reconciliation. Both defects now have
an HTTP/browser contract regression.

Firefox BiDi acceptance did not expose the sent-delete confirmation through
WebDriver alert lookup. The final fixture records window.confirm calls and
returns approval, then verifies busy refusal and idle deletion. This checks the
confirmation text and deletion behavior but does not validate native dialog UI.

The isolated Codex 0.154.0 native startup interrupted its first turn even with a
single CODEX_HOME shared by App Server, CLI and TUI. The exact same conversation
subsequently read the attached file through an ordinary Send. Preserve this
observation alongside the existing history-lookup note; do not claim that
aligning metadata homes alone eliminates every startup interruption.

Related initiative: work/2026-09-12-portal-file-uploads/.

The real initiative's interrupted creation also blocked workspace-host switch.
Recover the exact goal from this conversation's own command history if its
temporary file was removed; verify its digest, preserve current tracking, restore
the original committed plan/state during dev-session start, and restore current
tracking afterward. The first exact retry timed out. After read-only history
lookups (about 43–45 seconds), a second exact retry succeeded through the normal
CLI and cleared the creation journal. No guard was bypassed or shared App Server
restarted. The timing evidence suggests expensive history scans; it does not
prove a cache-related cause. Keep the original startup goal as recovery evidence.
