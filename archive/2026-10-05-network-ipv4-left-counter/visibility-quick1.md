# Non-admin list visibility quick-check packet

Prepared for the lead's inspection and fresh verification watcher. Nothing in
this packet has been launched. The owning API documentation uses the lead's
approved paragraph verbatim. No UI, metadata, locale or schema generator is
required for these query-only changes.

Run from the verified session tracking directory:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/visibility-quick1.sh
```

The wrapper checks session markers/current, V branch and baseline HEAD
`be136b6c00f03b85b7a12cc57550b4a1394a94a7`, the exact eight modified paths, an
empty staged index, source/helper hashes, and unchanged migrations/schema.
It refuses configured database access and existing output receipts. It captures
its aggregate output/status itself and stops on the first failed step. It never
edits application source, retries, commits, publishes, pins or invokes lifecycle
operations.

Three sequential commands use explicit repository-root working directories:

1. `VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash visibility-checks.sh ruby`
   syntax-checks the seven changed Ruby files and runs scoped RuboCop with
   `--force-exclusion`, honoring the declared generated-file exclusions.
2. `VPSADMIN_PLUGINS=none nix develop .#api --command bash visibility-checks.sh core 36954`
   runs every example in the five resource specs below in one isolated MariaDB
   process with randomized order and documentation/native JSON formatters.
3. `VPSADMIN_PLUGINS=all nix develop .#api --command bash visibility-checks.sh full 9346`
   runs the same five files in full-plugin mode, independently isolated.

The actual wrapper passes the helper's absolute tracking path. The API shell
starts in `api/`; the helper also selects its directory explicitly. Normal Nix
shell bootstrap may update ignored bundles/generated effective Gemfiles; these
are environment setup, not source generators. Database scratch directories,
RSpec JSON, RuboCop cache and logs stay beneath this session's tracking directory.
The wrapper sets `VISIBILITY_CHECK_PREFIX=visibility-quick1` for its helpers.
The existing test helper owns temporary database startup and cleanup.

| Spec (relative to `api/`) | Existing CI topic | Follow-up coverage |
| --- | --- | --- |
| `spec/api/resources/network_read_spec.rb` | `network` | 10 new examples: member/support enabled-only enumeration, disabled filter intersection, admin inventory/filter preservation, count/cursors, location/purpose intersection, re-enable and disabled Show |
| `spec/api/resources/ip_address_spec.rb` | `ip-ownership` | 10 new examples: enabled free, disabled owned and nonowned assigned rows, support, admin, explicit filters, count/cursors, purpose/location/userpick/private-role preservation and unchanged permitted/forbidden Show |
| `spec/api/resources/host_ip_address_spec.rb` | `network` | One new example: disabled assigned host Index/Show/includes and foreign denial |
| `spec/api/resources/ip_address_assignment_spec.rb` | `ip-ownership` | One new example: disabled active/history includes and foreign Show denial |
| `spec/api/resources/network_interface_spec.rb` | `network` | Two existing examples extended: disabled unowned export association access without direct IP access or foreign host access, and disabled owned export Index/includes |

These are 22 new declared examples and two extended examples. Actual executed
counts, plugin-dependent pending reasons and timing must come from this run.
All five specs are existing tracked files covered by the existing static topic
patterns exactly once in each mode; no spec, topic or CI pattern was added.

W remains unchanged after inspecting its member assignment-history/owned-detached
list, detail adapters and disabled badges. The legacy PHP list/detail consumer
also preserves returned disabled owned/assigned rows and included network data.
No UI checks are included because no UI consumer source changed.

The sole feature migration remains
`20261006120000_add_network_enabled`, immediately after
`20260914190000_add_node_kernel_evidence_checkpoints`. Baseline/current Git blobs:

| Path | Unchanged blob |
| --- | --- |
| `api/db/migrate/20261006120000_add_network_enabled.rb` | `ebdae14a34f6f48b137762559cc621af17578725` |
| `api/db/migrate/20260914190000_add_node_kernel_evidence_checkpoints.rb` | `84f30bed36a2df18388d9d7760b015ec5ee6005e` |
| `api/db/schema.rb` | `47bef8836892dd37339acb6352b1117c5977d324` |

The freeze includes these three files; the guard also checks the complete
migration directory and schema against the baseline. Migration release/deploy
provenance remains the original review record; this refinement adds no migration.

The lead selected one focused visibility follow-up commit, preserving the two
existing V logical commits. Commit/publication/pin helpers will be prepared
after passing checks and the exact committed source head are known. Old source
and downstream heads are V `be136b6c00f03b85b7a12cc57550b4a1394a94a7`, W
`e4c49bcdc91b33b7f644a2f125231cb413cf4bf4`, C
`dd10d88073da3aed6c4512e938abe4374422aab1`, K
`291566b2c0bd43389802f607852fd9a4f8241752`. No historical check certifies the
changed V working tree.
