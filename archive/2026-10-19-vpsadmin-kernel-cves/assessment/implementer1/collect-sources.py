#!/usr/bin/env python3
import concurrent.futures,hashlib,json,pathlib,subprocess,os
os.environ["GIT_NO_LAZY_FETCH"]="1"
ROOT=pathlib.Path.cwd();OUT=ROOT/'assessment/implementer1';GIT=ROOT.parent.parent/'repos/linux.git'
# Workspace path is fixed by this session binding, never selected from cwd alone.
GIT=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/repos/linux.git')
REV='1dfea587406b7dd79973831d1677fb2418e5e9aa'
ids=json.load(open('assessment/packages.json'))['groups']['implementer1'];rs={r['cve']:r for r in json.load(open('research/cve-evidence/range-records.json'))}
def git(*args):return subprocess.check_output(['git','--git-dir='+str(GIT),*args])
paths=sorted({f for cve in ids for a in rs[cve]['affected'] for f in a.get('programFiles',[])})
def source(path):
 raw=git('show',REV+':'+path);dest=OUT/'source/linux'/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
 return {'path':path,'revision':REV,'sha256':hashlib.sha256(raw).hexdigest(),'file':str(dest.relative_to(OUT)),'url':'https://github.com/vpsfreecz/linux/blob/'+REV+'/'+path}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:sources=list(ex.map(source,paths))
summary=[]
for cve in ids:
 r=rs[cve];p=OUT/'primary'/cve;p.mkdir(parents=True,exist_ok=True)
 raw=(ROOT/'research/cve-evidence/records'/(cve+'.json')).read_bytes();(p/'record.json').write_bytes(raw)
 fix=r['fixes'][0];patch=git('show','--no-ext-diff','--format=fuller',fix['sha']);(p/'stable-fix.patch').write_bytes(patch)
 d=json.loads(raw)['containers']['cna'];versions=[v for a in d['affected'] for v in a.get('versions',[]) if v.get('versionType')!='git'];summary.append({'cve':cve,'title':d.get('title'),'description':d['descriptions'],'versions':versions,'fix':{'sha':fix['sha'],'release':fix['release']},'affected_files':sorted({f for a in d['affected'] for f in a.get('programFiles',[])}),'primary_url':r['cna_url'],'primary_sha256':hashlib.sha256(raw).hexdigest(),'fix_patch_sha256':hashlib.sha256(patch).hexdigest()})
(OUT/'primary-summary.json').write_text(json.dumps(summary,indent=2)+'\n');(OUT/'source-manifest.json').write_text(json.dumps({'linux_revision':REV,'sources':sources},indent=2)+'\n');print('saved',len(summary),'primary records/fixes and',len(sources),'current source files')
