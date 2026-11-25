# Physical SMTP assertion copy mismatch

Additional source finding from the exact selected suite on9b385dbb. This should
have been updated with the mail-copy change; the focused API render specs did not
execute this physical scenario assertion. Source remains unchanged/frozen.

`tests/suite/alerts/incident-escalation.nix:99` requests delivered mail containing
`was stopped after repeated resource incidents`. The accepted built-in EN plain
:3 and HTML:8 render `was stopped after repeated incidents.`. The saved synthetic
actual MailLog preview under previews-labels-builtin confirms that final wording.

`tests/suite/alerts/common.nix:64` passes text_includes into
`services.wait_for_mailpit_message`, then also asserts it on the returned Text.
`tests/runner/extensions/vpsadmin_services.rb:256` waits with configured machine
default timeout (fallback300seconds), and :688 matches each substring literally.
`ensure_operational_alert_templates` at common.nix:83 installs the built-ins and
does not replace this stopped copy. There is no normalization that drops resource.

Thus this stale expectation can time out even after correct SMTP delivery if the
scenario reaches it with the final built-in definition. It is a test-copy seam,
not a product/enforcement defect. No current native result/log proves the running
job has reached or failed here, so it cannot explain the whole runtime or establish
a stall. The broad/full-suite scope and cb8 skipped-runtime distinction remain.

Smallest correction after lead reconciles export/review input ownership: change
only that expected literal to `was stopped after repeated incidents`, preserving
actual delivery, counts, history, privacy, restart/transfer/data checks and bounds.
No change was made and no test/CI run was launched or interrupted in this read-only
package. Root owns source-release/disposition and exact running CI observation.
