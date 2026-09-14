// Read-only layout reproduction with the portal's current template and assets.
// No live conversation is loaded and no request is submitted.
const fs = require('node:fs');
const {execFileSync} = require('node:child_process');
const path = require('node:path');
const assert = require('node:assert/strict');
const {chromium} = require('playwright');
const root = path.resolve(__dirname, '../../worktrees/2026-09-14-portal-planning-question-controls/dev-workspace');
const assets = path.join(root, 'portal/internal/web');
const baseline = file => execFileSync('git', ['-C', root, 'show', 'e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a:portal/internal/web/' + file], {encoding: 'utf8'});
const template = baseline('templates/session.html');
const start = template.indexOf('<section id="codex"');
const end = template.indexOf('<section id="handoff"');
const markup = template.slice(start, end).replace(/{{.*?}}/gs, '');
const css = baseline('static/style.css');
const app = baseline('static/app.js');
(async () => {
  const browser = await chromium.launch({headless: true, channel: "chromium"});
  const results = [];
  try {
    const page = await browser.newPage();
    await page.setContent('<div class="workspace-shell"><aside class="workspace-sidebar"></aside><main class="page session-page"><section class="session-tabs">' + markup + '</section></main></div>');
    await page.addStyleTag({content: css});
    await page.evaluate(() => { window.module = {exports: {}}; });
    await page.addScriptTag({content: app});
    await page.evaluate(() => {
      document.querySelector('#message-form textarea').value = 'Preserved draft';
      document.querySelector('#codex-mode').hidden = false;
      document.querySelector('#codex-mode').textContent = 'Plan';
      document.querySelector('#pending').innerHTML = '<article class="approval question-approval"><strong>Codex needs your input</strong><form class="input-wizard stack"><p class="eyebrow">Approach · 1 of 1</p><div class="wizard-content"><p class="wizard-question">Which approach should I use?</p><label class="wizard-option"><input type="radio" checked><span>Recommended approach</span></label><textarea placeholder="Add an optional note…"></textarea></div><div class="approval-actions wizard-actions"><button type="button">Back</button><button type="button">Submit answers</button></div></form></article>';
      // renderPlanActions takes this path for every active planning turn.
      window.module.exports.setPlanDecisionVisible(document.querySelector('#plan-actions'), document.querySelector('#message-form'), false);
    });
    for (const [width,height] of [[1440,1000],[1280,720],[1280,540],[390,844]]) {
      await page.setViewportSize({width,height});
      const row = await page.evaluate(() => {
        const visible = selector => {
          const e = document.querySelector(selector);
          return e.getClientRects().length > 0 && getComputedStyle(e).display !== 'none';
        };
        return {width: innerWidth, height: innerHeight, question:visible('.question-approval'), prompt:visible('#message-form textarea'), send:visible('#message-send'), model:visible('#codex-model'), reasoning:visible('#codex-effort'), mode:visible('#codex-mode'), interrupt:visible('#interrupt'), composerHeight:document.querySelector('#message-form').getBoundingClientRect().height};
      });
      assert(row.question && row.prompt && row.send && row.interrupt, JSON.stringify(row));
      assert.equal(row.model, height > 600);
      assert.equal(row.reasoning, height > 600);
      assert.equal(row.mode, height > 600);
      results.push(row);
    }
    await page.evaluate(() => {
      document.querySelector('#pending').replaceChildren();
      window.module.exports.setPlanDecisionVisible(document.querySelector('#plan-actions'), document.querySelector('#message-form'), true);
    });
    assert.equal(await page.locator('#message-form').isVisible(), false);
    assert.equal(await page.locator('#plan-actions').isVisible(), true);
    await page.evaluate(() => window.module.exports.setPlanDecisionVisible(document.querySelector('#plan-actions'), document.querySelector('#message-form'), false));
    assert.equal(await page.locator('#message-form').isVisible(), true);
    assert.equal(await page.locator('#message-form textarea').inputValue(), 'Preserved draft');
    const output = {source:'baseline e9ed544 portal template, stylesheet, and exported plan visibility helper; synthetic pending question DOM', results, completedPlanHidesComposer: true, dismissRestoresDraft:true};
    fs.writeFileSync(path.join(__dirname, 'layout-results.json'), JSON.stringify(output,null,2)+'\n');
    console.log(JSON.stringify(output,null,2));
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode=1; });
