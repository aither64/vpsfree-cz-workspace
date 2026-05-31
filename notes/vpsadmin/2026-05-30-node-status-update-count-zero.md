# Node status update_count zero can produce NaN

Date: 2026-05-30

Related initiative: `work/2026-05-30-dev-vpsadmin-clusters`

Symptom:

- `vpsadmin-supervisor` repeatedly logs
  `Mysql2::Error: Unknown column 'NaN' in 'VALUES'` while consuming
  `node:<node>:statuses`.
- The node stays down in vpsAdmin and keeps placeholder status values, such as
  `kernel = devcluster`, even though `nodectld` is running and RabbitMQ shows a
  live node connection.

Cause:

- A placeholder `node_current_statuses` row had `update_count = 0`.
- On the first live status update, supervisor status logging divided existing
  rolling-average sums by `update_count`, producing `NaN`.
- MySQL rejected the generated SQL before the live status could overwrite the
  placeholder row.

Fix/workaround:

- In vpsAdmin, reset node status rolling-average state when
  `update_count <= 0` before logging.
- In devcluster seeds, do not create placeholder status rows with
  `update_count = 0`.
- For an existing affected DB, updating to the fixed supervisor is enough; the
  next node status update repairs the row.

Verification:

- Targeted API spec:
  `bundle exec rspec spec/supervisor/node/status_spec.rb` passed with 5
  examples.
- After switching the devcluster services VM, node `101` updated to kernel
  `6.12.91` and recent `updated_at`, and supervisor logged no new warnings.
