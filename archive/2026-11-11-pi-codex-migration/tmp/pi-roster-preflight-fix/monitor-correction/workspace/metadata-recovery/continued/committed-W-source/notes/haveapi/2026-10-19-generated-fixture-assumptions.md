# Validate fixture assumptions against the owning API

The Rust generated-client acceptance harness exposed several fixture assumptions
before it reached all real-server tests:

- Distinct generated actions have distinct Output/Meta types. Compare a common
  field rather than placing their complete responses in one Rust array.
- Resource.define_action checks inherited constants. Naming a fixture action
  Custom silently skipped registration because HaveAPI already defines that
  constant. Use a distinct action name and verify actual DSL registration.
- Required string input rejects empty strings through Presence validation;
  nullable strings can normalize blanks to nil. Test empty-string preservation
  on an optional nonnullable parameter, while keeping required-value tests valid.
- URL path segments may retain legal sub-delimiters such as ampersand. The
  pinned url library produces child%3F& for child?&, preserving it as one path
  segment. Assert the complete request target, boundaries and absence of query/
  fragment rather than requiring query-style escaping of every special character.
- WebUI setting namespaces are model-validated against forms, tips and ui. Use
  an accepted namespace and a fixture-specific key; an arbitrary namespace
  yields a normal API failure envelope rather than permitting Custom storage.
- Positive token tests keep login notifications enabled and seed an available
  node with the canonical helper so the mail transaction has a recent target.
  API fixture bootstrap alone does not provide that NodeCurrentStatus.
- vpsAdmin rejects a record-level user when its DNS zone is already user-owned.
  Fixture setup should follow the canonical model and resource specs rather than
  duplicating ownership on the record.

Action-specific static assertions help identify failures inside shared async/
blocking macros without printing credentials or request payloads. Passing a
success envelope alone does not prove that the server received the intended
input. Keep exact input and metadata assertions for wire-contract acceptance.

These findings came from source-backed diagnosis and actual compiler/server
logs. Generic root/mounted and actual vpsAdmin acceptance passed in both modes,
including token lifecycle checks.
Session: [Rust client generator](../../work/2026-10-18-rust-client-generator/state.md).
