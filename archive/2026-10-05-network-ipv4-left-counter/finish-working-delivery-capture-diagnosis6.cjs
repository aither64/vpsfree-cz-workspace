const fs = require('node:fs');
const path = require('node:path');
const [source, metadata, output, stateRoot, diagnostic] = process.argv.slice(2);
const { main } = require(path.join(source, 'runner/capture.cjs'));
main({ argv: ['--cluster', 'same-slug', '--state-root', stateRoot, '--output-root', output,
  '--language', 'cs', '--checkpoint', 'networking/ip-address-list'],
  sourceMetadata: JSON.parse(fs.readFileSync(metadata)), defaultOutputRoot: process.cwd(),
  defaultStateRoot: stateRoot }).catch((error) => {
    fs.writeFileSync(diagnostic, JSON.stringify({ name: error.name, message: error.message,
      stack: error.stack }, null, 2), {mode: 0o600, flag: 'wx'});
    process.stderr.write('Exact exported capture core refused; private diagnostic retained.\n');
    process.exitCode = 1;
  });
