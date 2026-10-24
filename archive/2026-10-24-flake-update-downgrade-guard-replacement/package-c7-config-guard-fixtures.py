#!/usr/bin/env python3
"""Execute actual D workflow shell bodies using nonpublishing tool fixtures."""
import json, os, pathlib, shutil, subprocess, sys, tempfile
ROOT=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz')
SLUG='2026-10-24-flake-update-downgrade-guard-replacement'
PIN = os.environ.get('EXPECTED_CONFCTL_FLAKE', 'github:vpsfreecz/confctl/5436d3d7c36d3d5174eab3c44e3578830749d3db#confctl')
FAKE=r'''#!/usr/bin/env python3
import json,os,sys,subprocess
from pathlib import Path
name=Path(sys.argv[0]).name; a=sys.argv[1:]; r=Path(os.environ['RUNNER_TEMP']); case=os.environ['CASE']
def event(kind,**data):
 with (r/'events').open('a') as f: f.write(json.dumps(dict(kind=kind,**data))+'\n')
def stop(code): sys.exit(code)
if name=='nix':
 if a[0] in ('develop','shell'):
  if a[0]=='shell': assert a[1]==os.environ['CONFCTL_FLAKE']; event('new_tool',pin=a[1])
  else: event('old_shell')
  stop(subprocess.call(a[a.index('-c')+1:]))
 if a[0]=='eval':
  if any('github:numtide/llm-agents.nix' in x for x in a): print('1' if case=='llm_same' else '2',end='')
  else: print('2' if (r/'llm-updated').exists() and case!='llm_mismatch' else '1',end='')
  stop(0)
 raise AssertionError(a)
if name=='confctl':
 assert os.environ['GITHUB_TOKEN']=='fixture-token'
 if a[:3]==['inputs','channel','update']:
  assert '--forward-only' in a and '--commit' in a
  count=int((r/'updates').read_text())+1 if (r/'updates').exists() else 1
  (r/'updates').write_text(str(count)); event('update',args=a,count=count)
  if case=='reject_first' and count==1: stop(3)
  if case in ('reject_late','error_late') and count==int(os.environ['LAST_UPDATE']): stop(3 if case=='reject_late' else 1)
  p=Path('flake.lock'); data=json.loads(p.read_text()); data['generation']+=1; p.write_text(json.dumps(data))
  if a[-1]=='llm-agents': (r/'llm-updated').touch()
  if case=='hook_failure' and count==2: event('hook_failure'); stop(1)
  (r/'committed.lock').write_text(p.read_text()); event('local_commit'); stop(0)
 if a[:2]==['inputs','check-update']:
  old=Path(a[a.index('--old-lock')+1]); new=Path(a[a.index('--new-lock')+1])
  assert old==r/'flake-update-baseline.lock' and new==r/'flake-update-final.lock' and json.loads(old.read_text())==dict(generation=0)
  event('final_check')
  if case=='final_error': stop(1)
  if case=='final_reject' or json.loads(new.read_text())['generation']<0: stop(3)
  stop(0)
 raise AssertionError(a)
if name=='git' and a==['show','HEAD:flake.lock']:
 event('committed_snapshot'); print((r/'committed.lock').read_text(),end=''); stop(0)
if name=='git' and a[:1]==['push']:
 assert a==['push','origin','master']; event('push'); stop(1 if case=='remote_moved' else 0)
if name=='bundle' and a==['exec','rake','spec']:
 event('dependency_checks')
 if case in ('dependency_regression','worktree_drift'): Path('flake.lock').write_text(json.dumps(dict(generation=-1)))
 if case=='dependency_regression': (r/'committed.lock').write_text(json.dumps(dict(generation=-1)))
if name=='bundix':
 Path('gemset.nix').write_text('source = fixture;\n'); Path('Gemfile.lock').write_text('fixture')
stop(0)
'''

def workflow(project):
    path=ROOT/'worktrees'/SLUG/project/'.github/workflows/daily-update.yml'
    env={k:v for k,v in os.environ.items() if not(k.startswith('BUNDLE') or k.startswith('GEM_') or k in ('RUBYOPT','RUBYLIB'))}
    result=subprocess.run([shutil.which('ruby'),'-ryaml','-rjson','-e','puts JSON.generate(YAML.load_file(ARGV[0]))',str(path)],env=env,capture_output=True,text=True,check=True)
    data=json.loads(result.stdout)
    assert data['env']['CONFCTL_FLAKE']==PIN and data['env']['GITHUB_TOKEN']=='${{ secrets.GITHUB_TOKEN }}'
    steps=data['jobs']['update']['steps']
    assert steps[0]['with']=={'fetch-depth':0,'ref':'master'} and steps[1]['name']=='Save input baseline'
    for step in steps:
        if 'run' in step:
            subprocess.run(['bash','-n'],input=step['run'],text=True,check=True)
            assert 'nix develop -c confctl' not in step['run']
    return steps

