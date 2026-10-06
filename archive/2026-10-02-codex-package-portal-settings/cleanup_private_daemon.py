"""Stop only updater processes belonging to one explicitly named private probe."""
import os
from pathlib import Path
import select
import signal
import sys

root = Path(sys.argv[1])
assert not root.is_symlink() and root.resolve().parent == Path("/tmp")
assert root.name.startswith("codex-package-daemon-") and root.stat().st_uid == os.getuid()
home = root / "home"
assert not home.is_symlink() and home.stat().st_uid == os.getuid()
package = home / "packages" / "app-server-daemon"
count = 0
for process in Path("/proc").iterdir():
    if not process.name.isdecimal():
        continue
    descriptor = None
    try:
        if process.stat().st_uid != os.getuid():
            continue
        executable = (process / "exe").resolve(strict=True)
        if not executable.is_relative_to(package):
            continue
        descriptor = os.pidfd_open(int(process.name))
        # Recheck after obtaining a race-safe handle; never signal a reused PID.
        if (process / "exe").resolve(strict=True) != executable:
            continue
        arguments = (process / "cmdline").read_bytes().rstrip(b"\0").split(b"\0")
        if arguments != [str(executable).encode(), b"app-server", b"daemon", b"pid-update-loop"]:
            continue
        assert process.stat().st_uid == os.getuid()
        environment = (process / "environ").read_bytes().split(b"\0")
        assert b"CODEX_HOME=" + str(home).encode() in environment
        assert b"CODEX_SQLITE_HOME=" + str(home).encode() in environment
        signal.pidfd_send_signal(descriptor, signal.SIGTERM)
        assert select.select([descriptor], [], [], 5)[0], "private updater did not exit"
        count += 1
        print("Stopped owned private updater PID", process.name)
    except (FileNotFoundError, ProcessLookupError):
        pass
    except PermissionError:
        # Unrelated same-UID processes can disable /proc inspection. Never
        # signal them; an inspection failure after matching our root is fatal.
        if descriptor is not None:
            raise
    finally:
        if descriptor is not None:
            os.close(descriptor)
print("Private updater cleanup:", count, "processes")
