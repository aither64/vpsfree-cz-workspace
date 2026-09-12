# Retain temporary acceptance closures during concurrent GC

Related initiative: work/2026-09-12-portal-review-experience.

A browser bundle built with nix build --no-link disappeared between acceptance
commands while another process ran nix-collect-garbage. The Python executable
returned No such file or directory. Merely recording a store path or pointing
a fixture's ordinary profile symlink at it does not keep the closure alive.

Use a temporary nix build --out-link for browser tools and registered indirect
GC roots (`nix-store --add-root PATH --indirect --realise STORE_PATH`) for
acceptance/delivery packages. Keep them until all fixture processes and
rollback tests finish, then remove only these task-owned roots. Do not stop
another session's garbage collection.
