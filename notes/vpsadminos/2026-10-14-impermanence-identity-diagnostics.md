# Distinguish preserved identity from repeated fresh allocation

An impermanence guest can appear to preserve an allocated system UID/GID after
restart merely because fresh allocation repeats the same order. In the container
import initiative, an earlier-sorting declarative system account changed that
order. All three hosted impermanence variants then failed the original UID
expectation after restart, including the unchanged explicit unstable path.
Fixed IDs or resetting expectations would conceal this failure.

Keep the original numeric IDs and known payload ownership. Collect machine-id,
UID, GID, contents and numeric ownership independently before aggregate failure;
one changed UID must not hide later results. Record both visible and persistent
allocation maps, backing inode/device/ownership, effective mounts and activation
snippet boundaries plus the actual mount-script source invocation.

The source contains two early-mount paths. LXC's pre-mounted proc can skip the
stage-2 path, but activation also sources mounts in specialfs. Its ordering
relative to legacy users matters. Impermanence creates backing directories
after users/groups, so simply placing specialfs first also has a fresh-source
precondition. Static proc-guard evidence alone does not prove runtime map
visibility. Preserve numeric/mount evidence before widening a product fix.

The diagnostic improvement is implemented and checked; the proposed raw-file
prerequisite remains unaccepted and unverified. No identity repair or complete
persistence pass is claimed. Evidence and exact scope decisions belong to
`work/2026-10-12-streamline-vpsadminos-config-imports/`.
