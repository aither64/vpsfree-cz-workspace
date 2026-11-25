# G1 final API writing window

Full-plugin ordinary `rake vpsadmin:i18n:update` completed native31872 exit0.
No active G1 operation. Technical API behavior/field contract stable; all new
write/filter/shared permission readback cases passed. Core model changes are not
part of this writing window. Preserve owner0 source fact/notice strings and producer
files, owner4 PHP/gettext, unrelated API copy, placeholders and wire field names.

Exact owning files/sections offered to lead:

- api/lib/vpsadmin/api/resources/incident_policy.rb: discovery metadata and actions;
- api/lib/vpsadmin/api/resources/vps_incident_policy.rb: scoped typed fields/actions;
- api/lib/vpsadmin/api/resources/incident_report.rb: only policy_key filter and new
  nested PolicyEvaluation resource, not pre-existing notice/source copy;
- api/lib/vpsadmin/api/resources/vps.rb: only new shared incident_summary/settings
  metadata and explicit-policy status filter/errors;
- api/lib/vpsadmin/api/locales/{en,cs}.yml: generated new/changed feature keys/TODOs;
  preserve incident_reports.oomd and notice copy owned by G-mail;
- docs/incident-escalation.md: final generic replacement, technical behavior/current
  limits/creation-only selectors/one-chain/membership/privacy/mail/recovery. Root may
  edit this full owning document. No callback/Unknown/singular/bridge compatibility
  prose should remain.

New errors currently raw source strings: Unknown incident policy; An explicit
incident policy key is required; Provide at least one limit to update; Unable to
save incident limits. Existing errors.incident_escalation.invalid_configuration and
separate_update remain called; separate_update's prior text may mention obsolete
selected policy and needs current permission-only/scoped update meaning. Model
validation messages stay conventional ActiveRecord errors. Startup/engine safe
internal diagnostics are not public API output.

Source context: multiple arbitrary registry keys share adapter, declared limits are
known even with optional applies_if. A malformed persisted threshold combination
means configuration_valid=false/null effective fields, not old dynamic Unknown.
Limits Update is synchronous authoritative row with no chain metadata; shared VPS
permission uses existing ok acknowledgement followed by Show. No wording promises
a stop or SMTP inbox delivery. Nested historical evaluations are explicitly saved
facts. Root owns final EN/CS wording and localization choice for new errors.

After root returns exact files, owner1 runs ordinary full-plugin generation/health,
remaining narrow checks and normal hooks; no re-export or duplicate fullsuite.
