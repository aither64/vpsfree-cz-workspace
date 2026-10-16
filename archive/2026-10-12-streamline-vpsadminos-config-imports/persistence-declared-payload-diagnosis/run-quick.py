import subprocess,time
from pathlib import Path
record=Path(__file__).resolve().parent
out=record/'quick';out.mkdir(exist_ok=True)
source=record.parent.parent.parent/'worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos'
argv=['nix','develop','--profile','result/config-imports-dev-shell','--command','bash',str(record/'quick-checks.sh')]
status=130;start=time.monotonic()
try:
 with (out/'wrapper.log').open('w') as log: status=subprocess.call(argv,cwd=source,stdout=log,stderr=subprocess.STDOUT)
finally:
 (out/'wrapper.status').write_text(str(status)+'\n');(out/'elapsed-seconds').write_text(str(round(time.monotonic()-start))+'\n')
raise SystemExit(status)
