# Review probes and joined RSpec transactions

The API spec helper wraps each ordinary example in a transaction that is rolled
back afterward. An application `Model.transaction` normally joins that outer
transaction. If application code rescues an inner persistence exception, a
probe cannot assume that all earlier inner writes were independently rolled
back before the outer example ends.

A password-recovery review probe correctly reproduced an oversized User-Agent
as `ActiveRecord::ValueTooLong` and HTTP422, but an additional assertion that the
preceding challenge survived failed under this wrapper. Removed that unrelated
assertion and reran only the boundary being investigated; the original error
was reproduced. If transaction rollback itself is the subject, use the
repository's `:no_transaction` convention with isolated fixtures and cleanup
so the application owns the real transaction boundary.

Related: `work/2026-08-18-vpsadmin-password-reset/review-2026-09-13/`.
