# Prepared retained-builder inspection

Read-only package diagnosis for failed head
`fe9182dd2fb1ba627c30d54c39c1acd7b140df69`; no source edits or rebuild.
Lead assigns a fresh watcher. Preserve existing failure logs. Capture this
debug transcript as `bootstrap-builder-inspection.log` in the session.

Run from the session's vpsadminos worktree:

```sh
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-image image-scripts/test@opensuse-leap-16.1
```

In the existing Ruby REPL, inspect the exact builder ID recorded by the failed
run. Starting its retained container is only to read its existing package state;
do not install/refresh/download packages or invoke another image build.

```ruby
require "shellwords"
machine.wait_for_osctl_pool("tank")
machine.succeeds("osctl ct ls -H -o id,distribution,version,state")
_, builder_state = machine.succeeds("osctl ct show -H -o state builder-98c1959d")
machine.succeeds("osctl ct start builder-98c1959d") unless builder_state.strip == "running"
machine.all_succeed(
  "osctl ct exec builder-98c1959d cat /etc/os-release",
  "osctl ct exec builder-98c1959d rpm --version",
  "osctl ct exec builder-98c1959d zypper --version",
  "osctl ct exec builder-98c1959d rpm -q rpm zypper libzypp"
)
lua_query = '%{lua: print("global_exec=" .. type(exec)); print("rpm_execute=" .. type(rpm.execute)); print("posix_exec=" .. type(posix and posix.exec))}'
machine.succeeds("osctl ct exec builder-98c1959d rpm --eval #{Shellwords.escape(lua_query)}")
```

Report this version/API output promptly; it can independently establish the
scriptlet incompatibility before cached-file inspection completes.
Then inspect only surviving cached copies of the exact failing package versions:

```ruby
cached_rpm_inspection = <<~'SH'
  for cache_root in /var/cache/zypp /build; do
    [ -d "$cache_root" ] || continue
    find "$cache_root" -maxdepth 8 -type f \( \
      -name 'glibc-2.40-160100.3.1.x86_64.rpm' -o \
      -name 'systemd-257.13-160100.3.5.x86_64.rpm' -o \
      -name 'libgio-2_0-0-2.84.4-160100.3.1.x86_64.rpm' -o \
      -name 'gio-branding-openSUSE-42.1-lp161.2.2.noarch.rpm' \
    \) -exec sh -c '
      for candidate_rpm do
        printf "\nPACKAGE %s\n" "$candidate_rpm"
        sha256sum "$candidate_rpm"
        rpm -qp --scripts "$candidate_rpm"
        rpm -qp --triggers "$candidate_rpm"
        rpm -qp --dump "$candidate_rpm" | awk "/gio-2.0|mimeapps|cache|ldconfig/"
      done
    ' sh {} +
  done
SH
machine.succeeds("osctl ct exec builder-98c1959d sh -c #{Shellwords.escape(cached_rpm_inspection)}", timeout: 120)
exit
```

No `PACKAGE` output means no matching surviving cache, not a new transaction
failure. The failed build's cleanup destroyed its work/output datasets, including
the `--root` install tree and any cache there; do not recreate those just to
collect evidence. If the exact retained builder is absent, report that gap and
stop rather than creating a replacement. Native debug exit handles the VM.
