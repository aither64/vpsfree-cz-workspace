import json, os, pathlib, subprocess, time
root = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz')
slug = '2026-10-14-integration-performance'
tracking = root / 'work' / slug
worktrees = root / 'worktrees' / slug
inventory = json.loads((tracking / 'review-inventory.json').read_text())
results = []

def run(name, project, command):
    path = worktrees / project
    actual = subprocess.check_output(['git', '-C', str(path), 'rev-parse', 'HEAD'], text=True).strip()
    if actual != inventory[project]['head']:
        raise RuntimeError('tested head changed: ' + project)
    start = time.monotonic()
    logfile = tracking / (name + '.log')
    env = os.environ.copy()
    env.update(DEV_SESSION_SLUG=slug, DEV_SESSION_WORKSPACE=str(root))
    with logfile.open('w') as log:
        process = subprocess.run(command, cwd=path, env=env, stdout=log, stderr=subprocess.STDOUT)
    result = dict(name=name, project=project, head=actual, command=command, exitStatus=process.returncode,
                  seconds=time.monotonic()-start, log=str(logfile))
    results.append(result)
    (tracking / 'verification-results.json').write_text(json.dumps(results, indent=2)+'\n')
    print(json.dumps(result), flush=True)
    if process.returncode:
        raise SystemExit(process.returncode)

start = time.monotonic()
run('runtime-evaluate', 'dev-workspace', ['nix','flake','check','--no-build','--print-build-logs'])
# Ruby shards run as dependencies; package runs Go and browser regressions.
checks = json.loads(subprocess.check_output(['nix','eval','--json','.#checks.x86_64-linux','--apply','builtins.attrNames'], cwd=worktrees/'dev-workspace', text=True))
checks = [check for check in checks if check not in ['host-module-idempotency','session-recovery-boot']]
run('runtime-package-checks', 'dev-workspace', ['nix','build','--no-link','--print-build-logs'] + ['.#checks.x86_64-linux.'+check for check in checks])
run('extension-checks', 'vpsfree-dev-workspace', ['nix','flake','check','--print-build-logs'])
run('workspace-checks', 'workspace', ['nix','flake','check','--print-build-logs'])
run('workspace-build', 'workspace', ['nix','build','--no-link','--print-out-paths','--print-build-logs'])
run('aitherdev-build', 'vpsfree-cz-configuration', ['nix','develop','-c','confctl','build','--yes','cz.vpsfree/machines/aitherdev'])
print(json.dumps({'verificationPreparationSeconds':time.monotonic()-start}), flush=True)
for index in range(1,4):
    os.environ['INTEGRATION_BENCHMARK_SOURCE'] = str(worktrees/'dev-workspace')
    os.environ['INTEGRATION_BENCHMARK_OUTPUT'] = str(tracking/('driver-benchmark-'+str(index)+'.json'))
    run('driver-benchmark-'+str(index), 'dev-workspace', ['nix','develop','-c','ruby',str(tracking/'benchmark-driver.rb'),'--name','/test_driver_resumes_original_jobs_and_exports_compact_results/'])
    # Comparable warm-cache runs. Fresh verification above has its own timing.
    run('warm-workspace-'+str(index), 'workspace', ['nix','build','--no-link','--print-out-paths'])
    run('warm-aitherdev-'+str(index), 'vpsfree-cz-configuration', ['nix','develop','-c','confctl','build','--yes','cz.vpsfree/machines/aitherdev'])
run('runtime-ci', 'dev-workspace', ['nix','shell','--inputs-from','.','nixpkgs#gh','-c','gh','run','watch','38647942844','--repo','aither64/dev-workspace','--exit-status'])
