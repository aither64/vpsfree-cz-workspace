import concurrent.futures, json, pathlib, subprocess, time
root=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz')
out=root/'work/2026-10-16-idle-coordination-worker'
wt=root/'worktrees/2026-10-16-idle-coordination-worker'
heads=json.loads((out/'compat-final-heads.json').read_text())
results={}
def run(name, repo, args):
    cwd=wt/repo
    assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=cwd,text=True).strip()==heads[repo]['head']
    assert not subprocess.check_output(['git','status','--porcelain'],cwd=cwd,text=True)
    start=time.monotonic()
    with (out/(name+'.log')).open('w') as log:
        status=subprocess.run(args,cwd=cwd,stdout=log,stderr=subprocess.STDOUT).returncode
    result={'revision':heads[repo]['head'],'exitStatus':status,'seconds':round(time.monotonic()-start,2),'command':args}
    (out/(name+'.status')).write_text(str(status)+'\n')
    (out/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(name,json.dumps(result),flush=True)
    return result
commands=[
('compat-runtime-package','dev-workspace',['nix','build','--print-build-logs','--out-link',str(out/'compat-runtime-result'),'.#checks.x86_64-linux.package','.#checks.x86_64-linux.host-package-contract']),
('compat-workspace-build','workspace',['nix','build','--print-build-logs','--out-link',str(out/'compat-workspace-result'),'.#packages.x86_64-linux.default','.#checks.x86_64-linux.deployment-contract','.#checks.x86_64-linux.agent-instructions']),
('compat-system-build','vpsfree-cz-configuration',['nix','develop','--command','confctl','build','--yes','cz.vpsfree/machines/aitherdev']),
('compat-systemd','dev-workspace',['nix','develop','--command','ruby','test/background_integration_systemd_test.rb','-n','/systemd/']),
('compat-ci','dev-workspace',['nix','shell','--inputs-from','.','nixpkgs#gh','-c','gh','run','watch','39014845298','--repo','aither64/dev-workspace','--exit-status'])]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    pending={pool.submit(run,*c):c[0] for c in commands}
    for future in concurrent.futures.as_completed(pending):results[pending[future]]=future.result()
if results['compat-runtime-package']['exitStatus']==0:
    package=subprocess.check_output(['nix','eval','--raw','.#checks.x86_64-linux.package.outPath'],cwd=wt/'dev-workspace',text=True).strip()
    (out/'compat-runtime-package.path').write_text(package+'\n')
    results['compat-native']=run('compat-native','dev-workspace',['nix','develop','--command','go','-C','portal','run','-mod=readonly',str(out/'native-notification-check.go'),package])
results['compat-notification-protocol']=run('compat-notification-protocol','dev-workspace',['nix','develop','--command','go','-C','portal','test','-mod=readonly','./cmd/workspace-portal','-run','^TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery$','-count=1'])
(out/'compat-verification-results.json').write_text(json.dumps(results,indent=2)+'\n')
raise SystemExit(0 if all(v['exitStatus']==0 for v in results.values()) else 1)
