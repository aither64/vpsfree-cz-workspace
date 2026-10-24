"use strict";
const assert = require("node:assert/strict");
const path = require("node:path");
const helper = path.resolve(process.env.FIREFOX_READINESS_TEST_ROOT,
  "portal/internal/web/firefox_tabs_readiness.cjs");
require(helper);
require.cache[helper].exports.waitForRestoredStream = async ({baseline, status}) => {
  const snapshot = await status();
  assert(snapshot.counts[5].events.Count > baseline);
  return snapshot;
};
