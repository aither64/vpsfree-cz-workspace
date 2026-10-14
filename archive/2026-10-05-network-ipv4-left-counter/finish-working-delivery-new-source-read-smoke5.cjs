const fs = require('node:fs');
const path = require('node:path');
const { Connection, openLease, readConnection } = require(path.join(process.argv[3], 'lib/connection.cjs'));
const { launchBrowser, login } = require(path.join(process.argv[3], 'lib/browser.cjs'));
const { goto } = require(path.join(process.argv[3], 'lib/webui.cjs'));
const { inventoryIdentity, assertInventoryMember } = require(path.join(process.argv[3], 'fixtures/prepare.cjs'));
async function main() {
  const { value, digest } = readConnection(process.argv[1], ['ip-inventory']);
  const source = JSON.parse(fs.readFileSync(process.argv[2]));
  const expected = { schema: 1, instance_id: value.instance_id, run_id: value.run_id,
    artifact_id: value.artifact_id, artifact_sha256: value.artifact_sha256, descriptor_sha256: digest };
  const argv = [...value.control.argv, '--instance-id', value.instance_id, '--run-id', value.run_id,
    '--artifact-id', value.artifact_id, '--artifact-sha256', value.artifact_sha256, '--descriptor-sha256', digest];
  const lease = await openLease(argv, expected);
  let browser;
  try {
    const connection = new Connection(value, lease);
    await connection.verify(source);
    const { member } = await inventoryIdentity(connection);
    browser = await launchBrowser(connection, { width: 1280, height: 800 }, 'en');
    const page = await browser.context.newPage();
    await login(page, connection, 'en');
    await goto(page, '/?page=adminvps&action=list');
    await assertInventoryMember(page, member);
    lease.assertLive();
    process.stdout.write(JSON.stringify({ member, api_tls_verified: true, php_member_read: true,
      page: '/?page=adminvps&action=list', instance_id: value.instance_id, run_id: value.run_id }) + '\n');
  } finally {
    try { if (browser) await browser.close(); } finally { await lease.close(); }
  }
}
main().catch((error) => { process.stderr.write(`${error.message}\n`); process.exitCode = 1; });
