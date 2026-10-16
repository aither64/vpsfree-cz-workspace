"""Static-only checks. Does not execute fixture, collector, Nix or product code."""
import ast
import difflib
import hashlib
import json
from pathlib import Path
import re
import textwrap

HERE = Path(__file__).resolve().parent
original = (HERE / "original-session-recovery-boot.nix").read_text()
fixture = (HERE / "session-recovery-diagnostic.nix").read_text()
wrapper = (HERE / "flake.nix").read_text()
assert "mkPackage" not in wrapper
assert "self = runtime;" in wrapper
assert "runtime.packages.${system}.dev-workspace" in wrapper
assert "import runtime.inputs.nixpkgs" in wrapper
assert "assert toString devWorkspace == expectedProduct;" in wrapper
assert wrapper.count("checks.${system}.") == 2  # one exposed diagnostic + original identity
assert "checks.${system}.session-recovery-diagnostic = diagnostic;" in wrapper

old_nodes = json.loads((HERE / "original-runtime.lock.json").read_text())["nodes"]
new_nodes = json.loads((HERE / "flake.lock").read_text())["nodes"]
original_store = Path("/nix/store/fpqzq6vs24m668g5fnddmhc0110vw248-source")
assert (original_store / "nix/tests/session-recovery-boot.nix").read_text() == original
assert (original_store / "flake.lock").read_bytes() == (HERE / "original-runtime.lock.json").read_bytes()
assert new_nodes["runtime"]["locked"]["rev"] == "b8a6be26a75347dcc9ec0fd1330dff886e47c93f"
for name, old in old_nodes.items():
    new = new_nodes["runtime" if name == "root" else name]
    if name != "root":
        assert new.get("locked") == old.get("locked"), name
        assert new.get("original") == old.get("original"), name
    for key, value in old.get("inputs", {}).items():
        expected = ["runtime"] + value if isinstance(value, list) else value
        assert new["inputs"][key] == expected, (name, key)

# Node configuration and synthetic provider unchanged except explicit closure paths.
old_node = original.split("  nodes.machine = ", 1)[1].split("  testScript = ", 1)[0]
new_node = fixture.split("  nodes.machine = ", 1)[1].split("  testScript = ", 1)[0]
assert new_node == old_node.replace("[ devWorkspace ];", "[ devWorkspace probe collector ];")
setup_end = '    state_path = '
old_setup = original.split("  testScript = ''\n", 1)[1].split(setup_end, 1)[0]
new_setup = fixture.split("  testScript = ''\n", 1)[1].split(setup_end, 1)[0]
assert new_setup.replace("    import re\n", "") == old_setup
for line in [
    "subprocess.Popen(['sleep','300']",
    'provider request fixture pool aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa',
    '"/sys/fs/cgroup" + group + "/cgroup.procs"',
    "d['operation']['phase']=='waiting' and d['operation']['blockers']",
    'machine.succeed("kill " + foreign_pid)',
    'assert wait_phase("applied")["active"] == "pool"',
]:
    assert line in fixture, line
assert fixture.count('with subtest(') == 2
assert 'pooltwo bbbbbbbb' not in fixture
assert 'machine.reboot()' not in fixture
assert 'RestartSec=' not in fixture and 'KillMode=' not in fixture
assert 'systemctl --user set-environment' not in fixture
assert "Environment=RUBYOPT=-r${probe}" in fixture
assert "tail -c 65536" in fixture
assert 'DIAGNOSTIC_UNEXPECTED_TERMINAL' in fixture
assert 'DIAGNOSTIC_OBSERVER_RESULT=' in fixture
assert 'missing-active-inconclusive' in fixture
assert 'observed-no-raises' in fixture
assert 'except Exception:\n        collect_diagnostics()\n        raise' in fixture

# Compile Python after harmless interpolation replacement, never invoke its code.
driver = fixture.split("  testScript = ''\n", 1)[1].rsplit("  '';", 1)[0]
driver = re.sub(r"\$\{[^}]+\}", "/synthetic-store/path", driver)
driver = textwrap.dedent(driver)
compile(driver, "diagnostic-testScript", "exec")
collector = (HERE / "collect-metadata.py").read_text()
compile(collector, "collect-metadata.py", "exec")
compile((HERE / "summarize-run.py").read_text(), "summarize-run.py", "exec")
tree = ast.parse(driver)
wait = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "wait_phase")
assert any(isinstance(node, ast.Assert) for node in wait.body)
assert "os.O_NOFOLLOW" in collector and "os.O_NONBLOCK" in collector
assert 'info.st_uid != 1000' in collector
assert 'op.get("snapshot") == BASE + snapshot_name' in collector
assert 'snapshot.get("workspace") == ROOT' in collector
assert 'terminals.get("socket") == SOCKET' in collector
assert 'subprocess' not in collector
assert 'print(json.dumps(result,' in collector

diff = ''.join(difflib.unified_diff(original.splitlines(True), fixture.splitlines(True),
    fromfile="b8a6/nix/tests/session-recovery-boot.nix", tofile="recovery-diagnostic/session-recovery-diagnostic.nix"))
(HERE / "fixture.patch").write_text(diff)
print(json.dumps({"status": "PASS", "checks": ["original-locked-input-graph", "original-node-and-provider", "original-registration-setup", "first-foreign-cgroup-assertions", "one-diagnostic-check-only", "no-product-source-packaging", "single-worker-dropin", "terminal-return-to-python", "failure-projection-bounds", "python-driver-and-collector-compile"],
                  "fixturePatchSha256": hashlib.sha256(diff.encode()).hexdigest()}, indent=2))
