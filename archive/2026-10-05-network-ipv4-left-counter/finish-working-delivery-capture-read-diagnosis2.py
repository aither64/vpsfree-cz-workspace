"""One read-only diagnosis of the capture's original lease/browser consumers."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

os.umask(0o077)
tracking = Path(__file__).resolve().parent
prep = json.loads((tracking / 'finish-working-delivery-capture-read-diagnosis2-preparation.json').read_text())
packet = json.loads(Path(prep['packet_path']).read_text())
context = Path(prep['context']) / 'operation'
context.mkdir(mode=0o700)
selection = json.loads((tracking / 'finish-working-delivery-package-realize3-acceptance.json').read_text())['selection']
root = Path(packet['campaign_root'])
cycle = json.loads((tracking / 'finish-working-delivery-public-continuity5-proof.json').read_text())
failed = root / 'receipts/runtime-smoke-attempt.json'
records = []

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def call(name, argv):
    with (context / (name + '.stdout')).open('xb') as out, (context / (name + '.stderr')).open('xb') as err:
        result = subprocess.run(argv, stdin=subprocess.DEVNULL, stdout=out, stderr=err,
                                env=packet['environment'], cwd=packet['cwd'])
    records.append({'name': name, 'exit_code': result.returncode,
                    'stdout_sha256': sha(context / (name + '.stdout')),
                    'stderr_sha256': sha(context / (name + '.stderr'))})
    return result.returncode, (context / (name + '.stdout')).read_bytes()

code, raw = call('connection', [selection['runtime'] + '/bin/vpsfree-kb-devcluster',
                              '--state-root', str(root / 'state'), 'connection', 'same-slug'])
assert code == 0
value = json.loads(raw)
assert value['provenance']['source'] == json.loads(Path(selection['metadata']).read_text())
assert all(value[key] == cycle['resumed'][key] for key in ('instance_id', 'run_id', 'artifact_id', 'artifact_sha256'))
connection = context / 'connection.json'
connection.write_bytes(raw)
script = r'''
const fs = require('fs'); const path = require('path');
const [source, descriptor, metadata, output] = process.argv.slice(1);
const {readConnection, openLease, Connection} = require(path.join(source, 'lib/connection.cjs'));
const {launchBrowser, login} = require(path.join(source, 'lib/browser.cjs'));
let lease, browser, stage = 'read-connection', failure, closed = false;
const events = [];
const event = value => { stage = value; events.push({stage:value, at:new Date().toISOString()}); };
(async () => {
 try {
  const {value, digest} = readConnection(descriptor, ['ip-inventory']);
  event('public-lease');
  lease = await openLease([...value.control.argv, '--instance-id', value.instance_id, '--run-id', value.run_id,
    '--artifact-id', value.artifact_id, '--artifact-sha256', value.artifact_sha256, '--descriptor-sha256', digest],
    {schema:1, instance_id:value.instance_id, run_id:value.run_id, artifact_id:value.artifact_id,
     artifact_sha256:value.artifact_sha256, descriptor_sha256:digest});
  const cluster = new Connection(value, lease);
  const original = cluster.ssh.bind(cluster);
  cluster.ssh = async (machine, command, options) => {
    event('leased-ssh-' + machine + '-' + command[0]);
    return original(machine, command, options);
  };
  event('source-verification');
  await cluster.verify(JSON.parse(fs.readFileSync(metadata)));
  event('browser-launch');
  browser = await launchBrowser(cluster, {width:1440,height:1100}, 'cs');
  event('page-create');
  const page = await browser.context.newPage();
  event('ordinary-member-login');
  await login(page, cluster, 'cs');
  event('inventory-api-identity');
  const {inventoryIdentity, assertInventoryMember} = require(path.join(source, 'fixtures/prepare.cjs'));
  const {goto} = require(path.join(source, 'lib/webui.cjs'));
  const {member} = await inventoryIdentity(cluster);
  event('inventory-member-session');
  await assertInventoryMember(page, member);
  event('new-vps-form-read');
  await goto(page, `/?page=adminvps&action=new-step-1&user=${member.id}`);
  const forms = await page.locator('form[name="newvps-step1"], form[name="newvps-step2"]').count();
  if (forms < 1) throw new Error('Expected ordinary-member VPS creation form is absent');
  event('read-only-complete');
 } catch(error) {
  failure = {stage, error_class:error.constructor.name};
  fs.writeFileSync(path.join(output,'private-exception.txt'), String(error.stack || error).slice(0,16384), {mode:0o600,flag:'wx'});
 } finally {
  try { if(browser) await browser.close(); }
  finally { try { if(lease) await lease.close(); closed = true; }
    catch(error) { failure ||= {stage:'lease-cleanup',error_class:error.constructor.name}; } }
  fs.writeFileSync(path.join(output,'diagnosis.json'), JSON.stringify({complete:!failure,failure,events,closed,
    fixture_or_lifecycle_mutation:false},null,2), {mode:0o600,flag:'wx'});
  process.exitCode = failure ? 1 : 0;
 }
})();
'''
code, _ = call('read-only-consumers', ['node', '-e', script, selection['source'], str(connection),
                                     selection['metadata'], str(context)])
diagnosis = json.loads((context / 'diagnosis.json').read_text())
assert sha(failed) == cycle['original_failed_attempt_sha256']
proof = {'schema': 1, 'generator': prep['generator'], 'complete': code == 0,
         'diagnosis': diagnosis, 'commands': records, 'source_ids': {key:value[key] for key in
         ('instance_id', 'run_id', 'artifact_id', 'artifact_sha256')},
         'original_failed_attempt_sha256': sha(failed), 'original_campaign_completed': False}
with (tracking / 'finish-working-delivery-capture-read-diagnosis2-proof.json').open('x') as out:
    json.dump(proof, out, indent=2); out.write('\n')
print(json.dumps({'complete': code == 0, 'failure':diagnosis.get('failure'), 'closed':diagnosis['closed'],
                  'fixture_or_lifecycle_mutation':False}), flush=True)
sys.exit(code)
