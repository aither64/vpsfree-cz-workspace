"""Prepare the actual browser regression's old-reader counterfactual source.

Run only after the final driver passes. No current project file is changed.
"""
import hashlib
import json
import pathlib
import subprocess
import tarfile
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "worktrees" / HERE.name / "dev-workspace"
BASE = "7ceb6b943c7fa6e6db2b42b1fc2d9732c6413e03"
READER = "portal/internal/agentteams/provenance.go"
CONTRACT = "portal/internal/agentteams/creation_journal_contract_test.go"


def git(*args):
    return subprocess.check_output(["git", "-C", str(SOURCE), *args])


assert git("status", "--porcelain") == b"", "commit the complete final source first"
head = git("rev-parse", "HEAD").decode().strip()
destination = pathlib.Path(tempfile.mkdtemp(prefix="session-creation-old-reader-"))
with tempfile.TemporaryFile() as archive:
    subprocess.run(["git", "-C", str(SOURCE), "archive", head], stdout=archive, check=True)
    archive.seek(0)
    with tarfile.open(fileobj=archive) as tree:
        tree.extractall(destination, filter="data")
reader = git("show", f"{BASE}:{READER}")
(destination / READER).write_bytes(reader)
# This new compile-time contract accesses the new exported Provider field. Its
# absence lets the old package compile and fail at the actual browser workflow,
# rather than claiming a compile failure establishes the user's regression.
(destination / CONTRACT).unlink()
receipt = {
    "schema": 1,
    "sourceHead": head,
    "oldReaderBase": BASE,
    "source": str(destination),
    "oldReaderSHA256": hashlib.sha256(reader).hexdigest(),
    "removedCompileOnlyContract": CONTRACT,
    "mutations": [READER, CONTRACT],
    "nativeChanged": False,
    "executed": False,
}
(HERE / "old-reader-source-final.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt))
