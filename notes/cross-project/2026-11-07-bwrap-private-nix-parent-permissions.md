# Declare a traversable private /nix parent in namespace fixtures

A registered fixture inherited a restrictive service umask. Inside bubblewrap,
the automatically created `/nix` parent was mode 0700 even when `/nix/store`
and its Python files were readable. Root could execute Python, while a service
identity failed in the dynamic loader with a libpython permission error before
application import. Host path permissions were unchanged and were not the cause.

An isolated fork/drop/read/exec diagnostic exposed the private ancestor mode.
Setting the outer umask alone did not change bubblewrap's automatic parent.
The supported fixture repair explicitly created that sandbox-only parent with
`--perms 0755 --dir /nix` before the read-only `/nix/store` bind. The fixture also
set umask 022 for public scaffolding and asserted actual path modes before apps.
Service actors retained umask 0007; control, lock, inbox, credentials and private
key modes stayed explicitly restrictive. Never repair this by chmodding host
store paths, relaxing application identity checks or adding loader variables
without evidence.

The corrected fixed-command rehearsal passed in session
`2026-11-06-multilingual-blog-migration`; source and production permissions never
changed. Its evidence distinguishes setup failures from application probes.
