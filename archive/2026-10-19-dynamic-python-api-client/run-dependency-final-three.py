"""Complete only the three unrun post-review checks, once, with fresh CLI guards."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

SLUG = "2026-10-19-dynamic-python-api-client"
CLAIM = "342cd062-0205-45c7-b636-20d958b8fa75"
HEAD = "a8ea3132e7efe601aaa8965afe648459b3dab5c5"
TREE = "9a596258d912ca2075c36ded30d11b3984c656ae"
ROOT = Path("/home/aither/workspace/ai/vpsfree.cz")
CWD = ROOT / "worktrees" / SLUG / "haveapi"
# Invoke the stable user-profile entrypoint afresh for every guard. Never reuse
# a selected-package executable retained by a prior verification worker.
SESSION_CLI = "/home/aither/bin/dev-session"
OUTPUT = ROOT / "work" / SLUG / "verification/dependency-refresh/postreview-final-three"
LOCKS = {
    "Gemfile.lock": "450de01a459fd59f8237065094ee4bf59d1263049af14244a768b29b7f2ebfc5",
    "servers/ruby/Gemfile.lock": "9a67113645cceed6c4abf54a207d3cd8186f335e59c45b7b0161c840aacd4636",
    "clients/ruby/Gemfile.lock": "cf9311f2342ab2764b85a5092d47ff06a8567e6de17a03c8850a4d8f78e58b05",
    "clients/go/Gemfile.lock": "7fd2c67b745579cf39a9d9158d7cbe5503956b71c4237eff8ace3f028c98baf0",
}

# The workspace CLI uses its packaged Ruby, not project native gems. Every
# coordinator/head guard runs here, outside all child Nix development shells.
CLI_ENV = os.environ.copy()
for name in (
    "GEM_HOME", "GEM_PATH", "BUNDLE_GEMFILE", "BUNDLE_LOCKFILE", "BUNDLE_BIN_PATH", "BUNDLE_PATH",
    "BUNDLE_APP_CONFIG", "BUNDLER_VERSION", "BUNDLE_FROZEN", "RUBYOPT", "RUBYLIB",
):
    CLI_ENV.pop(name, None)

CHECK_ENV = CLI_ENV.copy()
CHECK_ENV.update({
    "BUNDLE_FROZEN": "true",
    "PYTHONDONTWRITEBYTECODE": "1",
    "DEV_WORKSPACE_CLAIM_ID": CLAIM,
})


def shell(selector, command):
    return ["nix", "develop", selector, "--command", "bash", "-euo", "pipefail", "-c", command]


CHECKS = [
    ("06-python-package", shell(".#client-python", "cd clients/python; uv run --locked python utils/package_smoke.py")),
    ("07-release-check", shell(".", "make release-check")),
    ("08-release-test", shell(".", "make release-test")),
]


def atomic(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def read(args):
    return subprocess.check_output(args, cwd=CWD, env=CLI_ENV, text=True).strip()


def guard():
    identity = [os.environ.get("DEV_SESSION_SLUG"), os.environ.get("DEV_SESSION_WORKSPACE")]
    assert all(value is None for value in identity) or identity == [SLUG, str(ROOT)]
    assert read([SESSION_CLI, "current"]) == SLUG
    claim = json.loads(read([
        SESSION_CLI, "coordination", "claim-status", SLUG, "--as-is",
        "--id", CLAIM, "--json",
    ]))
    assert claim["state"] == "held"
    assert claim["ownerId"] == "e51277e3-c4c3-43eb-b889-90e84d91b5bf"
    assert read(["git", "rev-parse", "HEAD"]) == HEAD
    assert read(["git", "rev-parse", "HEAD^{tree}"]) == TREE
    assert not read(["git", "--no-optional-locks", "status", "--porcelain"])
    assert read(["git", "config", "--local", "--get", "overcommit.configuration.verifySignatures"]) == "1"
    for name, expected in LOCKS.items():
        assert hashlib.sha256((CWD / name).read_bytes()).hexdigest() == expected, name
    for name in ("OVERCOMMIT_DISABLE", "OVERCOMMIT_DISABLED", "OVERCOMMIT_NO_VERIFY", "SKIP"):
        assert not os.environ.get(name), name


def main():
    guard()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    batch = OUTPUT / "batch.status.json"
    assert not batch.exists(), "Preserve earlier verification evidence; no automatic retries"
    started = time.monotonic()
    common = {"schema": 1, "head": HEAD, "tree": TREE, "claim": CLAIM, "pid": os.getpid(),
              "workspaceCli": SESSION_CLI,
              "workspaceCliSha256AtStart": hashlib.sha256(Path(SESSION_CLI).read_bytes()).hexdigest()}
    try:
        for label, command in CHECKS:
            guard()
            log = OUTPUT / (label + ".log")
            status = OUTPUT / (label + ".status.json")
            assert not log.exists() and not status.exists(), label
            step_started = time.monotonic()
            value = {
                **common, "check": label, "command": command, "cwd": str(CWD),
                "log": str(log), "startedAt": datetime.now(timezone.utc).isoformat(),
                "state": "running", "exitCode": None,
            }
            with log.open("x") as output:
                child = subprocess.Popen(command, cwd=CWD, env=CHECK_ENV,
                                         stdout=output, stderr=subprocess.STDOUT)
                value["childPid"] = child.pid
                atomic(status, value)
                atomic(batch, {**common, "state": "running", "check": label, "childPid": child.pid})
                try:
                    code = child.wait()
                except BaseException:
                    if child.poll() is None:
                        child.terminate()
                        child.wait()
                    raise
            value.update({"state": "passed" if code == 0 else "failed", "exitCode": code,
                          "elapsedSeconds": round(time.monotonic() - step_started, 3)})
            atomic(status, value)
            print(f"{label}: exit {code}", flush=True)
            if code != 0:
                atomic(batch, {**common, "state": "failed", "check": label,
                               "exitCode": code, "elapsedSeconds": round(time.monotonic() - started, 3)})
                return code if code > 0 else 1
        guard()
        atomic(batch, {**common, "state": "passed", "exitCode": 0,
                       "elapsedSeconds": round(time.monotonic() - started, 3)})
        return 0
    except BaseException as error:
        atomic(batch, {**common, "state": "interrupted" if isinstance(error, KeyboardInterrupt) else "failed",
                       "exitCode": 1, "error": str(error),
                       "elapsedSeconds": round(time.monotonic() - started, 3)})
        raise


if __name__ == "__main__":
    sys.exit(main())
