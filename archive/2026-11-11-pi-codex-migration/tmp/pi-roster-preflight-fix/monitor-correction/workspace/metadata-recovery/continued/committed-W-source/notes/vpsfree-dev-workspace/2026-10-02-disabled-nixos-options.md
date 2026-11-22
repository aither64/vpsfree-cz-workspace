# Omit unavailable NixOS options from disabled selections

`lib.mkIf false` does not make an unknown NixOS option valid. Module option
checking still sees the definition path before discarding its conditional
value. A default-off feature that depends on a newer module must omit the
unsupported attribute altogether in its disabled selection, for example
with `lib.optionalAttrs` around that attribute set. The enabled selection
still needs the compatible module and its required values.

An exported app can also force a new module configuration indirectly when
its program derivation interpolates a generated JSON derivation. Keeping the
feature off in ordinary cluster defaults does not keep that app evaluation
lazy. For an explicit fixture that requires a source override, build its fixed
configurations on invocation while retaining the selected input overrides.
Do not silently fall back to a default lock or omit required enabled options.

Provider Check run `37057284522` exposed the first issue against default API
`5c76e329`; source inspection identified the eager maintenance app as the
second affected consumer. The same-session API46 no-VM smoke had passed
because it selected the newer actual modules. Default-pin evaluation and the
explicit compatible fixture are separate checks. Correction and verification
are tracked in the [provider review record](../../work/2026-09-23-storage-redesign/storage-profile-provider-review.md).
