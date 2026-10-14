const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const [sourceRoot, metadataPath, descriptorPath, outputRoot] = process.argv.slice(2);
const { Connection, openLease, readConnection } = require(path.join(sourceRoot, 'lib/connection.cjs'));
const { inventoryIdentity } = require(path.join(sourceRoot, 'fixtures/prepare.cjs'));
async function main() {
  const source = JSON.parse(fs.readFileSync(metadataPath));
  const { value, digest } = readConnection(descriptorPath, ['ip-inventory']);
  const fixturePaths = fs.readdirSync(path.join(outputRoot, 'tmp')).filter(n => /^capture-/.test(n))
    .map(n => path.join(outputRoot, 'tmp', n, 'fixtures.json')).filter(n => fs.existsSync(n));
  assert(fixturePaths.length >= 3, 'three completed capture fixture records required');
  const fixtures = fixturePaths.map(n => {
    const s = fs.lstatSync(n);
    assert(s.isFile() && !s.isSymbolicLink() && s.uid === process.getuid()
      && (s.mode & 0o777) === 0o600 && s.size <= 2 * 1024 * 1024);
    return JSON.parse(fs.readFileSync(n));
  });
  const f = fixtures[0];
  for (const name of ['inventoryVpsId', 'disabledNetworkId', 'disabledIpId']) {
    assert(Number.isInteger(f[name]) && f[name] > 0);
    assert(fixtures.every(x => x[name] === f[name]));
  }
  const lease = await openLease([...value.control.argv, '--instance-id', value.instance_id,
    '--run-id', value.run_id, '--artifact-id', value.artifact_id,
    '--artifact-sha256', value.artifact_sha256, '--descriptor-sha256', digest],
    { schema: 1, instance_id: value.instance_id, run_id: value.run_id,
      artifact_id: value.artifact_id, artifact_sha256: value.artifact_sha256, descriptor_sha256: digest });
  try {
    const connection = new Connection(value, lease);
    await connection.verify(source);
    const { member, adminApi } = await inventoryIdentity(connection);
    const vps = (await adminApi('GET', `vpses/${f.inventoryVpsId}`)).vps;
    const resources = {};
    for (const [name, expected] of Object.entries({ cpu: 1, memory: 1024, swap: 0, diskspace: 4096 })) {
      assert(typeof vps[name] === 'number' && Number.isInteger(vps[name]) && vps[name] === expected,
        'fixture resource must be the exact typed numeric result');
      resources[name] = vps[name];
    }
    const id = v => v && typeof v === 'object' ? v.id : v;
    assert(vps.hostname === 'ip-inventory' && id(vps.user) === member.id);
    const network = (await adminApi('GET', `networks/${f.disabledNetworkId}`)).network;
    const ip = (await adminApi('GET', `ip_addresses/${f.disabledIpId}`)).ip_address;
    assert(network.enabled === false && network.address === '203.0.113.0');
    assert(ip.addr === '203.0.113.10' && ip.network_interface === null
      && id(ip.user) === member.id && id(ip.network) === network.id);
    lease.assertLive();
    process.stdout.write(JSON.stringify({ schema: 1, generator: source.revision,
      instance_id: value.instance_id, run_id: value.run_id, artifact_id: value.artifact_id,
      artifact_sha256: value.artifact_sha256, inventory_vps_id: f.inventoryVpsId,
      typed_resources: resources, disabled_network_id: network.id, disabled_address_id: ip.id,
      network_enabled: network.enabled, detached: true, member_id: member.id,
      read_only: true, actual_numeric_result: true }) + '\n');
  } finally { await lease.close(); }
}
main().catch(() => { process.stderr.write('Read-only typed inventory proof refused\n'); process.exitCode = 1; });
