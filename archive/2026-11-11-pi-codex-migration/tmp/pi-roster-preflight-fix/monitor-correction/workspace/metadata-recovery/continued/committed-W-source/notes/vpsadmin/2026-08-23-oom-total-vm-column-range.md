# OOM task `total_vm` can exceed a signed 32-bit integer

## Symptom

`vpsadmin-supervisor` raises
`VpsAdmin::Supervisor::Node::OomReports::TaskRangeError`, with an underlying
`ActiveModel::RangeError`, while saving OOM reports.

## Cause

The kernel task table reports `total_vm` in pages. A process with an
approximately 8 TiB virtual address space can exceed 2,147,483,647 pages, but
`oom_report_tasks.total_vm` is a signed four-byte `integer`.

The report parent, usage and statistic rows are inserted before the task rows,
without a common transaction, so the failure can leave a partial report.

## Fix and verification

Migrate `total_vm` to `bigint`, audit the other kernel-sized task fields, and
make report persistence atomic. Verify with a value above 2,147,483,647.

Related initiative: `work/2026-08-23-vpsadmin-supervisor-issue/`.
