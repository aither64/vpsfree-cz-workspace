"use strict";
const fs = require("node:fs");
const crypto = require("node:crypto");
const Module = require("node:module");
const {execFileSync} = require("node:child_process");
const target = "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace/portal/internal/web/notifications_browser_test.cjs";
const checkout = "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace";
const revision = "6c7d3851b005b47357e43688efccddde56f4e53b";
const sourceSHA256 = "f539862a57cf85b3ce6a6795fed33b289c085b5f10b6d3b3fa1dc37f5025bd32";
const sourceLines = 372;
const needle = "const safeError = error => [\"Error\", \"TimeoutError\", \"AbortError\", \"NotAllowedError\", \"SecurityError\", \"InvalidStateError\", \"TypeError\"].includes(error?.name) ? error.name : \"UnknownError\";";
const observerKey = Symbol.for("notification-fixture-diagnostic-6c7d3851");
const knownCheckbox = "Clicking the checkbox did not change its state";
const sha256 = text => crypto.createHash("sha256").update(text).digest("hex");

// Only this exact source file's first stack frame contributes numeric position.
// Nothing derived from message/stack/name other than this fixed enum is emitted.
function project(error) {
  let message = "", stack = "";
  try {if (typeof error?.message === "string") message = error.message.slice(0, 4096);} catch (_) {}
  try {if (typeof error?.stack === "string") stack = error.stack.slice(0, 16384);} catch (_) {}
  const escaped = target.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const frame = new RegExp("^\\s+at (?:async )?(?:[^()\\n]*\\()?" + escaped + ":(\\d{1,5}):(\\d{1,5})\\)?$");
  let line = null, column = null;
  for (const entry of stack.split("\n").slice(0, 48)) {
    const match = entry.length <= 1024 ? frame.exec(entry) : null;
    if (!match) continue;
    const candidateLine = Number(match[1]), candidateColumn = Number(match[2]);
    if (candidateLine >= 1 && candidateLine <= sourceLines && candidateColumn >= 1 && candidateColumn <= 4096) {
      line = candidateLine; column = candidateColumn; break;
    }
  }
  return {event: "error", line, column, category: message.includes(knownCheckbox) ? "checkbox_state_unchanged" : "other"};
}
function transform(content) {
  if (sha256(content) !== sourceSHA256 || content.split(needle).length !== 2) throw new Error("diagnostic_source_guard");
  // Keep the original line count and all other lines byte-identical. This
  // computes the original category first and returns that same value afterward.
  const expression = needle.slice("const safeError = error => ".length, -1);
  const replacement = `const safeError = error => { const category = ${expression}; try { globalThis[Symbol.for("notification-fixture-diagnostic-6c7d3851")](error); } catch (_) {} return category; };`;
  return content.replace(needle, replacement);
}
function install() {
  const actual = execFileSync("git", ["-C", checkout, "rev-parse", "HEAD"], {encoding: "utf8", stdio: ["ignore", "pipe", "ignore"]}).trim();
  if (actual !== revision || sha256(fs.readFileSync(target)) !== sourceSHA256) throw new Error("diagnostic_source_guard");
  let rows = 0, bytes = 0;
  const emit = record => {
    if (rows >= 8) return;
    const text = JSON.stringify({notificationFixtureDiagnostic: record}) + "\n";
    const size = Buffer.byteLength(text);
    if (size > 256 || bytes + size > 2048) return;
    rows++; bytes += size;
    try {process.stderr.write(text);} catch (_) {}
  };
  globalThis[observerKey] = error => emit(project(error));
  const original = Module.prototype._compile;
  Module.prototype._compile = function(content, filename) {
    if (filename !== target) return original.call(this, content, filename);
    // One targeted compile only; restore before any fixture imports execute.
    Module.prototype._compile = original;
    let transformed;
    try {transformed = transform(content);} catch (_) {
      emit({event: "guard_failed"}); process.exit(90);
    }
    emit({event: "installed"});
    return original.call(this, transformed, filename);
  };
}
module.exports = {project, transform, install, target, sourceSHA256, sourceLines, observerKey};
if (process.env.NOTIFICATION_FIXTURE_DIAGNOSTIC === "1") {
  try {install();} catch (_) {
    try {process.stderr.write('{"notificationFixtureDiagnostic":{"event":"guard_failed"}}\n');} catch (_) {}
    process.exit(90);
  }
}
