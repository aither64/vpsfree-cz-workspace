'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const fixture = fs.readFileSync('portal/internal/web/retry_backend_browser_test.cjs', 'utf8');
const declaration = fixture.slice(fixture.indexOf('const ancillaryExpectations ='), fixture.indexOf('const cases ='));
const context = {base: 'https://127.0.0.1:10001', manualBase: 'https://127.0.0.1:10002'};
vm.runInNewContext(declaration + '\nglobalThis.result = {table: ancillaryExpectations, match: ancillaryExpectation};', context);
const {table, match} = context.result;
const spec = JSON.parse(fs.readFileSync(__dirname + '/ancillary-expectations.json', 'utf8')).expectations;
const signature = row => ['method', 'path', 'query', 'status'].map(key => row[key]);
assert.equal(JSON.stringify(table.map(signature)), JSON.stringify(spec.map(signature)));
let positive = 0, negative = 0;
for (const row of table) {
  assert(row.reason && row.source);
  for (const origin of [context.base, context.manualBase]) {
    assert(match({...row, origin, kind: 'http'})); positive++;
    for (const changed of [{origin: 'https://foreign.example'}, {kind: 'transport'}, {method: 'POST'},
        {path: row.path + '/extra'}, {query: row.query + '&unexpected=1'}, {status: 500}]) {
      assert(!match({...row, origin, kind: 'http', ...changed})); negative++;
    }
  }
}
for (const origin of [context.base, context.manualBase]) {
  for (const path of ['/api/sessions/example/retry-policy', '/api/sessions/example/retry/activity',
      '/api/sessions/example/retry/now', '/api/sessions/example/retry/stop',
      '/api/sessions/example/message', '/api/sessions/example/settings',
      '/codex/conversations/example~implementer0/retry/activity',
      '/codex/conversations/example~implementer0/message',
      '/codex/conversations/example~implementer0/settings']) {
    for (const method of ['GET', 'POST']) {
      assert(!match({origin, kind: 'http', method, path, query: '', status: 503})); negative++;
    }
  }
}
console.log(JSON.stringify({tableEntries: table.length, exactMatches: positive, refusedMismatchOrProtectedInterface: negative, pass: true}));
