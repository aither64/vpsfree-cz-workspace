Result: **failed** — exit status 1, elapsed 1.01 seconds.

The helper emitted this sanitized failure excerpt:

```json
{"state":"failed","phase":"before","reason":"read_only_continuity_not_confirmed","stage":"own_manifest_socket","check":"assertion","source":"continuity-diagnostic.cjs","line":100}
```

I ran the assigned command once. The requested `diagnostic.log`, `diagnostic.stderr`, and `operation-result.json` were not created at the specified paths; the helper stopped before producing a receipt. No retry or diagnosis was performed.