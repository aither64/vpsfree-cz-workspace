import hashlib
import json
import subprocess
import time
from pathlib import Path

tracking = Path(__file__).resolve().parent
session = tracking.parents[1]
brief = tracking / "watcher-accepted-fork-brief.md"
if "Status: RELEASED" not in brief.read_text():
    raise SystemExit("Accepted-fork watcher remains held")
policy = json.loads((session / "ui-successor/watcher-policy.json").read_text())
catalog_path = Path(policy["catalog"])
catalog = json.loads(catalog_path.read_text())
utility = catalog["utilities"]["verification_watcher"]
assert hashlib.sha256(catalog_path.read_bytes()).hexdigest() == policy["catalogFileSha256"]
assert catalog["catalog_digest"] == policy["catalogDigest"]
assert utility["model"] == "gpt-6-luna" and utility["effort"] == "low"
assert catalog["execution_access"] == "full_access"
assert utility["lifetime"] == "operation" and utility["max_concurrent"] == 1
assert Path(policy["utilityConfiguration"]).is_file()
attempt = tracking / "watcher-accepted-fork-1"
attempt.mkdir(exist_ok=False)
message = (
    "You are one fresh managed operation-only verification watcher, native utility "
    + policy["nativeIdentity"] + ", catalog " + policy["catalogDigest"]
    + ". Read and execute only the RELEASED packet at " + str(brief)
    + ". Verify exact session, guidance and execution policy. Use your shell tool "
    "directly for the single python3 backend-successor/I-B1/accepted-fork-command.py "
    "operation once. No nested Codex CLI. Retain logs/exit and report without "
    "source edits, diagnosis, retry, other tests, deployment or lifecycle actions."
)
command = [
    "codex", "--ask-for-approval", "never", "--sandbox", "danger-full-access",
    "-c", 'model_reasoning_effort="low"',
    "-c", 'developer_instructions="Run only the assigned verification shell operation using your shell tool directly. The parent already launched this Codex process with the required model and execution policy; do not launch another codex CLI. Retain result and do not edit source, diagnose, retry, approve, or deploy."',
    "exec", "--ephemeral", "--json", "--color", "never", "--model", utility["model"],
    "--cd", str(session), "--output-last-message", str(attempt / "last-message.md"), message,
]
(attempt / "launch.json").write_text(json.dumps({"command": command, "policy": policy}, indent=2) + "\n")
started = time.monotonic()
with (attempt / "stdout.jsonl").open("w") as out, (attempt / "stderr.log").open("w") as err:
    result = subprocess.run(command, stdout=out, stderr=err)
(attempt / "exit.json").write_text(json.dumps({"exit": result.returncode, "elapsed": time.monotonic() - started}) + "\n")
print(json.dumps({"watcherExit": result.returncode, "evidence": str(attempt)}))
raise SystemExit(result.returncode)
