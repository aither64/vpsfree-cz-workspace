// One bounded read-only diagnostic through the existing owned public lease.
const fs = require('node:fs');
const path = require('node:path');
const https = require('node:https');
const crypto = require('node:crypto');
const selection = JSON.parse(fs.readFileSync(process.argv[2]));
const { Connection, openLease, readConnection } = require(path.join(selection.source, 'lib/connection.cjs'));
async function main() {
  process.umask(0o077);
  const { value, digest } = readConnection(process.argv[3], ['ip-inventory']);
  const expected = { schema: 1, instance_id: value.instance_id, run_id: value.run_id,
    artifact_id: value.artifact_id, artifact_sha256: value.artifact_sha256, descriptor_sha256: digest };
  const argv = [...value.control.argv, '--instance-id', value.instance_id, '--run-id', value.run_id,
    '--artifact-id', value.artifact_id, '--artifact-sha256', value.artifact_sha256, '--descriptor-sha256', digest];
  const lease = await openLease(argv, expected);
  const reports = [];
  try {
    const connection = new Connection(value, lease);
    await connection.verify(JSON.parse(fs.readFileSync(selection.metadata)));
    const secrets = connection.accounts.map(x => x.password).filter(x => typeof x === 'string' && x);
    const clean = value => {
      if (typeof value !== 'string') return null;
      for (const secret of secrets) value = value.split(secret).join('[REDACTED]');
      return value.slice(0, 512);
    };
    for (const login of ['test-user1', 'test-admin']) {
      connection.assertLease();
      const account = connection.account(login);
      const url = new URL('v7.0/users/current', connection.apiUrl);
      const endpoint = connection.route(url);
      const response = await new Promise((resolve, reject) => {
        const request = https.request({hostname:endpoint.host, port:endpoint.port, servername:url.hostname,
          path:url.pathname + url.search, method:'GET', ca:fs.readFileSync(connection.caPath), signal:lease.signal,
          headers:{Host:url.host, Accept:'application/json', Authorization:'Basic ' + Buffer.from(account.login + ':' + account.password).toString('base64')}}, res => {
          const chunks = []; let size = 0;
          res.on('data', bytes => {size += bytes.length; if(size > 2*1024*1024) request.destroy(new Error('Response exceeds diagnostic limit')); else chunks.push(bytes);});
          res.on('error', reject);
          res.on('end', () => resolve({code:res.statusCode, bytes:Buffer.concat(chunks)}));
        });
        request.setTimeout(30000, () => request.destroy(new Error('Read-only API diagnostic timed out')));
        request.on('error', reject); request.end();
      });
      connection.assertLease();
      const filename = path.join(process.argv[4], login + '-response.json');
      fs.writeFileSync(filename, response.bytes, {flag:'wx', mode:0o600});
      let parsed; try {parsed = JSON.parse(response.bytes);} catch (_) {parsed = null;}
      const report = {login, method:'GET', path:url.pathname, http_status:response.code,
        bytes:response.bytes.length, sha256:crypto.createHash('sha256').update(response.bytes).digest('hex'),
        json:parsed !== null, envelope_keys:parsed && typeof parsed === 'object' ? Object.keys(parsed) : [],
        status:typeof parsed?.status === 'boolean' ? parsed.status : null,
        response_keys:parsed?.response && typeof parsed.response === 'object' ? Object.keys(parsed.response) : [],
        user_keys:parsed?.response?.user && typeof parsed.response.user === 'object' ? Object.keys(parsed.response.user).filter(key => !/password|token|secret/i.test(key)) : [],
        message:clean(parsed?.message), error:clean(parsed?.error),
        errors_keys:parsed?.errors && typeof parsed.errors === 'object' ? Object.keys(parsed.errors) : []};
      reports.push(report);
    }
  } finally {await lease.close();}
  process.stdout.write(JSON.stringify({schema:1, instance_id:value.instance_id, run_id:value.run_id,
    artifact_id:value.artifact_id, descriptor_sha256:digest, read_only:true, reports}) + '\n');
}
main().catch(error => {process.stderr.write(error.message + '\n');process.exitCode=1;});
