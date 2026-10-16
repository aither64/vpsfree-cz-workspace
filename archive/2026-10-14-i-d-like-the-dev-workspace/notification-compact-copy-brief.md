# Main copy brief: compact notification menu

Main applied vpsfree-user-facing-writing and English Humanizer after the accepted
technical brief. Required visible labels: Notifications; Sound; Notification settings.
The link remains /browser-notifications. Full-panel labels/guidance remain as-is
except owning guide references that describe the menu accurately.

Menu-only short messages, selected explicitly at the owning failure branches:
- Incomplete setup/cleanup or retired observation: Notification setup needs attention.
- Failed status observation: Could not check notifications.
- Blocked permission: Notifications are blocked.
- Unsupported delivery context: Notifications are unavailable here.
- Delivery disabled on server: Notification delivery is unavailable.
- Failed Enable/Disable action, when not already represented by incomplete cleanup: Could not update notifications.
- Failed sound read: Could not read the sound setting.
- Failed sound save: Could not save the sound setting.
- Unsupported sound control: Sound control is unavailable.
- Failed/unconfirmed actual worker update: Notification update unconfirmed.

Show only one message using the architect's precedence and existing state owners.
No routine progress/success/help strings in the menu. Detailed panel messages stay
with their existing owners. Do not infer a category by matching these or existing
status strings. This copy brief does not authorize changing implementation scope.
Actual visible/style/docs diff still requires main inspection before commit.
