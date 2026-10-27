# Failed mounted 1ae9 operations

Both operations tested exact reviewed1ae9/tree7287 and failed the same Go
fixture postcondition after Chromium accepted browser assertions passed.
No later cases ran because of failfast. No publication occurred.

- Fresh Luna/low watcher `/root/recovery_input_1ae9_watch` first reported FINAL
  unstarted after ambient `dev-session` was unavailable. A queued follow-up later
  launched original19924. Its final tool result was exit1/no sessionID, Go21.253s,
  subcase21.20s. Complete original output is `mounted-1ae9.full.log`.
- Parent fallback original39101 had already been launched on the unstarted FINAL
  report. It returned exit1/no sessionID, Go21.070s/subcase21.02s. Complete original
  output is `mounted-1ae9.log`. Wrapper UTC start20:30:24Z, finish20:31:01Z.

This was an accidental duplicate operation, promptly reported to lead, not an
authorized rerun or additional evidence campaign. Test log times show watcher
Chromium20:30:03–22Z and parent Chromium20:30:42–31:01Z. Both finished; no command
or watcher remains running. The wrappers used the same `.meta`/`.exit` paths;
the retained `mounted-1ae9.meta` contains mixed original entries, not a clean
single-operation timestamp receipt. No reconstructed original is claimed.

Actual browser assertions passed: temporary error displayed with original receipt
blocked, coordinator cleared it without reload, exact originalID/text/attachment
returned real202, storage/reload checks passed. Go then saw seven literal
`resume` lines and recovery-check count2. The temporary failure helper logged
literalresume and returned75 for every DevSession call, including ordinary
coordination status reads (`coordination.go:77`). Those lines do not prove seven
resume commands. The narrow fixture correction intercepts only actual resume,
records its full argv and delegates other commands to the exact previous helper.
The count assertion remains one exact `resume example --as-is`.

Production and CJS are unchanged by that correction. Original failures and refs
are preserved; further mounted execution requires the corrected-head review
disposition. No rerun occurred before diagnosis.
