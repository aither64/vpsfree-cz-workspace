"""Private per-database online baseline; deliberately not a global snapshot."""
import datetime
import hashlib
import json
import os
import pathlib
import shutil
import sqlite3
import sys
import tempfile
import time

os.umask(0o077)
source = pathlib.Path(sys.argv[1]).resolve(strict=True)
parent = pathlib.Path(sys.argv[2])
parent.mkdir(parents=True, exist_ok=True, mode=0o700)
if parent.stat().st_uid != os.getuid() or parent.stat().st_mode & 0o077:
    raise SystemExit("backup parent must be private and owned by this user")
paths = sorted(source.glob("*.sqlite"))
required = {"state_5.sqlite", "queue_1.sqlite", "thread_history_1.sqlite"}
if not required <= {path.name for path in paths}:
    raise SystemExit("expected stores missing; resolve SQLite home before proceeding")
if any(path.is_symlink() or not path.is_file() for path in paths):
    raise SystemExit("resolve non-regular SQLite paths before proceeding")
estimate = sum(path.stat().st_size for path in paths)
estimate += sum(path.stat().st_size for path in source.glob("*.sqlite-wal"))
if shutil.disk_usage(parent).free < 2 * estimate + 1024**3:
    raise SystemExit("insufficient backup space with safety margin")
destination = pathlib.Path(tempfile.mkdtemp(prefix="online-", dir=parent))


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


record = {"kind": "per-database-online-baseline", "global_snapshot": False,
          "sqlite_version": sqlite3.sqlite_version, "started_at": utc(), "files": []}
for path in paths:
    item = {"name": path.name, "started_at": utc()}
    output = destination / path.name
    deadline = time.monotonic() + 180

    def progress(status, remaining, total):
        if time.monotonic() > deadline:
            raise TimeoutError("database backup exceeded its time budget")

    src = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True, timeout=5)
    dst = sqlite3.connect(output)
    try:
        src.backup(dst, pages=256, progress=progress, sleep=0.05)
        dst.execute("PRAGMA journal_mode=DELETE")
        if dst.execute("PRAGMA integrity_check").fetchall() != [("ok",)]:
            raise RuntimeError("backup integrity check failed")
    finally:
        dst.close()
        src.close()
    with output.open("rb") as saved:
        digest = hashlib.file_digest(saved, "sha256").hexdigest()
        os.fsync(saved.fileno())
    item.update(finished_at=utc(), bytes=output.stat().st_size, sha256=digest, integrity="ok")
    record["files"].append(item)
if [path.name for path in sorted(source.glob("*.sqlite"))] != [path.name for path in paths]:
    raise RuntimeError("database inventory changed; baseline is incomplete")
record["finished_at"] = utc()
with (destination / "complete.json").open("x") as manifest:
    json.dump(record, manifest, indent=2)
    manifest.write("\n")
    manifest.flush()
    os.fsync(manifest.fileno())
directory_fd = os.open(destination, os.O_RDONLY | os.O_DIRECTORY)
try:
    os.fsync(directory_fd)
finally:
    os.close(directory_fd)
print("Private SQLite baseline complete:", destination)
