Advisory CVE lists order rows by `cve_id`, while `from_id` filters by primary-key
ID. The inherited collector can omit CVEs across pages when those orders differ;
its monotonic-ID fixture does not establish multi-page completeness. Producer
ordering and cursor semantics need a focused alignment fix with a
nonmonotonic-ID regression.
