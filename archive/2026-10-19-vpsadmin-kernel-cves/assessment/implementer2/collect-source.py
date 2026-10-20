import os,json,hashlib,subprocess,urllib.request,concurrent.futures,base64
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent.parent;R=Path('/home/aither/workspace/ai/vpsfree.cz/repos');E=dict(os.environ,GIT_NO_LAZY_FETCH='1');ids=json.loads((S/'assessment/packages.json').read_text())['groups']['implementer2'];rs={x['cve']:x for x in json.loads((S/'research/cve-evidence/range-records.json').read_text())};manifest=[]
L='1dfea587406b7dd79973831d1677fb2418e5e9aa';O='87fc13aac3fc8ce3d6c71c7ef3a8e72a5993a088';V='fb2f51222503a45f2e5a42af505f719e44279ed0';C='a2ad6da408715de811cc6d8ea7b29ac55ea341ec'
def get(repo,rev,path,patch=False):
 dest=B/('fixes' if patch else 'source/'+repo)/(path if not patch else path+'.patch')
 url=f'https://github.com/vpsfreecz/{repo}/blob/{rev}/{path}'
 if dest.exists():data=dest.read_bytes();method='existing exact local read'
 else:
  cmd=['git','--git-dir='+str(R/(repo+'.git')),'show','--no-ext-diff','--format=fuller',rev]if patch else ['git','--git-dir='+str(R/(repo+'.git')),'show',rev+':'+path]
  p=subprocess.CompletedProcess(cmd, 1, stdout=b'', stderr=b'bounded exact HTTP fallback avoids expensive local pack walks')
  data=p.stdout;method='local git with GIT_NO_LAZY_FETCH=1'
  if p.returncode:
   if repo!='linux':
    p=subprocess.run(cmd,capture_output=True,env=E);data=p.stdout
    if p.returncode:return {'error':p.stderr.decode()[:150],'path':path}
    dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    return {'repository':repo,'revision':rev,'path':path,'file':str(dest.relative_to(B)),'sha256':hashlib.sha256(data).hexdigest(),'url':url,'method':'local source read without lazy fetch'}
   if patch:url=f'https://github.com/gregkh/linux/commit/{rev}.patch'
   else:url=f'https://raw.githubusercontent.com/vpsfreecz/linux/{rev}/{path}'
   try:
    with urllib.request.urlopen(url,timeout=35)as f:data=f.read()
    if data.lstrip().startswith(b'<!doctype html')or data.lstrip().startswith(b'<html'):raise ValueError('HTML instead of source')
    method='exact public HTTP fallback'
   except Exception as e:return {'error':str(e),'path':path,'revision':rev,'url':url}
  dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
 return {'repository':repo,'revision':rev,'path':path,'file':str(dest.relative_to(B)),'sha256':hashlib.sha256(data).hexdigest(),'url':url,'method':method}
jobs=[]
for c in ids:
 x=rs[c];p=B/'primary'/(c+'.json');p.parent.mkdir(exist_ok=True);p.write_bytes((S/'research/cve-evidence/records'/(c+'.json')).read_bytes())
 jobs+=[('linux',L,p,False)for p in set(f for a in x['affected']for f in a.get('programFiles',[]))];jobs.append(('linux',x['fixes'][0]['sha'],c,True))
extras=['fs/ceph/super.c','net/ceph/osd_client.c','fs/ceph/mds_client.c','net/ceph/crush/mapper.c','fs/smb/client/cifsfs.c','fs/smb/client/smb1ops.c','fs/super.c','fs/nfs/super.c','fs/nfs/nfs4client.c','net/ipv6/mip6.c','net/ipv6/exthdrs.c','net/xfrm/xfrm_state.c','net/xfrm/xfrm_interface_core.c','net/ipv4/ip_vti.c','net/xfrm/xfrm_user.c','net/mptcp/ctrl.c','net/mptcp/protocol.c','net/mptcp/Kconfig']
jobs +=[('linux',L,p,False)for p in extras]
jobs +=[('vpsadminos',O,p,False)for p in ['os/modules/config/kernel.nix','os/modules/config/tunables.nix','osctld/configs/lxc/common.conf','osctld/templates/ct/config.erb','osctld/templates/apparmor/profile.erb','os/packages/linux/available-kernels.nix','docs/os/livepatches/6.12.95.md']]
jobs +=[('vpsadmin',V,p,False)for p in ['api/models/vps_feature.rb','libnodectld/lib/nodectld/commands/vps/features.rb']]
jobs +=[('vpsfree-cz-configuration',C,p,False)for p in ['cluster/cz.vpsfree/nodes/common/all.nix','cluster/cz.vpsfree/nodes/common/storage.nix','configs/node/kernels.nix','modules/cluster/nodes/common.nix','modules/cluster/nodes/vpsadminos.nix','cluster/cz.vpsfree/nodes/common/tunables-common.nix']]
with concurrent.futures.ThreadPoolExecutor(max_workers=6)as pool:
 for entry in pool.map(lambda x:get(*x),list(dict.fromkeys(jobs))):manifest.append(entry)
(B/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print('sources',len(manifest),'errors',[x for x in manifest if'error'in x],flush=True)
# Batch local object reads without lazy fetch, then only exact missing Makefiles by HTTP.
qs=list(dict.fromkeys(v[k]+':Makefile'for c in ids for a in rs[c]['affected']for v in a['versions']if v.get('versionType')=='git'for k in ['version','lessThan']if v.get(k)))
versions={};missing=qs;provenance=[]
def version(data):
 vals={}
 for line in data.decode().splitlines()[:8]:
  if ' = 'in line:k,v=line.split(' = ',1);vals[k]=v
 return '.'.join(vals.get(k,'?')for k in ['VERSION','PATCHLEVEL','SUBLEVEL'])+vals.get('EXTRAVERSION','')
def remote(q):
 rev=q.split(':')[0];url=f'https://raw.githubusercontent.com/gregkh/linux/{rev}/Makefile'
 try:
  with urllib.request.urlopen(url,timeout=25)as f:data=f.read()
  dest=B/'makefiles'/(rev+'.txt');dest.parent.mkdir(exist_ok=True);dest.write_bytes(data)
  return q,version(data),{'object':q,'url':url,'sha256':hashlib.sha256(data).hexdigest()}
 except Exception as e:return q,None,{'object':q,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=8)as pool:
 for q,v,pr in pool.map(remote,missing):versions[q]=v;provenance.append(pr)
(B/'commit-versions.json').write_text(json.dumps(versions,indent=2)+'\n');(B/'version-source-manifest.json').write_text(json.dumps(provenance,indent=2)+'\n');print('versionobjects',len(versions),'missing',sum(v is None for v in versions.values()),flush=True)
