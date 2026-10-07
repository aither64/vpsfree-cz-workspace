# HaveAPI PHP resource field presence

The legacy network-availability browser scenario reached the correct page but
found no confirmation form. The form guarded its real response field with
`isset($network->enabled)`.

The selected HaveAPI PHP client stores response fields in protected `attrs` and
exposes them through `ResourceInstance::__get` and `attributes()`. Neither
ResourceInstance nor its Resource parent implements `__isset`. Consequently,
`isset` on a response field returns false even when reading that field through
`__get` succeeds. A stdClass fixture does not reproduce this behavior. Action
`getParameters()` returns a stdClass; its advertised parameter checks are a
different case.

Use the client's explicit response attributes to distinguish a missing field
from an enabled or disabled value. Verify both boolean states and old-API
omission with real client instances when testing capability-dependent UI.
Keep API admission enforcement independent of UI state.

Source evidence: `webui/vendor/haveapi/client/src/Client/ResourceInstance.php`
and `Resource.php` at vpsadmin feature cc3337d0. The exact legacy selector
failed before its first toggle. A typed helper using `attributes()` corrected
the presence checks; the full PHP suite passed with 104 tests and 515 assertions,
including seven real-client cases and 116 assertions. Browser verification of
the committed correction remains a separate step. See
[initiative evidence](../../work/2026-10-05-network-ipv4-left-counter/legacy-network-client-verification.md).
