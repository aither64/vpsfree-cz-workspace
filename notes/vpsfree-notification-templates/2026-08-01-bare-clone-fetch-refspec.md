# Restore a missing bare-clone fetch refspec

Initiative: `work/2026-08-01-test-framework-ci`

The canonical `vpsfree-notification-templates` bare clone had no
`remote.origin.fetch` value. An explicit fetch created an
`origin/2026-06-15-vpsadmin-events` ref, but Git still refused to configure the
local branch's upstream because the remote did not declare any branch mapping.

Restore the standard bare-clone refspec before setting upstream tracking:

```sh
git --git-dir=repos/vpsfree-notification-templates.git config \
  remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'
```

After adding the mapping, upstream configuration succeeded and the local and
remote event branches both resolved to `6dda345a`.
