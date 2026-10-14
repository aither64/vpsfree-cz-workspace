import hashlib,json,pathlib,subprocess
track=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
roots=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter')
specs=[('v','vpsadmin','6c706c285681f1bc356cdc2569f5bd53817c6326','7e86ee211d898256bd93cac7221c256636f3fcc3'),('c','vpsfree-cz-configuration','c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a','35b4fa2d664bde95db140240ac929b1f61c4e688')]
result={}
for label,name,base,head in specs:
    cwd=roots/name
    def git(*args): return subprocess.check_output(['git',*args],cwd=cwd)
    assert git('rev-parse','HEAD').decode().strip()==head
    assert not git('status','--porcelain')
    assert git('merge-base',base,head).decode().strip()==base
    artifacts={}
    for kind,args in [('diff',('diff','--binary','--full-index',base,head)),('history',('log','--reverse','--format=fuller',f'{base}..{head}')),('paths',('diff','--name-status',base,head))]:
        data=git(*args); target=track/f'finish-http-review1-{label}.{kind}'
        assert not target.exists()
        target.write_bytes(data)
        artifacts[kind]={'path':target.name,'sha256':hashlib.sha256(data).hexdigest()}
    commits=git('rev-list','--reverse',f'{base}..{head}').decode().splitlines()
    result[label]={'repository':name,'worktree':str(cwd),'base':base,'head':head,'tree':git('rev-parse',head+'^{tree}').decode().strip(),'commits':commits,'merge_count':int(git('rev-list','--count','--merges',f'{base}..{head}')),'artifacts':artifacts}
    assert len(commits)==(4 if label=='v' else 2)
    assert not result[label]['merge_count']
target=track/'finish-http-review1-inventory.json'
assert not target.exists()
target.write_text(json.dumps(result,indent=2)+'\n')
print('Committed V/C inventory captured; review awaits exact-head hosted API quick gate.')
