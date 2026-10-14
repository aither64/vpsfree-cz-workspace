const fs = require('node:fs'); const path = require('node:path'); const assert = require('node:assert/strict');
const [sourceRoot, metadataPath, descriptorPath] = process.argv.slice(2);
const { Connection, openLease, readConnection } = require(path.join(sourceRoot, 'lib/connection.cjs'));
const { inventoryIdentity, INVENTORY_POOL, INVENTORY_RESOURCES } = require(path.join(sourceRoot, 'fixtures/prepare.cjs'));
async function main() {
 const source=JSON.parse(fs.readFileSync(metadataPath)); const {value,digest}=readConnection(descriptorPath,['ip-inventory']);
 const lease=await openLease([...value.control.argv,'--instance-id',value.instance_id,'--run-id',value.run_id,'--artifact-id',value.artifact_id,'--artifact-sha256',value.artifact_sha256,'--descriptor-sha256',digest],{schema:1,instance_id:value.instance_id,run_id:value.run_id,artifact_id:value.artifact_id,artifact_sha256:value.artifact_sha256,descriptor_sha256:digest});
 try {
  const c=new Connection(value,lease); await c.verify(source); const {member,adminApi:api}=await inventoryIdentity(c);
  const id=v=>v&&typeof v==='object'?v.id:v;
  const rows=(await api('GET','vpses?_meta%5Blimit%5D=1000')).vpses;
  const selected=rows.filter(v=>v.hostname==='ip-inventory'&&id(v.user)===member.id);
  assert(selected.length===1); const v=selected[0]; const typed={};
  for (const [k,expected] of Object.entries(INVENTORY_RESOURCES)){assert(typeof v[k]==='number'&&Number.isInteger(v[k])&&v[k]===expected);typed[k]=v[k];}
  const pools=(await api('GET','networks?_meta%5Blimit%5D=1000')).networks.filter(n=>n.address===INVENTORY_POOL.address&&n.label===INVENTORY_POOL.label);assert(pools.length===1);const pool=pools[0];
  const flat=(await api('GET',`location_networks?network=${pool.id}&limit=1000`)).location_networks;
  const correct=(await api('GET',`location_networks?location_network%5Bnetwork%5D=${pool.id}&_meta%5Blimit%5D=1000`)).location_networks;
  assert(correct.every(n=>id(n.network)===pool.id));assert(flat.some(n=>id(n.network)!==pool.id));
  lease.assertLive(); process.stdout.write(JSON.stringify({schema:1,generator:source.revision,instance_id:value.instance_id,run_id:value.run_id,artifact_id:value.artifact_id,artifact_sha256:value.artifact_sha256,inventory_vps_id:v.id,typed_resources:typed,actual_numeric_result:true,network_id:pool.id,network_enabled:pool.enabled,flat_location_network_count:flat.length,namespaced_location_network_count:correct.length,flat_includes_unrelated_network:true,namespaced_only_target_network:true,read_only:true})+'\n');
 } finally {await lease.close();}
}
main().catch(()=>{process.stderr.write('Read-only inventory query comparison refused\n');process.exitCode=1;});
