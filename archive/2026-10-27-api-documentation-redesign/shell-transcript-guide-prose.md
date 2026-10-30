CLI and curl examples can show response output after the executable command.
Keep every physical response line inert when the complete block is pasted into a
shell. Normalize CRLF and bare CR to LF only within display-only response
fragments, then prefix every resulting line with `# `. Do not normalize or
comment the request command, and do not use shell escaping as a substitute for
commenting each physical response line. Regression tests must execute the
complete displayed block with temporary fake executables, preserve the exact
request arguments and curl JSON, and prove that hostile multiline response
values stay visible without being evaluated.
