# Compare migration index metadata by value

Pinned ActiveRecord8.1.4 represents `IndexDefinition` as a class without value
`==`; the MySQL subclass adds `enabled` and also retains identity equality.
Two calls to `connection.indexes` return distinct objects. Comparing their
arrays with `eq` fails even when the printed definitions are identical.

A handoff migration preservation example encountered this after the owning
API102-example suite passed. The migration suite ran8 examples with one
failure at the index equality; the following foreign-key assertion had not
been reached in that example.

Compare explicit public index attributes before and after migration, including
MySQL `enabled`, using the same local projection. Keep the complete metadata,
index count/order and behavioral uniqueness checks. Avoid object-address or
reflection-based comparisons. `ForeignKeyDefinition` is a Struct with value
equality, so its existing comparison can stay intact.

Fresh migration verification passed all8 examples after this fixture
correction, retaining foreign-key metadata and actual DELETE refusal. No
migration or adapter behavior change followed from the failed object equality.

Related initiative: `work/2026-09-23-storage-redesign/state.md`.
