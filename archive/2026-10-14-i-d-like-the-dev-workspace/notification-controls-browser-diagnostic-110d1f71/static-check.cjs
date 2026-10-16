"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const Module = require("node:module");
const diagnostic = require("./preload.cjs");
let stage = "projection";
try {
  const canary = "PRIVATE_CANARY_URL_endpoint_keys_body_storage_selector_0123456789";
  const known = "Clicking the checkbox did not change its state";
  const error = {name: "Error", message: `${known} ${canary}`, stack: `Error: ${canary}\n    at async run (${diagnostic.target}:265:23)\n    at foreign (/private/${canary}:33:44)`};
  const projected = diagnostic.project(error);
  assert.deepEqual(projected, {event: "error", line: 265, column: 23, category: "checkbox_state_unchanged"});
  assert.equal(JSON.stringify(projected).includes(canary), false);
  assert.ok(Buffer.byteLength(JSON.stringify(projected)) < 256);
  for (const stack of [`Error: ${canary}\n    at /private/notifications_browser_test.cjs:265:23`,
    `Error: ${diagnostic.target}:265:23`, `Error\n    at ${diagnostic.target}:${diagnostic.sourceLines + 1}:23`,
    `Error\n    at ${diagnostic.target}:265:4097`, `Error\n    at ${diagnostic.target.replace(".cjs", "Xcjs")}:265:23`,
    canary.repeat(2000) + `\n    at ${diagnostic.target}:265:23`]) {
    assert.deepEqual(diagnostic.project({message: canary, stack}), {event: "error", line: null, column: null, category: "other"});
  }
  stage = "transparent_transform";
  const source = fs.readFileSync(diagnostic.target, "utf8"), transformed = diagnostic.transform(source);
  const before = source.split("\n"), after = transformed.split("\n");
  assert.equal(before.length, after.length);
  assert.deepEqual(before.map((line, i) => line !== after[i] ? i + 1 : null).filter(Boolean), [5]);
  new vm.Script(transformed, {filename: diagnostic.target}); // Parse only; never execute fixture.
  assert.throws(() => diagnostic.transform(source + "\n"), /diagnostic_source_guard/);
  const originalCategory = vm.runInNewContext(before[4] + "\nsafeError");
  let calls = 0;
  const context = {Symbol}; context[diagnostic.observerKey] = () => {calls++;};
  const observedCategory = vm.runInNewContext(after[4] + "\nsafeError", context);
  for (const name of ["Error", "TimeoutError", "AbortError", "NotAllowedError", "SecurityError", "InvalidStateError", "TypeError", canary, undefined]) {
    assert.equal(observedCategory({name}), originalCategory({name}));
  }
  assert.equal(calls, 9);
  context[diagnostic.observerKey] = () => {throw Error(canary);};
  assert.equal(observedCategory(error), originalCategory(error), "sink failure cannot change original return category");
  stage = "wrong_head_guard";
  const guarded = {module: {exports: {}}, process: {env: {}}, require(name) {
    return name === "node:child_process" ? {execFileSync: () => "0".repeat(40)} : require(name);
  }};
  vm.runInNewContext(fs.readFileSync(require.resolve("./preload.cjs"), "utf8"), guarded);
  assert.throws(() => guarded.module.exports.install(), /diagnostic_source_guard/);
  stage = "single_target_hook_and_output_cap";
  const originalCompile = Module.prototype._compile, originalWrite = process.stderr.write;
  const forwards = [], output = [];
  try {
    const stub = function(content, filename) {forwards.push({content, filename}); return "same-return";};
    Module.prototype._compile = stub;
    process.stderr.write = text => {output.push(text); return true;};
    diagnostic.install();
    const hooked = Module.prototype._compile;
    assert.equal(hooked.call({}, "unchanged", "/tmp/unrelated.cjs"), "same-return");
    assert.equal(Module.prototype._compile, hooked);
    assert.equal(hooked.call({}, source, diagnostic.target), "same-return");
    assert.equal(Module.prototype._compile, stub, "loader restored before the targeted compile executes");
    assert.equal(forwards[0].content, "unchanged"); assert.equal(forwards[1].content, transformed);
    for (let i = 0; i < 1000; i++) globalThis[diagnostic.observerKey](error);
    assert.equal(output.length, 8); assert.ok(Buffer.byteLength(output.join("")) <= 2048);
    assert.ok(output.every(line => Buffer.byteLength(line) <= 256));
    assert.equal(output.join("").includes(canary), false);
    assert.equal(output.join("").includes(diagnostic.target), false);
    assert.deepEqual(JSON.parse(output[0]), {notificationFixtureDiagnostic: {event: "installed"}});
  } finally {
    Module.prototype._compile = originalCompile; process.stderr.write = originalWrite; delete globalThis[diagnostic.observerKey];
  }
  console.log(JSON.stringify({staticChecks: "PASS", changedSourceLines: [5], actionSourceLinesUnchanged: true,
    sourceParsedOnly: true, originalSafeErrorCategoriesPreserved: true, observerSinkFailureIsolated: true,
    singleTargetLoaderRestored: true, privacyCanariesExcluded: true, maximumRows: 8, maximumBytes: 2048}));
} catch (_) {
  console.error(JSON.stringify({staticChecks: "FAIL", stage})); process.exitCode = 1;
}
