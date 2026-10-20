import datetime
import hashlib
import json
import os
import subprocess
from pathlib import Path

OUT = Path(__file__).parent
BASE = '3fab2eaff537024f8ec32db6cdb3b0546808420d'
CVES = ['CVE-2026-53260', 'CVE-2026-72069', 'CVE-2026-64387']
EVIDENCE = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
RAW = Path('.state/editorial-scope-followup')
RAW.mkdir(mode=0o700, exist_ok=True)
RAW.chmod(0o700)
checks = []


def guard():
    assert subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip() == BASE
    assert not subprocess.check_output(['git', 'diff', '--cached', '--name-only']).strip()
    assert hashlib.sha256(Path('.state/evidence.json').read_bytes()).hexdigest() == EVIDENCE


def run(name, args, target=None):
    guard()
    log = target or OUT / (name + '.log')
    with log.open('w') as stream:
        result = subprocess.run(args, stdout=stream, stderr=subprocess.STDOUT)
    if target:
        log.chmod(0o600)
    checks.append({'name': name, 'args': args, 'exit_code': result.returncode, 'log': str(log)})
    print(f'{name}: exit {result.returncode}', flush=True)
    assert result.returncode == 0, f'{name} failed; inspect retained log; no automatic retry'
    guard()


assert os.environ.get('IN_NIX_SHELL')
guard()
run('validate3', ['bin/security-advisory', 'validate', *CVES])
for cve in CVES:
    run('evaluate-' + cve, ['bin/security-advisory', 'evaluate', cve], RAW / (cve + '.json'))
run('comparison', ['python3', str(OUT / 'verify.py')])
run('dossiers-spec', ['bundle', 'exec', 'rspec', 'spec/dossiers_spec.rb'])
run('dossiers-lint', ['bundle', 'exec', 'rubocop', '--force-exclusion', 'spec/dossiers_spec.rb'])
code = 'r = SecurityAdvisories::Reconciler.new(client: nil); ARGV.each { |cve| a = SecurityAdvisories::Advisory.load(cve); r.load_evaluation(a); puts "#{cve}: digest-bound evaluation accepted" }'
run('final-loader3', ['bundle', 'exec', 'ruby', '-r', './lib/security_advisories', '-e', code, *CVES])
comparison = json.loads((OUT / 'comparison.json').read_text())
receipt = {'recorded_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'base': BASE, 'status': 'technical-ready-awaiting-Git-release', 'checks': checks, 'comparison': comparison, 'no_API_calls': True, 'no_index_or_ref_mutation': True, 'no_runtime_predicate_schema_or_version_changes': True}
(OUT / 'ready-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print('READY: validation3/evaluation3/complete-comparison/dossiers-spec/lint/loader3 PASS; Git slot not exercised.', flush=True)
