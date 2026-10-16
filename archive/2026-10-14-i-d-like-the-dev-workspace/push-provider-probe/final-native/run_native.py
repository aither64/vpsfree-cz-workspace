"""Own one Xvfb process and one native provider fixture run; no retries."""

import datetime
import json
import os
from pathlib import Path
import select
import signal
import subprocess
import sys


def timestamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat() + "\n"


def main():
    executable_file, run_directory, portal_directory = map(Path, sys.argv[1:])
    xvfb = None
    test = None
    read_fd = None
    write_fd = None
    status = 2
    evidence = {"headless": False, "displayAllocated": False, "xvfbStarted": False,
                "xvfbReaped": False, "testStarted": False}
    (run_directory / "started-at").write_text(timestamp())

    def interrupted(signum, _frame):
        raise InterruptedError(signum)

    signal.signal(signal.SIGINT, interrupted)
    signal.signal(signal.SIGTERM, interrupted)
    try:
        executable = executable_file.read_text().strip()
        if not executable.startswith("/nix/store/") or not Path(executable).is_absolute() or not os.access(executable, os.X_OK):
            raise ValueError("Xvfb executable unavailable")
        read_fd, write_fd = os.pipe()
        with (run_directory / "xvfb.log").open("wb") as log:
            xvfb = subprocess.Popen(
                [executable, "-displayfd", str(write_fd), "-screen", "0", "1280x900x24", "-nolisten", "tcp", "-noreset"],
                pass_fds=(write_fd,), stdout=log, stderr=subprocess.STDOUT,
            )
        evidence["xvfbStarted"] = True
        (run_directory / "xvfb.pid").write_text(str(xvfb.pid) + "\n")
        os.close(write_fd)
        write_fd = None
        # This deadline bounds X display startup, not the browser/provider test.
        if not select.select([read_fd], [], [], 15)[0]:
            evidence["stage"] = "display_startup_timeout"
            raise ValueError("Xvfb display unavailable")
        display = os.read(read_fd, 32).strip()
        if not display.isdigit() or len(display) > 5 or xvfb.poll() is not None:
            evidence["stage"] = "display_startup_failed"
            raise ValueError("Xvfb display unavailable")
        os.close(read_fd)
        read_fd = None
        environment = os.environ.copy()
        environment["DISPLAY"] = ":" + display.decode("ascii")
        evidence["displayAllocated"] = True
        with (run_directory / "go-test.log").open("wb") as log:
            test = subprocess.Popen(
                ["go", "test", "-mod=readonly", "./internal/web", "-run", "^TestNotificationProviderProbe$", "-count=1", "-v"],
                cwd=portal_directory, env=environment, stdout=log, stderr=subprocess.STDOUT,
            )
            evidence["testStarted"] = True
            status = test.wait()
            evidence["testExitStatus"] = status
            (run_directory / "go-test.status").write_text(str(status) + "\n")
        evidence["stage"] = "test_completed"
    except InterruptedError:
        evidence["stage"] = "interrupted"
        status = 130
    except Exception:
        # Paths/exception strings are deliberately excluded from diagnostics.
        evidence.setdefault("stage", "runner_incomplete")
        status = 2
    finally:
        # Popen retains child ownership. Never discover, signal or enumerate a
        # foreign display/process, and never use a broad process-name kill.
        for child, label in ((test, "test"), (xvfb, "xvfb")):
            if child is None:
                continue
            try:
                if child.poll() is None:
                    child.terminate()
                    try:
                        child.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        child.kill()
                        child.wait()
                evidence[label + "Reaped"] = True
                evidence[label + "ProcessExitStatus"] = child.returncode
            except Exception:
                evidence[label + "Reaped"] = False
                if status == 0:
                    status = 2
        for fd in (read_fd, write_fd):
            if fd is not None:
                os.close(fd)
        (run_directory / "runner-summary.json").write_text(json.dumps(evidence, indent=2) + "\n")
        (run_directory / "status").write_text(str(status) + "\n")
        (run_directory / "finished-at").write_text(timestamp())
    log = run_directory / "go-test.log"
    if log.exists():
        sys.stdout.write(log.read_text())
    print(json.dumps(evidence))
    return status if status >= 0 else 128 - status


if __name__ == "__main__":
    raise SystemExit(main())
