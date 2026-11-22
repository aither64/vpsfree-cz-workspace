# Lifecycle cgroup resource paths are relative

Related initiative: `work/2026-07-24-ct-start-hang`

The `osctld/lifecycle` VM's downgrade/re-upgrade example failed while reading
an adopted cgroup resource even though osctld logged a successful write.

Lifecycle `resources` values such as `cgroup_root` and `lxc_payload` are
relative to the cgroup mount and begin with `osctl/...`; they do not begin with
`/`. Concatenating them as `/sys/fs/cgroup#{resource}` produces the malformed
path `/sys/fs/cgrouposctl/...`.

Build an absolute cgroup-v2 path as `/sys/fs/cgroup/#{resource}`. For
cgroup-v1, select the controller mount first and append the resource with the
same explicit separator.

The corrected `osctld/lifecycle` suite passed all four examples in 444.39
seconds.
