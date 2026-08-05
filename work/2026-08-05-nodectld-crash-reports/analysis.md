# nodectld crash report analysis

## Conclusion

All 24 reports are one bug, not a collection of Ruby or nodectld crashes.
MariaDB Connector/C 3.3.5 contains the out-of-bounds metadata read described
by [CONC-709](https://jira.mariadb.org/browse/CONC-709). A malformed column
definition encodes the schema-name field as `0xfb` (`NULL_LENGTH`). Connector/C
stores a null pointer for that field, subtracts it from the preceding field
pointer, underflows the length, and dereferences the resulting address. That is
the `unpack_fields+0x98` SIGSEGV in every report.

The crash reproduces with MariaDB's standalone CONC-709 test server and one
Ruby thread, so nodectld concurrency is not required. Connector/C 3.4.9 rejects
the same response and mysql2 raises `Mysql2::Error`; nodectld's existing
`NodeCtld::Db#protect` path can then close, reconnect, and retry.

The production trigger is not present in the crash reports. They prove that a
database server or protocol intermediary sent invalid result metadata, but not
why it did so. Fixing the client prevents the availability failure; server and
proxy evidence is still needed to explain the nightly malformed responses.

## Report inventory

| Item | Result |
| --- | --- |
| Reports | 24 |
| Nodes | node20–node25 in Prague and node5 in Brno |
| Time range | 2026-07-10 02:26 CEST to 2026-08-05 04:38 CEST |
| Per-node counts | node20: 2, node21: 3, node22: 5, node23: 4, node24: 5, node25: 4, node5: 1 |
| Runtime | Ruby 3.4.9, mysql2 0.5.6, Connector/C 3.3.5 |
| Native signature | `unpack_fields+0x98` → `mthd_my_read_query_result+0x2ab` → `mysql_read_query_result+0xe` → mysql2 |
| Ruby query site | `libnodectld/lib/nodectld/daemon.rb:244`, the second rollback-selection query |

The reports contain two independently rebuilt Nix package sets, twelve reports
each. Their store paths and binary hashes differ, but their versions, native
instruction, registers, and Ruby call paths are the same. The newer build did
not change or eliminate the failure.

Crashes are concentrated overnight and distributed across nodes. On
2026-08-03, node5 and node25 crashed nine seconds apart. That is evidence for a
shared database, proxy, failover, or maintenance trigger rather than unrelated
per-node memory corruption, but it is not enough to select among those causes.

## Native failure mechanism

Connector/C 3.3.5's `unpack_fields()` calculates each metadata field length
from adjacent pointers before ensuring that the next pointer is non-null:

```c
uint length = (uint)(row->data[i + 1] - row->data[i] - 1);
if (!row->data[i] || row->data[i][length])
  goto error;
```

The packet reader represents a length-encoded SQL `NULL` (`0xfb`) by setting
the corresponding `row->data` entry to null. In all reports:

- the current metadata index is zero;
- `row->data[0]` is a valid catalog string;
- `row->data[1]` is null;
- the unsigned subtraction produces the reported large offset; and
- `row->data[0] + length` equals the reported fault address ending in
  `ffffffff`.

MariaDB's CONC-709 report describes this same pointer state and stack. The
[upstream fix](https://github.com/mariadb-corporation/mariadb-connector-c/commit/12a70541944bf21bfbb9a07d3a1af0345d12b3b6)
validates the complete metadata pointer array before computing lengths. MariaDB
lists fixed releases 3.1.27, 3.3.14, and 3.4.4. Connector/C 3.4.9 is the newest
official tag as of 2026-08-05.

This is a Connector/C defect. Ruby and mysql2 expose it because mysql2 calls
`mysql_read_query_result()` without the Ruby GVL, but neither constructs the
invalid pointer arithmetic. The standalone reproducer excludes the large Ruby
thread count and nodectld's work loop as prerequisites.

## Implemented fix

vpsAdmin commit `8a71a3b79` overlays MariaDB Connector/C 3.4.9 until pinned
nixpkgs provides that version or newer. It also explicitly feeds the overlaid
package into the mysql2 gem configuration used by node and API packages. This
is necessary: replacing `libmariadb.so.3` under an already-built mysql2 is not
a supported validation or deployment strategy because mysql2 compiles
Connector option constants from the headers.

The overlay makes two packaging adaptations:

1. It clears nixpkgs patches that are already integrated in Connector/C 3.4.9
   and adjusts nixpkgs's compile-time `mariadb_config` path substitutions for
   GCC's format checks.
2. It sets `DEFAULT_SSL_VERIFY_SERVER_CERT=OFF`. Connector/C 3.4 otherwise
   enables certificate verification by default and consequently rejects the
   current plaintext-capable database connection configuration. Verified
   database TLS should be enabled as a separate coordinated change.

Both relevant consumers rebuild:

- nodectld/libnodectld use mysql2 0.5.6 linked to Connector/C 3.4.9;
- vpsadmin-api/database/supervisor use mysql2 0.5.7 linked to Connector/C
  3.4.9.

No database schema, persisted state, API, daemon protocol, or generated
configuration format changes. Old and new nodes can coexist against the same
database during a rolling system rebuild and service restart. Rollback can
load all state written by the new version, but restores the vulnerable client.

## Verification

- Built Connector/C 3.4.9 through the vpsAdmin overlay.
- Built final nodectld and vpsadmin-api packages.
- Inspected both recursive closures: neither contains Connector/C 3.3.5.
- Confirmed both rebuilt mysql2 extensions resolve `libmariadb.so.3` from the
  Connector/C 3.4.9 store path.
- Ran the official malformed-server reproducer against the rebuilt nodectld
  mysql2: it completed the plaintext handshake and returned `Mysql2::Error`
  instead of SIGSEGV.
- Passed all declared pre-commit hooks: Nixfmt, MigrationSpecs,
  VpsadminApiI18n, and VpsadminWebuiI18n.
- Passed the MariaDB-backed libnodectld suite: 423 examples, 0 failures.
- Passed the `services-up` NixOS integration test: all 27 service assertions,
  including MariaDB, packaged nodectld state, and API responsiveness.

Mandatory fresh-context review found no blockers. Its Important finding about
retaining the TLS compatibility flag after the nixpkgs source pin expires was
fixed before these long tests. The reviewer confirmed the amended design.

## Operational follow-up

To identify the producer of the malformed packet, correlate the exact crash
timestamps with:

- MariaDB server version, error log, restarts, failovers, and scheduled jobs;
- every database proxy or load balancer in the connection path;
- connection destination chosen by nodectld; and
- a packet capture of the second rollback-selection query when practical.

The invalid value to look for is `0xfb` in the schema/database-name position
of a column-definition packet. A normal empty schema name is encoded as an
empty length-encoded string, not SQL `NULL`.

An authenticated database endpoint or terminating intermediary able to return
this packet can remotely crash an unpatched client, so the defect is an
availability issue even if the database network is trusted. After deployment,
monitor for mysql2 query errors at this query site: they would confirm that the
malformed response still occurs while demonstrating that it is now contained.
