#!/usr/bin/env python3
import json,os,subprocess,tempfile
from pathlib import Path
record=Path(__file__).resolve().parent
source=record.parents[1]/'worktrees'/record.name/'vpsadminos'
def git(*args): return subprocess.check_output(['git',*args],cwd=source,text=True).strip()
head=git('rev-parse','HEAD')
assert head==(record/'effective-mounts-review-runtime-clearance').read_text().strip()
assert not git('status','--porcelain')
assert (record/'effective-mounts-final-quick/status').read_text().strip()=='0'
assert (record/'effective-mounts-i1-quick/status').read_text().strip()=='0'
assert (record/'effective-mounts-review/i1-final-head').read_text().strip()==head
attempt=Path(tempfile.mkdtemp(prefix='runtime-effective.',dir=record))
state=Path(tempfile.mkdtemp(prefix='ni.',dir='/tmp'))
owner={'session':record.name,'workspace':str(record.parents[1]),'uid':os.getuid(),'source':str(source),'head':head,'tree':git('rev-parse','HEAD^{tree}'),'state_dir':str(state),'patterns':['dist-config/nixos-persistence-upgrade#*']}
(attempt/'ownership.json').write_text(json.dumps(owner,indent=2)+'\n')
(attempt/'host-metadata.nix').write_text('{ system.vpsadminos = { revision = "'+head+'"; revisionDirty = false; versionSuffix = ".git.'+head[:9]+'"; }; }\n')
(attempt/'state-dir').write_text(str(state)+'\n')
(record/'effective-runtime-attempt').write_text(str(attempt)+'\n')
print(attempt)
