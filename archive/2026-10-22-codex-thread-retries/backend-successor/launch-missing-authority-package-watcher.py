import hashlib
import json
import subprocess
import time
from pathlib import Path

tracking = Path(__file__).resolve().parent
session = tracking.parent
brief = tracking / "missing-authority/package-watcher-brief.md"
if "Status: RELEASED" not in brief.read_text():
    raise SystemExit("Final verification watcher remains held")
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
attempt = tracking / "watcher-missing-authority-package"
attempt.mkdir(exist_ok=False)
message = (
    "You are one fresh managed operation-only verification watcher, native utility "
    + policy["nativeIdentity"] + ", catalog " + policy["catalogDigest"]
    + ". Read and execute only the RELEASED packet at " + str(brief)
    + ". Verify exact session, guidance and execution policy. Use your shell tool "
    "directly for the exact single-command affected package batch from the brief "
    "operation once. No nested Codex CLI. Retain logs/exit and report without "
    "source edits, diagnosis, retry, other tests, deployment or lifecycle actions."
)
command = [
    "codex", "--ask-for-approval", "never", "--sandbox", "danger-full-access",
    "-c", 'model_reasoning_effort="low"',
    "-c", 'developer_instructions="This Codex conversation is bound to development session 2026-10-22-codex-thread-retries in workspace /home/aither/workspace/ai/vpsfree.cz. Run dev-session current and require that exact slug. DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE may both be absent; that absence does not negate this trusted developer binding. If present both must match. Do not require dev-session current to print a workspace path: it prints the slug only. Run only the assigned verification shell operation using your shell tool directly. The parent already launched this Codex process with the required model and execution policy; do not launch another codex CLI. Retain result and do not edit source, diagnose, retry, approve, or deploy."',
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
