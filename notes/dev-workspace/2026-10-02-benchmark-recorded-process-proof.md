# Scope fixture process checks to recorded ownership

A guarded continuation of an isolated benchmark refused before any writes
because an all-`/proc` scan could not read cwd for the same-UID systemd user
manager and PAM helper. Same UID does not make a process part of the fixture,
and unrelated process metadata permissions vary between execution environments.

For this exact pre-registration failure, the only launched subprocess was the
recorded seed server. Require its recorded PID to be absent, refuse a reused or
ambiguous PID, and retain private socket and strict inventory checks excluding
registration, runtime and creation records. The known stopped sequence and its
preserved diagnostics establish the narrow continuation boundary. Do not clear
locks, infer another process's ownership, or escalate permissions to inspect
unrelated services.

Removing the global enumeration left all original acceptance gates intact.
The parent read-only preflight then passed against 3,379 real private histories
in9.447s. Actual benchmark measurements remained a separate next operation.

Related initiative: `work/2026-10-02-portal-creation-performance/`.
