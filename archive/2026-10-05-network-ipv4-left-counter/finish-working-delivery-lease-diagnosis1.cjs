// Observe the existing public lease helper; retain controller stderr privately.
const fs = require('node:fs');
const path = require('node:path');
const cp = require('node:child_process');
const selection = JSON.parse(fs.readFileSync(process.argv[2]));
const context = process.argv[5];
const originalSpawn = cp.spawn;
let index = 0;
cp.spawn = function (...args) {
  const child = originalSpawn.apply(this, args);
  const file = path.join(context, `controller-${++index}.stderr`);
  const fd = fs.openSync(file, 'wx', 0o600);
  let size = 0;
  child.stderr.on('data', bytes => {
    const retained = bytes.subarray(0, Math.max(0, 16384 - size));
    if (retained.length) fs.writeSync(fd, retained);
    size += retained.length;
  });
  child.once('close', (code, signal) => {
    fs.closeSync(fd);
    fs.writeFileSync(path.join(context, `controller-${index}.status.json`), JSON.stringify({code, signal, retained_stderr_bytes:size}), {flag:'wx', mode:0o600});
  });
  return child;
};
const { main } = require(path.join(selection.source, 'tools/verify-live-lease.cjs'));
main([process.argv[3], selection.metadata, selection.runtime, process.argv[4], path.join(path.dirname(process.argv[4]), 'config.json')])
  .then(() => { process.stdout.write('Separate public lease diagnostic succeeded\n'); })
  .catch(error => { process.stderr.write(error.message + '\n'); process.exitCode = 1; });
