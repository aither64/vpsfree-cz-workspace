# Attachment menus and cached provider assets

The portal imports a cached codex-web ES module, which imports uploads.js;
uploads.css is loaded separately. Provider assets use a five-minute max-age.
A new template with hidden upload roots can therefore run with the baseline
provider, which ignores controlsRoot and puts its only controls in those hidden
roots. New JS with old CSS can also render an unstyled menu.

Keep markup usable by the preceding provider, let the current component own
empty-root visibility, and change cache identities through the complete changed
chain (portal conversation import, nested upload import, upload stylesheet).
The compact-menu follow-up uses conversation v6 and upload JS/CSS v2. Its
isolated Firefox fixture warms baseline assets and switches forward and back;
both existing and new-session controls remain usable. See
work/2026-09-12-portal-file-uploads/menu-browser-acceptance.py.

A Selenium default click on the textarea center was intercepted by the popover
at 390 CSS pixels because the menu intentionally overlays that point. For the
outside-dismissal assertion, click a visible corner outside the menu using a
native pointer action. This is a test-target correction, not a product defect.

When an optional controlsRoot causes the component to change root.hidden,
restore the original value on destroy so later mounts can reuse the host root.

When testing the current provider API after warming legacy caches, import its
current versioned URL. An unversioned test import correctly returned the warmed
baseline module, which does not implement controlsRoot; that was fixture misuse.

Firefox WebDriver's execute_async_script dynamic import runs in an automation
realm. Calling the provider's Window-bound fetch there failed with “does not
implement interface Window”. Serve a same-origin external module in the fixture
and append its module script to the real page to test mountConversation; retain
the portal CSP. That native-page check passed without changing product code.
