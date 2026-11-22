# Kernel preflight package-name ambiguity

A temporary guard for the advisory-corrections KB acceptance run classified
`linux-6.12.107-modules-shrunk` and `initrd-linux-6.12.107` as kernel compilation.
The native dry-run succeeded, but this broad name match stopped the local batch
before any guest started. Inspecting the actual planned derivations showed
module-closure/initrd packaging; the Linux6.18.48 kernel and modules were fetches.
There was no planned kernel compilation.

Use actual derivation/build-plan evidence to distinguish Linux compilation from
packaging that mentions a kernel name. A `linux-` substring is insufficient.
Keep the ordinary uncached-kernel refusal for genuine compilation. Correct the
temporary classification once and continue only missing verification; do not
repeat an already-passed strict check or change product source to address this
observation error. In this case hosted exact-source KVM evidence subsequently
covered the missing checks, so no duplicate local KVM run was needed.

Evidence: work/2026-11-01-published-advisory-corrections/visibility-verification.md,
final strict/KVM acceptance receipts. No reusable guard framework was introduced.
