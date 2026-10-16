#!/usr/bin/env python3
import json, os, subprocess, tempfile
from pathlib import Path
record=Path(__file__).resolve().parent
repo=record.parents[1]/'worktrees'/record.name/'vpsadminos'
def git(*args): return subprocess.check_output(['git',*args],cwd=repo,text=True).strip()
old='6abc650f378a8cd4cc8ef4ecc25d74929ab6e1ed'
selector='6b187003124ed5cb8040edc0acbdf4155ecc90d1'
owner='822645a9725dd3653c5eedc1d25ebcdbf28d23b7'
base='4c25fa5f9d1dda58aa0d7019fe351356e6f66c05'
assert git('rev-parse','HEAD')==old
assert git('diff','--cached','--name-only')=='tests/suite/dist-config/nixos-persistence-upgrade.nix'
assert git('diff','--name-only')==''
expected_tree=git('write-tree')
subprocess.run(['git','branch','backup/2026-10-14-config-imports-pre-store-mode',old],cwd=repo,check=True)
message='''tests: provision guest Nix directory traversal mode

New dataset private directories use mode 0750. When mounted as /nix, that
prevents ordinary service users from reaching their executables. Set the
fresh fixture's /nix directory to its normal 0755 mode before first boot.
'''
f=tempfile.NamedTemporaryFile(mode='w',prefix='nixos-store-mode-message-',delete=False);f.write(message);f.close()
subprocess.run(['git','commit','-F',f.name],cwd=repo,check=True)
technical=git('rev-parse','HEAD')
subprocess.run(['git','branch','backup/2026-10-14-config-imports-store-mode-technical',technical],cwd=repo,check=True)
inputs={'old':old,'selector':selector,'owner':owner,'base':base,'technical':technical,'expected_tree':expected_tree,'message_file':f.name}
(record/'store-mode-history-inputs.json').write_text(json.dumps(inputs,indent=2)+'\n')
editor=record/'store-mode-sequence-editor.py'
editor.write_text('''#!/usr/bin/env python3
import json,sys
from pathlib import Path
record=Path(__file__).resolve().parent
i=json.loads((record/'store-mode-history-inputs.json').read_text())
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
(record/'store-mode-history-proof.json').write_text(json.dumps(proof,indent=2)+'\n')
(record/'compatibility-final-head').write_text(head+'\n')
print(json.dumps(proof))
