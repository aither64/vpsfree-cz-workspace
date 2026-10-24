import sys,subprocess
from pathlib import Path
p=Path(sys.argv[1]); lines=p.read_text().splitlines(keepends=True)
command,sha,*_=lines[0].split()
assert command=="pick" and subprocess.check_output(["git","rev-parse",sha],text=True).strip()=="991101f212eb7da24b5ba71e679eb4b59baef56d", lines[0]
p.write_text("".join(lines[1:]))
