"""Safe post-run summary. Never echo journal lines or exception messages."""
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
COVERAGE = {"missing-active-inconclusive", "observed-partial-inconclusive", "observed-with-raises", "observed-no-raises"}
summary = {
    "sourceRevision": "b8a6be26a75347dcc9ec0fd1330dff886e47c93f",
    "originalFailedSuite": "unchanged-unresolved",
    "rootCause": "unproved",
    "diagnosticExitStatus": int(sys.argv[1]),
    "diagnosticLaunched": sys.argv[2] == "launched",
    "coverage": "not-collected-inconclusive",
}
if summary["diagnosticLaunched"]:
    summary["scenario"] = "applied-nonreproduction" if summary["diagnosticExitStatus"] == 0 else "assertion-or-infrastructure-failed"
log_path = HERE / "run/check.log"
if log_path.is_file():
    # Stream the log, retaining only the fixed bounded projection from the driver.
    with log_path.open(errors="replace") as stream:
        for line in stream:
            match = re.search(r"DIAGNOSTIC_OBSERVER_RESULT=(\{[^\n]*\})", line)
            if not match:
                continue
            try:
                record = json.loads(match.group(1))
                assert record["coverage"] in COVERAGE
                assert isinstance(record["activePids"], list) and len(record["activePids"]) <= 256
                assert all(type(pid) is int and 0 < pid < 2**31 for pid in record["activePids"])
                clean = {"coverage": record["coverage"], "activePids": record["activePids"]}
                for key in ["raiseCount", "disabledCount", "truncationCount"]:
                    assert type(record[key]) is int and 0 <= record[key] <= 1000000
                    clean[key] = record[key]
                summary.update(clean)
            except Exception:
                summary["coverage"] = "not-collected-inconclusive"
(HERE / "run/result.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, sort_keys=True))
