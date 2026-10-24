"""Exercise actual inline release gates with fake Git and registry responses."""
import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import urllib.error
from unittest.mock import patch

root = Path(__file__).resolve().parent
workflows = json.loads((root / "workflows.json").read_text())
release = next(v for k, v in workflows.items() if k.endswith("/release.yml"))
ci = next(v for k, v in workflows.items() if k.endswith("/ci.yml"))
validate = release["jobs"]["validate"]["steps"][1]["run"]
prerequisites = next(s["run"] for s in release["jobs"]["publish"]["steps"]
                     if s.get("name") == "Check first-publication prerequisites")
recheck = next(s["run"] for s in release["jobs"]["publish"]["steps"]
              if s.get("name") == "Recheck verified source and release tag")

def python_body(shell):
    assert shell.startswith("python3 - <<'PY'\n") and shell.endswith("\nPY\n")
    return compile(shell.split("\n", 1)[1].rsplit("\nPY\n", 1)[0], "<inline gate>", "exec")

validate_code = python_body(validate)
bootstrap_code = python_body(prerequisites)
revision = "a" * 40
checks = []

with tempfile.TemporaryDirectory(prefix="gates-", dir=root) as temporary:
    temporary = Path(temporary)
    original_directory = Path.cwd()
    os.chdir(temporary)
    try:
        def validation_case(name, *, environment=None, package="vpsadmin-client",
                            version="0.1.0", checked_out=revision, tag=revision,
                            fetch_error=False, expected_error=None):
            Path("Cargo.toml").write_text(
                f'[package]\nname = "{package}"\nversion = "{version}"\n')
            output = temporary / "output"
            output.write_text("")
            env = {
                "GITHUB_REPOSITORY": "vpsfreecz/vpsadmin-rust-client",
                "AUTHENTICATION": "oidc", "GITHUB_REF_TYPE": "tag",
                "GITHUB_REF": "refs/tags/v0.1.0", "GITHUB_SHA": revision,
                "GITHUB_OUTPUT": str(output), **(environment or {}),
            }
            def fetch(*args, **kwargs):
                if fetch_error:
                    raise subprocess.CalledProcessError(128, args[0])
                return subprocess.CompletedProcess(args[0], 0)
            with patch.dict(os.environ, env, clear=True), \
                 patch("subprocess.check_output", side_effect=[checked_out + "\n", tag + "\n"]), \
                 patch("subprocess.run", side_effect=fetch):
                try:
                    exec(validate_code, {})
                except (SystemExit, subprocess.CalledProcessError) as error:
                    assert expected_error and expected_error in str(error), (name, str(error))
                    assert output.read_text() == "", name
                else:
                    assert expected_error is None, name
                    assert output.read_text() == f"revision={revision}\n", name
            checks.append(name)

        validation_case("valid OIDC release")
        validation_case("valid explicit bootstrap", environment={"AUTHENTICATION": "bootstrap"})
        validation_case("fork rejected", environment={"GITHUB_REPOSITORY": "other/repo"},
                        expected_error="restricted")
        validation_case("unknown authentication rejected", environment={"AUTHENTICATION": "fallback"},
                        expected_error="Select oidc or bootstrap")
        validation_case("unexpected package rejected", package="other", expected_error="package name")
        validation_case("branch dispatch rejected", environment={"GITHUB_REF_TYPE": "branch"},
                        expected_error="Dispatch against")
        validation_case("wrong tag version rejected", version="0.2.0", expected_error="Dispatch against")
        validation_case("unprefixed tag rejected", environment={"GITHUB_REF": "refs/tags/0.1.0"},
                        expected_error="Dispatch against")
        validation_case("wrong source rejected", checked_out="b" * 40, expected_error="Checkout differs")
        validation_case("moved tag rejected", tag="b" * 40, expected_error="tag moved")
        validation_case("Git fetch failure rejected", fetch_error=True, expected_error="128")

        def bootstrap_case(name, *, configured="true", response=None, expected_error=None):
            response = contextlib.nullcontext() if response is None else response
            with patch.dict(os.environ, {"BOOTSTRAP_TOKEN_CONFIGURED": configured}, clear=True), \
                 patch("urllib.request.urlopen") as lookup:
                if isinstance(response, BaseException):
                    lookup.side_effect = response
                else:
                    lookup.return_value = response
                try:
                    exec(bootstrap_code, {})
                except SystemExit as error:
                    assert expected_error and expected_error in str(error), (name, str(error))
                else:
                    assert expected_error is None, name
                assert lookup.call_count == (0 if configured != "true" else 1), name
            checks.append(name)

        def http_error(code):
            return urllib.error.HTTPError("https://example.invalid", code, "test", {}, None)

        bootstrap_case("missing bootstrap secret rejected without lookup",
                       configured="false", expected_error="Missing release environment secret")
        bootstrap_case("crate404 permits bootstrap", response=http_error(404))
        bootstrap_case("existing crate rejected", expected_error="absent crate")
        for status in (401, 403, 429, 500):
            bootstrap_case(f"registry HTTP{status} rejected", response=http_error(status),
                           expected_error="lookup failed")
        bootstrap_case("registry network failure rejected", response=urllib.error.URLError("test"),
                       expected_error="lookup failed")
        bootstrap_case("registry timeout rejected", response=TimeoutError(),
                       expected_error="lookup failed")

        git = temporary / "git"
        git.write_text("""#!/usr/bin/env python3
import os, sys
if sys.argv[1] == 'rev-parse':
    print(os.environ['FAKE_HEAD'] if sys.argv[2] == 'HEAD' else os.environ['FAKE_TAG'])
elif sys.argv[1] == 'fetch':
    sys.exit(int(os.environ.get('FAKE_FETCH_STATUS', '0')))
else:
    sys.exit(99)
""")
        git.chmod(0o700)
        for name, head, tag, fetch, expected in [
            ("final unchanged tag accepted", revision, revision, "0", 0),
            ("final moved tag rejected", revision, "b" * 40, "0", 1),
            ("final checkout mismatch rejected", "b" * 40, revision, "0", 1),
            ("final fetch failure rejected", revision, revision, "128", 128),
        ]:
            env = {
                **os.environ, "PATH": str(temporary) + os.pathsep + os.environ["PATH"],
                "FAKE_HEAD": head, "FAKE_TAG": tag, "FAKE_FETCH_STATUS": fetch,
                "RELEASE_REVISION": revision, "GITHUB_REF": "refs/tags/v0.1.0",
            }
            result = subprocess.run(["bash", "-e", "-c", recheck], env=env, capture_output=True)
            assert result.returncode == expected, (name, result.returncode)
            checks.append(name)
    finally:
        os.chdir(original_directory)