def run(project):
    steps=workflow(project); vpsfree=project.startswith('vpsfree-')
    cases=['success','reject_first','reject_late','error_late','final_reject','final_error','remote_moved','hook_failure']
    if vpsfree: cases+=['llm_same','llm_mismatch','dependency_regression','worktree_drift']
    for case in cases:
        with tempfile.TemporaryDirectory(prefix='confctl-d-workflow-') as temp:
            root=pathlib.Path(temp); checkout=root/'checkout'; checkout.mkdir(); runner=root/'runner'; runner.mkdir(); bins=root/'bin'; bins.mkdir()
            fake=bins/'fixture'; fake.write_text(FAKE); fake.chmod(0o755)
            for tool in ('nix','confctl','git','sudo','bundle','gem','bundix','nixfmt','bundler-audit'): (bins/tool).symlink_to(fake)
            for pkg in ('geminabox','ssh-exporter','syslog-exporter'): (checkout/'packages'/pkg).mkdir(parents=True)
            (runner/'committed.lock').write_text(json.dumps(dict(generation=0)))
            (checkout/'flake.lock').write_text(json.dumps(dict(generation=0))); (checkout/'Gemfile.lock').write_text('fixture')
            env=dict(os.environ,PATH=str(bins)+os.pathsep+os.environ['PATH'],RUNNER_TEMP=str(runner),CONFCTL_FLAKE=PIN,GITHUB_TOKEN='fixture-token',CASE=case,LAST_UPDATE='4' if vpsfree else '2')
            for step in steps:
                if 'run' not in step: continue
                result=subprocess.run(['bash','--noprofile','--norc','-e','-o','pipefail','-c',step['run']],cwd=checkout,env=env,text=True,capture_output=True)
                if result.returncode: break
            events=[json.loads(x) for x in (runner/'events').read_text().splitlines()]; kinds=[x['kind'] for x in events]; updates=[x['args'] for x in events if x['kind']=='update']
            if case in ('success','llm_same','worktree_drift'):
                assert result.returncode==0,(project,case,result.stderr)
                assert kinds[-1]=='push' and kinds.count('final_check')==1
                assert len(updates)==(3 if case=='llm_same' else int(env['LAST_UPDATE']))
            else:
                expected=3 if case in ('reject_first','reject_late','final_reject','dependency_regression') else 1
                assert result.returncode==expected,(project,case,result.returncode,result.stderr)
                assert ('push' in kinds)==(case=='remote_moved'),(project,case,kinds)
            if case in ('reject_first','reject_late','error_late','llm_mismatch','hook_failure'): assert 'final_check' not in kinds and 'dependency_checks' not in kinds
            if case in ('reject_late','error_late','hook_failure'): assert 'local_commit' in kinds
            if case in ('dependency_regression','worktree_drift'): assert kinds.index('dependency_checks')<kinds.index('committed_snapshot')<kinds.index('final_check')
            if 'final_check' in kinds: assert kinds.count('committed_snapshot')==1
            if updates:
                assert updates[0][:6]==['inputs','channel','update','--forward-only','--commit','--no-changelog']
                if vpsfree:
                    assert updates[0][-2:]==['{nixos-stable,production,staging}','nixpkgs']
                    if len(updates)>1: assert updates[1][-1]=='nixos-unstable'
                    if len(updates)>2: assert updates[2][-2:]==['{staging,os-staging}','vpsadminos'] and '--no-changelog' not in updates[2]
                    if len(updates)>3: assert updates[3][-1]=='llm-agents' and '--no-changelog' in updates[3]
                else:
                    assert updates[0][-1]=='nixos-stable'
                    if len(updates)>1: assert updates[1][-1]=='os-staging' and '--no-changelog' not in updates[1]
            print(f'{project}: {case} passed (exit {result.returncode})')
    return len(cases)

if __name__=='__main__':
    count=sum(run(p) for p in (sys.argv[1:] or ('vpsfree-cz-configuration','vpsadminos-org-configuration')))
    print(f'{count} workflow execution scenarios passed; YAML parse and Bash syntax passed.')
