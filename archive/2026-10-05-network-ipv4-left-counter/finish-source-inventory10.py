from pathlib import Path
import argparse, subprocess, json, hashlib, copy, re, datetime
p = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
a = argparse.ArgumentParser()
a.add_argument('--k-head', required=True)
a.add_argument('--e-head', required=True)
args = a.parse_args()
assert all(re.fullmatch('[0-9a-f]{40}', v) for v in [args.k_head, args.e_head])
old = json.loads((p/'finish-source-inventory9.json').read_text())
out = copy.deepcopy(old)
out['time'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
out['status'] = 'complete committed source and exact mechanical composition; review9 complete; narrow SSH interruption remediation requires direct step9 checks'
out['local_ci'] = False
blobs = {}
def git(repo, *cmd):
    return subprocess.check_output(['git','-C',str(repo),*cmd])
for item in out['repositories']:
    repo = Path(item['worktree'])
    base = item['base']
    head = {'k':args.k_head, 'e':args.e_head}.get(item['key'], item['head'])
    assert git(repo,'rev-parse','HEAD').decode().strip() == head
    assert git(repo,'branch','--show-current').decode().strip() == item['branch']
    assert git(repo,'status','--porcelain=v1','--untracked-files=all') == b''
    assert git(repo,'merge-base',base,head).decode().strip() == base
    assert git(repo,'rev-list','--merges',base+'..'+head) == b''
    item['head'] = head
    item['tree'] = git(repo,'rev-parse',head+'^{tree}').decode().strip()
    item['merge_base'] = base
    item['commits'] = [{'sha':line.split(' ',1)[0],'subject':line.split(' ',1)[1]} for line in git(repo,'log','--reverse','--format=%H %s',base+'..'+head).decode().splitlines()]
    assert len(item['commits']) == {'v':4,'w':1,'c':2,'k':2,'d':3,'e':2}[item['key']]
    item['changed_paths'] = git(repo,'diff','--name-only',base,head).decode().splitlines()
    item['artifacts'] = []
    for kind,data in [('diff',git(repo,'diff','--binary','--full-index',base,head)),('history',git(repo,'log','--reverse','--format=fuller',base+'..'+head))]:
        name = 'finish-source-inventory10-'+item['key']+'.'+kind
        if item['key'] not in ['k','e']:
            assert data == (p/('finish-source-inventory9-'+item['key']+'.'+kind)).read_bytes()
        assert not (p/name).exists()
        blobs[name] = data
        item['artifacts'].append({'kind':kind,'path':name,'sha256':hashlib.sha256(data).hexdigest()})
k = Path(next(i['worktree'] for i in out['repositories'] if i['key']=='k'))
aux = k.parent/'vpsfree-kb-contracts'
assert git(aux,'rev-parse','HEAD').decode().strip() == args.k_head
assert git(aux,'status','--porcelain=v1','--untracked-files=all') == b''
out['same_combined_k_auxiliary_head'] = args.k_head
out['preserved_consumed_sources'].update({'g8_hosted_only':'a1897006c445d5622d21ca5e15a2bf3c5dc54521','shutdown_correction_hosted_only':'74b0717db8d8686d99fac51052a99908c41dad19','review9_source':'d1260ed1eb3aed125f11488cf1c8ce45ed384ad4'})
out['migration_provenance'] = 'V sole feature migration20261006120000 after20260914190000 remains byte-identical and known disposable/preview-consumed; production merge/release/deployment/external consumption unverified. W/C/K/D/E no database migrations. K state2/artifact1/connection1/lease1 and E binding1 unchanged by SSH/session/live-handoff corrections. Consumed G4/G6 incomplete state is retained without adoption/conversion/manual finalization. New socket-retirement authority is operation-local, not a persistent format.'
assert not (p/'finish-source-inventory10.json').exists()
for name,data in blobs.items():
    with (p/name).open('xb') as f:f.write(data)
with (p/'finish-source-inventory10.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('Complete six-branch inventory10 created; no tests or review executed')
