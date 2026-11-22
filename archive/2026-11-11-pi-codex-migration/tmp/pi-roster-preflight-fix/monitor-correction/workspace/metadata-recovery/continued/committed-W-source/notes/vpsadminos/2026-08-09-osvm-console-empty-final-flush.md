# osvm console close can flush an empty scan buffer

Related initiative: `work/2026-08-09-test-vm-kernel-oops/`

## Symptom

The crashdump examples completed successfully, but their test processes failed
during teardown with `NoMethodError` from the console reader's final flush.
The failure appeared only when the console closed with no buffered text.

## Cause and fix

Ruby returns an empty array for `''.split("\\n", -1)`. Assigning `lines.pop`
directly therefore changed the console scan buffer from an empty string to
`nil`, and the final flush later called `empty?` on it.

Keep an empty string when `pop` has no element and cover console close with an
empty buffer in the machine specs.

## Verification

The corrected combined run passed `crashdump/default`, `crashdump/inspect`, and
`crashdump/nfs-inspect`. All intentional panics were logged as expected, and
the full osvm suite passed 108 examples.
