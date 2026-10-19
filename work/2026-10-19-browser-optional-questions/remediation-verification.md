# Review remediation verification

Important R1: controller no longer treats native thread idle as a terminal turn.
Terminal entry status or a different latest turn clears pins. Added explicit
idle-while-inProgress, reload/return-to-active and actual completion coverage.

Important R2: measure the complete UTF-8 native reply envelope before writing a
submission attempt; pass the portal handler's existing 20,000-byte budget. A new
locally failed or HTTP400/413 validation-rejected attempt is removed and leaves
the answer as editable draft. An already uncertain retry retains its original
identity regardless of a subsequent local/validation error. Added local storage
failure, oversize multibyte framing and corrected-answer tests; original network
uncertainty/reload test continues to pass.

Parent-found namespace correction: custom mount clients now use the same
canonical endpoint identity as their ordinary durable sender. No wire endpoint,
server ledger, user interaction, native protocol or authorization changed.

Direct focused verification on codex-web 641907fb: TestAsync* and
TestRequestUserInput* pass; shared browser contracts (nine cases/entries) pass,
including the new review regression cases. Runtime 911ed52 passes source-file,
shipped-client and free-form-input focused tests; new Playwright syntax passes.
The documented helper budget argument supplies the already-supported handler
limit and narrows invalid submissions; the correction remains inside the
reviewed delivery and validation design. Under review workflow step 9, these
narrow fixes can be inspected/verified directly. No unresolved original finding.
The original independent report is retained separately; broader browser/package
checks have not yet started.
