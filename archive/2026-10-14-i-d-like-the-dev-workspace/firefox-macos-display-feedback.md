# Physical Firefox/macOS non-display after successful browser record

User exact result after deployed469: “This test reached the browser and the
browser accepted the display request. A matching notification is recorded.
Check your screen to confirm it appeared.” User confirms no visible notification.

The shipped client reports that only for exact descriptor correlation, received,
showNotification resolved and a matching record immediately returned from
registration.getNotifications. This differs from prior Linux rejection and
establishes no actual macOS banner. No server/provider reattempt or resubscribe
is justified by this evidence.

Architect0 is checking appclose/tag/ACK paths; main asks whether macOSFirefox
notifications allow banners/alerts and whether test is in systemNotification
Center. Need distinguish macOS presentation suppression vs Firefox/platform
behavior; neither cause is proved yet. No source edit or production mutation.
Apple official notification/Focus docs read for settings meanings.

Sources:
- https://support.apple.com/guide/mac-help/notifications-settings-mh40583/mac
- https://support.apple.com/guide/mac-help/turn-a-focus-on-or-off-mchl999b7c1a/mac

No tabclose/reset/oldtabcompat workflow. Session/reservation remainopen.

## User confirmed macOS permission and audible delivery

User confirmed Firefox notifications were disabled in macOS System Settings.
After enabling them, the shipped Test emits sound but no visible notification.
This establishes the actual system permission issue and subsequent audible
delivery. It does not establish why banners remain absent. Next smallest check:
Firefox application alert style must show banners/alerts rather than None;
Focus may independently suppress presentation. No further application change or
reset selected. Physical visible banner/click acceptance still pending.

User then confirmed the notification is visible when manually opening macOS
Notification Center at the top right. Actual delivery, sound and a visible
systemNotificationCenter entry now confirmed on Firefox/macOS. Remaining issue
is automatic popup/banner presentation; check Firefox appalertstyle and Focus.
Notification click/authentication acceptance not yet observed.

User further confirmed the automatic notification popup was visible. Actual
Firefox/macOS arrival/sound/NotificationCenter/popup acceptance established after
OSsettings corrections. New soundpreference request is a separate feature; no
newdisplaydiagnosis needed. Notification click still unobserved.
