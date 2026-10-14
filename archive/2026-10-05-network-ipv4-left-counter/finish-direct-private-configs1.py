#!/usr/bin/env python3
"""Prepare private direct-campaign inputs after exact package acceptance."""
import copy, datetime, hashlib, json, os, pathlib, secrets
TRACKING = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
G = 'ab09bd437b310f57e4ff2453ec0432555d85eaca'
gate = json.loads((TRACKING / 'finish-source-review4-acceptance.json').read_text())
assert gate['generator'] == G and gate['construction_may_proceed'] is True
package = json.loads((TRACKING / 'finish-direct-package-realize1-acceptance.json').read_text())
assert package['generator'] == G and package['accepted'] is True
source = pathlib.Path(package['source'])
base = json.loads((source / 'cluster/default-config.json').read_text())
parent = pathlib.Path('/home/aither/.local/state/vpsfree-kb-verification')
if parent.exists():
    st = parent.lstat()
    assert not parent.is_symlink() and parent.is_dir() and st.st_uid == os.getuid() and st.st_mode & 0o777 == 0o700
else:
    parent.mkdir(mode=0o700)
private = parent / '2026-10-05-network-ipv4-left-counter-g4'
private.mkdir(mode=0o700)  # Refuse an unexplained existing campaign/input tree.
root = private / 'campaign'
users = []
for login, level, start, full in [('test-admin',99,1,'Test Administrator'),('test-user1',1,9,'Test User One'),('test-user2',1,17,'Test User Two')]:
    account = copy.deepcopy(next((u for u in base['seed']['users'] if u['login'] == login), {}))
    account.update(login=login,level=level,password=secrets.token_urlsafe(24),fullName=full,email=login+'@example.test',namespace={'blockStart':start,'blockCount':8})
    users.append(account)
summary = {'generator':G,'source':str(source),'private_parent':str(private),'campaign_root':str(root),'credentials_exported':False,'configurations':[]}
for index, name in enumerate(['a','b']):
    value=copy.deepcopy(base)
    for block in ['domains','tmpDomains']:
        value[block]={k:v.replace('.aitherdev.int.vpsfree.cz','.example.test') for k,v in value[block].items()}
    for entry in value['dns']['servers'].values():
        entry['serverName']=entry['serverName'].replace('.aitherdev.int.vpsfree.cz','.example.test')
    value['dns']['enable']=False
    value['resolver']={'mode':'cluster','upstreamNameservers':['10.0.2.3']}
    value['services'].update(memoryMiB=4096,rootDiskMiB=12288)
    value['nodes']['node1'].update(memoryMiB=4096,tankDiskGiB=16)
    value['seed']['users']=copy.deepcopy(users)
    port=24000+100*index
    value['local']={'bindAddress':'127.0.0.1','multicastPort':port+20,'ports':{'services':{'ssh':port,'https':port+10},'node1':{'ssh':port+1}}}
    data=(json.dumps(value,indent=2)+'\n').encode()
    path=private/('config-'+name+'.json')
    fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
    with os.fdopen(fd,'wb') as out:out.write(data)
    summary['configurations'].append({'name':name,'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'ports':value['local']['ports'],'udp':port+20,'account_logins':['test-admin','test-user1','test-user2']})
with (TRACKING/'finish-direct-private-configs1.json').open('x') as out:json.dump(summary,out,indent=2);out.write('\n')
print(json.dumps({'receipt':str(TRACKING/'finish-direct-private-configs1.json'),'credentials_exported':False}))
