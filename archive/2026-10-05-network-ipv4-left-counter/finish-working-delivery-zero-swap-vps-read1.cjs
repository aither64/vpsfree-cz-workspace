// Operator preparation using the genuine generator's exported public consumers.
const fs = require('fs');
const path = require('path');
const [source, descriptor, metadata, resultFile, errorFile] = process.argv.slice(2);
const { readConnection, openLease, Connection } = require(path.join(source, 'lib/connection.cjs'));
const { launchBrowser, login } = require(path.join(source, 'lib/browser.cjs'));
const { inventoryIdentity, inventoryApi, assertInventoryMember, createVpsIn, INVENTORY_RESOURCES } = require(path.join(source, 'fixtures/prepare.cjs'));
const { goto, preparePage, submitLast, selectRadioByRowText, DEFAULT_OS_TEMPLATE } = require(path.join(source, 'lib/webui.cjs'));
let lease, browser, stage = 'read-connection', createdVps = null, failure;
const result = { complete: false, actual_resource_proof: null, created_vps_id: null };
const check = (value, label) => { if (!value) throw new Error(label); };
const resourceId = value => value && typeof value === 'object' ? value.id : value;
(async () => {
  try {
    const { value, digest } = readConnection(descriptor, ['ip-inventory']);
    stage = 'public-lease-source-proof';
    lease = await openLease([...value.control.argv, '--instance-id', value.instance_id, '--run-id', value.run_id,
      '--artifact-id', value.artifact_id, '--artifact-sha256', value.artifact_sha256, '--descriptor-sha256', digest],
      { schema: 1, instance_id: value.instance_id, run_id: value.run_id, artifact_id: value.artifact_id,
        artifact_sha256: value.artifact_sha256, descriptor_sha256: digest });
    const cluster = new Connection(value, lease);
    await cluster.verify(JSON.parse(fs.readFileSync(metadata)));
    stage = 'ordinary-member-identity';
    browser = await launchBrowser(cluster, { width: 1440, height: 1100 }, 'cs');
    const page = await browser.context.newPage();
    await login(page, cluster, 'cs');
    const { member } = await inventoryIdentity(cluster);
    await assertInventoryMember(page, member);
    const api = inventoryApi(cluster, 'test-user1');
    stage = 'owned-name-and-zero-swap-allocation';
    const existing = (await api('GET', 'vpses?limit=1000')).vpses;
    check(Array.isArray(existing) && existing.length < 1000, 'Bounded member VPS inventory required');
    check(!existing.some(vps => vps.hostname === 'ip-inventory'), 'Existing inventory VPS requires separate disposition');
    const allocations = (await api('GET', `users/${member.id}/cluster_resources?limit=1000&meta%5Bincludes%5D=cluster_resource%2Cenvironment`)).cluster_resources;
    check(Array.isArray(allocations) && allocations.length < 1000, 'Bounded member resource allocation required');
    const swap = allocations.filter(row => row.cluster_resource?.name === 'swap' && row.environment?.label === 'Production');
    check(swap.length === 1 && swap[0].value === 0, 'Exact zero-swap member allocation required');
    check(INVENTORY_RESOURCES.swap === 0 && INVENTORY_RESOURCES.cpu === 1 && INVENTORY_RESOURCES.memory === 1024 && INVENTORY_RESOURCES.diskspace === 4096, 'Original inventory resource tuple differs');

    // These GET-form steps inspect the exact omitted control before creation.
    stage = 'rendered-creation-resource-contract';
    await goto(page, `/?page=adminvps&action=new-step-1&user=${member.id}`);
    const environment = page.locator('form[name="newvps-step1"]');
    if (await environment.count()) {
      const row = environment.locator('tr', { hasText: 'Production' });
      check(await row.count() === 1, 'Unique Production environment required');
      await row.locator('input[type="radio"][name="environment"]').check({ force: true });
      await submitLast(environment);
      await page.waitForLoadState('domcontentloaded');
      await preparePage(page);
    }
    let form = page.locator('form[name="newvps-step2"]');
    const location = form.locator('tr', { hasText: 'Praha' });
    check(await location.count() === 1, 'Unique Praha location required');
    await location.locator('input[type="radio"][name="location"]').check({ force: true });
    await submitLast(form);
    await page.waitForLoadState('domcontentloaded');
    await preparePage(page);
    form = page.locator('form[name="newvps-step2"]');
    await selectRadioByRowText(form, 'os_template', DEFAULT_OS_TEMPLATE);
    await submitLast(form);
    await page.waitForLoadState('domcontentloaded');
    await preparePage(page);
    form = page.locator('form[name="newvps-step3"]');
    check(await form.count() === 1 && await form.locator('input[name="swap"]').count() === 0, 'Zero-allocation swap must be omitted');
    for (const name of ['cpu', 'memory', 'diskspace']) check(await form.locator(`input[name="${name}"]`).count() === 1, 'Required resource control missing or ambiguous');
    await assertInventoryMember(page, member);
    result.read_only_complete = true;
    result.complete = true;
    return;
    stage = 'original-exported-member-ui-creation';
    createdVps = await createVpsIn(page, member.id, 'ip-inventory', true, 'Production', 'Praha',
      { cpu: 1, memory: 1024, diskspace: 4096 });
    result.created_vps_id = createdVps;
    await assertInventoryMember(page, member);
    stage = 'actual-api-owner-and-resource-tuple';
    const vps = (await api('GET', `vpses/${createdVps}`)).vps;
    check(vps && resourceId(vps.user) === member.id && vps.hostname === 'ip-inventory', 'Created fixture owner or identity differs');
    for (const [name, expected] of Object.entries(INVENTORY_RESOURCES)) check(typeof vps[name] === 'number' && vps[name] === expected, 'Created fixture resource tuple differs');
    result.actual_resource_proof = { id: vps.id, owner_id: member.id, hostname: vps.hostname,
      cpu: vps.cpu, memory: vps.memory, swap: vps.swap, diskspace: vps.diskspace };
    result.source_ids = Object.fromEntries(['instance_id', 'run_id', 'artifact_id', 'artifact_sha256'].map(key => [key, value[key]]));
    result.original_exported_helper = true;
    result.omitted_swap_zero_default = true;
    result.complete = true;
  } catch (error) {
    failure = { stage, error_class: error.constructor.name };
    fs.writeFileSync(errorFile, String(error.stack || error).slice(0, 16384), { mode: 0o600, flag: 'wx' });
  } finally {
    try { if (browser) await browser.close(); }
    catch (error) { failure ||= { stage: 'browser-cleanup', error_class: error.constructor.name }; }
    try { if (lease) await lease.close(); }
    catch (error) { failure ||= { stage: 'lease-cleanup', error_class: error.constructor.name }; }
    result.complete = result.complete && !failure;
    result.failure = failure || null;
    result.created_vps_id = createdVps;
    fs.writeFileSync(resultFile, JSON.stringify(result, null, 2), { mode: 0o600, flag: 'wx' });
    process.stdout.write(JSON.stringify({ complete: result.complete, failure }) + '\n');
    process.exitCode = result.complete && !failure ? 0 : 1;
  }
})();
