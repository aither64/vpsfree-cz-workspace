# Preserve UTF-8 when regenerating YAML content blocks

Related initiative: `work/2026-08-09-kb-kvm-review`

When a Ruby script copied DokuWiki text into a YAML replacement plan with
`File.binread`, Psych emitted the value as `!binary`. The candidate builder
later failed while generating its Markdown review with incompatible UTF-8 and
ASCII-8BIT encodings.

Read textual content explicitly as UTF-8 before serializing it:

```ruby
File.read(path, encoding: Encoding::UTF_8)
```

After regenerating the plan this way, `bin/kb-contract-build` completed and
the built page was byte-identical to the reviewed contract source.
