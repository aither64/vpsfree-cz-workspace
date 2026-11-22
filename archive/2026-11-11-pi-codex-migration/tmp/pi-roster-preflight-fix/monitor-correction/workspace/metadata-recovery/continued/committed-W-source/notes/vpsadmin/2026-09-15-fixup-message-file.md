# Fixup commits with message files

`git commit --fixup=<target> -F <message-file>` fails because Git does not allow
these options together. To follow vpsAdmin's message-file rule, write the exact
subject `fixup! <target subject>` and any rationale into a temporary file, then
run `git commit -F <message-file>`. `git rebase -i --autosquash <base>` recognizes
that subject normally. Keep these construction commits local until folded into
the owning feature commit.

Related initiative: `work/2026-09-09-ip-release-mechanism`.
