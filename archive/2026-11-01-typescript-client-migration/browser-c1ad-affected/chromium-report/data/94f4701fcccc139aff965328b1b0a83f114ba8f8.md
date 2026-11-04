# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/security_advisories_admin.spec.ts >> @smoke Security advisory admin management >> rejects a normal user before any advisory administration is rendered
- Location: e2e/specs/app/security_advisories_admin.spec.ts:653:3

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('auth.admin-required')
Expected: visible
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('auth.admin-required')

```

```yaml
- text: Loading…
```

# Test source

```ts
  565 |     expect(rebuildAttempts).toBe(2);
  566 |   });
  567 | 
  568 |   test('@pr-smoke @pr-smoke-mobile keeps rejected outage link changes in context for retry', async ({ page }) => {
  569 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'SECURITY_OUTAGE_RETRY' });
  570 | 
  571 |     const advisory = {
  572 |       id: 77,
  573 |       state: 'draft',
  574 |       content_revision: 0,
  575 |       name: 'Linux kernel advisory',
  576 |       published_at: null,
  577 |       created_at: '2026-07-27T10:00:00.000Z',
  578 |       en_summary: 'Kernel vulnerability',
  579 |       en_description: 'Affects supported compute nodes.',
  580 |       en_response: 'Apply the fixed kernel and reboot.',
  581 |     };
  582 |     let outageLinks: Array<Record<string, unknown>> = [];
  583 |     let linkAttempts = 0;
  584 |     let unlinkAttempts = 0;
  585 | 
  586 |     await installHaveApiMock(page, {
  587 |       description: advisoryContractDescription(),
  588 |       user: { id: 1, login: 'security-admin', level: 90 },
  589 |       handlers: {
  590 |         'GET languages': () => ({ languages }),
  591 |         'GET security_advisories/77': () => ({ security_advisory: advisory }),
  592 |         'GET security_advisory_cves': () => ({ security_advisory_cves: [] }),
  593 |         'GET nodes': () => ({ nodes: [] }),
  594 |         'GET security_advisories/77/node_statuses': () => ({ node_statuses: [] }),
  595 |         'GET security_advisory_updates': () => ({ security_advisory_updates: [] }),
  596 |         'GET outage_security_advisories': () => ({ outage_security_advisories: outageLinks }),
  597 |         'POST outage_security_advisories': ({ reqJson }) => {
  598 |           linkAttempts += 1;
  599 |           if (linkAttempts === 1) return failEnvelope('Outage link was rejected');
  600 |           const outageId = (reqJson as any)?.outage_security_advisory?.outage;
  601 |           const link = {
  602 |             id: 801,
  603 |             security_advisory_id: 77,
  604 |             outage_id: outageId,
  605 |             outage: {
  606 |               id: outageId,
  607 |               begins_at: '2026-07-27T14:00:00.000Z',
  608 |               en_summary: 'Emergency kernel maintenance',
  609 |             },
  610 |           };
  611 |           outageLinks = [link];
  612 |           return { outage_security_advisory: link };
  613 |         },
  614 |         'DELETE outage_security_advisories/801': () => {
  615 |           unlinkAttempts += 1;
  616 |           if (unlinkAttempts === 1) return failEnvelope('Outage unlink was rejected');
  617 |           outageLinks = [];
  618 |           return { outage_security_advisory: {} };
  619 |         },
  620 |       },
  621 |     });
  622 | 
  623 |     await page.goto('/admin/security-advisories/77?tab=outages');
  624 |     const outageInput = page.getByTestId('admin.security_advisory.outages.id');
  625 |     await outageInput.fill('321');
  626 |     await page.getByTestId('admin.security_advisory.outages.link').click();
  627 | 
  628 |     await expect(page.getByTestId('admin.security_advisory.outages.link_error')).toContainText(
  629 |       'Outage link was rejected'
  630 |     );
  631 |     await expect(outageInput).toHaveValue('321');
  632 | 
  633 |     await page.getByTestId('admin.security_advisory.outages.link').click();
  634 |     await expect(page.getByTestId('admin.security_advisory.outages.link_error')).toHaveCount(0);
  635 |     await expect(outageInput).toHaveValue('');
  636 |     await expect(page.getByRole('link', { name: '#321' })).toBeVisible();
  637 | 
  638 |     await page.getByTestId('admin.security_advisory.outages.unlink.801').click();
  639 |     await page.getByTestId('admin.security_advisory.outages.unlink.confirm').click();
  640 | 
  641 |     await expect(page.getByTestId('admin.security_advisory.outages.unlink.error')).toContainText(
  642 |       'Outage unlink was rejected'
  643 |     );
  644 |     await expect(page.getByTestId('admin.security_advisory.outages.unlink')).toBeVisible();
  645 | 
  646 |     await page.getByTestId('admin.security_advisory.outages.unlink.confirm').click();
  647 |     await expect(page.getByTestId('admin.security_advisory.outages.unlink')).toHaveCount(0);
  648 |     await expect(page.getByRole('link', { name: '#321' })).toHaveCount(0);
  649 |     expect(linkAttempts).toBe(2);
  650 |     expect(unlinkAttempts).toBe(2);
  651 |   });
  652 | 
  653 |   test('rejects a normal user before any advisory administration is rendered', async ({ page }) => {
  654 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  655 |     await installHaveApiMock(page, {
  656 |       description: advisoryContractDescription(),
  657 |       user: { id: 2, login: 'member', level: 1 },
  658 |       handlers: {
  659 |         'GET security_advisories': () => ({ security_advisories: [] }),
  660 |       },
  661 |     });
  662 | 
  663 |     await page.goto('/admin/security-advisories/77');
  664 | 
> 665 |     await expect(page.getByTestId('auth.admin-required')).toBeVisible();
      |                                                           ^ Error: expect(locator).toBeVisible() failed
  666 |     await expect(page.getByTestId('admin.security_advisory.detail')).toHaveCount(0);
  667 |     await expect(page.getByTestId('admin.security_advisories.page')).toHaveCount(0);
  668 |   });
  669 | 
  670 |   test('hides advisory management from support and rejects direct route access', async ({ page }) => {
  671 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  672 |     await installHaveApiMock(page, {
  673 |       description: advisoryContractDescription(),
  674 |       user: { id: 3, login: 'support-agent', level: 21 },
  675 |       handlers: {
  676 |         'GET security_advisories': () => ({ security_advisories: [] }),
  677 |       },
  678 |     });
  679 | 
  680 |     await page.goto('/admin');
  681 |     await expect(page.getByTestId('nav.sidebar.security-advisories')).toHaveCount(0);
  682 |     await expect(page.getByTestId('nav.drawer.security-advisories')).toHaveCount(0);
  683 | 
  684 |     await page.goto('/admin/security-advisories/77');
  685 | 
  686 |     await expect(page).toHaveURL(/\/admin\/?$/);
  687 |     await expect(page.getByTestId('admin.security_advisory.detail')).toHaveCount(0);
  688 |     await expect(page.getByTestId('admin.security_advisories.page')).toHaveCount(0);
  689 |   });
  690 | });
  691 | 
  692 | for (const language of ['en', 'cs'] as const) {
  693 |   test(`published original corrections and lifecycle ${language}`, async ({ page }, testInfo) => {
  694 |     let advisory = {
  695 |       id: 88,
  696 |       state: 'published',
  697 |       content_revision: 5,
  698 |       name: 'Synthetic kernel advisory',
  699 |       published_at: '2026-10-15T12:34:56Z' as string | null,
  700 |       en_summary: 'Kernel security correction',
  701 |       en_description: 'Synthetic assessment for preview.',
  702 |       en_response: 'Fixed by the reviewed kernel update.',
  703 |       cs_summary: 'Bezpečnostní oprava jádra',
  704 |       cs_description: 'Testovací hodnocení pro náhled.',
  705 |       cs_response: 'Ošetřeno ověřenou aktualizací jádra.',
  706 |     };
  707 |     let deleted = false;
  708 |     const writes: Array<Record<string, unknown>> = [];
  709 |     await setUiSettingsLocalStorage(page, { language, theme: 'light' });
  710 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  711 |     await installHaveApiMock(page, {
  712 |       description: advisoryContractDescription(),
  713 |       user: { id: 1, login: 'synthetic-admin', level: 90 },
  714 |       handlers: {
  715 |         'GET languages': () => ({ languages }),
  716 |         'GET security_advisories/88': () => (deleted ? failEnvelope('Not found') : { security_advisory: advisory }),
  717 |         'GET security_advisories': () => ({ security_advisories: deleted ? [] : [advisory] }),
  718 |         'GET security_advisory_cves': () => ({ security_advisory_cves: [] }),
  719 |         'GET nodes': () => ({ nodes: [] }),
  720 |         'GET security_advisories/88/node_statuses': () => ({ node_statuses: [] }),
  721 |         'GET security_advisory_updates': () => ({ security_advisory_updates: [] }),
  722 |         'GET outage_security_advisories': () => ({ outage_security_advisories: [] }),
  723 |         'PUT security_advisories/88': ({ reqJson }) => {
  724 |           const attrs = (reqJson as { security_advisory: Record<string, unknown> }).security_advisory;
  725 |           writes.push(attrs);
  726 |           if (
  727 |             attrs['expected_content_revision'] !== advisory.content_revision ||
  728 |             attrs['expected_state'] !== advisory.state
  729 |           )
  730 |             return failEnvelope('Concurrent correction');
  731 |           advisory = { ...advisory, ...attrs, content_revision: advisory.content_revision + 1 };
  732 |           return { security_advisory: advisory };
  733 |         },
  734 |         'POST security_advisories/88/retract': ({ reqJson }) => {
  735 |           const attrs = (reqJson as { security_advisory: Record<string, unknown> }).security_advisory;
  736 |           expect(attrs).toEqual({ expected_content_revision: advisory.content_revision, expected_state: 'published' });
  737 |           writes.push(attrs);
  738 |           advisory = { ...advisory, state: 'retracted', content_revision: advisory.content_revision + 1 };
  739 |           return { security_advisory: advisory };
  740 |         },
  741 |         'DELETE security_advisories/88': ({ reqJson }) => {
  742 |           expect(reqJson).toEqual({
  743 |             security_advisory: { expected_content_revision: advisory.content_revision, expected_state: 'retracted' },
  744 |           });
  745 |           deleted = true;
  746 |           return null;
  747 |         },
  748 |       },
  749 |     });
  750 |     await page.goto('/admin/security-advisories/88');
  751 |     await expect(page.getByTestId('admin.security_advisory.edit')).toBeVisible();
  752 |     await expect(page.getByTestId('admin.security_advisory.publish')).toHaveCount(0);
  753 |     await expect(page.getByTestId('admin.security_advisory.readiness')).toHaveCount(0);
  754 |     await page.getByTestId('admin.security_advisory.edit').click();
  755 |     const editor = page.getByTestId('admin.security_advisories.editor');
  756 |     await expect(editor).toBeVisible();
  757 |     await expect(page.getByTestId('admin.security_advisories.editor.published_at')).not.toHaveValue('');
  758 |     const captureRoot = process.env['ADVISORY_SCREENSHOT_ROOT'];
  759 |     if (captureRoot) {
  760 |       await mkdir(captureRoot, { recursive: true });
  761 |       await page.screenshot({
  762 |         path: path.join(captureRoot, `${testInfo.project.name}-${language}-editor.png`),
  763 |         fullPage: true,
  764 |       });
  765 |       await editor.getByRole('button', { name: language === 'cs' ? 'Zrušit' : 'Cancel', exact: true }).click();
```