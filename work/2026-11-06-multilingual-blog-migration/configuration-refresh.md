# Configuration feature refresh

```json
{
  "old_base": "85b38f1cd07d6b3a0fde3eefd32258f747e757e5",
  "old_head": "133a94b62b3c2161c126fa347cab61ae1b819001",
  "new_base": "5941cdb3dda259e91c6a988a7dbf08c84700b326",
  "new_dns_head": "b4a7f22a46c16be453052a37ac98fc4c39401a9f",
  "preserved_ref": "refs/heads/2026-11-06-multilingual-blog-migration-dns-reviewed",
  "record_patch_sha256": "3e9f8bcb7bdea2fecf482f7a7ab3ff42835e9201d0e93b7d283944ba42f07ecc",
  "record_payloads_identical": true,
  "old_predecessor_soa": 2026093000,
  "new_predecessor_soa": 2026110200,
  "feature_soa": 2026110600,
  "literal_patch_equivalence": false,
  "conclusion": "Same exact blog A record and inherited TTL; public CNAME boundary unchanged. Only removed predecessor SOA serial differs after upstream refresh. Old DNS build is not E0 verification."
}
```

No activation, default-branch integration or review reuse is claimed.
