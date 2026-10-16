#!/usr/bin/env python3
import json, os, subprocess, tempfile
from pathlib import Path
record=Path(__file__).resolve().parent
repo=record.parents[1]/'worktrees'/record.name/'vpsadminos'
def git(*args): return subprocess.check_output(['git',*args],cwd=repo,text=True).strip()
old='96b69056cb16017dfef2c9a73a1acc755c032b72'
selector='e51ee4eac81d6e46a6acd3bbeb715a3ba0d5940e'
owner='be90cb27c095861983ba6f50bc2c058d6ea2df3f'
base='1150e37b1cc997b1728f2fda806a3433ef55b798'
assert git('rev-parse','HEAD')==old
assert git('diff','--cached','--name-only')=='tests/suite/dist-config/nixos-persistence-upgrade.nix'
assert git('diff','--name-only')==''
expected_tree=git('write-tree')
subprocess.run(['git','branch','backup/2026-10-14-config-imports-pre-runtime-setup',old],cwd=repo,check=True)
message='''tests: prepare NixOS upgrade container mounts

The dataset CLI interprets a root slash as a literal dataset suffix, and
mapping the shared host store fails on its overlay filesystem before init.
Use the queried container root as the persistence bind source and share the
read-only store without ID mapping. Keep native mappings on container data.
'''
f=tempfile.NamedTemporaryFile(mode='w',prefix='nixos-runtime-setup-message-',delete=False);f.write(message);f.close()
subprocess.run(['git','commit','-F',f.name],cwd=repo,check=True)
technical=git('rev-parse','HEAD')
subprocess.run(['git','branch','backup/2026-10-14-config-imports-runtime-setup-technical',technical],cwd=repo,check=True)
inputs={'old':old,'selector':selector,'owner':owner,'base':base,'technical':technical,'expected_tree':expected_tree,'message_file':f.name}
(record/'runtime-setup-history-inputs.json').write_text(json.dumps(inputs,indent=2)+'\n')
editor=record/'runtime-setup-sequence-editor.py'
editor.write_text('''#!/usr/bin/env python3
import json,sys
from pathlib import Path
record=Path(__file__).resolve().parent
i=json.loads((record/'runtime-setup-history-inputs.json').read_text())
p=Path(sys.argv[1]); rows=[l.split() for l in p.read_text().splitlines() if l.strip() and not l.startswith('#')]
expected=[i['selector'],i['owner'],i['old'],i['technical']]
assert len(rows)==4 and all(r[0]=='pick' and s.startswith(r[1]) for r,s in zip(rows,expected))
p.write_text('pick '+i['selector']+'\\npick '+i['owner']+'\\nfixup '+i['technical']+'\\npick '+i['old']+'\\n')
''')
editor.chmod(0o755)
env=os.environ.copy();env['GIT_SEQUENCE_EDITOR']=str(editor)
subprocess.run(['git','rebase','-i',base],cwd=repo,env=env,check=True)
head=git('rev-parse','HEAD'); tree=git('rev-parse','HEAD^{tree}')
series=git('rev-list','--reverse',base+'..HEAD').splitlines()
assert len(series)==3 and series[0]==selector
assert tree==expected_tree and git('status','--porcelain')==''
assert git('diff','--name-only',old,head)=='tests/suite/dist-config/nixos-persistence-upgrade.nix'
assert git('show','-s','--format=%B',owner)==git('show','-s','--format=%B',series[1])
assert git('show','-s','--format=%B',old)==git('show','-s','--format=%B',head)
proof={'prior':old,'head':head,'tree':tree,'series':series,'only_changed_path':'tests/suite/dist-config/nixos-persistence-upgrade.nix','tree_matches_validated_index':True,'selector_unchanged':True,'owner_messages_unchanged':True,'clean':True}
(record/'runtime-setup-history-proof.json').write_text(json.dumps(proof,indent=2)+'\n')
(record/'compatibility-final-head').write_text(head+'\n')
print(json.dumps(proof))
