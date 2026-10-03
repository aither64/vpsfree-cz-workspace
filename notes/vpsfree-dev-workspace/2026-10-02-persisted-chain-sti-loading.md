# Load persisted chain classes in every reader

ActiveRecord stores a transaction chain's subclass name in its `type` column.
A provider-defined chain therefore needs the same named class in every API,
supervisor and database-task process that reads those rows, including terminal
history. Defining it only when the producer first fires a chain leaves fresh
readers raising `ActiveRecord::SubclassNotFound`.

Keep one authoritative chain definition and load it during normal active and
retired profile initialization, after the API models load. Loading the class
must not fire provisioning work. Retiring enrollment still needs the class to
read existing history; do not add an unknown-type fallback.

Same-process specs can conceal this defect because the producer already defined
the constant. Add a fresh reader that uses the ordinary configuration loader
and reads real nonempty queued and terminal chain rows without invoking the
producer. An outer rollback fixture needs an explicit test-only visibility
arrangement for a second process; it must remain bound to the disposable test
database and must not change runtime isolation or commit fixture state.

The [storage-profile review](../../work/2026-09-23-storage-redesign/storage-profile-provider-review.md)
found this defect in its final provider series. Its narrow correction and
focused verification are recorded there; no VM or storage-payload result
follows from a class-loading regression.
