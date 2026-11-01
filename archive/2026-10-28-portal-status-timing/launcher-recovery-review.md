# Packaged launcher correction

Bounded final review of rollout.md delta 867320a0e..HEAD. Same Sol/xhigh reviewer;
general and risk lanes, unchanged scoped adapter architecture. The second live
attempt reached nested activation but failed its real check_codex: raw Ruby
adapter bypassed the installed shell runtime PATH, selecting ambient Python
without jsonschema. Original native still running, portal offline, no hook/copy/
publication. This is our launcher defect, not upstream package incompatibility.

New migration-host.sh preserves public wrapper environment exports and libexec
runtime PATH verbatim from exact selected package d0wikyzpr7. Only final dispatch
changes to bundled Ruby + adjacent migration-host.rb. Python runner and nested
system_env! route through it. Exact old/new read-only check-codex calls are admitted
by the adapter for preflight; no deployment checks are bypassed. Unit framework,
source revision/package, claim, journals, partition/inotify unchanged.

Quick: six adapter cases/21 assertions pass; real new-native protocol/schema/socket
check through the new shell launcher passed. Old-native actual check and all16
synthetic partition cases are also being collected before assignment. Source
hashes and shell/Ruby syntax/diff checks must match. Verify wrapper reconstruction
against both installed shell scripts and selected Ruby shebang directly.

After review a fresh utility will rehearse conversion using real source read-only:
rehearse-native-home.py calls existing inventory/partition functions, classifies
actual source objects and JSON headers, checksums/copies only portal rollouts to
private disposable /tmp state, splits every actual database for portal and stock,
then uses exact0.165 in that private home to cold-read every portal thread. No
production credentials, resume, turn, queue or live service mutation. It confirms
loaded-thread set empty and removes only its successful disposable directory.
On failure retain that exact owned evidence. This is a verification command,
not installed functionality; report source is available for context.

No app feature heads, pins, schemas or migrations changed. Earlier whole-branch
history/lineage remains. Shared executed operational commits cannot be rewritten.
Write launcher-recovery-review-result.md; no edits/live actions/delegation.
