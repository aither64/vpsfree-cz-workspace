# Static v3 inspector application correction

Prepared only; no runner/import/guard/Nix/help/query/test/build/network operation
ran. Only this new directory was written. v2 and its actual failed result,
all earlier packets, the original37 inputs, source expressions and accepted
binding proposal remain frozen. The required current/session/environment and
saved roster32 Sol/xhigh/workspace_write checks matched. No tool, peer, Git or
application source scan was performed.

## Actual diagnosis and selected command

v2's saved01-evaluate receipt records actual exit1 and empty stdout. Its error is
`cannot convert a function to JSON` at unchanged inspect-selection.nix:2,
the top-level `{ bindingFile }:` function. This establishes that the evaluated
value remained a function. It does not establish a derivation-availability,
source-fetch or inspector-policy failure, and no output path was produced.
The finalization receipt records both file guards0, current0 and all three
recorded groups confirmed empty; these remain actual v2 facts only.

The selected Nix2.34.9 eval manual is bound at:

`/nix/store/addg4icdw1xadiwh6bk4lql8bxbvf11i-nix-manual-2.34.9/share/doc/nix/manual/command-ref/new-cli/nix3-eval.html`

SHA256 `0875f6132161ad7cad377041447c22f38b391b6f35206644710b75c7a8821a66`.
It says JSON cannot represent functions, demonstrates `--apply builtins.attrNames`
on an evaluated installable at line239, and documents at line282:
“Apply the function expr to each argument.” Line471 says `--file` interprets the
expression in the named file and “Implies --impure.”

Use the documented --apply form with the existing --file to preserve that
original source-access boundary. The one changed stage argv is:

```text
<same parent-bound nix entry> eval --json
--file <same original inspect-selection.nix>
--apply 'inspector: inspector { bindingFile = "<exact v3 active binding path>"; }'
<same original options>
```

The quotes above describe one expression argument, not shell interpolation.
ready.json contains its exact literal argv and UTF-8 expression hash. The runner
constructs the binding path from its own fixed v3 directory and passes the lambda
as one argv element. The lambda receives the existing inspector value and calls
it with the explicit bindingFile attribute. The old --argstr segment is removed.
No --expr, added --impure, legacy invocation, read/write flag, IFD allowance,
source override, option change or automatic retrieval route is introduced.
The new application has not been parsed or executed by Nix.

## Narrow unchanged proofs and retained inputs

evaluate-v2-to-v3.diff contains only that stage01 application and the projected
v3 attempt name. Reversing those exact edits reproduces the entire v2 source
byte-for-byte. Every function, all options and all other stage calls compare
AST-exact to v2. Its process settlement/failure finalization, root raw-file/
nonrecursive identity/store-validity gates and original inspector remain exact.
The unchanged modern offline settings keep their documented cache/source limits;
no new permission is inferred from the previous release.

retained-inputs.json binds v2's exact evaluator/packet, accepted current-input
assessment3e29b5d3, release6a2db312, exact80dd48cf active binding and attempt copy,
actual eval stdout/error/argv/exit, both current records and finalization/outcome.
The immutable proposal80dd48cf/acceptance64f40871 bindings are retained. Receipt
hashes are observations of the named frozen evidence, not refreshed expectations
for outputs. No evaluated graph/compiler/vendor/VM/native facts transfer from
the failed invocation. No browser metadata/path identity is imported.

## Held future execution

After independent parent inspection and a separate new release, the command is:

```sh
/home/aither/.nix-profile/bin/python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/naming-runtime-evaluation-availability-successor-v3/evaluate.py --execute-parent-released-evaluation
```

Cwd is this v3 directory. Active final-bindings.json, parent-release.json and
attempt-evaluation-availability-v3-01 remain absent. Parent alone binds current
tools/environment, copies an accepted binding, writes the v3 release and owns
one fresh utility invocation. This preparation authorizes no rerun or continuation.
Existing command/cap/settlement/outer bounds remain in ready.json unchanged.

Checks performed are Python AST/JSON decoding, local receipt/manual hashes and
narrow unchanged-source proofs only. No prepared script was imported or executed.
No actual output stage ran in v2; derived outputs remain unknown. All build,
managed/native, real-account/provider/VM/browser/system/deployment gates remain
separate and held. No claim, lifecycle or cleanup action was performed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
