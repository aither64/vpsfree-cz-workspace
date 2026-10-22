"""Execute the lead-authorized HaveAPI fast-forward, retaining native evidence."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path("/home/aither/workspace/ai/vpsfree.cz")
SLUG = "2026-10-19-dynamic-python-api-client"
FEATURE = ROOT / "worktrees" / SLUG / "haveapi"
TARGET = ROOT / "worktrees" / SLUG / "haveapi-dependency-merge-target"
OUTPUT = ROOT / "work" / SLUG / "verification/dependency-refresh/native-merge"
BASE = "c1823f3d70365b0442d0e2171bdf83bd4c6dbe31"
HEAD = "a8ea3132e7efe601aaa8965afe648459b3dab5c5"
TREE = "9a596258d912ca2075c36ded30d11b3984c656ae"
CLAIM = "d58eb8f6-0789-4ad6-829d-b6bd7927cc91"
REMOTE = "git@github.com:vpsfreecz/haveapi.git"
STASH = "bd8d94b3b6f40a60a18aa4b30c03193459890495"
CLI_ENV = os.environ.copy()
for variable in (
    "GEM_HOME", "GEM_PATH", "BUNDLE_GEMFILE", "BUNDLE_LOCKFILE", "BUNDLE_BIN_PATH",
    "BUNDLE_PATH", "BUNDLE_APP_CONFIG", "BUNDLER_VERSION", "BUNDLE_FROZEN", "RUBYOPT", "RUBYLIB",
):
    CLI_ENV.pop(variable, None)


def read(args, cwd=FEATURE, env=None):
    return subprocess.check_output(args, cwd=cwd, env=env, text=True).strip()


def refs():
    return dict(line.split(" ", 1) for line in read([
        "git", "for-each-ref", "--format=%(refname) %(objectname)",
    ]).splitlines())


def guard(local_master):
    identity = [os.environ.get("DEV_SESSION_SLUG"), os.environ.get("DEV_SESSION_WORKSPACE")]
    assert identity == [SLUG, str(ROOT)] or identity == [None, None], identity
    assert read(["/home/aither/bin/dev-session", "current"], env=CLI_ENV) == SLUG
    claim = json.loads(read([
        "/home/aither/bin/dev-session", "coordination", "claim-status", SLUG,
        "--as-is", "--id", CLAIM, "--json",
    ], env=CLI_ENV))
    assert claim["state"] == "held" and claim["revision"] == 2
    assert claim["ownerId"] == "e51277e3-c4c3-43eb-b889-90e84d91b5bf"
    assert read(["git", "rev-parse", "HEAD"]) == HEAD
    assert read(["git", "rev-parse", "HEAD^{tree}"]) == TREE
    assert read(["git", "symbolic-ref", "--short", "HEAD"]) == SLUG
    assert read(["git", "rev-parse", "refs/heads/master"]) == local_master
    assert not read(["git", "--no-optional-locks", "status", "--porcelain"])
    assert read(["git", "remote", "get-url", "--all", "origin"]) == REMOTE
    assert read(["git", "remote", "get-url", "--push", "--all", "origin"]) == REMOTE
    assert read(["git", "config", "--local", "--get", "overcommit.configuration.verifySignatures"]) == "1"
    for variable in ("OVERCOMMIT_DISABLE", "OVERCOMMIT_DISABLED", "OVERCOMMIT_NO_VERIFY", "SKIP"):
        assert not os.environ.get(variable), variable
    return claim


def remote_refs(expected_master):
    values = {line.split()[1]: line.split()[0] for line in read([
        "git", "ls-remote", "--heads", "origin", "refs/heads/master", "refs/heads/" + SLUG,
    ]).splitlines()}
    assert values == {"refs/heads/master": expected_master, "refs/heads/" + SLUG: HEAD}, values
    return values


def hook(name):
    value = Path(read(["git", "rev-parse", "--git-path", "hooks/" + name], cwd=TARGET))
    return value if value.is_absolute() else TARGET / value


def target_clean(expected):
    assert read(["git", "symbolic-ref", "--short", "HEAD"], cwd=TARGET) == "master"
    assert read(["git", "rev-parse", "HEAD"], cwd=TARGET) == expected
    assert not read(["git", "--no-optional-locks", "status", "--porcelain"], cwd=TARGET)


def main():
    record = {"base": BASE, "head": HEAD, "tree": TREE, "claim": CLAIM,
              "target": str(TARGET), "commands": [], "state": "running"}
    log_path = OUTPUT / "commands.log"
    result_path = OUTPUT / "result.json"
    assert not result_path.exists()
    with log_path.open("x") as log:
        def run(args, cwd=FEATURE, input=None):
            item = {"argv": [str(arg) for arg in args], "cwd": str(cwd),
                    "startedAt": datetime.now(timezone.utc).isoformat()}
            if input is not None:
                item["stdin"] = input
            log.write(json.dumps(item) + "\n")
            log.flush()
            process = subprocess.run(args, cwd=cwd, input=input, text=True,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            item["exitCode"] = process.returncode
            record["commands"].append(item)
            log.write(process.stdout + f"\nEXIT {process.returncode}\n")
            log.flush()
            print(json.dumps(item), flush=True)
            if process.stdout:
                print(process.stdout, flush=True)
            process.check_returncode()

        try:
            record["initialClaim"] = guard(BASE)
            remote_refs(BASE)
            assert not TARGET.exists()
            assert str(TARGET) not in read(["git", "worktree", "list", "--porcelain"])
            assert read(["git", "merge-base", BASE, HEAD]) == BASE
            before = refs()
            assert read(["git", "cat-file", "-t", STASH]) == "commit"
            preflight = json.loads((OUTPUT / "preflight.json").read_text())
            for filename, digest in preflight["unchangedHistoricalAndFinalHookHashes"].items():
                assert hashlib.sha256((FEATURE / filename).read_bytes()).hexdigest() == digest
            locks = {name: hashlib.sha256((FEATURE / name).read_bytes()).hexdigest()
                     for name in ("Gemfile.lock", "servers/ruby/Gemfile.lock", "clients/ruby/Gemfile.lock", "clients/go/Gemfile.lock")}
            run(["ruby", "--version"])
            run(["git", "worktree", "add", str(TARGET), "master"])
            target_clean(BASE)
            for filename, digest in preflight["unchangedHistoricalAndFinalHookHashes"].items():
                assert hashlib.sha256((TARGET / filename).read_bytes()).hexdigest() == digest
            run([str(hook("post-checkout")), BASE, BASE, "1"], cwd=TARGET)
            guard(BASE)
            remote_refs(BASE)
            run(["git", "merge", "--ff-only", HEAD], cwd=TARGET)
            run([str(hook("post-merge")), "0"], cwd=TARGET)
            target_clean(HEAD)
            assert read(["git", "rev-parse", "HEAD^{tree}"], cwd=TARGET) == TREE
            guard(HEAD)
            remote_refs(BASE)
            update = f"refs/heads/master {HEAD} refs/heads/master {BASE}\n"
            run([str(hook("pre-push")), "origin", REMOTE], cwd=TARGET, input=update)
            run(["git", "push", "origin", "refs/heads/master:refs/heads/master"], cwd=TARGET)
            record["remoteRefsAfter"] = remote_refs(HEAD)
            guard(HEAD)
            target_clean(HEAD)
            assert read(["git", "rev-parse", "@{upstream}"]) == HEAD
            assert read(["git", "cat-file", "-t", STASH]) == "commit"
            after = refs()
            expected = dict(before)
            expected["refs/heads/master"] = HEAD
            expected["refs/remotes/origin/master"] = HEAD
            assert after == expected, "Unexpected ref delta"
            for name, digest in locks.items():
                assert hashlib.sha256((FEATURE / name).read_bytes()).hexdigest() == digest, name
            guard(HEAD)
            run(["git", "worktree", "remove", str(TARGET)])
            assert not TARGET.exists()
            assert str(TARGET) not in read(["git", "worktree", "list", "--porcelain"])
            assert refs() == after
            guard(HEAD)
            record.update({"state": "passed", "targetRemoved": True, "worktreeAndIndexClean": True,
                           "ordinaryHookProof": "checkout/post-merge/pre-push explicit invocations exited0; native merge/push also exited0",
                           "preservedStashObject": STASH, "preservedOtherRefs": True,
                           "allCommandHandlesCompleted": True})
        except BaseException as error:
            record.update({"state": "failed", "error": str(error), "targetExists": TARGET.exists()})
            raise
        finally:
            with result_path.open("x") as output:
                json.dump(record, output, indent=2)
                output.write("\n")


if __name__ == "__main__":
    main()
