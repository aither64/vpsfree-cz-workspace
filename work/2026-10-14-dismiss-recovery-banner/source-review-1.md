Independent reviewer /root/final_review, gpt-6-astra/xhigh, installed default
review-purpose fallback because roster:null. Reviewed complete base
3b5550fdb8724d886a2515dd535217d98a02f2e2 to 88d9d12b9389d159ac87c5756a564a0016a68808
under general, architecture, scope and risk lanes.

Important (general/architecture/risk): portal-only reset misses canonical CLI
restoration and interruption after terminal restoration but before portal reset.
Resolution: bind notice ID to the already persisted canonical terminal authority
TmuxIdentity alongside session incarnation and native socket epoch. Remove the
portal reset callback and extra random nonce. Add direct-canonical-restoration and
interrupted-wrapper regressions. This changed binding design receives affected
lane review again on the same independent reviewer.

No other Blocking/Important findings. One focused source commit, no obsolete
history, no migrations, no repeated dependency streams. Browser/package checks
and downstream pin supplement remain pending.
