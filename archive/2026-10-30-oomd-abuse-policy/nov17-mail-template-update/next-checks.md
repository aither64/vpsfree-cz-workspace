# Focused verification and final source boundary

The producer/render batch uses existing actual-core dependencies and normal
MariaDB fixture bootstrap, seed36653, fail-fast, builtin then site reconciliation.
It covers source facts, saved payload, no live config callback, mode restrictions,
CS/EN fallback, recipient time zone, escaped hostile text, old producer/manual
payload, immutable rendered mail, available contributors and frozen selection.
Full raw logs/JSON and synthetic previews remain in this directory. Two failed
new-fixture setups are preserved separately; corrected production code was not
inferred from those failures.

After results: scoped RuboCop, API all-plugin catalog health, existing directory
checker and template flake checks/build. No SDK export is in owner0's batch:
lead reserved owner1 for final clean committed-source schema/client no-change
proof after independent review. Prepared final command from backend root:
`nix develop .#vpsadmin --command tools/export-api-schema --api-version 7.0 --output <fresh-directory>`.
Owner1 must retain raw provenance/schema/tooling and exact current final head;
prior exports prove only their original inputs. No deployment or guest action.
