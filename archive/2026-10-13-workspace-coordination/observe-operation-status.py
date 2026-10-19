"""Read-only observer for one parent-launched operation; no user-bus access."""
import argparse
import json
import time
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--status', required=True)
parser.add_argument('--invocation', required=True)
parser.add_argument('--log', required=True)
args = parser.parse_args()
started = time.monotonic()
invocation = Path(args.invocation).read_text().strip()
assert invocation
while not Path(args.status).exists():
    time.sleep(30)
assert Path(args.invocation).read_text().strip() == invocation
status = int(Path(args.status).read_text().strip())
result = {'result': 'passed' if status == 0 else 'failed', 'status': status,
          'invocation': invocation, 'elapsedSeconds': round(time.monotonic() - started, 1),
          'statusFile': args.status, 'logFile': args.log}
if status:
    result['failureTail'] = Path(args.log).read_text(errors='replace')[-4096:]
print(json.dumps(result))
