# Component lint baseline evidence

API RuboCop 1.93.0: 1588 files, 25 offenses in the files below. Every
working file Git blob equals the exact base blob at 81e930b25fa3252d7e849aff4819e663cec37b07.
No offending path overlaps the two changed paths (`api/lib/vpsadmin/api/resources/incident_report.rb` and `api/spec/api/resources/incident_report_spec.rb`).

| Offending path | Identical base/working blob |
| --- | --- |
| `api/db/migrate/20140927161700_add_storage.rb` | `abf2aaf1ac9df5f9fa052611912b716092cf3343` |
| `api/db/migrate/20141105175157_maintenance_mode.rb` | `e74ef4d5d9a11ed8814d33583220d110e9f77f80` |
| `api/db/migrate/20150717065916_add_integrity_check.rb` | `0e298dcf0f0c8cdd2e655d9ac7e7bca136f4d2d8` |
| `api/lib/vpsadmin/api/operations/base.rb` | `906db986a7f79bed99784075af2a3e1c3f83495c` |
| `api/models/transaction.rb` | `e1e16882d0a663b3525b7768c65ed79e36adab74` |
| `api/models/transaction_chains/dataset/group_snapshot.rb` | `cee3df1bc64d25ac6c1e6ebcbac1325161411fa7` |
| `api/models/transaction_chains/dataset/transfer.rb` | `b6ece749be71a3e060c512d0efcf11b8f8260c76` |
| `api/spec/api/plugins/newslog/news_log_spec.rb` | `914e55f651c864291c6aa69b07a46f63d93fb680` |
| `api/spec/models/tasks/lifetimes_spec.rb` | `a14ff1c9c05884e2a62ce760d43fe4f2bbcb3ab6` |
| `api/spec/models/transaction_chains/user/create_spec.rb` | `81db1c3696a012ed58326161f06e143a10e396db` |

Raw log: `/tmp/exception-root-cause-api-lint.log`. No lint pin/configuration
change, unrelated fix, or hook bypass is included.
