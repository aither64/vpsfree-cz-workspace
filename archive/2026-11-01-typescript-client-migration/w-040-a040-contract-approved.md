The advisory CVE API orders rows by `cve_id`, while `from_id` filters by
primary-key ID. The collector can omit CVEs across pages when these orders
differ; its fixture with increasing IDs does not establish multi-page completeness.
Aligning producer ordering and cursor semantics remains a separate follow-up,
with a regression using nonmonotonic IDs.
