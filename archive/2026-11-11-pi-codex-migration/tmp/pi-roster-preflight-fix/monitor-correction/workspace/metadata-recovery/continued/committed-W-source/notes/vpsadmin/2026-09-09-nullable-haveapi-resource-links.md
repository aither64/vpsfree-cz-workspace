# Nullable HaveAPI PHP resource links

Reading `$item->release_chain` can resolve the association through Show even
when its API value is null, causing unresolved path arguments. ResourceInstance
provides `<association>_id` specifically for reading IDs without resolution.
Use `$item->release_chain_id` (and equivalent nullable IDs) for guards and links.
This fixed IP campaign address rendering before any release chain existed.
The browser error context exposed the missing row and the transaction Show error;
no HaveAPI client change is needed.
Scalar attributes still work with null coalescing: a direct PHP check confirms
that __get returning false preserves false with `??`, even without __isset.
The association-resolution issue does not justify changing scalar reads.
Related initiative: work/2026-09-09-ip-release-mechanism.
