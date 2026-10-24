import json
import subprocess
import time
from pathlib import Path

tracking = Path(__file__).resolve().parent
brief = tracking / "watcher-brief-4.md"
if "Status: RELEASED" not in brief.read_text():
    raise SystemExit("Capture watcher remains held pending completed review")
attempt = tracking / "watcher-capture-4"
attempt.mkdir(exist_ok=False)
policy = json.loads((tracking / "watcher-policy.json").read_text())
message = (
    "You are one fresh managed operation-only verification watcher, native utility "
    + policy["nativeIdentity"] + ", catalog " + policy["catalogDigest"]
    + ". Read and execute only the RELEASED packet at " + str(brief)
    + ". Verify exact guidance paths and launch policy. Run the single capture-attempt-4.sh "
    "operation once, retain logs/exit, and report. No edits, diagnosis, retries, "
    "CI/native/build/deployment/claims/integration/release/lifecycle/nested agents."
)
command = [
    "codex", "--ask-for-approval", "never", "--sandbox", "danger-full-access",
    "-c", 'model_reasoning_effort="low"',
    "-c", 'developer_instructions="Run only the assigned verification operation, retain its result, and do not edit application source, diagnose failures, retry, approve, or deploy."',
    "exec", "--ephemeral", "--json", "--color", "never", "--model", policy["model"],
    "--cd", str(tracking.parent), "--output-last-message", str(attempt / "last-message.md"), message,
]
(attempt / "launch.json").write_text(json.dumps({"command": command, "policy": policy}, indent=2) + "\n")
started = time.monotonic()
with (attempt / "stdout.jsonl").open("w") as out, (attempt / "stderr.log").open("w") as err:
    result = subprocess.run(command, stdout=out, stderr=err)
(attempt / "exit.json").write_text(json.dumps({"exit": result.returncode, "elapsed": time.monotonic() - started}) + "\n")
print(json.dumps({"watcherExit": result.returncode, "evidence": str(attempt)}))
raise SystemExit(result.returncode)