shellcheck = "/nix/store/ixvpvkr2s92pbi6si1ki8yk3fs1gvlf2-shellcheck-0.11.0-bin/bin/shellcheck"
for filename, workflow in workflows.items():
    for job in workflow["jobs"].values():
        for step in job.get("steps", []):
            if "run" in step:
                subprocess.run(["bash", "-n"], input=step["run"], text=True, check=True)
                subprocess.run([shellcheck, "--shell=bash", "-"], input=step["run"],
                               text=True, check=True)
checks.append("all inline shell syntax and ShellCheck")

assert set(release["true"]) == {"workflow_dispatch"}
assert release["permissions"] == {"contents": "read"}
assert release["concurrency"]["cancel-in-progress"] is False
assert release["jobs"]["verify"] == {"needs": "validate", "uses": "./.github/workflows/ci.yml"}
assert ci["true"]["push"] == {"branches": ["**"]}
assert "workflow_call" in ci["true"]
publish = release["jobs"]["publish"]
assert publish["needs"] == ["validate", "verify"]
assert publish["environment"] == "release"
assert publish["permissions"] == {"contents": "read", "id-token": "write"}
for job_name, job in release["jobs"].items():
    if job_name != "publish":
        assert "id-token" not in job.get("permissions", {})
    for step in job.get("steps", []):
        if step.get("uses", "").startswith("actions/checkout@"):
            assert step["with"]["persist-credentials"] is False
        for variable, expression in step.get("env", {}).items():
            if ("secrets." in str(expression) and variable != "BOOTSTRAP_TOKEN_CONFIGURED") \
                    or "steps.registry.outputs.token" in str(expression):
                assert step.get("run") == "nix develop --command cargo publish --locked"
checks.append("dispatch, reuse, permissions and credential boundaries")
print(json.dumps({"passed": len(checks), "checks": checks}, indent=2))
