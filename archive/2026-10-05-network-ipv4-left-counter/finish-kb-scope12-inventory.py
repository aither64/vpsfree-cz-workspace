from pathlib import Path
import subprocess,json,hashlib,datetime
T=Path(__file__).resolve().parent
old=json.loads((T/'finish-target11-inventory.json').read_bytes())
out={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':[]}
for row in old['rows']:
 R=Path(row['worktree']);base=row['base']
 def git(*a):return subprocess.check_output(['git','-C',str(R),*a])
 head=git('rev-parse','HEAD').decode().strip()
 assert not git('status','--porcelain')
 assert git('merge-base',base,head).decode().strip()==base
 commits=git('log','--reverse','--format=%H %s',base+'..'+head).decode().splitlines()
 assert len(commits)=={'v':6,'w':1,'c':2,'k':2,'d':3,'e':2}[row['key']]
 assert not git('rev-list','--merges',base+'..'+head)
 artifacts={}
 for kind,data in [('diff',git('diff','--binary','--full-index',base,head)),('history',git('log','--reverse','--format=fuller','--date=iso-strict',base+'..'+head))]:
  p=T/('finish-kb-scope12-inventory-'+row['key']+'.'+kind);p.write_bytes(data)
  artifacts[kind]={'path':p.name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
  if row['key'] not in ('k','e'):assert data==(T/row['artifacts'][kind]['path']).read_bytes()
 out['rows'].append({**row,'head':head,'tree':git('rev-parse','HEAD^{tree}').decode().strip(),'merge_base':base,'commits':commits,'clean':True,'merge_commits':[],'artifacts':artifacts})
out['migration_provenance']='No database migrations K/E/C/D/W/W30. V sole20261006120000 immediately after20260914190000 unchanged; disposable/preview consumption known, production/release/external consumption unverified. Engine2/artifact1/connection1/lease1/Ebinding1 unchanged; no adoption/conversion.'
(T/'finish-kb-scope12-inventory.json').write_text(json.dumps(out,indent=2)+'\n')
print([(r['key'],r['head'],len(r['commits'])) for r in out['rows']])
