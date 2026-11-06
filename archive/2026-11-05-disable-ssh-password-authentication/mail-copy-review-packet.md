# Final copy-only revision

Reviewed predecessor: 858b18811c9363fe6c2fd875b224a813d8e360d4.
New committed head: 8b90ad54f6c5450a207da89eb1d344582c372e84.
Same full base 2fdc9f2889ac419136cd0cde0e0955c015ae7107 and unchanged SSH
parent2e7c9add2958e614a77e96236e92c55c8b22ad5c. Same two coherent commits;
only two mail templates changed. All intended changes committed, clean tree,
focused rendered nonempty/mixed recipient tests, byte equality and whitespace pass.

Latest user requested removing Czech sentence about updates not removing earlier
compromise and support-reply paragraph; corresponding English removed. User asked
if another account with real password was required: lead checked primary
V_10_6_P1 auth-passwd.c (one-character '*' passes null salt) and
openbsd-compat/xcrypt.c pick_salt (scan account hashes, '$' salt else DES fallback).
Reworded as another account with stored password hash for the described attack.
User correctly identified redundant unless changed_vpses.empty guard; final
recipient filter guarantees nonempty list, so guards removed from both templates.
Long lines rewrapped without word changes, trailing spaces removed.

General/copy and risk/factual lanes only. Original architecture/scope/logic and
full-history review in mail-review.md retained, no new interfaces/source/filters.
Review exact old/new diff and rendered content against user edits; primary source:
https://raw.githubusercontent.com/openssh/openssh-portable/V_10_6_P1/auth-passwd.c
https://raw.githubusercontent.com/openssh/openssh-portable/V_10_6_P1/openbsd-compat/xcrypt.c
https://sshhole.com/

Lead directly applied writing/humanizer skills; exact templates in session remain
source of latest wording. Read mandatory-review skill and affected references;
same retained reviewer0 saved settings/read-only, no nested agents. No live DB or
sends; no new migrations/dependency streams/obsolete history. Complete final
history conclusion from prior review can be updated by proving only this copy diff.
