import json,pathlib,subprocess,tempfile,time
root=pathlib.Path(__file__).resolve().parent
state=json.loads((root/'projection-state.json').read_text())
worktree=state['projection_worktree']
def git(*args,**kwargs):
 return subprocess.check_output(['git',*args],cwd=worktree,**kwargs)
assert not git('status','--porcelain')
assert git('rev-parse','HEAD',text=True).strip()==state['old'][7]
items=[(c,state['snapshots'][c]) for c in state['old'][8:]]
items.append((state['cli'],git('rev-parse',state['convergence']+'^{tree}',text=True).strip()))
records=[]
for i,(original,tree) in enumerate(items,9):
 before=git('rev-parse','HEAD',text=True).strip()
 changes=git('diff','--no-renames','--name-status','-z','HEAD',tree).decode().split('\0')
 paths=[];deletes=[]
 for n in range(0,len(changes)-1,2):
  status,path=changes[n:n+2]
  (deletes if status=='D' else paths).append(path)
 if paths:git('restore','--source='+tree,'--staged','--worktree','--',*paths)
 if deletes:git('rm','--',*deletes)
 assert git('write-tree',text=True).strip()==tree
 git('diff','--cached','--check')
 message=git('show','-s','--format=%B',original,text=True)
 if i==9:
  message="""portal: browse all session files beside an inline preview

List every regular file beneath the confined current tracking root without
Git or registration. Reuse the same nofollow opener for content, sanitized
Markdown, checked raster images and byte-exact downloads, including legacy
URLs across ordinary archive and revive transitions.

Load the directory tree on first open or Refresh. Show selected files in a
shared inline renderer with Raw/Preview, original-text Copy and Download;
retain native modified links, selection, scrolling and the composer draft.
Document the reader/API and browser behavior with their owning fixtures.
"""
 if i==19:
  message="""session: deprecate artifact registration for automatic Files

Session files appear automatically beneath their tracking root. Retain
artifact add and its legacy options as a successful notice without manifest
writes, lifecycle locks or runtime readiness checks. Existing declarations
and readers remain compatible.

Replace registration-writer tests with no-op and parser coverage, preserve
manifest validation, and update registration guidance. Registration no longer
changes labels or ownership state.
"""
 assert all(len(line)<=80 for line in message.splitlines()),original
 with tempfile.NamedTemporaryFile(mode='w',prefix='files-history-imp3-',suffix='.txt',delete=False) as f:
  f.write(message);message_path=f.name
 author=git('show','-s','--format=%an <%ae>',original,text=True).strip()
 authored=git('show','-s','--format=%aI',original,text=True).strip()
 start=time.monotonic()
 output=git('commit','--author='+author,'--date='+authored,'-F',message_path,text=True,stderr=subprocess.STDOUT)
 (root/('commit-group-'+str(i)+'.log')).write_text(output)
 after=git('rev-parse','HEAD',text=True).strip()
 assert git('rev-parse','HEAD^{tree}',text=True).strip()==tree
 assert not git('status','--porcelain')
 records.append({'group':i,'original':original,'head':after,'parent':before,'tree':tree,'seconds':time.monotonic()-start})
 (root/'commits.json').write_text(json.dumps(records,indent=2)+'\n')
 print(str(i)+' '+after+' '+git('show','-s','--format=%s','HEAD',text=True).strip(),flush=True)
assert git('rev-parse','HEAD^{tree}',text=True).strip()==git('rev-parse',state['convergence']+'^{tree}',text=True).strip()
state['projected_head']=records[-1]['head']
(root/'projection-state.json').write_text(json.dumps(state,indent=2)+'\n')
print('FINAL EXACT TREE '+git('rev-parse','HEAD^{tree}',text=True).strip(),flush=True)
