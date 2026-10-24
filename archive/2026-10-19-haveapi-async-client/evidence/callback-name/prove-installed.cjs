const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const { spawnSync, execFileSync } = require('node:child_process');
const { createRequire } = require('node:module');

const repo = '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-haveapi-async-client/haveapi';
const head = 'f5320eae05cbf8256a40cb04358be876ea7bde75';
const tar = path.join(__dirname, 'package/haveapi-client-0.29.0.tgz');
const tarSha = '23cad7163435c9d2cd51e83b9d6751db895ddbbfb3c586f1343f42f7070e9647';
const git = (...args) => execFileSync('git', args, { cwd: repo });
assert.equal(git('rev-parse', 'HEAD').toString().trim(), head);
assert.equal(git('status', '--porcelain').length, 0);
assert.equal(crypto.createHash('sha256').update(fs.readFileSync(tar)).digest('hex'), tarSha);

const directory = fs.mkdtempSync(path.join(__dirname, 'installed-proof-'));
const receipt = { head, tar, tarSha, directory, status: 'incomplete', operations: [] };
console.log('proof-directory', directory);
function run(label, command, args) {
  const result = spawnSync(command, args, { cwd: directory, encoding: 'utf8', maxBuffer: 16 * 1024 * 1024 });
  const output = (result.stdout || '') + (result.stderr || '');
  fs.writeFileSync(path.join(directory, label + '.log'), output);
  receipt.operations.push({ label, command, args, exit: result.status, signal: result.signal });
  if (result.error) throw result.error;
  assert.equal(result.status, 0, label + ': ' + output.slice(-3000));
  return output;
}
try {
  // A new minimal prefix has no existing dependency graph or lock to drift.
  fs.writeFileSync(path.join(directory, 'package.json'), JSON.stringify({ name: 'haveapi-naming-proof', version: '0.0.0', private: true }));
  run('install', 'npm', ['install', '--ignore-scripts', '--no-save', '--package-lock=false', '--no-audit', '--no-fund', tar]);
  const installedRequire = createRequire(path.join(directory, 'package.json'));
  const main = installedRequire.resolve('haveapi-client');
  const packageRoot = path.join(directory, 'node_modules/haveapi-client');
  assert.equal(main, path.join(packageRoot, 'dist/haveapi-client.js'));
  assert.deepEqual(fs.readFileSync(main), git('show', head + ':clients/js/dist/haveapi-client.js'));
  assert.deepEqual(fs.readFileSync(path.join(packageRoot, 'dist/types/haveapi.d.ts')), git('show', head + ':clients/js/dist/types/haveapi.d.ts'));
  const api = installedRequire('haveapi-client');
  assert.equal(api.CallbackClient, api.Client);
  assert.equal(api.CallbackClient.name, 'Client');
  assert.equal(api.CallbackClient.prototype, api.Client.prototype);
  assert.ok(new api.CallbackClient('https://api.example') instanceof api.Client);
  assert.equal(typeof api.AsyncClient, 'function');
  receipt.actualCommonJSRequire = main;

  // Reuse the committed three loader cases, reading the installed main bytes.
  const fixture = git('show', head + ':clients/js/test/compatibility/callback.spec.cjs').toString();
  const originalPath = "const bundlePath = path.resolve(__dirname, '../../dist/haveapi-client.js');";
  assert.equal(fixture.split(originalPath).length, 2);
  fs.writeFileSync(path.join(directory, 'callback-package.spec.cjs'), fixture.replace(originalPath, "const bundlePath = require.resolve('haveapi-client');"));
  run('loaders', process.execPath, ['--test', '--test-name-pattern', 'retains Client/CallbackClient identity', 'callback-package.spec.cjs']);

  // Only rewrite source import locations; preserve every consumer assertion.
  for (const name of ['callback', 'async']) {
    const source = git('show', head + ':clients/js/test/types/' + name + '.ts').toString();
    const consumer = source.replaceAll("'../../dist/types/haveapi'", "'haveapi-client'")
      .replaceAll("'../../dist/types/haveapi/", "'haveapi-client/dist/types/haveapi/");
    assert.ok(!consumer.includes('../../dist/'));
    fs.writeFileSync(path.join(directory, name + '.ts'), consumer);
    fs.writeFileSync(path.join(directory, name + '.tsconfig.json'), git('show', head + ':clients/js/test/types/' + name + '.tsconfig.json'));
  }
  const tsc = path.join(repo, 'clients/js/node_modules/typescript/bin/tsc');
  for (const name of ['callback', 'async']) {
    const trace = run('types-' + name, process.execPath, [tsc, '-p', name + '.tsconfig.json', '--traceResolution', '--listFiles', '--pretty', 'false']);
    assert.ok(trace.includes(path.join(packageRoot, 'dist/types/haveapi.d.ts')));
    assert.ok(!trace.includes(path.join(repo, 'clients/js/dist/types')));
    assert.ok(!trace.includes(path.join(repo, 'clients/js/src')));
  }
  assert.equal(git('rev-parse', 'HEAD').toString().trim(), head);
  assert.equal(git('status', '--porcelain').length, 0);
  receipt.status = 'passed';
  receipt.sourceClean = true;
  receipt.installedPackageTypes = path.join(packageRoot, 'dist/types/haveapi.d.ts');
  receipt.processes = 'All owned synchronous children exited; fixtures use fake XHR and no servers.';
  console.log('proof-passed', head, tarSha);
} catch (error) {
  receipt.status = 'failed';
  receipt.error = String(error.stack || error);
  console.error(error);
  process.exitCode = 1;
} finally {
  fs.writeFileSync(path.join(directory, 'receipt.json'), JSON.stringify(receipt, null, 2) + '\n');
}
