# nodectld transaction recovery after a network interruption

## Symptom

After database connectivity returns, status reporting can remain healthy while
transactions are not polled. The watchdog correctly reports the daemon as
unresponsive because `last_transaction_check` is stale. Some affected daemons
do not exit on TERM and require SIGKILL.

## Cause

Status runs in a separate thread. Transaction polling is performed by the main
loop, which can remain inside `Db#connect` between its `Trying to connect` and
`Connected` messages. During the 2026-08-23 incident, this interval outlived
the configured mysql2 15-second timeouts on several nodes while other database
threads in the same process recovered.

The SIGKILL requirement supports a blocked native mysql2/MariaDB Connector/C
connect or initialization operation. The exact frame remains unconfirmed
because no thread dump was captured before termination.

## Fix and verification

Add diagnostics that capture all daemon thread stacks before watchdog restart,
and bound the whole reconnect/initialization operation with a mechanism that
does not depend solely on Connector/C timeouts. Test a database operation that
never returns and confirm deterministic recovery.

Related initiative: `work/2026-08-23-vpsadmin-supervisor-issue/`.
