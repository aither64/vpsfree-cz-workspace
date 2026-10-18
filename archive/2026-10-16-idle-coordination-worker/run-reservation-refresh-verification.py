import concurrent.futures, json, pathlib, subprocess, time
root=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz')
out=root/'work/2026-10-16-idle-coordination-worker'
wt=root/'worktrees/2026-10-16-idle-coordination-worker'
heads=json.loads((out/'reservation-refresh-heads.json').read_text())
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
('reservation-refresh-runtime-package','dev-workspace',['nix','build','--print-build-logs','--out-link',str(out/'reservation-refresh-runtime-result'),'.#checks.x86_64-linux.package','.#checks.x86_64-linux.host-package-contract']),
('reservation-refresh-workspace-build','workspace',['nix','build','--print-build-logs','--out-link',str(out/'reservation-refresh-workspace-result'),'.#packages.x86_64-linux.default','.#checks.x86_64-linux.deployment-contract','.#checks.x86_64-linux.agent-instructions']),
('reservation-refresh-system-build','vpsfree-cz-configuration',['nix','develop','--command','confctl','build','--yes','cz.vpsfree/machines/aitherdev']),
('reservation-refresh-systemd','dev-workspace',['nix','develop','--command','ruby','test/background_integration_systemd_test.rb','-n','/systemd/']),
('reservation-refresh-ci','dev-workspace',['nix','shell','--inputs-from','.','nixpkgs#gh','-c','gh','run','watch','39018599934','--repo','aither64/dev-workspace','--exit-status'])]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    pending={pool.submit(run,*c):c[0] for c in commands}
    for future in concurrent.futures.as_completed(pending):results[pending[future]]=future.result()
if results['reservation-refresh-runtime-package']['exitStatus']==0:
    package=subprocess.check_output(['nix','eval','--raw','.#checks.x86_64-linux.package.outPath'],cwd=wt/'dev-workspace',text=True).strip()
    (out/'reservation-refresh-runtime-package.path').write_text(package+'\n')
    results['reservation-refresh-native']=run('reservation-refresh-native','dev-workspace',['nix','develop','--command','go','-C','portal','run','-mod=readonly',str(out/'native-notification-check.go'),package])
results['reservation-refresh-notification-protocol']=run('reservation-refresh-notification-protocol','dev-workspace',['nix','develop','--command','go','-C','portal','test','-mod=readonly','./cmd/workspace-portal','-run','^TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery$','-count=1'])
(out/'reservation-refresh-verification-results.json').write_text(json.dumps(results,indent=2)+'\n')
raise SystemExit(0 if all(v['exitStatus']==0 for v in results.values()) else 1)
