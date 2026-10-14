const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const [sourceRoot, metadataPath, descriptorPath] = process.argv.slice(2);
const { Connection, openLease, readConnection } = require(path.join(sourceRoot, 'lib/connection.cjs'));
const { inventoryIdentity } = require(path.join(sourceRoot, 'fixtures/prepare.cjs'));
async function main() {
  const metadata=JSON.parse(fs.readFileSync(metadataPath));
  const {value,digest}=readConnection(descriptorPath,['ip-inventory']);
  const lease=await openLease([...value.control.argv,'--instance-id',value.instance_id,'--run-id',value.run_id,'--artifact-id',value.artifact_id,'--artifact-sha256',value.artifact_sha256,'--descriptor-sha256',digest],{schema:1,instance_id:value.instance_id,run_id:value.run_id,artifact_id:value.artifact_id,artifact_sha256:value.artifact_sha256,descriptor_sha256:digest});
  try {
    const connection=new Connection(value,lease); await connection.verify(metadata);
    const {adminApi}=await inventoryIdentity(connection);
    const networks=(await adminApi('GET','networks?network%5Blimit%5D=1000')).networks;
    const pools=networks.filter(n=>n.address==='203.0.113.0' && n.label==='Documentation disabled inventory');
    assert.equal(pools.length,1);
    const pool=pools[0];
    const locations=(await adminApi('GET',`location_networks?location_network%5Bnetwork%5D=${pool.id}&location_network%5Blimit%5D=1000`)).location_networks;
    lease.assertLive();
    process.stdout.write(JSON.stringify({schema:1,read_only:true,generator:metadata.revision,instance_id:value.instance_id,run_id:value.run_id,artifact_id:value.artifact_id,network_id:pool.id,network_enabled:pool.enabled,location_associations:locations.map(x=>({id:x.id,primary:x.primary,autopick:x.autopick,userpick:x.userpick,types:{primary:x.primary===null?'null':typeof x.primary,autopick:typeof x.autopick,userpick:typeof x.userpick}}))})+'\n');
  } finally {await lease.close();}
}
main().catch(()=>{process.stderr.write('Read-only location flag observation refused\n');process.exitCode=1;});
