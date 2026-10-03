# ActiveRecord isolation assertions in MariaDB readers

ActiveRecord's MySQL adapter starts an isolated transaction with `SET
TRANSACTION ISOLATION LEVEL ...` and `BEGIN`. The unqualified setting applies
to the next transaction. MariaDB's `@@tx_isolation` exposes the session default,
so it can still report `REPEATABLE-READ` inside a READ COMMITTED transaction.
An assertion against that variable alone can reject a correctly configured
reader before reaching its actual visibility checks.

When a disposable test needs both a session-level assertion and READ COMMITTED
reads, set `SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED` on its verified,
distinct reader connection before starting the transaction. Disconnect that
owned adapter after transaction unwind so the session setting is not returned
to the pool for reuse. Keep the actual committed-row and lock-release checks;
the setting itself does not prove staging visibility.

This was observed in the storage-profile autocommit regression's first full-file
run (47 examples, 13 failures at the same isolation assertion). The runtime
correction was unchanged. See [MariaDB's SET TRANSACTION documentation](https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/set-commands/set-transaction)
and ActiveRecord 8.1.4's `begin_isolated_db_transaction` implementation.
