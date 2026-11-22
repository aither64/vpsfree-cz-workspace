# JSON 3.0 prevents the API test environment from booting

## Symptom

With `packages/api/Gemfile.lock` from vpsAdmin commit `cd3fac386`, loading the
API test environment fails in `ActiveSupport::JSON.decode`:

```text
json-3.0.0/lib/json/common.rb:296:in `parse':
wrong number of arguments (given 2, expected 1)
```

## Cause

ActiveSupport 8.1.3.1 calls `JSON.parse` with a second positional options
argument. JSON 3.0.0 accepts only one positional argument. The vpsAdmin source
itself did not change between deployed commit `1acc1955f` and `cd3fac386`; only
packaged gem locks changed.

## Workaround

For local validation against the deployed dependency set, copy the packaged API
lock to the ignored `api/Gemfile.lock` and keep JSON at 2.21.2. Do not commit the
local lock.

## Verification

The API schema, seeds, and IP repair validation booted and passed with JSON
2.21.2. Related initiative:
`work/2026-09-07-fix-ip-charged-environments`.
