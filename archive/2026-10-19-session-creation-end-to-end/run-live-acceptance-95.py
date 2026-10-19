"""One exact deployed-browser verification batch; no retries or cleanup."""
import json
import os
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
NODE = "/nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node"
PYTHON = "/nix/store/gf65ylg0vyxygm8j104lxh07vakkswfw-python3-3.13.15-env/bin/python"
ENV = dict(os.environ, PLAYWRIGHT_MODULE="/nix/store/2xc3ahwfjaa3k3wpn4gslgws25swsyd7-playwright-core-1.59.1", CHROMIUM_EXECUTABLE="/nix/store/789yhb4v2kq51jwl4acmmjvxs7mfrlhv-chromium-152.0.7977.75/bin/chromium")
SCENARIOS = [
    ("create", "default-auto", {"auto": True}, "openai", "0"),
    ("create", "alternate-team", {"provider": "codex-lb", "team": "lead_reviewed"}, "codex-lb", "1"),
    ("fork", "alternate-fork", {"provider": "codex-lb", "source": "default-auto"}, "codex-lb", "0"),
    ("plan", "alternate-plan", {"provider": "codex-lb", "team": "lead_reviewed", "source": "default-auto"}, "codex-lb", "1"),
]
results = []
for action, label, options, provider, members in SCENARIOS:
    for phase, command in [
        ("browser", [NODE, "live-browser.cjs", action, label, json.dumps(options)]),
        ("proof", [PYTHON, "live-proof.py", label, provider, members]),
    ]:
        log = HERE / f"live-{label}-{phase}.log"
        print(json.dumps({"phase": "started", "label": label, "step": phase}), flush=True)
        start = time.monotonic()
        with log.open("w") as output:
            result = subprocess.run(command, cwd=HERE, env=ENV, stdout=output, stderr=subprocess.STDOUT)
        row = {"label": label, "step": phase, "exitStatus": result.returncode, "elapsedSeconds": time.monotonic() - start, "log": str(log)}
        results.append(row)
        (HERE / "live-acceptance-95-timing.json").write_text(json.dumps(results, indent=2) + "\n")
        print(json.dumps(row), flush=True)
        print(log.read_text()[-5000:], flush=True)
        if result.returncode:
            sys.exit(result.returncode)
    print(json.dumps({"phase": "pair-complete", "label": label}), flush=True)
