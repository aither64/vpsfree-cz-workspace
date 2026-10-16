# Main visible/style/copy pass

Inspected actual notification-compact-copy-style.patch: labels, all ten fixed short
error messages and their explicit branch use, hidden single menu status region,
native checkbox labels/descriptions, natural-width scoped CSS, cache selections
clientv5/stylev17/storev3 and detailed-panel preservation are accepted. Main used
vpsfree-user-facing-writing and English Humanizer after technical review. No
product style/label/error change is requested. Make only these final docs edits
and ordinary line wrapping, then commit after final quick checks pass.

In docs/browser-notifications.md replace the added menu paragraph with:

The workspace menu on index and session pages has **Notifications** and **Sound**
checkboxes. **Notification settings** opens the full panel with detailed status,
Test and recovery controls, also available in session Settings. The
**Notifications** checkbox shows confirmed browser setup. A mixed, disabled
checkbox means setup is uncertain; open **Notification settings** to check it.
Opening the menu reads the current state without requesting permission or
changing a subscription. Changing **Notifications** uses the same Enable or
Disable action as the full panel. Disabling applies across sessions in this
browser, while title attention and reservation markers keep updating. Per-session
notification settings remain unchanged and apply again after browser Enable.
A provider-accepted message may still arrive after Disable.

Start the following sound paragraph with:

The **Sound** checkbox in the menu controls the same setting as **Play sound** in
settings. It applies to notifications from this portal in the current browser
profile, across sessions and tests. It defaults on when no choice has been
saved. Turn it off for visual-only notifications.

Keep the subsequent sound/default/OS/storage/worker facts unchanged.

In docs/browser-notifications-operations.md replace the changed menu paragraph with:

The **Notifications** checkbox in the workspace menu and the full-panel buttons
use the same Enable/Disable actions. **Sound** and **Play sound** use the same
browser-local choice. Loading the page or opening the menu does not request
permission or change subscriptions. The worker may check for an update.
Permission and subscription changes require an explicit action. Disabling
notifications for this browser leaves per-session mute preferences, title
attention and reservation markers intact. If cleanup is incomplete, use
**Notification settings** to retry Disable. The menu shows a brief notice and a
mixed checkbox.

Retain all other guide content. Report any unexpected additional visible strings
before commit; no new generic copy pass is required for the exact edits above.
