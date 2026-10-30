Replace the existing CLI / curl / HTTP row with these two rows:

| CLI / curl | Preserve shell continuations. Serialize data first, then encode every complete dynamic shell argument with `Shellwords.escape`; this includes URLs, headers, option names and values. |
| HTTP | Preserve the protocol/JSON transcript, especially the header/body separator. Shell quoting rules do not apply. |

Insert after the paragraph ending "Tests may use native formatters.":

For CLI and curl, keep authored shell syntax separate from argument data. Encode
each argument once after its value has been serialized; surrounding raw data
with single or double quotes is insufficient. Check generated commands with
temporary fake executables: require successful execution, exact captured argument
values and order, and no unintended command execution. Parse captured curl JSON
to verify that shell encoding preserves the complete request body.
