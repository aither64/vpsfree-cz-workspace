# Activation correction operational note

Source46975718 activation gate is independently reviewed, with the single
Advisory narrowly remedied/directly checked. Actual retained-tab update test
passed in Firefox/Chromium. Unchanged sources and failed evidence remain bound
to their historical exact heads. Fullflake and same-head CI run once; no retry.

Consumer changes use owning tools, one final selection each. Config channel set
ran normal hooks; the first config environment source was mistakenly invoked
from tracking and emitted 'requires ./Gemfile'. It still exported tools and the
owning channel command completed successfully. Final consolidation/amend and
push sourced from configuration CWD, passed Nixfmt/commit hooks with the existing
allowed generated-text width warning. No hooks were bypassed. Future wrappers
always cd to the configuration root before sourcing its generated environment.

Published complete heads are worker-update-final-heads.json. Both locks differ
from their protected bases only in the intended runtime node; no sibling/follows
changes. Old consumed consumer750/c90 refs remain outside final feature ancestry.
No merge/default/ref deletion, session lifecycle or reservation-release action.
