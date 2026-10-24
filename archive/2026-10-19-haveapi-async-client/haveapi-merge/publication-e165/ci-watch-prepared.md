# Prepared exact e165 CI observation — not launched

Wait for separate lead release and sole utility slot. One fresh retained-catalog
Luna/low/full_access watcher observes these exact workflow IDs at exact SHA
e16526d42949bae96bf35e8db6cd984d739dcc2a in vpsfreecz/haveapi:

- release 39500061560 (in progress at discovery)
- RuboCop 39500061611 (success)
- JavaScript 39500061644 (success)
- Python 39500061516 (success)
- Ruby 39500061650 (success)
- i18n 39500061639 (success)

Use normal declared HaveAPI tools. Observe fixed IDs, not moving branch/latest.
Known pending wait command: gh run watch 39500061560 --repo vpsfreecz/haveapi
--exit-status. Save each complete
run/job conclusion using gh api repos/vpsfreecz/haveapi/actions/runs/ID and
/actions/runs/ID/jobs?per_page=100. Preserve actual workflow boundaries; release
push run builds only and grants no registry publication authorization.

Keep raw logs/status, exact command exits and elapsed time under a fresh owned
/tmp/2026-10-19-haveapi-async-client-e165-ci.* directory. On failure retain failed
job logs/artifact metadata and report first evidence; watcher does not diagnose
or retry. No manual dispatch, rerun, source/Git/ref/hook changes, other branch
cancellation, master integration, registry publication, version/tag, WebUI,
runtime/deployment/lifecycle action or nested watcher. No quiet timeout.
Watcher owns observation to explicit exit and releases sole utility when done.
