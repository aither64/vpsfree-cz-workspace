# Keep plan identity separate from the CLI goal digest

Real portal acceptance created a session from a completed plan ending in a
newline, but the portal reported `creation completion goal changed`. The CLI
created the session and completed its initial turn. Its existing `read_goal`
uses Ruby `String#strip`; the portal had hashed the untrimmed derived goal.

Normalize only the derived submitted goal and its digest using the CLI's exact
character set: space, tab, LF, VT, FF, CR and NUL. Preserve captured plan text,
turn ID and digest byte for byte. Go `strings.TrimSpace` is broader than Ruby
`String#strip` and would remove Unicode whitespace that the CLI preserves.

Apply that same normalization when verifying an already-frozen receipt so a
matching created session can recover without resubmission. Keep all receipt,
binding, source, thread, manifest and tracking-identity checks. Validate against
the actual Ruby `read_goal`, including NBSP, U+3000 and internal indentation.
Related initiative: work/2026-09-12-portal-review-experience/.
