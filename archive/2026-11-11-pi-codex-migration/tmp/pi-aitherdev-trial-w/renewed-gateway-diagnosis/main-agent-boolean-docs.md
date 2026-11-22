An optional `modelOverrides` object under `providers.openai` sets native
`samplingParams.parallel_tool_calls` to a boolean for exactly one model:

```json
"modelOverrides":{"gpt-6.1-sol":{"samplingParams":{"parallel_tool_calls":false}}}
```

The model key must match an installed catalog model for the OpenAI provider.
Validation accepts `true` or `false` and rejects wildcards, multiple model keys,
other model or sampling fields, and non-boolean values. Set the value required
by the selected endpoint. Omitting the override preserves the native SDK default;
omission is not a substitute for an explicitly required value.

This setting controls the serialized provider request. Tool permissions and local
tool execution policy remain unchanged. Input validation and local transport
checks do not establish remote gateway compatibility.
