#!/usr/bin/env python3
import json,os,subprocess,time
from pathlib import Path
record=Path(__file__).resolve().parent
attempt=Path((record/'effective-runtime-attempt').read_text().strip()); owner=json.loads((attempt/'ownership.json').read_text()); source=Path(owner['source'])
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=source,text=True).strip()==owner['head']==(record/'effective-mounts-review-runtime-clearance').read_text().strip()
assert not subprocess.check_output(['git','status','--porcelain'],cwd=source,text=True).strip()
argv=['./test-runner.sh','test','--state-dir',owner['state_dir'],'--test-config',str(record/'image-test-config.nix'),'--no-destructive','--jobs','1',*owner['patterns']]
env=os.environ.copy();env['VPSADMINOS_CONFIG']=str(attempt/'host-metadata.nix')
(attempt/'invocation.json').write_text(json.dumps({'cwd':str(source),'argv':argv,'VPSADMINOS_CONFIG':env['VPSADMINOS_CONFIG']},indent=2)+'\n')
status=130;start=time.monotonic()
try:
 with (attempt/'runtime.log').open('w') as log: status=subprocess.call(argv,cwd=source,env=env,stdout=log,stderr=subprocess.STDOUT)
finally:
 (attempt/'runtime.status').write_text(str(status)+'\n');(attempt/'elapsed-seconds').write_text(str(round(time.monotonic()-start))+'\n')
raise SystemExit(status)
