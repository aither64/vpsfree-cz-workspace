# Protect DokuWiki operator literals

Related initiative: `work/2026-06-15-vpsadmin-events`

## Symptom

A DokuWiki table containing an inline-code glob explanation rendered as one
large malformed row. Later rows appeared inside the first glob row, and `<=`
was rendered as a typography arrow.

## Cause

DokuWiki still interprets markup and typography inside ordinary `''inline
code''`. A literal `**` therefore opens bold markup, while operator strings can
be subject to character substitution.

## Fix

Wrap syntax-sensitive literals in no-format spans inside inline code:

```text
''%%**%%''
''%%<=%%''
''%%cgroup =* /user.slice/**/*.scope%%''
```

Use this form consistently for operator tables and expressions instead of
escaping only one character. Plain `%%literal%%` is also safe when inline-code
styling is not needed.

## Verification

Rebuild the KB candidate and manifest, stage it at the real page ID, and
inspect the rendered HTML. A two-column table must remain two columns, every
operator and example must have its own row, and the literal `**` and `<=`
strings must remain unchanged.
