# JavaScript library-lock policy support

Source is yielded to owner0 in the shared session-owned
`haveapi-library-lockfiles` root. Four owned paths only; no Git/index mutation,
setup/install, generation, compiler or test command was performed by owner2.
Exact baseline binding, source hashes and static fidelity checks:
[source-receipt.json](source-receipt.json). Actual edit:
[source.diff](source.diff).

The shared RSpec workflow changes only its initial library preparation to
`npm install --no-audit --no-fund`; action references and actual build/spec
commands are unchanged. Both JS README files explain local ignored lock
preparation and the resolution boundary between build and checks. The helper
regression changes only its title/comment: all original assertions, loader/ES5/
TypeScript-helper/declaration checks and obsolete dependency negatives remain
byte-for-byte unchanged. No dependency constraints or application runtime were
changed. Highlighter preparation was outside owner2's paths and is untouched.

Lead completed the main prose pass and accepted both README additions unchanged.
Owner1 was asked for the coordinated declared Node environment. Current own
node_modules is absent, while dist bundle/declarations and the preserved local
lock exist. No independent install or borrowed native/node_modules preparation
is authorized. Known-short Node syntax check is pending that handoff. Lead accepted the static
unchanged-oracle proof and explicitly excluded dependency installation or a
repeat of the unchanged full compatibility suite from this support package.
No full campaign or old exact-resolution guard is proposed.

Original untracking/.gitignore/Makefile/release files belong exclusively to
owner0. The user-authorized later backport/release work keeps its review and
actual candidate gates; this support receipt claims no publication prerequisite
or release success. Owner2 remains responsible for assigned follow-up findings.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
