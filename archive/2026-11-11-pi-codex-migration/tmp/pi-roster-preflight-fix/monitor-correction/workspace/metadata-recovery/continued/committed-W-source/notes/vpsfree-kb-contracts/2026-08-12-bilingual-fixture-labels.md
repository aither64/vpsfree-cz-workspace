# Isolate bilingual capture fixture state

## Symptom

Running a complete Czech capture followed by a complete English capture in the
same development cluster produced duplicate documentation snapshots and TOTP
devices. The second contact sheet also contained both language variants.

## Cause

Snapshot and TOTP fixture discovery uses translated labels such as
`Dokumentační snapshot` and `Documentation snapshot`. A capture in the other
language cannot recognize the existing fixture as its own, so it creates a
second one. Hash and inventory validation accept the resulting images because
the captured files and manifest agree; visual review is what exposes the
semantic duplication.

## Workaround

Until the fixtures have language-independent identity or cleanup, reset the
dedicated cluster between complete Czech and English capture passes. Run each
language from fresh seeded state, validate its result file, and inspect both
contact sheets before committing generated images.

## Verification

For `work/2026-08-09-kb-kvm-review`, both fresh-state 59-checkpoint passes and
strict 118-image validation succeeded. Their contact sheets each contain one
language-appropriate snapshot and TOTP device.
