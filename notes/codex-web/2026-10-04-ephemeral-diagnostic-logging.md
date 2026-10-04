# Native ephemeral threads still enter diagnostic logging

Initiative: `work/2026-10-03-automatic-session-slugs/`.
Inspected native source: pinned Codex 0.160.0.

The isolation fixture found a synthetic utility prompt marker in SQLite after
ephemeral inference. Its original log did not identify the file or table;
bounded owner diagnostics were added rather than exempting a database.
The subsequent actual run at4651d764 identified `logs_2.sqlite`, table `logs`,
with both prompt and owned-identity markers. Counts saturated the64-statement
diagnostic bound; no rows or prompt bytes were emitted.

`core/src/session/session.rs:1008,1112` omits normal live-thread persistence and
the session state handle for ephemeral threads. This does not suppress the
process logger: `core/src/session/handlers.rs:427-432` records the submitted
operation's debug fields, including input text, without an ephemeral filter.
`app-server/src/lib.rs:735-746` installs the SQLite layer with the independent
TRACE default in `state/src/log_db.rs:61-88`. Its formatted event body is inserted
into `logs` in `logs_2.sqlite`. The sink batches up to512 records or ten seconds,
so an immediate absence check cannot establish that a prompt will never persist.

`RUST_LOG` controls a separate stderr filter. History, feedback and OTEL
preferences are not per-call suppression for this SQLite layer. No supported
per-call switch was found in the inspected source. Do not equate ephemeral
history behavior with absence from daemon diagnostic logs, erase rows after a
call, or shorten observation to hide batching.

The requested naming feature's diagnostic-logging preference is pending. No
persistence assertion has been relaxed and no native isolation or deployment
pass is claimed. Record any accepted logging boundary in provider and consumer
documentation and review it before release.
